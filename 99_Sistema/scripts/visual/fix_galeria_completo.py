#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix_galeria_completo.py
=======================
1. Corrige encoding corrupto (mojibake) en títulos y vibes
2. Repara links de imagen rotos → busca archivo real en Git
3. Convierte bloques ```carousel``` → <details> con tabla HTML (compatible GitHub)
"""

import re, subprocess, sys, os, shutil
from pathlib import Path
from datetime import datetime

REPO_ROOT   = Path(r"c:\Users\farid\LaVouteDAnais")
GALERIA     = REPO_ROOT / "00_Ele" / "galeria_outfits.md"
BACKUP      = GALERIA.with_name(f"galeria_outfits.BACKUP_FIX_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md")
REMOTE_BASE = "https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/"

sys.stdout.reconfigure(encoding="utf-8")

# ══════════════════════════════════════════════════════════════════════════════
# PASO 1 — Construir índice de imágenes reales en Git
# ══════════════════════════════════════════════════════════════════════════════
print("Paso 1: Cargando índice Git de imágenes...")

git_raw = subprocess.run(
    ["git", "ls-files", "05_Imagenes"],
    capture_output=True, text=True, cwd=REPO_ROOT
).stdout.splitlines()

IMG_EXT = {'.png', '.jpg', '.jpeg', '.webp'}

POSE_MAP = {
    'standing':     ['_standing'],
    'back_view':    ['_back_view', '_backview', '_back.', '_back_'],
    'seated':       ['_seated'],
    'side_profile': ['_side_profile', '_side.', '_sideview', '_side_', '_profile'],
    'ditzy':        ['_ditzy'],
    'pov':          ['_pov'],
    'odalisque':    ['_odalisque'],
    'closeup':      ['_closeup', '_close_up'],
    'kneeling':     ['_kneeling'],
    'lying':        ['_lying'],
    'mirror':       ['_mirror'],
    'low_angle':    ['_low_angle'],
    'front_arched': ['_front_arched'],
}

LABEL_MAP = {
    'standing': 'De Pie', 'back_view': 'Espalda', 'seated': 'Sentada',
    'side_profile': 'Perfil', 'ditzy': 'Ditzy', 'pov': 'POV',
    'odalisque': 'Odalisca', 'closeup': 'Closeup', 'kneeling': 'Kneeling',
    'lying': 'Lying', 'mirror': 'Mirror', 'low_angle': 'Low Angle',
    'front_arched': 'Front Arched',
}

# image_index[(look_num, pose_key)] = relative_path
image_index = {}
look_folders = {}  # look_num -> folder_path

for f in git_raw:
    if Path(f).suffix.lower() not in IMG_EXT:
        continue
    f_lower = f.lower().replace('\\', '/')
    m = re.search(r'look0*(\d+)', f_lower)
    if not m:
        continue
    look_num = int(m.group(1))
    look_folders[look_num] = '/'.join(f_lower.split('/')[:-1])
    fname = '/' + Path(f).name.lower()
    for pose_key, patterns in POSE_MAP.items():
        if any(p in fname for p in patterns):
            key = (look_num, pose_key)
            if key not in image_index:
                image_index[key] = f.replace('\\', '/')
            break

print(f"  {len(image_index)} poses indexadas, {len(look_folders)} looks con imágenes")


# ══════════════════════════════════════════════════════════════════════════════
# PASO 2 — Reparar un URL roto dado su alt text y look number
# ══════════════════════════════════════════════════════════════════════════════
def detect_pose_from_alt_or_url(alt, url):
    """Detecta la pose a partir del alt text o la URL."""
    combined = (alt + ' ' + url).lower()
    for pose_key, patterns in POSE_MAP.items():
        label = LABEL_MAP[pose_key].lower()
        if label in combined or pose_key in combined:
            return pose_key
        for p in patterns:
            if p.strip('_').rstrip('.') in combined:
                return pose_key
    # Fallback: número de versión en URL
    m = re.search(r'_v(\d+)[_.]', url.lower())
    if m:
        v = int(m.group(1))
        pose_order = ['standing', 'seated', 'back_view', 'side_profile', 'ditzy', 'kneeling', 'lying', 'mirror', 'front_arched']
        if 1 <= v <= len(pose_order):
            return pose_order[v - 1]
    return None

def fix_image_url(look_num, alt, url):
    """Intenta reparar un URL roto. Retorna el URL corregido o None."""
    pose = detect_pose_from_alt_or_url(alt, url)
    if pose:
        key = (look_num, pose)
        if key in image_index:
            return REMOTE_BASE + image_index[key]
    # Intentar con todas las poses del look
    for (ln, pk), path in image_index.items():
        if ln == look_num:
            for p in POSE_MAP.get(pk, []):
                if p.strip('_.') in url.lower():
                    return REMOTE_BASE + path
    return None


# ══════════════════════════════════════════════════════════════════════════════
# PASO 3 — Función de reparación de encoding (mojibake)
# ══════════════════════════════════════════════════════════════════════════════
MOJIBAKE_PAT = re.compile(r'(?:[ÃÅÂ\xc0-\xff][\xa0-\xff\x80-\x9f])+')

def fix_mojibake(text):
    """Intenta recuperar texto UTF-8 que fue leído como latin-1 y re-guardado."""
    def try_recover(m):
        s = m.group(0)
        # Intentar en bloques de longitud decreciente
        result = []
        i = 0
        while i < len(s):
            recovered = False
            for length in range(min(8, len(s) - i), 1, -1):
                chunk = s[i:i+length]
                try:
                    raw = chunk.encode('latin-1')
                    decoded = raw.decode('utf-8')
                    result.append(decoded)
                    i += length
                    recovered = True
                    break
                except (UnicodeEncodeError, UnicodeDecodeError):
                    pass
            if not recovered:
                # Si no se puede recuperar, eliminar el carácter corrupto
                i += 1
        return ''.join(result)
    return MOJIBAKE_PAT.sub(try_recover, text)


# ══════════════════════════════════════════════════════════════════════════════
# PASO 4 — Leer y procesar el archivo
# ══════════════════════════════════════════════════════════════════════════════
print("\nPaso 4: Leyendo galería...")
shutil.copy2(GALERIA, BACKUP)
print(f"  Backup: {BACKUP.name}")

with open(GALERIA, 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.splitlines()
print(f"  {len(lines)} líneas")

# Rastrear look actual
current_look = None

# Resultado final
output_lines = []

# Estadísticas
stats = dict(encoding_fixed=0, links_fixed=0, links_not_found=0,
             carousels_converted=0)

IMG_PAT = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')

def is_broken_url(url):
    if not url.startswith('http'):
        return False
    if url.startswith(REMOTE_BASE):
        rel = url[len(REMOTE_BASE):].lower()
        git_set = {f.replace('\\','/').lower() for f in git_raw}
        return rel not in git_set
    return False

i = 0
while i < len(lines):
    line = lines[i]

    # Detectar look actual
    m = re.match(r'^## .{0,10}Look (\d+)', line)
    if m:
        current_look = int(m.group(1))

    # ── Encoding: sólo en encabezados ## y en líneas de vibe *...*
    if MOJIBAKE_PAT.search(line):
        fixed = fix_mojibake(line)
        if fixed != line:
            stats['encoding_fixed'] += 1
            line = fixed

    # ── Detectar inicio de bloque carousel
    if re.match(r'^`{2,5}carousel\s*$', line.strip()):
        # Recopilar todo el bloque hasta el cierre
        backticks = len(line) - len(line.lstrip('`'))
        close_pat = re.compile(r'^`{' + str(backticks) + r',}\s*$')
        carousel_lines_inner = []
        j = i + 1
        while j < len(lines):
            if close_pat.match(lines[j].strip()):
                break
            carousel_lines_inner.append(lines[j])
            j += 1

        # Extraer imágenes del bloque
        images = []  # (alt, url)
        for cl in carousel_lines_inner:
            for mm in IMG_PAT.finditer(cl):
                alt = mm.group(1)
                url = mm.group(2).strip()
                # Intentar reparar si está roto
                if is_broken_url(url) and current_look:
                    fixed_url = fix_image_url(current_look, alt, url)
                    if fixed_url:
                        url = fixed_url
                        stats['links_fixed'] += 1
                    else:
                        stats['links_not_found'] += 1
                images.append((alt, url))

        # Construir <details> con tabla
        n = len(images)
        if n > 0:
            # Tabla en filas de máx 7
            ROW_MAX = 7
            headers = [alt if alt else f"Pose {k+1}" for k, (alt, _) in enumerate(images)]
            urls    = [url for _, url in images]

            # Dividir en filas
            rows_h = [headers[k:k+ROW_MAX] for k in range(0, n, ROW_MAX)]
            rows_u = [urls[k:k+ROW_MAX]    for k in range(0, n, ROW_MAX)]

            detail_lines = [
                f'<details>',
                f'<summary>📸 {n} poses — ver imágenes</summary>',
                '',
            ]
            for rh, ru in zip(rows_h, rows_u):
                detail_lines.append('| ' + ' | '.join(rh) + ' |')
                detail_lines.append('| ' + ' | '.join([':---:'] * len(rh)) + ' |')
                detail_lines.append('| ' + ' | '.join(f'![{a}]({u})' for a, u in zip(rh, ru)) + ' |')
                detail_lines.append('')

            detail_lines.append('</details>')
            output_lines.extend(detail_lines)
            stats['carousels_converted'] += 1
        else:
            # Bloque vacío → eliminarlo
            pass

        i = j + 1  # saltar hasta después del cierre
        continue

    # ── Reparar links de imagen sueltos (fuera de carousel)
    if IMG_PAT.search(line) and current_look:
        def fix_match(mm):
            alt = mm.group(1)
            url = mm.group(2).strip()
            if is_broken_url(url):
                fixed = fix_image_url(current_look, alt, url)
                if fixed:
                    stats['links_fixed'] += 1
                    return f'![{alt}]({fixed})'
                else:
                    stats['links_not_found'] += 1
            return mm.group(0)
        new_line = IMG_PAT.sub(fix_match, line)
        if new_line != line:
            line = new_line

    output_lines.append(line)
    i += 1

# ══════════════════════════════════════════════════════════════════════════════
# PASO 5 — Escribir resultado
# ══════════════════════════════════════════════════════════════════════════════
new_content = '\n'.join(output_lines)
with open(GALERIA, 'w', encoding='utf-8', newline='\n') as f:
    f.write(new_content)

print(f"\n✅ COMPLETADO")
print(f"  Líneas: {len(lines)} → {len(output_lines)}")
print(f"  Encoding corregido:      {stats['encoding_fixed']} líneas")
print(f"  Links reparados:         {stats['links_fixed']}")
print(f"  Links sin match en Git:  {stats['links_not_found']}")
print(f"  Carouseles convertidos:  {stats['carousels_converted']}")
print(f"  Backup: {BACKUP.name}")
