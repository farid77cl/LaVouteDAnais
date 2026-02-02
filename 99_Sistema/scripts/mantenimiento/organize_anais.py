import os
import re
import shutil

TARGET_DIR = r"C:\Users\fabara\LaVouteDAnais\05_Imagenes\anais"
DRY_RUN = False  # EXECUTE

def clean_name(name):
    name = re.sub(r'_\d{13,}', '', name)
    return name

def get_new_name(filename, index):
    name, ext = os.path.splitext(filename)
    new_name = filename
    origin = "custom"
    char = "anais"
    theme = "general"
    desc = "image"
    
    # Pattern: anais_belland_canon... anais_canon...
    if "canon" in name or "profile" in name or "portrait" in name:
        origin = "custom"
        theme = "canon"
        parts = name.split('_')
        # Remove anais/belland/canon parts for desc
        clean_parts = [p for p in parts if p not in ["anais", "belland", "canon", "v2026"]]
        if not clean_parts: desc = "reference"
        else: desc = "_".join(clean_parts)

    # Pattern: anais_babydoll...
    elif "babydoll" in name or "bikini" in name:
        origin = "custom"
        theme = "outfit"
        parts = name.replace("anais_", "").split('_')
        if parts[-1].isdigit() and len(parts[-1]) > 10:
            parts.pop()
        desc = "_".join(parts)
        
    # Pattern: anais_... (scenes like casino, opera, paris)
    elif name.startswith("anais_"):
        origin = "custom"
        parts = name.replace("anais_", "").split('_')
        if "helena" in name:
            theme = "duo"
        else:
            theme = "scene"
            
        if parts[-1].isdigit() and len(parts[-1]) > 10:
            parts.pop()
        desc = "_".join(parts)

    else:
        origin = "custom"
        parts = name.split('_')
        if parts[-1].isdigit() and len(parts[-1]) > 10:
            parts.pop()
        desc = "_".join(parts)

    theme = theme.lower().replace(" ", "")
    desc = desc.lower().replace(" ", "_").replace("__", "_")
    
    # Remove redundant timestamps from desc if any slipped through
    desc = re.sub(r'\d{13,}', '', desc).strip('_')
    
    new_filename = f"{origin}_{char}_{theme}_s{index:03d}_{desc}{ext}"
    return new_filename, theme

def main():
    print(f"Processing directory: {TARGET_DIR}")
    files = [f for f in os.listdir(TARGET_DIR) if os.path.isfile(os.path.join(TARGET_DIR, f)) and f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    files.sort()
    
    planned_moves = []
    
    print("\n--- Processing ---")
    for i, f in enumerate(files):
        new_name, theme = get_new_name(f, i+1)
        
        subfolder = "General"
        if theme == "canon":
            subfolder = "Canon_Reference"
        elif theme == "outfit":
            subfolder = "Outfits"
        elif theme == "scene":
            subfolder = "Scenes"
        elif theme == "duo":
            subfolder = "Duos"
        
        src = os.path.join(TARGET_DIR, f)
        dst_folder = os.path.join(TARGET_DIR, subfolder)
        dst = os.path.join(dst_folder, new_name)
        
        print(f"[{subfolder}] {f} -> {new_name}")
        planned_moves.append((src, dst, dst_folder))

    if not DRY_RUN:
        print("\n--- Executing Changes ---")
        for src, dst, dst_folder in planned_moves:
            if not os.path.exists(dst_folder):
                os.makedirs(dst_folder)
            try:
                shutil.move(src, dst)
                print(f"Moved: {os.path.basename(src)} -> {os.path.basename(dst)}")
            except Exception as e:
                print(f"Error moving {src}: {e}")

if __name__ == "__main__":
    main()
