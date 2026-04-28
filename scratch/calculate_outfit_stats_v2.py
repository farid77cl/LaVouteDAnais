import re

file_path = r'c:\Users\farid\LaVouteDAnais\00_Ele\galeria_outfits.md'
with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Look headers: ## ... Look XXX
looks = re.findall(r'## .* Look (\d+)', content)
categories = re.findall(r'- \*\*Categoría:\*\* (.*)', content)

stats = {
    'Mix': 0,
    'Bikini': 0,
    'Lencería': 0,
    'Gym': 0
}

for cat in categories:
    cat = cat.strip()
    if cat in stats:
        stats[cat] += 1
    elif 'Mix' in cat:
        stats['Mix'] += 1

total = len(looks)
print(f"Total Looks found in headers: {total}")
print(f"Total Categories found: {len(categories)}")
for cat, count in stats.items():
    perc = (count / total * 100) if total > 0 else 0
    print(f"{cat}: {count} ({perc:.1f}%)")
