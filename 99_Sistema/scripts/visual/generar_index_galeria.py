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

# ── Parser ──────────────────────────────────────────────────────────────────

def parse_galeria(path: Path) -> list[dict]:
    """Extrae metadatos de cada look de la galería."""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    looks = []
    # Separar por bloques de look (## ... Look N ...)
    blocks = re.split(r'\n(?=## )', content)

    for block in blocks:
        # Encabezado de look
        m = re.match(r'^## .{0,10}Look (\d+)[:\s]*(.+?)(?:\n|$)', block)
        if not m:
            continue

        num   = int(m.group(1))
        name  = m.group(2).strip().rstrip('*').strip()
        # Limpiar fecha del nombre si viene pegada: "Nombre (DD/MM/YYYY)"
        name  = re.sub(r'\s*\(\d{2}/\d{2}/\d{4}\)\s*$', '', name).strip()

        # Fecha
        fecha_m = re.search(r'\*\*Fecha:\*\*\s*(.+?)(?:\n|$)', block)
        fecha = fecha_m.group(1).strip() if fecha_m else "—"

        # Categoría
        cat_m = re.search(r'\*\*Categor[ií]a:\*\*\s*(.+?)(?:\n|$)', block)
        categoria = cat_m.group(1).strip() if cat_m else "—"

        # Paleta
        pal_m = re.search(r'\*\*Paleta:\*\*\s*(.+?)(?:\n|$)', block)
        paleta = pal_m.group(1).strip() if pal_m else "—"

        # Materiales
        mat_m = re.search(r'\*\*Materiales:\*\*\s*(.+?)(?:\n|$)', block)
        materiales = mat_m.group(1).strip() if mat_m else "—"

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
    now = datetime.now().strftime("%d/%m/%Y %H:%M")
    total = len(looks)

    lines = []
    lines.append("# 📇 Índice Rápido — Galería de Outfits Ele\n")
    lines.append(f"> Generado automáticamente el {now} — **{total} looks registrados**  \n")
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

    lines.append(f"*Índice generado por Ele — {now} — La Voûte d'Anaïs* 🫦👠💅\n")
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
