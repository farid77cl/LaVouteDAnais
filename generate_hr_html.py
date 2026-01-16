# -*- coding: utf-8 -*-
"""
Genera HTML limpio de HR: Human Repurposing
Solo cuerpo narrativo, formato Dollhouse 2026
"""
import re
from pathlib import Path

source_dir = Path(r"C:\Users\fabara\LaVouteDAnais\03_Literatura\en_progreso\hr_human_repurposing")
target_path = Path(r"C:\Users\fabara\LaVouteDAnais\03_Literatura\finalizadas\html\hr_human_repurposing.html")

chapters = [
    "capitulo_01.md",
    "capitulo_02.md", 
    "capitulo_03.md",
    "capitulo_04.md",
    "epilogo.md"
]

def clean_metadata(content):
    """Elimina metadatos de capítulo y títulos de secciones"""
    # Eliminar línea de título del capítulo
    content = re.sub(r'^#\s*HR:.*?\n', '', content, flags=re.MULTILINE)
    content = re.sub(r'^#\s*NEXUM:.*?\n', '', content, flags=re.MULTILINE)
    # Eliminar metadatos
    content = re.sub(r'\*\*Estado:\*\*.*?\n', '', content)
    content = re.sub(r'\*\*Palabras:\*\*.*?\n', '', content)
    content = re.sub(r'\*\*Fecha:\*\*.*?\n', '', content)
    # Eliminar "Continuará en Capítulo X"
    content = re.sub(r'>\s*\*Continuará.*?\n', '', content)
    # Eliminar firma Helena
    content = re.sub(r'\*Helena de Anaïs\*.*', '', content, flags=re.DOTALL)
    # Eliminar títulos de secciones como "## I. EL ANALISTA VALIOSO" o "## III. LA REUNIÓN"
    content = re.sub(r'^##\s+[IVXLCDM]+\.\s+.*$', '', content, flags=re.MULTILINE)
    # Eliminar también headers sin numeración romana
    content = re.sub(r'^##\s+PRÓLOGO:.*$', '', content, flags=re.MULTILINE)
    content = re.sub(r'^##\s+EPÍLOGO:.*$', '', content, flags=re.MULTILINE)
    return content

def md_to_html(content):
    """Convierte Markdown básico a HTML"""
    # Encabezados ## restantes -> separadores con título centrado
    content = re.sub(r'^##\s+(.+)$', r'<hr>\n<p align="center"><strong>\1</strong></p>\n<hr>', content, flags=re.MULTILINE)
    
    # Blockquotes > *texto* -> caja de cita
    content = re.sub(r'^>\s*\*(.+?)\*\s*$', r'<blockquote style="background:#f8f0ff;border-left:3px solid #9370db;padding:10px;font-style:italic;margin:1em 0;">\1</blockquote>', content, flags=re.MULTILINE)
    content = re.sub(r'^>\s*(.+)$', r'<blockquote style="background:#f8f0ff;border-left:3px solid #9370db;padding:10px;font-style:italic;margin:1em 0;">\1</blockquote>', content, flags=re.MULTILINE)
    
    # Líneas horizontales
    content = re.sub(r'^---+$', '<hr>', content, flags=re.MULTILINE)
    
    # Negritas y cursivas
    content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', content)
    content = re.sub(r'\*(.+?)\*', r'<em>\1</em>', content)
    
    # Párrafos - cada línea no vacía que no empiece con < se envuelve
    lines = content.split('\n')
    html_lines = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            html_lines.append('')
        elif stripped.startswith('<'):
            html_lines.append(line)
        elif stripped.startswith('—'):
            # Diálogos
            html_lines.append(f'<p>{stripped}</p>')
        else:
            html_lines.append(f'<p>{stripped}</p>')
    
    content = '\n'.join(html_lines)
    
    # Limpiar múltiples líneas vacías
    content = re.sub(r'\n{3,}', '\n\n', content)
    # Limpiar párrafos vacíos
    content = re.sub(r'<p>\s*</p>', '', content)
    
    return content

# Nota de la autora
NOTA_AUTORA = """
<hr style="border:2px solid #9370db;margin:3em 0;">

<p align="center" style="border:2px solid #9370db;padding:20px;background:#f8f0ff;max-width:600px;margin:0 auto;">
<strong>Nota de la Autora</strong><br><br>
¿Sentiste el frío del látex en tu piel, <em>mon cher</em>? ¿O fue el alivio de Dahlia al soltar por fin el peso de su antigua vida lo que resonó en ti?<br><br>
NEXUM no solo fabrica empleados, fabrica deseos. Si la transformación de Daniel —su caída y su renacimiento como el objeto perfecto de Marcus— despertó algo oscuro en tu interior, confésalo.<br><br>
<em>Dis-moi, as-tu déjà rêvé de te perdre pour mieux te trouver ?</em><br><br>
📧 anais.belland@outlook.com<br><br>
<em>Avec dévotion obscure,</em><br>
<strong>Anaïs Belland</strong>
</p>
"""

# Generar HTML
html_parts = []

for chapter_file in chapters:
    filepath = source_dir / chapter_file
    if filepath.exists():
        content = filepath.read_text(encoding='utf-8')
        content = clean_metadata(content)
        content = md_to_html(content)
        html_parts.append(content)
        html_parts.append('\n<hr style="border:2px solid #ff1493;margin:2em 0;">\n')

# Unir todo
full_html = '\n'.join(html_parts)

# Eliminar último separador rosa y agregar nota de autora
full_html = re.sub(r'<hr style="border:2px solid #ff1493;margin:2em 0;">\s*$', '', full_html)
full_html += NOTA_AUTORA

# Guardar con encoding UTF-8 y BOM para compatibilidad
target_path.write_text(full_html, encoding='utf-8-sig')

print(f"✅ HTML generado: {target_path}")
print(f"   Tamaño: {target_path.stat().st_size / 1024:.1f} KB")
