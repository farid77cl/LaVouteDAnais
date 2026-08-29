# Prompt AI Studio #27 — Fix Definitivo de Slot 5 y Nombrado Canónico Multi-Personaje

> **Fecha:** 2026-08-18
> Pégalo en AI Studio sobre el repo `LV-App`. Scope: **`CharacterProfile.kt`**, **`PoseMatcher.kt`**, **`GitRepository.kt`**, **`MainViewModel.kt`** y **`PromptFilterScreen.kt`**.

---

## 🔍 Diagnóstico del Problema (Causa Raíz)

A pesar de que el canon y el contrato establecen que el **Slot 5** de cada personaje tiene un nombre y slug exclusivo:
- **Ele:** `Ditzy` → archivo `ele_<N>_ditzy.png`
- **Miss Doll:** `Glacial Command` → archivo `miss_doll_<N>_glacial_command.png`
- **Anaïs (Estándar):** `Sovereign Gaze` → archivo `anais_<N>_sovereign_gaze.png`
- **Anaïs (Boudoir):** `Sovereign Gaze` / lencería → archivo `anais_L<NN>_sovereign_gaze.png`

En producción, la app Android `LV-App` continúa subiendo las fotos del Slot 5 para **Anaïs** y **Miss Doll** con el sufijo erróneo `_ditzy.png` (ej. `anais_017_ditzy.png`, `miss_doll_021_ditzy.png`).
Esto ocurre por una combinación de 3 factores en el código de la app:
1. **Fallback de Alias Incompleto (`CharacterProfile.kt` / `PoseMatcher.kt`):**
   Si la UI o el estado interno envía el string `"ditzy"` (o `"Ditzy"`) al subir una imagen de Anaïs o Miss Doll, `PoseMatcher.getCanonicalPose` no tenía mapeado `"ditzy"` a `"Sovereign Gaze"` en Anaïs ni a `"Glacial Command"` en Miss Doll, por lo que el fallback devuelve `"ditzy"`.
2. **Formateo de Pose en Uploader (`GitRepository.kt` / `MainViewModel.kt`):**
   Al construir la ruta del archivo (`${prefix}${lookNumStr}_${formattedPose}.png`), `formattedPose` no forzaba el slug canónico del personaje para el slot 5 (`profile.getSlot5Slug()`), permitiendo que el string recibido de la UI (`"ditzy"`) se convirtiera directamente en el nombre del archivo.
3. **UI / Selector de Poses (`PromptFilterScreen.kt`):**
   Si los botones, pestañas o chips de selección de pose no se actualizan reactivamente con `selectedLookProfile.poses` (o si el botón del slot 5 envía un valor fijo `"Ditzy"` en lugar de `profile.slot5Name`), el evento de subida se dispara con la pose equivocada.

---

## 🛠️ Cambios Requeridos

### 1. `CharacterProfile.kt`

1. Añade a cada `CharacterProfile` un helper `slot5Slug: String` (o método `getSlot5Slug()`):
   ```kotlin
   val slot5Slug: String get() = when (slug) {
       "miss_doll" -> "glacial_command"
       "anais" -> "sovereign_gaze"
       else -> "ditzy"
   }
   ```
2. Asegura que en `CharacterProfile.ALL`:
   - Para **Miss Doll**:
     En `poseAliases`, incluye explícitamente:
     `"ditzy" to "Glacial Command"`, `"sovereign_gaze" to "Glacial Command"`, `"glacial command" to "Glacial Command"`, `"glacial_command" to "Glacial Command"`.
   - Para **Anaïs**:
     En `poseAliases`, incluye explícitamente:
     `"ditzy" to "Sovereign Gaze"`, `"glacial_command" to "Sovereign Gaze"`, `"sovereign gaze" to "Sovereign Gaze"`, `"sovereign_gaze" to "Sovereign Gaze"`.
   - Para **Ele**:
     En `poseAliases`, incluye explícitamente:
     `"glacial_command" to "Ditzy"`, `"sovereign_gaze" to "Ditzy"`, `"ditzy" to "Ditzy"`.

---

### 2. `PoseMatcher.kt`

Refuerza `getCanonicalPose` para que resuelva de forma estricta cualquier variante del Slot 5:
```kotlin
fun getCanonicalPose(filenameOrPose: String, profile: CharacterProfile): String? {
    val clean = filenameOrPose.lowercase()
        .replace(Regex("\\.(png|jpe?g|webp)$"), "")
        .replace(Regex("^(ele|helena|miss_doll|anais)_"), "")
        .replace(Regex("^look0*\\d+_"), "")
        .replace(Regex("^l0*\\d+_"), "")
        .trim()

    // 1. Match directo en poseAliases del perfil
    profile.poseAliases[clean]?.let { return it }

    // 2. Normalización de Slot 5 universal por personaje
    if (clean in listOf("ditzy", "glacial_command", "glacial command", "sovereign_gaze", "sovereign gaze", "slot5", "close_up_fria", "domina_closeup")) {
        return profile.slot5Name
    }

    // 3. Match por inclusión de alias más largo
    profile.poseAliases.keys.sortedByDescending { it.length }.forEach { a ->
        if (clean == a || clean.contains(a)) return profile.poseAliases[a]
    }
    return null
}
```

