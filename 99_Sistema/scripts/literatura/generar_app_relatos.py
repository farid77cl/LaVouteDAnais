#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generar_app_relatos.py
======================
Genera `app/relatos.json` — el índice de relatos que consume LV-App-3.

POR QUÉ EXISTE (Tarea 4 del Plan 5 de la app, pedido de la Ama 12/09/2026):
    La app ya ve las fotos y los videos del repo. Los relatos no. Sin este
    índice no hay lector, no hay escucharlos y no hay Gate desde el teléfono
    — que es lo que de verdad le cambia el día, porque hoy un Gate ES un
    archivo y eso la obliga a estar en el computador para cerrar un capítulo.

    Mismo criterio que `visual/generar_app_index.py`: el índice NO copia el
    texto. Un capítulo de esta casa son ~14.000 palabras y hay 54 relatos;
    el índice apunta al archivo y la app lo baja por la API autenticada
    cuando ella lo abre.

FUENTE DE VERDAD:
    `git ls-files` — NO el disco. Lo que no está commiteado no existe para la
    app, que lee del repo remoto. El contenido sí se lee del disco (son .md,
    viajan en cualquier clon); un archivo trackeado que no esté en disco se
    reporta y se salta, nunca se inventa.

⚠️ LA SUPOSICIÓN DEL PLAN ERA FALSA, Y ESO DEFINE EL PARSER (medido 13/09/2026):
    El plan decía «los terminados tienen uno o varios `capitulo_*.md` en la
    raíz de su carpeta». Medido sobre las 42 carpetas reales: **sólo 4 lo
    cumplen** (`cafe_con_piernas`, `la_piel_que_diseno`, `de_esteban_a_secretaria`,
    `la_app_la_bimboficacion_de_mi_novio`). Las otras 38 son lo que manda el
    CLAUDE.md para un relato finalizado — UN md canónico en la raíz, con el
    nombre del relato (`Tetitas.md`, `el_collar_de_nancy_completo.md`,
    `El_hotel_primera_noche.md`, `Capítulo_I_Le_miroir_d'Anaïs.md`).

    Por eso la prosa se detecta por EXCLUSIÓN y no por el prefijo `capitulo_`:
    se listan los archivos de trabajo conocidos (canon, cronología, walkthrough,
    investigación, brief, kit de Wattpad, notas, gates…) y **todo lo demás que
    sea .md en la raíz del relato es prosa**. Un prefijo `capitulo_` habría
    dejado 38 relatos invisibles en el lector.

    El precio de elegir exclusión es que un tipo de archivo de trabajo NUEVO
    entraría al lector como si fuera un capítulo. Por eso la corrida imprime
    SIEMPRE qué descartó y con qué regla: si aparece un nombre que no debería
    estar en esa lista, se ve en la corrida, no en el teléfono de la Ama.

EL GATE NO SE INFIERE NUNCA (Regla de Oro 8c):
    `espera_gate` es verdadero cuando el relato está en progreso y NO existe
    `gate_capitulo_[N]_[slug]_v0.[X].md` en su raíz. Nunca se deriva de un
    veredicto del validador, ni de que el archivo diga «maestro», ni del
    silencio. Hoy no hay NI UN archivo de gate en el repo: los 10 capítulos en
    progreso esperan Gate, y eso es el estado real, no una falla del parser.

Uso:
    python 99_Sistema/scripts/literatura/generar_app_relatos.py
    python 99_Sistema/scripts/literatura/generar_app_relatos.py --dry-run
    python 99_Sistema/scripts/literatura/generar_app_relatos.py --pretty
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import unicodedata
from datetime import date
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

REPO_ROOT = Path(__file__).resolve().parents[3]
BASE_PROGRESO = "03_Literatura/01_En_Progreso"
BASE_FINALIZADAS = "03_Literatura/02_Finalizadas"
SALIDA = REPO_ROOT / "app" / "relatos.json"
VERSION_ESQUEMA = 1

