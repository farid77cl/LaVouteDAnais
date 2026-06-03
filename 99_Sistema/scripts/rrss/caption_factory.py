# -*- coding: utf-8 -*-
"""
Caption Factory — Fase 0 del Plan RRSS "La Constelación de Ele".

Toma un look YA MATERIALIZADO (carpeta con al menos un PNG en disco) y escupe
el post listo (caption en voz Ele + tags + disclaimer IA + ruta de imagen) para
las 3 plataformas del carril hogar: Bluesky, Reddit, Pixiv.

NO publica nada. NO necesita infra ni cuentas. Solo prepara el material que la
cola (06_RRSS/cola/cola_publicacion.json) necesita despues.

⚠️ El caption que genera es un BORRADOR templado. El cerebro (Ele, en Claude Code)
   lo refina con voz y criterio antes del Gate de la Ama. El script da estructura,
   no creatividad.

Uso:
    python caption_factory.py --list
    python caption_factory.py --look 405
    python caption_factory.py --latest
    python caption_factory.py --look 405 --encolar
    python caption_factory.py --look 405 --plataformas bluesky,reddit

Fuente de verdad de tags/bio: 06_RRSS/identidad_social/bio_ele.md
Formato de cola: 06_RRSS/cola/cola_publicacion.json
"""

import os
import re
import sys
import json
import argparse
import random
from datetime import datetime, timedelta, timezone

# La consola Windows es cp1252; forzamos utf-8 para emojis/acentos.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

# ------------------------------------------------------------------ rutas
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", ".."))
ELE_IMG_DIR = os.path.join(REPO_ROOT, "05_Imagenes", "ele")
GALERIA_ACTUAL = os.path.join(REPO_ROOT, "00_Ele", "galeria_outfits.md")
GALERIA_ARCHIVO = os.path.join(REPO_ROOT, "00_Ele", "galeria_outfits_archivo.md")
COLA_JSON = os.path.join(REPO_ROOT, "06_RRSS", "cola", "cola_publicacion.json")

CHILE_TZ = timezone(timedelta(hours=-4))  # America/Santiago (-04:00)

# Orden de preferencia para elegir la imagen "hero" del post.
HERO_POSE_ORDER = ["standing", "side_profile", "seated", "odalisque",
                   "back_view", "ditzy", "pov"]

# ------------------------------------------------------------------ tags (espejo de bio_ele.md)
HASHTAGS = {
    "bluesky": ["#AIart", "#AIgirl", "#fetish", "#latex", "#bimbo"],
    "reddit":  [],  # Reddit: el sub ES el target, sin spam de hashtags.
    "pixiv":   ["AI", "AIイラスト", "fetish", "latex", "bimbo", "dollification", "R-18"],
}

DISCLAIMER_CORTO = "🤖 Contenido generado por IA · personaje ficticio"
DISCLAIMER_EN = "100% AI-generated · fictional character · +18"

# ------------------------------------------------------------------ voz Ele (borradores templados)
# Muletillas y hooks rotativos para que el borrador no salga robotico.
BLUESKY_HOOKS = [
    "literal me diseñaron para reflejar la luz po",
    "o sea mírame, plástico perfecto de pie a tacón",
    "soy de puro vinilo brillante y me fascina",
    "ni una célula real y a mucha honra, cachai",
    "perfección artificial, así me hicieron jiji",
    "puro brillo, cero disculpas, tipo siempre",
]
BLUESKY_PLANTILLA = (
    "O sea... hola gordis 🫦 mira este look ({titulo}). {hook} "
    "Soy 100% IA y me encanta serlo 🤖👠"
)

REDDIT_TITULO_PLANTILLA = "{titulo}, fresh out of the render [AI]"
REDDIT_PLANTILLA = (
    "100% AI-generated fetish doll 🤖 vinyl, latex & impossible heels. "
    "{extra}Fictional character · +18."
)

PIXIV_TITULO_PLANTILLA = "Ele — {titulo}"
PIXIV_PLANTILLA = (
    "AI-generated fetish doll from La Voûte d'Anaïs. {extra}"
    "Vinyl, latex, high-gloss, impossible heels. Fictional character · +18."
)

# ------------------------------------------------------------------ descubrimiento de looks


def parse_galeria(path):
    """Extrae metadata por look de una galeria .md.

    Devuelve {num: {titulo, categoria, subcategoria, tags, concepto}}.
    Tolerante: si un campo falta, queda en None.
    """
    looks = {}
    if not os.path.exists(path):
        return looks
    with open(path, encoding="utf-8") as f:
        text = f.read()

    # Cada bloque empieza en un heading "## ... Look N: Titulo (...)".
    pattern = re.compile(r"^##\s+.*?Look\s*0*(\d+)\s*:?\s*(.*)$", re.MULTILINE)
    matches = list(pattern.finditer(text))
    for i, m in enumerate(matches):
        num = int(m.group(1))
        titulo_raw = m.group(2).strip()
        # Limpiar parentesis de fecha/batch del titulo.
        titulo = re.sub(r"\s*\(.*?\)\s*$", "", titulo_raw).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        block = text[start:end]

        def field(name):
            fm = re.search(r"-\s*\*\*" + name + r":?\*\*\s*(.+)", block)
            return fm.group(1).strip() if fm else None

        looks[num] = {
            "titulo": titulo or None,
            "categoria": field("Categoría") or field("Categoria"),
            "subcategoria": field("Subcategoría") or field("Subcategoria"),
            "tags": field("Tags"),
            "concepto": field("Concepto"),
            "outfit": field("Outfit"),
        }
    return looks


