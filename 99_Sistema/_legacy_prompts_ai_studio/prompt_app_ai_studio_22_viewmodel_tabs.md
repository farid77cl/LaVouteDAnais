# Prompt AI Studio #22 — ViewModel multi-personaje + Pestañas P2 + Fix Sincronización de Imágenes

> **Fecha:** 2026-08-05 · **Prerequisito:** prompt #21 ya aplicado.
> Pégalo en AI Studio sobre el repo `LV-App`. Scope: `MainViewModel.kt`, `PromptFilterScreen.kt` y `GitRepository.kt`.

---

## Contexto

El prompt #21 añadió `CharacterProfile.kt`, `PoseMatcher` parametrizado por personaje, descubrimiento multi-galería y ruta de subida por personaje.

Quedan tres aspectos por ajustar:

### Gap 1 — `GitRepository.kt` filtra solo imágenes de Ele en el sync del árbol
En `GitRepository.kt:736`, el parser de imágenes tiene hardcodeado:
`if (path.startsWith("05_Imagenes/ele/")...)`
Esto hace que las imágenes de Miss Doll (`05_Imagenes/miss_doll/`) y Anaïs (`05_Imagenes/anais/`) sean ignoradas al sincronizar el árbol del repositorio desde GitHub.

### Gap 2 — PoseMatcher.matches() en MainViewModel usa fallback Ele
Hay 6 llamadas a `PoseMatcher.matches(poseA, poseB)` (overload de 2 argumentos, que internamente usa el perfil de Ele) en `MainViewModel.kt`.

### Gap 3 — No hay UI para filtrar por personaje (P2: pestañas)
Hoy todos los looks se muestran juntos con Ele flotando arriba. Se necesitan pestañas de personaje.

---

## Tareas

### 1. Fix Sincronización de Imágenes en `GitRepository.kt`

En `GitRepository.kt` (aprox. línea 736 en `parseAndSaveTree`):

```kotlin
// ANTES (línea 736):
if (path.startsWith("05_Imagenes/ele/") && imageFormats.any { path.lowercase().endsWith(it) }) {

// DESPUÉS:
if (path.startsWith("05_Imagenes/") && imageFormats.any { path.lowercase().endsWith(it) }) {
```

> Al cambiar `path.startsWith("05_Imagenes/ele/")` por `path.startsWith("05_Imagenes/")`, la app sincronizará correctamente las imágenes de `05_Imagenes/ele/`, `05_Imagenes/miss_doll/` y `05_Imagenes/anais/`. El código existente subsiguiente (`subPath`, `extractLookNumber`, `CharacterProfile.fromPath(path)`) ya sabe procesar la ruta completa de cada personaje.

---

### 2. Resolver el perfil del look activo en MainViewModel

En `MainViewModel.kt`, añade una propiedad derivada que expone el `CharacterProfile` del look seleccionado:

```kotlin
// Cerca de línea 85, después de selectedLookNumber
private val selectedLookProfile: StateFlow<com.example.util.CharacterProfile> = combine(
    _selectedLookNumber,
    allLooks
) { number, looks ->
    val look = number?.let { n -> looks.firstOrNull { it.number == n } }
    if (look != null) com.example.util.CharacterProfile.ALL.firstOrNull { it.slug == look.characterSlug }
        ?: com.example.util.CharacterProfile.ALL.first { it.slug == "ele" }
    else com.example.util.CharacterProfile.ALL.first { it.slug == "ele" }
}.stateIn(viewModelScope, SharingStarted.Lazily, com.example.util.CharacterProfile.ALL.first { it.slug == "ele" })

private val selectedLookIsBoudoir: StateFlow<Boolean> = combine(
    _selectedLookNumber, allLooks
) { number, looks -> looks.firstOrNull { it.number == number }?.isBoudoir ?: false
}.stateIn(viewModelScope, SharingStarted.Lazily, false)
```

---

### 3. Pasar el perfil a las 6 llamadas de PoseMatcher.matches()

**Línea 245** (`activePromptText`):
```kotlin
// ANTES:
prompts.firstOrNull { com.example.util.PoseMatcher.matches(pose, it.poseName) }?.promptText
// DESPUÉS:
prompts.firstOrNull { com.example.util.PoseMatcher.matches(pose, it.poseName, selectedLookProfile.value, selectedLookIsBoudoir.value) }?.promptText
```

**Líneas 516, 549, 581, 613, 670** (filtros de galería):

```kotlin
// ANTES:
val matchesPose = pose == "Todas" || com.example.util.PoseMatcher.matches(pose, img.poseName)
// DESPUÉS:
val imgProfile = associatedLook?.let { al ->
    com.example.util.CharacterProfile.ALL.firstOrNull { it.slug == al.characterSlug }
} ?: com.example.util.CharacterProfile.ALL.first { it.slug == "ele" }
val imgIsBoudoir = associatedLook?.isBoudoir ?: false
val matchesPose = pose == "Todas" || com.example.util.PoseMatcher.matches(pose, img.poseName, imgProfile, imgIsBoudoir)
```

---

### 4. Pestañas de personaje en UI (P2)

#### 4a. Estado en MainViewModel

```kotlin
private val _selectedCharacterFilter = MutableStateFlow("Todas")
val selectedCharacterFilter: StateFlow<String> = _selectedCharacterFilter.asStateFlow()

fun setCharacterFilter(filter: String) {
    _selectedCharacterFilter.value = filter
}
```

#### 4b. Aplicar filtro en `filteredLooks`

En `filteredLooks` (aprox. línea 214):

```kotlin
val matchesCharacter = characterFilter == "Todas" || when (characterFilter) {
    "Ele" -> look.characterSlug == "ele"
    "Miss Doll" -> look.characterSlug == "miss_doll"
    "Anaïs" -> look.characterSlug == "anais"
    else -> true
}

matchesCategory && matchesColor && matchesTag && matchesQuery && matchesCharacter

// Ordenar por número descendente (sin forzar a Ele arriba):
}.sortedWith(compareByDescending<LookEntity> { it.number }
    .thenBy { it.name }
)
```

#### 4c. UI de pestañas en `PromptFilterScreen.kt`

Añade un selector de chips/tabs (Todas · Ele · Miss Doll · Anaïs) arriba de la lista.

---

## Criterios de aceptación

1. **Sincronización:** Al refrescar la app, las imágenes de `05_Imagenes/miss_doll/` y `05_Imagenes/anais/` se descargan y muestran en la galería.
2. **Subida:** Las fotos subidas desde la app a Ele van a `05_Imagenes/ele/`, las de Miss Doll a `05_Imagenes/miss_doll/`, y las de Anaïs a `05_Imagenes/anais/`.
3. **Prompts:** Las poses de Miss Doll y Anaïs matchean correctamente con sus alias.
4. **Build:** `./gradlew assembleDebug` exitoso.
