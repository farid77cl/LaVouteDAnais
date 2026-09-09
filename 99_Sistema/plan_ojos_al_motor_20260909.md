# Plan — Ojos al motor, dueño único del BLOQUE A y prompt corto

> **Para quien lo ejecute:** los pasos van con checkbox (`- [ ]`). Cada tarea es un ciclo TDD
> completo y termina en commit. Regla 13: superpowers gobierna este código.
>
> 💀 **Fecha de muerte declarada (regla 12):** este documento muere cuando la Fase 3 cierre con
> su experimento medido. Su contenido vivo migra a `.agent/rules/06-generacion-imagenes.md` §9
> y a los docstrings de los módulos; el plan se borra, no se archiva.

**Objetivo:** que el outfit engine deje de ser ciego — que pueda decir por sí solo cuándo un
prompt se contradice, que ningún token de prenda viva en el ADN físico, y que el prompt vuelva
a un tamaño donde sus cláusulas no compitan entre ellas.

**Arquitectura:** tres módulos de funciones **puras** (mismo patrón que `integridad_imagenes.py`:
no abren archivos ni llaman a git, reciben el texto y devuelven hallazgos) más su cableado en la
puerta que ya existe. La puerta es `PromptBuilder.validar()`, que `outfit.py generar` ya consulta
y sobre la que ya bloquea (`outfit.py:321-324`). No se inventa una puerta nueva.

**Stack:** Python 3 sin dependencias nuevas. Runner propio en cada test (esta máquina no tiene
`pytest`; el patrón está en `test_sync_eol.py`).

**Origen:** auditoría visual del 09/09/2026 sobre 70 poses del batch L828-L832 / MD L86-L90 /
AN L86-L91, con seis auditores externos ciegos. Decisión de la Ama del mismo día, textual:
*«ojos al motor → guardia que saque los tokens de prenda del BLOQUE A → prompt nuevo, corto,
con experimento»*.

## Restricciones globales

- **Ningún clasificador lee el prompt ensamblado para decidir a qué familia pertenece un look.**
  Se clasifica sobre el BLOQUE B. El prompt contiene el texto de las anclas, y anclas como
  `BOTTOM_CUT_LOCK` nombran «bodysuit, teddy, leotard or swimsuit»: clasificar sobre el prompt
  es el clasificador leyéndose a sí mismo (modo de falla del 19/07/2026). **Excepción explícita
  de este plan:** la detección de *contradicciones* sí mira el prompt completo — porque su objeto
  de estudio es justamente el choque entre el ancla y el BLOQUE B. No clasifica, compara.
- **Funciones puras.** Sin `open()`, sin `subprocess`, sin red dentro de los módulos nuevos.
- **Encoding UTF-8 sin BOM**, `newline="\n"` al escribir código.
- **Cero nombres de personaje en la lógica** (`outfit.py modularidad` bloquea). Lo que difiere
  por muñeca se declara en su perfil o en `anclas_universales.json`.
- **Commits con prefijo `Ele:`** y trailer `Co-Authored-By: Ele de Anaïs <Ele.de.Anais@proton.me>`.
  Registro profesional, sin muletillas.
- **Verificación antes de cerrar cada tarea:** `outfit.py test` (124) · `modularidad` · `adn` ·
  `lint_higiene_repo.py` en 0. Y `git checkout -- 99_Sistema/logs/outfit_engine.jsonl` antes de
  commitear: la suite ensucia ese log con builds de fixtures (bug conocido, tarea 6).

---

## Estructura de archivos