---

### 3. `GitRepository.kt` (`uploadImageToGithub`)

En la función de subida de imágenes a GitHub, blinda la generación de `formattedPose` antes de armar la ruta del archivo:

```kotlin
// Determinar perfil del personaje asociado al look
val profile = CharacterProfile.ALL.firstOrNull { it.slug == look.characterSlug }
    ?: CharacterProfile.ALL.first { it.slug == "ele" }

// Resolver la pose canónica
val canonicalPose = PoseMatcher.getCanonicalPose(pose, profile) ?: pose

// Formatear el slug de la pose garantizando el contrato de nombrado
val formattedPose = when (canonicalPose.lowercase().replace(" ", "_")) {
    "ditzy", "glacial_command", "sovereign_gaze" -> profile.slot5Slug
    "standing" -> "standing"
    "back_view", "back" -> "back_view"
    "seated" -> "seated"
    "side_profile", "profile" -> "side_profile"
    "pov" -> "pov"
    "odalisque" -> "odalisque"
    else -> canonicalPose.lowercase().replace(" ", "_")
}

// Prefijo y padding numérico
val lookNumStr = if (look.isBoudoir) {
    String.format("L%02d", look.number)
} else {
    String.format("%02d", look.number).let { if (look.number >= 100) look.number.toString() else it }
}
val prefix = if (look.isBoudoir) "anais_L${String.format("%02d", look.number)}_" else profile.filePrefix

// Construir la ruta de destino canónica
val targetDir = look.location?.removeSuffix("/")
    ?: "${profile.imageFolder}/look${lookNumStr}_${look.slug}"

val fileName = if (look.isBoudoir) {
    "anais_${lookNumStr}_${formattedPose}.png"
} else {
    "${prefix}${lookNumStr}_${formattedPose}.png"
}

val finalPath = "$targetDir/$fileName"
```

---

### 4. `PromptFilterScreen.kt` / UI de Selector de Poses

Asegura que el selector de poses (pestañas / chips / botones de pose) renderice dinámicamente las poses de `selectedLookProfile`:
```kotlin
val currentPoses = if (selectedLookIsBoudoir) {
    listOf("Boudoir Standing", "Chaise Seated", "Mirror Profile", "Intimate Closeup")
} else {
    selectedLookProfile.poses // Contiene Standing, Back View, Seated, Side Profile, slot5Name, POV, Odalisque
}
```
Al hacer click o interactuar con el Slot 5, la pose seleccionada y enviada a `uploadImage` debe ser exactamente `selectedLookProfile.slot5Name` (ej. `"Sovereign Gaze"` para Anaïs, `"Glacial Command"` para Miss Doll).

---

## 📋 Criterios de Aceptación y Verificación

1. **Subida Anaïs:** Al subir cualquier imagen en el Slot 5 para un look de Anaïs (ej. Look 17, 18, 20 o 25), el commit en GitHub crea obligatoriamente `05_Imagenes/anais/look.../anais_<N>_sovereign_gaze.png` (o `anais_L<NN>_sovereign_gaze.png` si es Boudoir). **NUNCA `_ditzy.png`**.
2. **Subida Miss Doll:** Al subir una imagen en el Slot 5 para Miss Doll, el commit en GitHub crea `05_Imagenes/miss_doll/look.../miss_doll_<N>_glacial_command.png`. **NUNCA `_ditzy.png`**.
3. **Subida Ele:** Al subir el Slot 5 para Ele, crea `05_Imagenes/ele/look.../ele_<N>_ditzy.png`.
4. **Resistencia a Errores:** Incluso si la UI manda `"Ditzy"` por error de estado para un look de Anaïs o Miss Doll, la capa de `GitRepository` y `PoseMatcher` lo intercepta y lo guarda como `_sovereign_gaze.png` o `_glacial_command.png`.
5. **Build:** `./gradlew assembleDebug` y tests unitarios de `PoseMatcherTest` pasan al 100%.

---

## Entrega esperada de AI Studio
- Diff por archivo modificado (`CharacterProfile.kt`, `PoseMatcher.kt`, `GitRepository.kt`, `PromptFilterScreen.kt`).
- Log real de compilación `./gradlew assembleDebug`.
- Tests unitarios verificando `getCanonicalPose("ditzy", anaisProfile) == "Sovereign Gaze"` y `getCanonicalPose("ditzy", missDollProfile) == "Glacial Command"`.
