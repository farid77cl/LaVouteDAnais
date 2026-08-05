"""
Renombrado de nomenclatura legacy — Miss Doll (C-N.png / md_NNN_cN_*.png) y
Anais (anais_lookNUM_pose.png -> anais_NUM_pose.png), post-estandarizacion de
poses del 05/08/2026 (ver _perfiles_visuales/miss_doll.md y anais.md, S4).

Corre en la maquina VISUAL (donde existen los PNG). En la maquina solo-literaria
no encuentra nada que mover y termina sin tocar disco.

Uso:
    python renombrar_legacy_multipersonaje.py            # dry-run (default)
    python renombrar_legacy_multipersonaje.py --apply     # ejecuta de verdad

No toca la linea Boudoir de Anais (L01/L02..., poses propias) - queda fuera
de este remapeo por decision explicita de la Ama (05/08/2026).
"""
import os
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", ".."))

MD_GALLERY = os.path.join(REPO_ROOT, "02_Personajes", "01_Principales", "miss_doll", "GALERIA_OUTFITS_MISS_DOLL.md")
MD_IMAGES_DIR = os.path.join(REPO_ROOT, "05_Imagenes", "miss_doll")

ANAIS_GALLERY = os.path.join(REPO_ROOT, "02_Personajes", "01_Principales", "anais", "galeria_looks_anais.md")
ANAIS_IMAGES_DIR = os.path.join(REPO_ROOT, "05_Imagenes", "anais")

DRY_RUN = "--apply" not in sys.argv

# C-1 Cruel Contrapposto / C-2 Monarch Throne / C-3 Espalda Total /
# C-4 Tres Cuartos Arrogante / C-5 Close Up Fria / C-6 Throne en Suelo
# -> las 7 categorias universales (Standing/Back View/Seated/Side Profile/
#    Glacial Command/POV/Odalisque). No hay pose legacy para POV: nunca se
#    genero esa toma en el set viejo, queda 0/7 hasta que se genere.
MD_LEGACY_POSE_MAP = {
    "c1": "standing",
    "c2": "seated",
    "c3": "back_view",
    "c4": "side_profile",
    "c5": "glacial_command",
    "c6": "odalisque",
}

# Slugs ya "limpios" que usa la linea principal de Anais (no la Boudoir).
ANAIS_MAIN_POSE_SLUGS = {"standing", "seated", "three_quarter", "closeup"}


def git_mv(src, dst):
    print(f"    git mv  {os.path.relpath(src, REPO_ROOT)}  ->  {os.path.relpath(dst, REPO_ROOT)}")
    if not DRY_RUN:
        subprocess.run(["git", "mv", src, dst], cwd=REPO_ROOT, check=True)


def patch_markdown_per_look(path, look_header_re, renames_by_look):
    """renames_by_look: {look_num_str: [(old_filename, new_filename), ...]}"""
    if not os.path.exists(path):
        print(f"  [!] No existe {path}, no se toca el markdown.")
        return
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    headers = list(look_header_re.finditer(text))
    if not headers:
        print(f"  [!] No se encontraron encabezados de look en {path}.")
        return

    for i, m in enumerate(headers):
        look_num = m.group(1)
        start = m.end()
        end = headers[i + 1].start() if i + 1 < len(headers) else len(text)
        section = text[start:end]
        pairs = renames_by_look.get(look_num.lstrip("0") or "0") or renames_by_look.get(look_num)
        if not pairs:
            continue
        for old_name, new_name in pairs:
            new_section = section.replace(f"`{old_name}`", f"`{new_name}`")
            if new_section != section:
                text = text[:start] + new_section + text[start + len(section):]
                # recompute offsets for remaining headers since length may have changed
                delta = len(new_section) - len(section)
                headers = list(look_header_re.finditer(text))
                section = new_section
                end = end + delta

    if not DRY_RUN:
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        print(f"  [OK] Markdown actualizado: {os.path.relpath(path, REPO_ROOT)}")
    else:
        print(f"  [DRY-RUN] Markdown a actualizar: {os.path.relpath(path, REPO_ROOT)}")


