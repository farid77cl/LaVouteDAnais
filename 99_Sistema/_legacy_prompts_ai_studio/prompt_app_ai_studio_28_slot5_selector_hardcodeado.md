# Prompt AI Studio #28 — El selector de poses está hardcodeado: 8 chips en vez de 7

> **Fecha:** 2026-08-18
> **Repo:** `LV-App` · **Medido sobre HEAD `eb9a049`** (2026-08-18 09:14, versionCode 21 / versionName "4.12")
> **Reemplaza al #27** en lo que respecta al slot 5. Leer la sección "Qué NO hacer" antes de tocar nada.

---

## 0. Estado verificado del repo (no re-diagnosticar)

Se clonó el repo y se leyó el código. **Estos puntos del #27 YA ESTÁN APLICADOS y NO deben volver a tocarse:**

- `CharacterProfile.kt` ya tiene `slot5Name` por personaje (`"Ditzy"` / `"Glacial Command"` / `"Sovereign Gaze"`) y la propiedad `poses`.
- `poseAliases` ya mapea `"ditzy"` → `"Glacial Command"` (Miss Doll, línea 34) y `"ditzy"` → `"Sovereign Gaze"` (Anaïs, línea 48).
- `PoseMatcher.getCanonicalPose` ya resuelve correctamente: se trazó `anais_017_ditzy.png` → `sansPrefix = "ditzy"` → `poseAliases["ditzy"]` → **`"Sovereign Gaze"`**. Funciona. **No reescribir `PoseMatcher.kt`.**
- `GitRepository.parseMarkdown` ya resuelve el nombre del prompt del slot 5: para la línea `**5. Sovereign Gaze:**` el regex captura `text = "gaze"`, ningún `contains` matchea, cae al fallback numérico `5 -> profile.slot5Name` y guarda el `PromptEntity` con `poseName = "Sovereign Gaze"`. **Correcto. No tocar el parser.**

---

## 1. Causa raíz REAL (medida, no inferida)

La Ama reporta: *"hoy tengo 8 slugs, el Sovereign Gaze que es idéntico a Ditzy"*.

**`app/src/main/java/com/example/ui/PromptFilterScreen.kt`, líneas 490-493:**

```kotlin
val standardPoses = listOf("Standing", "Back View", "Seated", "Side Profile", "Ditzy", "POV", "Odalisque")
val customPoses = remember(availablePrompts) {
    availablePrompts.map { it.poseName }.filter { !standardPoses.contains(it) }.distinct()
}
val poses = standardPoses + customPoses
```

Cadena exacta para un look de Anaïs:

| Paso | Valor |
|---|---|
| `standardPoses` (hardcodeado) | `[Standing, Back View, Seated, Side Profile, `**`Ditzy`**`, POV, Odalisque]` |
| `availablePrompts.map { it.poseName }` (del parser) | `[Standing, Back View, Seated, Side Profile, `**`Sovereign Gaze`**`, POV, Odalisque]` |
| `customPoses` = los que NO están en `standardPoses` | `[Sovereign Gaze]` |
| `poses = standardPoses + customPoses` | **8 chips** — `Ditzy` (fantasma, sin prompt detrás) + `Sovereign Gaze` (el real) |

**Consecuencia de tocar el chip equivocado:** `GitRepository.kt:128` (`poseName.equals("Ditzy", ...) -> "ditzy"`) escribe `anais_<N>_ditzy.png`. Ese nombre **no lo mapea `update_galleries.py`** del repo de contenido, que arma la tabla de Anaïs buscando la columna `sovereign_gaze`: **la foto existe en GitHub y la galería maestra muestra la pose vacía.** Van 4 reincidencias (24 archivos renombrados a mano los días 15, 17 y 18/08).

**La pantalla YA tiene el perfil disponible:** `PromptFilterScreen.kt:124` declara `val selectedLookProfile by viewModel.selectedLookProfile.collectAsState()` (tipo `StateFlow<CharacterProfile>`, **no nullable**) y ya lo usa en las líneas 134 y 157. La línea 490 simplemente no lo consulta.

---

## 2. Cambios requeridos (3 archivos + versión, quirúrgicos)

### 2.1 `app/src/main/java/com/example/util/CharacterProfile.kt`

Agregar la propiedad computada **inmediatamente después** de `val poses` (línea 12). Derivarla de `slot5Name` — dueño único, sin un `when (slug)` paralelo que pueda divergir:

```kotlin
    val poses: List<String> get() = listOf("Standing", "Back View", "Seated", "Side Profile", slot5Name, "POV", "Odalisque")

    /** Slug canonico del slot 5 en disco: ditzy | glacial_command | sovereign_gaze. */
    val slot5Slug: String get() = slot5Name.lowercase().replace(" ", "_")
```

