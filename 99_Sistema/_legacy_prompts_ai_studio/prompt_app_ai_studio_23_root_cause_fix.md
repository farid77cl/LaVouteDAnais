# Prompt AI Studio #23 — Fix Crítico: Offset de ID, characterSlug e Imágenes

> **Fecha:** 2026-08-05
> Pégalo en AI Studio sobre el repo `LV-App`. Scope: **`GitRepository.kt`**.

---

## 🔍 Diagnóstico del Problema

Al auditar `GitRepository.kt`, se encontraron 3 bugs de raíz que causan que al filtrar por Miss Doll aparezcan los datos de Ele y que en la ficha de imágenes solo aparezca Ele:

1. **`parseMarkdown` no pasaba `characterSlug` a `LookEntity`:**
   En las líneas 499-513, al crear `LookEntity`, no se enviaba `characterSlug = profile.slug`. Por defecto, `Entities.kt` asignaba `"ele"` a **TODOS** los looks (incluyendo los de Miss Doll y Anaïs). Al filtrar por Miss Doll (`characterSlug == "miss_doll"`), la app no encontraba ningún look de Miss Doll y caía al fallback de Ele.

2. **Colisión de IDs (`number` como PrimaryKey):**
   Miss Doll tiene "Look 1", Anaïs tiene "Look 1" y Ele tiene "Look 1". Como `number` es la clave primaria en la DB Room, los de Miss Doll y Anaïs sobreescribían a los de Ele (o viceversa) porque todos tenían ID `1`.
   `Entities.kt` ya tiene preparado `displayNumber` para usar offsets (`number % 10000`), pero `GitRepository.kt` no estaba aplicando los offsets:
   - **Ele:** `1..9999`
   - **Miss Doll:** `20000 + number` (ej. Look 1 → 20001)
   - **Anaïs:** `30000 + number` (ej. Look 1 → 30001)
   - **Anaïs Boudoir:** `40000 + number` (ej. Look L01 → 40001)

3. **`parseAndSaveTree` filtraba solo `05_Imagenes/ele/`:**
   En la línea 736, el parser del árbol de imágenes de Git decía `if (path.startsWith("05_Imagenes/ele/"))`. Esto descartaba completamente las imágenes de `05_Imagenes/miss_doll/` y `05_Imagenes/anais/`.

---

## 🛠️ Cambios en `GitRepository.kt`

### 1. Actualizar `parseMarkdown` (líneas ~373 a ~515)

Modifica `parseMarkdown` para aplicar offset al número de look, guardar `characterSlug` y marcar `isBoudoir`:

```kotlin
// Dentro de parseMarkdown:
val isBoudoirLook = profile.slug == "anais" && (
    detailsInParentheses.contains("Boudoir", ignoreCase = true) || 
    rawTitleAndMaybeDetails.contains("Look L", ignoreCase = true) ||
    trimmedLine.contains("Look L", ignoreCase = true)
)

val finalNumber = when (profile.slug) {
    "miss_doll" -> 20000 + number
    "anais" -> if (isBoudoirLook) 40000 + number else 30000 + number
    else -> number
}

// Al agregar el LookEntity (línea ~499):
lookList.add(LookEntity(
    number = finalNumber,
    characterSlug = profile.slug,
    isBoudoir = isBoudoirLook,
    name = cleanedName.ifEmpty { "Look $number" },
    category = outfitType,
    outfitType = outfitType, 
    color = "Otros Colores",
    tags = tagsString,
    fullTitle = trimmedLine.replace("#", "").trim(),
    date = if (detailsInParentheses.contains("/")) detailsInParentheses.substringBefore("—").trim() else "Mayo 2026",
    emoji = emojiMatch,
    details = detailsInParentheses.ifEmpty { "Protocolo ${profile.displayName} V3.5" },
    canonicalInfo = "",
    negativePrompt = null,
    location = null
))

// Al agregar los Prompts (línea ~460):
promptList.add(PromptEntity(
    "${finalNumber}_${currentPose!!.replace(" ", "_").lowercase()}",
    finalNumber,
    currentPose!!,
    finalPrompt
))
```

---

### 2. Actualizar `parseAndSaveTree` (líneas ~736 a ~760)

Permite procesar cualquier subcarpeta de `05_Imagenes/` y calcula el `lookNumber` con el offset correspondiente al personaje:

```kotlin
// Línea 736:
if (path.startsWith("05_Imagenes/") && imageFormats.any { path.lowercase().endsWith(it) }) {
    val segments = path.split("/")
    if (segments.size < 4) continue // 05_Imagenes/<character>/<folder>/<filename>

    val parentFolder = segments[segments.size - 2]
    val fileName = segments[segments.size - 1]

    val subPath = path.substringAfter("05_Imagenes/")
    val profile = com.example.util.CharacterProfile.fromPath(path)
    val rawLookNumber = extractLookNumber(subPath)

    val isBoudoir = profile.slug == "anais" && (
        path.contains("boudoir", ignoreCase = true) || 
        fileName.contains("lookL", ignoreCase = true)
    )

    val lookNumber = rawLookNumber?.let { num ->
        when (profile.slug) {
            "miss_doll" -> if (num < 20000) 20000 + num else num
            "anais" -> if (isBoudoir) (if (num < 40000) 40000 + num else num) else (if (num < 30000) 30000 + num else num)
            else -> num
        }
    }

    val poseName = com.example.util.PoseMatcher.getCanonicalPose(fileName, profile, isBoudoir) ?: "unknown"
    val downloadUrl = "https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/$path?v=${entry.sha}"

    imageList.add(
        ImageEntity(
            path = path,
            fileName = fileName,
            lookNumber = lookNumber,
            poseName = poseName,
            downloadUrl = downloadUrl,
            parentFolder = parentFolder
        )
    )
}
```

---

## Criterios de Aceptación

1. **Filtro de personaje:** Al presionar "Miss Doll", se muestran **exclusivamente** los looks y prompts de Miss Doll.
2. **Pestaña de imágenes:** La galería de imágenes muestra las fotos de `05_Imagenes/miss_doll/` y `05_Imagenes/anais/`.
3. **Cero colisiones:** Los "Look 1" de Ele, Miss Doll y Anaïs coexisten sin sobreescribirse gracias a los offsets (1, 20001, 30001).
4. **Build limpio:** `./gradlew assembleDebug` exitoso.
