# -*- coding: utf-8 -*-
"""
Linter de VESTUARIO canonico para los inyectores de batch de Ele (hermano de footwear_canon.py).

POR QUE EXISTE (Directiva Ama 11/07/2026 — "aplica los fix en el engine para que no pase"):
La auditoria visual de los ultimos 50 looks (L691-L760) encontro TRES desvios sistematicos que
solo se cazaban mirando la imagen ya generada, y que un token de vestuario libre no valida:

  1) RAYA DE LA MEDIA AL FRENTE (L691, L752, L748): "back-seam stockings" es relativo a la camara;
     en poses de frente Gemini pinta la costura por delante. FIX: rotate_poses(..., seam=True)
     ancla la orientacion pose-aware. Este linter EXIGE que, si hay medias con costura, el look
     declare seam=True (o pegue el ancla), y sugiere anadir NEG_FRONT_SEAM al negative.

  2) CORTES PARA MOSTRAR RUNAS/OMBLIGO (L706, L699): los tokens de Bloque A ("navel piercing",
     "visible under clothing", "rune tattoo along hip crease and bikini line") hacen que Gemini
     le ABRA ventanas a la prenda. FIX: en arquetipos CUBIERTOS (traje/gala/maid/catsuit) el
     inyector debe pegar OPAQUE_LOCK. Este linter lo exige.

  3) MATERIAL MATE pese al token vinyl/latex (L732 traje, L750 rib): en siluetas que primean tela
     mate (sastreria, rib atletico, saten plano) el sesgo del arquetipo le gana al token "vinyl"
     -> sale tela natural. Tener "vinyl" en el texto NO basta (L732 lo tenia). FIX: esas siluetas
     de riesgo deben pegar GLOSS_LOCK (el token fuerte redundante). Este linter lo exige.

Este modulo NO genera vestuario: LINTEA el token que escribe el inyector, igual que footwear_canon.
Las constantes OPAQUE_LOCK / GLOSS_LOCK / NEG_* viven en pose_rotation_v5 (fuente unica).

USO OBLIGATORIO en todo inyector de batch (antes de escribir la galeria):
    from garment_canon import audit_garment_batch
    problems = audit_garment_batch(LOOKS)   # LOOKS = lista de dicts por look
    if problems:
        for p in problems: print(p)
        raise SystemExit("Vestuario no-canonico: corrige antes de cerrar el batch.")

Cada look (dict) necesita, como minimo:
    - "outfit"   : la descripcion de prendas (str)   [claves alt: "garments","vestuario","prendas"]
    - "category" : sub-arquetipo / categoria (str)   [claves alt: "subarchetype","subcategoria","archetype"]
    - "seam"     : bool — True si se paso seam=True a rotate_poses (solo relevante si hay medias con costura)
"""
import re

# --- Vocabulario de deteccion -------------------------------------------------
# Medias CON COSTURA (las que disparan el bug de la raya al frente):
SEAMED = ["back-seam", "back seam", "seamed stocking", "seamed nylon", "seamed hold-up",
          "seamed hosiery", "rht stocking", "cuban heel stocking", "seam stocking", "seamed tights",
          "stockings with a seam", "stockings with back seam", "seamed pantyhose", "seamed bodystocking"]

# Arquetipos CUBIERTOS (donde la prenda debe cubrir -> exigir OPAQUE_LOCK para que no la corten):
COVERED_ARCHETYPES = ["corporate", "office", "executive", "power suit", "domme", "maid",
                      "gown", "gala", "catsuit", "coat-dress", "coat dress", "blazer", "tuxedo",
                      "shirt-dress", "column gown", "evening gown"]

# Siluetas que PRIMEAN tela mate (exigir GLOSS_LOCK, el token fuerte, no solo "vinyl"):
MATTE_PRONE = ["suit", "suiting", "blazer", "pencil skirt", "ribbed", "rib knit", "rib-knit",
               "wool", "crepe", "tweed", "cotton", "jersey", "knit set", "sports-bra", "sports bra",
               "leggings", "seamless set", "athletic set", "sweatpant", "hoodie", "track suit",
               "tracksuit", "plain satin", "matte satin"]

# Marcadores de que el inyector YA pego el lock fuerte (subcadenas distintivas de las constantes):
OPAQUE_MARKERS = ["solid and uncut", "no keyhole", "no keyhole, cutout", "concealed beneath the fabric wherever"]
GLOSS_MARKERS  = ["absolutely no matte", "mirror-like reflective surface", "glossy mirror-like reflective"]
CONSISTENCY_MARKERS = ["neckline shape, sleeve length", "identical and unchanged across all poses",
                       "the exact same single outfit in every shot"]

