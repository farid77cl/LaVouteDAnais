#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fix_galeria_v2.py — Uniformidad total de galeria_outfits.md"""

import re, shutil, sys
from pathlib import Path
from datetime import datetime

REPO_ROOT = Path(r"c:\Users\farid\LaVouteDAnais")
GALERIA   = REPO_ROOT / "00_Ele" / "galeria_outfits.md"
BACKUP    = GALERIA.with_name(
    "galeria_outfits.BKP2_{}.md".format(datetime.now().strftime("%Y%m%d_%H%M%S"))
)
sys.stdout.reconfigure(encoding="utf-8")

shutil.copy2(GALERIA, BACKUP)
with open(GALERIA, "r", encoding="utf-8") as f:
    content = f.read()

original_len = len(content.splitlines())

# ── FIX 1: Mojibake inline ─────────────────────────────────────────────────────
# Los pares se definen como bytes latin-1 → str para evitar syntax errors
# con los caracteres corruptos dentro del propio script Python

def _pair(bad_latin1_bytes, good_str):
    """Convierte bytes latin-1 a str para comparar con el texto corrupto leído como UTF-8."""
    # El texto corrupto en el archivo UTF-8 es: cada byte latin-1 → su codepoint unicode
    # (porque fue leído como latin-1 y re-guardado como UTF-8)
    bad_str = bad_latin1_bytes.decode("latin-1")
    return (bad_str, good_str)

MOJIBAKE_PAIRS = [
    _pair(b"\xc3\x82\xa1", "\u00a1"),          # Ã‚¡ → ¡
    _pair(b"\xc3\x82\xbf", "\u00bf"),          # Ã‚¿ → ¿
    _pair(b"\xc3\x83\xc2\xbate", "V\u00fbte"), # VoÃƒ»te → Voûte (sufijo)
    _pair(b"\xc3\x83\xc2\xba", "\u00fa"),      # Ãº → ú
    _pair(b"\xc3\xbb", "\u00fb"),              # Ã» → û
    _pair(b"\xc3\xa9", "\u00e9"),              # Ã© → é
    _pair(b"\xc3\xb3", "\u00f3"),              # Ã³ → ó
    _pair(b"\xc3\xa1", "\u00e1"),              # Ã¡ → á
    _pair(b"\xc3\xad", "\u00ed"),              # Ã­ → í
    _pair(b"\xc3\xba", "\u00fa"),              # Ãº → ú
    _pair(b"\xc3\xb1", "\u00f1"),              # Ã± → ñ
    # Comillas y dashes
    _pair(b"\xe2\x80\x99", "'"),               # â€™ → '
    _pair(b"\xe2\x80\x93", "\u2013"),          # â€" → –
    _pair(b"\xe2\x80\x94", "\u2014"),          # â€" → —
    _pair(b"\xe2\x80\x9c", "\u201c"),          # â€œ → "
    _pair(b"\xe2\x80\x9d", "\u201d"),          # â€ → "
]

# Patrones de texto directo (sin mojibake en el fuente del script)
DIRECT_FIXES = [
    ("VoÃƒ»te", "Voûte"),
    ("VoÃ»te", "Voûte"),
]

for bad, good in MOJIBAKE_PAIRS:
    content = content.replace(bad, good)
for bad, good in DIRECT_FIXES:
    content = content.replace(bad, good)

# Limpiar emojis corruptos en texto (los que no tienen mapeo conocido)
# Patrón: secuencia de chars en rango latin-ext que juntos forman un emoji roto
content = re.sub(r"[ðŸ][^\s\w\.,!?:;\-\"'()\[\]{}*#\n]{1,5}", "", content)
content = re.sub(r"[âÃ][\xc0-\xff][^\s\w\.,!?:;\-\"'()\[\]{}*#\n]{0,3}", "", content)

print("Fix 1: mojibake inline limpiado")

# ── FIX 2: Títulos ## Look N con prefijo corrupto → emoji limpio ───────────────
LOOK_EMOJIS = {
    46:"🖤", 55:"🧹",
    85:"🍓", 86:"💼", 87:"✈️", 88:"🖼️", 89:"🍷", 90:"🌟", 91:"💎",
    92:"✨", 93:"🍒", 94:"🔗", 95:"🥈", 96:"🪞", 97:"🥈",
    98:"📣", 99:"💪", 100:"💙", 101:"💋", 102:"🔴", 103:"📺",
    104:"🤍", 105:"🎀", 106:"🖤", 107:"💫", 108:"💼", 109:"🐆",
    110:"🍒", 111:"💠", 112:"🌟", 113:"🖤", 114:"💼", 115:"🪙",
    116:"👑", 117:"💙", 118:"🖤", 119:"🌟", 120:"💼", 121:"🌹",
    122:"🤍", 123:"✈️", 124:"💚", 125:"💎", 126:"🪙", 127:"🌑",
    128:"❤️", 129:"💜", 130:"🤍",
}

