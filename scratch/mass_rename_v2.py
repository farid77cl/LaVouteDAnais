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
        
        # 1. Pad look numbers to 3 digits (look01 -> look001, etc.)
        # Match "look" followed by digits, but only if length is < 3
        new_content = re.sub(r"look(\d+)(?=[_/])", pad_look, content)
        
        # 2. Remote-Only Enforcement: Convert all local paths to remote GitHub URLs
        # Matches patterns like: ../05_Imagenes/ or ..\05_Imagenes\
        remote_prefix = "https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/"
        
        # Regex to match Markdown image/link syntax with local paths
        # Matches ![[alt]](..\05_Imagenes\...) or ![[alt]](../05_Imagenes/...)
        local_pattern_1 = r"(\!\[.*?\])\(\.\.[\/\\]05_Imagenes[\/\\]"
        new_content = re.sub(local_pattern_1, rf"\1({remote_prefix}05_Imagenes/", new_content)
        
        # Also handle cases starting with /05_Imagenes or 05_Imagenes
        local_pattern_2 = r"(\!\[.*?\])\((?:\/)?05_Imagenes[\/\\]"
        new_content = re.sub(local_pattern_2, rf"\1({remote_prefix}05_Imagenes/", new_content)

        # 3. Fix internal backslashes in paths within the remote URLs (normalize to forward slash)
        # Find the full GitHub raw URL and replace any lingering backslashes
        def normalize_github_urls(match):
            return match.group(0).replace("\\", "/")
            
        new_content = re.sub(rf"{re.escape(remote_prefix)}05_Imagenes/[^\)]+", normalize_github_urls, new_content)

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
if os.path.exists(docs_dir):
    for f in os.listdir(docs_dir):
        if f.endswith(".md"):
            update_file(os.path.join(docs_dir, f))

# Update READMEs in images subdirs
if os.path.exists(images_dir):
    for root, dirs, files in os.walk(images_dir):
        if "README.md" in files:
            update_file(os.path.join(root, "README.md"))