# Prendas cuyo CORTE (escote/manga/ruedo) suele driftear entre poses -> exigir que el token lo fije
# o pegar CONSISTENCY_LOCK (bug L746 escote, L707 mangas, L693 estampado):
DRIFTY_GARMENTS = ["dress", "gown", "cheongsam", "qipao", "slip", "minidress", "mini-dress",
                   "column", "wiggle", "cocktail", "chemise", "robe", "kimono", "catsuit", "bodysuit"]
# Tokens que demuestran que el ESCOTE esta fijado:
NECKLINE_TOKENS = ["neckline", "off-shoulder", "off shoulder", "bardot", "halter", "sweetheart",
                   "scoop", "square neck", "mock neck", "high neck", "mandarin collar", "cowl",
                   "plunging", "strapless", "bandeau", "boat neck", "bateau", "one-shoulder", "v-neck"]
# Tokens que demuestran que la MANGA esta fijada:
SLEEVE_TOKENS = ["sleeve", "sleeveless", "long sleeves", "short sleeves", "cap sleeve", "strapless",
                 "spaghetti strap", "spaghetti-strap", "thin strap", "bardot", "off-shoulder", "long-sleeve"]
# Tokens que demuestran que el RUEDO/LARGO esta fijado:
HEM_TOKENS = ["hem", "-length", " length", "floor-length", "floor length", "knee-length", "mini",
              "midi", "maxi", "mid-thigh", "ankle-length", "to the knee", "to the floor", "micro"]


def _has_any(text, needles):
    t = (text or "").lower()
    return [n.strip() for n in needles if n.lower() in t]


def _has_any_word(text, needles):
    """Como _has_any pero con limites de palabra: 'suit' NO matchea 'catsuit'/'bodysuit'."""
    t = (text or "").lower()
    hits = []
    for n in needles:
        if re.search(r'(?<![a-z])' + re.escape(n.lower()) + r'(?![a-z])', t):
            hits.append(n.strip())
    return hits


def audit_garment(outfit, archetype="", seam=False, tag=""):
    """Lintea el vestuario de UN look. Devuelve lista de mensajes de violacion (vacia = limpio).
    tag = etiqueta libre (ej. 'L732'). seam = True si el inyector paso seam=True a rotate_poses."""
    pre = f"[{tag}] " if tag else ""
    out = []
    og = (outfit or "")
    arch = (archetype or "").lower()

    # 1) MEDIAS CON COSTURA sin ancla de orientacion (bug raya al frente)
    seamed = _has_any(og, SEAMED)
    if seamed and not seam:
        out.append(f"{pre}MEDIAS CON COSTURA ({', '.join(sorted(set(seamed)))}) sin seam=True: "
                   f"pasa rotate_poses(..., seam=True) o la raya sale por delante. "
                   f"Anade tambien NEG_FRONT_SEAM al negative.")

    # 2) ARQUETIPO CUBIERTO sin OPAQUE_LOCK (bug cortes para mostrar runas/ombligo)
    #    word-boundary: 'maid' no debe matchear 'mermaid'.
    covered = _has_any_word(arch + " " + og.lower(), COVERED_ARCHETYPES)
    if covered and not _has_any(og, OPAQUE_MARKERS):
        out.append(f"{pre}ARQUETIPO CUBIERTO ({', '.join(sorted(set(covered)))}) sin OPAQUE_LOCK: "
                   f"pega OPAQUE_LOCK en la clausula de vestuario o Gemini corta la prenda para "
                   f"mostrar ombligo/runas. Anade NEG_CUTOUT al negative.")

    # 3) SILUETA MATE-PRONE sin GLOSS_LOCK (desvio material mate; tener 'vinyl' no basta)
    #    word-boundary: 'suit' no debe matchear 'catsuit'/'bodysuit'/'jumpsuit'.
    matte = _has_any_word(og, MATTE_PRONE)
    if matte and not _has_any(og, GLOSS_MARKERS):
        out.append(f"{pre}SILUETA MATE-PRONE ({', '.join(sorted(set(matte)))}) sin GLOSS_LOCK: "
                   f"pega GLOSS_LOCK (el token fuerte) — 'vinyl' suelto no basta (L732 lo tenia y "
                   f"salio mate). Anade NEG_MATTE al negative.")

    # 4) DRIFT DE PRENDA ENTRE POSES: vestido/gown cuyo token no fija escote/manga/ruedo y tampoco
    #    trae CONSISTENCY_LOCK -> Gemini reinventa el corte por pose (bug L746 escote, L707 mangas).
    drifty = _has_any_word(og, DRIFTY_GARMENTS)
    if drifty and not _has_any(og, CONSISTENCY_MARKERS):
        missing = []
        if not _has_any(og, NECKLINE_TOKENS): missing.append("escote/neckline")
        if not _has_any(og, SLEEVE_TOKENS):   missing.append("manga/sleeve")
        if not _has_any(og, HEM_TOKENS):      missing.append("largo/hem")
        if missing:
            out.append(f"{pre}PRENDA CON DRIFT ({', '.join(sorted(set(drifty)))}) sin fijar "
                       f"[{', '.join(missing)}] ni CONSISTENCY_LOCK: nombra escote+manga+ruedo "
                       f"explicito y pega CONSISTENCY_LOCK, o el corte cambia entre poses. "
                       f"Anade NEG_INCONSISTENT al negative.")
    return out


