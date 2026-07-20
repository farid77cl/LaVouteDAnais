# -*- coding: utf-8 -*-
"""Genera los 7 prompts V3.5 Hard-Sync (motor v3) para los looks del ARCHIVO que nunca los
tuvieron, a partir de las fichas de `fichas_archivo_l85_l199.py`.

Estos looks se registraron antes de que existiera el canon de 7 poses: quedaron con descripcion
en espanol y CERO prompts. La app los lee igual que la galeria viva (GitRepository.kt:302 filtra
por `path.contains("galeria_outfits")`), asi que sin prompts simplemente no se pueden regenerar.

El Bloque A NO se escribe a mano: se EXTRAE de un prompt v3 real de la galeria viva y se le
recalcula solo el segmento de marcas segun la cobertura del outfit. Asi es imposible que este
generador introduzca una variante del ADN distinta de la que ya esta en produccion.

Uso:  python generar_prompts_archivo.py [--apply]
"""
import re, sys, os
sys.stdout.reconfigure(encoding="utf-8")

REPO = r"c:\Users\farid\LaVouteDAnais"
sys.path.insert(0, os.path.join(REPO, "99_Sistema", "scripts"))
sys.path.insert(0, os.path.join(REPO, "99_Sistema", "scripts", "visual"))

from pose_rotation_v5 import (rotate_poses, build_marks_clause, build_negative,
                              find_forbidden, SINGLE_FRAME, SINGLE_FRAME_TAIL, SKIN_LOCK)
import refrescar_rango_v3 as R
from fichas_archivo_l85_l199 import FICHAS

GAL = os.path.join(REPO, "00_Ele", "galeria_outfits_archivo.md")
VIVA = os.path.join(REPO, "00_Ele", "galeria_outfits.md")
POSE_LABELS = ["Standing", "Back View", "Seated", "Side Profile", "Ditzy", "POV", "Odalisque"]


def plantilla_bloque_a():
    """Prefijo canonico del Bloque A tomado de un prompt v3 REAL de la galeria viva.

    Se devuelve partido en (antes_de_marcas, despues_de_marcas) usando el mismo span que
    MARKS_RE: entre 'wide hips, ' y el token de maquillaje+unas. Recalcular las marcas por
    cobertura es obligatorio — nombrar una marca que la ropa tapa es una ORDEN de pintarla
    sobre la tela (el defecto que costo meses).
    """
    texto = open(VIVA, encoding="utf-8", newline="").read()
    for m in re.finditer(r"```(.*?)```", texto, re.S):
        p = m.group(1).strip()
        if SINGLE_FRAME not in p or "5cm." not in p:
            continue
        cab = p.split("5cm.", 1)[0] + "5cm. "
        mm = R.MARKS_RE.search(cab)
        if mm:
            return cab[:mm.start(2)], cab[mm.end(2):]
    raise SystemExit("no encontre un Bloque A v3 de referencia en la galeria viva")


def construir(look, f, pre, post):
    """Devuelve (lista_de_7_prompts, negativo) para un look."""
    outfit = f["outfit"]
    flags, neg, kind, mate_risk, consistencia = R.clasificar(outfit, f.get("categoria", ""))
    marcas = build_marks_clause(**flags)
    locks = R.construir_locks(neg, kind, mate_risk, consistencia)
    neg["seam"] = f.get("seam", False) or neg["seam"]

    cabeza = pre + marcas + post + outfit + ", " + locks + ". "
    poses = rotate_poses(look,
                         seat=f.get("seat", "a sculptural bench"),
                         wall=f.get("wall", "a wall"),
                         surface=f.get("surface", "a surface"),
                         wrap_mode=f.get("wrap"),
                         seam=neg["seam"],
                         shoe_echo=f["shoe"])
    out = []
    for slot, direccion in poses:
        p = cabeza + direccion + ", " + f["setting"]
        if slot == "Ditzy":
            p += ", " + SINGLE_FRAME_TAIL
        p += ", 8k editorial fashion photography."
        out.append((slot, p))
    return out, build_negative(**neg)


def bloque_markdown(prompts, negativo):
    eol = "\r\n"
    t = [f"{eol}### 📝 Prompts V3.5 Hard-Sync{eol}"]
    for i, (slot, p) in enumerate(prompts, 1):
        t.append(f"{eol}**{i}. {slot}:**{eol}{eol}```{eol}{p}{eol}```{eol}")
    t.append(f"{eol}**Negative Prompt:** `{negativo}`{eol}")
    return "".join(t)


def main():
    apply = "--apply" in sys.argv
    pre, post = plantilla_bloque_a()
    texto = open(GAL, encoding="utf-8", newline="").read()
    partes = re.split(r"(?m)^(## .*?Look (\d+):.*)$", texto)

    salida, hechos, fallos, vistos = [partes[0]], [], [], set()
    for i in range(1, len(partes), 3):
        header, num, body = partes[i], int(partes[i + 1]), partes[i + 2]
        f = FICHAS.get(num)
        # Los duplicados (L124-L128 aparecen dos veces) se atienden UNA sola vez: la segunda
        # entrada se deja intacta y queda reportada como estructura a resolver aparte.
        if not f or num in vistos or "```" in body:
            salida += [header, body]
            continue
        vistos.add(num)

        prompts, negativo = construir(num, f, pre, post)
        malos = [s for s, p in prompts if find_forbidden(p) or SKIN_LOCK not in p
                 or SINGLE_FRAME not in p or re.search(r"\bglove", R.solo_prenda(p), re.I)]
        if malos or len(prompts) != 7:
            fallos.append((num, malos or "conteo != 7"))
            salida += [header, body]
            continue

        # Artefacto de truncado: a L172/L173 les quedo un '**1. Standing:**' huerfano pegado al
        # final de la linea de Ambientacion cuando se perdieron sus prompts.
        nuevo = re.sub(r"\s*\*\*1\.\s*Standing:\*\*", "", body)
        # Insertar ANTES del separador final del look para no romper la estructura del archivo.
        m = re.search(r"(\r?\n-{3,}\r?\n\s*)$", nuevo)
        if m:
            nuevo = nuevo[:m.start()] + "\r\n" + bloque_markdown(prompts, negativo) + m.group(1)
        else:
            nuevo = nuevo.rstrip() + "\r\n" + bloque_markdown(prompts, negativo)
        hechos.append(num)
        salida += [header, nuevo if apply else body]

    print(f"Looks con ficha: {len(FICHAS)}  |  generados: {len(hechos)}  |  fallos: {len(fallos)}")
    print(f"  generados: {sorted(hechos)}")
    sin_tocar = sorted(set(FICHAS) - set(hechos))
    if sin_tocar:
        print(f"  ⚠️ con ficha pero NO generados (ya tenian prompts o duplicados): {sin_tocar}")
    for f_ in fallos:
        print("  FALLO:", f_)
    print(f"  prompts nuevos: {len(hechos) * 7}")

    if apply:
        open(GAL, "w", encoding="utf-8", newline="").write("".join(salida))
        print(f"\n>>> APLICADO sobre {os.path.basename(GAL)}")
    else:
        print("\n>>> DRY-RUN. Reejecutar con --apply")


if __name__ == "__main__":
    main()
