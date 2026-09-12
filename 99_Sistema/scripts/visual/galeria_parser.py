#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
galeria_parser.py — Parser de galerias del outfit-engine, compartido.

Parsea la galeria markdown EXACTAMENTE como la parsea LV-App (port de
`GitRepository.parseMarkdown`, repo farid77cl/LV-App). Es el unico dueño de
este formato: lo usa `lint_prompts_personaje.py` para auditar lo que la app
REALMENTE va a ingerir, y lo usa el generador del indice de LV-App-3 para
producir el JSON que la app Android consume. Copiar este parser en vez de
importarlo dejaria dos duenos del mismo formato — la misma trampa en la que
cayo `color_canon.py`, que quedo sin quien lo llamara desde el 29/08.
"""

import re
import sys
import unicodedata

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# --- puerto del parser de la app -------------------------------------------

LOOK_HEADING = re.compile(
    r"(?i).*?\b(?:Look|Boudoir)\s+(?:[A-Za-z]+)?(\d+)\b[:\s]*(.*?)(?:\((.*)\))?\s*$")
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")


def sin_tildes(s):
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn")


POSES_CANON = ["standing", "back_view", "seated", "side_profile", "slot5", "pov", "odalisque"]

_DISPLAY_A_SLUG = {
    "Standing": "standing",
    "Back View": "back_view",
    "Seated": "seated",
    "Side Profile": "side_profile",
    "POV": "pov",
    "Odalisque": "odalisque",
}


def _extraer_campo_simple(texto, campo):
    """Extrae el valor de `**campo:**` del cuerpo crudo (sin fences) de un look.

    Cubre las DOS formas reales que usan las tres galerías para el campo de
    arquetipo (Ama 12/09/2026, Tarea 5 ux-flujo-corto): `- **Categoria:**
    valor` / `- **Arquetipo:** valor` en línea propia (forma canónica de Ele
    y de la mayoría de Miss Doll, dentro del bloque canon) y `**Arquetipo:**
    valor · **Paleta:** ...` compartiendo línea con más campos (forma que usa
    Anaïs desde el reset del 11/08/2026 y que Miss Doll adoptó también desde
    el Look 47 — ninguna convención reemplazó a la otra, conviven en la misma
    galería). El valor se corta en el primer `·` y se le quita cualquier
    emoji pegado (Miss Doll escribe `🎀 Girly Girl` en esa segunda forma).
    """
    if not campo:
        return None
    m = re.search(rf"\*\*{re.escape(campo)}:\*\*\s*([^\n]*)", texto)
    if not m:
        return None
    valor = m.group(1).split("·")[0]
    valor = EMOJI.sub("", valor).strip().strip("*").strip()
    return valor or None


def slug_de_pose(nombre_display, slot5):
    """Nombre de pose para mostrar -> llave canónica del JSON.

    La quinta pose se llama distinto en cada muñeca (Ditzy / Glacial Command /
    Sovereign Gaze) y en el artefacto SIEMPRE viaja como `slot5`: el nombre
    bonito vive una sola vez, en la cabecera del índice.
    """
    if nombre_display == slot5:
        return "slot5"
    return _DISPLAY_A_SLUG.get(nombre_display)


def detectar_pose(linea, slot5):
    """Mismo arbol de decision que el parser de la app (orden incluido)."""
    t = linea.lower()
    m = re.match(r"^(?:\*\*)?(?:PROMPT\s+)?(\d+)[.\s—]+(?:[A-Za-z0-9-]+\s+)?(.*?)(?:[:\*]+|$)", linea)
    if m:
        t = m.group(2).strip().lower()
        num = int(m.group(1))
    else:
        num = None
    orden = [
        (["standing", "cruel contrapposto", "cruel_contrapposto", "c-1", "c1"], "Standing"),
        (["back view", "back_view", "espalda", "c-3", "c3"], "Back View"),
        (["seated", "monarch throne", "monarch_throne", "c-2", "c2"], "Seated"),
        (["side profile", "profile", "tres cuartos", "three_quarter", "three-quarter", "c-4", "c4"], "Side Profile"),
        (["ditzy", "glacial command", "glacial_command", "sovereign gaze", "sovereign_gaze",
          "close up fria", "close_up_fria", "c-5", "c5"], slot5),
        (["pov", "close up", "intimate", "c-6", "c6"], "POV"),
        (["odalisque", "throne en suelo", "throne_suelo", "throne_en_suelo", "c-7", "c7"], "Odalisque"),
    ]
    for i, (claves, nombre) in enumerate(orden):
        for k in claves:
            if k in t:
                if i == 1 and k == "back view" or k != "back view":
                    pass
                return nombre
        if i == 1 and "back" in t and "background" not in t:
            return "Back View"
    if m and num is not None:
        return {1: "Standing", 2: "Back View", 3: "Seated", 4: "Side Profile",
                5: slot5, 6: "POV", 7: "Odalisque"}.get(num)
    return None


def parse_como_la_app(texto, slot5, campo_arquetipo=None):
    """Devuelve [{num, titulo, meta, ubicacion, tags, negative, arquetipo, prompts:{pose:txt}}].

    `campo_arquetipo` es el nombre del campo declarado en
    `anclas_universales.json → personajes.<slug>.campo_arquetipo`
    ("Categoria" para Ele, "Arquetipo" para Miss Doll/Anaïs). `None` (el
    default, usado por los llamadores que no lo necesitan, p.ej.
    `construir_prompts`) deja `arquetipo` en `None` para todos los looks.
    """
    looks = []
    cur = None
    pose = None
    leyendo_codigo = False
    leyendo_canon = False
    buf = []
    canon = []
    arq_buf = []

    def cerrar_arquetipo():
        if cur is not None:
            cur["arquetipo"] = _extraer_campo_simple("\n".join(arq_buf), campo_arquetipo)

    def cerrar_prompt():
        nonlocal pose, buf
        txt = "\n".join(buf).strip()
        if txt and pose and cur is not None:
            cur["prompts"][pose] = cur["prompts"].get(pose, [])
            cur["prompts"][pose].append(txt)
            pose = None
        buf = []

    def cerrar_canon():
        if cur is None:
            return
        for l in canon:
            s = l.strip()
            if s.startswith("- **"):
                clave = sin_tildes(s.split(":**")[0][4:].strip()).lower()
                valor = s.split(":**", 1)[1].strip().strip("`").strip() if ":**" in s else ""
                if clave == "ubicacion":
                    cur["ubicacion"] = valor
                elif clave == "tags":
                    cur["tags"] = valor

    for linea in texto.split("\n"):
        t = linea.strip()
        m = LOOK_HEADING.match(t) if t.startswith("#") else None
        if m:
            if leyendo_codigo:
                leyendo_codigo = False
                cerrar_prompt()
            cerrar_canon()
            cerrar_arquetipo()
            canon = []
            arq_buf = []
            leyendo_canon = True
            cur = {"num": int(m.group(1)), "titulo": (m.group(2) or "").strip(),
                   "meta": (m.group(3) or "").strip() or None,
                   "ubicacion": None, "tags": None, "negative": None,
                   "arquetipo": None, "prompts": {}}
            looks.append(cur)
            pose = None
            continue
        if cur is None:
            continue

        # El campo de arquetipo se busca en TODO el cuerpo del look fuera de
        # fences, no solo en el bloque canon (ubicacion/tags): la forma
        # inline de Anaïs/Miss-Doll-desde-L47 vive DESPUÉS del primer
        # `### 📸 Imágenes`, que es justo donde `leyendo_canon` ya cerró.
        if not leyendo_codigo:
            arq_buf.append(linea)

        if leyendo_canon:
            if t.startswith("### "):
                leyendo_canon = False
            else:
                canon.append(linea)

        es_pose_header = t.startswith("**") and t.endswith(":**")
        es_negative = t.startswith("**Negative Prompt:**") or t.startswith("**Negative prompt:**")

        if leyendo_codigo and (es_pose_header or t.startswith("###") or es_negative):
            leyendo_codigo = False
            cerrar_prompt()

        if es_negative:
            mm = re.search(r"`([^`]+)`", t)
            if mm:
                cur["negative"] = mm.group(1).strip()
            continue

        if leyendo_codigo:
            if t.startswith("```"):
                leyendo_codigo = False
                cerrar_prompt()
            else:
                buf.append(linea)
            continue

        if not t.startswith("`") and (len(t) < 100 or "prompt" in t.lower()):
            p = detectar_pose(t, slot5)
            if p:
                pose = p
                inline = re.search(r"`(.*?)`", t)
                if inline and inline.group(1).strip():
                    cur["prompts"].setdefault(pose, []).append(inline.group(1).strip())
                    pose = None
                continue

        if t.startswith("```"):
            if pose:
                leyendo_codigo = True
            continue

    if leyendo_codigo:
        cerrar_prompt()
    cerrar_canon()
    cerrar_arquetipo()
    return looks
