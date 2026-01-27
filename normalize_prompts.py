import os
import re

# Directorio de bancos
directory = r"C:\Users\fabara\LaVouteDAnais\00_Helena\bancos_prompts"

# Archivos a procesar (v55 en adelante)
files_to_process = [
    "banco_prompts_v55_shiny_influencer.md",
    "banco_prompts_v56_eternal_loop.md",
    "banco_prompts_v57_precious_metals.md",
    "banco_prompts_v58_oh_polly_rainbow.md",
    "banco_prompts_v59_animal_print.md",
    "banco_prompts_v60_bikini_lingerie_metals.md",
    "banco_prompts_v61_corporate_plastic.md",
    "banco_prompts_v62_high_gloss_gym.md",
    "banco_prompts_v63_mixed_fetish_dynamic.md",
    "banco_prompts_v64_miss_doll_animal_fashion.md",
    "banco_prompts_v67_red_carpet_paparazzi.md"
]

def normalize_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Eliminar "Prompt X: " de los títulos
        # Busca "### Prompt \d+: Texto" y lo reemplaza por "### Texto"
        content = re.sub(r'### Prompt \d+:\s*(.+)', r'### \1', content)

        # 2. Eliminar líneas de Evaluación
        # Busca líneas que empiecen con "**Eval:**" y las elimina
        content = re.sub(r'\*\*Eval:\*\*.*\n', '', content)
        content = re.sub(r'\*\*Eval:\*\*.*', '', content) # Por si está al final sin salto

        # 3. Eliminar nota de sistema de evaluación
        # Busca el bloque > [!NOTE] hasta el final del bloque
        note_pattern = r'> \[!NOTE\]\n> \*\*Sistema de Evaluación:\*\*(\n> - .*)+'
        content = re.sub(note_pattern, '', content)
        
        # Eliminar líneas vacías extra que puedan haber quedado tras borrar la nota
        content = re.sub(r'\n\n\n+', '\n\n', content)

        # 4. Asegurar "Vertical portrait orientation." al final del bloque de código
        # Estrategia: Buscar bloques ```text ... ``` y asegurar que terminen con la frase.
        def fix_prompt_block(match):
            block_content = match.group(1)
            if "Vertical portrait orientation" not in block_content:
                # Si termina en newline, agregar la frase.
                block_content = block_content.rstrip() + " Vertical portrait orientation.\n"
            return f"```text{block_content}```"

        content = re.sub(r'```text(.*?)```', fix_prompt_block, content, flags=re.DOTALL)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Propagado formato a: {os.path.basename(filepath)}")

    except Exception as e:
        print(f"Error procesando {filepath}: {e}")

print("Iniciando normalización de bancos v55+...")
for filename in files_to_process:
    normalize_file(os.path.join(directory, filename))
print("Normalización completada.")
