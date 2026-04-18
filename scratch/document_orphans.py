import os
import re

md_path = r'C:\Users\farid\LaVouteDAnais\00_Ele\galeria_outfits_era_gotica.md'
ele_path = r'C:\Users\farid\LaVouteDAnais\05_Imagenes\ele'

orphaned_looks = [19, 20, 21, 22, 23, 24, 25, 33, 34, 61, 62, 63, 68, 76, 91, 107]

def generate_entry(look_num):
    # Find folder for this look
    target_folder = ""
    for folder in os.listdir(ele_path):
        if folder.startswith(f"look{look_num:03d}"):
            target_folder = folder
            break
    
    if not target_folder: return ""
    
    title = target_folder.split('_', 1)[1].replace('_', ' ').title() if '_' in target_folder else "Unknown Look"
    prefix = "helena" if look_num <= 84 else "ele"
    
    entry = f"\n---\n\n## 🔮 Look {look_num}: {title}\n\n"
    entry += f"*Registro restaurado quirúrgicamente*\n\n"
    entry += f"- **Ubicación:** `05_Imagenes/ele/{target_folder}/`\n\n"
    entry += f"### 📸 Imágenes\n\n"
    entry += f"| Pose | Archivo |\n"
    entry += f"|------|---------|\n"
    
    # Add image rows if they exist
    full_folder = os.path.join(ele_path, target_folder)
    for f in sorted(os.listdir(full_folder)):
        if f.endswith('.png'):
            pose = "Detail"
            for p in ['standing', 'seated', 'back', 'profile', 'ditzy', 'portrait', 'sitting', 'selfie', 'frontal']:
                if p in f.lower():
                    pose = p.title()
                    break
            url = f"https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/05_Imagenes/ele/{target_folder}/{f}"
            entry += f"| **{pose}** | ![{pose}]({url}) |\n"
            
    return entry

with open(md_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Append orphaned looks to the end of the file or after look 18
# For simplicity, I'll append them before the "ERA GOTICA ARCHIVADA" message or at the end.
# Actually, I'll insert them after Look 18.
look18_marker = "## ?? Look 18: CEO of Nothing (Corporate Goth)"
if look18_marker in content:
    # Find the end of Look 18 section (next ---)
    parts = content.split(look18_marker, 1)
    subparts = parts[1].split('---', 1)
    
    new_entries = ""
    for l in orphaned_looks:
        # Only add looks that are <= 84 to this file
        if l <= 84:
            new_entries += generate_entry(l)
    
    if len(subparts) > 1:
        new_content = parts[0] + look18_marker + subparts[0] + "\n---" + new_entries + "\n---" + subparts[1]
    else:
        new_content = content + new_entries
    
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Orphaned looks documentation generated.")
else:
    print("Look 18 marker not found.")