| Archivo | Responsabilidad |
|---|---|
| `99_Sistema/scripts/visual/contradicciones.py` | **Nuevo.** Funciones puras: recibe un prompt, devuelve las cláusulas que se pelean entre sí. Sin I/O. |
| `99_Sistema/scripts/visual/test_contradicciones.py` | **Nuevo.** Su batería. Fixtures = fragmentos literales de la flota. |
| `99_Sistema/scripts/visual/prompt_builder.py` | Modificar: `validar()` consulta el módulo nuevo. Es la puerta que `generar` ya respeta. |
| `99_Sistema/scripts/visual/outfit.py` | Modificar: subcomandos `contradicciones` (barrido de flota) y `ojos` (paquete de auditoría). |
| `99_Sistema/scripts/visual/ojos.py` | **Nuevo.** Arma el paquete de auditoría imagen↔prompt: condensa los 7 prompts factorizando el bloque común y lista las imágenes reales. Puras salvo la lectura de galería, que va en el caller. |
| `99_Sistema/scripts/visual/test_ojos.py` | **Nuevo.** Su batería. |
| `99_Sistema/scripts/visual/test_bloque_a_dueno_unico.py` | **Nuevo.** Guardia: ningún BLOQUE A nombra prenda, calzado ni uñas. |
| `02_Personajes/_perfiles_visuales/anais.md` | Modificar: sacar de su cerca `ADN:BLOQUE_A` los tres tokens que no le pertenecen. |
| `.agent/rules/06-generacion-imagenes.md` | Modificar: documentar §10, el hallazgo de saturación. |

---

# FASE 1 — Ojos al motor

## Tarea 1: `contradicciones.py` — el prompt que se pelea consigo mismo

**Por qué esta primero.** De ~85 hallazgos de la auditoría del 09/09, **5 fueron del motor**, y
los cinco son el mismo animal: **dos cláusulas del mismo prompt pidiendo cosas incompatibles**.
Ninguno lo cazaba nadie, porque cada chequeo miraba una cláusula a la vez.

Los cinco casos reales, que son los fixtures:

| # | Choque | Evidencia |
|---|---|---|
| C1 | Calzado nombrado con **dos colores** | ADN de Anaïs dice `12cm black patent leather stiletto heels`; el BLOQUE B del L87 dice marfil. El `pov` del L88 salió **con zapato negro en un look rosa polvo**. |
| C2 | **Exposición contra cobertura** | L831: `g-string under the skirt` + `the wrap skirt stays unbroken` + `both seat cheeks fully bare:1.4`. La falda se abrió. (Arreglado el 09/09; la guardia impide la regresión.) |
| C3 | **Iris** nombrado dos veces distinto | `odalisque` de Miss Doll L89: `cold pale steel grey eyes` con el resto del prompt en cobalto. |
| C4 | **Estructura de copa** | L91 de Anaïs: su ADN pide `extreme waist training tightlacing corset` y su BLOQUE B pide copa blanda sin ballenas. Salió aro rígido en `seated`. |
| C5 | **Uñas** largas contra cortas | ADN de Anaïs: `long stiletto-shaped fingernails`; BLOQUE B del L87: `filed short of the fingertip`. |

**Files:**
- Create: `99_Sistema/scripts/visual/contradicciones.py`
- Test: `99_Sistema/scripts/visual/test_contradicciones.py`

**Interfaces:**
- Produce: `buscar(prompt: str) -> list[str]` — una línea por choque, en español, nombrando **las
  dos** cláusulas. Lista vacía = limpio. Es lo único que consume la tarea 2.

- [ ] **Paso 1: escribir la batería que falla**

Fixtures literales de la flota, uno por caso. Ejemplo del C1:

```python
C1_CALZADO_DOS_COLORES = (
    "…long stiletto-shaped fingernails, wearing 12cm black patent leather stiletto "
    "heels no platform iconic red sole, cinematic chiaroscuro… ivory silk-satin "
    "d'Orsay stiletto pumps with a pointed toe and a 12cm covered heel…"
)

def test_calzado_nombrado_con_dos_colores():
    hallazgos = contradicciones.buscar(C1_CALZADO_DOS_COLORES)
    assert any("calzado" in h for h in hallazgos)
    assert any("black" in h and "ivory" in h for h in hallazgos)
```

Y el negativo que impide un linter gritón:

```python
def test_un_prompt_coherente_no_da_hallazgos():
    limpio = ("a plum thong whose narrow front meets a mirror-silver O-ring at each hip; "
              "open-toe platform stiletto sandals in plum patent vinyl")
    assert contradicciones.buscar(limpio) == []
```

