#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""`outfit.py ojos` — el paquete de auditoría imagen↔prompt.

Por qué existe (09/09/2026). Medido ese día: **ningún auditor del motor abre un
PNG**. Los 124 tests, `lint_galeria`, `cruce`, `auditar_canon_flota`,
`modularidad` y `lint_prompts_personaje` miden TEXTO; los únicos tres scripts
del repo que importan PIL son de portadas, Bluesky y Tumblr. Por eso los
instrumentos decían LIMPIA mientras la Ama veía fotos malas: no mentían,
**miraban el otro extremo del tubo**.

La auditoría de ese día necesitó seis agentes externos, y **la mitad del costo
fue preparar el material**: extraer los prompts, factorizar el bloque que las 7
poses comparten por diseño, emparejar con las imágenes reales. Eso bajó cada
look de ~70.000 a ~19.000 caracteres — **70 % menos**. Hecho a mano no se
repite; hecho comando, sí.

Este módulo NO juzga imágenes (eso necesita ojos de verdad). Arma el paquete
para que quien juzgue gaste su presupuesto en mirar, no en preparar.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).parent))

import os as _os
# Una batería ejercita el motor con FIXTURES: su rastro no es historial del
# motor y no puede ensuciar `99_Sistema/logs/outfit_engine.jsonl`, que está
# trackeado (09/09/2026). Se apaga ANTES de importar el motor.
_os.environ.setdefault("OUTFIT_ENGINE_LOG", "0")


import ojos  # noqa: E402


# ------------------------------------------------- condensar: el 70 % ---

def test_condensar_factoriza_el_prefijo_compartido():
    prompts = {"standing": "ADN COMUN. de pie, mirando al lente",
               "seated": "ADN COMUN. sentada, mirando abajo"}
    r = ojos.condensar(prompts)
    assert r["comun"] == "ADN COMUN. "
    assert r["unico"]["standing"] == "de pie, mirando al lente"
    assert r["unico"]["seated"] == "sentada, mirando abajo"


def test_condensar_factoriza_tambien_el_sufijo_compartido():
    prompts = {"standing": "ADN. de pie. FIN COMUN",
               "seated": "ADN. sentada. FIN COMUN"}
    r = ojos.condensar(prompts)
    # El sufijo real es ". FIN COMUN": el punto TAMBIÉN se comparte, y sacarlo
    # rompería la reconstrucción. La expectativa correcta es que la cola
    # compartida salga del texto único, no que empiece en una palabra concreta.
    assert r["sufijo"].endswith("FIN COMUN")
    assert "FIN COMUN" not in r["unico"]["standing"]
    assert r["unico"]["standing"].strip() == "de pie"


def test_condensar_con_una_sola_pose_no_inventa_bloque_comun():
    """El L89 de Anaïs llegó 1/7. Un `condensar` ingenuo declararía el prompt
    entero como «bloque común» y el auditor no vería nada que juzgar."""
    r = ojos.condensar({"standing": "texto único"})
    assert r["comun"] == ""
    assert r["sufijo"] == ""
    assert r["unico"]["standing"] == "texto único"


def test_condensar_no_pierde_ni_un_caracter():
    """Guardia dura: comun + unico + sufijo tiene que reconstruir el original.
    Un condensador que se coma texto le miente al auditor sobre lo que se pidió."""
    prompts = {"standing": "ADN COMUN. de pie, al lente. FIN",
               "seated": "ADN COMUN. sentada, abajo. FIN",
               "pov": "ADN COMUN. retrato cerrado. FIN"}
    r = ojos.condensar(prompts)
    for pose, original in prompts.items():
        assert r["comun"] + r["unico"][pose] + r["sufijo"] == original, pose


def test_condensar_reporta_cuanto_ahorro():
    prompts = {"a": "X" * 900 + "uno", "b": "X" * 900 + "dos"}
    r = ojos.condensar(prompts)
    assert r["ahorro_pct"] > 40, r["ahorro_pct"]
    assert r["chars_original"] > r["chars_condensado"]


def test_condensar_sin_prompts_no_revienta():
    r = ojos.condensar({})
    assert r["unico"] == {} and r["comun"] == "" and r["chars_original"] == 0


# ------------------------------------- el paquete contra la flota real ---

