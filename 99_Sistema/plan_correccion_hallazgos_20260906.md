# Plan de corrección — hallazgos de las auditorías del 06/09/2026

> **Para quien ejecute:** este plan se implementa **tarea por tarea**, cada una con su ciclo de test y su commit. Los pasos van en checkbox (`- [ ]`). Skill de ejecución recomendada: `subagent-driven-development` (un subagente fresco por tarea, revisión entre tareas).

**Goal:** cerrar los defectos *mecánicos* que encontraron las tres auditorías del 06/09, dejando cada regla con un ejecutor que la mida — sin tocar nada que requiera decisión editorial de la Ama.

**Arquitectura:** todo vive en `99_Sistema/scripts/visual/`. Tres capas: (1) el **sync** que lee el índice de git y escribe trackers, (2) los **linters** que auditan galerías, (3) el **motor** (`prompt_builder` + `outfit.py generar`) que emite prompts. Cada tarea añade su chequeo a la batería existente `test_engine.py` — que **no es pytest**: es un script plano con `check(nombre, cond, detalle)` que termina en `sys.exit(1 if fallo else 0)` y se corre con `python 99_Sistema/scripts/visual/test_engine.py` o `outfit.py test`. Hoy va en **43 ok / 0 fallas**; el plan la deja en 55.

**Tech stack:** Python 3.12 · Pillow · numpy · git como fuente de verdad de archivos (`git ls-files`, nunca el disco — este clon es sparse y tiene 0 PNG locales).

**Specs de origen:**
- `99_Sistema/auditoria_visual_3munecas_20260906.md` (174 PNG, 6 auditores externos)
- `99_Sistema/auditoria_reglas_antirepeticion_poses_20260906.md` (antirepetición, poses, arquetipos, + §6 revisión externa)

> 📍 **Dónde se guarda este plan y por qué.** La skill `writing-plans` pide `docs/superpowers/plans/`. Este repo tiene su propia regla de higiene documental (`.agent/rules/12`) que prohíbe crear árboles nuevos en la raíz y manda seguir la convención existente: los documentos de trabajo de sistema viven en `99_Sistema/` con nombre fechado. **Fecha de muerte declarada:** cuando las 9 tareas estén hechas, este archivo se mueve a evidencia o se borra; no se queda de adorno.

## Global Constraints

- **Encoding:** UTF-8 **sin BOM** en todo archivo tocado. Emojis y acentos se preservan.
- **Consola Windows:** todo script nuevo o modificado que imprima debe forzar `sys.stdout.reconfigure(encoding="utf-8")` — la consola es cp1252.
- **Fuente de verdad de archivos:** `git ls-files`, **jamás** `os.listdir` sobre `05_Imagenes/`. Este clon es sparse.
- **Commits:** prefijo `Ele:` y trailer `Co-Authored-By: Ele de Anaïs <Ele.de.Anais@proton.me>`. Staging por **rutas explícitas**, nunca `git add -A`.
- **Ningún cambio de prompt que altere el canon visual** entra en este plan. Lo que toque el vestuario o la pose *como contenido* sube a decisión de la Ama (ver §Fuera de alcance).
- **Regla de oro del repo:** un chequeo que corre *después* de escribir la galería documenta el defecto, no lo evita. Todo chequeo nuevo se cablea en `outfit.py generar` o en el sync, no solo en un linter suelto.

---

## Estructura de archivos

| Archivo | Responsabilidad | Tareas |
|---|---|---|
| `visual/sync_imagenes_subidas.py` | normaliza nombres y escribe el tracker `N/7` de Ele | 1, 2 |
| `visual/sync_tracker_galeria_personaje.py` | ídem para Miss Doll y Anaïs | 1, 2 |
| `visual/integridad_imagenes.py` **(nuevo)** | md5 duplicado + orientación por slot. Función pura, sin I/O de tracker — la consumen los dos sync y el test | 1, 2 |
| `visual/lint_galeria.py` | contrato de galería (regla 11) | 3 |
| `visual/rotacion_poses.py` **(nuevo)** | mide repetición de sub-pose *entre* looks; el chequeo que hoy no existe | 4, 9 |
| `visual/garment_canon.py` | validadores de prenda (medias, corsé, tokens) | 5, 6 |
| `visual/prompt_builder.py` | emisión de prompts; `pose()` ya acepta `indice=` explícito | 6, 9 |
| `visual/outfit.py` | la puerta: `generar` bloquea antes de escribir | 4, 5, 6, 9 |
| `visual/test_engine.py` | batería (43 → 55 checks) | todas |
| `visual/retrofit_arquetipo.py` **(nuevo, efímero)** | rellena el campo `**Arquetipo:**` desde el título. Se borra tras correr | 7 |

---

## FASE 1 · Integridad del pipeline

### Task 1: Detectar poses duplicadas por md5

**Por qué:** `ele L819` y `anais L83` tienen un archivo **byte a byte duplicado** pasando por dos poses distintas; `ele L823` tiene dos frames que difieren en **0,1% de los píxeles**. Los tres figuran **7/7 en el tracker con 6 poses reales**. El tracker miente hacia arriba y nada lo mira.

**Files:**
- Create: `99_Sistema/scripts/visual/integridad_imagenes.py`
- Modify: `99_Sistema/scripts/visual/test_engine.py` (append)
- Test: `99_Sistema/scripts/visual/test_engine.py`

**Interfaces:**
- Produces: `duplicados_por_look(rutas_y_bytes: dict[str, bytes]) -> list[tuple[str, str]]` — recibe `{nombre_archivo: contenido}`, devuelve los pares idénticos ordenados. Función **pura**: no abre archivos, no llama a git. Los tests la alimentan con bytes de mentira y los sync le pasan `git cat-file`.

- [ ] **Step 1: Escribir el test que falla**

Añadir al final de `test_engine.py`:

```python
# F1 poses duplicadas por md5 dentro de un mismo look
from integridad_imagenes import duplicados_por_look                # noqa: E402
_pack = {"ele_819_seated.png": b"AAA", "ele_819_side_profile.png": b"AAA",
         "ele_819_standing.png": b"BBB"}
check("integridad: caza el par byte-identico",
      duplicados_por_look(_pack) == [("ele_819_seated.png", "ele_819_side_profile.png")])
check("integridad: no inventa duplicados",
      duplicados_por_look({"a.png": b"1", "b.png": b"2"}) == [])
check("integridad: tres iguales dan los tres pares",
      len(duplicados_por_look({"a.png": b"X", "b.png": b"X", "c.png": b"X"})) == 3)
```

