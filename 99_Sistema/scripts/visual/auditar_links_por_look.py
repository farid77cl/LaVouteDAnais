#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
auditar_links_por_look.py
=========================
Lee galeria_outfits.md link por link y verifica que la imagen corresponda
al look en cuyo contexto aparece. Detecta:
  - Imagen de lookX en sección de lookY (mismatch)
  - Imagen con ruta de Reference/ (legacy path)
  - Imagen con nombre de archivo que no coincide con el look actual
"""

import re, sys, subprocess
from pathlib import Path
from collections import defaultdict

REPO_ROOT   = Path(r"c:\Users\farid\LaVouteDAnais")
GALERIA     = REPO_ROOT / "00_Ele" / "galeria_outfits.md"
REPORT_OUT  = REPO_ROOT / "00_Ele" / "galeria_link_audit.md"
REMOTE_BASE = "https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/"

sys.stdout.reconfigure(encoding="utf-8")

with open(GALERIA, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Cargar índice git
git_set = set(
    subprocess.run(
        ["git", "ls-files", "05_Imagenes"],
        capture_output=True, text=True, cwd=REPO_ROOT
    ).stdout.splitlines()
)
git_set_lower = {f.replace("\\", "/").lower() for f in git_set}

IMG_PAT  = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
LOOK_HDR = re.compile(r"^## .*\bLook\s+(\d+)\b", re.IGNORECASE)
URL_LOOK = re.compile(r"[/_](?:look|helena_look|missdoll_look|ele_look)0*(\d+)[/_]", re.IGNORECASE)

# Resultados
mismatches   = []   # (línea, look_actual, look_en_url, alt, url)
reference_paths = []  # (línea, look_actual, alt, url)
not_in_git   = []   # (línea, look_actual, alt, url)
ok_count     = 0

current_look = None

for i, line in enumerate(lines, 1):
    # Actualizar look actual
    hm = LOOK_HDR.match(line)
    if hm:
        current_look = int(hm.group(1))
        continue

    # Procesar cada imagen en la línea
    for img_m in IMG_PAT.finditer(line):
        alt = img_m.group(1)
        url = img_m.group(2).strip()

        # Solo analizar URLs de raw.githubusercontent.com
        if not url.startswith(REMOTE_BASE):
            continue

        rel_path = url[len(REMOTE_BASE):]
        rel_lower = rel_path.lower().replace("\\", "/")

        # Detectar look number en la URL
        url_look_match = URL_LOOK.search(rel_lower)
        url_look = int(url_look_match.group(1)) if url_look_match else None

        # Detectar rutas de Reference/ (legacy)
        is_reference = "/reference/" in rel_lower

        # ── Verificar si existe en git ────────────────────────────────────────
        in_git = rel_lower in git_set_lower

        # ── Reportar ──────────────────────────────────────────────────────────
        if is_reference:
            reference_paths.append((i, current_look, url_look, alt, rel_path))
        elif url_look and current_look and url_look != current_look:
            mismatches.append((i, current_look, url_look, alt, rel_path))
        elif not in_git:
            not_in_git.append((i, current_look, url_look, alt, rel_path))
        else:
            ok_count += 1

total_imgs = ok_count + len(mismatches) + len(reference_paths) + len(not_in_git)

# ── Generar reporte ────────────────────────────────────────────────────────────
lines_out = [
    "# 🔍 Auditoría de Links por Look — galeria_outfits.md",
    "",
    f"**Fecha:** {__import__('datetime').datetime.now().strftime('%d/%m/%Y %H:%M')}",
    "",
    "## 📊 Resumen",
    "",
    "| Métrica | Valor |",
    "|:--------|------:|",
    f"| 🖼️ Imágenes analizadas | {total_imgs} |",
    f"| ✅ Correctas (look y archivo coinciden) | {ok_count} |",
    f"| ❌ Mismatch (imagen de lookX en sección lookY) | {len(mismatches)} |",
    f"| 📁 Rutas Reference/ (legacy) | {len(reference_paths)} |",
    f"| ⚠️ No encontradas en Git | {len(not_in_git)} |",
    "",
    "---",
]

# Mismatches
if mismatches:
    lines_out += [
        "## ❌ Mismatches — Imagen no corresponde al Look",
        "",
        "> La imagen está en la sección del Look **actual** pero la URL apunta al Look **en URL**.",
        "",
        "| Línea | Look sección | Look en URL | Alt | Archivo |",
        "|------:|:------------:|:-----------:|:----|:--------|",
    ]
    for ln, cur, url_l, alt, path in mismatches:
        short = path[-70:] if len(path) > 70 else path
        lines_out.append(f"| {ln} | **{cur}** | **{url_l}** | {alt} | `...{short}` |")
    lines_out.append("")
    lines_out.append("---")
    lines_out.append("")

# Reference paths
if reference_paths:
    lines_out += [
        "## 📁 Rutas Reference/ (Legacy — posiblemente incorrectas)",
        "",
        "| Línea | Look | Alt | Archivo |",
        "|------:|:----:|:----|:--------|",
    ]
    for ln, cur, url_l, alt, path in reference_paths:
        short = path[-70:] if len(path) > 70 else path
        lines_out.append(f"| {ln} | **{cur}** | {alt} | `...{short}` |")
    lines_out.append("")
    lines_out.append("---")
    lines_out.append("")

# Not in git
if not_in_git:
    lines_out += [
        "## ⚠️ No encontradas en Git (link roto potencial)",
        "",
        "| Línea | Look | Alt | Archivo |",
        "|------:|:----:|:----|:--------|",
    ]
    for ln, cur, url_l, alt, path in not_in_git:
        short = path[-70:] if len(path) > 70 else path
        lines_out.append(f"| {ln} | **{cur}** | {alt} | `...{short}` |")
    lines_out.append("")
    lines_out.append("---")
    lines_out.append("")

lines_out.append("*Auditoría generada por `auditar_links_por_look.py`* 🫦")

with open(REPORT_OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(lines_out))

print(f"\n✅ Auditoría completa")
print(f"   Total imágenes: {total_imgs}")
print(f"   ✅ Correctas:   {ok_count}")
print(f"   ❌ Mismatches:  {len(mismatches)}")
print(f"   📁 Reference/:  {len(reference_paths)}")
print(f"   ⚠️ No en Git:   {len(not_in_git)}")
print(f"   Reporte: {REPORT_OUT.name}")
