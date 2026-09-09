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


# ======================================================================
# TAREA 2 · A por campos, con la cerca compartida
# ======================================================================
# Un dueño, dos lectores. La cerca ADN:BLOQUE_A pasa a UNA LÍNEA POR CAMPO, sin
# etiquetas: el motor viejo (`PromptBuilder.bloque_a`) une las líneas con
# `_limpiar` y obtiene el mismo texto; el nuevo las parte por el orden universal.

def test_los_campos_A_unidos_son_el_bloque_a_de_siempre():
    for slug in bloques.personajes():
        viejo = PromptBuilder(slug).bloque_a
        nuevo = ", ".join(t for t in bloques.campos_a(slug).values() if t)
        assert PromptBuilder._limpiar(nuevo) == viejo, slug


def test_cada_personaje_escribe_tantas_lineas_como_campos_A_universales():
    orden = bloques.cargar_campos()["orden_A"]          # universal, NO por personaje
    for slug in bloques.personajes():
        lineas = bloques.lineas_adn(slug)
        assert len(lineas) == len(orden), (slug, len(lineas), len(orden))


def test_campos_a_devuelve_los_ids_del_orden_universal_en_orden():
    orden = bloques.cargar_campos()["orden_A"]
    for slug in bloques.personajes():
        assert list(bloques.campos_a(slug)) == orden, slug


def test_ningun_campo_A_contiene_vocabulario_de_B():
    """El cuerpo no lleva puesto nada. Hoy Anaïs sí (calzado, uñas, corsé)."""
    for slug in bloques.personajes():
        for campo, texto in bloques.campos_a(slug).items():
            m = bloques.RX_VOCAB_B.search(texto or "")
            assert not m, (slug, campo, m.group(0) if m else None, (texto or "")[:80])


def test_ningun_campo_A_contiene_vocabulario_de_C():
    """El cuerpo no trae luz ni cámara. Hoy Anaïs sí: `cinematic chiaroscuro
    dramatic lighting… George Hurrell style portraiture` viven en su ADN."""
    for slug in bloques.personajes():
        for campo, texto in bloques.campos_a(slug).items():
            m = bloques.RX_VOCAB_C.search(texto or "")
            assert not m, (slug, campo, m.group(0) if m else None)


# ======================================================================
# TAREA 3 · B por campos, desde el batch
# ======================================================================
# El batch ya declara `bloque_b` como párrafo. No se rompe: `campos_b(look)`
# acepta `bloque_b` (párrafo entero -> prenda_principal) o `campos_b` (dict por
# campo). Los batches nuevos usan el dict; los viejos siguen emitiendo.

def test_un_look_con_campos_b_por_dict_los_devuelve_en_orden_del_contrato():
    look = {"campos_b": {"calzado": "15cm black patent stiletto sandals",
                         "prenda_principal": "a plum latex bikini"}}
    b = bloques.campos_b(look)
    assert list(b) == ["prenda_principal", "calzado"]     # orden de campos.json, no del dict


def test_un_look_viejo_con_bloque_b_parrafo_sigue_emitiendo():
    b = bloques.campos_b({"bloque_b": "a plum latex bikini; 15cm black stiletto sandals"})
    assert b["prenda_principal"].startswith("a plum latex bikini")


def test_un_campo_b_desconocido_no_pasa_en_silencio():
    try:
        bloques.campos_b({"campos_b": {"prenda_principal": "x", "zapatos": "y"}})
        assert False, "debía fallar: 'zapatos' no es un campo del contrato (es 'calzado')"
    except bloques.CampoDesconocido as e:
        assert "zapatos" in str(e) and "calzado" in str(e)


def test_falta_un_campo_obligatorio_y_lo_dice_con_nombre():
    try:
        bloques.campos_b({"campos_b": {"prenda_principal": "a plum latex bikini"}}, estricto=True)
        assert False, "debía fallar: falta calzado"
    except bloques.CampoFaltante as e:
        assert "calzado" in str(e)


def test_ningun_campo_B_contiene_vocabulario_de_C():
    look = {"campos_b": {"prenda_principal": "a bikini, standing facing the camera",
                         "calzado": "black pumps"}}
    f = bloques.fugas_b(bloques.campos_b(look))
    assert any("prenda_principal" in x and "standing" in x for x in f), f


def test_un_B_limpio_no_tiene_fugas():
    look = {"campos_b": {"prenda_principal": "a plum latex bikini", "calzado": "black pumps"}}
    assert bloques.fugas_b(bloques.campos_b(look)) == []


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
