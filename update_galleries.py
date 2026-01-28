import os
import re
from datetime import datetime

def generate_gallery(directory):
    files = [f for f in os.listdir(directory) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    if not files:
        return

    gallery_path = os.path.join(directory, 'GALERIA.md')
    rel_dir_name = os.path.basename(directory)
    
    with open(gallery_path, 'w', encoding='utf-8') as f:
        f.write(f"# 🖼️ Galería: {rel_dir_name}\n")
        f.write(f"Total imágenes: {len(files)}\n\n")
        
        # --- GITHUB COMPATIBILITY TABLE ---
        f.write("## 📸 Vista Previa\n\n")
        cols = 3
        # Header
        f.write("| " + " | ".join(["Imagen"] * min(len(files), cols)) + " |\n")
        f.write("| " + " | ".join([":---:"] * min(len(files), cols)) + " |\n")
        
        for i in range(0, len(files), cols):
            chunk = files[i:i+cols]
            # GitHub needs relative paths to work in the web view
            row = "| " + " | ".join([f"![{img}](./{img})" for img in chunk]) + " |\n"
            f.write(row)
        f.write("\n\n---\n\n")

        # --- ASSISTANT CAROUSEL ---
        if len(files) > 0:
            f.write("## 🎡 Carrusel Interactivo\n\n")
            f.write("````carousel\n")
            for i, img in enumerate(files):
                f.write(f"![{img}](./{img})\n")
                if i < len(files) - 1:
                    f.write("<!-- slide -->\n")
            f.write("````\n\n")
        
        f.write("## 📜 Lista de Archivos\n")
        sorted_files = sorted(files)
        for img in sorted_files:
            f.write(f"- [{img}](./{img})\n")
            
        f.write(f"\n---\n*Actualizado automáticamente: {datetime.now().strftime('%Y-%m-%d')}*")

def generate_master_outfit_gallery(base_path):
    """Generates the master GALERIA_LOOKS.md for Helena's outfits."""
    helena_path = os.path.join(base_path, 'helena')
    output_file = os.path.join(helena_path, 'GALERIA_LOOKS.md')
    
    if not os.path.exists(helena_path):
        return

    # Scan for look folders
    look_folders = []
    for item in os.listdir(helena_path):
        full_path = os.path.join(helena_path, item)
        if os.path.isdir(full_path) and item.lower().startswith("look"):
            # Extract look number for sorting
            match = re.search(r'look(\d+)', item.lower())
            look_num = int(match.group(1)) if match else 999
            look_folders.append((look_num, item, full_path))
    
    # Sort folders by look number
    look_folders.sort(key=lambda x: x[0])

    content = []
    content.append("# 👗 Galería de Looks: Helena de Anaïs\n\n")
    content.append("> Galería visual completa — Ultra Goth Bimbo 🦇\n\n")
    content.append("---\n\n")

    for look_num, folder_name, folder_path in look_folders:
        images = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        if not images:
            continue
            
        # Try to format the title nicely (replace underscores)
        # e.g. look45_midnight_secretary -> Look 45: Midnight Secretary
        clean_name = folder_name.replace('_', ' ').title()
        # Ensure look number format
        display_title = re.sub(r'Look(\d+)', r'Look \1:', clean_name)
        
        content.append(f"## 🕷️ {display_title}\n\n")
        
        # Identify poses
        standing = next((img for img in images if 'standing' in img.lower() or 'hero' in img.lower()), None)
        seated = next((img for img in images if 'seated' in img.lower() or 'desk' in img.lower()), None)
        profile = next((img for img in images if 'profile' in img.lower() or 'side' in img.lower()), None)
        back = next((img for img in images if 'back' in img.lower()), None)
        ditzy = next((img for img in images if 'ditzy' in img.lower() or 'empty' in img.lower()), None)
        
        # If specific poses aren't found, fill with available images in order
        remaining = [img for img in images if img not in [standing, seated, profile, back, ditzy]]
        
        def get_img_md(img_name):
            if img_name:
                return f"![{img_name}]({folder_name}/{img_name})"
            elif remaining:
                img = remaining.pop(0)
                return f"![{img}]({folder_name}/{img})"
            return "Pending"

        content.append("| De Pie | Sentada | Perfil | Espalda | Ditzy |\n")
        content.append("|:---:|:---:|:---:|:---:|:---:|\n")
        content.append(f"| {get_img_md(standing)} | {get_img_md(seated)} | {get_img_md(profile)} | {get_img_md(back)} | {get_img_md(ditzy)} |\n\n")
        content.append("---\n\n")

    content.append(f"*Galería generada automáticamente - {datetime.now().strftime('%d/%m/%Y')}* 🦇")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(content)
    print(f"Master Gallery Updated: {output_file}")

def main():
    base_path = r'C:\Users\fabara\LaVouteDAnais\05_Imagenes'
    
    # 1. Update individual folder galleries
    for root, dirs, files in os.walk(base_path):
        if '.git' in root:
            continue
        print(f"Procesando: {root}")
        generate_gallery(root)
    
    # 2. Update Master Outfit Gallery
    print("Generando Master Outfit Gallery...")
    generate_master_outfit_gallery(base_path)

if __name__ == "__main__":
    main()
