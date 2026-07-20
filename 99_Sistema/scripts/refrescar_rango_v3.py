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
# Archivo historico L85-L199 (era Ele V3.5; L1-L84 es Helena y NO se toca). Vive en un fichero
# aparte pero la app lo lee igual — su filtro es `path.contains("galeria_outfits")`, verificado
# en GitRepository.kt:302 — asi que sus prompts fosilizados SI llegan al generador.
GAL_ARCHIVO = os.path.join(REPO, "00_Ele", "galeria_outfits_archivo.md")
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

# Aperturas literales de cada lock inyectado por v3. Marcan donde TERMINA la prenda y empieza
# el motor hablando de si mismo: sin este corte, re-clasificar un prompt ya v3 lee los locks
# como si fueran vestuario (ver `solo_prenda`).
LOCK_MARKERS = (
    "wherever the garment covers the body",          # SKIN_LOCK
    "the garment is solid and uncut",                # OPAQUE_LOCK
    "her hands, fingers, neck, throat",              # UNMARKED_ZONES
    "the stockings are exactly ONE single pair",     # HOSIERY_LOCK
    "the outfit is exactly ONE garment ensemble",    # CONSISTENCY_LOCK
    "rendered in a high-shine liquid latex",         # GLOSS_LOCK
    "beyond the garment's described sleeve length",  # NO_ARMWEAR
)


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


def solo_prenda(outfit):
    """Devuelve la descripcion REAL de la prenda, sin el preambulo de titulo/firma.

    El bloque de vestuario abre asi:
        stunning woman wearing a <TITULO DEL LOOK> <sub-arquetipo> signature in <familia>: <prenda>
    Clasificar sobre el texto completo hace que una palabra del TITULO decida la cobertura del
    CUERPO. Caso probado (L307, imagen del 19/07/2026): el titulo dice "Sports Bikini Crossfit"
    pero la prenda es un short de talle alto — `bikini` disparo pelvis_bare=True, el prompt
    NOMBRO las runas del hip crease sobre una zona tapada, y Gemini las pinto SOBRE el short.
    Mismo genero de bug que el L352: la palabra vivia en el titulo, no en la prenda.

    Y corta por el final en el primer LOCK. Un prompt ya en v3 lleva los locks pegados detras
    del outfit, y re-clasificarlo entero hace que el motor se lea A SI MISMO: "never split into a
    two-piece or cropped version" (CONSISTENCY_LOCK) disparaba `navel_bare` en 203 looks con el
    vientre tapado — vestidos hasta el suelo incluidos. Bucle de retroalimentacion: cada pasada
    de --todas sobre texto ya v3 corrompia lo que la pasada anterior habia calculado bien.
    """
    m = re.search(r"\bwearing\b(.{0,220}?):\s", outfit, re.S | re.I)
    prenda = outfit[m.end():] if m else outfit
    cortes = [prenda.find(mark) for mark in LOCK_MARKERS]
    cortes = [c for c in cortes if c != -1]
    return prenda[:min(cortes)] if cortes else prenda


