#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pruebas del generador del índice de relatos que consume LV-App-3.

Fixtures a mano, nunca la carpeta real: mismo criterio que el resto de
`99_Sistema/scripts/`. Corre sin pytest (esta máquina no lo tiene):

    python 99_Sistema/scripts/literatura/test_generar_app_relatos.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).parent))

import generar_app_relatos as G  # noqa: E402

FALLAS: list[str] = []


def check(nombre, cond, detalle=""):
    if cond:
        print(f"  ✅ {nombre}")
    else:
        FALLAS.append(nombre)
        print(f"  ❌ {nombre}  {detalle}")


# --------------------------------------------------------------------------
# es_prosa -- la decisión de la que depende que un relato se vea o no
# --------------------------------------------------------------------------
def test_es_prosa():
    print("\nes_prosa")
    # Las cuatro formas REALES que tiene la prosa en este repo, medidas el
    # 13/09/2026. Sólo la primera lleva el prefijo `capitulo_`.
    for nombre in [
        "capitulo_1_mi_primer_turno.md",
        "Tetitas.md",
        "el_collar_de_nancy_completo.md",
        "El_hotel_primera_noche.md",
        "Capítulo_I_Le_miroir_d’Anaïs.md",
        "trance_office_siren_v0.18.md",
        "relato_final_V1.md",
        "La_Evaluacion_de_Miss_Doll.md",
    ]:
        check(f"prosa: {nombre}", G.es_prosa(nombre))

    for nombre in [
        "canon_relato.md", "cronologia.md", "walkthrough.md", "brief_idea.md",
        "concepto.md", "investigacion.md", "investigacion_tema.md",
        "investigacion_fetiches.md", "diseno_trance.md", "arco_y_timeline.md",
        "fichas_personajes.md", "kit_wattpad.md", "prompts_portada.md",
        "README.md", "notas.md", "pitch_arquitectura_del_castigo_v2.md",
        "nota_capitulo_4_cafe_v0.3.md", "gate_capitulo_4_cafe_v0.3.md",
        "portada.png",
    ]:
        check(f"NO prosa: {nombre}", not G.es_prosa(nombre))


# --------------------------------------------------------------------------
# numero_de_capitulo -- la regresión del `\b`
# --------------------------------------------------------------------------
def test_numero_de_capitulo():
    print("\nnumero_de_capitulo")
    # Éstos son exactamente los nombres que devolvían None por el `\b`: en una
    # expresión regular el guión bajo es carácter de palabra, así que no hay
    # frontera entre el número y el `_` que le sigue. El defecto quedaba
    # tapado porque el orden alfabético del nombre coincidía con el orden real
    # de los capítulos -- en todos los relatos menos `serie_anais`.
    casos = {
        "capitulo_1_el_cajon_v0.3.md": 1,
        "capitulo_01_la_promesa_de_armadura_v0.1.md": 1,
        "capitulo_4_cuanto_es.md": 4,
        "capitulo_02_los_cuadernos_de_anais_v0.1.md": 2,
        "capitulo_01_la_palabra_maestro_v1.0.md": 1,
        "Capítulo_I_Le_miroir_d’Anaïs.md": 1,
        "_Capítulo_II_Sous_la_dentelle_l.md": 2,
        "_Capítulo_III_La_semaine_du_miro.md": 3,
        "_Capítulo_IV_La_cena_del_juicio.md": 4,
        "Tetitas.md": None,
        "El_hotel_primera_noche.md": None,
    }
    for nombre, esperado in casos.items():
        real = G.numero_de_capitulo(nombre)
        check(f"{nombre} -> {esperado}", real == esperado, f"dio {real}")


def test_version_de_capitulo():
    print("\nversion_de_capitulo")
    casos = {
        "capitulo_1_el_cajon_v0.3.md": "0.3",
        "trance_office_siren_v0.18.md": "0.18",
        "capitulo_01_la_palabra_maestro_v1.0.md": "1.0",
        "relato_final_V1.md": "1",
        "Tetitas.md": None,
    }
    for nombre, esperado in casos.items():
        real = G.version_de_capitulo(nombre)
        check(f"{nombre} -> {esperado}", real == esperado, f"dio {real}")


def test_romanos():
    print("\nnumero_romano")
    for texto, esperado in {"I": 1, "II": 2, "III": 3, "IV": 4, "IX": 9,
                            "XL": 40, "": None, "ABC": None}.items():
        check(f"{texto!r} -> {esperado}", G.numero_romano(texto) == esperado)


