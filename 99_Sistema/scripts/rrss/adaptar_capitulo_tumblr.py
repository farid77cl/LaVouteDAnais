#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
adaptar_capitulo_tumblr.py — envuelve un capitulo aprobado en el envase de Tumblr.

LA LEY QUE GOBIERNA ESTE ARCHIVO (D10 de la Ama, 07/09/2026)
------------------------------------------------------------
*"solo el envase. el texto no se toca ni una coma"* — el capitulo que viaja es el que
paso su Gate. Este script **no resume, no recorta y no reescribe**: pega alrededor.

Nace porque lo contrario ya paso y esta medido: de los 38 archivos `_tumblr.md` del repo,
**32 son teasers de menos de 450 palabras**, con un `[NOTA: ...]` explicando que el relato
era muy largo y un `[...]` donde deberia estar. «El Collar de Nancy» tiene 8.500 palabras
de relato y 425 en su archivo de Tumblr. La adaptacion nunca se hizo; se hizo un resumen y
se le puso el nombre de adaptacion.

QUE NO HACE, A PROPOSITO
------------------------
- **No escribe el gancho.** Es prosa nueva y en este repo la prosa la escribe un subagente,
  nunca el orquestador (CLAUDE.md). Sin `--gancho`, el script se niega.
- **No inventa tags.** Salen de `prompts_portada.md` del relato, que es su dueño unico.
- **No inventa enlaces.** La navegacion se arma solo con URLs ya conocidas; la de un post
  que todavia no existe simplemente no aparece.
- **No coloca las imagenes interiores** (§4.1 pide dos por capitulo). Donde va cada una es
  decision editorial y ademas todavia no existen. Queda declarado como pendiente del spec.

DUEÑO
-----
Spec: `99_Sistema/specs/2026-09-07-publicacion-tumblr-design.md` §4.1.
Pruebas: `test_adaptar_capitulo_tumblr.py` (correr antes de tocar nada aca).

FECHA DE MUERTE
---------------
Vive mientras La Voûte publique relatos en Tumblr como destino (D9).

USO
---
    python 99_Sistema/scripts/rrss/adaptar_capitulo_tumblr.py \\
        03_Literatura/02_Finalizadas/cafe_con_piernas/capitulo_1_mi_primer_turno.md \\
        --gancho gancho_cap1.txt \\
        --portada 05_Imagenes/portadas/cafe_con_piernas.png
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")  # la consola de Windows es cp1252

CORTE = "<!-- more -->"

ADVERTENCIA = (
    "**⚠️ +18 — Contenido explícito para adultos.** Ficción. Todos los personajes son "
    "mayores de edad y producto de la imaginación."
)


class CapituloInvalido(Exception):
    """El archivo no tiene la forma de un capitulo canonico."""


class TagsAusentes(Exception):
    """`prompts_portada.md` no declara tags para ese capitulo."""


class GanchoAusente(Exception):
    """El gancho es prosa nueva y lo escribe un subagente, no este script."""


@dataclass
class Capitulo:
    titulo: str
    teaser: str
    cuerpo: str


def separar_capitulo(texto: str) -> Capitulo:
    """Parte un capitulo canonico en titulo / teaser viejo / prosa."""
    if CORTE not in texto:
        raise CapituloInvalido(
            "el capitulo no trae %s — sin ese corte no se sabe donde termina el "
            "encabezado y empieza la prosa, y adivinarlo es justo lo que rompe la D10" % CORTE
        )
    cabecera, cuerpo = texto.split(CORTE, 1)

    m = re.search(r"^#\s+(.+?)\s*$", cabecera, re.M)
    if not m:
        raise CapituloInvalido("el capitulo no tiene titulo H1")
    titulo = m.group(1).strip()

    # El teaser es lo ultimo del encabezado: despues del separador que cierra el
    # bloque de metadatos y antes del corte.
    trozos = [t.strip() for t in cabecera.split("\n---\n")]
    teaser = trozos[-1].strip()

    # La prosa arranca despues del separador decorativo que sigue al corte.
    cuerpo = cuerpo.lstrip("\n")
    cuerpo = re.sub(r"\A-{3,}\s*\n", "", cuerpo).strip("\n")

    return Capitulo(titulo=titulo, teaser=teaser, cuerpo=cuerpo)


def leer_tags(prompts_portada: str, numero: int) -> list[str]:
    """Los tags de Tumblr de un capitulo, leidos de su dueño unico."""
    patron = re.compile(r"^###\s*Cap[ií]tulo\s+%d\b(.*)$" % numero, re.M)
    m = patron.search(prompts_portada)
    if not m:
        raise TagsAusentes("`prompts_portada.md` no declara el capitulo %d" % numero)
    resto = prompts_portada[m.end():]
    for linea in resto.splitlines():
        if not linea.strip():
            continue
        tags = re.findall(r"`(#[^`]+)`", linea)
        if tags:
            return [t.strip() for t in tags]
        break
    raise TagsAusentes("el capitulo %d no lista tags bajo su titulo" % numero)