# --- Qué NO es prosa -------------------------------------------------------
# Nombres exactos (comparados en minúscula, sin tildes) y prefijos. Todo lo
# demás que sea .md en la raíz de un relato viaja al lector. Ver el aviso del
# encabezado: esto se elige a propósito por exclusión, y la corrida reporta
# cada descarte para que un archivo de trabajo nuevo se vea acá y no allá.
NO_PROSA_EXACTOS = {
    "readme.md",
    "canon_relato.md",
    "cronologia.md",
    "walkthrough.md",
    "brief_idea.md",
    "concepto.md",
    "notas.md",
    "investigacion.md",
    "diseno_trance.md",
    "arco_y_timeline.md",
    "fichas_personajes.md",
    "kit_wattpad.md",
    "prompts_portada.md",
}
NO_PROSA_PREFIJOS = (
    "nota_capitulo_",
    "gate_capitulo_",
    "investigacion",
    "investigaci",
    "pitch_",
    "diseno_",
    "ficha",
    "resumen_",
    "reporte_",
    "medicion_",
    "validacion_",
)

# ⚠️ El cierre NO puede ser `\b`: en una expresión regular el guión bajo ES
# carácter de palabra, así que `capitulo_1_el_cajon` no tiene frontera entre el
# `1` y el `_` y el patrón no cerraba NUNCA. Las dos regex devolvían None para
# todos los nombres reales del repo, y el orden de capítulos salía bien igual
# porque el orden alfabético de los archivos coincidía -- hasta `serie_anais`,
# que numera en romano y ahí se vio (I, III, II, IV). Se cierra contra el
# separador real del nombre.
_FIN_TOKEN = r"(?=[_ \-.]|$)"
RE_CAP_ARABIGO = re.compile(r"^cap[ií]tulo[_ -]0*(\d+)" + _FIN_TOKEN, re.IGNORECASE)
RE_CAP_ROMANO = re.compile(r"^_?cap[ií]tulo[_ -]([IVXLC]+)" + _FIN_TOKEN, re.IGNORECASE)
RE_VERSION = re.compile(r"_v(\d+(?:\.\d+)?)(?=\.md$|_|$)", re.IGNORECASE)
RE_GATE = re.compile(r"^gate_capitulo_0*(\d+)_.*?_v(\d+(?:\.\d+)?)\.md$", re.IGNORECASE)
RE_NOTA = re.compile(r"^nota_capitulo_0*(\d+)_", re.IGNORECASE)
RE_H1 = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
# Los slugs de serie llevan numeral romano en mayúscula
# (`brillando_en_tacones_I`, `esposa_de_mi_esposa_II`): un rango `[a-z0-9_]`
# los dejaba a todos sin título declarado.
RE_ENLACE_README = re.compile(r"\[([^\]\[]+)\]\(([A-Za-z0-9_]+)/\)")

ROMANOS = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100}


def sin_tildes(texto: str) -> str:
    """Compara nombres de archivo sin que una tilde decida si algo es prosa."""
    return "".join(
        c for c in unicodedata.normalize("NFD", texto) if unicodedata.category(c) != "Mn"
    )


def es_prosa(nombre: str) -> bool:
    """¿Este archivo de la raíz de un relato es un capítulo que la Ama lee?"""
    if not nombre.lower().endswith(".md"):
        return False
    plano = sin_tildes(nombre).lower()
    if plano in NO_PROSA_EXACTOS:
        return False
    return not plano.startswith(NO_PROSA_PREFIJOS)


def numero_romano(texto: str) -> int | None:
    """`IV` → 4. Devuelve None si no es un romano bien formado."""
    texto = texto.upper()
    if not texto or any(c not in ROMANOS for c in texto):
        return None
    total = 0
    for i, c in enumerate(texto):
        valor = ROMANOS[c]
        siguiente = ROMANOS.get(texto[i + 1]) if i + 1 < len(texto) else None
        total += -valor if siguiente and siguiente > valor else valor
    return total or None


def numero_de_capitulo(nombre: str) -> int | None:
    """
    El número declarado por el NOMBRE del archivo, arábigo o romano.

    `serie_anais` numera en romano (`_Capítulo_III_La_semaine…`). Ordenar esos
    cuatro alfabéticamente da el orden correcto por casualidad (`C` < `_` en
    ASCII, y II < III < IV alfabéticamente); esta función lo hace por
    construcción, que es distinto de tener suerte.
    """
    plano = sin_tildes(nombre.removesuffix(".md")).lstrip("_")
    m = RE_CAP_ARABIGO.match(plano)
    if m:
        return int(m.group(1))
    m = RE_CAP_ROMANO.match("_" + plano)
    return numero_romano(m.group(1)) if m else None