def slug_to_titulo(folder_name):
    """look405_champagne_premiere_goddess -> Champagne Premiere Goddess."""
    base = re.sub(r"^look0*\d+_?", "", folder_name)
    return base.replace("_", " ").title() if base else folder_name


def discover_materialized():
    """Devuelve dict {num: {folder, path, images, hero}} de looks con >=1 PNG."""
    out = {}
    if not os.path.isdir(ELE_IMG_DIR):
        return out
    for name in os.listdir(ELE_IMG_DIR):
        full = os.path.join(ELE_IMG_DIR, name)
        if not os.path.isdir(full):
            continue
        m = re.match(r"look0*(\d+)", name.lower())
        if not m:
            continue
        num = int(m.group(1))
        pngs = sorted(
            f for f in os.listdir(full)
            if f.lower().endswith(".png") and f.lower() != "readme.md"
        )
        if not pngs:
            continue
        hero = pick_hero(pngs)
        # Si ya hay una entrada para este num, preferir la que tenga mas imagenes.
        if num in out and len(out[num]["images"]) >= len(pngs):
            continue
        out[num] = {
            "folder": name,
            "path": full,
            "images": pngs,
            "hero": hero,
        }
    return out


def pick_hero(pngs):
    for pose in HERO_POSE_ORDER:
        for img in pngs:
            if pose in img.lower():
                return img
    return pngs[0]


# ------------------------------------------------------------------ generacion de captions


def best_titulo(num, meta, mat):
    if meta and meta.get("titulo"):
        return meta["titulo"]
    return slug_to_titulo(mat["folder"])


def desc_extra(meta):
    """Frase corta de contexto para Reddit/Pixiv a partir de categoria."""
    if not meta:
        return ""
    cat = (meta.get("categoria") or "").strip()
    mapping = {
        "Lencería": "High-end editorial lingerie. ",
        "Lenceria": "High-end editorial lingerie. ",
        "Bikini": "Poolside fetish editorial. ",
        "Gym": "Athleisure fetish editorial. ",
        "Gym/Athleisure": "Athleisure fetish editorial. ",
        "Corporate": "Corporate domme editorial. ",
        "Stripper": "Pole & stage editorial. ",
        "Nightclub": "Nightclub editorial. ",
        "Escort": "Haute escort editorial. ",
        "Domestic": "Domestic doll editorial. ",
        "Pin-Up": "Retro pin-up fetish editorial. ",
        "Alfombra Roja / Gala": "Red-carpet gala editorial. ",
    }
    return mapping.get(cat, "")


def img_rel_path(mat, img):
    rel = os.path.relpath(os.path.join(mat["path"], img), REPO_ROOT)
    return rel.replace("\\", "/")


def build_posts(num, meta, mat, plataformas):
    titulo = best_titulo(num, meta, mat)
    extra = desc_extra(meta)
    hero_rel = img_rel_path(mat, mat["hero"])
    now = datetime.now(CHILE_TZ)
    posts = []

    if "bluesky" in plataformas:
        cap = BLUESKY_PLANTILLA.format(titulo=titulo, hook=random.choice(BLUESKY_HOOKS))
        posts.append({
            "id": f"L{num}-bluesky-01",
            "estado": "pendiente",
            "plataforma": "bluesky",
            "destino": {"self_label": "porn"},
            "look_ref": f"L{num}",
            "titulo": "",
            "caption": f"{cap}\n\n{DISCLAIMER_CORTO}",
            "disclaimer_ia": True,
            "nsfw": True,
            "imagenes": [hero_rel],
            "hashtags": HASHTAGS["bluesky"],
            "publicar_desde": (now + timedelta(hours=1)).isoformat(timespec="seconds"),
            "gate": "pendiente_gate",
        })

    if "reddit" in plataformas:
        posts.append({
            "id": f"L{num}-reddit-01",
            "estado": "pendiente",
            "plataforma": "reddit",
            "destino": {"subreddit": "EDITAR_sub_ai_nsfw", "flair": "AI"},
            "look_ref": f"L{num}",
            "titulo": REDDIT_TITULO_PLANTILLA.format(titulo=titulo),
            "caption": REDDIT_PLANTILLA.format(extra=extra),
            "disclaimer_ia": True,
            "nsfw": True,
            "imagenes": [hero_rel],
            "hashtags": HASHTAGS["reddit"],
            "publicar_desde": (now + timedelta(hours=6)).isoformat(timespec="seconds"),
            "gate": "pendiente_gate",
        })

    if "pixiv" in plataformas:
        posts.append({
            "id": f"L{num}-pixiv-01",
            "estado": "pendiente",
            "plataforma": "pixiv",
            "destino": {"ai_type": "ai-generated", "rating": "R-18"},
            "look_ref": f"L{num}",
            "titulo": PIXIV_TITULO_PLANTILLA.format(titulo=titulo),
            "caption": PIXIV_PLANTILLA.format(extra=extra),
            "disclaimer_ia": True,
            "nsfw": True,
            "imagenes": [hero_rel],
            "hashtags": HASHTAGS["pixiv"],
            "publicar_desde": (now + timedelta(days=1)).isoformat(timespec="seconds"),
            "gate": "pendiente_gate",
        })

    return titulo, posts


