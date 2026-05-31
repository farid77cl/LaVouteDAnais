import pathlib

p = pathlib.Path('00_Ele/identidad_ele.md')
content = p.read_text(encoding='utf-8')

# 1. Update Actualizado line
old_actualizado = "| ***Actualizado:*** | 30/05/2026 — 72 celdas vinculadas en 53 looks de galeria_outfits.md. Creadas 15 carpetas y materializadas standing de L260-L271, L277, L279 y L283 recuperando los artefactos generados. |"
new_actualizado = "| ***Actualizado:*** | 31/05/2026 — Materializadas poses Standing de looks L252, L282, L284 y L285. Actualizados READMEs de looks e índices de galería maestra. |"

if old_actualizado in content:
    content = content.replace(old_actualizado, new_actualizado)
else:
    print("Warning: old_actualizado pattern not found!")

# 2. Update Materializados line
old_materializados = "| **Materializados** | L001-L201 completos (L200 al 7/7) · L202 (4/7) · L203 (1/7) · L204-L210 (1/7) · L216 (7/7) · L219 (2/7) · L249 (2/7) · L250 completo (7/7) · L251 completo (7/7) · L252 (2/7) · L253-L254 (2/7) · L256-L259 completos · L260-L271 (1/7) · L272-L276 completos · L277 (1/7) · L278 completo · L279 (1/7) · L280-L281 completos · L283 (1/7) · L287-L294 completos · L296-L298 completos · L300-L310 completos · Resto pendientes cuota API |"
new_materializados = "| **Materializados** | L001-L201 completos (L200 al 7/7) · L202 (4/7) · L203 (1/7) · L204-L210 (1/7) · L216 (7/7) · L219 (2/7) · L249 (2/7) · L250 completo (7/7) · L251 completo (7/7) · L252 (3/7) · L253-L254 (2/7) · L256-L259 completos · L260-L271 (1/7) · L272-L276 completos · L277 (1/7) · L278 completo · L279 (1/7) · L280-L281 completos · L282 (1/7) · L283 (1/7) · L284 (1/7) · L285 (1/7) · L287-L294 completos · L296-L298 completos · L300-L310 completos · Resto pendientes cuota API |"

if old_materializados in content:
    content = content.replace(old_materializados, new_materializados)
else:
    print("Warning: old_materializados pattern not found!")

# 3. Update footnote
old_footnote = "*Actualizado: 30/05/2026 — Auditoría y normalización total de la flota L200-L310. Vinculadas 72 celdas en 53 looks del disco a galeria_outfits.md. Creadas 15 carpetas físicas y materializados standing de L260-L271, L277, L279 y L283 recuperando artefactos generados. Flota L310 (227 únicos).*"
new_footnote = "*Actualizado: 31/05/2026 — Materializadas poses Standing de looks L252, L282, L284 y L285. Actualizados READMEs de looks e índices de galería maestra. Flota L310 (227 únicos).*"

if old_footnote in content:
    content = content.replace(old_footnote, new_footnote)
else:
    print("Warning: old_footnote pattern not found!")

p.write_text(content, encoding='utf-8')
print("identidad_ele.md updated successfully.")
