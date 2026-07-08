#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
consolidar_carpetas_looks.py
============================
Analiza 05_Imagenes/ele/ y produce un plan de acción:
  - Carpetas lookXX_* vacías (o solo README) que tienen look0XX_* → ELIMINAR
  - Carpetas lookXX_* con imágenes sin look0XX_* equivalente → RENOMBRAR a look0XX_*
  - Carpetas lookXX_* con imágenes Y look0XX_* también existe → FUSIONAR → ELIMINAR legacy

Fase 1: Solo diagnóstico (dry run)
Fase 2: Ejecutar con --execute
"""

import re, sys, os, shutil, subprocess
from pathlib import Path
from collections import defaultdict

REPO_ROOT = Path(r"c:\Users\farid\LaVouteDAnais")
ELE_DIR   = REPO_ROOT / "05_Imagenes" / "ele"
EXECUTE   = "--execute" in sys.argv

sys.stdout.reconfigure(encoding="utf-8")

# ── Clasificar carpetas ────────────────────────────────────────────────────────
LOOK_PAT = re.compile(r"^look0*(\d+)_(.+)$")

folders = {}
for d in sorted(ELE_DIR.iterdir()):
    if not d.is_dir():
        continue
    m = LOOK_PAT.match(d.name)
    if not m:
        continue
    look_n   = int(m.group(1))
    suffix   = m.group(2)
    is_zeropad = d.name.startswith(f"look{look_n:03d}_")
    
    # Contar archivos (excluyendo README)
    files = [f for f in d.rglob("*") if f.is_file() and f.name.lower() != "readme.md"]
    img_files = [f for f in files if f.suffix.lower() in {'.png', '.jpg', '.jpeg', '.webp'}]
    
    if look_n not in folders:
        folders[look_n] = {"zeropad": [], "legacy": []}
    
    entry = {
        "path": d,
        "name": d.name,
        "suffix": suffix,
        "total_files": len(files),
        "img_files": len(img_files),
        "all_files": files,
        "all_imgs": img_files,
    }
    
    if is_zeropad:
        folders[look_n]["zeropad"].append(entry)
    else:
        folders[look_n]["legacy"].append(entry)

# ── Análisis ───────────────────────────────────────────────────────────────────
actions_delete  = []  # (path, reason)
actions_rename  = []  # (old_path, new_path)
actions_merge   = []  # (src_path, dst_path, files_to_move)

for look_n in sorted(folders):
    zp = folders[look_n]["zeropad"]
    lg = folders[look_n]["legacy"]
    
    if not lg:
        continue  # no hay legacy, nada que hacer
    
    for legacy_entry in lg:
        if legacy_entry["img_files"] == 0:
            # Sin imágenes → eliminar
            if zp:
                actions_delete.append((legacy_entry["path"], 
                    f"Vacía/solo-README, ya existe {zp[0]['name']}"))
            else:
                actions_delete.append((legacy_entry["path"], 
                    f"Vacía/solo-README, sin equivalente zero-pad"))
        else:
            # Tiene imágenes
            if zp:
                # Fusionar imágenes al zero-pad, luego eliminar legacy
                dst = zp[0]["path"]
                files_to_move = legacy_entry["all_imgs"]
                actions_merge.append((legacy_entry["path"], dst, files_to_move))
            else:
                # Renombrar a zero-pad
                new_name = f"look{look_n:03d}_{legacy_entry['suffix']}"
                new_path = ELE_DIR / new_name
                if not new_path.exists():
                    actions_rename.append((legacy_entry["path"], new_path))
                else:
                    # Nombre ya existe (raro pero seguro)
                    actions_merge.append((legacy_entry["path"], new_path, legacy_entry["all_imgs"]))

# ── Reporte ────────────────────────────────────────────────────────────────────
print("=" * 70)
print(f"  DIAGNÓSTICO — Consolidación de carpetas look en 05_Imagenes/ele/")
print(f"  Modo: {'⚡ EJECUCIÓN' if EXECUTE else '🔍 DRY RUN (usar --execute para aplicar)'}")
print("=" * 70)

print(f"\n🗑️  ELIMINAR (vacías/solo-README): {len(actions_delete)}")
for path, reason in actions_delete:
    print(f"  ❌ {path.name}  — {reason}")

print(f"\n📁 RENOMBRAR (sin equivalente zero-pad): {len(actions_rename)}")
for old, new in actions_rename:
    print(f"  📂 {old.name} → {new.name}")

print(f"\n🔀 FUSIONAR (imágenes legacy → zero-pad): {len(actions_merge)}")
for src, dst, files in actions_merge:
    print(f"  🔀 {src.name} → {dst.name} ({len(files)} imgs)")

total = len(actions_delete) + len(actions_rename) + len(actions_merge)
print(f"\n📊 Total acciones: {total}")

# ── Ejecutar ───────────────────────────────────────────────────────────────────
if not EXECUTE:
    print("\n⚠️  Ejecutar con --execute para aplicar los cambios")
    sys.exit(0)

print("\n" + "=" * 70)
print("  EJECUTANDO...")
print("=" * 70)

# 1. Renombrar
for old, new in actions_rename:
    print(f"\n📂 Renombrando {old.name} → {new.name}")
    # git mv para mantener historial
    result = subprocess.run(
        ["git", "mv", str(old.relative_to(REPO_ROOT)), str(new.relative_to(REPO_ROOT))],
        capture_output=True, text=True, cwd=REPO_ROOT
    )
    if result.returncode != 0:
        print(f"  ⚠️ git mv falló: {result.stderr.strip()}")
        # Fallback: renombrar directo
        old.rename(new)
        print(f"  📁 Renombrado manualmente")
    else:
        print(f"  ✅ git mv exitoso")

# 2. Fusionar
for src, dst, files in actions_merge:
    print(f"\n🔀 Fusionando {src.name} → {dst.name}")
    for f in files:
        dst_file = dst / f.name
        if dst_file.exists():
            print(f"  ⚠️ Ya existe en destino: {f.name} (skip)")
            continue
        # git mv
        result = subprocess.run(
            ["git", "mv", str(f.relative_to(REPO_ROOT)), str(dst_file.relative_to(REPO_ROOT))],
            capture_output=True, text=True, cwd=REPO_ROOT
        )
        if result.returncode == 0:
            print(f"  ✅ {f.name}")
        else:
            shutil.move(str(f), str(dst_file))
            print(f"  📁 {f.name} (movido manualmente)")
    # Eliminar carpeta legacy si queda vacía o solo README
    remaining = [f for f in src.rglob("*") if f.is_file()]
    if len(remaining) <= 1:  # solo README o vacía
        # git rm la carpeta
        subprocess.run(
            ["git", "rm", "-rf", str(src.relative_to(REPO_ROOT))],
            capture_output=True, text=True, cwd=REPO_ROOT
        )
        print(f"  🗑️ {src.name} eliminada")

# 3. Eliminar
for path, reason in actions_delete:
    print(f"\n🗑️ Eliminando {path.name}")
    result = subprocess.run(
        ["git", "rm", "-rf", str(path.relative_to(REPO_ROOT))],
        capture_output=True, text=True, cwd=REPO_ROOT
    )
    if result.returncode == 0:
        print(f"  ✅ Eliminada vía git rm")
    else:
        # Carpeta no tracked? Eliminar directo
        if path.exists():
            shutil.rmtree(path)
            print(f"  📁 Eliminada manualmente")
        else:
            print(f"  ⚠️ Ya no existe")

print(f"\n✅ Consolidación completada. Ejecutar git commit para confirmar.")
