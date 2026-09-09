#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El auditor de flota separa lo ARREGLABLE de lo que ya es historia.

Deuda declarada el 08/09/2026: *«`auditar_canon_flota` va en 872 violaciones
sobre 685 looks… ese auditor está en el estado de "linter que grita lo
inarreglable"»*. Medido el 09/09 y el reparto es el punto:

    toda la galería      →  872 violaciones
    solo looks SIN imagen →   20 violaciones

O sea **852 de las 872 son de looks YA MATERIALIZADOS**. El prompt de un look
con sus 7 fotos hechas es historia: reescribirlo dejaría un archivo prolijo que
**miente sobre su propia flota** (la misma razón por la que las 35 copias del
ADN de Miss Doll no se actualizaron el 04/09). No son deuda: son registro.

Este arreglo NO cambia qué se detecta ni relaja una sola regla. Cambia **qué
número queda como titular**, que es lo que decide si alguien lo lee: el
accionable arriba, el histórico contado aparte y declarado como tal. Es el mismo
patrón que ya rige en `rotacion_*.historicos_declarados`, donde un look
materializado que viola una regla baja a aviso — *un linter que grita lo
inarreglable enseña a ignorarlo, y la meta es 0, y 0 tiene que significar algo*.

Y el **exit code** pasa a mirar solo lo accionable: hoy sale 1 siempre, así que
no sirve de puerta para nada.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

AQUI = Path(__file__).parent
RAIZ = AQUI.parent.parent.parent


def _correr_auditor(*flags):
    return subprocess.run([sys.executable, str(AQUI / "auditar_canon_flota.py"), *flags],
                          capture_output=True, text=True, encoding="utf-8", cwd=str(RAIZ))


def test_el_titular_es_lo_accionable_no_el_historico():
    r = _correr_auditor()
    assert "ACCIONABLE" in r.stdout, "el titular tiene que nombrar lo accionable"
    assert "historico" in r.stdout.lower() or "histórico" in r.stdout.lower(), \
        "lo ya materializado tiene que contarse aparte y declararse"


def test_el_exit_code_mira_solo_lo_accionable():
    """Hoy sale 1 siempre (872 > 0), así que no sirve de puerta para nada.
    Tiene que reflejar lo que alguien PUEDE arreglar."""
    r = _correr_auditor()
    accionables = _accionables()
    assert r.returncode == (1 if accionables else 0), (r.returncode, accionables)


def _accionables():
    r = _correr_auditor("--solo-sin-imagen")
    import re
    m = re.search(r"violaciones=(\d+)", r.stdout)
    return int(m.group(1)) if m else None


def test_los_dos_numeros_aparecen_y_cuadran():
    """El histórico no se esconde: se cuenta, se nombra y suma con el accionable."""
    import re
    r = _correr_auditor()
    m = re.search(r"ACCIONABLE[^\d]*(\d+)", r.stdout)
    h = re.search(r"[Hh]ist[oó]ric[oa][^\d]*(\d+)", r.stdout)
    assert m and h, r.stdout[-700:]
    total = re.search(r"violaciones=(\d+)", r.stdout)
    assert total and int(m.group(1)) + int(h.group(1)) == int(total.group(1)), \
        (m.group(1), h.group(1), total.group(1) if total else None)


def test_no_se_relaja_ninguna_regla():
    """Guardia: el total detectado no puede bajar. Esto reordena el reporte,
    no afloja el canon."""
    import re
    r = _correr_auditor()
    total = re.search(r"violaciones=(\d+)", r.stdout)
    assert total and int(total.group(1)) >= 800, \
        "el total detectado bajó: esto debía reordenar el reporte, no relajar reglas"


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
