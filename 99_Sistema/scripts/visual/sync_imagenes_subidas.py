#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sync_imagenes_subidas.py — Flujo de sincronización de imágenes subidas por la app Android (Gemini → GitHub).

La app móvil sube imágenes generadas en Gemini directamente al repo. Este script:
  1. NORMALIZA los nombres no-canónicos que usa la app SOLO en la era app (looks >= MIN_LOOK):
        ele_<N>_back.png    -> ele_<N>_back_view.png
        ele_<N>_profile.png -> ele_<N>_side_profile.png
     (el resto de poses ya coinciden: standing, seated, ditzy, pov, odalisque).
  2. ACTUALIZA el tracker en 00_Ele/galeria_outfits.md: regenera la sección "### 📸 Imágenes" SOLO de
     los looks >= MIN_LOOK cuya sección esté en "Pendiente cuota API" o "Materializado parcial (app/Gemini)".
     Las pasa a "N/7" con la tabla de View links según las imágenes presentes (⏳ Pendiente las que faltan).
  3. Es IDEMPOTENTE y ACOTADO: NO toca el fleet histórico (<MIN_LOOK), que usa nombres timestamped/curados
     a mano. Correr de nuevo tras subir más poses actualiza solo el conteo de la era app.

Después de correr esto, ejecutar update_galleries.py para regenerar los README de cada carpeta + galería maestra.

  4. MODO ARCHIVO (--archivo, 22/07/2026): desde el 20/07 la app también materializa los looks
     del archivo histórico (`galeria_outfits_archivo.md`), que la app SÍ lee. Ahí la era NO se
     puede deducir del número —el L105 es del archivo y aun así llega con nombre canónico— sino
     del NOMBRE del archivo: solo cuentan las poses `ele_<N>_<pose>.png` que reconoce
     buscar_pose(). Los nombres curados a mano (`v1_standing.png`, `look106_v1.png`) NO cuentan
     y por eso NO pueden inventar un tracker: si un look del archivo no tiene ni una pose
     canónica, se lo deja intacto. Sin esa guardia insertaríamos «0/7» sobre looks que sí tienen
     imágenes viejas — la mentira del tracker del 14/07 otra vez, y con el mismo costo en cuota.

Uso:  python 99_Sistema/scripts/visual/sync_imagenes_subidas.py [MIN_LOOK]
      python 99_Sistema/scripts/visual/sync_imagenes_subidas.py --archivo
      (MIN_LOOK por defecto = 291, primer batch generado por la app)
