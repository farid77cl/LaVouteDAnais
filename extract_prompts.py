import re

file_path = r"C:\Users\fabara\LaVouteDAnais\00_Helena\bancos_prompts\banco_prompts_v18_pole.md"

try:
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.readlines()
        
    print(f"Total lines: {len(content)}")
    
    found_prompts = []
    
    for line in content:
        line = line.strip()
        if "Miss Doll" in line:
             found_prompts.append(line)

    with open(r"C:\Users\fabara\LaVouteDAnais\miss_doll_prompts.md", 'w', encoding='utf-8') as f:
        f.write("\n".join(found_prompts))
    print("Done.")
             
except Exception as e:
    print(f"Error: {e}")
