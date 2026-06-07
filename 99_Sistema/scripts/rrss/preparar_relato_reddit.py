# -*- coding: utf-8 -*-
"""Transforma un relato 'Estándar Completo Bloque' a texto Reddit-ready (self-post).
Quita la atribución + título + bloque de metadata interno + marcador <!-- more -->,
deja el teaser (hook) + la prosa, y agrega el disclosure IA/+18 al final.
Salida: 06_RRSS/reddit_relatos/<slug>.txt  (el título va aparte, en la cola).

Uso:  python preparar_relato_reddit.py
"""
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", ".."))
OUT_DIR = os.path.join(REPO, "06_RRSS", "reddit_relatos")
os.makedirs(OUT_DIR, exist_ok=True)

DISCLOSURE = ("\n\n---\n\n*Relato de ficción del universo **La Voûte d'Anaïs**. "
              "Personajes ficticios, +18. Texto asistido por IA. 🤖*")

# (slug salida, ruta relativa del relato canónico)
RELATOS = [
    ("el_mandato_de_los_tacones", "03_Literatura/02_Finalizadas/el_mandato_de_los_tacones/El_mandato_de_los_tacones.md"),
    ("ginny_la_genio_bimbo",      "03_Literatura/02_Finalizadas/ginny_la_genio_bimbo/Ginny_la_Genio_Bimbo.md"),
]

def transform(path):
    raw = open(os.path.join(REPO, path), encoding="utf-8").read()
    if "<!-- more -->" in raw:
        before, after = raw.split("<!-- more -->", 1)
    else:
        before, after = "", raw
    # teaser = último párrafo en negrita antes del <!-- more -->
    teaser = ""
    for m in re.finditer(r"\*\*(.+?)\*\*", before, flags=re.S):
        teaser = m.group(1).strip()
    # limpiar 'after': quitar --- y blancos iniciales
    after = after.lstrip()
    after = re.sub(r"^-{3,}\s*", "", after).lstrip()
    body = (("**" + teaser + "**\n\n") if teaser else "") + after.rstrip()
    body += DISCLOSURE
    return body

print("=== Relatos → Reddit-ready ===")
for slug, path in RELATOS:
    body = transform(path)
    outp = os.path.join(OUT_DIR, slug + ".txt")
    with open(outp, "w", encoding="utf-8", newline="\n") as f:
        f.write(body)
    words = len(body.split())
    ok = "✅ cabe" if len(body) <= 40000 else "❌ EXCEDE — dividir en partes"
    print(f"- {slug}: {len(body)} chars · ~{words} palabras · {ok}")
    print(f"  -> 06_RRSS/reddit_relatos/{slug}.txt")
