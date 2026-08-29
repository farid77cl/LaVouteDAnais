# Prompt AI Studio #29 — Paso 1 de modernización: Compose BOM + Kotlin + toolchain

> **Fecha:** 2026-08-18
> **Repo:** `LV-App` · **Medido sobre HEAD `f83dc00`** (versionCode 22 / versionName "4.13")
> **Este prompt sube versiones y NADA MÁS.** Es el paso 1 de 7 de `99_Sistema/auditoria_stack_lv_app_20260818.md`. Los pasos siguientes (navegación, Media3, Hilt, Coil/OkHttp/Retrofit) tienen su propio prompt y **no van aquí**.

---

## 1. Por qué

El Compose BOM del proyecto está en `2024.09.00`. Lo vigente al 18/08/2026 es `2026.08.00`: unas 23 releases de atraso. Es la única pieza anclada en 2024 mientras AGP, Gradle, Kotlin y `compileSdk` avanzaron a 2026 — se está compilando Compose de septiembre de 2024 sobre AGP 9.1.1 y `compileSdk 36`, una combinación que Google no prueba.

**Restricción que manda el salto:** a partir de **Compose 1.12.0** se exige `compileSdk 37` y AGP 9. Y **todos** los BOM de 2026 mapean a Compose UI 1.12.0 / Material3 1.4.0 — no existe un BOM 2026 intermedio que evite el `compileSdk 37`. Por eso este paso mueve el bloque completo de toolchain de una sola vez: son requisitos encadenados, no un capricho.

**Encadenamiento verificado:**
- Compose 1.12.0 → exige `compileSdk 37` + AGP 9
- AGP 9.3 → exige **Gradle ≥ 9.5.0** y **JDK ≥ 17**; soporta hasta API 37; SDK Build Tools ≥ 36.0.0
- Kotlin 2.4.10 → pareja de KSP **2.3.10**

---

## 2. Cambios exactos

### 2.1 `gradle/libs.versions.toml`

```toml
# ANTES -> DESPUES
agp = "9.1.1"                  ->  agp = "9.3.0"
kotlin = "2.2.10"              ->  kotlin = "2.4.10"
composeBom = "2024.09.00"      ->  composeBom = "2026.08.00"
googleDevtoolsKsp = "2.3.5"    ->  googleDevtoolsKsp = "2.3.10"
```

**Eliminar además este pin, que contradice el BOM:**

```toml
androidxComposeUiTextGoogleFonts = "1.7.5"
```
y su entrada de librería `androidx-compose-ui-text-google-fonts`. Está fijada **fuera** del BOM (versión de la era Compose 1.7, 2024) y **no se usa en `dependencies`** — verificarlo antes de borrar con una búsqueda de `androidx.compose.ui.text.googlefonts` en `app/src/main`. Si apareciera algún uso, entonces **no** borrarla: quitarle el `version.ref` para que la gobierne el BOM.

> El plugin del compilador de Compose (`org.jetbrains.kotlin.plugin.compose`) usa `version.ref = "kotlin"`, así que sube solo con Kotlin. No agregar una versión aparte.

### 2.2 `gradle/wrapper/gradle-wrapper.properties`

```properties
# ANTES
distributionUrl=https\://services.gradle.org/distributions/gradle-9.3.1-bin.zip
# DESPUES
distributionUrl=https\://services.gradle.org/distributions/gradle-9.5.1-bin.zip
```

AGP 9.3 tiene **mínimo Gradle 9.5.0**; con 9.3.1 el build falla al arrancar.

### 2.3 `app/build.gradle.kts` — `compileSdk` y versión de la app

```kotlin
// ANTES
compileSdk { version = release(36) { minorApiLevel = 1 } }
// DESPUES
compileSdk { version = release(37) }
```

```kotlin
// ANTES            // DESPUES
versionCode = 22    versionCode = 23
versionName = "4.13"  versionName = "4.14"
```

**`targetSdk` se queda en 36. No tocarlo.** Subir `targetSdk` activa cambios de comportamiento en tiempo de ejecución (permisos, background, almacenamiento) y merece su propio paso con pruebas en el teléfono. `compileSdk 37` + `targetSdk 36` es una combinación válida y es la conservadora.

### 2.4 `PromptFilterScreen.kt:405` — única ruptura de código conocida

`Divider` está deprecado desde Material3 1.2 y con M3 1.4.0 se espera que ya no compile. Es **la única** aparición en el proyecto (los otros cinco sitios ya usan `HorizontalDivider`):

```kotlin
// ANTES
Divider(color = MaterialTheme.colorScheme.outline, thickness = 1.dp)
// DESPUES
HorizontalDivider(color = MaterialTheme.colorScheme.outline, thickness = 1.dp)
```

