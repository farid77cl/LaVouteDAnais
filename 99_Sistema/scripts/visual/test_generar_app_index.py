#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pruebas del generador del índice que consume LV-App-3."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).parent))

import generar_app_index as GEN  # noqa: E402

AQUI = Path(__file__).parent
FIXTURES = AQUI / "fixtures_galerias"
CFG = json.loads((AQUI / "anclas_universales.json").read_text(encoding="utf-8"))["personajes"]

GALERIAS = {
    "ele": (FIXTURES / "ele_min.md").read_text(encoding="utf-8"),
    "miss_doll": (FIXTURES / "miss_doll_min.md").read_text(encoding="utf-8"),
    "anais": (FIXTURES / "anais_min.md").read_text(encoding="utf-8"),
}

ELE_ARCHIVO = (FIXTURES / "ele_archivo_min.md").read_text(encoding="utf-8")

# Sólo Ele tiene una imagen subida, y sólo la standing. La carpeta viaja con
# las imágenes porque el índice la toma de git, no del markdown (ver
# `test_la_carpeta_sale_de_git_y_no_del_markdown`).
IMAGENES = {
    "ele": {800: {"carpeta": "05_Imagenes/ele/look800_chrome_hooded_column/",
                  "poses": {"standing": "ele_800_standing.png"}}},
    "miss_doll": {},
    "anais": {},
}


def _indice():
    return GEN.construir_indice(CFG, IMAGENES, GALERIAS)


def test_estan_las_tres_munecas():
    idx = _indice()
    assert set(idx["personajes"]) == {"ele", "miss_doll", "anais"}
    slugs = {l["p"] for l in idx["looks"]}
    assert slugs == {"ele", "miss_doll", "anais"}


def test_cada_look_declara_las_siete_poses():
    for look in _indice()["looks"]:
        assert list(look["img"]) == GEN.POSES_CANON, look


def test_una_pose_sin_imagen_igual_declara_su_nombre_de_destino():
    look = next(l for l in _indice()["looks"] if l["p"] == "ele")
    assert look["img"]["standing"] == {"a": "ele_800_standing.png", "hay": True}
    assert look["img"]["pov"] == {"a": "ele_800_pov.png", "hay": False}


def test_anais_declara_el_numero_de_tres_digitos():
    look = next(l for l in _indice()["looks"] if l["p"] == "anais")
    assert look["img"]["standing"]["a"] == "anais_009_standing.png"


def test_el_nombre_de_la_quinta_pose_viaja_en_la_cabecera():
    idx = _indice()
    assert idx["personajes"]["anais"]["slot5"] == "Sovereign Gaze"
    assert idx["personajes"]["ele"]["slot5"] == "Ditzy"


# --- varias galerías por personaje (regla 11 §9bis: el archivo de Ele y la era
# gótica alimentan la app a propósito) --------------------------------------


def _galerias_con_archivo():
    g = dict(GALERIAS)
    g["ele"] = [GALERIAS["ele"], ELE_ARCHIVO]
    return g


def test_un_personaje_puede_declarar_mas_de_una_galeria():
    idx = GEN.construir_indice(CFG, IMAGENES, _galerias_con_archivo())
    assert sorted(l["n"] for l in idx["looks"] if l["p"] == "ele") == [42, 800]


def test_la_galeria_viva_gana_el_numero_repetido():
    idx = GEN.construir_indice(CFG, IMAGENES, _galerias_con_archivo())
    look = next(l for l in idx["looks"] if l["p"] == "ele" and l["n"] == 800)
    assert look["t"] == "Chrome Hooded Column"


def test_el_numero_repetido_se_reporta_como_hallazgo():
    hallazgos = []
    GEN.construir_indice(CFG, IMAGENES, _galerias_con_archivo(), hallazgos)
    assert any("800" in h for h in hallazgos), hallazgos


def test_los_prompts_tambien_salen_de_las_galerias_extra():
    p = GEN.construir_prompts(CFG, _galerias_con_archivo())
    assert "ele/42" in p
    assert p["ele/800"]["prompts"]["standing"] == "prompt de pie para ele look 800"


def test_el_indice_no_lleva_prompts():
    crudo = json.dumps(_indice(), ensure_ascii=False)
    assert "prompt de pie" not in crudo


def test_la_fecha_del_encabezado_llega_al_campo_emitido():
    """El campo `f` del índice, no `meta`.

    La prueba vieja miraba `look["meta"]` — que lo llena el parser — y por eso
    no vio nunca que `_fecha_de` no calzaba: la función rota era la que ningún
    test llamaba. El encabezado de Anaïs 9 lleva `11/08/2026`.
    """
    look = next(l for l in _indice()["looks"] if l["p"] == "anais")
    assert look["f"] == "11/08/2026"


def test_todos_los_looks_de_las_fixtures_traen_fecha():
    for look in _indice()["looks"]:
        assert look["f"] is not None, look


