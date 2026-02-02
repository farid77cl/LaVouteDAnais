import os
import re
from pathlib import Path

BANCOS_DIR = Path(r"C:\Users\fabara\LaVouteDAnais\00_Helena\bancos_prompts")

def check_syntax(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check code blocks
    blocks = re.findall(r'```', content)
    imbalanced = len(blocks) % 2 != 0
    
    # Check open alerts
    alerts_open = len(re.findall(r'> \[!', content))
    # This is harder to check for closing as they are line-based
    
    return imbalanced, len(blocks)

def main():
    banks = sorted(BANCOS_DIR.glob("banco_prompts_v*.md"))
    error_count = 0
    
    print(f"Auditing {len(banks)} files...")
    for bank in banks:
        imbalanced, total_blocks = check_syntax(bank)
        if imbalanced:
            print(f"❌ {bank.name}: Imbalanced code blocks ({total_blocks} total)")
            error_count += 1
        # Optional: check for prompts without text tag
        if '```\n' in bank.read_text(encoding='utf-8') and '### Prompt' in bank.read_text(encoding='utf-8'):
            pass # Script existing fixes this
            
    if error_count == 0:
        print("✅ No imbalanced code blocks detected.")
    else:
        print(f"⚠️ Found {error_count} files with syntax errors.")

if __name__ == "__main__":
    main()
