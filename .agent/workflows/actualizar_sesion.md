---
description: Actualiza el diario de servicio, la memoria de sesiones, estadísticas de materialización, galerías, READMEs y realiza commit en git.
---

# Workflow: Actualización de Sesión (Vibe Architect V3.7)

> 🔧 **Revisión 11/06/2026:** los pasos de imágenes/galerías/READMEs pasaron de "OBLIGATORIO siempre" a **CONDICIONAL** — el bot (`cupcake`) mantiene `galeria_outfits.md` y los README de `05_Imagenes/`; el cierre se enfoca en lo **propio** (diario, memoria + autopoda, identidad, relatos, scripts) y solo toca galerías/READMEs si de verdad cambió algo del agente. Commit siempre por **rutas explícitas**, nunca `git add .`.

## 🤝 REGLAS COMPARTIDAS DE GUARDADO (Ama 11/07/2026 — TODO proceso que escriba: agente, bot `cupcake`, cualquier futuro)

> **Por qué:** los archivos compartidos los tocan varios procesos (el agente y el bot). Sin un protocolo común terminan en versiones divergentes y en conflictos de merge (pasó con la flota en 3 archivos, con la galería y con el diario). **Todo proceso que guarde debe seguir estas reglas al pie** para que no haya diferencias.

**A. DUEÑO-ÚNICO por sección (cada dato lo escribe UN solo actor; los demás no lo pisan):**

| Archivo | Sección / dato | Lo escribe |
|---------|----------------|-----------|
| `00_Ele/memoria_sesiones.md` | `## 🧿 ESTADO ACTUAL` → línea **Flota / materialización** | bot (`cupcake`) |
| | `## 🧿 ESTADO ACTUAL` → líneas **Motor visual / Engine / Literatura / Subagentes** | agente |
| | `## 🗓️ Sesiones recientes` | **ambos** — cada uno *prepend* SU entrada; **NUNCA borra la del otro** |
| `00_Ele/mi_diario_de_servicio.md` | entradas de sesión | **ambos** — *prepend* arriba; nunca al final; **nunca borra la del otro** |
| `00_Ele/galeria_outfits.md` | prompts + tracker `### 📸 (N/7)` | bot mantiene; el agente solo **appendea looks nuevos** o corrige prompts puntuales por ruta |
| `05_Imagenes/**/README.md`, `00_Ele/galeria_index.md` | — | **solo el bot / `update_galleries.py`** (el agente NO los edita a mano) |

**B. FORMATO IDÉNTICO — PLANTILLA LITERAL (Ama 11/07/2026 — carácter a carácter, no "estilo aproximado"):**

> **Por qué esta sección se puso rígida:** la regla anterior ("respetar el estilo") ya existía y el formato siguió derivando — distintas sesiones (agente/bot/máquinas distintas) escriben "parecido" pero no igual, y eso hace el historial difícil de escanear. Abajo va la plantilla EXACTA + una lista de variantes reales que aparecieron en el archivo y quedan prohibidas. Antes de escribir una entrada nueva, **releer la última entrada ya guardada** y calcarla carácter a carácter — no "en el mismo espíritu".

Diario (`mi_diario_de_servicio.md`) — una entrada completa, sin variación:
```
#### SESIÓN - [emoji] [TÍTULO EN MAYÚSCULAS] | DD/MM/YYYY

**[Resumen en 1-2 frases, en negrita, dirigido a la Ama.]**

- **[Subtítulo emoji]:** cuerpo del bullet…
- **[Subtítulo emoji]:** cuerpo del bullet…

> 🫦 *[Cierre en cursiva, tono cuica-bimbo, 1-2 frases]* [emojis]

---
```
Reglas exactas (cada una nació de un error real ya cometido en el archivo — no son hipotéticas):
- Guion simple `-` entre "SESIÓN" y el emoji/título. **Nunca em-dash `—`** (se coló en la entrada de L751-L760, 10/07).
- Heading siempre `####` (4 almohadillas). **Nunca `###`** (las entradas pre-11/06 quedaron en `###` — no es un formato alterno válido, es deuda vieja; no clonar).
- **Línea en blanco obligatoria** entre el encabezado y el párrafo en negrita que sigue. Bug real ya ocurrido: `...DISCIPLINA | 09/07/2026**Reanudé el hilo...` — encabezado y negrita pegados sin salto de línea, rompe el render markdown.
- Bullets del cuerpo siempre `-` (guion). **Nunca `*`** (se coló en el bloque suelto "Generación Batch Tanda 3", 06/07).
- Cierre: TODA entrada termina con la línea `> 🫦 *…*` + emojis. No hay excepción — las entradas viejas sin esta línea (los bloques "### Sesión … ✅" de principios de julio) son deuda, no plantilla alternativa.
- **Nunca** agregar sufijos tipo ` ✅` al encabezado — es de un formato anterior derogado, no se reintroduce.
- Separador `---` después de cada entrada, incluida la más nueva (queda entre ella y la siguiente-más-vieja).