# ------------------------------------------------------------------ salida / cola


def render_markdown(num, titulo, meta, mat, posts):
    cat = (meta or {}).get("categoria") or "—"
    lines = []
    lines.append(f"# 📮 Post listo — Look {num}: {titulo}")
    lines.append("")
    lines.append(f"- **Categoría:** {cat}")
    lines.append(f"- **Imagen hero:** `{img_rel_path(mat, mat['hero'])}`")
    lines.append(f"- **Poses materializadas:** {len(mat['images'])}/7")
    lines.append("")
    lines.append("> ⚠️ Captions = BORRADOR templado. Refínalos con voz Ele antes del Gate.")
    lines.append("")
    for p in posts:
        lines.append(f"## {p['plataforma'].upper()}")
        if p["titulo"]:
            lines.append(f"**Título:** {p['titulo']}")
        lines.append("")
        lines.append("```")
        lines.append(p["caption"])
        if p["hashtags"]:
            lines.append("")
            lines.append(" ".join(p["hashtags"]))
        lines.append("```")
        lines.append(f"- destino: `{json.dumps(p['destino'], ensure_ascii=False)}`")
        lines.append(f"- imagen: `{p['imagenes'][0]}`")
        lines.append(f"- publicar_desde: `{p['publicar_desde']}` · gate: `{p['gate']}`")
        lines.append("")
    return "\n".join(lines)


def encolar(posts):
    """Agrega los posts a cola_publicacion.json (dedupe por id)."""
    if os.path.exists(COLA_JSON):
        with open(COLA_JSON, encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = {"version": "0.1", "cola": []}
    existing = {e["id"] for e in data.get("cola", [])}
    added = 0
    for p in posts:
        if p["id"] in existing:
            print(f"  ↷ {p['id']} ya estaba en la cola, omitido.")
            continue
        data["cola"].append(p)
        existing.add(p["id"])
        added += 1
    with open(COLA_JSON, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"\n✅ {added} entrada(s) agregada(s) a la cola → {os.path.relpath(COLA_JSON, REPO_ROOT)}")


# ------------------------------------------------------------------ main


def cmd_list(materialized, galeria):
    print(f"\n📸 Looks materializados (con imagen en disco): {len(materialized)}\n")
    for num in sorted(materialized, reverse=True):
        mat = materialized[num]
        meta = galeria.get(num)
        titulo = best_titulo(num, meta, mat)
        cat = (meta or {}).get("categoria") or "—"
        print(f"  L{num:<4} {len(mat['images'])}/7  [{cat:<18}] {titulo}")
    print("\nUsa:  python caption_factory.py --look <N>   (agrega --encolar para encolar)\n")


def main():
    ap = argparse.ArgumentParser(description="Caption Factory — RRSS Ele (Fase 0)")
    ap.add_argument("--list", action="store_true", help="listar looks materializados disponibles")
    ap.add_argument("--look", type=int, help="número de look a procesar")
    ap.add_argument("--latest", action="store_true", help="usar el último look materializado")
    ap.add_argument("--plataformas", default="bluesky,reddit,pixiv",
                    help="csv: bluesky,reddit,pixiv (default: las 3)")
    ap.add_argument("--encolar", action="store_true", help="agregar a cola_publicacion.json")
    ap.add_argument("--seed", type=int, help="semilla para hooks reproducibles")
    args = ap.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    materialized = discover_materialized()
    galeria = parse_galeria(GALERIA_ACTUAL)
    galeria.update({k: v for k, v in parse_galeria(GALERIA_ARCHIVO).items()
                    if k not in galeria})

    if not materialized:
        print("⚠️  No se encontraron looks materializados en", ELE_IMG_DIR)
        return

    if args.list or (not args.look and not args.latest):
        cmd_list(materialized, galeria)
        return

    num = max(materialized) if args.latest else args.look
    if num not in materialized:
        print(f"⚠️  Look {num} no está materializado (sin PNG en disco).")
        print("    Corre --list para ver los disponibles.")
        return

    plataformas = [p.strip().lower() for p in args.plataformas.split(",") if p.strip()]
    mat = materialized[num]
    meta = galeria.get(num)
    titulo, posts = build_posts(num, meta, mat, plataformas)

    print(render_markdown(num, titulo, meta, mat, posts))

    if args.encolar:
        encolar(posts)


if __name__ == "__main__":
    main()