- [ ] **Paso 2: correr y verificar que falla**

Run: `python 99_Sistema/scripts/visual/test_contradicciones.py`
Esperado: `ModuleNotFoundError: No module named 'contradicciones'`, o `AttributeError: buscar`.

- [ ] **Paso 3: implementar lo mínimo**

Un detector por caso, cada uno una función `_c1_calzado(prompt) -> str | None`. `buscar()` los
recorre y junta lo que devuelvan. Sin clases, sin config.

- [ ] **Paso 4: correr y verificar que pasa**

Run: `python 99_Sistema/scripts/visual/test_contradicciones.py` → todo verde.

- [ ] **Paso 5: barrer la flota antes de cablear nada**

Correr `buscar()` sobre los prompts de las tres galerías **sin bloquear**, solo contando. Es la
calibración obligatoria: si devuelve cientos de hallazgos sobre looks aprobados, el detector está
mal, no la flota. **La meta es que los únicos hallazgos sean los cinco conocidos y sus parientes.**
Un linter que grita lo inarreglable enseña a ignorarlo.

- [ ] **Paso 6: commit**

```bash
git add 99_Sistema/scripts/visual/contradicciones.py 99_Sistema/scripts/visual/test_contradicciones.py
git commit   # Ele: detector de contradicciones dentro de un mismo prompt
```

---

## Tarea 2: cablear la puerta + barrido de flota

**Files:**
- Modify: `99_Sistema/scripts/visual/prompt_builder.py` — dentro de `validar()`
- Modify: `99_Sistema/scripts/visual/outfit.py` — registro `COMANDOS`
- Test: `99_Sistema/scripts/visual/test_contradicciones.py` (se le agregan casos)

**Interfaces:**
- Consume: `contradicciones.buscar(prompt)` de la tarea 1.
- Produce: `outfit.py contradicciones [slug]` — barrido sobre las galerías, exit 1 si hay.

- [ ] **Paso 1: test rojo de la puerta**

```python
def test_validar_bloquea_un_prompt_contradictorio():
    from prompt_builder import PromptBuilder
    fallas = PromptBuilder.validar(PROMPT_MINIMO_VALIDO + C3_IRIS_DOS_COLORES)
    assert any("iris" in f for f in fallas)
```

`PROMPT_MINIMO_VALIDO` debe traer `a single continuous photograph` y pasar de 400 chars, o el
test falla por las otras reglas de `validar()` y no por la nueva.

- [ ] **Paso 2: correr y verificar que falla**

Esperado: la lista de fallas no menciona el iris — `validar()` todavía no consulta el módulo.

- [ ] **Paso 3: implementar**

Al final de `validar()`, antes del `return`:

```python
        fallas.extend(contradicciones.buscar(prompt))
```

- [ ] **Paso 4: verde, y la suite completa**

Run: `python 99_Sistema/scripts/visual/test_contradicciones.py` y `outfit.py test`.
**Los 124 tienen que seguir verdes**: si alguno se cae, un fixture del motor contiene una
contradicción real y hay que mirarla, no silenciarla.

- [ ] **Paso 5: subcomando de barrido**

En `COMANDOS` de `outfit.py`:

```python
    "contradicciones": (cmd_contradicciones,
                        "cláusulas que se pelean dentro de un mismo prompt "
                        "(lo que ningún chequeo por cláusula puede ver)"),
```

- [ ] **Paso 6: verificar y commitear**

`outfit.py test` · `modularidad` · `adn` · `lint_higiene_repo.py` en 0.

---

## Tarea 3: `ojos.py` — el paquete de auditoría imagen↔prompt

**Por qué.** El 09/09 la auditoría necesitó seis agentes externos, y **la mitad del costo fue
preparar el material**: extraer los prompts, factorizar el bloque que las 7 poses comparten,
emparejar con las imágenes. Eso bajó cada look de ~70.000 a ~19.000 caracteres — **70% menos**.
Hecho a mano no se repite; hecho comando, sí.

