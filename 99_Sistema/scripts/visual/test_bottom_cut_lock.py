#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BOTTOM_CUT_LOCK: la tanga se nombra siempre, pero solo se EXPONE cuando va afuera.

Diagnóstico de la Ama (09/09/2026): *"creo que el definir la tanga para ele es
problema, hace que se vea siempre, pasa en esa foto de espalda."*

Medido antes de escribir una línea. El ancla se reforzó el 30/08 con una cola de
peso alto: `(thong back: a single thin strip, both seat cheeks fully bare:1.4)`.
Esa cola es **incondicional**, así que entra igual en los looks donde la tanga va
DEBAJO de una falda, un vestido o un pantalón. Resultado en el mismo prompt del
L831:

    "a sapphire vinyl g-string under the skirt"          <- BLOQUE B
    "the wrap skirt stays unbroken"                      <- ancla de costura
    "(… both seat cheeks fully bare:1.4)"                <- BOTTOM_CUT_LOCK

Tres instrucciones, la contradictoria con el peso más alto. La imagen resultante
abrió la falda en un recorte y dejó el glúteo entero al aire: el generador
obedeció el 1.4. Medido sobre la flota: **12 de 22 looks** del rango reforzado
llevan prenda exterior que cubre el asiento y la cola incondicional a la vez.

Lo que NO cambia (directiva de la Ama 13/08/2026, Look 801): el CORTE se sigue
nombrando con todas sus letras en los dos casos. Nunca un calzón de talle alto,
nunca cobertura total. Lo que se vuelve condicional es la EXPOSICIÓN, no el corte.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).parent))

import os as _os
# Una batería ejercita el motor con FIXTURES: su rastro no es historial del
# motor y no puede ensuciar `99_Sistema/logs/outfit_engine.jsonl`, que está
# trackeado (09/09/2026). Se apaga ANTES de importar el motor.
_os.environ.setdefault("OUTFIT_ENGINE_LOG", "0")


from prompt_builder import PromptBuilder  # noqa: E402

PB = PromptBuilder("ele")

# --- Fragmentos LITERALES de BLOQUE B de la flota (00_Ele/galeria_outfits.md) ---

L829_BIKINI = (
    "a plum thong whose narrow front meets a mirror-silver O-ring at each hip, "
    "the back reduced to a single fine cord"
)
L831_BAJO_FALDA = (
    "a sapphire vinyl wrap miniskirt riding high on the hip; a sapphire vinyl "
    "g-string under the skirt, cut narrow at the front and down to one cord behind"
)
L824_BAJO_PANTALON = (
    "acid chartreuse high-gloss vinyl wide-leg trousers; under the trousers an "
    "acid chartreuse vinyl g-string, narrowed to a panel at the front"
)
L823_PRONOMBRE = (
    "a deep oxblood high-gloss latex column dress with a narrow slit at the back "
    "hem; beneath it an oxblood latex thong, its front a slim tapered panel"
)
L814_ELIPTICA = (
    "an oil-slick multichrome liquid-lamé gown, the hem split to the hip on the "
    "left leg; a mirror-silver PVC thong beneath; bare legs, no stockings"
)
L813_INVERTIDA = (
    "an acid chartreuse liquid-latex blazer dress worn as the single garment, the "
    "waist cinched by a mirror-chrome buckled belt, worn over a black high-gloss PVC thong"
)
L812_EXTERIOR_TRANSPARENTE = (
    "a sheer PVC blush-pink overlay babydoll skirt falling to mid-thigh with an "
    "open-front drape revealing the hips; a matching blush rose latex micro-thong "
    "with a narrow vinyl waistband"
)
L815_EL_SHORT_ES_LA_TANGA = (
    "a bandeau cut to sit just under the bust, paired with high-waisted micro "
    "shorts cut as a thong at the back with a narrow tapered front panel"
)
L826_LENCERIA_SUELTA = (
    "moulded triangle cups and a chrome ring at the centre gore, and a matching "
    "deep teal vinyl thong with a slim tapered front panel and a single fine cord at the back"
)
# El defecto original que hizo nacer el ancla (Ama 13/08/2026).
L801_SIN_CORTE = "matching white wet-satin micro bikini bottoms"


# ---------------------------------------------------------------- se EXPONE ---

def test_bikini_sin_prenda_exterior_va_expuesto():
    assert PB.calzon_va_cubierto(L829_BIKINI) is False


def test_conjunto_de_lenceria_suelta_va_expuesto():
    assert PB.calzon_va_cubierto(L826_LENCERIA_SUELTA) is False


def test_el_short_que_ES_la_tanga_va_expuesto():
    # No hay prenda exterior: el short mismo está cortado en tanga atrás.
    assert PB.calzon_va_cubierto(L815_EL_SHORT_ES_LA_TANGA) is False


def test_prenda_exterior_transparente_sigue_expuesto():
    # Una falda `sheer` con drapeado abierto enseña la tanga a propósito.
    assert PB.calzon_va_cubierto(L812_EXTERIOR_TRANSPARENTE) is False


def test_el_caso_del_look_801_sigue_recibiendo_el_ancla_expuesta():
    # Regresión de la directiva original: calzón sin corte declarado y sin
    # prenda exterior -> variante expuesta, que es la que prohíbe el talle alto.
    assert PB.calzon_va_cubierto(L801_SIN_CORTE) is False


