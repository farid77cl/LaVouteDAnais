import os
import re

def process_file(file_path, replacements):
    print(f"Procesando: {file_path}")
    if not os.path.exists(file_path):
        print(f"Error: {file_path} no existe.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Aplicar reemplazos de lista
    for target, replacement in replacements:
        content = content.replace(target, replacement)
    
    # 2. Bloque de imágenes para Look 132
    look132_target = """### 📸 Imágenes (0/5 — Pendiente)

| Pose | Previsión |
|------|---------|
| **Standing** | Pendiente |
| **Back View** | Pendiente |
| **Seated** | Pendiente |
| **Side Profile** | Pendiente |
| **Ditzy** | Pendiente |"""
    
    look132_replacement = """### 📸 Imágenes (5/5 — COMPLETO)

| Pose | Archivo |
|------|---------|
| **Standing** | ![Standing](https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/05_Imagenes/ele/look132_emerald_silk_lace/ele_132_standing.png) |
| **Back View** | ![Back View](https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/05_Imagenes/ele/look132_emerald_silk_lace/ele_132_back_view.png) |
| **Seated** | ![Seated](https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/05_Imagenes/ele/look132_emerald_silk_lace/ele_132_seated.png) |
| **Side Profile** | ![Side Profile](https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/05_Imagenes/ele/look132_emerald_silk_lace/ele_132_side_profile.png) |
| **Ditzy** | ![Ditzy](https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/05_Imagenes/ele/look132_emerald_silk_lace/ele_132_ditzy.png) |"""

    # Reemplazar la primera ocurrencia de "Pendiente" (Look 132)
    content = content.replace(look132_target, look132_replacement, 1)

    # 3. Bloque para Look 133
    # Usamos look132_target porque el bloque de texto es idéntico
    look133_replacement = look132_replacement.replace('look132_emerald_silk_lace', 'look133_hot_pink_strings').replace('ele_132', 'ele_133')
    
    # Usamos regex para asegurar que solo reemplazamos el que sigue al Look 133
    # Buscamos la cabecera del 133 y luego el bloque de imágenes
    pattern = r'(## 👙 Look 133: Hot Pink Strings \(14/04/2026\).*?)(### 📸 Imágenes \(0/5 — Pendiente\).*?\| \*\*Ditzy\*\* \| Pendiente \|)'
    
    def repl_func(match):
        return match.group(1) + look133_replacement

    content = re.sub(pattern, repl_func, content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Sincronización de galería completada con éxito.")

# Ejecución
replacements = [('../05_Imagenes/', 'https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/05_Imagenes/')]
process_file('c:/Users/farid/LaVouteDAnais/00_Ele/galeria_outfits.md', replacements)

# Walkthrough fix
walkthrough_path = r'C:\Users\farid\.gemini\antigravity\brain\a6381cbe-dd85-4acd-a9cf-5c19c01b830d\walkthrough.md'
walkthrough_replacements = [('file:///c:/Users/farid/LaVouteDAnais/', 'https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/')]
process_file(walkthrough_path, walkthrough_replacements)