> Ya verificado que **no** rompen: los `LinearProgressIndicator` (`LaVouteApp.kt:226`) y `CircularProgressIndicator` (`LightboxViewer.kt:299`) usan las sobrecargas indeterminadas, que siguen vigentes. Y **no hay iconos sin AutoMirrored** en el proyecto (`ArrowBack`, `List`, `Send`, etc. → 0 apariciones).

---

## 3. Puntos de riesgo — reportar, NO improvisar

1. **SDK Platform 37 debe estar instalado** en el entorno de build. Si no lo está, el build falla con "failed to find target with hash string android-37". **Instalarlo. Si no se puede, DETENERSE y reportarlo** — no bajar el BOM en silencio para que compile.
2. **JDK 17 mínimo** (AGP 9.3). Si el entorno corre con menos, reportarlo.
3. **Roborazzi `1.59.0` y Robolectric `4.16.1`** siguen de cerca la versión de Compose. Si los tests dejan de compilar por eso, **reportar el error literal y proponer la versión compatible; no adivinar un número ni desactivar los tests**.
4. **Material3 1.4.0 puede haber removido más APIs** además de `Divider`. Si aparece otro error de compilación: **pegar el error literal y proponer el reemplazo equivalente**. Prohibido "arreglarlo" borrando la funcionalidad, comentando la línea o bajando el BOM.
5. `compileOptions` se queda en `JavaVersion.VERSION_11`. No es requisito de este salto y cambiarlo agrega superficie de rotura — va en un paso posterior.

---

## 4. 🚫 Qué NO hacer en este prompt

- **No** subir `targetSdk`.
- **No** tocar Coil, OkHttp, Retrofit, Room, Lifecycle ni Moshi. Cada uno cambia de paquete o de API y tiene su propio paso.
- **No** introducir Navigation ni Hilt.
- **No** tocar `MainViewModel`, `GitRepository`, `CharacterProfile`, `PoseMatcher` ni `PromptFilterScreen` **más allá** de la línea 405. El fix del slot 5 acaba de aterrizar (commit `f83dc00`) y debe quedar intacto.
- **No** descomentar dependencias del catálogo (CameraX, location, DataStore, Accompanist, Firebase AI). La purga es el paso 2.
- **No** activar `isMinifyEnabled`.

---

## 5. Criterios de aceptación

1. `./gradlew assembleDebug` compila.
2. `./gradlew testDebugUnitTest` pasa, **incluidos los 8 `@Test` de `CharacterProfileTest.kt`** (los 4 del slot 5 entre ellos).
3. `grep -rn "Divider(" app/src/main --include=*.kt | grep -v HorizontalDivider | grep -v VerticalDivider` → **0 resultados**.
4. La cabecera de la app muestra `v4.14 (23) · <sha>`.
5. En un look de Anaïs el selector sigue mostrando **7 chips** con `Sovereign Gaze` en el quinto — la regresión del #28 no volvió.
6. La app abre, la galería carga imágenes y el lector de relatos abre. (Verificación visual mínima: este salto toca el renderizado de toda la UI.)

---

## 6. Entrega esperada (formato obligatorio)

1. **Diff completo por archivo.**
2. **Log real y literal** de `./gradlew assembleDebug` y de `./gradlew testDebugUnitTest` — pegado, no parafraseado. Si un comando falla o el wrapper no existe, **decirlo**: en este proyecto ya se reportó un `BUILD SUCCESSFUL` junto a un `build.log` propio que decía `./gradlew: not found`.
3. **Sección "NO HECHO"** explícita, con cada criterio de §5 que no se haya cumplido o verificado. Si está vacía, escribir "ninguno" — no omitirla.
4. **Hash del commit.**
5. Si algo de §3 obligó a desviarse del plan, decir **qué** se cambió y **por qué**, antes que entregarlo como si hubiera salido según lo pedido.

> ⚠️ **AI Studio corre su propio git "Init":** sus commits llegan a `farid77cl/LV-App` **solo cuando la Ama los pushea**. Un "listo, commit abc1234" no significa que esté en GitHub — pushear y verificar el HEAD real.

---

## Fuentes

- [Jetpack Compose — release de agosto '26](https://android-developers.googleblog.com/2026/08/jetpack-compose-august-2026-release.html)
- [Mapeo BOM → versiones de librería](https://developer.android.com/develop/ui/compose/bom/bom-mapping)
- [AGP 9.3.0 — notas de la versión](https://developer.android.com/build/releases/agp-9-3-0-release-notes)
- [Kotlin — releases](https://kotlinlang.org/docs/releases.html) · [KSP — quickstart y compatibilidad](https://kotlinlang.org/docs/ksp-quickstart.html)
- [Gradle — releases](https://gradle.org/releases/)
