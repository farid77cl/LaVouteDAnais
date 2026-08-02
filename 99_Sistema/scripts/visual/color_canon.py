#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
color_canon.py — Linter de paleta de Ele (Ama 02/08/2026: "hay colores en los outfit de ele
que ya me tienen superado").

Nace de medir la flota: en el rango reciente el NEGRO estaba en 42% de los looks y los
METALICOS (chrome 29% / gold 23% / silver 21%) se comian mas de la mitad; ademas aparecia
ROJO/CHERRY como color de prenda (red 14% + cherry 5%), que el canon reserva a pelo y labios.

Reglas que impone (dueno: perfil de Ele §5.2). Todo inyector de Ele DEBE correr
audit_color_batch(LOOKS) antes de escribir la galeria, igual que footwear_canon:

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
    print("\nself-check color_canon:", "LIMPIO (caza racha metal/dark + rojo dominante)" if ok else f"FALLA {d}")
