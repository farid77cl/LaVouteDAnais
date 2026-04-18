import os
import subprocess
import re

def git_show_to_file(commit, old_path, new_path):
    # Ensure directory exists
    os.makedirs(os.path.dirname(new_path), exist_ok=True)
    
    # Run git show
    try:
        # We use stdout redirection to handle binary data
        with open(new_path, 'wb') as f:
            subprocess.run(["git", "show", f"{commit}:{old_path}"], stdout=f, check=True)
        return True
    except Exception as e:
        print(f"Error restoring {old_path}: {e}")
        return False

def extract_pose(filename):
    # Common poses: standing, seated, back, profile, ditzy, portrait, detail, sitting, selfie, frontal, hero
    poses = ['standing', 'seated', 'back', 'profile', 'ditzy', 'portrait', 'detail', 'sitting', 'selfie', 'frontal', 'hero']
    for pose in poses:
        if pose in filename.lower():
            return pose
    return "unknown"

mapping_file = r'C:\Users\farid\LaVouteDAnais\scratch\reorganization_data.txt'
repo_root = r'C:\Users\farid\LaVouteDAnais'
old_commit = "f8731e96"

if not os.path.exists(mapping_file):
    print("Mapping file not found.")
    exit(1)

with open(mapping_file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

is_missing_section = False
restored_count = 0

for line in lines:
    line = line.strip()
    if line == "MISSING_MAPPINGS:":
        is_missing_section = True
        continue
    if not line or line == "DUPLICATES:":
        is_missing_section = False
        continue
    
    if is_missing_section and "|" in line:
        old_path, new_path_raw = line.split('|')
        
        # Determine new filename standard
        # 05_Imagenes/ele/look031_industrial_siren/helena_look031_standing.png
        match = re.search(r'look(\d+)', new_path_raw)
        if match:
            look_num = int(match.group(1))
            prefix = "helena" if look_num <= 84 else "ele"
            pose = extract_pose(os.path.basename(old_path))
            
            # Format: {prefix}_{0XX}_{pose}.png
            new_filename = f"{prefix}_{look_num:03d}_{pose}.png"
            new_path = os.path.join(os.path.dirname(os.path.join(repo_root, new_path_raw)), new_filename)
            
            # If standard naming fails to unique (same pose multiple times), add counter
            if os.path.exists(new_path):
                counter = 1
                while os.path.exists(new_path):
                    new_filename = f"{prefix}_{look_num:03d}_{pose}_{counter}.png"
                    new_path = os.path.join(os.path.dirname(os.path.join(repo_root, new_path_raw)), new_filename)
                    counter += 1
            
            print(f"Restoring: {old_path} -> {new_path}")
            if git_show_to_file(old_commit, old_path, new_path):
                restored_count += 1

print(f"\nSuccessfully restored {restored_count} assets.")
