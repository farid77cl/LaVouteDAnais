# -*- coding: utf-8 -*-
"""Motor de tres bloques — A cuerpo · B outfit · C toma — con campos de dueño único.

Concepto de la Ama (09/09/2026): *«el bloque A es donde se describe el físico,
no debería cambiar entre prompts; el bloque B debería describir el outfit,
tampoco debería variar; el bloque C debería describir pose y ambiente»*. Y su
experiencia manda: *«mientras más detalles menos desviación»*.

La ley que sale de ahí: **un atributo, un campo, un bloque.** El detalle es
bienvenido; dos cláusulas sobre el mismo atributo son una pelea, y en la pelea
gana la de más peso, que es la equivocada (L831: la falda que se abrió). Los
tres bloques responden CUÁNDO cambia el texto (nunca / por look / por pose), y
dentro de cada uno no hay párrafo sino campos con nombre y dueño — así la
contradicción es imposible por construcción, no por detector.

El contrato vive en `campos.json` (dueño único). Este módulo lo carga, lo
valida y ensambla. Spec: `99_Sistema/specs/2026-09-09-motor-tres-bloques-design.md`.

**Un personaje nuevo es dato, nunca código** (Ama: *«debe ser flexible para
poder agregar nuevos personajes»*): perfil + entrada en `anclas_universales.json`
+ repertorio. Cero `.py`. Por eso el orden de campos A es universal.
"""
from __future__ import annotations

import json
import os
import re

AQUI = os.path.dirname(os.path.abspath(__file__))
JSON_CAMPOS = os.path.join(AQUI, "campos.json")
JSON_ANCLAS = os.path.join(AQUI, "anclas_universales.json")

_CACHE = {}


def cargar_campos(ruta=JSON_CAMPOS):
    """El contrato, cargado una vez. Lista vacía de campos = contrato roto."""
    if ruta not in _CACHE:
        with open(ruta, encoding="utf-8") as fh:
            c = json.load(fh)
        if not c.get("campos"):
            raise ValueError("campos.json sin campos: el contrato está vacío")
        _CACHE[ruta] = c
    return _CACHE[ruta]


# ======================================================================
# A · el cuerpo, por campos, desde la cerca compartida
# ======================================================================
# Un dueño, dos lectores. La cerca `ADN:BLOQUE_A` del perfil pasa a UNA LÍNEA
# POR CAMPO en el orden universal de `orden_A`, cada línea cerrando en coma.
# El motor viejo (`PromptBuilder.bloque_a`) la une con `_limpiar` y obtiene el
# mismo texto de siempre; este módulo la parte. Una línea vacía = campo que esa
# muñeca no tiene. Así una muñeca nueva llena, no configura.

from prompt_builder import PromptBuilder, cargar_config, _log_evento  # noqa: E402


def personajes(config=None):
    """Los slugs registrados en anclas_universales.json — nunca una lista escrita acá."""
    return sorted((config or cargar_config()).get("personajes", {}))


def _ruta_perfil(slug, config=None):
    perfil = (config or cargar_config())["personajes"][slug]
    rel = perfil["perfil_visual"]
    return os.path.normpath(os.path.join(AQUI, "..", "..", "..", rel.replace("/", os.sep)))


def lineas_adn(slug, config=None):
    """Las líneas crudas de la cerca, tal cual (vacías incluidas)."""
    with open(_ruta_perfil(slug, config), encoding="utf-8") as fh:
        m = PromptBuilder._RX_ADN.search(fh.read())
    if not m:
        raise ValueError("el perfil de '%s' no tiene la cerca %s" % (slug, PromptBuilder.MARCA_ADN))
    return m.group(1).split("\n")


def campos_a(slug, config=None):
    """{campo: texto} en el orden universal. Texto '' = la muñeca no tiene ese campo."""
    orden = cargar_campos()["orden_A"]
    lineas = lineas_adn(slug, config)
    if len(lineas) != len(orden):
        raise ValueError(
            "la cerca de '%s' tiene %d líneas y el orden universal de A tiene %d campos: "
            "una línea por campo, vacía si no aplica (%s)"
            % (slug, len(lineas), len(orden), ", ".join(orden)))
    return {campo: PromptBuilder._limpiar(l).rstrip(",").strip() for campo, l in zip(orden, lineas)}


