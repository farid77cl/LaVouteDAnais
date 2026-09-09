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


# ======================================================================
# TAREA 4 · C por campos — pose, cámara, ambiente, y las anclas partidas
# ======================================================================
# C se arma desde tres dueños: el repertorio (postura), el slot (sus anclas,
# agrupadas por el campo que el contrato les asigna) y el setting (ambiente).
# Y dos campos son CONDICIONALES A B, decididos acá y no en B: `piernas`
# (cerradas si B declara vestido/falda/bata) y `exposicion_asiento` (asiento a
# la vista si el calzón va por fuera; prenda de encima cerrada si va debajo).

_SETTING = "a grey minimalist penthouse corner at dusk"
# Mobiliario REAL del setting: las sub-poses sentadas/reclinadas llevan {seat},
# {wall}, {surface}, {upright} y el motor se niega a resolverlas sin él —
# correctamente (Ama 08/06/2026: "cada pose debe ser armoniosa con el ambiente").
_PROPS = {"seat": "the long grey velvet banquette", "wall": "the floor-to-ceiling glass wall",
          "surface": "the low marble table", "upright": "the steel column"}


def _pb():
    return bloques.BloquesBuilder("ele")


def _c(slot, look):
    return bloques.campos_c(_pb(), slot, 8, _SETTING, look, props=_PROPS)


def test_c_lleva_la_subpose_del_repertorio_sin_anclas_dentro():
    c = _c("seated", {})
    assert c["postura"] and "single continuous photograph" not in c["postura"]


def test_c_agrupa_las_anclas_del_slot_por_su_campo():
    c = _c("seated", {})
    assert "supported entirely by the seat" in c["apoyo"]            # SEAT_ANCHOR
    assert "single continuous photograph" in c["un_solo_cuadro"]      # SINGLE_FRAME
    assert "five fingers" in c["anatomia_en_cuadro"]                   # ANATOMY_FULL


def test_c_no_lleva_anclas_de_B():
    """GARMENT_CONSISTENCY y FABRIC_PRISTINE viven en `_todos` del motor viejo
    y describen PRENDA: en el motor nuevo son B, y C no puede traerlas."""
    c = _c("standing", {})
    todo = " ".join(c.values())
    assert "exactly ONE garment ensemble" not in todo
    assert "pristine and unprinted" not in todo


def test_exposicion_del_asiento_es_condicional_a_B():
    cubierto = {"campos_b": {"prenda_principal": "a sapphire wrap miniskirt",
                             "calzon": "a sapphire g-string under the skirt"}}
    expuesto = {"campos_b": {"prenda_principal": "a plum thong bikini"}}
    assert "not lifted" in _c("back_view", cubierto)["exposicion_asiento"]
    assert "fully bare" in _c("back_view", expuesto)["exposicion_asiento"]


def test_piernas_cerradas_solo_si_B_declara_vestido_o_falda():
    con_falda = {"campos_b": {"prenda_principal": "a sapphire wrap miniskirt"}}
    bikini = {"campos_b": {"prenda_principal": "a plum thong bikini"}}
    assert "legs stay closed" in _c("seated", con_falda).get("piernas", "")
    assert "piernas" not in _c("seated", bikini)


def test_en_cuadro_referencia_y_no_redescribe():
    look = {"campos_b": {"prenda_principal": "x", "calzado": "15cm sapphire patent pumps"}}
    c = _c("standing", look)
    assert "as described above" in c["en_cuadro"]
    assert "sapphire" not in c["en_cuadro"]


def test_ambiente_es_el_setting_y_la_mirada_separa_slot5_de_pov():
    c5 = _c("slot5", {})
    cp = _c("pov", {})
    assert c5["ambiente"].startswith(_SETTING)
    assert "never at the lens" in c5["mirada"] and "directly into the lens" in cp["mirada"]


# ======================================================================
# TAREA 5 · ensamblar() + fugas() — tres oraciones y la guardia
# ======================================================================
# Orden fijo, siempre: A -> B -> C, y dentro de cada bloque el orden del
# contrato (que ya viene dado por campos_a/b/c). Tres oraciones, cada una
# cierra con punto. Sin pesos por defecto. Determinista byte a byte.

def test_ensamblar_produce_tres_oraciones_en_orden_A_B_C():
    p = bloques.ensamblar({"ojos": "grey-green eyes"}, {"calzado": "black pumps"},
                          {"postura": "seated", "ambiente": "a grey room"})
    assert p == "grey-green eyes. black pumps. seated, a grey room."