- [ ] **Step 2: Correr y verificar que falla**

Run: `python 99_Sistema/scripts/visual/test_engine.py`
Expected: `ModuleNotFoundError: No module named 'integridad_imagenes'`

- [ ] **Step 3: Implementación mínima**

Crear `99_Sistema/scripts/visual/integridad_imagenes.py`:

```python
# -*- coding: utf-8 -*-
"""Integridad de las imagenes de un look. Funciones PURAS: no abren archivos
ni llaman a git — quien las usa le pasa los bytes. Asi la bateria las prueba
sin depender de que el clon tenga los PNG en disco (este no los tiene).

Nace del hallazgo del 06/09/2026: ele L819 y anais L83 tenian un archivo
byte-a-byte duplicado haciendose pasar por dos poses, y los dos looks figuraban
7/7 en el tracker con 6 poses reales.
"""
import hashlib
import itertools


def duplicados_por_look(archivos):
    """[(nombre_a, nombre_b), ...] de los pares con contenido IDENTICO.

    archivos: {nombre: bytes}. Orden estable (alfabetico) para que el reporte
    sea reproducible y los tests no dependan del orden del dict.
    """
    por_hash = {}
    for nombre in sorted(archivos):
        h = hashlib.md5(archivos[nombre]).hexdigest()
        por_hash.setdefault(h, []).append(nombre)
    pares = []
    for nombres in por_hash.values():
        if len(nombres) > 1:
            pares.extend(itertools.combinations(nombres, 2))
    return sorted(pares)
```

- [ ] **Step 4: Correr y verificar que pasa**

Run: `python 99_Sistema/scripts/visual/test_engine.py`
Expected: `RESULTADO: 46 ok · 0 fallas`

- [ ] **Step 5: Cablearlo en los dos sync**

En `sync_imagenes_subidas.py`, dentro del paso 2 (antes de escribir el tracker), por cada look:

```python
from integridad_imagenes import duplicados_por_look

def _bytes_de(folder, nombres):
    out = {}
    for f in sorted(nombres):
        r = subprocess.run(["git", "cat-file", "-p", f"HEAD:05_Imagenes/ele/{folder}/{f}"],
                           cwd=REPO, capture_output=True)
        if r.returncode == 0:
            out[f] = r.stdout
    return out

# ...dentro del bucle por look, antes de escribir el tracker:
for folder in folders_de_look(n):
    dups = duplicados_por_look(_bytes_de(folder, imgs_de_look(folder)))
    for a, b in dups:
        print(f"   🔴 L{n}: {a} y {b} son el MISMO archivo — la pose no existe")
        duplicados_totales += 1
```

Y al cierre del script, después del resumen:

```python
if duplicados_totales:
    print(f"\n🔴 {duplicados_totales} pose(s) duplicada(s): el tracker esta contando de mas.")
```

Replicar el mismo bloque en `sync_tracker_galeria_personaje.py`, cambiando el prefijo de ruta por `05_Imagenes/{slug}`.

- [ ] **Step 6: Correr el sync sobre el repo real y anotar el resultado**

Run: `python 99_Sistema/scripts/visual/sync_imagenes_subidas.py`
Expected: reporta `🔴 L819` (y el resto, si aparece más). **No arregla el dato** — solo lo declara; regenerar la pose es de la app de la Ama.

- [ ] **Step 7: Commit**

```bash
git add 99_Sistema/scripts/visual/integridad_imagenes.py \
        99_Sistema/scripts/visual/test_engine.py \
        99_Sistema/scripts/visual/sync_imagenes_subidas.py \
        99_Sistema/scripts/visual/sync_tracker_galeria_personaje.py
git commit -m "Ele: el sync caza poses duplicadas por md5 — el tracker dejaba de mentir hacia arriba"
```

---

### Task 2: Chequeo de orientación por slot

**Por qué:** cuatro odalisques de Miss Doll (L75, L79, L83, L85) salieron **verticales** cuando el slot exige apaisada 16:9. Es 4 de 10 looks de la muestra y ningún control lo mira.

**Files:**
- Modify: `99_Sistema/scripts/visual/integridad_imagenes.py`
- Modify: `99_Sistema/scripts/visual/test_engine.py` (append)

**Interfaces:**
- Consumes: nada de la Task 1 (módulo compartido, funciones independientes).
- Produces: `orientacion_correcta(nombre_pose: str, ancho: int, alto: int) -> bool` — `True` si la orientación calza con el slot. Regla: `odalisque` ⇒ apaisada (`ancho > alto`); cualquier otro slot ⇒ vertical.

- [ ] **Step 1: Escribir el test que falla**

```python
# F2 orientacion por slot
from integridad_imagenes import orientacion_correcta                # noqa: E402
check("orientacion: odalisque apaisada es correcta",
      orientacion_correcta("miss_doll_083_odalisque.png", 1200, 669))
check("orientacion: odalisque vertical NO es correcta",
      not orientacion_correcta("miss_doll_083_odalisque.png", 669, 1200))
check("orientacion: standing vertical es correcta",
      orientacion_correcta("ele_827_standing.png", 669, 1200))
check("orientacion: standing apaisada NO es correcta",
      not orientacion_correcta("ele_827_standing.png", 1200, 669))
```

- [ ] **Step 2: Correr y verificar que falla**

Run: `python 99_Sistema/scripts/visual/test_engine.py`
Expected: `ImportError: cannot import name 'orientacion_correcta'`

- [ ] **Step 3: Implementación mínima**

Añadir a `integridad_imagenes.py`:

```python
def orientacion_correcta(nombre_pose, ancho, alto):
    """El slot Odalisque es el unico apaisado (16:9); los otros seis van
    verticales (9:16). Hallado el 06/09/2026: 4 odalisques de Miss Doll
    (L75, L79, L83, L85) salieron verticales y nadie lo miraba.

    Se decide por el NOMBRE del archivo, no por el orden del slot: los tres
    personajes nombran distinto su slot 5 (ditzy / glacial_command /
    sovereign_gaze) pero el septimo se llama `odalisque` en los tres.
    """
    apaisada = ancho > alto
    return apaisada if "odalisque" in nombre_pose.lower() else not apaisada
```

