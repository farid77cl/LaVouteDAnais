#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_medir_capitulo.py — pruebas de Loreto (07/09/2026)

Nace de la orden de la Ama del 07/09/2026: *"me refería a la prosa extraña, por qué escribe de
manera que un humano no lo haría, se está notando demasiado que es escrito por IA"*.

Loreto medía temperatura, repetición y voz — nunca **firma de máquina**. Las medidas M13-M17 se
escriben con test primero porque el medidor es el único control que corre SIEMPRE (Fase 2.5), y
un chequeo que no se probó pasa en verde sobre hallazgos reales (ya pasó dos veces este mes con
el byte 0x08 en `outfit.py`).

Correr:  python 99_Sistema/scripts/literatura/test_medir_capitulo.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).parent))

import medir_capitulo as M  # noqa: E402

FALLAS: list[str] = []


def check(nombre: str, cond: bool, detalle: str = "") -> None:
    if cond:
        print(f"  ✅ {nombre}")
    else:
        print(f"  ❌ {nombre}" + (f"  — {detalle}" if detalle else ""))
        FALLAS.append(nombre)


def _sents(texto: str) -> list[dict]:
    """Construye la lista de frases igual que medir(), para no duplicar el parser."""
    out, escena = [], 1
    for ln, p in M.parrafos_con_linea(texto):
        if p == "***":
            escena += 1
            continue
        for s in M.oraciones(p):
            ws = M.palabras(s)
            if ws:
                out.append({"text": s, "words": ws, "linea": ln, "escena": escena,
                            "hot": False, "dial": M.es_dialogo(s)})
    return out


# ────────────────────────────────────────────────────────────────────────────
# M13 · Ritmo de cláusula — la unidad de respiración, no la oración
# ────────────────────────────────────────────────────────────────────────────

def test_m13_mide_la_clausula_y_no_la_oracion():
    # Una sola oración de 12 palabras partida en tres cláusulas de 4.
    t = "Se dobló sobre el acero, le habló muy al oído, y él tragó saliva feo.\n"
    r = M.m13_ritmo_clausula(_sents(t), [])
    check("M13 parte la oración en cláusulas, no la cuenta entera",
          r["n"] == 3 and r["mediana"] <= 6, f"n={r.get('n')} mediana={r.get('mediana')}")


def test_m13_ignora_el_dialogo():
    t = ("La barra estaba fría, muy fría, y ella lo sabía.\n\n"
         "—Mire, mi rey, cómo se le fue el aire, cómo tiembla.\n")
    r = M.m13_ritmo_clausula(_sents(t), [])
    check("M13 no mide las cláusulas del diálogo", r["n"] == 3, f"n={r.get('n')}")


def _texto_con_ritmo(patron: list[int], oraciones: int, vocab: list[str]) -> str:
    """Texto donde cada oración lleva cláusulas de los largos de `patron`.

    El vocabulario cambia entre a y b para que lo ÚNICO compartido sea el ritmo:
    si M13 midiera palabras en vez de respiración, estos dos textos no se parecerían.
    """
    pars, k = [], 0
    for i in range(oraciones):
        cls = []
        for largo in patron:
            ws = [vocab[(k + j) % len(vocab)] for j in range(largo)]
            k += largo
            cls.append(" ".join(ws))
        pars.append(", ".join(cls) + ".")
    return "\n\n".join(pars)


VOC_A = "taza barra acero billete liga vidrio banco vapor cortina espejo".split()
VOC_B = "puerta mesa madera moneda cinta ventana silla humo alfombra marco".split()


def test_m13_marca_clon_ritmico_contra_capitulo_previo():
    # Mismo patrón de respiración (3-5-4-7), palabras completamente distintas.
    a = _texto_con_ritmo([3, 5, 4, 7], 100, VOC_A)
    b = _texto_con_ritmo([3, 5, 4, 7], 100, VOC_B)
    r = M.m13_ritmo_clausula(_sents(a), [_sents(b)])
    check("M13 marca clon rítmico cuando la respiración es la misma",
          r["clon_ritmico"] is True and r["jsd_min"] < M.RITMO_JSD_CLON,
          f"jsd_min={r.get('jsd_min')} n={r.get('n')}")


