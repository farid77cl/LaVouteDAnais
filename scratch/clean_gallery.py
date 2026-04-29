
import sys

filepath = r'c:\Users\farid\LaVouteDAnais\00_Ele\galeria_outfits.md'
with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

# Line numbers in view_file were 1-indexed.
# Lines to delete: 4019 to 4028 (approximately, based on last view)
# Wait, I should re-read to be absolutely sure of current indices.
# After deleting 4019-4022 and then 4020...
# Let's just look for the "Look 155" header and delete everything between the end of Look 154 table and that header.

start_marker = "| **Lying Down** | ![Lying Down](https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/05_Imagenes/ele/look154_platinum_chrome_galatea/ele_154_pose7_lying.png) |"
end_marker = "## 🏢 Look 155: High-Voltage Corporate (29/04/2026)"

new_lines = []
skip = False
for line in lines:
    if start_marker in line:
        new_lines.append(line)
        new_lines.append("\n---\n\n")
        skip = True
        continue
    if end_marker in line:
        skip = False
    
    if not skip:
        new_lines.append(line)

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
print("File cleaned successfully.")