- [ ] **Step 4: Correr y verificar que pasa**

Run: `python 99_Sistema/scripts/visual/test_engine.py`
Expected: `RESULTADO: 50 ok · 0 fallas`

- [ ] **Step 5: Cablearlo en los dos sync**

En el mismo bucle por look de la Task 1, y **leyendo el tamaño sin escribir el PNG a disco**:

```python
import io as _io
from PIL import Image
from integridad_imagenes import orientacion_correcta

def _tam(blob):
    return Image.open(_io.BytesIO(blob)).size

for nombre, blob in _bytes_de(folder, imgs_de_look(n)).items():
    w, h = _tam(blob)
    if not orientacion_correcta(nombre, w, h):
        print(f"   🟠 L{n}: {nombre} sale {w}x{h} — orientacion equivocada para su slot")
```

- [ ] **Step 6: Correr sobre el repo real**

Run: `python 99_Sistema/scripts/visual/sync_tracker_galeria_personaje.py miss_doll`
Expected: reporta 🟠 en L75, L79, L83 y L85.

- [ ] **Step 7: Commit**

```bash
git add 99_Sistema/scripts/visual/integridad_imagenes.py \
        99_Sistema/scripts/visual/test_engine.py \
        99_Sistema/scripts/visual/sync_imagenes_subidas.py \
        99_Sistema/scripts/visual/sync_tracker_galeria_personaje.py
git commit -m "Ele: chequeo de orientacion por slot — 4 odalisques de Miss Doll salieron verticales"
```

---

### Task 3: Encoding roto en las galerías

**Por qué:** **11 looks de Ele (L690-L700)** tienen mojibake (`Â·`, `â€"`, `ðŸ§›`, `Ã©`) y `lint_higiene_repo.py` da el repo **LIMPIO**. No es un fallo del linter: su chequeo H6 **excluye las galerías a propósito** (pertenecen a `lint_galeria.py`) y `lint_galeria.py` **no chequea encoding**. La galería más grande del repo no tiene a nadie mirándole eso.

**Files:**
- Modify: `99_Sistema/scripts/visual/lint_galeria.py`
- Modify: `00_Ele/galeria_outfits.md` (reparación de datos, looks L690-L700)
- Modify: `99_Sistema/scripts/visual/test_engine.py` (append)

**Interfaces:**
- Produces: `secuencias_mojibake(texto: str) -> list[str]` en `lint_galeria.py` — devuelve las secuencias rotas encontradas, vacía si está limpio.

- [ ] **Step 1: Escribir el test que falla**

```python
# F3 mojibake en galeria
from lint_galeria import secuencias_mojibake                        # noqa: E402
check("mojibake: caza el punto medio roto",
      secuencias_mojibake("batch L691 Â· Gym Â· dusty rose") == ["Â·", "Â·"])
check("mojibake: caza la e acentuada rota",
      "Ã©" in secuencias_mojibake("Lencerï¿½a Ã©rotica"))
check("mojibake: texto sano da lista vacia",
      secuencias_mojibake("Look 827 · Lencería · 🫦 atroz de regio") == [])
```

- [ ] **Step 2: Correr y verificar que falla**

Run: `python 99_Sistema/scripts/visual/test_engine.py`
Expected: `ImportError: cannot import name 'secuencias_mojibake'`

- [ ] **Step 3: Implementación mínima**

Añadir a `lint_galeria.py`, junto a `es_ascii_limpio`:

```python
# UTF-8 leido como cp1252/latin-1: las secuencias que deja son inconfundibles.
# No se usa una heuristica general de "caracter raro" porque las galerias llevan
# emojis legitimos (🫦 💅 👠) y acentos correctos — eso seria un linter que grita
# por todo, y un linter que grita por todo enseña a ignorarlo.
MOJIBAKE = re.compile(r"Â·|Â«|Â»|â€”|â€“|â€œ|â€\x9d|â€™|ðŸ|Ã¡|Ã©|Ã­|Ã³|Ãº|Ã±|Ã\x81|ï¿½")


def secuencias_mojibake(texto):
    """Secuencias de encoding roto. Vacia = limpio.

    Existe porque el 06/09/2026 se midieron 11 looks de Ele (L690-L700) con el
    encoding roto mientras `lint_higiene_repo.py` daba LIMPIO: su chequeo H6
    excluye las galerias a proposito (son de este linter) y este linter no
    miraba encoding. El hueco no era de nadie.
    """
    return MOJIBAKE.findall(texto)
```

Y en `main()`, dentro del bucle por look, sumando a `fallas`:

```python
malas = secuencias_mojibake(bloque)
if malas:
    fallas.setdefault(n, []).append(
        f"encoding roto: {len(malas)} secuencia(s) — {sorted(set(malas))[:4]}")
```

- [ ] **Step 4: Correr y verificar que pasa el test, y que el linter encuentra los 11 looks**

Run: `python 99_Sistema/scripts/visual/test_engine.py`
Expected: `RESULTADO: 53 ok · 0 fallas`

Run: `python 99_Sistema/scripts/visual/lint_galeria.py --solo-desde 690`
Expected: 11 looks con hallazgo de encoding (L690-L700).

- [ ] **Step 5: Reparar el dato**

```bash
python - <<'PY'
import io
p = "00_Ele/galeria_outfits.md"
s = io.open(p, encoding="utf-8").read()
# Se repara re-decodificando SOLO las secuencias rotas: el resto del archivo
# (628 looks, ~40MB de prompts) no se toca.
for malo, bueno in [("Â·", "·"), ("â€”", "—"), ("â€“", "–"), ("â€œ", "“"),
                    ("â€\x9d", "”"), ("â€™", "’"), ("Ã¡", "á"), ("Ã©", "é"),
                    ("Ã­", "í"), ("Ã³", "ó"), ("Ãº", "ú"), ("Ã±", "ñ")]:
    s = s.replace(malo, bueno)
# Los emojis rotos (ðŸ...) se re-decodifican por bloque, no por tabla:
s = s.encode("utf-8").decode("utf-8")
io.open(p, "w", encoding="utf-8", newline="\n").write(s)
print("reparado")
PY
```

