#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Sincroniza el tracker "### 📸 Imágenes (N/7 — Estado)" y su tabla de poses
en las galerías de Anaïs y Miss Doll contra la realidad de `git ls-files`.

Por qué existe
--------------
`update_galleries.py` NO toca este tracker: es manual, y por eso envejece hacia
la mentira (13/08/2026: decía 0/7 en 13 de 14 looks con 52 imágenes en el índice;
17/08/2026: decía 0/7 en L15-L25 con 60 imágenes reales). Contar el disco tampoco
sirve — los PNG llevan skip-worktree. La fuente de verdad es el índice de git.

Lo que preserva
---------------
- Anotaciones humanas dentro de una celda (p.ej. "⚠️ outfit incorrecto"): si la
  celda ya apunta al archivo real, se deja intacta byte a byte.
- Encabezados con nota propia (p.ej. "7/7 en disco · **6/7 útil** — ver ..."):
  no se reescriben; se reportan para revisión manual.

Uso:
    python 99_Sistema/scripts/visual/sync_tracker_galeria_personaje.py            # anais + miss_doll
    python 99_Sistema/scripts/visual/sync_tracker_galeria_personaje.py anais
    python 99_Sistema/scripts/visual/sync_tracker_galeria_personaje.py --dry-run
"""

import os
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

# Slot 5 es lo único que cambia por personaje (taxonomía universal de 7 poses,
# contenido propio de cada muñeca). Dueño único: 02_Personajes/_perfiles_visuales/<slug>.md §4
PERSONAJES = {
    "anais": {
        "galeria": "02_Personajes/01_Principales/anais/galeria_looks_anais.md",
        "imagenes": "05_Imagenes/anais",
        "slot5": "sovereign_gaze",
    },
    "miss_doll": {
        "galeria": "02_Personajes/01_Principales/miss_doll/GALERIA_OUTFITS_MISS_DOLL.md",
        "imagenes": "05_Imagenes/miss_doll",
        "slot5": "glacial_command",
    },
}

EXT = (".png", ".jpg", ".jpeg", ".webp")

# Alias tolerados por pose (mismo criterio que update_galleries.py)
ALIAS = {
    "standing": ("standing", "frontal"),
    "back_view": ("back_view", "backview", "back", "espalda"),
    "seated": ("seated", "sitting", "sentada"),
    "side_profile": ("side_profile", "sideprofile", "profile", "side", "perfil"),
    "sovereign_gaze": ("sovereign_gaze", "sovereign", "gaze", "domina_closeup"),
    "glacial_command": ("glacial_command", "glacial", "command"),
    "pov": ("pov",),
    "odalisque": ("odalisque", "lying", "chaise"),
}

RE_LOOK = re.compile(r"^##\s+\S+\s+Look\s+(\d+):", re.M)
RE_UBIC = re.compile(r"^-\s+\*\*Ubicacion:\*\*\s+`([^`]+)`", re.M)
RE_TRACKER = re.compile(r"^###\s+📸\s+Imágenes\s+\((.*?)\)\s*$", re.M)
RE_TRACKER_SIMPLE = re.compile(r"^\d+/7\s+—\s+\S+$")
RE_CELL_LINK = re.compile(r"\]\(([^)]+)\)")


def git_ls(path):
    out = subprocess.run(
        ["git", "-C", REPO, "ls-files", path],
        capture_output=True, text=True, encoding="utf-8", check=True,
    ).stdout
    return [l.strip() for l in out.splitlines() if l.strip().lower().endswith(EXT)]


def pose_de(nombre, poses):
    """Resuelve el nombre de archivo a una pose canónica. Alias más largo primero
    para que 'back_view' gane sobre 'back' y 'side_profile' sobre 'side'."""
    base = os.path.splitext(os.path.basename(nombre))[0].lower()
    # quitar el prefijo <personaje>_<numero>_
    base = re.sub(r"^(?:ele|helena|miss_doll|anais)_(?:look|l)?\d+_", "", base)
    candidatos = []
    for pose in poses:
        for a in ALIAS[pose]:
            if base == a or base.startswith(a + "_") or base.endswith("_" + a) or base == a:
                candidatos.append((len(a), pose))
    if not candidatos:
        return None
    return max(candidatos)[1]


def procesar(slug, cfg, dry_run):
    ruta = os.path.join(REPO, cfg["galeria"])
    with open(ruta, encoding="utf-8") as f:
        texto = f.read()

    poses = ["standing", "back_view", "seated", "side_profile", cfg["slot5"], "pov", "odalisque"]
    lineas = texto.split("\n")

    # Índice de secciones de look: (linea_inicio, numero)
    marcas = []
    for i, l in enumerate(lineas):
        m = re.match(r"^##\s+\S+\s+Look\s+(\d+):", l)
        if m:
            marcas.append((i, int(m.group(1))))
    marcas.append((len(lineas), None))

    cambios, avisos, huerfanos = [], [], []

    for idx in range(len(marcas) - 1):
        ini, num = marcas[idx]
        fin = marcas[idx + 1][0]
        bloque = lineas[ini:fin]

        # carpeta de imágenes declarada en el look
        carpeta = None
        for l in bloque:
            m = RE_UBIC.match(l)
            if m:
                carpeta = m.group(1).rstrip("/")
                break
        if not carpeta:
            continue

        reales = git_ls(carpeta)
        mapa = {}
        for r in reales:
            p = pose_de(r, poses)
            if p and p not in mapa:
                mapa[p] = r
            elif not p:
                huerfanos.append(r)

        # localizar tracker + tabla dentro del bloque
        t_i = h_i = None
        for j, l in enumerate(bloque):
            if RE_TRACKER.match(l):
                t_i = j
            if l.startswith("| Standing |") and t_i is not None:
                h_i = j
                break
        if t_i is None or h_i is None or h_i + 2 >= len(bloque):
            continue

        fila_i = h_i + 2
        celdas = [c.strip() for c in bloque[fila_i].strip().strip("|").split("|")]
        if len(celdas) != 7:
            avisos.append(f"L{num:02d}: fila de {len(celdas)} celdas (se esperan 7) — sin tocar")
            continue

        nuevas, toco = [], False
        for k, pose in enumerate(poses):
            actual = celdas[k]
            archivo = mapa.get(pose)
            link_actual = RE_CELL_LINK.search(actual)
            destino_actual = link_actual.group(1).split("/")[-1] if link_actual else None

            if archivo:
                if destino_actual == os.path.basename(archivo):
                    nuevas.append(actual)          # intacta: preserva anotaciones humanas
                    continue
                nuevas.append(f"[📸 View](../../../{archivo})")
                toco = True
            else:
                if link_actual:
                    nuevas.append("⏳ Pendiente")   # el archivo desapareció del índice
                    toco = True
                else:
                    nuevas.append(actual)

        n = sum(1 for p in poses if p in mapa)
        cab = RE_TRACKER.match(bloque[t_i]).group(1)
        estado = "Completo" if n == 7 else ("Pendiente" if n == 0 else "Parcial")
        nueva_cab = f"### 📸 Imágenes ({n}/7 — {estado})"

        if not RE_TRACKER_SIMPLE.match(cab):
            if not cab.startswith(f"{n}/7"):
                avisos.append(f"L{num:02d}: encabezado con nota propia («{cab}») y el conteo real es {n}/7 — revisar a mano")
        elif bloque[t_i] != nueva_cab:
            viejo = cab.split("/")[0]
            cambios.append(f"L{num:02d}: {viejo}/7 → {n}/7")
            bloque[t_i] = nueva_cab
            toco = True

        if toco:
            bloque[fila_i] = "| " + " | ".join(nuevas) + " |"
            if not any(c.startswith(f"L{num:02d}:") for c in cambios):
                cambios.append(f"L{num:02d}: celdas re-enlazadas ({n}/7)")
            lineas[ini:fin] = bloque

    nuevo = "\n".join(lineas)
    print(f"\n== {slug} ==")
    if cambios:
        for c in cambios:
            print(f"   ⬆️  {c}")
    else:
        print("   ✅ tracker ya sincronizado")
    for a in avisos:
        print(f"   ⚠️  {a}")
    for h in sorted(set(huerfanos)):
        print(f"   ❓ archivo sin pose reconocible: {h}")

    if nuevo != texto and not dry_run:
        with open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(nuevo)
        print(f"   💾 escrito: {cfg['galeria']}")
    elif nuevo != texto:
        print("   (dry-run: no se escribió)")

    return len(cambios)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry-run" in sys.argv
    objetivos = args or list(PERSONAJES)
    total = 0
    for slug in objetivos:
        if slug not in PERSONAJES:
            print(f"❌ personaje desconocido: {slug}")
            return 1
        total += procesar(slug, PERSONAJES[slug], dry)
    print(f"\n── {total} look(s) corregidos ──")
    return 0


if __name__ == "__main__":
    sys.exit(main())
