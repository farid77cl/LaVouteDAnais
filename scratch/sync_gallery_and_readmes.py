import os
import json
import re

REPO_PATH = r"C:\Users\farid\LaVouteDAnais"
MAPPING_FILE = os.path.join(REPO_PATH, "scratch", "migration_mapping.json")
GALLERY_FILE = os.path.join(REPO_PATH, "00_Ele", "galeria_outfits.md")
GITHUB_BASE = "https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/"

def sync():
    if not os.path.exists(MAPPING_FILE):
        print("Error: mapping file not found.")
        return
        
    with open(MAPPING_FILE, "r") as f:
        mapping = json.load(f)
        
    print(f"Loaded {len(mapping)} mappings.")
    
    # Sort mapping keys by length (longest first) to prevent partial replacements
    sorted_old_paths = sorted(mapping.keys(), key=len, reverse=True)
    
    # 1. Update Gallery
    if os.path.exists(GALLERY_FILE):
        with open(GALLERY_FILE, "r", encoding="utf-8") as f:
            content = f.read()
            
        updated_count = 0
        for old_path in sorted_old_paths:
            new_path = mapping[old_path]
            
            # Paths to check (helena and ele variants)
            path_variants = [old_path]
            if "05_Imagenes/ele/" in old_path:
                path_variants.append(old_path.replace("05_Imagenes/ele/", "05_Imagenes/helena/"))
            
            for path_var in path_variants:
                # Variant 1: Remote URL
                old_url = GITHUB_BASE + path_var
                new_url = GITHUB_BASE + new_path
                
                if old_url in content:
                    content = content.replace(old_url, new_url)
                    updated_count += 1
                    
                # Variant 2: Local path in MD link (if any)
                if path_var in content:
                    content = content.replace(path_var, new_path)
                    updated_count += 1
                
            # Variant 3: Catch variations where "helena" was replaced by "ele" in the old path but not in the folder
            # Usually handled by the mapping entries themselves
            
        with open(GALLERY_FILE, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Gallery updated: {updated_count} references changed.")
    else:
        print("Gallery file not found.")

    # 2. Update READMEs in look folders
    ele_path = os.path.join(REPO_PATH, "05_Imagenes", "ele")
    readme_count = 0
    ref_count = 0
    
    for root, dirs, files in os.walk(ele_path):
        if "README.md" in files:
            readme_path = os.path.join(root, "README.md")
            with open(readme_path, "r", encoding="utf-8") as f:
                r_content = f.read()
                
            original_content = r_content
            for old_path in sorted_old_paths:
                new_path = mapping[old_path]
                # In folder READMEs, links are often relative or filenames only
                # But we standardized filenames too.
                old_fname = old_path.split("/")[-1]
                new_fname = new_path.split("/")[-1]
                
                if old_fname in r_content:
                    r_content = r_content.replace(old_fname, new_fname)
                    ref_count += 1
            
            if r_content != original_content:
                with open(readme_path, "w", encoding="utf-8") as f:
                    f.write(r_content)
                readme_count += 1

    print(f"READMEs updated: {readme_count} files, {ref_count} filename references.")

if __name__ == "__main__":
    sync()
