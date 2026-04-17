
import re

content = open('C:/Users/farid/LaVouteDAnais/00_Ele/galeria_outfits.md', 'r', encoding='utf-8').read()

looks = re.findall(r'## .*? Look (\d+):.*?- \*\*Categoría:\*\* (.*?)\n', content, re.DOTALL)

stats = {}
total = 0
for look_id, cat in looks:
    if int(look_id) >= 90:
        cat = cat.strip()
        stats[cat] = stats.get(cat, 0) + 1
        total += 1

print(f"Stats from Look 90 (Total {total} looks):")
for cat, count in stats.items():
    perc = (count / total) * 100
    print(f"- {cat}: {count} ({perc:.1f}%)")
