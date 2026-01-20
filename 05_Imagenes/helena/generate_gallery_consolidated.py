
import os
import re
import urllib.parse
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = r"C:\Users\fabara\LaVouteDAnais\05_Imagenes\helena"
OUTFITS_FILE = r"C:\Users\fabara\LaVouteDAnais\00_Helena\galeria_outfits.md"
OUTPUT_FILE = os.path.join(BASE_DIR, "GALERIA_LOOKS.md")

def fix_mojibake(text):
    if not text:
        return text
    try:
        return text.encode('cp1252').decode('utf-8')
    except:
        return text

def get_look_id(line):
    m = re.search(r"look\s*0?(\d+)", line, re.IGNORECASE)
    if m:
        return int(m.group(1))
    return None

def parse_metadata():
    looks_metadata = {}
    try:
        with open(OUTFITS_FILE, "r", encoding="utf-8", errors="replace") as f:
            lines = f.readlines()
        
        current_look = None
        buffer = []
        
        for line in lines:
            stripped = line.strip()
            
            if stripped.startswith("## ") and "Look" in stripped:
                look_id = get_look_id(stripped)
                if look_id is not None:
                    if current_look is not None:
                        looks_metadata[current_look]['desc'] = "".join(buffer).strip()
                    
                    current_look = look_id
                    buffer = []
                    
                    if ':' in stripped:
                        title_part = stripped.split(':', 1)[1].strip()
                        looks_metadata[current_look] = {'title': fix_mojibake(title_part)}
                    else:
                        looks_metadata[current_look] = {'title': fix_mojibake(stripped.replace('#', '').strip())}
                    continue
            
            if current_look is not None:
                if stripped.startswith("---") or (stripped.startswith("## ") and "Look" not in stripped):
                    looks_metadata[current_look]['desc'] = "".join(buffer).strip()
                    current_look = None
                    buffer = []
                else:
                    buffer.append(fix_mojibake(line))
                    
        if current_look is not None:
            looks_metadata[current_look]['desc'] = "".join(buffer).strip()

    except Exception as e:
        print(f"Error reading metadata: {e}")
    return looks_metadata

def scan_images():
    looks_images = {}
    for root, dirs, files in os.walk(BASE_DIR):
        for filename in files:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                if "look" in filename.lower() or "look" in os.path.basename(root).lower():
                    look_num = get_look_id(filename)
                    if look_num is None:
                        look_num = get_look_id(os.path.basename(root))
                    
                    if look_num is not None:
                        if look_num not in looks_images:
                            looks_images[look_num] = []
                        
                        full_path = os.path.join(root, filename)
                        rel_path = os.path.relpath(full_path, BASE_DIR)
                        rel_path = rel_path.replace("\\", "/")
                        rel_path_encoded = urllib.parse.quote(rel_path)
                        
                        looks_images[look_num].append({
                            'name': filename,
                            'path': rel_path_encoded
                        })
    return looks_images

def generate_gallery():
    metadata = parse_metadata()
    images = scan_images()
    sorted_ids = sorted(images.keys())

    print(f"Generating gallery with {len(sorted_ids)} looks...")

    # Build as a list of lines, then join with single newlines
    lines = []
    
    lines.append("# 👗 Galería de Looks: Helena de Anaïs")
    lines.append("")
    lines.append("> Galería curada de vestuarios canónicos.")
    lines.append("")
    lines.append("---")
    lines.append("")

    for look_id in sorted_ids:
        look_imgs = sorted(images[look_id], key=lambda x: x['name'])
        look_meta = metadata.get(look_id, {'title': '', 'desc': ''})
        
        title = f": {look_meta['title']}" if look_meta['title'] else ""
        lines.append(f"## 👗 Look {look_id}{title}")
        lines.append("")
        
        # Description as simple blockquote - each line prefixed with >
        if look_meta['desc']:
            desc_lines = look_meta['desc'].split('\n')
            for dl in desc_lines:
                dl_stripped = dl.strip()
                if dl_stripped:
                    lines.append(f"> {dl_stripped}")
                else:
                    lines.append(">")
            lines.append("")
        
        # Simple 3-column image grid
        lines.append("| | | |")
        lines.append("|:---:|:---:|:---:|")
        
        for i in range(0, len(look_imgs), 3):
            chunk = look_imgs[i:i+3]
            row_parts = []
            for item in chunk:
                row_parts.append(f"![]({item['path']})<br>`{item['name']}`")
            while len(row_parts) < 3:
                row_parts.append("")
            lines.append("| " + " | ".join(row_parts) + " |")
        
        lines.append("")
        lines.append("---")
        lines.append("")

    lines.append("*Generado automáticamente por Helena v2026*")

    # Write with explicit Unix line endings
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline='\n') as f:
        f.write('\n'.join(lines))

    print(f"Success! Gallery saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_gallery()
