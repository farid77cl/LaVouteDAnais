#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_adaptar_capitulo_tumblr.py — pruebas del adaptador de post de Tumblr (07/09/2026)

Se escriben ANTES del adaptador (regla 13: `99_Sistema/scripts/**` va con TDD).

Por que estas pruebas y no otras: la ley que gobierna este adaptador es la D10 de la Ama
-- *"solo el envase; el texto no se toca ni una coma"* -- y esa ley es exactamente lo que
fallo hasta ahora. Medido el 07/09/2026: **32 de 38 archivos `_tumblr.md` del repo son
teasers de menos de 450 palabras**, con un `[NOTA: ...]` adentro y un `[...]` donde deberia
ir el relato. O sea el modo de falla no es un bug sutil: es entregar un recorte creyendo que
se entrego el capitulo. Por eso la prueba central compara el cuerpo **caracter por caracter**
contra el capitulo real de `02_Finalizadas/`, y no contra un fixture comodo.

Correr:  python 99_Sistema/scripts/rrss/test_adaptar_capitulo_tumblr.py
"""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).parent))

import adaptar_capitulo_tumblr as A  # noqa: E402

REPO = Path(__file__).resolve().parents[3]
CAFE = REPO / "03_Literatura/02_Finalizadas/cafe_con_piernas"

FALLAS: list[str] = []


def check(nombre: str, cond: bool, detalle: str = "") -> None:
    if cond:
        print("  ok   %s" % nombre)
    else:
        print("  FALLA %s %s" % (nombre, ("- " + detalle) if detalle else ""))
        FALLAS.append(nombre)


CAP_FIXTURE = """*Un relato de Anaïs Belland*

# Relato de Prueba: Capitulo Uno

---

**Universo:** La Voûte d'Anaïs
**Temáticas:** #Uno #Dos
**Palabras:** ~1,000
**Perspectiva:** Tercera Persona
**Intensidad:** Extrema

---

**Teaser viejo de Wattpad que no es el gancho de Tumblr.**

<!-- more -->

---

Primera línea de la prosa, con acentos: canción, ñandú, «comillas».

Segunda línea — con raya y puntos suspensivos...
"""

PROMPTS_FIXTURE = """# Relato de Prueba — Tags y Prompts de Portada

## Tags (Tumblr/RRSS, con `#`, por capítulo)

### Relato completo
`#Uno` `#Dos` `#LaVoûtedAnaïs`

### Capítulo 1 — Capitulo Uno
`#Uno` `#Dos` `#PrimerTurno`

