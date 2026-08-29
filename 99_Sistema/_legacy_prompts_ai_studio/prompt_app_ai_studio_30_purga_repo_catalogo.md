# Prompt AI Studio #30 — Paso 2: purga del repo y del catálogo de dependencias

> **Fecha:** 2026-08-18
> **Repo:** `LV-App` · **Medido sobre HEAD `0c2b7c7`** (versionCode 23 / versionName "4.14")
> **Paso 2 de 7** de `99_Sistema/auditoria_stack_lv_app_20260818.md`. Este prompt **borra archivos muertos y entradas de catálogo muertas. No cambia ni una versión de dependencia** — eso fue el #29 y lo que viene son los pasos 3 a 7.

---

## 1. Por qué

Auditado el índice de git: **109 archivos trackeados son basura de trabajo** — scripts desechables de edición, salidas de prueba y un árbol de código duplicado. Se fueron acumulando commit a commit y hoy son más archivos que el código real de la app (32 `.kt` en `app/src/main`).

Y no es solo ruido cosmético. `app/applet/app/src/main/java/com/example/util/PoseMatcher.kt` es una **copia vieja** del matcher con la lista de poses hardcodeada:

```kotlin
val CANONICAL_POSES = listOf(
    "Standing", "Back View", "Seated", "Side Profile", "Ditzy", "POV", "Odalisque"
)
```

Es exactamente el bug que se arregló en el #28. Hoy no entra al build (`settings.gradle.kts` solo declara `include(":app")` y el árbol vive fuera de `app/src`), pero es una mina esperando que alguien la incluya o la copie.

En el catálogo, aparte: **51 alias declarados, 41 en uso**. Diez están muertos.

---

## 2. Cambios requeridos

### A. Borrar los 109 archivos basura

```bash
git rm -r --cached -q app/applet          # arbol de codigo duplicado (1 archivo)
git rm -q *.py                            # 72 scripts desechables en la raiz
git rm -q app/*.js app/app/test.js workspace/fetch2.js   # ~26 scripts de sondeo
git rm -q app/TestRegex.java
git rm -q app/test_output.txt app/api_test_output.txt
rm -rf app/applet workspace
```

Las familias, para que se reconozcan y no quede ninguna:

| Familia | Dónde | Cuántos |
|---|---|---|
| `fix_*.py`, `run_*.py`, `test_*.py`, `modify_*.py`, `rewrite_*.py`, `patch_repo.py`, `commit_push.py`, `generate_test.py`, `append_imagenote_dialog.py`, `add_filters_sheet.py`, `find_zero_brace.py`, `print_dialog.py`, `remove_size_restriction.py`, `revert_paste_btn.py`, `update_viewmodel.py` | raíz | **72** |
| `check*.js`, `download*.js`, `fetch.js`, `test_db.js`, `test_regex.js`, `app/app/test.js` | `app/` | **33** (incluye `TestRegex.java`) |
| `app/applet/**` | `app/` | **1** |
| `app/test_output.txt`, `app/api_test_output.txt`, `workspace/fetch2.js` | varios | **3** |

**Lo que NO se toca bajo ninguna circunstancia:** `app/src/**` · `gradle/**` · `gradlew`, `gradlew.bat` · `build.gradle.kts`, `app/build.gradle.kts`, `settings.gradle.kts` · `.gitignore`, `app/.gitignore` · `.env.example` (lo necesita el secrets plugin como `defaultPropertiesFileName`) · `app/proguard-rules.pro` · `debug.keystore` si estuviera trackeado.

### B. `.gitignore` — que no vuelva a pasar

Agregar al `.gitignore` de la raíz:

```gitignore
# --- Scratch de herramientas (no commitear) ---
/scratch/
/fix_*.py
/run_*.py
/patch_*.py
/rewrite_*.py
/modify_*.py
/check*.js
/download*.js
*_output.txt
```

**Convención a respetar de aquí en adelante:** todo script de edición o sondeo de un solo uso va a `/scratch/`, que está ignorado. **No se commitea.** Si un script merece quedarse, se le pone nombre propio, se documenta y se mueve a una carpeta `tools/` — no se deja `fix_profile4.py` en la raíz.

### C. Purga del catálogo — 10 entradas muertas

En `gradle/libs.versions.toml`, borrar la entrada de `[libraries]` **y** su línea de `[versions]`:

| Alias a borrar | `[versions]` a borrar | Evidencia de que está muerto |
|---|---|---|
| `accompanist-permissions` | `accompanistPermissions` | 0 usos. `MainActivity.kt:52` pide POST_NOTIFICATIONS con `requestPermissions()` del framework. |
| `play-services-location` | `playServicesLocation` | 0 usos de `FusedLocation`/`LocationServices`; el manifest no declara permisos de ubicación. |
| `androidx-camera-camera2` | `cameraCamera2` | 0 usos de CameraX. La app no toma fotos: lee de la galería. |
| `androidx-camera-lifecycle` | `cameraLifecycle` | ídem |
| `androidx-camera-view` | `cameraView` | ídem |
| `androidx-camera-core` | `cameraCore` | ídem |
| `firebase-ai` | — | 0 referencias a Firebase en `app/src`. |
| `firebase-bom` | `firebase-bom` | ídem. **Además hay que borrar la línea ACTIVA** `implementation(platform(libs.firebase.bom))` de `app/build.gradle.kts`: es un BOM sin ningún artefacto detrás, no aporta nada. No existe `google-services.json` ni el plugin `google-services`. |
| `compose-markdown` | `composeMarkdown` | Nunca se menciona en `dependencies`, ni comentado. El markdown lo renderiza `compose-richtext`, que sí está activo. |

