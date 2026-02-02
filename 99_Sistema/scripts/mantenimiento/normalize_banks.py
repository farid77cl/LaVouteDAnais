#!/usr/bin/env python3
"""
Script para normalizar el formato de todos los bancos de prompts.
Convierte:
  #### [Nombre] - [Título] 🆕
  ```
  [prompt]
  ```

A:
  ### Prompt X: [Título]
  
  ```text
  [prompt]
  ```
"""

import re
import os
import sys
from pathlib import Path

# Fix Windows console encoding
sys.stdout.reconfigure(encoding='utf-8')


BANCOS_DIR = Path(r"C:\Users\fabara\LaVouteDAnais\00_Helena\bancos_prompts")

def normalize_bank(filepath: Path) -> tuple[int, int]:
    """
    Normaliza un banco de prompts al formato estándar.
    Returns: (prompts_encontrados, prompts_normalizados)
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Patrón para encontrar prompts en formato antiguo
    # #### [Personaje] - [Título] [emojis opcionales]
    # ```
    # [prompt]
    # ```
    old_pattern = r'####\s+([^\n]+?)\s*\n\n```\n([^`]+)\n```'
    
    matches = list(re.finditer(old_pattern, content))
    
    if not matches:
        # Intentar otro patrón: #### N. [Título]
        old_pattern2 = r'####\s+(\d+)\.\s+([^\n]+?)\s*\n\n```\n([^`]+)\n```'
        matches2 = list(re.finditer(old_pattern2, content))
        
        if matches2:
            # Ya tiene números, solo necesita cambiar #### por ### Prompt X:
            for i, match in enumerate(reversed(matches2)):
                num = match.group(1)
                title = match.group(2).strip()
                prompt_text = match.group(3)
                
                new_format = f'### Prompt {num}: {title}\n\n```text\n{prompt_text}\n```'
                content = content[:match.start()] + new_format + content[match.end():]
            
            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                return (len(matches2), len(matches2))
        
        return (0, 0)
    
    # Reemplazar cada match con el nuevo formato
    prompt_counter = 1
    for match in reversed(matches):  # Reversed para no afectar los índices
        title = match.group(1).strip()
        # Limpiar emojis del título
        title = re.sub(r'\s*(🆕|💎|⭐|⚠️)\s*', '', title).strip()
        prompt_text = match.group(2)
        
        new_format = f'### Prompt {prompt_counter}: {title}\n\n```text\n{prompt_text}\n```'
        content = content[:match.start()] + new_format + content[match.end():]
        prompt_counter += 1
    
    # También normalizar bloques ``` a ```text
    content = re.sub(r'```\n([^`]+)\n```', r'```text\n\1\n```', content)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return (len(matches), len(matches))
    
    return (len(matches), 0)

def main():
    print("="*60)
    print("NORMALIZADOR DE BANCOS DE PROMPTS")
    print("="*60)
    
    # Encontrar todos los bancos
    banks = sorted(BANCOS_DIR.glob("banco_prompts_v*.md"))
    
    total_found = 0
    total_normalized = 0
    
    for bank in banks:
        found, normalized = normalize_bank(bank)
        total_found += found
        total_normalized += normalized
        
        status = "✅ NORMALIZADO" if normalized > 0 else ("⏭️ YA OK" if found == 0 else "⚠️ SIN CAMBIOS")
        print(f"{bank.name}: {found} prompts encontrados, {normalized} normalizados {status}")
    
    print("="*60)
    print(f"TOTAL: {total_found} prompts encontrados, {total_normalized} normalizados")
    print("="*60)

if __name__ == "__main__":
    main()
