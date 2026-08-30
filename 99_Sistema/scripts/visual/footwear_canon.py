# -*- coding: utf-8 -*-
"""
Linter de CALZADO canonico para los inyectores de batch de Ele.

POR QUE EXISTE (Directiva Ama 09/07/2026 — "aplica los fix en el engine para que no pase"):
El calzado se redacta como token libre por look (Token de Calzado Bloqueado, 8 atributos) y
se pega verbatim en las 7 poses. Nada valida ese token -> se colaron errores de canon que
solo se cazaban mirando las imagenes ya generadas. Auditoria del batch blanco de novia
(L731-L740) encontro, sistematico:
  - open/peep toe CON medias (viola la regla de medias del 20/06: con medias -> puntera cerrada).
  - mule usado fuera de Lenceria (L734 Domestic) — mule ahora es EXCLUSIVO de Lenceria (Ama 09/07).
  - mule finito sin plataforma (L738 Lenceria) — el mule debe ser platform mule >=4" (Ama 09/07).

Este modulo NO genera calzado: LINTEA el token que escribe el inyector y devuelve la lista de
violaciones (vacia = limpio), igual que check_setting_variety / los self-checks de pose_rotation_v5.

USO OBLIGATORIO en todo inyector de batch (antes de escribir la galeria):
    from footwear_canon import audit_footwear_batch
    problems = audit_footwear_batch(LOOKS)   # LOOKS = lista de dicts por look
    if problems:
        for p in problems: print(p)
        raise SystemExit("Calzado no-canonico: corrige antes de cerrar el batch.")

Cada look (dict) necesita, como minimo:
    - "footwear"  : el token de calzado (str)               [claves alt: "calzado","shoe","heel"]
    - "outfit"    : la descripcion de prendas (str)         [claves alt: "garments","vestuario","prendas"]
                    -> se usa para detectar MEDIAS (stocking/fishnet/nylon/hold-up/bodystocking...).
    - "category"  : sub-arquetipo / categoria (str)         [claves alt: "subarchetype","subcategoria","archetype"]
                    -> se usa para saber si es Lenceria (unico arquetipo con mule permitido).
"""
import re

# --- Vocabulario de deteccion -------------------------------------------------
# MEDIAS: se detectan en la descripcion de PRENDAS (no en el token de calzado, para no confundir
# con "thigh-high BOOTS", que son calzado). Tokens inequivocos de hosiery.
HOSIERY = ["stocking", "fishnet", "nylon", "hosiery", "pantyhose", "bodystocking",
           "hold-up", "holdup", "seamed", "sheer sock", " media", "medias"]
# PUNTA ABIERTA prohibida con medias:
OPEN_TOE = ["open toe", "open-toe", "opentoe", "peep toe", "peep-toe", "peeptoe", "toe cleavage"]
# Calzado plano/no-canonico que NUNCA debe ir en el POSITIVE (va solo en el negative):
NON_CANON_POSITIVE = ["flat shoe", "flat sandal", "flats", "sneaker", "barefoot", "bare foot",
                      "kitten heel", "wedge", "block heel", "espadrille", "slipper", "ballet flat",
                      "loafer", "clog", "birkenstock", "ugg"]
# "chunky" produce tacon bloque -> prohibido en el positive (solo negative: "chunky heel").
CHUNKY = "chunky"
# Familias de arquetipo que cuentan como Lenceria (unico lugar con mule permitido):
LENCERIA_KEYS = ["lenc", "lingerie", "boudoir"]


_RX_CACHE = {}


def _rx(needle):
    """Regex de PALABRA COMPLETA para un termino del vocabulario.

    Antes esto era `needle in texto`, subcadena pura — y con 6 casos de prueba
    escritos a mano nunca se noto. Corrido por primera vez sobre la flota real
    (29/08/2026, auditar_canon_flota.py) el termino "ugg" salto en decenas de
    looks de Ele: la palabra que lo disparaba era **suggestion**. Mismo riesgo
    latente en "clog" (clogged), "wedge" (wedged) y " media" (immediate).

    Se permite el espacio y el guion internos de los terminos compuestos
    ("peep-toe", "flat shoe"), y se toleran ambos como separador.

    El sufijo `s?` NO es adorno: el vocabulario esta escrito en singular
    ("stocking", "sneaker", "wedge") y la galeria escribe en plural. Un `\b`
    seco al final los mataba — el primer intento de este fix bajo los casos
    detectados del self-check de 4 a 2 sin tocar una regla de canon. Es el
    tropiezo registrado en `feedback_fix_que_hace_pasar_puede_corromper`: hay
    que leer los casos que CAMBIAN de estado, no el contador.
    """
    if needle not in _RX_CACHE:
        cuerpo = r"[\s-]+".join(re.escape(p) for p in needle.strip().lower().split())
        _RX_CACHE[needle] = re.compile(r"\b%ss?\b" % cuerpo, re.I)
    return _RX_CACHE[needle]