# Vocabulario que NO puede aparecer en A. Se mide, no se promete.
# B: prenda, calzado, forma/largo de uña, corsetería. (El COLOR de sombra o de
# labios no está acá a propósito: hoy vive en A por herencia y moverlo a B
# cambia el motor viejo — decisión de la Ama, pendiente.)
RX_VOCAB_B = re.compile(
    r"\b(?:wearing|stiletto heels?|stiletto pumps?|pumps?|sandals?|boots?|platform|"
    r"corset|tightlacing|waist training|fingernails?|stiletto-shaped|thong|g-string|"
    r"stockings?|gloves?|dress|skirt|bodysuit|bikini(?! line))\b", re.I)
# «bikini line» es zona anatómica (los tatuajes de Ele van «along one hip crease
# at the bikini line»), no una prenda. Medido: el primer barrido lo marcó.
# C: pose, orientación y encuadre. (La LUZ tampoco está acá a propósito: Anaïs
# lleva «cinematic chiaroscuro… George Hurrell portraiture» en su ADN por
# herencia; sacarla cambia el motor viejo — decisión de la Ama, pendiente.)
RX_VOCAB_C = re.compile(
    # «sitting» pelado es AJUSTE de prenda («the band sitting on the natural
    # waist», «a thin waistband sitting high on the hip bones» — los dos medidos
    # en el L831 real); la pose en este corpus dice «seated» o «sitting down/
    # upright». Y «the frame» solo no es pose ni cámara: GARMENT_EXCLUSION_LOCK,
    # que es B, dice «not present anywhere in the frame».
    # Y «lying» pelado es COLOCACIÓN («a fine mirror-silver chain lying across
    # the ribcage», L829 real); la pose dice «lying down/back/flat».
    r"\b(?:standing|seated|sitting\s+(?:down|upright|up)|kneeling|reclining|"
    r"lying\s+(?:down|back|flat|prone|supine)|from behind|back view|"
    r"side profile|three-quarter|low angle|full body|close-up|the lens|the camera|"
    r"aspect ratio|looking at|gaze (?:locked|drifting))\b", re.I)


# ======================================================================
# B · lo que lleva puesto, por campos, desde el batch
# ======================================================================
# El batch ya declara `bloque_b` como párrafo y eso NO se rompe: un look viejo
# entra entero como `prenda_principal`. Un look nuevo declara `campos_b` como
# dict por campo, y el orden de salida es SIEMPRE el del contrato, no el del
# dict — así el prompt es idéntico sin importar cómo lo escribió quien lo hizo.

class CampoFaltante(ValueError):
    """Un campo obligatorio del contrato no viene en el look."""


class CampoDesconocido(ValueError):
    """El look declara un campo que el contrato no conoce. Se dice cuál y se
    sugieren los válidos: 'zapatos' no pasa en silencio cuando el campo es
    'calzado' — un campo mal escrito es un atributo que nunca llega a Gemini."""


def _campos_de(bloque):
    return [c for c in cargar_campos()["campos"] if c["bloque"] == bloque]


def campos_b(look, estricto=False):
    """{campo: texto} de B en el orden del contrato, solo los que el look trae.

    look["campos_b"]  -> dict por campo (batches nuevos)
    look["bloque_b"]  -> párrafo entero como prenda_principal (batches viejos)
    estricto=True     -> exige los obligatorios (lo usa la puerta, no el lector)
    """
    contrato = _campos_de("B")
    validos = [c["id"] for c in contrato]
    if "campos_b" in look:
        crudo = dict(look["campos_b"])
        raros = sorted(set(crudo) - set(validos))
        if raros:
            raise CampoDesconocido(
                "campo(s) de B que el contrato no conoce: %s. Válidos: %s"
                % (", ".join(raros), ", ".join(validos)))
    else:
        crudo = {"prenda_principal": look.get("bloque_b", "")}
    salida = {}
    for c in contrato:
        t = PromptBuilder._limpiar(crudo.get(c["id"], ""))
        if t:
            salida[c["id"]] = t
        elif estricto and c["obligatorio"]:
            raise CampoFaltante("falta el campo obligatorio de B: %s" % c["id"])
    return salida


