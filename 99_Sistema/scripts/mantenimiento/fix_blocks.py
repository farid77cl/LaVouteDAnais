#!/usr/bin/env python3
"""Fix code block closures: ```text → ```"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

BANCOS_DIR = Path(r"C:\Users\fabara\LaVouteDAnais\00_Helena\bancos_prompts")

count = 0
for bank in sorted(BANCOS_DIR.glob("banco_prompts_v*.md")):
    with open(bank, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix: ```text at end of blocks should be ```
    new_content = re.sub(r'```text(\r?\n\r?\n### Prompt)', r'```\1', content)
    new_content = re.sub(r'```text(\r?\n\r?\n---)', r'```\1', new_content)
    new_content = re.sub(r'```text(\r?\n\r?\n## )', r'```\1', new_content)
    new_content = re.sub(r'```text(\r?\n\r?\n\*)', r'```\1', new_content)
    new_content = re.sub(r'```text(\r?\n$)', r'```\1', new_content)
    new_content = re.sub(r'```text\r?\n\Z', '```\n', new_content)
    
    if new_content != content:
        with open(bank, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✅ {bank.name}: bloques corregidos")
        count += 1
    else:
        print(f"⏭️ {bank.name}: sin cambios")

print(f"\n{'='*40}\nTotal: {count} archivos corregidos")
