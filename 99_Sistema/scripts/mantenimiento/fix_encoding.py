#!/usr/bin/env python3
"""Script para corregir encoding mojibake en archivos markdown."""
import os

# Reemplazos en formato bytes para evitar problemas de encoding
BYTE_REPLACEMENTS = [
    # Emojis rotos comunes
    (b'\xc3\x90\xc2\x9f', b''),  # Limpiar prefijo roto
    (b'\xc3\xa2\xc2\x80\xc2\x94', b'\xe2\x80\x94'),  # em-dash
    (b'\xc3\xa2\xc2\x80\xc2\x99', b'\xe2\x80\x99'),  # apostrophe
    (b'\xc3\xa2\xc2\x86\xc2\x92', b'\xe2\x86\x92'),  # arrow
    (b'\xc3\xa2\xc2\x9c\xc2\x85', b'\xe2\x9c\x85'),  # check
    (b'\xc3\xa2\xc2\x9c\xc2\xa8', b'\xe2\x9c\xa8'),  # sparkles
    (b'\xc3\xa2\xc2\x9b\xc2\x93', b'\xe2\x9b\x93'),  # chains
    (b'\xc3\xa2\xc2\x8c\xc2\x98', b'\xe2\x8c\x98'),  # command key
    # Caracteres espanoles rotos
    (b'\xc3\x83\xc2\xa1', b'\xc3\xa1'),  # a con tilde
    (b'\xc3\x83\xc2\xa9', b'\xc3\xa9'),  # e con tilde
    (b'\xc3\x83\xc2\xad', b'\xc3\xad'),  # i con tilde
    (b'\xc3\x83\xc2\xb3', b'\xc3\xb3'),  # o con tilde
    (b'\xc3\x83\xc2\xba', b'\xc3\xba'),  # u con tilde
    (b'\xc3\x83\xc2\xb1', b'\xc3\xb1'),  # n con tilde
    (b'\xc3\x83\xc2\xaf', b'\xc3\xaf'),  # i con dieresis
    (b'\xc3\x83\xc5\x93', b'\xc3\x93'),  # O con tilde
    (b'\xc3\x83\xc2\x89', b'\xc3\x89'),  # E mayuscula
]

def fix_file(filepath):
    try:
        with open(filepath, 'rb') as f:
            content = f.read()
        
        original = content
        for wrong, correct in BYTE_REPLACEMENTS:
            content = content.replace(wrong, correct)
        
        if content != original:
            with open(filepath, 'wb') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    base = r"C:\Users\fabara\LaVouteDAnais\00_Helena"
    files = ["memoria_sesiones.md", "galeria_outfits.md", "mi_diario_de_servicio.md"]
    
    for f in files:
        path = os.path.join(base, f)
        if os.path.exists(path):
            result = fix_file(path)
            print(f"{'OK' if result else 'Sin cambios'}: {f}")

if __name__ == "__main__":
    main()
