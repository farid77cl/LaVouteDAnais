#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Motor de tres bloques — A cuerpo · B outfit · C toma — con campos de dueño único.

Concepto de la Ama (09/09/2026): *«el bloque A es donde se describe el físico,
no debería cambiar entre prompts; el bloque B debería describir el outfit,
tampoco debería variar; el bloque C debería describir pose y ambiente»*. Y la
ley que sale de ahí: **un atributo, un campo, un bloque**. Spec:
`99_Sistema/specs/2026-09-09-motor-tres-bloques-design.md`.

Estas pruebas se escribieron ANTES del código y se vieron fallar (regla 13,
Ley de Hierro del TDD). Cada tarea del plan agrega su bloque abajo.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).parent))

import bloques  # noqa: E402
from prompt_builder import PromptBuilder  # noqa: E402


# ======================================================================
# TAREA 1 · el contrato existe y se valida solo
# ======================================================================

def test_el_contrato_carga_y_tiene_los_tres_bloques():
    c = bloques.cargar_campos()
    assert set(c["bloques"]) == {"A", "B", "C"}


def test_cada_campo_declara_bloque_dueno_y_fuente():
    for campo in bloques.cargar_campos()["campos"]:
        assert campo["bloque"] in ("A", "B", "C"), campo["id"]
        assert campo["dueño"], campo["id"]
        assert campo["fuente"], campo["id"]


def test_ninguna_ancla_de_anclas_universales_queda_sin_bloque():
    """Las 37 anclas tienen que caer en algún campo. Una ancla sin campo es un
    atributo sin dueño — justo lo que este motor existe para eliminar."""
    anclas = json.load(open(bloques.JSON_ANCLAS, encoding="utf-8"))["anclas"]
    referidas = set()
    for c in bloques.cargar_campos()["campos"]:
        for f in c["fuente"].split("+"):
            if f.startswith("ancla:"):
                referidas.add(f.split(":", 1)[1].split("#")[0])
    faltan = sorted(set(anclas) - referidas)
    assert not faltan, faltan


def test_un_id_de_ancla_no_cae_en_dos_bloques():
    """Una ancla que se PARTE (BOTTOM_CUT_LOCK, FOOTWEAR_ECHO, DRESS_LEG_CLOSURE)
    puede alimentar dos campos, pero cada parte lleva su #sufijo: la misma parte
    jamás en dos bloques."""
    vistos = {}
    for c in bloques.cargar_campos()["campos"]:
        for f in c["fuente"].split("+"):
            if f.startswith("ancla:"):
                clave = f.split(":", 1)[1]           # con #parte si la tiene
                assert vistos.setdefault(clave, c["bloque"]) == c["bloque"], clave


def test_los_ids_de_campo_son_unicos_y_el_orden_A_los_conoce():
    c = bloques.cargar_campos()
    ids = [x["id"] for x in c["campos"]]
    assert len(ids) == len(set(ids)), "id de campo repetido"
    # orden_A mapea LÍNEA de la cerca -> campo. Solo los campos A cuyo dueño es el
    # perfil (los que vienen de un ancla universal, como el fotorrealismo, no
    # ocupan línea: se agregan después, iguales para todas las muñecas).
    de_cerca = [x["id"] for x in c["campos"] if x["bloque"] == "A" and x["fuente"] == "perfil"]
    assert c["orden_A"] == de_cerca, "orden_A tiene que listar, en orden, los campos A que salen de la cerca"


def _correr():
    import traceback
    pruebas = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    ok = fallas = 0
    for fn in pruebas:
        try:
            fn()
            ok += 1
            print(f"  ok   {fn.__name__}")
        except Exception as e:
            fallas += 1
            print(f"  FALLA {fn.__name__}: {type(e).__name__}: {e}")
            if not isinstance(e, AssertionError):
                traceback.print_exc(limit=1)
    print(f"\n  RESULTADO: {ok} ok · {fallas} fallas")
    return 1 if fallas else 0


if __name__ == "__main__":
    raise SystemExit(_correr())