def clasificar(outfit, categoria):
    """Deriva flags de cobertura (marcas) y de negativo desde el texto del outfit.

    SESGO DELIBERADO en las marcas: ante la duda, NO nombrar la zona. Nombrar una marca
    cubierta es una ORDEN DIRECTA de pintarla sobre la tela (el defecto que matamos);
    omitir una marca genuinamente desnuda solo hace que no se luzca. El costo es asimetrico.

    Las flags de COBERTURA (marcas) se derivan de la prenda sola (`solo_prenda`); las de
    NEGATIVO siguen mirando el texto completo — ahi el titulo es informacion util
    (p.ej. "Leopard" en el titulo justifica el animal_print_lock) y no ordena pintar nada.
    """
    t = solo_prenda(outfit).lower()
    t_full = outfit.lower()
    c = (categoria or "").lower()

    # Limite de palabra SOLO AL INICIO. Con \b a ambos lados "stocking" no matcheaba
    # "stockings" ni "back-seam" a "back-seamed" (se perdian los plurales y las flexiones:
    # la deteccion de costura caia de ~78 poses a 17). Con \b solo al inicio, "suit" sigue
    # sin matchear "swimsuit" — que era el falso positivo que marcaba un bikini como prenda
    # cerrada. Las trampas restantes se cierran con lookahead.
    TRAMPAS = {"mini": "malist", "rib": "bon", "coat": "ed"}

    def _busca(texto, ws):
        for w in ws:
            pat = r"\b" + re.escape(w) + (r"(?!%s)" % TRAMPAS[w] if w in TRAMPAS else "")
            if re.search(pat, texto):
                return True
        return False

    def has(*ws):        # cobertura del CUERPO -> solo la prenda (el titulo no desnuda a nadie)
        return _busca(t, ws)

    def has_full(*ws):   # locks/negativo -> texto completo, titulo incluido
        return _busca(t_full, ws)

    bikini = has("bikini", "monokini", "brazilian", "thong", "g-string", "microkini",
                 "swimsuit", "triangle top")
    lenceria = "lencer" in c
    # Piernas cubiertas: medias/leggings/catsuit/botas hasta el muslo tapan el muslo.
    # Bota sobre la rodilla = muslo TAPADO. La lista pedia la frase exacta "thigh-high boot" y no
    # cazaba "OTK thigh-high stiletto boots" (L356), asi que se evalua por PARES (altura + bota):
    # el adjetivo y el sustantivo casi nunca vienen pegados. Deliberadamente NO se acepta
    # "thigh-high" a secas: cazaria tambien las medias y moveria 47 looks que no he verificado.
    bota_alta = has("boot") and has("thigh-high", "thigh high", "over-the-knee", "otk")
    # Cualquier media cuenta como muslo tapado, no solo la opaca: una media ES tela sobre el
    # muslo, y nombrar ahi el tatuaje es exactamente el defecto confirmado el 13/07 (tatuajes
    # del brazo pintados SOBRE la manga de vinilo en L763/L764). Antes solo valia
    # "opaque stocking" y un look con medias violeta (L795) se ganaba marcas en el muslo.
    medias = has("stocking", "hosiery", "fishnet", "pantyhose", "thigh-high")
    piernas_tapadas = bool(bota_alta or medias) or has(
        "leggings", "tights", "catsuit", "thigh boot", "thigh-high boot",
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
        # NO agregar aqui disparadores tipo "exposed midriff"/"sports bra" (probado 19/07/2026):
        # suenan correctos y son ciertos, pero mueven 1.627 poses de golpe sin una sola imagen
        # que pruebe que hacen falta. El canon manda al reves — ante la duda NO se nombra la zona,
        # porque nombrar de mas ORDENA pintar sobre la tela y omitir solo deja un detalle sin lucir.
        navel_bare=bool((bikini and not has("monokini", "one-piece")) or has("crop", "two-piece")),
    )
    neg = dict(
        seam=has_full("back-seam", "back seam", "seamed stocking"),
        stockings=has_full("stocking", "hosiery", "thigh-high", "tights", "fishnet"),
        # Un bikini/monokini nunca es "prenda que cubre": NEG_CUTOUT pelearia con sus cortes.
        covered=bool(has_full("gown", "dress", "catsuit", "jumpsuit", "bodysuit", "leotard",
                              "suit", "blazer", "coat", "romper", "one-piece") and not bikini),
        gloss_risk=True,   # NEG_MATTE nunca choca: Ele jamas usa tela mate natural
        lingerie=lenceria,  # unico arquetipo donde el canon permite el mule
        animal_print=has_full("leopard", "tiger", "python", "snake", "zebra", "animal print"),
    )
    kind = next((k for k in ("leopard", "tiger", "python", "snake", "zebra") if k in t_full), None)
    # GLOSS_LOCK positivo solo en siluetas que primean tela mate (el resto ya dice vinyl/latex)
    mate_risk = has_full("suit", "blazer", "wool", "crepe", "satin", "rib", "knit", "tweed",
                         "tulle", "velvet", "tutu", "jersey", "cotton")
    consistencia = has_full("gown", "dress", "catsuit", "jumpsuit", "bodysuit", "leotard",
                            "romper")
    return flags, neg, kind, mate_risk, consistencia


