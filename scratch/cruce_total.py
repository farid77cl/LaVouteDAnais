import subprocess
import re
from collections import defaultdict

def get_git_files(commit, path):
    result = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", commit, path],
        capture_output=True, text=True, cwd=r"C:\Users\farid\LaVouteDAnais"
    )
    if result.returncode != 0:
        return []
    return result.stdout.strip().split('\n')

def get_looks_from_md(path):
    looks = set()
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            matches = re.findall(r'## .*?Look (\d+)', content)
            for m in matches:
                looks.add(int(m))
    except:
        pass
    return looks

galeria_path = r'C:\Users\farid\LaVouteDAnais\00_Ele\galeria_outfits.md'
galeria_gotica_path = r'C:\Users\farid\LaVouteDAnais\00_Ele\galeria_outfits_era_gotica.md'
ele_base_path = "05_Imagenes/ele"

md_looks = get_looks_from_md(galeria_path)
md_looks.update(get_looks_from_md(galeria_gotica_path))

# Get all files in Git for the ele directory
all_git_files = get_git_files("HEAD", ele_base_path)

# Track physical (git-tracked) folders and their images
physical_looks = defaultdict(list)
look_pattern = re.compile(r'look(\d+)', re.IGNORECASE)

for f in all_git_files:
    parts = f.split('/')
    if len(parts) > 2:
        folder_name = parts[2]
        m = look_pattern.match(folder_name)
        if m:
            num = int(m.group(1))
            if f.endswith('.png') or f.endswith('.jpg'):
                physical_looks[num].append(f)
            # Ensure the look key exists even if no images yet
            if num not in physical_looks:
                physical_looks[num] = []

print("--- REPORTE DE CRUCE GIT-HEAD (AUDITORÍA TOTAL) ---")
print(f"Total Looks en Markdown: {len(md_looks)}")
print(f"Total Looks con carpeta/archivos en Git: {len(physical_looks)}")

missing_folders = sorted([l for l in md_looks if l not in physical_looks])
orphaned_folders = sorted([l for l in physical_looks if l not in md_looks])
empty_folders = sorted([l for l, files in physical_looks.items() if not files])

print(f"\nLooks en MD sin NADA en Git ({len(missing_folders)}):")
if missing_folders:
    print(missing_folders)

print(f"\nCarpetas en Git sin entrada en MD ({len(orphaned_folders)}):")
if orphaned_folders:
    # Just print look numbers for brevity
    print(orphaned_folders)

print(f"\nLooks con carpeta en Git pero SIN IMÁGENES ({len(empty_folders)}):")
if empty_folders:
    print(empty_folders)

# Save detailed results
with open('scratch/cruce_total_report.txt', 'w', encoding='utf-8') as out:
    out.write("MISSING_IN_GIT:\n")
    out.write(f"{missing_folders}\n")
    out.write("\nORPHANED_IN_GIT:\n")
    out.write(f"{orphaned_folders}\n")
    out.write("\nEMPTY_LOOKS_IN_GIT:\n")
    out.write(f"{empty_folders}\n")