def _has_any(text, needles):
    t = (text or "").lower()
    return [n.strip() for n in needles if _rx(n).search(t)]


def _platform_inches(footwear):
    """Devuelve la altura de PLATAFORMA en pulgadas si el token la declara, o None.
    Acepta pulgadas (4\", 4 inch, 4in) y cm (>=10cm ~ 4in). Busca el numero cercano a 'platform'."""
    t = (footwear or "").lower()
    best = None
    # patrones "<n> in/\" platform"  y  "platform ... <n> in/\""
    for m in re.finditer(r'(\d+(?:\.\d+)?)\s*(?:\"|inch(?:es)?|in)\b', t):
        # ¿hay 'platform' cerca (misma clausula, +-30 chars)?
        a, b = max(0, m.start()-30), min(len(t), m.end()+30)
        if "platform" in t[a:b]:
            val = float(m.group(1))
            best = val if best is None else max(best, val)
    for m in re.finditer(r'(\d+(?:\.\d+)?)\s*cm\b', t):
        a, b = max(0, m.start()-30), min(len(t), m.end()+30)
        if "platform" in t[a:b]:
            val = float(m.group(1)) / 2.54
            best = val if best is None else max(best, val)
    return best


def audit_footwear(footwear, garments="", archetype="", tag=""):
    """Lintea UN look. Devuelve lista de mensajes de violacion (vacia = limpio).
    tag = etiqueta libre para el mensaje (ej. 'L734')."""
    pre = f"[{tag}] " if tag else ""
    out = []
    fw = (footwear or "")
    is_mule = "mule" in fw.lower()
    is_lenceria = any(k in (archetype or "").lower() for k in LENCERIA_KEYS)
    # neutraliza negaciones ("no stockings"/"without hosiery") para no dar falso positivo (L698).
    garments_pos = re.sub(r"\bno\s+(stockings?|hosiery|tights|pantyhose|nylons?|bodystocking)\b", "",
                          garments or "", flags=re.I)
    medias = _has_any(garments_pos, HOSIERY)
    open_toe = _has_any(fw, OPEN_TOE)
    # 'sandal' ES puntera abierta por naturaleza: escribir "closed pointed toe
    # sandals" es un oximoron que Gemini resuelve al azar — el Standing de Miss
    # Doll L70 (29/08) declaraba exactamente eso y salio open-toe con medias.
    # La palabra manda sobre el atributo. (Nota Ama 29/08: "Open toe nunca con
    # medias, esa regla es para todas".)
    sandalia = ["sandal"] if "sandal" in fw.lower() else []

    # 1) MEDIAS + PUNTA ABIERTA (regla Ama 20/06 · universal a toda muñeca 29/08)
    if medias and (open_toe or sandalia):
        que = open_toe or sandalia
        out.append(f"{pre}MEDIAS + puntera abierta ({', '.join(que)}): con medias "
                   f"({', '.join(sorted(set(medias)))}) la puntera va CERRADA — y "
                   f"'sandal' cuenta como abierta aunque el texto diga 'closed toe' "
                   f"(regla 20/06, universal 29/08).")

    # 2) MULE fuera de Lenceria (regla Ama 09/07)
    if is_mule and not is_lenceria:
        out.append(f"{pre}MULE fuera de Lenceria (arquetipo='{archetype}'): el mule es EXCLUSIVO "
                   f"de Lenceria. Usa pump/bota/sandalia/plataforma stiletto.")

    # 3) MULE sin plataforma >=4\" (regla Ama 09/07) — aplica en Lenceria, donde el mule si va.
    if is_mule:
        plat = _platform_inches(fw)
        if plat is None:
            out.append(f"{pre}MULE sin plataforma declarada: debe ser platform mule >=4\" (~10cm).")
        elif plat < 4:
            out.append(f"{pre}MULE con plataforma {plat:.1f}\" < 4\": el mule debe ser platform >=4\".")

    # 4) Calzado no-canonico o 'chunky' en el POSITIVE
    non_canon = _has_any(fw, NON_CANON_POSITIVE)
    if non_canon:
        out.append(f"{pre}Calzado plano/no-canonico en el positive ({', '.join(non_canon)}): "
                   f"eso va SOLO en el negative. Ele siempre stiletto/Pleaser.")
    if CHUNKY in fw.lower():
        out.append(f"{pre}'chunky' en el token de calzado (positive): produce tacon bloque. "
                   f"Solo va en el negative ('chunky heel').")
    return out


