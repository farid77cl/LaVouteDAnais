# Prompt AI Studio #21 — LV-App multi-personaje (P1: Miss Doll + Anaïs + Boudoir)

> **Gate cerrado 05/08/2026 — listo para pegar en AI Studio.** Base: `AUDITORIA_PLAN_LVAPP_multi_personaje_20260803.md` §5.
> Pégalo en AI Studio sobre el repo de la app `LV-App`. Implementa la Fase 1 (descubrimiento + parseo + subida correcta para las tres muñecas, **incluida la línea Boudoir de Anaïs**). NO toca UI de selector (eso es P2 — pestañas, ya decidido, se implementa después).
> ⚠️ El renombrado físico de archivos legacy (Miss Doll `C-N.png`, Anaïs `anais_look<NUM>`) es un cambio en el repo de **contenido**, no en la app — vive en `99_Sistema/scripts/mantenimiento/renombrar_legacy_multipersonaje.py`, se corre aparte en la máquina visual. Este prompt asume que esos archivos YA quedaron con nombre canónico antes de correr la app en producción; no dupliques ese trabajo acá.
>
> **🔁 Estandarización de poses (directiva Ama 05/08/2026):** las 3 muñecas ya NO tienen taxonomías de pose independientes. Comparten las **mismas 7 categorías de cámara que Ele** (`Standing/Back View/Seated/Side Profile/[slot 5]/POV/Odalisque`), mismo orden, mismo propósito de encuadre — solo el **nombre del slot 5** (el que en Ele es "Ditzy") y el **contenido/expresión** de cada pose cambian por personaje. Ver `_perfiles_visuales/miss_doll.md` §4 y `_perfiles_visuales/anais.md` §4 (fuente de verdad del canon; este prompt solo la traduce a código). Esto reemplaza el diseño de `CharacterProfile` de la versión anterior de este documento — no dejes las 5/4 poses viejas.

---

## Objetivo
Hoy la app solo reconoce a Ele. Debe reconocer también a **Miss Doll** y **Anaïs**, cuyas galerías viven en:
- Ele: `00_Ele/galeria_outfits.md` y `00_Ele/galeria_outfits_archivo.md`
- Miss Doll: `02_Personajes/01_Principales/miss_doll/GALERIA_OUTFITS_MISS_DOLL.md`  ← nombre en MAYÚSCULAS
- Anaïs: `02_Personajes/01_Principales/anais/galeria_looks_anais.md`  ← el nombre NO contiene "galeria_outfits"

Sin cambios, el filtro de descubrimiento (`GitRepository.kt`, ~línea 300) las excluye a ambas, y el uploader (`GitRepository.kt`, ~línea 134) y `PoseMatcher.kt` son Ele-only.

## Tareas

### 1. Registro de perfiles de personaje (fuente única, data-driven)
Crea `com/example/util/CharacterProfile.kt`. Las **7 categorías universales**, en orden fijo, son: `Standing, Back View, Seated, Side Profile, <slot5>, POV, Odalisque` — `slot5Name` es el único campo que varía el NOMBRE del slot entre personajes (Ele="Ditzy", Miss Doll="Glacial Command", Anaïs="Sovereign Gaze"); el resto de nombres de slot son literalmente idénticos entre los tres.

