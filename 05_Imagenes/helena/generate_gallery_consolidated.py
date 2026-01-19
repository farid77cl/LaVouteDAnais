
import os
import re
import urllib.parse
import sys

# Forces UTF-8 for stdout
sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"C:\Users\fabara\LaVouteDAnais\05_Imagenes\helena"
outfits_file = r"C:\Users\fabara\LaVouteDAnais\00_Helena\galeria_outfits.md"
output_file = os.path.join(base_dir, "GALERIA_LOOKS.md")

def fix_mojibake(text):
    if not text:
        return text
    try:
        # Common fix for UTF-8 misinterpretation: Encode to Windows-1252 (Latin-1 variant) and decode back to UTF-8
        # The file shows 'Ã¡' which is utf-8 bytes for 'á' seen as latin1.
        return text.encode('cp1252').decode('utf-8')
    except:
        # If it fails, return original
        return text

def get_look_id(line):
    # Strictly matches Look followed by numbers, allows helena_lookXX or lookXX
    m = re.search(r"look\s*0?(\d+)", line, re.IGNORECASE)
    if m:
        return int(m.group(1))
    return None

looks_metadata = {}

# 1. Parse Metadata with Encoding Fix
try:
    with open(outfits_file, "r", encoding="utf-8", errors="replace") as f:
        lines = f.readlines()
        
    current_look = None
    buffer = []
    
    for line in lines:
        stripped = line.strip()
        
        if stripped.startswith("## ") and "Look" in stripped:
            look_id = get_look_id(stripped)
            if look_id is not None:
                if current_look is not None:
                    looks_metadata[current_look]['desc_lines'] = buffer
                
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
            if stripped.startswith("---") or (stripped.startswith("## ") and "Look" not in stripped):
                looks_metadata[current_look]['desc_lines'] = buffer
                current_look = None
                buffer = []
            else:
                # Store line with mojibake fix immediately
                buffer.append(fix_mojibake(line))
                
    if current_look is not None:
        looks_metadata[current_look]['desc_lines'] = buffer

except Exception as e:
    print(f"Error reading metadata: {e}")

# Process descriptions
for lid, data in looks_metadata.items():
    raw_lines = data.get('desc_lines', [])
    # Join then strip
    full_text = "".join(raw_lines).strip()
    data['description'] = full_text

# 2. Scan Images (Strict Look Filtering)
looks_images = {}
for root, dirs, files in os.walk(base_dir):
    for filename in files:
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Only include if filename contains "look"
            if "look" in filename.lower() or "look" in os.path.basename(root).lower():
                look_num = get_look_id(filename)
                if look_num is None:
                    look_num = get_look_id(os.path.basename(root))
                
                if look_num is not None:
                    if look_num not in looks_images:
                        looks_images[look_num] = []
                    
                    full_path = os.path.join(root, filename)
                    rel_path = os.path.relpath(full_path, base_dir)
                    rel_path = rel_path.replace("\\", "/")
                    rel_path_encoded = urllib.parse.quote(rel_path)
                    
                    looks_images[look_num].append({
                        'name': filename,
                        'path': rel_path_encoded
                    })

sorted_ids = sorted(looks_images.keys())

# 3. Generate Markdown with Extra Newlines
md = "# 👗 Galería de Looks: La Voûte de Helena  \n\n"
md += "> *Galería curada de vestuarios canónicos.*  \n\n"
md += "---\n\n"

for look_id in sorted_ids:
    imgs = sorted(looks_images[look_id], key=lambda x: x['name'])
    meta = looks_metadata.get(look_id, {'title': '', 'description': ''})
    
    title_str = f": {meta['title']}" if meta['title'] else ""
    md += f"## 👗 Look {look_id}{title_str}  \n\n"
    
    if meta['description']:
        # Ensure description lines have trailing spaces for breaks
        desc_lines = meta['description'].split('\n')
        quoted_lines = [f"> {line.strip()}  " if line.strip() else ">  " for line in desc_lines]
        md += "\n".join(quoted_lines) + "\n\n"
    
    # Grid Header
    md += "| | | |\n"
    md += "|:---:|:---:|:---:|\n"
    
    # Image Rows
    for i in range(0, len(imgs), 3):
        chunk = imgs[i:i+3]
        row_imgs = "|"
        for item in chunk:
            row_imgs += f" ![]({item['path']})<br>`{item['name']}` |"
        
        while len(chunk) < 3:
            row_imgs += " |"
            chunk.append(None)
        
        md += row_imgs + "\n"
    
    md += "\n---\n\n"

md += "*Generado automáticamente por Helena v2026*  \n"

# Write with standard newline handling
with open(output_file, "w", encoding="utf-8") as f:
    f.write(md)

print(f"Gallery V4 generated with encoding fixes. Processed {len(sorted_ids)} looks.")
