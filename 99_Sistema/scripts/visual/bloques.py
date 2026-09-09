# -*- coding: utf-8 -*-
"""Motor de tres bloques — A cuerpo · B outfit · C toma — con campos de dueño único.

Concepto de la Ama (09/09/2026): *«el bloque A es donde se describe el físico,
no debería cambiar entre prompts; el bloque B debería describir el outfit,
tampoco debería variar; el bloque C debería describir pose y ambiente»*. Y su
experiencia manda: *«mientras más detalles menos desviación»*.

La ley que sale de ahí: **un atributo, un campo, un bloque.** El detalle es
bienvenido; dos cláusulas sobre el mismo atributo son una pelea, y en la pelea
gana la de más peso, que es la equivocada (L831: la falda que se abrió). Los
tres bloques responden CUÁNDO cambia el texto (nunca / por look / por pose), y
dentro de cada uno no hay párrafo sino campos con nombre y dueño — así la
contradicción es imposible por construcción, no por detector.

El contrato vive en `campos.json` (dueño único). Este módulo lo carga, lo
valida y ensambla. Spec: `99_Sistema/specs/2026-09-09-motor-tres-bloques-design.md`.

**Un personaje nuevo es dato, nunca código** (Ama: *«debe ser flexible para
poder agregar nuevos personajes»*): perfil + entrada en `anclas_universales.json`
+ repertorio. Cero `.py`. Por eso el orden de campos A es universal.
"""
from __future__ import annotations

import json
import os
import re

AQUI = os.path.dirname(os.path.abspath(__file__))
JSON_CAMPOS = os.path.join(AQUI, "campos.json")
JSON_ANCLAS = os.path.join(AQUI, "anclas_universales.json")

_CACHE = {}


def cargar_campos(ruta=JSON_CAMPOS):
    """El contrato, cargado una vez. Lista vacía de campos = contrato roto."""
    if ruta not in _CACHE:
        with open(ruta, encoding="utf-8") as fh:
            c = json.load(fh)
        if not c.get("campos"):
            raise ValueError("campos.json sin campos: el contrato está vacío")
        _CACHE[ruta] = c
    return _CACHE[ruta]


# ======================================================================
# A · el cuerpo, por campos, desde la cerca compartida
# ======================================================================
# Un dueño, dos lectores. La cerca `ADN:BLOQUE_A` del perfil pasa a UNA LÍNEA
# POR CAMPO en el orden universal de `orden_A`, cada línea cerrando en coma.
# El motor viejo (`PromptBuilder.bloque_a`) la une con `_limpiar` y obtiene el
# mismo texto de siempre; este módulo la parte. Una línea vacía = campo que esa
# muñeca no tiene. Así una muñeca nueva llena, no configura.

from prompt_builder import PromptBuilder, cargar_config  # noqa: E402


def personajes(config=None):
    """Los slugs registrados en anclas_universales.json — nunca una lista escrita acá."""
    return sorted((config or cargar_config()).get("personajes", {}))


def _ruta_perfil(slug, config=None):
    perfil = (config or cargar_config())["personajes"][slug]
    rel = perfil["perfil_visual"]
    return os.path.normpath(os.path.join(AQUI, "..", "..", "..", rel.replace("/", os.sep)))


def lineas_adn(slug, config=None):
    """Las líneas crudas de la cerca, tal cual (vacías incluidas)."""
    with open(_ruta_perfil(slug, config), encoding="utf-8") as fh:
        m = PromptBuilder._RX_ADN.search(fh.read())
    if not m:
        raise ValueError("el perfil de '%s' no tiene la cerca %s" % (slug, PromptBuilder.MARCA_ADN))
    return m.group(1).split("\n")


def campos_a(slug, config=None):
    """{campo: texto} en el orden universal. Texto '' = la muñeca no tiene ese campo."""
    orden = cargar_campos()["orden_A"]
    lineas = lineas_adn(slug, config)
    if len(lineas) != len(orden):
        raise ValueError(
            "la cerca de '%s' tiene %d líneas y el orden universal de A tiene %d campos: "
            "una línea por campo, vacía si no aplica (%s)"
            % (slug, len(lineas), len(orden), ", ".join(orden)))
    return {campo: PromptBuilder._limpiar(l).rstrip(",").strip() for campo, l in zip(orden, lineas)}


# Vocabulario que NO puede aparecer en A. Se mide, no se promete.
# B: prenda, calzado, forma/largo de uña, corsetería. (El COLOR de sombra o de
# labios no está acá a propósito: hoy vive en A por herencia y moverlo a B
# cambia el motor viejo — decisión de la Ama, pendiente.)
RX_VOCAB_B = re.compile(
    r"\b(?:wearing|stiletto heels?|stiletto pumps?|pumps?|sandals?|boots?|platform|"
    r"corset|tightlacing|waist training|fingernails?|stiletto-shaped|thong|g-string|"
    r"stockings?|gloves?|dress|skirt|bodysuit|bikini(?! line))\b", re.I)
# «bikini line» es zona anatómica (los tatuajes de Ele van «along one hip crease
# at the bikini line»), no una prenda. Medido: el primer barrido lo marcó.
# C: pose, orientación y encuadre. (La LUZ tampoco está acá a propósito: Anaïs
# lleva «cinematic chiaroscuro… George Hurrell portraiture» en su ADN por
# herencia; sacarla cambia el motor viejo — decisión de la Ama, pendiente.)
RX_VOCAB_C = re.compile(
    r"\b(?:standing|seated|sitting|kneeling|reclining|lying|from behind|back view|"
    r"side profile|three-quarter|low angle|full body|close-up|the lens|the camera|"
    r"the frame|aspect ratio|looking at|gaze (?:locked|drifting))\b", re.I)
