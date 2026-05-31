import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

repo_root = Path("c:/Users/farid/LaVouteDAnais")
ele_dir = repo_root / "05_Imagenes" / "ele"
galeria_path = repo_root / "00_Ele" / "galeria_outfits.md"

if not galeria_path.exists():
    print("galeria_outfits.md not found!")
    exit(1)

content = galeria_path.read_text(encoding="utf-8")

# Let's find look sections from galeria_outfits.md for looks 200 to 310
matches = list(re.finditer(r'^##\s+.*?\bLook\s+(\d+)\b', content, re.MULTILINE | re.IGNORECASE))
look_locations = {}
for i in range(len(matches)):
    start_pos = matches[i].start()
    end_pos = matches[i+1].start() if i+1 < len(matches) else len(content)
    look_num = int(matches[i].group(1))
    section_text = content[start_pos:end_pos]
    
    loc_match = re.search(r'-\s+\*\*Ubicación:\*\*\s+\`(.*?)\`', section_text)
    if loc_match:
        loc = loc_match.group(1).replace("../", "").strip("/")
        look_locations[look_num] = repo_root / loc

# Now let's list all actual folders on disk
actual_dirs = [d for d in ele_dir.iterdir() if d.is_dir() and d.name.startswith("look")]
actual_looks = {}
for d in actual_dirs:
    m = re.match(r'^look0*(\d+)', d.name)
    if m:
        actual_looks[int(m.group(1))] = d

print("--- Scan of Poses in Looks 200-310 ---")
missing_standing = []
missing_back = []

for num in range(200, 311):
    # Find directory path
    folder_path = look_locations.get(num)
    if not folder_path:
        # If not in expected, check actual
        folder_path = actual_looks.get(num)
        
    if not folder_path or not folder_path.exists():
        print(f"Look {num}: [MISSING DIRECTORY] - expected {folder_path}")
        missing_standing.append(num)
        missing_back.append(num)
        continue
        
    # Check files inside directory
    files = [f.name.lower() for f in folder_path.glob("*.png")]
    
    # Check standing pose
    has_standing = False
    for f in files:
        if "standing" in f:
            has_standing = True
            break
            
    # Check back view pose
    has_back = False
    for f in files:
        # Look for back_view or backview or back
        if "back" in f:
            has_back = True
            break
            
    status = []
    if has_standing:
        status.append("Standing: YES")
    else:
        status.append("Standing: MISSING")
        missing_standing.append(num)
        
    if has_back:
        status.append("Back View: YES")
    else:
        status.append("Back View: MISSING")
        missing_back.append(num)
        
    print(f"Look {num}: {folder_path.name} | {', '.join(status)}")

print("\n--- Summary ---")
print(f"Looks missing Standing: {missing_standing}")
print(f"Looks missing Back View: {missing_back}")
