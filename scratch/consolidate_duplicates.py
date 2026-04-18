import os
import shutil
import subprocess

ele_path = r'C:\Users\farid\LaVouteDAnais\05_Imagenes\ele'

merges = {
    'look132_emerald_silk_lace': 'look132_emerald_silk_lace_lingerie',
    'look134_champagne_silk_sequins': 'look134_champagne_silk_sequins_lingerie',
    'look135_silver_sequined': 'look135_silver_sequined_bikini',
    'look136_plum_velvet_romance': 'look136_plum_velvet_romance_lingerie'
}

def get_git_files(folder):
    result = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", "HEAD", f"05_Imagenes/ele/{folder}"],
        capture_output=True, text=True, cwd=r"C:\Users\farid\LaVouteDAnais"
    )
    return result.stdout.strip().split('\n') if result.stdout else []

for src_f, dst_f in merges.items():
    src_path = os.path.join(ele_path, src_f)
    dst_path = os.path.join(ele_path, dst_f)
    
    if not os.path.exists(dst_path):
        os.makedirs(dst_path)
    
    # 1. Move local files if any
    if os.path.exists(src_path):
        for f in os.listdir(src_path):
            if f.endswith('.png'):
                # Standardize while moving
                look_num = src_f[4:7]
                pose = "unknown"
                for p in ['standing', 'seated', 'back', 'profile', 'ditzy', 'sitting']:
                    if p in f.lower():
                        pose = p
                        break
                new_name = f"ele_{look_num}_{pose}.png"
                shutil.move(os.path.join(src_path, f), os.path.join(dst_path, new_name))
        
        # Remove empty src folder
        if not os.listdir(src_path):
            os.rmdir(src_path)

    # 2. Extract from Git HEAD if missing
    git_files = get_git_files(src_f)
    for gf in git_files:
        if gf.endswith('.png'):
            filename = os.path.basename(gf)
            look_num = src_f[4:7]
            pose = "unknown"
            for p in ['standing', 'seated', 'back', 'profile', 'ditzy', 'sitting']:
                if p in filename.lower():
                    pose = p
                    break
            new_name = f"ele_{look_num}_{pose}.png"
            target_path = os.path.join(dst_path, new_name)
            
            if not os.path.exists(target_path):
                print(f"Restoring {gf} -> {new_name}")
                subprocess.run(["git", "show", f"HEAD:{gf}"], capture_output=True, cwd=r"C:\Users\farid\LaVouteDAnais")
                # Wait, I need to write the bytes
                proc = subprocess.run(["git", "show", f"HEAD:{gf}"], capture_output=True)
                with open(target_path, 'wb') as out_f:
                    out_f.write(proc.stdout)

print("Consolidation of duplicate folders complete.")