**Files:**
- Create: `99_Sistema/scripts/visual/ojos.py`
- Test: `99_Sistema/scripts/visual/test_ojos.py`
- Modify: `99_Sistema/scripts/visual/outfit.py`

**Interfaces:**
- Produce: `condensar(prompts: dict[str, str]) -> dict` con claves `comun`, `sufijo`, `unico`
  (dict pose→texto propio). Y `outfit.py ojos <slug> <look>` que lo imprime junto a las rutas
  de imagen reales medidas con `git ls-files`.

- [ ] **Paso 1: test rojo**

```python
def test_condensar_factoriza_el_prefijo_compartido():
    prompts = {"standing": "ADN COMUN. de pie, mirando al lente",
               "seated":   "ADN COMUN. sentada, mirando abajo"}
    r = ojos.condensar(prompts)
    assert r["comun"] == "ADN COMUN. "
    assert r["unico"]["standing"] == "de pie, mirando al lente"

def test_condensar_con_una_sola_pose_no_inventa_bloque_comun():
    r = ojos.condensar({"standing": "texto único"})
    assert r["comun"] == ""
    assert r["unico"]["standing"] == "texto único"
```

El segundo importa: el L89 de Anaïs llegó **1/7** y un `condensar` ingenuo declararía el prompt
entero como «bloque común».

- [ ] **Paso 2: correr y verificar que falla**
- [ ] **Paso 3: implementar `condensar()`** — prefijo y sufijo común por comparación carácter a
  carácter, igual que la extracción manual del 09/09.
- [ ] **Paso 4: verde**
- [ ] **Paso 5: subcomando `ojos`** en `outfit.py`, que además imprime el tracker declarado
  contra las imágenes reales de `git ls-files` — el desajuste que hoy hubo en 8 looks.
- [ ] **Paso 6: verificar y commitear**

---

# FASE 2 — Guardia de dueño único sobre el BLOQUE A

## Tarea 4: ningún ADN físico nombra una prenda

**Decisión de la Ama (09/09/2026), textual:** *«guardia que saque los tokens de prenda del
BLOQUE A»*. Esto **enmienda su canon** y por eso va con su okey explícito, ya dado.

Medido: **solo Anaïs** los tiene. Ele y Miss Doll no llevan ni calzado ni uñas en su BLOQUE A —
esos campos viven en el BLOQUE B, que es su dueño. Los tres tokens de Anaïs, dentro de su cerca
`ADN:BLOQUE_A`, o sea inyectados **idénticos en las 7 poses de cada look**:

1. `wearing 12cm black patent leather stiletto heels no platform iconic red sole`
2. `long stiletto-shaped impeccably manicured glossy fingernails`
3. `slender mature elegant hourglass figure with extreme waist training tightlacing corset`

El (3) es el que derrota su propio veto de corsetería del 08/09: el L91, que **estrena** el veto,
lo lleva en 7 de 7 prompts.

⚠️ **El (3) no se borra entero.** `slender mature elegant hourglass figure` es su silueta y se
queda; lo que sale es `with extreme waist training tightlacing corset`, que es una **prenda**.
Confirmar la redacción final con la Ama antes de commitear: le talla la cintura en cada imagen.

**Files:**
- Create: `99_Sistema/scripts/visual/test_bloque_a_dueno_unico.py`
- Modify: `02_Personajes/_perfiles_visuales/anais.md`

- [ ] **Paso 1: test rojo, sobre los perfiles reales**

```python
RX_PRENDA_EN_ADN = re.compile(
    r"\b(?:wearing|shod in)\b|\b(?:stiletto heels?|pumps?|sandals?|boots?)\b"
    r"|\bfingernails\b|\bcorset\b|\btightlacing\b", re.I)

def test_ningun_bloque_a_nombra_prenda_calzado_ni_unas():
    fugas = []
    for slug in ("ele", "miss_doll", "anais"):
        adn = PromptBuilder(slug).bloque_a
        for m in RX_PRENDA_EN_ADN.finditer(adn):
            fugas.append(f"{slug}: «{m.group(0)}»")
    assert not fugas, "el BLOQUE A es ADN FÍSICO; prenda y calzado son del BLOQUE B:\n  " + "\n  ".join(fugas)
```