```kotlin
data class CharacterProfile(
    val slug: String,
    val displayName: String,
    val galleryPathContains: List<String>, // lowercase
    val imageFolder: String,
    val filePrefix: String,
    val slot5Name: String,                 // "Ditzy" | "Glacial Command" | "Sovereign Gaze"
    val poseAliases: Map<String, String>   // alias lowercase (nombre de pose o legacy) -> categoría universal
) {
    val poses: List<String> get() = listOf("Standing","Back View","Seated","Side Profile",slot5Name,"POV","Odalisque")

    companion object {
        val ALL: List<CharacterProfile> = listOf(
            CharacterProfile("ele","Ele", listOf("galeria_outfits"),
                "05_Imagenes/ele","ele_","Ditzy",
                /* alias de Ele: los ya existentes en PoseMatcher — NO tocar, cópialos literal */
                mapOf(/*…*/)),

            CharacterProfile("miss_doll","Miss Doll", listOf("galeria_outfits_miss_doll","miss_doll"),
                "05_Imagenes/miss_doll","miss_doll_","Glacial Command",
                mapOf(
                    // 7 slugs canónicos post-renombrado (ver §4 de miss_doll.md)
                    "standing" to "Standing", "back_view" to "Back View", "seated" to "Seated",
                    "side_profile" to "Side Profile", "glacial_command" to "Glacial Command",
                    "pov" to "POV", "odalisque" to "Odalisque",
                    // alias legacy — nombres de pose descriptivos que sobreviven en prompts/headers antiguos
                    "cruel_contrapposto" to "Standing", "espalda_total" to "Back View",
                    "monarch_throne" to "Seated", "tres_cuartos_arrogante" to "Side Profile",
                    "close_up_fria" to "Glacial Command", "throne_suelo" to "Odalisque",
                    "throne_en_suelo" to "Odalisque"
                    // NOTA: hip_carry / pie_en_hombro / caminata_circular fueron RETIRADAS del canon
                    // (05/08) — si aparecen en un archivo viejo sin match, caen al fallback de pose
                    // cruda (tarea 3), no se inventan alias falsos para ellas.
                )),

            CharacterProfile("anais","Anaïs", listOf("galeria_looks_anais","anais"),
                "05_Imagenes/anais","anais_","Sovereign Gaze",
                mapOf(
                    "standing" to "Standing", "back_view" to "Back View", "seated" to "Seated",
                    "side_profile" to "Side Profile", "sovereign_gaze" to "Sovereign Gaze",
                    "pov" to "POV", "odalisque" to "Odalisque",
                    // alias — nombres de pose ya materializados en L01-L04, mismo contenido, categoría nueva
                    "command_standing" to "Standing", "throne_seated" to "Seated",
                    "three_quarter" to "Side Profile", "domina_closeup" to "Sovereign Gaze",
                    "mirror_back" to "Back View", "kneeling_pov" to "POV", "chaise_command" to "Odalisque"
                ))
        )
        // La línea Boudoir de Anaïs (L01/L02…, poses boudoir_standing/chaise_seated/mirror_profile/
        // intimate_closeup) es un repertorio APARTE — no vive en poseAliases de "anais" para no
        // colisionar con las 7 categorías principales. Ver tarea 3b.
        fun fromPath(path: String): CharacterProfile {
            val p = path.lowercase()
            // orden importa: miss_doll y anais antes que el genérico ele
            return ALL.firstOrNull { prof -> prof.slug != "ele" && prof.galleryPathContains.any { p.contains(it) } }
                ?: ALL.first { it.slug == "ele" }
        }
    }
}
```
> ⚠️ Rellena el `poseAliases` de Ele con exactamente el `ALIAS_MAP` que hoy tiene `PoseMatcher.kt` (no lo pierdas).

### 2. Descubrimiento de galerías (`GitRepository.kt`, filtro ~línea 300)
Reemplaza la condición `entry.path.contains("galeria_outfits") || _batch_ …` por una que acepte el archivo si su ruta (lowercase) matchea el registro:
```kotlin
val markdownFiles = treeResponse.tree.filter { entry ->
    val p = entry.path.lowercase()
    entry.type == "blob" && p.endsWith(".md") &&
    (
        CharacterProfile.ALL.any { prof -> prof.galleryPathContains.any { p.contains(it) } } ||
        p.startsWith("_batch_") || p.contains("/_batch_")
    ) && !p.contains("galeria_index") && !p.contains("report") && !p.contains(".bkp")
}
```
Mantén el `sourceTag` existente (ya distingue miss_doll/anais/gotica). Además, guarda el `slug` de `CharacterProfile.fromPath(fileEntry.path).slug` en el look/prompt para uso del uploader.

### 3. `PoseMatcher` por personaje (`PoseMatcher.kt`)
Parametriza el emparejado con el perfil. Añade:
```kotlin
fun getCanonicalPose(filenameOrPose: String, profile: CharacterProfile): String? {
    val clean = filenameOrPose.lowercase().replace(Regex("\\.(png|jpe?g|webp)$"),"")
    val sansPrefix = clean
        .replace(Regex("^(ele|helena|miss_doll|anais)_"),"")
        .replace(Regex("^look0*\\d+_"),"")
    profile.poseAliases[sansPrefix]?.let { return it }
    profile.poseAliases.keys.sortedByDescending { it.length }.forEach { a ->
        if (sansPrefix == a || sansPrefix.contains(a)) return profile.poseAliases[a]
    }
    return null
}
```
El emparejado en `MainViewModel.kt` (~línea 243) debe pasar el perfil del look activo. Si no hay match, usar el nombre de pose crudo normalizado — **nunca** dejar la subida sin pose.

