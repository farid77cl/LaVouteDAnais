# 📊 ESTADO DE MATERIALIZACIÓN Y ESTADÍSTICAS (V3.12)

Este documento es el registro de "memoria viva" sobre el progreso visual del repositorio. Debe ser consultado antes de cada Batch y actualizado después de cada sincronización exitosa (Última actualización: 02/07/2026 — poda dueño-único).

## 📱 FLUJO DE IMÁGENES SUBIDAS POR LA APP (Gemini → GitHub) — era app, looks ≥ 291

## Auditoría 25 de Junio 2026 (Looks 200 a 300)
- **Rango analizado:** `look200_*` a `look300_*`
- **Total de prompts registrados (L200-L300):** 338
- **Imágenes esperadas (4 poses por look aprox + extras):** 338
- **Total imágenes encontradas físicamente:** 281
- **Imágenes materializadas recientemente:** L313 y L314 completos. **L315 y L316 quedan 6/7** — sus POV se purgaron (salieron *selfie literal*, violando el canon POV) y esperan regeneración con el prompt ya corregido.
- **Faltantes reales restantes:** En avance progresivo sobre déficit L317-L400.
- **🐍 Batch L761-L770 «Veneno Tropical»:** la app lo está materializando — **L761, L762, L763 y L765 completos (7/7)** · **L764 6/7** (falta Standing) · **L766 2/7** · **L767-L770 sin empezar**.

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

### 🛠️ Estado por look

> El estado real por look vive en la **galería** y los README de `05_Imagenes/` (los mantiene el bot / `update_galleries.py`) y en el tracker `### 📸 Imágenes (N/7)` de `galeria_outfits.md`. Esta sección dejó de duplicarlos (poda dueño-único 02/07/2026).

---

## 🌹 ESTADÍSTICAS DE ANAÏS BELLAND

| Categoría | Valor | Estado |
|-----------|-------|--------|
| **Total Looks Planificados** | **40** (numeración real hasta Look 40) + **6 Boudoir** (L01-L06) | 🟢 Activo |
| **Materializados** | Sin verificar desde esta máquina (literaria, 0 PNG en disco) | ⚠️ Verificar en máquina visual |
| **Pendientes de Generación** | Ver detalle abajo | 🟡 |

> **🔎 Auditoría de `galeria_looks_anais.md` (10/08/2026):** el dato "21 planificados" estaba obsoleto — el archivo real llega al Look 40. Se encontraron y corrigieron dos huecos reales:
> - **13 looks (22-34) tenían solo 1 de sus 4 prompts escritos** (Standing/Seated/Side Profile/Sovereign Gaze) — 38 prompts faltantes, completados el 10/08/2026 siguiendo el estilo ya establecido en cada look (mismo ADN + BLOQUE B, acción nueva por pose).
> - **Los números Look 12, 13, 14, 19, 20, 21 nunca se crearon** (ni como header) — hueco real, pendiente agendar su diseño en un próximo batch de Anaïs (no confundir con la serie Boudoir L01-L06, que es aparte y está completa).

---

## 🎀 ESTADÍSTICAS DE MISS DOLL (rediseño 11/08/2026)

> 🔎 **Corrección de estado (11/08/2026):** esta sección decía "V5.0, 5 looks disponibles, L01-L03 materializados" — al auditar la galería real (`GALERIA_OUTFITS_MISS_DOLL.md`) se encontraron **26 looks / ~182 prompts bajo canon V3.5**, no 5. El dato viejo estaba desactualizado (ver `feedback_app_verificar_codigo_real` — no confiar en el reporte). Corregido con la medición real.

| Categoría | Valor | Estado |
|-----------|-------|--------|
| **Canon Activo** | **Rediseño 11/08/2026** (rostro ovalado + cuerpo gym + materiales suaves + corsé opcional) | ✅ Vigente |
| **Legacy (canon V3.5, pre-11/08)** | **26 looks / ~182 prompts** | 🗄️ Archivado en `GALERIA_OUTFITS_MISS_DOLL_ARCHIVO_LEGACY.md` — imágenes ya generadas quedan como material histórico, no se regeneran automáticamente |
| **Looks bajo canon nuevo** | **1** (Look 01 — Neon Pink Cage, Club/Escenario) | 🟡 Prompts escritos (7/7), 0/7 materializados |
| **Estado Actual** | Listo para generar Look 01 vía app; próximos looks se agregan on-demand, mismo ritmo que Ele/Anaïs (no se regenera todo el roster legacy de una vez) | 🟢 |

---

## 🔄 PROTOCOLO DE ACTUALIZACIÓN
1. **POST-GENERACIÓN:** Tras materializar un set (5-7 poses), actualizar el contador en este archivo.
2. **POST-SYNC:** Tras ejecutar `update_galleries.py`, verificar que los números coincidan con la realidad física del disco.
3. **NOTIFICACIÓN:** Informar a la Ama sobre el nuevo porcentaje de completitud.
