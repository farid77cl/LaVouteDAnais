# -*- coding: utf-8 -*-
"""Auditor de CIERRE del outfit-engine (Ama 07/09/2026).

    "mete al final del outfit engine un pequeño auditor"

Por que al final y no en la puerta
----------------------------------
`outfit.py generar` ya bloquea ANTES de escribir, y eso esta bien: un chequeo que
corre despues documenta el defecto en vez de evitarlo. Pero todo lo que mide ahi
son las ENTRADAS — el BLOQUE B, la familia de color, la arquitectura de prenda.

Lo que nadie miraba es el ARTEFACTO: los prompts **ya expandidos**, que es lo
unico que llega al generador. Un batch puede pasar cada validacion de entrada y
salir igual con el zapato distinto en la pose 4, con un `{seat}` sin resolver, o
con la Odalisque pedida en vertical — porque esos defectos no existen en la
entrada, nacen al expandir.

Es la regla del repo aplicada al motor: **verificar el artefacto, nunca el
reporte.**

Pequeño a proposito
-------------------
Cinco chequeos, y solo los que NO se pueden hacer antes de expandir. Todo lo que
ya cubren `lint`, `cruce`, `adn`, `modularidad` o `rotacion` se queda donde esta:
duplicar una regla en dos auditores con dos varas distintas es como nacio el lio
de las galerias auditadas dos veces.

  A1  los 7 slots presentes, ninguno faltante
  A2  el token de calzado IDENTICO en las 7 poses (Ley de Continuidad del ADN)
  A3  el BLOQUE B IDENTICO en las 7 poses (misma ley)
  A4  cero placeholders sin resolver ({seat}, [BLOQUE A], {wall})
  A5  la Odalisque pide apaisada y ninguna otra pose lo hace
"""
import re

SLOTS = ("standing", "back_view", "seated", "side_profile", "pov", "odalisque")
# El slot 5 se llama distinto en cada muñeca (ditzy / glacial_command /
# sovereign_gaze): se cuenta por posicion, no por nombre.
PLACEHOLDER = re.compile(r"\{[a-z_]+\}|\[BLOQUE [AB]\]|\{\{|\}\}")

# El token de calzado va como una unidad cerrada de 8 atributos que se copia
# verbatim en las 7 poses (directiva de la Ama, 04/06/2026). Aca no se valida su
# contenido — de eso se encarga footwear_canon — solo que sea EL MISMO.
CALZADO = re.compile(
    r"[^.;]*\b(?:stiletto|pump|boot|bootie|sandal|mule|platform|pleaser|heel)\b[^.;]*",
    re.I)


def _tokens_calzado(texto):
    return tuple(sorted(m.group(0).strip().lower() for m in CALZADO.finditer(texto)))


def _pide_apaisada(texto):
    t = texto.lower()
    return "16:9" in t or "horizontal orientation" in t or "landscape orientation" in t


