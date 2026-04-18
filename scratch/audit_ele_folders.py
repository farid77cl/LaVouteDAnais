import os
import re

dir_path = r'C:\Users\farid\LaVouteDAnais\05_Imagenes\ele'
folders = [f for f in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, f))]

look_pattern = re.compile(r'look(\d{3})', re.IGNORECASE)
look_map = {}

for folder in folders:
    match = look_pattern.search(folder)
    if match:
        look_num = match.group(1)
        if look_num not in look_map:
            look_map[look_num] = []
        look_map[look_num].append(folder)

duplicates = {k: v for k, v in look_map.items() if len(v) > 1}

if duplicates:
    print("Duplicate Look Numbers found:")
    for k, v in duplicates.items():
        print(f"Look {k}: {v}")
else:
    print("No obvious duplicate look numbers found in folder names.")

# Also check for folders that are just digits
digit_folders = [f for f in folders if re.match(r'^\d{3}$', f)]
if digit_folders:
    print("\n folders named as digits found:")
    print(digit_folders)
else:
    print("\nNo folders named as 3 digits found.")

# Check for empty folders
print("\nChecking for empty folders in Ele...")
for folder in folders:
    full_path = os.path.join(dir_path, folder)
    if not os.listdir(full_path):
        print(f"Empty folder: {folder}")
