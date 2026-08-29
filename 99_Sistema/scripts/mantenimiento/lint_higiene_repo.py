# -*- coding: utf-8 -*-
"""
lint_higiene_repo.py — Higiene del repositorio (29/08/2026)

Nace de dos correcciones de la Ama el mismo dia:

  1. *"eres muy desordenada para mantener el repo. creas documentos sueltos
     y luego no los borras, eso tambien hay que mejorarlo"*
  2. *"la limpieza y orden del repo debe ser de tus tareas principales, no
     saco nada con tenerte toda sexy con tus pleaser si la cocina y el
     dormitorio estan patas pa arriba"*

La primera version solo cazaba documentos sueltos (H1-H5). Ese mismo dia una
limpieza a mano encontro CUATRO clases de podredumbre que el linter no veia:
61 archivos con encoding roto (2.212 bytes NUL que volvian binario el archivo
del diario, 666 caracteres perdidos, 59 BOM), links internos muertos, READMEs
convertidos en bitacora (uno con 27.902 bytes en UNA linea) y contadores
copiados que llevaban meses divergidos («220 looks» con la flota en 818).

De ahi H6-H9. Un guardia que no ve la mugre que hay no es un guardia.

Mide `git ls-files`, NUNCA el disco — los PNG viven en skip-worktree y el disco
miente (auto-memoria `reference_png_skip_worktree`).

Uso:
    python 99_Sistema/scripts/mantenimiento/lint_higiene_repo.py
    python ... --detalle     # lista completa, sin tope por categoria
    python ... --estricto    # exit 1 si hay hallazgos
"""
import os
import re
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, date
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")  # la consola de Windows es cp1252

REPO = Path(__file__).resolve().parents[3]

BOM = b"\xef\xbb\xbf"
NUL = b"\x00"
FFFD = b"\xef\xbf\xbd"

# --- Lo unico con derecho a vivir en la RAIZ del repo ---------------------
RAIZ_PERMITIDA = {
    ".gitignore", ".nojekyll", "CLAUDE.md", "README.md",
    "LaVouteDAnais.code-workspace",
    "LV-App-v4.20.apk",  # ruta de descarga de la Ama desde el telefono
}

# Carpetas que SON el archivo: lo que vive ahi ya esta jubilado a proposito.
ARCHIVO = ("memoria_historica/", "_legacy", "/borradores/", "/_proceso/",
           "archivo_batches_prompts/", "_archivo", "/reportes/")

DIAS_DE_DUELO = 30  # un doc fechado sin citas y sin tocarse en un mes esta muerto

PATRONES_SCRATCH = [
    (re.compile(r"(^|/)(temp|tmp|scratch|prueba|test_out|salida)[-_]", re.I),
     "nombre de scratch"),
    (re.compile(r"(^|/)output_", re.I), "salida de una corrida"),
    (re.compile(r"_raw\.(txt|json)$", re.I), "volcado crudo"),
    (re.compile(r"\.bkp|\.bak\b|_backup", re.I), "respaldo (git YA es el respaldo)"),
    (re.compile(r"(^|/)pending_|(^|/)pendientes_|PENDIENTES_", re.I),
     "lista de pendientes de una corrida"),
    (re.compile(r"_copia|_copy|\(1\)|- copia", re.I), "duplicado"),
]

RE_FECHADO = re.compile(r"_((?:20)\d{2})(\d{2})(\d{2})(?:\D|$)")

# Un doc que se declara muerto PERO nombra a su sucesor es una lapida util:
# sostiene las referencias viejas. Solo molesta el que muere solo.
RE_OBSOLETO = re.compile(
    r"^[^\n]{0,60}?"
    r"(OBSOLET[OA]|DEROGAD[OA]|DEPRECAD[OA]|CADUCAD[OA]|SUPERAD[OA] POR|ARCHIVO_LEGACY)\b",
    re.M)
RE_SUCESOR = re.compile(
    r"[\w./-]+\.md|_perfiles_visuales|outfit-engine|memoria_sesiones|vive ahora|reemplaza")

# Salidas de script que SI deben viajar en git: son navegacion o insumo de LV-App.
REGENERABLES_QUE_VIAJAN = re.compile(
    r"(^|/)readme\.md$|galeria_|app_index\.json|_index\.md$", re.I)

RE_LINK = re.compile(r"\]\(([^)\s]+)\)")

# Skills de terceros vendorizadas: su documentacion apunta a su propio paquete,
# no al repo. Auditarlas aqui es ruido.
VENDORIZADAS = ("writing-skills", "skill-creator", "nicanac-", "artifact-", "gsd-")