# Quita la clausula de guantes del outfit (canon: manos siempre desnudas).
# EL PUNTO ESTA EXCLUIDO DE LA CLASE A PROPOSITO (bug 19/07/2026): con `[^,]*` el patron
# cruzaba el fin de frase y, en el L352 —cuyo TITULO contiene la palabra ("Burlesque Glove
# Tease")— se trago el token de unas Y la apertura entera del outfit, porque entre la coma
# anterior y la palabra "Glove" no habia ninguna otra coma. Al excluir `.` el borrado no
# puede salir de su propia oracion.
GLOVE_RE = re.compile(r",\s*[^,.]*\bglove[^,.]*", re.I)

# Segundo formato de clausula de guante (archivo historico L157-L199): el outfit se escribe con
# PUNTOS en vez de comas, asi que el guante es una ORACION entera y GLOVE_RE —que exige coma
# inicial— no la ve. Casos reales: L177/L182 "matching ivory cream vinyl elbow-length fitted
# gloves, seamless." y L187/L188 "Hot pink mesh fingerless opera gloves with claw cut-outs
# exposing French XXXL nails fully visible.". Se borra la oracion COMPLETA (son integramente de
# guante; las unas ya viven en el Bloque A). El `[^.]*` no cruza el punto: igual que en GLOVE_RE,
# el borrado no puede salirse de su propia oracion (leccion del L352).
GLOVE_SENT_RE = re.compile(r"(?<=\.)\s*[^.]*?\bglove[^.]*\.", re.I)


def quitar_guantes(texto):
    """Canon absoluto: manos SIEMPRE desnudas (feedback_guantes_prohibidos). Cubre los dos
    formatos de clausula y deja el espaciado limpio."""
    t = GLOVE_SENT_RE.sub(" ", texto)
    t = GLOVE_RE.sub("", t)
    return re.sub(r"  +", " ", t)


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
# PLURALES OBLIGATORIOS (bug 20/07/2026): `heel\b` NO caza "heels" — el \b de cierre exige que
# la palabra termine ahi. El L175 cierra su outfit en "8-inch clear stripper heels with rhinestone
# ankle straps" y quedaba SIN limite localizable: sus 7 poses fallaban enteras con "no se pudo
# ubicar el fin del outfit". Es la misma familia del bug de plurales ya documentado en `clasificar`
# (\b a ambos lados perdia "stockings"/"back-seamed"). `boots?/pumps?/sandals?` ya lo traian; los
# que faltaban eran justo los mas frecuentes como palabra final de la clausula de calzado.
SHOE_KW = re.compile(r"\b(pointed-toe|peep-toe|round-toe|platforms?|heels?|boots?|pumps?|"
                     r"sandals?|stilettos?|mules?|booties|bootie)\b", re.I)


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
            cola = prompt[ini + m.end():]
            # GUARDIA DE COLA NO VACIA (20/07/2026): el corte solo es valido si detras queda una
            # direccion de pose REAL. Cuando el outfit no nombra el calzado hasta despues de la
            # pose (L187 Ditzy/POV/Odalisque: la clausula se corta en los guantes y el zapato solo
            # reaparece DENTRO de la pose), el unico fin de frase con calzado detras es el punto
            # FINAL del prompt: `head` se traga el prompt entero y `cola` sale vacia. El resultado
            # era un prompt con SINGLE_FRAME al final y CERO pose — roto en silencio. Fallar aqui
            # lo manda a la lista de "requieren mano", que es lo correcto: son datos defectuosos.
            if len(cola.strip()) < 40:
                return None, None
            return prompt[:corte], cola
    return None, None