def test_poses_reales_lee_el_indice_de_git_no_el_disco():
    """Medido dos veces en este repo (H7 del lint con 3.594 links falsos, y la
    auditoría de PNG): leer el disco en un clon sparse miente. La fuente es
    `git ls-files`."""
    reales = ojos.poses_reales("ele", 832)
    # La llave es la CANÓNICA de `galeria_parser.POSES_CANON` — la quinta pose
    # es `slot5` y no «ditzy», porque cada muñeca la llama distinto (Ditzy /
    # Glacial Command / Sovereign Gaze) y así la misma toma se compara entre las
    # tres. Corregido tras leer la firma real del dueño en vez de suponerla.
    import galeria_parser
    assert set(reales) == set(galeria_parser.POSES_CANON), sorted(reales)
    assert reales["standing"].endswith("ele_832_standing.png")
    assert reales["slot5"].endswith("ele_832_ditzy.png")


def test_poses_reales_de_un_look_sin_imagenes_devuelve_vacio():
    assert ojos.poses_reales("ele", 828) == {}


def test_paquete_trae_prompts_imagenes_y_el_desajuste_del_tracker():
    """El L832 estaba 7/7 real con el tracker diciendo «0/7 — Pendiente»
    esta misma mañana: el paquete tiene que mostrar los dos números."""
    p = ojos.paquete("ele", 832)
    assert p["slug"] == "ele" and p["look"] == 832
    assert len(p["prompts"]) == 7
    assert len(p["imagenes"]) == 7
    assert p["tracker_declarado"] is not None
    assert p["condensado"]["ahorro_pct"] > 50


def test_paquete_de_un_look_inexistente_lo_dice_con_nombre():
    try:
        ojos.paquete("ele", 99999)
        assert False, "un look que no está en la galería no puede pasar en silencio"
    except ojos.LookNoEncontrado as e:
        assert "99999" in str(e) and "ele" in str(e)


def test_render_no_repite_el_bloque_comun_por_pose():
    """El ahorro es el punto: el bloque común se imprime UNA vez."""
    texto = ojos.render(ojos.paquete("ele", 832))
    comun = ojos.paquete("ele", 832)["condensado"]["comun"]
    assert len(comun) > 500, "el fixture depende de un ADN real largo"
    assert texto.count(comun[:200]) == 1, texto.count(comun[:200])


def test_render_nombra_cada_pose_con_su_archivo_real():
    texto = ojos.render(ojos.paquete("ele", 832))
    assert "ele_832_back_view.png" in texto
    for pose in ("standing", "back_view", "odalisque"):
        assert pose in texto


# ---------------------------------------------- el subcomando de la CLI ---

def _cli(*args):
    import subprocess, sys, os
    aqui = os.path.dirname(os.path.abspath(__file__))
    return subprocess.run([sys.executable, os.path.join(aqui, "outfit.py"), "ojos", *args],
                          capture_output=True, text=True, encoding="utf-8",
                          cwd=os.path.normpath(os.path.join(aqui, "..", "..", "..")))


def test_cli_ojos_emite_el_paquete_de_un_look():
    r = _cli("ele", "832")
    assert r.returncode == 0, (r.stdout[-800:], r.stderr[-800:])
    assert "AUDITORÍA IMAGEN↔PROMPT" in r.stdout
    assert "ele_832_back_view.png" in r.stdout
    assert "% menos" in r.stdout


def test_cli_ojos_sin_argumentos_explica_como_se_usa():
    r = _cli()
    assert r.returncode == 2
    assert "ojos" in r.stdout and "<slug>" in r.stdout


def test_cli_ojos_con_un_look_inexistente_no_revienta_con_traceback():
    r = _cli("ele", "99999")
    assert r.returncode == 1
    assert "Traceback" not in r.stderr, r.stderr[-500:]
    assert "99999" in r.stdout


def test_cli_ojos_escribe_a_archivo_con_out():
    import tempfile, os
    with tempfile.TemporaryDirectory() as d:
        destino = os.path.join(d, "paquete.md")
        r = _cli("ele", "832", "--out", destino)
        assert r.returncode == 0, r.stderr[-500:]
        assert os.path.exists(destino)
        assert "AUDITORÍA IMAGEN↔PROMPT" in open(destino, encoding="utf-8").read()


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
