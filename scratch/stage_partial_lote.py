import os
import shutil

# Configuration
BRAIN_DIR = r"C:\Users\farid\.gemini\antigravity\brain\02b4c1db-5348-413a-b982-0b18ca388c8e"
REPO_DIR = r"C:\Users\farid\LaVouteDAnais"
TARGET_BASE = os.path.join(REPO_DIR, "05_Imagenes", "ele")

# Mapping: Brain Filename Fragment -> (Look Folder, Final Filename)
MAPPING = {
    "ele_132_standing": ("look132_emerald_silk_lace_lingerie", "ele_132_standing.png"),
    "ele_132_seated": ("look132_emerald_silk_lace_lingerie", "ele_132_seated.png"),
    "ele_132_side_profile": ("look132_emerald_silk_lace_lingerie", "ele_132_side_profile.png"),
    "ele_132_ditzy": ("look132_emerald_silk_lace_lingerie", "ele_132_ditzy.png"),
    
    "ele_134_standing": ("look134_champagne_silk_sequins_lingerie", "ele_134_standing.png"),
    "ele_134_seated": ("look134_champagne_silk_sequins_lingerie", "ele_134_seated.png"),
    "ele_134_side_profile": ("look134_champagne_silk_sequins_lingerie", "ele_134_side_profile.png"),
    
    "ele_135_standing": ("look135_silver_sequined_bikini", "ele_135_standing.png"),
    "ele_135_seated": ("look135_silver_sequined_bikini", "ele_135_seated.png"),
    "ele_135_side_profile": ("look135_silver_sequined_bikini", "ele_135_side_profile.png"),
    "ele_135_ditzy": ("look135_silver_sequined_bikini", "ele_135_ditzy.png"),
    
    "ele_136_back_view": ("look136_plum_velvet_romance_lingerie", "ele_136_back_view.png"),
    "ele_136_seated": ("look136_plum_velvet_romance_lingerie", "ele_136_seated.png")
}

def stage_files():
    files_in_brain = os.listdir(BRAIN_DIR)
    
    for fragment, (folder, final_name) in MAPPING.items():
        # Find matching file in brain
        match = [f for f in files_in_brain if f.startswith(fragment) and f.endswith(".png")]
        if not match:
            print(f"Skipping: {fragment} (not found)")
            continue
            
        src = os.path.join(BRAIN_DIR, match[0])
        dest_dir = os.path.join(TARGET_BASE, folder)
        dest = os.path.join(dest_dir, final_name)
        
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
            
        print(f"Moving {match[0]} -> {folder}/{final_name}")
        shutil.copy2(src, dest)

if __name__ == "__main__":
    stage_files()
