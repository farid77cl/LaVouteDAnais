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


# La convención es UNA sola para las tres muñecas desde el 07/09/2026:
# número de tres dígitos con ceros a la izquierda. Medido contra `git ls-files`,
# es lo que emite hoy el productor vivo (`miss_doll_085_back_view.png`,
# `anais_085_back_view.png`) y lo que lleva la mayoría de cada flota. Lo que
# declaraba el config antes (`{n}` en Miss Doll, `L{n:02d}` en Anaïs) calzaba
# con 96 de 585 y 154 de 585 archivos respectivamente.


def test_ele_numera_con_tres_digitos():
    assert N.nombre_archivo(800, "standing", CFG["ele"]) == "ele_800_standing.png"


def test_miss_doll_numera_con_tres_digitos():
    assert N.nombre_archivo(10, "seated", CFG["miss_doll"]) == "miss_doll_010_seated.png"


def test_anais_numera_con_tres_digitos():
    assert N.nombre_archivo(9, "standing", CFG["anais"]) == "anais_009_standing.png"


def test_las_tres_munecas_comparten_el_formato_de_numero():
    """Un look de dos y otro de tres dígitos, para que el padding quede fijado
    por prueba y no por costumbre."""
    assert N.nombre_archivo(85, "standing", CFG["miss_doll"]) == "miss_doll_085_standing.png"
    assert N.nombre_archivo(85, "standing", CFG["anais"]) == "anais_085_standing.png"
    assert N.nombre_archivo(85, "standing", CFG["ele"]) == "ele_085_standing.png"
    assert N.nombre_archivo(445, "standing", CFG["ele"]) == "ele_445_standing.png"
    assert N.nombre_archivo(445, "standing", CFG["anais"]) == "anais_445_standing.png"


def test_el_slot5_usa_el_slug_de_cada_muneca_en_el_archivo():
    assert N.nombre_archivo(800, "slot5", CFG["ele"]) == "ele_800_ditzy.png"
    assert N.nombre_archivo(9, "slot5", CFG["anais"]) == "anais_009_sovereign_gaze.png"
    assert N.nombre_archivo(10, "slot5", CFG["miss_doll"]) == "miss_doll_010_glacial_command.png"


def test_carpeta_del_look():
    assert N.carpeta_look(800, "chrome_hooded_column", CFG["ele"]) == \
        "05_Imagenes/ele/look800_chrome_hooded_column/"


if __name__ == "__main__":
    import pytest
    raise SystemExit(pytest.main([__file__, "-v"]))
