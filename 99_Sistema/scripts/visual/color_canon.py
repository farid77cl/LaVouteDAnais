#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
color_canon.py — Linter de paleta de Ele (Ama 02/08/2026: "hay colores en los outfit de ele
que ya me tienen superado").

Nace de medir la flota: en el rango reciente el NEGRO estaba en 42% de los looks y los
METALICOS (chrome 29% / gold 23% / silver 21%) se comian mas de la mitad; ademas aparecia
ROJO/CHERRY como color de prenda (red 14% + cherry 5%), que el canon reserva a pelo y labios.

> ⚠️ **CABLEADO DE VERDAD EL 05/09/2026 — antes era letra muerta.** Este archivo decia
> que "todo inyector de Ele DEBE correr audit_color_batch antes de escribir la galeria".
> Medido ese dia: **nadie lo llamaba.** La unica referencia en todo el repo era
> `outfit.py test`, que corre su SELF-CHECK sobre fixtures, no sobre la flota. Cuando los
> batches pasaron a ser JSON + `outfit.py generar` (29/08), el inyector que debia llamarlo
> dejo de existir y la regla se quedo sin quien la ejecutara. Consecuencia medida sobre el
> batch de colorimetria del 04/09: la regla 3 habria cazado **4 colisiones reales**
> (Ele L819 verde, Ele L821 azul, Miss Doll L79 rosa, Anais L80) y no cazó ninguna,
> hasta que la Ama las vio a ojo. Ahora `cmd_generar` lo corre y **bloquea el batch**.
> Mismo patron que footwear_canon/garment_canon en CLAUDE.md: un self-test verde no
> es una flota limpia.

Reglas que impone (dueno: perfil de Ele §5.2 + `rotacion_color` en anclas_universales.json):

    from color_canon import audit_color_batch
    problems = audit_color_batch(LOOKS)   # cada look: dict {look, garment} o {look, dominant}
    if problems:
        for p in problems: print(p)
        raise SystemExit("Paleta no-canonica: corrige antes de cerrar el batch.")

1. ROJO/CHERRY como dominante -> prohibido (reservado al ADN, choca con el pelo cereza).
2. NEGRO o METALICO dominante 3+ veces seguidas -> prohibido (el 3º debe ser color saturado).
3. Mismo color dominante repetido dentro de los ultimos 3 looks -> prohibido (variedad).
"""
import re, sys

METALLIC = {"chrome","silver","gold","gunmetal","steel","bronze","champagne","platinum","mirror-chrome","pewter","titanium"}
DARK_NEUTRAL = {"black","onyx","jet"}
RED_RESERVED = {"red","cherry","crimson","scarlet","ruby","cherry-red"}
# familia de color para la ventana de variedad (agrupa matices)
FAMILY = {
 "pink":"pink","fuchsia":"pink","magenta":"pink","blush":"pink","rose":"pink","bubblegum":"pink",
 "red":"red","cherry":"red","crimson":"red","scarlet":"red","ruby":"red","wine":"red","maroon":"red","oxblood":"red","burgundy":"red",
 "black":"neutral-dark","onyx":"neutral-dark","jet":"neutral-dark",
 "white":"neutral-light","ivory":"neutral-light","pearl":"neutral-light","cream":"neutral-light",
 "chrome":"metal","silver":"metal","gold":"metal","gunmetal":"metal","steel":"metal","bronze":"metal","champagne":"metal","platinum":"metal","pewter":"metal","titanium":"metal",
 "blue":"blue","navy":"blue","cobalt":"blue","cyan":"blue","teal":"blue","turquoise":"blue","indigo":"blue","aqua":"blue",
 "green":"green","emerald":"green","jade":"green","mint":"green","lime":"green","olive":"green",
 "violet":"purple","lavender":"purple","amethyst":"purple","purple":"purple","lilac":"purple","plum":"purple",
 # Ampliado 05/09/2026: sin estos tonos, `detect_dominant` saltaba al primer
 # metal del texto y clasificaba mal. Medido: "deep aubergine latex corset con
 # antique-silver boning" salia METAL, cuando su dominante es violeta.
 "aubergine":"purple","berenjena":"purple","eggplant":"purple",
 "esmeralda":"green","verde":"green","chartreuse":"green",
 "sapphire":"blue","azul":"blue","midnight":"blue","peacock":"blue",
 "carbon":"neutral-dark","graphite":"neutral-dark","charcoal":"neutral-dark",
 "marfil":"neutral-light","chocolate":"neutral-warm","camel":"neutral-warm",
 "brown":"neutral-warm","beige":"neutral-warm","nude":"neutral-warm",
 "tan":"neutral-warm","taupe":"neutral-warm","sand":"neutral-warm",
 "orange":"orange","coral":"orange","tangerine":"orange","peach":"orange","apricot":"orange",
 "yellow":"yellow","mustard":"yellow","gold-yellow":"yellow",
}
# orden importa: multi-palabra primero para no partir "hot pink" en "pink"
_ALL = sorted(set(list(FAMILY)+list(METALLIC)+list(RED_RESERVED)+["nude","beige","tan"]), key=len, reverse=True)

def detect_dominant(garment):
    """Heuristica: el primer color nombrado suele ser el dominante de la prenda principal."""
    g = garment.lower()
    best=None; bestpos=10**9
    for col in _ALL:
        m=re.search(r'\b'+re.escape(col)+r'\b', g)
        if m and m.start()<bestpos:
            bestpos=m.start(); best=col
    return best

def is_metal_or_dark(col):
    return col in METALLIC or col in DARK_NEUTRAL

def audit_color_batch(looks):
    """looks: lista de dicts. Cada uno {look:N, garment:str} o {look:N, dominant:str}.
    Devuelve lista de strings con las violaciones (vacia = limpio). Respeta el orden dado."""
    problems=[]
    hist=[]          # familias de los looks previos (para ventana de 3)
    streak=0         # racha de metal/dark consecutivos
    for it in looks:
        n=it.get("look","?")
        dom=it.get("dominant") or detect_dominant(it.get("garment",""))
        if not dom:
            continue
        fam=FAMILY.get(dom, dom)
        # 1. rojo/cherry reservado
        if dom in RED_RESERVED:
            problems.append(f"L{n}: dominante ROJO/CHERRY ('{dom}') — reservado a pelo/labios, prohibido en prenda dominante.")
        # 2. racha metal/dark
        if is_metal_or_dark(dom):
            streak+=1
            if streak>=3:
                problems.append(f"L{n}: 3+ looks seguidos con dominante negro/metalico ('{dom}') — el 3º debe ser color saturado.")
        else:
            streak=0
        # 3. repeticion de familia dominante en ventana de 3
        if fam in hist[-3:]:
            problems.append(f"L{n}: familia dominante '{fam}' repetida dentro de los ultimos 3 looks — falta variedad.")
        hist.append(fam)
    return problems


def familia_de(dominante):
    """Familia cromatica de un color dominante. Dueno unico de la taxonomia:
    `auditar_cruce_batches.py` la importa de aca en vez de tener la suya."""
    return FAMILY.get(dominante, dominante)


def audit_rotacion_familia(looks, rot):
    """Ventana de familia cromatica CONFIGURABLE por personaje.

    Ama 05/09/2026, literal:
        "hay libertad de color, pero con la colorimetria ahora se limito,
         pero no puedo tener 3 outfit con el mismo color, asi que dale
         balance y restricciones"

    Las dos mitades de esa frase son la regla entera:

      * **La libertad sigue.** La derogacion del 12/06/2026 (libertad total de
        color y materiales) NO se repone: no hay familias vetadas, no hay cuotas
        de color obligatorias, no vuelve la ventana de 5 ni el cero-solapamiento
        de batch. Se elige por criterio estetico, como ella dijo.
      * **Lo que cambio es el contexto, no el permiso.** La colorimetria del
        04/09 ancló a cada muñeca a un eco de iris (verde en Ele, cobalto en
        Miss Doll, ambar/oro en Anais) y eso ESTRECHA de hecho el rango que cada
        una usa. Con el rango mas angosto, la misma libertad produce mas
        colisiones. Por eso hace falta un tope, no una prohibicion.

    El tope es literal: `max_por_familia` (2) dentro de `ventana` looks. El
    tercero del mismo color es la violacion — ni el segundo.

    **El balance sale solo del tope, no hace falta una regla aparte:** con maximo
    2 por familia en una ventana de 5, el mejor caso degenerado es 2+2+1, o sea
    **siempre >= 3 familias distintas por batch**. Un piso explicito seria una
    segunda regla diciendo lo mismo.

    **Son DOS restricciones, y juntas son el "balance" que ella pidio:**

      1. `max_por_familia` (2) en la ventana — su regla literal.
      2. `prohibir_consecutivos` — los 2 permitidos **no pueden ir pegados**.

    La segunda existe porque sin ella la regla no caza lo que la Ama vio. Medido
    sobre el batch de colorimetria del 04/09: Ele salio verde-verde-azul-azul-
    violeta. Eso **cumple** el tope de 2 y aun asi es exactamente lo que ella
    describio como "repitiendo los mismos colores muy seguido". El tope solo
    limita la CANTIDAD; lo que faltaba era gobernar la DISTRIBUCION. Con las dos,
    verde-azul-verde-azul-violeta pasa y verde-verde-azul-azul-violeta no: misma
    libertad de paleta, repartida.

    Nota de linaje: la regla 3 de `audit_color_batch` (max 1 por familia en
    ventana de 3) es aun mas estricta — prohibiria los dos verdes incluso
    separados. Se conserva viva para Ele porque es canon suyo del 02/08, pero la
    ventana configurable es la que gobierna a las tres desde hoy.

    looks: [{look, garment}] o [{look, dominant}], en orden.
    rot:   dict `rotacion_color` del personaje (anclas_universales.json).
    Devuelve (duros, avisos) — dos listas de strings.
    """
    duros, avisos = [], []
    if not rot:
        return duros, avisos
    ventana = rot.get("ventana", 5)
    tope = rot.get("max_por_familia", 2)
    desde = rot.get("desde_look", 0)
    sin_consecutivos = rot.get("prohibir_consecutivos", True)

    hist = []                       # [(look, familia)]
    for it in looks:
        n = it.get("look", "?")
        dom = it.get("dominant") or detect_dominant(it.get("garment", ""))
        if not dom:
            continue
        fam = familia_de(dom)
        prev = hist[-(ventana - 1):] if ventana > 1 else []
        mismos = [str(l) for l, f in prev if f == fam]
        try:
            historico = int(n) < desde
        except (TypeError, ValueError):
            historico = False
        if len(mismos) + 1 > tope:
            msg = ("L%s: familia '%s' aparece %d veces en una ventana de %d looks "
                   "(ya en L%s) — el tope es %d. Rediseña el COLOR de este look."
                   % (n, fam, len(mismos) + 1, ventana, ", L".join(mismos), tope))
            (avisos if historico else duros).append(
                msg + (" (HISTORICO: la regla rige desde el L%s)" % desde if historico else ""))
        elif sin_consecutivos and prev and prev[-1][1] == fam:
            msg = ("L%s: familia '%s' en dos looks SEGUIDOS (L%s y L%s). El tope de %d por "
                   "ventana se cumple, pero los dos no pueden ir pegados — reparte el color."
                   % (n, fam, prev[-1][0], n, tope))
            (avisos if historico else duros).append(
                msg + (" (HISTORICO: la regla rige desde el L%s)" % desde if historico else ""))
        hist.append((n, fam))
    return duros, avisos


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    # Auto-audit sobre la galeria real (rango reciente) para dimensionar el problema.
    gal="00_Ele/galeria_outfits.md"
    t=open(gal,encoding="utf-8").read()
    blocks={}
    for m in re.finditer(r'(?ms)^(##[^\n]*Look (\d+):.*?)(?=^##[^\n]*Look |\Z)', t):
        blocks[int(m.group(2))]=m.group(1)
    def garment(b):
        m=re.search(r'(?ms)\*\*(?:\d+\.\s*)?Standing:\*\*\s*\n+```\n(.*?)\n```',b)
        if not m: return ""
        p=m.group(1)
        w=re.search(r'wearing (.*?)(?:, rendered in|, beyond the garment|; the garment|\. a single continuous)',p,re.S)
        return w.group(1) if w else ""
    looks=[{"look":k,"garment":garment(blocks[k])} for k in sorted(blocks) if 700<=k<=800 and garment(blocks[k])]
    probs=audit_color_batch(looks)
    print(f"Auto-audit L700-L800 ({len(looks)} looks): {len(probs)} violaciones de paleta")
    for p in probs[:40]:
        print("  -",p)
    # self-check funcional
    demo=[{"look":1,"garment":"a black vinyl corset"},{"look":2,"garment":"a black latex gown"},
          {"look":3,"garment":"a chrome bodysuit"},{"look":4,"garment":"a cherry-red latex dress"}]
    d=audit_color_batch(demo)
    ok = any("3+ looks" in x for x in d) and any("ROJO/CHERRY" in x for x in d)

    # Rotacion de familia (Ama 05/09/2026): el TERCERO del mismo color es la
    # violacion, el segundo no. Y el aubergine no puede salir clasificado METAL.
    rot = {"ventana": 5, "max_por_familia": 2, "desde_look": 0}
    dos = [{"look":1,"garment":"a jade green latex catsuit"},
           {"look":2,"garment":"an emerald green vinyl bikini"}]
    tres = dos + [{"look":3,"garment":"a deep olive green pvc skirt"}]
    d2, a2 = audit_rotacion_familia(dos, rot)
    d3, _   = audit_rotacion_familia(tres, rot)
    aub = familia_de(detect_dominant("a deep aubergine high-shine latex overbust corset with antique-silver boning"))
    sep = [{"look":1,"garment":"a jade green latex catsuit"},
           {"look":2,"garment":"a cobalt blue vinyl bodysuit"},
           {"look":3,"garment":"an emerald green pvc skirt"}]
    d_sep, _ = audit_rotacion_familia(sep, rot)          # 2 verdes separados -> pasa
    ok_rot = (len(d2) == 1 and "SEGUIDOS" in d2[0]       # 2 verdes pegados -> duro
              and not d_sep                              # 2 verdes repartidos -> limpio
              and len(d3) >= 1                           # 3 verdes -> duro
              and aub == "purple")
    if not ok_rot:
        ok = False
        print(f"  detalle rotacion: dos={d2} tres={d3} avisos={a2} aubergine={aub}")
    print("\nself-check color_canon:",
          "LIMPIO (racha metal/dark + rojo dominante + tope de familia + taxonomia)" if ok else f"FALLA {d}")