### 3b. Línea Boudoir de Anaïs — repertorio de pose separado + numeración no-entera
La galería de Anaïs tiene una segunda serie, marcada `# 🌹 LENCERÍA RETRO — Boudoir de La Voûte`, con looks numerados `L01, L02…` (prefijo no-numérico) y **4 poses propias, sin relación con las 7 principales**: `boudoir_standing, chaise_seated, mirror_profile, intimate_closeup`.
1. **Número:** el parser guarda `number: Int`. Antes de `toInt()`, aplica `Regex("^[Ll]0*(\\d+)").find(raw)?.groupValues?.get(1) ?: raw` para aceptar `L01`→`1`. Guarda además un flag `isBoudoir: Boolean` en el look (true si el header contenía el prefijo `L` o la ruta cae bajo la sección Boudoir) para no mezclarlo con la numeración principal de Anaïs.
2. **Poses:** NO uses `CharacterProfile.anais.poseAliases` para esta línea — sus 4 poses no son alias de las 7 categorías (no representan Standing/Back View/etc., son su propio repertorio de lencería). Añade un mapa separado, solo consultado cuando `isBoudoir == true`:
   ```kotlin
   val boudoirPoses = mapOf(
       "boudoir_standing" to "Boudoir Standing", "chaise_seated" to "Chaise Seated",
       "mirror_profile" to "Mirror Profile", "intimate_closeup" to "Intimate Closeup"
   )
   ```
3. **Subida:** mismo `imageFolder`/`filePrefix` de Anaïs, pero el nombre de archivo usa el número boudoir (`isBoudoir` con su propio contador), no el correlativo principal — para no colisionar `anais_1_standing.png` (look principal) con lo que sería `anais_1_boudoir_standing.png` (boudoir L01).

### 4. Ruta de subida por personaje (`GitRepository.kt` ~línea 134-142)
Deriva carpeta y prefijo del perfil del look (no `ele_` fijo):
```kotlin
val profile = CharacterProfile.ALL.first { it.slug == look.characterSlug } // el guardado en tarea 2
val prefix = profile.filePrefix // "ele_" | "miss_doll_" | "anais_"
val path = existingPath ?: run {
    val dir = (existingParentFolder ?: look.location)?.removeSuffix("/")
        ?: "${profile.imageFolder}/look${lookNumStr}_${slug}"
    "$dir/${prefix}${lookNumStr}_${formattedPose}.png"
}
```
> El prefijo de Anaïs ya no lleva "look" embebido (normalizado 05/08) → el nombre final queda `anais_5_standing.png`, no `anais_look05_command_standing.png`. Los 4 looks ya materializados (L01-L04) se renombran aparte, en el repo de contenido (ver script de mantenimiento) — no en este cambio de app.

### 5. NO tocar
- La guardia de resolución (>0.3 MP) ni el sello `[gallery WxH]` del commit.
- El repo destino (`farid77cl/LaVouteDAnais`).
- La lógica de literatura/audio.

## Criterios de aceptación (verificables)
1. Con las tres galerías presentes en el repo, la app las descubre las tres (el reporte de sync debe listar looks de Ele, Miss Doll y Anaïs con su conteo).
2. Al abrir un look de Miss Doll, aparecen sus **7** prompts emparejados a Standing/Back View/Seated/Side Profile/Glacial Command/POV/Odalisque. Al abrir uno de Anaïs (línea principal), sus **7** (mismas categorías, slot 5 = Sovereign Gaze). Al abrir un look Boudoir de Anaïs (`L01…`), sus **4** propias (Boudoir Standing/Chaise Seated/Mirror Profile/Intimate Closeup), sin mezclarse con las 7 principales.
3. Al subir un PNG desde un look de Miss Doll, el commit lo coloca en `05_Imagenes/miss_doll/look<NNN>_<tema>/miss_doll_<N>_<pose>.png`. Desde Anaïs (línea principal): `05_Imagenes/anais/look<NUM>_<slug>/anais_<NUM>_<pose>.png` (sin "look" en el nombre de archivo). Desde Ele: idéntico a hoy.
4. Los looks de Ele siguen funcionando exactamente igual que antes (regresión cero).
5. Un test unitario nuevo en `ParserTest`/`RegexTest` cubre `CharacterProfile.fromPath` para las tres rutas, `getCanonicalPose` para una pose de cada personaje (incluyendo al menos un alias legacy de Miss Doll, ej. `monarch_throne`→`Seated`), y el parseo de número boudoir (`L01`→`1`, `isBoudoir=true`).

## Entrega esperada de AI Studio
- Diff por archivo de los cambios reales (no resumen).
- Salida del build (`./gradlew assembleDebug` o equivalente) — **el log real**, no "BUILD SUCCESSFUL" a secas.
- Resultado de los tests unitarios nuevos.
- ⚠️ Recordar: los commits de AI Studio llegan a GitHub solo cuando la Ama pushea.
