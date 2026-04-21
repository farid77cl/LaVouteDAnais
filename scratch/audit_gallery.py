import re

file_path = r'c:\Users\farid\LaVouteDAnais\00_Ele\galeria_outfits.md'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Buscar todos los bloques de looks (## Look X)
looks = re.findall(r'## .*? Look (\d+)', content)
total_looks = len(looks)

# Buscar las categorías
# El patrón busca "Categoría: [Nombre]" o "Categoría:** [Nombre]"
categories = re.findall(r'Categoría:?\**?\s*(Bikini|Lencería|Gym|Mix)', content, re.IGNORECASE)

stats = {
    "Mix": 0,
    "Bikini": 0,
    "Lencería": 0,
    "Gym": 0
}

for cat in categories:
    c = cat.capitalize()
    if c == "Lenceria": c = "Lencería"
    if c in stats:
        stats[c] += 1

print(f"Total Looks identificados: {total_looks}")
print(f"Categorías mapeadas: {len(categories)}")
for k, v in stats.items():
    perc = (v / total_looks * 100) if total_looks > 0 else 0
    print(f"{k}: {v} ({perc:.1f}%)")

# Mostrar los últimos 5 looks para ver si faltan categorías
print("\nÚltimos 10 looks y sus categorías (extracto):")
look_blocks = re.split(r'## ', content)
for block in look_blocks[-10:]:
    lines = block.split('\n')
    if lines:
        title = lines[0]
        cat_match = re.search(r'Categoría:?\**?\s*(\w+)', block, re.IGNORECASE)
        cat = cat_match.group(1) if cat_match else "No encontrada"
        print(f"- {title} -> {cat}")
