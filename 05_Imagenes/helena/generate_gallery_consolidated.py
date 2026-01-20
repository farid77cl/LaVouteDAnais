import os
import re
import urllib.parse

BASE_DIR = r"C:\Users\fabara\LaVouteDAnais\05_Imagenes\helena"
OUTFITS_FILE = r"C:\Users\fabara\LaVouteDAnais\00_Helena\galeria_outfits.md"
OUTPUT_FILE = os.path.join(BASE_DIR, "GALERIA_LOOKS.md")

def get_look_id(text):
    m = re.search(r"look\s*0?(\d+)", text, re.IGNORECASE)
    return int(m.group(1)) if m else None

def parse_metadata():
    looks = {}
    with open(OUTFITS_FILE, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()
    
    # Split by look headers
    sections = re.split(r'(?=## [🖤👗🐍⚡✨💀🦇]* ?Look \d+)', content)
    
    for section in sections:
        if not section.strip():
            continue
        lines = section.strip().split('\n')
        if not lines:
            continue
        
        header = lines[0]
        look_id = get_look_id(header)
        if look_id is None:
            continue
        
        # Extract title after colon
        title = ""
        if ':' in header:
            title = header.split(':', 1)[1].strip()
        
        # Description is everything after header until --- or ### or ## or end
        desc_lines = []
        for line in lines[1:]:
            if line.strip().startswith('---') or line.strip().startswith('###') or (line.strip().startswith('## ') and 'Look' not in line):
                break
            desc_lines.append(line)
        
        looks[look_id] = {
            'title': title,
            'desc': '\n'.join(desc_lines).strip()
        }
    
    return looks

def scan_images():
    looks = {}
    for root, dirs, files in os.walk(BASE_DIR):
        for f in files:
            if f.lower().endswith(('.png', '.jpg', '.jpeg')):
                folder_name = os.path.basename(root)
                look_id = get_look_id(f) or get_look_id(folder_name)
                
                if look_id:
                    if look_id not in looks:
                        looks[look_id] = []
                    
                    rel_path = os.path.relpath(os.path.join(root, f), BASE_DIR).replace("\\", "/")
                    looks[look_id].append({
                        'name': f,
                        'path': urllib.parse.quote(rel_path)
                    })
    return looks

def generate():
    meta = parse_metadata()
    imgs = scan_images()
    
    # Build the markdown content as a single string
    md = """# 👗 Galería de Looks: Helena de Anaïs

> Galería curada de vestuarios canónicos.

---

"""
    
    for look_id in sorted(imgs.keys()):
        look_imgs = sorted(imgs[look_id], key=lambda x: x['name'])
        look_meta = meta.get(look_id, {'title': '', 'desc': ''})
        
        title = f": {look_meta['title']}" if look_meta['title'] else ""
        md += f"## Look {look_id}{title}\n\n"
        
        # Description as blockquote
        if look_meta['desc']:
            for line in look_meta['desc'].split('\n'):
                line = line.strip()
                if line:
                    md += f"> {line}\n"
                else:
                    md += ">\n"
            md += "\n"
        
        # Image table - 2 columns like the test
        md += "| Imagen | Imagen |\n"
        md += "|:---:|:---:|\n"
        
        for i in range(0, len(look_imgs), 2):
            row = "|"
            for j in range(2):
                if i + j < len(look_imgs):
                    img = look_imgs[i + j]
                    row += f" ![]({img['path']}) |"
                else:
                    row += " |"
            md += row + "\n"
        
        md += "\n---\n\n"
    
    md += "*Generado por Helena v2026*\n"
    
    # Write with Unix LF line endings (not Windows CRLF)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline='\n') as f:
        f.write(md)
    
    print(f"Gallery generated: {len(imgs)} looks")

if __name__ == "__main__":
    generate()