### 2.2 `app/src/main/java/com/example/ui/PromptFilterScreen.kt` — **el fix principal**

Reemplazar **solo la línea 490**. No tocar `customPoses`, `poses`, el `LazyRow` ni nada más de ese bloque:

```kotlin
// ANTES
val standardPoses = listOf("Standing", "Back View", "Seated", "Side Profile", "Ditzy", "POV", "Odalisque")

// DESPUES
// El slot 5 cambia por personaje (Ditzy | Glacial Command | Sovereign Gaze).
// Hardcodear "Ditzy" agregaba un chip fantasma Y empujaba el nombre real del
// slot 5 a customPoses => 8 chips en Anais/Miss Doll, con el slot 5 duplicado.
val standardPoses = selectedLookProfile.poses
```

`customPoses` sigue funcionando igual para las poses realmente no estándar (las 4 de Boudoir: `Boudoir Standing`, `Chaise Seated`, `Mirror Profile`, `Intimate Closeup`), que deben seguir apareciendo.

### 2.3 `app/src/main/java/com/example/data/repository/GitRepository.kt` — segunda capa

En `saveImageToGithub` (línea ~118). Hoy `profile` se calcula en la línea 134, **después** de `formattedPose`. Subirlo y usar el slug del perfil en la rama del slot 5:

```kotlin
// ANTES (lineas 123-135)
val formattedPose = when {
    poseName.equals("Standing", ignoreCase = true) -> "standing"
    poseName.equals("Back View", ignoreCase = true) -> "back_view"
    poseName.equals("Seated", ignoreCase = true) -> "seated"
    poseName.equals("Side Profile", ignoreCase = true) -> "side_profile"
    poseName.equals("Ditzy", ignoreCase = true) -> "ditzy"
    poseName.equals("POV", ignoreCase = true) -> "pov"
    poseName.equals("Odalisque", ignoreCase = true) -> "odalisque"
    else -> poseName.lowercase().replace(" ", "_")
}

val slug = slugify(look.name)
val profile = com.example.util.CharacterProfile.ALL.first { it.slug == look.characterSlug }

// DESPUES
val profile = com.example.util.CharacterProfile.ALL.first { it.slug == look.characterSlug }

val formattedPose = when {
    poseName.equals("Standing", ignoreCase = true) -> "standing"
    poseName.equals("Back View", ignoreCase = true) -> "back_view"
    poseName.equals("Seated", ignoreCase = true) -> "seated"
    poseName.equals("Side Profile", ignoreCase = true) -> "side_profile"
    // Slot 5: cualquier alias (incluido el legacy "Ditzy") se escribe SIEMPRE con
    // el slug canonico del perfil, asi una imagen de Anais no puede volver a
    // subirse como _ditzy.png y desaparecer de la galeria maestra.
    poseName.equals(profile.slot5Name, ignoreCase = true) -> profile.slot5Slug
    poseName.equals("Ditzy", ignoreCase = true) -> profile.slot5Slug
    poseName.equals("POV", ignoreCase = true) -> "pov"
    poseName.equals("Odalisque", ignoreCase = true) -> "odalisque"
    else -> poseName.lowercase().replace(" ", "_")
}

val slug = slugify(look.name)
```

Para Ele nada cambia: `slot5Name = "Ditzy"` → `slot5Slug = "ditzy"`.

### 2.4 `app/build.gradle.kts`

