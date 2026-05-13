#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
estandarizar_galeria.py
=======================
Estandariza galeria_outfits.md sin modificar ningún prompt.

Correcciones aplicadas:
  1. Colapsa runs de líneas en blanco >2 a máximo 2
  2. Normaliza variantes de ### Imágenes (...)
  3. Normaliza variantes de ### Prompts (V3.5 Hard-Sync)
  4. Normaliza variantes de **PROMPT N — Seated:** → **PROMPT 3 — Seated View:**
  5. Normaliza variantes de **PROMPT N  X:** (doble espacio) → **PROMPT N — X:**
  6. Normaliza BLOQUE B con número de look → **BLOQUE B (Outfit — igual en los 7 prompts):**
  7. Normaliza **NEGATIVE PROMPT:** (solo el encabezado, no el contenido)
  8. Corrige el emoji corrupto de sección imágenes
  9. Normaliza CRLF → LF (consistencia)

NO toca: contenido de prompts, descripciones de outfits, nombres de looks,
         rutas de imágenes, metadatos de fecha/categoría/paleta.
"""

import re
import shutil
from pathlib import Path
from datetime import datetime

GALERIA = Path(r"c:\Users\farid\LaVouteDAnais\00_Ele\galeria_outfits.md")
BACKUP  = GALERIA.with_name(f"galeria_outfits.BACKUP_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md")

# ─────────────────────────────────────────────
# 1. Leer
# ─────────────────────────────────────────────
print("Leyendo archivo...")
with open(GALERIA, "r", encoding="utf-8") as f:
    content = f.read()

original_len = len(content.splitlines())
print(f"  Líneas originales: {original_len}")

# ─────────────────────────────────────────────
# 2. Backup
# ─────────────────────────────────────────────
shutil.copy2(GALERIA, BACKUP)
print(f"  Backup: {BACKUP.name}")

# Normalizar saltos de línea a LF
content = content.replace("\r\n", "\n").replace("\r", "\n")

# ─────────────────────────────────────────────
# 3. Definir patrón de zona de PROMPT
#    (todo lo que está dentro de backticks o entre encabezados de prompt)
#    Usaremos sustituciones línea a línea fuera de bloques de código
# ─────────────────────────────────────────────

lines = content.split("\n")
result = []
in_code_block = False
changes = {
    "blank_lines_removed": 0,
    "imagenes_headers": 0,
    "prompts_headers": 0,
    "prompt_seated": 0,
    "prompt_double_space": 0,
    "bloque_b": 0,
    "negative_prompt": 0,
    "emoji_corrupt": 0,
}

# Buffer para colapsar líneas en blanco
blank_run = 0
MAX_BLANKS = 2

i = 0
while i < len(lines):
    line = lines[i]

    # ── Detectar bloques de código (no tocar internamente)
    if line.strip().startswith("```"):
        in_code_block = not in_code_block
        # Reset blank run counter antes de volcar buffer
        if blank_run > 0:
            keep = min(blank_run, MAX_BLANKS)
            result.extend([""] * keep)
            changes["blank_lines_removed"] += blank_run - keep
            blank_run = 0
        result.append(line)
        i += 1
        continue

    if in_code_block:
        # Dentro de bloque de código: volcar blancos acumulados y pasar línea sin tocar
        if blank_run > 0:
            keep = min(blank_run, MAX_BLANKS)
            result.extend([""] * keep)
            changes["blank_lines_removed"] += blank_run - keep
            blank_run = 0
        result.append(line)
        i += 1
        continue

    # ── Líneas en blanco: acumular
    if line.strip() == "":
        blank_run += 1
        i += 1
        continue
    else:
        # Volcar blancos acumulados (máx MAX_BLANKS)
        if blank_run > 0:
            keep = min(blank_run, MAX_BLANKS)
            result.extend([""] * keep)
            changes["blank_lines_removed"] += blank_run - keep
            blank_run = 0

    # ── Normalizaciones fuera de bloque de código ──────────────────────────

    # A. Emoji corrupto en encabezado de imágenes
    if re.search(r'Ã°Å¸Å½Å¾', line) or '\x8f' in line:
        line = re.sub(r'Ã°Å¸Å½Å¾ï¸\x8f\s*', '📸 ', line)
        changes["emoji_corrupt"] += 1

    # B. Normalizar ### Imágenes / Imagenes
    # Formas: "### Imagenes (0/7) Pendiente materializacion",
    #         "### 📸 Imágenes (5/5 - 100% Completo)", etc.
    # → Extraer el conteo si existe, sino dejar sin conteo
    if re.match(r'^###\s*(📸\s*)?[Ii]m[aá]genes', line):
        # Extraer el conteo (X/Y) si existe
        m = re.search(r'(\d+/\d+)', line)
        count_str = f" ({m.group(1)})" if m else ""
        # ¿Está completo?
        if m:
            num, den = m.group(1).split("/")
            if num == den:
                line = f"### 📸 Imágenes ({m.group(1)} — Completo){count_str.replace(count_str, '')}"
                line = f"### 📸 Imágenes ({m.group(1)} — Completo)"
            else:
                line = f"### 📸 Imágenes ({m.group(1)})"
        else:
            line = "### 📸 Imágenes"
        changes["imagenes_headers"] += 1

    # C. Normalizar ### Prompts
    if re.match(r'^###\s*.*[Pp]rompts', line) and not re.match(r'^###\s*📝 Prompts V3\.5 Hard-Sync$', line):
        line = "### 📝 Prompts V3.5 Hard-Sync"
        changes["prompts_headers"] += 1

    # D. Normalizar encabezados PROMPT con doble espacio (sin guión)
    # "**PROMPT 3  Seated:**" → "**PROMPT 3 — Seated View:**"
    m = re.match(r'^(\*\*PROMPT\s+(\d+))\s{2,}([^:]+):(\*\*)$', line)
    if m:
        prefix, num, name, suffix = m.group(1), m.group(2), m.group(3).strip(), m.group(4)
        line = f"{prefix} — {name}:{suffix}"
        changes["prompt_double_space"] += 1

    # E. Normalizar "Seated:" → "Seated View:" (solo en encabezados de prompt, no en prompts)
    # Solo afecta líneas que son ENCABEZADOS (comienzan con **)
    if re.match(r'^\*\*PROMPT\s+\d+\s+—\s+Seated:\*\*', line) or \
       re.match(r'^\*\*PROMPT\s+\d+\s*—\s*Seated:\*\*', line):
        line = re.sub(r'(PROMPT\s+\d+\s*—\s*)Seated:', r'\1Seated View:', line)
        changes["prompt_seated"] += 1

    # F. Normalizar BLOQUE B
    # "**BLOQUE B — Look 143 (invariable en los 7 prompts):**" → estándar
    # "**BLOQUE B  Look 146 (invariable...):**" → estándar
    if re.match(r'^\*\*BLOQUE B', line) and not re.match(r'^\*\*BLOQUE B \(Outfit\):\*\*$', line):
        # Preservar si ya está en formato estándar simple
        if re.match(r'^\*\*BLOQUE B\s*[—\s]', line):
            line = "**BLOQUE B (Outfit):**"
            changes["bloque_b"] += 1

    # G. Normalizar **NEGATIVE PROMPT:** — solo el encabezado, nunca el contenido
    # Variantes: "**NEGATIVE PROMPT:**", "**Negative Prompt:**"
    m_neg = re.match(r'^\*\*[Nn]egative\s+[Pp]rompt\*\*:', line)
    if m_neg and not line.strip().startswith("**NEGATIVE PROMPT:**"):
        # Solo normalizar si la línea ES solo el encabezado (no tiene contenido tras los dos puntos del encabezado)
        rest = line[m_neg.end():].strip()
        if rest == "" or rest.startswith("`"):
            line = "**NEGATIVE PROMPT:**" + (f" {rest}" if rest else "")
            changes["negative_prompt"] += 1

    result.append(line)
    i += 1

# Volcar blancos finales
if blank_run > 0:
    keep = min(blank_run, MAX_BLANKS)
    result.extend([""] * keep)
    changes["blank_lines_removed"] += blank_run - keep

# ─────────────────────────────────────────────
# 4. Escribir resultado
# ─────────────────────────────────────────────
new_content = "\n".join(result)
with open(GALERIA, "w", encoding="utf-8", newline="\n") as f:
    f.write(new_content)

# ─────────────────────────────────────────────
# 5. Reporte
# ─────────────────────────────────────────────
new_lines = len(new_content.splitlines())
print("\n✅ ESTANDARIZACIÓN COMPLETADA")
print(f"  Líneas originales:         {original_len}")
print(f"  Líneas finales:            {new_lines}")
print(f"  Reducción:                 {original_len - new_lines} líneas")
print(f"\n  Cambios aplicados:")
for k, v in changes.items():
    if v > 0:
        print(f"    {k+':':<35} {v}")
print(f"\n  Backup guardado en: {BACKUP.name}")
print("  (Los prompts NO fueron modificados)")