**Borrar también las líneas comentadas correspondientes** en `app/build.gradle.kts` (`// implementation(libs.accompanist.permissions)`, las cuatro de camera, `// implementation(libs.play.services.location)`, `// implementation(libs.firebase.ai)`).

#### 🚨 Dos entradas que se CONSERVAN comentadas — no borrarlas

| Alias | Por qué se queda |
|---|---|
| `androidx-navigation-compose` | Es la dependencia del **paso 3** (migrar el `when (selectedTab)` de `LaVouteApp.kt:210` a `NavHost`). |
| `androidx-datastore-preferences` | Es el reemplazo de las `SharedPreferences` en un paso posterior. |

Dejarlas tal cual están hoy: declaradas en el catálogo y comentadas en `dependencies`.

### D. `androidx.media` al catálogo

En `app/build.gradle.kts` hay una dependencia con versión hardcodeada, fuera del catálogo:

```kotlin
implementation("androidx.media:media:1.7.0")
```

Moverla al catálogo por consistencia:

```toml
# [versions]
androidxMedia = "1.7.0"
# [libraries]
androidx-media = { group = "androidx.media", name = "media", version.ref = "androidxMedia" }
```
```kotlin
// app/build.gradle.kts
implementation(libs.androidx.media)
```

> **No migrar a Media3 aquí.** `androidx.media` está deprecada y se reemplaza en el paso 4; mientras tanto, que al menos su versión viva donde viven todas.

### E. Sacar `BUILD_DATE`, que rompe el build cache

```kotlin
// BORRAR esta linea de defaultConfig:
buildConfigField("String", "BUILD_DATE", "\"${Date().toString()}\"")
```
y el `import java.util.Date` de la primera línea del archivo, si queda sin uso.

Cambia en **cada** invocación de Gradle, así que `BuildConfig` se regenera siempre y se invalida la compilación incremental de todo lo que dependa de él. **Verificado: `BUILD_DATE` tiene 0 referencias en `app/src`** — la trazabilidad ya la da `GIT_SHA`, que sí se usa en la cabecera (`LaVouteApp.kt:79`).

### F. Versión

`versionCode = 24` · `versionName = "4.15"`.

---

## 3. 🚫 Qué NO hacer

- **No** cambiar ninguna versión de dependencia. El #29 acaba de mover el bloque de toolchain y hay que poder distinguir qué rompió qué.
- **No** introducir Navigation, Hilt ni Media3. Son los pasos 3, 4 y 5.
- **No** tocar `app/src/**` salvo lo que exija E (que no toca `app/src`: es solo `app/build.gradle.kts`). O sea: **este prompt no modifica ni un archivo `.kt` de la app.**
- **No** borrar `.env.example`.
- **No** borrar `androidx-navigation-compose` ni `androidx-datastore-preferences`.
- **No** activar `isMinifyEnabled` ni tocar `targetSdk` / `compileSdk`.
- **No** "aprovechar el viaje" para reformatear archivos o reordenar imports: el diff tiene que ser legible como borrado puro.

---

## 4. Criterios de aceptación

1. `git ls-files | grep -cE "\.(js|py)$"` → **0**.
2. `git ls-files | grep -c "applet"` → **0**.
3. `git ls-files | grep -c "_output.txt"` → **0**.
4. `git ls-files | wc -l` bajó en **109** exactos respecto de `0c2b7c7`.
5. `git ls-files app/src | wc -l` **no cambió** (el código de la app está intacto).
6. `grep -c "firebase" gradle/libs.versions.toml app/build.gradle.kts` → **0** en ambos.
7. `grep -c "navigation-compose\|datastore-preferences" gradle/libs.versions.toml` → **2** (siguen ahí).
8. `grep -c "BUILD_DATE" app/build.gradle.kts app/src -r` → **0**.
9. `./gradlew assembleDebug` compila.
10. `./gradlew testDebugUnitTest` pasa, incluidos los 8 `@Test` de `CharacterProfileTest.kt`.
11. La cabecera muestra `v4.15 (24) · <sha>`.

---

## 5. Entrega esperada (formato obligatorio)

1. **Diff de los archivos de configuración** (`libs.versions.toml`, `app/build.gradle.kts`, `.gitignore`) completo. Para los 109 borrados basta la lista de rutas, no el contenido.
2. **La salida literal de los comandos de los criterios 1-8**, pegada.
3. **Log real y literal** de `./gradlew assembleDebug` y `./gradlew testDebugUnitTest`. Si un comando falla o no se puede ejecutar, **decirlo explícitamente**.
   > El #29 se entregó **sin ningún log de build** — el único archivo de salida que trajo era la prueba del parser, no una compilación. Este paso borra 109 archivos: sin log, no hay forma de saber que el proyecto sigue compilando.
4. **Sección "NO HECHO"** explícita con cada criterio de §4 no cumplido o no verificado. Si está vacía, escribir "ninguno" — no omitirla.
5. **Hash del commit.**

> ⚠️ **AI Studio corre su propio git "Init":** sus commits llegan a `farid77cl/LV-App` **solo cuando la Ama los pushea**. Pushear y verificar el HEAD real antes de dar el paso por cerrado.
