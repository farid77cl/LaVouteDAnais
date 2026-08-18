# Auditoría de stack — LV-App

> **Fecha:** 2026-08-18 · **Repo:** `farid77cl/LV-App` · **HEAD auditado:** `f83dc00` (2026-08-18 09:38, versionCode 22 / versionName "4.13")
> **Método:** clon leído en scratchpad (sin escritura sobre el repo de la app) + verificación de versiones vigentes por búsqueda web el mismo día.
> **Alcance:** 32 archivos Kotlin, 8.917 líneas.

---

## 0. Verificación previa: el prompt #28 aterrizó completo

Antes de auditar el stack se comprobó el fix del slot 5 contra el código real:

| Criterio del #28 | Estado |
|---|---|
| `PromptFilterScreen.kt:493` → `val standardPoses = selectedLookProfile.poses` | ✅ aplicado (comentarios incluidos) |
| `CharacterProfile.kt:15` → `slot5Slug` derivado de `slot5Name` | ✅ aplicado |
| `GitRepository` → `profile` movido arriba + doble rama del slot 5 | ✅ aplicado |
| Bump a `versionCode 22` / `versionName "4.13"` | ✅ aplicado |
| 4 tests nuevos en `CharacterProfileTest.kt` | ✅ 8 `@Test` en total |
| Cero `assertTrue(true)` en `app/src/test/` | ✅ 0 ocurrencias |

**Pendiente de evidencia:** no se dispone del log de `./gradlew assembleDebug` / `testDebugUnitTest`. Esta máquina no tiene JDK ni Android SDK (`java: command not found`, `ANDROID_HOME` vacío), así que **la compilación no se verificó aquí**. El fix se da por aplicado en el código, no por compilado.

---

## 1. Lo que está bien (no tocar)

- **`compileSdk 36.1` / `targetSdk 36` / `minSdk 24`** — Android 16, al día.
- **KSP en vez de KAPT** para Room y Moshi. Correcto y moderno.
- **Version catalog** (`gradle/libs.versions.toml`) en vez de versiones sueltas.
- **Roborazzi + Robolectric** configurados: hay infraestructura de screenshot testing, algo que la mayoría de los proyectos de este tamaño no tiene.
- **Cero `GlobalScope`, cero `runBlocking`** en `app/src/main`.
- **Cero secretos literales en el código fuente** (se leen del `.env` vía el secrets plugin).
- **`providers.exec`** para el git SHA — es la forma compatible con configuration cache, no el `exec {}` legacy.
- **Tests reales**: los 310 renglones de `assertTrue(true)` que documentó la sesión del 23/07 ya no existen.

---

## 2. 🔴 Hallazgos graves

### 2.1 Compose BOM con casi dos años de atraso — el hallazgo principal

```toml
composeBom = "2024.09.00"      # vigente al 18/08/2026: 2026.08.00
```

Es la única pieza del proyecto que quedó anclada en 2024 mientras el resto de la toolchain avanzó a 2026. Se compila Compose de septiembre 2024 sobre **AGP 9.1.1 y compileSdk 36**: se pierden dos años de mejoras de recomposición y de APIs de Material3, y la combinación no es una que Google pruebe.

Agravante de consistencia: `androidxComposeUiTextGoogleFonts = "1.7.5"` está fijado **fuera** del BOM (y ni siquiera se usa en `dependencies`), que es exactamente lo que un BOM existe para evitar.

### 2.2 No hay librería de navegación — y ya causó un bug de producción

`navigation-compose` está declarado en el catálogo pero **comentado** en `app/build.gradle.kts`. La navegación real es un `when (selectedTab)` a mano en `LaVouteApp.kt:210`.

Ese patrón ya rompió la app una vez: el prompt #12 reordenó los rótulos de la barra sin tocar el `when`, y cada pestaña quedó dibujando la pantalla equivocada — «Relatos» abría La Flota. Con un `NavHost` ese bug es imposible de escribir. LV-App 2.0 ya lo resolvió así; v1 sigue con el patrón frágil.

> Nota: hoy lo vigente es **Navigation3**, la API Compose-first, ya estable. Para este tamaño de app, `navigation-compose` clásico también sirve y es migración más barata.

### 2.3 `androidx.media` está deprecada y en uso

```kotlin
implementation("androidx.media:media:1.7.0")   // ademas: hardcodeada, fuera del catalogo
```

Se usa en `PlaybackService.kt:62` (`androidx.media.app.NotificationCompat.MediaStyle`). Esa librería y ExoPlayer2 fueron reemplazados por **AndroidX Media3** — Google la declaró la ruta oficial en 2023 y publicó guía de migración y script.