# --------------------------------------------------------------------------
# El Gate: nunca se infiere (Regla de Oro 8c)
# --------------------------------------------------------------------------
def test_el_gate_no_se_infiere():
    print("\nel Gate sale del archivo, nunca de otra cosa")
    archivos = {
        "canon_relato.md": "# Canon Relato — «Hora Pedida»",
        "capitulo_1_el_cajon_v0.3.md": "# Capítulo 1: El cajón\n\ntexto",
    }
    r = G.construir_relato("hora_pedida", "en_progreso", "x/hora_pedida", archivos)
    check("sin archivo de gate -> espera Gate", r["caps"][0]["espera_gate"] is True)
    check("sin archivo de gate -> gate False", r["caps"][0]["gate"] is False)

    con_gate = dict(archivos)
    con_gate["gate_capitulo_1_hora_pedida_v0.3.md"] = "aprobado"
    r2 = G.construir_relato("hora_pedida", "en_progreso", "x/hora_pedida", con_gate)
    check("con el archivo -> hay Gate", r2["caps"][0]["gate"] is True)
    check("con el archivo -> ya no espera", r2["caps"][0]["espera_gate"] is False)
    check("el archivo de gate no es un capítulo", len(r2["caps"]) == 1)

    # Un gate de OTRA versión no vale para ésta: la Regla de Oro 8c nombra
    # capítulo Y versión.
    otra = dict(archivos)
    otra["gate_capitulo_1_hora_pedida_v0.1.md"] = "aprobado"
    r3 = G.construir_relato("hora_pedida", "en_progreso", "x/hora_pedida", otra)
    check("un gate de otra versión no cuenta", r3["caps"][0]["espera_gate"] is True)

    # El archivo que dice «maestro» NO es un Gate.
    maestro = {"capitulo_01_la_palabra_maestro_v1.0.md": "# La palabra\n\ntexto"}
    r4 = G.construir_relato("x", "en_progreso", "x/x", maestro)
    check("«maestro» no vale como Gate", r4["caps"][0]["espera_gate"] is True)

    # Un relato terminado no espera nada.
    r5 = G.construir_relato("tetitas", "terminado", "x/tetitas", {"Tetitas.md": "# Tetitas\n\nt"})
    check("un terminado no espera Gate", r5["caps"][0]["espera_gate"] is False)


def test_nota_pendiente():
    print("\nnota sin aplicar")
    archivos = {
        "capitulo_4_cuanto_es.md": "# Cuánto es\n\ntexto",
        "nota_capitulo_4_cafe_v0.3.md": "arréglame esto",
    }
    r = G.construir_relato("cafe", "en_progreso", "x/cafe", archivos)
    check("la nota marca el capítulo 4", r["caps"][0]["nota"] is True)
    check("la nota no es un capítulo", len(r["caps"]) == 1)


# --------------------------------------------------------------------------
# Orden, numeración y títulos
# --------------------------------------------------------------------------
def test_orden_y_numeracion():
    print("\norden y numeración")
    # serie_anais: el caso que destapó el `\b`. Ordenados por NOMBRE quedan
    # I, III, II, IV -- porque `I` (0x49) es menor que `_` (0x5F).
    archivos = {
        "Capítulo_I_Le_miroir_d’Anaïs.md": "# Le Miroir — Capítulo I\n\na",
        "_Capítulo_III_La_semaine_du_miro.md": "# La Semaine — Capítulo III\n\na",
        "_Capítulo_II_Sous_la_dentelle_l.md": "# Sous la Dentelle — Capítulo II\n\na",
        "_Capítulo_IV_La_cena_del_juicio.md": "# La Cena — Capítulo IV\n\na",
    }
    r = G.construir_relato("serie_anais", "terminado", "x/serie_anais", archivos)
    check("los cuatro romanos, en orden", [c["n"] for c in r["caps"]] == [1, 2, 3, 4],
          str([c["n"] for c in r["caps"]]))

    # Un relato de un solo archivo sin número declarado queda en el capítulo 1.
    r2 = G.construir_relato("tetitas", "terminado", "x/tetitas", {"Tetitas.md": "# Tetitas\n\na b c"})
    check("archivo único -> capítulo 1", r2["caps"][0]["n"] == 1)
    check("cuenta palabras del cuerpo", r2["caps"][0]["pal"] == 5, str(r2["caps"][0]["pal"]))


