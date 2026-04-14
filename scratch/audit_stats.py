import re
import os

def audit_gallery():
    path = r'c:\Users\fabara\LaVouteDAnais\00_Ele\galeria_outfits.md'
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return

    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by Look headers
    looks = re.split(r'\n## .*? Look ', content)
    
    counts = {
        'Mix': 0,
        'Bikini': 0,
        'Lencería': 0,
        'Gym': 0,
        'Otro': 0
    }
    
    for look in looks[1:]: # Skip the first part before any Look
        # Search for category
        # - **Categoría:** Mix
        # matches cases with accents or differnet types of Mix
        match = re.search(r'\*\*Categoría:\*\*\s*(.*)', look, re.IGNORECASE)
        if match:
            cat = match.group(1).strip()
            if 'Mix' in cat:
                counts['Mix'] += 1
            elif 'Bikini' in cat:
                counts['Bikini'] += 1
            elif 'Lencería' in cat or 'Lenceria' in cat:
                counts['Lencería'] += 1
            elif 'Gym' in cat:
                counts['Gym'] += 1
            else:
                counts['Otro'] += 1
        else:
            # Try to infer from content if missing
            if 'bikini' in look.lower():
                counts['Bikini'] += 1
            elif 'gym' in look.lower() or 'deportivo' in look.lower():
                counts['Gym'] += 1
            elif 'lencería' in look.lower() or 'lenceria' in look.lower() or 'sostén' in look.lower():
                counts['Lencería'] += 1
            else:
                counts['Mix'] += 1 # Default is Mix
                
    total = sum(counts.values())
    if total == 0:
        print("No looks found.")
        return

    print(f"Total Looks: {total}")
    for cat, count in counts.items():
        percentage = (count / total) * 100
        print(f"{cat}: {count} ({percentage:.1f}%)")

if __name__ == "__main__":
    audit_gallery()