def process_miss_doll():
    print("\n=== Miss Doll ===")
    if not os.path.isdir(MD_IMAGES_DIR):
        print(f"  [!] No existe {MD_IMAGES_DIR} en esta maquina (0 PNG en disco) - nada que hacer.")
        return

    renames_by_look = {}
    look_folder_re = re.compile(r"^look0*(\d+)_", re.IGNORECASE)

    for entry in sorted(os.listdir(MD_IMAGES_DIR)):
        folder = os.path.join(MD_IMAGES_DIR, entry)
        if not os.path.isdir(folder):
            continue
        fm = look_folder_re.match(entry)
        if not fm:
            continue
        look_num = fm.group(1)
        print(f"\n  Look {look_num} ({entry}):")

        for fname in sorted(os.listdir(folder)):
            if not fname.lower().endswith(".png"):
                continue
            base = fname[:-4]
            legacy_key = None

            # Patron A: C-1.png ... C-6.png (bare)
            m = re.fullmatch(r"[Cc]-(\d)", base)
            if m:
                legacy_key = f"c{m.group(1)}"
            else:
                # Patron B: md_001_c1_cruel.png (ya trae numero + slug propio)
                m2 = re.fullmatch(r"md_\d+_c(\d)_.+", base, re.IGNORECASE)
                if m2:
                    legacy_key = f"c{m2.group(1)}"

            if legacy_key is None or legacy_key not in MD_LEGACY_POSE_MAP:
                continue

            new_pose = MD_LEGACY_POSE_MAP[legacy_key]
            new_name = f"miss_doll_{look_num}_{new_pose}.png"
            if fname == new_name:
                continue

            src = os.path.join(folder, fname)
            dst = os.path.join(folder, new_name)
            git_mv(src, dst)
            renames_by_look.setdefault(look_num, []).append((fname, new_name))

    if renames_by_look:
        look_header_re = re.compile(r"^## .* Look (\d+):", re.MULTILINE)
        patch_markdown_per_look(MD_GALLERY, look_header_re, renames_by_look)
    else:
        print("\n  Sin archivos legacy encontrados (o ya estan todos en convencion nueva).")


def process_anais():
    print("\n=== Anais (linea principal, Boudoir NO se toca) ===")
    if not os.path.isdir(ANAIS_IMAGES_DIR):
        print(f"  [!] No existe {ANAIS_IMAGES_DIR} en esta maquina (0 PNG en disco) - nada que hacer.")
        return

    renames_by_look = {}
    fname_re = re.compile(r"^anais_look0*(\d+)_([a-z_]+)\.png$", re.IGNORECASE)

    for root, _dirs, files in os.walk(ANAIS_IMAGES_DIR):
        if "boudoir" in root.lower() or "lenceria" in root.lower():
            continue
        for fname in sorted(files):
            m = fname_re.match(fname)
            if not m:
                continue
            look_num, pose_slug = m.group(1), m.group(2).lower()
            if pose_slug not in ANAIS_MAIN_POSE_SLUGS:
                continue  # probablemente Boudoir con otro nombre de carpeta; no tocar
            new_name = f"anais_{look_num}_{pose_slug}.png"
            if fname == new_name:
                continue
            src = os.path.join(root, fname)
            dst = os.path.join(root, new_name)
            git_mv(src, dst)
            renames_by_look.setdefault(look_num, []).append((fname, new_name))

    if renames_by_look:
        look_header_re = re.compile(r"^## .* Look (\d+):", re.MULTILINE)
        patch_markdown_per_look(ANAIS_GALLERY, look_header_re, renames_by_look)
    else:
        print("\n  Sin archivos legacy encontrados (o ya estan todos en convencion nueva).")


def main():
    print(f"Modo: {'DRY-RUN (nada se toca)' if DRY_RUN else 'EJECUTANDO CAMBIOS REALES'}")
    process_miss_doll()
    process_anais()
    if DRY_RUN:
        print("\n[DRY-RUN] Nada fue modificado. Correr con --apply para ejecutar de verdad.")


if __name__ == "__main__":
    main()