def test_titulos():
    print("\ntítulos")
    check("del README",
          G.titulos_del_readme("| [Café con Piernas](cafe_con_piernas/) ☕ |")
          == {"cafe_con_piernas": "Café con Piernas"})
    check("los slugs de serie llevan mayúscula",
          "brillando_en_tacones_I" in G.titulos_del_readme("[Brillando I](brillando_en_tacones_I/)"))
    check("el enlace cuyo texto ES la carpeta no es un título",
          G.titulos_del_readme("[serie_anais/](serie_anais/)") == {})

    check("del canon, entre comillas angulares",
          G.titulo_de_documento_de_trabajo("# Canon Relato — «Hora Pedida»\n") == "Hora Pedida")
    check("del canon, con nota al margen entre paréntesis",
          G.titulo_de_documento_de_trabajo(
              "# Canon Relato — Modo Trofeo (título de trabajo)\n") == "Modo Trofeo")
    check("de la ficha de trance",
          G.titulo_de_documento_de_trabajo(
              "# Diseño de Trance — Office Siren (La Ejecutiva)\n") == "Office Siren")

    # Cascada completa: sin README y sin canon, cae al H1 del primer capítulo
    # antes que al slug.
    r = G.construir_relato("la_evaluacion_de_miss_doll", "en_progreso", "x/y",
                           {"La_Evaluacion_de_Miss_Doll.md": "# La Evaluación de Miss Doll\n\na"})
    check("cae al H1 del capítulo antes que al slug", r["t"] == "La Evaluación de Miss Doll")

    fuentes = {}
    G.construir_relato("sin_nada", "terminado", "x/y", {}, None, None, fuentes)
    check("sin nada de nada, cae al slug", fuentes["sin_nada"] == "slug")


# --------------------------------------------------------------------------
# La forma del JSON -- contrato con la app
# --------------------------------------------------------------------------
def test_forma_del_indice():
    print("\nforma del índice")
    por_relato = {("terminado", "tetitas"): ["Tetitas.md", "portada.png"]}
    textos = {"03_Literatura/02_Finalizadas/tetitas/Tetitas.md": "# Tetitas\n\nuno dos"}
    idx = G.construir_indice(por_relato, textos.get, {}, [], [])
    check("trae versión de esquema", idx["v"] == G.VERSION_ESQUEMA)
    r = idx["relatos"][0]
    check("carpeta completa para pedirle el archivo a GitHub",
          r["carpeta"] == "03_Literatura/02_Finalizadas/tetitas")
    check("campos del capítulo",
          set(r["caps"][0]) == {"n", "t", "a", "ver", "pal", "gate", "nota", "espera_gate"},
          str(sorted(r["caps"][0])))
    check("el .png no entra", len(r["caps"]) == 1)

    # Un archivo trackeado que no está en disco se reporta, nunca se inventa.
    ausentes = []
    idx2 = G.construir_indice(
        {("terminado", "x"): ["fantasma.md"]}, lambda _: None, {}, [], ausentes)
    check("el archivo ausente se reporta", ausentes == ["03_Literatura/02_Finalizadas/x/fantasma.md"])
    check("y no produce capítulo", idx2["relatos"][0]["caps"] == [])


def test_raices_y_carpetas_sin_raiz():
    print("\nraíces")
    rutas = [
        "03_Literatura/02_Finalizadas/tetitas/Tetitas.md",
        "03_Literatura/02_Finalizadas/tetitas/_publicacion/x.html",
        "03_Literatura/02_Finalizadas/the_dollhouse/_publicacion/x.html",
        "03_Literatura/01_En_Progreso/hora_pedida/canon_relato.md",
        "03_Literatura/README.md",
    ]
    sin_raiz = []
    r = G._raices(rutas, sin_raiz)
    check("sólo archivos de la raíz del relato",
          r[("terminado", "tetitas")] == ["Tetitas.md"], str(r))
    check("el estado sale de la carpeta base", ("en_progreso", "hora_pedida") in r)
    check("la carpeta sin raíz se reporta", sin_raiz == ["the_dollhouse"], str(sin_raiz))


def main() -> int:
    test_es_prosa()
    test_numero_de_capitulo()
    test_version_de_capitulo()
    test_romanos()
    test_el_gate_no_se_infiere()
    test_nota_pendiente()
    test_orden_y_numeracion()
    test_titulos()
    test_forma_del_indice()
    test_raices_y_carpetas_sin_raiz()
    print()
    if FALLAS:
        print(f"❌ {len(FALLAS)} falla(s): " + " · ".join(FALLAS))
        return 1
    print("✅ todas verdes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