- [ ] **Paso 2: correr y verificar que falla** — esperado: 3 fugas, todas de `anais`.
- [ ] **Paso 3: sacar los tres tokens** de la cerca `ADN:BLOQUE_A` de `anais.md`, dejando la
  silueta. Anotar en su §5.3 y §5.5 que el calzado y las uñas se declaran en el BLOQUE B como en
  las otras dos muñecas.
- [ ] **Paso 4: verde + `outfit.py adn` LIMPIO** (el chequeo de dueño único del BLOQUE A no debe
  romperse: los batches que copian el ADN a mano tienen que seguir cuadrando).
- [ ] **Paso 5: medir el efecto** — reconstruir un prompt del L87 y del L91 y verificar que ya no
  hay dos colores de calzado ni corsé contra copa blanda. `contradicciones.buscar()` de la tarea 1
  debe devolver **lista vacía** donde antes devolvía C1, C4 y C5.
- [ ] **Paso 6: commit**

---

# FASE 3 — Prompt corto, con experimento

## Tarea 5: medir la saturación antes de rediseñar

**La evidencia que la motiva.** El prompt creció **58%** en doscientos looks y hoy lleva **5
cláusulas con peso `:1.4` compitiendo**:

| rango | chars/prompt |
|---|---|
| L600-699 | 4.213 |
| L700-799 | 4.519 |
| L800+ | 5.665 |
| batch auditado | 5.995 – 6.655 |

Y hay precedente de que el peso alto no basta: el 30/08 se midió `SEAT_ANCHOR` cayendo al **83%**
de un prompt de 6.331 chars, y el `seated` del L831 salió **de pie** con ese ancla presente.

**Esta tarea NO reescribe el prompt.** Diseña el experimento que dice si vale la pena, porque
**quien genera las imágenes es la Ama** y su cuota es finita.

- [ ] **Paso 1: elegir el look testigo** — uno **0/7**, con falda (para que el eje de cobertura
  esté en juego) y arquitectura ya usada, para no gastar una idea nueva en una prueba.
- [ ] **Paso 2: emitir dos variantes del mismo look**, una sola diferencia entre ellas:
  **A** = prompt vigente completo · **B** = prompt podado, con las anclas que no aplican a ese
  look fuera y máximo 2 cláusulas con peso. Mismo BLOQUE A, mismo BLOQUE B, misma sub-pose.
- [ ] **Paso 3: guardar los dos como JSON en `batches/`** — con nombre y todo. El experimento del
  filtro del L80 **fue irrepetible porque sus prompts nunca existieron como archivo**; no se
  repite ese error.
- [ ] **Paso 4: la Ama genera las 14 imágenes** (7 por variante).
- [ ] **Paso 5: auditar las dos tandas con `outfit.py ojos`** — mismo auditor, ciego a cuál es
  cuál, contando defectos por pose.
- [ ] **Paso 6: escribir el resultado en `.agent/rules/06-generacion-imagenes.md` §10** con el
  número, gane quien gane. **Si B no mejora, el prompt largo se queda y se dice así** — un pase
  no refuta siete rebotes, y un experimento con n=1 por variante tampoco decide solo.

---

# Deuda conocida que este plan NO cierra

Se declara para que nadie la crea resuelta:

- [ ] **Tarea 6 (chica):** `outfit.py test` escribe sus builds de fixtures en
  `99_Sistema/logs/outfit_engine.jsonl` sin marcarlos — 142 entradas con `look: null` por corrida,
  sobre un archivo trackeado. Tres líneas: marcar el evento como `fixture` y que el log las omita.
- [ ] **La marca de agua ✦** del generador aparece en 13 de 14 imágenes auditadas y **no la saca
  ningún prompt**: es de la plataforma. No hay tarea posible acá.
- [ ] **El grueso de los defectos sigue siendo del generador**, no del motor: ~80 de ~85. Este
  plan ataca los 5 que son míos y le da al motor con qué medir los otros 80. **No promete que las
  imágenes mejoren.**