def fugas_b(campos):
    """Vocabulario de C (pose, cámara, encuadre) dentro de un campo de B."""
    return ["B/%s: «%s» es vocabulario de C (pose/cámara)" % (k, m.group(0))
            for k, t in campos.items() for m in [RX_VOCAB_C.search(t or "")] if m]


# ======================================================================
# C · la toma, por campos — repertorio + slot + setting, y lo condicional a B
# ======================================================================

class BloquesBuilder(PromptBuilder):
    """El motor nuevo. Hereda el ACCESO A DATOS que ya funciona (perfil,
    repertorio de sub-poses y su rotación, negativo base, anclas) y reemplaza
    el ENSAMBLADO. Misma superficie que `generar` exige del builder viejo.

    Después de cada `build()` deja `ultimo_por_bloque` ({'A','B','C'} en texto)
    y `ultimo_reporte` (chars y palabras por bloque): el largo se MIDE en cada
    emisión, no se impone — el A/B decide.
    """

    ultimo_por_bloque = None
    ultimo_reporte = None

    def build(self, bloque_a, bloque_b, slot, pose_text, setting,
              extra_final=None, extra_anclas=None, auto_opt_in=True,
              eco_busto_declarado=None):
        """Misma firma que el motor viejo, ensamblado nuevo: A. B. C.

        bloque_a  : None = la cerca del perfil por campos (dueño único). Un str
                    explícito entra entero como un solo campo (batches viejos).
        bloque_b  : el LOOK del batch (dict con `campos_b` o `bloque_b`) o el
                    párrafo (str) — los dos caminos emiten.
        pose_text : la sub-pose ya resuelta por `pose()`; None = sacarla acá.
        eco_busto_declarado se ignora a propósito: los ecos que re-describen la
        prenda murieron con este motor (C solo REFERENCIA a B).
        """
        look = bloque_b if isinstance(bloque_b, dict) else {"bloque_b": bloque_b or ""}
        slot_n = self.normalizar_slot(slot)
        ruta = _mapa_anclas_a_campos()

        # ---- A: la cerca por campos + las anclas de cuerpo (fotorrealismo)
        A = ({"cuerpo": self._limpiar(bloque_a)} if bloque_a
             else campos_a(self.slug, self.cfg))
        # ---- B: los campos del look + las anclas de PRENDA que le tocan
        B = campos_b(look)
        texto_b = " ".join(B.values())
        nombres = list(self.anclas_de_slot(slot_n)) + [n for n in (extra_anclas or []) if n]
        if auto_opt_in:
            nombres += [n for n in self.opt_in_de(texto_b) if n not in nombres]
        kind = self.animal_print_kind(texto_b) if "ANIMAL_PRINT_LOCK" in nombres else None
        for n in nombres:
            if n == "BOTTOM_CUT_LOCK":
                if "BOTTOM_CUT_LOCK" in self.anclas_siempre:
                    # Solo el CORTE, exposición-neutro. La exposición es C.
                    B["calzon"] = ", ".join(x for x in (B.get("calzon"), self.anclas[n]["texto_corte"]) if x)
                continue
            bloque, campo = ruta.get(n, (None, None))
            if bloque not in ("A", "B"):
                continue                     # las de C las pone campos_c
            t = self.anclas[n]["texto"]
            if "{kind}" in t:
                if not kind:
                    continue                 # sin especie no se escribe un candado a medias
                t = t.replace("{kind}", kind)
            dest = A if bloque == "A" else B
            dest[campo] = ", ".join(x for x in (dest.get(campo), t) if x)
        B = {c["id"]: B[c["id"]] for c in _campos_de("B") if c["id"] in B}
        A = {k: A[k] for k in (list(A) if bloque_a else cargar_campos()["orden_A"] + ["fotorrealismo"]) if A.get(k)}
        # ---- C: la toma
        C = campos_c(self, slot_n, int(look.get("numero", 0) or 0), setting, look,
                     props=look.get("props"), postura=pose_text, extra_anclas=extra_anclas)
        if extra_final:
            C["ambiente"] = ", ".join(x for x in (C.get("ambiente"), self._limpiar(extra_final)) if x)

        prompt, por_bloque = ensamblar(A, B, C, con_bloques=True)
        prompt = self._colapsar(prompt)
        self.ultimo_por_bloque = por_bloque
        self.ultimo_reporte = {k: {"chars": len(v), "palabras": len(v.split())}
                               for k, v in por_bloque.items()}
        fallas = self.validar(prompt)
        _log_evento({"evento": "build", "motor": "bloques", "personaje": self.slug,
                     "slot": slot_n, "chars": len(prompt),
                     "por_bloque": {k: v["chars"] for k, v in self.ultimo_reporte.items()},
                     "fallas": fallas})
        return prompt


