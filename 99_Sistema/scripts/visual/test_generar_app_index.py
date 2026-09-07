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


def test_anais_declara_su_numeracion_propia():
    look = next(l for l in _indice()["looks"] if l["p"] == "anais")
    assert look["img"]["standing"]["a"] == "anais_L09_standing.png"


def test_el_nombre_de_la_quinta_pose_viaja_en_la_cabecera():
    idx = _indice()
    assert idx["personajes"]["anais"]["slot5"] == "Sovereign Gaze"
    assert idx["personajes"]["ele"]["slot5"] == "Ditzy"


def test_el_indice_no_lleva_prompts():
    crudo = json.dumps(_indice(), ensure_ascii=False)
    assert "prompt de pie" not in crudo


def test_np_cuenta_solo_imagenes_reales():
    look = next(l for l in _indice()["looks"] if l["p"] == "ele")
    assert look["np"] == 1


if __name__ == "__main__":
    import pytest
    raise SystemExit(pytest.main([__file__, "-v"]))
