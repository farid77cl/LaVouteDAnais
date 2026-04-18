import os
import shutil
import re

REPO_PATH = r"C:\Users\farid\LaVouteDAnais"
ELE_PATH = os.path.join(REPO_PATH, "05_Imagenes", "ele")

def cleanup():
    if not os.path.exists(ELE_PATH):
        print("Path not found.")
        return

    folders = os.listdir(ELE_PATH)
    look_folders = {}
    
    # Identify folders by Look ID
    for f in folders:
        if not os.path.isdir(os.path.join(ELE_PATH, f)): continue
        m = re.match(r"look(\d+)", f)
        if m:
            look_id = int(m.group(1))
            if look_id not in look_folders:
                look_folders[look_id] = []
            look_folders[look_id].append(f)

    # Resolve duplicates
    for look_id, names in look_folders.items():
        if len(names) > 1:
            # Prefer the one with 3-digit padding (look0XX)
            canonical = None
            for n in names:
                if re.match(r"look\d{3}", n):
                    canonical = n
                    break
            
            if not canonical:
                # If neither is 3-digit, pick one but this shouldn't happen now
                canonical = sorted(names)[0] # e.g. look10
            
            print(f"Look {look_id}: Merging {names} into {canonical}")
            
            target_dir = os.path.join(ELE_PATH, canonical)
            for n in names:
                if n == canonical: continue
                source_dir = os.path.join(ELE_PATH, n)
                
                # Move files
                for item in os.listdir(source_dir):
                    s_item = os.path.join(source_dir, item)
                    d_item = os.path.join(target_dir, item)
                    if os.path.exists(d_item):
                        # Collision: rename or skip
                        base, ext = os.path.splitext(item)
                        d_item = os.path.join(target_dir, f"{base}_collided{ext}")
                    
                    shutil.move(s_item, d_item)
                
                # Remove empty dir
                try:
                    os.rmdir(source_dir)
                    print(f" Removed obsolete folder: {n}")
                except OSError:
                    print(f" Warning: Could not remove folder {n} (not empty?)")

if __name__ == "__main__":
    cleanup()
