import os
import re

# Rutas de origen y destino
base_dir = r"c:\Users\farid\LaVouteDAnais"
src_dir = os.path.join(base_dir, "03_Literatura", "01_En_Progreso", "la_app")
dest_dir = os.path.join(base_dir, "03_Literatura", "02_Finalizadas", "la_app_la_bimboficacion_de_mi_novio")

# Título y metadatos
titulo = "La app: La bimboficación de mi novio"
teaser = "Una app de obediencia, una racha que Tomás no debe romper y una polola que se divierte dominándolo. Catalina cree que tiene el control de su transformación, pero la calibración de la app exige avanzar de nivel. Y en este juego, subir de nivel es hundirse."

cabecera = f"""*Un relato de Anaïs Belland*

# {titulo}

---

**Universo:** La Voûte d'Anaïs
**Temáticas:** #Bimboficación #FeminizaciónForzada #ControlMental #Hipnosis #Chile #Látex
**Palabras:** 19,928
**Perspectiva:** Primera Persona Alternada (Catalina / Tomás)
**Intensidad:** Extrema

---

**{teaser}**

<!-- more -->

---
"""

invitacion = """

¿Sentiste el calor en tu vientre cada vez que Tomás obedecía? ¿Se te erizó la piel al ver a Catalina perder el control creyendo que mandaba?

Si tu cuerpo también arde por ser calibrado bajo mi racha, escríbeme.

*Dis-moi ce que tu désires vintage.*

📧 anais.belland@outlook.com

*Avec dévotion obscure,*
**Anaïs Belland**
"""

# Corregir frase en francés a la canónica
invitacion = invitacion.replace("Dis-moi ce que tu désires vintage.", "Dis-moi ce que tu désires vraiment.")

# Leer capítulos
files = [
    ("La instalación", "capitulo_01_la_instalacion_v0.3.md"),
    ("La racha", "capitulo_02_la_racha_v0.6.md"),
    ("El nivel", "capitulo_03_el_nivel_v0.5.md")
]

cuerpo_completo_md = ""

for name, fname in files:
    fpath = os.path.join(src_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read().strip()
    
    # Remover el título del capítulo (# Capítulo X...)
    lines = content.split("\n")
    if lines[0].startswith("# "):
        content = "\n".join(lines[1:]).strip()
    
    cuerpo_completo_md += f"## {name}\n\n{content}\n\n---\n\n"

# Quitar el último separador
cuerpo_completo_md = cuerpo_completo_md.rstrip()[:-3].rstrip()

# Unificar Markdown
relato_md = cabecera + cuerpo_completo_md + "\n\n**Fin**\n" + invitacion

# Crear directorios
os.makedirs(dest_dir, exist_ok=True)
os.makedirs(os.path.join(dest_dir, "_proceso"), exist_ok=True)
os.makedirs(os.path.join(dest_dir, "_publicacion"), exist_ok=True)

# Guardar MD completo
md_path = os.path.join(dest_dir, "la_app_la_bimboficacion_de_mi_novio.md")
with open(md_path, "w", encoding="utf-8") as f:
    f.write(relato_md)

print(f"MD Guardado en {md_path}")

# Función mejorada para convertir Markdown a HTML body-only
def md_to_html(md_text):
    # Separar cabecera MD, quedarnos solo con lo que va después de <!-- more -->
    parts = md_text.split("<!-- more -->\n\n---")
    if len(parts) > 1:
        body_md = parts[1].strip()
    else:
        body_md = md_text.strip()
    
    lines = body_md.split("\n")
    html_lines = []
    current_paragraph = []

    def flush_paragraph():
        if current_paragraph:
            text = " ".join(current_paragraph).strip()
            # Aplicar formato en línea
            # Negritas **texto** -> <strong>texto</strong>
            text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)
            # Cursivas *texto* -> <em>texto</em>
            text = re.sub(r"\*(.*?)\*", r"<em>\1</em>", text)
            # Caracteres de trigger
            html_lines.append(f"<p>{text}</p>")
            current_paragraph.clear()

    for line in lines:
        line_stripped = line.strip()
        
        # Si es un encabezado <h2>
        if line_stripped.startswith("## "):
            flush_paragraph()
            heading_text = line_stripped[3:].strip()
            html_lines.append(f"<h2>{heading_text}</h2>")
        
        # Si es un separador <hr>
        elif line_stripped == "---" or line_stripped == "---":
            flush_paragraph()
            html_lines.append("<hr>")
            
        # Si es una línea vacía
        elif not line_stripped:
            flush_paragraph()
            
        # Si es texto normal
        else:
            current_paragraph.append(line_stripped)
            
    # Flush final
    flush_paragraph()
            
    return "\n\n".join(html_lines)

html_body = md_to_html(relato_md)

# Guardar HTML body-only
html_path = os.path.join(dest_dir, "_publicacion", "la_app_la_bimboficacion_de_mi_novio.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_body)

print(f"HTML Guardado en {html_path}")

# Copiar archivos originales a _proceso
import shutil
for _, fname in files:
    shutil.copy2(os.path.join(src_dir, fname), os.path.join(dest_dir, "_proceso", fname))
shutil.copy2(os.path.join(src_dir, "canon_relato.md"), os.path.join(dest_dir, "_proceso", "canon_relato.md"))
shutil.copy2(os.path.join(src_dir, "cronologia.md"), os.path.join(dest_dir, "_proceso", "cronologia.md"))
if os.path.exists(os.path.join(src_dir, f"nota_capitulo_01_la_instalacion_v0.3.md")):
    shutil.copy2(os.path.join(src_dir, f"nota_capitulo_01_la_instalacion_v0.3.md"), os.path.join(dest_dir, "_proceso", f"nota_capitulo_01_la_instalacion_v0.3.md"))

print("Archivos de proceso copiados exitosamente.")
