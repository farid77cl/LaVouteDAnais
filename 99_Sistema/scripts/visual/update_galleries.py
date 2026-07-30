import os
import re
import subprocess
import importlib.util
from datetime import datetime

# Configuración del servidor remoto
GITHUB_USER = "farid77cl"
GITHUB_REPO = "LaVouteDAnais"
GITHUB_BRANCH = "main"
REMOTE_PREFIX = f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/{GITHUB_BRANCH}/"

def get_remote_url(local_path, repo_root):
    """Convierte una ruta local a una URL de GitHub."""
    rel_path = os.path.relpath(local_path, start=repo_root)
    return REMOTE_PREFIX + rel_path.replace("\\", "/")

def get_tracked_images(directory):
    """Obtiene la lista de imágenes trackeadas por Git en el directorio."""
    try:
        # Ejecutamos git ls-files para ver qué archivos están en el índice (incluyendo untracked no ignorados)
        result = subprocess.run(['git', 'ls-files', '-c', '-o', '--exclude-standard', directory], capture_output=True, text=True, check=True)
        files = result.stdout.splitlines()
        # Solo imagenes hijas directas, no imagenes de subcarpetas.
        directory_abs = os.path.abspath(directory)
        images = []
        for file_path in files:
            if not file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
                continue
            file_abs = os.path.abspath(file_path)
            if os.path.normcase(os.path.dirname(file_abs)) == os.path.normcase(directory_abs):
                images.append(os.path.basename(file_path))
        return sorted(list(set(images)))
    except Exception as e:
        print(f"Error al listar archivos de Git en {directory}: {e}")
        # Fallback a listdir
        if os.path.exists(directory):
            return sorted([f for f in os.listdir(directory) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))])
        return []

# ── Mapeo de poses (Ama 22/07/2026) ─────────────────────────────────────────
# El mapeo viejo era `next(img for img in images if key in img.lower())`: buscaba
# la pose como SUBCADENA suelta y, si no encontraba, un fallback rellenaba la
# casilla vacía con cualquier imagen no mapeada. Resultado medido: 116 carpetas
# mostrando una imagen en la casilla de OTRA pose — `ele_200_back.png` no contiene
# "back_view", así que la Espalda quedaba vacía y se rellenaba con una ajena.
# Ahora: alias por pose + match por TOKEN (no subcadena) + la casilla sin imagen
# muestra ⏳. Una imagen jamás ocupa la casilla de otra pose.
POSE_ALIASES = {
    'standing':     ('standing', 'frontal'),
    'back_view':    ('back_view', 'backview', 'back', 'espalda'),
    'seated':       ('seated', 'sitting', 'sentada'),
    'side_profile': ('side_profile', 'sideprofile', 'profile', 'side', 'perfil'),
    'ditzy':        ('ditzy',),
    'pov':          ('pov',),
    'odalisque':    ('odalisque', 'lying'),
}

_POSE_PREFIX_RE = re.compile(r'^(?:ele|helena)_\d+_', re.I)

def pose_de_imagen(img_name):
    """(pose_canónica, rango, sufijo) de un nombre de archivo, o (None, 99, '').

    `rango` ordena la calidad del match, de mejor a peor:
      0..n  el nombre EMPIEZA con el alias (tras `ele_NNN_`), en el orden en que
            está declarado en POSE_ALIASES — así `standing` le gana a `frontal`
            y `back_view` a `back` para la misma pose.
      10+   el alias aparece como token suelto en cualquier posición: cubre los
            nombres heredados tipo `look87_01_standing_1774187079234.png`.
    Gana siempre el alias más largo, para que `side`/`profile` no le roben la
    imagen a `side_profile`.
    """
    resto = _POSE_PREFIX_RE.sub('', os.path.splitext(img_name)[0].lower())
    acolchado = '_' + resto + '_'
    mejor = None  # (canon, rango, largo_alias, sufijo)
    for canon, aliases in POSE_ALIASES.items():
        for orden, alias in enumerate(aliases):
            if resto == alias or resto.startswith(alias + '_'):
                cand = (canon, orden, len(alias), resto[len(alias):])
            elif ('_' + alias + '_') in acolchado:
                cand = (canon, 10 + orden, len(alias), '')
            else:
                continue
            # más específico primero; a igual especificidad, mejor rango
            if mejor is None or (cand[2], -cand[1]) > (mejor[2], -mejor[1]):
                mejor = cand
    return (mejor[0], mejor[1], mejor[3]) if mejor else (None, 99, '')

