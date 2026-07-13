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

> [!CAUTION]
> **🔴 PENDIENTE #1 — LOS PROMPTS SIGUEN FOSILIZADOS RESPECTO AL BLINDAJE DEL 13/07 (diferido por la Ama).**
> El blindaje del 13/07 (`SKIN_LOCK`, `build_negative()`, costura por primacía, `HOSIERY_LOCK`, odalisca anti-percha) vive en el **motor** (`pose_rotation_v5.py`) — pero **la app genera desde `galeria_outfits.md`**, y ahí los prompts todavía traen:
> - el **Bloque A viejo** (`nipple piercings pressing against and visible under clothing` → pinta los piercings/tatuajes **a través de la tela**);
> - **cero bloque negativo** desde el **L711** (191 bloques para 400 looks: el último es el L710 → **60 looks / 420 poses** generadas con el negative vacío);
> - sin `SKIN_LOCK` ni `HOSIERY_LOCK`.
>
> **Hasta que se barran, lo que se genere sigue saliendo con el defecto y quema cuota.** Alcance del barrido: **todas las poses SIN imagen** (rango 300+ en materialización + L766-L770). Las que ya tienen imagen no se tocan.

> [!NOTE]
> **⚠️ Auditar el repo MIENTE (aprendido 13/07):** las imágenes commiteadas son las **sobrevivientes** de varios reintentos de la Ama — miden su tasa de éxito *después* del filtro humano, no la del prompt. Si la Ama dice que tuvo que regenerar, **el defecto existe** aunque lo guardado se vea limpio.

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
