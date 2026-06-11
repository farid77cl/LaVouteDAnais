#!/usr/bin/env python3
import re
from pathlib import Path

REPO = Path(r'c:\Users\farid\LaVouteDAnais')
galeria_file = REPO / '00_Ele' / 'galeria_outfits.md'

with open(galeria_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's list the replacements we need to make
# We will match the exact prompt lines in galeria_outfits.md and replace them

replacements = {
    # Look 200
    ", one gloved arm extended showing XXXL nails, crystal-encrusted sandals pointed and visible": ", crystal-encrusted sandals pointed and visible",
    # Look 201
    ", one gloved arm extended showing XXXL nails, white stiletto pumps pointed and visible": ", white stiletto pumps pointed and visible",
    # Look 202
    ", one gloved arm extended showing XXXL nails, indigo stiletto boots pointed and visible": ", indigo stiletto boots pointed and visible",
    # Look 204
    ", one clawed-glove arm extended showing XXXL nails, emerald cage-strap stiletto sandals pointed and visible": ", emerald cage-strap stiletto sandals pointed and visible",
    # Look 205
    ", one fingerless-gloved arm extended showing XXXL nails, black stiletto trainer-boots pointed and visible": ", black stiletto trainer-boots pointed and visible",
    # Look 206
    ", one gloved arm extended showing XXXL nails, crimson stiletto boots pointed and visible": ", crimson stiletto boots pointed and visible",
    # Look 207
    ", one gloved arm extended showing XXXL nails, copper stiletto pumps pointed and visible": ", copper stiletto pumps pointed and visible",
    # Look 209
    ", one gloved arm extended showing XXXL nails, rose-gold knee-laced stiletto sandals pointed and visible": ", rose-gold knee-laced stiletto sandals pointed and visible",
    # Look 213
    ", one gloved arm extended showing XXXL nails through transparent fingertips, dome skirt fabric spreading like black petals, black stiletto pumps pointed and visible": ", dome skirt fabric spreading like black petals, black stiletto pumps pointed and visible",
}

modified = content
replaced_count = 0
for target, replacement in replacements.items():
    if target in modified:
        # We replace all occurrences of this target in the file (there should be 1 or 2 per look prompt)
        count = len(re.findall(re.escape(target), modified))
        modified = modified.replace(target, replacement)
        print(f"Replaced {count} occurrences of Look target: {target[:50]}...")
        replaced_count += count
    else:
        print(f"Target not found: {target[:50]}...")

if replaced_count > 0:
    with open(galeria_file, 'w', encoding='utf-8') as f:
        f.write(modified)
    print(f"Successfully wrote changes to galeria_outfits.md. Total replacements: {replaced_count}")
else:
    print("No replacements were made.")
