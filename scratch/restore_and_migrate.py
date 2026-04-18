import subprocess
import os
import re
import json

REPO_PATH = r"C:\Users\farid\LaVouteDAnais"
COMMIT_REF = "f8731e96"
GALLERY_PATH = os.path.join(REPO_PATH, "00_Ele", "galeria_outfits.md")

def run_git(args):
    result = subprocess.run(["git"] + args, capture_output=True, text=True, cwd=REPO_PATH)
    if result.returncode != 0:
        print(f"Error running git {' '.join(args)}: {result.stderr}")
    return result.stdout

def get_new_folders():
    ele_path = os.path.join(REPO_PATH, "05_Imagenes", "ele")
    folders = [f for f in os.listdir(ele_path) if os.path.isdir(os.path.join(ele_path, f)) and f.startswith("look")]
    mapping = {}
    for f in folders:
        m = re.match(r"look(\d+)", f)
        if m:
            mapping[int(m.group(1))] = f
    return mapping

def cleanup_pose(filename, look_id):
    # Remove metadata like timestamps and identity prefixes
    # input: helena_look1_morticia_back_view_1767312626882.png
    # output: back_view
    clean = filename.lower()
    clean = re.sub(r"^(helena|ele|look\d+|missdoll|rocio)_+", "", clean)
    clean = re.sub(r"look\d+_*", "", clean)
    clean = re.sub(r"_\d{10,}.png$", ".png", clean)
    clean = re.sub(r"\.png$", "", clean)
    # Remove suffix names if present (like morticia)
    clean = re.sub(r"^[a-z]+_", "", clean) if "_" in clean else clean
    
    # Generic pose fallback if cleanup was too aggressive
    if not clean or clean in ["v1", "v2", "v3", "v4", "v5"]:
        # Try to keep the vX if it's the only thing left
        pass
    return clean

def migrate():
    new_folder_map = get_new_folders()
    # List all files in the history commit
    files_list = run_git(["ls-tree", "-r", "--name-only", COMMIT_REF]).splitlines()
    target_files = [f for f in files_list if f.startswith("05_Imagenes/ele/look") and f.endswith(".png")]
    
    mapping_report = {}
    
    print(f"Starting restoration of {len(target_files)} files...")
    
    for old_path in target_files:
        parts = old_path.split("/")
        old_folder = parts[2]
        old_filename = parts[-1]
        
        m = re.search(r"look(\d+)", old_folder)
        if not m: continue
        look_id = int(m.group(1))
        
        if look_id not in new_folder_map:
            print(f"Warning: No new folder for Look {look_id} ({old_folder})")
            continue
            
        new_folder = new_folder_map[look_id]
        
        # Determine canonical identity
        identity = "helena" if look_id <= 92 else "ele"
        
        # Standardize name
        pose = cleanup_pose(old_filename, look_id)
        new_filename = f"{identity}_{look_id:03d}_{pose}.png"
        new_path = f"05_Imagenes/ele/{new_folder}/{new_filename}"
        
        # Perform checkout and move
        abs_old_path = os.path.join(REPO_PATH, *old_path.split("/"))
        abs_new_path = os.path.join(REPO_PATH, *new_path.split("/"))
        
        # Restore file
        run_git(["checkout", COMMIT_REF, "--", old_path])
        
        # Create target dir if missing (should exist)
        os.makedirs(os.path.dirname(abs_new_path), exist_ok=True)
        
        # Move and rename
        if os.path.exists(abs_old_path):
            if os.path.exists(abs_new_path):
                # Handle collision by adding a suffix
                base, ext = os.path.splitext(new_filename)
                counter = 2
                while os.path.exists(os.path.join(REPO_PATH, "05_Imagenes", "ele", new_folder, f"{base}_v{counter}{ext}")):
                    counter += 1
                new_filename = f"{base}_v{counter}{ext}"
                new_path = f"05_Imagenes/ele/{new_folder}/{new_filename}"
                abs_new_path = os.path.join(REPO_PATH, *new_path.split("/"))
            
            os.rename(abs_old_path, abs_new_path)
            mapping_report[old_path] = new_path
        else:
            print(f"Error: Restored file {old_path} not found on disk after checkout.")

    # Save mapping for gallery update
    with open(os.path.join(REPO_PATH, "scratch", "migration_mapping.json"), "w") as f:
        json.dump(mapping_report, f, indent=4)
    
    print(f"Migration complete. {len(mapping_report)} files processed.")

if __name__ == "__main__":
    migrate()
