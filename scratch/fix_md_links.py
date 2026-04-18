import os
import re

ele_path = r'C:\Users\farid\LaVouteDAnais\05_Imagenes\ele'
md_files = [
    r'C:\Users\farid\LaVouteDAnais\00_Ele\galeria_outfits.md',
    r'C:\Users\farid\LaVouteDAnais\00_Ele\galeria_outfits_era_gotica.md'
]

# 1. Map physical files
# physical_map[look_num][pose_type] = filename
physical_map = {}
look_pattern = re.compile(r'look(\d+)', re.IGNORECASE)

for folder in os.listdir(ele_path):
    m = look_pattern.match(folder)
    if m:
        num = int(m.group(1))
        physical_map[num] = {}
        full_folder = os.path.join(ele_path, folder)
        if os.path.isdir(full_folder):
            for f in os.listdir(full_folder):
                if f.endswith('.png') or f.endswith('.jpg'):
                    # Check for pose in filename
                    for pose in ['standing', 'seated', 'back', 'profile', 'ditzy', 'portrait', 'detail', 'sitting', 'selfie', 'frontal', 'hero']:
                        if pose in f.lower():
                            physical_map[num][pose] = f
                            break

# 2. Function to fix links in a line
def fix_links(line, current_look_num):
    # Regex for standard image links in MD
    # ![Pose](https://.../lookXXX_desc/filename.png)
    link_pattern = re.compile(r'!\[(.*?)\]\((.*?)\)')
    
    def replacer(match):
        label = match.group(1).lower()
        url = match.group(2)
        
        # Try to identify look number from URL if not provided by context
        url_look_match = re.search(r'look(\d+)', url)
        look_num = int(url_look_match.group(1)) if url_look_match else current_look_num
        
        if look_num in physical_map:
            # Match label to pose type
            pose_type = "unknown"
            if "standing" in label or "frontal" in label: pose_type = "standing"
            elif "seated" in label or "sitting" in label: pose_type = "seated"
            elif "back" in label: pose_type = "back"
            elif "profile" in label or "side" in label: pose_type = "profile"
            elif "ditzy" in label: pose_type = "ditzy"
            
            if pose_type in physical_map[look_num]:
                new_filename = physical_map[look_num][pose_type]
                # Replace filename in URL
                new_url = re.sub(r'/[^/]+\.(png|jpg)\)$', f'/{new_filename})', url + ")")[:-1]
                return f"![{match.group(1)}]({new_url})"
        
        return match.group(0)

    return link_pattern.sub(replacer, line)

# 3. Process MD files
for md_path in md_files:
    if not os.path.exists(md_path): continue
    
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    current_look = None
    
    for line in lines:
        # Detect current look context
        look_hdr_match = re.search(r'## .*?Look (\d+)', line)
        if look_hdr_match:
            current_look = int(look_hdr_match.group(1))
        
        if "![" in line and "https://" in line:
            line = fix_links(line, current_look)
        
        new_lines.append(line)
    
    with open(md_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

print("Markdown links updated successfully.")
