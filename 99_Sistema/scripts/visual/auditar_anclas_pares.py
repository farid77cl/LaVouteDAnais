# -*- coding: utf-8 -*-
"""
auditar_anclas_pares.py — Detector heuristico de anclas que se contradicen entre si.

POR QUE EXISTE (Ama 09/09/2026 — "lo que debe hacer el prompt es hacer que Gemini haga
lo que dice el prompt, sin lugar a interpretaciones y con el mayor detalle. desde ahi
hay que construir el outfit engine"):

Dos casos reales, encontrados el mismo dia MIRANDO FOTOS YA GENERADAS:

  1. FABRIC_PRISTINE ("garment surfaces... unmarked:1.4") vs ANIMAL_PRINT_LOCK ("a
     genuine marking texture") -- el Look 832 (zebra) llevaba las dos.
  2. BOTTOM_CUT_LOCK ("seat fully bare:1.4") vs DRESS_LEG_CLOSURE ("hem falling
     closed") -- causa real de la falda del Look 831 abriendose para mostrar la
     tanga (cruzado contra Miss Doll L89, mismo defecto).

La doctrina pide encontrar el PROXIMO caso leyendo el texto, no la foto. Detectar
contradiccion semantica perfecta en lenguaje libre no es realista -- este modulo NO
decide, senala DONDE MIRAR. Es hermano de footwear_canon.py / garment_canon.py: mismo
patron (funciones puras + autotest sobre fixtures, nunca toca la flota real).

DOS FAMILIAS DE CONTRADICCION QUE CUBRE (calibradas contra los dos casos de arriba):

  A) NEGACION vs AFIRMACION del MISMO termino (el caso FABRIC_PRISTINE/ANIMAL_PRINT):
     una ancla dice "NOT/never/no <X>" y otra afirma <X> sin negarlo.
  B) ESTADO ABIERTO vs CERRADO sobre la MISMA region anatomica/de prenda (el caso
     BOTTOM_CUT_LOCK/DRESS_LEG_CLOSURE): ninguna de las dos niega literalmente a la
     otra -- las dos afirman, pero una dice "bare/uncovered/exposed" de una region
     y la otra dice "closed/covered/unbroken" de una region compartida.

USO:
    python auditar_anclas_pares.py                 -> autotest (fixtures), imprime
                                                        "Self-check: ..." (lo lee
                                                        outfit.py test)
    python auditar_anclas_pares.py --escanear [slug] -> escanea anclas_universales.json
                                                        real (uno o los tres personajes)
                                                        e imprime candidatos para
                                                        revision humana
"""
import re
import sys

# --- Familia A: negacion vs afirmacion --------------------------------------

_NEGADOR = re.compile(
    r"\b(?:not|never|no)\b\s+(?:a\s+|an\s+|the\s+)?"
    r"([a-z][a-z\-]{2,}(?:\s+[a-z][a-z\-]{2,}){0,3})", re.I)

_STOP = frozenset((
    "the", "and", "for", "with", "any", "than", "that", "this", "from",
    "into", "over", "than", "then", "than", "her", "she", "its", "his",
))


def _tokens_negados(texto):
    """Frases (y sus palabras sueltas, sin stopwords) que `texto` niega."""
    frases = set()
    palabras = set()
    for m in _NEGADOR.finditer(texto or ""):
        frase = m.group(1).lower().strip()
        frases.add(frase)
        for w in re.findall(r"[a-z\-]{3,}", frase):
            if w not in _STOP:
                palabras.add(w)
    return frases, palabras


def _sin_negaciones(texto):
    """`texto` con los tramos "not/never/no <frase>" borrados -- para no
    confundir una negacion propia con una afirmacion (dos anclas que niegan
    LO MISMO estan de acuerdo, no se contradicen)."""
    return _NEGADOR.sub(" ", texto or "")