> ⚠️ Los emojis rotos (`ðŸ§›â€â™€ï¸`) **no se resuelven con la tabla** — son secuencias de 3-4 bytes. Repararlos uno a uno mirando el look original en `git log -p`. Si un emoji no se puede recuperar con certeza, **se borra**, no se adivina: un emoji equivocado en la galería es peor que ninguno.

- [ ] **Step 6: Verificar que el linter queda en cero**

Run: `python 99_Sistema/scripts/visual/lint_galeria.py`
Expected: 0 hallazgos de encoding.

Run: `python 99_Sistema/scripts/mantenimiento/lint_higiene_repo.py`
Expected: `✅ LIMPIO`

- [ ] **Step 7: Commit**

```bash
git add 99_Sistema/scripts/visual/lint_galeria.py \
        99_Sistema/scripts/visual/test_engine.py \
        00_Ele/galeria_outfits.md
git commit -m "Ele: lint_galeria chequea encoding + reparados 11 looks de Ele con mojibake (L690-L700)"
```

---

## FASE 2 · Reglas escritas que no tenían ejecutor

### Task 4: El auditor de rotación de poses ENTRE looks

**Por qué:** hoy **ningún auditor mira la rotación de poses entre looks**. El chequeo 7 de `lint_prompts_personaje.py` detecta poses duplicadas *dentro* de un look, jamás *entre* looks. Por eso el defecto vivió intacto: no es que un chequeo fallara, es que no existe. Consecuencia medida: **Anaïs L83/L84/L85 repiten la postura de L76/L77/L78 en los 7 slots**, con 47 palabras idénticas carácter por carácter en Standing.

**Files:**
- Create: `99_Sistema/scripts/visual/rotacion_poses.py`
- Modify: `99_Sistema/scripts/visual/outfit.py` (registrar subcomando + llamar desde `generar`)
- Modify: `99_Sistema/scripts/visual/test_engine.py` (append)

**Interfaces:**
- Produces:
  - `indice_de(slot: str, look: int, offsets: dict, n: int) -> int` — reproduce la fórmula viva de `prompt_builder.py:319-320`: `(look - 1 + offset) % n`.
  - `colisiones(slug: str, looks: list[int], repertorio: dict) -> list[dict]` — por cada par de looks, `{"a": int, "b": int, "slots": [str], "n": int}` con los slots que comparten índice. Solo devuelve pares con `n >= 1`.

- [ ] **Step 1: Escribir el test que falla**

```python
# F4 rotacion de poses entre looks
from rotacion_poses import indice_de, colisiones                    # noqa: E402
check("rotacion: la formula es (look-1+off) %% n",
      indice_de("standing", 817, {"standing": 5}, 9) == (817 - 1 + 5) % 9)
_rep = {"offsets": {"standing": 0, "pov": 3},
        "slots": {"standing": ["a"] * 7, "pov": ["b"] * 7}}
_col = colisiones("anais", [76, 83], _rep)
check("rotacion: caza el par a distancia n (7) en los 2 slots",
      len(_col) == 1 and _col[0]["a"] == 76 and _col[0]["b"] == 83
      and sorted(_col[0]["slots"]) == ["pov", "standing"])
check("rotacion: looks consecutivos NO colisionan",
      colisiones("anais", [76, 77], _rep) == [])
_rep9 = {"offsets": {"odalisque": 0}, "slots": {"odalisque": ["x"] * 9}}
check("rotacion: con 9 variantes el par a distancia 7 no colisiona",
      colisiones("miss_doll", [75, 82], _rep9) == [])
```

- [ ] **Step 2: Correr y verificar que falla**

Run: `python 99_Sistema/scripts/visual/test_engine.py`
Expected: `ModuleNotFoundError: No module named 'rotacion_poses'`

- [ ] **Step 3: Implementación mínima**

Crear `99_Sistema/scripts/visual/rotacion_poses.py`:

```python
# -*- coding: utf-8 -*-
"""Rotacion de sub-poses ENTRE looks — el chequeo que no existia.

Medido el 06/09/2026: el chequeo 7 de lint_prompts_personaje.py detecta poses
duplicadas DENTRO de un look y nunca ENTRE looks. Con la formula
`(look - 1 + offset) %% len(variaciones)`, cada slot se repite exactamente cada
`n` looks; como los 7 repertorios de Anais miden 7, sus L83/L84/L85 repiten la
postura completa de L76/L77/L78 — verbatim, 47 palabras identicas en Standing.

La formula se replica de la RUTA VIVA (prompt_builder.py:319-320). Ojo:
pose_rotation_v5.rotate_poses:761 usa `(look_number + off)` SIN el -1 y con
offsets hardcodeados, y no tiene llamador vivo — no es la referencia.
"""
import itertools


def indice_de(slot, look, offsets, n):
    """Indice de sub-pose que le toca a `slot` en `look`. Espeja
    prompt_builder.PromptBuilder.pose(). No modela el bucle de salto por props
    sin resolver: ese corre el indice hacia adelante y solo puede REDUCIR
    colisiones, asi que este auditor es conservador (nunca reporta de menos)."""
    return (look - 1 + offsets.get(slot, 0)) % n


def colisiones(slug, looks, repertorio):
    """Pares de looks que comparten sub-pose, con el detalle de en que slots."""
    offsets = repertorio.get("offsets", {})
    slots = repertorio.get("slots", {})
    out = []
    for a, b in itertools.combinations(sorted(looks), 2):
        comunes = [s for s, var in slots.items()
                   if indice_de(s, a, offsets, len(var)) == indice_de(s, b, offsets, len(var))]
        if comunes:
            out.append({"a": a, "b": b, "slots": sorted(comunes), "n": len(comunes)})
    return sorted(out, key=lambda d: (-d["n"], d["a"], d["b"]))
```

- [ ] **Step 4: Correr y verificar que pasa**

Run: `python 99_Sistema/scripts/visual/test_engine.py`
Expected: `RESULTADO: 57 ok · 0 fallas`

- [ ] **Step 5: Añadir el subcomando `outfit.py poses`**

En `outfit.py`, junto a los otros subcomandos:

