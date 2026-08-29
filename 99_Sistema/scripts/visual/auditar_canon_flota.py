#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
auditar_canon_flota.py — Corre el canon de calzado y de vestuario sobre la FLOTA REAL.

POR QUE EXISTE (auditoria 29/08/2026, hallazgo F-03)
----------------------------------------------------
`footwear_canon.py` y `garment_canon.py` estan documentados en CLAUDE.md como
auditorias de la flota ("stiletto/Pleaser rule **across looks**", "garment-token
consistency"). Medido: **ninguno de los dos abre un solo archivo**. Son la funcion
validadora mas su self-test con casos inventados a mano (L734, L737, L746,
L791-negviejo...). Nunca miraron una galeria.

Consecuencia real: el 28/08/2026 el Look 812 se materializo con un `mule` sin
plataforma — violacion de la directiva del 09/07 que `footwear_canon.audit_footwear`
detecta perfectamente. La pillo un ojo humano leyendo el markdown, no el auditor,
porque al auditor nadie le paso nunca el look.

Este script es el cable que faltaba: parsea las tres galerias y le entrega los
looks reales a esas mismas funciones. No reimplementa el canon — lo consume.

EL RIESGO QUE ESQUIVA: el clasificador se lee a si mismo
-------------------------------------------------------
No se le puede pasar el prompt entero al auditor. Las anclas del propio prompt
nombran `flats, block heels, wedges` (FOOTWEAR_ECHO), `bikini bottom`, `thong`,
`bodysuit`, `leotard` (BOTTOM_CUT_LOCK) — el auditor leeria SU PROPIA defensa como
si fuera el outfit y marcaria violaciones inexistentes. Es el error registrado en
auto-memoria `feedback_clasificador_se_lee_a_si_mismo` (19/07/2026), donde los
locks v3 re-leidos dispararon `navel_bare` en 203 looks vestidos.

Por eso se extrae el SEGMENTO DE OUTFIT acotado: lo que va entre el final del
BLOQUE A (ADN) y el comienzo de la primera ancla. Un look cuyo segmento no se
puede acotar con seguridad se reporta como NO AUDITABLE — nunca se audita a medias.

USO
---
    python 99_Sistema/scripts/visual/auditar_canon_flota.py                # las tres
    python 99_Sistema/scripts/visual/auditar_canon_flota.py ele            # una
    python 99_Sistema/scripts/visual/auditar_canon_flota.py --solo-sin-imagen
    python 99_Sistema/scripts/visual/auditar_canon_flota.py --detalle
"""
import io
import os
import re
import subprocess
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", ".."))
sys.path.insert(0, AQUI)

import lint_prompts_personaje as L  # noqa: E402
from footwear_canon import audit_footwear  # noqa: E402
from garment_canon import audit_garment  # noqa: E402
from prompt_builder import PromptBuilder, cargar_config  # noqa: E402

# Cierre del BLOQUE A. El ADN de las tres muñecas termina en la clausula de uñas;
# el punto que la sigue es el unico separador fiable entre ADN y outfit.
# Las tres muñecas cierran su ADN con la clausula de uñas, pero la escriben
# distinto: Ele en centimetros ("French XXXL nails ... 5cm."), Miss Doll y Anais
# con peso de enfasis ("manicured long glossy nails:1."). La primera version de
# esta regex solo aceptaba centimetros y dejaba 122 de sus 130 looks sin auditar.
RX_FIN_ADN = re.compile(r"\bnails\b[^.]{0,90}?(?::\d(?:\.\d)?)?\.\s+", re.I)

# Comienzo del bloque de anclas: la primera que aparece cierra el outfit.
# Se toman los primeros 40 chars de cada ancla del contrato, mas los arranques
# historicos de la flota vieja de Ele.
ARRANQUES_HISTORICOS = (
    "a single continuous photograph",
    "anatomically correct with exactly two arms",
    "a real photograph taken with a real camera",
    "the outfit is exactly ONE garment ensemble",
)


def _prefijos_ancla(cfg):
    p = [a["texto"][:40] for a in cfg["anclas"].values()]
    return sorted(set(p) | set(ARRANQUES_HISTORICOS), key=len, reverse=True)


def segmento_outfit(prompt, prefijos):
    """Devuelve (outfit, motivo_si_no_auditable).

    El outfit es lo que queda entre el final del ADN y la primera ancla. Si no se
    puede acotar por los dos lados, se devuelve None: auditar el prompt completo
    haria que el auditor leyera sus propias anclas como si fueran la prenda.
    """
    m = RX_FIN_ADN.search(prompt)
    if not m:
        return None, "no se ubica el cierre del BLOQUE A"
    ini = m.end()
    cortes = [prompt.find(p, ini) for p in prefijos]
    cortes = [c for c in cortes if c > ini]
    if not cortes:
        return None, "no se ubica el comienzo de las anclas"
    seg = prompt[ini:min(cortes)].strip()
    if len(seg) < 40:
        return None, "segmento de outfit demasiado corto (%d chars)" % len(seg)
    return seg, None


def poses_con_imagen(slug):
    out = subprocess.run(["git", "ls-files", "05_Imagenes"], cwd=RAIZ,
                         capture_output=True, text=True, encoding="utf-8").stdout
    rx = re.compile(r"(^|/)%s_0*(\d+)_[a-z_]+\.(png|jpg)$" % slug, re.I)
    nums = set()
    for f in out.split("\n"):
        m = rx.search(f.strip())
        if m:
            nums.add(int(m.group(2)))
    return nums


def auditar(slug, cfg, solo_sin_imagen=False, detalle=False):
    pb = PromptBuilder(slug, cfg)
    ruta = os.path.join(RAIZ, pb.perfil["galeria"].replace("/", os.sep))
    if not os.path.exists(ruta):
        print("  [CRITICO] no existe la galeria %s" % pb.perfil["galeria"])
        return 0, 0, 0
    texto = open(ruta, encoding="utf-8").read()
    arquetipos = L.extraer_arquetipos(texto)
    looks = L.parse_como_la_app(texto, pb.perfil.get("slot5") or "Ditzy")
    prefijos = _prefijos_ancla(cfg)
    materializados = poses_con_imagen(slug) if solo_sin_imagen else set()

    violaciones, auditados, no_auditables = [], 0, []
    for lk in looks:
        if solo_sin_imagen and lk["num"] in materializados:
            continue
        # Un look = un outfit: basta el primer prompt que se pueda acotar.
        seg = None
        for _pose, txts in lk["prompts"].items():
            for t in txts:
                seg, motivo = segmento_outfit(t, prefijos)
                if seg:
                    break
            if seg:
                break
        if not seg:
            no_auditables.append((lk["num"], motivo))
            continue
        auditados += 1
        arq = arquetipos.get(lk["num"], "")
        tag = "L%d" % lk["num"]
        for p in audit_footwear(seg, garments=seg, archetype=arq, tag=tag):
            violaciones.append(("calzado", lk["num"], p))
        for p in audit_garment(seg, archetype=arq, tag=tag):
            violaciones.append(("vestuario", lk["num"], p))

    print("  %-10s looks=%-4d auditados=%-4d no auditables=%-4d VIOLACIONES=%d"
          % (slug, len(looks), auditados, len(no_auditables), len(violaciones)))
    if violaciones:
        porluk = {}
        for fam, num, p in violaciones:
            porluk.setdefault(num, []).append((fam, p))
        for num in sorted(porluk):
            if detalle:
                print("     L%d:" % num)
                for fam, p in porluk[num]:
                    print("        [%s] %s" % (fam, p))
            else:
                print("     L%-5d %s" % (num, "; ".join(p.split(":")[0] for _f, p in porluk[num])[:150]))
    if no_auditables and detalle:
        print("     no auditables: %s" % sorted(n for n, _ in no_auditables)[:30])
    return auditados, len(violaciones), len(no_auditables)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    solo_sin_imagen = "--solo-sin-imagen" in sys.argv
    detalle = "--detalle" in sys.argv
    slugs = args or ["ele", "miss_doll", "anais"]
    cfg = cargar_config()
    print("=" * 78)
    print("CANON DE CALZADO Y VESTUARIO SOBRE LA FLOTA REAL")
    print("  alcance: %s" % ("solo looks SIN imagen (riesgo vivo)" if solo_sin_imagen
                             else "toda la galeria"))
    print("=" * 78)
    ta = tv = tn = 0
    for slug in slugs:
        a, v, n = auditar(slug, cfg, solo_sin_imagen, detalle)
        ta += a
        tv += v
        tn += n
    print("-" * 78)
    print("TOTAL  auditados=%d  violaciones=%d  no auditables=%d" % (ta, tv, tn))
    print("-" * 78)
    return 1 if tv else 0


if __name__ == "__main__":
    sys.exit(main())