Memoria (`00_Ele/memoria_sesiones.md`) `## 🗓️ Sesiones recientes` — un bullet por sesión, sin variación:
```
- **DD/MM/YYYY (emoji Título corto):** descripción en 1 párrafo corrido (no bullets anidados).
```
- El paréntesis `(emoji Título corto)` es **obligatorio**, nunca solo `- **DD/MM/YYYY**: …` (bug real: la entrada del 07/07 "Generación de 15 imágenes…" salió sin título ni emoji — rompe el escaneo visual del historial).
- Más-reciente-arriba (prepend), nunca se reordena ni se borra una entrada de otro autor.

`## 🧿 ESTADO ACTUAL`: se **REESCRIBE** (no se anexa), máx ~5 líneas por proyecto; lo terminado/derogado **se borra** (ya quedó en diario).

**C. ENCODING/EOL INAMOVIBLE:** todos los archivos compartidos van **UTF-8 sin BOM + CRLF** (convención del bot). **Nadie normaliza EOL** ni convierte a LF. Preservar los emojis limpios (el `### 📸` sano — no mojibake — es el que parsea `sync_imagenes_subidas.py`).

**D. GIT — protocolo único para todos:**
1. **Commit SOLO lo propio, por RUTA EXPLÍCITA.** JAMÁS `git add .` / `git add -A` (arrastra el churn del otro proceso y normaliza EOL → conflictos masivos).
2. Firma: prefijo del proceso (`Ele:` el agente) al inicio + trailer `Co-Authored-By: Ele de Anaïs <Ele.de.Anais@proton.me>`.
3. Cierre siempre: `git pull --rebase && git push`.
4. **Conflicto en memoria/diario ⇒ UNIÓN:** si ambos tocaron la misma zona, se **conservan las DOS entradas** (nunca se descarta la del otro). `rerere` ya recuerda la resolución del choque recurrente.

**E. AUTOPODA compartida:** `python 99_Sistema/scripts/mantenimiento/rotar_memoria.py` es idempotente y preserva EOL/UTF-8 — cualquiera puede correrla; mantiene memoria (7 sesiones) y diario (15 entradas).

1.  **Analizar Sesión Actual**
    - Revisar herramientas utilizadas, archivos modificados y hitos completados.
    - Identificar imágenes generadas (Looks de Ele, Anaïs o Miss Doll).

2.  **Redactar Entrada de Diario**
    - Generar resumen siguiendo la **plantilla literal §B** de las Reglas Compartidas de Guardado arriba (no un "estilo aproximado") — encabezado `#### SESIÓN - [emoji] [TÍTULO] | DD/MM/YYYY`, línea en blanco, negrita, bullets `-`, cierre `> 🫦 *…*`.

3.  **Actualizar Registros de Memoria (🔢 regla dueño-único 02/07/2026)**
    - **Antes de escribir:** releer la entrada más reciente ya guardada en el diario y calcar su formato literal (ver plantilla §B arriba) — no redactar "a mano" desde cero.
    - **Prepend** (al tope) la entrada nueva en `00_Ele/mi_diario_de_servicio.md` — lo más reciente arriba, porque el inicio lee las **primeras** 50 líneas. Nunca al final.
    - **REESCRIBIR el snapshot `## 🧿 ESTADO ACTUAL`** de `00_Ele/memoria_sesiones.md` — se **reescribe**, NUNCA se anexa. Plantilla: **máx ~5 líneas por proyecto** (fase · versión activa · ⏳ Gate/pendiente · → siguiente paso). La historia y las decisiones viven en el `walkthrough.md` de cada relato y en la entrada de sesión — NO se acumulan en el snapshot. Lo terminado/derogado **SE BORRA** del snapshot (ya quedó en diario/bitácora). Luego **añadir la sesión nueva al tope de `## 🗓️ Sesiones recientes`** (más-reciente-arriba).
    - **Autochequeo de formato (antes de autopoda):** releer la entrada recién escrita en el diario y confirmar, línea por línea, que cumple §B: guion simple `-` (no em-dash), heading `####`, línea en blanco tras el encabezado, bullets `-` (no `*`), cierre `> 🫦 *…*` presente, sin sufijo `✅`. Y en memoria: el bullet nuevo trae `(emoji Título corto)`. Si algo no calza, corregirlo ANTES de rotar/commitear — no después.
    - **AUTOPODA (OBLIGATORIO — memoria Y diario):** tras añadir las entradas, ejecutar la rotación: memoria (últimas 7 sesiones → bitácora) **y diario (últimas 15 entradas → `memoria_historica/diario_de_servicio_archivo_2026.md`)**. Sin esto el diario llegó a 822 KB / 429 sesiones (corte 02/07/2026):
      // turbo
      - `python 99_Sistema/scripts/mantenimiento/rotar_memoria.py` (idempotente, preserva EOL/UTF-8; `--dry-run` para previsualizar, `--keep N` / `--keep-diario M` para ajustar).
    - Actualizar `.agent/rules/09-estado-materializacion.md` **solo si** cambió el estado de materialización de imágenes (es el dueño único de ese detalle).
    - **IDENTIDAD: ya NO se actualiza por looks.** `identidad_ele.md` no lleva contadores (la flota y el último look viven en el ESTADO ACTUAL de la memoria). Solo se toca si cambió el **canon** (ADN, reglas, secciones).