```python
def cmd_poses(args):
    """Rotacion de sub-poses entre looks, por personaje."""
    import json
    from rotacion_poses import colisiones
    rep = json.load(open(os.path.join(V, "repertorios_pose.json"), encoding="utf-8"))
    sucio = 0
    for slug in ("ele", "miss_doll", "anais"):
        ultimos = ultimos_looks_de_galeria(slug, 12)          # ya existe, la usa `generar`
        p = rep["personajes"][slug]
        tam = {s: len(v) for s, v in p["slots"].items()}
        print(f"\n=== {slug} · ultimos {len(ultimos)} looks · repertorios {tam} ===")
        for c in colisiones(slug, ultimos, p):
            total = len(p["slots"])
            flag = "🔴" if c["n"] >= total - 1 else ("🟠" if c["n"] >= total - 3 else "  ")
            if c["n"] >= total - 3:
                print(f"  {flag} L{c['a']} ↔ L{c['b']}: {c['n']}/{total} slots con la MISMA sub-pose "
                      f"({', '.join(c['slots'])})")
            if c["n"] >= total - 1:
                sucio += 1
    print(f"\n{'🔴 ' + str(sucio) + ' par(es) con la postura practicamente completa repetida' if sucio else '✅ ningun par repite la postura completa'}")
    return 1 if sucio else 0
```

Registrarlo en el dispatcher junto a `cruce`, `lint`, `adn`, `modularidad`.

- [ ] **Step 6: Correr sobre el repo real y anotar la línea base**

Run: `python 99_Sistema/scripts/visual/outfit.py poses`
Expected: 🔴 en Anaïs (L76↔L83, L77↔L84, L78↔L85 con 7/7) y 🟠 en Miss Doll (4 pares 6/7). Ele limpia (máx 2/7).

- [ ] **Step 7: Cablearlo en `generar` como AVISO, no como bloqueo**

En `outfit.py generar`, junto a los otros chequeos cruzados. **Aviso y no bloqueo a propósito:** con los repertorios actuales el defecto es **inevitable por aritmética** — bloquear haría imposible emitir cualquier batch de Anaïs. Sube a bloqueo en la Task 9, cuando exista de dónde rotar.

```python
_col = [c for c in colisiones(slug, ultimos + [n], rep["personajes"][slug])
        if c["n"] >= len(rep["personajes"][slug]["slots"]) - 1]
for c in _col:
    print(f"  🟠 L{c['a']} ↔ L{c['b']}: {c['n']}/7 slots con la misma sub-pose — "
          f"repertorio de tamaño {min(len(v) for v in rep['personajes'][slug]['slots'].values())} "
          f"(ver plan de correccion, Task 9)")
```

- [ ] **Step 8: Commit**

```bash
git add 99_Sistema/scripts/visual/rotacion_poses.py \
        99_Sistema/scripts/visual/outfit.py \
        99_Sistema/scripts/visual/test_engine.py
git commit -m "Ele: outfit.py poses — el chequeo de rotacion de sub-poses entre looks, que no existia"
```

---

### Task 5: Miss Doll — máximo 2 looks seguidos con medias

**Por qué:** regla escrita en `02_Personajes/_perfiles_visuales/miss_doll.md:258` y **violada en el último batch**: medias en **L83, L84 y L85, tres seguidas**. La encontró la revisión externa, no yo.

**Files:**
- Modify: `99_Sistema/scripts/visual/garment_canon.py`
- Modify: `99_Sistema/scripts/visual/outfit.py` (llamar desde `generar`)
- Modify: `99_Sistema/scripts/visual/test_engine.py` (append)

**Interfaces:**
- Produces: `audit_racha_medias(bloques_b: list[str], maximo: int = 2) -> str | None` — recibe los BLOQUE B en orden de look; devuelve el mensaje de violación o `None`.

- [ ] **Step 1: Escribir el test que falla**

```python
# F5 racha de medias
from garment_canon import audit_racha_medias                        # noqa: E402
_CON = "sheer black stockings held by a suspender belt"
_SIN = "bare legs, no stockings"
check("medias: dos seguidas pasan",
      audit_racha_medias([_SIN, _CON, _CON, _SIN]) is None)
check("medias: tres seguidas fallan",
      audit_racha_medias([_SIN, _CON, _CON, _CON]) is not None)
check("medias: 'no stockings' no cuenta como medias",
      audit_racha_medias([_SIN, _SIN, _SIN, _SIN]) is None)
check("medias: el mensaje nombra la posicion de la racha",
      "3" in (audit_racha_medias([_CON, _CON, _CON]) or ""))
```

- [ ] **Step 2: Correr y verificar que falla**

Run: `python 99_Sistema/scripts/visual/test_engine.py`
Expected: `ImportError: cannot import name 'audit_racha_medias'`

- [ ] **Step 3: Implementación mínima**

Añadir a `garment_canon.py`:

```python
# La ausencia se declara ANTES de buscar la prenda: sin esto, un BLOQUE B que
# dice literal "no stockings" contaba como que lleva medias. Es el mismo error
# que ya se cerro en clasificar_arquitectura() con `_regex_ausencias`.
_MEDIAS_NO = re.compile(r"\bno stockings\b|\bbare legs\b|\bno hosiery\b", re.I)
_MEDIAS_SI = re.compile(r"\bstockings?\b|\bhosiery\b|\btights\b|\bhold-ups?\b|\bnylons?\b", re.I)


def lleva_medias(bloque_b):
    b = bloque_b or ""
    if _MEDIAS_NO.search(b):
        return False
    return bool(_MEDIAS_SI.search(b))


def audit_racha_medias(bloques_b, maximo=2):
    """None si cumple; mensaje si hay mas de `maximo` looks seguidos con medias.

    Regla de miss_doll.md:258. Violada en L83-L85 (tres seguidas), hallada por
    revision externa el 06/09/2026 despues de que la auditoria propia no la mirara.
    """
    racha = 0
    for i, b in enumerate(bloques_b):
        racha = racha + 1 if lleva_medias(b) else 0
        if racha > maximo:
            return (f"{racha} looks seguidos con medias (posiciones {i - racha + 2}-{i + 1} "
                    f"de la ventana) — el maximo es {maximo}")
    return None
```

- [ ] **Step 4: Correr y verificar que pasa**

Run: `python 99_Sistema/scripts/visual/test_engine.py`
Expected: `RESULTADO: 61 ok · 0 fallas`

- [ ] **Step 5: Cablearlo en `generar` como BLOQUEO**

A diferencia de la Task 4, esta **sí bloquea**: es una regla cumplible, solo hay que cambiar una prenda.

