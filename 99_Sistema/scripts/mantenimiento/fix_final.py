import os
import shutil

# 1. Restore banco_prompts_v01_basico.md from backup
banco_path = r"C:\Users\fabara\LaVouteDAnais\00_Helena\bancos_prompts\banco_prompts_v01_basico.md"
banco_bak = banco_path + ".bak"

if os.path.exists(banco_bak):
    print(f"Restoring {banco_path} from backup...")
    shutil.copy(banco_bak, banco_path)
else:
    print(f"Backup not found for {banco_path}!")

# 2. Fix galeria_outfits.md
outfit_path = r"C:\Users\fabara\LaVouteDAnais\00_Helena\galeria_outfits.md"
outfit_replacements = {
    "ÃƒÂ³": "ó",
    "ÃƒÂ­": "í",
    "ÃƒÂ¡": "á",
    "ÃƒÂ©": "é",
    "ÃƒÂ±": "ñ",
    "ÃƒÂº": "ú",
    "ÃƒÅ¡": "Ú",
    "ÃƒÂ¯": "ï",
    "Ãƒâ€˜": "Ñ",
    "Ã°Å¸Â¦â€¡": "🦉",
    "Ã°Å¸Å’â„¢": "🌙",
    "Ã°Å¸â€™Å½": "💎",
    "Ã°Å¸Å’â€˜": "🌑", # Adjust as needed
}

print(f"Fixing {outfit_path}...")
try:
    with open(outfit_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for k, v in outfit_replacements.items():
        content = content.replace(k, v)
        
    with open(outfit_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Done fixes for outfit gallery.")
except Exception as e:
    print(f"Error fixing outfits: {e}")

# 3. Fix banco_prompts (Partial)
print(f"Fixing {banco_path}...")
try:
    # Read as cp1252 to rescue it if possible, or utf8 replace
    # The backup was likely the "cp1252 read as utf8" one or original?
    # Original view showed ?? so it might be CP1252.
    # Let's try reading as cp1252 and saving as utf8 FIRST.
    try:
        with open(banco_path, 'r', encoding='cp1252') as f:
            content = f.read()
        # If successfully read, write as utf8
        with open(banco_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Converted banco_prompts from CP1252 to UTF-8.")
    except:
        print("Could not read as CP1252, reading as UTF-8...")
        with open(banco_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
    # Apply text fixes
    prompt_replacements = {
        "CANNICAS": "CANÓNICAS",
        "CANNICAS": "CANÓNICAS",
        "fsicos": "físicos",
        "especficos": "específicos",
        "ANAS": "ANAÏS",
        "?? ": "",
        "??": "" 
    }
    for k, v in prompt_replacements.items():
        content = content.replace(k, v)

    with open(banco_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Done fixes for prompt bank.")

except Exception as e:
    print(f"Error fixing prompts: {e}")
