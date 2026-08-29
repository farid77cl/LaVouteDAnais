#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
outfit.py — CLI único del outfit-engine.

POR QUE EXISTE (Ama 29/08/2026)
-------------------------------
    "me molesta que el outfit engine no sea un programa, una app como tal
     si ya está en un 80% como app"

Tenia razon, y el inventario lo confirma. Lo que YA era app: un motor con clase
(`PromptBuilder`), sus datos con dueño unico (`anclas_universales.json`,
`repertorios_pose.json`, los perfiles visuales), una capa de reglas
(`footwear_canon`, `garment_canon`, `color_canon`) y herramientas de verificacion.

Lo que faltaba para serlo:

1. **Generar un batch de looks era ESCRIBIR UN PROGRAMA.** Medido sobre
   `gen_lenceria_808_812.py`: de sus 158 lineas, ~140 son datos (BLOQUE_B,
   SETTING, PROPS, META por look) y ~18 son el bucle que los emite. Ese bucle se
   reescribia a mano en cada batch, con variaciones — y ahi nacio el defecto del
   Look 801, que se escribio con su propio bucle y salio sin GARMENT_CONSISTENCY,
   sin PHOTOREAL_LOCK y sin ancla de orientacion: cuatro poses con otro outfit.
   Un batch es DATOS. El programa que los emite es este, uno solo, probado.
2. **No habia punto de entrada.** Habia que recordar veinte nombres de script.
3. Cada herramienta se auto-descubria con `sys.path.insert` (6 archivos).

USO
---
    python 99_Sistema/scripts/visual/outfit.py                      # ayuda
    python 99_Sistema/scripts/visual/outfit.py generar batches/L808_L812_lenceria.json
    python 99_Sistema/scripts/visual/outfit.py adn                  # dueño unico del BLOQUE A
    python 99_Sistema/scripts/visual/outfit.py lint [slug]          # parseo como LV-App
    python 99_Sistema/scripts/visual/outfit.py auditar [--solo-sin-imagen]
    python 99_Sistema/scripts/visual/outfit.py anclas <slug> [--solo-sin-imagen] [--opt-in]
    python 99_Sistema/scripts/visual/outfit.py test                 # todos los self-checks
    python 99_Sistema/scripts/visual/outfit.py personajes | poses [slug]

UN BATCH ES UN JSON
-------------------
    {
      "personaje": "ele", "batch": "La Perla y HB Lencería",
      "fecha": "27/08/2026", "categoria": "Lencería", "rango": "808-812",
      "tags_comunes": ["laperla", "honeybirdette", "V7poses"],
      "negative_extra": "cotton lingerie, organic fabric, ...",
      "looks": {
        "808": {
          "titulo": "Noir Lace La Perla Suite", "codigo": "LA1", "polo": "A Boudoir",
          "bloque_b": "<el outfit del dia>",
          "setting":  "<BLOQUE C>",
          "props":    {"seat": "...", "wall": "...", "surface": "...", "upright": "..."}
        }
      }
    }