def map_poses(images, canonical_keys):
    """Una imagen por pose. Gana el alias canónico y el nombre limpio sobre las
    variantes (`_1`, `_v1`, `_fixed`). Devuelve (pose_map, sobrantes)."""
    candidatas = {k: [] for k in canonical_keys}
    sobrantes = []
    for img in images:
        pose, rango, sufijo = pose_de_imagen(img)
        if pose in candidatas:
            candidatas[pose].append((rango, len(sufijo), sufijo, img))
        else:
            sobrantes.append(img)
    pose_map = {}
    for k in canonical_keys:
        if candidatas[k]:
            candidatas[k].sort()          # rango, luego sufijo más corto, luego nombre
            pose_map[k] = candidatas[k][0][3]
            sobrantes.extend(t[3] for t in candidatas[k][1:])
        else:
            pose_map[k] = None
    return pose_map, sorted(sobrantes)

def get_tracked_directories(base_dir):
    """Lista carpetas existentes en Git y en el disco local bajo base_dir."""
    directories = set()
    base_abs = os.path.abspath(base_dir)

    if os.path.exists(base_dir):
        for root, dirs, _ in os.walk(base_dir):
            if '.git' in root:
                continue
            directories.add(os.path.abspath(root))
            for dir_name in dirs:
                if not dir_name.startswith('.'):
                    directories.add(os.path.abspath(os.path.join(root, dir_name)))

    try:
        result = subprocess.run(['git', 'ls-files', base_dir], capture_output=True, text=True, check=True)
        for file_path in result.stdout.splitlines():
            directory = os.path.abspath(os.path.dirname(file_path))
            while os.path.normcase(directory).startswith(os.path.normcase(base_abs)):
                directories.add(directory)
                if os.path.normcase(directory) == os.path.normcase(base_abs):
                    break
                directory = os.path.dirname(directory)
    except Exception as e:
        print(f"Error al descubrir carpetas de Git en {base_dir}: {e}")

    return sorted(directories, key=lambda path: path.count(os.sep), reverse=True)

def get_look_number(directory):
    match = re.match(r'look0*(\d+)', os.path.basename(directory).lower())
    return int(match.group(1)) if match else None

def is_top_level_look(directory, ele_path):
    return (
        os.path.normcase(os.path.dirname(directory)) == os.path.normcase(os.path.abspath(ele_path))
        and get_look_number(directory) is not None
    )

def has_readme(directory):
    local_readme = os.path.join(directory, 'README.md')
    if os.path.exists(local_readme):
        return True
    try:
        result = subprocess.run(['git', 'ls-files', local_readme], capture_output=True, text=True, check=True)
        return bool(result.stdout.strip())
    except Exception:
        return False

