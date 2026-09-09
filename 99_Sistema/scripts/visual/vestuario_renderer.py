# -*- coding: utf-8 -*-
"""
vestuario_renderer.py — Fase 2 del plan del 09/09/2026 (BLOQUE B deja de ser
texto libre). Renderiza el string BLOQUE B desde un MANIFIESTO tipado en vez de
que alguien lo escriba a mano y el motor lo adivine con regex.

POR QUE EXISTE
---------------
El 09/09/2026 se encontraron 11 defectos reales, cinco con la misma causa raiz:
el motor lee prosa libre con regex para adivinar que lleva el look, y "no
corset" contiene la palabra "corset" igual que "corset" a secas. Dos auditores
externos (Fable, consultados por separado, sin verse entre si) llegaron a la
misma conclusion: el vestuario no deberia escribirse como texto que el motor
interpreta -- deberia declararse como datos, y la prosa deberia ser una
CONSECUENCIA renderizada, nunca la fuente.

EL RIESGO QUE ESTO RESUELVE (y que ninguna de las dos Fable resolvio)
-----------------------------------------------------------------------
La prosa real de BLOQUE B no es solo categorica ("un top azul de vinilo") --
tiene construccion narrativa especifica por look ("su panel exterior cruza el
frente y cierra en la cadera izquierda bajo una placa plana de gunmetal"). Un
renderizador que solo ensamblara categorias perderia justo eso.

Por eso cada prenda del manifiesto lleva DOS tipos de campo:
  - CATEGORICOS (pieza, material, color, cobertura, corte...): vocabulario
    cerrado, validado contra vocabulario_vestuario.json. Esto es lo que las
    anclas y auditores LEEN DIRECTO -- cero regex, cero adivinanza.
  - DESCRIPTIVOS (pieza_desc, material_desc, descripcion, conector): texto
    libre corto que sigue escribiendo un humano (la Ama, o quien redacte el
    look) -- la creatividad no se automatiza.

El renderizador ensambla la frase de apertura desde lo descriptivo (que es la
version LEGIBLE de lo categorico) y la continua con `descripcion` tal cual se
escribio. Ver el plan (`C:\\Users\\farid\\.claude\\plans\\humble-shimmying-stroustrup.md`)
para el ejemplo completo contra el Look 831 real.

QUE NO HACE
-----------
No migra ningun look historico. Los ~1.400 looks ya materializados siguen con
su BLOQUE B de prosa tal cual esta; este modulo solo aplica a looks NUEVOS que
declaren `manifiesto` en su batch (retrofit-al-tocar, nunca migracion masiva).
"""
import json
import os
import re

AQUI = os.path.dirname(os.path.abspath(__file__))
JSON_VOCAB = os.path.join(AQUI, "vocabulario_vestuario.json")


def cargar_vocabulario(ruta=JSON_VOCAB):
    with open(ruta, encoding="utf-8") as f:
        return json.load(f)


class PrendaInvalida(ValueError):
    """Un campo categorico no esta en el vocabulario aprobado -- error de
    COMPILACION, antes de escribir nada (mismo principio que ya rige
    `outfit.py generar`: la puerta bloquea antes, no audita despues)."""


def validar_prenda(prenda, vocab):
    """Lanza PrendaInvalida si algun campo categorico no esta aprobado.

    Solo valida los campos que declaran vocabulario cerrado (pieza, estampado).
    `material`/`color` quedan libres a proposito: color_canon.FAMILY ya cubre
    el color con su propio audit de rotacion, y forzar aca una segunda lista
    duplicaria exactamente el error que este plan existe para evitar."""
    pieza = prenda.get("pieza")
    if pieza and pieza not in vocab.get("piezas", {}):
        raise PrendaInvalida(
            "pieza '%s' no esta en vocabulario_vestuario.json -> piezas. "
            "Si es real y nueva, agregarla ahi ANTES de escribir el look "
            "(decision de canon, no del motor)." % pieza)
    estampado = prenda.get("estampado_animal")
    if estampado and estampado not in vocab.get("estampado_animal", {}).get("aprobadas", []):
        raise PrendaInvalida(
            "estampado_animal '%s' no esta aprobado. Especies vigentes: %s"
            % (estampado, vocab.get("estampado_animal", {}).get("aprobadas")))
    estampado_h = prenda.get("estampado_hosiery")
    if estampado_h and estampado_h not in vocab.get("estampado_hosiery", {}).get("aprobadas", []):
        raise PrendaInvalida(
            "estampado_hosiery '%s' no esta aprobado. Patrones vigentes: %s"
            % (estampado_h, vocab.get("estampado_hosiery", {}).get("aprobadas")))


