#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El prompt que se pelea consigo mismo.

De los ~85 hallazgos de la auditoría visual del 09/09/2026 (70 poses, tres
muñecas, seis auditores externos ciegos), **5 fueron del motor** — y los cinco
son el mismo animal: **dos cláusulas del mismo prompt pidiendo cosas
incompatibles**. Ninguno los cazaba nadie, porque cada chequeo del repo mira una
cláusula a la vez y todas estaban individualmente bien escritas.

Los fixtures de abajo NO son inventados: son fragmentos literales de prompts
ensamblados de la flota, con su look de origen anotado.

⚠️ Este es el único clasificador del repo que lee el PROMPT ENSAMBLADO y no el
BLOQUE B. Es deliberado y no contradice la regla del 19/07/2026: aquella prohíbe
*clasificar* sobre el prompt (el ancla nombra «bodysuit, teddy, leotard» y el
clasificador se leería a sí mismo). Acá no se clasifica nada — se **comparan**
dos cláusulas del mismo texto, que es justamente lo que ningún chequeo por
cláusula puede hacer.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).parent))

import contradicciones  # noqa: E402

# --------------------------------------------------------------- fixtures ---
# Todos salen de prompts REALES. Cada uno anota su look de origen.

# C1 · AN L87 «Gasa de Marfil» — el ADN clava el calzado en negro charol y el
# BLOQUE B lo declara marfil. La imagen del `pov` del L88, mismo defecto, salió
# con zapato NEGRO en un look rosa polvo íntegro.
C1_CALZADO = (
    "…wearing 12cm black patent leather stiletto heels no platform iconic red sole, "
    "cinematic chiaroscuro dramatic lighting. a floor-length sheer ivory silk-gauze "
    "dress worn as the outer layer; 12cm D'Orsay stiletto pump with open sides, in "
    "ivory patent leather, closed pointed toe, a red lacquered sole."
)

# C2 · ELE L831 — la cola incondicional de BOTTOM_CUT_LOCK exigía el asiento al
# aire mientras el BLOQUE B ponía la tanga BAJO la falda y otra ancla pedía la
# falda cerrada. La imagen abrió la falda. Arreglado el 09/09; esto es la guardia
# de regresión.
C2_EXPOSICION = (
    "a sapphire vinyl wrap miniskirt riding high on the hip; a sapphire vinyl g-string "
    "under the skirt; the wrap skirt stays unbroken, "
    "(thong back: a single thin strip, both seat cheeks fully bare:1.4)"
)

# C3 · MD L89 — la odalisque pedía gris cuando las otras seis poses pedían
# cobalto. Sobrevivió cinco días a la corrección del 04/09 escondida en el
# repertorio de sub-poses. Arreglado el 09/09; guardia de regresión.
C3_IRIS = (
    "(saturated cobalt blue iris, vivid and pigmented, never grey and never pale:1.4), "
    "medium almond eyes… her chin lifted and her cold pale steel grey eyes locked "
    "directly onto the camera with an arrogant dominant smirk"
)

# C4 · AN L91 «Encaje Esmeralda» — el look que ESTRENA el veto de corsetería del
# 08/09, con el corsé escrito en su propio ADN. La imagen devolvió aro rígido en
# `seated` y copa moldeada en `side_profile`.
C4_COPA = (
    "slender mature elegant hourglass figure with extreme waist training tightlacing "
    "corset, S-curve posture… an emerald Leavers lace body, its cups SOFT and "
    "unstructured with no boning and no moulding anywhere"
)

# C5 · AN L87 — uñas largas de estilete en el ADN contra almendra corta en el
# BLOQUE B. El auditor las vio LARGAS en las dos poses donde se ven.
C5_UNAS = (
    "long stiletto-shaped impeccably manicured glossy fingernails, cinematic "
    "chiaroscuro… fingernails: almond-shaped, filed short of the fingertip and "
    "lacquered in pale antique gold"
)