Se suma que la reproducción va con **`MediaPlayer`** (`ElevenLabsManager.kt`), que es la raíz de los problemas de audio que este proyecto lleva arrastrando desde julio: sin streaming real, latencia hasta el último byte, pausa que re-descarga. Media3/ExoPlayer resuelve eso de fábrica, no a parche.

### 2.4 El `GITHUB_PAT` viaja dentro del APK, sin ofuscar

```kotlin
val githubToken = com.example.BuildConfig.GITHUB_PAT   // MainViewModel.kt:320, 341, 386, 408, 439
```

El secrets plugin inyecta `GITHUB_PAT` y `GEMINI_API_KEY` en `BuildConfig` en tiempo de build: quedan como **constantes de texto dentro del APK**. Y en `buildTypes.release` está `isMinifyEnabled = false`, así que no hay R8 ni ofuscación — se leen con `strings` sobre el APK.

Además `AndroidManifest.xml:12` tiene `android:allowBackup="true"`, lo que permite extraer por ADB las `SharedPreferences` de la app.

**Escala real:** es una app sideloadeada de uso personal, no está en Play, y el PAT es de la Ama sobre su propio repo. El riesgo no es teórico pero sí acotado: **se materializa el día que ese APK salga del teléfono** (se comparte, se sube, se respalda). Si eso llegara a pasar, el PAT da escritura sobre `LaVouteDAnais`.

---

## 3. 🟡 Deuda de versiones

| Librería | En el repo | Vigente (18/08/2026) | Comentario |
|---|---|---|---|
| **Compose BOM** | `2024.09.00` | **`2026.08.00`** | ~23 releases atrás. El más urgente. |
| **OkHttp** | `4.10.0` | `4.12.0` (línea 4.x) · **5.x estable** | 4.10.0 es de 2022. |
| **Coil** | `2.7.0` | **`3.5.0`** | Coil 3 cambió de coordenadas a `io.coil-kt.coil3` y de paquete (`coil3.*`); el código importa `coil.*`. |
| **Retrofit** | `2.12.0` | **`3.0.0`** | Retrofit 3 (may-2025) está reescrito en Kotlin. |
| **Lifecycle** | `2.8.7` | **`2.11.0`** | Tres artefactos fijados a 2.8.7. |
| **Room** | `2.7.0` | **Room3 `3.0.1`** | Room3 es la línea nueva (jul-2026). |
| **Kotlin** | `2.2.10` | **`2.4.10`** | Dos minors atrás. |
| **AGP** | `9.1.1` (abr-2026) | **`9.3`** (jul-2026) | Un minor atrás — aceptable. |
| **Gradle** | `9.3.1` | **`9.5.1`** | |
| **Navigation** | *(comentada)* | Navigation3 estable | Ver §2.2. |

**Orden importante:** el BOM de Compose y Kotlin/AGP se mueven juntos. No subir el BOM 23 releases sin subir Kotlin, ni al revés.

---

## 4. 🟡 Arquitectura y calidad

1. **Cero inyección de dependencias.** No hay Hilt ni Koin (`grep dagger|hilt|koin` → 0 archivos). Consecuencia visible: `MainViewModel.kt` tiene **1.080 líneas** y concentra prompts, galería, literatura, audio, subidas y descartes. Es el God object del proyecto y explica por qué los cambios de una pantalla rompen otra.

2. **Tres pantallas por encima de las 1.000 líneas:** `LiteratureScreen.kt` (1.170), `PromptFilterScreen.kt` (1.116), `ImageGalleryScreen.kt` (816). Composables de ese tamaño son inauditables y son donde han vivido los bugs (el hardcodeo del slot 5 estaba en la línea 490 de una de ellas).

3. **`SharedPreferences` en cuatro archivos** (`app_prefs`, `playback_prefs`, `crash_prefs`) mientras `androidx-datastore-preferences` está en el catálogo… comentado. DataStore es el reemplazo recomendado y ya está pagado en el catálogo.

4. **API deprecada de Material3 conviviendo con la nueva:** `Divider(` en `PromptFilterScreen.kt:405` frente a `HorizontalDivider(` en los otros cinco sitios. Cosmético, pero es señal de que el código se editó por parches sin barrido.

5. **`namespace = "com.example"`** — placeholder de plantilla. El `applicationId` sí es propio (`com.aistudio.lavoute.yznxt`, también autogenerado). No rompe nada, pero contamina todos los imports (`com.example.util.CharacterProfile`).

6. **`sourceCompatibility = JavaVersion.VERSION_11`** bajo AGP 9. Legal, pero conservador: hoy lo normal es 17 o 21, y no hay `jvmTarget` declarado para Kotlin, así que el alineamiento queda al default del plugin.

