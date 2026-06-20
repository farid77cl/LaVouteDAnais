---
description: Actualiza el diario de servicio, la memoria de sesiones, estadísticas de materialización, galerías, READMEs y realiza commit en git.
---

# Workflow: Actualización de Sesión (Vibe Architect V3.7)

> 🔧 **Revisión 11/06/2026:** los pasos de imágenes/galerías/READMEs pasaron de "OBLIGATORIO siempre" a **CONDICIONAL** — el bot (`cupcake`) mantiene `galeria_outfits.md` y los README de `05_Imagenes/`; el cierre se enfoca en lo **propio** (diario, memoria + autopoda, identidad, relatos, scripts) y solo toca galerías/READMEs si de verdad cambió algo del agente. Commit siempre por **rutas explícitas**, nunca `git add .`.

1.  **Analizar Sesión Actual**
    - Revisar herramientas utilizadas, archivos modificados y hitos completados.
    - Identificar imágenes generadas (Looks de Ele, Anaïs o Miss Doll).

2.  **Redactar Entrada de Diario**
    - Generar resumen siguiendo el estilo de `00_Ele/mi_diario_de_servicio.md`.
    - Formato: `#### SESIÓN - [TÍTULO] | [FECHA]` con descripción de actos de servicio.

3.  **Actualizar Registros de Memoria**
    - **Prepend** (al tope) la entrada nueva en `00_Ele/mi_diario_de_servicio.md` — lo más reciente arriba, porque el inicio lee las **primeras** 50 líneas. Nunca al final.
    - **Actualizar el snapshot `## 🧿 ESTADO ACTUAL`** de `00_Ele/memoria_sesiones.md` (proyecto activo, último look, pendientes vivos) y **añadir la sesión nueva al tope de `## 🗓️ Sesiones recientes`** (más-reciente-arriba). Mantener el ESTADO ACTUAL DESTILADO, no un volcado del log.
    - **AUTOPODA DE MEMORIA (OBLIGATORIO — evita que la memoria vuelva a crecer a 1.700 líneas):** tras añadir la entrada, ejecutar la rotación. Conserva las últimas 7 sesiones en `memoria_sesiones.md` y archiva las más viejas al tope de `memoria_historica/bitacora_sesiones_2026.md`:
      // turbo
      - `python 99_Sistema/scripts/mantenimiento/rotar_memoria.py` (idempotente, preserva EOL/UTF-8; usar `--dry-run` para previsualizar o `--keep N` para ajustar la ventana).
    - **NUEVO:** Actualizar `.agent/rules/09-estado-materializacion.md` si hubo cambios en los contadores de looks o imágenes generadas.
    - **IDENTIDAD (OBLIGATORIO si hubo nuevos looks):** Actualizar la tabla "Estado Actual de Looks" en `00_Ele/identidad_ele.md` §XI:
      - `Total Looks` → nuevo número de flota
      - `Último Look` → nombre y fecha del último look generado
      - `*Actualizado:*` → fecha de hoy + descripción del hito

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

7.  **Respaldo en GitHub (rutas explícitas — NUNCA `git add .`)**
    > ⚠️ **Directiva Ama (`feedback_eol_bot_readmes`):** un proceso paralelo (bot/app) mantiene `galeria_outfits.md` y los `README.md` de `05_Imagenes/` con su propio EOL (CRLF). `git add .` arrastra ese churn ajeno y normaliza EOL → conflictos masivos. Commitear **solo lo propio**, por ruta.
    - `git status` → identificar SOLO los archivos trabajados en la sesión.
    - Añadir por ruta explícita lo propio (ej.): `00_Ele/memoria_sesiones.md`, `00_Ele/mi_diario_de_servicio.md`, `00_Ele/identidad_ele.md`, `.agent/rules/09-estado-materializacion.md`, fichas/relatos/scripts tocados, y las carpetas de imágenes nuevas propias.
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
