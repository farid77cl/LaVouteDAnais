---
description: Cierre de sesión — diario, memoria (reescritura + autopoda), higiene, galerías/READMEs si tocaste imágenes, y commit por rutas explícitas.
---

# Workflow: Actualización de Sesión (Vibe Architect)

> 🔧 **Corregido 10/09/2026 (auditoría externa Fable, ciega):** hasta hoy este archivo decía que el bot `cupcake` "mantiene `galeria_outfits.md` y los README de `05_Imagenes/`". **Es falso, medido contra `git log`:** los últimos commits a esos archivos son todos `Ele de Anaïs`/`Claude` — `cupcake` es la identidad de la app de la Ama (sube/borra PNG, edita notas), nunca ha tocado galería ni READMEs. El paso 5 llevaba meses diciendo "normalmente NO correr `update_galleries.py`" por esta razón falsa, contradiciendo el flujo real de `CLAUDE.md` § Image flow. Corregido abajo: la galería/READMEs son trabajo del agente, condicional a si hubo imágenes nuevas.

## 🤝 Reglas compartidas de guardado (todo proceso que escriba: agente, app `cupcake`)

**A. Dueño único por dato** (detalle completo: `.agent/rules/00-contexto-obligatorio.md` §🔢 — aquí solo lo que ese archivo no cubre):

| Archivo | Sección | Lo escribe |
|---|---|---|
| `00_Ele/memoria_sesiones.md`, `00_Ele/mi_diario_de_servicio.md` | Sesiones / entradas | **ambos** — cada uno hace *prepend* de la suya, nunca borra la del otro |
| `00_Ele/galeria_outfits.md`, `05_Imagenes/**/README.md`, `galeria_index.md` | prompts, tracker, READMEs | **el agente** (vía `update_galleries.py` / a mano) — la app `cupcake` solo sube/borra PNG y edita notas, nunca estos archivos |

**B. Plantilla literal — carácter a carácter, no "estilo aproximado" (Ama 11/07/2026):**

> Nació porque "respetar el estilo" no bastaba: sesiones/máquinas distintas escribían "parecido" y el historial quedó difícil de escanear. Antes de escribir una entrada nueva, **releer la última ya guardada y calcarla**.

Diario (`mi_diario_de_servicio.md`) — una entrada completa:
```
#### SESIÓN - [emoji] [TÍTULO EN MAYÚSCULAS] | DD/MM/YYYY

**[Resumen en 1-2 frases, en negrita, dirigido a la Ama.]**

- **[Subtítulo emoji]:** cuerpo del bullet…
- **[Subtítulo emoji]:** cuerpo del bullet…

> 🫦 *[Cierre en cursiva, tono cuica-bimbo, 1-2 frases]* [emojis]

---
```
Reglas exactas (cada una nació de un error real ya cometido en el archivo):
- Guion simple `-`, **nunca em-dash `—`**.
- Heading `####` (4 almohadillas), **nunca `###`** (deuda pre-11/06, no clonar).
- Línea en blanco entre el encabezado y el párrafo en negrita (bug real: quedaron pegados y rompieron el render).
- Bullets `-`, **nunca `*`**.
- Cierre `> 🫦 *…*` + emojis siempre presente — sin excepción, sin sufijo ` ✅`.
- Separador `---` después de cada entrada.

Memoria (`00_Ele/memoria_sesiones.md`) `## 🗓️ Sesiones recientes` — un bullet por sesión:
```
- **DD/MM/YYYY (emoji Título corto):** descripción en 1 párrafo corrido (no bullets anidados).
```
El paréntesis `(emoji Título corto)` es obligatorio (bug real: una entrada salió sin él y rompió el escaneo visual). Prepend siempre — nunca se reordena ni se borra una entrada de otro autor.

**C. Encoding/EOL:** UTF-8 sin BOM + CRLF en archivos compartidos. Nadie normaliza EOL ni convierte a LF.

