import os
import re
import shutil

TARGET_DIR = r"C:\Users\fabara\LaVouteDAnais\05_Imagenes\helena"
DRY_RUN = False  # EXECUTE

def clean_name(name):
    name = re.sub(r'_\d{13,}', '', name)
    return name

def get_new_name(filename, index):
    name, ext = os.path.splitext(filename)
    new_name = filename
    origin = "custom"
    char = "helena"
    theme = "general"
    desc = "image"
    
    # Pattern: helena_look40_... or helena_look_14enero...
    if "look" in name:
        origin = "custom"
        # Extract look number or ID
        match = re.search(r'look(\d+)', name)
        if match:
            theme = f"look{match.group(1)}"
        elif "14enero" in name:
            theme = "look_pilot"
        else:
            theme = "look_misc"
            
        parts = name.split('_')
        if parts[-1].isdigit() and len(parts[-1]) > 10:
            parts.pop()
        
        # Clean parts
        clean_parts = [p for p in parts if "look" not in p and p != "helena" and "14enero" not in p]
        desc = "_".join(clean_parts)
        if not desc: desc = "pose"

    # Pattern: helena_babydoll_... or helena_lingerie_...
    elif "babydoll" in name or "lingerie" in name or "corset" in name or "latex" in name:
        origin = "custom"
        theme = "outfit"
        parts = name.replace("helena_", "").split('_')
        if parts[-1].isdigit() and len(parts[-1]) > 10:
            parts.pop()
        desc = "_".join(parts)

    # Pattern: helena_stripper...
    elif "stripper" in name or "pole" in name:
        origin = "custom"
        theme = "action"
        desc = name.replace("helena_", "")
        if parts := desc.split('_'):
             if parts[-1].isdigit() and len(parts[-1]) > 10:
                desc = "_".join(parts[:-1])

    # Pattern: secretary_scene...
    elif name.startswith("secretary"):
        origin = "story"
        theme = "secretary_arc"
        parts = name.split('_')
        if parts[-1].isdigit() and len(parts[-1]) > 10:
            parts.pop()
        desc = "_".join(parts[1:]) # Skip 'secretary'

    # Pattern: helena_... generic
    elif name.startswith("helena_"):
        origin = "custom"
        theme = "general"
        parts = name.replace("helena_", "").split('_')
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
        if "look" in theme:
            subfolder = "Looks_Archives"
        elif theme == "outfit":
            subfolder = "Outfits"
        elif theme == "secretary_arc":
            subfolder = "Story_Arcs"
        elif theme == "action":
            subfolder = "Action_Poses"
        elif "canon" in new_name or "test" in new_name:
            subfolder = "Reference"
        
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