def get_canonical_look_directories(ele_path):
    groups = {}
    for directory in get_tracked_directories(ele_path):
        if not is_top_level_look(directory, ele_path):
            continue
        number = get_look_number(directory)
        groups.setdefault(number, []).append(directory)

    canonical = set()
    for number, directories in groups.items():
        # Una carpeta SIN imágenes nunca puede ser la canónica si alguna hermana sí las
        # tiene. Sin esta guardia el bono de README (+1000) le gana al conteo de imágenes
        # y un look entero desaparece de la galería: pasó con el L85 el 20/07/2026, cuando
        # la app creó `look085_vinyl_fresa_bimbo_xxxl` (7 poses, sin README) y la vieja
        # `look085_vinyl_fresa_bimbo` quedó vacía pero con README — ganaba 1500 a 507 y las
        # 7 imágenes recién materializadas no se veían en ninguna parte.
        con_imagenes = [d for d in directories if get_tracked_images(d)]
        candidatas = con_imagenes or directories

        def era_rank(directory):
            """Prioridad por ERA, por encima de cualquier puntaje.

            Bug detectado el 20/07/2026 mientras la Ama materializaba el archivo: el L88
            tenía `look088_gallery_opening` con 16 imágenes `helena_look88_*` (era Helena,
            capítulo cerrado) y README, contra `look088_highgloss_gallery_opening` con las
            3 imágenes `ele_88_*` recién subidas y sin README. Ganaba 1016 a 3, así que las
            imágenes NUEVAS de la Ama quedaban invisibles en la galería. Mismo cuadro en el
            L87 (`ele_v3_core` 5 imgs con README le ganaba a `vinyl_flight_attendant`, que
            es donde la app está subiendo AHORA).

            El defecto de fondo es que el bono de README es CIRCULAR: el README lo escribe
            este mismo script, así que la carpeta elegida una vez se auto-blinda y ninguna
            carpeta nueva puede desbancarla por muchas imágenes vigentes que tenga. La era
            va como clave separada y primera para que ese bono no pueda pisarla.
            (Pariente del bug 'el clasificador se lee a sí mismo', 19/07/2026.)
            """
            imagenes = [os.path.basename(i).lower() for i in get_tracked_images(directory)]
            if not imagenes:
                return 0
            if any(i.startswith('ele_') for i in imagenes):
                return 2      # era vigente
            if all(i.startswith('helena_') for i in imagenes):
                return 1      # era Helena — cerrada, solo si no hay nada mejor
            return 2          # nombres históricos/curados: se tratan como vigentes

        def score(directory):
            name = os.path.basename(directory).lower()
            value = len(get_tracked_images(directory))
            if has_readme(directory):
                value += 1000
            if number < 100 and re.match(r'look\d{3}($|_)', name):
                value += 500
            if re.search(r'_(lingerie|bikini)($|_)', name):
                value += 100
            return value

        # Desempate DETERMINISTA por nombre de carpeta: con puntajes iguales, `max()` devolvía
        # el primero que encontrara y el orden de iteración varía entre corridas — el L113
        # (dos looks distintos con el mismo número, 6 imágenes cada uno) se daba vuelta solo
        # en cada regeneración y ensuciaba el diff sin que nadie hubiera cambiado nada.
        # Esto NO decide cuál de los dos looks se queda con el número: eso es juicio de la Ama.
        canonical.add(max(candidatas, key=lambda d: (era_rank(d), score(d), os.path.basename(d))))

    return canonical