**D. Git — protocolo único:**
1. Commit **solo lo propio, por ruta explícita**. Jamás `git add .` / `git add -A` (arrastra churn ajeno + normaliza EOL → conflictos masivos, `feedback_eol_bot_readmes`).
2. Firma: `Ele:` al inicio + trailer `Co-Authored-By: Ele de Anaïs <Ele.de.Anais@proton.me>`.
3. Cierre siempre: `git pull --rebase && git push`.
4. **Conflicto en memoria/diario ⇒ unión:** si ambos tocaron la misma zona, se conservan las DOS entradas — nunca se descarta la del otro.

**E. Autopoda:** `rotar_memoria.py` es idempotente — detalle y evidencia en el paso 3.

---

0. **Traer lo que llegó primero (antes de escribir nada):**
   // turbo
   - `git pull --rebase` — si escribes memoria/diario antes de traer el remoto, el rebase de después choca contra tus propios cambios sin sentido. Barato, se corre siempre.

1. **Analizar la sesión:** herramientas usadas, archivos modificados, hitos completados, imágenes generadas (Ele/Anaïs/Miss Doll).

2. **Redactar la entrada de diario** según la plantilla literal **§B** — no un estilo aproximado.

3. **Actualizar memoria (dueño-único 02/07/2026):**
   - Releer la última entrada guardada y calcar su formato (§B) antes de escribir.
   - **Prepend** la entrada nueva en `mi_diario_de_servicio.md` — nunca al final (el arranque lee la primera entrada).
   - **REESCRIBIR** `## 🧿 ESTADO ACTUAL` de `memoria_sesiones.md` — nunca se anexa. Máx ~5 líneas por proyecto (fase · versión activa · ⏳ Gate/pendiente · → siguiente paso); la historia vive en el `walkthrough.md` de cada relato, no aquí. Lo terminado/derogado se borra del snapshot. Luego prepend de la sesión nueva en `## 🗓️ Sesiones recientes`.
   - **Autochequeo antes de rotar:** releer lo recién escrito contra los 7 puntos de §B (diario) y la plantilla del bullet (memoria). Corregir ahora, no después.
   - **Autopoda (obligatoria, memoria y diario):** sin esto el diario llegó a 822 KB / 429 sesiones (corte 02/07/2026).
     // turbo
     - `python 99_Sistema/scripts/mantenimiento/rotar_memoria.py` (idempotente, preserva EOL/UTF-8; `--dry-run` para previsualizar, `--keep N` / `--keep-diario M` para ajustar; mantiene 7 sesiones / 15 entradas por defecto).
   - `.agent/rules/09-estado-materializacion.md`: tocar **solo si** cambió el estado de materialización (es su dueño único).
   - `identidad_ele.md`: tocar **solo si** cambió el canon (ADN, reglas, secciones) — no lleva contadores de flota.

4. **Imágenes y galería (condicional — solo si hubo PNG nuevos, de la app o propios):**
   - `git status`/`git log` ya deberían mostrarlo tras el pull del paso 0.
   - Si hay PNG nuevos de la app:
     // turbo
     - `python 99_Sistema/scripts/visual/sync_imagenes_subidas.py` (normaliza `back→back_view`/`profile→side_profile`, actualiza el tracker `### 📸 (N/7)`, looks ≥ 291; no toca el fleet histórico).
   - Si la galería quedó desincronizada (imágenes propias, o tras el sync de arriba):
     // turbo
     - `python 99_Sistema/scripts/visual/update_galleries.py` (regenera READMEs + galería maestra — **este paso lo hace el agente, nadie más lo mantiene**).
   - Si NO hubo PNG nuevos ni cambios de galería → saltar el paso entero.

