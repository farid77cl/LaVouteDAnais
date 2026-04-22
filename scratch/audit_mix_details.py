import re

filepath = r'c:\Users\farid\LaVouteDAnais\00_Ele\galeria_outfits.md'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Split by Look headers
looks = re.split(r'## (?:[\s\S]*?)Look \d+:', content)[1:]

stats = {
    "Corporate": 0,
    "Domestic": 0,
    "High-Fashion & Nightclub": 0,
    "Pin-Up & Athleisure": 0,
    "Professional Stripper": 0,
    "Escort de Lujo": 0,
    "Otros/Unclassified": 0
}

keywords = {
    "Corporate": ["secretary", "office", "corporativo", "ejecutiva", "boardroom", "oficina", "siren"],
    "Domestic": ["maid", "mucama", "stepford", "uniforme", "housewife", "doméstico", "servicio", "asset"],
    "High-Fashion & Nightclub": ["mugler", "editorial", "party", "nightclub", "vanguardia", "lentejuelas", "disco", "fashion"],
    "Pin-Up & Athleisure": ["pinup", "retro", "tennis", "equestrian", "pastel", "50s", "athleisure", "club de polo"],
    "Professional Stripper": ["stripper", "pole", "exotic", "show", "pedrería", "performance"],
    "Escort de Lujo": ["escort", "luxury", "silk", "satin", "gala", "compañía", "seda", "satén"]
}

total_mix = 0

for look in looks:
    # Check if it's Lenceria, Bikini or Gym first (to exclude from Mix audit)
    # Actually, we want to audit the 102 looks that are already classified as Mix.
    # For now, let's just audit everything that doesn't clearly state "Categoría: Lencería" etc.
    if "Categoría: Lencería" in look or "Categoría: Bikini" in look or "Categoría: Gym" in look:
        continue
    
    total_mix += 1
    found = False
    look_lower = look.lower()
    
    # Simple keyword matching
    for cat, keys in keywords.items():
        if any(k in look_lower for k in keys):
            stats[cat] += 1
            found = True
            break
    
    if not found:
        stats["Otros/Unclassified"] += 1

print(f"Total Mix Auditados: {total_mix}")
for cat, count in stats.items():
    perc = (count / total_mix * 100) if total_mix > 0 else 0
    print(f"{cat}: {count} ({perc:.1f}%)")