def _mapa_anclas_a_campos():
    """{id_ancla: (bloque, campo)} desde el contrato. Una ancla partida
    (ID#parte) se registra por su parte; su ID pelado NO aparece: el motor
    nuevo no la inyecta entera nunca."""
    m = {}
    for c in cargar_campos()["campos"]:
        for f in c["fuente"].split("+"):
            if f.startswith("ancla:"):
                m[f.split(":", 1)[1]] = (c["bloque"], c["id"])
    return m


def _exposicion_asiento(pb, texto_b):
    """La cola de EXPOSICIÓN de BOTTOM_CUT_LOCK, y solo ella: el corte es B.
    Elige la variante leyendo B (calzón por fuera -> asiento a la vista;
    calzón debajo de prenda -> la prenda de encima se mantiene cerrada)."""
    a = pb.anclas["BOTTOM_CUT_LOCK"]
    return a["texto_exposicion_cubierto"] if pb.calzon_va_cubierto(texto_b) else a["texto_exposicion_expuesto"]


def campos_c(pb, slot, look_number, setting, look, props=None, postura=None, extra_anclas=None):
    """{campo: texto} de C en el orden del contrato, solo los que aplican.

    pb           : BloquesBuilder (o PromptBuilder) del personaje
    slot         : standing | back_view | seated | side_profile | slot5 | pov | odalisque
    look_number  : para la rotación del repertorio y la orientación alterna
    setting      : el ambiente del look (texto)
    look         : el look del batch (para lo condicional a B: piernas, exposición)
    """
    slot_n = pb.normalizar_slot(slot)
    ruta = _mapa_anclas_a_campos()
    texto_b = " ".join(campos_b(look).values()) if look else ""
    acum = {}

    def poner(campo, texto):
        if texto:
            acum.setdefault(campo, []).append(texto)

    # 1) la sub-pose del repertorio, con su rotación — pelada, sin anclas
    poner("postura", postura or pb.pose(slot_n, look_number, props=props or (look or {}).get("props")))
    # 2) el ambiente
    poner("ambiente", setting)
    # 3) las anclas del slot (+ las de siempre del personaje), CADA UNA a su
    #    campo del contrato. Las de bloque B o A NO entran acá: son de otro dueño.
    nombres = list(pb.anclas_de_slot(slot_n)) + [n for n in (extra_anclas or []) if n]
    if slot_n == "odalisque" and not any(n.startswith("ASPECT_") for n in nombres):
        nombres.append(pb.orientacion_odalisque(look_number))   # orientación alterna
    # 4) las que B dispara por su texto (DRESS_LEG_CLOSURE, SEAM_BACK…)
    for n in pb.opt_in_de(texto_b):
        if n not in nombres:
            nombres.append(n)
    for n in nombres:
        if n == "BOTTOM_CUT_LOCK":
            if "BOTTOM_CUT_LOCK" in pb.anclas_siempre:
                poner("exposicion_asiento", _exposicion_asiento(pb, texto_b))
            continue
        bloque, campo = ruta.get(n, (None, None))
        if bloque == "C":
            poner(campo, pb.anclas[n]["texto"])
    # salida en el orden del contrato
    return {c["id"]: ", ".join(acum[c["id"]]) for c in _campos_de("C") if c["id"] in acum}


