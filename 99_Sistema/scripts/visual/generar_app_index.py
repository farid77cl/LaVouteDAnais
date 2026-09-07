#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar_app_index.py
====================
Genera `app/index.json` — el índice que consume LV-App-3.

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

TRES MUÑECAS:
    Ele, Miss Doll y Anaïs comparten este índice. Lo que cambia entre ellas
    (prefijo de archivo, carpeta, slug del slot5) vive en
    `nombres_canonicos.py` + `anclas_universales.json`, no aquí. El parseo de galería vive en
    `galeria_parser.py`. Este módulo solo junta las dos piezas por personaje
    y escribe el JSON — no reimplementa ninguna de las dos.

POSES CANÓNICAS (orden fijo, es también la prioridad de portada):
    standing · back_view · seated · side_profile · slot5 · pov · odalisque
    La quinta pose se llama distinto por personaje (Ditzy / Glacial Command /
    Sovereign Gaze); en el índice viaja siempre como `slot5` — el nombre
    bonito vive una sola vez, en la cabecera de `personajes`.

CADA LOOK DECLARA LAS 7 POSES, TENGA O NO IMAGEN:
    La app sube con el nombre que el índice le dicta y deja de inventarlo:
    `img[pose] = {"a": nombre_archivo, "hay": bool}`.

Uso:
    python 99_Sistema/scripts/visual/generar_app_index.py
    python 99_Sistema/scripts/visual/generar_app_index.py --dry-run
    python 99_Sistema/scripts/visual/generar_app_index.py --pretty   # legible, pesa más
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

sys.path.insert(0, str(Path(__file__).parent))

import galeria_parser  # noqa: E402
import nombres_canonicos  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[3]
SALIDA_INDICE = REPO_ROOT / "app" / "index.json"
SALIDA_PROMPTS = REPO_ROOT / "app" / "prompts"

POSES_CANON = galeria_parser.POSES_CANON

# Sin paréntesis de apertura: `_fecha_de` recibe el grupo 3 de `LOOK_HEADING`,
# que es lo que va DENTRO de los paréntesis del encabezado — ya vienen
# consumidos. Exigir un `(` literal aquí dejaba `"f": null` en 795 de 798
# looks, y los 3 que sobrevivían eran encabezados con paréntesis anidados.
RE_FECHA = re.compile(r"(\d{2}/\d{2}/\d{4})")

# Alias históricos → canónica. Cubre lo que sube la app (back/profile), el
# español y los nombres viejos de la flota pre-convención (`helena_...`).
# Sólo entra en juego en el camino histórico de `pose_canonica`, cuando el
# archivo no calza con lo que `nombres_canonicos.py` generaría hoy.
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


def pose_canonica(nombre_archivo, numero_look, cfg):
    """`ele_800_standing.png` → `standing`. `miss_doll_10_glacial_command.png` → `slot5`.

    Devuelve None si no reconoce la pose.

    Camino canónico primero: compara el archivo contra lo que
    `nombres_canonicos.nombre_archivo()` generaría para cada pose — reusa al
    dueño único de la convención de numeración en vez de re-derivarla aquí
    (Anaïs numera `L{n:02d}`, y un regex propio sobre el número la deja sin
    resolver: la misma trampa de dueño único que `color_canon.py`).

    Camino histórico después, sólo si el canónico no calzó: prefijo viejo
    (`helena_001_`), sufijos de reintento (`_2`/`_v1`), legado `pose5_ditzy`
    y alias en español/inglés (`back`, `profile`...) de antes de que
    existiera esta convención.
    """
    for pose in POSES_CANON:
        if nombre_archivo == nombres_canonicos.nombre_archivo(numero_look, pose, cfg):
            return pose

    slot5_slug = cfg.get("slot5_slug")

    tallo = Path(nombre_archivo).stem.lower()
    # Prefijo del personaje + número: `ele_800_`, `miss_doll_10_`, `helena_001_`.
    tallo = re.sub(rf"^[a-z_]+[_-]0*{numero_look}[_-]", "", tallo)
    tallo = re.sub(r"^pose\d+[_-]", "", tallo)                   # legado pose5_ditzy
    tallo = re.sub(r"[_-](\d+|v\d+)$", "", tallo)                # sufijos _2 / _v1
    tallo = tallo.strip("_-")

    if tallo == slot5_slug:
        return "slot5"
    if tallo in POSES_CANON:
        return tallo
    plano = tallo.replace("_", "").replace("-", "")
    if plano in ALIAS:
        return ALIAS[plano]
    if tallo in ALIAS:
        return ALIAS[tallo]
    # Último recurso: la pose aparece embebida (`ele_159_pose5_ditzy_final`).
    if slot5_slug and slot5_slug.replace("_", "") in plano:
        return "slot5"
    for canon in POSES_CANON:
        if canon.replace("_", "") in plano:
            return canon
    return None


