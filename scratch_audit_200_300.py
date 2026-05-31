import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

repo_root = Path("c:/Users/farid/LaVouteDAnais")
ele_dir = repo_root / "05_Imagenes" / "ele"

# Find folders for looks 200 to 300
actual_dirs = [d for d in ele_dir.iterdir() if d.is_dir() and d.name.startswith("look")]
looks_folders = {}

for d in actual_dirs:
    m = re.match(r'^look0*(\d+)', d.name)
    if m:
        num = int(m.group(1))
        if 200 <= num <= 300:
            if num not in looks_folders:
                looks_folders[num] = []
            looks_folders[num].append(d)

print(f"Analyzing {len(looks_folders)} looks in 200-300 range...\n")

missing_folders = []
for num in range(200, 301):
    if num not in looks_folders:
        missing_folders.append(num)

if missing_folders:
    print(f"❌ Looks with NO folder on disk at all: {missing_folders}\n")
else:
    print("✅ All looks 200-300 have at least one folder on disk.\n")

print("--- Detailed Pose Analysis (Expected: 7 poses) ---")

for num in sorted(looks_folders.keys()):
    folders = looks_folders[num]
    
    # Collect all PNG files recursively
    all_png_files = []
    for fld in folders:
        all_png_files.extend(list(fld.rglob("*.png")))
        
    detected_poses = set()
    for f in all_png_files:
        name = f.name.lower()
        if "standing" in name or "de_pie" in name or "de pie" in name:
            detected_poses.add("standing")
        elif "back" in name or "espalda" in name:
            detected_poses.add("back_view")
        elif "seated" in name or "sentada" in name:
            detected_poses.add("seated")
        elif "profile" in name or "perfil" in name or "side" in name:
            detected_poses.add("side_profile")
        elif "ditzy" in name:
            detected_poses.add("ditzy")
        elif "pov" in name:
            detected_poses.add("pov")
        elif "odalisque" in name or "lying" in name or "acostada" in name or "recostada" in name:
            detected_poses.add("odalisque")
            
    expected = {"standing", "back_view", "seated", "side_profile", "ditzy", "pov", "odalisque"}
    missing = expected - detected_poses
    
    folder_names = " + ".join([f.name for f in folders])
    if missing:
        print(f"⚠️ Look {num} ({folder_names}): MISSING {sorted(list(missing))} | Has {len(all_png_files)} PNGs: {sorted(list(detected_poses))}")

print("\nAnalysis completed.")
