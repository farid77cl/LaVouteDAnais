# -*- coding: utf-8 -*-
"""Cláusulas que se pelean DENTRO de un mismo prompt.

Nace de la auditoría visual del 09/09/2026 (70 poses, tres muñecas, seis
auditores externos ciegos). De ~85 hallazgos, **5 fueron del motor** — y los
cinco son el mismo animal: dos cláusulas del mismo prompt pidiendo cosas
incompatibles. Cada una estaba bien escrita por separado; ningún chequeo del
repo mira dos a la vez, así que ninguno las vio.

  · **C1 calzado** — el ADN de Anaïs clava `12cm black patent leather stiletto
    heels` y su BLOQUE B declara marfil. El `pov` del L88 salió con zapato NEGRO
    en un look rosa polvo íntegro.
  · **C2 exposición** — L831: `g-string under the skirt` + `the wrap skirt stays
    unbroken` + `both seat cheeks fully bare:1.4`. Ganó la de más peso y la falda
    se abrió en un recorte.
  · **C3 iris** — la odalisque de Miss Doll pedía `cold pale steel grey eyes` con
    las otras seis poses en cobalto. Sobrevivió cinco días a la corrección del
    04/09 escondida en el repertorio de sub-poses.
  · **C4 copa** — el ADN de Anaïs pide `extreme waist training tightlacing
    corset` y el L91, que ESTRENA su veto de corsetería, pide copa blanda sin
    ballenas. Salió aro rígido.
  · **C5 uñas** — `long stiletto-shaped fingernails` en el ADN contra almendra
    corta en el BLOQUE B.

Funciones **puras**: no abren archivos, no llaman a git, no leen config. Reciben
el texto y devuelven hallazgos. Mismo patrón que `integridad_imagenes.py`, y por
la misma razón: así la batería corre en cualquier máquina.

⚠️ **Este es el único clasificador del repo que mira el PROMPT ENSAMBLADO.** Es
deliberado y no contradice la regla del 19/07/2026. Aquella prohíbe *clasificar*
sobre el prompt —el ancla nombra «bodysuit, teddy, leotard or swimsuit», así que
el clasificador se leería a sí mismo—. Acá no se clasifica: se **comparan** dos
cláusulas del mismo texto, que es exactamente lo que un chequeo por cláusula no
puede hacer.

⚠️ **Y por eso mismo el umbral es alto a propósito.** Un hallazgo solo sale
cuando las dos cláusulas están explícitas y son incompatibles sin
interpretación. Preferimos un falso negativo a un falso positivo: un linter que
grita lo inarreglable enseña a ignorarlo, y esa lección ya se pagó con
`auditar_canon_flota`, que va en 872 avisos sobre 685 looks y nadie lee.
"""
import re

# --------------------------------------------------------------------------
# Vocabularios. Van acá y no en cada detector para que se lean juntos: si dos
# detectores discrepan sobre qué es "calzado", el bug es invisible.
# --------------------------------------------------------------------------

_COLORES = (
    r"black|white|ivory|cream|nude|blush|pink|rose|red|crimson|oxblood|burgundy|plum|"
    r"purple|violet|lilac|lavender|blue|sapphire|cobalt|navy|teal|jade|emerald|green|"
    r"olive|chartreuse|yellow|gold|golden|bronze|copper|tan|beige|taupe|brown|grey|gray|"
    r"graphite|gunmetal|silver|chrome|champagne|magenta|coral|tangerine|orange"
)

# El sustantivo que hace de calzado. `heel` a secas queda fuera: aparece en
# "heel of the hand" y en la altura del tacón dentro de otra cláusula.
# ⚠️ Los bordes de palabra NO son decorativos: sin ellos `boots?` matcheaba
# «VIP booth purple blur background» —el SETTING del L211— y lo comparaba contra
# el zapato real como si fueran dos zapatos.
_CALZADO = (
    r"\b(?:stiletto heels?|stiletto sandals?|stiletto pumps?|platform stiletto|"
    r"d'orsay|pumps?|sandals?|mules?|slingbacks?|ankle boots?|thigh-high boots?|boots?)\b"
)

# Colores de HERRAJE: describen el tacón, la hebilla o el canto de suela, nunca
# el cuerpo del zapato. Un «magenta pump with a chrome heel» es UN zapato de dos
# colores, no dos zapatos — y contarlo como dos fue el 227 de falsos positivos.
_HERRAJE = {"chrome", "silver", "gold", "golden", "gunmetal", "graphite", "bronze", "copper"}