def test_m13_no_marca_clon_cuando_el_ritmo_cambia():
    a = _texto_con_ritmo([2, 2, 3], 120, VOC_A)
    b = _texto_con_ritmo([14, 9, 18], 120, VOC_B)
    r = M.m13_ritmo_clausula(_sents(a), [_sents(b)])
    check("M13 no marca clon cuando el ritmo es distinto",
          r["clon_ritmico"] is False, f"jsd_min={r.get('jsd_min')}")


def test_m13_no_opina_con_muestra_chica():
    a = _texto_con_ritmo([3, 5, 4, 7], 3, VOC_A)
    b = _texto_con_ritmo([3, 5, 4, 7], 3, VOC_B)
    r = M.m13_ritmo_clausula(_sents(a), [_sents(b)])
    check("M13 no declara clon rítmico si la muestra no alcanza",
          r["clon_ritmico"] is False and r["medible"] is False, str(r)[:160])


# ────────────────────────────────────────────────────────────────────────────
# M14 · Dos puntos revelatorios
# ────────────────────────────────────────────────────────────────────────────

def test_m14_cuenta_los_dos_puntos_revelatorios():
    t = ("Y no caminó derecho: dio el rodeo largo por detrás del banco.\n\n"
         "El cuerpo contestó primero: el coño se le cerró de un golpe.\n")
    r = M.m14_dos_puntos(_sents(t))
    check("M14 cuenta el enunciado neutro + dos puntos + revelación", len(r) == 2, f"n={len(r)}")


def test_m14_no_cuenta_la_enumeracion():
    # El inventario de salvaguardas («Uno: no siento.») es un motivo permanente del
    # canon, no un tell. Medido en Modo Trofeo Cap1: 11 de los 32 que M14 contaba.
    t = ("Uno: no siento. Lo que le pase a este cuerpo se queda en este cuerpo.\n\n"
         "Dos: hay pared. Tres: sé quién soy.\n")
    r = M.m14_dos_puntos(_sents(t))
    check("M14 no cuenta los dos puntos de enumeración", len(r) == 0, f"n={len(r)} {r}")


def test_m14_no_cuenta_el_dos_puntos_que_abre_dialogo():
    # Párrafo que termina en «:» y abajo viene un parlamento. Es puntuación de
    # diálogo, no el golpe de revelación.
    t = ("Y después, al cuerpo, con el mismo tono con que se le habla a un ascensor:\n\n"
         "—Bambi. TROFEO.\n")
    pars = M.parrafos_con_linea(t)
    r = M.m14_dos_puntos(_sents(t), pars)
    check("M14 no cuenta el dos puntos que abre un parlamento", len(r) == 0, f"n={len(r)} {r}")


def test_m14_sigue_cazando_el_revelatorio_con_izquierda_corta():
    # El filtro de enumeración no puede tragarse un revelatorio de verdad.
    t = "El problema: no puedo cerrar los ojos ni un segundo.\n"
    r = M.m14_dos_puntos(_sents(t))
    check("M14 no se traga un revelatorio de izquierda corta", len(r) == 1, f"n={len(r)}")


def test_m14_no_cuenta_la_hora_ni_el_dialogo():
    t = ("A las 10:20 llegó el primero de la mañana.\n\n"
         "—Mire, mi rey: se le nota en la cara lo que está pensando.\n")
    r = M.m14_dos_puntos(_sents(t))
    check("M14 ignora la hora y el diálogo", len(r) == 0, f"n={len(r)} {r}")


# ────────────────────────────────────────────────────────────────────────────
# M15 · Símil-molde «como si / como quien»
# ────────────────────────────────────────────────────────────────────────────

def test_m15_cuenta_el_simil_molde():
    t = ("Le abrió las rodillas como quien abre una carpeta.\n\n"
         "Se quedó quieta como si le hubieran sacado el aire de golpe.\n\n"
         "Lo miró como el que ya sabe la respuesta entera.\n")
    r = M.m15_simil_molde(_sents(t))
    check("M15 cuenta «como quien», «como si» y «como el que»", len(r) == 3, f"n={len(r)}")


