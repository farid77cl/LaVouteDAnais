#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
auditar_cruce_batches.py — el auditor CRUZADO: entre muñecas y entre batches.

POR QUE EXISTE (Ama 05/09/2026)
-------------------------------
    "vi los promps con la colorimetria nueva, perfectos, pero estas repitiendo
     los mismos colores muy seguido, a miss doll le diste el mismo outfit con
     colores distintos. y a las 3 les diste el mismo outfit."

Tenia razon en los tres cargos, y **ninguno de los auditores existentes los vio**.
Medido el mismo dia sobre el batch de colorimetria (Ele L818-L822 · Miss Doll
L76-L80 · Anais L76-L80), con todo en verde:

    outfit.py auditar      -> 0 violaciones en miss_doll y anais
    outfit.py adn          -> LIMPIO
    outfit.py modularidad  -> LIMPIA
    outfit.py lint (x3)    -> CRITICOS: 0

...y sin embargo habia 5 pares de looks con arquitectura de prenda IDENTICA
entre muñecas distintas, con hasta 39 n-gramas de 8 palabras clonados verbatim
(Miss Doll L78 <-> Anais L80, corseteria; Miss Doll L80 <-> Anais L79, slip de
malla, con la clausula "the mesh transparent enough that the lingerie beneath
reads clearly from every angle including from behind" copiada tal cual).

LA CAUSA, Y POR QUE NO ERA UN DESCUIDO
--------------------------------------
Las dos reglas que gobiernan la silueta miran donde el defecto no estaba:

1. **`rotacion_prenda` (chequeo 12 del lint) es PER-PERSONAJE.** Compara a Ele
   con Ele. Nada en el motor compara a Ele con Anais — asi que tres muñecas
   pueden salir con el mismo corset el mismo dia y las tres pasan limpias.
2. **Su `ventana_global` es de 3 looks, y los batches son de 5.** Miss Doll
   repitio 4 de sus 5 arquitecturas del batch inmediatamente anterior
   (L71 falda <-> L77 falda · L72 corset <-> L78 corset · L73 bikini <-> L79
   bikini · L75 vestido <-> L80 vestido). Todas a distancia 5-6: fuera de la
   ventana, invisibles. Eso es exactamente "el mismo outfit con colores
   distintos" que ella leyo a ojo.

Mismo patron que ya esta escrito en CLAUDE.md: `modularidad` reportaba LIMPIA
mientras Ele tenia 630 poses sin numerar. **Un chequeo verde solo prueba que
miro donde miro.**

QUE MIDE (y que NO)
-------------------
    X1  arquitectura de prenda identica ENTRE muñecas distintas
    X2  clausulas clonadas verbatim (n-gramas de >=8 palabras) entre muñecas
    X3  familia cromatica repetida dentro de un mismo batch
    X4  arquitectura repetida contra el batch ANTERIOR del mismo personaje
        (el hueco que la ventana de 3 no alcanza)

NO mide si el look es lindo, ni si el color le queda bien a la muñeca: eso es
la colorimetria de §5.2b/§5.2c de cada perfil y lo decide la Ama. Esto mide
REPETICION, que es lo unico que una maquina puede contar.

Reutiliza `clasificar_arquitectura` de lint_prompts_personaje y la taxonomia
`arquitecturas_de_prenda` de anclas_universales.json — a proposito: un segundo
clasificador con criterio propio es como nacio el problema de auditar la misma
galeria dos veces con reglas incompatibles.

USO
---
    python 99_Sistema/scripts/visual/auditar_cruce_batches.py
    python 99_Sistema/scripts/visual/auditar_cruce_batches.py --batches L818_L822_eco_de_iris MD_L76_L80_eco_de_iris AN_L76_L80_eco_de_iris
    python 99_Sistema/scripts/visual/auditar_cruce_batches.py --desde 2026-09-04   # por fecha del batch
    python 99_Sistema/scripts/visual/auditar_cruce_batches.py --verbose

Salida: exit 1 si hay algun hallazgo 🔴 (bloquea el batch), 0 si esta limpio.
"""

import io
import itertools
import json
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", ".."))
sys.path.insert(0, AQUI)

from color_canon import audit_rotacion_familia, detect_dominant, familia_de  # noqa: E402
from lint_prompts_personaje import clasificar_arquitectura  # noqa: E402
from prompt_builder import cargar_config  # noqa: E402

BATCHES = os.path.join(AQUI, "batches")

# ⚠️ La taxonomia de familias cromaticas NO vive aca: es `color_canon.FAMILY`,
# su dueño unico, y de ahi salen `detect_dominant` y `familia_de`. La primera
# version de este archivo (05/09/2026, mismo dia) traia su propia tabla de
# familias — o sea el mismo error que este auditor existe para cazar: dos
# criterios distintos midiendo lo mismo. Corregido antes de commitear.

UMBRAL_LEXICO_ROJO = 45.0     # % de lexico compartido -> 🔴
UMBRAL_LEXICO_NARANJA = 35.0
NGRAMA = 8                    # palabras seguidas para llamarlo "verbatim"


def cargar_batches(nombres=None, desde=None):
    """Devuelve [(archivo, dict)] ordenados por rango."""
    salida = []
    for f in sorted(os.listdir(BATCHES)):
        if not f.endswith(".json"):
            continue
        base = f[:-5]
        if nombres and base not in nombres:
            continue
        try:
            j = json.loads(open(os.path.join(BATCHES, f), encoding="utf-8").read())
        except Exception as e:                                    # pragma: no cover
            print("  [!] no se pudo leer %s: %s" % (f, e))
            continue
        if desde and (j.get("fecha", "") or "") < desde:
            continue
        salida.append((base, j))
    return salida


def familia_del_look(bloque_b):
    """Familia cromatica dominante de un BLOQUE B, via color_canon (dueño unico)."""
    dom = detect_dominant(bloque_b)
    return familia_de(dom) if dom else None


def palabras(t):
    return re.findall(r"[a-z]{4,}", t.lower())


def ngramas(t, n=NGRAMA):
    w = re.findall(r"[a-z]+", t.lower())
    return {" ".join(w[i:i + n]) for i in range(len(w) - n + 1)}


def similitud(a, b):
    wa, wb = set(palabras(a)), set(palabras(b))
    return 100.0 * len(wa & wb) / len(wa | wb) if wa | wb else 0.0


def main(argv):
    nombres = None
    desde = None
    verbose = "--verbose" in argv
    if "--batches" in argv:
        i = argv.index("--batches")
        nombres = [a for a in argv[i + 1:] if not a.startswith("--")]
    if "--desde" in argv:
        desde = argv[argv.index("--desde") + 1]

    cfg = cargar_config()
    tax = cfg.get("arquitecturas_de_prenda")
    lote = cargar_batches(nombres, desde)
    if not lote:
        print("no hay batches que auditar (revisa --batches / --desde)")
        return 2

    # ---- indexar todos los looks -------------------------------------------
    looks = []   # (personaje, batch, num, titulo, bloque_b, arq, familia)
    for base, j in lote:
        pj = j.get("personaje", "?")
        for num, lk in sorted(j.get("looks", {}).items(), key=lambda kv: int(kv[0])):
            b = lk.get("bloque_b", "")
            cod, _cub, _av = clasificar_arquitectura(b, tax) if tax else (None, None, None)
            looks.append((pj, base, num, lk.get("titulo", ""), b, cod, familia_del_look(b)))

    print("=" * 78)
    print("🔀 AUDITOR CRUZADO — %d looks de %d batches" % (len(looks), len(lote)))
    print("   batches: " + ", ".join(b for b, _ in lote))
    print("=" * 78)

    rojos, avisos = [], []

    # ---- X1 / X2 : cruce entre muñecas -------------------------------------
    print("\nX1 · ARQUITECTURA DE PRENDA IDENTICA ENTRE MUÑECAS DISTINTAS")
    pares = 0
    for a, b in itertools.combinations(looks, 2):
        if a[0] == b[0]:
            continue                                  # solo cruzado
        if not a[5] or not b[5] or a[5] != b[5]:
            continue
        pares += 1
        sim = similitud(a[4], b[4])
        com = ngramas(a[4]) & ngramas(b[4])
        et = "%s L%s" % (a[0], a[2]), "%s L%s" % (b[0], b[2])
        msg = ("%-14s ↔ %-14s  arquitectura %s · %.1f%% de léxico común · %d n-gramas de %d palabras verbatim"
               % (et[0], et[1], a[5], sim, len(com), NGRAMA))
        if sim >= UMBRAL_LEXICO_ROJO or len(com) >= 20:
            rojos.append(("X1", msg))
            print("   🔴 " + msg)
            if verbose and com:
                for g in sorted(com, key=len, reverse=True)[:2]:
                    print("        «...%s...»" % g)
        elif sim >= UMBRAL_LEXICO_NARANJA:
            avisos.append(("X1", msg))
            print("   🟠 " + msg)
        elif verbose:
            print("   🟡 " + msg)
    if not pares:
        print("   ✅ ninguna arquitectura compartida entre muñecas")

    # ---- X3 : tope de familia cromatica (Ama 05/09/2026) --------------------
    # "hay libertad de color, pero con la colorimetria ahora se limito, pero no
    #  puedo tener 3 outfit con el mismo color, asi que dale balance y
    #  restricciones". El tope y la ventana viven en `rotacion_color` de cada
    #  personaje (anclas_universales.json) — aca solo se aplican.
    # (!) La ventana es RODANTE POR PERSONAJE, no por batch (corregido 05/09/2026,
    # segunda pasada del mismo dia). Calculada batch por batch, una ventana de 5
    # nunca cruza el borde entre lotes -- y ahi vivia justo lo que la Ama vio: su
    # Anais L80 (aubergine) y su L84 (ciruela) estan a CUATRO looks, los dos
    # 'purple', y salieron limpios porque el L80 cerraba un batch y el L84 abria
    # el siguiente. Misma ceguera de ALCANCE que la ventana de silueta atada al
    # arquetipo: la regla estaba bien, su recorte la dejaba mirando al lado
    # equivocado. Se conserva el detalle por batch, que es como se leen.
    print("\nX3 . TOPE DE FAMILIA CROMATICA (ventana RODANTE por personaje, cruza batches)")
    perfiles = cfg.get("personajes", {})
    por_pj_c = {}
    for l in looks:
        por_pj_c.setdefault(l[0], []).append(l)
    for pj, ls in sorted(por_pj_c.items()):
        ls = sorted(ls, key=lambda x: int(x[2]))
        rot = (perfiles.get(pj) or {}).get("rotacion_color")
        duros_c, avisos_c = audit_rotacion_familia(
            [{"look": l[2], "garment": l[4]} for l in ls], rot)
        for d in duros_c:
            rojos.append(("X3", "%s . %s" % (pj, d)))
            print("   🔴 %s . %s" % (pj, d))
        for a in avisos_c:
            avisos.append(("X3", "%s . %s" % (pj, a)))
            print("   🟠 %s . %s" % (pj, a))
        if not duros_c and not avisos_c:
            print("   ✅ %s: sin colision de familia en la ventana rodante" % pj)
        for base, _j in lote:
            deste = [l for l in ls if l[1] == base]
            if deste:
                print("      %s -> %s" % (base, " . ".join("L%s=%s" % (l[2], l[6] or "?")
                                                           for l in deste)))
        if not rot:
            print("      ⚠️  %s no declara `rotacion_color` en anclas_universales.json" % pj)

    # ---- X4 : arquitectura repetida contra el batch anterior del personaje --
    print("\nX4 · ARQUITECTURA REPETIDA CONTRA EL BATCH ANTERIOR DEL MISMO PERSONAJE")
    por_pj = {}
    for l in looks:
        por_pj.setdefault(l[0], []).append(l)
    hubo = False
    for pj, ls in sorted(por_pj.items()):
        ls = sorted(ls, key=lambda x: int(x[2]))
        batches_pj = []
        for l in ls:
            if not batches_pj or batches_pj[-1][0] != l[1]:
                batches_pj.append((l[1], []))
            batches_pj[-1][1].append(l)
        for (b_ant, ant), (b_nue, nue) in zip(batches_pj, batches_pj[1:]):
            arq_ant = {l[5]: l[2] for l in ant if l[5]}
            repetidas = [(l[2], l[5], arq_ant[l[5]]) for l in nue if l[5] and l[5] in arq_ant]
            if repetidas:
                hubo = True
                msg = ("%s · %s repite %d de %d arquitecturas de %s: %s"
                       % (pj, b_nue, len(repetidas), len(nue), b_ant,
                          ", ".join("L%s=%s (ya en L%s)" % (n, a, v) for n, a, v in repetidas)))
                # 🔴 DESDE EL 05/09/2026: UNA sola repeticion contra el batch
                # inmediatamente anterior ya es dura. Antes el umbral era >=3 y dos
                # repeticiones salian 🟠 -- que es exactamente lo que paso con
                # AN_L81_L85 (L84 repetia el L78, L85 repetia el L77): el auditor
                # AVISO, y la excusa quedo escrita dentro del propio batch ("fuera
                # de la ventana de 3 y en registro opuesto"). La Ama lo vio en la
                # primera imagen. Un aviso que se puede argumentar no es un control,
                # y el batch anterior es lo ultimo que ella tiene en el ojo: ahi la
                # vara es cero.
                #
                # `cross_batch_desde_look` evita el grito retroactivo: los lotes ya
                # materializados quedan en 🟠 HISTORICO, porque rediseñarlos no es
                # posible y un linter que grita lo inarreglable enseña a ignorarlo.
                rotp = (cfg.get("personajes", {}).get(pj) or {}).get("rotacion_prenda") or {}
                desde = rotp.get("cross_batch_desde_look")
                vivo = desde is not None and min(int(x[2]) for x in nue) >= desde
                if not vivo:
                    msg += ("   (HISTORICO: la vara dura rige desde el Look %s)" % desde
                            if desde is not None
                            else "   (%s no declara cross_batch_desde_look)" % pj)
                duro = vivo or len(repetidas) >= 3
                (rojos if duro else avisos).append(("X4", msg))
                print("   %s %s" % ("🔴" if duro else "🟠", msg))
    if not hubo:
        print("   ✅ ningún batch repite arquitecturas del anterior del mismo personaje")

    # ---- veredicto ----------------------------------------------------------
    print("\n" + "-" * 78)
    if rojos:
        print("🔴 CRUCE SUCIO — %d hallazgos duros, %d avisos" % (len(rojos), len(avisos)))
        print("   Un 🔴 significa que dos looks distintos son el mismo outfit con otro color.")
        print("   Se rediseña la silueta, NO se le cambia el color.")
        return 1
    if avisos:
        print("🟠 CRUCE CON AVISOS — %d, ninguno duro." % len(avisos))
        return 0
    print("✅ CRUCE LIMPIO — cada muñeca lleva lo suyo. Atroz de regio. 💅")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
