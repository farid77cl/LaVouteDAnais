#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pruebas del constructor de nombres canónicos de imagen."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).parent))

import nombres_canonicos as N  # noqa: E402

CFG = json.loads(
    (Path(__file__).parent / "anclas_universales.json").read_text(encoding="utf-8")
)["personajes"]


def test_ele_numera_pelado():
    assert N.nombre_archivo("ele", 800, "standing", CFG["ele"]) == "ele_800_standing.png"


def test_miss_doll_numera_pelado():
    assert N.nombre_archivo("miss_doll", 10, "seated", CFG["miss_doll"]) == "miss_doll_10_seated.png"


def test_anais_numera_con_L_y_dos_digitos():
    assert N.nombre_archivo("anais", 9, "standing", CFG["anais"]) == "anais_L09_standing.png"


def test_el_slot5_usa_el_slug_de_cada_muneca_en_el_archivo():
    assert N.nombre_archivo("ele", 800, "slot5", CFG["ele"]) == "ele_800_ditzy.png"
    assert N.nombre_archivo("anais", 9, "slot5", CFG["anais"]) == "anais_L09_sovereign_gaze.png"
    assert N.nombre_archivo("miss_doll", 10, "slot5", CFG["miss_doll"]) == "miss_doll_10_glacial_command.png"


def test_carpeta_del_look():
    assert N.carpeta_look("ele", 800, "chrome_hooded_column", CFG["ele"]) == \
        "05_Imagenes/ele/look800_chrome_hooded_column/"


if __name__ == "__main__":
    import pytest
    raise SystemExit(pytest.main([__file__, "-v"]))
