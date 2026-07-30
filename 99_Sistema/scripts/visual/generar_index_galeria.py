#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar_index_galeria.py
========================
Genera 00_Ele/galeria_index.md — índice rápido y navegable de todos
los looks registrados en galeria_outfits.md.

Columnas del índice:
  N° | Nombre | Fecha | Categoría | Paleta | Materiales | Poses | Estado

Incluye:
  - Tabla ordenada por número de look
  - Sección de búsqueda por categoría
  - Sección de búsqueda por paleta/color dominante
"""

import re
import sys
from pathlib import Path
from datetime import datetime

GALERIA_PATH = Path(r"c:\Users\farid\LaVouteDAnais\00_Ele\galeria_outfits.md")
INDEX_PATH   = Path(r"c:\Users\farid\LaVouteDAnais\00_Ele\galeria_index.md")

# ── Metadata del TÍTULO (contrato §4) ───────────────────────────────────────
# El contrato manda la metadata en el heading, no en campos:
#   ## Look N: <Título> (<fecha> · batch L<X>-L<Y> "<Tema>" · <Cat> · <Subcat> · <Modo>)
# Los campos `- **Categoria:**` son el formato viejo (491 looks) y conviven con
# el nuevo (110 looks). Antes este índice sólo miraba los campos, así que los
# looks en formato de contrato salían con toda la fila en «—».
CATEGORIAS = ["High-Fashion Editorial", "Alfombra Roja / Gala", "Alfombra Roja",
              "Pin-Up", "Stripper", "Corporate", "Escort", "Domestic",
              "Nightclub", "Lencería", "Lenceria", "Bikini", "Gym/Athleisure", "Gym"]
MODOS = ["Neutro+Pop", "Monoblock", "Contraste", "Triada", "Gradiente"]
MATERIALES = ["vinyl", "pvc", "latex", "látex", "wet-look", "wetlook", "chrome", "lamé",
              "lame", "satin", "satén", "mesh", "crystal", "rhinestone", "leather",
              "cuero", "iridescent", "holographic", "leopard", "python", "zebra", "tiger"]

def parse_titulo(titulo: str) -> tuple[str, dict]:
    """Devuelve (nombre limpio, metadata) leyendo el paréntesis del heading."""
    m = re.match(r'^(.*?)\s*\((.*)\)\s*$', titulo.strip(), re.S)
    if not m:
        return titulo.strip(), {}
    nombre, meta = m.group(1).strip(), m.group(2)
    partes = [p.strip() for p in re.split(r'\s*[·|]\s*', meta) if p.strip()]
    d: dict = {}
    for p in partes:
        fm = re.search(r'\b(\d{2}/\d{2}/\d{4})\b', p)
        if fm and "fecha" not in d:
            d["fecha"] = fm.group(1)
        if "categoria" not in d:
            for c in CATEGORIAS:
                if re.search(r'\b' + re.escape(c) + r'\b', p, re.I):
                    d["categoria"] = "Lencería" if c.lower() == "lenceria" else (
                                     "Gym" if c.lower() == "gym/athleisure" else c)
                    break
        if "modo" not in d:
            for k in MODOS:
                if re.search(re.escape(k), p, re.I):
                    d["modo"] = k
                    break
    return nombre, d

def materiales_de_tags(block: str) -> str:
    m = re.search(r'\*\*Tags:?\*\*\s*(.+?)(?:\n|$)', block)
    if not m:
        return ""
    tags = [t.lstrip("#").lower() for t in re.findall(r'#[\w\-áéíóúñ]+', m.group(1))]
    hit = [t for t in tags if t in MATERIALES]
    return ", ".join(dict.fromkeys(hit))

# ── Parser ──────────────────────────────────────────────────────────────────

def parse_galeria(path: Path) -> list[dict]:
    """Extrae metadatos de cada look de la galería."""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    looks = []
    # Separar por bloques de look (## ... Look N ...)
    blocks = re.split(r'\n(?=## )', content)
    total_blocks = len(blocks)
    print(f"  -> Parseando {total_blocks} bloques de galeria_outfits.md...", flush=True)

    for idx, block in enumerate(blocks, start=1):
        if idx % 100 == 0 or idx == total_blocks:
            print(f"  -> Parseo galería: {idx}/{total_blocks} bloques analizados ({int(idx/total_blocks*100)}%)", flush=True)

        # Encabezado de look
        m = re.match(r'^## .{0,10}Look (\d+)[:\s]*(.+?)(?:\n|$)', block)
        if not m:
            continue

        num   = int(m.group(1))
        titulo_crudo = m.group(2).strip().rstrip('*').strip()
        # El nombre limpio y la metadata salen del propio heading (contrato §4)
        name, meta = parse_titulo(titulo_crudo)

        # Fecha: campo si existe, si no la del título
        fecha_m = re.search(r'\*\*Fecha:?\*\*\s*(.+?)(?:\n|$)', block)
        fecha = fecha_m.group(1).strip() if fecha_m else meta.get("fecha", "—")

        # Categoría: campo (formato viejo) → título (contrato). La clave va sin
        # tilde por regla 11 §5, pero se acepta tildada por si queda alguna.
        cat_m = re.search(r'\*\*Categor[ií]a:?\*\*\s*(.+?)(?:\n|$)', block)
        categoria = cat_m.group(1).strip() if cat_m else meta.get("categoria", "—")

        # Paleta: no existe como campo en ningún look; el modo cromático del
        # título es lo más cercano y es lo que gobierna el anti-monoblock.
        pal_m = re.search(r'\*\*Paleta:?\*\*\s*(.+?)(?:\n|$)', block)
        paleta = pal_m.group(1).strip() if pal_m else meta.get("modo", "—")

        # Materiales: campo → tags (#vinyl, #latex, #chrome…)
        mat_m = re.search(r'\*\*Materiales:?\*\*\s*(.+?)(?:\n|$)', block)
        materiales = mat_m.group(1).strip() if mat_m else (materiales_de_tags(block) or "—")

        # Poses / estado de imágenes — buscar "### 📸 Imágenes (X/Y..."
        img_m = re.search(r'### 📸 Imágenes\s*\((\d+/\d+)', block)
        if img_m:
            poses = img_m.group(1)
        else:
            # Contar líneas de imagen markdown como fallback
            img_lines = re.findall(r'!\[.*?\]\(.*?\)', block)
            poses = f"{len(img_lines)}/?" if img_lines else "0/?"

        # Estado
        estado_m = re.search(r'\*\*Estado:\*\*\s*(.+?)(?:\n|$)', block)
        if estado_m:
            estado = estado_m.group(1).strip()
        elif "Completo" in block or "COMPLETO" in block or "completo" in block:
            estado = "✅ Completo"
        elif "Pendiente" in block:
            estado = "⏳ Pendiente"
        else:
            estado = "—"

        looks.append({
            "num":        num,
            "name":       name,
            "fecha":      fecha,
            "categoria":  categoria,
            "paleta":     paleta,
            "materiales": materiales,
            "poses":      poses,
            "estado":     estado,
        })

    looks.sort(key=lambda x: x["num"])
    return looks


# ── Generador de índice ──────────────────────────────────────────────────────

def gen_index(looks: list[dict]) -> str:
    # Salida DETERMINISTA (Ama 16/06/2026): sin fecha/hora volátil. Antes tenía HH:MM ->
    # el índice churneaba cada minuto y peleaba con el bot. Misma galería = mismos bytes.
    total = len(looks)

    lines = []
    lines.append("# 📇 Índice Rápido — Galería de Outfits Ele\n")
    lines.append(f"> Generado automáticamente desde la galería — **{total} looks registrados**  \n")
    lines.append("> Fuente: `00_Ele/galeria_outfits.md`  \n")
    lines.append("> Para ver prompts y detalles completos: buscar `## 👠 Look N` en la galería.\n\n")
    lines.append("---\n\n")

    # ── Tabla maestra ────────────────────────────────────────────────────────
    lines.append("## 📋 Tabla Maestra de Looks\n\n")
    lines.append("| N° | Nombre | Fecha | Categoría | Paleta | Materiales | Poses | Estado |\n")
    lines.append("|:--:|:-------|:-----:|:----------|:-------|:-----------|:-----:|:------:|\n")

    for l in looks:
        # Acortar paleta y materiales para que la tabla sea legible
        paleta_short = l["paleta"][:40] + "…" if len(l["paleta"]) > 40 else l["paleta"]
        mat_short    = l["materiales"][:35] + "…" if len(l["materiales"]) > 35 else l["materiales"]
        lines.append(
            f"| **{l['num']}** | {l['name']} | {l['fecha']} | {l['categoria']} "
            f"| {paleta_short} | {mat_short} | {l['poses']} | {l['estado']} |\n"
        )

    lines.append("\n---\n\n")

    # ── Índice por Categoría ─────────────────────────────────────────────────
    lines.append("## 🗂️ Looks por Categoría\n\n")

    cats: dict[str, list[dict]] = {}
    for l in looks:
        cat = l["categoria"] if l["categoria"] != "—" else "Sin categoría"
        cats.setdefault(cat, []).append(l)

    for cat in sorted(cats.keys()):
        items = cats[cat]
        lines.append(f"### {cat} ({len(items)} looks)\n")
        nums = ", ".join(f"**{l['num']}**" for l in items)
        lines.append(f"{nums}\n\n")

    lines.append("---\n\n")

    # ── Índice por Color Dominante ───────────────────────────────────────────
    lines.append("## 🎨 Looks por Color Dominante\n\n")

    COLOR_KEYWORDS = {
        "Rojo / Cherry / Crimson": ["red", "cherry", "crimson", "rojo", "sangre", "blood"],
        "Rosa / Hot Pink":        ["pink", "rosa", "flamingo", "bubblegum", "coral"],
        "Magenta / Fucsia":       ["magenta", "fucsia", "fuchsia"],
        "Violeta / Lila":         ["violet", "lila", "lilac", "purple", "morado"],
        "Azul / Cyan / Zafiro":   ["blue", "cyan", "azul", "cobalt", "sapphire", "indigo"],
        "Verde / Esmeralda":      ["green", "verde", "emerald", "jade", "lime"],
        "Dorado / Bronce":        ["gold", "dorado", "bronze", "bronce", "champagne", "copper"],
        "Plateado / Plata":       ["silver", "plata", "platinum", "mercury", "chrome", "steel"],
        "Blanco / Crema":         ["white", "blanco", "cream", "ivory", "crema"],
        "Negro (dominante)":      ["black", "negro", "obsidian"],
        "Naranja / Coral Neón":   ["orange", "naranja", "coral neon", "coral neón"],
        "Amarillo / Lima":        ["yellow", "amarillo", "lime", "acid"],
    }

    for color_label, keywords in COLOR_KEYWORDS.items():
        matching = [
            l for l in looks
            if any(k in l["paleta"].lower() or k in l["name"].lower() for k in keywords)
        ]
        if not matching:
            continue
        lines.append(f"### {color_label} ({len(matching)} looks)\n")
        nums = ", ".join(f"**{l['num']}**" for l in matching)
        lines.append(f"{nums}\n\n")

    lines.append("---\n\n")

    # ── Looks incompletos / pendientes ───────────────────────────────────────
    incomplete = [l for l in looks if "Pendiente" in l["estado"] or "⏳" in l["estado"] or l["poses"].startswith("0")]
    if incomplete:
        lines.append("## ⚠️ Looks Pendientes / Incompletos\n\n")
        lines.append("| N° | Nombre | Poses | Estado |\n")
        lines.append("|:--:|:-------|:-----:|:------:|\n")
        for l in incomplete:
            lines.append(f"| **{l['num']}** | {l['name']} | {l['poses']} | {l['estado']} |\n")
        lines.append("\n---\n\n")

    lines.append("*Índice generado por Ele — La Voûte d'Anaïs* 🫦👠💅\n")
    return "".join(lines)


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Leyendo {GALERIA_PATH.name}…")
    looks = parse_galeria(GALERIA_PATH)
    print(f"  → {len(looks)} looks encontrados")

    content = gen_index(looks)
    with open(INDEX_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

    print(f"  → Índice escrito en {INDEX_PATH.name}")
    print("✅ galeria_index.md generado.")


if __name__ == "__main__":
    main()