# Texto EXACTO del NO_ARMWEAR v2 (negacion-primero) que vive en L771-L800. La leccion del
# 15/07 es que Gemini obedece la descripcion AFIRMATIVA de la superficie deseada, asi que el
# v3 abre con la piel desnuda del brazo y recien despues veta las piezas.
NO_ARMWEAR_V2 = ("bare hands with no gloves of any kind, and beyond the garment's described "
                 "sleeve length the arms are genuinely bare skin, with no separate arm sleeves, "
                 "arm warmers, detached cuffs, forearm bands or elbow-length coverings added")


def upgrade_v2(prompt, label, marks_new):
    """Sube una pose de la capa v2 a v3 SUSTITUYENDO los bloques viejos (nunca appendeando:
    appendear deja SINGLE_FRAME y SKIN_LOCK duplicados)."""
    p = re.sub(r"a single continuous photograph.*?(?=, anatomically correct)",
               lambda _: SINGLE_FRAME, prompt, count=1, flags=re.S)
    if p == prompt:
        return None, "no se pudo delimitar el SINGLE_FRAME v2"
    if NO_ARMWEAR_V2 in p:
        p = p.replace(NO_ARMWEAR_V2, NO_ARMWEAR, 1)
    if len(MARKS_RE.findall(p)) == 1:
        p = MARKS_RE.sub(lambda m: m.group(1) + marks_new + m.group(3), p)
    if label == "Ditzy" and SINGLE_FRAME_TAIL not in p:
        p = re.sub(r",?\s*8k editorial fashion photography\.(\s*)$",
                   lambda mm: ", " + SINGLE_FRAME_TAIL +
                   ", 8k editorial fashion photography." + mm.group(1), p)
    return p, None


# ADN de busto pre-L185. La Ama fijo los implantes en 1000cc el 18/05/2026 y el token quedo
# declarado "Hard-Sync inamovible en BLOQUE A" (identidad_ele.md §II), reemplazando al antiguo
# `full bust`. El rango L157-L184 del archivo historico nunca se migro: 26 looks lo arrastran.
# La galeria viva tiene 0 ocurrencias, asi que esto solo toca al archivo.
BUST_VIEJO = "slender hourglass silhouette, full bust, wide hips"
BUST_CANON = ("slender hourglass silhouette, massive 1000cc breast implants each side, "
              "ultra high-profile, perfectly spherical augmented bust, obviously fake "
              "gravity-defying shape, wide hips")


def normalizar_adn(prompt):
    """Sube el Bloque A al ADN vigente. Se aplica ANTES de MARKS_RE porque el token de busto
    vive justo antes de 'wide hips, ', que es el ancla izquierda del span de marcas."""
    return prompt.replace(BUST_VIEJO, BUST_CANON)


