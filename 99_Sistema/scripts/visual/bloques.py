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