_RX_ESPACIOS = re.compile(r"\s+")


def _limpiar(t):
    return _RX_ESPACIOS.sub(" ", (t or "").strip()).strip(" ,;")


def renderizar_prenda(prenda):
    """Una prenda del manifiesto -> su fragmento de prosa.

    Apertura categorica legible: "{conector} a {color_desc} {material_desc}
    {pieza_desc}" -- `conector` (opcional: "above it", "beneath the skirt"...)
    va ANTES de "a" porque asi se escribe la prosa real (verificado contra el
    Look 831 real: "above it a graphite mirror-vinyl halter blouse...").

    `descripcion` se CONCATENA tal cual, sin insertar coma ni espacio de mas
    -- la puntuacion de la continuacion (si lleva coma o va pegada con un
    participio: "blouse tied behind the neck" vs "miniskirt, its outer panel
    crossing...") es decision de estilo de quien escribe, no algo que el
    renderizador deba adivinar. `descripcion` debe incluir su propio
    espacio/coma inicial cuando corresponda (medido contra el Look 831: la
    falda lleva coma antes de la continuacion, el top no la lleva -- las dos
    formas son reales, ninguna es un error de una).
    """
    conector = _limpiar(prenda.get("conector"))
    apertura_partes = [_limpiar(prenda.get(k)) for k in ("color_desc", "material_desc", "pieza_desc")]
    apertura = " ".join(p for p in apertura_partes if p)
    # "a"/"an" segun la primera letra (09/09/2026, encontrado probando el
    # primer look real por manifiesto -- "a emerald..." leia mal donde una
    # persona habria escrito "an emerald..."). No afecta la imagen (Gemini no
    # lee concordancia de articulo), pero si afecta si la prosa lee tan bien
    # como la escrita a mano -- que es justo lo que la Fase 5 mide.
    _articulo = "an" if apertura[:1].lower() in "aeiou" else "a"
    frase_a = ("%s %s" % (_articulo, apertura)) if apertura else ""
    cabeza = " ".join(p for p in (conector, frase_a) if p)
    descripcion = (prenda.get("descripcion") or "").rstrip()
    return (cabeza + descripcion).strip() if descripcion else cabeza


def renderizar(manifiesto, vocab=None):
    """manifiesto: {"prendas": [ {...}, {...} ]} -> string BLOQUE B.

    Valida cada prenda contra el vocabulario (si no se pasa, se carga solo)
    antes de renderizar nada -- una pieza no aprobada nunca llega a producir
    texto."""
    vocab = vocab or cargar_vocabulario()
    prendas = manifiesto.get("prendas", [])
    for p in prendas:
        validar_prenda(p, vocab)
    fragmentos = [renderizar_prenda(p) for p in prendas]
    return "; ".join(f for f in fragmentos if f)


def cobertura_de(manifiesto, vocab=None):
    """True si ALGUNA prenda del manifiesto declara cobertura "cubierta".

    Reemplaza, para looks CON manifiesto, la adivinanza por regex de
    `garment_canon.clasificar_arquitectura()` -- el dato ya viene declarado,
    no hay nada que inferir. Cada prenda puede fijar su propia `cobertura`
    (campo explicito) o heredarla de `piezas[pieza].cobertura` en el
    vocabulario si no la fija."""
    vocab = vocab or cargar_vocabulario()
    piezas = vocab.get("piezas", {})
    for p in manifiesto.get("prendas", []):
        cob = p.get("cobertura")
        if cob is None and p.get("pieza"):
            cob = piezas.get(p["pieza"], {}).get("cobertura")
        if cob == "cubierta":
            return True
    return False


def color_dominante_de(manifiesto):
    """El color de la PRIMERA prenda del manifiesto -- reemplaza, para looks
    CON manifiesto, la heuristica `color_canon.detect_dominant()` (que busca
    la primera palabra de color en la prosa, con todo el riesgo de que una
    ausencia declarada la confunda). Con manifiesto no hay nada que buscar:
    el color dominante es un campo, no una adivinanza."""
    prendas = manifiesto.get("prendas", [])
    return prendas[0].get("color") if prendas else None


def lleva_estampado_animal(manifiesto):
    """Especie de estampado animal declarada, o None. Reemplaza
    `PromptBuilder.animal_print_kind()` para looks con manifiesto."""
    for p in manifiesto.get("prendas", []):
        if p.get("estampado_animal"):
            return p["estampado_animal"]
    return None