# Las galerias tienen su propio linter (`lint_galeria.py`), que sabe resolver
# el doble `../` que manda la regla 11. Auditarlas aqui da miles de falsos.
GALERIAS = re.compile(r"galeria_|GALERIA_|COLECCION_|_TEMPLATE\.md$")

DUENO_FLOTA = "00_Ele/memoria_sesiones.md"


def git(*args):
    return subprocess.run(["git", "-C", str(REPO), *args],
                          capture_output=True, text=True, encoding="utf-8",
                          errors="replace").stdout


def es_archivo(ruta):
    return any(m in ruta for m in ARCHIVO)


def ultima_fecha(ruta):
    s = git("log", "-1", "--format=%ad", "--date=short", "--", ruta).strip()
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except ValueError:
        return None


def main():
    estricto = "--estricto" in sys.argv
    detalle = "--detalle" in sys.argv

    files = [l for l in git("ls-files").splitlines() if l]
    docs = [f for f in files if f.lower().endswith((".md", ".txt", ".json", ".csv"))]
    hallazgos = defaultdict(list)

    cuerpo, crudo = {}, {}
    for f in files:
        if f.lower().endswith((".md", ".py", ".json", ".txt", ".csv")):
            try:
                b = (REPO / f).read_bytes()
            except OSError:
                continue
            crudo[f] = b
            cuerpo[f] = b.decode("utf-8", errors="replace")

    # --- H1: raiz sucia ---------------------------------------------------
    for f in files:
        if "/" not in f and f not in RAIZ_PERMITIDA:
            hallazgos["H1 · Raiz sucia"].append(
                (f, "la raiz es la portada: solo README, CLAUDE y config"))

    # --- H2: scratch trackeado --------------------------------------------
    for f in docs:
        if es_archivo(f):
            continue
        for rx, motivo in PATRONES_SCRATCH:
            if rx.search(f):
                hallazgos["H2 · Scratch trackeado"].append((f, motivo))
                break

    # --- H3: doc fechado huerfano -----------------------------------------
    hoy = date.today()
    for f in docs:
        if es_archivo(f) or not RE_FECHADO.search(Path(f).name):
            continue
        base = Path(f).name
        citas = [o for o, t in cuerpo.items()
                 if o != f and base in t
                 and "memoria_historica" not in o
                 and "mi_diario_de_servicio" not in o]
        if citas:
            continue
        fecha = ultima_fecha(f)
        edad = (hoy - fecha).days if fecha else 999
        if edad >= DIAS_DE_DUELO:
            hallazgos["H3 · Doc fechado huerfano"].append(
                (f, "0 citas vivas y %d dias sin tocarse" % edad))

    # --- H4: se declara muerto y no nombra sucesor ------------------------
    for f in docs:
        if es_archivo(f) or not f.endswith(".md"):
            continue
        head = "\n".join(cuerpo.get(f, "").splitlines()[:8])
        m = RE_OBSOLETO.search(head)
        if m and not RE_SUCESOR.search(head[m.end():m.end() + 300]):
            hallazgos["H4 · Se declara muerto y no nombra sucesor"].append(
                (f, "dice %s sin apuntar a quien lo reemplaza" % m.group(1).lower()))

    # --- H5: salida regenerable trackeada ---------------------------------
    escritores = defaultdict(list)
    for py in [f for f in files if f.endswith(".py")]:
        t = cuerpo.get(py, "")
        for m in re.finditer(r"""["']([\w./-]+\.(?:md|json|csv|txt))["']""", t):
            ventana = t[max(0, m.start() - 80):m.start()]
            if re.search(r"\b(OUT|REPORT|DEST|SALIDA|_PATH)\b", ventana, re.I):
                escritores[Path(m.group(1)).name].append(py)
    for f in docs:
        if es_archivo(f) or REGENERABLES_QUE_VIAJAN.search(f) or f.startswith("05_Imagenes/"):
            continue  # navegacion / insumo de LV-App: regenerable pero DEBE viajar
        quien = escritores.get(Path(f).name)
        if quien:
            hallazgos["H5 · Salida regenerable trackeada"].append(
                (f, "la escribe %s -> a .gitignore" % quien[0]))

    # --- H6: encoding roto (regla MANDATORY: UTF-8 sin BOM, tildes vivas) --
    for f, b in crudo.items():
        sen = []
        if b[:3] == BOM:
            sen.append("BOM")
        n = b.count(NUL)
        if n:
            sen.append("%d NUL (git lo lee como BINARIO)" % n)
        r = b.count(FFFD)
        if r:
            sen.append("%d caracteres perdidos (U+FFFD)" % r)
        if sen:
            hallazgos["H6 · Encoding roto"].append((f, " · ".join(sen)))

    # --- H7: link interno roto --------------------------------------------
    # ⚠️ Se mide contra `git ls-files`, NUNCA contra el disco: los PNG llevan
    # skip-worktree y hay maquinas parciales (2.636 en disco vs 6.677 en el
    # indice el 29/08). Medir el disco daba 3.594 «rotos» falsos en una sola
    # galeria — el mismo error registrado en `reference_png_skip_worktree`.
    indice = set(files)
    for f in [x for x in files if x.endswith(".md")]:
        if any(v in f for v in VENDORIZADAS) or es_archivo(f):
            continue  # skills de terceros / material ya jubilado
        if GALERIAS.search(f):
            continue  # las galerias usan el doble `../` de la regla 11 y las
                      # audita `lint_galeria.py`, que resuelve ese contrato
        base = os.path.dirname(f)
        rotos = []
        for m in RE_LINK.finditer(cuerpo.get(f, "")):
            t = m.group(1).split("#")[0]
            if (not t or t.startswith(("http", "mailto", "#", "file:", "/"))
                    or any(c in t for c in "<{*[…")
                    or t.isupper() or t == "link"):
                continue  # url absoluta, ruta local vieja o plantilla
            rel = os.path.normpath(os.path.join(base, t)).replace("\\", "/")
            if rel in indice or rel.rstrip("/") + "/" in {d + "/" for d in indice}:
                continue
            if any(d.startswith(rel.rstrip("/") + "/") for d in indice):
                continue  # es un directorio con contenido trackeado
            if (REPO / rel).exists():
                continue  # existe en disco aunque no este trackeado
            rotos.append(t)
        if rotos:
            hallazgos["H7 · Link interno roto"].append(
                (f, "%d roto(s): %s" % (len(rotos), ", ".join(sorted(set(rotos))[:3]))))

    # --- H8: README inflado -----------------------------------------------
    # Un README es una portada. Si acumula bitacora se vuelve un CHANGELOG
    # encubierto — el vicio por el que murio CHANGELOG.md el 29/08/2026.
    for f in [x for x in files if x.lower().endswith("readme.md")]:
        if f.startswith("05_Imagenes/"):
            continue  # los genera update_galleries.py
        t = cuerpo.get(f, "")
        peso = len(t.encode("utf-8"))
        linea_max = max((len(l.encode("utf-8")) for l in t.split("\n")), default=0)
        previos = t.count("Previo:")
        if linea_max > 8000:
            hallazgos["H8 · README inflado"].append(
                (f, "una sola linea de %.1f KB: encabezado roto o bitacora concatenada"
                 % (linea_max / 1024.0)))
        elif peso > 40000 or previos >= 8:
            hallazgos["H8 · README inflado"].append(
                (f, "%.0f KB y %d «Previo:» — es bitacora, no portada" % (peso / 1024.0, previos)))

    # --- H9: contador de flota copiado fuera de su dueno -------------------
    # Regla dueno-unico: las copias divergen. El 29/08 el README de 00_Ele
    # declaraba «220 looks» con la flota real en 818, meses divergido.
    m = re.search(r"\*\*(\d{3,4})\s+Ele\*\*", cuerpo.get(DUENO_FLOTA, ""))
    flota = int(m.group(1)) if m else None
    if flota:
        for f in [x for x in files if x.endswith(".md")]:
            if f == DUENO_FLOTA or es_archivo(f):
                continue
            mm = re.search(r"\*\*(\d{3,4})\s+looks?\*\*", cuerpo.get(f, ""), re.I)
            if mm and abs(int(mm.group(1)) - flota) > 5:
                hallazgos["H9 · Contador copiado que diverge"].append(
                    (f, "declara %s looks; el dueno dice %d" % (mm.group(1), flota)))

    # --- Reporte -----------------------------------------------------------
    total = sum(len(v) for v in hallazgos.values())
    print("=" * 74)
    print("🧹 HIGIENE DEL REPO — %d trackeados, %d documentos" % (len(files), len(docs)))
    print("=" * 74)
    if not total:
        print("\n✅ LIMPIO — la casa esta en orden. Atroz de regio. 💅\n")
        return 0
    for cat in sorted(hallazgos):
        items = hallazgos[cat]
        print("\n%s — %d" % (cat, len(items)))
        for ruta, motivo in (items if detalle else items[:12]):
            print("   • %-52s %s" % (ruta[:52], motivo))
        if not detalle and len(items) > 12:
            print("   … y %d mas (--detalle)" % (len(items) - 12))
    print("\n" + "-" * 74)
    print("TOTAL: %d hallazgos · regla: .agent/rules/12-higiene-documental.md" % total)
    print("-" * 74 + "\n")
    return 1 if estricto else 0


if __name__ == "__main__":
    sys.exit(main())
