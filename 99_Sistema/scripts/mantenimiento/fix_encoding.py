import os
import shutil

files = [
    r"C:\Users\fabara\LaVouteDAnais\00_Helena\galeria_outfits.md",
    r"C:\Users\fabara\LaVouteDAnais\00_Helena\bancos_prompts\banco_prompts_v01_basico.md"
]

def fix_file(path):
    print(f"Processing {path}...")
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return

    # Backup
    shutil.copy(path, path + ".bak")
    print(f"Backed up to {path}.bak")

    # Try 1: Fix Mojibake (UTF-8 double encoded as cp1252)
    # This works for galeria_outfits.md etc.
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Heuristic: Check for Mojibake patterns like Ã³ (ó), Ã± (ñ), Ã­ (í)
        if "Ã³" in content or "Ã±" in content or "Ã" in content:
            print("Detected potential Mojibake (UTF-8 -> cp1252 -> UTF-8). Attempting fix...")
            # We must handle potential errors if content wasn't perfectly CP1252-mappable,
            # but usually mojibake comes from strict CP1252 decoding of UTF-8.
            try:
                fixed = content.encode('cp1252').decode('utf-8')
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(fixed)
                print("Applied Mojibake fix (encode cp1252 -> decode utf-8).")
                return
            except UnicodeEncodeError:
                print("Content contained characters not mapable to cp1252, skipping Mojibake fix.")
            except UnicodeDecodeError:
                print("Resulting bytes were not valid UTF-8, skipping Mojibake fix.")

    except UnicodeDecodeError:
        print("File is not valid UTF-8. Trying CP1252...")

    # Try 2: Fix CP1252 read as UTF-8 (i.e. file IS cp1252 but we want UTF-8)
    try:
        with open(path, 'r', encoding='cp1252') as f:
            content = f.read()
            
        # Verify it looks like Spanish/contains expected chars
        # Just writing it as UTF-8 is usually safe if it was CP1252
        print("Reading as CP1252 and saving as UTF-8...")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Applied CP1252 -> UTF-8 conversion.")
        return

    except Exception as e:
        print(f"Error processing file: {e}")

    print("No fix applied.")

if __name__ == "__main__":
    for f in files:
        fix_file(f)
