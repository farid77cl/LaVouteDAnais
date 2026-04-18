import os
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

old_commit = "f8731e96"
head_commit = "HEAD"
path = "05_Imagenes/ele"

old_files = get_git_files(old_commit, path)
head_files = get_git_files(head_commit, path)

# Map old folders to files
old_folders = defaultdict(list)
for f in old_files:
    if f.endswith('.png') or f.endswith('.jpg'):
        parts = f.split('/')
        if len(parts) > 3:
            folder = parts[2]
            old_folders[folder].append(f)

# Map current folders to files
head_folders = defaultdict(list)
for f in head_files:
    if f.endswith('.png') or f.endswith('.jpg'):
        parts = f.split('/')
        if len(parts) > 3:
            folder = parts[2]
            head_folders[folder].append(f)

print("--- AUDIT OF LOOK REORGANIZATION ---")

# Find duplicates in current (HEAD) folders based on look number
look_pattern = re.compile(r'look(\d+)', re.IGNORECASE)
ele_path = r'C:\Users\farid\LaVouteDAnais\05_Imagenes\ele'
current_folders = [f for f in os.listdir(ele_path) if os.path.isdir(os.path.join(ele_path, f))]

look_to_folders = defaultdict(list)
for f in current_folders:
    m = look_pattern.match(f)
    if m:
        num = int(m.group(1))
        # Correct to 3-digit normalization for mapping
        look_to_folders[num].append(f)

duplicates = {k: v for k, v in look_to_folders.items() if len(v) > 1}
if duplicates:
    print("\n[!] DUPLICATE FOLDERS FOUND IN HEAD:")
    for num, folders in duplicates.items():
        print(f"  Look {num:03d}: {folders}")

# Find missing images
missing_assets = []
for old_folder, files in old_folders.items():
    m = look_pattern.match(old_folder)
    if m:
        num = int(m.group(1))
        targets = look_to_folders.get(num, [])
        if targets:
            # Preferred target is the one with the longest name (usually has description)
            target_folder = max(targets, key=len)
            for f in files:
                filename = f.split('/')[-1]
                expected_path = f"05_Imagenes/ele/{target_folder}/{filename}"
                if expected_path not in head_files:
                    missing_assets.append((f, expected_path))
        else:
            print(f"  [!] No target folder found for look {num:03d} (Old: {old_folder})")

print(f"\nTotal assets missing in descriptive folders: {len(missing_assets)}")
if missing_assets:
    print("Example missing mappings (First 5):")
    for old, new in missing_assets[:5]:
        print(f"  {old} -> {new}")

# Check for files in "Looks_Archives" that should be in specific look folders
archive_files = [f for f in head_files if "Looks_Archives" in f and (f.endswith('.png') or f.endswith('.jpg'))]
print(f"\nAssets currently in Archives in HEAD: {len(archive_files)}")

with open('scratch/reorganization_data.txt', 'w', encoding='utf-8') as out:
    out.write("MISSING_MAPPINGS:\n")
    for old, new in missing_assets:
        out.write(f"{old}|{new}\n")
    out.write("\nDUPLICATES:\n")
    for num, folders in duplicates.items():
        out.write(f"{num:03d}|{','.join(folders)}\n")
    out.write("\nARCHIVE_ASSETS:\n")
    for f in archive_files:
        out.write(f"{f}\n")
