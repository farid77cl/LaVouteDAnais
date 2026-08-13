#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
inyectar_anclas.py — Retrofit de anclas anti-defecto sobre galerias YA escritas.

QUE HACE
--------
Lee la galeria de un personaje **parseandola como la parsea LV-App**, detecta que
anclas del contrato le faltan a cada prompt y las **inyecta en el texto existente**,
sin reescribir la pose, el outfit ni el setting propios de ese look.

POR QUE NO REENSAMBLA
---------------------
`prompt_builder.build()` construye un prompt desde cero a partir de BLOQUE A/B/C.
Sirve para looks NUEVOS. Para una galeria ya escrita, reensamblar obligaria a
re-derivar la clausula de pose y el setting de cada look — y ahi es donde vive la
riqueza propia de cada uno (el objeto en la mano, el mueble, la accion). El 13/08
se decidio NO sobrescribir los 98 de Anais justamente por eso. Este script hace lo
contrario: **conserva el texto y agrega lo que falta**.

DONDE INYECTA
-------------
Todas las anclas viven en la COLA del prompt, despues del setting. La unica regla
de orden que importa es que **FOOTWEAR_ECHO cierra siempre** (asi lo arma el
builder: el calzado se repite al final porque en Back View y en las poses bajas
queda lejos del bloque que lo describe). Entonces:

    ... setting, [anclas existentes] , [anclas inyectadas] , FOOTWEAR_ECHO.

Si FOOTWEAR_ECHO ya esta, lo nuevo entra ANTES de el. Si falta y toca, se agrega
al final del todo.

PRESENCIA: se detecta por los primeros 45 chars del ancla — el mismo criterio que
usa el linter. En la flota de Ele hay 2.617 anclas con la redaccion vieja (mismo
prefijo, cola distinta): esas cuentan como PRESENTES y no se duplican.

ANCLAS OPT-IN
-------------
ASYMMETRY_LOCK / ACCESSORY_COUNT_LOCK / GARMENT_EXCLUSION_LOCK no aplican a todo
look: las dispara la descripcion del outfit. Como la galeria de Ele no tiene campo
BLOQUE B separado (el outfit vive dentro del prompt), las regex del builder se
corren sobre el prompt completo. Se agregan solo con --opt-in.

⚠️ Esa aproximacion tiene un falso positivo medido (13/08/2026): en Ele, el token
`no gloves of any kind` aparece en 4.207 prompts porque es clausula UNIVERSAL de su
ADN (los guantes le estan prohibidos por canon) y ya lo cubre su propia ancla
NO_ARMWEAR — no es una ausencia declarada por look, que es el caso para el que se
escribio GARMENT_EXCLUSION_LOCK (el `no corset` del Look 04 de Miss Doll). Por eso
existe --sin: `--sin=GARMENT_EXCLUSION_LOCK` en Ele. En Anais el mismo disparador
SI es legitimo (`bare legs, no stockings` declarado en su BLOQUE B, look por look).

ALCANCE (--solo-sin-imagen)
---------------------------
Reescribir un prompt cuya pose YA tiene imagen no cambia ninguna imagen: solo
genera churn. La convencion del repo es retrofit-al-tocar. Con --solo-sin-imagen
se tocan unicamente las poses **sin archivo en el indice de git** — el riesgo vivo
real, lo que la app todavia va a generar. (El disco miente: los PNG llevan
skip-worktree, la fuente de verdad es `git ls-files`.)

USO
---
    python 99_Sistema/scripts/visual/inyectar_anclas.py anais --dry-run
    python 99_Sistema/scripts/visual/inyectar_anclas.py anais
    python 99_Sistema/scripts/visual/inyectar_anclas.py ele --solo-sin-imagen --dry-run
    python 99_Sistema/scripts/visual/inyectar_anclas.py ele --solo-sin-imagen --opt-in

