import os
import re
import json

REPO_PATH = r"C:\Users\farid\LaVouteDAnais"
GALLERY_FILE = os.path.join(REPO_PATH, "00_Ele", "galeria_outfits.md")
GITHUB_BASE = "https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/"

def get_look_folders():
    ele_path = os.path.join(REPO_PATH, "05_Imagenes", "ele")
    folders = [f for f in os.listdir(ele_path) if os.path.isdir(os.path.join(ele_path, f)) and f.startswith("look")]
    mapping = {}
    for f in folders:
        m = re.match(r"look(\d+)", f)
        if m:
            mapping[int(m.group(1))] = f
    return mapping

def get_physical_files(look_folders):
    # Map (look_id, cleaned_pose) -> actual_filename
    files_map = {}
    for look_id, folder_name in look_folders.items():
        folder_path = os.path.join(REPO_PATH, "05_Imagenes", "ele", folder_name)
        if os.path.exists(folder_path):
            for f in os.listdir(folder_path):
                if f.endswith(".png"):
                    # Extract pose part from helena_001_pose.png
                    m = re.match(r"^(helena|ele)_\d{3}_(.*)\.png$", f)
                    if m:
                        pose = m.group(2)
                        files_map[(look_id, pose)] = f
    return files_map

def cleanup_pose(filename_part):
    # Standardize pose names for matching
    clean = filename_part.lower()
    clean = re.sub(r"^(helena|ele|look\d+|missdoll|rocio)_+", "", clean)
    clean = re.sub(r"look\d+_*", "", clean)
    clean = re.sub(r"_\d{10,}", "", clean) # timestamps
    clean = re.sub(r"\.png$", "", clean)
    # common variations
    clean = clean.replace("back_view", "back")
    clean = clean.replace("side_profile", "side")
    return clean

def smart_sync():
    look_folders = get_look_folders()
    physical_files = get_physical_files(look_folders)
    
    if not os.path.exists(GALLERY_FILE):
        print("Gallery not found.")
        return
        
    with open(GALLERY_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    new_lines = []
    total_replaced = 0
    
    # Regex to find markdown images
    # Supports both raw.github... and local relative paths
    img_regex = r"!\[(.*?)\]\((.*?)\)"
    
    for line in lines:
        matches = re.finditer(img_regex, line)
        new_line = line
        
        for m in matches:
            label = m.group(1)
            url = m.group(2)
            
            # Check if it's a look image
            if "05_Imagenes" in url and ("helena" in url or "ele" in url) and "look" in url:
                # Extract Look ID
                look_m = re.search(r"look(\d+)", url)
                if look_m:
                    look_id = int(look_m.group(1))
                    
                    # Extract filename to get pose
                    filename = url.split("/")[-1]
                    raw_pose = cleanup_pose(filename)
                    
                    # Also try to use label as pose if filename is generic (v1, v2...)
                    if raw_pose in ["v1", "v2", "v3", "v4", "v5", "standing", "seated", "back", "side", "ditzy"]:
                        pose = raw_pose
                    else:
                        pose = cleanup_pose(label) if label else raw_pose
                    
                    # Attempt to find the best match in physical restoration
                    # Normalize common poses
                    pose_variants = [pose]
                    if pose == "standing": pose_variants.extend(["standing_view", "pasarela"])
                    if pose == "back": pose_variants.extend(["back_view", "arched_back"])
                    if pose == "side": pose_variants.extend(["side_profile", "sideview"])
                    
                    match_found = False
                    for p_var in pose_variants:
                        if (look_id, p_var) in physical_files:
                            target_filename = physical_files[(look_id, p_var)]
                            target_folder = look_folders[look_id]
                            new_url = f"{GITHUB_BASE}05_Imagenes/ele/{target_folder}/{target_filename}"
                            new_line = new_line.replace(url, new_url)
                            total_replaced += 1
                            match_found = True
                            break
                    
                    if not match_found and look_id in look_folders:
                        # Fallback: Just update the folder structure if file match fails
                        target_folder = look_folders[look_id]
                        new_url = f"{GITHUB_BASE}05_Imagenes/ele/{target_folder}/{filename}"
                        
                        # Apply new standardized filename if possible
                        ident = "helena" if look_id <= 92 else "ele"
                        standard_filename = f"{ident}_{look_id:03d}_{raw_pose}.png"
                        if (look_id, raw_pose) in physical_files:
                            standard_filename = physical_files[(look_id, raw_pose)]
                        
                        new_url = f"{GITHUB_BASE}05_Imagenes/ele/{target_folder}/{standard_filename}"
                        
                        if url != new_url:
                            new_line = new_line.replace(url, new_url)
                            total_replaced += 1
                        else:
                            # Link might already be correct
                            pass

        new_lines.append(new_line)

    with open(GALLERY_FILE, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
        
    print(f"Smart sync complete. {total_replaced} gallery links updated.")

if __name__ == "__main__":
    smart_sync()