def test_ensamblar_salta_campos_vacios_y_no_deja_comas_dobles():
    p = bloques.ensamblar({"ojos": "grey-green eyes", "cejas": ""},
                          {"calzado": "black pumps,"}, {"postura": " seated "})
    assert p == "grey-green eyes. black pumps. seated."


def test_ensamblar_es_deterministico():
    args = ({"ojos": "x"}, {"calzado": "y"}, {"postura": "z"})
    assert bloques.ensamblar(*args) == bloques.ensamblar(*args)


def test_ensamblar_devuelve_tambien_el_texto_por_bloque():
    """Para medir el largo por bloque y para `fugas()`: el prompt final es
    UNA cadena, pero quien lo arma tiene que poder mirar cada tercio."""
    p, por_bloque = bloques.ensamblar({"ojos": "x"}, {"calzado": "y"}, {"postura": "z"},
                                      con_bloques=True)
    assert por_bloque == {"A": "x", "B": "y", "C": "z"} and p == "x. y. z."


def test_fugas_detecta_calzado_en_A_e_iris_en_C():
    f = bloques.fugas({"A": "grey eyes, black stiletto pumps", "B": "a bikini", "C": "blue iris"})
    assert any(x.startswith("A") and "pumps" in x for x in f), f
    assert any(x.startswith("C") and "iris" in x for x in f), f


def test_fugas_detecta_pose_en_B_y_prenda_en_C():
    f = bloques.fugas({"A": "grey eyes", "B": "a bikini, standing facing the camera",
                       "C": "seated on the banquette wearing a wrap skirt"})
    assert any(x.startswith("B") and "standing" in x for x in f), f
    assert any(x.startswith("C") and ("skirt" in x or "wearing" in x) for x in f), f


def test_un_prompt_limpio_no_tiene_fugas():
    assert bloques.fugas({"A": "grey-green eyes, dark cherry red hair",
                          "B": "black patent pumps, a plum latex bikini",
                          "C": "seated on the grey banquette, a penthouse at dusk"}) == []


def test_fugas_deja_pasar_las_referencias_de_C_a_B():
    """C puede REFERIRSE a B («the footwear exactly as described above») sin
    re-describirlo. Una referencia no es una fuga; una descripción sí."""
    assert bloques.fugas({"A": "x", "B": "y",
                          "C": "the footwear clearly visible and exactly as described above"}) == []


# ======================================================================
# TAREA 6 · BloquesBuilder.build() — la misma firma, el ensamblado nuevo
# ======================================================================
# `build(bloque_a, bloque_b, slot, pose_text, setting, ...)` conserva la firma
# que `generar` usa. `bloque_b` acepta el LOOK entero (dict, batches nuevos) o
# el párrafo (str, batches viejos); `pose_text=None` = sacar la sub-pose del
# repertorio; `bloque_a=None` = leer la cerca del perfil (dueño único).

_LOOK = {"campos_b": {"prenda_principal": "a plum high-gloss latex thong bikini, moulded "
                                          "triangle cups joined by a mirror-silver O-ring",
                      "calzado": "15cm plum patent platform stiletto sandals, open toe, "
                                 "a 4-inch platform and a razor pin heel"},
         "props": _PROPS}
_SLOTS = ("standing", "back_view", "seated", "side_profile", "slot5", "pov", "odalisque")


def test_build_del_builder_nuevo_pasa_validar_y_no_tiene_fugas():
    pb = bloques.BloquesBuilder("ele")
    p = pb.build(None, _LOOK, "standing", None, _SETTING)
    assert PromptBuilder.validar(p) == [], PromptBuilder.validar(p)
    assert bloques.fugas(pb.ultimo_por_bloque) == [], bloques.fugas(pb.ultimo_por_bloque)


def test_build_reporta_el_largo_por_bloque():
    pb = bloques.BloquesBuilder("ele")
    pb.build(None, _LOOK, "standing", None, _SETTING)
    r = pb.ultimo_reporte
    assert set(r) == {"A", "B", "C"}
    assert all(r[k]["chars"] > 0 and r[k]["palabras"] > 0 for k in r), r


def test_build_es_identico_en_las_7_poses_en_A_y_B():
    pb = bloques.BloquesBuilder("ele")
    partes = []
    for s in _SLOTS:
        pb.build(None, _LOOK, s, None, _SETTING)
        partes.append(dict(pb.ultimo_por_bloque))
    assert len({p["A"] for p in partes}) == 1, "A cambia entre poses"
    assert len({p["B"] for p in partes}) == 1, "B cambia entre poses"
    assert len({p["C"] for p in partes}) == 7, "C tiene que cambiar en cada pose"


