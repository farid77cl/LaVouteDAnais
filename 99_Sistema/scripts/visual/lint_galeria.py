#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lint_galeria.py — Verifica que 00_Ele/galeria_outfits.md cumpla el CONTRATO
(.agent/rules/11-contrato-galeria.md), el formato que comparten la app Android,
el bot paralelo y el agente.

Chequea, por look:
  C1  slug único      — carpeta en disco == campo Ubicacion == links de la tabla 📸
  C2  slug ASCII      — sin acentos ni basura tipo 'lencer_a' / 'shangh_i'
  C3  título          — descriptivo, nunca la categoría pelada
  C4  orden           — Ubicacion/Tags ANTES del primer '###' (si no, la app queda muda)
  C5  campos ASCII    — '**Ubicacion:**' y no '**Ubicación:**'
  C6  categoría       — dentro de la lista cerrada de 10
  C7  fences          — ``` de apertura/cierre en su propia línea
  C8  negative        — bloque 'Negative Prompt' presente
  C9  carpeta única   — un solo directorio por número de look
  C10 links vivos     — cada link 📸 apunta a un archivo que existe

Uso:  python 99_Sistema/scripts/visual/lint_galeria.py [--solo-desde N]
Salida: exit 1 si hay violaciones (rompe el cierre de batch).
"""
import os, re, sys, subprocess, unicodedata
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", ".."))
ELE = os.path.join(REPO, "05_Imagenes", "ele")
GALERIA = os.path.join(REPO, "00_Ele", "galeria_outfits.md")

CATEGORIAS = {
    "Stripper", "Corporate", "Escort", "Domestic", "Pin-Up",
    "High-Fashion Editorial", "Nightclub", "Lencería", "Bikini", "Gym",
    # 11ª categoría, agregada 17/08/2026: la lista estaba VIEJA, no los looks.
    # El batch 261-270 la usa con Categoria+Subcategoria propias desde el 25/05
    # y "gala" es material declarado en el canon. Se escribía de 3 formas
    # ("Alfombra Roja / Gala", "Alfombra Roja", "Gala") — unificadas a una.
    "Alfombra Roja / Gala",
}
NORMALIZAR = {
    "Lenceria": "Lencería",
    "Alfombra Roja": "Alfombra Roja / Gala",
    "Gala": "Alfombra Roja / Gala",
    # "Mix" NO es categoría de vestuario: es la meta cromática, y se había
    # colado en el campo Categoria de 18 looks (L201-L220) cuya categoría real
    # vivía en Subcategoria. Corregido 17/08/2026 leyendo el campo, no adivinando.
    "Mix": "(meta cromática, no categoría — usar la de Subcategoria)",
    "Gym/Athleisure": "Gym",
    "HF Editorial": "High-Fashion Editorial",
}
POSES = ["standing", "back_view", "seated", "side_profile", "ditzy", "pov", "odalisque"]

SOLO_DESDE = 0
if "--solo-desde" in sys.argv:
    SOLO_DESDE = int(sys.argv[sys.argv.index("--solo-desde") + 1])


def slugify(titulo: str) -> str:
    """Algoritmo del contrato §2 — el mismo que usa la app sobre el título."""
    t = titulo.lower()
    t = t.replace("-", "").replace("'", "").replace("’", "")
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    t = re.sub(r"[^a-z0-9]+", "_", t).strip("_")
    return t


def es_ascii_limpio(s: str) -> bool:
    return all(ord(c) < 128 for c in s)


def rutas_en_git():
    """Rutas de 05_Imagenes/ele trackeadas por git, en POSIX.

    El lint medía el DISCO (`os.listdir` / `os.path.exists`). En la máquina
    literaria los PNG llevan skip-worktree — 709 en disco contra 5.023 en el
    índice — así que C10 reportaba 2.729 «links rotos» que estaban perfectos,
    y ese ruido enterraba los 133 hallazgos reales. La verdad es el repo.
    """
    try:
        out = subprocess.run(
            ["git", "-C", REPO, "-c", "core.quotepath=false", "ls-files", "-z",
             "05_Imagenes/ele"],
            capture_output=True, text=True, encoding="utf-8", check=True).stdout
        rutas = {p for p in out.split("\0") if p}
        if rutas:
            return rutas
    except Exception as e:
        print(f"⚠️  git ls-files falló ({e}); cayendo a disco")
    # Fallback: disco (repos sin git o sin índice)
    rutas = set()
    for raiz, _, archivos in os.walk(ELE):
        for a in archivos:
            rutas.add(os.path.relpath(os.path.join(raiz, a), REPO).replace(os.sep, "/"))
    return rutas


RUTAS_GIT = None   # se llena en main()


def carpetas_por_look():
    d = defaultdict(list)
    vistas = set()
    for ruta in sorted(RUTAS_GIT or ()):
        partes = ruta.split("/")
        if len(partes) < 4:
            continue
        carpeta = partes[2]
        if carpeta in vistas:
            continue
        vistas.add(carpeta)
        m = re.match(r"look0*(\d+)_", carpeta.lower())
        if m:
            d[int(m.group(1))].append(carpeta)
    return d


def main():
    global RUTAS_GIT
    texto = open(GALERIA, encoding="utf-8").read()
    RUTAS_GIT = rutas_en_git()
    folders = carpetas_por_look()
    fallas = defaultdict(list)   # look -> [mensajes]
    looks = 0

    for blk in re.split(r"(?=^## .*?Look \d+:)", texto, flags=re.M):
        m = re.match(r"^## .*?Look (\d+):\s*(.+?)\s*\(", blk)
        if not m:
            continue
        n, titulo = int(m.group(1)), m.group(2).strip()
        if n < SOLO_DESDE:
            continue
        looks += 1

        # --- C5: clave del campo en ASCII ---
        if "**Ubicación:**" in blk:
            fallas[n].append("C5 campo '**Ubicación:**' con tilde (deja ciego al parser de la app)")

        # --- C3: título descriptivo, no la categoría pelada ---
        if titulo in CATEGORIAS or titulo in NORMALIZAR or titulo.rstrip("s") in {"Gym", "Bikini"}:
            fallas[n].append(f"C3 título '{titulo}' es la categoría pelada → slug que colisiona")

        # --- C6: categoría de la lista cerrada ---
        mcat = re.search(r"\*\*Categor[ií]a:\*\*\s*(.+)", blk)
        cat_head = None
        mh = re.match(r"^## .*?Look \d+:.*?\((.*?)\)\s*$", blk.split("\n")[0])
        if mh:
            partes = [p.strip() for p in mh.group(1).split("·")]
            for p in partes:
                if p in CATEGORIAS or p in NORMALIZAR:
                    cat_head = p
                    break
        cat = (mcat.group(1).strip() if mcat else cat_head)
        if cat and cat not in CATEGORIAS:
            sug = NORMALIZAR.get(cat)
            fallas[n].append(f"C6 categoría '{cat}' fuera de la lista cerrada" + (f" → usar '{sug}'" if sug else ""))

        # --- C1/C2/C9: slug ---
        mu = re.search(r"\*\*Ubicaci[oó]n:\*\*\s*`?([^`\n]+)`?", blk)
        declarado = mu.group(1).strip().rstrip("/").split("/")[-1] if mu else None
        reales = folders.get(n, [])

        if len(reales) > 1:
            fallas[n].append(f"C9 {len(reales)} carpetas para el mismo look: {reales}")

        for r in reales:
            if not es_ascii_limpio(r):
                fallas[n].append(f"C2 carpeta con caracteres no-ASCII: '{r}'")
            if re.search(r"_[a-z]$", r) and len(r.rsplit("_", 1)[-1]) == 1:
                fallas[n].append(f"C2 carpeta con cola de acento mal plegado: '{r}'")

        if declarado and reales and declarado not in reales:
            fallas[n].append(f"C1 Ubicacion declara '{declarado}' pero en disco está {reales}")

        esperado = f"look{n}_" + slugify(titulo)
        if reales and esperado not in reales and titulo not in CATEGORIAS:
            fallas[n].append(f"C1 el slug del título sería '{esperado}' pero la carpeta es '{reales[0]}'")

        # --- C4: metadata antes del primer '###' ---
        head_idx = blk.find("\n###")
        cabecera = blk[:head_idx] if head_idx > 0 else blk
        if "**Ubicacion:**" not in cabecera and "**Ubicación:**" not in cabecera:
            fallas[n].append("C4 'Ubicacion' no está antes del primer '###' (canonicalInfo vacío en la app)")

        # --- C7: fences bien formados ---
        if re.search(r"```[^\n`]+```", blk):
            fallas[n].append("C7 fence en una sola línea (mezcla prompts entre poses/looks)")
        if blk.count("```") % 2 != 0:
            fallas[n].append("C7 fences impares (bloque de código sin cerrar)")

        # --- C8: negative prompt ---
        if "Negative Prompt" not in blk:
            fallas[n].append("C8 sin bloque 'Negative Prompt'")

        # --- C10: links vivos (contra el índice de git, no contra el disco) ---
        for link in re.findall(r"\(\.\./\.\./(05_Imagenes/ele/[^)]+\.png)\)", blk):
            if link not in RUTAS_GIT:
                fallas[n].append(f"C10 link roto: {link}")

    # ---------------- reporte ----------------
    print(f"== Lint del contrato de galeria_outfits.md ==")
    print(f"   Looks auditados: {looks}" + (f" (desde L{SOLO_DESDE})" if SOLO_DESDE else ""))

    if not fallas:
        print("\n✅ CONTRATO EN VERDE — los tres actores hablan lo mismo.")
        return 0

    por_codigo = defaultdict(int)
    for msgs in fallas.values():
        for msg in msgs:
            por_codigo[msg.split()[0]] += 1

    print(f"\n❌ {len(fallas)} look(s) con violaciones · {sum(len(v) for v in fallas.values())} hallazgo(s)\n")
    print("   Resumen por regla:")
    desc = {
        "C1": "slug único (carpeta = Ubicacion = título)",
        "C2": "slug ASCII", "C3": "título descriptivo", "C4": "orden de metadata",
        "C5": "campo con tilde", "C6": "categoría fuera de lista", "C7": "fences",
        "C8": "sin Negative Prompt", "C9": "carpeta duplicada", "C10": "link roto",
    }
    for c in sorted(por_codigo):
        print(f"     {c:<4} {desc.get(c,''):<38} {por_codigo[c]:>5}")

    print("\n   Detalle (primeros 25 looks):")
    for n in sorted(fallas)[:25]:
        print(f"     L{n}:")
        for msg in fallas[n][:4]:
            print(f"        · {msg}")
    if len(fallas) > 25:
        print(f"     … y {len(fallas)-25} look(s) más.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
