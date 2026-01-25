import os

def generate_gallery(directory):
    files = [f for f in os.listdir(directory) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    if not files:
        return

    gallery_path = os.path.join(directory, 'GALERIA.md')
    rel_dir_name = os.path.basename(directory)
    
    with open(gallery_path, 'w', encoding='utf-8') as f:
        f.write(f"# 🖼️ Galería: {rel_dir_name}\n")
        f.write(f"Total imágenes: {len(files)}\n\n")
        
        if len(files) > 3:
            f.write("````carousel\n")
            for i, img in enumerate(files):
                f.write(f"![{img}](./{img})\n")
                if i < len(files) - 1:
                    f.write("<!-- slide -->\n")
            f.write("````\n\n")
        
        f.write("## 📜 Lista de Archivos\n")
        for img in files:
            f.write(f"- [{img}](./{img})\n")
            
        f.write(f"\n---\n*Actualizado automáticamente: 2026-01-25*")

def main():
    base_path = r'C:\Users\fabara\LaVouteDAnais\05_Imagenes'
    for root, dirs, files in os.walk(base_path):
        # Evitar carpetas ocultas o de sistema si las hubiera
        if '.git' in root:
            continue
        print(f"Procesando: {root}")
        generate_gallery(root)

if __name__ == "__main__":
    main()