def test_build_acepta_un_bloque_b_de_parrafo_como_los_batches_viejos():
    pb = bloques.BloquesBuilder("ele")
    p = pb.build(None, "a plum latex thong bikini; 15cm plum patent platform stiletto sandals",
                 "standing", None, _SETTING)
    assert "plum latex thong bikini" in pb.ultimo_por_bloque["B"]
    assert PromptBuilder.validar(p) == []


def test_build_pone_las_anclas_de_prenda_en_B_y_no_en_C():
    """GARMENT_CONSISTENCY y FABRIC_PRISTINE describen prenda: van en B."""
    pb = bloques.BloquesBuilder("ele")
    pb.build(None, _LOOK, "standing", None, _SETTING)
    assert "exactly ONE garment ensemble" in pb.ultimo_por_bloque["B"]
    assert "exactly ONE garment ensemble" not in pb.ultimo_por_bloque["C"]
    assert "pristine and unprinted" in pb.ultimo_por_bloque["B"]


def test_build_pone_el_fotorrealismo_en_A():
    pb = bloques.BloquesBuilder("ele")
    pb.build(None, _LOOK, "standing", None, _SETTING)
    assert "real photograph" in pb.ultimo_por_bloque["A"]


def test_build_es_deterministico():
    pb = bloques.BloquesBuilder("ele")
    a = pb.build(None, _LOOK, "seated", None, _SETTING)
    b = pb.build(None, _LOOK, "seated", None, _SETTING)
    assert a == b


def test_build_no_se_contradice_cuando_el_calzon_va_bajo_falda():
    """Medido sobre el L831 real: el motor nuevo partia BOTTOM_CUT_LOCK en el
    ultimo parentesis, pero la PROSA del corte ya decia «the seat is left
    uncovered» — corte y exposicion venian mezclados en la frase, no solo en
    la cola. B decia asiento al aire y C decia falda cerrada: la pelea que
    este motor existe para eliminar, fabricada por el propio motor."""
    import contradicciones
    pb = bloques.BloquesBuilder("ele")
    look = {"campos_b": {"prenda_principal": "a sapphire vinyl wrap miniskirt riding high on the hip",
                         "calzon": "a sapphire vinyl g-string under the skirt",
                         "calzado": "15cm sapphire patent pumps"}, "props": _PROPS}
    p = pb.build(None, look, "back_view", None, _SETTING)
    assert contradicciones.buscar(p) == [], contradicciones.buscar(p)
    assert "left uncovered" not in pb.ultimo_por_bloque["B"]
    assert "not lifted" in pb.ultimo_por_bloque["C"]


def test_el_verbo_de_ajuste_de_una_prenda_no_es_pose():
    """«the band sitting on the natural waist» (L831 real) es AJUSTE, no pose.
    En este corpus la pose dice «seated» o «sitting down/upright»."""
    assert bloques.fugas({"A": "x", "B": "a wrap skirt, the band sitting on the natural waist, "
                                        "a thin waistband sitting high on the hip bones", "C": "y"}) == []


def test_un_ancla_de_prenda_que_nombra_el_cuadro_no_es_pose():
    """GARMENT_EXCLUSION_LOCK dice «not present anywhere in the frame»: es B y
    «the frame» solo no es señal de pose ni de cámara."""
    assert bloques.fugas({"A": "x", "B": "every item named as NOT worn is genuinely absent, "
                                        "not present anywhere in the frame", "C": "y"}) == []


def test_sitting_down_sigue_siendo_pose():
    assert any("sitting down" in f for f in
               bloques.fugas({"A": "x", "B": "a bikini, genuinely sitting down on the bench", "C": "y"}))


def test_un_accesorio_que_reposa_sobre_el_cuerpo_no_es_pose():
    """«a fine mirror-silver chain lying across the ribcage» (L829 real) es
    COLOCACIÓN de una joya, no la modelo acostada. La pose dice «lying down»."""
    assert bloques.fugas({"A": "x", "B": "a fine mirror-silver chain lying across the ribcage", "C": "y"}) == []


def test_lying_down_sigue_siendo_pose():
    assert any("lying down" in f for f in
               bloques.fugas({"A": "x", "B": "a bikini, lying down on the chaise", "C": "y"}))


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
