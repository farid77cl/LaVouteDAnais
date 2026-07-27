#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar_app_index.py
====================
Genera `99_Sistema/app_index.json` — el índice que consume LV-App 2.0.

POR QUÉ EXISTE (decisión de la Ama, 27/07/2026):
    La app NO clona el repo. Un `git clone --depth 1` de LaVouteDAnais son
    ~1,56 GB y 5.242 PNG en el teléfono antes de pintar la primera foto.
    En vez de eso la app baja ESTE índice (cientos de KB) y carga cada
    imagen por URL raw bajo demanda, con caché de Coil.

FUENTE DE VERDAD:
    `git ls-files` — NO el disco. Así corre igual en la máquina literaria
    (que tiene 0 PNG en disco) que en la visual. Lo que no está commiteado
    no existe para la app, que es exactamente el criterio correcto: la app
    lee del repo remoto.

POSES CANÓNICAS:
    standing · back_view · seated · side_profile · ditzy · pov · odalisque
    Se normalizan alias y formatos viejos (`pose5_ditzy`, `_2`, `back`,
    `profile`) con la misma lógica que el PoseMatcher de la app.

PORTADA JERÁRQUICA:
    Standing > Side Profile > Seated > primera disponible.

Uso:
    python 99_Sistema/scripts/visual/generar_app_index.py
    python 99_Sistema/scripts/visual/generar_app_index.py --dry-run
    python 99_Sistema/scripts/visual/generar_app_index.py --pretty   # legible, pesa más
