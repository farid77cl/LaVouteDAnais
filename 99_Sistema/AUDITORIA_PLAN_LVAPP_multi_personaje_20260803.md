# Auditoría + Plan — LV-App v1 multi-personaje (Miss Doll + Anaïs)

> **Fecha:** 2026-08-03 · **Autor:** Ele (orquestadora) · **Estado:** PLAN listo, pendiente de Gate de la Ama.
> **Repo de la app:** `github.com/farid77cl/LV-App` (código Kotlin/Jetpack Compose). NO vive en este repo.
> **Repo de contenido que la app lee/escribe:** `farid77cl/LaVouteDAnais` (este).
> **Método:** auditoría sobre clon real (`git clone --depth 1`), evidencia con archivo:línea. La app NO genera imágenes: es visor + copiador de prompts + uploader de PNG a GitHub.

---

## 1 · Hallazgos con evidencia

### H1 — El filtro de descubrimiento es Ele-céntrico y **case-sensitive** → ni Miss Doll ni Anaïs entran
`GitRepository.kt:299-306`:
```kotlin
val markdownFiles = treeResponse.tree.filter { entry ->
    entry.type == "blob" && entry.path.endsWith(".md") &&
    (
        entry.path.contains("galeria_outfits") ||   // case-sensitive
        entry.path.startsWith("_batch_") ||
        entry.path.contains("/_batch_")
    ) && !entry.path.contains("galeria_index") && !entry.path.contains("report") && !entry.path.contains(".BKP")
}
```
- **Ele:** `00_Ele/galeria_outfits.md` ✅ y `00_Ele/galeria_outfits_archivo.md` ✅ (ambos contienen `galeria_outfits`).
- **Miss Doll:** `02_Personajes/01_Principales/miss_doll/GALERIA_OUTFITS_MISS_DOLL.md` → contiene `GALERIA_OUTFITS` en **mayúsculas**; `.contains("galeria_outfits")` en Kotlin es sensible a mayúsculas → **NO entra**. ❌
- **Anaïs:** `02_Personajes/01_Principales/anais/galeria_looks_anais.md` → el nombre es `galeria_looks_anais`, **no contiene** `galeria_outfits` → **NO entra**. ❌

Este es el bloqueo #1 y el más barato de arreglar.

### H2 — El tagging por personaje YA existe (medio cableado)
`GitRepository.kt:314-318`:
```kotlin
val sourceTag = when {
    fileEntry.path.contains("gotica", ignoreCase = true) -> "Era Gótica"
    fileEntry.path.contains("miss_doll", ignoreCase = true) -> "Miss Doll"
    fileEntry.path.contains("anais", ignoreCase = true) -> "Anaïs"
    else -> "Ele"
}
```
La app ya sabe distinguir el personaje por la ruta y lo guarda como `sourceTag`/tag del look. **Lo que falta es que los archivos lleguen hasta acá** (los frena H1) y que el resto del pipeline (poses + subida) respete ese personaje.

### H3 — El uploader hardcodea prefijo `ele_` y carpeta `05_Imagenes/ele/`
`GitRepository.kt:134-142`:
```kotlin
val path = existingPath ?: if (!existingParentFolder.isNullOrEmpty()) {
    "$dir/ele_${lookNumStr}_${formattedPose}.png"
} else if (!look.location.isNullOrEmpty()) {
    "$dir/ele_${lookNumStr}_${formattedPose}.png"
} else {
    "05_Imagenes/ele/look${lookNumStr}_${slug}/ele_${lookNumStr}_${formattedPose}.png"
}
```
- Respeta `existingParentFolder`/`look.location` si vienen en la ficha (útil), **pero fuerza el prefijo `ele_`** en el nombre de archivo en los tres ramos.
- El destino por defecto es `05_Imagenes/ele/…`.
- Miss Doll necesita `05_Imagenes/miss_doll/…` + `miss_doll_<N>_<pose>.png`; Anaïs necesita `05_Imagenes/anais/…` + `anais_look<NUM>_<pose>.png` (⚠️ el nombre de Anaïs lleva `look` embebido — inconsistente con Ele/MD).

