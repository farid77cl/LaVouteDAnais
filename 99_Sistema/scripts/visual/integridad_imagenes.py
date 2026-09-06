# -*- coding: utf-8 -*-
"""Integridad de las imagenes de un look.

Funciones PURAS a proposito: no abren archivos ni llaman a git — quien las usa
les pasa los bytes y las medidas. Asi la bateria las prueba en cualquier maquina,
incluida esta, que es un clon sparse con **0 PNG en disco** (las 8.504 imagenes
viven solo en el remoto). Un validador que necesitara el archivo real seria
inauditable justo donde mas falta hace.

Nace de la auditoria visual del 06/09/2026 sobre las tres munecas:

  · `ele L819` y `anais L83` tenian un archivo **byte a byte duplicado**
    haciendose pasar por dos poses distintas, y los dos looks figuraban **7/7**
    en el tracker con **6 poses reales**. El tracker miente hacia ARRIBA, que es
    la direccion cara: manda a no regenerar lo que si falta.
  · Cuatro odalisques de Miss Doll (L75, L79, L83, L85) salieron **verticales**
    cuando ese slot es el unico apaisado del set.

Ninguno de los dos defectos tenia quien lo mirara.
"""
import hashlib
import itertools


def _pares_con_clave_repetida(mapa):
    """[(a, b), ...] de los pares que comparten valor. Orden alfabetico estable:
    el reporte tiene que ser reproducible y los tests no pueden depender del
    orden de insercion del dict."""
    por_clave = {}
    for nombre in sorted(mapa):
        por_clave.setdefault(mapa[nombre], []).append(nombre)
    pares = []
    for nombres in por_clave.values():
        if len(nombres) > 1:
            pares.extend(itertools.combinations(nombres, 2))
    return sorted(pares)


def duplicados_por_sha(shas):
    """[(nombre_a, nombre_b), ...] a partir de {nombre: blob_sha} del indice de git.

    Es la version BARATA de `duplicados_por_look`, y la que corre en produccion.
    Leer los bytes de las 8.504 imagenes de la flota toma minutos por corrida;
    `git ls-files -s` ya trae el SHA de cada blob, y dos blobs con el mismo SHA
    son el mismo contenido por definicion. Cero lecturas, mismo veredicto.
    """
    return _pares_con_clave_repetida(shas)


def duplicados_por_look(archivos):
    """[(nombre_a, nombre_b), ...] de los pares con contenido IDENTICO.

    `archivos`: {nombre: bytes}. El orden de salida es alfabetico y estable —
    el reporte tiene que ser reproducible y los tests no pueden depender del
    orden de insercion del dict.

    Solo caza el duplicado EXACTO. El casi-duplicado (mismo frame reencodeado,
    como `ele L823 side_profile` vs `standing`: 0,1% de pixeles distintos con
    diferencia maxima de 5/255) necesita hash perceptual y no se resuelve aca:
    esto es el candado barato que corre en cada sync.
    """
    return _pares_con_clave_repetida(
        {n: hashlib.md5(b).hexdigest() for n, b in archivos.items()})


def orientacion_correcta(nombre_pose, ancho, alto):
    """True si la orientacion calza con el slot que el nombre del archivo declara.

    El slot Odalisque es el UNICO apaisado (16:9); los otros seis van verticales
    (9:16).

    Se decide por el NOMBRE del archivo y no por el indice del slot a proposito:
    las tres munecas nombran distinto su slot 5 (`ditzy` / `glacial_command` /
    `sovereign_gaze`), pero el septimo se llama `odalisque` en las tres. Atarlo
    al indice seria una rama por personaje, que es justo lo que
    `outfit.py modularidad` prohibe.
    """
    apaisada = ancho > alto
    return apaisada if "odalisque" in nombre_pose.lower() else not apaisada


def veredicto_orientacion(nombre_pose, ancho, alto, pide):
    """Cuatro estados, porque el defecto puede estar en dos lados distintos.

    `pide` es lo que el prompt de ESA pose declara: "16:9", "9:16" o None.

      · "ok"            — la imagen calza con el canon del slot.
      · "render"        — el prompt pidio lo correcto y la imagen salio al reves.
                          Se arregla regenerando.
      · "prompt"        — la imagen obedecio, pero el prompt pedia lo contrario
                          del canon. Se arregla en el TEXTO; regenerar no sirve.
      · "sin_declarar"  — el prompt no dice orientacion. No es defecto de nadie
                          todavia: es un hueco del prompt.

    Nace de cablear el chequeo binario el 06/09/2026 y medir el resultado:
    marcaba 37 odalisques de Miss Doll como defecto de render cuando **18 piden
    vertical en su propio prompt** y **30 no declaran nada**. Las imagenes
    estaban bien; el texto estaba mal. Un chequeo que confunde las dos cosas
    manda a regenerar lo que ya es correcto — y un linter que grita por lo que
    no se puede arreglar enseña a ignorarlo.
    """
    if not orientacion_correcta(nombre_pose, ancho, alto):
        if pide is None:
            return "sin_declarar"
        # el prompt pidio lo mismo que salio => el texto es el que contradice al canon
        salio = "16:9" if ancho > alto else "9:16"
        return "prompt" if pide == salio else "render"
    return "ok"
