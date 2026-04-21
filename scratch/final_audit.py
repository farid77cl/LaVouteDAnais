import re

file_path = r'c:\Users\farid\LaVouteDAnais\00_Ele\galeria_outfits.md'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Dividir por looks
look_blocks = re.split(r'## .*? Look (\d+)', content)
# El primer elemento es el header del archivo
# Luego vienen en pares: (numero, contenido)

counts = {
    "Mix": 0,
    "Bikini": 0,
    "Lencería": 0,
    "Gym": 0
}

# Inicializar con los datos de la era gótica (1-84)
counts["Mix"] = 72
counts["Bikini"] = 5
counts["Lencería"] = 3
counts["Gym"] = 4

processed_looks = set()

for i in range(1, len(look_blocks), 2):
    look_num = look_blocks[i]
    look_content = look_blocks[i+1]
    
    if look_num in processed_looks: continue
    processed_looks.add(look_num)
    
    # Prioridad 1: Categoría explícita
    cat_match = re.search(r'Categoría:?\**?\s*(\w+)', look_content, re.IGNORECASE)
    category = None
    if cat_match:
        cat_str = cat_match.group(1).capitalize()
        if "Lenc" in cat_str: category = "Lencería"
        elif "Bikini" in cat_str: category = "Bikini"
        elif "Gym" in cat_str or "Sport" in cat_str: category = "Gym"
        elif "Mix" in cat_str: category = "Mix"
    
    # Prioridad 2: Título del look
    if not category:
        title_line = look_content.split('\n')[0].lower()
        if "bikini" in title_line or "mermaid" in title_line or "strings" in title_line or "triangle" in title_line:
            category = "Bikini"
        elif "lingerie" in title_line or "boudoir" in title_line or "lace" in title_line or "silk" in title_line or "lenceria" in title_line:
            category = "Lencería"
        elif "gym" in title_line or "yoga" in title_line or "performance" in title_line or "aerobics" in title_line:
            category = "Gym"
        else:
            category = "Mix"
    
    counts[category] += 1

total = sum(counts.values())
print(f"Auditoría Completa (1-{max(map(int, processed_looks))}):")
print(f"Total Looks: {total}")
for k, v in counts.items():
    perc = (v / total * 100) if total > 0 else 0
    print(f"{k}: {v} ({perc:.1f}%)")
