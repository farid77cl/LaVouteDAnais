import os
import re
import glob

# New Miss Doll canon description (compact version for varied contexts)
NEW_CANON_FULL = """Glamorous woman with platinum blonde bob haircut with straight bangs,
flawless porcelain skin with satin finish (NO rosy cheeks),
delicate refined nose, high cheekbones with soft contour,
HEAVY GLAMOUR MAKEUP: bronze/champagne smokey eyes with shimmer inner corners, thick cat-eye winged liner, mega volume wispy false lashes, defined arched brows, ULTRA PLUMP overlined glossy RED lips (bee-stung bimbo lips),
human realistic face with parted lips and dreamy seductive expression (NOT CGI, NOT plastic),
EXTREME hourglass silhouette with large round high-profile breast implants creating prominent cleavage, tiny cinched waist,
PLEASER platform heels 16-18cm (7-8"), visible external corset over clothing."""

banks_path = r"C:\Users\fabara\LaVouteDAnais\00_Helena\banco_prompts_v*.md"
updated_count = 0

for filepath in glob.glob(banks_path):
    filename = os.path.basename(filepath)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip if already updated
    if 'shimmer inner corners' in content:
        print(f"✓ Already updated: {filename}")
        continue
    
    # Pattern: Find old Miss Doll descriptions and replace
    # Look for patterns like "Glamorous woman with platinum blonde bob..." up to closing ```
    
    patterns_to_replace = [
        # Standard multiline pattern
        (r'(Glamorous woman with platinum blonde bob haircut with straight bangs,?\s*\n?\s*flawless porcelain skin[^`]+?(?:platform heels 16-18cm|PLEASER platform heels)[^`]*?\.)', NEW_CANON_FULL),
        # Single line compact pattern
        (r'Glamorous woman with platinum blonde bob haircut with straight bangs,\s*flawless porcelain skin \(NO rosy cheeks\),\s*HEAVY GLAMOUR MAKEUP:[^.]+?platform heels 16-18cm[^.]*\.', NEW_CANON_FULL),
    ]
    
    modified = False
    for pattern, replacement in patterns_to_replace:
        if re.search(pattern, content, re.DOTALL | re.IGNORECASE):
            content = re.sub(pattern, replacement, content, count=1, flags=re.DOTALL | re.IGNORECASE)
            modified = True
            break
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Updated: {filename}")
        updated_count += 1
    else:
        print(f"⚠️ No pattern matched: {filename}")

print(f"\n✅ Updated: {updated_count} files")
