# 🧹 Prompt #20 · LV-App 2.0 — PASO 1.1: Saneamiento del Esqueleto

> **Parche del P1** (convención `xx.x` para pasos que aterrizan con deuda).
> **Contexto:** el P1 aterrizó **funcionalmente correcto** — commit `250beb6` en `farid77cl/LV-app-2`, código viejo `com/example/*` borrado de verdad, estructura `com.lavoute.app` completa, SDK 36, test real. Pero la auditoría del repo (26/07/2026) encontró **6 deudas** que el reporte de AI Studio no mencionó y que hay que cerrar ANTES del P2.
> **No toca funcionalidad.** Ni una pantalla nueva.

---

## 🩺 Lo que encontró la auditoría (evidencia)

| # | Hallazgo | Evidencia en el repo | Por qué importa |
|---|---|---|---|
| 1 | **Compose BOM fosilizado en `2024.09.00`** | `gradle/libs.versions.toml:12` | El prompt pedía "última estable". Es de ~2 años atrás: material3 viejo, y el P2/P4 (Coil3, Media3) van a chocar con él |
| 2 | **El `libs.versions.toml` NO se regeneró — se heredó de la app vieja** | el commit cambió **6 líneas** de 120; arrastra Firebase, Room, Retrofit, CameraX, Roborazzi, Moshi, credentials… | Es la causa raíz del #1, y contradice el "borrón total" |
| 3 | **No existe el Gradle wrapper en el repo** | no hay `gradlew`, `gradlew.bat` ni `gradle/wrapper/`; `build.log` (commiteado) dice literalmente `sh: 1: ./gradlew: not found` | Un `git clone` **no puede compilar**. Y contradice el "BUILD SUCCESSFUL in 13s" del reporte |
| 4 | **`debug.keystore` referenciado pero gitignoreado** | `app/build.gradle.kts:19-26` lo exige · `.gitignore` lo excluye | Build debug roto en cualquier clon; revienta el P8 (APK) |
| 5 | **Tema de plantilla sin renombrar y en claro** | `themes.xml` → `Theme.MyApplication`, parent `android:Theme.DeviceDefault.NoActionBar` | Flash blanco al abrir, contra el fondo OLED `#0B0612` del canon |
| 6 | **Restos de plantilla vivos** | `app/src/androidTest/java/com/example/ExampleInstrumentedTest.kt` (asegura `packageName == "com.example"` → **fallará**, el applicationId ahora es `com.lavoute.app`) · `app/src/test/screenshots/greeting.png` · `build.log` commiteado | Test que va a reventar en el P8 + basura en el repo |

---

## 📋 PROMPT PARA PEGAR EN AI STUDIO

```markdown
PASO 1.1 de LV-App 2.0: SANEAMIENTO del esqueleto. NO agregues funcionalidad,
NO crees pantallas nuevas, NO toques la navegación ni el tema por personaje.
Solo cierra las 6 deudas de abajo y deja el repo limpio y clonable.

=====================================================================
## 1. Compose BOM y dependencias al día
=====================================================================
- `gradle/libs.versions.toml` tiene `composeBom = "2024.09.00"`. Es de ~2 años atrás.
  SÚBELO a la ÚLTIMA VERSIÓN ESTABLE del Compose BOM.
- Actualiza también a su última estable: androidx-core-ktx, activity-compose,
  navigation-compose, lifecycle-viewmodel-compose.
- Recordatorio de la regla que ya rompimos una vez: si algo exige un compileSdk
  mayor, SUBE el compileSdk. Nunca bajes librerías para que compile.

=====================================================================
## 2. Purga el catálogo de versiones (viene heredado de la app vieja)
=====================================================================
`gradle/libs.versions.toml` arrastra el catálogo COMPLETO de la app anterior:
Firebase, Room, Retrofit, Moshi, OkHttp, CameraX, Coil, Media3, Robolectric,
Roborazzi, accompanist, play-services-location, credentials, googleid, KSP,
secrets-gradle-plugin, google-services.

Déjalo SOLO con lo que el P1 usa hoy:
  [versions]  agp · kotlin · composeBom · coreKtx · activityCompose ·
              navigationCompose · lifecycleViewmodelCompose · junit
  [libraries] androidx-compose-bom · androidx-compose-material3 ·
              androidx-activity-compose · androidx-navigation-compose ·
              androidx-lifecycle-viewmodel-compose · androidx-core-ktx · junit
  [plugins]   android-application · kotlin-android · kotlin-compose

Cada paso siguiente (P2…P8) agregará SUS propias entradas cuando le toque, ya en
versión actual. Esto es parte del borrón total: el catálogo también se rehace.

=====================================================================
## 3. Commitea el Gradle wrapper
=====================================================================
El repo NO tiene `gradlew`, `gradlew.bat` ni `gradle/wrapper/`. Por eso el
`build.log` que quedó commiteado dice `sh: 1: ./gradlew: not found`.
- Genera el wrapper con una versión de Gradle compatible con el AGP en uso.
- COMMITEA `gradlew`, `gradlew.bat`, `gradle/wrapper/gradle-wrapper.jar` y
  `gradle/wrapper/gradle-wrapper.properties` (el wrapper SIEMPRE va al repo).
- Verifica que `./gradlew tasks` corre de verdad antes de decir que está listo.

=====================================================================
## 4. Saca el keystore del build
=====================================================================
`app/build.gradle.kts` define un `signingConfigs.create("debugConfig")` que apunta
a `${rootDir}/debug.keystore`, pero ese archivo está en `.gitignore` → en cualquier
clon el build debug falla.
- ELIMINA ese bloque `signingConfigs` y la línea `signingConfig = ...` del buildType
  debug. Usa el debug signing por defecto de AGP.
- El keystore de release se resolverá en el P8, no ahora.

=====================================================================
## 5. Tema de la app (renombrar + oscuro)
=====================================================================
- `res/values/themes.xml`: renombra `Theme.MyApplication` → `Theme.LVApp`.
- Parent oscuro sin action bar, y agrega
  `<item name="android:windowBackground">#0B0612</item>` para que no haya flash
  blanco al abrir (el fondo OLED del canon).
