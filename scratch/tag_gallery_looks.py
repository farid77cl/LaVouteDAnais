import re
import os

filepath = r'c:\Users\farid\LaVouteDAnais\00_Ele\galeria_outfits.md'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Split by Look sections
sections = re.split(r'(## .*?Look \d+:.*?\n)', content)
header = sections[0]
looks = sections[1:]

def classify_look(text):
    text_lower = text.lower()
    
    # Category
    category = "Mix"
    if "lencería" in text_lower or "lingerie" in text_lower: category = "Lencería"
    elif "bikini" in text_lower: category = "Bikini"
    elif "gym" in text_lower or "sport" in text_lower or "yoga" in text_lower: category = "Gym"
    
    # Subcategory (only for Mix)
    subcategory = "None"
    if category == "Mix":
        if any(k in text_lower for k in ["secretary", "office", "oficina", "ejecutiva", "corporate"]): subcategory = "Corporate"
        elif any(k in text_lower for k in ["maid", "mucama", "stepford", "domestic", "servicio"]): subcategory = "Domestic"
        elif any(k in text_lower for k in ["stripper", "pole", "exotic"]): subcategory = "Professional Stripper"
        elif any(k in text_lower for k in ["escort", "luxury", "gala", "compañía"]): subcategory = "Escort de Lujo"
        elif any(k in text_lower for k in ["pinup", "retro", "50s", "athleisure", "tennis"]): subcategory = "Pin-Up & Athleisure"
        else: subcategory = "High-Fashion & Nightclub"
    
    # Tags
    tags = []
    if "vinyl" in text_lower or "vinilo" in text_lower: tags.append("#vinyl")
    if "latex" in text_lower or "látex" in text_lower: tags.append("#latex")
    if "pvc" in text_lower: tags.append("#pvc")
    if "silk" in text_lower or "seda" in text_lower: tags.append("#silk")
    if "satin" in text_lower or "satén" in text_lower: tags.append("#satin")
    if "gloss" in text_lower or "brillo" in text_lower: tags.append("#glossy")
    
    return category, subcategory, " ".join(tags)

new_content = header
for i in range(0, len(looks), 2):
    look_header = looks[i]
    look_body = looks[i+1]
    
    cat, sub, tags = classify_look(look_body)
    
    # Build tag block
    tag_block = f"\n- **Categoría:** {cat}\n"
    if sub != "None":
        tag_block += f"- **Subcategoría:** {sub}\n"
    tag_block += f"- **Tags:** {tags}\n"
    
    # Insert tag block after Location if present, else after header
    if "**Ubicación:**" in look_body:
        look_body = re.sub(r'(\*\*Ubicación:\*\*.*?\n)', r'\1' + tag_block, look_body)
    else:
        look_body = tag_block + look_body
        
    new_content += look_header + look_body

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Tagging complete.")
