import os
import re

md_path = r"c:\Users\farid\LaVouteDAnais\03_Literatura\01_En_Progreso\manos_de_la_ama\capitulo_1_manos_de_la_ama_v0.8.md"
out_dir = r"c:\Users\farid\LaVouteDAnais\03_Literatura\01_En_Progreso\manos_de_la_ama\_publicacion"
out_path = os.path.join(out_dir, "cartas_a_anais_obtuve_lo_que_pedi.html")

os.makedirs(out_dir, exist_ok=True)

with open(md_path, "r", encoding="utf-8") as f:
    text = f.read()

# Split into paragraphs by double newlines
lines = text.split("\n")

header_html = """<p><em>Un relato de Anaïs Belland</em></p>

<h1>Cartas a Anaïs: Obtuve lo que pedí</h1>

<hr>

<p><strong>Universo:</strong> La Voûte d'Anaïs<br><strong>Temáticas:</strong> #Bimbofication #MtF #Femdom #Chastity #LaVouteDAnais #FeminizaciónForzada #StrapOn #BDSM #Transformación #EsposaDominante<br><strong>Palabras:</strong> ~8.083<br><strong>Perspectiva:</strong> Tercera persona omnisciente<br><strong>Intensidad:</strong> Extrema</p>

<hr>

<p><strong>Le escribí a La Voûte d'Anaïs confesando mi matrimonio sin deseo y rogando entregar el control de mi vida. Obtuve exactamente lo que pedí... pero jamás imaginé la sorpresa que me esperaba al cruzar esa puerta.</strong></p>

<!-- more -->

<hr>

"""

body_parts = []

for line in lines:
    line_str = line.strip()
    if not line_str:
        continue
    if line_str.startswith("# "):
        # Skip top H1 title
        continue
    if line_str == "---":
        body_parts.append("<hr>")
        continue
    
    # Process markdown formatting (bold, italic)
    # **bold** -> <strong>bold</strong>
    # *italic* -> <em>italic</em>
    processed = line_str
    processed = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', processed)
    processed = re.sub(r'(?<!\*)\*(?!\*)(.*?)(?<!\*)\*(?!\*)', r'<em>\1</em>', processed)
    processed = re.sub(r'_(.*?)_', r'<em>\1</em>', processed)
    
    body_parts.append(f"<p>{processed}</p>")

full_html = header_html + "\n".join(body_parts) + "\n"

with open(out_path, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"HTML generado exitosamente en {out_path} ({len(full_html)} bytes)")