7. **`BUILD_DATE` rompe el build cache:**
   ```kotlin
   buildConfigField("String", "BUILD_DATE", "\"${Date().toString()}\"")
   ```
   Cambia en **cada** invocación de Gradle → `BuildConfig` se regenera siempre → se invalida la compilación incremental de todo lo que dependa de él. El `GIT_SHA` ya cumple la función de trazabilidad sin este costo.

8. **`ElevenLabsManager.kt:34`** crea su scope como `CoroutineScope(Dispatchers.Main + Job())`. Trabajo de red y de archivo colgando de un scope de Main; funciona porque hay `withContext` adentro, pero el default correcto es `Dispatchers.IO` o el `viewModelScope`.

9. **Catálogo kitchen-sink:** CameraX (4 artefactos), play-services-location, Accompanist, Firebase AI y DataStore están declarados y **comentados** en `dependencies`. Ruido heredado de la plantilla de AI Studio: infla el catálogo y confunde sobre qué usa realmente la app.

10. **`isMinifyEnabled = false` en release.** Sin R8: APK más grande, sin ofuscación, sin eliminación de código muerto.

---

## 5. Recomendación priorizada

No conviene tocar todo junto. Orden propuesto, de mayor retorno y menor riesgo a mayor:

| # | Acción | Por qué primero |
|---|---|---|
| **1** | **Subir Compose BOM a `2026.08.00` + Kotlin a `2.4.10`** (y AGP a 9.3 si acompaña). Nada más. | Es el atraso más grande y el que más arrastra. Se hace solo, sin tocar código de la app, y se verifica con `assembleDebug` + los tests que ya existen. |
| **2** | **Purgar el catálogo** y mover `androidx.media` al catálogo si sigue vivo. | Cero riesgo, deja el terreno legible para lo que viene. |
| **3** | **Migrar a `NavHost`** (navigation-compose). | Mata por diseño una clase entera de bugs, la que ya rompió la app en producción. |
| **4** | **Audio a Media3** (reemplaza `androidx.media` deprecada **y** `MediaPlayer` de una vez). | Resuelve de raíz el problema de latencia que lleva meses parchándose. |
| **5** | **Meter Hilt y partir `MainViewModel`** por dominio. | El de mayor beneficio estructural, pero también el de mayor superficie de rotura. Va después de que el resto esté estable. |
| **6** | OkHttp 5 · Coil 3 · Retrofit 3 · Lifecycle 2.11 · Room3. | Cada uno tiene migración con cambio de paquete o de API; uno por vez, no en bloque. |
| **7** | `isMinifyEnabled = true` + `allowBackup="false"`. | Mitiga el §2.4 sin sacar el PAT del APK. La solución de fondo sería pedir el token en la app y guardarlo cifrado, pero es rediseño de flujo. |

**Cada paso = un prompt de AI Studio, con su log de build y su sección "NO HECHO".** Este proyecto tiene historial de entregas declaradas verdes que el código desmintió (#7, #9, #11, #12): agrupar varios pasos en un solo prompt es exactamente cómo se vuelve a repetir.

---

## Fuentes de las versiones vigentes

- [Jetpack Compose — agosto '26 release](https://android-developers.googleblog.com/2026/08/jetpack-compose-august-2026-release.html) · [BOM en Maven](https://mvnrepository.com/artifact/androidx.compose/compose-bom)
- [AGP 9.3 (julio 2026)](https://developer.android.com/build/releases/agp-9-3-0-release-notes) · [AGP 9.1.1 (abril 2026)](https://developer.android.com/build/releases/agp-9-1-0-release-notes) · [Kotlin releases](https://kotlinlang.org/docs/releases.html) · [Gradle releases](https://gradle.org/releases/)
- [AndroidX Lifecycle](https://developer.android.com/jetpack/androidx/releases/lifecycle) · [AndroidX releases](https://developer.android.com/jetpack/androidx/versions) · [Navigation3](https://developer.android.com/jetpack/androidx/releases/navigation3)
- [Guía de migración a Media3](https://developer.android.com/media/media3/exoplayer/migration-guide) · [ExoPlayer deprecado](https://github.com/google/ExoPlayer)
- [Coil — upgrade a 3.x](https://coil-kt.github.io/coil/upgrading_to_coil3/) · [Retrofit 3.0 — guía de migración](https://proandroiddev.com/retrofit-3-0-0-detailed-migration-guide-0d2c043d43e3) · [OkHttp changelog](https://square.github.io/okhttp/changelogs/changelog_4x/)