# Negativos: prompts coherentes de verdad. Un linter que grita lo inarreglable
# enseña a ignorarlo — la meta es 0 falsos positivos sobre flota sana.
LIMPIO_BIKINI = (
    "a plum thong whose narrow front meets a mirror-silver O-ring at each hip, the back "
    "reduced to a single fine cord; open-toe platform stiletto sandals in plum patent "
    "vinyl, 15cm heel plus a 4-inch platform, (thong back: a single thin strip, both "
    "seat cheeks fully bare:1.4)"
)
LIMPIO_BAJO_FALDA = (
    "a sapphire vinyl wrap miniskirt; a sapphire vinyl g-string under the skirt; the wrap "
    "skirt stays unbroken, (the outer garment over her hips and seat stays closed and "
    "unbroken, not lifted, not parted:1.4)"
)


def _hay(hallazgos, *palabras):
    return any(all(p.lower() in h.lower() for p in palabras) for h in hallazgos)


# ------------------------------------------------------------ los 5 casos ---

def test_c1_calzado_nombrado_con_dos_colores():
    h = contradicciones.buscar(C1_CALZADO)
    assert _hay(h, "calzado"), h
    assert _hay(h, "black", "ivory"), h


def test_c2_exposicion_contra_prenda_que_cubre():
    h = contradicciones.buscar(C2_EXPOSICION)
    assert _hay(h, "expone"), h


def test_c3_iris_nombrado_con_dos_colores():
    h = contradicciones.buscar(C3_IRIS)
    assert _hay(h, "iris"), h
    assert _hay(h, "cobalt", "grey"), h


def test_c4_corse_contra_copa_blanda():
    h = contradicciones.buscar(C4_COPA)
    assert _hay(h, "copa"), h


def test_c5_unas_largas_contra_cortas():
    h = contradicciones.buscar(C5_UNAS)
    assert _hay(h, "uñas"), h


# ------------------------------------------------- que no grite de más ---

def test_un_bikini_coherente_no_da_hallazgos():
    assert contradicciones.buscar(LIMPIO_BIKINI) == []


def test_una_tanga_bajo_falda_con_la_variante_correcta_no_da_hallazgos():
    assert contradicciones.buscar(LIMPIO_BAJO_FALDA) == []


def test_un_prompt_vacio_no_revienta():
    assert contradicciones.buscar("") == []
    assert contradicciones.buscar(None) == []


def test_cada_hallazgo_nombra_LAS_DOS_clausulas():
    """Un hallazgo que dice 'hay un problema' sin decir cuál no sirve.

    El costo real del 09/09 no fue detectar, fue LOCALIZAR: seis agentes leyendo
    prompts de 8.500 chars. Un hallazgo tiene que traer el texto de las dos
    cláusulas que se pelean, o no ahorra nada.
    """
    for fixture in (C1_CALZADO, C3_IRIS, C4_COPA, C5_UNAS):
        for h in contradicciones.buscar(fixture):
            assert "«" in h and h.count("«") >= 2, f"hallazgo sin las dos citas: {h}"


# --------------------------------------- falsos positivos medidos en la flota ---
# El primer barrido dio 968 hallazgos sobre 5.706 prompts (16%). Un linter que
# grita lo inarreglable enseña a ignorarlo — la lección ya pagada con
# `auditar_canon_flota`, que va en 872 avisos sobre 685 looks y nadie lee.
# Estos tres son los defectos REALES del detector, con su look de origen.

# ELE L211 — «booth» del setting matcheaba `boots?` por falta de \b.
FP_BOOTH = (
    "neon magenta patent stiletto pumps with 14cm chrome needle pin heel, "
    "medium full shot framed knee-up to head, a VIP booth purple blur background"
)