# ======================================================================
# ensamblar() + fugas() — tres oraciones y la guardia
# ======================================================================

def _oracion(campos):
    """Une los campos no vacíos de un bloque con ', ', sin comas dobles ni
    espacios de más. Devuelve '' si el bloque está vacío."""
    partes = []
    for t in (campos or {}).values():
        t = re.sub(r"\s+", " ", (t or "")).strip().strip(",;. ").strip()
        if t:
            partes.append(t)
    return ", ".join(partes)


def ensamblar(A, B, C, con_bloques=False):
    """El prompt: A. B. C. — orden fijo, tres oraciones, cada una cierra con punto.

    Determinista byte a byte: el mismo input da el mismo prompt. Con
    `con_bloques=True` devuelve también {'A':…,'B':…,'C':…} (sin el punto), que
    es lo que miden `fugas()` y el reporte de largo por bloque.
    """
    por_bloque = {"A": _oracion(A), "B": _oracion(B), "C": _oracion(C)}
    prompt = " ".join(t + "." for t in por_bloque.values() if t)
    return (prompt, por_bloque) if con_bloques else prompt


# Sustantivos de A (cuerpo) y de B (prenda) que, DESCRITOS con color o material
# fuera de su bloque, son una segunda versión del atributo — una fuga. Pelados
# son una referencia («the eyes unfocused», «wearing a dress, skirt or robe her
# legs stay closed») y se dejan pasar.
_NOUN_A = r"(?:iris|eyes|hair|skin|breasts?|bust|implants?|lips|cheekbones?|nails?)"
_NOUN_B = (r"(?:pumps?|sandals?|boots?|stiletto heels?|thong|g-string|stockings?|gloves?|"
           r"dress|skirt|gown|robe|corset|bikini|bodysuit|catsuit|trousers|jacket|coat)")
_DESCRIPTOR = (r"(?:black|white|ivory|cream|nude|blush|pink|rose|red|crimson|oxblood|burgundy|"
               r"plum|purple|violet|lilac|lavender|blue|sapphire|cobalt|navy|teal|jade|emerald|"
               r"green|olive|chartreuse|yellow|gold|golden|bronze|copper|tan|beige|taupe|brown|"
               r"grey|gray|graphite|gunmetal|silver|chrome|champagne|magenta|coral|orange|"
               r"vinyl|latex|pvc|leather|patent|satin|silk|lace|mesh|velvet|chiffon|gauze|fur|"
               r"suede|lamé|wet-look|glossy|matte|"
               # …y el CORTE también describe: «a wrap skirt» en C introduce una
               # prenda, mientras «wearing a dress, skirt or robe» (la condición
               # de DRESS_LEG_CLOSURE) no lleva ningún modificador y es referencia.
               r"wrap|mini|micro|pleated|high-waisted|low-rise|over-the-knee|thigh-high|"
               r"knee-high|platform|open-toe|pointed|halter|strapless|sheer|sleeveless|"
               r"fitted|tailored|structured|boned|laced|zipped|buttoned|belted)")
RX_A_DESCRITO = re.compile(r"\b" + _DESCRIPTOR + r"(?:[\s-]+[\w-]+){0,3}?\s+" + _NOUN_A + r"\b", re.I)
RX_B_DESCRITO = re.compile(r"\b" + _DESCRIPTOR + r"(?:[\s-]+[\w-]+){0,3}?\s+" + _NOUN_B + r"\b", re.I)


