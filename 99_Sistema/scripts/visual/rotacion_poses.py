# -*- coding: utf-8 -*-
"""Rotacion de sub-poses ENTRE looks — el chequeo que no existia.

Medido el 06/09/2026: el chequeo 7 de `lint_prompts_personaje.py` detecta poses
duplicadas DENTRO de un look y jamas ENTRE looks. La silueta tiene ventana de
bloqueo (>=3) y el color tiene tope (2 en 5); la pose no tenia NADA salvo la
garantia de que dos looks *seguidos* no coinciden, que es distancia 1.

Con `indice = (look - 1 + offset) %% len(variaciones)`, cada slot se repite
exactamente cada `n` looks. Consecuencia medida:

  · Anais: los SIETE repertorios miden 7 -> sus L83/L84/L85 repiten la postura
    completa de L76/L77/L78. Verificado contra el texto real: 47 palabras
    identicas caracter por caracter en Standing.
  · Miss Doll: 6 de 7 slots con el mismo periodo; solo `odalisque` (9 variantes)
    rompe el patron.
  · Ele se salva por accidente, no por diseño: sus tamanos son 9-7-6-7-6-8-8,
    distintos entre si (NO coprimos: hay dos 7, dos 6 y dos 8), y eso basta para
    que los slots desfasen. Ningun par de su ventana comparte mas de 2 de 7.

⚠️ La formula se replica de la RUTA VIVA: `prompt_builder.py` §pose(), donde
`i0 = (look_number - 1 + off) %% n` con los offsets leidos del JSON. NO de
`pose_rotation_v5.rotate_poses`, que usa `(look_number + off)` SIN el -1, con
offsets hardcodeados, y que **no tiene ningun llamador vivo**. Son dos copias de
la misma idea y pueden divergir: el check `rotacion: la formula espeja
prompt_builder.pose()` de `test_engine.py` existe para que, si `pose()` cambia,
la bateria grite.
"""
import itertools


def indice_de(slot, look, offsets, n):
    """Indice de sub-pose que le toca a `slot` en `look`.

    No modela el bucle de salto de `pose()` — el que corre el indice hacia
    adelante cuando la variante pide un prop que el look no declara. Ese bucle
    solo puede REDUCIR colisiones, asi que este auditor es conservador: puede
    reportar de mas, nunca de menos.
    """
    return (look - 1 + offsets.get(slot, 0)) % n


def colisiones(looks, repertorio):
    """Pares de looks que comparten sub-pose, con el detalle de en que slots.

    Devuelve [{"a", "b", "slots", "n"}] ordenado por gravedad: primero el par
    que mas slots comparte.
    """
    offsets = repertorio.get("offsets", {})
    slots = repertorio.get("slots", {})
    out = []
    for a, b in itertools.combinations(sorted(looks), 2):
        comunes = sorted(
            s for s, var in slots.items()
            if var and indice_de(s, a, offsets, len(var)) == indice_de(s, b, offsets, len(var)))
        if comunes:
            out.append({"a": a, "b": b, "slots": comunes, "n": len(comunes)})
    return sorted(out, key=lambda d: (-d["n"], d["a"], d["b"]))


def periodo_por_slot(repertorio):
    """{slot: cada cuantos looks se repite}. Es, literalmente, el tamaño del
    repertorio: por eso agrandarlo es el unico arreglo que sube el numero."""
    return {s: len(v) for s, v in repertorio.get("slots", {}).items() if v}


# ---------------------------------------------------------------------------
# CLI: `outfit.py rotacion`
# ---------------------------------------------------------------------------
def _main():
    import io
    import json
    import os
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    V = os.path.dirname(os.path.abspath(__file__))
    RAIZ = os.path.normpath(os.path.join(V, "..", "..", ".."))
    sys.path.insert(0, V)
    from prompt_builder import PromptBuilder
    from lint_prompts_personaje import extraer_bloques_b

    rep = json.load(io.open(os.path.join(V, "repertorios_pose.json"), encoding="utf-8"))
    ventana = 12
    solo = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else None
    sucio = 0

    print("=" * 78)
    print("ROTACION DE SUB-POSES ENTRE LOOKS  ·  ventana = ultimos %d looks" % ventana)
    print("=" * 78)
    for slug, p in rep.get("personajes", {}).items():
        if solo and slug != solo:
            continue
        try:
            pb = PromptBuilder(slug)
            ruta = os.path.join(RAIZ, pb.perfil.get("galeria", "").replace("/", os.sep))
            looks = sorted(extraer_bloques_b(io.open(ruta, encoding="utf-8").read()))[-ventana:]
        except Exception as e:                                    # pragma: no cover
            print("\n  %s: no se pudo leer la galeria (%s)" % (slug, e))
            continue
        per = periodo_por_slot(p)
        total = len(p.get("slots", {}))
        print("\n=== %s · L%d-L%d · periodo por slot: %s ==="
              % (slug, looks[0], looks[-1], per))
        peor = 0
        for c in colisiones(looks, p):
            peor = max(peor, c["n"])
            if c["n"] < total - 2:
                continue
            duro = c["n"] >= total - 1
            print("  %s L%d <-> L%d: %d/%d slots con la MISMA sub-pose (%s)"
                  % ("[DURO]" if duro else "[AVISO]", c["a"], c["b"], c["n"], total,
                     ", ".join(c["slots"])))
            if duro:
                sucio += 1
        if peor <= total - 3:
            print("  OK ningun par comparte mas de %d de %d slots" % (peor, total))
        chico = min(per.values()) if per else 0
        if chico and chico <= ventana:
            print("  NOTA: el repertorio mas chico mide %d y la ventana es %d — la "
                  "repeticion es INEVITABLE por aritmetica hasta que crezca" % (chico, ventana))
    print()
    if sucio:
        print("%d par(es) repiten la postura practicamente completa." % sucio)
        print("Arreglo real: agrandar los repertorios (Task 9 del plan). Una ventana de")
        print("seleccion no sirve mientras haya menos variantes que looks en la ventana.")
    else:
        print("OK ningun par repite la postura completa.")
    return 1 if sucio else 0


if __name__ == "__main__":
    import sys
    sys.exit(_main())
