import re

filepath = r'c:\Users\farid\LaVouteDAnais\00_Ele\galeria_outfits.md'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern 1: Remove old category lines if new ones (with tags) exist below
# - **Categoría:** Cat
# - **Ubicación:** Loc
# \n
# - **Categoría:** Cat
# - **Tags:** Tags

def cleanup(match):
    header = match.group(1)
    location = match.group(2)
    new_block = match.group(3)
    return f"{location}\n{new_block}"

# Consolidate double categories
# Find pairs of category lines separated by location
cleaned_content = re.sub(
    r'(- \*\*Categoría:\*\* .*?\n)(- \*\*Ubicación:\*\* .*?\n)\n+(- \*\*Categoría:\*\* .*?\n)',
    r'\2\3',
    content
)

# Also fix the order: Location should be above Category/Tags block
# Actually, the tagging script put the block AFTER Location if found.
# But some had Categoría ABOVE Location initially.

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(cleaned_content)

print("Cleanup complete.")