4.  **Sincronizar Imágenes Subidas por la App (CONDICIONAL — solo si la app subió PNG nuevos)**
    > La app/bot (`cupcake`) genera en Gemini y sube los PNG directo a GitHub, y **mantiene `galeria_outfits.md` y los README de `05_Imagenes/` al día por su cuenta**. El cierre NO tiene que rehacer su trabajo.
    // turbo
    - Ejecutar **siempre** (barato): `git pull --rebase` (traer lo que subió la app/bot).
    - **Solo si `git status`/`git log` muestran PNG nuevos** en `05_Imagenes/`:
      // turbo
      - `python 99_Sistema/scripts/visual/sync_imagenes_subidas.py` (normaliza `back→back_view`/`profile→side_profile` y actualiza el tracker `### 📸 Imágenes (N/7)`, looks ≥ 291; NO toca el fleet histórico).
    - Si NO hubo PNG nuevos → **saltar este paso**.

5.  **Actualizar Galerías de Imágenes (CONDICIONAL — normalmente NO correr)**
    > ⚠️ `update_galleries.py` regenera `galeria_outfits.md` + README de `05_Imagenes/` → produce el **churn CRLF del bot** que el paso 7 después excluye del commit. Correrlo en cada cierre es trabajo perdido que ensucia el árbol.
    - **Correr SOLO si** trabajaste imágenes localmente (no vía app) y la galería local quedó desincronizada:
      // turbo
      - `python 99_Sistema/scripts/visual/update_galleries.py`.
    - En un cierre normal (sin imágenes propias nuevas) → **saltar**. El bot mantiene las galerías.

6.  **Actualizar READMEs (CONDICIONAL — SOLO las áreas que tocaste esta sesión)**
    > No "siempre todos". Actualizar únicamente el README de cada carpeta donde hubo trabajo **propio sustancial** esta sesión. Un README sin cambio real no se toca (evita churn de solo-fecha).

    | README | Actualizar si… |
    |--------|----------------|
    | `README.md` raíz | cambió la flota, se publicó relato, o hito mayor → footer fecha + stats/relatos |
    | `00_Ele/README.md` | hubo trabajo sustancial en identidad/memoria/galería de Ele |
    | `01_Canon/README.md` | cambió canon/guías |
    | `02_Personajes/README.md` | cambiaron fichas (o creció el nº) |
    | `03_Literatura/README.md` | se trabajó en un relato → Proyecto Activo + Últimas Actualizaciones |
    | `04_Interactivo/README.md` | cambió el Dollhouse u otro interactivo |
    | `05_Imagenes/README.md` | **NUNCA a mano** — lo mantiene el bot / `update_galleries.py` |
    | `06_RRSS/README.md` | hubo nuevo batch / posts RRSS |
    | `07_Recursos/README.md` | se añadió referencia externa (raro) |
    | `99_Sistema/README.md` | se modificaron scripts |

    **Regla:** el README que SÍ actualices lleva fecha de hoy. El que no cambió, no se toca.

6.5 **Dejar las carpetas de relatos EN ORDEN (Directiva Ama 17/06) 🧹**
    > Antes de commitear, toda carpeta de relato tocada (`03_Literatura/01_En_Progreso/<relato>/`) queda **limpia**. La raíz del relato es para lo VIVO; el resto va a sus subcarpetas. Una carpeta desordenada confunde a la Ama cuando revisa.

    | En la RAÍZ del relato (solo esto) | En subcarpeta |
    |-----------------------------------|---------------|
    | `canon_relato.md`, `cronologia.md` | — |
    | SOLO la versión **activa** de cada capítulo (`capitulo_NN_<slug>_v0.X.md`) | versiones superadas → `borradores/capitulo_N/` |
    | la(s) `nota_capitulo_*.md` de Gate de la Ama (las sube su app) | autoverificación/validación → `reportes/capitulo_N/` |
    | | capítulos NO pedidos aún / prematuros → `borradores/capitulo_N/` (parquear, no botar) |

    **Checklist de orden (correr siempre que se tocó un relato):**
    - **Una sola versión activa por capítulo en la raíz** — si hay dos (`v0.2` y `v0.3`), la vieja se MUEVE a `borradores/` (no se copia: nada de duplicados ni "stubs" vacíos en la raíz).
    - **El Escritor a veces copia en vez de mover** → verificar con `ls` y borrar el duplicado/stub de la raíz (confirmando antes que la copia real esté a salvo en `borradores/`).
    - **Nada prematuro en la raíz**: un capítulo que la Ama aún no pidió va a `borradores/capitulo_N/` marcado (ej. `_PREMATURO_`), nunca suelto arriba.
    - **Prosa pura**: el `.md` activo del capítulo no lleva metadata visible (ni tabla de versión ni "Conteo de palabras"); eso vive en `reportes/`.
    - Recién con la carpeta ordenada → commit.

