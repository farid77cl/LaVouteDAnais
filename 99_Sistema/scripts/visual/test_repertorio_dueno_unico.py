#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Guardia de dueño único sobre `repertorios_pose.json`.

Por qué existe (09/09/2026). El 04/09 la Ama cambió el iris de Miss Doll
(*"miss doll que sean azules solamente, el steel grey a veces le salen los ojos
blancos, como un white walker"*). La corrección se aplicó donde correspondía —el
BLOQUE A del perfil y el negative base §3— pero **nadie barrió el repertorio de
sub-poses**, y ahí quedaron cinco variantes del slot `odalisque` con el token
derogado escrito adentro: `her cold pale steel grey eyes locked onto the camera`.

Medido antes de arreglarlo: **10 looks emitidos DESPUÉS del cambio** llevan el
token gris en su prompt de Odalisque —y solo ahí— mientras sus otras seis poses
llevan el cobalto correcto. O sea el mismo prompt pedía las dos cosas. La imagen
del L89 salió azul igual, pero eso es suerte del generador, no la regla puesta.

La regla estructural que esto viola es la de dueño único: **el color de iris es
del BLOQUE A del perfil**; la sub-pose describe la MIRADA (dirección, frialdad,
gesto), nunca el color. Ele y Anaïs ya cumplían — sus sub-poses no nombran color
de ojos en ninguna de las 63. Las cinco de Miss Doll eran las únicas fuera.
"""

from __future__ import annotations

import json
import re
import sys

import os as _os
# Una bateria ejercita el motor con FIXTURES: su rastro no es historial del motor
# y no puede ensuciar `99_Sistema/logs/outfit_engine.jsonl`, que esta trackeado
# (09/09/2026). Se apaga ANTES de importar el motor.
_os.environ.setdefault("OUTFIT_ENGINE_LOG", "0")
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

REPERTORIO = Path(__file__).parent / "repertorios_pose.json"

# Color de iris: propiedad del BLOQUE A, prohibida dentro de una sub-pose.
# "cold eyes" / "eyes locked onto the lens" SÍ se permiten: eso es mirada.
RX_COLOR_DE_IRIS = re.compile(
    r"\b(?:grey|gray|blue|green|amber|honey|cobalt|hazel|steel|icy|violet|"
    r"golden|silver)\b[^,.]{0,30}?\b(?:eyes|iris)\b",
    re.I,
)


def _sub_poses():
    data = json.loads(REPERTORIO.read_text(encoding="utf-8"))
    for slug, ficha in data["personajes"].items():
        for slot, variantes in ficha["slots"].items():
            for i, texto in enumerate(variantes):
                yield slug, slot, i, texto


def test_ninguna_sub_pose_nombra_el_color_del_iris():
    fugas = [
        f"{slug} > {slot} > [{i}]: «{RX_COLOR_DE_IRIS.search(t).group(0)}»"
        for slug, slot, i, t in _sub_poses()
        if RX_COLOR_DE_IRIS.search(t)
    ]
    assert not fugas, (
        "El color de iris es del BLOQUE A del perfil, no de la sub-pose:\n  "
        + "\n  ".join(fugas)
    )


def test_el_token_derogado_de_miss_doll_no_revive():
    # Token exacto que la Ama derogó el 04/09/2026.
    derogados = ("steel grey eyes", "pale icy grey iris", "icy grey eyes")
    fugas = [
        f"{slug} > {slot} > [{i}]: «{d}»"
        for slug, slot, i, t in _sub_poses()
        for d in derogados
        if d in t.lower()
    ]
    assert not fugas, "Token de iris derogado el 04/09/2026, vivo otra vez:\n  " + "\n  ".join(fugas)


def test_el_repertorio_sigue_teniendo_las_tres_munecas_con_sus_siete_slots():
    # Guardia de que el barrido no borró nada por el camino.
    data = json.loads(REPERTORIO.read_text(encoding="utf-8"))
    for slug in ("ele", "miss_doll", "anais"):
        slots = data["personajes"][slug]["slots"]
        assert len(slots) == 7, f"{slug} tiene {len(slots)} slots, no 7"
        for slot, variantes in slots.items():
            assert variantes, f"{slug} > {slot} quedó sin variantes"


def _correr():
    import traceback
    pruebas = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    ok = fallas = 0
    for fn in pruebas:
        try:
            fn()
            ok += 1
            print(f"  ok   {fn.__name__}")
        except Exception:
            fallas += 1
            print(f"  FALLA {fn.__name__}")
            traceback.print_exc()
    print(f"\n  RESULTADO: {ok} ok · {fallas} fallas")
    return 1 if fallas else 0


if __name__ == "__main__":
    raise SystemExit(_correr())
