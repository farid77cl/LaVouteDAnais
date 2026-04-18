"""Find all look folders with .png files in a given git commit."""
import subprocess
import re
from collections import defaultdict

# Get all files from the last commit before renaming (f8731e96)
result = subprocess.run(
    ["git", "ls-tree", "-r", "--name-only", "f8731e96"],
    capture_output=True, text=True, cwd=r"C:\Users\farid\LaVouteDAnais"
)

# Also get current HEAD
result_head = subprocess.run(
    ["git", "ls-tree", "-r", "--name-only", "HEAD"],
    capture_output=True, text=True, cwd=r"C:\Users\farid\LaVouteDAnais"
)

# Parse looks with PNGs from the old commit
old_looks = defaultdict(list)
for line in result.stdout.strip().split('\n'):
    if line.startswith('05_Imagenes/ele/look') and line.endswith('.png'):
        parts = line.split('/')
        folder = parts[2]  # e.g. look01_morticia
        filename = parts[-1]
        old_looks[folder].append(filename)

# Parse looks with PNGs from HEAD
head_looks = defaultdict(list)
for line in result_head.stdout.strip().split('\n'):
    if line.startswith('05_Imagenes/ele/look') and line.endswith('.png'):
        parts = line.split('/')
        folder = parts[2]
        filename = parts[-1]
        head_looks[folder].append(filename)

print("=" * 80)
print("LOOKS CON IMAGENES EN COMMIT f8731e96 (pre-renombrado)")
print("=" * 80)
for folder in sorted(old_looks.keys()):
    # Extract look number
    m = re.match(r'look(\d+)', folder)
    num = int(m.group(1)) if m else 0
    era = "HELENA (Gótica)" if num <= 84 else "ELE (V3.3)"
    print(f"\n{folder} [{era}] ({len(old_looks[folder])} imgs):")
    for f in sorted(old_looks[folder]):
        print(f"  - {f}")

print("\n" + "=" * 80)
print("LOOKS CON IMAGENES EN HEAD (post-renombrado)")
print("=" * 80)
for folder in sorted(head_looks.keys()):
    m = re.match(r'look(\d+)', folder)
    num = int(m.group(1)) if m else 0
    era = "HELENA (Gótica)" if num <= 84 else "ELE (V3.3)"
    print(f"\n{folder} [{era}] ({len(head_looks[folder])} imgs):")
    for f in sorted(head_looks[folder]):
        print(f"  - {f}")

# Find lost images (in old but not in head under new name)
print("\n" + "=" * 80)
print("ANÁLISIS DE MIGRACIÓN PENDIENTE")
print("=" * 80)

# Build mapping: old 2-digit folder -> new 3-digit folder
old_to_new = {}
for old_folder in old_looks:
    m = re.match(r'look(\d+)_(.*)', old_folder)
    if m:
        num = int(m.group(1))
        suffix = m.group(2)
        new_folder = f"look{num:03d}_{suffix}"
        old_to_new[old_folder] = new_folder
    else:
        m2 = re.match(r'look(\d+)$', old_folder)
        if m2:
            num = int(m2.group(1))
            new_folder = f"look{num:03d}"
            old_to_new[old_folder] = new_folder

lost_count = 0
lines = []
for old_folder, files in sorted(old_looks.items()):
    new_folder = old_to_new.get(old_folder, old_folder)
    head_files = head_looks.get(new_folder, [])
    missing = [f for f in files if f not in head_files]
    if missing:
        lost_count += len(missing)
        m = re.match(r'look(\d+)', old_folder)
        num = int(m.group(1)) if m else 0
        era = "HELENA" if num <= 84 else "ELE"
        lines.append(f"{old_folder} -> {new_folder} [{era}] -- {len(missing)} LOST")
        for f in sorted(missing):
            lines.append(f"  {f}")

lines.append(f"\nTOTAL LOST: {lost_count}")

with open('scratch/migration_report.txt', 'w', encoding='utf-8') as out:
    out.write('\n'.join(lines))
print(f"Report written. Total lost: {lost_count}")