def candidatos_negacion(nombre_a, texto_a, nombre_b, texto_b):
    """Pares (a niega lo que b afirma) en cualquier direccion. Lista de avisos."""
    avisos = []
    for na, ta, nb, tb in ((nombre_a, texto_a, nombre_b, texto_b),
                            (nombre_b, texto_b, nombre_a, texto_a)):
        _frases, palabras = _tokens_negados(ta)
        if not palabras:
            continue
        resto_b = _sin_negaciones(tb).lower()
        acertadas = sorted(p for p in palabras if len(p) >= 4 and
                            re.search(r"\b%s\b" % re.escape(p), resto_b))
        # Se exige mas de un termino compartido: una sola palabra suelta
        # (ej. "seat") pega demasiado seguido y ahoga la lista de candidatos
        # en ruido -- el detector deja de senalar algo util.
        if len(acertadas) >= 2:
            avisos.append("%s niega %s, y %s lo afirma (%s)"
                           % (na, sorted(acertadas), nb, ", ".join(acertadas)))
    return avisos


# --- Familia B: dos vocabularios en tension sobre el mismo dominio ---------
#
# Ni "unmarked" niega sintacticamente a "genuine marking texture" (FABRIC_PRISTINE
# vs ANIMAL_PRINT_LOCK), ni "left uncovered" niega a "falling closed" (BOTTOM_CUT_LOCK
# vs DRESS_LEG_CLOSURE) -- las dos son AFIRMACIONES, cada una de su propio lado de un
# mismo eje (marcado/sin marcar, abierto/cerrado). Un dominio = dos listas de frases
# que se oponen; basta que una ancla toque un lado y la otra el lado contrario.
#
# Deliberadamente SIN exigir una region/sustantivo compartido entre A y B: el intento
# original (cruzar "seat"/"hip" contra "leg"/"skirt"/"hem") fallo el propio caso real
# -- BOTTOM_CUT_LOCK habla de "seat"/"hip" y DRESS_LEG_CLOSURE de "leg"/"skirt"/"hem",
# la misma zona del cuerpo con otro sustantivo. Esta etapa prefiere ruido a silencio.
DOMINIOS = {
    "cobertura (abierto/cerrado)": (
        [r"\bbare\b", r"\buncovered\b", r"\bexposed\b", r"\bfully bare\b",
         r"\bleft\s+uncovered\b", r"\bcut away\b", r"\bopen(?:ed)?\b"],
        [r"\bclosed\b", r"\bcovered\b", r"\bconcealed\b", r"\bunbroken\b",
         r"\bnever\s+opened\b", r"\bnever\s+parted\b", r"\bstays?\s+shut\b",
         r"\bnever\s+spread\b"],
    ),
    "marca de tela (sin marca/con marca)": (
        [r"\bunmarked\b", r"\bunprinted\b", r"\bunmarred\b", r"\bunblemished\b",
         r"\bplain\b", r"\bblank\b"],
        [r"\bmarking\b", r"\bpattern\b", r"\btexture\b", r"\bprint(?:ed)?\b",
         r"\bscale\b", r"\bstripe\b", r"\bmotif\b"],
    ),
}
_DOMINIOS_RX = {k: (re.compile("|".join(izq), re.I), re.compile("|".join(der), re.I))
                for k, (izq, der) in DOMINIOS.items()}


def candidatos_dominio(nombre_a, texto_a, nombre_b, texto_b):
    avisos = []
    for dominio, (rx_izq, rx_der) in _DOMINIOS_RX.items():
        a_izq, a_der = bool(rx_izq.search(texto_a or "")), bool(rx_der.search(texto_a or ""))
        b_izq, b_der = bool(rx_izq.search(texto_b or "")), bool(rx_der.search(texto_b or ""))
        if a_izq and b_der and not (a_der or b_izq):
            avisos.append("%s vs %s en '%s' (%s = lado A, %s = lado B)"
                           % (nombre_a, nombre_b, dominio, nombre_a, nombre_b))
        elif b_izq and a_der and not (b_der or a_izq):
            avisos.append("%s vs %s en '%s' (%s = lado A, %s = lado B)"
                           % (nombre_b, nombre_a, dominio, nombre_b, nombre_a))
    return avisos