def _get(look, *keys, default=""):
    for k in keys:
        if k in look and look[k]:
            return look[k]
    return default


def audit_footwear_batch(looks, footwear_keys=("footwear", "calzado", "shoe", "heel"),
                         garment_keys=("outfit", "garments", "vestuario", "prendas"),
                         archetype_keys=("category", "subarchetype", "subcategoria", "archetype")):
    """Lintea una lista de looks (dicts). Devuelve lista plana de violaciones de todo el batch."""
    problems = []
    for i, lk in enumerate(looks):
        tag = _get(lk, "tag", "id", "look", default=f"idx{i}")
        problems += audit_footwear(
            _get(lk, *footwear_keys),
            _get(lk, *garment_keys),
            _get(lk, *archetype_keys),
            tag=str(tag),
        )
    return problems


if __name__ == "__main__":
    import sys, io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

    # Casos del batch de novia que DEBEN saltar:
    bad = [
        dict(tag="L734", category="Domestic Trophy",
             outfit="white satin wrap mini-dress, sheer nude stockings with lace top, veil",
             footwear="white patent peep-toe mule slip-on, 12cm stiletto heel, no platform"),
        dict(tag="L737", category="Nightclub",
             outfit="white sequin mini-dress, thigh-high stockings with lace band, veil",
             footwear="white open-toe ankle-strap stiletto sandal 13cm"),
        dict(tag="L738", category="Lenceria Boudoir",
             outfit="ivory latex corset bodysuit, garter, sheer stockings, bridal veil",
             footwear="ivory peep-toe mule, 12cm stiletto heel"),  # mule OK arquetipo, pero open-toe+medias y sin platform
        dict(tag="MD70", category="Nightclub",
             outfit="magenta chrome bodysuit, sheer black hold-up stockings, suspender belt",
             footwear="platform stiletto sandals in mirror-chrome, 17cm heel, closed pointed toe"),  # 'sandal' gana al 'closed toe' (caso real 29/08)
    ]
    # Casos que DEBEN pasar limpios:
    good = [
        dict(tag="L735", category="Pin-Up",
             outfit="white latex wiggle dress, bare legs, veil",
             footwear="white patent closed pointed-toe stiletto pump 13cm"),
        dict(tag="L738fix", category="Lenceria Boudoir",
             outfit="ivory latex corset bodysuit, garter, sheer stockings, bridal veil",
             footwear="ivory closed-toe platform mule, 16cm stiletto heel + 4.5in platform"),
        dict(tag="L739", category="Bikini",
             outfit="white micro bikini, bare legs, veil",
             footwear="white open-toe ankle-strap stiletto sandal 13cm"),  # sin medias -> open toe OK
        dict(tag="MD70fix", category="Nightclub",
             outfit="magenta chrome bodysuit, sheer black hold-up stockings, suspender belt",
             footwear="closed pointed-toe platform stiletto pumps in mirror-chrome, 17cm heel"),  # pump cerrada + medias OK
    ]
    print("=== DEBEN saltar (bad) ===")
    pb = audit_footwear_batch(bad)
    for p in pb: print("  ", p)
    print("=== DEBEN pasar limpios (good) ===")
    pg = audit_footwear_batch(good)
    for p in pg: print("  ", p)
    ok = (len(pb) >= 4 and len(pg) == 0)
    print("\nSelf-check:", "LIMPIO (bad detectados, good sin falsos positivos)" if ok
          else f"REVISAR (bad={len(pb)} esperado>=4, good={len(pg)} esperado 0)")