### H4 — `PoseMatcher` conoce solo las 7 poses de Ele
`PoseMatcher.kt:4-32`:
```kotlin
val CANONICAL_POSES = listOf("Standing","Back View","Seated","Side Profile","Ditzy","POV","Odalisque")
// ALIAS_MAP: solo alias de esas 7
// strip de prefijo: Regex("^(ele|helena)_\\d+_") y Regex("^look0*\\d+_")
```
- El emparejado pose↔prompt en UI usa esto: `MainViewModel.kt:243` → `PoseMatcher.matches(pose, it.poseName)`.
- Poses de **Miss Doll** (5): `monarch_throne, hip_carry, pie_en_hombro, throne_suelo, caminata_circular` → no mapeadas.
- Poses de **Anaïs** (4): `command_standing, throne_seated, three_quarter, domina_closeup` (+ línea boudoir con slugs distintos: `boudoir_standing, chaise_seated, mirror_profile, intimate_closeup`) → no mapeadas.
- El strip `^look0*\d+_` ayuda parcialmente, pero sin alias por personaje el `formattedPose` de la subida sale mal.

### H5 — El parser de markdown es bastante genérico (buena noticia)
`parseMarkdown(content, source)` en `GitRepository.kt`: detecta encabezado de look por regex, poses por líneas `**…:**`, y captura los code blocks (```)  como prompt de la pose. Lee campos canónicos (`Ubicacion`, `Categoria`, `Tags`) y `location`. No asume las 7 poses al parsear — toma los nombres de pose que encuentre en los headers. **El nudo NO es el parseo del texto, es (a) el descubrimiento del archivo, (b) el mapeo de pose para la subida y (c) la ruta de subida.**

### H6 — Ordenamiento y fallback siguen siendo Ele-first
- `MainViewModel.kt:225`: `compareByDescending { it.tags.contains("Ele") }` — Ele flota arriba (cosmético, no bloquea).
- `GitRepository.kt:335`: el fallback por URL estática solo baja `00_Ele/galeria_outfits.md`.

---

## 2 · Modelo objetivo — "un perfil, muchos personajes" (dentro de la app)

Replicar en la app el patrón que ya rige el repo de contenido (motor agnóstico + perfil por personaje). Introducir un registro de datos, no ramas `if (ele/miss_doll/anais)` desparramadas:

```kotlin
data class CharacterProfile(
    val slug: String,             // "ele" | "miss_doll" | "anais"
    val displayName: String,      // "Ele" | "Miss Doll" | "Anaïs"
    val galleryPathContains: List<String>, // fragmentos de ruta (lowercase) que identifican sus galerías
    val imageFolder: String,      // "05_Imagenes/ele" | "…/miss_doll" | "…/anais"
    val filePrefix: String,       // "ele_" | "miss_doll_" | "anais_look"  (⚠ Anaïs lleva 'look')
    val poses: List<String>,      // nombres canónicos en orden
    val poseAliases: Map<String,String> // alias(lowercase) -> canónico
)
```
Registro (fuente única en la app):
| slug | galería (contains, lowercase) | carpeta imágenes | prefijo archivo | nº poses |
|---|---|---|---|---|
| `ele` | `galeria_outfits` | `05_Imagenes/ele` | `ele_` | 7 |
| `miss_doll` | `galeria_outfits_miss_doll` (case-insensitive) o `miss_doll` | `05_Imagenes/miss_doll` | `miss_doll_` | 5 |
| `anais` | `galeria_looks_anais` o `anais` | `05_Imagenes/anais` | `anais_look` | 4 (+4 boudoir, P2) |

Todo lo demás (descubrimiento, PoseMatcher, uploader) consulta este registro.

---

## 3 · Plan fásado

### P1 — Mínimo funcional (que las tres reciban y suban bien)
1. **Descubrimiento (H1):** ampliar el filtro de `GitRepository.kt:299-306` para incluir las tres galerías. Enfoque recomendado: iterar el registro `CharacterProfile` y aceptar el archivo si su ruta (en lowercase) contiene alguno de los `galleryPathContains`. Mantener las exclusiones (`galeria_index`, `report`, `.BKP`). Esto de una arregla mayúsculas de Miss Doll y el nombre distinto de Anaïs.
2. **Inferencia de personaje:** reutilizar/mover el `when` de H2 a `CharacterProfile.fromPath(path)`; el `else` sigue siendo Ele. Persistir el `slug` del personaje en `LookEntity`/`PromptEntity` (no solo el tag visible) para que la subida sepa a quién pertenece el look.
3. **PoseMatcher por personaje (H4):** parametrizar `getCanonicalPose`/`matches` con el `CharacterProfile` (o su `poseAliases` + lista de poses). Añadir alias y strip de prefijo para `miss_doll_`, `anais_` y la numeración `look\d+_`. Fallback: si no hay match, usar el nombre de pose crudo (ya normalizado) — nunca romper la subida.
4. **Ruta de subida por personaje (H3):** derivar carpeta y prefijo desde el `CharacterProfile` del look:
   - Ele → `05_Imagenes/ele/look<N>_<slug>/ele_<N>_<pose>.png` (igual que hoy).
   - Miss Doll → `05_Imagenes/miss_doll/look<NNN>_<tema>/miss_doll_<N>_<pose>.png`.
   - Anaïs → `05_Imagenes/anais/look<NUM>_<slug>/anais_look<NUM>_<pose>.png`.
   - Seguir respetando `look.location`/`existingParentFolder` cuando venga en la ficha, pero con el **prefijo del personaje**, no `ele_` fijo.
5. **Preservar** la guardia de resolución (>0.3 MP) y el sello `[gallery WxH]` del commit — no tocarlos.

**Criterio de aceptación P1:** con las tres galerías en el repo, la app lista looks de los tres personajes; al elegir un look de Miss Doll o Anaïs muestra sus 5/4 prompts correctamente emparejados a la pose; y al subir un PNG lo deja en la carpeta y con el nombre canónicos del personaje (verificable en el commit que genera la app).

### P2 — Mejoras
6. **UI selector de personaje** (recomendado: tabs Ele / Miss Doll / Anaïs, o filtro "Personaje" en `PromptFilterScreen.kt`). Hoy el tag existe pero no hay control dedicado; el orden Ele-first de `MainViewModel.kt:225` conviene volverlo neutral o por personaje activo.
7. **Miss Doll legacy `C-1..C-6.png`** (bandera §9 del perfil): decidir renombrado histórico vs convención solo hacia adelante — **decisión de la Ama** (§5).
8. **Línea Boudoir de Anaïs** (`L01…`, slugs de pose distintos, numeración no-entera): el parser guarda `number` como Int → `L01` no parsea. Requiere namespacing (personaje+línea) o un segundo set de poses. Dejar fuera de P1.
9. **Trackers N/N por personaje** (7/5/4) en las estadísticas de galería, si se muestran.

---

## 4 · Riesgos y casos borde
- **Case-sensitivity** (causa raíz de que Miss Doll sea invisible hoy): al ampliar el filtro, comparar siempre en lowercase.
- **No barrer archivos equivocados:** las exclusiones actuales (`galeria_index`/`report`/`.BKP`) deben mantenerse; el archivo de Ele `galeria_outfits_archivo.md` debe seguir entrando (contiene `galeria_outfits`).
- **Anaïs `number` boudoir no-entero** (`L01`) → romperá el parseo de número si se incluye sin namespacing (por eso va a P2).
- **Nombre de archivo de Anaïs** lleva `look` embebido (`anais_look<NUM>_<pose>`), inconsistente con Ele/MD (`<slug>_<N>_<pose>`). El registro lo encapsula, pero conviene que la Ama confirme si prefiere **normalizar** Anaïs a `anais_<NUM>_<pose>` (afectaría también a `update_galleries.py`) o conservar el histórico.
- **Formato de headers de pose:** el parser espera `**…:**` + code block. Confirmado en Anaïs (`**POSE 1 — command_standing:**` + ```). Verificar el mismo patrón en la galería de Miss Doll antes de dar P1 por cerrado.
- **La app pushea a `farid77cl/LaVouteDAnais`** (`GitHubApiService.kt:67,75`) — mismo repo de contenido; sin cambio de repo.

---

## 5 · Preguntas abiertas para la Ama (Gate)
1. **Miss Doll `C-N.png` legacy:** ¿renombrar los sets viejos a `miss_doll_<N>_<pose>.png`, o aplicar la convención solo a los looks nuevos hacia adelante?
2. **Boudoir de Anaïs (`L01…`):** ¿lo metemos en la app (P2, requiere namespacing) o lo dejamos fuera por ahora?
3. **UI:** ¿selector de personaje por pestañas, por filtro desplegable, o lista mixta con etiqueta de personaje?
4. **Nombre de archivo de Anaïs:** ¿conservar `anais_look<NUM>_<pose>` o normalizar a `anais_<NUM>_<pose>` por consistencia con Ele/Miss Doll?

---

## 6 · Entregable de implementación
El borrador de prompt para AI Studio que implementa **P1** está en:
`99_Sistema/prompt_app_ai_studio_21_multi_personaje.md` (marcado BORRADOR, pendiente de revisión de la Ama).
