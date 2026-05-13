#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
auditar_galeria.py
==================
Auditoría completa de 00_Ele/galeria_outfits.md:
  1. Encoding / caracteres corruptos
  2. Links de imágenes rotos (relativas y GitHub raw)
  3. Tablas malformadas
  4. Bloques 'carousel' no estándar
  5. Estadísticas generales por look
"""

import re, subprocess, sys, os
from pathlib import Path
from collections import defaultdict

REPO_ROOT  = Path(r"c:\Users\farid\LaVouteDAnais")
GALERIA    = REPO_ROOT / "00_Ele" / "galeria_outfits.md"
REPORT_OUT = REPO_ROOT / "00_Ele" / "galeria_audit_report.md"
REMOTE_BASE = "https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/"

sys.stdout.reconfigure(encoding="utf-8")

# ── 1. Cargar archivo ──────────────────────────────────────────────────────────
with open(GALERIA, "r", encoding="utf-8") as f:
    content = f.read()
lines = content.splitlines()
print(f"Archivo: {GALERIA.name}  ({len(lines)} líneas, {len(content)} bytes)")

# ── 2. Obtener archivos trackeados por Git ─────────────────────────────────────
print("Cargando índice Git...")
git_files_raw = subprocess.run(
    ["git", "ls-files"], capture_output=True, text=True, cwd=REPO_ROOT
).stdout.splitlines()
git_files = {f.replace("\\", "/").lower() for f in git_files_raw}
print(f"  {len(git_files)} archivos trackeados")

# ── 3. Encoding corruptos ──────────────────────────────────────────────────────
CORRUPT_PAT = re.compile(r'(?:Ã[°¢£\xa4-\xff])|(?:Å[^\s])|(?:\x8f|\x9d|\x9e|\x9f)')

corrupt_lines = []
for i, l in enumerate(lines, 1):
    if CORRUPT_PAT.search(l):
        corrupt_lines.append((i, l.strip()[:120]))

# ── 4. Extraer todos los links de imagen ───────────────────────────────────────
IMG_PAT = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')

all_img_links = []
for i, l in enumerate(lines, 1):
    for m in IMG_PAT.finditer(l):
        alt = m.group(1)
        url = m.group(2).strip()
        all_img_links.append((i, alt, url))

# Clasificar: relativa vs GitHub raw vs otra URL
broken = []
ok = []
unknown_url = []

for ln, alt, url in all_img_links:
    if url.startswith("https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/"):
        # Convertir a ruta relativa para verificar
        rel = url[len(REMOTE_BASE):].lower()
        if rel in git_files:
            ok.append((ln, url))
        else:
            broken.append((ln, alt, url, "GitHub Raw — no encontrado en Git"))
    elif url.startswith("../") or url.startswith("./") or not url.startswith("http"):
        # Ruta relativa — resolver desde REPO_ROOT/00_Ele
        rel_from_file = (REPO_ROOT / "00_Ele" / url).resolve()
        rel_from_root = os.path.relpath(rel_from_file, REPO_ROOT).replace("\\", "/").lower()
        if rel_from_root in git_files:
            ok.append((ln, url))
        else:
            broken.append((ln, alt, url, "Ruta relativa — no encontrado en Git"))
    elif url.startswith("http"):
        unknown_url.append((ln, alt, url))
    else:
        broken.append((ln, alt, url, "URL no reconocida"))

# ── 5. Tablas malformadas ──────────────────────────────────────────────────────
bad_tables = []
in_table = False
table_start = 0
table_lines = []
for i, l in enumerate(lines, 1):
    stripped = l.strip()
    if stripped.startswith("|"):
        if not in_table:
            in_table = True
            table_start = i
            table_lines = []
        table_lines.append((i, l))
    else:
        if in_table:
            # Analizar la tabla acumulada
            if len(table_lines) >= 2:
                header = table_lines[0][1]
                sep_idx = None
                for ti, (tln, tl) in enumerate(table_lines):
                    if re.match(r'^\|[\s\-:|]+\|', tl.strip()):
                        sep_idx = ti
                        break
                if sep_idx is None:
                    bad_tables.append((table_start, len(table_lines), "Sin separador de encabezado"))
                elif sep_idx != 1:
                    bad_tables.append((table_start, len(table_lines), f"Separador en posición {sep_idx} (debería ser 1)"))
                # Comprobar columnas consistentes
                else:
                    ncols = header.count("|") - 1
                    for tln, tl in table_lines:
                        if abs(tl.count("|") - 1 - ncols) > 1:
                            bad_tables.append((tln, 1, f"Columnas inconsistentes ({tl.count('|')-1} vs {ncols} esperadas)"))
                            break
        in_table = False
        table_lines = []

# ── 6. Bloques carousel no estándar ───────────────────────────────────────────
carousel_lines = [(i, l) for i, l in enumerate(lines, 1)
                  if 'carousel' in l.lower() and ('```' in l or '``' in l)]

# ── 7. Estadísticas por look ───────────────────────────────────────────────────
look_stats = {}
current_look = None
for i, l in enumerate(lines, 1):
    m = re.match(r'^## .{0,10}Look (\d+)', l)
    if m:
        current_look = int(m.group(1))
        look_stats[current_look] = {"line": i, "images": 0, "broken": 0, "corrupt": 0}
    if current_look is not None:
        if IMG_PAT.search(l):
            look_stats[current_look]["images"] += IMG_PAT.subn("", l)[1] if False else len(IMG_PAT.findall(l))
        if CORRUPT_PAT.search(l):
            look_stats[current_look]["corrupt"] += 1

# Marcar looks con links rotos
for ln, alt, url, reason in broken:
    # Encontrar a qué look pertenece
    closest = None
    for num, data in look_stats.items():
        if data["line"] <= ln:
            closest = num
    if closest:
        look_stats[closest]["broken"] += 1

# ── 8. Generar reporte ─────────────────────────────────────────────────────────
report = []
report.append("# 🔍 Auditoría Completa — galeria_outfits.md\n")
report.append(f"**Fecha:** 13/05/2026  \n**Archivo:** `00_Ele/galeria_outfits.md`  \n**Líneas:** {len(lines)} | **Bytes:** {len(content):,}\n\n---\n\n")

# Resumen ejecutivo
report.append("## 📊 Resumen Ejecutivo\n\n")
report.append("| Métrica | Valor |\n|:--------|------:|\n")
report.append(f"| Looks registrados | {len(look_stats)} |\n")
report.append(f"| Links de imagen totales | {len(all_img_links)} |\n")
report.append(f"| ✅ Links válidos (en Git) | {len(ok)} |\n")
report.append(f"| ❌ Links ROTOS | {len(broken)} |\n")
report.append(f"| ⚠️ URLs externas (no verificables) | {len(unknown_url)} |\n")
report.append(f"| 🔣 Líneas con encoding corrupto | {len(corrupt_lines)} |\n")
report.append(f"| 📊 Tablas malformadas | {len(bad_tables)} |\n")
report.append(f"| 🎠 Bloques carousel no estándar | {len(carousel_lines)} |\n")
report.append("\n---\n\n")

# Links rotos
if broken:
    report.append(f"## ❌ Links de Imagen Rotos ({len(broken)})\n\n")
    report.append("| Línea | Alt | URL | Motivo |\n|------:|:----|:----|:-------|\n")
    for ln, alt, url, reason in broken[:100]:
        url_short = url[-70:] if len(url) > 70 else url
        report.append(f"| {ln} | {alt[:30]} | `...{url_short}` | {reason} |\n")
    if len(broken) > 100:
        report.append(f"\n*... y {len(broken)-100} más.*\n")
    report.append("\n---\n\n")

# Encoding corrupto
if corrupt_lines:
    report.append(f"## 🔣 Líneas con Encoding Corrupto ({len(corrupt_lines)})\n\n")
    report.append("| Línea | Contenido |\n|------:|:----------|\n")
    for ln, txt in corrupt_lines[:50]:
        txt_safe = txt.replace("|", "\\|")
        report.append(f"| {ln} | `{txt_safe[:100]}` |\n")
    if len(corrupt_lines) > 50:
        report.append(f"\n*... y {len(corrupt_lines)-50} más.*\n")
    report.append("\n---\n\n")

# Tablas malformadas
if bad_tables:
    report.append(f"## 📊 Tablas Malformadas ({len(bad_tables)})\n\n")
    report.append("| Línea inicio | Filas | Problema |\n|-------------:|------:|:---------|\n")
    for start, nrows, problem in bad_tables[:30]:
        report.append(f"| {start} | {nrows} | {problem} |\n")
    report.append("\n---\n\n")

# Carousel no estándar
if carousel_lines:
    report.append(f"## 🎠 Bloques Carousel No Estándar ({len(carousel_lines)})\n\n")
    report.append("> GitHub Flavored Markdown **no soporta carruseles nativos**. El contenido se mostrará como texto plano.\n\n")
    report.append("| Línea | Contenido |\n|------:|:----------|\n")
    for ln, l in carousel_lines:
        report.append(f"| {ln} | `{l.strip()[:80]}` |\n")
    report.append("\n---\n\n")

# Looks con problemas
looks_with_issues = {n: d for n, d in look_stats.items()
                      if d["broken"] > 0 or d["corrupt"] > 0 or d["images"] == 0}
if looks_with_issues:
    report.append(f"## 👠 Looks con Problemas ({len(looks_with_issues)})\n\n")
    report.append("| Look | Línea | Imágenes | Rotas | Corrupt |\n|-----:|------:|---------:|------:|--------:|\n")
    for num in sorted(looks_with_issues.keys()):
        d = looks_with_issues[num]
        report.append(f"| **{num}** | {d['line']} | {d['images']} | {d['broken']} | {d['corrupt']} |\n")
    report.append("\n---\n\n")

# URLs externas (no verificadas)
if unknown_url:
    report.append(f"## ⚠️ URLs Externas No Verificadas ({len(unknown_url)})\n\n")
    report.append("*Estas URLs apuntan a dominios distintos a GitHub raw. No se pudo verificar su estado.*\n\n")
    report.append("| Línea | Alt | URL |\n|------:|:----|:----|\n")
    for ln, alt, url in unknown_url[:30]:
        url_short = url[:80]
        report.append(f"| {ln} | {alt[:30]} | `{url_short}` |\n")
    report.append("\n---\n\n")

report.append("## 💡 Recomendaciones\n\n")
report.append("1. **Encoding:** Los ~" + str(len(corrupt_lines)) + " caracteres corruptos son emojis en encabezados de looks legados (era pre-V3). Se pueden limpiar sin afectar el contenido.\n")
report.append(f"2. **Links rotos ({len(broken)}):** Verificar si las imágenes existen en otra ruta o simplemente ya no están en el repositorio.\n")
report.append("3. **Carouseles:** GitHub Markdown no soporta carouseles. La mejor alternativa es una tabla HTML de imágenes con `<details>` colapsable por look.\n")
report.append("4. **Tablas:** Las tablas malformadas son principalmente bloques de texto que contienen `|` sin ser tablas reales.\n\n")
report.append("---\n\n*Reporte generado automáticamente por `auditar_galeria.py`* 🫦\n")

with open(REPORT_OUT, "w", encoding="utf-8", newline="\n") as f:
    f.writelines(report)

print(f"\n✅ Reporte guardado en: {REPORT_OUT.name}")
print(f"   {len(broken)} links rotos | {len(corrupt_lines)} líneas corruptas | {len(bad_tables)} tablas malformadas | {len(carousel_lines)} bloques carousel")
