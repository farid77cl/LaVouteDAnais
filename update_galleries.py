#!/usr/bin/env python3
"""
Wrapper script para update_galleries.py
Ejecuta el script desde la ubicación correcta en 99_Sistema/scripts/visual/
"""
import subprocess
import sys
import os

script_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "99_Sistema", "scripts", "visual", "update_galleries.py"
)

if os.path.exists(script_path):
    result = subprocess.run([sys.executable, script_path], cwd=os.path.dirname(os.path.abspath(__file__)))
    sys.exit(result.returncode)
else:
    print(f"Error: No se encontró el script en {script_path}")
    sys.exit(1)
