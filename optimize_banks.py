import os
import re

# Constantes
DIRECTORY = r"C:\Users\fabara\LaVouteDAnais\00_Helena\bancos_prompts"
TEMPLATE_FILE = r"C:\Users\fabara\LaVouteDAnais\00_Helena\bancos_prompts\PLANTILLA_BANCO_PROMPTS.md"

# Archivos objetivo (v55-v67)
TARGET_FILES = [
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

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def extract_canon_section(template_content):
    match = re.search(r'(## I\. CANON VISUAL OBLIGATORIO.*?)## II\. PROMPTS', template_content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def extract_prompts_section_raw(file_content):
    # Encontrar el inicio de los prompts
    # Puede ser "## II. PROMPTS..." o "## II. PROMPTS DEL BANCO" o simplemente el primer prompt
    
    # Intento 1: Header estandarizado
    if "## II. PROMPTS" in file_content:
        parts = file_content.split("## II. PROMPTS", 1)
        # El resto es el cuerpo... pero hay que quitar lo que no sea prompt (Headers, Notes, Footer)
        raw_body = parts[1]
        # Quitar header line (ej: " DEL BANCO\n\n")
        raw_body = raw_body.split('\n', 1)[1]
    else:
        # Intento 2: Buscar primer prompt
        match = re.search(r'(### .+)', file_content)
        if match:
            start_pos = match.start()
            raw_body = file_content[start_pos:]
        else:
            return ""

    # Recortar el final (Notes, Footer)
    if "## III. NOTAS" in raw_body:
        raw_body = raw_body.split("## III. NOTAS")[0]
    if "*🦇 Helena de Anaïs" in raw_body:
        raw_body = raw_body.split("*🦇 Helena de Anaïs")[0]
        
    return raw_body.strip()

def sanitize_prompts_body(body):
    # 1. Eliminar "Prompt X: "
    body = re.sub(r'### Prompt \d+:\s*(.+)', r'### \1', body)
    
    # 2. Eliminar líneas de Evaluación viejas
    body = re.sub(r'\*\*Eval:\*\*.*\n', '', body)
    body = re.sub(r'\*\*Eval:\*\*.*', '', body)

    # 3. Eliminar nota de sistema de evaluación vieja
    note_pattern = r'> \[!NOTE\]\n> \*\*Sistema de Evaluación:\*\*(\n> - .*)+'
    body = re.sub(note_pattern, '', body)
    
    # 4. Asegurar "Vertical portrait orientation."
    def fix_prompt_block(match):
        block_content = match.group(1)
        if "Vertical portrait orientation" not in block_content:
            block_content = block_content.rstrip() + " Vertical portrait orientation.\n"
        return f"```text{block_content}```"

    body = re.sub(r'```text(.*?)```', fix_prompt_block, body, flags=re.DOTALL)
    
    # 5. Limpiar dobles saltos de línea excesivos
    body = re.sub(r'\n\n\n+', '\n\n', body)
    
    return body

def generate_compliant_content(original_content, canon_section, filename):
    # Extraer titulo original o generar uno
    lines = original_content.split('\n')
    title = lines[0] if lines[0].startswith("# ") else f"# 🖤 BANCO DE PROMPTS - {filename}"
    
    # Construir nuevo contenido siguiendo PLANTILLA_BANCO_PROMPTS.md
    new_content = f"{title}\n\n"
    new_content += "> **USO:** Copiar el texto del prompt directamente y pegar en el generador de imágenes.\n"
    new_content += "> **Estado:** Optimizado v2.0 (Sensuality Protocol)\n\n"
    new_content += "---\n\n"
    
    new_content += "## 📋 CÓMO USAR ESTE ARCHIVO\n\n"
    new_content += "1. **Buscar** el personaje y outfit deseado\n"
    new_content += "2. **Copiar** todo el texto del prompt\n"
    new_content += "3. **Pegar** directamente en el generador\n\n"
    new_content += "---\n\n"
    
    new_content += f"{canon_section}\n\n"
    new_content += "---\n\n"
    
    new_content += "## II. PROMPTS DEL BANCO\n\n"
    
    # Extraer y sanear prompts
    raw_body = extract_prompts_section_raw(original_content)
    clean_body = sanitize_prompts_body(raw_body)
    
    new_content += clean_body + "\n\n"
    
    new_content += "---\n\n"
    new_content += "## III. NOTAS Y VARIACIONES\n\n"
    new_content += "- **Fondo Sugerido:** Studio lighting, Club neon, Luxury interior.\n"
    new_content += "- **Expresión:** Seductive, Dominant, Vacant.\n\n"
    new_content += "---\n\n"
    new_content += "*🦇 Helena de Anaïs — La Voûte d'Anaïs*\n"
    
    return new_content

def main():
    print("Leyendo plantilla maestra...")
    template_content = read_file(TEMPLATE_FILE)
    canon_section = extract_canon_section(template_content)
    
    if not canon_section:
        print("ERROR CRÍTICO: No se pudo extraer la sección CANON.")
        return

    print("Iniciando estandarización estricta...")
    for filename in TARGET_FILES:
        filepath = os.path.join(DIRECTORY, filename)
        if not os.path.exists(filepath):
            print(f"Saltando {filename} (No encontrado)")
            continue
            
        print(f"Procesando: {filename}")
        original_content = read_file(filepath)
        
        optimized_content = generate_compliant_content(original_content, canon_section, filename)
        
        write_file(filepath, optimized_content)
        print(f"✅ Estandarizado: {filename}")

if __name__ == "__main__":
    main()
