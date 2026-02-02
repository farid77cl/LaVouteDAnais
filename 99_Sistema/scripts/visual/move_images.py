import os
import shutil
import glob

source_dir = r"C:\Users\fabara\.gemini\antigravity\brain\3232ec5b-8f5f-4658-93ab-20e96eb44e5e"
dest_dir = r"C:\Users\fabara\LaVouteDAnais\05_Imagenes\miss_doll\stripper_series"
gallery_file = os.path.join(dest_dir, "GALERIA.md")

# Ensure destination directory exists
os.makedirs(dest_dir, exist_ok=True)

# Pattern to find the new images
pattern = os.path.join(source_dir, "miss_doll_stripper_*.png")
files_to_move = glob.glob(pattern)

moved_files = []

print(f"Encontrados {len(files_to_move)} archivos para mover.")

for file_path in files_to_move:
    filename = os.path.basename(file_path)
    dest_path = os.path.join(dest_dir, filename)
    
    try:
        shutil.move(file_path, dest_path)
        moved_files.append(filename)
        print(f"Movido: {filename}")
    except Exception as e:
        print(f"Error moviendo {filename}: {e}")

# Update GALERIA.md
if moved_files:
    try:
        with open(gallery_file, 'a', encoding='utf-8') as f:
            f.write("\n\n### Nuevas Adiciones (Stripper Series v2 - No Corset)\n\n")
            f.write("````carousel\n")
            for i, filename in enumerate(moved_files):
                f.write(f"![{filename}](file:///{dest_dir.replace(os.sep, '/')}/{filename})\n")
                if i < len(moved_files) - 1:
                    f.write("<!-- slide -->\n")
            f.write("````\n")
        print("GALERIA.md actualizado.")
    except Exception as e:
        print(f"Error actualizando GALERIA.md: {e}")
else:
    print("No se movieron archivos, no se actualizó la galería.")
