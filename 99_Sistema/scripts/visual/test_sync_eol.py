#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pruebas de regresión del escritor que preserva finales de línea.

Por qué existen (09/09/2026). `sync_imagenes_subidas.py` leía la galería en modo
texto —que traduce CRLF a LF al leer— y la escribía con el default de la
plataforma. Medido: una corrección real de **9 líneas** en los trackers de L829,
L831 y L832 salió como **42.495 inserciones y 42.495 borrados**, o sea la galería
entera reescrita por churn de EOL. Es lo que CLAUDE.md prohíbe expresamente, solo
que aquí lo producía el script y no el `git add`.

El caso difícil es que `galeria_outfits.md` está en **EOL mixto**: 42.470 líneas
CRLF y 25 con LF pelado. Normalizar a un solo terminador deja 25 líneas de ruido;
deducir "el dominante" y aplicarlo a todo, también. La única salida limpia es
alinear línea a línea y que cada línea sin cambios conserve SU terminador.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).parent))

from sync_imagenes_subidas import _escribir_preservando_eol  # noqa: E402


def _round_trip(tmp_path, original_raw, nuevo_lf):
    ruta = tmp_path / "galeria.md"
    ruta.write_bytes(original_raw.encode("utf-8"))
    _escribir_preservando_eol(str(ruta), original_raw, nuevo_lf)
    return ruta.read_bytes()


def test_sin_cambios_el_archivo_queda_byte_a_byte_igual(tmp_path):
    original = "a\r\nb\r\nc\r\n"
    assert _round_trip(tmp_path, original, "a\nb\nc\n") == original.encode("utf-8")


def test_una_linea_cambiada_no_toca_el_eol_de_las_otras(tmp_path):
    original = "a\r\nb\r\nc\r\n"
    assert _round_trip(tmp_path, original, "a\nB\nc\n") == b"a\r\nB\r\nc\r\n"


def test_eol_mixto_conserva_la_linea_con_lf_pelado(tmp_path):
    # El caso real de galeria_outfits.md: mayoría CRLF, unas pocas líneas con LF.
    original = "a\r\nb\nc\r\n"
    assert _round_trip(tmp_path, original, "a\nb\nC\n") == b"a\r\nb\nC\r\n"


def test_archivo_en_lf_puro_se_queda_en_lf(tmp_path):
    original = "a\nb\nc\n"
    assert _round_trip(tmp_path, original, "a\nB\nc\n") == b"a\nB\nc\n"


def test_linea_insertada_toma_el_terminador_dominante(tmp_path):
    original = "a\r\nb\r\n"
    assert _round_trip(tmp_path, original, "a\nnueva\nb\n") == b"a\r\nnueva\r\nb\r\n"


def test_linea_borrada_no_arrastra_a_sus_vecinas(tmp_path):
    original = "a\r\nb\r\nc\r\n"
    assert _round_trip(tmp_path, original, "a\nc\n") == b"a\r\nc\r\n"


def test_preserva_acentos_y_emojis(tmp_path):
    original = "### 📸 Imágenes (0/7 — Pendiente)\r\nLencería\r\n"
    esperado = "### 📸 Imágenes (7/7 — Materializado)\r\nLencería\r\n"
    nuevo = "### 📸 Imágenes (7/7 — Materializado)\nLencería\n"
    assert _round_trip(tmp_path, original, nuevo) == esperado.encode("utf-8")


def _correr():
    """Runner propio: este repo no tiene pytest instalado en toda maquina."""
    import tempfile, traceback
    pruebas = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    ok = fallas = 0
    for fn in pruebas:
        with tempfile.TemporaryDirectory() as d:
            try:
                fn(Path(d))
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
