#!/usr/bin/env python3
import subprocess, sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

REPO = Path(r'c:\Users\farid\LaVouteDAnais')
git_files = subprocess.run(['git', 'ls-files', '05_Imagenes/ele'], capture_output=True, text=True, cwd=REPO).stdout.splitlines()

POSES = ['standing', 'back', 'seated', 'side_profile', 'ditzy', 'pov', 'odalisque']

for look_n in range(175, 182):
    folder_pat = f'look{look_n:03d}_'
    look_files = [f for f in git_files if folder_pat in f and f.endswith('.png')]
    folder_name = None
    for f in look_files:
        parts = f.split('/')
        if len(parts) >= 3 and folder_pat in parts[2]:
            folder_name = parts[2]
            break

    found_poses = set()
    for f in look_files:
        fname = Path(f).name.lower()
        for p in POSES:
            if p in fname:
                found_poses.add(p)

    missing = [p for p in POSES if p not in found_poses]
    status = f'{len(found_poses)}/7'
    fn = folder_name if folder_name else "NO FOLDER"

    print(f'Look {look_n}: {fn} -- {status} poses -- {len(look_files)} imgs')
    if missing:
        print(f'  Faltan: {missing}')
    else:
        print(f'  Completo')
