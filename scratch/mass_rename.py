import os
import re

def pad_look(match):
    prefix = match.group(0)
    digits = match.group(1)
    if len(digits) < 3:
        new_digits = digits.zfill(3)
        return prefix.replace(f"look{digits}", f"look{new_digits}")
    return prefix

def update_file(file_path):
    print(f"Updating {file_path}")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Regex to find look folder names: look[digits]_
        # We search specifically for look follow by 1 or 2 digits and an underscore or slash
        new_content = re.sub(r"look(\d+)(?=[_/])", pad_look, content)
        
        # Special fix for Look 133 and 136 local links to remote
        # Revert ![...] (../05_Imagenes/...) to https://raw.githubusercontent.com/...
        remote_prefix = "https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/"
        new_content = re.sub(r"\!\[(.*?)\]\(\.\./05_Imagenes/", rf"![\1]({remote_prefix}05_Imagenes/", new_content)

        if new_content != content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            return True
    except Exception as e:
        print(f"Error updating {file_path}: {e}")
    return False

# Directories to process
docs_dir = "C:/Users/farid/LaVouteDAnais/00_Ele"
images_dir = "C:/Users/farid/LaVouteDAnais/05_Imagenes"

# Update docs
for f in os.listdir(docs_dir):
    if f.endswith(".md"):
        update_file(os.path.join(docs_dir, f))

# Update READMEs in images subdirs
for root, dirs, files in os.walk(images_dir):
    if "README.md" in files:
        update_file(os.path.join(root, "README.md"))