5. **READMEs (condicional — solo las áreas tocadas esta sesión):** un README sin cambio real no se toca (evita churn de solo-fecha).

   | README | Actualizar si… |
   |---|---|
   | `README.md` raíz | cambió la flota, se publicó relato, o hito mayor |
   | `00_Ele/README.md` | trabajo sustancial en identidad/memoria/galería de Ele |
   | `01_Canon/README.md` | cambió canon/guías |
   | `02_Personajes/README.md` | cambiaron fichas |
   | `03_Literatura/README.md` | se trabajó un relato |
   | `04_Interactivo/README.md` | cambió el Dollhouse |
   | `05_Imagenes/README.md` | vía `update_galleries.py` (paso 4) — nunca a mano |
   | `06_RRSS/README.md` | nuevo batch/posts RRSS |
   | `07_Recursos/README.md` | referencia externa nueva |
   | `99_Sistema/README.md` | scripts modificados |

5.5. **Carpetas de relato en orden (Ama 17/06) 🧹** — antes de commitear, toda carpeta de relato tocada (`03_Literatura/01_En_Progreso/<relato>/`) queda limpia: la raíz es solo lo VIVO.

   | En la raíz (solo esto) | En subcarpeta |
   |---|---|
   | `canon_relato.md`, `cronologia.md` | — |
   | Solo la versión **activa** de cada capítulo | versiones superadas → `borradores/capitulo_N/` |
   | `nota_capitulo_*.md` de Gate (sube la app) | autoverificación/validación → `reportes/capitulo_N/` |
   | | capítulos no pedidos aún → `borradores/capitulo_N/` (parquear, no botar) |

   Checklist: una sola versión activa por capítulo en la raíz (la vieja se MUEVE, no se copia) · el Escritor a veces copia en vez de mover — verificar con `ls` y borrar el duplicado · nada prematuro suelto en la raíz · prosa pura, sin metadata visible.

5.6. **Higiene documental — lo que ensucia ESTA sesión (Ama 29/08/2026) 🧹** — el 5.5 ordena relatos, este ordena todo lo demás. Regla completa: [`../rules/12-higiene-documental.md`](../rules/12-higiene-documental.md).
   // turbo
   - `python 99_Sistema/scripts/mantenimiento/lint_higiene_repo.py` — meta **0**. Los nueve chequeos y las tres preguntas de "¿se commitea esto?" viven en la regla 12 §6-§7, no se repiten aquí.
   - Lo efímero (pendientes, volcados, salidas de una corrida) no se commitea — se regenera con su script.
   - Un doc de trabajo que ya cumplió se entierra en este mismo cierre.

6. **Commit — rutas explícitas, protocolo en §D:**
   - `git status` → identificar solo lo trabajado esta sesión.
   - Añadir por ruta explícita: memoria, diario, `memoria_historica/` (si la autopoda rotó), `09-estado-materializacion.md` si cambió, fichas/relatos/scripts tocados, imágenes propias nuevas.
   - Si `galeria_outfits.md` / READMEs de `05_Imagenes/` aparecen modificados, verificar con `git diff` que el cambio es real (no solo CRLF de una regeneración sin contenido nuevo) antes de incluirlos.
   // turbo
   - `git commit -m "Ele: <resumen real de lo que se hizo esta sesión>"` (nunca un mensaje fijo genérico — §D.2 para la firma completa).
   // turbo
   - `git pull --rebase && git push`

7. **Notificar:** confirmar el cierre, mostrar archivos y activos nuevos, y el estado que corresponda (materialización si cambió, Gates pendientes, lo que quedó abierto).

8. **Reinicio limpio (Ama 03/06/2026 — siempre al cerrar):**
   - Cerrar el mensaje indicando la secuencia: **1) `/clear`** (limpia el contexto) → **2) `/inicio-ele`** (identidad fresca).
   - Mensaje tipo: *"Listo Ama, sesión guardada y commiteada 🫦 Ahora dale `/clear` y después `/inicio-ele` para arrancar fresquita ✨"*.
   - **Por qué lo pide la Ama y no lo ejecuta el agente:** `/clear` es un comando del CLI que el agente no puede auto-invocar, y corta el hilo — `/inicio-ele` tiene que ser un turno nuevo después. Por eso el cierre siempre es una instrucción visible, nunca una ejecución silenciosa.