def test_la_carpeta_sale_de_git_y_no_del_markdown():
    """El `Ubicacion:` de la galería es texto a mano y ya divergió en vivo:
    miss_doll 80 apuntaba a `look80_sapphire_liquid_private_slip/` mientras git
    tenía `look80_sapphire_mesh_private_slip/`, con lo que las 7 entradas
    `hay:true` de ese look apuntaban a rutas inexistentes."""
    imgs = {"ele": {800: {"carpeta": "05_Imagenes/ele/look800_otro_slug/",
                          "poses": {"standing": "ele_800_standing.png"}}},
            "miss_doll": {}, "anais": {}}
    look = next(l for l in GEN.construir_indice(CFG, imgs, GALERIAS)["looks"]
                if l["p"] == "ele")
    assert look["d"] == "05_Imagenes/ele/look800_otro_slug/"


def test_la_carpeta_discrepante_se_reporta_como_hallazgo():
    imgs = {"ele": {800: {"carpeta": "05_Imagenes/ele/look800_otro_slug/",
                          "poses": {"standing": "ele_800_standing.png"}}},
            "miss_doll": {}, "anais": {}}
    hallazgos = []
    GEN.construir_indice(CFG, imgs, GALERIAS, hallazgos)
    assert any("look800_otro_slug" in h and "look800_chrome_hooded_column" in h
               for h in hallazgos), hallazgos


def test_sin_imagen_trackeada_la_carpeta_sale_del_markdown():
    look = next(l for l in _indice()["looks"] if l["p"] == "miss_doll")
    assert look["d"] == "05_Imagenes/miss_doll/look10_midnight_plum_rite/"


def test_un_look_sin_ninguna_imagen_no_declara_portada():
    """Sin parser defensivo en la app, un `c` apuntando a `hay:false` es una
    peticion garantizada de una imagen que no existe."""
    look = next(l for l in _indice()["looks"] if l["p"] == "miss_doll")
    assert look["np"] == 0
    assert look["c"] is None


def test_con_imagen_la_portada_es_una_pose_presente():
    look = next(l for l in _indice()["looks"] if l["p"] == "ele")
    assert look["c"] == "standing"
    assert look["img"][look["c"]]["hay"] is True


def test_np_cuenta_solo_imagenes_reales():
    look = next(l for l in _indice()["looks"] if l["p"] == "ele")
    assert look["np"] == 1


# --- pose_canonica: camino canónico (reusa nombres_canonicos) y camino
# histórico (alias/prefijos de la flota vieja) ------------------------------

def test_pose_canonica_anais_standing_via_su_propia_numeracion():
    assert GEN.pose_canonica("anais_L09_standing.png", 9, CFG["anais"]) == "standing"


def test_pose_canonica_anais_slot5_via_su_propia_numeracion():
    assert GEN.pose_canonica("anais_L09_sovereign_gaze.png", 9, CFG["anais"]) == "slot5"


def test_pose_canonica_ele_standing():
    assert GEN.pose_canonica("ele_800_standing.png", 800, CFG["ele"]) == "standing"


def test_pose_canonica_ele_slot5():
    assert GEN.pose_canonica("ele_800_ditzy.png", 800, CFG["ele"]) == "slot5"


def test_pose_canonica_miss_doll_slot5():
    assert GEN.pose_canonica("miss_doll_10_glacial_command.png", 10, CFG["miss_doll"]) == "slot5"


def test_pose_canonica_alias_historico_back():
    assert GEN.pose_canonica("helena_001_back.png", 1, CFG["ele"]) == "back_view"


def test_pose_canonica_alias_historico_profile():
    assert GEN.pose_canonica("helena_001_profile.png", 1, CFG["ele"]) == "side_profile"


def test_pose_canonica_irreconocible_es_none():
    assert GEN.pose_canonica("ele_800_calzado_extra.png", 800, CFG["ele"]) is None


# --- construir_prompts: los 7 prompts de cada look en un archivo JSON
# descargado bajo demanda por la app -----------------------------------------


def _prompts():
    return GEN.construir_prompts(CFG, GALERIAS)


def test_hay_un_archivo_de_prompts_por_look():
    assert set(_prompts()) == {"ele/800", "miss_doll/10", "anais/9"}


def test_los_prompts_van_bajo_su_llave_canonica():
    p = _prompts()["anais/9"]["prompts"]
    assert p["standing"] == "prompt de pie para anais look 9"
    assert p["slot5"] == "prompt de mirada soberana para anais look 9"
    assert "sovereign_gaze" not in p


def test_el_negative_viaja_con_el_look():
    assert "flat shoes" in _prompts()["ele/800"]["neg"]


def test_una_pose_sin_prompt_escrito_no_aparece():
    assert "pov" not in _prompts()["ele/800"]["prompts"]


if __name__ == "__main__":
    import pytest
    raise SystemExit(pytest.main([__file__, "-v"]))