def version_de_capitulo(nombre: str) -> str | None:
    """`capitulo_1_el_cajon_v0.3.md` → `0.3`. Sin sufijo de versión → None."""
    m = RE_VERSION.search(nombre.removesuffix(".md") + ".md")
    return m.group(1) if m else None


def titulo_de_prosa(texto: str, respaldo: str) -> str:
    """El primer `# ` del archivo. Todos los capítulos medidos tienen uno."""
    m = RE_H1.search(texto)
    return m.group(1).strip() if m else respaldo


def titulo_de_documento_de_trabajo(texto: str) -> str | None:
    """
    El título del relato tal como lo escribe su canon o su ficha de trance:
    `# Canon Relato — «Hora Pedida»` · `# Diseño de Trance — Office Siren (La
    Ejecutiva)`. Se corta en el guión largo y se limpian comillas angulares y
    el paréntesis de nota al margen.
    """
    m = RE_H1.search(texto or "")
    if not m:
        return None
    titulo = m.group(1)
    if "—" in titulo:
        titulo = titulo.split("—", 1)[1]
    titulo = titulo.split("(", 1)[0]
    return titulo.strip().strip("«»\"' ") or None


def bonito(slug: str) -> str:
    """Último recurso: `hora_pedida` → `Hora Pedida`. Sin tildes, a la vista."""
    return " ".join(p.capitalize() for p in slug.split("_") if p)


def palabras(texto: str) -> int:
    return len(texto.split())


def titulos_del_readme(texto: str) -> dict[str, str]:
    """
    `02_Finalizadas/README.md` es el dueño de los títulos legibles de los
    terminados: los escribe con tilde y con los dos puntos que el slug perdió
    (`[Café con Piernas](cafe_con_piernas/)`). Se lee de ahí en vez de
    inventarlos desde el slug.
    """
    # La tabla de series usa la CARPETA como texto del enlace
    # (`[serie_anais/](serie_anais/)`): eso no es un título, es el slug otra vez.
    # Se descarta y el relato cae al siguiente escalón de la cascada.
    declarados = {}
    for t, slug in RE_ENLACE_README.findall(texto or ""):
        t = t.strip()
        if t.rstrip("/").lower() == slug.lower():
            continue
        declarados[slug] = t
    return declarados


