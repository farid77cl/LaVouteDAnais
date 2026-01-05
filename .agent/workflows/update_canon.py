import os
import re
import glob

# New Miss Doll canon description
NEW_CANON = """Glamorous woman with platinum blonde bob haircut with straight bangs,
flawless porcelain skin with satin finish (NO rosy cheeks),
delicate refined nose, high cheekbones with soft contour,
HEAVY GLAMOUR MAKEUP: bronze/champagne smokey eyes with shimmer inner corners, thick cat-eye winged liner, mega volume wispy false lashes, defined arched brows, ULTRA PLUMP overlined glossy RED lips (bee-stung bimbo lips),
human realistic face with parted lips and dreamy seductive expression (NOT CGI, NOT plastic),
EXTREME hourglass silhouette with large round high-profile breast implants creating prominent cleavage, tiny cinched waist,
PLEASER platform heels 16-18cm (7-8"), visible external corset over clothing."""

# Pattern to match old Miss Doll descriptions (flexible)
OLD_PATTERNS = [
    # Pattern 1: Standard format with feminine hourglass
    r'Glamorous woman with platinum blonde bob haircut with straight bangs,\s*\n\s*flawless porcelain skin[^`]+?PLEASER platform heels 16-18cm \(7-8"\)[^`]*?visible external corset over clothing\.',
    # Pattern 2: With [OUTFIT] placeholder
    r'Glamorous woman with platinum blonde bob haircut with straight bangs,\s*\n\s*flawless porcelain skin[^`]+?PLEASER platform heels 16-18cm \(7-8"\)[^`]*?\[OUTFIT\][^`]*?visible external corset over clothing\.',
]

# Path to prompt banks
banks_path = r"C:\Users\fabara\LaVouteDAnais\00_Helena\banco_prompts_v*.md"

updated_count = 0
skipped_count = 0

for filepath in glob.glob(banks_path):
    filename = os.path.basename(filepath)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if this file has the OLD canon that needs updating
    # Look for the old description markers
    if 'flawless porcelain skin (NO rosy cheeks)' in content and 'shimmer inner corners' not in content:
        # Find and replace the Miss Doll canon block
        # Look for content between ```text or ``` after MISS DOLL header
        
        # Pattern to find the code block after MISS DOLL
        pattern = r'(### 💖 MISS DOLL.*?```(?:text)?)\s*\n(Glamorous woman with platinum blonde bob haircut.*?visible external corset over clothing\.)'
        
        match = re.search(pattern, content, re.DOTALL)
        if match:
            # Replace just the canon description part
            new_content = re.sub(pattern, r'\1\n' + NEW_CANON, content, flags=re.DOTALL)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✅ Updated: {filename}")
            updated_count += 1
        else:
            print(f"⚠️ Pattern not found in: {filename}")
            skipped_count += 1
    elif 'shimmer inner corners' in content:
        print(f"✓ Already updated: {filename}")
    else:
        print(f"⚠️ No Miss Doll canon found in: {filename}")
        skipped_count += 1

print(f"\n✅ Updated: {updated_count} files")
print(f"⚠️ Skipped: {skipped_count} files")