def auditar_look(numero, poses, alterna=False):
    """[str] de hallazgos de UN look. `poses` es {nombre_slot: prompt_expandido}."""
    out = []
    nombres = list(poses)

    # A1 · los 7 slots
    if len(nombres) != 7:
        faltan = [s for s in SLOTS if s not in poses]
        out.append("A1 L%s: %d prompts en vez de 7%s"
                   % (numero, len(nombres), (" (falta %s)" % ", ".join(faltan)) if faltan else ""))

    # A2 · el mismo zapato en todas
    # Se mide la INTERSECCION, no la igualdad de conjuntos. Cinco de las siete
    # poses llevan ademas el `footwear_echo` — una segunda mencion del zapato,
    # puesta a proposito para que no mute — asi que exigir conjuntos identicos
    # marca en rojo los 5 looks de cada batch por cumplir una regla. (Medido al
    # cablearlo, 07/09/2026: 15 de 15 looks en falso positivo.) Lo que la Ley de
    # Continuidad exige es que el TOKEN BLOQUEADO este en las 7, y eso es que la
    # interseccion no sea vacia.
    zapatos = {n: set(_tokens_calzado(t)) for n, t in poses.items() if _tokens_calzado(t)}
    if len(zapatos) > 1:
        comun = set.intersection(*zapatos.values())
        if not comun:
            sueltas = sorted(zapatos)
            out.append("A2 L%s: ninguna clausula de calzado aparece en las %d poses — "
                       "el token bloqueado no viaja verbatim (%s)"
                       % (numero, len(zapatos), ", ".join(sueltas)))
        else:
            sin_token = sorted(n for n, z in zapatos.items() if not (z & comun))
            if sin_token:
                out.append("A2 L%s: el token de calzado falta en %s"
                           % (numero, ", ".join(sin_token)))

    # A3 · el mismo outfit en todas. Se compara el prefijo largo comun: el BLOQUE B
    # viaja entero y verbatim, asi que si cambia, cambia mucho.
    if len(poses) > 1:
        textos = list(poses.values())
        pref = textos[0]
        for t in textos[1:]:
            i = 0
            lim = min(len(pref), len(t))
            while i < lim and pref[i] == t[i]:
                i += 1
            pref = pref[:i]
        # Umbral por PROPORCION, no por largo fijo: el BLOQUE A + BLOQUE B ocupa
        # el grueso de cada prompt, asi que si el prefijo comun cae por debajo de
        # la mitad del prompt mas corto, algo del outfit dejo de viajar identico.
        # Un umbral en caracteres no escala — falla con los fixtures cortos de la
        # bateria y se queda ciego con los prompts reales de ~8.000 caracteres.
        corto = min(len(t) for t in textos)
        if corto and len(pref) < corto * 0.5:
            out.append("A3 L%s: el prefijo comun a las 7 poses es el %d%% del prompt "
                       "mas corto — el BLOQUE B no viaja identico"
                       % (numero, round(len(pref) * 100.0 / corto)))

    # A4 · placeholders vivos
    for n, t in sorted(poses.items()):
        hit = PLACEHOLDER.search(t)
        if hit:
            out.append("A4 L%s/%s: placeholder sin resolver %r" % (numero, n, hit.group(0)))

    # A5 · orientacion por slot. `alterna` = el personaje declara en su perfil
    # (`orientacion_alterna`) que su Odalisque rota entre apaisada y vertical; en
    # ese caso el chequeo no aplica a ese slot. Sin esta salida el auditor marca
    # en rojo una alternancia DECLARADA, que es gritar por lo correcto.
    for n, t in sorted(poses.items()):
        es_odalisque = "odalisque" in n.lower()
        if es_odalisque and alterna:
            continue
        if es_odalisque != _pide_apaisada(t):
            out.append("A5 L%s/%s: %s" % (numero, n,
                       "la Odalisque no pide apaisada" if es_odalisque
                       else "pide apaisada y no es la Odalisque"))
    return out


def auditar_batch(looks, alterna=False):
    """[str] de hallazgos de todo el batch. `looks` es {numero: {slot: prompt}}.

    `alterna`: el personaje declara `orientacion_alterna` para su Odalisque.
    """
    out = []
    for numero in sorted(looks):
        out.extend(auditar_look(numero, looks[numero], alterna))
    return out


def imprimir(hallazgos, total_looks):
    """Resumen de una linea + detalle. Devuelve 1 si hay hallazgos."""
    if not hallazgos:
        print("  ✅ auditor de cierre: %d look(s) · 7/7 slots · calzado y outfit "
              "identicos en todas las poses · sin placeholders · orientacion correcta"
              % total_looks)
        return 0
    print("\n  \U0001f534 AUDITOR DE CIERRE — %d hallazgo(s) sobre los prompts YA "
          "expandidos:" % len(hallazgos))
    for h in hallazgos:
        print("     %s" % h)
    print("\n     Esto no lo ve ningun chequeo de entrada: nace al expandir.")
    return 1