_MAX_CITA = 110


def _cita(texto):
    """Recorta una cláusula para que quepa en un mensaje legible."""
    t = " ".join((texto or "").split())
    return t if len(t) <= _MAX_CITA else t[: _MAX_CITA - 1] + "…"


def _clausula(prompt, pos, radio=70):
    """El tramo de prompt alrededor de una coincidencia, cortado en comas."""
    ini = prompt.rfind(",", max(0, pos - radio), pos)
    ini = ini + 1 if ini != -1 else max(0, pos - radio)
    fin = prompt.find(",", pos)
    fin = fin if fin != -1 else min(len(prompt), pos + radio)
    return prompt[ini:fin].strip()


def _colores_de(texto):
    return {c.lower() for c in re.findall(_COLORES, texto, re.I)}


# --------------------------------------------------------------------------
# C1 · Calzado nombrado con dos colores distintos
# --------------------------------------------------------------------------

def _c1_calzado(prompt):
    vistos = []
    for m in re.finditer(_CALZADO, prompt, re.I):
        cl = _clausula(prompt, m.start(), radio=95)
        # El color tiene que estar en la MISMA FRASE NOMINAL que el sustantivo
        # de calzado: desde la coma anterior hasta el sustantivo, sin cruzar
        # puntuación. Una ventana de N caracteres le prestaba al eco de cierre
        # («weight on one stiletto sandal», que no trae color propio) el color
        # del vecino, y contaba el mismo zapato como dos.
        ini = max(prompt.rfind(",", 0, m.start()), prompt.rfind(";", 0, m.start()),
                  prompt.rfind(".", 0, m.start()), prompt.rfind("(", 0, m.start()))
        frase = prompt[ini + 1:m.start()]
        cols = _colores_de(frase) - _HERRAJE if len(frase.split()) <= 8 else set()
        # Anaïs escribe el color DESPUÉS del zapato: «D'Orsay stiletto pump with
        # open sides, in ivory patent leather». Se acepta un «in <color>» en los
        # 60 caracteres que siguen al sustantivo, antes del siguiente punto y coma.
        cola = prompt[m.end():m.end() + 60].split(";")[0].split(".")[0]
        mi = re.search(r"\bin\s+(?:[\w-]+\s+){0,2}(" + _COLORES + r")\b", cola, re.I)
        if mi:
            cols = cols | ({mi.group(1).lower()} - _HERRAJE)
        if cols:
            # El BLOQUE B separa PRENDAS con «;». Dos menciones de calzado dentro
            # del mismo segmento son la misma prenda («platform pump, closed
            # pointed toe, secured slingback strap» del MD L62 es UN zapato):
            # se comparan solo entre segmentos distintos.
            vistos.append((cols, cl, prompt.count(";", 0, m.start())))
    if len(vistos) < 2:
        return None
    for i in range(len(vistos)):
        for j in range(i + 1, len(vistos)):
            a, b = vistos[i], vistos[j]
            if a[2] == b[2]:
                continue
            # Incompatibles solo si NO comparten ningún color: "black patent" y
            # "black leather" son la misma prenda descrita dos veces, que es lo
            # normal (el eco de calzado la repite a propósito).
            if not (a[0] & b[0]):
                return ("calzado con dos colores distintos en el mismo prompt: "
                        "«%s» contra «%s»" % (_cita(a[1]), _cita(b[1])))
    return None


# --------------------------------------------------------------------------
# C2 · Se expone el asiento y a la vez hay prenda que lo cubre
# --------------------------------------------------------------------------

_EXPONE = r"both seat cheeks fully bare|the seat is left uncovered|seat fully exposed"
# ⚠️ Solo la relación EXPLÍCITA «el calzón va debajo de tal prenda». La rama
# `stays unbroken` que esto tenía antes disparaba 673 falsos positivos: ese texto
# es de DRESS_LEG_CLOSURE y habla de la caída de la falda sobre el REGAZO en la
# pose sentada, no de cubrir el asiento. Las dos cláusulas citadas eran, encima,
# texto de anclas: el detector comparaba el prompt contra sí mismo.
_CUBRE_ASIENTO = (
    r"\b(?:under|underneath|beneath)\s+(?:the|her)\s+(?:[a-z\-]+\s+){0,3}"
    r"(?:skirt|dress|gown|trousers|pants|catsuit)\b"
)


