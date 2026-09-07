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

# Sólo Ele tiene una imagen subida, y sólo la standing.
IMAGENES = {
    "ele": {800: {"standing": "ele_800_standing.png"}},
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
