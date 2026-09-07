#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Construye carpeta y nombre de archivo canónicos de una pose.

Dueño único de la convención de nombres de imagen. La app NO la replica:
recibe el nombre ya resuelto en el índice. Existe porque las tres muñecas
numeran distinto (`ele_800_`, `miss_doll_10_`, `anais_L09_`) y esa diferencia
sólo vivía en la costumbre.
"""
from __future__ import annotations

import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def _numero(numero, cfg):
    return cfg.get("formato_numero_archivo", "{n}").format(n=numero)


def nombre_archivo(numero, pose, cfg):
    """(800, "standing", cfg) -> "ele_800_standing.png".

    No recibe el slug del personaje: todo lo suyo viaja en cfg. Un slug
    aparte que nadie usa dejaría pasar en silencio una llamada con el cfg
    equivocado, que es la deriva que este módulo existe para impedir.
    """
    sufijo = cfg["slot5_slug"] if pose == "slot5" else pose
    return f"{cfg['prefijo_archivo']}{_numero(numero, cfg)}_{sufijo}.png"


def carpeta_look(numero, slug_titulo, cfg):
    """(800, "chrome_hooded_column", cfg) -> carpeta con barra final."""
    return f"{cfg['carpeta_imagenes']}/{cfg['prefijo_carpeta_look']}{numero}_{slug_titulo}/"