def _c2_exposicion(prompt):
    e = re.search(_EXPONE, prompt, re.I)
    c = re.search(_CUBRE_ASIENTO, prompt, re.I)
    if not (e and c):
        return None
    return ("se expone el asiento y a la vez hay prenda que lo cubre: "
            "«%s» contra «%s»" % (_cita(_clausula(prompt, c.start())),
                                  _cita(_clausula(prompt, e.start()))))


# --------------------------------------------------------------------------
# C3 · Iris nombrado con dos colores distintos
# --------------------------------------------------------------------------

# «eyes in midnight sapphire shimmer smoke» es SOMBRA, no iris: la gramática de
# maquillaje de la galería es «eyes in <color> …» / «mouth in <color> …». Se
# excluye «eyes in». (MD L86, L88, L90 daban falso positivo por esto.)
_IRIS = r"\biris\b|\beyes\b(?!\s+in\b)"
_COLOR_DE_OJO = (
    r"\b(?:cobalt|sapphire|blue|grey|gray|steel|green|amber|honey|hazel|violet|golden)\b"
)


def _c3_iris(prompt):
    vistos = []
    for m in re.finditer(_IRIS, prompt, re.I):
        cl = _clausula(prompt, m.start(), radio=85)
        cols = {c.lower() for c in re.findall(_COLOR_DE_OJO, cl, re.I)}
        # Una negación NO declara color: "never grey and never pale" es la
        # defensa del ancla, no una segunda instrucción. Se descuenta.
        for neg in re.finditer(r"never\s+(?:and\s+never\s+)?(\w+)", cl, re.I):
            cols.discard(neg.group(1).lower())
        cols.discard("steel") if "grey" in cols or "gray" in cols else None
        if cols:
            vistos.append((cols, cl))
    for i in range(len(vistos)):
        for j in range(i + 1, len(vistos)):
            a, b = vistos[i], vistos[j]
            if not (a[0] & b[0]):
                return ("iris con dos colores distintos en el mismo prompt: "
                        "«%s» contra «%s»" % (_cita(a[1]), _cita(b[1])))
    return None


# --------------------------------------------------------------------------
# C4 · Estructura de copa: corsetería contra copa blanda
# --------------------------------------------------------------------------

_ESTRUCTURA = r"tightlacing|waist training corset|\bcorset\b|boned bodice|moulded cups?"
_BLANDA = r"soft and unstructured|no boning|unlined soft cup|without boning|no moulding"


def _c4_copa(prompt):
    e = re.search(_ESTRUCTURA, prompt, re.I)
    b = re.search(_BLANDA, prompt, re.I)
    if not (e and b):
        return None
    return ("estructura de copa contradictoria: «%s» contra «%s»"
            % (_cita(_clausula(prompt, e.start())), _cita(_clausula(prompt, b.start()))))


# --------------------------------------------------------------------------
# C5 · Uñas largas contra uñas cortas
# --------------------------------------------------------------------------

# ⚠️ Los dos lados exigen la palabra «nail» cerca. Sin eso, `XXXL` matcheaba las
# EXTENSIONES DE PELO y `cut short` matcheaba «high-cut shorts» — 55 falsos
# positivos del L461 y compañía, ninguno con una uña a la vista.
_UNA_LARGA = (r"long stiletto-shaped[^.;]{0,60}nails?|XXXL[^.;]{0,30}nails?"
              r"|extra[- ]long[^.;]{0,30}nails?|5\s*cm[^.;]{0,30}nails?")
_UNA_CORTA = (r"nails?[^.;]{0,40}\bfiled short\b|nails?[^.;]{0,40}\bshort of the fingertip\b"
              r"|\bfiled short\b[^.;]{0,40}fingertip")


def _c5_unas(prompt):
    lg = re.search(_UNA_LARGA, prompt, re.I)
    ct = re.search(_UNA_CORTA, prompt, re.I)
    if not (lg and ct):
        return None
    return ("uñas largas y cortas en el mismo prompt: «%s» contra «%s»"
            % (_cita(_clausula(prompt, lg.start())), _cita(_clausula(prompt, ct.start()))))


_DETECTORES = (_c1_calzado, _c2_exposicion, _c3_iris, _c4_copa, _c5_unas)


def buscar(prompt):
    """Devuelve las contradicciones del prompt. Lista vacía = limpio.

    Cada hallazgo cita **las dos** cláusulas que se pelean, entre «». Localizar
    es la mitad del trabajo: el 09/09 detectar fue barato y ubicar la cláusula
    dentro de 8.500 caracteres fue lo caro.
    """
    if not prompt:
        return []
    return [h for h in (d(prompt) for d in _DETECTORES) if h]
