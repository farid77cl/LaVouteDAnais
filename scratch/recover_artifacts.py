import os
import shutil
import re

brain_path = r'C:\Users\farid\.gemini\antigravity\brain\02b4c1db-5348-413a-b982-0b18ca388c8e'
ele_path = r'C:\Users\farid\LaVouteDAnais\05_Imagenes\ele'

# Mapping of look numbers to canonical folder names
canonical_folders = {
    121: 'look121_pink_silk_satin',
    122: 'look122_black_latex_suit',
    126: 'look126_red_vinyl_set',
    128: 'look128_red_silk_noir',
    129: 'look129_blue_velvet_set',
    130: 'look130_midnight_rooftop_bikini',
    132: 'look132_emerald_silk_lace_lingerie',
    134: 'look134_champagne_silk_sequins_lingerie',
    135: 'look135_silver_sequined_bikini',
    136: 'look136_plum_velvet_romance_lingerie'
}

artifacts = [f for f in os.listdir(brain_path) if f.endswith('.png')]

for art in artifacts:
    # Pattern: ele_XXX_pose_TIMESTAMP.png or ele_XXX_pose.png
    m = re.match(r'(ele|helena)_(\d+)_(.*?)_?\d*\.png', art)
    if m:
        prefix = m.group(1)
        look_num = int(m.group(2))
        pose = m.group(3).replace('_v1', '').replace('_retry', '').replace('_view', '').strip('_')
        
        if look_num in canonical_folders:
            dest_folder = os.path.join(ele_path, canonical_folders[look_num])
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
            
            new_name = f"{prefix}_{look_num:03d}_{pose}.png"
            src = os.path.join(brain_path, art)
            dst = os.path.join(dest_folder, new_name)
            
            print(f"Moving {art} -> {new_name}")
            shutil.copy2(src, dst)

print("Artifact recovery complete.")