def test_m15_no_cuenta_la_comparacion_directa():
    t = "El acero estaba frío como el mármol de la entrada.\n"
    r = M.m15_simil_molde(_sents(t))
    check("M15 no marca el símil directo sin molde", len(r) == 0, f"n={len(r)} {r}")


# ────────────────────────────────────────────────────────────────────────────
# M16 · El recibo de excitación (cierre de párrafo que certifica la calentura)
# ────────────────────────────────────────────────────────────────────────────

def test_m16_detecta_el_recibo_al_cierre_del_parrafo():
    t = ("Él dejó el billete sobre el acero y no la miró, y eso también la mojó.\n\n"
         "Le salió un número chico, y el número chico la mojó más que la verga.\n")
    r = M.m16_recibo_excitacion(M.parrafos_con_linea(t))
    check("M16 detecta el comprobante de calentura al final del párrafo", len(r) == 2, f"n={len(r)}")


def test_m16_no_marca_la_excitacion_dentro_de_la_escena():
    t = ("Se le mojó la tanga mientras él contaba los billetes, y ella siguió doblada sobre el "
         "acero sin moverse ni un centímetro hasta que el viejo terminó de contar.\n")
    r = M.m16_recibo_excitacion(M.parrafos_con_linea(t))
    check("M16 no marca la calentura ejecutada dentro del párrafo", len(r) == 0, f"n={len(r)} {r}")


# ────────────────────────────────────────────────────────────────────────────
# M17 · Diálogo sin disfluencia — nadie habla mal
# ────────────────────────────────────────────────────────────────────────────

def test_m17_marca_el_dialogo_demasiado_limpio():
    t = "\n\n".join([
        "—Buenos días, don Manuel, siéntese donde quiera.",
        "—Gracias, mija, hoy hace frío afuera.",
        "—Le sirvo el de siempre entonces.",
        "—Ya, el de siempre está bien.",
    ])
    r = M.m17_disfluencia(M.parrafos_con_linea(t))
    check("M17 marca el diálogo sin una sola marca de habla real",
          r["parlamentos"] == 4 and r["con_disfluencia"] == 0 and r["marca"] is True,
          str(r))


def test_m17_no_marca_cuando_hay_muletilla_o_interrupcion():
    t = "\n\n".join([
        "—Oye, po, no sé, es que yo pensaba que—",
        "—Que nada. Cachai que no es así.",
        "—Ya, ya, perdón, o sea, tenís razón.",
        "—Este… mejor no digái nada más.",
    ])
    r = M.m17_disfluencia(M.parrafos_con_linea(t))
    check("M17 no marca cuando el diálogo tiene muletillas e interrupciones",
          r["con_disfluencia"] >= 3 and r["marca"] is False, str(r))


# ────────────────────────────────────────────────────────────────────────────
# Integración: medir() expone la firma de IA y la reporta
# ────────────────────────────────────────────────────────────────────────────

def test_medir_expone_la_firma_de_ia(tmp: Path):
    cap = tmp / "cap_prueba.md"
    cap.write_text("\n\n".join([
        "Y no caminó derecho: dio el rodeo largo, muy largo, por detrás del banco.",
        "Le abrió las rodillas como quien abre una carpeta, sin apuro, sin mirarlo.",
        "Él dejó el billete sobre el acero y no dijo nada, y eso también la mojó.",
        "—Ya. Sal a vender café.",
    ]), encoding="utf-8")
    r = M.medir(cap, [], 120, 300)
    firma = r.get("m13_m17", {})
    check("medir() devuelve el bloque m13_m17",
          bool(firma) and "dos_puntos" in firma and "simil" in firma
          and "recibo" in firma and "ritmo" in firma and "dialogo" in firma, str(firma)[:200])
    check("medir() reporta la firma de IA en los avisos",
          any("M14" in b or "M15" in b or "M16" in b for b in r["blandos"]),
          str(r["blandos"]))


