import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
gallery_path = os.path.abspath(os.path.join(script_dir, "..", "..", "..", "05_Imagenes", "ele"))
looks = []

for folder in os.listdir(gallery_path):
    if folder.startswith("look"):
        match = re.search(r"look(\d+)", folder)
        if match:
            num = int(match.group(1))
            if num >= 92: # Starts from 24/03/2026
                looks.append(folder.lower())

stats = {
    "Lenceria": 0,
    "Bikini": 0,
    "Gym": 0,
    "Mix": 0
}

for look in looks:
    if "lenceria" in look or "lingerie" in look or "boudoir" in look:
        stats["Lenceria"] += 1
    elif "bikini" in look:
        stats["Bikini"] += 1
    elif "gym" in look or "sport" in look or "workout" in look:
        stats["Gym"] += 1
    else:
        stats["Mix"] += 1

total = len(looks)
print(f"Total looks since 24/03/2026: {total}")
for k, v in stats.items():
    perc = (v / total * 100) if total > 0 else 0
    print(f"{k}: {v} ({perc:.1f}%)")