def transformar(prompt, label, marks_new, locks, seam, canonico=True):
    """Cirugia sobre UNA pose pendiente. Devuelve (nuevo, motivo_si_falla)."""
    prompt = normalizar_adn(prompt)
    # Guardia por MARCADOR, no por la constante exacta: el rango L771+ trae una version
    # ANTERIOR de SINGLE_FRAME (v2, sin la clausula anti-espejo). Comparar contra la
    # constante v3 no la reconocia y le appendeaba la capa encima -> doble inyeccion.
    # El marcador estable es la frase de apertura.
    if "a single continuous photograph" in prompt:
        if SINGLE_FRAME in prompt:
            # Ya es v3 en su ESTRUCTURA, pero la clausula de marcas puede haber quedado mal
            # calculada por un bug de `clasificar` (caso L307, 19/07/2026: el titulo "Sports
            # Bikini" desnudaba una pelvis tapada por un short de talle alto y el generador
            # pintaba las runas SOBRE la tela). La estructura no basta: hay que reconciliar
            # tambien el contenido. Si las marcas ya coinciden, entonces si es idempotente.
            if len(MARKS_RE.findall(prompt)) == 1:
                resync = MARKS_RE.sub(lambda m: m.group(1) + marks_new + m.group(3), prompt)
                if resync != prompt:
                    return resync, None
            return None, "ya v3 (idempotente)"
        return upgrade_v2(prompt, label, marks_new)   # v2 -> v3: se SUSTITUYE, no se appendea

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
    head = quitar_guantes(head)              # canon: manos siempre desnudas
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
    gal = GAL_ARCHIVO if "--archivo" in sys.argv else GAL
    # newline="" en LECTURA y escritura: la galeria es CRLF y el proceso paralelo del bot
    # tambien la escribe. Leer con saltos universales convertiria todo a LF y el commit
    # saldria con el archivo entero reescrito (ver feedback_eol_bot_readmes).
    text = open(gal, encoding="utf-8", newline="").read()
    img = imagenes_existentes(lo, hi)

    parts = re.split(r"(?m)^(## .*?Look (\d+):.*)$", text)
    salida = [parts[0]]
    tot_pend = tot_ok = 0
    fallos, sin_guante, reporte, negs_nuevos = [], 0, [], []

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
            nuevo_body, n_sub = re.subn(
                r"(\*\*Negative Prompt:\*\*\s*)`[^`]*`",
                lambda mm: mm.group(1) + "`" + nuevo_neg + "`", nuevo_body, count=1)
            if not n_sub:
                # El look NUNCA tuvo bloque negativo (102 de 121 en el archivo historico). Sin el,
                # el positive pelea solo — el mismo agujero que costo 60 looks / 420 poses en el
                # L711 (feedback_negative_perdido_L711). Se INSERTA tras el ultimo fence de prompt,
                # que es donde vive en los looks que si lo traen (formato L181+).
                fences = list(re.finditer(r"```", nuevo_body))
                if fences:
                    corte = fences[-1].end()
                    eol = "\r\n" if "\r\n" in nuevo_body else "\n"
                    bloque = f"{eol}{eol}**Negative Prompt:** `{nuevo_neg}`{eol}"
                    nuevo_body = nuevo_body[:corte] + bloque + nuevo_body[corte:]
                    negs_nuevos.append(num)
                else:
                    fallos.append((num, "-", "sin fence: no se pudo insertar el negativo"))

        reporte.append((num, len(hechas), categoria[:22],
                        "".join(k[0].upper() if v else "·" for k, v in flags.items()),
                        "seam" if neg["seam"] else "", kind or ""))
        salida += [header, nuevo_body if apply else body]

    print(f"Rango {lo}-{hi}  |  poses pendientes: {tot_pend}  |  transformadas: {tot_ok}")
    print(f"Looks con guante retirado del outfit (canon manos desnudas): {sin_guante}")
    print(f"Looks que NO tenian bloque negativo y se les inserto ({len(negs_nuevos)}): {negs_nuevos}")
    print(f"\nFallos ({len(fallos)}) — requieren mano:")
    for f in fallos:
        print("   ", f)
    print("\nFlags por look  [A=arms B=back T=thighs P=pelvis N=navel]")
    for r in reporte:
        print(f"   L{r[0]}  {r[1]}p  {r[2]:<22} marcas={r[3]:<5} {r[4]:<4} {r[5]}")

    if apply:
        # ESCRIBIR SOBRE `gal`, NUNCA SOBRE `GAL` (incidente 20/07/2026): al agregar --archivo
        # cambie la lectura a `gal` y deje la escritura en la constante GAL -> el contenido del
        # ARCHIVO se escribio encima de galeria_outfits.md y borro 38.888 lineas de la galeria
        # viva. Se recupero con `git checkout` porque el arbol estaba limpio. Por eso el nombre
        # del fichero se imprime desde la variable: si vuelve a divergir, se ve en el reporte.
        open(gal, "w", encoding="utf-8", newline="").write("".join(salida))
        print(f"\n>>> APLICADO sobre {os.path.basename(gal)}")
    else:
        print("\n>>> DRY-RUN (sin escribir). Reejecutar con --apply")


if __name__ == "__main__":
    main()
