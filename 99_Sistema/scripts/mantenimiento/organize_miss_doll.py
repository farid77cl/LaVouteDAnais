import os
import re
import shutil

TARGET_DIR = r"C:\Users\fabara\LaVouteDAnais\05_Imagenes\miss_doll"
DRY_RUN = False  # EXECUTE

def clean_name(name):
    name = re.sub(r'_\d{13,}', '', name)
    return name

def get_new_name(filename, index):
    name, ext = os.path.splitext(filename)
    new_name = filename
    origin = "custom"
    char = "missdoll"
    theme = "general"
    desc = "image"
    
    # Pattern: md_banner... or md_strip...
    if name.startswith("md_banner") or name.startswith("md_strip"):
        origin = "story"
        theme = "comic" if "comic" in name else "real"
        if "strip" in name: theme = "strip"
        
        parts = name.split('_')
        clean_parts = [p for p in parts if not p.isdigit() and len(p) < 13]
        for rem in ["md", "banner", "comic", "real", "strip"]:
            if rem in clean_parts:
                clean_parts.remove(rem)
        desc = "_".join(clean_parts)
        if not desc: desc = "asset"
        
    # Pattern: miss_doll_...
    elif name.startswith("miss_doll"):
        origin = "custom"
        theme = "outfit"
        parts = name.replace("miss_doll_", "").split('_')
        if parts[-1].isdigit() and len(parts[-1]) > 10:
            parts.pop()
            
        if parts:
            first = parts[0]
            if first in ["babydoll", "latex", "bunny", "black", "pink", "red", "white", "lingerie"]:
                theme = "outfit"
            elif first in ["bob", "hair"]:
                theme = "hair"
            elif first in ["face", "canon", "makeup"]:
                theme = "face"
            else:
                theme = "general"
            desc = "_".join(parts)
    
    # Pattern: Separators/UI
    elif name.startswith("separator") or name.startswith("thin_separator"):
        origin = "ui"
        theme = "asset"
        desc = name.replace("separator_", "")
        
    else:
        origin = "custom"
        parts = name.split('_')
        if parts[-1].isdigit() and len(parts[-1]) > 10:
            parts.pop()
        desc = "_".join(parts)

    theme = theme.lower().replace(" ", "")
    desc = desc.lower().replace(" ", "_")
    
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
        if theme in ["comic", "real"]:
            subfolder = "Banners"
        elif theme == "strip":
            subfolder = "Strips"
        elif theme == "outfit":
            subfolder = "Outfits"
        elif theme in ["hair", "face"]:
            subfolder = "Reference"
        elif theme == "asset":
            subfolder = "UI_Assets"
        
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
    else:
        print("\n[DRY RUN] No changes made. Set DRY_RUN = False to execute.")

if __name__ == "__main__":
    main()
