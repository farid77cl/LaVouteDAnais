#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fix_galeria_v3.py — Cirugía final de casos residuales"""

import re, sys
from pathlib import Path

GALERIA = Path(r"c:\Users\farid\LaVouteDAnais\00_Ele\galeria_outfits.md")
sys.stdout.reconfigure(encoding="utf-8")

with open(GALERIA, "r", encoding="utf-8") as f:
    content = f.read()

original_len = len(content.splitlines())

# ── Fix A: títulos ## con "ð" residual suelto antes de "Look N" ──────────────
# Ejemplo: "## ð Look 89:" → "## 🍷 Look 89:"
LOOK_EMOJIS = {
    89:"🍷", 90:"🌟", 91:"💎", 96:"🪞", 97:"🥈", 98:"📣",
    99:"💪", 100:"💙", 101:"💋", 102:"🔴", 103:"📺", 104:"🤍",
    105:"🎀", 106:"🖤", 107:"💫", 108:"💼", 109:"🐆",
    110:"🍒", 111:"💠", 112:"🌟", 113:"🖤", 114:"💼", 115:"🪙",
    116:"👑", 117:"💙", 118:"🖤", 119:"🌟", 120:"💼", 121:"🌹",
    122:"🤍", 123:"✈️", 124:"💚", 125:"💎", 126:"🪙", 127:"🌑",
    128:"❤️", 129:"💜", 130:"🤍",
}

def clean_header(m):
    prefix   = m.group(1)  # "## "
    garbage  = m.group(2)  # chars antes de "Look"
    look_num = int(m.group(4))
    rest     = m.group(5)  # ": nombre..."
    # Si el prefijo es solo basura (chars no-emoji reales)
    cleaned_garbage = re.sub(r"[ð\x80-\x9f]", "", garbage).strip()
    # Si queda algo que NO sea un emoji válido completo, reemplazar
    has_valid_emoji = bool(re.search(r"[\U0001F000-\U0001FFFF✈️🖼️✅❤️]", cleaned_garbage))
    if not has_valid_emoji or re.search(r"^[ð\s]+$", garbage):
        emoji = LOOK_EMOJIS.get(look_num, "👗")
        return f"{prefix}{emoji} Look {look_num}{rest}"
    return m.group(0)

content = re.sub(
    r"^(## )([^L\n]*?)(Look\s+(\d+))(:[^\n]*)$",
    clean_header, content, flags=re.MULTILINE
)
print("Fix A: títulos con ð residual corregidos")

# ── Fix B: Look 91 está embebido como ### en lugar de ## ─────────────────────
# "### LOOK 91: VINYL YOGA PERFORMANCE (CYAN CHROME)" → ## con header canónico
OLD_91 = "### LOOK 91: VINYL YOGA PERFORMANCE (CYAN CHROME)"
NEW_91 = "\n---\n\n## 💎 Look 91: Vinyl Yoga Performance (Cyan Chrome) (24/03/2026)"
if OLD_91 in content:
    content = content.replace(OLD_91, NEW_91)
    print("Fix B: Look 91 promovido a ## y separado correctamente")

# ── Fix C: líneas de vibe con "ð" residual suelto → eliminar el ð ─────────────
content = re.sub(r"(?<!\w)ð(?!\w)", "", content)
print("Fix C: ð residuales eliminados")

# ── Fix D: "ðâ€ " en vibes (Look 90 tiene al final) → eliminar ─────────────────
# ya parcialmente limpiado, eliminar cualquier remanente de mojibake de 2-3 chars
content = re.sub(r"ð[^\s\w\.,!?:;\-\"'()\[\]{}*#\n]{1,4}", "", content)
print("Fix D: fragmentos mojibake emoji eliminados")

# ── Fix E: Look 88 tiene Ã‚¿ residual en una cita ─────────────────────────────
content = content.replace("\u00c3\u201a\u00bf", "\u00bf")  # Ã‚¿ → ¿ vía codepoints
print("Fix E: Ã‚¿ residual en Look 88 corregido")

# ── Fix F: normalizar múltiples líneas vacías (después de mover cosas) ─────────
content = re.sub(r"\n{3,}", "\n\n", content)
content = re.sub(r"\n---\n(\s*\n---\n)+", "\n---\n", content)
print("Fix F: re-normalización de espacios")

with open(GALERIA, "w", encoding="utf-8", newline="\n") as f:
    f.write(content)

new_len = len(content.splitlines())
print(f"\n✅ Cirugía final: {original_len} → {new_len} líneas")