# ELE L246 — las DOS cláusulas son texto del propio ancla: DRESS_LEG_CLOSURE
# habla de la caída de la falda sobre el regazo, no de cubrir el asiento.
FP_HEM_SOBRE_EL_REGAZO = (
    "at the back a single slim strip following the centre line so the curve of the "
    "hips and the seat is left uncovered, with the hem falling closed over the lap "
    "so the line of the skirt stays unbroken"
)

# ELE L461 — `XXXL` es el PELO, y «high-cut shorts» contiene «cut short».
FP_PELO_Y_SHORTS = (
    "dark cherry red hair, artificial XXXL extensions hip-length, voluminous waves; "
    "the high-cut shorts riding up on the hip"
)


def test_booth_del_setting_no_es_un_zapato():
    assert contradicciones.buscar(FP_BOOTH) == [], contradicciones.buscar(FP_BOOTH)


def test_la_falda_sobre_el_regazo_no_es_cubrir_el_asiento():
    h = contradicciones.buscar(FP_HEM_SOBRE_EL_REGAZO)
    assert h == [], h


def test_el_pelo_XXXL_y_los_high_cut_shorts_no_son_unas():
    h = contradicciones.buscar(FP_PELO_Y_SHORTS)
    assert h == [], h


# Segunda ronda de calibración: el barrido bajó de 968 a 194, pero C1 seguía
# contando el MISMO zapato dos veces. FOOTWEAR_ECHO lo repite al cierre a
# propósito, y ese eco casi nunca trae color propio — así que la ventana de
# contexto le prestaba el color del vecino.

# ELE L304 — el eco nombra el mismo zapato flamingo sin repetir el color.
FP_ECO_MISMO_ZAPATO = (
    "flamingo pink vinyl lace-up stiletto sandals with 12cm gold needle heel and "
    "ankle lace-up straps and open-toe, standing tall in contrapposto with weight "
    "on one flamingo stiletto sandal and the other leg extended"
)

# ELE L704 — «rising above the boots» habla de las MEDIAS, no de un segundo par.
FP_MEDIAS_SOBRE_LA_BOTA = (
    "sheer imperial-red thigh-high stockings with a black back-seam rising above "
    "the boots, a 14cm thin pin stiletto heel"
)

# AN L76 — el eco cita el tacón sin color; el color lo puso el vecino.
FP_ECO_SIN_COLOR = (
    "wearing 12cm black patent leather stiletto heels no platform iconic red sole, "
    "her weight settled over a 12cm razor-thin stiletto heel with no platform"
)


def test_el_eco_del_mismo_zapato_no_es_una_contradiccion():
    h = contradicciones.buscar(FP_ECO_MISMO_ZAPATO)
    assert h == [], h


def test_las_medias_que_suben_sobre_la_bota_no_son_un_segundo_zapato():
    h = contradicciones.buscar(FP_MEDIAS_SOBRE_LA_BOTA)
    assert h == [], h


def test_un_eco_sin_color_propio_no_hereda_el_del_vecino():
    h = contradicciones.buscar(FP_ECO_SIN_COLOR)
    assert h == [], h


# AN L62 — este SÍ es real y no se puede perder al apretar: el ADN clava negro
# charol y el BLOQUE B declara una bota azul medianoche. Es la razón de C1.
# Fiel al prompt real: el ADN cierra en «intimate tension.» y el BLOQUE B arranca
# SIN ningún «;» antes de la bota — la frontera entre los dos es de oración.
REAL_DOS_ZAPATOS = (
    "wearing 12cm black patent leather stiletto heels no platform iconic red sole, "
    "cinematic chiaroscuro dramatic lighting, intimate tension. an overbust corset in "
    "midnight-blue silk charmeuse; (12cm midnight-blue suede knee-high stiletto boot "
    "ending exactly at the knee, iconic red sole)"
)


def test_apretar_C1_no_puede_perder_el_caso_real():
    h = contradicciones.buscar(REAL_DOS_ZAPATOS)
    assert any("calzado" in x for x in h), h


# Tercera ronda, sobre el barrido con el parser real de la galería (814 looks).