def _slug_titulo(t):
    if not t:
        return ""
    return re.sub(r"[^a-z0-9]+", "_", galeria_parser.sin_tildes(t).lower()).strip("_")


def _fecha_de(meta):
    if not meta:
        return None
    m = RE_FECHA.search(meta)
    return m.group(1) if m else None


def imagenes_trackeadas(slug, cfg):
    """{numero_look: {pose_canonica: nombre_archivo}} desde git ls-files."""
    out = subprocess.run(
        ["git", "-C", str(REPO_ROOT), "ls-files", cfg["carpeta_imagenes"] + "/"],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    if out.returncode != 0:
        raise SystemExit(f"git ls-files falló para {slug}:\n{out.stderr}")

    patron = re.compile(
        rf"^{re.escape(cfg['carpeta_imagenes'])}/{cfg['prefijo_carpeta_look']}(\d+)_[^/]+/(.+\.png)$",
        re.IGNORECASE,
    )
    por_look = defaultdict(dict)
    for ruta in out.stdout.splitlines():
        if not ruta.lower().endswith(".png"):
            continue
        m = patron.match(ruta)
        if not m:
            continue
        numero = int(m.group(1))
        pose = pose_canonica(m.group(2), numero, cfg)
        if pose:
            # Dos archivos para la misma pose: gana el primero alfabético.
            # Los `_2` son reintentos, no la toma buena.
            por_look[numero].setdefault(pose, Path(ruta).name)
    return dict(por_look)


def construir_indice(cfg_personajes, imagenes_por_personaje, galerias):
    """El JSON completo del índice. No toca disco ni git a propósito:
    recibe todo por parámetro, así que se puede probar con fixtures sin
    montar un repo falso.
    """
    looks = []
    cabecera_personajes = {}

    for slug, cfg in cfg_personajes.items():
        cabecera_personajes[slug] = {
            "nombre": cfg["nombre"],
            "slot5": cfg["slot5_nombre"],
            "carpeta": cfg["carpeta_imagenes"],
        }
        imagenes = imagenes_por_personaje.get(slug, {})
        for parsed in galeria_parser.parse_como_la_app(galerias[slug], cfg["slot5_nombre"]):
            numero = parsed["num"]
            presentes = imagenes.get(numero, {})
            img = {}
            for pose in POSES_CANON:
                nombre = presentes.get(pose) or nombres_canonicos.nombre_archivo(numero, pose, cfg)
                img[pose] = {"a": nombre, "hay": pose in presentes}

            carpeta = parsed["ubicacion"] or nombres_canonicos.carpeta_look(
                numero, _slug_titulo(parsed["titulo"]), cfg)
            portada = next((p for p in ("standing", "side_profile", "seated") if img[p]["hay"]), None)
            if portada is None:
                portada = next((p for p in POSES_CANON if img[p]["hay"]), "standing")

            looks.append({
                "p": slug,
                "n": numero,
                "t": parsed["titulo"] or None,
                "f": _fecha_de(parsed["meta"]),
                "d": carpeta if carpeta.endswith("/") else carpeta + "/",
                "img": img,
                "c": portada,
                "np": sum(1 for p in POSES_CANON if img[p]["hay"]),
            })

    looks.sort(key=lambda l: (l["p"], l["n"]))
    return {
        "v": 2,
        "generado": date.today().isoformat(),
        "poses": POSES_CANON,
        "personajes": cabecera_personajes,
        "looks": looks,
    }


def construir_prompts(cfg_personajes, galerias):
    """{"<slug>/<n>": {v, p, n, neg, prompts:{pose: texto}}}

    Un prompt promedia 5,8 KB: todos en un índice serían ~30 MB. En vez de eso,
    el índice navega y cada look descarga su archivo de prompts bajo demanda.
    """
    salida = {}
    for slug, cfg in cfg_personajes.items():
        slot5 = cfg["slot5_nombre"]
        for parsed in galeria_parser.parse_como_la_app(galerias[slug], slot5):
            prompts = {}
            for display, textos in parsed["prompts"].items():
                pose = galeria_parser.slug_de_pose(display, slot5)
                if pose and textos:
                    # Si el mismo slot aparece dos veces, gana el primero:
                    # el segundo es un remiendo pegado abajo.
                    prompts.setdefault(pose, textos[0])
            salida[f"{slug}/{parsed['num']}"] = {
                "v": 2,
                "p": slug,
                "n": parsed["num"],
                "neg": parsed["negative"],
                "prompts": {p: prompts[p] for p in POSES_CANON if p in prompts},
            }
    return salida


def _cargar():
    cfg = json.loads(
        (Path(__file__).parent / "anclas_universales.json").read_text(encoding="utf-8")
    )["personajes"]
    galerias = {
        slug: (REPO_ROOT / c["galeria"]).read_text(encoding="utf-8")
        for slug, c in cfg.items()
    }
    imagenes = {slug: imagenes_trackeadas(slug, c) for slug, c in cfg.items()}
    return cfg, galerias, imagenes


def main():
    ap = argparse.ArgumentParser(description="Genera el índice que consume LV-App-3.")
    ap.add_argument("--dry-run", action="store_true", help="no escribe, solo reporta")
    ap.add_argument("--pretty", action="store_true", help="JSON indentado (pesa más)")
    args = ap.parse_args()

    cfg, galerias, imagenes = _cargar()
    indice = construir_indice(cfg, imagenes, galerias)
    prompts = construir_prompts(cfg, galerias)

    if args.pretty:
        texto = json.dumps(indice, ensure_ascii=False, indent=2)
    else:
        texto = json.dumps(indice, ensure_ascii=False, separators=(",", ":"))

    kb = len(texto.encode("utf-8")) / 1024
    completos = sum(1 for l in indice["looks"] if l["np"] == len(POSES_CANON))

    print(f"Muñecas:          {len(indice['personajes'])}")
    print(f"Looks:            {len(indice['looks'])}")
    print(f"Imágenes:         {sum(l['np'] for l in indice['looks'])}")
    print(f"Completos (7/7):  {completos}")
    print(f"Con título:       {sum(1 for l in indice['looks'] if l['t'])}")
    print(f"Tamaño índice:    {kb:.1f} KB")
    print(f"Archivos prompts: {len(prompts)}")

    if args.dry_run:
        print("\n--dry-run: no se escribió nada.")
        return

    if kb > 2048:
        raise SystemExit(
            f"El índice pesa {kb:.1f} KB, sobre el techo de 2 MB del spec §2.1.\n"
            "Partirlo por personaje antes de que la app lo consuma."
        )

    SALIDA_INDICE.parent.mkdir(parents=True, exist_ok=True)
    SALIDA_INDICE.write_text(texto, encoding="utf-8", newline="\n")
    print(f"\nEscrito: {SALIDA_INDICE.relative_to(REPO_ROOT)}")

    for llave, contenido in prompts.items():
        destino = SALIDA_PROMPTS / f"{llave}.json"
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(
            json.dumps(contenido, ensure_ascii=False, separators=(",", ":")),
            encoding="utf-8", newline="\n",
        )
    print(f"Escrito: {SALIDA_PROMPTS.relative_to(REPO_ROOT)}/ ({len(prompts)} archivos)")


if __name__ == "__main__":
    main()