### Capítulo 2 — Capitulo Dos
`#Uno` `#Tres` `#Oficina`
"""


def cuerpo_de(texto: str) -> str:
    """La prosa que va DESPUES del corte del feed."""
    return texto.split("<!-- more -->", 1)[1]


def main() -> int:
    print("=" * 70)
    print("PRUEBAS — adaptador de capitulo a post de Tumblr")
    print("=" * 70)

    # ---------------------------------------------------------------- separar
    print("\n[1] Lectura del capitulo canonico")
    cap = A.separar_capitulo(CAP_FIXTURE)
    check("saca el titulo del H1", cap.titulo == "Relato de Prueba: Capitulo Uno", repr(cap.titulo))
    check("saca el teaser viejo", cap.teaser.startswith("**Teaser viejo"), repr(cap.teaser[:40]))
    check("el cuerpo empieza en la prosa",
          cap.cuerpo.lstrip().startswith("Primera línea"), repr(cap.cuerpo[:40]))
    check("el cuerpo NO arrastra el separador del encabezado",
          not cap.cuerpo.lstrip().startswith("---"), repr(cap.cuerpo[:20]))

    print("\n[2] Un capitulo sin corte de feed no se adivina: se rechaza")
    try:
        A.separar_capitulo("# Sin corte\n\nprosa suelta\n")
        check("sin <!-- more --> levanta error", False, "no levanto nada")
    except A.CapituloInvalido:
        check("sin <!-- more --> levanta error", True)

    # ------------------------------------------------------------------ tags
    print("\n[3] Los tags salen de su dueño, no se inventan")
    check("tags del capitulo 1",
          A.leer_tags(PROMPTS_FIXTURE, 1) == ["#Uno", "#Dos", "#PrimerTurno"],
          repr(A.leer_tags(PROMPTS_FIXTURE, 1)))
    check("tags del capitulo 2",
          A.leer_tags(PROMPTS_FIXTURE, 2) == ["#Uno", "#Tres", "#Oficina"],
          repr(A.leer_tags(PROMPTS_FIXTURE, 2)))
    try:
        A.leer_tags(PROMPTS_FIXTURE, 9)
        check("capitulo sin tags levanta error", False, "no levanto nada")
    except A.TagsAusentes:
        check("capitulo sin tags levanta error", True)

    # ----------------------------------------------------------------- armado
    print("\n[4] El post armado")
    post = A.construir_post(
        cap,
        numero=1,
        gancho="Dos líneas nuevas.\nQue deciden si alguien abre.",
        portada="05_Imagenes/portadas/prueba.png",
        tags=["#Uno", "#Dos"],
        nav={2: "https://ejemplo/2", "indice": "https://ejemplo/indice"},
    )
    check("un solo corte de feed", post.count("<!-- more -->") == 1, str(post.count("<!-- more -->")))
    check("la portada va antes del corte",
          post.index("prueba.png") < post.index("<!-- more -->"))
    check("el gancho va antes del corte",
          post.index("Que deciden si alguien abre.") < post.index("<!-- more -->"))
    check("el teaser viejo de Wattpad NO viaja", "Teaser viejo" not in post)
    check("lleva advertencia +18", "+18" in post)
    check("lleva los tags al final", post.rstrip().endswith("#Dos"), repr(post.rstrip()[-30:]))

    print("\n[5] LA LEY D10 — el texto no se toca ni una coma")
    check("el cuerpo del post contiene la prosa intacta", cap.cuerpo.strip() in post)
    check("no aparece ningun corchete de recorte",
          "[...]" not in post and "[NOTA:" not in post)

    print("\n[6] Navegacion")
    check("el capitulo 1 no ofrece 'anterior'", "anterior" not in post.lower())
    check("el capitulo 1 ofrece 'siguiente'", "siguiente" in post.lower())
    check("enlaza el indice", "https://ejemplo/indice" in post)
    post_solo = A.construir_post(cap, numero=1, gancho="g", portada="p.png", tags=["#X"], nav={})
    check("sin URLs conocidas no inventa enlaces",
          "http" not in post_solo, "aparecio un enlace de la nada")

    print("\n[7] Sin gancho no hay post — la prosa la escribe un subagente, no el script")
    try:
        A.construir_post(cap, numero=1, gancho="", portada="p.png", tags=["#X"], nav={})
        check("gancho vacio levanta error", False, "no levanto nada")
    except A.GanchoAusente:
        check("gancho vacio levanta error", True)

    # ------------------------------------------------- el capitulo DE VERDAD
    print("\n[8] Contra el capitulo real de «Café con Piernas» (10.297 palabras)")
    real = CAFE / "capitulo_1_mi_primer_turno.md"
    if not real.exists():
        check("existe el capitulo real", False, str(real))
    else:
        crudo = real.read_text(encoding="utf-8")
        cap_real = A.separar_capitulo(crudo)
        post_real = A.construir_post(
            cap_real, numero=1, gancho="Gancho de prueba.",
            portada="05_Imagenes/portadas/cafe.png",
            tags=A.leer_tags((CAFE / "prompts_portada.md").read_text(encoding="utf-8"), 1),
            nav={},
        )
        check("la prosa real viaja completa, caracter por caracter",
              cuerpo_de(post_real).find(cap_real.cuerpo.strip()) >= 0)
        palabras_post = len(cuerpo_de(post_real).split())
        check("el post NO es un teaser (>9.000 palabras de prosa)",
              palabras_post > 9000, "%d palabras" % palabras_post)
        check("los tags reales salen del dueño",
              "#CaféConPiernas" in post_real)

    print("\n" + "=" * 70)
    if FALLAS:
        print("%d FALLA(S): %s" % (len(FALLAS), ", ".join(FALLAS)))
        return 1
    print("TODO VERDE 💅")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
