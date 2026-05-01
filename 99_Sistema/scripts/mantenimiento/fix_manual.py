import os

# Replacements for galeria_outfits.md (handling various mojibake layers)
outfit_replacements = {
    "Ãƒ³": "ó",
    "Ãƒ­": "í",
    "Ãƒ¡": "á",
    "Ãƒ©": "é",
    "Ãƒ±": "ñ",
    "Ãƒº": "ú",
    "ó": "ó",
    "í": "í",
    "á": "á",
    "é": "é",
    "ñ": "ñ",
    "ú": "ú",
    "Ã": "í", # Final fallback if Áappears alone in some contexts (e.g. GalerÃ)
    "ðŸ¦‡": "🦉", # Bat? No, 0xF0 0x9F 0xA6 0x87 is Bat. Let's assume Bat.
    "ðŸŒ™": "🌙",
    "ðŸ’€": "💀",
    "ðŸ©¸": "🩸",
    "ðŸ•¸ï¸": "🕷️",
    "ðŸŒ‘": "🌑",
    "ðŸ”®": "🔮",
    "â¤ï¸": "❤️", # This handles the sequence seen in line 225
    "ðŸ’Ž": "💎",
    "ðŸ’™": "💙",
    "ðŸ": "💚",
    "ðŸ·": "🍷",
    "ðŸ’œ": "💜",
    "ðŸ¥‚": "🥂",
    "â›“ï¸": "⛓️",
    "ðŸ": "", # Remove broken partial emojis if any left
}

# Replacements for banco_prompts_v01_basico.md (fixing missing chars)
prompt_replacements = {
    "CANNICAS": "CANÓNICAS",
    "fsicos": "físicos",
    "especficos": "específicos",
    "ANAS": "ANAÏS",
    "Ana s": "Anaïs",
    "?? ": "", # Remove leading question marks
    "??": "",
}

files_to_process = [
    {
        "path": r"C:\Users\fabara\LaVouteDAnais\00_Helena\galeria_outfits.md",
        "replacements": outfit_replacements
    },
    {
        "path": r"C:\Users\fabara\LaVouteDAnais\00_Helena\bancos_prompts\banco_prompts_v01_basico.md",
        "replacements": prompt_replacements
    }
]

def process_file(file_info):
    path = file_info["path"]
    replacements = file_info["replacements"]
    
    print(f"Processing {path}...")
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return

    try:
        # Read as UTF-8
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Apply replacements
        new_content = content
        for bad, good in replacements.items():
            new_content = new_content.replace(bad, good)
            
        if new_content != content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Applied fixes to {path}")
        else:
            print(f"No patterns found in {path}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    for f in files_to_process:
        process_file(f)