El BLOQUE A **no va aca**: lo lee el motor del perfil visual, que es su dueño
unico (29/08/2026). Los slots y sus etiquetas tampoco: salen del contrato.
"""
import io
import json
import os
import subprocess
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, "..", "..", ".."))
sys.path.insert(0, AQUI)

from prompt_builder import PromptBuilder, cargar_config, slugify  # noqa: E402


# --------------------------------------------------------------------- generar

def _etiquetas(pb, cfg):
    """(slots internos, etiquetas visibles) para este personaje.

    El slot 5 cambia de nombre por personaje — Ditzy en Ele, Sovereign Gaze en
    Anais, Glacial Command en Miss Doll — y esa etiqueta es la que el parser de
    LV-App busca en la galeria. Escribirla a mano en cada batch fue exactamente
    como los archivos de Anais y Miss Doll terminaron con el slot 5 mal nombrado.
    """
    slots = list(cfg["slots_universales"])
    etiquetas = []
    for s in slots:
        etiquetas.append(pb.perfil["slot5_nombre"] if s == "slot5"
                         else s.replace("_", " ").title().replace("Pov", "POV"))
    return slots, etiquetas


def cmd_generar(args):
    if not args:
        print("uso: outfit.py generar <batch.json> [--out <archivo.md>] [--stdout]")
        return 2
    ruta = args[0]
    if not os.path.isabs(ruta):
        for base in (os.getcwd(), AQUI, RAIZ):
            if os.path.exists(os.path.join(base, ruta)):
                ruta = os.path.join(base, ruta)
                break
    if not os.path.exists(ruta):
        print("no existe el batch: %s" % args[0])
        return 1

    b = json.load(open(ruta, encoding="utf-8"))
    cfg = cargar_config()
    pb = PromptBuilder(b["personaje"], cfg)
    slots, etiquetas = _etiquetas(pb, cfg)

    faltan = [k for k in ("personaje", "looks") if k not in b]
    if faltan:
        print("batch invalido, faltan claves: %s" % ", ".join(faltan))
        return 1

    out = []
    n_prompts = 0
    for num in sorted(b["looks"], key=int):
        lk = b["looks"][num]
        for k in ("titulo", "bloque_b", "setting"):
            if k not in lk:
                print("look %s: falta '%s'" % (num, k))
                return 1
        # El emoji del encabezado es del personaje (Ele 👗 · Miss Doll 💅 · Anaïs 🌹)
        # y vive en su perfil, como todo lo que difiere entre muñecas.
        cab = "## %s Look %s: %s" % (pb.perfil.get("emoji_look", "\U0001f457"),
                                     num, lk["titulo"])
        ctx = [x for x in (b.get("fecha"),
                           ('batch %s "%s"' % (b.get("rango", ""), b["batch"])).strip()
                           if b.get("batch") else None,
                           b.get("categoria"),
                           (" ".join(x for x in (lk.get("codigo"), lk.get("polo")) if x) or None))
               if x]
        if ctx:
            cab += " (%s)" % " · ".join(ctx)
        out += [cab, ""]
        # carpeta_imagenes + prefijo_carpeta_look + numero + slug. Los tres campos
        # salen del perfil: la ruta es contrato con LV-App, que filtra por subcadena.
        out.append("- **Ubicacion:** `%s/%s%s_%s/`"
                   % (pb.perfil["carpeta_imagenes"].rstrip("/"),
                      pb.perfil["prefijo_carpeta_look"], num, slugify(lk["titulo"])))
        if lk.get("tags"):                      # tags escritos a mano para este look
            out += ["- **Tags:** %s" % lk["tags"], ""]
        else:
            tags = ["#" + slugify(b.get("categoria", "")).replace("_", "")] if b.get("categoria") else []
            for extra in (lk.get("polo"), lk.get("codigo")):
                if extra:
                    tags.append("#" + slugify(extra))
            tags += ["#" + t.lstrip("#") for t in b.get("tags_comunes", [])]
            out += ["- **Tags:** %s" % " ".join(tags), ""]
        if lk.get("concepto"):
            out += ["**Concepto:** %s" % lk["concepto"], ""]
        # El fence `**BLOQUE B:**` no es decorativo: es lo que lee
        # `lint_prompts_personaje.extraer_bloques_b()` para clasificar la
        # arquitectura de prenda y medir la cuota de silueta cubierta. La galeria
        # de Ele no lo tiene y por eso su rotacion de prenda no se puede auditar.
        if b.get("emitir_bloque_b"):
            out += ["**BLOQUE B (outfit -- copiado textual e identico en los %d prompts):**"
                    % len(slots), "```text", lk["bloque_b"], "```", ""]
        out += ["### \U0001f4f8 Imágenes (0/7 — Pendiente)", ""]
        out += ["| " + " | ".join(etiquetas) + " |",
                "| " + " | ".join([":---:"] * len(etiquetas)) + " |",
                "| " + " | ".join(["⏳ Pendiente"] * len(etiquetas)) + " |", ""]
        # ADN: lo lee el motor del perfil (dueño unico). Un look puede DECLARAR
        # variaciones sobre el, no reescribirlo: Miss Doll rota sombra y color de
        # labios por look, que es canon suyo (perfil §5.5, "nunca el mismo tono en
        # looks consecutivos"). El reemplazo se aplica sobre el texto del dueño y
        # falla ruidosamente si el fragmento buscado ya no existe — asi un cambio
        # de ADN no deja overrides zombis pegados en silencio.
        adn = None
        if lk.get("adn_overrides"):
            adn = pb.bloque_a
            for viejo, nuevo in lk["adn_overrides"].items():
                if viejo not in adn:
                    print("  \U0001f534 Look %s: adn_overrides busca %r y no está en el "
                          "BLOQUE A del perfil. Actualiza el override o quítalo." % (num, viejo))
                    return 1
                adn = adn.replace(viejo, nuevo)
        # Orientacion alterna: en Ele y Anais la Odalisque es SIEMPRE horizontal y
        # su ancla ya vive en el mapa de slots. Miss Doll la alterna por numero de
        # look (Ama 17/08/2026, "debe tener Odalisque en vertical y horizontal"),
        # asi que su perfil lo declara y hay que pedirsela al builder. Se lee del
        # perfil, no se codifica el nombre del personaje.
        alterna = pb.perfil.get("orientacion_alterna") or {}
        for i, (slot, label) in enumerate(zip(slots, etiquetas)):
            pose = pb.pose(slot, int(num), props=lk.get("props"))
            extra = [pb.orientacion_odalisque(int(num))] if slot in alterna else None
            prompt = pb.build(adn, lk["bloque_b"], slot, pose, lk["setting"],
                              extra_anclas=extra)
            fallas = pb.validar(prompt)
            if fallas:
                print("  \U0001f534 Look %s / %s: %s" % (num, label, "; ".join(fallas)))
                return 1
            n_prompts += 1
            out += ["### %d. %s" % (i + 1, label), "```text", prompt, "```", ""]
        out += ["**Negative Prompt:** `%s`"
                % pb.build_negative(lk.get("negative_extra", b.get("negative_extra", ""))),
                "", "---", ""]

    texto = "\n".join(out)
    if "--stdout" in args:
        print(texto)
        return 0
    destino = args[args.index("--out") + 1] if "--out" in args else \
        os.path.join(AQUI, "output_%s.md" % os.path.splitext(os.path.basename(ruta))[0])
    open(destino, "w", encoding="utf-8", newline="\n").write(texto)
    print("✅ %d looks · %d prompts · 0 fallas de validación" % (len(b["looks"]), n_prompts))
    print("   escrito: %s" % destino)
    print("   verificar antes de pegar en la galería:")
    print("     python %s lint %s" % (os.path.basename(__file__), b["personaje"]))
    return 0


# ------------------------------------------------------------------ delegacion

def _correr(script, extra):
    return subprocess.call([sys.executable, os.path.join(AQUI, script)] + list(extra), cwd=RAIZ)


def cmd_modularidad(args):
    """Audita que el engine sea de verdad modular por personaje.

    Ama 29/08/2026: "el outfit engine debe ser modular, las poses son únicas para
    cada personaje, además cada uno tiene cosas que las diferencian".

    Sin una medida, "modular" es una intención. Esto la vuelve un número:

      1. Ningún nombre de personaje escrito en la LÓGICA del motor. Cada `if
         slug == "x"` es una rama que el siguiente personaje no hereda — asi
         nacio la excepcion de DRESS_LEG_CLOSURE que Miss Doll arrastro una
         semana y que solo existia para proteger una pose ya derogada.
      2. Cada personaje declara los campos que lo diferencian, en su perfil.
      3. Las sub-poses son PROPIAS: ninguna identica entre personajes, y ningun
         slot clonado. La taxonomia de los 7 slots es universal (misma toma de
         camara); el CONTENIDO de cada toma es de cada muñeca.
    """
    import difflib
    import glob
    import itertools
    import re as _re

    cfg = cargar_config()
    reps = json.load(open(os.path.join(AQUI, "repertorios_pose.json"), encoding="utf-8"))
    slugs = list(cfg["personajes"])
    fallos = 0

    print("=" * 74)
    print("MODULARIDAD DEL OUTFIT-ENGINE")
    print("=" * 74)

    # 1 -- personajes hardcodeados en la logica
    print("\n1. Nombres de personaje en la LÓGICA del motor")
    rx = _re.compile(r"""(?:slug|personaje)\s*==\s*["'](%s)["']""" % "|".join(slugs))
    duros = []
    for f in sorted(glob.glob(os.path.join(AQUI, "*.py"))):
        for i, linea in enumerate(open(f, encoding="utf-8", errors="replace"), 1):
            if rx.search(linea) and not linea.lstrip().startswith("#"):
                duros.append("%s:%d  %s" % (os.path.basename(f), i, linea.strip()[:80]))
    if duros:
        fallos += len(duros)
        for d in duros:
            print("   \U0001f534 %s" % d)
    else:
        print("   ok   ninguno — lo que difiere sale del perfil, no de una rama del código")

    # 2 -- campos que diferencian, declarados
    print("\n2. Campos propios declarados por personaje")
    ESPERADOS = ("perfil_visual", "galeria", "carpeta_imagenes", "prefijo_archivo",
                 "prefijo_carpeta_look", "slot5_nombre", "slot5_slug", "emoji_look")
    for slug in slugs:
        p = cfg["personajes"][slug]
        faltan = [c for c in ESPERADOS if not p.get(c)]
        propios = [k for k in p if k not in ESPERADOS and not k.startswith("_")]
        if faltan:
            fallos += 1
            print("   \U0001f534 %-10s faltan: %s" % (slug, ", ".join(faltan)))
        else:
            print("   ok   %-10s %d campos base + %d propios (%s)"
                  % (slug, len(ESPERADOS), len(propios), ", ".join(propios) or "—"))

    # 3 -- sub-poses propias
    print("\n3. Sub-poses propias de cada personaje")
    P = reps["personajes"]
    for slug in slugs:
        s = P.get(slug, {}).get("slots", {})
        print("   %-10s %d sub-poses en %d slots" % (slug, sum(len(v) for v in s.values()), len(s)))
    idem, clonados = [], []
    for a, b in itertools.combinations(slugs, 2):
        for slot in sorted(set(P.get(a, {}).get("slots", {})) & set(P.get(b, {}).get("slots", {}))):
            va, vb = P[a]["slots"][slot], P[b]["slots"][slot]
            comunes = [x for x in va if x in vb]
            if comunes:
                idem.append((slot, a, b, len(comunes)))
            m = sum(max(difflib.SequenceMatcher(None, x, y).ratio() for y in vb) for x in va) / len(va)
            if m > 0.70:
                clonados.append((slot, a, b, m))
    if idem:
        fallos += sum(n for *_r, n in idem)
        for slot, a, b, n in idem:
            print("   \U0001f534 %-14s %s ↔ %s: %d sub-pose(s) IDÉNTICAS" % (slot, a, b, n))
    else:
        print("   ok   ninguna sub-pose idéntica entre personajes")
    umbral = "--estricto" in args
    for slot, a, b, m in clonados:
        marca = "\U0001f534" if umbral else "⚠ "
        if umbral:
            fallos += 1
        print("   %s %-14s %s ↔ %s: repertorio clonado al %.1f%%" % (marca, slot, a, b, m * 100))
    if not clonados:
        print("   ok   ningún slot con repertorio clonado (>70%)")

    print("\n" + "-" * 74)
    print("MODULARIDAD: %s" % ("LIMPIA" if not fallos else "\U0001f534 %d problema(s)" % fallos))
    print("-" * 74)
    return 1 if fallos else 0


def cmd_test(_args):
    """Corre los self-checks de la capa de reglas. NO auditan la flota."""
    print("Self-checks de la capa de reglas (fixtures, NO la flota):\n")
    fallo = 0
    for s in ("footwear_canon.py", "garment_canon.py", "color_canon.py"):
        r = subprocess.run([sys.executable, os.path.join(AQUI, s)], cwd=RAIZ,
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
        linea = [l for l in (r.stdout or "").strip().split("\n") if "self-check" in l.lower()]
        estado = linea[-1].split(":", 1)[-1].strip() if linea else "sin veredicto"
        malo = "LIMPIO" not in estado
        fallo += malo
        print("  %s %-20s %s" % ("\U0001f534" if malo else "  ok  ", s, estado))
    print("\n  Para medir la FLOTA (no los fixtures): outfit.py auditar")
    return 1 if fallo else 0


COMANDOS = {
    "generar":     (cmd_generar, "emite un batch de looks desde su JSON de datos"),
    "adn":         (lambda a: _correr("prompt_builder.py", ["--adn"] + a),
                    "verifica el dueño único del BLOQUE A contra batches y galería"),
    "lint":        (lambda a: _correr("lint_prompts_personaje.py", a),
                    "parsea las galerías como LV-App y avisa anclas faltantes"),
    "auditar":     (lambda a: _correr("auditar_canon_flota.py", a),
                    "corre el canon de calzado y vestuario sobre la FLOTA REAL"),
    "anclas":      (lambda a: _correr("inyectar_anclas.py", a),
                    "inyecta anclas faltantes en una galería ya escrita"),
    "stats":       (lambda a: _correr("count_stats.py", a), "estadísticas de la flota"),
    "personajes":  (lambda a: _correr("prompt_builder.py", ["--personajes"] + a),
                    "personajes registrados en el engine"),
    "poses":       (lambda a: _correr("prompt_builder.py", ["--poses"] + a),
                    "repertorio de sub-poses de un personaje"),
    "modularidad": (cmd_modularidad,
                    "audita que el engine sea modular: 0 personajes en el código, "
                    "campos propios declarados, sub-poses únicas (--estricto)"),
    "test":        (cmd_test, "self-checks de la capa de reglas (fixtures, no la flota)"),
}


def main():
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help", "help"):
        print(__doc__.split("USO\n---")[0].strip())
        print("\nCOMANDOS\n" + "-" * 8)
        for nombre, (_f, ayuda) in COMANDOS.items():
            print("  %-12s %s" % (nombre, ayuda))
        print("\n  outfit.py <comando> --help  para el detalle de cada uno")
        return 0
    cmd = args[0]
    if cmd not in COMANDOS:
        print("comando desconocido: %s\ncomandos: %s" % (cmd, ", ".join(COMANDOS)))
        return 2
    return COMANDOS[cmd][0](args[1:])


if __name__ == "__main__":
    sys.exit(main())
