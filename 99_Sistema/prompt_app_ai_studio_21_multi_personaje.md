# Prompt AI Studio #21 — LV-App multi-personaje (P1: Miss Doll + Anaïs)

> **BORRADOR — pendiente de revisión de la Ama.** Base: `AUDITORIA_PLAN_LVAPP_multi_personaje_20260803.md`.
> Pégalo en AI Studio sobre el repo de la app `LV-App`. Implementa SOLO la Fase 1 (que las tres muñecas se descubran, se parseen y suban a la carpeta/nombre correctos). NO toca UI de selector (eso es P2).

---

## Objetivo
Hoy la app solo reconoce a Ele. Debe reconocer también a **Miss Doll** y **Anaïs**, cuyas galerías viven en:
- Ele: `00_Ele/galeria_outfits.md` y `00_Ele/galeria_outfits_archivo.md`
- Miss Doll: `02_Personajes/01_Principales/miss_doll/GALERIA_OUTFITS_MISS_DOLL.md`  ← nombre en MAYÚSCULAS
- Anaïs: `02_Personajes/01_Principales/anais/galeria_looks_anais.md`  ← el nombre NO contiene "galeria_outfits"

Sin cambios, el filtro de descubrimiento (`GitRepository.kt`, ~línea 300) las excluye a ambas, y el uploader (`GitRepository.kt`, ~línea 134) y `PoseMatcher.kt` son Ele-only.

## Tareas

### 1. Registro de perfiles de personaje (fuente única, data-driven)
Crea `com/example/util/CharacterProfile.kt`:
```kotlin
data class CharacterProfile(
    val slug: String,
    val displayName: String,
    val galleryPathContains: List<String>, // lowercase
    val imageFolder: String,
    val filePrefix: String,
    val poses: List<String>,               // canónicos, en orden
    val poseAliases: Map<String, String>   // alias lowercase -> canónico
) {
    companion object {
        val ALL: List<CharacterProfile> = listOf(
            CharacterProfile("ele","Ele", listOf("galeria_outfits"),
                "05_Imagenes/ele","ele_",
                listOf("Standing","Back View","Seated","Side Profile","Ditzy","POV","Odalisque"),
                /* alias de Ele: los ya existentes en PoseMatcher */ mapOf(/*…*/)),
            CharacterProfile("miss_doll","Miss Doll", listOf("galeria_outfits_miss_doll","miss_doll"),
                "05_Imagenes/miss_doll","miss_doll_",
                listOf("Monarch Throne","Hip Carry","Pie en Hombro","Throne Suelo","Caminata Circular"),
                mapOf("monarch_throne" to "Monarch Throne","hip_carry" to "Hip Carry",
                      "pie_en_hombro" to "Pie en Hombro","throne_suelo" to "Throne Suelo",
                      "caminata_circular" to "Caminata Circular")),
            CharacterProfile("anais","Anaïs", listOf("galeria_looks_anais","anais"),
                "05_Imagenes/anais","anais_look",
                listOf("Command Standing","Throne Seated","Three Quarter","Domina Closeup"),
                mapOf("command_standing" to "Command Standing","throne_seated" to "Throne Seated",
                      "three_quarter" to "Three Quarter","domina_closeup" to "Domina Closeup"))
        )
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

### 4. Ruta de subida por personaje (`GitRepository.kt` ~línea 134-142)
Deriva carpeta y prefijo del perfil del look (no `ele_` fijo):
```kotlin
val profile = CharacterProfile.ALL.first { it.slug == look.characterSlug } // el guardado en tarea 2
val prefix = profile.filePrefix // "ele_" | "miss_doll_" | "anais_look"
val path = existingPath ?: run {
    val dir = (existingParentFolder ?: look.location)?.removeSuffix("/")
        ?: "${profile.imageFolder}/look${lookNumStr}_${slug}"
    "$dir/${prefix}${lookNumStr}_${formattedPose}.png"
}
```
> ⚠️ Para Anaïs el prefijo `anais_look` ya incluye "look" → el nombre final queda `anais_look05_command_standing.png`, que es la convención vigente. No dupliques "look".

### 5. NO tocar
- La guardia de resolución (>0.3 MP) ni el sello `[gallery WxH]` del commit.
- El repo destino (`farid77cl/LaVouteDAnais`).
- La lógica de literatura/audio.

## Criterios de aceptación (verificables)
1. Con las tres galerías presentes en el repo, la app las descubre las tres (el reporte de sync debe listar looks de Ele, Miss Doll y Anaïs con su conteo).
2. Al abrir un look de Miss Doll, aparecen sus **5** prompts, cada uno emparejado a su pose (Monarch Throne…). Al abrir uno de Anaïs, sus **4** (Command Standing…).
3. Al subir un PNG desde un look de Miss Doll, el commit lo coloca en `05_Imagenes/miss_doll/look<NNN>_<tema>/miss_doll_<N>_<pose>.png`. Desde Anaïs: `05_Imagenes/anais/look<NUM>_<slug>/anais_look<NUM>_<pose>.png`. Desde Ele: idéntico a hoy.
4. Los looks de Ele siguen funcionando exactamente igual que antes (regresión cero).
5. Un test unitario nuevo en `ParserTest`/`RegexTest` cubre `CharacterProfile.fromPath` para las tres rutas y `getCanonicalPose` para una pose de cada personaje.

## Entrega esperada de AI Studio
- Diff por archivo de los cambios reales (no resumen).
- Salida del build (`./gradlew assembleDebug` o equivalente) — **el log real**, no "BUILD SUCCESSFUL" a secas.
- Resultado de los tests unitarios nuevos.
- ⚠️ Recordar: los commits de AI Studio llegan a GitHub solo cuando la Ama pushea.
