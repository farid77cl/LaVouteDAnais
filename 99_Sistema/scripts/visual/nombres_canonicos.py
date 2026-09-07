#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Construye carpeta y nombre de archivo canónicos de una pose.

Dueño único de la convención de nombres de imagen. La app NO la replica:
recibe el nombre ya resuelto en el índice. Existe porque la convención sólo
vivía en la costumbre, y la costumbre se había partido: hasta el 07/09/2026
el config declaraba un formato de número distinto por muñeca (`{n}` en Ele y
Miss Doll, `L{n:02d}` en Anaïs) y dos de los tres estaban mal contra
`git ls-files`. Hoy es UNO solo para las tres: `{n:03d}` — `ele_800_`,
`miss_doll_085_`, `anais_009_`. Lo que difiere por muñeca sigue viviendo en
`anclas_universales.json` (prefijo, carpeta, slug del slot5), no aquí.
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
