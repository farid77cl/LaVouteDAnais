#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El log del motor no se ensucia con builds de fixtures.

`99_Sistema/logs/outfit_engine.jsonl` es un archivo **trackeado** y el dueño
único del registro de `build()`: cada prompt emitido deja su timestamp,
personaje, slot, largo, anclas opt-in y fallas. Nació de la auditoría del
17/08/2026, cuando reconstruir de dónde se copió un bloque fue trabajo manual
sobre el historial de git.

El defecto (declarado como deuda el 08/09/2026, arreglado el 09/09): **la propia
suite lo escribe**. `outfit.py test` ejercita el motor con fixtures y cada uno
deja su línea — ~142 por corrida, todas con `look: null`. Consecuencias reales
medidas: el árbol queda sucio después de correr los tests, y hubo que hacer
`git checkout -- 99_Sistema/logs/outfit_engine.jsonl` a mano **antes de cada uno
de los commits de esta sesión**. Peor: un log cuya mayoría son fixtures deja de
servir para lo que existe — buscar cuándo se emitió un prompt de verdad.

La corrida de fixtures no es un evento del motor. Se marca y se omite.
"""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).parent))

import os as _os
# Una batería ejercita el motor con FIXTURES: su rastro no es historial del
# motor y no puede ensuciar `99_Sistema/logs/outfit_engine.jsonl`, que está
# trackeado (09/09/2026). Se apaga ANTES de importar el motor.
_os.environ.setdefault("OUTFIT_ENGINE_LOG", "0")


AQUI = Path(__file__).parent
RAIZ = AQUI.parent.parent.parent


def _lineas_del_log():
    p = RAIZ / "99_Sistema" / "logs" / "outfit_engine.jsonl"
    return len(p.read_text(encoding="utf-8").splitlines()) if p.exists() else 0


def test_correr_la_suite_no_agrega_ni_una_linea_al_log():
    antes = _lineas_del_log()
    r = subprocess.run([sys.executable, str(AQUI / "outfit.py"), "test"],
                       capture_output=True, text=True, encoding="utf-8", cwd=str(RAIZ))
    assert r.returncode == 0, r.stdout[-600:]
    assert _lineas_del_log() == antes, (
        "la suite escribió %d línea(s) en un log trackeado"
        % (_lineas_del_log() - antes))


def test_una_emision_de_verdad_SI_queda_registrada():
    """La guardia no puede apagar el log entero: el registro existe por algo."""
    import importlib
    import prompt_builder
    importlib.reload(prompt_builder)
    # Esta batería apaga el log al importar (guardia de arriba); acá se enciende
    # a propósito, porque lo que se prueba es justamente que registre.
    previo = os.environ.pop("OUTFIT_ENGINE_LOG", None)
    try:
        with tempfile.TemporaryDirectory() as d:
            destino = os.path.join(d, "motor.jsonl")
            prompt_builder.LOG_PATH = destino
            prompt_builder._log_evento({"evento": "build", "personaje": "ele", "slot": "standing"})
            assert os.path.exists(destino), "un build de verdad TIENE que quedar registrado"
            assert "standing" in open(destino, encoding="utf-8").read()
    finally:
        if previo is not None:
            os.environ["OUTFIT_ENGINE_LOG"] = previo


def test_un_evento_marcado_fixture_no_se_escribe():
    import importlib
    import prompt_builder
    importlib.reload(prompt_builder)
    with tempfile.TemporaryDirectory() as d:
        destino = os.path.join(d, "motor.jsonl")
        prompt_builder.LOG_PATH = destino
        prompt_builder._log_evento({"evento": "build", "personaje": "ele", "fixture": True})
        assert not os.path.exists(destino), "un build de fixture no es un evento del motor"


def test_ninguna_suite_suelta_ensucia_el_log():
    """No basta con apagarlo en `outfit.py test`: las baterías que se corren
    solas (`python test_bloques.py`) también llaman a `build()`. Medido — con la
    guardia puesta solo en el comando, `test_bloques` y `test_bottom_cut_lock`
    seguían escribiendo."""
    suites = ["test_bloques.py", "test_bottom_cut_lock.py", "test_ojos.py",
              "test_contradicciones.py"]
    antes = _lineas_del_log()
    for suite in suites:
        r = subprocess.run([sys.executable, str(AQUI / suite)],
                           capture_output=True, text=True, encoding="utf-8", cwd=str(RAIZ))
        assert r.returncode == 0, (suite, r.stdout[-400:])
    assert _lineas_del_log() == antes, (
        "las suites sueltas escribieron %d línea(s)" % (_lineas_del_log() - antes))


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