- Actualiza `android:theme` en el AndroidManifest.

=====================================================================
## 6. Borra los restos de plantilla
=====================================================================
- BORRA `app/src/androidTest/java/com/example/ExampleInstrumentedTest.kt`
  (afirma `packageName == "com.example"`; el applicationId ahora es
  `com.lavoute.app`, así que ese test está condenado a fallar).
- BORRA `app/src/test/screenshots/greeting.png`.
- BORRA `build.log` del repo y agrégalo a `.gitignore` (los logs no se commitean).
- Crea los paquetes del andamiaje que faltan, cada uno con un `.gitkeep`:
  `com/lavoute/app/domain/`, `com/lavoute/app/data/`, `com/lavoute/app/service/`.

=====================================================================
## DISCIPLINA DE COMPILACIÓN (anti-timeout)
=====================================================================
- UNA sola compilación a la vez. Si una quedó colgada, mátala antes de lanzar otra.
- Deja lista TODA la configuración y compila UNA vez, limpio.

=====================================================================
## CRITERIO DE ÉXITO DEL PASO 1.1
=====================================================================
- `./gradlew assembleDebug` y `./gradlew test` corren desde el repo limpio.
- `DestinationsTest` sigue pasando.
- La app abre igual que antes: 5 pestañas, chips de personaje recolorean en vivo,
  header "LV-App 2.0 · v1.0". Sin flash blanco al abrir.
- El repo no tiene `build.log`, ni archivos en `com/example`.

=====================================================================
## AL TERMINAR, REPORTA (texto, fuera del código)
=====================================================================
- Versión FINAL de: Compose BOM · core-ktx · activity-compose · navigation-compose ·
  lifecycle-viewmodel-compose · AGP · Kotlin · Gradle (wrapper).
- La salida LITERAL de `./gradlew assembleDebug` y de `./gradlew test`
  (pega las últimas líneas reales, no un resumen).
- Lista de archivos borrados.
- Si NO pudiste hacer alguno de los 6 puntos, dilo explícitamente en vez de omitirlo.
```

---

## ✅ Cómo verificar antes del P2
1. Que el reporte traiga la **salida literal** de `./gradlew`, no "Build succeeded".
2. Que el Compose BOM sea del 2026, no del 2024.
3. Que en el repo aparezcan `gradlew` + `gradle/wrapper/` y **desaparezcan** `build.log` y `com/example/`.
4. **Pushear** desde AI Studio (sus commits no llegan a GitHub hasta que la Ama pushea).
5. Verde → **P2 (Pestaña Visual)**.

> ⚠️ **Repo nuevo:** LV-App 2.0 vive en `farid77cl/LV-app-2`, no en `farid77cl/LV-App` (ese quedó con la era v4.12).