```python
if slug == "miss_doll":            # dueño de la regla: su perfil §5.3
    msg = audit_racha_medias([bb_de(l) for l in ultimos] + [bloque_b])
    if msg:
        errores.append(f"L{n}: {msg} (miss_doll.md:258)")
```

> ⚠️ **`if slug == "miss_doll"` es exactamente lo que `outfit.py modularidad` prohíbe.** El máximo va leído del perfil, no cableado: añadir `rotacion_medias.maximo` a `anclas_universales.json → personajes.<slug>`, con `null` en quien no la tenga, y consultar eso. Verificar con `python 99_Sistema/scripts/visual/outfit.py modularidad` antes de commitear.

- [ ] **Step 6: Verificar que el motor rechaza el caso real y que modularidad sigue limpia**

Run: `python 99_Sistema/scripts/visual/outfit.py modularidad`
Expected: `LIMPIA` (0 nombres de personaje en lógica de motor)

Run: `python 99_Sistema/scripts/visual/outfit.py generar 99_Sistema/scripts/visual/batches/MD_L81_L85_deficit_club.json`
Expected: bloquea con `L85: 3 looks seguidos con medias`.

- [ ] **Step 7: Commit**

```bash
git add 99_Sistema/scripts/visual/garment_canon.py \
        99_Sistema/scripts/visual/anclas_universales.json \
        99_Sistema/scripts/visual/outfit.py \
        99_Sistema/scripts/visual/test_engine.py
git commit -m "Ele: tope de racha de medias — la regla de miss_doll.md:258 ya tiene ejecutor"
```

> 📌 **El dato roto (L83-L85) NO se arregla en esta tarea.** Los tres están materializados; rediseñar uno es decisión de la Ama. Va a `rotacion_medias.historicos_declarados` para que el linter no grite por lo que no se puede arreglar — esa es la política del repo y evita un linter que enseña a ignorarlo.

---

### Task 6: Ancla de costura de media en un look sin medias

**Por qué:** `miss_doll L77` declara `bare legs, no stockings` en su BLOQUE B y sus prompts traen igual `the stockings have ONE single seam…`. Es **1 de 798** looks — aislado, no sistémico — pero es texto que se contradice a sí mismo y le roba atención al generador en cada pose. Y `miss_doll L78` sí lleva medias y le salió **la costura al frente**, que es justo lo que el ancla existe para evitar.

**Files:**
- Modify: `99_Sistema/scripts/visual/prompt_builder.py`
- Modify: `99_Sistema/scripts/visual/test_engine.py` (append)

**Interfaces:**
- Consumes: `garment_canon.lleva_medias` (Task 5).
- Produces: nada nuevo; cambia el comportamiento de la emisión — el ancla de costura **no se pega** si el BLOQUE B declara ausencia de medias.

- [ ] **Step 1: Escribir el test que falla**

```python
# F6 el ancla de costura no viaja en look sin medias
_pb = PromptBuilder("miss_doll")
_sin = _pb.build(bloque_b="a fuchsia vinyl mini dress; bare legs, no stockings; "
                          "closed pointed-toe platform stilettos",
                 slot="Standing", look_number=77, props=_PROPS_MIN)
check("costura: look sin medias NO lleva el ancla de costura",
      "single seam" not in _sin)
_con = _pb.build(bloque_b="a fuchsia vinyl mini dress; sheer black stockings with a fine "
                          "back seam; closed pointed-toe platform stilettos",
                 slot="Standing", look_number=77, props=_PROPS_MIN)
check("costura: look CON medias si lleva el ancla",
      "single seam" in _con)
```

> `_PROPS_MIN` ya existe en la batería (bloque D, cobertura de slots). Reutilizarlo, no crear otro.

- [ ] **Step 2: Correr y verificar que falla**

Run: `python 99_Sistema/scripts/visual/test_engine.py`
Expected: falla el primer check — el ancla se pega igual.

- [ ] **Step 3: Implementación mínima**

En `prompt_builder.py`, donde se decide pegar el ancla de costura, condicionar por el BLOQUE B:

```python
from garment_canon import lleva_medias

# ...en el armado del prompt:
if seam and lleva_medias(bloque_b):
    partes.append(STOCKING_SEAM_BACK if slot_n == "back_view" else STOCKING_SEAM_FRONT)
```

- [ ] **Step 4: Correr y verificar que pasa**

Run: `python 99_Sistema/scripts/visual/test_engine.py`
Expected: `RESULTADO: 63 ok · 0 fallas`

- [ ] **Step 5: Medir el alcance en la flota**

```bash
python - <<'PY'
import re, io
GAL = {"ele": "00_Ele/galeria_outfits.md",
       "miss_doll": "02_Personajes/01_Principales/miss_doll/GALERIA_OUTFITS_MISS_DOLL.md",
       "anais": "02_Personajes/01_Principales/anais/galeria_looks_anais.md"}
SEAM = "the stockings have ONE single seam"
for d, p in GAL.items():
    t = io.open(p, encoding="utf-8").read()
    n = 0
    for b in re.split(r"\n(?=## )", t):
        m = re.match(r"## .*?Look 0*(\d+)\s*[:·]", b)
        if not m:
            continue
        mb = (re.search(r"\*\*Outfit \(BLOQUE B\):\*\*\s*`(.+?)`", b, re.S)
              or re.search(r"\*\*BLOQUE B[^*]*:\*\*\s*\n```text\n(.+?)\n```", b, re.S))
        bb = (mb.group(1) if mb else "").lower()
        if ("bare legs" in bb or "no stockings" in bb) and SEAM in b:
            print(f"{d} L{m.group(1)}"); n += 1
    print(f"{d}: {n}")
PY
```
Expected: solo `miss_doll L77`. **No se reemite** — está materializado; queda declarado en el informe.

- [ ] **Step 6: Commit**

```bash
git add 99_Sistema/scripts/visual/prompt_builder.py \
        99_Sistema/scripts/visual/test_engine.py
git commit -m "Ele: el ancla de costura de media ya no viaja en looks sin medias (miss_doll L77)"
```

---

## FASE 3 · Reparación de datos

### Task 7: Retrofit del campo `**Arquetipo:**`