def _get(look, *keys, default=""):
    for k in keys:
        if k in look and look[k] not in (None, ""):
            return look[k]
    return default


def audit_garment_batch(looks, garment_keys=("outfit", "garments", "vestuario", "prendas"),
                        archetype_keys=("category", "subarchetype", "subcategoria", "archetype"),
                        seam_keys=("seam", "seamed_anchor")):
    """Lintea una lista de looks (dicts). Devuelve lista plana de violaciones de todo el batch."""
    problems = []
    for i, lk in enumerate(looks):
        tag = _get(lk, "tag", "id", "look", default=f"idx{i}")
        problems += audit_garment(
            _get(lk, *garment_keys),
            _get(lk, *archetype_keys),
            seam=bool(_get(lk, *seam_keys, default=False)),
            tag=str(tag),
        )
    return problems


if __name__ == "__main__":
    import sys, io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

    # Casos de la auditoria L691-L760 que DEBEN saltar:
    bad = [
        dict(tag="L752", category="Corporate",
             outfit="midnight blue liquid latex blazer minidress, black back-seam stockings",
             seam=False),  # medias con costura sin seam=True
        dict(tag="L732", category="Corporate power suit",
             outfit="ivory white vinyl blazer-dress, pencil skirt, high-gloss specularity on vinyl",
             seam=False),  # traje/blazer/pencil skirt sin GLOSS_LOCK (y arquetipo cubierto sin OPAQUE_LOCK)
        dict(tag="L750", category="Gym Performance",
             outfit="black seamless ribbed sports-bra and high-waist leggings, high-gloss on ribbed fabric",
             seam=False),  # rib atletico sin GLOSS_LOCK
        dict(tag="L746", category="High-Fashion Editorial",
             outfit="black wet-look mermaid column gown with oxblood cape",
             seam=False),  # gown sin escote/manga/ruedo fijo ni CONSISTENCY_LOCK -> drift (bug real L746)
    ]
    # Casos que DEBEN pasar limpios (ya con los locks / sin gatillo):
    from pose_rotation_v5 import OPAQUE_LOCK, GLOSS_LOCK, CONSISTENCY_LOCK
    good = [
        dict(tag="L732fix", category="Corporate power suit",
             outfit="ivory white vinyl blazer-dress with a plunging neckline, long sleeves, knee-length hem, "
                     "pencil skirt, " + GLOSS_LOCK + ", " + OPAQUE_LOCK + ", " + CONSISTENCY_LOCK,
             seam=False),
        dict(tag="L752fix", category="Corporate",
             outfit="midnight blue liquid latex blazer minidress with a plunging neckline, long sleeves, "
                     "mini hem, black back-seam stockings, " + GLOSS_LOCK + ", " + OPAQUE_LOCK + ", " + CONSISTENCY_LOCK,
             seam=True),
        dict(tag="L746fix", category="High-Fashion Editorial",
             outfit="black wet-look mermaid column gown, off-shoulder bardot neckline, long fitted sleeves to "
                     "the wrist, floor-length hem, oxblood cape, " + OPAQUE_LOCK + ", " + CONSISTENCY_LOCK,
             seam=False),
        dict(tag="L742", category="Corporate",  # catsuit liquid latex: fija cuello alto+manga larga+full length
             outfit="black patent liquid latex catsuit, high mock neck, long sleeves, full-length legs, "
                     + OPAQUE_LOCK + ", " + CONSISTENCY_LOCK,
             seam=False),
        dict(tag="L699", category="Stripper Stage",  # lenceria alto-corte: runas/ombligo on-brand, NO exige opaque;
             # teddy fija escote halter + sin mangas + alto-corte -> sin drift
             outfit="baby pink pvc high-cut teddy, halter neckline, sleeveless, high-cut micro hem, bare hips, exposed navel",
             seam=False),
    ]
    print("=== DEBEN saltar (bad) ===")
    pb = audit_garment_batch(bad)
    for p in pb: print("  ", p)
    print("=== DEBEN pasar limpios (good) ===")
    pg = audit_garment_batch(good)
    for p in pg: print("  ", p)
    ok = (len(pb) >= 4 and len(pg) == 0)
    print("\nSelf-check:", "LIMPIO (bad detectados, good sin falsos positivos)" if ok
          else f"REVISAR (bad={len(pb)} esperado>=4, good={len(pg)} esperado 0)")
