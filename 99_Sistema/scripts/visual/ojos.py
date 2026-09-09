# -*- coding: utf-8 -*-
"""Ojos para el motor — el paquete de auditoría imagen↔prompt.

Medido el 09/09/2026: **ningún auditor del motor abre un PNG**. Los 124 tests,
`lint_galeria`, `cruce`, `auditar_canon_flota`, `modularidad` y
`lint_prompts_personaje` miden TEXTO; los únicos tres scripts del repo que
importan PIL son `make_covers.py`, `publicar_bluesky.py` y
`recortar_header_tumblr.py`, ninguno del motor. Por eso los instrumentos decían
LIMPIA mientras la Ama veía fotos malas: no mentían, **miraban el otro extremo
del tubo**.

La auditoría de ese día (70 poses, tres muñecas) necesitó seis agentes externos,
y **la mitad del costo fue preparar el material**: extraer los prompts de la
galería, factorizar el bloque que las 7 poses comparten *por diseño* (la Ley de
Continuidad lo exige idéntico), y emparejarlos con las imágenes que existen de
verdad. Eso bajó cada look de ~70.000 a ~19.000 caracteres — **70 % menos**.
Hecho a mano no se repite; hecho comando, sí.

**Lo que este módulo NO hace:** juzgar la imagen. Eso necesita ojos de verdad
—la Ama, o un agente con visión— y no se simula. Acá se arma el paquete para
que quien juzgue gaste su presupuesto **en mirar, no en preparar**.

Dos fuentes, las dos ya con dueño: los prompts salen de `galeria_parser` (el
dueño único del parseo de galerías) y las imágenes de **`git ls-files`, nunca
del disco** — este repo ya pagó dos veces por leer el disco de un clon sparse
(el H7 del lint de higiene reportando 3.594 links rotos, y la auditoría de PNG
del mismo origen).
"""
from __future__ import annotations

import os
import re
import subprocess

import galeria_parser
from prompt_builder import cargar_config

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, "..", "..", ".."))


class LookNoEncontrado(ValueError):
    """El look no está en la galería de ese personaje. Se dice cuál y de quién:
    un look que no existe no puede devolver un paquete vacío en silencio."""


# --------------------------------------------------------------------------
# condensar — el 70 % de ahorro
# --------------------------------------------------------------------------

def _prefijo_comun(textos):
    if len(textos) < 2:
        return 0
    m = min(len(t) for t in textos)
    i = 0
    while i < m and len({t[i] for t in textos}) == 1:
        i += 1
    return i


def _sufijo_comun(textos, tope):
    if len(textos) < 2:
        return 0
    m = min(min(len(t) for t in textos) - tope, min(len(t) for t in textos))
    i = 0
    while i < m and len({t[-1 - i] for t in textos}) == 1:
        i += 1
    return i


def condensar(prompts):
    """Factoriza lo que TODAS las poses comparten y deja solo lo que varía.

    El bloque compartido no es redundancia: la Ley de Continuidad exige que el
    ADN y el outfit sean **idénticos** en las 7 poses. Por eso se imprime una
    vez y no siete — el auditor lo lee igual, y le sobra presupuesto para mirar.

    Devuelve `comun` · `sufijo` · `unico` {pose: texto} · las cifras del ahorro.
    Garantía probada: `comun + unico[pose] + sufijo == prompt original`.
    """
    prompts = dict(prompts or {})
    textos = list(prompts.values())
    original = sum(len(t) for t in textos)
    p = _prefijo_comun(textos)
    s = _sufijo_comun(textos, p)
    comun = textos[0][:p] if textos else ""
    sufijo = textos[0][len(textos[0]) - s:] if (textos and s) else ""
    unico = {k: v[p:len(v) - s] if s else v[p:] for k, v in prompts.items()}
    condensado = len(comun) + len(sufijo) + sum(len(v) for v in unico.values())
    return {
        "comun": comun,
        "sufijo": sufijo,
        "unico": unico,
        "chars_original": original,
        "chars_condensado": condensado,
        "ahorro_pct": round((original - condensado) * 100.0 / original, 1) if original else 0.0,
    }


# --------------------------------------------------------------------------
# la flota real — git ls-files, jamás el disco
# --------------------------------------------------------------------------

def _tracked(patron):
    try:
        out = subprocess.check_output(["git", "ls-files", patron], cwd=RAIZ,
                                      text=True, encoding="utf-8")
    except (subprocess.CalledProcessError, OSError):
        return []
    return [l for l in out.splitlines() if l.strip()]


def poses_reales(slug, look, config=None):
    """{pose: ruta} de las imágenes que EXISTEN para ese look, del índice de git."""
    cfg = config or cargar_config()
    perfil = cfg["personajes"][slug]
    slot5 = perfil.get("slot5_nombre", "Ditzy")
    carpeta = perfil.get("carpeta_imagenes", "05_Imagenes/%s" % slug)
    salida = {}
    for ruta in _tracked("%s/look%d_*" % (carpeta.rstrip("/"), int(look))):
        if not ruta.lower().endswith(".png"):
            continue
        # Se devuelve la llave CANÓNICA (`slot5`, no «ditzy»/«glacial_command»):
        # es la que permite comparar la misma toma entre las tres muñecas, y su
        # dueño único es `galeria_parser`.
        nombre = galeria_parser.detectar_pose(os.path.basename(ruta), slot5)
        if nombre:
            salida[galeria_parser.slug_de_pose(nombre, slot5)] = ruta
    return salida


