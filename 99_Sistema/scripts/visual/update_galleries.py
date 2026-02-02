import os
import re
from datetime import datetime

def generate_gallery(directory):
    # Get all items in directory
    all_items = os.listdir(directory)
    images = [f for f in all_items if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    subdirs = [d for d in all_items if os.path.isdir(os.path.join(directory, d)) and not d.startswith('.')]
    
    gallery_path = os.path.join(directory, 'GALERIA.md')
    rel_dir_name = os.path.basename(directory)
    
    # If folder is completely empty (no images, no subdirs), clean up or skip
    if not images and not subdirs:
        if os.path.exists(gallery_path):
            os.remove(gallery_path)
        return

    with open(gallery_path, 'w', encoding='utf-8') as f:
        f.write(f"# 🖼️ Galería: {rel_dir_name}\n")
        
        # --- SECTION 1: DIRECT IMAGES ---
        if images:
            f.write(f"Total imágenes: {len(images)}\n\n")
            f.write("## 📸 Vista Previa\n\n")
            cols = 3
            f.write("| " + " | ".join(["Imagen"] * min(len(images), cols)) + " |\n")
            f.write("| " + " | ".join([":---:"] * min(len(images), cols)) + " |\n")
            
            for i in range(0, len(images), cols):
                chunk = images[i:i+cols]
                row = "| " + " | ".join([f"![{img}](./{img})" for img in chunk]) + " |\n"
                f.write(row)
            f.write("\n\n---\n\n")

            # --- ASSISTANT CAROUSEL ---
            carousel_files = images[:15]
            if carousel_files:
                f.write("## 🎡 Carrusel Interactivo (Top 15)\n\n")
                f.write("````carousel\n")
                for i, img in enumerate(carousel_files):
                    f.write(f"![{img}](./{img})\n")
                    if i < len(carousel_files) - 1:
                        f.write("<!-- slide -->\n")
                f.write("````\n\n")

        # --- SECTION 2: NAVIGATION (SUBFOLDERS) ---
        if subdirs:
            f.write("## 📁 Subcarpetas / Colecciones\n")
            f.write("Explora las secciones de esta categoría:\n\n")
            for d in sorted(subdirs):
                # Check if subfolder has a gallery
                sub_gallery = os.path.join(directory, d, 'GALERIA.md')
                status = "✅" if os.path.exists(sub_gallery) or any(f.lower().endswith(('.png', '.jpg', '.jpeg')) for f in os.listdir(os.path.join(directory, d))) else "📁"
                f.write(f"- {status} [**{d.replace('_', ' ').title()}**](./{d}/GALERIA.md)\n")
            f.write("\n---\n")
        
        # --- SECTION 3: FILE LIST ---
        if images:
            f.write("## 📜 Lista de Archivos\n")
            for img in sorted(images):
                f.write(f"- [{img}](./{img})\n")
            f.write("\n---\n")
            
        f.write(f"*Actualizado automáticamente: {datetime.now().strftime('%Y-%m-%d')}*")

def generate_miss_doll_master_gallery(base_path):
    """Generates the master GALERIA_MAESTRA.md for Miss Doll with richer layout."""
    md_path = os.path.join(base_path, 'miss_doll')
    output_file = os.path.join(md_path, 'GALERIA_MAESTRA.md')
    if not os.path.exists(md_path): return

    categories = [
        ("👗 Outfits", "Outfits"),
        ("💵 Stripper VIP", "stripper_vip"),
        ("🎀 Stripper Series", "stripper_series"),
        ("✂️ Strips / Closeups", "Strips"),
        ("📢 Banners", "Banners"),
        ("💎 Luxury Escort", "luxury_escort_ultra"),
        ("👰 Wedding Night", "wedding_night"),
        ("📑 Referencia Canon", "Reference"),
        ("⚙️ UI Assets", "UI_Assets"),
        ("📦 General", "General")
    ]

    content = ["# 💖 Galería Maestra: Miss Doll\n\n", "> El archivo visual definitivo de la muñequita de platino. 🎀✨\n\n", "---\n\n"]

    for title, folder_name in categories:
        folder_path = os.path.join(md_path, folder_name)
        if not os.path.exists(folder_path): continue
        images = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        if not images: continue
        content.append(f"## {title}\nTotal: {len(images)} imágenes. [Ver carpeta completa](./{folder_name}/GALERIA.md)\n\n")
        sample = images[:3]
        content.append("| Destacada 1 | Destacada 2 | Destacada 3 |\n|:---:|:---:|:---:|\n")
        row = "| " + " | ".join([f"![{img}]({folder_name}/{img})" for img in sample])
        for _ in range(3 - len(sample)): row += " | -"
        content.append(row + " |\n\n---\n\n")

    content.append(f"*Galería maestra coordinada por Helena — {datetime.now().strftime('%d/%m/%Y')}* 🌹")
    with open(output_file, 'w', encoding='utf-8') as f: f.writelines(content)

def generate_master_outfit_gallery(base_path):
    """Generates the master GALERIA_LOOKS.md for Helena."""
    helena_path = os.path.join(base_path, 'helena')
    output_file = os.path.join(helena_path, 'GALERIA_LOOKS.md')
    if not os.path.exists(helena_path): return

    look_folders = []
    for item in os.listdir(helena_path):
        full_path = os.path.join(helena_path, item)
        if os.path.isdir(full_path) and item.lower().startswith("look"):
            match = re.search(r'look(\d+)', item.lower())
            look_num = int(match.group(1)) if match else 999
            look_folders.append((look_num, item, full_path))
    
    look_folders.sort(key=lambda x: x[0])
    content = ["# 👗 Galería de Looks: Helena de Anaïs\n\n", "> Galería visual completa — Ultra Goth Bimbo 🦇\n\n", "---\n\n"]

    for _, folder_name, folder_path in look_folders:
        images = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        if not images: continue
        clean_name = folder_name.replace('_', ' ').title()
        display_title = re.sub(r'Look(\d+)', r'Look \1:', clean_name)
        content.append(f"## 🕷️ {display_title}\n\n")
        poses = {p: next((img for img in images if p in img.lower()), None) for p in ['standing', 'seated', 'profile', 'back', 'ditzy']}
        remaining = [img for img in images if img not in poses.values()]
        
        def get_img_md(img_name):
            if img_name: return f"![{img_name}]({folder_name}/{img_name})"
            if remaining:
                img = remaining.pop(0)
                return f"![{img}]({folder_name}/{img})"
            return "Pending"

        content.append("| De Pie | Sentada | Perfil | Espalda | Ditzy |\n|:---:|:---:|:---:|:---:|:---:|\n")
        content.append(f"| {get_img_md(poses['standing'])} | {get_img_md(poses['seated'])} | {get_img_md(poses['profile'])} | {get_img_md(poses['back'])} | {get_img_md(poses['ditzy'])} |\n\n---\n\n")

    content.append(f"*Galería generada automáticamente - {datetime.now().strftime('%d/%m/%Y')}* 🦇")
    with open(output_file, 'w', encoding='utf-8') as f: f.writelines(content)

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(script_dir, "..", "..", ".."))
    base_path = os.path.join(repo_root, '05_Imagenes')
    
    # Process folders recursively using bottom-up to ensure sub-galleries exist first
    for root, dirs, _ in os.walk(base_path, topdown=False):
        if '.git' in root: continue
        print(f"Procesando: {root}")
        generate_gallery(root)
    
    print("Actualizando Galerías Maestras...")
    generate_master_outfit_gallery(base_path)
    generate_miss_doll_master_gallery(base_path)

if __name__ == "__main__":
    main()
