import os

path = r'c:\Users\farid\LaVouteDAnais\README.md'
with open(path, 'rb') as f:
    raw = f.read()

content = raw.decode('utf-8', 'ignore')
content = content.replace('â”‚', '│')
content = content.replace('â”œâ”€â”€', '├──')
content = content.replace('â””â”€â”€', '└──')
content = content.replace('â”', '│')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Fixed README.md encoding")