def construir_relato(
    slug: str,
    estado: str,
    carpeta: str,
    archivos: dict[str, str],
    titulo_declarado: str | None = None,
    descartes: list[str] | None = None,
    fuentes: dict[str, str] | None = None,
) -> dict:
    """
    Un relato del índice, a partir de `{nombre de archivo: contenido}` de su
    raíz. Función pura: no toca git ni el disco, así las pruebas le dan
    fixtures a mano igual que el resto de `99_Sistema/scripts/`.
    """
    gates = set()
    notas = set()
    prosa: list[tuple[str, str]] = []
    for nombre, contenido in archivos.items():
        m = RE_GATE.match(nombre)
        if m:
            gates.add((int(m.group(1)), m.group(2)))
            continue
        m = RE_NOTA.match(nombre)
        if m:
            notas.add(int(m.group(1)))
            continue
        if es_prosa(nombre):
            prosa.append((nombre, contenido))
        elif descartes is not None and nombre.lower().endswith(".md"):
            descartes.append(f"{carpeta}/{nombre}")

    # Orden: por número declarado cuando lo hay, y los sin número al final por
    # nombre. Un relato de un solo archivo queda en el capítulo 1.
    prosa.sort(key=lambda par: (numero_de_capitulo(par[0]) or 10_000, par[0]))

    capitulos = []
    for i, (nombre, contenido) in enumerate(prosa, start=1):
        n = numero_de_capitulo(nombre) or i
        ver = version_de_capitulo(nombre)
        tiene_gate = (n, ver) in gates if ver else any(num == n for num, _ in gates)
        capitulos.append(
            {
                "n": n,
                "t": titulo_de_prosa(contenido, f"Capítulo {n}"),
                "a": nombre,
                "ver": ver,
                "pal": palabras(contenido),
                "gate": tiene_gate,
                "nota": n in notas,
                # Regla de Oro 8c: sin archivo de gate no hay Gate. Un relato
                # terminado ya no espera nada; uno en progreso sin ese archivo
                # espera, aunque el capítulo se llame «maestro».
                "espera_gate": estado == "en_progreso" and not tiene_gate,
            }
        )

    # Cascada de títulos, de la fuente más deliberada a la más automática. La
    # `fuente` se anota aparte (no viaja al JSON) para que la corrida pueda
    # decir cuántos relatos NO tienen título escrito por una persona -- medirlo
    # comparando el resultado contra `bonito(slug)` daba falsos positivos en
    # todos los relatos de una sola palabra (`Tetitas`, `Milk`, `Superficie`).
    titulo, fuente = titulo_declarado, "readme"
    if not titulo:
        for doc in ("canon_relato.md", "diseno_trance.md", "concepto.md"):
            titulo = titulo_de_documento_de_trabajo(archivos.get(doc, ""))
            if titulo:
                fuente = doc
                break
    if not titulo and capitulos:
        # El H1 del primer capítulo. Para un relato de un solo archivo es el
        # título del relato (`# La Evaluación de Miss Doll`); para uno de
        # varios es el del capítulo 1, que sigue siendo mejor que el slug.
        titulo, fuente = capitulos[0]["t"], "capitulo"
    if not titulo:
        titulo, fuente = bonito(slug), "slug"
    if fuentes is not None:
        fuentes[slug] = fuente
    return {
        "slug": slug,
        "t": titulo or bonito(slug),
        "estado": estado,
        "carpeta": carpeta,
        "caps": capitulos,
    }


def _archivos_trackeados() -> list[str]:
    """
    `-z` NO es decoración. Sin él, git aplica `core.quotePath`: cualquier ruta
    con tilde vuelve envuelta en comillas y con los bytes escapados
    (`"…/Cap\\303\\255tulo_I_Le_miroir_d\\342\\200\\231Ana\\303\\257s.md"`). El nombre
    deja de terminar en `.md` y el archivo se cae del índice SIN ERROR: en la
    primera corrida de este script, 5 relatos aparecieron con cero capítulos
    (`serie_anais`, `trance_belen`, `trance_de_muneca`, `la_creacion_util`,
    `la_dulce_aniquilacion`) y el reporte los dio por vacíos. Con `-z` las
    rutas vienen crudas, separadas por NUL.
    """
    salida = subprocess.run(
        ["git", "ls-files", "-z", BASE_PROGRESO, BASE_FINALIZADAS],
        cwd=REPO_ROOT, capture_output=True, check=True,
    ).stdout.decode("utf-8")
    return [l for l in salida.split("\0") if l.strip()]


def _raices(rutas: list[str], sin_raiz: list[str] | None = None):
    """
    `{(estado, slug): [nombres de archivo de la RAÍZ del relato]}`.

    [sin_raiz] recoge las carpetas de relato que existen en git pero no tienen
    NI UN archivo en su raíz -- sólo subcarpetas. Hoy es exactamente una,
    `the_dollhouse`, que es contenido interactivo y guarda sólo HTML en
    `_publicacion/`. Se reporta en vez de emitir un relato fantasma con cero
    capítulos: un lector no tiene nada que hacer con él.
    """
    por_relato: dict[tuple[str, str], list[str]] = {}
    carpetas: set[str] = set()
    for ruta in rutas:
        partes = ruta.split("/")
        if len(partes) < 4:
            continue
        base, slug = partes[1], partes[2]
        carpetas.add(slug)
        if len(partes) != 4:  # 03_Literatura/<base>/<slug>/<archivo>
            continue
        estado = "en_progreso" if base == "01_En_Progreso" else "terminado"
        por_relato.setdefault((estado, slug), []).append(partes[3])
    if sin_raiz is not None:
        vistos = {slug for _, slug in por_relato}
        sin_raiz.extend(sorted(carpetas - vistos))
    return por_relato