"""
import os, re, subprocess, sys

sys.stdout.reconfigure(encoding="utf-8")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", ".."))
ELE = os.path.join(REPO, "05_Imagenes", "ele")

# Lectura y escritura salen de la MISMA variable a propósito: el 20/07/2026 un inyector
# cambió la lectura a `galeria_outfits_archivo.md` y dejó la escritura en la constante vieja
# → escribió el archivo encima de la galería viva y borró 38.888 líneas.
ARGS = [a for a in sys.argv[1:]]
MODO_ARCHIVO = "--archivo" in ARGS
ARGS = [a for a in ARGS if a != "--archivo"]

GALERIA = os.path.join(REPO, "00_Ele",
                       "galeria_outfits_archivo.md" if MODO_ARCHIVO else "galeria_outfits.md")

# En el archivo la era la define el NOMBRE del PNG, no el número del look → sin piso numérico.
MIN_LOOK = int(ARGS[0]) if ARGS else (0 if MODO_ARCHIVO else 291)

POSES = [
    ("standing",     "Standing"),
    ("back_view",    "Back View"),
    ("seated",       "Seated"),
    ("side_profile", "Side Profile"),
    ("ditzy",        "Ditzy (plano 3/4)"),
    ("pov",          "POV (single hand)"),
    ("odalisque",    "Odalisque"),
]

def git_mv(src, dst):
    try:
        subprocess.run(["git", "mv", src, dst], cwd=REPO, capture_output=True, text=True, check=True)
        return True
    except Exception:
        try:
            os.rename(src, dst); return True
        except Exception as e:
            print(f"  ! No se pudo renombrar {src}: {e}"); return False

def look_num(folder):
    m = re.match(r"look0*(\d+)_", folder.lower())
    return int(m.group(1)) if m else None

def normalizar_nombres():
    """Normaliza SOLO ele_<N>_back.png / ele_<N>_profile.png para N >= MIN_LOOK."""
    cambios = 0
    if not os.path.isdir(ELE):
        return cambios
    for folder in os.listdir(ELE):
        fpath = os.path.join(ELE, folder)
        n = look_num(folder)
        if not os.path.isdir(fpath) or n is None or n < MIN_LOOK:
            continue
        for canon, bad in (("back_view", "back"), ("back_view", "espalda"), ("side_profile", "profile"), ("side_profile", "perfil"), ("seated", "sentada")):
            src = os.path.join(fpath, f"ele_{n}_{bad}.png")
            dst = os.path.join(fpath, f"ele_{n}_{canon}.png")
            if os.path.exists(src) and not os.path.exists(dst):
                if git_mv(src, dst):
                    print(f"  ↳ {folder}/ele_{n}_{bad}.png -> ele_{n}_{canon}.png")
                    cambios += 1
    return cambios

_INDICE = None

def indice_git():
    """{carpeta: {archivo.png}} leído del ÍNDICE DE GIT, no del disco.

    Antes esto hacía os.listdir(). En las máquinas con sparse-checkout / skip-worktree
    (la solo-literaria tiene 0 PNG en disco) el tracker se reescribía a la baja y
    declaraba pendientes cientos de poses que sí existen en el repo — la misma mentira
    del 14/07 pero al revés, y con el mismo costo: cuota quemada regenerando lo que ya
    está. `update_galleries.py` ya usaba git ls-files; ahora ambos miden lo mismo.
    """
    global _INDICE
    if _INDICE is None:
        _INDICE = {}
        res = subprocess.run(["git", "ls-files", "05_Imagenes/ele"], cwd=REPO,
                             capture_output=True, text=True, encoding="utf-8")
        for ruta in res.stdout.splitlines():
            m = re.match(r"05_Imagenes/ele/([^/]+)/([^/]+\.png)$", ruta, re.I)
            if m:
                _INDICE.setdefault(m.group(1), set()).add(m.group(2))
    return _INDICE

def folders_de_look(n):
    """TODAS las carpetas del look. Un mismo look puede tener 2 slugs distintos
    (la app y el agente los nombraron distinto) con las poses repartidas entre ambas."""
    pref = re.compile(rf"^look0*{n}_", re.I)
    found = [f for f in indice_git() if pref.match(f)]
    # la carpeta con más PNG manda cuando una pose está en las dos
    return sorted(found, key=lambda f: (-len(imgs_de_look(f)), f))

def imgs_de_look(folder):
    return set(indice_git().get(folder, ()))

def buscar_pose(n, key, folders):
    """Devuelve (folder, filename) de la pose, o None.

    Tres nomenclaturas conviven y las TRES cuentan:
      · canónica            ele_313_back_view.png
      · con timestamp API   ele_313_back_view_1783817436657.png
      · slug largo          ele_look300_black_satin_veiled_femme_fatale_noir_back_view.png
    El slug largo no se reconocía y el tracker declaraba pendientes poses que sí existen
    (L299 4/7 y L300 2/7 cuando ambos están completos, 19/07). La pose va ANCLADA AL FINAL,
    así que un slug que contenga una palabra de pose no puede robar el match.

    ALIAS DE POSE (22/07/2026): en el archivo histórico conviven nombres que la normalización
    nunca alcanzó a corregir, porque `normalizar_nombres()` trabaja sobre el DISCO y esta
    máquina tiene skip-worktree con 0 PNG. Al extender el sync al archivo, 8 looks perdían 12
    links que apuntaban a imágenes REALES: `ele_136_back.png`, `ele_165_pose2_back.png` y los
    `ele_1NN_lying.png` (así se llamaba la Odalisque en la era vieja). Sin estos alias el fix
    "pasaba" con más links que antes y aun así destruía referencias vivas — el patrón exacto
    de `feedback_fix_que_hace_pasar_puede_corromper` (20/07). El ancla `$` impide que el alias
    corto le robe el match al canónico: `back_view.png` nunca casa con la alternativa `back`.
    """
    alias = {"back_view": ["back_view", "back"],
             "side_profile": ["side_profile", "profile"],
             "odalisque": ["odalisque", "lying"]}.get(key, [key])
    # El canónico se prueba PRIMERO y en todas las carpetas antes de bajar al alias: si un look
    # tiene `ele_86_back_view.png` y `ele_86_back.png`, el sort alfabético entregaría el alias
    # ("back.png" < "back_view.png") y el tracker apuntaría al nombre viejo teniendo el bueno.
    for candidato in alias:
        rx = re.compile(rf"^ele_(?:look)?0*{n}_(?:.*_)?{candidato}(_\d+)?\.png$", re.I)
        for folder in folders:
            for f in sorted(imgs_de_look(folder)):
                if rx.match(f):
                    return folder, f
    return None

def construir_seccion(n, folders):
    cells, mat = [], 0
    for key, _ in POSES:
        hit = buscar_pose(n, key, folders)
        if hit:
            folder, fname = hit
            cells.append(f"[📸 View](../../05_Imagenes/ele/{folder}/{fname})")
            mat += 1
        else:
            cells.append("⏳ Pendiente")
    estado = "Materializado" if mat == 7 else "Materializado parcial (app/Gemini)"
    headers = " | ".join(lbl for _, lbl in POSES)
    seps = " | ".join([":---:"] * len(POSES))
    texto = (f"### 📸 Imágenes ({mat}/7 — {estado})\n\n"
             f"| {headers} |\n| {seps} |\n| {' | '.join(cells)} |\n\n")
    return texto, mat

def insertar_seccion(block, nueva):
    """Inserta la sección 📸 DESPUÉS de los bullets de metadata y ANTES de los prompts.

    El orden importa y no es cosmético: el 13/07 se encontraron 60 looks con «### 📸 Imágenes»
    puesto ANTES de Ubicacion/Tags, y eso dejaba vacío el `canonicalInfo` que la app usa para
    el chat y el contexto. La metadata va primero, el tracker después, los prompts al final.
    """
    for ancla in (r"^### 📝 ", r"^\*\*\s*1\.\s*Standing", r"^\*\*Standing:\*\*"):
        m = re.search(ancla, block, re.MULTILINE)
        if m:
            return block[:m.start()] + nueva + block[m.start():]
    return block.rstrip("\n") + "\n\n" + nueva

def actualizar_galeria():
    with open(GALERIA, encoding="utf-8") as f:
        content = f.read()
    parts = re.split(r"(?=^## .*?Look \d+:)", content, flags=re.MULTILINE)
    out, actualizados, rutas_corregidas = [], [], []
    # La sección 📸 va desde su heading hasta el siguiente heading (##/###) o hasta el primer
    # prompt suelto (**Standing:**). NO se puede anclar en "### 📝 Prompts": la mitad de los looks
    # no tiene ese heading y quedaban invisibles al sync (L717/L732 llevaban días en 0/7 con las
    # 7 imágenes en disco, y la Ama regeneraba lo que ya existía).
    # El ancla de corte DEBE cubrir las dos formas en que se escriben los prompts sueltos:
    # `**Standing:**` y `**1. Standing:**`. Reconocer solo la primera es destructivo: en un
    # look numerado y sin heading `### 📝`, la sección 📸 se comía TODOS los prompts hasta el
    # siguiente `##` y construir_seccion los reemplazaba por la tabla. Medido el 22/07/2026:
    # 63 prompts (9 looks × 7 poses, L691-L700) borrados en el árbol de trabajo. No llegó a
    # commitearse porque el conteo de prompts se comparó contra HEAD antes de guardar.
    img_re = re.compile(
        r"^### 📸 Imágenes[^\n]*\n(?:(?!^#{2,3}\s|^\*\*\s*\d*\.?\s*Standing:?\*\*).*\n)*",
        re.MULTILINE)
    for block in parts:
        m = re.match(r"^## .*?Look (\d+):", block)
        if not m:
            out.append(block); continue
        n = int(m.group(1))
        sec = img_re.search(block)
        if n < MIN_LOOK:
            out.append(block); continue
        if not sec:
            # Sin sección 📸: la insertamos SOLO si el look ya tiene al menos una pose con
            # nombre canónico (`ele_<N>_<pose>.png`). Los looks 102-113 del archivo estrenaron
            # prompts el 21/07 y la app los empezó a materializar sin que existiera contador:
            # las subidas no se veían en ninguna parte. La guardia mat>=1 es la que impide
            # estampar un «0/7» sobre un look que sí tiene imágenes con nombre curado a mano.
            folders = folders_de_look(n)
            if folders and any(imgs_de_look(f) for f in folders):
                nueva, mat = construir_seccion(n, folders)
                if mat >= 1:
                    block = insertar_seccion(block, nueva)
                    actualizados.append((n, -1, mat))
            out.append(block); continue
        actual = sec.group(0)
        folders = folders_de_look(n)
        if folders and any(imgs_de_look(f) for f in folders):
            nueva, mat = construir_seccion(n, folders)
            m_trk = re.search(r"### 📸 Imágenes \((\d+)/7", actual)
            declarado = int(m_trk.group(1)) if m_trk else -1
            # Regenerar en cuanto la sección difiera del disco — NO basta comparar el conteo:
            # al fusionar/renombrar una carpeta el conteo queda igual pero las RUTAS de los links
            # apuntan a una carpeta que ya no existe (49 links rotos tras la fusión del 14/07).
            if actual.strip() != nueva.strip():
                block = block[:sec.start()] + nueva + block[sec.end():]
                if declarado != mat:
                    actualizados.append((n, declarado, mat))
                else:
                    rutas_corregidas.append(n)
        out.append(block)
    nuevo = "".join(out)

    # GUARDIA DE NO-DESTRUCCIÓN: este script toca SOLO la sección 📸. Si el número de
    # prompts o de fichas cambió, algún regex se comió contenido que no le tocaba y es
    # preferible abortar ruidosamente a guardar la pérdida (22/07/2026: un ancla de corte
    # incompleta borró 63 prompts). Falla fuerte, no en silencio.
    def censo(t):
        return (len(re.findall(r"^stunning woman with", t, re.MULTILINE)),
                len(re.findall(r"^## .*?Look \d+:", t, re.MULTILINE)),
                len(re.findall(r"^\*\*Negative Prompt", t, re.MULTILINE)))

    antes, despues = censo(content), censo(nuevo)
    if antes != despues:
        raise SystemExit(
            f"❌ ABORTADO sin escribir: el contenido no-📸 cambió.\n"
            f"   (prompts, fichas, negativos)  antes={antes}  después={despues}")

    if nuevo != content:
        with open(GALERIA, "w", encoding="utf-8") as f:
            f.write(nuevo)
    return actualizados, rutas_corregidas

def main():
    destino = os.path.basename(GALERIA)
    alcance = "ARCHIVO histórico (era por nombre ele_*)" if MODO_ARCHIVO else f"era app: looks >= {MIN_LOOK}"
    print(f"== Sync imágenes app (Gemini → GitHub) · {alcance} ==")
    print("1) Normalizando nombres no-canónicos (back→back_view, profile→side_profile)...")
    print(f"   {normalizar_nombres()} archivo(s) renombrado(s).")
    print(f"2) Actualizando tracker en {destino}...")
    upd, rutas = actualizar_galeria()
    if upd:
        # viejo == -1 marca «no había tracker»: esas poses no estaban declaradas pendientes,
        # así que no cuentan como recuperadas (sumarlas inflaría el número con un +1 fantasma).
        recup = sum(nuevo - viejo for _, viejo, nuevo in upd if viejo >= 0 and nuevo > viejo)
        for n, viejo, nuevo in sorted(upd):
            if viejo == -1:
                print(f"   L{n}: (sin tracker) → {nuevo}/7  🆕 sección insertada")
                continue
            flecha = "⬆️ recuperadas" if nuevo > viejo else "⬇️ corregido (decía de más)"
            print(f"   L{n}: {viejo}/7 → {nuevo}/7  {flecha}")
        print(f"   ── {len(upd)} look(s) corregidos · {recup} pose(s) reales que figuraban como pendientes")
    else:
        print("   (conteos ya coinciden con el disco)")
    if rutas:
        print(f"   🔗 {len(rutas)} look(s) con links re-apuntados a la carpeta correcta: "
              f"{', '.join('L'+str(n) for n in sorted(rutas)[:12])}{' …' if len(rutas)>12 else ''}")
    print("3) Ejecuta luego: python 99_Sistema/scripts/visual/update_galleries.py")

if __name__ == "__main__":
    main()
