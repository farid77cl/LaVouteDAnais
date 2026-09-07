#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pruebas del parser de galerías compartido entre el linter y el generador."""
from __future__ import annotations

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).parent))

import galeria_parser as G  # noqa: E402

FIXTURES = Path(__file__).parent / "fixtures_galerias"


def _anais():
    return (FIXTURES / "anais_min.md").read_text(encoding="utf-8")


def test_parsea_el_numero_y_el_titulo_del_look():
    looks = G.parse_como_la_app(_anais(), "Sovereign Gaze")
    assert len(looks) == 1
    assert looks[0]["num"] == 9
    assert looks[0]["titulo"] == "Esmeralda Íntima"


def test_recoge_los_tres_prompts_bajo_su_pose():
    looks = G.parse_como_la_app(_anais(), "Sovereign Gaze")
    prompts = looks[0]["prompts"]
    assert "Standing" in prompts
    assert "Back View" in prompts
    assert "Sovereign Gaze" in prompts
    assert prompts["Standing"][0] == "prompt de pie para anais look 9"


def test_el_slot5_de_cada_personaje_cae_en_la_misma_llave():
    assert G.slug_de_pose("Sovereign Gaze", "Sovereign Gaze") == "slot5"
    assert G.slug_de_pose("Ditzy", "Ditzy") == "slot5"
    assert G.slug_de_pose("Glacial Command", "Glacial Command") == "slot5"
    assert G.slug_de_pose("Back View", "Ditzy") == "back_view"


def test_lee_ubicacion_tags_y_negative():
    look = G.parse_como_la_app(_anais(), "Sovereign Gaze")[0]
    assert look["ubicacion"] == "05_Imagenes/anais/look9_esmeralda_intima/"
    assert "#boudoir" in look["tags"]
    assert "flat shoes" in look["negative"]


def test_conserva_el_parentesis_del_encabezado_donde_vive_la_fecha():
    look = G.parse_como_la_app(_anais(), "Sovereign Gaze")[0]
    assert look["meta"] is not None
    assert "11/08/2026" in look["meta"]


if __name__ == "__main__":
    import pytest
    raise SystemExit(pytest.main([__file__, "-v"]))