# --------------------------------------------------------------- va CUBIERTO ---

def test_calzon_bajo_falda_va_cubierto():
    assert PB.calzon_va_cubierto(L831_BAJO_FALDA) is True


def test_calzon_bajo_pantalon_va_cubierto():
    assert PB.calzon_va_cubierto(L824_BAJO_PANTALON) is True


def test_relacion_con_pronombre_va_cubierto():
    assert PB.calzon_va_cubierto(L823_PRONOMBRE) is True


def test_relacion_eliptica_va_cubierto():
    # "…a mirror-silver PVC thong beneath;" — la prenda no se repite.
    assert PB.calzon_va_cubierto(L814_ELIPTICA) is True


def test_relacion_invertida_va_cubierto():
    # "…blazer dress worn over a … thong" — la relación se escribe al revés.
    assert PB.calzon_va_cubierto(L813_INVERTIDA) is True


# ------------------------------------------------- qué dice cada variante ---

def test_el_texto_cubierto_no_pide_las_nalgas_al_aire():
    t = PB.texto_bottom_cut_lock(L831_BAJO_FALDA)
    assert "both seat cheeks fully bare" not in t
    assert "is left uncovered" not in t


def test_el_texto_cubierto_sigue_nombrando_el_corte():
    # La directiva del 13/08 sobrevive entera: el corte se nombra igual.
    t = PB.texto_bottom_cut_lock(L831_BAJO_FALDA)
    for exigido in ("thong or g-string", "never a full-seat brief", "never a high-waisted"):
        assert exigido in t, f"falta «{exigido}» en la variante cubierta"


def test_el_texto_cubierto_manda_mantener_cerrada_la_prenda_de_encima():
    t = PB.texto_bottom_cut_lock(L831_BAJO_FALDA)
    assert ":1.4)" in t, "la variante cubierta necesita su propia cola con peso"
    cola = t[t.rindex("("):]
    assert "not lifted" in cola and "not parted" in cola


def test_el_texto_expuesto_es_el_ancla_de_siempre():
    # Los looks de bikini no cambian ni un carácter.
    assert PB.texto_bottom_cut_lock(L829_BIKINI) == PB.anclas["BOTTOM_CUT_LOCK"]["texto"]


# ------------------------------------ el prompt ENSAMBLADO usa la variante ---

_POSE = "seen from behind, her shoulders square to the wall, looking back over one shoulder"
_SETTING = "a grey minimalist penthouse corner at dusk"


def _prompt(bloque_b):
    return PB.build(None, bloque_b, "back_view", _POSE, _SETTING)


def test_el_prompt_de_un_look_cubierto_no_pide_las_nalgas_al_aire():
    # Es el defecto que la Ama vio en la foto de espalda del L831.
    assert "both seat cheeks fully bare" not in _prompt(L831_BAJO_FALDA)


def test_el_prompt_de_un_look_cubierto_manda_cerrada_la_prenda_de_encima():
    assert "not lifted, not parted" in _prompt(L831_BAJO_FALDA)


def test_el_prompt_de_un_bikini_conserva_el_ancla_expuesta():
    assert "both seat cheeks fully bare" in _prompt(L829_BIKINI)


def test_el_prompt_cubierto_sigue_nombrando_el_corte():
    # La directiva del 13/08 tiene que sobrevivir al ensamblado, no solo al texto.
    assert "never a full-seat brief" in _prompt(L831_BAJO_FALDA)


# ------------------------------- el linter no se valida a si mismo (19/07/2026) ---

def test_la_variante_cubierta_no_valida_un_calzon_sin_corte():
    # BLOQUE B que nombra el calzon SIN declarar corte, debajo de una falda.
    # El aviso tiene que salir igual: si no se descuenta el texto del ancla, su
    # propio "thong or g-string" hace pasar al look. Mismo error que el barrido
    # de marcas del 19/07/2026, que leia el titulo del look.
    sucio = "a black vinyl wrap miniskirt; under the skirt matching black panties"
    assert PB.calzon_sin_corte(sucio) is True


def test_un_calzon_con_corte_declarado_bajo_falda_no_da_aviso():
    limpio = "a black vinyl wrap miniskirt; under the skirt a black vinyl thong, front narrow"
    assert PB.calzon_sin_corte(limpio) is False


def test_el_linter_no_se_autovalida_con_la_variante_cubierta():
    """El aviso tiene que salir sobre el PROMPT ENSAMBLADO, no solo sobre el BLOQUE B.

    `lint_prompts_personaje.py` valida el prompt completo de la galeria, y
    `calzon_sin_corte` descuenta el texto del ancla antes de medir justamente
    para no leerse a si misma. Al aparecer una SEGUNDA variante, descontar solo
    la primera deja pasar cualquier calzon sin corte que vaya bajo una falda:
    el "thong or g-string" de la propia variante cubierta lo valida.
    """
    sucio = "a black vinyl wrap miniskirt; under the skirt matching black panties"
    prompt = PB.build(None, sucio, "back_view", _POSE, _SETTING)
    assert "not lifted, not parted" in prompt, "el look de prueba tiene que salir CUBIERTO"
    assert PB.calzon_sin_corte(prompt) is True


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
    print(f"\n  RESULTADO: {ok} ok · {fallas} fallas")
    return 1 if fallas else 0


if __name__ == "__main__":
    raise SystemExit(_correr())
