import os
import re

# Rutas
base_dir = r"c:\Users\farid\LaVouteDAnais"
proceso_dir = os.path.join(base_dir, "03_Literatura", "02_Finalizadas", "la_app_la_bimboficacion_de_mi_novio", "_proceso")
dest_dir = os.path.join(base_dir, "03_Literatura", "02_Finalizadas", "la_app_la_bimboficacion_de_mi_novio")
publicacion_dir = os.path.join(dest_dir, "_publicacion")

# Metadata común
universo = "La Voûte d'Anaïs"
tematicas = "#Bimboficación #FeminizaciónForzada #ControlMental #Hipnosis #Chile #Látex"
perspectiva = "Primera Persona Alternada (Catalina / Tomás)"
intensidad = "Extrema"

# Datos específicos por capítulo, incluyendo las invitaciones personalizadas
caps_data = [
    {
        "num": 1,
        "src_file": "capitulo_01_la_instalacion_v0.3.md",
        "dest_base": "capitulo_1_la_instalacion",
        "teaser": "Catalina le instala a su pololo una app para transformarlo en su criada sumisa. Se divierte dominándolo, sin sospechar que el aparato también la calibra a ella. La racha acaba de iniciarse, y Tomás ya empieza a sentir el primer calor de la obediencia en su boca.",
        "conteo": "~3,500",
        "invitacion": """
¿Sentiste la tentación de que alguien decida por ti al primer click? ¿Te imaginas cediendo a una racha diaria que no puedes parar?

Si esta historia despertó tu morbo por ceder el control o por calibrar a quien tienes al lado, quiero saberlo. Escríbeme.

*Dis-moi ce que tu désires vraiment.*

*Mantén tu pantalla encendida. La racha continúa en el Capítulo 2.*

📧 anais.belland@outlook.com

*Avec dévotion obscure,*
**Anaïs Belland**
"""
    },
    {
        "num": 2,
        "src_file": "capitulo_02_la_racha_v0.6.md",
        "dest_base": "capitulo_2_la_racha",
        "teaser": "Al cuarto día de la racha, el cuerpo de Tomás empieza a transformarse visiblemente a la vista de Catalina: pechos de silicona y una boca que ya no es de hombre. Catalina goza de su sumisión en el cruce de la racha, sin ver la trampa que se cierra en su propio espejo.",
        "conteo": "~9,000",
        "invitacion": """
¿Sentiste el calor líquido en tu vientre cada vez que Tomás perdía su masculinidad en el espejo? ¿Se te aceleró el pulso al ver a Catalina gozar del control mientras la trampa se cerraba?

Si esta historia despertó tus ganas de dejarte moldear o de ver caer a quien cree mandar, quiero saberlo. Escríbeme.

*Dis-moi ce que tu désires vraiment.*

*No rompas la racha. El nivel definitivo se desbloquea en el Capítulo 3.*

📧 anais.belland@outlook.com

*Avec dévotion obscure,*
**Anaïs Belland**
"""
    },
    {
        "num": 3,
        "src_file": "capitulo_03_el_nivel_v0.5.md",
        "dest_base": "capitulo_3_el_nivel",
        "teaser": "Tomás ya viste el uniforme de criada, pero Catalina decide humillarlo una última vez antes de que la racha del Nivel Dos los alcance a ambos. Un clímax de inversión completa donde el control se evapora. En este juego de obediencia, subir de nivel es hundirse.",
        "conteo": "~5,200",
        "invitacion": """
¿Sentiste el calor en tu vientre cada vez que Tomás obedecía en uniforme? ¿Se te erizó la piel al ver a Catalina perder el control creyendo que mandaba?

Si tu cuerpo también arde por ser calibrado bajo mi racha, quiero saberlo. Escríbeme.

*Dis-moi ce que tu désires vraiment.*

📧 anais.belland@outlook.com

*Avec dévotion obscure,*
**Anaïs Belland**
"""
    }
]

# Función mejorada para convertir MD a HTML body-only
def md_to_html(md_text):
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
            text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)
            text = re.sub(r"\*(.*?)\*", r"<em>\1</em>", text)
            html_lines.append(f"<p>{text}</p>")
            current_paragraph.clear()

    for line in lines:
        line_stripped = line.strip()
        
        # Si es un encabezado <h2> o <h1>
        if line_stripped.startswith("## ") or line_stripped.startswith("# "):
            flush_paragraph()
            prefix_len = 3 if line_stripped.startswith("## ") else 2
            heading_text = line_stripped[prefix_len:].strip()
            tag = "h2" if prefix_len == 3 else "h1"
            html_lines.append(f"<{tag}>{heading_text}</{tag}>")
        
        # Si es un separador <hr>
        elif line_stripped == "---":
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

for cap in caps_data:
    # 1. Leer archivo original desde _proceso/
    src_path = os.path.join(proceso_dir, cap["src_file"])
    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read().strip()
    
    # Remover el título del capítulo (# Capítulo X...)
    lines = content.split("\n")
    if lines[0].startswith("# "):
        content = "\n".join(lines[1:]).strip()
    
    # Calcular palabras exactas
    words_count = len(content.split())
    rounded_words = f"~{int(round(words_count, -2)):,}"
    
    # 2. Construir cabecera (Título corto limitado a Capítulo X como máximo)
    cabecera_cap = f"""*Un relato de Anaïs Belland*

# La app: La bimboficación de mi novio — Capítulo {cap["num"]}

---

**Universo:** {universo}
**Temáticas:** {tematicas}
**Palabras:** {rounded_words}
**Perspectiva:** {perspectiva}
**Intensidad:** {intensidad}

---

**{cap["teaser"]}**

<!-- more -->

---

"""
    # 3. Unir todo
    relato_cap_md = cabecera_cap + content + "\n\n**Fin**\n" + cap["invitacion"]
        
    # 4. Guardar archivo Markdown
    dest_md_path = os.path.join(dest_dir, f"{cap['dest_base']}.md")
    with open(dest_md_path, "w", encoding="utf-8") as f:
        f.write(relato_cap_md)
    print(f"MD Guardado: {dest_md_path} ({rounded_words} palabras)")
    
    # 5. Guardar archivo HTML
    html_body = md_to_html(relato_cap_md)
    dest_html_path = os.path.join(publicacion_dir, f"{cap['dest_base']}.html")
    with open(dest_html_path, "w", encoding="utf-8") as f:
        f.write(html_body)
    print(f"HTML Guardado: {dest_html_path}")

print("Compilación capítulo a capítulo con títulos cortos completada exitosamente.")
