import re
import os

filepath = r'c:\Users\farid\LaVouteDAnais\00_Ele\galeria_outfits.md'
output_path = r'c:\Users\farid\LaVouteDAnais\00_Ele\galeria_outfits.md'

# List of folders for mapping
folders = [
    "look001_morticia", "look002_elvira", "look003_vampiresa", "look004_widow", "look005_interview",
    "look006_bloodmoon", "look007", "look008_esmeralda", "look009_corazon", "look010_zafiro",
    "look011_absinthe", "look012_borgona", "look013_amatista", "look014_midnight", "look015_vampire_bride",
    "look016_ghost_bride", "look017_cybergoth", "look018_ceo", "look019_velvet_witch", "look020_latex_mistress",
    "look021_opera_diva", "look022_corset_queen", "look023_latex_goddess", "look024_gothic_bikini", "look025_office_dominatrix",
    "look026_tattoo", "look031_industrial_siren", "look032_corporate_widow", "look033_velvet_chains", "look034_white_chrome",
    "look035_velvet_noir_empress", "look036_crimson_serpent", "look037_midnight_widow", "look038_victorian_mourning",
    "look039_cyber_goth_oracle", "look040_baroque_gold_empress", "look041_vampire_queen", "look042_neon_neural_goth",
    "look045_midnight_secretary", "look046_latex_nun", "look047_midnight_pvc_doll", "look050_golden_cage",
    "look051_obsidian_rose_queen", "look057_hypnotic_spiral", "look058_subliminal_waveform", "look059_midnight_cowgirl",
    "look061_venom_wire_doll", "look062_sporty_latex_goth", "look063_beach_goth_bimbo", "look064_goth_pop_princess",
    "look066_bimbo_stripper", "look068_retro_aerobics", "look069_toxic_aerobics", "look070_cyber_yoga", "look071_goth_nurse",
    "look073_urban_fetish_trap_canon", "look074_50s_diner", "look075_golden_trap_diva", "look076_liquid_metal_silver",
    "look077_alpine_goth_luxury", "look079_goth_freshman", "look080_siberian_weather_diva", "look081_fox_news_anchor",
    "look082_abyssal_secretary", "look083_biker_punk_90s", "look084_crimson_spike", "look085_vinyl_fresa_bimbo",
    "look086_office_siren", "look087_ele_v3_core", "look088_gallery_opening", "look089_imperial_burgundy",
    "look090_liquid_gold", "look091_vinyl_yoga_gym", "look092_corporate_paradox_v3_2", "look093_high_gloss_cherry",
    "look094_the_locked_legacy_lingerie", "look095_liquid_platinum", "look096_mercury_goddess", "look097_plastic_arch",
    "look098_vinyl_cheerleader", "look099_gym_bimbo", "look100_cobalt_chrome", "look101_elite_lingerie",
    "look102_red_vinyl_siren", "look103_fox_news_weather_diva", "look104_platinum_lace_secret", "look105_french_maid",
    "look106_latex_ceo", "look107_latex_nun_v3_2", "look108_sanhattan_power_secretary", "look109_leopard_vinyl_siren",
    "look110_cherry_vinyl_trench_siren", "look111_cyan_chrome_boudoir_assassin", "look112_stepford_gold",
    "look113_mob_wife", "look113_neon_pink_latex_gym_bimbo", "look114_santiago_power_secretary", "look115_silver_bikini",
    "look116_cuico_flaite_leather", "look117_cobalt_bikini", "look118_noir_vinyl_blood_lace",
    "look119_liquid_gold_bikini", "look120_boardroom_siren", "look121_vinyl_rose_boudoir", "look122_white_vinyl_mermaid",
    "look123_skygate_siren", "look124_neon_gym_bimbo", "look125_sapphire_glow_bikini", "look126_mirror_platinum_ceo",
    "look127_silk_noir_lace", "look128_red_silk_noir", "look129_bridal_purity", "look130_midnight_rooftop",
    "look131_electric_blue_wrap", "look132_emerald_silk_lace", "look133_hot_pink_strings", "look134_champagne_silk_sequins",
    "look135_silver_sequined", "look136_plum_velvet_romance_lingerie", "look137_leopard_micro", "look138_white_lace_mist",
    "look139_red_metallic_siren", "look140_dark_sequin_empress", "look141_radiant_neon_lattice"
]

def get_best_folder(look_id):
    # Standardize ID to 3 digits
    look_id_str = str(look_id).zfill(3)
    # Search for folder starting with look[ID]
    for f in folders:
        if f.startswith(f"look{look_id_str}"):
            return f
    # Fallback to 2 digits if 3 not found
    look_id_str_2 = str(look_id).zfill(2)
    for f in folders:
        if f.startswith(f"look{look_id_str_2}"):
            return f
    return None

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
current_look_id = None
current_folder = None

for i, line in enumerate(lines):
    # Detect Look header
    header_match = re.search(r'## (?:[\s\S]*?)Look (\d+):', line)
    if header_match:
        current_look_id = int(header_match.group(1))
        current_folder = get_best_folder(current_look_id)
    
    # Detect Ubicación line
    if "**Ubicación:**" in line or "- **Ubicación:**" in line:
        if current_look_id:
            folder = get_best_folder(current_look_id)
            if folder:
                line = f"- **Ubicación:** `05_Imagenes/ele/{folder}/`\n"
    
    # Clean up my $newLook mistake
    if line.strip() == "$newLook":
        continue
    
    # Detect Image tags
    if "![" in line and "](" in line:
        # Regex to find the markdown image tag
        image_matches = re.finditer(r'!\[(.*?)\]\((.*?)\)', line)
        for match in image_matches:
            alt_text = match.group(1)
            original_path = match.group(2)
            
            # If already a full URL, we might still want to check/fix it
            # But the primary goal is to fix broken/relative paths
            if not original_path.startswith("http"):
                if current_folder:
                    # Map common descriptor to file name
                    descriptor = alt_text.lower().replace(" ", "_")
                    # Handle special cases in alt text
                    if descriptor == "back_view": descriptor = "back"
                    if descriptor == "side_profile": descriptor = "side_profile"
                    
                    filename = f"ele_{str(current_look_id).zfill(3)}_{descriptor}.png"
                    new_path = f"https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/05_Imagenes/ele/{current_folder}/{filename}"
                    line = line.replace(f"({original_path})", f"({new_path})")
            else:
                # Standardize existing full URLs to main branch and farid77cl
                line = line.replace("raw.githubusercontent.com/farid77cl/LaVouteDAnais/master/", "raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/")
    
    new_lines.append(line)

# Handle the missing Look 141 if not found
if current_look_id != 141:
    # (Assuming I want to re-add Look 141 properly if it was lost)
    pass

with open(output_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Standardization complete.")