def pares_sospechosos(anclas):
    """anclas: dict {nombre: texto}. Devuelve [(nombre_a, nombre_b, [avisos])]."""
    nombres = sorted(anclas)
    salida = []
    for i, na in enumerate(nombres):
        for nb in nombres[i + 1:]:
            avisos = (candidatos_negacion(na, anclas[na], nb, anclas[nb])
                       + candidatos_dominio(na, anclas[na], nb, anclas[nb]))
            if avisos:
                salida.append((na, nb, avisos))
    return salida


# --- Enumeracion del conjunto real por personaje (modo --escanear) ---------

def anclas_por_slot_personaje(cfg, slug):
    """{slot: {nombre: texto}} -- SOLO lo que PUEDE coexistir en ESE slot.

    Corregida tras la primera corrida (09/09/2026): la version anterior unia
    los 7 slots en un solo conjunto y comparaba, por ejemplo, FRONT_ANCHOR
    contra SIDE_ANCHOR -- dos anclas que JAMAS caen en el mismo prompt porque
    viven en slots distintos (Standing vs Side Profile). Eso llenaba el
    reporte de pares imposibles en la realidad -- ruido puro que ahogaba a
    los que si importan (20 pares por muñeca, la mayoria cruces entre slots).
    Cruzar por slot real es MAS preciso, no menos conservador: el caso real
    de hoy (BOTTOM_CUT_LOCK/DRESS_LEG_CLOSURE) sigue apareciendo en los 7
    slots -- ninguna de las dos es de un slot, viven en anclas_siempre/opt-in
    sin restriccion, asi que coexisten en TODOS igual que en el prompt real."""
    import os
    AQUI = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, AQUI)
    from prompt_builder import PromptBuilder  # noqa: E402  (mismo directorio, sin ciclo)

    mapa = cfg["mapa_por_defecto"]
    personaje = cfg["personajes"][slug]
    globales = set(mapa.get("_todos", [])) | set(personaje.get("anclas_siempre", []))
    overrides = personaje.get("overrides", {})
    opt_in_todos = (set(n for n, _rx in PromptBuilder.OPT_IN)
                     | set(PromptBuilder._vocab().keys())
                     | {"SEAM_FRONT", "SEAM_BACK"})

    salida = {}
    for slot in cfg["slots_universales"]:
        de_slot = set(overrides.get(slot, mapa.get(slot, [])))
        opt_in_slot = set(n for n in opt_in_todos if PromptBuilder._aplica_en_slot(n, slot))
        nombres = globales | de_slot | opt_in_slot
        salida[slot] = {n: cfg["anclas"][n]["texto"].replace("{kind}", "leopard")
                         for n in nombres if n in cfg["anclas"]}
    return salida


