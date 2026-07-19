# -*- coding: utf-8 -*-
"""
Refresco v3 de prompts fosilizados en galeria_outfits.md — SOLO poses SIN imagen.

POR QUE (Ama 18/07/2026): los prompts del rango 300+ FOSILIZAN (feedback_prompts_fosilizan):
guardan el texto de su epoca. El rango arrastra el Bloque A que nombra INCONDICIONALMENTE
"outer thighs" + "navel piercing" (-> Gemini las pinta SOBRE la tela cuando el outfit cubre
esas zonas), sin SINGLE_FRAME (anti-collage), sin SKIN_LOCK/UNMARKED_ZONES/NO_ARMWEAR y con
el negativo en formato v1 (sin la familia anti-collage ni anti-marca-a-traves-de-tela).

REGLA DE ORO: las poses que YA TIENEN IMAGEN NO SE TOCAN. La verdad de que imagenes existen
es `git ls-files` (el tracker de la galeria MIENTE — feedback_tracker_galeria_miente; y el
disco de esta maquina esta en sparse checkout, sin PNGs).

METODO — CIRUGIA, no regeneracion: la direccion de pose ya trae los anclas del 12/07
(anatomica, seated, odalisca, frontalidad) CON sus props armonizados al ambiente. Regenerar
con rotate_poses() perderia esos props (volverian a "a surface" generico). Se conserva el
texto y se le AGREGA la capa v3.

Uso:  python refrescar_rango_v3.py <desde> <hasta> [--apply]
      (sin --apply = dry-run: solo reporte de flags y conteos)
"""
import sys, io, re, os, subprocess
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(REPO) if os.path.basename(REPO) == "99_Sistema" else REPO
REPO = r"c:\Users\farid\LaVouteDAnais"
sys.path.insert(0, os.path.join(REPO, "99_Sistema", "scripts", "visual"))

from pose_rotation_v5 import (
    build_marks_clause, build_negative, SINGLE_FRAME, SINGLE_FRAME_TAIL,
    SKIN_LOCK, UNMARKED_ZONES, NO_ARMWEAR, OPAQUE_LOCK, GLOSS_LOCK,
    HOSIERY_LOCK, CONSISTENCY_LOCK, animal_print_lock,
    STOCKING_SEAM_FRONT, STOCKING_SEAM_BACK, FULL_ANCHOR, HANDS_ANCHOR,
    STANDING_ANCHOR, find_forbidden,
)

GAL = os.path.join(REPO, "00_Ele", "galeria_outfits.md")
POSE_LABELS = ["Standing", "Back View", "Seated", "Side Profile", "Ditzy", "POV", "Odalisque"]
LABEL2TOKEN = {"Standing": "standing", "Back View": "back_view", "Seated": "seated",
               "Side Profile": "side_profile", "Ditzy": "ditzy", "POV": "pov",
               "Odalisque": "odalisque"}
POSE_TOKENS = ["back_view", "side_profile", "standing", "seated", "ditzy", "pov", "odalisque"]
SEAM_SKIP = {"Side Profile"}

# Segmento de marcas del Bloque A. NO es una cadena fija: conviven 4 redacciones segun la
# epoca del look (con/sin runa pelvica, "subtle navel piercing" vs "navel piercing", y las
# 280+910 que todavia arrastran la frase-orden PROHIBIDA "nipple piercings pressing against
# and visible under clothing"). Lo estable son los DOS EXTREMOS: el segmento va siempre entre
# "wide hips, " y el token de maquillaje ("dramatic editorial makeup" en los viejos,
# "aggressive bimbomakeup" en los nuevos) que precede a las unas.
MARKS_RE = re.compile(
    r"(wide hips, )(.*?)(, [^,]*makeup[^,]*, extra long French XXXL nails)", re.S)
SPLIT = ". anatomically correct"


def imagenes_existentes(lo, hi):
    """look -> set(pose_token) segun git ls-files (fuente de verdad)."""
    pats = sorted({f"05_Imagenes/ele/look{n // 100}*" for n in (lo, hi)})
    out = ""
    for p in pats:
        out += subprocess.run(["git", "ls-files", p], cwd=REPO,
                              capture_output=True, text=True).stdout
    img = {}
    for line in out.splitlines():
        m = re.search(r"/look(\d+)_[^/]*/(ele_[^/]+\.png)$", line)
        if not m:
            continue
        look = int(m.group(1))
        if not (lo <= look <= hi):
            continue
        fn = re.sub(r"_\d{6,}$", "", m.group(2)[:-4])
        for t in POSE_TOKENS:
            if fn.endswith(t):
                img.setdefault(look, set()).add(t)
                break
    return img


