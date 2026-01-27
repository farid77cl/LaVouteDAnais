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
    # Extraer desde "## I. CANON VISUAL OBLIGATORIO" hasta "## II. PROMPTS"
    match = re.search(r'(## I\. CANON VISUAL OBLIGATORIO.*?)## II\. PROMPTS', template_content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None

def extract_prompts_section(file_content):
    # Intentar encontrar donde empiezan los prompts reales
    # Opcion 1: Buscar "## II. PROMPTS" si ya existe
    if "## II. PROMPTS" in file_content:
        # Extraer todo desde ahí hasta el final (o hasta Notas)
        parts = file_content.split("## II. PROMPTS", 1)
        # Check si hay sección III
        body = parts[1]
        if "## III. NOTAS" in body:
            body = body.split("## III. NOTAS")[0]
        return body.strip()
    
    # Opcion 2: Si no tiene estructura nueva, buscar headers antiguos
    # En archivos antiguos, los prompts suelen empezar despues del primer separador ---
    # Pero cuidado, el header tiene ---
    
    # Estrategia segura: Buscar el primer "### " que indica un prompt
    match = re.search(r'(### .+)', file_content)
    if match:
        start_pos = match.start()
        # Encontrar hasta donde llegan (evitar footer)
        # Asumimos que los prompts llegan hasta el final o hasta Notas
        content_from_first_prompt = file_content[start_pos:]
        if "## III. NOTAS" in content_from_first_prompt:
            content_from_first_prompt = content_from_first_prompt.split("## III. NOTAS")[0]
        if "*🦇 Helena de Anaïs" in content_from_first_prompt:
             content_from_first_prompt = content_from_first_prompt.split("*🦇 Helena de Anaïs")[0]
             
        return content_from_first_prompt.strip()
        
    return ""

def generate_optimized_content(original_content, canon_section, filename):
    # Obtener Metadatos del archivo original (Titulo y descripcion)
    header_lines = []
    lines = original_content.split('\n')
    for line in lines[:20]: # Buscar en las primeras lineas
        if line.startswith("# "):
            header_lines.append(line)
        elif line.startswith("> **Descripción:") or line.startswith("**Referencia Visual:**") or line.startswith("**Estética:**"):
             # Adaptar al formato de plantilla si es posible, o guardar raw
             header_lines.append(line)
             
    # Si no encontramos titulo #, usar nombre de archivo
    title = header_lines[0] if header_lines and header_lines[0].startswith("# ") else f"# 🖤 BANCO DE PROMPTS - {filename}"
    
    # Construir nuevo contenido
    new_content = f"{title}\n\n"
    
    # Metadata block style from template
    new_content += "> **USO:** Copiar el texto del prompt directamente y pegar en el generador de imágenes.\n"
    new_content += "> **Estado:** Optimizado v2.0 (Sensuality Protocol)\n\n"
    new_content += "---\n\n"
    new_content += "## 📋 CÓMO USAR ESTE ARCHIVO\n\n"
    new_content += "1. **Buscar** el personaje y outfit deseado\n"
    new_content += "2. **Copiar** todo el texto del prompt\n"
    new_content += "3. **Pegar** directamente en el generador\n\n"
    new_content += "---\n\n"
    
    # Insertar CANON
    new_content += f"{canon_section}\n\n"
    new_content += "---\n\n"
    
    # Insertar PROMPTS
    prompts_body = extract_prompts_section(original_content)
    
    # Normalización extra de prompts por si acaso
    # Asegurar que no haya "Prompt X:"
    prompts_body = re.sub(r'### Prompt \d+:\s*', '### ', prompts_body)
    
    new_content += "## II. PROMPTS DEL BANCO\n\n"
    new_content += prompts_body + "\n\n"
    
    new_content += "---\n\n"
    new_content += "## III. NOTAS Y VARIACIONES\n\n"
    new_content += "- **Fondo Sugerido:** Studio lighting, Club neon, Luxury interior.\n"
    new_content += "- **Expresión:** Seductive, Dominant, Vacant.\n\n"
    new_content += "---\n\n"
    new_content += "*🦇 Helena de Anaïs — La Voûte d'Anaïs*\n"
    
    return new_content

def main():
    print("Leyendo plantilla...")
    template_content = read_file(TEMPLATE_FILE)
    canon_section = extract_canon_section(template_content)
    
    if not canon_section:
        print("ERROR: No se pudo extraer la sección CANON de la plantilla.")
        return

    print("Procesando archivos...")
    for filename in TARGET_FILES:
        filepath = os.path.join(DIRECTORY, filename)
        if not os.path.exists(filepath):
            print(f"Skipping {filename} (Not found)")
            continue
            
        print(f"Optimizando: {filename}")
        original_content = read_file(filepath)
        
        optimized_content = generate_optimized_content(original_content, canon_section, filename)
        
        write_file(filepath, optimized_content)
        print(f"Guardado: {filename}")

if __name__ == "__main__":
    main()
