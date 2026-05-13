#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
reparar_mismatches.py
=====================
Corrige automáticamente los mismatches detectados por auditar_links_por_look.py:
  - Busca en el índice Git la imagen correcta para cada look+pose
  - Reemplaza las URLs incorrectas en galeria_outfits.md
  - Los que no tienen imagen en Git se marcan como pendientes
"""

import re, sys, subprocess, shutil
from pathlib import Path
from datetime import datetime

REPO_ROOT   = Path(r"c:\Users\farid\LaVouteDAnais")
GALERIA     = REPO_ROOT / "00_Ele" / "galeria_outfits.md"
BACKUP      = GALERIA.with_name(f"galeria_outfits.BKP3_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md")
REMOTE_BASE = "https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/"

sys.stdout.reconfigure(encoding="utf-8")

# ── Índice Git ─────────────────────────────────────────────────────────────────
git_raw = subprocess.run(
    ["git", "ls-files", "05_Imagenes"],
    capture_output=True, text=True, cwd=REPO_ROOT
).stdout.splitlines()

IMG_EXT = {'.png', '.jpg', '.jpeg', '.webp'}

POSE_KEYS = {
    'standing':    ['_standing'],
    'back_view':   ['_back_view', '_backview', '_back.', '_back_'],
    'seated':      ['_seated'],
    'side_profile':['_side_profile', '_side.', '_sideview', '_side_', '_profile'],
    'ditzy':       ['_ditzy'],
    'pov':         ['_pov'],
    'odalisque':   ['_odalisque'],
    'closeup':     ['_closeup'],
    'kneeling':    ['_kneeling'],
    'lying':       ['_lying'],
    'front_arched':['_front_arched'],
    'aesthetic_bound':['_aesthetic_bound'],
}

ALT_TO_POSE = {
    'standing':    'standing',
    'de pie':      'standing',
    'back view':   'back_view',
    'espalda':     'back_view',
    'backview':    'back_view',
    'seated':      'seated',
    'sentada':     'seated',
    'side profile':'side_profile',
    'side':        'side_profile',
    'perfil':      'side_profile',
    'ditzy':       'ditzy',
    'pov':         'pov',
    'odalisque':   'odalisque',
    'odalisca':    'odalisque',
    'closeup':     'closeup',
    'portrait':    'closeup',
    'kneeling':    'kneeling',
    'lying':       'lying',
    'lying down':  'lying',
    'front arched':'front_arched',
    'aesthetic bound':'aesthetic_bound',
}

# Construir índice: (look_num, pose_key) -> ruta
image_index = {}
for f in git_raw:
    if Path(f).suffix.lower() not in IMG_EXT:
        continue
    f_lower = f.replace("\\", "/").lower()
    # Excluir duplicate_look_folders
    if "duplicate_look_folders" in f_lower:
        continue
    m = re.search(r"look0*(\d+)[_/]", f_lower)
    if not m:
        continue
    look_n = int(m.group(1))
    fname = "/" + Path(f).name.lower()
    for pose_key, patterns in POSE_KEYS.items():
        if any(p in fname for p in patterns):
            key = (look_n, pose_key)
            if key not in image_index:  # primer match gana
                image_index[key] = f.replace("\\", "/")
            break

print(f"Índice: {len(image_index)} poses para {len({k[0] for k in image_index})} looks")

# ── Leer galería ───────────────────────────────────────────────────────────────
shutil.copy2(GALERIA, BACKUP)
with open(GALERIA, "r", encoding="utf-8") as f:
    content = f.read()

lines = content.splitlines()

# ── Detectar look actual por contexto ─────────────────────────────────────────
LOOK_HDR = re.compile(r"^## .*\bLook\s+(\d+)\b", re.IGNORECASE)
IMG_PAT  = re.compile(r"!\[([^\]]*)\]\((https://raw\.githubusercontent\.com[^)]+)\)")
URL_LOOK = re.compile(r"[/_](?:look|helena_look|missdoll_look|ele_look)0*(\d+)[/_]", re.IGNORECASE)

git_set_lower = {f.replace("\\", "/").lower() for f in git_raw}

def get_pose_from_alt(alt):
    return ALT_TO_POSE.get(alt.strip().lower())

def get_pose_from_url(url):
    fname = "/" + url.split("/")[-1].lower()
    for pose_key, patterns in POSE_KEYS.items():
        if any(p in fname for p in patterns):
            return pose_key
    return None

def find_correct_url(look_n, pose_key):
    """Busca la URL correcta para (look_n, pose_key). Retorna None si no existe."""
    if pose_key and (look_n, pose_key) in image_index:
        return REMOTE_BASE + image_index[(look_n, pose_key)]
    # Fallback: buscar cualquier imagen del look
    for (ln, pk), path in image_index.items():
        if ln == look_n and pk == pose_key:
            return REMOTE_BASE + path
    return None

# ── Procesar línea por línea ───────────────────────────────────────────────────
current_look = None
fixed_count  = [0]   # mutable para uso en closure
unfixable    = []
new_lines    = []

for i, line in enumerate(lines):
    hm = LOOK_HDR.match(line)
    if hm:
        current_look = int(hm.group(1))
        new_lines.append(line)
        continue

    if not IMG_PAT.search(line) or current_look is None:
        new_lines.append(line)
        continue

    def fix_img(m):
        alt = m.group(1)
        url = m.group(2)
        rel = url[len(REMOTE_BASE):].lower()

        # Detectar look en URL
        url_look_m = URL_LOOK.search(rel)
        url_look   = int(url_look_m.group(1)) if url_look_m else None
        in_git     = rel in git_set_lower
        is_duplicate = "duplicate_look_folders" in rel

        # Condición de mismatch o duplicate
        is_mismatch = url_look and url_look != current_look
        is_bad      = is_mismatch or is_duplicate or not in_git

        if not is_bad:
            return m.group(0)  # OK

        # Intentar reparar
        pose = get_pose_from_alt(alt) or get_pose_from_url(url)
        correct_url = find_correct_url(current_look, pose) if pose else None

        if correct_url:
            fixed_count[0] += 1
            return f"![{alt}]({correct_url})"
        else:
            # No hay imagen → mantener pero registrar
            unfixable.append((i + 1, current_look, url_look, alt, rel[-60:]))
            return m.group(0)

    new_line = IMG_PAT.sub(fix_img, line)
    new_lines.append(new_line)

# ── Guardar ───────────────────────────────────────────────────────────────────
with open(GALERIA, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(new_lines))

print(f"\n✅ COMPLETADO")
print(f"   URLs corregidas: {fixed_count[0]}")
print(f"   Sin imagen en Git (sin fix): {len(unfixable)}")
if unfixable:
    print("\n   No reparables:")
    for ln, cur, url_l, alt, path in unfixable:
        print(f"     L{ln}: Look {cur} | Look URL={url_l} | [{alt}] ...{path}")