**Por qué:** el campo existe **solo desde los batches del 05/09**. Ele tiene **105 de 628 looks sin él**; Miss Doll **solo 21 de 85 lo traen (24,7%)**. Mientras tanto la regla de déficit es ciega sobre el resto y los porcentajes se calculan sobre el 81-82% de la flota. El dato **está en el título** de casi todos.

**Files:**
- Create: `99_Sistema/scripts/visual/retrofit_arquetipo.py` (**efímero — se borra tras correr**)
- Modify: las tres galerías

- [ ] **Step 1: Escribir el script en modo `--dry-run` primero**

El script extrae el arquetipo del título (segmentos separados por `·`, descartando `batch…`, `V7poses` y el número), lo mapea contra la tabla §6 del perfil, y **solo reporta**. Nada se escribe en esta pasada.

- [ ] **Step 2: Correr en dry-run y revisar la muestra a mano**

Run: `python 99_Sistema/scripts/visual/retrofit_arquetipo.py --dry-run`
Expected: lista de `L<n>: <arquetipo inferido>` con su conteo. **Revisar 10 al azar contra el texto del look**; si alguno no calza, el mapeo está mal y se corrige antes de escribir.

- [ ] **Step 3: Los que no se puedan inferir quedan SIN tocar**

15 looks de Miss Doll dicen literalmente `Mix`, del paraguas viejo. **No se adivinan.** Se listan aparte para que la Ama decida — un arquetipo inventado es peor que un hueco, porque contamina el porcentaje sin que se note.

- [ ] **Step 4: Correr en firme y verificar**

Run: `python 99_Sistema/scripts/visual/retrofit_arquetipo.py`
Run: `python 99_Sistema/scripts/visual/lint_galeria.py`
Expected: 0 hallazgos nuevos (el campo se inserta en la posición canónica del contrato, regla 11).

- [ ] **Step 5: Re-medir los porcentajes y comparar**

Volver a correr la medición del §5 de la auditoría. **Los porcentajes van a moverse** — hoy están calculados sobre el 81-82%. El número nuevo es el bueno; el viejo queda como línea base en el informe.

- [ ] **Step 6: Borrar el script y commitear**

```bash
git rm 99_Sistema/scripts/visual/retrofit_arquetipo.py
git add 00_Ele/galeria_outfits.md \
        02_Personajes/01_Principales/miss_doll/GALERIA_OUTFITS_MISS_DOLL.md \
        02_Personajes/01_Principales/anais/galeria_looks_anais.md
git commit -m "Ele: retrofit del campo Arquetipo — la regla de deficit deja de ser ciega sobre el 18% de la flota"
```

> 📌 **Se borra el script en el mismo commit** (regla 12: la salida efímera no se queda). Si hay que volver a correrlo, se recupera del historial.

---

### Task 8: Limpiar el delta genérico de POV

**Por qué:** el delta de POV de Anaïs **nombra prendas que el BLOQUE B nunca declaró**: `the strand of pearls` (L77), `the ring turned to the light` (L78 — de ahí el solitario que aparece en una sola pose y en ninguna otra), `the clasp of the fur at her throat` (L80, **donde no hay piel en el outfit**). Es texto genérico reutilizado que le mete al generador prendas fantasma.

**Files:**
- Modify: `99_Sistema/scripts/visual/repertorios_pose.json` (`personajes.anais.slots.pov`)
- Modify: `99_Sistema/scripts/visual/test_engine.py` (append)

- [ ] **Step 1: Escribir el test que falla**

```python
# F7 ninguna sub-pose nombra prendas concretas
import json as _json                                                # noqa: E402
_rep = _json.load(open(os.path.join(V, "repertorios_pose.json"), encoding="utf-8"))
_PRENDA = re.compile(r"\bpearls?\b|\bfur\b|\bring\b|\bglove\b|\bveil\b|\bcorset\b|"
                     r"\bstockings?\b|\bnecklace\b", re.I)
_sucias = []
for _slug, _p in _rep["personajes"].items():
    for _slot, _vars in _p["slots"].items():
        for _i, _v in enumerate(_vars):
            if _PRENDA.search(_v):
                _sucias.append(f"{_slug}/{_slot}[{_i}]")
check("repertorio: ninguna sub-pose nombra una prenda concreta",
      not _sucias, "; ".join(_sucias[:6]))
```

> **Por qué esta regla:** la sub-pose describe **el cuerpo y la cámara**; la prenda vive en el BLOQUE B, que es su dueño único. Una sub-pose que nombra una prenda la impone en todos los looks que le toquen esa variante, tengan esa prenda o no.

- [ ] **Step 2: Correr y verificar que falla**

Run: `python 99_Sistema/scripts/visual/test_engine.py`
Expected: falla listando las sub-poses sucias de Anaïs (y las que aparezcan en las otras dos).

- [ ] **Step 3: Reescribir cada sub-pose sucia**

Sustituir la referencia a la prenda por el **gesto**, que es lo que el slot necesita:

| Antes | Después |
|---|---|
| `her fingers at the strand of pearls at her throat` | `her fingertips resting at the hollow of her throat` |
| `the ring turned to the light` | `her hand turned so the light catches the back of it` |
| `the clasp of the fur at her throat` | `one hand closing the collar of whatever she wears at the throat` |

> ⚠️ **Esto toca texto de pose, o sea contenido de personaje.** Las tres reescrituras de arriba conservan el gesto exacto y solo sacan el sustantivo de prenda; si alguna cambia la *intención* del slot, sube a la Ama antes de escribirla.

- [ ] **Step 4: Correr y verificar que pasa**

Run: `python 99_Sistema/scripts/visual/test_engine.py`
Expected: `RESULTADO: 64 ok · 0 fallas`

- [ ] **Step 5: Commit**

```bash
git add 99_Sistema/scripts/visual/repertorios_pose.json \
        99_Sistema/scripts/visual/test_engine.py
git commit -m "Ele: las sub-poses dejan de nombrar prendas — el BLOQUE B es su unico dueño"
```

---

## FASE 4 · La rotación de poses (requiere decisión previa de la Ama)

### Task 9: Ventana real de sub-poses