# --------------------------------------------------------------------------
# el paquete
# --------------------------------------------------------------------------

_RX_TRACKER = re.compile(r"### 📸 Imágenes \(([^)]*)\)")


def _bloque_de_galeria(slug, look, config=None):
    cfg = config or cargar_config()
    ruta = os.path.join(RAIZ, cfg["personajes"][slug]["galeria"].replace("/", os.sep))
    txt = open(ruta, encoding="utf-8", newline="").read().replace("\r\n", "\n")
    cabezas = [(m.start(), int(re.search(r"\b(?:LOOK|Look)\s*0*(\d+)\b", m.group(0)).group(1)))
               for m in re.finditer(r"^#{1,4} .*?\b(?:LOOK|Look)\s*0*(\d+)\b.*$", txt, re.M)]
    for i, (pos, num) in enumerate(cabezas):
        if num == int(look):
            fin = cabezas[i + 1][0] if i + 1 < len(cabezas) else len(txt)
            return txt[pos:fin]
    raise LookNoEncontrado(
        "el look %s no está en la galería de '%s' (%s)"
        % (look, slug, cfg["personajes"][slug]["galeria"]))


def paquete(slug, look, config=None):
    """Todo lo que un auditor necesita de un look, y nada más.

    Trae los prompts condensados, las imágenes que existen de verdad, y **los
    dos números del tracker**: el declarado y el real. Esta mañana ocho looks
    decían «0/7 — Pendiente» con sus fotos ya en el índice — un auditor que
    confía en el tracker audita el vacío.
    """
    cfg = config or cargar_config()
    slot5 = cfg["personajes"][slug].get("slot5_nombre", "Ditzy")
    bloque = _bloque_de_galeria(slug, look, cfg)
    prompts = {}
    for m in re.finditer(r"^#{3}\s*\d+\.\s*(.+?)\s*$\n```(?:text)?\n(.*?)\n```",
                         bloque, re.M | re.S):
        nombre, texto = m.group(1).strip(), m.group(2)
        if len(texto) < 400:          # el BLOQUE B suelto no es un prompt de pose
            continue
        pose = galeria_parser.slug_de_pose(nombre, slot5) or nombre.lower().replace(" ", "_")
        prompts[pose] = texto
    tr = _RX_TRACKER.search(bloque)
    imagenes = poses_reales(slug, look, cfg)
    titulo = re.match(r"^#{1,4}\s*(.+)$", bloque.splitlines()[0]).group(1)
    return {
        "slug": slug, "look": int(look), "titulo": titulo,
        "prompts": prompts, "imagenes": imagenes,
        "condensado": condensar(prompts),
        "tracker_declarado": tr.group(1) if tr else None,
        "tracker_real": "%d/7" % len(imagenes),
    }


def render(p):
    """El paquete como texto, listo para pegarle a quien audite."""
    c = p["condensado"]
    L = []
    L.append("# AUDITORÍA IMAGEN↔PROMPT — %s look %d" % (p["slug"], p["look"]))
    L.append("")
    L.append(p["titulo"])
    L.append("")
    desajuste = (p["tracker_declarado"] or "").startswith(p["tracker_real"])
    L.append("- **Tracker declarado en la galería:** %s" % p["tracker_declarado"])
    L.append("- **Imágenes reales (git ls-files):** %s%s"
             % (p["tracker_real"], "" if desajuste else "   ⚠️ DESAJUSTE"))
    L.append("- **Prompts en la galería:** %d de 7" % len(p["prompts"]))
    L.append("- **Condensado:** %d → %d chars (**%s%% menos**)"
             % (c["chars_original"], c["chars_condensado"], c["ahorro_pct"]))
    L.append("")
    L.append("## Bloque COMÚN a todas las poses")
    L.append("")
    L.append("> Idéntico en las 7 **por diseño** — la Ley de Continuidad lo exige. "
             "Se imprime UNA vez; no es un defecto que se repita en el prompt real.")
    L.append("")
    L.append("```text")
    L.append(c["comun"] or "(ninguno — este look tiene una sola pose)")
    L.append("```")
    if c["sufijo"].strip():
        L.append("")
        L.append("### Sufijo común")
        L.append("")
        L.append("```text")
        L.append(c["sufijo"])
        L.append("```")
    L.append("")
    L.append("## Lo ÚNICO de cada pose, con su imagen")
    for pose in galeria_parser.POSES_CANON:
        if pose not in c["unico"] and pose not in p["imagenes"]:
            continue
        img = p["imagenes"].get(pose)
        L.append("")
        L.append("### %s" % pose)
        L.append("")
        L.append("- **Imagen:** %s" % (img if img else "⏳ NO GENERADA"))
        if pose in c["unico"]:
            L.append("")
            L.append("```text")
            L.append(c["unico"][pose])
            L.append("```")
        else:
            L.append("- ⚠️ **hay imagen y NO hay prompt en la galería**")
    faltan = [x for x in c["unico"] if x not in galeria_parser.POSES_CANON]
    for pose in faltan:
        L.append("")
        L.append("### %s  (pose fuera de la taxonomía canónica)" % pose)
        L.append("")
        L.append("```text")
        L.append(c["unico"][pose])
        L.append("```")
    return "\n".join(L)
