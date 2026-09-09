#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""H1 — el detector de tricolones no cuenta lo que objetivamente no lo es.

Deuda declarada el 08/09/2026 («`medir_capitulo.py` sobre-cuenta ola acumulativa
como tricolon»), reproducida y acotada el 09/09.

**Reproducción:** sobre el Cap 1 de «Hora Pedida» (11.763 palabras) el detector
marca **65** tricolones. Leídos uno por uno, la mayoría no lo son: el patrón
`…, … y …` atrapa cláusulas coordinadas, olas acumulativas deliberadas, rangos
y hasta numerales.

**Alcance de este arreglo — deliberadamente angosto.** Se excluye SOLO lo que no
es tricolon *por gramática*, no por gusto:

  · **el numeral partido** — «cuarenta y un años» no es una enumeración, es un
    número; la «y» es parte de la cifra.
  · **el rango** — «entre el segundo y el tercer piso» es UNA locución
    prepositiva, no un tercer miembro.

Lo que NO se toca, y queda declarado como límite conocido: distinguir un
tricolon retórico de dos cláusulas coordinadas o de una ola acumulativa
deliberada es **criterio literario, no gramática**, y esa llamada es de la Ama y
de su Validador. El detector es «aprox. greppable» por diseño y **H1 alimenta
`blandos`, jamás `duros`** — no bloquea ningún capítulo, así que un falso
positivo cuesta ruido, nunca un rechazo.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).parent))

import medir_capitulo as M  # noqa: E402


def _hits(texto):
    # `iter_h1` es el único camino de producción: la regex cruda sigue siendo
    # amplia a propósito y el filtro gramatical vive aparte, para poder leerlo.
    return [m.group(0) for m in M.iter_h1(texto)]


# --- lo que SÍ es tricolon y tiene que seguir contándose -------------------

def test_un_tricolon_de_verdad_se_cuenta():
    # Del Cap 1 de «Hora Pedida», tres miembros paralelos con la misma preposición.
    t = "Ya me lo dijiste con el teléfono, con la comida y con la receta de tu mamá."
    assert len(_hits(t)) == 1, _hits(t)


def test_un_tricolon_de_adjetivos_se_cuenta():
    t = "Se quedó con la boca así, pintada y abierta, sin decir nada."
    assert len(_hits(t)) == 1, _hits(t)


# --- lo que objetivamente NO lo es ----------------------------------------

def test_un_numeral_partido_no_es_un_tricolon():
    """«cuarenta y un años» es una cifra, no una enumeración. Caso real del Cap 1."""
    t = "Se la sabía, cuarenta y un años, y no le hizo falta preguntar."
    assert _hits(t) == [], _hits(t)


def test_otros_numerales_tampoco():
    for t in ("Tenía veinte y tantos, nada más.",
              "Eran las siete y media, y todavía no llegaba.",
              "Le quedaban treinta y seis horas, ni una más."):
        assert _hits(t) == [], (t, _hits(t))


def test_un_rango_con_entre_no_es_un_tricolon():
    """«entre el segundo y el tercer piso» es una locución, no un tercer miembro.
    Caso real del Cap 1."""
    t = "Fue en el ascensor, entre el segundo y el tercer piso, con la puerta cerrada."
    assert _hits(t) == [], _hits(t)


def test_un_rango_de_desde_hasta_tampoco():
    t = "Lo leyó entero, desde el encabezado hasta la firma y sin levantar la vista."
    assert _hits(t) == [], _hits(t)


# --- la medición sobre el capítulo real -----------------------------------

def test_sobre_el_capitulo_real_baja_el_ruido_sin_matar_la_señal():
    cap = (Path(__file__).parent.parent.parent.parent /
           "03_Literatura" / "01_En_Progreso" / "hora_pedida" /
           "capitulo_1_el_cajon_v0.3.md")
    if not cap.exists():
        return                      # el capítulo puede haber avanzado de versión
    n = len(_hits(cap.read_text(encoding="utf-8")))
    assert n < 65, "no bajó del conteo original de 65"
    assert n > 20, "bajó tanto que probablemente se está comiendo tricolones reales"


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
