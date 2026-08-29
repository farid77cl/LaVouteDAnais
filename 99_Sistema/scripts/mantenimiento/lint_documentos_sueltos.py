# -*- coding: utf-8 -*-
"""
lint_documentos_sueltos.py — Higiene documental del repo (29/08/2026)

Nace de una correccion de la Ama: *"eres muy desordenada para mantener el repo.
Creas documentos sueltos y luego no los borras, eso tambien hay que mejorarlo"*.

Medido ese dia, todo trackeado y todo invisible porque nadie lo contaba:
20 archivos de cache de graphify en la raiz, 8 scratch de prompts, un respaldo de
galeria de 7,35 MB, un experimento `.agents/` muerto hacia dos meses, 27 prompts
de un flujo derogado el 28/08 y un `.env` con credenciales.

La leccion propia del repo, aplicada a si mismo: una regla sin script que la mida
es un recuerdo. Este script es la medida.

Mide `git ls-files`, NUNCA el disco — los PNG viven en skip-worktree y el disco
miente (ver auto-memoria `reference_png_skip_worktree`).

Uso:
    python 99_Sistema/scripts/mantenimiento/lint_documentos_sueltos.py
    python ... --detalle     # lista completa, sin tope de 12 por categoria
    python ... --estricto    # exit 1 si hay hallazgos (para cierre de sesion)
"""
import re
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, date
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")  # la consola de Windows es cp1252

REPO = Path(__file__).resolve().parents[3]

# --- Lo unico con derecho a vivir en la RAIZ del repo ---------------------
# La raiz es la portada. Todo lo demas tiene una carpeta que lo reclama.
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

    cuerpo = {}
    for f in files:
        if f.lower().endswith((".md", ".py", ".json")):
            try:
                cuerpo[f] = (REPO / f).read_text(encoding="utf-8", errors="replace")
            except OSError:
                cuerpo[f] = ""

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

    # --- H3: doc fechado huerfano (nadie lo cita y ya paso el duelo) ------
    hoy = date.today()
    for f in docs:
        if es_archivo(f) or not RE_FECHADO.search(Path(f).name):
            continue
        base = Path(f).name
        citas = [o for o, txt in cuerpo.items()
                 if o != f and base in txt
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
        txt = cuerpo.get(py, "")
        for m in re.finditer(r"""["']([\w./-]+\.(?:md|json|csv|txt))["']""", txt):
            ventana = txt[max(0, m.start() - 80):m.start()]
            if re.search(r"\b(OUT|REPORT|DEST|SALIDA|_PATH)\b", ventana, re.I):
                escritores[Path(m.group(1)).name].append(py)
    for f in docs:
        if es_archivo(f) or REGENERABLES_QUE_VIAJAN.search(f) or f.startswith("05_Imagenes/"):
            continue  # navegacion / insumo de LV-App: regenerable pero DEBE viajar
        quien = escritores.get(Path(f).name)
        if quien:
            hallazgos["H5 · Salida regenerable trackeada"].append(
                (f, "la escribe %s -> a .gitignore" % quien[0]))

    # --- Reporte -----------------------------------------------------------
    total = sum(len(v) for v in hallazgos.values())
    print("=" * 74)
    print("🧹 HIGIENE DOCUMENTAL — %d trackeados, %d documentos" % (len(files), len(docs)))
    print("=" * 74)
    if not total:
        print("\n✅ LIMPIO — ni un documento suelto. Atroz de regio. 💅\n")
        return 0
    for cat in sorted(hallazgos):
        items = hallazgos[cat]
        print("\n%s — %d" % (cat, len(items)))
        for ruta, motivo in (items if detalle else items[:12]):
            print("   • %-56s %s" % (ruta[:56], motivo))
        if not detalle and len(items) > 12:
            print("   … y %d mas (--detalle)" % (len(items) - 12))
    print("\n" + "-" * 74)
    print("TOTAL: %d hallazgos · regla: .agent/rules/12-higiene-documental.md" % total)
    print("-" * 74 + "\n")
    return 1 if estricto else 0


if __name__ == "__main__":
    sys.exit(main())