"""

import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parents[3]
SALIDA = REPO_ROOT / "99_Sistema" / "app_index.json"
GALERIA = REPO_ROOT / "00_Ele" / "galeria_outfits.md"

RAW_BASE = "https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/"

# Orden canónico. El índice es también la prioridad de portada para las 3 primeras.
POSES_CANON = [
    "standing",
    "side_profile",
    "seated",
    "back_view",
    "ditzy",
    "pov",
    "odalisque",
]
PRIORIDAD_PORTADA = ["standing", "side_profile", "seated"]

# Alias → canónica. Cubre lo que sube la app (back/profile), el español y
# los nombres viejos de la flota histórica.
ALIAS = {
    "back": "back_view",
    "backview": "back_view",
    "espalda": "back_view",
    "profile": "side_profile",
    "sideprofile": "side_profile",
    "perfil": "side_profile",
    "sentada": "seated",
    "frontal": "standing",
    "depie": "standing",
    "acostada": "odalisque",
    "odalisca": "odalisque",
}

# `05_Imagenes/ele/look675_slug/ele_675_standing.png`
RE_RUTA_ELE = re.compile(r"^05_Imagenes/ele/look(\d+)_([^/]+)/(.+\.png)$", re.IGNORECASE)
# `## Look 221: Título (21/05/2026 — batch 221-230 · Pin-Up ...)`
# Muchos headings llevan emoji delante (`## 👰 Look 200: ...`), así que se
# admite cualquier cosa entre `##` y `Look`.
# La fecha y el paréntesis de metadata NO siempre están: el título se captura
# igual y la fecha queda en None cuando falta.
RE_HEADING = re.compile(r"^#{2,3}\s*\S*\s*Look (\d+):\s*(.+?)\s*$")
RE_FECHA = re.compile(r"\((\d{2}/\d{2}/\d{4})")


def archivos_trackeados():
    """Lista de PNG de Ele según git. Falla ruidosamente si git no responde."""
    out = subprocess.run(
        ["git", "-C", str(REPO_ROOT), "ls-files", "05_Imagenes/ele/"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if out.returncode != 0:
        raise SystemExit(f"git ls-files falló:\n{out.stderr}")
    return [l for l in out.stdout.splitlines() if l.lower().endswith(".png")]


def pose_canonica(nombre_archivo, numero_look):
    """`ele_675_back.png` → `back_view`. Devuelve None si no reconoce la pose."""
    tallo = Path(nombre_archivo).stem.lower()
    # Prefijo del personaje + número: `ele_675_`, y también `helena_001_`
    # (la era pre-V3.5 archivada; sus archivos siguen en el repo).
    tallo = re.sub(rf"^[a-z]+[_-]0*{numero_look}[_-]", "", tallo)
    tallo = re.sub(r"^pose\d+[_-]", "", tallo)                   # legado pose5_ditzy
    tallo = re.sub(r"[_-](\d+|v\d+)$", "", tallo)                # sufijos _2 / _v1
    tallo = tallo.strip("_-")

    if tallo in POSES_CANON:
        return tallo
    plano = tallo.replace("_", "").replace("-", "")
    if plano in ALIAS:
        return ALIAS[plano]
    if tallo in ALIAS:
        return ALIAS[tallo]
    # Último recurso: la pose aparece embebida (`ele_159_pose5_ditzy_final`)
    for canon in POSES_CANON:
        if canon.replace("_", "") in plano:
            return canon
    return None


def titulos_de_galeria():
    """{numero_look: (titulo, fecha)} leído de galeria_outfits.md (19 MB, streaming)."""
    titulos = {}
    if not GALERIA.exists():
        return titulos
    with GALERIA.open(encoding="utf-8") as f:
        for linea in f:
            # Filtro barato antes del regex, pero SIN exigir `## Look` literal:
            # muchos headings llevan emoji en medio (`## 👰 Look 200:`).
            if not (linea.startswith("#") and "Look" in linea):
                continue
            m = RE_HEADING.match(linea)
            if not m:
                continue
            crudo = m.group(2)
            fecha_m = RE_FECHA.search(crudo)
            # El título es lo que va antes del paréntesis de metadata.
            titulo = crudo.split("(")[0].strip(" —-·") if "(" in crudo else crudo.strip()
            titulos[int(m.group(1))] = (titulo, fecha_m.group(1) if fecha_m else None)
    return titulos


def construir():
    titulos = titulos_de_galeria()

    por_look = defaultdict(lambda: {"carpeta": None, "poses": {}, "extras": 0})
    sin_reconocer = []

    for ruta in archivos_trackeados():
        m = RE_RUTA_ELE.match(ruta)
        if not m:
            continue
        numero = int(m.group(1))
        entrada = por_look[numero]
        entrada["carpeta"] = f"05_Imagenes/ele/look{m.group(1)}_{m.group(2)}/"

        pose = pose_canonica(m.group(3), numero)
        if pose is None:
            entrada["extras"] += 1
            sin_reconocer.append(ruta)
            continue
        # Si hay dos archivos para la misma pose, gana el primero (alfabético):
        # los `_2` son reintentos, no la toma buena.
        entrada["poses"].setdefault(pose, Path(ruta).name)

    looks = []
    for numero in sorted(por_look):
        entrada = por_look[numero]
        poses = entrada["poses"]
        if not poses:
            continue

        portada = next((p for p in PRIORIDAD_PORTADA if p in poses), None)
        if portada is None:
            portada = next(p for p in POSES_CANON if p in poses)

        titulo, fecha = titulos.get(numero, (None, None))
        looks.append(
            {
                "n": numero,
                "t": titulo,
                "f": fecha,
                "d": entrada["carpeta"],
                # {pose: nombre_archivo} — la app arma la URL con raw + d + archivo
                "p": {k: poses[k] for k in POSES_CANON if k in poses},
                "c": portada,
                "np": len(poses),
                "x": entrada["extras"],
            }
        )

    return {
        "v": 1,
        "generado": date.today().isoformat(),
        "raw": RAW_BASE,
        "poses": POSES_CANON,
        "total_looks": len(looks),
        "total_imagenes": sum(l["np"] for l in looks),
        "looks": looks,
    }, sin_reconocer


def main():
    ap = argparse.ArgumentParser(description="Genera el índice que consume LV-App 2.0.")
    ap.add_argument("--dry-run", action="store_true", help="no escribe, solo reporta")
    ap.add_argument("--pretty", action="store_true", help="JSON indentado (pesa más)")
    args = ap.parse_args()

    indice, sin_reconocer = construir()

    if args.pretty:
        texto = json.dumps(indice, ensure_ascii=False, indent=2)
    else:
        texto = json.dumps(indice, ensure_ascii=False, separators=(",", ":"))

    kb = len(texto.encode("utf-8")) / 1024
    completos = sum(1 for l in indice["looks"] if l["np"] == 7)

    print(f"Looks:            {indice['total_looks']}")
    print(f"Imágenes:         {indice['total_imagenes']}")
    print(f"Completos (7/7):  {completos}")
    print(f"Con título:       {sum(1 for l in indice['looks'] if l['t'])}")
    print(f"Sin reconocer:    {len(sin_reconocer)} archivo(s)")
    print(f"Tamaño índice:    {kb:.1f} KB")

    if sin_reconocer:
        print("\nMuestra de archivos cuya pose no se reconoció:")
        for r in sin_reconocer[:10]:
            print(f"  {r}")

    if args.dry_run:
        print("\n--dry-run: no se escribió nada.")
        return

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(texto, encoding="utf-8", newline="\n")
    print(f"\nEscrito: {SALIDA.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