def test_render_muestra_la_firma_de_ia(tmp: Path):
    cap = tmp / "cap_render.md"
    cap.write_text("\n\n".join([
        "Y no caminó derecho: dio el rodeo largo, muy largo, por detrás del banco.",
        "Le abrió las rodillas como quien abre una carpeta, sin apuro, sin mirarlo.",
        "Él dejó el billete sobre el acero y no dijo nada, y eso también la mojó.",
    ]), encoding="utf-8")
    md = M.render(M.medir(cap, [], 120, 300))
    check("render() imprime la sección de firma de IA",
          "FIRMA DE IA" in md and "cláusula" in md.lower(), md[-400:])


# ────────────────────────────────────────────────────────────────────────────
# T0 · Piso duro de temperatura (Ama 08/09/2026, desde la Mesa de La Voûte)
#
# Su decisión, literal: *"Sí, ponle piso — que frene bajo cierto porcentaje de
# cuerpo en apertura y en el global. No mide si calienta, pero corta lo que va
# por debajo del suelo."*
#
# Los umbrales NO son de criterio: salen de medir los 140 capítulos ≥1500
# palabras del repo (08/09/2026). Ver `medir_capitulo.PISO_*` para la
# calibración y para lo que el piso deliberadamente NO promete.
# ────────────────────────────────────────────────────────────────────────────

def test_piso_frena_el_capitulo_sin_cuerpo():
    # 5,0% global: por debajo de TODO lo que la Ama aprobó (su mínimo publicado es 9,0).
    duros = M.t0_piso_temperatura(global_share=5.0, apertura=30.0)
    check("T0 piso global: 5,0% de narración con cuerpo es duro",
          any("T0" in d and "global" in d for d in duros), str(duros))
    # Y el mínimo publicado NO cae: el piso pasa por debajo, no por encima.
    check("T0 piso global: 9,0% (mínimo publicado) no es duro",
          not M.t0_piso_temperatura(global_share=9.0, apertura=30.0), "")


def test_piso_frena_la_apertura_muerta():
    duros = M.t0_piso_temperatura(global_share=30.0, apertura=0.0)
    check("T0 piso apertura: 0% de cuerpo en las primeras 500 palabras es duro",
          any("T0" in d and "apertura" in d for d in duros), str(duros))


def test_piso_deja_pasar_el_capitulo_real_que_la_ama_va_a_leer():
    # «Hora Pedida» Cap 1 v0.2, medido el 08/09/2026: global 25,8 · apertura 25,8.
    duros = M.t0_piso_temperatura(global_share=25.8, apertura=25.8)
    check("T0 no frena el v0.2 aprobado por Loreto y el Validador", not duros, str(duros))


def test_piso_deja_pasar_el_capitulo_mas_frio_que_la_ama_publico():
    # El más frío de prosa real en 02_Finalizadas (08/09/2026): global 9,0 · apertura 2,6
    # («la_app_la_bimboficacion_de_mi_novio», capítulo 3). Un piso que reprueba lo que ella ya
    # publicó es un linter que enseña a ignorarlo. Esta prueba es la que fija el techo del piso.
    duros = M.t0_piso_temperatura(global_share=9.0, apertura=2.6)
    check("T0 no reprueba prosa que la Ama ya aprobó y publicó", not duros, str(duros))
    duros = M.t0_piso_temperatura(global_share=11.5, apertura=6.0)
    check("T0 tampoco reprueba el segundo más frío publicado (11,5 / 6,0)", not duros, str(duros))


def test_piso_si_caza_el_peor_borrador_del_repo():
    # `el_podcast` cap 1 v0.1 (08/09/2026): 1,8 global · 0,0 apertura. Es el vacío real.
    duros = M.t0_piso_temperatura(global_share=1.8, apertura=0.0)
    check("T0 caza el vacío real: los dos pisos disparan", len(duros) == 2, str(duros))


