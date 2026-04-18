import os
import re

galeria_path = r'C:\Users\farid\LaVouteDAnais\00_Ele\galeria_outfits.md'
galeria_gotica_path = r'C:\Users\farid\LaVouteDAnais\00_Ele\galeria_outfits_era_gotica.md'
ele_path = r'C:\Users\farid\LaVouteDAnais\05_Imagenes\ele'

def get_looks_from_md(path):
    looks = set()
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        matches = re.findall(r'## .*?Look (\d+)', content)
        for m in matches:
            looks.add(int(m))
    return looks

md_looks = get_looks_from_md(galeria_path)
md_looks.update(get_looks_from_md(galeria_gotica_path))

physical_folders = os.listdir(ele_path)
look_pattern = re.compile(r'look(\d+)', re.IGNORECASE)

physical_looks = {}
for f in physical_folders:
    m = look_pattern.match(f)
    if m:
        num = int(m.group(1))
        physical_looks[num] = f

missing_folders = sorted([l for l in md_looks if l not in physical_looks])
orphaned_folders = sorted([l for l in physical_looks if l not in md_looks])

print("--- REPORTE DE CRUCE (AUDITORÍA GALERÍA) ---")
print(f"Total Looks en Markdown: {len(md_looks)}")
print(f"Total Carpetas de Looks Físicas: {len(physical_looks)}")

print(f"\nLooks en MD sin carpeta física ({len(missing_folders)}):")
if missing_folders:
    # Print first 20 for brevity
    print(missing_folders[:20])

print(f"\nCarpetas físicas sin entrada en MD ({len(orphaned_folders)}):")
if orphaned_folders:
    for l in orphaned_folders[:10]:
        print(f"  {physical_looks[l]}")

# Check for empty folders
empty_folders = []
for l, folder in physical_looks.items():
    full_path = os.path.join(ele_path, folder)
    if not os.listdir(full_path) or (len(os.listdir(full_path)) == 1 and os.listdir(full_path)[0] == 'README.md'):
        empty_folders.append(folder)

print(f"\nCarpetas de looks vacías o solo con README ({len(empty_folders)}):")
if empty_folders:
    print(empty_folders[:10])

with open('scratch/cruce_report.txt', 'w', encoding='utf-8') as out:
    out.write(f"MISSING_FOLDERS: {missing_folders}\n")
    out.write(f"ORPHANED_FOLDERS: {orphaned_folders}\n")
    out.write(f"EMPTY_FOLDERS: {empty_folders}\n")
