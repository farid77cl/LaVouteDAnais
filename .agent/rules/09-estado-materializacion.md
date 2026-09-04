# 📊 ESTADO DE MATERIALIZACIÓN Y ESTADÍSTICAS (V3.12)

Este documento es el registro de "memoria viva" sobre el progreso visual del repositorio. Debe ser consultado antes de cada Batch y actualizado después de cada sincronización exitosa (Última actualización: 03/09/2026 — sync `sync_imagenes_subidas.py` + `sync_tracker_galeria_personaje.py`: **19 looks de Ele L397-L463 corregidos, 70 poses reales que el tracker daba por pendientes** · Anaïs L64 recuperado a 7/7 y **L75 subió a 4/7 real** (Standing/Back View/Seated/Side Profile ya generados con el prompt de rostro corregido — ver nota del mismo día abajo) · Miss Doll ya sincronizado, 0 correcciones. Antes: 02/09 — 24 looks L332-L396 corregidos, 137 poses.

> 🗑️💅 **04/09/2026 — Miss Doll L71-L75: los cinco looks se RECHAZARON y se rediseñaron desde cero, no se les corrigió el prompt.** La Ama: *"odié los últimos 5 outfits de miss doll, hazlos de nuevo, desde cero"*, y marcó las cuatro causas a la vez — fórmula clonada, arquetipos elegidos por matemática de déficit, siluetas demasiado tapadas y paleta apagada. **Esto deroga la línea del 03/09 que los dejaba "pendientes de regenerar con el prompt corregido": el prompt corregido también murió.** Medido antes de rehacer: 5/5 llevaban choker de chrome, 5/5 plataforma de suela chrome, 5/5 el rosa firma degradado a un detalle decorativo, y 3/5 repetían la cláusula de tanga **verbatim**. **Imágenes: no había ninguna que borrar** — verificado con `git ls-files 05_Imagenes/miss_doll/ | grep -E "look7[1-5]_"` → **0 archivos**, la última carpeta materializada es `look70_magenta_chrome_stage_sovereign`; las 33 se borraron el 03/09 y nunca se regeneraron, así que el rechazo fue sobre texto, no sobre PNG. Batch nuevo: `batches/MD_L71_L75_rediseno.json` (el viejo `MD_L71_L75_deficit.json` se borró del repo). Arquitecturas M7·M4·M2·M3·M6, cinco familias cromáticas distintas, el rosa firma en un lugar distinto en cada look. **Siguen en 0/7 — la generación es de la app de la Ama, nunca del agente.**
>
> 🐛🫦 **03/09/2026 — bug real del negative + rostro de Anaïs poco dominante, ambos encontrados y corregidos.** `PromptBuilder.build_negative()` solo ensamblaba `negative_extra`, nunca la base §3 del perfil — desde el 29/08 probablemente todos los batches salieron con el negative incompleto. Fix: property `negativo_base` (mismo patrón que `bloque_a`) + inyección automática + `negative_excluir` para excepciones puntuales. De paso, auditoría Fable sobre 18 imágenes de Anaïs (L66-75) encontró rostro sistemáticamente poco dominante (boca cerrada en 10/10 Standing, Sovereign Gaze con mirada sumisa hacia abajo en 4/8) — reforzado el BLOQUE A (instrucción facial concreta, peso 1.5), corregido el negativo (sacado `open mouth/seductive/tempting`) y reescritas 3 de 7 sub-poses del slot5 con mirada baja. **Borradas las 33 imágenes ya materializadas de Anaïs L71-75 y Miss Doll L71-75** (prompts viejos, orden de la Ama) para que la próxima generación tome la corrección — trackers de esos 10 looks vueltos a 0/7. Detalle completo: commits `356a74caa` y de la sesión del 03/09. **Pendiente: auditar contra el Fable las 4 poses nuevas de Anaïs L75 (ya con el fix puesto) cuando la Ama lo pida.**
>
> 🎀 **Mismo día — clon de silueta en Girly Girl de Miss Doll, encontrado antes de generar.** Looks 47, 53 y el nuevo 75 eran la misma arquitectura (minifalda plisada + top corto), solo cambiaba el color — hallazgo de la Ama. El 75 (0/7 en ese momento) se rediseñó a romper + peto pinafore antes de que se generara nada.

## 📱 FLUJO DE IMÁGENES SUBIDAS POR LA APP (Gemini → GitHub) — era app, looks ≥ 291

## Auditoría 25 de Junio 2026 (Looks 200 a 300)
- **Rango analizado:** `look200_*` a `look300_*`
- **Total de prompts registrados (L200-L300):** 338
- **Imágenes esperadas (4 poses por look aprox + extras):** 338
- **Total imágenes encontradas físicamente:** 281
- **Imágenes materializadas recientemente:** L313 y L314 completos. **L315 y L316 quedan 6/7** — sus POV se purgaron (salieron *selfie literal*, violando el canon POV) y esperan regeneración con el prompt ya corregido.
- **Faltantes reales restantes:** En avance progresivo sobre déficit L317-L400.
- **🐍 Batch L761-L770 «Veneno Tropical»:** la app lo está materializando — **L761, L762, L763 y L765 completos (7/7)** · **L764 6/7** (falta Standing) · **L766 2/7** · **L767-L770 sin empezar**.

> [!NOTE]
> **📸 BATCH DE PRUEBA DEL MOTOR v3.0 — L813-817 / MD L66-70 / Anaïs L66-70 (30/08/2026).** Materialización medida contra `git ls-files`: **Ele** L813/814/815/817 en 7/7, **L816 6/7** (su Ditzy era copia byte a byte del Side Profile — nunca se generó, borrado) · **Miss Doll** L68/69/70 en 7/7, L66-L67 en 0/7 · **Anaïs** L66-L68 en 1/7 (solo Standing), L69-L70 en 0/7. **⚠️ Envejeció hacia la mentira — corregido 03/09/2026:** la app siguió subiendo entre sesiones; medido de nuevo contra `git ls-files` antes de tocar nada, **Anaïs L66-L70 estaban 7/7 reales** (quedan así, no se tocaron) y **L71-L74 también habían llegado a 7/7** — pero esas sí se borraron ese mismo día (33 imágenes, prompt viejo, orden de la Ama — ver nota del 03/09 arriba) y vuelven a estar en 0/7 a propósito, pendientes de regenerar con el prompt corregido.
> 🐛 **Bug del look fantasma, reincidente:** la app archivó dos poses bajo un número de look que no existe — `look20062` (miss_doll L62, 29/08) y `look20069` (miss_doll L69, 30/08), ambas con prefijo `2` pegado al número real. Las dos rescatadas a mano; **la causa raíz sigue sin diagnosticar en LV-App**, queda para la v5.0.
> 🎯 **Auditoría prompt↔imagen (35 poses de Ele leídas una por una) encontró 4 defectos con ANCLA PRESENTE** — no arbitrarios: L813 Back View (marcas de tatuaje sobre la chaqueta) · L813 POV (salió sin mangas) · L814 Seated (no está sentada, sigue de pie) · L815 Back View (short con cobertura completa, viola tanga). Directiva de la Ama: *"si las anclas estaban y se generaron imágenes malas hay que reforzar el ancla"* — no se acepta "lotería de Gemini" como explicación. Reforzadas con cola afirmativa `:1.4` (SEAM_FRONT/BACK, SEAT_ANCHOR, BOTTOM_CUT_LOCK, GARMENT_CONSISTENCY) + ancla nueva `FABRIC_PRISTINE`. Detalle: `.agent/rules/06-generacion-imagenes.md` §9.
> ⏳ **Pendiente de materializar con el prompt reforzado** (ya escrito en la galería, solo falta la imagen): Ele L813 back_view+pov · L814 seated · L815 back_view · L816 ditzy · Miss Doll L69 back_view · Miss Doll L70 standing · Anaïs L68 standing.
> ⛔ **Miss Doll L68 "Liquid Rose Catsuit" queda FUERA de esta lista a propósito** — vetado por la Ama (*"horrible outfit"*), conservado **como contraejemplo**, no se regenera ni se rediseña.

> [!IMPORTANT]
> **Los prompts del rango 300+ fueron REFRESCADOS el 12/07** contra los fixes del motor **de esa fecha** (1.167 poses reescritas). Antes arrastraban texto pre-fix: POV literal que salía **selfie**, tokens **anti-safe que rebotaban el filtro y quemaban cuota**, y falta de ancla anatómica. Las poses que ya tenían imagen quedaron intactas.

> [!NOTE]
> **🧪 VEREDICTO DEL BATCH DE ESTRÉS L791-L800 (auditado 15/07/2026 — 62 poses + 8 descartes etiquetados).**
> **Vectores MUERTOS:** odalisca-percha (L796 en el suelo ✅) · Seated-isla bug L754 (L797 en el taburete ✅) · control inverso (L798 runas perfectas en piel desnuda ✅) · leopard drift (L794 ✅) · deriva color medias (L795 ✅) · capucha (L800 6/7).
> **Vectores VIVOS (motor v3 los ataca):** collage (L792 Standing 7-paneles DESCALZA · Ditzy reincidente ×3 · variante nueva: marcos/light-boxes con su imagen dentro de la escena) · guantes-manga gris (L792 ×7, L799 ×2 en bikini) · marcas nombradas sobre zona cubierta (aro sobre látex L791, glifos sobre el calzón L792, runas migradas a muslos L797). **L793 quedó 0/7** (sin imágenes NI descartes = no se intentó o murió sin registro). ⚠️ **38/62 poses entraron como miniaturas 286×512 pese a la guardia del APK #5** — confirmar versión del APK instalado.

> [!NOTE]
> **🔎 HUECOS L309/L310/L350 + PAQUETE V3 PERDIDO (auditoría 17/07/2026):** 13 poses faltantes — **L309:** back_view, side_profile, ditzy, pov, odalisque · **L310:** back_view, ditzy, odalisque · **L350:** seated, side_profile, ditzy, pov, odalisque. El paquete de prompts V3 preparado el 16/07 para flujo manual **se perdió** (era un artifact de conversación, no un archivo del repo) y la única imagen generada ese día (L309 side_profile) **nunca se commiteó** (revisar working tree de la máquina visual). Sus prompts en galería siguen v1 fosilizados. ⏳ Pendiente: regenerar el paquete **como archivo** con el método de inyectores del 15/07. Lateral: trackers L355-L361 desactualizados respecto a las subidas del 16-17/07 (L358 real 7/7 vs «2/7») — corregir con sync desde la máquina visual (la solo-literaria cuenta 0 PNG en disco).

> [!CAUTION]
> **🔴 PENDIENTE #1 — CORREGIDO 22/07/2026: EL RANGO FOSILIZADO ES L200-L299, NO EL 300-760.**
> Esta nota decía que los prompts **300-760** seguían fosilizados. **Se midió sobre los 601 looks y es falso** — el refresco del 12/07 sí llegó a ese rango:
>
> | Rango | SKIN_LOCK | SINGLE_FRAME (`a single continuous photograph`) |
> |---|---|---|
> | **L200-L299** | **0/100** | **0/100** |
> | L300-L499 | 200/200 | 200/200 |
> | L500-L699 | 200/200 | 200/200 |
> | L700-L800 | 101/101 | 101/101 |
>
> **El hueco real son los 100 looks de L200-L299**, sin un solo candado del motor. De ellos, **21 tienen poses sin materializar**: si la app genera ahí, sale con el defecto y quema cuota. Ese es el alcance del barrido pendiente (las poses que ya tienen imagen no se tocan).
>
> Dos correcciones más de la misma medición:
> - El **Bloque A viejo** (`nipple piercings pressing against and visible under clothing`) no está en todo el rango: son **7 apariciones** en total.
> - El **metalenguaje multi-toma** (`in every shot`, causa registrada de collage) sobrevive en **39 looks**, y **30 de ellos están en L761-L800** — los más nuevos, no los viejos. Llevan el ancla afirmativa `SINGLE_FRAME` puesta, así que el riesgo es residual, pero el token prohibido sigue escrito.
>
> ⚠️ **Lección de método:** esta nota se escribió una vez y nunca se volvió a medir. Un estado que dice "pendiente" sin fecha de verificación **envejece hacia la mentira** y manda a barrer donde ya está limpio mientras el hueco real queda sin tocar.

> [!NOTE]
> **⚠️ Auditar el repo MIENTE (aprendido 13/07):** las imágenes commiteadas son las **sobrevivientes** de varios reintentos de la Ama — miden su tasa de éxito *después* del filtro humano, no la del prompt. Si la Ama dice que tuvo que regenerar, **el defecto existe** aunque lo guardado se vea limpio.

> [!TIP]
> **✅ EL CASO DE LAS MINIATURAS QUEDÓ CERRADO (20/07/2026 — con evidencia de producción).**
> El **prompt #8** bajó la guardia de resolución a **precondición de `uploadImageToGithub`** (`MainViewModel.kt:362`), o sea **debajo de la UI**: una ruta nueva ya no puede saltársela por olvido, que era el defecto de fondo (la guardia vivía en la pantalla y el share simplemente no la llamó). Además el origen viaja al mensaje de commit (`GitRepository.kt:156`).
>
> **Verificación en producción:** las primeras **6 subidas** con el APK nuevo traen **las 2 señales** — sello `[gallery …]` y **full-res**: `Upload image Look 85 {Standing, Back View, Seated, Side Profile, Ditzy} [gallery 669x1200]` y `Upload image Look 566 Standing [gallery 805x1200]`. **Cero miniaturas de 286×512.**
>
> **Sigue vigente:** las **1.701 históricas** son irrecuperables (la original solo existió en Gemini) y **auditar defectos finos sobre 286 px sigue siendo inútil** — comprobar resolución antes de auditar. Lo que cambió es que **la flota dejó de contaminarse hacia adelante**.

> [!CAUTION]
> **🔴 EL 40% DE LA FLOTA SON MINIATURAS (descubierto 14/07/2026 — daño histórico; ver el cierre del caso arriba).**
> **1.701 imágenes** están subidas a **~286×512 px (0,15 MP)**. Las sanas están en **1024×1024 (1,05 MP)** — **7× más píxeles**.
>
> **Causa:** la Ama copia la imagen en Gemini con **"Copiar"** y la pega en la app. Pero Android **limita el tamaño del portapapeles**: cuando una app copia una imagen, deja un **preview reducido**, no el original. La app (`PromptFilterScreen.kt`, la rama `clipboard.primaryClip → item.uri → BitmapFactory.decodeStream`) lee ese preview fielmente y sube la miniatura. **El código de resize de la app NO tiene la culpa** (su `maxDim=1200` solo achica lo que es *mayor* a 1200).
>
> **✅ FLUJO CORRECTO (sin tocar código):**
> 1. En Gemini: **"Descargar" / "Guardar imagen"** — NUNCA "Copiar".
> 2. En la app: el **selector de galería** (lee el archivo real) — NUNCA el botón de pegar.
>
> **Consecuencia para las auditorías:** revisar defectos finos (puntera del zapato, piercing marcado sobre la tela, costura de la media) **sobre una miniatura de 286 px es inútil**. Antes de auditar, comprobar la resolución: `Image.open(f).size`. Si es <0,3 MP, lo que no se ve puede ser falta de píxeles, no ausencia de defecto.
>
> El daño ya hecho es **irrecuperable** (la original solo existió en Gemini): recuperar = regenerar.

> [!WARNING]
> La generación masiva se pausa por límite de cuota de la API (429 Too Many Requests).

---

Desde L291, las imágenes ya NO las genera/mueve el agente: la **app Android de la Ama** genera en Gemini (más cuota, más rápido) y sube los PNG directamente al repo en GitHub. El agente las **encuentra ya commiteadas tras `git pull`**. Flujo de sincronización al detectar imágenes nuevas:

1. `git pull` — traer las imágenes que subió la app.
2. `python 99_Sistema/scripts/visual/sync_imagenes_subidas.py` — normaliza los nombres no-canónicos de la app (`ele_<N>_back.png`→`ele_<N>_back_view.png`, `ele_<N>_profile.png`→`ele_<N>_side_profile.png`) y regenera el tracker `### 📸 Imágenes (N/7)` en `galeria_outfits.md` SOLO para looks ≥ 291 cuya sección esté en "Pendiente"/"parcial". **Es idempotente y NO toca el fleet histórico** (<291, que usa nombres timestamped/curados a mano).
3. `python 99_Sistema/scripts/visual/update_galleries.py` — regenera los README de cada carpeta + galería maestra (mapea poses por nombre canónico).
4. Commit + push.

⚠️ La app nombra `back`/`profile`; el canon usa `back_view`/`side_profile`. La normalización del paso 2 es obligatoria o las poses se mapean mal en la galería maestra.

> 🔴 **17/08/2026 — LA APP SIGUE SUBIENDO EL SLOT 5 COMO `ditzy` EN ANAÏS Y MISS DOLL.** La sesión del 16/08 reportó *"normalizado el selector de poses en LV-App para respetar las 7 poses canónicas por personaje (Slot 5: Sovereign Gaze para Anaïs, Glacial Command para Miss Doll)"*. **El artefacto lo desmiente:** todo lo subido desde entonces llegó como `anais_0NN_ditzy.png` y `miss_doll_0NN_ditzy.png` — **14 archivos** (Anaïs L15/L16/L20/L23/L25 · Miss Doll L12/L14/L15-L20/L25).
>
> **Por qué importa y no es cosmético:** `update_galleries.py` arma la galería maestra de Anaïs con la columna `sovereign_gaze` (línea 428). Un archivo `_ditzy` cae en otro bucket y **la imagen desaparece de la tabla del look**. No es un nombre feo, es una foto invisible.
>
> **Repo-side ya corregido** (14 `git mv` a `_sovereign_gaze` / `_glacial_command`, precedente del 15/08). **App-side pendiente:** mientras `LV-App` siga ofreciendo "Ditzy" en el slot 5 de estas dos, el próximo batch vuelve a llegar mal y hay que renombrar de nuevo. Es otro repo — decisión de la Ama.

> 🧮 **El tracker `### 📸 Imágenes (N/7)` de Anaïs y Miss Doll ya NO se mantiene a mano (17/08/2026).** `update_galleries.py` nunca lo tocó — por eso envejecía mintiendo (13/08: 0/7 en 13 de 14 looks con 52 imágenes en el índice; 17/08: **33 looks** desfasados, con L15-L25 en "0/7 — Pendiente" y 60 imágenes reales). Herramienta nueva: `python 99_Sistema/scripts/visual/sync_tracker_galeria_personaje.py [anais|miss_doll] [--dry-run]` — mide contra `git ls-files` (nunca el disco: los PNG llevan skip-worktree), preserva anotaciones humanas dentro de las celdas y no pisa encabezados con nota propia (los reporta). Correrlo después de `sync_imagenes_subidas.py` y antes de `update_galleries.py`.

> 👙 **LOOK 812 — defecto de texto encontrado y corregido 28/08/2026, pero 3/7 poses YA MATERIALIZADAS lo arrastran.** Auditando el batch L808-L812 recién llegado por pull contra el canon de calzado (`identidad_ele.md` §II, directiva mule 09/07/2026) encontré que las 7 poses declaraban `pointed-toe mule stiletto sandals... 12cm thin pin stiletto heel` **sin plataforma** — Look 812 es Lencería, así que el mule está permitido en el arquetipo, pero la regla exige `platform mule ≥4" (~10cm)` siempre; un mule fino sin plataforma es la misma violación que un mule fuera de Lencería. Corregido en texto (replace_all a `platform mule stiletto sandals... 12cm thin pin stiletto heel plus 4-inch platform`) antes de que la app generara las 4 poses que faltaban.
> **Pero el `sync_imagenes_subidas.py` de la misma sesión reveló que 3 poses (Standing, Seated, Back View) ya estaban materializadas** con el texto viejo — inspeccionadas a 0,80 MP (669×1200, sobre el piso de validez): confirman el defecto exacto (mule sin plataforma visible, punta abierta en vez de la `pointed almond toe` cerrada que pedía el propio prompt) y además el busto sale **notoriamente por debajo del ADN** (`massive 1000cc... perfectly spherical... obviously fake gravity-defying shape`) — se ve un busto grande pero orgánico/realista, no la forma esférica exagerada exigida en las tres poses. El tatuaje rúnico de cadera sí aparece correcto (visible en Back View, piel desnuda). **Regenerar Standing, Seated y Back View de L812 una vez que la Ama vuelva a pasar por la app** — el texto que usará ahora ya trae la plataforma; el hueco del busto es defecto de generación, no de texto (el token ya pedía la forma correcta), así que puede repetirse aunque el texto esté bien.

## 👠 ESTADÍSTICAS DE ELE (FLOTA PRINCIPAL)

| Categoría | Valor | Estado |
|-----------|-------|--------|
| **Flota / batches diseñados** | → `00_Ele/memoria_sesiones.md` (ESTADO ACTUAL, dueño único) | 🔢 Puntero |
| **Canon ADN (tatuaje, busto, etc.)** | → `00_Ele/identidad_ele.md` §II + Bloque A | 🔢 Puntero |
| **Reparaciones del motor de poses** | historial → bitácora + auto-memoria (`feedback_pov_retrato_ig_no_literal`, `feedback_gemini_safe_poses`, `feedback_anti_3_piernas_poses`, `feedback_medias_calzado_reglas`) | ✅ Blindado |
| **Materialización L441-L470 (parcial vía app)** | 7/7: **L443, L445, L458, L460, L461** · 5-6/7: L444, L446, L457, L459 · resto solo standing · L471-490 0/7 | 🟡 En curso vía app |
| **Materialización L735-L750 (parcial vía app)** | L735-L742 materializados parcialmente (40 imgs). L743-L750 pendientes | 🟡 En curso vía app |
| **Legado (Looks 01-100)** | **100/100** | ✅ Completo |
| **Balance Mix (Auditoría)** | **100%** | ✅ Flota Base |

> 👙 **LOOK 801 — auditado 13/08/2026 (1,06 MP, sobre el piso de validez).** Tracker corregido de **1/7 a 4/7** contra `git ls-files`; y la memoria decía *«Ditzy materializada»* — **es falso**, ese archivo no existe: lo que hay es `side_profile`.
> - 🔴 **Back View:** calzón de talle alto cubriendo el asiento entero (defecto que levantó la Ama). **Causa de texto:** el BLOQUE B decía `micro bikini bottoms` — prenda y material, **nunca el corte**. De ahí nace el ancla `BOTTOM_CUT_LOCK`.
> - 🔴 **Side Profile:** **otro outfit completo** — PVC blanco con ribete rojo + minifalda + medias de red (contra un `no stockings` explícito) + plataforma negra en vez de acrílico transparente + escenario equivocado. Viola además medias + punta abierta (regla 04 §1).
> - ⚙️ **Causa raíz de proceso:** el look **se escribió a mano** (`generar_look801.py`) en vez de ensamblarse con `prompt_builder.py`, y sus 4 poses materializadas salieron **sin `GARMENT_CONSISTENCY`, sin `PHOTOREAL_LOCK` y sin ancla de orientación**. `GARMENT_CONSISTENCY` es exactamente el ancla que impide que la prenda se re-estilice entre tomas. **Todo look nuevo se ensambla con el motor** — es la lección, no el parche.
> - ⏳ **Regenerar 5:** Back View · Side Profile · Ditzy · POV · Odalisque. Standing y Seated quedan válidas. Las 7 poses ya están en 0 anclas faltantes.
>
> 🔬 **RE-AUDITADO 17/08/2026 — ahora 7/7 en disco, y las 3 nuevas salieron BIEN.** Tracker corregido de 4/7 a **7/7** (`sync_imagenes_subidas.py`; las tres llegaron el mismo 13/08 y el contador nunca se movió). Auditadas las 7 a 0,80-1,06 MP → `99_Sistema/auditoria_visual_ele_missdoll_20260817.md`.
> - ✅ **Ditzy, POV y Odalisque quedaron correctas** — son las que se pidieron después, con el texto ya corregido. La regeneración pendiente baja de 5 a **2**.
> - 🔴 **Back View sigue mal** y suma un defecto que la auditoría del 13/08 no vio: **tatuajes bajando hasta manos y dedos**, contra el `no tattoos and no glyphs` explícito sobre manos/dedos del propio prompt. Más el escenario cambiado a baño con tina y estante BDSM.
> - 🔴 **Side Profile confirmado como el peor de la flota reciente:** ocho violaciones simultáneas (PVC con ribete rojo, minifalda, medias de red contra `no stockings`, plataforma negra contra acrílico transparente, cofia agregada, estudio victoriano, brazos sin tatuajes, cara distinta).
> - 🟡 **Deriva entre poses del mismo look:** cruz roja inventada **solo** en Seated · busto que baja de tamaño en Seated y Odalisque · pelo que oscila de cereza a rojo brillante. El **token de calzado aguantó en 6 de 7**.
> - ⚠️ **Antes de regenerar: reensamblar los 7 prompts con `prompt_builder.py`.** Regenerar sobre el texto escrito a mano repite el defecto.

> ✅ **RESUELTO 15/08/2026 — Nombrado canónico LV-App completado.** Las 10 imágenes de Miss Doll fueron renombradas a `miss_doll_<N>_glacial_command.png` y las de Anaïs a `anais_<N>_sovereign_gaze.png` / `anais_L<NN>_...` para Boudoir, alineando 100% las carpetas en disco, las tablas markdown y el contrato de LV-App (`CharacterProfile.kt` y `GitRepository.kt`). Se eliminaron las versiones duplicadas obsoletas.

### 🛠️ Estado por look

> El estado real por look vive en la **galería** y los README de `05_Imagenes/` (los mantiene el bot / `update_galleries.py`) y en el tracker `### 📸 Imágenes (N/7)` de `galeria_outfits.md`. Esta sección dejó de duplicarlos (poda dueño-único 02/07/2026).

---

## 🌹 ESTADÍSTICAS DE ANAÏS BELLAND

| Categoría | Valor | Estado |
|-----------|-------|--------|
| **Galería viva** | **Look 01-40 · 280 prompts** (batches: Reset L01-L14 11/08 · Ampliación L15-L20 16/08 · Ampliación II L21-L25 17/08 · L26-L35 diseñados sin fecha registrada · Flota V L36-L40 20/08) | 🟢 Activo |
| **Materializados** | **273/280** (97,5% · medido **23/08/2026** sobre `sync_tracker_galeria_personaje.py` → `git ls-files`): **39/40 looks en 7/7** · **solo L40 sin empezar (0/7)** | 🟢 Casi completo |
| **Legacy (Looks 1-40, canon anterior)** | `archivo_legacy_anais_v1.md` — museo, sin retrofit. Imágenes en `05_Imagenes/anais/_ARCHIVO_LEGACY_V1/legacy_look*/` | 🗄️ Archivado |
| **Boudoir** | 6 (L01-L06), serie aparte con su propia numeración | 🟢 |

> 🩹 **Corrección 12/08/2026 — las 98 poses se estaban pidiendo SIN negativo.** Los 14 looks nuevos no tenían `Ubicacion`, ni `Tags`, ni la etiqueta `**Negative Prompt:**` que es la única que el parser de la app reconoce. **Las 50 imágenes ya materializadas se generaron así.** Agregados los tres campos, el tracker `### 📸` medido contra el índice de git (antes decía 0/7 en los 14 looks, con 50 imágenes en el repo) y las anclas anti-defecto en los 98 prompts.
>
> ⚠️ La línea de arriba decía **"40 planificados, materializados sin verificar"** — dato de antes del reset del 11/08. La numeración vive ahora entre Look 01 y Look 14.
>
> 🔍 **AUDITORÍA VISUAL 12/08/2026 → `99_Sistema/auditoria_visual_anais_20260812.md`.** 26 de las 50 imágenes inspeccionadas contra su prompt (resolución 0,8 MP, por encima del piso de validez). **Causa raíz única, de texto:** el BLOQUE B se abreviaba por pose — Standing llevaba 81-100% y el resto 7-39%, y **65 de 98 prompts no nombraban el calzado**. De ahí salen las desviaciones fotografiadas (cierre del catsuit que desaparece, zapato que cambia de color, broche que se esfuma, kimono con dragones inventados). **Corregido el mismo día: los 98 prompts llevan el BLOQUE B completo, cobertura mínima 100%.**
>
> 🎥 **Segundo hallazgo, levantado por la Ama sobre la app:** *"las imágenes de ditzy salen casi todas iguales"*. Medido: el texto de pose+setting era **87% idéntico en POV, 78% en Side Profile, 59% en Sovereign Gaze y 57% en Back View** entre los 14 looks, con tres tríos de prompts idénticos carácter por carácter. Causa: el perfil mandaba rotar el encuadre pero **no existía repertorio del cual rotar**. Creado `02_Personajes/01_Principales/anais/repertorio_camara_anais.md` (7 variaciones por slot + escenario específico por look + 4 anclas de prenda); la similitud bajó a **9-13%**. Aparte: el **Ditzy del L08 salió en cuerpo entero** por no tener el recorte `chest up` anclado.
>
> ⏳ **11 poses recomendadas para regenerar** (prompts ya corregidos): L01 Seated/POV/Odalisque · L03 Seated/Side/Odalisque · L08 Sovereign Gaze · L12 Side Profile · L13 Standing/Back View · L14 Seated. Y vale la pena rehacer slot 5 + POV de los 8 looks materializados: sus imágenes son casi la misma foto.
>
> 🔥 **14/08/2026 — LOS 98 PROMPTS SE REESCRIBIERON POR SENSUALIDAD. La lista de arriba queda AMPLIADA: ahora vale la pena regenerar todo el set, no 11 poses.**
> La Ama levantó *«la ropa interior es muy de señora, sin gracia»* y *«el entorno no es sensual»*. Medido sobre los 98 antes de tocar: `balconette` ×21 y **ningún otro sujetador** · `Brazilian-cut brief` **4 de 4** · **corsetería 0** · liguero **9/98** (canon §86: imprescindible) · «Tensión Textil» **0** y «Manos Nunca Inactivas» **2** · **547 muebles contra 0 huella de cuerpo, 0 atmósfera y 0 luz sobre la piel**.
> **Tres anclas nuevas en los 98** (`anclas_universales.json` v2.4): **`LEG_CUT_LOCK`** · **`SENSUAL_STATE`** · **`LIVED_IN_ROOM`**. Más biblioteca de 10 arquitecturas de lencería (perfil §5.6), liguero de 6 tirantes inyectado en L01/L05/L07, y el Look 11 corregido de pantalón a pencil skirt.
> **Orden de regeneración recomendado: L02 · L08 · L09 · L10** (Boudoir — es donde las tres anclas pegan más fuerte), después el resto. Linter: **CRÍTICOS 0**.
> 🖤 El **catsuit quedó autorizado** (Ama 14/08) pero **ningún look lo usa todavía** — es diseño nuevo, no regeneración.
> ✅ **CERRADO 17/08/2026 — el desajuste `anais_L02_standing.png` vs `anais_2_standing.png` ya no existe.** La nota decía "falta decisión de la Ama"; medido contra `git ls-files`, el duplicado no canónico se borró en el commit `accc5649f` («Alineacion canonica de imagenes... segun contrato de LV-App»). `look2_rosa_y_latex/` tiene hoy 7 archivos, uno por pose. *Otro estado que envejeció hacia la mentira: se escribió una vez y nunca se volvió a medir.*
>
> ✅ **El Odalisque apaisado (1200×669) NO es defecto — la Ama lo pide así a Gemini** porque la figura reclinada se aprecia mejor en horizontal (12/08/2026). Es el único slot horizontal de su set, es deliberado y **ninguna auditoría futura debe marcarlo.** En canon: `anais.md` §4.

> **🔎 Auditoría de `galeria_looks_anais.md` (10/08/2026):** el dato "21 planificados" estaba obsoleto — el archivo real llega al Look 40. Se encontraron y corrigieron dos huecos reales:
> - **13 looks (22-34) tenían solo 1 de sus 4 prompts escritos** (Standing/Seated/Side Profile/Sovereign Gaze) — 38 prompts faltantes, completados el 10/08/2026 siguiendo el estilo ya establecido en cada look (mismo ADN + BLOQUE B, acción nueva por pose).
> - **Los números Look 12, 13, 14, 19, 20, 21 nunca se crearon** (ni como header) — hueco real, pendiente agendar su diseño en un próximo batch de Anaïs (no confundir con la serie Boudoir L01-L06, que es aparte y está completa).

---

## 🎀 ESTADÍSTICAS DE MISS DOLL (rediseño 11/08/2026)

> 🔎 **Corrección de estado (11/08/2026):** esta sección decía "V5.0, 5 looks disponibles, L01-L03 materializados" — al auditar la galería real (`GALERIA_OUTFITS_MISS_DOLL.md`) se encontraron **26 looks / ~182 prompts bajo canon V3.5**, no 5. El dato viejo estaba desactualizado (ver `feedback_app_verificar_codigo_real` — no confiar en el reporte). Corregido con la medición real.

| Categoría | Valor | Estado |
|-----------|-------|--------|
| **Canon Activo** | **Rediseño 11/08/2026** (rostro ovalado + cuerpo gym + materiales suaves + corsé opcional) | ✅ Vigente |
| **Legacy (canon V3.5, pre-11/08)** | **26 looks / ~182 prompts** | 🗄️ Archivado en `ARCHIVO_LEGACY_MISS_DOLL_V35_GALERIA.md` (+ `..._PROMPTS.md`, ex `OUTFITS_MISS_DOLL.md`). Imágenes movidas a `05_Imagenes/miss_doll/_ARCHIVO_LEGACY_V35/legacy_look*/`. **Renombrados 11/08 para salir del filtro de LV-App** — ver `.agent/rules/11-contrato-galeria.md` §9bis |
| **Looks bajo canon nuevo** | **40** (Look 01-40, rotación de los 8 arquetipos) · **280 prompts** | 🟢 **275/280** (98,2% · medido **23/08/2026** sobre `sync_tracker_galeria_personaje.py` → `git ls-files`): **39/40 looks en 7/7** · **solo L36 parcial (2/7)** |
| **Arquetipos** | **8** desde el 13/08/2026 — entra **👙 Bikini / Lencería Erótica al 15%** (Ama), con las siete metas anteriores prorrateadas y frontera escrita contra VIP/Privado. Dueño único: `02_Personajes/_perfiles_visuales/miss_doll.md` §6 | 🆕 |
| **Estado Actual** | Prompts listos (280/280) y verificados contra el parser de la app (0 críticos). Batch L31-L35 incorporado el 19/08/2026, batch L36-L40 ("Flota V") incorporado el 20/08/2026. L22 completado al 7/7 con pose Odalisque cenital. | 🟢 |

> 🩹 **Corrección 12/08/2026 — los 98 prompts NO eran generables.** Estaban escritos con la notación del motor **literal** (`[BLOQUE A] + [BLOQUE B], …, [BLOQUE C setting]`), sin `Ubicacion`, sin `Tags` y con el negativo bajo una etiqueta que el parser de LV-App no reconoce. Medición sobre el archivo commiteado, parseándolo con el mismo algoritmo que la app: **98/98 con placeholder · 0/14 looks con negativo · 0/14 con ubicación**. Reescritos expandidos + anclas anti-defecto + contrato de archivo (regla 11 §9ter). Verificable: `python 99_Sistema/scripts/visual/lint_prompts_personaje.py miss_doll`.
>
> ⚠️ La línea de arriba decía **"1 look (Look 01)"** — quedó congelada tras la primera tanda del 11/08 mientras se generaban 13 looks más. Otro estado que envejeció hacia la mentira. *(Volvió a pasar: el 12/08 decía "6/98" con 44 ya subidas.)*
>
> 🔍 **AUDITORÍA VISUAL 13/08/2026 → `99_Sistema/auditoria_visual_miss_doll_20260813.md`.** Las 8 imágenes nuevas del pull (Look 07 completo + Look 08 Standing) inspeccionadas contra su prompt, con recorte ampliado ×3-×5 en cada duda. Resolución 0,80-0,97 MP, sobre el piso de validez. **La causa raíz de Anaïs NO aplica:** la cobertura del BLOQUE B es **100% en las 98** y el linter da `CRITICOS: 0` — el texto está bien y la prenda deriva igual.
>
> **El patrón nuevo es la asimetría:** el `architectural asymmetric one-shoulder` del Look 07 se pierde en **3 de 7 poses**, siempre en las que el torso gira o se recorta (Back View → strapless · Side Profile → dos tiras + lace-up inventado en la espalda · POV → V simétrico). `GARMENT_CONSISTENCY` nombra escote, manga, ruedo, corte y color, **pero no la asimetría ni el lado** → no la protege. Fix propuesto: ancla **`ASYMMETRY_LOCK`** en `anclas_universales.json` (no existe entre las 16 actuales), nombrando **qué hombro va desnudo**. Sin ella, regenerar el Look 07 repite la deriva.
>
> **Otros hallazgos:** Look 07 Odalisque salió con **dos cuffs cromados** (el BLOQUE B pide uno solo) · **Look 08 Standing salió como render 3D**, no fotografía (piel sin poros, luz de videojuego) contra `editorial realistic human skin texture` y el negative `plastic mannequin skin, doll face` — única de las 8 así, conviene regenerarla **antes** de que la app siga con sus 6 poses restantes. **⏳ 5 poses recomendadas para regenerar:** L07 Back View · Side Profile · POV · Odalisque · L08 Standing. Más el L04 Back View heredado del 12/08.
>
> ✅ **Cerrados sin marcar:** botas knee-high del L08 (correctas, ampliadas antes de afirmarlo) · Odalisque apaisado 1200×669 (mismo criterio deliberado que la Ama fijó para Anaïs el 12/08) · **destello ✦ de Gemini** abajo a la derecha — es marca de agua de **toda** la flota (está también en L01/L03/L05/L14), no regresión de este batch. Importa solo para RRSS: es visible sobre fondo claro.
>
> 🔴 **CORRECCIÓN del mismo 13/08 — la primera medición estaba mal planteada.** Medí **pose + setting juntos** (10-28% por slot) y concluí que Miss Doll no tenía el problema de Anaïs. **Es falso.** Lo que varía es el **escenario**; eso arrastraba el número y escondía que la pose se repite. Medida la **cláusula de pose sola** (sin anclas, sin setting): **Standing 68% · Side Profile 70% · Odalisque 54% · Seated 53% · POV 52% · Back View 41% · Glacial Command 21%**. En 4 de 5 Standing muestreados la pose es la misma —`contrapposto, weight shifted onto one hip`— cambiando solo el adjetivo. **El único slot sano (21%) es el único con repertorio escrito**, y `repertorio_camara_miss_doll.md` ya lo decía en su §PENDIENTE. ⏳ Faltan los repertorios de **Standing, Back View, Seated, Side Profile y Odalisque** (referencia: el motor de Ele lleva **51 sub-poses** en código con rotación automática). **Lección de método: una métrica que mezcla dos variables mide la que más se mueve, no la que se está auditando.**
>
> 🧹 **Dos arreglos de repo hechos el 13/08:** (1) el tracker `### 📸 Imágenes (N/7)` decía **0/7 en 13 de los 14 looks** con 52 imágenes reales en el índice — corregido contra `git ls-files`, con tabla enlazada donde hay archivo (`update_galleries.py` **no** toca este tracker: es manual y por eso envejece). (2) La nota de auditoría del 12/08 en el Look 04 llevaba el nombre del archivo **entre backticks**, y el parser de LV-App lo tomaba como prompt inline del slot Back View (25 chars) — el `REPLACE` lo salvaba, pero era frágil. Backticks fuera; el linter pasó de **7 avisos a 0**.

---

## 🔄 PROTOCOLO DE ACTUALIZACIÓN
1. **POST-GENERACIÓN:** Tras materializar un set (5-7 poses), actualizar el contador en este archivo.
2. **POST-SYNC:** Tras ejecutar `update_galleries.py`, verificar que los números coincidan con la realidad física del disco.
3. **NOTIFICACIÓN:** Informar a la Ama sobre el nuevo porcentaje de completitud.
