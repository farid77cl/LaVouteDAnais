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

> [!CAUTION]
> **🔴 PENDIENTE #1 — LOS PROMPTS 300-760 SIGUEN FOSILIZADOS (diferido por la Ama).**
> El motor está en **v3 (15/07 tarde: `build_marks_clause()` — el segmento de marcas del Bloque A se construye por cobertura, lo cubierto NO se nombra, nipple piercings JAMÁS — + `SINGLE_FRAME` v3 anti-espejo/marco + `SINGLE_FRAME_TAIL` en Ditzy + `NO_ARMWEAR` afirmativo-primero)**. En galería: **L793 ×7 + L794 Odalisque en v3** (los únicos sin imagen del batch); el resto de **L771-L800 en v2** (refresco 15/07: 104 poses + 17 negatives). Pero **la app genera desde `galeria_outfits.md`**, y el rango **300-760** todavía trae:
> - el **Bloque A viejo** (`nipple piercings pressing against and visible under clothing`);
> - los **locks v1 con metalenguaje multi-toma** ("across all poses / in every shot" → riesgo de collage);
> - sin `SKIN_LOCK`/`HOSIERY_LOCK`/`SINGLE_FRAME`. (El bloque negativo sí existe ya en los 591 looks — reparado 14/07 — pero es v1.)
>
> **Hasta que se barran, lo que se genere en ese rango sigue saliendo con el defecto y quema cuota.** Alcance del barrido: **todas las poses SIN imagen** del rango 300-760. Las que ya tienen imagen no se tocan.

> [!NOTE]
> **⚠️ Auditar el repo MIENTE (aprendido 13/07):** las imágenes commiteadas son las **sobrevivientes** de varios reintentos de la Ama — miden su tasa de éxito *después* del filtro humano, no la del prompt. Si la Ama dice que tuvo que regenerar, **el defecto existe** aunque lo guardado se vea limpio.

> [!CAUTION]
> **🔴 EL 40% DE LA FLOTA SON MINIATURAS (descubierto 14/07/2026).**
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
| **Total Looks Planificados** | **21** | 🟢 Activo |
| **Materializados (100%)** | **4** | 🔴 19.0% |
| **Pendientes de Generación** | **17** | 🟡 Batch 05-21 |

---

## 🎀 ESTADÍSTICAS DE MISS DOLL (V5.0)

| Categoría | Valor | Estado |
|-----------|-------|--------|
| **Canon Activo** | **V5.0 Realismo Couture** | ✅ Validado |
| **Looks Disponibles** | **5** | 🟢 Activo |
| **Materializados** | **3.0** | ✅ L01-L03 (100%) |
| **Estado Actual** | **Listo L04** | 🟢 Preparada para Batch Zero |

---

## 🔄 PROTOCOLO DE ACTUALIZACIÓN
1. **POST-GENERACIÓN:** Tras materializar un set (5-7 poses), actualizar el contador en este archivo.
2. **POST-SYNC:** Tras ejecutar `update_galleries.py`, verificar que los números coincidan con la realidad física del disco.
3. **NOTIFICACIÓN:** Informar a la Ama sobre el nuevo porcentaje de completitud.
