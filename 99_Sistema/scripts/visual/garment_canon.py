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

REFUERZO 13/07/2026 (auditoria "revisa las ultimas imagenes... busca tatuajes/piercings mostrandose
donde no corresponde"): la auditoria de L764/766-770 (batch generado ANTES del blindaje SKIN_LOCK)
confirmo con zoom el defecto en 3 looks (piercings marcados sobre latex/vinilo opaco en L767/L768/L770,
mas un keyhole no pedido en L767 y la costura de la media al frente en L764). Causa de fondo: este
linter validaba OPAQUE_LOCK/GLOSS_LOCK/CONSISTENCY_LOCK pero (a) NUNCA revisaba si la frase-orden
vieja ("...pressing against and visible under clothing") seguia viva en el texto, (b) NUNCA exigia
el bloque Negative Prompt (pese a que la documentacion decia que si), y (c) su lista de arquetipos
"cubiertos" no incluia bodycon/crop-top/halter/monokini/bra/palazzo/sarong — exactamente las siluetas
del batch que fallo. Los 3 agujeros se cierran aqui: audit_garment() ahora es DURA (frase prohibida =
violacion siempre, sin importar arquetipo), audit_negative() exige el bloque negative + su marca
NEG_MARKS_THROUGH, y COVERED_ARCHETYPES crecio a la lista real de siluetas fetish del canon.

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
    - "negative" : el bloque Negative Prompt ya construido con build_negative(...) (str) — OBLIGATORIO,
                   se audita con audit_negative_batch() / esta incluido en audit_garment_batch()
"""
import re
from pose_rotation_v5 import find_forbidden, has_skin_lock, NEG_MARKS_THROUGH

# --- Vocabulario de deteccion -------------------------------------------------
# Medias CON COSTURA (las que disparan el bug de la raya al frente):
# Marcadores de que el ancla de orientacion de costura YA esta escrita en el prompt
# (subcadenas distintivas de STOCKING_SEAM_FRONT / STOCKING_SEAM_BACK):
SEAM_ANCHOR_MARKERS = ["one single seam and it runs strictly up the centre-back",
                       "single back-seam of each stocking clearly visible",
                       "front of each leg is completely smooth and seamless"]

# Contexto que confirma que una "costura trasera" es de MEDIA y no de chaqueta:
HOSIERY_CONTEXTO = ["stocking", "nylon", "hold-up", "holdup", "hosiery", "pantyhose",
                    "tights", "bodystocking", "fishnet", "thigh-high", "thigh high"]
SEAMED = ["back-seam", "back seam", "seamed stocking", "seamed nylon", "seamed hold-up",
          "seamed hosiery", "rht stocking", "cuban heel stocking", "seam stocking", "seamed tights",
          "stockings with a seam", "stockings with back seam", "seamed pantyhose", "seamed bodystocking"]

# Arquetipos CUBIERTOS (donde la prenda debe cubrir -> exigir OPAQUE_LOCK para que no la corten):
# AMPLIADO 13/07/2026 tras el batch L761-L770: la lista vieja NO incluia bodycon/crop-top/palazzo —
# siluetas de PANEL SOLIDO que fallaron de verdad (L767 bodycon con keyhole no pedido, L768 crop-top
# + palazzo). OJO: "halter"/"bra"/"monokini"/"sarong" quedan FUERA a proposito — son demasiado
# genericos y matchean piezas que son strappy/expuestas POR DISENO (teddy, bikini, cage monokini,
# donde mostrar piel es on-brand, no un bug); exigirles OPAQUE_LOCK dio un falso positivo real en el
# self-check (L699 teddy). La defensa universal contra marcas-a-traves-de-tela para ESOS casos es el
# chequeo 0b (SKIN_LOCK/clausula solo-piel-desnuda), que no depende del arquetipo.
COVERED_ARCHETYPES = ["corporate", "office", "executive", "power suit", "domme", "maid",
                      "gown", "gala", "catsuit", "coat-dress", "coat dress", "blazer", "tuxedo",
                      "shirt-dress", "column gown", "evening gown", "bodycon", "crop top", "crop-top",
                      "palazzo", "bustier", "corselette", "corset", "bodystocking"]

# Familias de estampado ANIMAL cuya fidelidad hay que blindar (bug L764: python-print salio como
# encaje/enredadera). Si el outfit las nombra, exige animal_print_lock(kind) pegado.
ANIMAL_PRINTS = ["python", "snake", "leopard", "tiger", "zebra"]
ANIMAL_PRINT_MARKER = "not a lace pattern"

# Siluetas que PRIMEAN tela mate (exigir GLOSS_LOCK, el token fuerte, no solo "vinyl"):
MATTE_PRONE = ["suit", "suiting", "blazer", "pencil skirt", "ribbed", "rib knit", "rib-knit",
               "wool", "crepe", "tweed", "cotton", "jersey", "knit set", "sports-bra", "sports bra",
               "leggings", "seamless set", "athletic set", "sweatpant", "hoodie", "track suit",
               "tracksuit", "plain satin", "matte satin"]

# Marcadores de que el inyector YA pego el lock fuerte (subcadenas distintivas de las constantes):
OPAQUE_MARKERS = ["solid and uncut", "no keyhole", "no keyhole, cutout", "concealed beneath the fabric wherever"]
GLOSS_MARKERS  = ["absolutely no matte", "mirror-like reflective surface", "glossy mirror-like reflective"]
CONSISTENCY_MARKERS = ["neckline shape, sleeve length", "rendered precisely as described",
                       "exactly one garment ensemble"]

# METALENGUAJE MULTI-TOMA (Ama 15/07/2026 — BUG "la imagen sale como collage de paneles"): el
# CONSISTENCY_LOCK v1 decia "IDENTICAL and unchanged across all poses / in every shot" y el batch
# de prueba L791-L800 rindio 4 collages/grillas en 30 imagenes (L792 Standing = 9 paneles con la
# figura central DESCALZA) — un generador de UNA imagen lee "all poses" y entrega la hoja de
# contactos. Los locks v2 lo derogaron; este chequeo impide que un inyector futuro lo reintroduzca
# copiando texto viejo de la galeria (mismo patron que FORBIDDEN_PHRASES).
META_SHOT_LANGUAGE = ["across all poses", "in every shot", "between shots", "in every pose",
                      "in all shots", "across the poses"]

# Prendas cuyo CORTE (escote/manga/ruedo) suele driftear entre poses -> exigir que el token lo fije
# o pegar CONSISTENCY_LOCK (bug L746 escote, L707 mangas, L693 estampado):
# AMPLIACION 20/07/2026 (Ama: auditoria del L86/L87 recien materializados). La lista original solo
# miraba VESTIDOS y enterizos, asi que la prenda MAS propensa a driftear la manga —una chaqueta o
# blusa de dos piezas— nunca se revisaba. Evidencia: el L87 rindio manga larga hasta la muneca en
# Back View y la MISMA chaqueta SIN MANGAS en el POV; el L86 igual con su blusa. Ninguna ficha de
# los dos declaraba largo de manga, y el chequeo no lo reclamo porque "jacket"/"blouse" no estaban
# aca. Medido tras la ampliacion: 305 looks de la galeria viva + 64 del archivo quedan sin manga
# declarada — deuda real que este chequeo ahora si reporta.
# RE-MEDIDO 23/07/2026 (el "305+64" quedo FOSILIZADO — es del 20/07, ANTES del barrido del 22/07 que
# inyecto CONSISTENCY_LOCK al grueso de la galeria). Estado real hoy: 70 looks viva + 6 archivo (76,
# no 369), y de la viva 68 YA estan 7/7 materializados (arreglar el prompt no cambia una imagen que
# ya existe). Accionables con poses pendientes: L260 (blusa Office Siren -> long fitted sleeves) y
# L268 (cover-up crochet -> sleeveless), ambos ya inyectados; los demas eran falsos positivos de
# prenda-sin-manga (ver SLEEVELESS_BY_NATURE) o cascarones sin prompt (L148/L150). Leccion repetida:
# un conteo de "deuda" sin fecha de re-medicion envejece hacia la mentira (misma que el Pendiente #1).
DRIFTY_GARMENTS = ["dress", "gown", "cheongsam", "qipao", "slip", "minidress", "mini-dress",
                   "column", "wiggle", "cocktail", "chemise", "robe", "kimono", "catsuit", "bodysuit",
                   # dos piezas y torso (ampliacion 20/07/2026):
                   "jacket", "blazer", "blouse", "shirt", "coat", "cardigan", "sweater",
                   "turtleneck", "jumpsuit", "corset", "overbust", "bustier", "bodice", "top"]
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

# Prendas SIN MANGA POR NATURALEZA (bikini, sujetador, top de gimnasio): exigirles "manga
# declarada" es un FALSO POSITIVO — un top triangular de bikini, un sports-bra o un push-up bra
# no tienen manga que driftear entre poses, y Gemini no le inventa una a un triangulo de bikini.
# AMPLIACION 23/07/2026 (Ama, pendiente "manga sin declarar"): al medir el estado real (76 looks,
# no los 305+64 fosilizados del 20/07 — el barrido del 22/07 ya inyecto CONSISTENCY_LOCK al grueso)
# los unicos accionables con poses pendientes eran L124 (sports-bra), L125 (bikini triangle) y L127
# (push-up bra): NINGUNO tiene manga. El defecto era del linter, que matcheaba "top"/"bra" y pedia
# una manga inexistente. La exencion SOLO aplica si no hay una capa EXTERIOR con manga encima
# (una chaqueta/blusa/cover-up sobre el bikini SI debe declarar su manga).
SLEEVELESS_BY_NATURE = ["bikini", "micro-bikini", "microbikini", "micro bikini", "triangle top",
                        "triangular top", "sports bra", "sports-bra", "sports top", "push-up bra",
                        "pushup bra", "push up bra", "bralette", "bandeau top", "string top"]
OUTER_LAYERS = ["jacket", "blazer", "coat", "cardigan", "blouse", "shirt", "sweater", "turtleneck",
                "cover-up", "coverup", "kimono", "robe", "bolero", "shrug", "kaftan"]


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


def audit_garment(outfit, archetype="", seam=False, tag="", bloque_a="", slot=""):
    """Lintea el vestuario de UN look. Devuelve lista de mensajes de violacion (vacia = limpio).
    tag = etiqueta libre (ej. 'L732'). seam = True si el inyector paso seam=True a rotate_poses.
    bloque_a = el Bloque A (ADN fisico) completo del prompt, si el inyector lo tiene disponible por
    separado; si no se pasa, los chequeos 0a/0b caen sobre `outfit` como mejor esfuerzo."""
    pre = f"[{tag}] " if tag else ""
    out = []
    og = (outfit or "")
    arch = (archetype or "").lower()
    full_text = f"{bloque_a} {og} {arch}"

    # 0a) FRASE-ORDEN PROHIBIDA (Ama 13/07 — causa raiz de "piercings a traves de la tela" en
    #     L767/L768/L770). Chequeo DURO: no importa el arquetipo, si la frase esta, es violacion.
    forbidden = find_forbidden(full_text)
    if forbidden:
        out.append(f"{pre}FRASE-ORDEN PROHIBIDA presente ({', '.join(forbidden)}): esto le pide "
                    f"directamente al generador que muestre piercings/tatuajes A TRAVES de la ropa. "
                    f"Reemplaza por el Bloque A corregido de dna_v3_5.md (clausula solo-piel-desnuda).")

    # 0b) SKIN_LOCK / clausula solo-piel-desnuda AUSENTE (universal, no solo en arquetipos cubiertos):
    #     el Bloque A fijo YA trae la clausula desde el 13/07; si no aparece, o el inyector uso un
    #     Bloque A viejo o no paso bloque_a= para poder verificarlo.
    if bloque_a and not has_skin_lock(full_text):
        out.append(f"{pre}SIN clausula solo-piel-desnuda en el Bloque A: pega el Bloque A vigente de "
                    f"dna_v3_5.md (trae 'visible ONLY on genuinely bare skin... never through or over "
                    f"any garment') o anade SKIN_LOCK explicito.")

    # 0d) METALENGUAJE MULTI-TOMA vivo en el texto (Ama 15/07 — invita el collage/hoja de contactos):
    meta = _has_any(full_text, META_SHOT_LANGUAGE)
    if meta:
        out.append(f"{pre}METALENGUAJE MULTI-TOMA presente ({', '.join(sorted(set(meta)))}): un generador "
                    f"de UNA imagen lee 'all poses/every shot' y entrega una grilla de paneles (4 collages "
                    f"reales en el batch L791-L800). Usa los locks v2 de pose_rotation_v5 (CONSISTENCY_LOCK/"
                    f"HOSIERY_LOCK sin lenguaje de tomas) y pega SINGLE_FRAME via rotate_poses().")

    # 0c) ESTAMPADO ANIMAL sin candado de fidelidad (bug L764: python-print salio como encaje)
    prints = _has_any_word(og.lower(), ANIMAL_PRINTS)
    if prints and ANIMAL_PRINT_MARKER not in og.lower():
        out.append(f"{pre}ESTAMPADO ANIMAL ({', '.join(sorted(set(prints)))}) sin candado de fidelidad: "
                    f"pega animal_print_lock('{sorted(set(prints))[0]}') de pose_rotation_v5 o el print "
                    f"puede rendir como encaje/enredadera generica. Anade NEG_PRINT_DRIFT al negative.")

    # 1) MEDIAS CON COSTURA sin ancla de orientacion (bug raya al frente)
    # La costura solo es de MEDIA si hay media. "back seam" a secas tambien lo dice
    # una chaqueta — el ancla WRAP_BACK_TAILORED describe "the smooth continuous back
    # panel of the jacket with its centre-back seam and vent" — y sin este guardia el
    # auditor marcaba MEDIAS CON COSTURA en todo look de blazer (medido 29/08/2026).
    # Los terminos que ya nombran la media ("seamed stocking", "seamed nylon"...) no
    # necesitan el contexto: se bastan solos.
    seamed = _has_any(og, SEAMED)
    if seamed and not _has_any(og, HOSIERY_CONTEXTO):
        seamed = [s for s in seamed if "stocking" in s or "nylon" in s or "hold-up" in s]
    # `seam=True` era la unica forma de declarar el ancla, porque solo el inyector
    # de pose_rotation_v5 sabia ponerla. Desde el 29/08/2026 prompt_builder tambien
    # la escribe (SEAM_FRONT / SEAM_BACK), asi que un prompt ya anclado se reconoce
    # por su texto y no por un parametro que el motor nuevo no tiene como pasar.
    if seamed and _has_any(og, SEAM_ANCHOR_MARKERS):
        seam = True
    # El Side Profile NO lleva ancla de costura, y es deliberado: de perfil la raya
    # trasera cae en el borde posterior de la pierna, que es justo donde debe estar
    # (pose_rotation_v5._SEAM_SKIP_SLOTS). Sin este dato el auditor marcaba una
    # violacion en cada Side Profile con medias -- ruido garantizado, no defecto.
    # Solo aplica cuando quien llama sabe de que toma viene el prompt.
    if slot and slot.strip().lower().replace("_", " ") == "side profile":
        seam = True
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
        # Prenda sin manga por naturaleza (bikini/sports-bra/push-up) y SIN capa exterior con
        # manga encima -> no se exige "manga declarada" (falso positivo, Ama 23/07/2026).
        sleeveless_ctx = bool(_has_any(og, SLEEVELESS_BY_NATURE)) and not _has_any_word(og, OUTER_LAYERS)
        missing = []
        if not _has_any(og, NECKLINE_TOKENS): missing.append("escote/neckline")
        if not sleeveless_ctx and not _has_any(og, SLEEVE_TOKENS): missing.append("manga/sleeve")
        if not _has_any(og, HEM_TOKENS):      missing.append("largo/hem")
        if missing:
            out.append(f"{pre}PRENDA CON DRIFT ({', '.join(sorted(set(drifty)))}) sin fijar "
                       f"[{', '.join(missing)}] ni CONSISTENCY_LOCK: nombra escote+manga+ruedo "
                       f"explicito y pega CONSISTENCY_LOCK, o el corte cambia entre poses. "
                       f"Anade NEG_INCONSISTENT al negative.")
    return out


def audit_negative(negative, tag=""):
    """Lintea el bloque Negative Prompt de UN look (Ama 13/07 — bug 'sin negative desde el L711':
    60 looks / 420 poses salieron con el negative vacio porque cada inyector lo tipeaba a mano y
    ninguno lo revisaba). Devuelve lista de violaciones (vacia = limpio)."""
    pre = f"[{tag}] " if tag else ""
    out = []
    neg = (negative or "").strip()
    if not neg:
        out.append(f"{pre}SIN Negative Prompt: todo look DEBE registrar el bloque negative construido "
                    f"con build_negative(...) de pose_rotation_v5 — el negative vacio es lo que dejo "
                    f"pasar la costura al frente y las marcas a traves de la tela desde el L711.")
        return out
    if NEG_MARKS_THROUGH.split(",")[0].strip().lower() not in neg.lower():
        out.append(f"{pre}Negative Prompt sin NEG_MARKS_THROUGH: el par negativo del SKIN_LOCK "
                    f"(piercings/tatuajes a traves de la tela) debe ir SIEMPRE, construcelo con "
                    f"build_negative(...) en vez de escribirlo a mano.")
    # v2 15/07/2026 — VETO DE COLOR DESNUDO (bug L791: el negativo traia "oxblood" a secas y el
    # catsuit ES oxblood — el negativo peleaba contra su propia prenda). Un color en el negative
    # solo puede ir CALIFICADO (ej. "oxblood lips"); el color a secas veta la paleta entera.
    if re.search(r"(?<![a-z])oxblood(?!\s+lips)", neg.lower()):
        out.append(f"{pre}Negative Prompt con 'oxblood' A SECAS (color desnudo): veta la prenda entera "
                    f"si el look viste oxblood (bug real L791). Usa 'oxblood lips' — regenera el bloque "
                    f"con build_negative(...) v2.")
    # v2 15/07/2026 — familia anti-collage obligatoria (el "split image" solo no basto: L792/L795
    # rindieron grillas igual; el par afirmativo SINGLE_FRAME viaja en el positive via rotate_poses):
    if "collage" not in neg.lower():
        out.append(f"{pre}Negative Prompt sin familia anti-collage ('collage, grid of images, multi-panel "
                    f"layout, contact sheet...'): regenera el bloque con build_negative(...) v2.")
    return out


def _get(look, *keys, default=""):
    for k in keys:
        if k in look and look[k] not in (None, ""):
            return look[k]
    return default


def audit_garment_batch(looks, garment_keys=("outfit", "garments", "vestuario", "prendas"),
                        archetype_keys=("category", "subarchetype", "subcategoria", "archetype"),
                        seam_keys=("seam", "seamed_anchor"),
                        bloque_a_keys=("bloque_a", "dna_block", "full_prompt"),
                        negative_keys=("negative", "negative_prompt")):
    """Lintea una lista de looks (dicts). Devuelve lista plana de violaciones de todo el batch.
    Incluye ahora el chequeo de Negative Prompt (audit_negative) — antes vivia solo en la
    documentacion, nunca se ejecutaba de verdad (Ama 13/07)."""
    problems = []
    for i, lk in enumerate(looks):
        tag = _get(lk, "tag", "id", "look", default=f"idx{i}")
        problems += audit_garment(
            _get(lk, *garment_keys),
            _get(lk, *archetype_keys),
            seam=bool(_get(lk, *seam_keys, default=False)),
            tag=str(tag),
            bloque_a=_get(lk, *bloque_a_keys),
        )
        problems += audit_negative(_get(lk, *negative_keys), tag=str(tag))
    return problems


if __name__ == "__main__":
    import sys, io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

    from pose_rotation_v5 import OPAQUE_LOCK, GLOSS_LOCK, CONSISTENCY_LOCK, SKIN_LOCK, build_negative, animal_print_lock

    # Casos de la auditoria L691-L760 + L761-L770 (13/07) que DEBEN saltar:
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
        dict(tag="L767", category="Escort Nightside",  # BUG REAL 13/07: bodycon (nueva entrada COVERED)
             outfit="second-skin mini bodycon dress in high-gloss coral neon latex, halter neckline, "
                     "sleeveless, hem cut high on the thigh",
             seam=False),  # bodycon cubierto sin OPAQUE_LOCK -> keyhole no pedido que expuso el ombligo
        dict(tag="L768-fraseorden", category="Domestic Trophy",  # BUG REAL 13/07: frase vieja viva
             outfit="jade vinyl cropped halter top, wide-leg palazzo trousers, nipple piercings pressing "
                     "against and visible under clothing",
             seam=False),  # la orden vieja SIGUE viva -> violacion dura sin importar arquetipo
        dict(tag="L764-print", category="Corporate Coat-Dress",  # BUG REAL 13/07: python-print sin candado
             outfit="jade vinyl coat-dress, plunging neckline, long sleeves, mid-thigh hem, sheer black "
                     "python-print back-seamed stockings, " + OPAQUE_LOCK + ", " + CONSISTENCY_LOCK,
             seam=True),  # "python-print" sin animal_print_lock -> puede rendir como encaje (L764 real)
        dict(tag="L768-sinneg", category="Domestic Trophy",  # BUG REAL 13/07: negative vacio
             outfit="jade vinyl cropped halter top, wide-leg palazzo trousers, " + OPAQUE_LOCK + ", " + CONSISTENCY_LOCK,
             seam=False, negative=""),  # sin negative -> violacion dura (causa raiz del batch L761-L790)
        dict(tag="L792-meta", category="Lenceria",  # BUG REAL 15/07: metalenguaje multi-toma = collage
             outfit="amethyst wet-satin kimono robe, deep open V-neck front, wide kimono sleeves, "
                     "floor-length hem, the exact same single outfit in every shot: IDENTICAL and "
                     "unchanged across all poses",
             seam=False, negative=build_negative(lingerie=True)),  # texto viejo -> debe saltar META
        dict(tag="L791-negviejo", category="Corporate",  # BUG REAL 15/07: 'oxblood' a secas + sin anti-collage
             outfit="full-coverage oxblood latex executive catsuit, high turtleneck neckline, long "
                     "fitted sleeves, full-length legs, " + OPAQUE_LOCK + ", " + CONSISTENCY_LOCK,
             seam=False,
             negative="red lips, oxblood, nipple piercings visible through clothing, split image"),
        dict(tag="L268-coverup", category="Bikini",  # 23/07: bikini + blusa cover-up ENCIMA -> SI exige manga
             outfit="aqua triangle bikini top, high-cut bottoms, with a sheer white chiffon blouse cover-up, "
                     "scoop neckline, micro hem",
             seam=False, negative=build_negative(lingerie=True)),  # tiene capa exterior -> guarda NO exime
    ]
    # Casos que DEBEN pasar limpios (ya con los locks + negative + bloque_a al dia):
    def _neg(**kw):
        return build_negative(**kw)
    good = [
        dict(tag="L732fix", category="Corporate power suit",
             outfit="ivory white vinyl blazer-dress with a plunging neckline, long sleeves, knee-length hem, "
                     "pencil skirt, " + GLOSS_LOCK + ", " + OPAQUE_LOCK + ", " + CONSISTENCY_LOCK,
             seam=False, negative=_neg(covered=True, gloss_risk=True)),
        dict(tag="L752fix", category="Corporate",
             outfit="midnight blue liquid latex blazer minidress with a plunging neckline, long sleeves, "
                     "mini hem, black back-seam stockings, " + GLOSS_LOCK + ", " + OPAQUE_LOCK + ", " + CONSISTENCY_LOCK,
             seam=True, negative=_neg(seam=True, covered=True, stockings=True)),
        dict(tag="L746fix", category="High-Fashion Editorial",
             outfit="black wet-look mermaid column gown, off-shoulder bardot neckline, long fitted sleeves to "
                     "the wrist, floor-length hem, oxblood cape, " + OPAQUE_LOCK + ", " + CONSISTENCY_LOCK,
             seam=False, negative=_neg(covered=True)),
        dict(tag="L742", category="Corporate",  # catsuit liquid latex: fija cuello alto+manga larga+full length
             outfit="black patent liquid latex catsuit, high mock neck, long sleeves, full-length legs, "
                     + OPAQUE_LOCK + ", " + CONSISTENCY_LOCK,
             seam=False, negative=_neg(covered=True)),
        dict(tag="L699", category="Stripper Stage",  # lenceria alto-corte: runas/ombligo on-brand, NO exige opaque;
             # teddy fija escote halter + sin mangas + alto-corte -> sin drift
             outfit="baby pink pvc high-cut teddy, halter neckline, sleeveless, high-cut micro hem, bare hips, exposed navel",
             seam=False, negative=_neg(lingerie=True)),
        dict(tag="L767fix", category="Escort Nightside",  # bodycon YA con OPAQUE_LOCK + negative + bloque_a al dia
             outfit="second-skin mini bodycon dress in high-gloss coral neon latex, halter neckline, "
                     "sleeveless, hem cut high on the thigh, " + OPAQUE_LOCK + ", " + CONSISTENCY_LOCK,
             seam=False, negative=_neg(covered=True),
             bloque_a="navel piercing, nipple piercings, " + SKIN_LOCK),
        dict(tag="L764fix", category="Corporate Coat-Dress",  # python-print YA con animal_print_lock
             outfit="jade vinyl coat-dress, plunging neckline, long sleeves, mid-thigh hem, sheer black "
                     "python-print back-seamed stockings, " + animal_print_lock("python") + ", "
                     + OPAQUE_LOCK + ", " + CONSISTENCY_LOCK,
             seam=True, negative=_neg(seam=True, covered=True, stockings=True, animal_print=True)),
        dict(tag="L124-sleeveless", category="Gym Performance",  # 23/07: sports-bra sin manga POR NATURALEZA
             outfit="neon pink latex sports bra with a halter neckline, high-waisted micro leggings with "
                     "neon side stripes, " + GLOSS_LOCK,  # neckline+hem fijos, manga inexistente -> NO debe flaggear
             seam=False, negative=_neg(gloss_risk=True)),
    ]
    print("=== DEBEN saltar (bad) ===")
    pb = audit_garment_batch(bad)
    for p in pb: print("  ", p)
    print("=== DEBEN pasar limpios (good) ===")
    pg = audit_garment_batch(good)
    for p in pg: print("  ", p)
    ok = (len(pb) >= 10 and len(pg) == 0)
    print("\nSelf-check:", "LIMPIO (bad detectados, good sin falsos positivos)" if ok
          else f"REVISAR (bad={len(pb)} esperado>=10, good={len(pg)} esperado 0)")