def clasificar(outfit, categoria):
    """Deriva flags de cobertura (marcas) y de negativo desde el texto del outfit.

    SESGO DELIBERADO en las marcas: ante la duda, NO nombrar la zona. Nombrar una marca
    cubierta es una ORDEN DIRECTA de pintarla sobre la tela (el defecto que matamos);
    omitir una marca genuinamente desnuda solo hace que no se luzca. El costo es asimetrico.
    """
    t = outfit.lower()
    c = (categoria or "").lower()

    # Limite de palabra SOLO AL INICIO. Con \b a ambos lados "stocking" no matcheaba
    # "stockings" ni "back-seam" a "back-seamed" (se perdian los plurales y las flexiones:
    # la deteccion de costura caia de ~78 poses a 17). Con \b solo al inicio, "suit" sigue
    # sin matchear "swimsuit" — que era el falso positivo que marcaba un bikini como prenda
    # cerrada. Las trampas restantes se cierran con lookahead.
    TRAMPAS = {"mini": "malist", "rib": "bon", "coat": "ed"}

    def has(*ws):
        for w in ws:
            pat = r"\b" + re.escape(w) + (r"(?!%s)" % TRAMPAS[w] if w in TRAMPAS else "")
            if re.search(pat, t):
                return True
        return False

    bikini = has("bikini", "monokini", "brazilian", "thong", "g-string", "microkini",
                 "swimsuit", "triangle top")
    lenceria = "lencer" in c
    # Piernas cubiertas: medias/leggings/catsuit/botas hasta el muslo tapan el muslo.
    piernas_tapadas = has("leggings", "tights", "catsuit", "thigh boot", "thigh-high boot",
                          "opaque stocking", "full-length", "jumpsuit", "unitard")
    muslo_libre = has("bikini", "monokini", "brazilian", "thong", "g-string", "high-cut",
                      "micro", "mini", "hot pants", "shorts", "cheeky", "teddy", "leotard")

    flags = dict(
        arms_bare=not has("long sleeve", "long-sleeve", "long fitted sleeve", "full sleeve",
                          "turtleneck", "long gauntlet"),
        back_bare=has("halter", "backless", "open back", "open-back", "strapless", "bandeau",
                      "bikini", "racerback", "cross-back", "deep open back"),
        thighs_bare=bool(muslo_libre and not piernas_tapadas),
        pelvis_bare=bool(bikini or (lenceria and has("high-cut", "thong", "g-string", "brazilian"))),
        navel_bare=bool((bikini and not has("monokini", "one-piece")) or has("crop", "two-piece")),
    )
    neg = dict(
        seam=has("back-seam", "back seam", "seamed stocking"),
        stockings=has("stocking", "hosiery", "thigh-high", "tights", "fishnet"),
        # Un bikini/monokini nunca es "prenda que cubre": NEG_CUTOUT pelearia con sus cortes.
        covered=bool(has("gown", "dress", "catsuit", "jumpsuit", "bodysuit", "leotard", "suit",
                         "blazer", "coat", "romper", "one-piece") and not bikini),
        gloss_risk=True,   # NEG_MATTE nunca choca: Ele jamas usa tela mate natural
        lingerie=lenceria,  # unico arquetipo donde el canon permite el mule
        animal_print=has("leopard", "tiger", "python", "snake", "zebra", "animal print"),
    )
    kind = next((k for k in ("leopard", "tiger", "python", "snake", "zebra") if k in t), None)
    # GLOSS_LOCK positivo solo en siluetas que primean tela mate (el resto ya dice vinyl/latex)
    mate_risk = has("suit", "blazer", "wool", "crepe", "satin", "rib", "knit", "tweed",
                    "tulle", "velvet", "tutu", "jersey", "cotton")
    consistencia = has("gown", "dress", "catsuit", "jumpsuit", "bodysuit", "leotard", "romper")
    return flags, neg, kind, mate_risk, consistencia


GLOVE_RE = re.compile(r",\s*[^,]*\bglove[^,]*", re.I)


def construir_locks(neg, kind, mate_risk, consistencia):
    locks = [SKIN_LOCK, UNMARKED_ZONES, NO_ARMWEAR]
    if neg["covered"]:
        locks.append(OPAQUE_LOCK)
    if mate_risk:
        locks.append(GLOSS_LOCK)
    if neg["stockings"]:
        locks.append(HOSIERY_LOCK)
    if consistencia:
        locks.append(CONSISTENCY_LOCK)
    if kind:
        locks.append(animal_print_lock(kind))
    return ", ".join(locks)


# Fallback para prompts SIN ancla anatomica (formato pre-12/07 y los "Pose Set Stripper"):
# el unico limite fiable entre el outfit y la pose es el final de la clausula de CALZADO —
# el outfit siempre cierra nombrando el zapato. Se busca la ultima palabra de calzado y el
# primer ". " despues de ella.
SHOE_KW = re.compile(r"\b(pointed-toe|peep-toe|round-toe|platform|heel|boots?|pumps?|sandals?|"
                     r"stiletto|mule)\b", re.I)