def fugas(por_bloque):
    """Vocabulario de un bloque viviendo en otro. Lista vacía = limpio.

    A no referencia nada: cualquier prenda o pose en A es fuga. En B y C un
    sustantivo ajeno solo es fuga si viene DESCRITO (color/material pegado).
    """
    A = por_bloque.get("A", "") or ""
    B = por_bloque.get("B", "") or ""
    C = por_bloque.get("C", "") or ""
    out = []
    for m in RX_VOCAB_B.finditer(A):
        out.append("A: «%s» es vocabulario de B (prenda)" % m.group(0))
    for m in RX_VOCAB_C.finditer(A):
        out.append("A: «%s» es vocabulario de C (pose/cámara)" % m.group(0))
    for m in RX_VOCAB_C.finditer(B):
        out.append("B: «%s» es vocabulario de C (pose/cámara)" % m.group(0))
    for m in RX_A_DESCRITO.finditer(B):
        out.append("B: «%s» describe el cuerpo, que es A" % m.group(0))
    for m in RX_A_DESCRITO.finditer(C):
        out.append("C: «%s» describe el cuerpo, que es A" % m.group(0))
    for m in RX_B_DESCRITO.finditer(C):
        out.append("C: «%s» describe la prenda, que es B" % m.group(0))
    return out


# ======================================================================
# Un personaje nuevo es DATO, nunca código (Ama 09/09/2026)
# ======================================================================
# Estos dos helpers construyen los datos que una muñeca nueva necesita, sin
# mutar los reales. Son lo que usa la guardia de extensibilidad (test 6bis) y
# lo que usaría un batch de prueba de un personaje todavía sin perfil escrito.

def config_con_personaje(slug, perfil_visual, slot5, base=None, **extra):
    """Copia del config real + la entrada mínima de un personaje nuevo.

    Lo mínimo que el motor LEE de un personaje: dónde está su perfil (las dos
    cercas), cómo se llama su slot 5, qué anclas propias lleva siempre, y sus
    rutas de galería/imágenes para `generar`. Todo lo demás es opcional y se
    pasa en `extra`. El config real no se toca.
    """
    import copy
    from prompt_builder import slugify
    cfg = copy.deepcopy(base or cargar_config())
    entrada = {
        "nombre": slug.replace("_", " ").title(),
        "perfil_visual": perfil_visual,
        "galeria": extra.pop("galeria", "02_Personajes/%s/GALERIA_%s.md" % (slug, slug.upper())),
        "carpeta_imagenes": extra.pop("carpeta_imagenes", "05_Imagenes/%s" % slug),
        "slot5_nombre": slot5,
        "slot5_slug": slugify(slot5),
        "anclas_siempre": extra.pop("anclas_siempre", []),
        "overrides": extra.pop("overrides", {}),
    }
    entrada.update(extra)
    cfg["personajes"][slug] = entrada
    return cfg


def repertorio_minimo(slug, base=None):
    """Copia de los repertorios reales + un repertorio mínimo para `slug`:
    una sub-pose neutra por slot (sin placeholders de mobiliario) y offsets
    en cero. Suficiente para emitir; nunca para producción — un repertorio
    real trae 7-10 variantes por slot, que es lo que hace que dos looks no
    salgan iguales."""
    import copy
    from prompt_builder import cargar_repertorios
    rep = copy.deepcopy(base or cargar_repertorios())
    neutras = {
        "standing": "full body, standing upright and facing the camera, weight on one heel",
        "back_view": "full body seen from behind, looking back over one shoulder",
        "seated": "seated upright on the named seat with knees together and hands on the thighs",
        "side_profile": "full body in strict profile, the spine in a long arch",
        "slot5": "portrait framing, the gaze drifting away from the lens",
        "pov": "portrait framing from a low angle, the gaze locked into the lens",
        "odalisque": "reclining along the named surface, one knee raised, the head propped on one hand",
    }
    rep["personajes"][slug] = {"slots": {k: [v] for k, v in neutras.items()},
                               "offsets": {k: 0 for k in neutras}}
    return rep