def escanear(cfg, slugs):
    total = 0
    for slug in slugs:
        por_slot = anclas_por_slot_personaje(cfg, slug)
        vistos = {}
        for slot, anclas in por_slot.items():
            for na, nb, avisos in pares_sospechosos(anclas):
                info = vistos.setdefault((na, nb), {"avisos": avisos, "slots": set(),
                                                      "ta": anclas[na], "tb": anclas[nb]})
                info["slots"].add(slot)
        print("\n=== %s -- %d par(es) sospechoso(s) (cruzados por slot real) ==="
              % (slug, len(vistos)))
        for (na, nb) in sorted(vistos):
            info = vistos[(na, nb)]
            total += 1
            print("\n  %s  <->  %s   [slots: %s]"
                  % (na, nb, ", ".join(sorted(info["slots"]))))
            for a in info["avisos"]:
                print("    - %s" % a)
            print("    %s: %s" % (na, info["ta"][:200]))
            print("    %s: %s" % (nb, info["tb"][:200]))
    print("\n%d par(es) candidato(s) en total -- revision humana, no veredicto."
          % total)
    return total


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--escanear":
        import io
        import json
        import os
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
        AQUI = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(AQUI, "anclas_universales.json"), encoding="utf-8") as f:
            _cfg = json.load(f)
        _slugs = [sys.argv[2]] if len(sys.argv) > 2 else list(_cfg["personajes"])
        sys.exit(0 if escanear(_cfg, _slugs) == 0 else 0)  # informativo, nunca bloquea

    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

    # Los DOS casos reales de hoy -- el detector DEBE marcarlos, o no sirve.
    bad = [
        ("FABRIC_PRISTINE",
         "every fabric surface is pristine and unprinted: no tattoo, rune, glyph, "
         "line, scribble or drawing appears on any garment, (all garment surfaces "
         "clean, solid-coloured and unmarked:1.4)",
         "ANIMAL_PRINT_LOCK",
         "the leopard print is a genuine leopard-skin scale/marking texture rendered "
         "consistently across every visible inch of the printed fabric, NOT a lace "
         "pattern, NOT a floral or vine motif"),
        ("BOTTOM_CUT_LOCK",
         "any bottom garment she wears is cut as a thong or g-string: a narrow "
         "tapered front panel, and at the back a single slim strip following the "
         "centre line so the curve of the hips and the seat is left uncovered; "
         "(thong back: a single thin strip, both seat cheeks fully bare:1.4)",
         "DRESS_LEG_CLOSURE",
         "wearing a dress, skirt or robe her legs stay closed: knees and thighs held "
         "together, with the hem falling closed over the lap so the line of the "
         "skirt stays unbroken"),
    ]
    # Pares sanos, conocidos, que NO deben marcarse (control negativo).
    good = [
        ("SINGLE_FRAME",
         "a single continuous photograph: one woman alone in one single full-bleed "
         "frame that fills the entire image edge to edge, NOT a collage",
         "PHOTOREAL_LOCK",
         "a real photograph taken with a real camera: true photographic skin with "
         "visible pores and fine texture, NOT a 3D render, NOT CGI"),
        ("GARMENT_CONSISTENCY",
         "the outfit is exactly ONE garment ensemble rendered precisely as "
         "described: its neckline shape, sleeve length, hemline length, cut, "
         "colour and finish follow the description word for word",
         "HOSIERY_LOCK",
         "the stockings are exactly ONE single pair rendered precisely as "
         "described: their colour, their print or pattern, their opacity and "
         "their length on the thigh follow the description word for word"),
        ("ACCESSORY_COUNT_LOCK",
         "every accessory appears exactly the number of times stated and on the "
         "side stated: a single cuff, bracelet, glove, earring or anklet is worn "
         "on ONE limb only",
         "ASYMMETRY_LOCK",
         "an asymmetric hem or a one-shoulder neckline is rendered on the exact "
         "side described, never mirrored to the other side"),
    ]

    print("=== DEBEN marcarse (bad) ===")
    n_bad = 0
    for na, ta, nb, tb in bad:
        avisos = candidatos_negacion(na, ta, nb, tb) + candidatos_dominio(na, ta, nb, tb)
        print("  %s <-> %s: %s" % (na, nb, avisos or "(nada -- FALLO)"))
        n_bad += bool(avisos)

    print("=== NO deben marcarse (good) ===")
    n_good_malos = 0
    for na, ta, nb, tb in good:
        avisos = candidatos_negacion(na, ta, nb, tb) + candidatos_dominio(na, ta, nb, tb)
        if avisos:
            print("  %s <-> %s: %s  (FALSO POSITIVO)" % (na, nb, avisos))
            n_good_malos += 1
        else:
            print("  %s <-> %s: limpio" % (na, nb))

    ok = (n_bad == len(bad) and n_good_malos == 0)
    print("\nSelf-check:", "LIMPIO (bad detectados, good sin falsos positivos)" if ok
          else "REVISAR (bad=%d/%d, good con falsos positivos=%d)"
               % (n_bad, len(bad), n_good_malos))
    sys.exit(0 if ok else 1)