def _cortar_sin_ancla(prompt):
    """Devuelve (head, pose_y_setting) o (None, None) si no se puede ubicar el limite.

    OJO: no sirve la ULTIMA mencion de calzado — el zapato se vuelve a nombrar dentro de la
    pose ("pointed in the platform stiletto"). El limite es el PRIMER fin de frase, ya pasado
    el Bloque A, que tenga alguna palabra de calzado por detras: ahi cerro el outfit.
    """
    dna = prompt.find("5cm. ")
    ini = dna + 5 if dna != -1 else 0
    for m in re.finditer(r"\.\s+", prompt[ini:]):
        corte = ini + m.start()
        if SHOE_KW.search(prompt[ini:corte]):
            return prompt[:corte], prompt[ini + m.end():]
    return None, None


def transformar(prompt, label, marks_new, locks, seam, canonico=True):
    """Cirugia sobre UNA pose pendiente. Devuelve (nuevo, motivo_si_falla)."""
    # Guardia por MARCADOR, no por la constante exacta: el rango L771+ trae una version
    # ANTERIOR de SINGLE_FRAME (v2, sin la clausula anti-espejo). Comparar contra la
    # constante v3 no la reconocia y le appendeaba la capa encima -> doble inyeccion
    # (26 poses). El marcador estable es la frase de apertura.
    if "a single continuous photograph" in prompt:
        if SINGLE_FRAME in prompt:
            return None, "ya v3 (idempotente)"
        return None, "capa v2 previa — requiere upgrade v2->v3, no append"

    if prompt.count(SPLIT) == 1:
        head, tail = prompt.split(SPLIT, 1)
        tail = "anatomically correct" + tail
    else:
        # Sin ancla: hay que ubicar el limite Y fabricar el ancla que nunca tuvo.
        head, pose = _cortar_sin_ancla(prompt)
        if head is None:
            return None, "no se pudo ubicar el fin del outfit"
        anchor = HANDS_ANCHOR if label in ("Ditzy", "POV") else FULL_ANCHOR
        # Las anclas de SLOT solo valen si la pose es la canonica de ese slot. En un
        # "Pose Set Stripper" el slot 1 es un Pole Climb: pegarle STANDING_ANCHOR
        # ("a FRONT view: NOT a back view") contradiria la pose escrita.
        if canonico and label == "Standing":
            anchor += ", " + STANDING_ANCHOR
        tail = anchor + ", " + pose

    if len(MARKS_RE.findall(head)) != 1:
        return None, "span de marcas no encontrado"

    head = MARKS_RE.sub(lambda m: m.group(1) + marks_new + m.group(3), head)
    head = GLOVE_RE.sub("", head)            # canon: manos siempre desnudas
    head = head.rstrip().rstrip(",")

    if seam and label not in SEAM_SKIP:
        anchor = HANDS_ANCHOR if label in ("Ditzy", "POV") else FULL_ANCHOR
        seam_cl = STOCKING_SEAM_BACK if label == "Back View" else STOCKING_SEAM_FRONT
        if anchor in tail:
            tail = tail.replace(anchor, anchor + ", " + seam_cl, 1)

    nuevo = head + ", " + locks + ". " + SINGLE_FRAME + ", " + tail

    if label == "Ditzy":  # reincidente del collage: primacia + recencia
        # El (\s*) final se RECUPERA: comerselo pegaria el cierre ``` al prompt y rompe el bloque.
        nuevo = re.sub(r",?\s*8k editorial fashion photography\.(\s*)$",
                       lambda mm: ", " + SINGLE_FRAME_TAIL +
                       ", 8k editorial fashion photography." + mm.group(1),
                       nuevo)
    return nuevo, None