Subir `versionCode = 22` y `versionName = "4.13"`. La cabecera muestra `v{VERSION_NAME} ({VERSION_CODE}) · {GIT_SHA}`: sin bump, la Ama no puede distinguir en pantalla si el APK que está corriendo trae el fix. (El #12 no bumpeó y por eso no se supo qué versión estaba rota.)

---

## 3. 🚫 Qué NO hacer (el #27 pedía esto y es peligroso)

- **NO aplicar el bloque de `GitRepository` del #27 §3.** Inventa `look.slug`, `String.format("%02d", look.number)` y un prefijo Boudoir propio que **contradicen el código real**, el cual usa `slugify(look.name)`, `padStart(3, '0')`, `existingPath` y `existingParentFolder`. Aplicarlo literal cambia las rutas de destino y rompe carpetas ya materializadas. El único cambio necesario en ese archivo es el de §2.3.
- **NO reescribir `PoseMatcher.kt`.** Ya resuelve bien; el #27 §2 es churn sobre código sano.
- **NO agregar alias cruzados** (por ejemplo `"sovereign_gaze"` → `"Ditzy"` en el perfil de Ele), como pedía el #27 §1.2: hacen que el archivo de un personaje se lea como pose de otro.
- **NO tocar** `customPoses`, el parser de markdown ni el `LazyRow` del selector.

---

## 4. Tests unitarios obligatorios

Agregar a `app/src/test/java/com/example/util/CharacterProfileTest.kt` (los tests existentes de ese archivo son reales — respetarlos). Estos 4 fueron trazados a mano contra `PoseMatcher` y `CharacterProfile` y deben pasar sin modificar la lógica:

```kotlin
    @Test
    fun testCadaPerfilExponeExactamenteSietePoses() {
        CharacterProfile.ALL.forEach { profile ->
            assertEquals("El perfil ${profile.slug} debe exponer 7 poses", 7, profile.poses.size)
            assertEquals("El perfil ${profile.slug} no debe repetir poses", 7, profile.poses.distinct().size)
        }
    }

    @Test
    fun testSlot5EsElNombreDelPersonajeYNoDitzy() {
        val ele = CharacterProfile.ALL.first { it.slug == "ele" }
        val missDoll = CharacterProfile.ALL.first { it.slug == "miss_doll" }
        val anais = CharacterProfile.ALL.first { it.slug == "anais" }

        assertEquals("Ditzy", ele.poses[4])
        assertEquals("Glacial Command", missDoll.poses[4])
        assertEquals("Sovereign Gaze", anais.poses[4])

        assertFalse("Miss Doll no debe ofrecer Ditzy", missDoll.poses.contains("Ditzy"))
        assertFalse("Anais no debe ofrecer Ditzy", anais.poses.contains("Ditzy"))
    }

    @Test
    fun testSlot5SlugEsElNombreDeArchivoCanonico() {
        val esperado = mapOf(
            "ele" to "ditzy",
            "miss_doll" to "glacial_command",
            "anais" to "sovereign_gaze"
        )
        CharacterProfile.ALL.forEach { profile ->
            assertEquals(esperado[profile.slug], profile.slot5Slug)
        }
    }

    @Test
    fun testAliasDitzyResuelveAlSlot5DeCadaPersonaje() {
        val missDoll = CharacterProfile.ALL.first { it.slug == "miss_doll" }
        val anais = CharacterProfile.ALL.first { it.slug == "anais" }

        assertEquals("Glacial Command", PoseMatcher.getCanonicalPose("miss_doll_021_ditzy.png", missDoll))
        assertEquals("Sovereign Gaze", PoseMatcher.getCanonicalPose("anais_017_ditzy.png", anais))
        assertEquals("Sovereign Gaze", PoseMatcher.getCanonicalPose("anais_017_sovereign_gaze.png", anais))
    }
```

**Prohibido** `assertTrue(true)` o cuerpos mockeados. El `when (selectedTab)` roto del #12 pasó en verde porque `LaVouteTests.kt` eran 310 líneas de eso.

---

## 5. Criterios de aceptación (observables, no declarativos)

1. **El selector muestra 7 chips, no 8**, en un look de Anaïs (por ejemplo el Look 17) y en uno de Miss Doll. El chip 5 dice `Sovereign Gaze` / `Glacial Command`. **`Ditzy` no aparece en ninguno de los dos.**
2. En un look de Ele el chip 5 sigue diciendo `Ditzy` y son 7 chips.
3. En un look **Boudoir** de Anaïs siguen apareciendo las 4 poses Boudoir como custom.
4. Subir el slot 5 de un look de Anaïs crea `anais_<N>_sovereign_gaze.png`. **Nunca `_ditzy.png`.**
5. `./gradlew testDebugUnitTest` pasa, incluidos los 4 tests nuevos.
6. `./gradlew assembleDebug` compila.

---

## 6. Entrega esperada (formato obligatorio)

1. **Diff completo por archivo**, tal como quedó en el código.
2. **Log real y literal** de `./gradlew assembleDebug` y `./gradlew testDebugUnitTest` — pegado, no parafraseado. Si el comando falla o no existe el wrapper, **decirlo**: ya ocurrió en este proyecto un `BUILD SUCCESSFUL` reportado junto a un `build.log` propio que decía `./gradlew: not found`.
3. **Sección "NO HECHO"** explícita: todo criterio de §5 que no se haya cumplido o verificado. Si está vacía, escribir "ninguno" — no omitirla.
4. **Hash del commit.**

> ⚠️ **AI Studio corre su propio git "Init":** sus commits viven en su sandbox y llegan a `farid77cl/LV-App` **solo cuando la Ama los pushea**. Un "listo, commit abc1234" **no significa que esté en GitHub**. La Ama debe pushear y verificar el HEAD real antes de dar el fix por aterrizado.