Verificacion obligatoria despues: `lint_prompts_personaje.py <personaje>`.
"""

import io
import os
import re
import subprocess
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", ".."))
sys.path.insert(0, AQUI)
from prompt_builder import PromptBuilder, cargar_config  # noqa: E402
from lint_prompts_personaje import LOOK_HEADING, detectar_pose  # noqa: E402

# Un prompt real de este motor (ADN + outfit + anclas) no baja de ~1.500 chars.
# Por debajo de 600 es una linea de metadata que el parser confunde con prompt
# inline (caso documentado: los slugs que contienen "back").
MIN_PROMPT = 600

SLOT_POR_NOMBRE = {
    "Standing": "standing", "Back View": "back_view", "Seated": "seated",
    "Side Profile": "side_profile", "POV": "pov", "Odalisque": "odalisque",
}
ARCHIVO_POR_NOMBRE = {
    "Standing": "standing", "Back View": "back_view", "Seated": "seated",
    "Side Profile": "side_profile", "POV": "pov", "Odalisque": "odalisque",
}


def imagenes_en_git(carpeta, prefijo):
    """(look, pose) que YA tienen archivo en el indice de git. Nunca en disco."""
    out = subprocess.run(["git", "ls-files", carpeta], capture_output=True,
                         text=True, cwd=RAIZ).stdout
    rx = re.compile(re.escape(prefijo) + r"(\d+)_([a-z_]+)\.(?:png|jpg|jpeg|webp)$")
    vistas = set()
    for linea in out.splitlines():
        m = rx.search(os.path.basename(linea).lower())
        if m:
            vistas.add((int(m.group(1)), m.group(2)))
    return vistas


def recorrer_prompts(lineas, slot5_nombre):
    """
    Genera (look_num, pose_nombre, indice_de_linea) por cada prompt en fence.

    Espeja el arbol de decision del parser de la app (misma deteccion de heading
    y de pose), pero devolviendo la POSICION en el archivo para poder reescribir.
    """
    look = None
    pose_pendiente = None
    dentro = False
    inicio = None
    for i, linea in enumerate(lineas):
        t = linea.strip()
        if t.startswith("#"):
            m = LOOK_HEADING.match(t)
            if m:
                look = int(m.group(1))
                pose_pendiente = None
                dentro = False
                continue
        if look is None:
            continue

        if dentro:
            if t.startswith("```"):
                dentro = False
                for j in range(inicio, i):
                    if len(lineas[j].strip()) >= MIN_PROMPT:
                        yield look, pose_actual, j
                pose_pendiente = None
            continue

        if t.startswith("```"):
            if pose_pendiente:
                dentro = True
                inicio = i + 1
                pose_actual = pose_pendiente
            continue

        if not t.startswith("`") and (len(t) < 100 or "prompt" in t.lower()):
            p = detectar_pose(t, slot5_nombre)
            if p:
                pose_pendiente = p


def anclas_requeridas(pb, slot, prompt, con_opt_in, excluidas=()):
    """Nombres de ancla que este prompt DEBE llevar, en orden de escritura."""
    nombres = list(pb.anclas_de_slot(slot))
    if con_opt_in:
        # n_globales = `_todos` + las `anclas_siempre` del personaje (13/08/2026).
        # Antes era len(mapa["_todos"]) a mano y las opt-in se colaban ANTES de
        # BOTTOM_CUT_LOCK, desordenando el bloque global.
        n_globales = pb.n_globales
        for n in pb.opt_in_de(prompt):
            if n not in nombres and n not in excluidas:
                nombres.insert(n_globales, n)
    # FOOTWEAR_ECHO siempre al final.
    if "FOOTWEAR_ECHO" in nombres:
        nombres = [n for n in nombres if n != "FOOTWEAR_ECHO"] + ["FOOTWEAR_ECHO"]
    return nombres


def inyectar(pb, prompt, slot, con_opt_in, excluidas=()):
    """Devuelve (prompt_nuevo, [anclas_agregadas]). Idempotente."""
    requeridas = anclas_requeridas(pb, slot, prompt, con_opt_in, excluidas)
    faltan = [n for n in requeridas if pb.anclas[n]["texto"][:45] not in prompt]
    if not faltan:
        return prompt, []

    eco = pb.anclas["FOOTWEAR_ECHO"]["texto"]
    eco_falta = "FOOTWEAR_ECHO" in faltan
    cuerpo = [n for n in faltan if n != "FOOTWEAR_ECHO"]

    nuevo = prompt
    if cuerpo:
        texto = ", ".join(pb.anclas[n]["texto"] for n in cuerpo)
        pos = nuevo.find(eco[:45])
        if pos > 0:
            # Entra ANTES del eco de calzado, que debe seguir cerrando.
            nuevo = nuevo[:pos].rstrip(" ,") + ", " + texto + ", " + nuevo[pos:]
        else:
            nuevo = nuevo.rstrip().rstrip(".").rstrip(" ,") + ", " + texto + "."
    if eco_falta:
        nuevo = nuevo.rstrip().rstrip(".").rstrip(" ,") + ", " + eco + "."
    return nuevo, faltan


def main():
    cfg = cargar_config()
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    dry = "--dry-run" in sys.argv or "-n" in sys.argv
    solo_sin_img = "--solo-sin-imagen" in sys.argv
    con_opt_in = "--opt-in" in sys.argv
    excluidas = []
    for a in sys.argv[1:]:
        if a.startswith("--sin="):
            excluidas += [x.strip().upper() for x in a[6:].split(",") if x.strip()]
    if not args:
        print(__doc__)
        return 1

    slug = args[0]
    pb = PromptBuilder(slug, cfg)
    perfil = pb.perfil
    ruta = os.path.join(RAIZ, perfil["galeria"].replace("/", os.sep))
    slot5_nombre = perfil["slot5_nombre"]
    slot_por_nombre = dict(SLOT_POR_NOMBRE)
    slot_por_nombre[slot5_nombre] = "slot5"
    archivo_por_nombre = dict(ARCHIVO_POR_NOMBRE)
    archivo_por_nombre[slot5_nombre] = perfil["slot5_slug"]

    con_imagen = set()
    if solo_sin_img:
        con_imagen = imagenes_en_git(perfil["carpeta_imagenes"], perfil["prefijo_archivo"])

    texto = io.open(ruta, encoding="utf-8", newline="").read()
    salto = "\r\n" if "\r\n" in texto else "\n"
    lineas = texto.split(salto)

    tocados = 0
    saltados_con_img = 0
    por_ancla = {}
    looks_tocados = set()

    for look, pose, idx in recorrer_prompts(lineas, slot5_nombre):
        slot = slot_por_nombre.get(pose)
        if not slot:
            continue
        if solo_sin_img and (look, archivo_por_nombre.get(pose, "")) in con_imagen:
            saltados_con_img += 1
            continue
        original = lineas[idx]
        nuevo, agregadas = inyectar(pb, original.strip(), slot, con_opt_in, excluidas)
        if not agregadas:
            continue
        lineas[idx] = nuevo
        tocados += 1
        looks_tocados.add(look)
        for n in agregadas:
            por_ancla[n] = por_ancla.get(n, 0) + 1

    print("=" * 78)
    print("INYECCION DE ANCLAS — %s (%s)" % (perfil["nombre"], slug))
    print("  galeria        : %s" % perfil["galeria"])
    print("  alcance        : %s" % ("solo poses SIN imagen en git (riesgo vivo)"
                                     if solo_sin_img else "todos los prompts"))
    print("  anclas opt-in  : %s" % ("si (disparadas por el outfit)" if con_opt_in else "no"))
    if excluidas:
        print("  opt-in excluida: %s" % ", ".join(excluidas))
    print("=" * 78)
    if solo_sin_img:
        print("  poses con imagen, no tocadas : %d" % saltados_con_img)
    print("  prompts modificados          : %d  (en %d looks)" % (tocados, len(looks_tocados)))
    for n, c in sorted(por_ancla.items(), key=lambda x: -x[1]):
        print("      + %-22s %d" % (n, c))

    if dry:
        print("\n  DRY-RUN — no se escribio nada.")
        return 0
    if tocados:
        io.open(ruta, "w", encoding="utf-8", newline="").write(salto.join(lineas))
        print("\n  ESCRITO: %s" % perfil["galeria"])
        print("  Verificar ahora: python 99_Sistema/scripts/visual/lint_prompts_personaje.py %s" % slug)
    else:
        print("\n  Nada que inyectar — la galeria ya cumple el contrato.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