def main():
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    apply = "--apply" in sys.argv
    todas = "--todas" in sys.argv
    # newline="" en LECTURA y escritura: la galeria es CRLF y el proceso paralelo del bot
    # tambien la escribe. Leer con saltos universales convertiria todo a LF y el commit
    # saldria con el archivo entero reescrito (ver feedback_eol_bot_readmes).
    text = open(GAL, encoding="utf-8", newline="").read()
    img = imagenes_existentes(lo, hi)

    parts = re.split(r"(?m)^(## .*?Look (\d+):.*)$", text)
    salida = [parts[0]]
    tot_pend = tot_ok = 0
    fallos, sin_guante, reporte = [], 0, []

    for i in range(1, len(parts), 3):
        header, num, body = parts[i], int(parts[i + 1]), parts[i + 2]
        if not (lo <= num <= hi):
            salida += [header, body]
            continue

        # --todas (Ama 19/07/2026): barrer TAMBIEN las poses que ya tienen imagen. Motivo:
        # la Ama regenero varias de esas poses y "siguen con los errores" — porque el prompt
        # viejo es el que ORDENA el defecto (guantes, marcas sobre la tela). Sin este flag
        # solo se tocan las pendientes, que era la regla anterior.
        have = set() if todas else img.get(num, set())
        pendientes = [l for l in POSE_LABELS if LABEL2TOKEN[l] not in have]
        if not pendientes:
            salida += [header, body]
            continue

        # Clave POSICIONAL, no por nombre: los looks "Pose Set Stripper" (p.ej. L391/L398)
        # reemplazan las 7 poses canonicas por poses de pole/escenario ("Pole Climb",
        # "Stage Walk"...). El uploader igual nombra los PNG por slot canonico y posicion
        # (slot 1 -> ele_NNN_standing.png), asi que la posicion es el unico mapeo fiable.
        # Dos formatos de encabezado conviven: "**1. Standing:**" (hasta L710) y
        # "**Standing:**" sin numero (desde L711). El numero es opcional; si falta,
        # el slot se resuelve por nombre.
        bloques = list(re.finditer(r"(\*\*(?:(\d)\.)?\s*([^:*]+):\*\*\s*```)(.*?)(```)",
                                   body, re.S))
        by_label, coincidencias = {}, 0
        for m in bloques:
            nombre = m.group(3).split("(")[0].strip()
            if m.group(2):
                idx = int(m.group(2))
                if not (1 <= idx <= 7):
                    continue
                slot = POSE_LABELS[idx - 1]
            elif nombre in POSE_LABELS:
                slot = nombre
            else:
                continue
            by_label[slot] = m
            if nombre == slot:
                coincidencias += 1
        # Look canonico = sus 7 poses son las del canon. Si no, es un "Pose Set Stripper"
        # (pole/escenario) y NO debe recibir anclas de slot.
        canonico = coincidencias >= 4
        categoria = (re.search(r"\*\*Categoría:\*\*\s*(.+)", body) or None)
        categoria = categoria.group(1).strip() if categoria else ""

        # outfit de referencia: de cualquier pose (el Bloque A+outfit es identico en las 7)
        ref = next((by_label[l].group(4) for l in POSE_LABELS if l in by_label), "")
        outfit = ref.split(SPLIT)[0] if SPLIT in ref else ref
        outfit = outfit.split("5cm.", 1)[-1]

        flags, neg, kind, mate_risk, consistencia = clasificar(outfit, categoria)
        marks_new = build_marks_clause(**flags)
        locks = construir_locks(neg, kind, mate_risk, consistencia)
        if GLOVE_RE.search(outfit):
            sin_guante += 1

        nuevo_body = body
        hechas = []
        for lab in pendientes:
            tot_pend += 1
            m = by_label.get(lab)
            if not m:
                fallos.append((num, lab, "prompt no parseado"))
                continue
            nuevo, err = transformar(m.group(4), lab, marks_new, locks, neg["seam"], canonico)
            if err:
                fallos.append((num, lab, err))
                continue
            if find_forbidden(nuevo):
                fallos.append((num, lab, "frase-orden prohibida en el resultado"))
                continue
            nuevo_body = nuevo_body.replace(m.group(0), m.group(1) + nuevo + m.group(5), 1)
            hechas.append(lab)
            tot_ok += 1

        if hechas:
            nuevo_neg = build_negative(**neg)
            nuevo_body = re.sub(
                r"(\*\*Negative Prompt:\*\*\s*)`[^`]*`",
                lambda mm: mm.group(1) + "`" + nuevo_neg + "`", nuevo_body, count=1)

        reporte.append((num, len(hechas), categoria[:22],
                        "".join(k[0].upper() if v else "·" for k, v in flags.items()),
                        "seam" if neg["seam"] else "", kind or ""))
        salida += [header, nuevo_body if apply else body]

    print(f"Rango {lo}-{hi}  |  poses pendientes: {tot_pend}  |  transformadas: {tot_ok}")
    print(f"Looks con guante retirado del outfit (canon manos desnudas): {sin_guante}")
    print(f"\nFallos ({len(fallos)}) — requieren mano:")
    for f in fallos:
        print("   ", f)
    print("\nFlags por look  [A=arms B=back T=thighs P=pelvis N=navel]")
    for r in reporte:
        print(f"   L{r[0]}  {r[1]}p  {r[2]:<22} marcas={r[3]:<5} {r[4]:<4} {r[5]}")

    if apply:
        open(GAL, "w", encoding="utf-8", newline="").write("".join(salida))
        print("\n>>> APLICADO sobre galeria_outfits.md")
    else:
        print("\n>>> DRY-RUN (sin escribir). Reejecutar con --apply")


if __name__ == "__main__":
    main()