def _navegacion(numero: int, nav: dict) -> str:
    partes = []
    anterior = nav.get(numero - 1)
    if anterior:
        partes.append("[← Capítulo %d](%s)" % (numero - 1, anterior))
    indice = nav.get("indice")
    if indice:
        partes.append("[Índice](%s)" % indice)
    siguiente = nav.get(numero + 1)
    if siguiente:
        partes.append("[Capítulo siguiente →](%s)" % siguiente)
    return " · ".join(partes)


def construir_post(cap: Capitulo, *, numero: int, gancho: str, portada: str,
                   tags: list[str], nav: dict) -> str:
    """Arma el post completo. El cuerpo entra intacto."""
    if not gancho or not gancho.strip():
        raise GanchoAusente(
            "el gancho es prosa nueva: lo escribe un subagente, no este script"
        )

    arriba = [
        "![Portada](%s)" % portada,
        "",
        "**«%s» — Capítulo %d**" % (cap.titulo, numero),
        "",
        gancho.strip(),
        "",
        CORTE,
        "",
        cap.cuerpo.strip(),
        "",
        "---",
        "",
        ADVERTENCIA,
    ]
    nav_txt = _navegacion(numero, nav)
    if nav_txt:
        arriba += ["", nav_txt]
    arriba += ["", " ".join(tags)]
    return "\n".join(arriba) + "\n"


# --------------------------------------------------------------------------- CLI

def main() -> int:
    ap = argparse.ArgumentParser(description="Envuelve un capitulo aprobado en el envase de Tumblr.")
    ap.add_argument("capitulo", help="ruta del capitulo canonico en 02_Finalizadas/<slug>/")
    ap.add_argument("--gancho", required=True,
                    help="archivo de texto con el gancho (2-3 lineas, prosa NUEVA de un subagente)")
    ap.add_argument("--portada", required=True, help="ruta de la imagen de portada del relato")
    ap.add_argument("--numero", type=int, default=None,
                    help="numero de capitulo (por defecto se lee del nombre del archivo)")
    ap.add_argument("--nav", default=None,
                    help="JSON con las URLs ya publicadas, p.ej. {\"1\": \"...\", \"indice\": \"...\"}")
    ap.add_argument("--salida", default=None, help="ruta de salida (por defecto _publicacion/<nombre>_tumblr.md)")
    args = ap.parse_args()

    src = Path(args.capitulo)
    if not src.exists():
        sys.exit("No existe: %s" % src)

    numero = args.numero
    if numero is None:
        m = re.search(r"capitulo[_-](\d+)", src.name, re.I)
        if not m:
            sys.exit("No pude leer el numero de capitulo del nombre; pasa --numero")
        numero = int(m.group(1))

    gancho = Path(args.gancho).read_text(encoding="utf-8")

    prompts = src.parent / "prompts_portada.md"
    if not prompts.exists():
        sys.exit("Falta el dueño de los tags: %s" % prompts)

    nav: dict = {}
    if args.nav:
        crudo = json.loads(Path(args.nav).read_text(encoding="utf-8")) \
            if Path(args.nav).exists() else json.loads(args.nav)
        for k, v in crudo.items():
            nav[int(k) if str(k).isdigit() else k] = v

    cap = separar_capitulo(src.read_text(encoding="utf-8"))
    tags = leer_tags(prompts.read_text(encoding="utf-8"), numero)
    post = construir_post(cap, numero=numero, gancho=gancho, portada=args.portada,
                          tags=tags, nav=nav)

    dest = Path(args.salida) if args.salida else src.parent / "_publicacion" / (src.stem + "_tumblr.md")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(post, encoding="utf-8", newline="\n")

    print("=" * 66)
    print("POST DE TUMBLR — %s (capitulo %d)" % (cap.titulo, numero))
    print("=" * 66)
    print("  prosa origen  : %d palabras" % len(cap.cuerpo.split()))
    print("  prosa en post : %d palabras" % len(post.split(CORTE, 1)[1].split()))
    print("  tags          : %s" % " ".join(tags))
    faltan = [n for n in (numero - 1, numero + 1) if n >= 1 and n not in nav]
    if faltan:
        print("  sin enlace    : capitulos %s (aun sin URL publicada)"
              % ", ".join(str(n) for n in faltan))
    if "indice" not in nav:
        print("  sin enlace    : indice (aun sin URL publicada)")
    print("-" * 66)
    print("  escrito       : %s" % dest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