def test_piso_no_se_confunde_con_el_aviso_de_apertura():
    # El aviso T8 vive en 40%, sobre la MEDIANA de 25,0 de los 140 capítulos:
    # avisa en la mayoría. El piso es otra cosa y va mucho más abajo.
    duros = M.t0_piso_temperatura(global_share=27.7, apertura=25.0)
    check("T0 el piso no hereda el umbral del aviso T8 (40%)", not duros, str(duros))


def test_medir_marca_duro_el_capitulo_frio(tmp: Path):
    cap = tmp / "frio.md"
    cap.write_text("\n\n".join([
        "La reunión terminó a las once y el informe quedó sobre el escritorio.",
        "Firmó el acta, archivó la carpeta y revisó el calendario del trimestre.",
        "El presupuesto se aprobaría en la sesión siguiente, según el reglamento.",
        "Anotó la fecha, cerró el cuaderno y apagó la lámpara del escritorio.",
    ] * 8), encoding="utf-8")
    r = M.medir(cap, [], 120, 300)
    check("medir(): un capítulo sin un solo cuerpo cae en duro por T0",
          any(d.startswith("T0") for d in r["duros"]), str(r["duros"]))


def test_medir_no_marca_duro_por_t0_el_capitulo_con_cuerpo(tmp: Path):
    cap = tmp / "con_cuerpo.md"
    cap.write_text("\n\n".join([
        "Le puso la mano en el muslo y sintió la piel caliente bajo la media.",
        "La boca se le abrió sola y el pezón se le marcó contra la seda.",
        "Los dedos le subieron por la cadera y ella apretó los muslos.",
        "El aliento le quedó en el cuello y las tetas le temblaron.",
    ] * 8), encoding="utf-8")
    r = M.medir(cap, [], 120, 300)
    check("medir(): con cuerpo en toda la prosa, T0 no aparece en duros",
          not any(d.startswith("T0") for d in r["duros"]), str(r["duros"]))


def main() -> int:
    import tempfile
    print("🧪 Loreto — pruebas de las medidas de firma de IA (M13-M17)\n")
    test_m13_mide_la_clausula_y_no_la_oracion()
    test_m13_ignora_el_dialogo()
    test_m13_marca_clon_ritmico_contra_capitulo_previo()
    test_m13_no_marca_clon_cuando_el_ritmo_cambia()
    test_m13_no_opina_con_muestra_chica()
    test_m14_cuenta_los_dos_puntos_revelatorios()
    test_m14_no_cuenta_la_enumeracion()
    test_m14_no_cuenta_el_dos_puntos_que_abre_dialogo()
    test_m14_sigue_cazando_el_revelatorio_con_izquierda_corta()
    test_m14_no_cuenta_la_hora_ni_el_dialogo()
    test_m15_cuenta_el_simil_molde()
    test_m15_no_cuenta_la_comparacion_directa()
    test_m16_detecta_el_recibo_al_cierre_del_parrafo()
    test_m16_no_marca_la_excitacion_dentro_de_la_escena()
    test_m17_marca_el_dialogo_demasiado_limpio()
    test_m17_no_marca_cuando_hay_muletilla_o_interrupcion()
    test_piso_frena_el_capitulo_sin_cuerpo()
    test_piso_frena_la_apertura_muerta()
    test_piso_deja_pasar_el_capitulo_real_que_la_ama_va_a_leer()
    test_piso_deja_pasar_el_capitulo_mas_frio_que_la_ama_publico()
    test_piso_si_caza_el_peor_borrador_del_repo()
    test_piso_no_se_confunde_con_el_aviso_de_apertura()
    with tempfile.TemporaryDirectory() as d:
        test_medir_expone_la_firma_de_ia(Path(d))
        test_render_muestra_la_firma_de_ia(Path(d))
        test_medir_marca_duro_el_capitulo_frio(Path(d))
        test_medir_no_marca_duro_por_t0_el_capitulo_con_cuerpo(Path(d))
    print()
    if FALLAS:
        print(f"❌ {len(FALLAS)} falla(s): " + " · ".join(FALLAS))
        return 1
    print("✅ todas verdes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
