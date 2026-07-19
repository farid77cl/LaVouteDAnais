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

_INDICE = None

def indice_git():
    """{carpeta: {archivo.png}} leído del ÍNDICE DE GIT, no del disco.

    Antes esto hacía os.listdir(). En las máquinas con sparse-checkout / skip-worktree
    (la solo-literaria tiene 0 PNG en disco) el tracker se reescribía a la baja y
    declaraba pendientes cientos de poses que sí existen en el repo — la misma mentira
    del 14/07 pero al revés, y con el mismo costo: cuota quemada regenerando lo que ya
    está. `update_galleries.py` ya usaba git ls-files; ahora ambos miden lo mismo.
    """
    global _INDICE
    if _INDICE is None:
        _INDICE = {}
        res = subprocess.run(["git", "ls-files", "05_Imagenes/ele"], cwd=REPO,
                             capture_output=True, text=True, encoding="utf-8")
        for ruta in res.stdout.splitlines():
            m = re.match(r"05_Imagenes/ele/([^/]+)/([^/]+\.png)$", ruta, re.I)
            if m:
                _INDICE.setdefault(m.group(1), set()).add(m.group(2))
    return _INDICE

def folders_de_look(n):
    """TODAS las carpetas del look. Un mismo look puede tener 2 slugs distintos
    (la app y el agente los nombraron distinto) con las poses repartidas entre ambas."""
    pref = re.compile(rf"^look0*{n}_", re.I)
    found = [f for f in indice_git() if pref.match(f)]
    # la carpeta con más PNG manda cuando una pose está en las dos
    return sorted(found, key=lambda f: (-len(imgs_de_look(f)), f))

def imgs_de_look(folder):
    return set(indice_git().get(folder, ()))

def buscar_pose(n, key, folders):
    """Devuelve (folder, filename) de la pose, o None.

    Tres nomenclaturas conviven y las TRES cuentan:
      · canónica            ele_313_back_view.png
      · con timestamp API   ele_313_back_view_1783817436657.png
      · slug largo          ele_look300_black_satin_veiled_femme_fatale_noir_back_view.png
    El slug largo no se reconocía y el tracker declaraba pendientes poses que sí existen
    (L299 4/7 y L300 2/7 cuando ambos están completos, 19/07). La pose va ANCLADA AL FINAL,
    así que un slug que contenga una palabra de pose no puede robar el match.
    """
    rx = re.compile(rf"^ele_(?:look)?0*{n}_(?:.*_)?{key}(_\d+)?\.png$", re.I)
    for folder in folders:
        for f in sorted(imgs_de_look(folder)):
            if rx.match(f):
                return folder, f
    return None

def construir_seccion(n, folders):
    cells, mat = [], 0
    for key, _ in POSES:
        hit = buscar_pose(n, key, folders)
        if hit:
            folder, fname = hit
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
    out, actualizados, rutas_corregidas = [], [], []
    # La sección 📸 va desde su heading hasta el siguiente heading (##/###) o hasta el primer
    # prompt suelto (**Standing:**). NO se puede anclar en "### 📝 Prompts": la mitad de los looks
    # no tiene ese heading y quedaban invisibles al sync (L717/L732 llevaban días en 0/7 con las
    # 7 imágenes en disco, y la Ama regeneraba lo que ya existía).
    img_re = re.compile(r"^### 📸 Imágenes[^\n]*\n(?:(?!^#{2,3}\s|^\*\*Standing:\*\*).*\n)*", re.MULTILINE)
    for block in parts:
        m = re.match(r"^## .*?Look (\d+):", block)
        if not m:
            out.append(block); continue
        n = int(m.group(1))
        sec = img_re.search(block)
        if not sec or n < MIN_LOOK:
            out.append(block); continue
        actual = sec.group(0)
        folders = folders_de_look(n)
        if folders and any(imgs_de_look(f) for f in folders):
            nueva, mat = construir_seccion(n, folders)
            m_trk = re.search(r"### 📸 Imágenes \((\d+)/7", actual)
            declarado = int(m_trk.group(1)) if m_trk else -1
            # Regenerar en cuanto la sección difiera del disco — NO basta comparar el conteo:
            # al fusionar/renombrar una carpeta el conteo queda igual pero las RUTAS de los links
            # apuntan a una carpeta que ya no existe (49 links rotos tras la fusión del 14/07).
            if actual.strip() != nueva.strip():
                block = block[:sec.start()] + nueva + block[sec.end():]
                if declarado != mat:
                    actualizados.append((n, declarado, mat))
                else:
                    rutas_corregidas.append(n)
        out.append(block)
    nuevo = "".join(out)
    if nuevo != content:
        with open(GALERIA, "w", encoding="utf-8") as f:
            f.write(nuevo)
    return actualizados, rutas_corregidas

def main():
    print(f"== Sync imágenes app (Gemini → GitHub) · era app: looks >= {MIN_LOOK} ==")
    print("1) Normalizando nombres no-canónicos (back→back_view, profile→side_profile)...")
    print(f"   {normalizar_nombres()} archivo(s) renombrado(s).")
    print("2) Actualizando tracker en galeria_outfits.md...")
    upd, rutas = actualizar_galeria()
    if upd:
        recup = sum(nuevo - viejo for _, viejo, nuevo in upd if nuevo > viejo)
        for n, viejo, nuevo in sorted(upd):
            flecha = "⬆️ recuperadas" if nuevo > viejo else "⬇️ corregido (decía de más)"
            print(f"   L{n}: {viejo}/7 → {nuevo}/7  {flecha}")
        print(f"   ── {len(upd)} look(s) corregidos · {recup} pose(s) reales que figuraban como pendientes")
    else:
        print("   (conteos ya coinciden con el disco)")
    if rutas:
        print(f"   🔗 {len(rutas)} look(s) con links re-apuntados a la carpeta correcta: "
              f"{', '.join('L'+str(n) for n in sorted(rutas)[:12])}{' …' if len(rutas)>12 else ''}")
    print("3) Ejecuta luego: python 99_Sistema/scripts/visual/update_galleries.py")

if __name__ == "__main__":
    main()
