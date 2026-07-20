# -*- coding: utf-8 -*-
"""Inyector del CANDADO DE ESCOTE ALTO (Ama 20/07/2026).

Orden de la Ama viendo la Ditzy del L88: "trata de que ese efecto del escote sea recurrente".
El efecto que le gusta: borde estructurado BAJO + las dos esferas sentadas muy altas y llenas
por encima del filo. Salia por azar porque el Bloque A fija el implante pero nunca la RELACION
prenda-busto.

Alcance deliberado (regla de 09-estado-materializacion.md): **solo poses SIN imagen**.
Las que ya tienen imagen NO se tocan — su render ya paso el filtro de la Ama.

Uso:
    python 99_Sistema/scripts/inyectar_escote_alto.py            # dry-run (reporta, no escribe)
    python 99_Sistema/scripts/inyectar_escote_alto.py --apply    # escribe
"""
import io
import os
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

REPO = r"C:\Users\farid\LaVouteDAnais"
GALERIAS = [
    os.path.join(REPO, "00_Ele", "galeria_outfits.md"),
    os.path.join(REPO, "00_Ele", "galeria_outfits_archivo.md"),
]

sys.path.insert(0, os.path.join(REPO, "99_Sistema", "scripts", "visual"))
from pose_rotation_v5 import CORSET_BUST_LOCK  # noqa: E402

# Siluetas que sostienen el efecto: no solo el corse. El escote estructurado bajo funciona
# igual en bustier, sweetheart, strapless, plunge y bodysuit de copa armada (visto en el
# L566 sweetheart dorado y en el L86, cuya blusa tensada da el mismo resultado).
NECKLINE_KW = [
    "corset", "overbust", "underbust", "under-bust", "bustier", "basque", "corselette",
    "merry widow", "waist cincher", "corseted",
    "sweetheart", "strapless", "bandeau", "plunge", "plunging", "balconette", "demi-cup",
    "structured cup", "moulded cup", "molded cup", "push-up", "bralette", "underwire",
]

MARCA = "rest very high, full and rounded above"  # firma del candado (idempotencia)

# El candado se pega al final de la clausula de vestuario, justo antes del SKIN_LOCK.
ANCLA_SKIN_LOCK = ", wherever the garment covers"


def looks_con_imagen():
    """Devuelve el set de numeros de look que ya tienen al menos un PNG en git."""
    out = subprocess.run(
        ["git", "ls-files", "05_Imagenes"], cwd=REPO,
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    ).stdout
    nums = set()
    for line in out.splitlines():
        if not line.lower().endswith(".png"):
            continue
        m = re.search(r"/look0*(\d+)[_/]", line)
        if m:
            nums.add(int(m.group(1)))
    return nums


def procesar(path, con_imagen, apply):
    with io.open(path, "r", encoding="utf-8", newline="") as fh:
        txt = fh.read()

    # partir por look conservando el texto exacto
    partes = re.split(r"(^## .*?Look (\d+)[:\s].*?$)", txt, flags=re.M)
    salida = [partes[0]]
    tocados, saltados_img, sin_silueta, ya_tenia = [], [], [], []

    for i in range(1, len(partes), 3):
        header, num, cuerpo = partes[i], int(partes[i + 1]), partes[i + 2]

        if num in con_imagen:
            saltados_img.append(num)
            salida.extend([header, str(num) and "", cuerpo][::2] if False else [header, cuerpo])
            continue

        # aplicar sobre cada clausula de vestuario del look (una por pose)
        def repl(m):
            clausula = m.group(1)
            if MARCA in clausula:
                return m.group(0)
            if not any(k in clausula.lower() for k in NECKLINE_KW):
                return m.group(0)
            return ". " + clausula.rstrip().rstrip(",") + ", " + CORSET_BUST_LOCK + ANCLA_SKIN_LOCK

        nuevo, n = re.subn(
            r"\. ((?:a|an) .*?)" + re.escape(ANCLA_SKIN_LOCK),
            repl, cuerpo, flags=re.S,
        )
        if nuevo != cuerpo:
            tocados.append((num, n))
        elif any(k in cuerpo.lower() for k in NECKLINE_KW) and MARCA in cuerpo:
            ya_tenia.append(num)
        else:
            sin_silueta.append(num)
        salida.extend([header, nuevo])

    final = "".join(salida)

    if apply and final != txt:
        with io.open(path, "w", encoding="utf-8", newline="") as fh:
            fh.write(final)

    return final, txt, tocados, saltados_img, sin_silueta, ya_tenia


def main():
    apply = "--apply" in sys.argv
    con_imagen = looks_con_imagen()
    print(f"looks con al menos una imagen en git: {len(con_imagen)}  (NO se tocan)")
    print()
    total_looks = total_poses = 0
    for path in GALERIAS:
        final, txt, tocados, img, sinsil, ya = procesar(path, con_imagen, apply)
        nom = os.path.basename(path)
        poses = sum(n for _, n in tocados)
        total_looks += len(tocados)
        total_poses += poses
        print(f"=== {nom} ===")
        print(f"  looks con escote estructurado SIN imagen y sin candado: {len(tocados)}")
        print(f"  poses inyectadas                                      : {poses}")
        print(f"  looks saltados por tener imagen                       : {len(img)}")
        print(f"  looks sin silueta de escote                           : {len(sinsil)}")
        if tocados:
            print(f"  -> {[n for n, _ in tocados][:40]}")
        # guardia: el archivo no debe perder tamano
        if len(final) < len(txt):
            print("  !! ABORTA: el resultado es MAS CORTO que el original")
            sys.exit(1)
        print()
    print(f"TOTAL: {total_looks} looks · {total_poses} poses  "
          f"({'ESCRITO' if apply else 'DRY-RUN, nada escrito'})")


if __name__ == "__main__":
    main()