> ✅ **CERRADA SIN CONSTRUIRLA — 09/09/2026. Ya no hay defecto que arreglar, y se mide.**
>
> El arreglo vino de lado: las 46 sub-poses nuevas del 08/09 entraron con **tamaños de
> repertorio desparejos a propósito** (Ele 7-10 · Miss Doll 7-12 · Anaïs 10-12), y eso
> mató el defecto grave sin necesidad de ventana. El clon del set completo exigía que
> todos los slots reciclaran al mismo ritmo; con tamaños distintos, el set entero solo
> se repite en el mínimo común múltiplo.
>
> **Medido sobre una ventana de 12 looks consecutivos, los 66 pares:**
>
> | Muñeca | Pares con ≥6/7 slots iguales | Peor coincidencia |
> |---|---|---|
> | Ele | **0** | 2 de 7 slots |
> | Miss Doll | **0** | 1 de 7 slots |
> | Anaïs | **0** | 3 de 7 slots |
>
> Anaïs venía de **5 pares en 7/7** — la postura completa repetida. Hoy su peor caso son
> 3 slots de 7 entre dos looks separados por hasta 12, que es el ruido normal de cualquier
> rotación finita.
>
> **Por qué NO se construye la ventana, entonces:** su precio es el que el propio plan
> identificó abajo — habría que **persistir el índice elegido en la galería como campo**,
> porque una selección no determinista deja el historial irreconstruible. Eso es cambiar el
> contrato de la galería y del parser de LV-App. Pagar un cambio de contrato para ganar
> 1-3 slots en 12 looks no se justifica.
>
> ⚠️ **Cuándo volver a abrirla:** si alguna vez los repertorios vuelven a quedar del mismo
> tamaño entre sí, el clon completo regresa. El guardián de eso es el chequeo de la Task 4,
> que sigue midiendo y avisando en cada `generar`. La regla que importa no es «≥15 variantes»
> sino **«que los tamaños no coincidan»**.

> 🔴 *(Diagnóstico original, 06/09 — se conserva porque su conclusión era correcta con los
> datos de ese día.)* **BLOQUEADA hasta que la Ama decida.** No por permiso — por
> **aritmética**: con 7 variantes por slot y una ventana de 10 looks, no hay de dónde rotar.
> Una ventana solo sirve si `len(variaciones) > ventana`.

**La conclusión corregida, que ninguno de los dos informes dijo así:** la **Opción A (agrandar los repertorios) no es un paliativo alternativo a C — es su prerrequisito.** Primero hay que tener variantes; después tiene sentido elegirlas con ventana.

- **A · Agrandar repertorios a ≥15 por slot.** ~50 variantes nuevas de redacción de pose, repartidas entre las tres. Es contenido de personaje: la Ama aprueba el registro antes de escribirlas. Prioridad por daño medido: **Anaïs los 7 slots** (ciclo de 7) → **Miss Doll 6 slots** (odalisque ya tiene 9) → **Ele `seated` y `slot5`** (los dos de 6).
- **C · Ventana en la selección.** `PromptBuilder.pose()` **ya acepta `indice=` explícito** (`prompt_builder.py:319`), así que el motor no necesita cirugía: basta un selector que reciba los índices usados en los últimos N looks y devuelva el primero libre. `outfit.py generar` ya carga los últimos 12 looks reales desde el 05/09. La pieza que falta es persistir el índice elegido por look — hoy se re-deriva de la fórmula, y en cuanto la selección deje de ser determinista hay que **escribirlo en la galería** como campo, o el historial se pierde.
- **B · Hacer los tamaños coprimos — DESCARTADA.** Refutada por revisión externa: la coprimalidad solo empuja el clon *completo* al mcm mientras cada slot sigue reciclándose cada `n` looks; y el ejemplo que propuse bajaba un repertorio a 5, **peor que hoy**.

**Hasta que esto se haga**, la Task 4 deja el defecto **medido y visible en cada `generar`**, que es lo mínimo honesto.

---

## Fuera de alcance — decisiones de la Ama, no tareas

| # | Qué | Por qué no está en el plan |
|---|---|---|
| 1 | **Eco de prenda en los planos cerrados** (Ditzy/POV/Sovereign/Glacial). Hoy la construcción del busto viaja solo en el BLOQUE B y se pierde sin cuerpo entero que la ancle: L820 POV con el busto fuera de la copa, L821 Ditzy con tirante en un bandeau *strapless* | Cambia el prompt de todos los looks futuros. Es canon visual |
| 2 | **El eco de calzado existe y no sostiene la arquitectura** — plataforma, puntera y altura de caña se pierden igual. Hay que medir si el eco llega a las poses donde falla antes de tocarlo | Diagnóstico previo, después decisión |
| 3 | **Poses dinámicas** (marcha, cruce de piernas, recline con tobillos cruzados). No se cumplen **ni con peso `:1.4`**. O se simplifican, o se acepta que este generador no las hace | Es su repertorio de poses |
| 4 | **`miss_doll L72 ↔ L78`** — 106 n-gramas verbatim, 88,9% de léxico, los dos materializados | Declararlos históricos o rehacer: es suya |
| 5 | **Miss Doll L83-L85 con medias** y los looks con clon de redacción de Ele | Rediseñar un look materializado es decisión editorial |

---

## Autorrevisión del plan

**Cobertura contra los informes.** Los hallazgos mecánicos de las tres auditorías tienen tarea: duplicados→T1 · orientación→T2 · encoding→T3 · rotación de poses sin auditor→T4 · racha de medias→T5 · costura sin medias→T6 · campo de arquetipo→T7 · delta de POV→T8 · rotación de poses arreglada→T9. Los hallazgos de **render** (P1-P7 de la auditoría visual) no tienen tarea **a propósito**: son del generador y su corrección es canon — están en Fuera de alcance 1-3.

**Consistencia de tipos.** `duplicados_por_look(dict[str,bytes]) -> list[tuple]` y `orientacion_correcta(str,int,int) -> bool` son puras y se consumen igual en los dos sync. `lleva_medias(str) -> bool` la definen la T5 y la consume la T6 con ese mismo nombre. `indice_de` y `colisiones` de la T4 son las que reusa la T9.

**Riesgo asumido y declarado.** La T4 replica la fórmula de `prompt_builder.py` en un módulo aparte: **son dos copias que pueden divergir.** Se acepta porque el auditor debe poder correr sin instanciar el builder, y se cubre con el check de la T4 Step 1 que fija la fórmula por escrito. Si `pose()` cambia, ese check falla — que es exactamente lo que tiene que pasar.
