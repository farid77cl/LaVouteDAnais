
import os
import re
import urllib.parse
import sys

# Forces UTF-8 for stdout
sys.stdout.reconfigure(encoding='utf-8')

# Configuration
BASE_DIR = r"C:\Users\fabara\LaVouteDAnais\05_Imagenes\helena"
OUTFITS_FILE = r"C:\Users\fabara\LaVouteDAnais\00_Helena\galeria_outfits.md"
OUTPUT_FILE = os.path.join(BASE_DIR, "GALERIA_LOOKS.md")

def fix_mojibake(text):
    if not text:
        return text
    try:
        # Common fix for UTF-8 misinterpretation: Encode to Windows-1252 (Latin-1 variant) and decode back to UTF-8
        return text.encode('cp1252').decode('utf-8')
    except:
        return text

def get_look_id(line):
    # Strictly matches Look followed by numbers, allows helena_lookXX or lookXX
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
            
            # Look Header Detection
            if stripped.startswith("## ") and "Look" in stripped:
                look_id = get_look_id(stripped)
                if look_id is not None:
                    # Save previous look buffer
                    if current_look is not None:
                        looks_metadata[current_look]['desc'] = "".join(buffer).strip()
                    
                    current_look = look_id
                    buffer = []
                    
                    # Title extraction
                    if ':' in stripped:
                        title_part = stripped.split(':', 1)[1].strip()
                        looks_metadata[current_look] = {'title': fix_mojibake(title_part)}
                    else:
                        looks_metadata[current_look] = {'title': fix_mojibake(stripped.replace('#', '').strip())}
                    continue
            
            if current_look is not None:
                # End of look section detection
                if stripped.startswith("---") or (stripped.startswith("## ") and "Look" not in stripped):
                    looks_metadata[current_look]['desc'] = "".join(buffer).strip()
                    current_look = None
                    buffer = []
                else:
                    buffer.append(fix_mojibake(line))
                    
        # Final buffer save
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
                # Filter specifically for look-related files
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

    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="\n") as f:
        # 1. Main Header
        f.write("# 👗 Galería de Looks: La Voûte de Helena\n\n")
        f.write("> *Galería curada de vestuarios canónicos de Helena.*\n\n")
        f.write("---\n\n")

        for look_id in sorted_ids:
            look_imgs = sorted(images[look_id], key=lambda x: x['name'])
            look_meta = metadata.get(look_id, {'title': '', 'desc': ''})
            
            title = f": {look_meta['title']}" if look_meta['title'] else ""
            f.write(f"## 👗 Look {look_id}{title}\n\n")
            
            # 2. Description Block
            if look_meta['desc']:
                desc_lines = look_meta['desc'].split('\n')
                for line in desc_lines:
                    l = line.strip()
                    if l:
                        f.write(f"> {l}  \n") # Double space for Markdown breaks
                    else:
                        f.write(">  \n")
                f.write("\n") # Close blockquote

            # 3. Image Table
            f.write("| | | |\n")
            f.write("|:---:|:---:|:---:|\n")
            
            for i in range(0, len(look_imgs), 3):
                chunk = look_imgs[i:i+3]
                row = "|"
                for item in chunk:
                    row += f" ![]({item['path']})<br>`{item['name']}` |"
                
                # Fill balance
                while len(chunk) < 3:
                    row += " |"
                    chunk.append(None)
                
                f.write(row + "\n")
            
            f.write("\n---\n\n")

        f.write("*Generado automáticamente por Helena v2026*\n")

if __name__ == "__main__":
    generate_gallery()
    print(f"Success! Gallery saved to: {OUTPUT_FILE}")