def generate_folder_gallery(directory, repo_root):
    """Genera el README.md para una carpeta individual."""
    os.makedirs(directory, exist_ok=True)
    images = get_tracked_images(directory)
    all_local = os.listdir(directory) if os.path.exists(directory) else []
    subdirs = [d for d in all_local if os.path.isdir(os.path.join(directory, d)) and not d.startswith('.')]
    
    gallery_path = os.path.join(directory, 'README.md')
    rel_dir_name = os.path.basename(directory)
    
    if not images and not subdirs and not "look" in rel_dir_name.lower():
        if os.path.exists(gallery_path):
            os.remove(gallery_path)
        return

    with open(gallery_path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(f"# 🖼️ Galería: {rel_dir_name}\n")
        f.write(f"> **Estado:** ☁️ Almacenamiento Remoto (GitHub)\n\n")
        
        if images:
            f.write(f"Total imágenes: {len(images)}\n\n")
            f.write("## Colección Destacada\n")
            featured = images[:6]
            cols_feat = 3
            f.write("| | | |\n|:---:|:---:|:---:|\n")
            for i in range(0, len(featured), cols_feat):
                chunk = featured[i:i+cols_feat]
                row_items = []
                for img in chunk:
                    url = get_remote_url(os.path.join(directory, img), repo_root)
                    row_items.append(f"![{img}]({url})")
                f.write("| " + " | ".join(row_items) + " |\n")
            f.write("\n---\n\n")

            f.write("## 📸 Vista Previa Completa\n\n")
            cols = 4
            f.write("| " + " | ".join(["Imagen"] * min(len(images), cols)) + " |\n")
            f.write("| " + " | ".join([":---:"] * min(len(images), cols)) + " |\n")
            
            for i in range(0, len(images), cols):
                chunk = images[i:i+cols]
                row_items = []
                for img in chunk:
                    url = get_remote_url(os.path.join(directory, img), repo_root)
                    row_items.append(f"![{img}]({url})")
                f.write("| " + " | ".join(row_items) + " |\n")
            f.write("\n\n---\n\n")

        if subdirs:
            f.write("## 📁 Subcarpetas / Colecciones\n")
            for d in sorted(subdirs):
                f.write(f"- 📁 [**{d.replace('_', ' ').title()}**](./{d}/README.md)\n")
            f.write("\n---\n")
        
        if images:
            f.write("## 📜 Lista de Archivos (Descarga Directa)\n")
            for img in sorted(images):
                url = get_remote_url(os.path.join(directory, img), repo_root)
                f.write(f"- [{img}]({url})\n")
            f.write("\n---\n")
            
        # Salida DETERMINISTA (Ama 16/06/2026): sin fecha volátil. El bot paralelo corre
        # este mismo script; con datetime.now() cada corrida flipeaba la fecha y churneaba
        # TODOS los README aunque no cambiara una imagen -> pelea perpetua. Sin fecha,
        # misma entrada = mismos bytes = cero diff.
        f.write("*Sincronizado con GitHub.* 👄")

def generate_master_outfit_gallery(base_path, repo_root):
    """Genera la Galería Maestra de Looks de Ele."""
    ele_path = os.path.join(base_path, 'ele')
    output_file = os.path.join(ele_path, 'README.md')
    if not os.path.exists(ele_path): return

    look_folders = []
    for full_path in get_canonical_look_directories(ele_path):
        item = os.path.basename(full_path)
        look_num = get_look_number(full_path) or 999
        look_folders.append((look_num, item, full_path))
    
    look_folders.sort(key=lambda x: x[0], reverse=True)
    content = ["# 👗 Galería de Looks: Ele de Anaïs\n\n", "> El clóset visual infinito en la nube. 🫦✨\n\n", "---\n\n"]

    # Poses canónicas V3.5 — 7 por look
    CANONICAL_POSES = [
        ('standing',    'De Pie'),
        ('back_view',   'Espalda'),
        ('seated',      'Sentada'),
        ('side_profile','Perfil'),
        ('ditzy',       'Ditzy'),
        ('pov',         'POV'),
        ('odalisque',   'Odalisca'),
    ]

    total_looks = len(look_folders)
    print(f"  -> Procesando {total_looks} looks para la Galería Maestra de Ele...", flush=True)

    for idx, (_, folder_name, folder_path) in enumerate(look_folders, start=1):
        if idx % 50 == 0 or idx == total_looks:
            print(f"  -> Galería Maestra Ele: {idx}/{total_looks} looks procesados ({int(idx/total_looks*100)}%)", flush=True)
        images = get_tracked_images(folder_path)
        if not images: continue
        clean_name = folder_name.replace('_', ' ').title()
        display_title = re.sub(r'Look(\d+)', r'Look \1:', clean_name)
        content.append(f"## 👠 {display_title}\n\n")

        # Mapear cada pose canónica a la imagen correspondiente
        pose_map, sobrantes = map_poses(images, [k for k, _ in CANONICAL_POSES])

        def get_md(img_name, folder_path=folder_path):
            # Sin fallback: una casilla vacía se muestra vacía. Rellenarla con una
            # imagen de otra pose es mentirle a la galería (ver POSE_ALIASES).
            if img_name:
                url = get_remote_url(os.path.join(folder_path, img_name), repo_root)
                return f"![{img_name}]({url})"
            return "⏳"

        # Detectar si el look tiene 7 poses o solo 5
        has_7 = any(pose_map.get(k) for k in ('pov', 'odalisque'))
        active_poses = CANONICAL_POSES if has_7 else CANONICAL_POSES[:5]

        headers = ' | '.join(label for _, label in active_poses)
        separators = ' | '.join([':---:'] * len(active_poses))
        cells = ' | '.join(get_md(pose_map.get(key)) for key, _ in active_poses)
        content.append(f"| {headers} |\n| {separators} |\n| {cells} |\n\n")

        # Tomas extra: variantes de una pose ya ocupada, o archivos sin pose
        # reconocible. Se listan en vez de colarse en una casilla ajena.
        if sobrantes:
            enlaces = ', '.join(
                f"[{img}]({get_remote_url(os.path.join(folder_path, img), repo_root)})"
                for img in sobrantes)
            content.append(f"<sub>📎 Tomas extra ({len(sobrantes)}): {enlaces}</sub>\n\n")
        content.append("---\n\n")

    content.append("*Galería maestra de Ele.* 🦇")  # determinista: sin fecha volátil (no pelear con el bot)
    with open(output_file, 'w', encoding='utf-8', newline='\n') as f: f.writelines(content)

def generate_miss_doll_master_gallery(base_path, repo_root):
    """Genera la Galería Maestra de Miss Doll."""
    md_path = os.path.join(base_path, 'miss_doll')
    output_file = os.path.join(md_path, 'README.md')
    if not os.path.exists(md_path): return

    categories = [
        ("👗 Outfits", "Outfits"),
        ("💵 Stripper VIP", "stripper_vip"),
        ("Stripper Series", "stripper_series"),
        ("✂️ Strips / Closeups", "Strips"),
        ("📢 Banners", "Banners"),
        ("💎 Luxury Escort", "luxury_escort_ultra"),
        ("👰 Wedding Night", "wedding_night"),
        ("📑 Referencia Canon", "Reference"),
        ("⚙️ UI Assets", "UI_Assets"),
        ("📦 General", "General")
    ]

    content = ["# 💖 Galería Maestra: Miss Doll\n\n", "> El archivo visual de la muñequita de platino (Edición Nube). 🎀✨\n\n", "---\n\n"]

    for title, folder_name in categories:
        folder_path = os.path.join(md_path, folder_name)
        images = get_tracked_images(folder_path)
        if not images: continue
        
        content.append(f"## {title}\nTotal: {len(images)} imágenes. [Ver carpeta completa](./{folder_name}/README.md)\n\n")
        sample = images[:3]
        content.append("| Destacada 1 | Destacada 2 | Destacada 3 |\n|:---:|:---:|:---:|\n")
        row_items = []
        for img in sample:
            url = get_remote_url(os.path.join(folder_path, img), repo_root)
            row_items.append(f"![{img}]({url})")
        while len(row_items) < 3: row_items.append("-")
        content.append("| " + " | ".join(row_items) + " |\n\n---\n\n")

    content.append("*Galería Miss Doll coordinada por Ele.* 🌹")  # determinista: sin fecha volátil
    with open(output_file, 'w', encoding='utf-8', newline='\n') as f: f.writelines(content)

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
    base_path = os.path.join(repo_root, '05_Imagenes')
    ele_path = os.path.join(base_path, 'ele')
    canonical_looks = get_canonical_look_directories(ele_path)
    
    tracked_dirs = get_tracked_directories(base_path)
    total_dirs = len(tracked_dirs)
    print(f"Iniciando actualización masiva de galerías ({total_dirs} carpetas)...", flush=True)
    
    processed = 0
    for root in tracked_dirs:
        if '.git' in root: continue
        if is_top_level_look(root, ele_path) and root not in canonical_looks:
            continue
        generate_folder_gallery(root, repo_root)
        processed += 1
        if processed % 25 == 0 or processed == total_dirs:
            print(f"  -> Progreso: {processed}/{total_dirs} carpetas procesadas ({int(processed/total_dirs*100)}%)", flush=True)
    
    print("Actualizando Galería Maestra de Ele...", flush=True)
    generate_master_outfit_gallery(base_path, repo_root)
    
    print("Actualizando Galería Maestra de Miss Doll...", flush=True)
    generate_miss_doll_master_gallery(base_path, repo_root)
    
    print("Actualizando Índice Rápido de Galería...", flush=True)
    try:
        index_script = os.path.join(script_dir, "generar_index_galeria.py")
        spec = importlib.util.spec_from_file_location("generar_index_galeria", index_script)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        mod.main()
    except Exception as e:
        print(f"  (Advertencia: no se pudo generar el índice: {e})", flush=True)

    print("Proceso completado exitosamente.", flush=True)

if __name__ == "__main__":
    main()
