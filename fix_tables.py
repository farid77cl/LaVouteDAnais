import re

filepath = r'c:\Users\farid\LaVouteDAnais\00_Ele\galeria_outfits.md'
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
i = 0
replaced = 0

while i < len(lines):
    line = lines[i]
    stripped = line.strip().replace('*', '')
    
    if 'Pose' in stripped and '|' in stripped and stripped.startswith('|'):
        images = []
        j = i + 1
        table_ended = False
        
        while j < len(lines):
            row_stripped = lines[j].strip()
            
            if row_stripped == '':
                j += 1
                continue
                
            if row_stripped.startswith('|'):
                # Try to extract image
                m = re.search(r'!\[.*?\]\((.*?)\)', row_stripped)
                if m:
                    images.append(m.group(1))
                else:
                    m2 = re.search(r'\[.*?\]\((.*?)\)', row_stripped)
                    if m2:
                        images.append(m2.group(1))
                    else:
                        m3 = re.search(r'<img.*?src=\"(.*?)\"', row_stripped)
                        if m3:
                            images.append(m3.group(1))
                j += 1
            else:
                table_ended = True
                break
                
        if images:
            replaced += 1
            new_lines.append('``carousel\n')
            for k, img_url in enumerate(images):
                new_lines.append('![](' + img_url + ')\n')
                if k < len(images) - 1:
                    new_lines.append('<!-- slide -->\n')
            new_lines.append('``\n\n')
            i = j
            continue

    new_lines.append(line)
    i += 1

print('Replaced tables:', replaced)

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