def construir_indice(por_relato, leer, titulos_declarados, descartes, ausentes,
                     fuentes=None) -> dict:
    relatos = []
    for (estado, slug), nombres in sorted(por_relato.items(), key=lambda kv: kv[0][1]):
        base = BASE_PROGRESO if estado == "en_progreso" else BASE_FINALIZADAS
        carpeta = f"{base}/{slug}"
        archivos = {}
        for nombre in sorted(nombres):
            if not nombre.lower().endswith(".md"):
                continue
            contenido = leer(f"{carpeta}/{nombre}")
            if contenido is None:
                ausentes.append(f"{carpeta}/{nombre}")
                continue
            archivos[nombre] = contenido
        relatos.append(
            construir_relato(
                slug, estado, carpeta, archivos,
                titulos_declarados.get(slug), descartes, fuentes,
            )
        )
    return {
        "v": VERSION_ESQUEMA,
        "generado": date.today().isoformat(),
        "relatos": relatos,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Genera el índice de relatos de LV-App-3.")
    ap.add_argument("--dry-run", action="store_true", help="no escribe, sólo reporta")
    ap.add_argument("--pretty", action="store_true", help="JSON indentado (pesa más)")
    args = ap.parse_args()

    def leer(ruta_rel: str) -> str | None:
        f = REPO_ROOT / ruta_rel
        return f.read_text(encoding="utf-8") if f.is_file() else None

    readme = leer(f"{BASE_FINALIZADAS}/README.md") or ""
    descartes: list[str] = []
    ausentes: list[str] = []
    sin_raiz: list[str] = []
    fuentes: dict[str, str] = {}
    indice = construir_indice(
        _raices(_archivos_trackeados(), sin_raiz), leer,
        titulos_del_readme(readme), descartes, ausentes, fuentes,
    )

    texto = (
        json.dumps(indice, ensure_ascii=False, indent=2)
        if args.pretty
        else json.dumps(indice, ensure_ascii=False, separators=(",", ":"))
    )
    kb = len(texto.encode("utf-8")) / 1024

    relatos = indice["relatos"]

    caps = [c for r in relatos for c in r["caps"]]
    sin_caps = [r["slug"] for r in relatos if not r["caps"]]
    sin_titulo = [s for s, f in fuentes.items() if f == "slug"]
    esperan = [(r["slug"], c["n"]) for r in relatos for c in r["caps"] if c["espera_gate"]]

    print(f"Relatos:          {len(relatos)}  "
          f"({sum(1 for r in relatos if r['estado'] == 'terminado')} terminados · "
          f"{sum(1 for r in relatos if r['estado'] == 'en_progreso')} en progreso)")
    print(f"Capítulos:        {len(caps)}")
    print(f"Palabras totales: {sum(c['pal'] for c in caps):,}")
    print(f"Esperan Gate:     {len(esperan)}")
    print(f"Notas sin aplicar:{sum(1 for c in caps if c['nota']):5d}")
    print(f"Tamaño índice:    {kb:.1f} KB")

    if sin_caps:
        print(f"\n⚠ {len(sin_caps)} relato(s) SIN prosa en la raíz: {', '.join(sin_caps)}")
    if sin_titulo:
        print(f"\n⚠ {len(sin_titulo)} sin título declarado (cae al slug): {', '.join(sin_titulo)}")
    if sin_raiz:
        print(f"\n⚠ {len(sin_raiz)} carpeta(s) sin archivos en la raíz: {', '.join(sin_raiz)}")
    if ausentes:
        print(f"\n⚠ {len(ausentes)} trackeado(s) que no están en disco: {ausentes[:3]}")

    print(f"\n--- Descartados por no ser prosa ({len(descartes)}) ---")
    nombres = sorted({d.rsplit('/', 1)[1] for d in descartes})
    print("  " + ", ".join(nombres) if nombres else "  (ninguno)")

    if args.dry_run:
        print("\n--dry-run: no se escribió nada.")
        return 0

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(texto, encoding="utf-8", newline="\n")
    print(f"\nEscrito: {SALIDA.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
