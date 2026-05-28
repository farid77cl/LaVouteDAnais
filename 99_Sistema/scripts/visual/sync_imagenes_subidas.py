#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sync_imagenes_subidas.py — Flujo de sincronización de imágenes subidas por la app Android (Gemini → GitHub).

La app móvil sube imágenes generadas en Gemini directamente al repo. Este script:
  1. NORMALIZA los nombres no-canónicos que usa la app SOLO en la era app (looks >= MIN_LOOK):
        ele_<N>_back.png    -> ele_<N>_back_view.png
        ele_<N>_profile.png -> ele_<N>_side_profile.png
     (el resto de poses ya coinciden: standing, seated, ditzy, pov, odalisque).
  2. ACTUALIZA el tracker en 00_Ele/galeria_outfits.md: regenera la sección "### 📸 Imágenes" SOLO de
     los looks >= MIN_LOOK cuya sección esté en "Pendiente cuota API" o "Materializado parcial (app/Gemini)".
     Las pasa a "N/7" con la tabla de View links según las imágenes presentes (⏳ Pendiente las que faltan).
  3. Es IDEMPOTENTE y ACOTADO: NO toca el fleet histórico (<MIN_LOOK), que usa nombres timestamped/curados
     a mano. Correr de nuevo tras subir más poses actualiza solo el conteo de la era app.

Después de correr esto, ejecutar update_galleries.py para regenerar los README de cada carpeta + galería maestra.

Uso:  python 99_Sistema/scripts/visual/sync_imagenes_subidas.py [MIN_LOOK]
      (MIN_LOOK por defecto = 291, primer batch generado por la app)
"""
import os, re, subprocess, sys

sys.stdout.reconfigure(encoding="utf-8")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", ".."))
ELE = os.path.join(REPO, "05_Imagenes", "ele")
GALERIA = os.path.join(REPO, "00_Ele", "galeria_outfits.md")

MIN_LOOK = int(sys.argv[1]) if len(sys.argv) > 1 else 291

POSES = [
    ("standing",     "Standing"),
    ("back_view",    "Back View"),
    ("seated",       "Seated"),
    ("side_profile", "Side Profile"),
    ("ditzy",        "Ditzy (plano 3/4)"),
    ("pov",          "POV (single hand)"),
    ("odalisque",    "Odalisque"),
]

def git_mv(src, dst):
    try:
        subprocess.run(["git", "mv", src, dst], cwd=REPO, capture_output=True, text=True, check=True)
        return True
    except Exception:
        try:
            os.rename(src, dst); return True
        except Exception as e:
            print(f"  ! No se pudo renombrar {src}: {e}"); return False

def look_num(folder):
    m = re.match(r"look0*(\d+)_", folder.lower())
    return int(m.group(1)) if m else None

def normalizar_nombres():
    """Normaliza SOLO ele_<N>_back.png / ele_<N>_profile.png para N >= MIN_LOOK."""
    cambios = 0
    if not os.path.isdir(ELE):
        return cambios
    for folder in os.listdir(ELE):
        fpath = os.path.join(ELE, folder)
        n = look_num(folder)
        if not os.path.isdir(fpath) or n is None or n < MIN_LOOK:
            continue
        for canon, bad in (("back_view", "back"), ("side_profile", "profile")):
            src = os.path.join(fpath, f"ele_{n}_{bad}.png")
            dst = os.path.join(fpath, f"ele_{n}_{canon}.png")
            if os.path.exists(src) and not os.path.exists(dst):
                if git_mv(src, dst):
                    print(f"  ↳ {folder}/ele_{n}_{bad}.png -> ele_{n}_{canon}.png")
                    cambios += 1
    return cambios

def folder_de_look(n):
    pref = f"look{n}_"
    for folder in os.listdir(ELE):
        if folder.lower().startswith(pref):
            return folder
    return None

def imgs_de_look(folder):
    fpath = os.path.join(ELE, folder)
    return {f.lower() for f in os.listdir(fpath) if f.lower().endswith(".png")}

def construir_seccion(n, folder):
    files = imgs_de_look(folder)
    cells, mat = [], 0
    for key, _ in POSES:
        fname = f"ele_{n}_{key}.png"
        if fname.lower() in files:
            cells.append(f"[📸 View](../../05_Imagenes/ele/{folder}/{fname})")
            mat += 1
        else:
            cells.append("⏳ Pendiente")
    estado = "Materializado" if mat == 7 else "Materializado parcial (app/Gemini)"
    headers = " | ".join(lbl for _, lbl in POSES)
    seps = " | ".join([":---:"] * len(POSES))
    texto = (f"### 📸 Imágenes ({mat}/7 — {estado})\n\n"
             f"| {headers} |\n| {seps} |\n| {' | '.join(cells)} |\n\n")
    return texto, mat

def actualizar_galeria():
    with open(GALERIA, encoding="utf-8") as f:
        content = f.read()
    parts = re.split(r"(?=^## .*?Look \d+:)", content, flags=re.MULTILINE)
    out, actualizados = [], []
    img_re = re.compile(r"### 📸 Imágenes[^\n]*\n(?:.*?\n)*?(?=### 📝 Prompts)", re.MULTILINE)
    for block in parts:
        m = re.match(r"^## .*?Look (\d+):", block)
        if not m:
            out.append(block); continue
        n = int(m.group(1))
        sec = img_re.search(block)
        if not sec or n < MIN_LOOK:
            out.append(block); continue
        actual = sec.group(0)
        regenerar = ("Pendiente" in actual) or ("app/Gemini" in actual)
        folder = folder_de_look(n)
        if regenerar and folder and any(imgs_de_look(folder)):
            nueva, mat = construir_seccion(n, folder)
            block = block[:sec.start()] + nueva + block[sec.end():]
            actualizados.append((n, mat))
        out.append(block)
    nuevo = "".join(out)
    if nuevo != content:
        with open(GALERIA, "w", encoding="utf-8") as f:
            f.write(nuevo)
    return actualizados

def main():
    print(f"== Sync imágenes app (Gemini → GitHub) · era app: looks >= {MIN_LOOK} ==")
    print("1) Normalizando nombres no-canónicos (back→back_view, profile→side_profile)...")
    print(f"   {normalizar_nombres()} archivo(s) renombrado(s).")
    print("2) Actualizando tracker en galeria_outfits.md...")
    upd = actualizar_galeria()
    if upd:
        for n, mat in sorted(upd):
            print(f"   L{n}: {mat}/7 registradas")
    else:
        print("   (sin secciones que actualizar)")
    print("3) Ejecuta luego: python 99_Sistema/scripts/visual/update_galleries.py")

if __name__ == "__main__":
    main()
