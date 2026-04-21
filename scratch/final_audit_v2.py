import re

file_path = r'c:\Users\farid\LaVouteDAnais\00_Ele\galeria_outfits.md'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Capturar headers de nivel 2 o 3 que contengan "Look X"
look_blocks = re.split(r'##+ .*?[Ll]ook (\d+)', content)

counts = {
    "Mix": 0,
    "Bikini": 0,
    "Lencería": 0,
    "Gym": 0
}

# Gothic Era base (1-84)
counts["Mix"] = 72
counts["Bikini"] = 5
counts["Lencería"] = 3
counts["Gym"] = 4

processed_looks = set()

for i in range(1, len(look_blocks), 2):
    look_num = look_blocks[i]
    look_content = look_blocks[i+1]
    
    # Ignorar si el número ya se procesó (evitar duplicados de merge)
    if look_num in processed_looks: continue
    num_int = int(look_num)
    if num_int < 85: continue # Ya contados en la base gótica
    
    processed_looks.add(look_num)
    
    category = None
    
    # Categoría explícita
    cat_match = re.search(r'Categoría:?\**?\s*(\w+)', look_content, re.IGNORECASE)
    if cat_match:
        cat_str = cat_match.group(1).capitalize()
        if "Lenc" in cat_str: category = "Lencería"
        elif "Bikini" in cat_str: category = "Bikini"
        elif "Gym" in cat_str or "Sport" in cat_str: category = "Gym"
        elif "Mix" in cat_str: category = "Mix"
    
    # Título o Concepto
    if not category:
        # Buscar en las primeras 10 líneas del bloque
        lines = look_content.split('\n')[:10]
        text_to_check = " ".join(lines).lower()
        if "bikini" in text_to_check or "mermaid" in text_to_check or "strings" in text_to_check or "triangle" in text_to_check:
            category = "Bikini"
        elif "lingerie" in text_to_check or "boudoir" in text_to_check or "lace" in text_to_check or "silk" in text_to_check or "lenceria" in text_to_check:
            category = "Lencería"
        elif "gym" in text_to_check or "yoga" in text_to_check or "performance" in text_to_check or "aerobics" in text_to_check or "workout" in text_to_check:
            category = "Gym"
        else:
            category = "Mix"
    
    counts[category] += 1

total = sum(counts.values())
print(f"Auditoría Final (1-140):")
print(f"Total Looks: {total}")
for k, v in counts.items():
    perc = (v / total * 100) if total > 0 else 0
    print(f"{k}: {v} ({perc:.1f}%)")
