import os
import re

dir_path = r'C:\Users\farid\LaVouteDAnais\05_Imagenes\ele'
folders = [f for f in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, f))]

# 1. Check for 2-digit look folders (e.g. look01)
two_digit_pattern = re.compile(r'look\d{2}(_|$)', re.IGNORECASE)
two_digit_folders = [f for f in folders if two_digit_pattern.match(f)]

# 2. Check for 3-digit folders that are empty (likely targets of a failed move)
empty_target_folders = []
for folder in folders:
    if re.match(r'look\d{3}', folder):
        full_path = os.path.join(dir_path, folder)
        # Check if it has any images (.png, .jpg)
        has_images = any(f.endswith('.png') or f.endswith('.jpg') for f in os.listdir(full_path))
        if not has_images:
            empty_target_folders.append(folder)

# 3. Check for folders that ARE digits only (as user mentioned 0xx)
digit_folders = [f for f in folders if re.match(r'^\d{2,3}$', f)]

print("--- AUDIT RESULTS ---")
print(f"2-digit folders: {two_digit_folders}")
print(f"Digit-only folders: {digit_folders}")
print(f"Empty 3-digit folders: {len(empty_target_folders)}")
if empty_target_folders:
    print(f"First 10 empty: {empty_target_folders[:10]}")

# 4. Check for duplicates in Looks_Archives
archive_path = os.path.join(dir_path, 'Looks_Archives', 'ERA_GOTICA')
if os.path.exists(archive_path):
    archive_folders = os.listdir(archive_path)
    print(f"Folders in ERA_GOTICA archive: {len(archive_folders)}")