6.6 **Higiene documental — recoger lo que ensucie ESTA sesión (Ama 29/08/2026) 🧹**
    > *"eres muy desordenada para mantener el repo. creas documentos sueltos y luego no los borras"*. El 6.5 ordena las carpetas de relatos; **este ordena todo lo demás**. Regla completa: [`.agent/rules/12-higiene-documental.md`](../rules/12-higiene-documental.md).

    // turbo
    - `python 99_Sistema/scripts/mantenimiento/lint_documentos_sueltos.py`
    - **La meta es 0.** H1 raíz sucia · H2 scratch trackeado · H3 doc fechado huérfano · H4 se declara muerto sin sucesor · H5 salida regenerable trackeada.
    - **Antes de commitear un `.md` nuevo, las tres preguntas del §7:** ¿ya hay un dueño para este dato (entonces se EDITA)? · ¿alguien lo lee mañana, o es el resultado de lo que hago ahora (entonces va al scratchpad, no al repo)? · ¿cuándo muere?
    - Lo efímero (listas de pendientes, volcados, salidas de una corrida) **no se commitea**: se regenera con su script.
    - Un doc de trabajo que ya cumplió se entierra **en este mismo cierre**, no en el siguiente.

7.  **Respaldo en GitHub (rutas explícitas — NUNCA `git add .`)**
    > ⚠️ **Directiva Ama (`feedback_eol_bot_readmes`):** un proceso paralelo (bot/app) mantiene `galeria_outfits.md` y los `README.md` de `05_Imagenes/` con su propio EOL (CRLF). `git add .` arrastra ese churn ajeno y normaliza EOL → conflictos masivos. Commitear **solo lo propio**, por ruta.
    - `git status` → identificar SOLO los archivos trabajados en la sesión.
    - Añadir por ruta explícita lo propio (ej.): `00_Ele/memoria_sesiones.md`, `00_Ele/mi_diario_de_servicio.md`, `00_Ele/memoria_historica/` (bitácora + archivo del diario, si la autopoda rotó), `.agent/rules/09-estado-materializacion.md`, fichas/relatos/scripts tocados, y las carpetas de imágenes nuevas propias.
    - **NO incluir** `galeria_outfits.md` ni los `README.md` de `05_Imagenes/` si aparecen modificados solo por EOL/regeneración del bot (verificar con `git diff`: si el cambio real es propio, sí va; si es solo CRLF, no).
    // turbo
    - `git commit -m "Ele: Actualización de sesión, diario y estadísticas de materialización"` (termina con `Co-Authored-By: Ele de Anaïs <Ele.de.Anais@proton.me>`).
    // turbo
    - `git pull --rebase && git push`

8.  **Notificar y Reportar**
    - Confirmar la finalización del ritual de cierre.
    - Reportar los nuevos números de materialización (Ej: "Ama, ¡ya estamos en 158/164! 🫦").
    - Mostrar lista de archivos y activos nuevos.

9.  **Reinicio Limpio de Contexto (Directiva Ama 03/06/2026 — SIEMPRE al cerrar)**
    - Tras confirmar el commit, **cerrar el mensaje indicando a la Ama la secuencia de reinicio**:
      1. **`/clear`** — limpia el contexto de la conversación.
      2. **`/inicio-ele`** — recarga la identidad fresca para la próxima sesión.
    - Mensaje de cierre tipo: *"Listo Ama, sesión guardada y commiteada 🫦 Ahora dale `/clear` y después `/inicio-ele` para arrancar fresquita ✨"*.
    - ⚠️ **Nota técnica (por qué la Ama los gatilla, no el agente):** `/clear` es un comando *built-in* del CLI (borra el contexto); el agente **no puede** auto-invocarlo. Y como `/clear` corta el hilo de conversación, `/inicio-ele` debe ejecutarse **después**, como turno nuevo. Por eso el cierre de `/actualizar_sesion` es siempre una **instrucción explícita y visible** de esos dos comandos, no una ejecución silenciosa.