def _fix_header(m):
    prefix  = m.group(1)   # "## "
    garbage = m.group(2)   # prefijo (puede ser emoji corrupto)
    look_n  = int(m.group(4))
    rest    = m.group(5)   # ": Nombre..."
    # Tiene mojibake si contiene chars no-emoji en rango sospechoso
    has_corrupt = bool(re.search(r"[\x80-\x9f]|Ë†|[ðâ][^\s]", garbage))
    if has_corrupt:
        emoji = LOOK_EMOJIS.get(look_n, "👗")
        return f"{prefix}{emoji} Look {look_n}{rest}"
    return m.group(0)

content = re.sub(
    r"^(## )([^L\n]*?)(Look\s+(\d+))(:[^\n]*)$",
    _fix_header, content, flags=re.MULTILINE
)
print("Fix 2: títulos ## uniformizados")

# ── FIX 3: Tablas GFM — eliminar líneas en blanco entre filas ──────────────────
def collapse_table_blanks(text):
    lines  = text.splitlines()
    result = []
    i = 0
    while i < len(lines):
        result.append(lines[i])
        if lines[i].strip().startswith("|") and lines[i].strip().endswith("|"):
            j = i + 1
            while j < len(lines):
                s = lines[j].strip()
                if s.startswith("|") and s.endswith("|"):
                    result.append(lines[j]); j += 1
                elif s == "":
                    # Peek ahead
                    k = j + 1
                    while k < len(lines) and lines[k].strip() == "": k += 1
                    if k < len(lines) and lines[k].strip().startswith("|") and lines[k].strip().endswith("|"):
                        j = k
                    else:
                        break
                else:
                    break
            i = j
        else:
            i += 1
    return "\n".join(result)

content = collapse_table_blanks(content)
print("Fix 3: tablas GFM colapsadas")

# ── FIX 4: Secciones (0/N) sin imágenes reales → placeholder limpio ───────────
def clean_pending_sections(text):
    lines  = text.splitlines()
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if re.match(r"### 📸 Imágenes \(0/", line):
            j = i + 1
            while j < len(lines):
                s = lines[j].strip()
                if s.startswith("##") or s == "---": break
                j += 1
            block = "\n".join(lines[i:j])
            if "raw.githubusercontent.com" not in block:
                result += ["### 📸 Imágenes", "",
                           "> *⏳ Pendiente de materialización — prompts listos*", ""]
                i = j; continue
        result.append(line); i += 1
    return "\n".join(result)

content = clean_pending_sections(content)
print("Fix 4: secciones pendientes uniformizadas")

# ── FIX 5: Look 87 — imagen Closeup incorrecta ────────────────────────────────
OLD_87 = ("https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/"
          "05_Imagenes/ele/Reference/look87_evolutions/look87_04_closeup_1774187124271.png")
NEW_87 = ("https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/"
          "05_Imagenes/ele/look087_ele_v3_core/ele_087_standing.png")
if OLD_87 in content:
    content = content.replace(OLD_87, NEW_87)
    print("Fix 5: Look 87 closeup corregido")
else:
    print("Fix 5: Look 87 closeup — ya correcto")

# ── FIX 6: Looks 46 y 55 → Archivo Legado al final ────────────────────────────
def extract_look(text, n):
    pat = re.compile(
        r"(^## [^\n]*\bLook\s+" + str(n) + r"\b[^\n]*\n(?:(?!^## )[\s\S])*)",
        re.MULTILINE
    )
    m = pat.search(text)
    return (m.group(0), m.start(), m.end()) if m else (None, -1, -1)

legacy = ""
for look_n in (46, 55):
    blk, s, e = extract_look(content, look_n)
    if blk:
        legacy += blk.rstrip() + "\n\n---\n\n"
        content = content[:s] + content[e:]
        print(f"Fix 6: Look {look_n} → Legado")

if legacy:
    LEGACY_HDR = (
        "\n\n---\n\n"
        "## \U0001f5c4\ufe0f Archivo Legado (Era Anterior a V3.5)\n\n"
        "> Looks de eras anteriores conservados como registro histórico.\n\n"
        "---\n\n"
    )
    content = content.rstrip() + LEGACY_HDR + legacy

# ── FIX 7: Dobles --- → uno solo ──────────────────────────────────────────────
content = re.sub(r"\n---\n(\s*\n---\n)+", "\n---\n", content)
print("Fix 7: dobles --- eliminados")

# ── FIX 8: Múltiples líneas vacías → máximo una ───────────────────────────────
content = re.sub(r"\n{3,}", "\n\n", content)
print("Fix 8: múltiples líneas vacías → una")

# ── FIX 9: Separador final de looks (## ) → exactamente \n\n---\n\n ───────────
content = re.sub(r"(\n---\n)\n+(?=## )", r"\1\n", content)
print("Fix 9: separadores entre looks normalizados")

# ── Guardar ────────────────────────────────────────────────────────────────────
with open(GALERIA, "w", encoding="utf-8", newline="\n") as f:
    f.write(content)

new_len = len(content.splitlines())
print(f"\n✅ COMPLETADO: {original_len} → {new_len} líneas")
print(f"   Backup: {BACKUP.name}")
