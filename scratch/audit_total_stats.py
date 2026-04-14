import re
import os

def audit_file(path):
    if not os.path.exists(path):
        return []
    
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Improved regex to find looks: starts with ## and contains "Look X"
    look_sections = re.split(r'\n##\s+', content)
    
    looks_data = []
    for section in look_sections[1:]:
        header_match = re.search(r'(?:.*?Look\s*)(\d+)', section, re.IGNORECASE)
        if not header_match:
            continue
            
        look_id = int(header_match.group(1))
        
        # Determine category
        cat_match = re.search(r'\*\*Categoría:\*\*\s*(.*)', section, re.IGNORECASE)
        category = 'Mix' # Default
        if cat_match:
            cat_str = cat_match.group(1).strip().lower()
            if 'mix' in cat_str: category = 'Mix'
            elif 'bikini' in cat_str: category = 'Bikini'
            elif 'lencería' in cat_str or 'lenceria' in cat_str: category = 'Lencería'
            elif 'gym' in cat_str or 'deportivo' in cat_str: category = 'Gym'
        else:
            # Fallback based on content keywords
            low_section = section.lower()
            if 'bikini' in low_section: category = 'Bikini'
            elif 'gym' in low_section or 'fittness' in low_section: category = 'Gym'
            elif 'lencería' in low_section or 'lenceria' in low_section or 'boudoir' in low_section: category = 'Lencería'
        
        looks_data.append({'id': look_id, 'category': category})
    
    return looks_data

def run_total_audit():
    modern_path = r'c:\Users\fabara\LaVouteDAnais\00_Ele\galeria_outfits.md'
    gothic_path = r'c:\Users\fabara\LaVouteDAnais\00_Ele\galeria_outfits_era_gotica.md'
    
    modern_looks = audit_file(modern_path)
    gothic_looks = audit_file(gothic_path)
    
    all_looks = modern_looks + gothic_looks
    
    # Deduplicate by ID just in case
    unique_looks = {}
    for l in all_looks:
        unique_looks[l['id']] = l['category']
    
    results = {
        'Mix': 0,
        'Bikini': 0,
        'Lencería': 0,
        'Gym': 0
    }
    
    for cat in unique_looks.values():
        if cat in results:
            results[cat] += 1
        else:
            results['Mix'] += 1
            
    total = len(unique_looks)
    print(f"--- REPORTE FINAL DE AUDITORÍA ---")
    print(f"Total de Looks Únicos: {total}")
    for cat, count in results.items():
        perc = (count / total * 100) if total > 0 else 0
        print(f"{cat}: {count} ({perc:.1f}%)")

if __name__ == "__main__":
    run_total_audit()
