import os
import re
import subprocess
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
        # Ejecutamos git ls-files para ver qué archivos están en el índice
        # Usamos -c para archivos cacheados y -z para manejar espacios si hubiera
        result = subprocess.run(['git', 'ls-files', directory], capture_output=True, text=True, check=True)
        files = result.stdout.splitlines()
        # Solo imagenes hijas directas, no imagenes de subcarpetas.
        directory_abs = os.path.abspath(directory)
        images = []
        for file_path in files:
            if not file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
                continue
            file_abs = os.path.abspath(file_path)
            if os.path.normcase(os.path.dirname(file_abs)) == os.path.normcase(directory_abs):
                images.append(os.path.basename(file_path))
        return sorted(list(set(images)))
    except Exception as e:
        print(f"Error al listar archivos de Git en {directory}: {e}")
        # Fallback a listdir
        if os.path.exists(directory):
            return sorted([f for f in os.listdir(directory) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
        return []

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

        canonical.add(max(directories, key=score))

    return canonical

def generate_folder_gallery(directory, repo_root):
    """Genera el README.md para una carpeta individual."""
    os.makedirs(directory, exist_ok=True)
    images = get_tracked_images(directory)
    all_local = os.listdir(directory) if os.path.exists(directory) else []
    subdirs = [d for d in all_local if os.path.isdir(os.path.join(directory, d)) and not d.startswith('.')]
    
    gallery_path = os.path.join(directory, 'README.md')
    rel_dir_name = os.path.basename(directory)
    
    # Si no hay imágenes ni subcarpetas, y no es un look, borramos README si existe
    if not images and not subdirs and not "look" in rel_dir_name.lower():
        if os.path.exists(gallery_path):
            os.remove(gallery_path)
        return

    with open(gallery_path, 'w', encoding='utf-8') as f:
        f.write(f"# 🖼️ Galería: {rel_dir_name}\n")
        f.write(f"> **Estado:** ☁️ Almacenamiento Remoto (GitHub)\n\n")
        
        if images:
            f.write(f"Total imágenes: {len(images)}\n\n")
            
            # --- SECCIÓN 1: COLECCIÓN DESTACADA ---
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

            # --- SECCIÓN 2: VISTA PREVIA COMPLETA ---
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
            
        f.write(f"*Sincronizado con GitHub: {datetime.now().strftime('%Y-%m-%d')}* 👄")

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
    content = ["# 👗 Galería de Looks: Helena de Anaïs\n\n", "> El clóset visual infinito en la nube. 🫦✨\n\n", "---\n\n"]

    for _, folder_name, folder_path in look_folders:
        images = get_tracked_images(folder_path)
        if not images: continue
        clean_name = folder_name.replace('_', ' ').title()
        display_title = re.sub(r'Look(\d+)', r'Look \1:', clean_name)
        content.append(f"## 🕷️ {display_title}\n\n")
        
        poses = {p: next((img for img in images if p in img.lower()), None) for p in ['standing', 'seated', 'profile', 'back', 'ditzy']}
        remaining = [img for img in images if img not in poses.values()]
        
        def get_md(img_name):
            if img_name:
                url = get_remote_url(os.path.join(folder_path, img_name), repo_root)
                return f"![{img_name}]({url})"
            if remaining:
                img = remaining.pop(0)
                url = get_remote_url(os.path.join(folder_path, img), repo_root)
                return f"![{img}]({url})"
            return "⏳"

        content.append("| De Pie | Sentada | Perfil | Espalda | Ditzy |\n|:---:|:---:|:---:|:---:|:---:|\n")
        content.append(f"| {get_md(poses['standing'])} | {get_md(poses['seated'])} | {get_md(poses['profile'])} | {get_md(poses['back'])} | {get_md(poses['ditzy'])} |\n\n---\n\n")

    content.append(f"*Última actualización maestra: {datetime.now().strftime('%d/%m/%Y')}* 🦇")
    with open(output_file, 'w', encoding='utf-8') as f: f.writelines(content)

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

    content.append(f"*Galería Miss Doll coordinada por Helena — {datetime.now().strftime('%d/%m/%Y')}* 🌹")
    with open(output_file, 'w', encoding='utf-8') as f: f.writelines(content)

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
    base_path = os.path.join(repo_root, '05_Imagenes')
    ele_path = os.path.join(base_path, 'ele')
    canonical_looks = get_canonical_look_directories(ele_path)
    
    print(f"Iniciando actualización masiva de galerías (Modelo Remoto)...")
    
    # 1. Procesar todas las carpetas individuales
    for root in get_tracked_directories(base_path):
        if '.git' in root: continue
        if is_top_level_look(root, ele_path) and root not in canonical_looks:
            continue
        generate_folder_gallery(root, repo_root)
    
    # 2. Generar galerías maestras
    print("Actualizando Galería Maestra de Ele...")
    generate_master_outfit_gallery(base_path, repo_root)
    
    print("Actualizando Galería Maestra de Miss Doll...")
    generate_miss_doll_master_gallery(base_path, repo_root)
    
    print("Proceso completado exitosamente.")

if __name__ == "__main__":
    main()