# MD L62 — UN solo zapato dentro de un paréntesis; «slingback strap» es una
# característica del pump, no un segundo par. El BLOQUE B separa PRENDAS con
# «;» — dos menciones de calzado dentro del mismo segmento son la misma prenda.
FP_SLINGBACK_DEL_MISMO_PUMP = (
    "a small dusty-rose satin bow pinned at the center busk as the signature pink "
    "accent; (13cm ivory champagne patent platform pump, closed pointed toe, secured "
    "slingback strap, razor-thin metal needle heel, gold heel cap:1.3); long faceted "
    "pearl drops at the ears"
)

# MD L86 — «eyes in midnight sapphire shimmer smoke» es SOMBRA DE OJOS, no iris.
# El detector de iris tiene que distinguir el ojo del maquillaje que lo rodea.
# Fiel al prompt real: la cláusula «eyes in …» va aislada por comas, lejos del
# iris. (La primera versión de este fixture la pegaba al cobalto y el radio de la
# cláusula los fundía — "pasaba" sin probar nada. Un test que pasa solo no prueba.)
FP_SOMBRA_NO_ES_IRIS = (
    "(huge oversized round almond-shaped cold vivid blue eyes, (richly pigmented deep "
    "cobalt blue iris:1.4), thick lashes, a pale matte face; rose-gold bands at both "
    "wrists, long faceted pearl drops at the ears; eyes in midnight sapphire shimmer "
    "smoke, mouth in high-gloss cherry"
)


def test_el_slingback_del_mismo_pump_no_es_un_segundo_zapato():
    h = contradicciones.buscar(FP_SLINGBACK_DEL_MISMO_PUMP)
    assert h == [], h


def test_la_sombra_de_ojos_no_es_el_iris():
    h = contradicciones.buscar(FP_SOMBRA_NO_ES_IRIS)
    assert h == [], h


def test_el_barrido_de_flota_no_puede_pasar_del_1_por_ciento():
    """Guardia de ruido, con número.

    Se mide sobre los fixtures sanos que tenemos acá: si alguno de ellos
    empieza a dar hallazgo, el detector se volvió gritón otra vez.
    """
    sanos = [LIMPIO_BIKINI, LIMPIO_BAJO_FALDA, FP_BOOTH,
             FP_HEM_SOBRE_EL_REGAZO, FP_PELO_Y_SHORTS]
    ruido = [h for s in sanos for h in contradicciones.buscar(s)]
    assert ruido == [], ruido


# ------------------------------------------------------ la PUERTA (Tarea 2) ---
# `outfit.py generar` bloquea sobre lo que devuelve `PromptBuilder.validar()`
# (outfit.py:321-324). Es la única puerta: si el detector no está ahí, un prompt
# contradictorio llega igual a la galería y se documenta en vez de prevenirse.

# Lo mínimo que `validar()` deja pasar hoy: >400 chars, con SINGLE_FRAME, sin
# placeholders ni metalenguaje multi-toma. Relleno neutro a propósito.
_PROMPT_MINIMO_VALIDO = (
    "a single continuous photograph of a glamorous woman in a grey minimalist penthouse, "
    "soft window light, editorial framing, her posture composed and still, the room "
    "quiet and wide, " * 4
)


def test_validar_bloquea_un_prompt_contradictorio():
    from prompt_builder import PromptBuilder
    fallas = PromptBuilder.validar(_PROMPT_MINIMO_VALIDO + C3_IRIS)
    assert any("iris" in f for f in fallas), fallas


def test_validar_sigue_dejando_pasar_un_prompt_coherente():
    from prompt_builder import PromptBuilder
    assert PromptBuilder.validar(_PROMPT_MINIMO_VALIDO + LIMPIO_BIKINI) == []


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
                traceback.print_exc()
    print(f"\n  RESULTADO: {ok} ok · {fallas} fallas")
    return 1 if fallas else 0


if __name__ == "__main__":
    raise SystemExit(_correr())
