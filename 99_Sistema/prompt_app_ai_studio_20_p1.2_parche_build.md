# 🔧 Prompt #20 · LV-App 2.0 — PASO 1.2: Parche de Build del Esqueleto

> **Segundo parche del P1** (convención `xx.x` para pasos que aterrizan con deuda).
> **Contexto:** el P1.1 (saneamiento) aterrizó **a medias** — commit `24cf4d4` en `farid77cl/LV-app-2`, mensaje "chore: update project dependencies and build config". Cerró 4 de sus 6 puntos (wrapper commiteado ✅, keystore fuera ✅, `Theme.LVApp` oscuro ✅, restos de plantilla borrados + paquetes `domain/data/service` creados ✅), pero **dejó vivo el punto #2 (purgar el catálogo)** y **subió el Compose BOM sólo hasta 2025.02.00** (no a la última estable). Además, la auditoría del código (26/07/2026) encontró **una deuda nueva que el P1.1 no cubría**: el plugin de Kotlin-Android no se aplica.
> **No toca funcionalidad.** Ni una pantalla nueva. Solo deja el build limpio, mínimo y demostrablemente compilable.

---

## 🩺 Lo que encontró la auditoría del clon `24cf4d4` (evidencia)

| # | Hallazgo | Evidencia en el repo | Por qué importa |
|---|---|---|---|
| 1 | **`org.jetbrains.kotlin.android` NO se aplica en ningún build script** | `app/build.gradle.kts:1-4` aplica solo `android.application` + `kotlin.compose`; el root `build.gradle.kts:1-4` igual; el plugin está **definido pero muerto** en `gradle/libs.versions.toml:112` | Sin el plugin de Kotlin, un toolchain AGP 8.x **no compila `.kt`**. Aquí es **AGP 9.1.1**, que trae Kotlin integrado experimental — así que puede compilar igual, o puede fallar. **Hay que MEDIRLO, no asumirlo** (aplicarlo a ciegas puede *chocar* con el built-in). Es el hallazgo #1 porque decide si la app buildea |
| 2 | **El catálogo de versiones sigue SIN purgar** (P1.1 #2 quedó pendiente) | `gradle/libs.versions.toml` = **119 líneas**, **56 referencias** a Firebase, Room, Retrofit, CameraX, Media3, Moshi, OkHttp, Coil, accompanist, credentials, googleid, DataStore, Roborazzi, KSP, secrets, google-services | El "borrón total" nunca se completó: el catálogo es el de la app vieja. Ruido que arrastra plugins/libs que este paso no usa y que envejecen mal |
| 3 | **Compose BOM y libs core no están en la última estable** | `gradle/libs.versions.toml`: `composeBom = "2025.02.00"` (~1.5 años atrás para 07/2026) | El P1.1 pedía "última estable" y quedó a medias. El P2/P4 (Coil3, Media3) van a chocar con un BOM viejo |
| 4 | **`resolver.gradle.kts` huérfano en la raíz** | archivo `resolver.gradle.kts` define `configurations{create("myConf")}` + tarea `resolveBom` con `compose-bom:+` (versión dinámica); **no lo aplica nadie** (`settings`/`build.gradle.kts` no lo referencian) | Script muerto de andamiaje. Usa versión dinámica (mala práctica) y confunde al que abre el repo |
| 5 | **`backup_rules.xml` y `data_extraction_rules.xml` huérfanos** | existen en `res/xml/`; el `AndroidManifest.xml` tiene `allowBackup="true"` pero **no** referencia `android:fullBackupContent` ni `android:dataExtractionRules` | Recursos muertos: o se cablean o se borran. No pasa nada grave, pero es basura de plantilla |
| 6 | **`colors.xml` conserva los colores de plantilla de Android Studio** | `res/values/colors.xml` → `purple_200/500/700`, `teal_200/700`, sin uso (el color real vive en `ui/theme/Color.kt`) | Restos de plantilla, contradicen el "borrón total" |

---

## 📋 PROMPT PARA PEGAR EN AI STUDIO

```markdown
PASO 1.2 de LV-App 2.0: PARCHE DE BUILD del esqueleto. NO agregues funcionalidad,
NO crees pantallas nuevas, NO toques la navegación, el tema por personaje ni el
DestinationsTest. Solo cierra las 6 deudas de abajo y deja el repo con un build
LIMPIO, MÍNIMO y DEMOSTRABLEMENTE compilable.

Repo: farid77cl/LV-app-2 · paquete com.lavoute.app · estado actual: commit 24cf4d4.

=====================================================================
## 0. PRIMERO MIDE (no asumas) — esto decide el punto 1
=====================================================================
Antes de cambiar nada, corre UNA vez y GUARDA la salida literal:
    ./gradlew :app:assembleDebug --stacktrace
    ./gradlew :app:testDebugUnitTest
Necesito ver si el código Kotlin compila HOY tal como está. No resumas: pega las
últimas líneas reales (BUILD SUCCESSFUL o el error exacto).

=====================================================================
## 1. Plugin de Kotlin-Android: diagnostica y resuelve (NO a ciegas)
=====================================================================
Hoy `app/build.gradle.kts` aplica solo `android.application` + `kotlin.compose`
(el compilador de Compose), y NO aplica `org.jetbrains.kotlin.android`, aunque
está definido en el catálogo (`libs.versions.toml`, alias `kotlin-android`).
AGP 9.1.1 puede traer soporte de Kotlin integrado, así que hay dos escenarios y
debes elegir según lo que dio el punto 0:

  (a) Si el build de Kotlin FALLÓ en el punto 0 (p.ej. "no Kotlin compile task",
      ".kt sin compilar", o error del plugin de Compose por falta del de Kotlin):
      → APLICA el plugin de Kotlin-Android:
          - root build.gradle.kts:  alias(libs.plugins.kotlin.android) apply false
          - app/build.gradle.kts:   alias(libs.plugins.kotlin.android)  // dentro de plugins {}
        (mantén también kotlin.compose; van juntos en Kotlin 2.x).

  (b) Si el build de Kotlin FUNCIONÓ tal cual (AGP 9 ya provee Kotlin integrado):
      → NO agregues el plugin (chocaría con el integrado). En su lugar ELIMINA la
        entrada MUERTA `kotlin-android` del `[plugins]` del catálogo, para que
        nadie crea que se usa.

En AMBOS casos, al final el estado debe ser coherente: o el plugin está aplicado y
en el catálogo, o no está aplicado y tampoco en el catálogo. Nada de plugins
definidos-pero-muertos. REPORTA cuál de los dos escenarios fue, con la evidencia
del punto 0.

=====================================================================
## 2. Purga el catálogo de versiones (deuda heredada del P1.1 #2)
=====================================================================
`gradle/libs.versions.toml` sigue con el catálogo COMPLETO de la app vieja
(Firebase, Room, Retrofit, Moshi, OkHttp, CameraX, Coil, Media3, Robolectric,
Roborazzi, accompanist, play-services-location, credentials, googleid, KSP,
secrets-gradle-plugin, google-services, datastore).

Déjalo SOLO con lo que el P1 usa hoy:
  [versions]  agp · kotlin · composeBom · coreKtx · activityCompose ·
              navigationCompose · lifecycleViewmodelCompose · junit
  [libraries] androidx-compose-bom · androidx-compose-material3 ·
              androidx-activity-compose · androidx-navigation-compose ·
              androidx-lifecycle-viewmodel-compose · androidx-core-ktx · junit
  [plugins]   android-application · kotlin-compose
              (+ kotlin-android SOLO si el punto 1 escenario (a) lo aplicó)

Cada paso siguiente (P2…P8) agregará SUS propias entradas cuando le toque, ya en
versión actual. El catálogo también se rehace: es parte del borrón total.

=====================================================================
## 3. Compose BOM y libs core a la ÚLTIMA ESTABLE REAL
=====================================================================
`composeBom` quedó en 2025.02.00. Súbelo a la ÚLTIMA VERSIÓN ESTABLE real del
Compose BOM (verifícala, no inventes un número). Sube también a su última estable
core-ktx, activity-compose, navigation-compose y lifecycle-viewmodel-compose.
- Si algo exige un compileSdk mayor, SUBE el compileSdk. Nunca bajes librerías
  para que compile.
- Si 2025.02.00 resultara ser de verdad la última estable que resuelve, déjalo y
  DILO explícitamente en el reporte (no lo dejes callado).

=====================================================================
## 4. Borra el script huérfano resolver.gradle.kts
=====================================================================
En la raíz hay un `resolver.gradle.kts` con una configuración `myConf` y una tarea
`resolveBom` que usa `compose-bom:+` (versión dinámica). No lo aplica nadie.
BÓRRALO del repo.

=====================================================================
## 5. Cablea o borra las reglas de backup huérfanas
=====================================================================
`res/xml/backup_rules.xml` y `res/xml/data_extraction_rules.xml` existen pero el
Manifest no los referencia. Deja el estado coherente (elige UNA):
  - Referéncialos en <application>: android:fullBackupContent="@xml/backup_rules"
    y android:dataExtractionRules="@xml/data_extraction_rules"; o
  - Bórralos si no los vas a usar.
No los dejes huérfanos.

=====================================================================
## 6. Limpia colors.xml de la plantilla
=====================================================================
`res/values/colors.xml` conserva purple_200/500/700 y teal_200/700 de la plantilla
de Android Studio, sin uso (el color real vive en ui/theme/Color.kt). Bórralos.
Deja colors.xml vacío (o solo con los colores que de verdad referencie el XML).

=====================================================================
## DISCIPLINA DE COMPILACIÓN (anti-timeout)
=====================================================================
- UNA sola compilación a la vez. Si una quedó colgada, mátala antes de lanzar otra
  (dos builds de Gradle en paralelo se pelean el daemon y ninguna termina).
- Deja lista TODA la configuración y compila UNA vez, limpio. No compiles "para ir
  viendo". Si el build falla, arregla la causa; no reintentes esperando otro resultado.

=====================================================================
## CRITERIO DE ÉXITO DEL PASO 1.2
=====================================================================
- `./gradlew :app:assembleDebug` y `./gradlew :app:testDebugUnitTest` corren desde
  el repo limpio y terminan en BUILD SUCCESSFUL.
- `DestinationsTest` sigue pasando.
- La app abre IGUAL que antes: 5 pestañas, chips de personaje recolorean en vivo,
  header "LV-App 2.0 · v1.0". Sin flash blanco al abrir.
- `libs.versions.toml` quedó chico (solo lo que el P1 usa) y sin entradas muertas.
- No queda `resolver.gradle.kts`, ni recursos de backup huérfanos, ni colores de
  plantilla sin uso.

=====================================================================
## AL TERMINAR, REPORTA (texto, fuera del código)
=====================================================================
- La salida LITERAL del punto 0 (assembleDebug + test ANTES de tocar nada) y la
  salida LITERAL de assembleDebug + test DESPUÉS de los cambios. Últimas líneas
  reales, no un resumen.
- Qué escenario del punto 1 fue (a) o (b), con la evidencia que lo decidió.
- Versión FINAL de: Compose BOM · core-ktx · activity-compose · navigation-compose ·
  lifecycle-viewmodel-compose · AGP · Kotlin · Gradle (wrapper).
- Lista de archivos borrados y de líneas quitadas del catálogo (de 119 a cuántas).
- Si NO pudiste hacer alguno de los 6 puntos, dilo explícitamente en vez de omitirlo.
```

---

## ✅ Cómo verificar antes del P2
1. Que el reporte traiga la **salida literal** de `./gradlew` **antes y después** — no "Build succeeded".
2. Que quede claro el **escenario del punto 1** (plugin aplicado vs. built-in de AGP 9) y que **no queden plugins muertos** en el catálogo.
3. Que `libs.versions.toml` haya **bajado de 119 líneas** a lo mínimo (sin firebase/room/retrofit/camera/media3…).
4. Que en el repo **desaparezcan** `resolver.gradle.kts` y los colores de plantilla.
5. **Pushear** desde AI Studio (sus commits no llegan a GitHub hasta que la Ama pushea).
6. Verde → **P2 (Pestaña Visual)**.

> ⚠️ **Repo:** LV-App 2.0 vive en `farid77cl/LV-app-2`, no en `farid77cl/LV-App` (ese quedó con la era v4.12).
> ⚠️ **Método:** este parche **diagnostica antes de tocar** (punto 0). El plugin de Kotlin NO se agrega a ciegas: con AGP 9.1.1 el Kotlin integrado puede hacer que aplicarlo *choque*. Se mide, se decide, se reporta la evidencia.
