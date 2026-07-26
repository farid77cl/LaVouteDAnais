# 🚑 Prompt #13 para AI Studio — HOTFIX DE EMERGENCIA: el #12 descuadró TODA la navegación y el #11 borró el engranaje de voz y dejó el spinner mintiendo

> **Base:** repo `farid77cl/LV-App` en HEAD **`58c96ed`** ("feat: implement La Flota and add search functionality"), `versionCode = 15`, `versionName = "4.8"`.
>
> **Esto NO es una mejora — es un hotfix.** Los prompts #11 y #12 aterrizaron **a medias** y dejaron la app inusable: hoy al tocar «Relatos» NO aparece el lector (aparece La Flota), y el engranaje de configuración de voz desapareció. Todo lo de abajo está verificado leyendo el código del commit `58c96ed`, con archivo y línea. No investigues: ejecuta.
>
> **Alcance:** navegación (LaVouteApp.kt), lector de relatos (LiteratureScreen.kt) y audio (ElevenLabsManager.kt / PlaybackManager.kt). El flujo de subida de imágenes NO se toca.

---

## 🔴 DIAGNÓSTICO — con archivo y línea (verificado en `58c96ed`)

### F1 · CRÍTICO — cada pestaña dibuja la pantalla EQUIVOCADA (esto es «no puedo reproducir el relato»)

El #12 reordenó los **rótulos** de la barra de navegación (puso «La Flota» primero) pero **NO reordenó el `when (selectedTab)`** que decide qué pantalla se dibuja. Quedó descuadrado:

`LaVouteApp.kt:134-190` (lo que la Ama TOCA):
- tab 0 → «La Flota» · `selectTab(0)`
- tab 1 → «Prompts» · `selectTab(1)`
- tab 2 → «Galería» · `selectTab(2)`
- tab 3 → «Relatos» · `selectTab(3)`

`LaVouteApp.kt:207-212` (lo que se DIBUJA — quedó en el orden viejo):
```
when (selectedTab) {
    0 -> PromptFilterScreen(viewModel = viewModel)   // ❌ debería ser SummaryScreen
    1 -> ImageGalleryScreen(viewModel = viewModel)   // ❌ debería ser PromptFilterScreen
    2 -> LiteratureScreen(viewModel = viewModel)     // ❌ debería ser ImageGalleryScreen
    3 -> SummaryScreen(viewModel = viewModel)        // ❌ debería ser LiteratureScreen
}
```

Resultado real hoy:

| La Ama toca | selectTab | Pantalla que aparece |
|---|---|---|
| **La Flota** | 0 | **Prompts** ❌ |
| **Prompts** | 1 | **Galería** ❌ |
| **Galería** | 2 | **Relatos (el lector)** ❌ |
| **Relatos** | 3 | **La Flota** ❌ |

Por eso al tocar «Relatos» sale La Flota y no hay botón de reproducir. El lector quedó escondido tras «Galería». Y los saltos internos de La Flota también apuntan mal: `SummaryScreen.kt:192,344` hacen `selectTab(1)` para «ir a Prompts» → con el `when` roto muestran **Galería**; `:227,299` hacen `selectTab(2)` para «ir a Galería» → muestran **Relatos**.

> ⚠️ OJO: los `selectTab()` internos de `SummaryScreen` **ya están en el índice correcto** para el mapeo bueno (pose→`selectTab(1)`=Prompts, look→`selectTab(2)`=Galería). NO los cambies. El único defecto es el bloque `when`. Arreglar SOLO el `when` deja todo alineado.

### F2 · CRÍTICO — el engranaje de configuración de voz desapareció

El #11 **borró** el botón que abría la configuración de voz. En `LiteratureScreen.kt` se eliminó:
```
IconButton(onClick = { showTtsSettings = true }) {
    Icon(Icons.Default.Settings, contentDescription = "Configurar Voz", tint = MaterialTheme.colorScheme.primary)
}
```
La variable `showTtsSettings` sigue declarada (`LiteratureScreen.kt:199`) y el diálogo completo (selector Flash/Multilingual, velocidad, tono) sigue en el código (`if (showTtsSettings)` en `:669`), pero **NADIE lo abre**: quedó código muerto e inalcanzable. Verificado: `grep -rn "showTtsSettings = true"` en `app/src/main/` → **0 resultados**.

### F3 · CRÍTICO — el spinner nunca se apaga en la primera reproducción (el «arreglo» del #11 quedó invertido)

El #11 debía borrar SOLO el `onChunkStarted` prematuro (el del principio de `playNextChunk`) y **conservar** el de `setOnPreparedListener` (el que se dispara cuando el audio de verdad suena). En cambio **borró los dos**. En `ElevenLabsManager.kt:274-280` hoy:
```
setOnPreparedListener {
    start()
    // ← acá FALTA onChunkStarted?.invoke(currentChunkIndex)
    val prefs = ...
    prefetchNextChunk(currentChunkIndex + 1, modelId)
}
```
`onChunkStarted` solo se invoca ahora en `resume()` (`:127`), nunca en el arranque en frío. Como `_isBuffering` se apaga en ese callback (`PlaybackManager.kt:66-74`), en la PRIMERA reproducción **el spinner + «⏳ Preparando la voz…» se quedan encendidos para siempre** aunque el audio ya esté sonando. Es exactamente el síntoma «no arranca / toma siglos», reintroducido al revés.

### F4 · La velocidad de lectura (pedida en el #11 B1) nunca se cableó a ElevenLabs

`grep -rn "PlaybackParams\|setSpeed\|playbackParams"` en `app/src/main/` → **0 resultados**. `PlaybackManager.play(...)` recibe `speed` pero solo lo aplica al TTS del sistema (`:151 tts?.setSpeechRate`). `ElevenLabsManager.playTextChunks(...)` (`:138`) ni siquiera recibe `speed`. Con voz ElevenLabs la velocidad no hace nada.

### F5 · El #12 no subió la versión

`build.gradle.kts` quedó en `versionCode 15 / versionName "4.8"` — el mismo APK del #11. Dos entregas con la misma versión (el problema histórico del versionado). Este hotfix debe bumpear.

---

```
Eres el desarrollador de LV-App (Kotlin / Jetpack Compose / Room / Retrofit / Moshi / Coil).
Trabaja sobre el repo al día (base: commit 58c96ed, versionCode 15, versionName 4.8).

CONTEXTO: esto es un HOTFIX. La app está inusable: la navegación está descuadrada y el
engranaje de voz desapareció. Los defectos están sobre TU código, con archivo y línea.
No investigues ni expliques: ejecuta. Si discrepas de un diagnóstico, dilo al final en
"NO HECHO:" con evidencia.

⭐ INTOCABLE: TODO el flujo de subida de imágenes (portapapeles, selector de galería, guardia
de resolución, share, descartes). No se toca ni un archivo de esa ruta.

#####################################################################
##  F1 — DESCUADRE DE NAVEGACIÓN (el más grave, arréglalo primero)
#####################################################################

En LaVouteApp.kt, el bloque `when (selectedTab)` (:207-212) quedó en el orden viejo mientras la
barra de navegación (:134-190) ya está reordenada. Deja el `when` así, alineado con los rótulos:

    when (selectedTab) {
        0 -> SummaryScreen(viewModel = viewModel)        // La Flota  (tab 0)
        1 -> PromptFilterScreen(viewModel = viewModel)   // Prompts   (tab 1)
        2 -> ImageGalleryScreen(viewModel = viewModel)   // Galería   (tab 2)
        3 -> LiteratureScreen(viewModel = viewModel)     // Relatos   (tab 3)
    }

NO toques los selectTab() internos de SummaryScreen (:192,:227,:299,:344): ya apuntan al índice
correcto para este mapeo. El único cambio es el orden del `when`.

CRITERIO DE ACEPTACIÓN (verificable a mano en el emulador):
 - Tocar «La Flota» muestra el dashboard de flota (SummaryScreen).
 - Tocar «Relatos» muestra el LECTOR con el botón de reproducir.
 - Tocar «Galería» muestra la galería de imágenes.
 - Tocar «Prompts» muestra los prompts.
 - En La Flota, tocar una pose faltante lleva a Prompts con el prompt listo para copiar; tocar un
   look lleva a Galería en ese look.

#####################################################################
##  F2 — RESTAURAR EL ENGRANAJE DE CONFIGURACIÓN DE VOZ
#####################################################################

En LiteratureScreen.kt, dentro de la barra superior del lector (la Row que contiene el botón de
volver, el título y los controles de reproducir/detener/comentar, ~:336-482), vuelve a agregar el
botón que abre el diálogo de configuración (que sigue existiendo, `if (showTtsSettings)` en :669):

    IconButton(onClick = { showTtsSettings = true }) {
        Icon(Icons.Default.Settings, contentDescription = "Configurar Voz",
             tint = MaterialTheme.colorScheme.primary)
    }

Colócalo junto a los otros controles de la barra (por ejemplo a la derecha del botón Detener,
antes o después del botón Comentarios). Asegúrate de que `Icons.Default.Settings` esté importado.

CRITERIO DE ACEPTACIÓN: en el lector aparece un ícono de engranaje; al tocarlo se abre el diálogo
con el selector de modelo (Flash/Multilingual), velocidad y tono.

#####################################################################
##  F3 — EL SPINNER HONESTO (restaurar el onChunkStarted que se borró de más)
#####################################################################

En ElevenLabsManager.kt, dentro de `setOnPreparedListener` (:274), DESPUÉS de `start()`, vuelve a
invocar el callback que quedó eliminado por error:

    setOnPreparedListener {
        if (pausedByUser) {
            // el usuario pausó durante la carga: dejar el player preparado, NO sonar, NO apagar
            // el spinner todavía (para no mentir). Se retomará en resume().
        } else {
            start()
            onChunkStarted?.invoke(currentChunkIndex)   // ← ESTA línea es la que faltaba
        }
        val prefs = context.getSharedPreferences("app_prefs", Context.MODE_PRIVATE)
        val modelId = prefs.getString("eleven_labs_model", "eleven_flash_v2_5") ?: "eleven_flash_v2_5"
        prefetchNextChunk(currentChunkIndex + 1, modelId)
    }

NO vuelvas a poner el `onChunkStarted` prematuro al principio de `playNextChunk` (ese estuvo bien
borrarlo). El único `onChunkStarted` del arranque debe ser este, dentro de onPrepared.

CRITERIO DE ACEPTACIÓN: al tocar Reproducir por primera vez, el spinner + «Preparando la voz…» se
mantienen hasta que se oye la primera palabra y en ese instante (no antes, no nunca) se apagan y el
botón pasa a Pausa. Tocar Pausa durante «Preparando la voz…» deja isPlaying en false y NO suena
audio al terminar la descarga.

#####################################################################
##  F4 — VELOCIDAD DE LECTURA EN ELEVENLABS (cerrar lo que quedó del #11 B1)
#####################################################################

MediaPlayer soporta velocidad desde API 23 vía PlaybackParams.
 - Propaga `speed` desde PlaybackManager.play(...) → resumePlayback() → ElevenLabsManager. Hoy
   `playTextChunks(...)` (:138) no recibe speed: agrégalo como parámetro y guárdalo en un campo.
 - En setOnPreparedListener (:274), ANTES de start(), aplica la velocidad con guarda de versión y
   try/catch (setSpeed(0f) lanza excepción → coerce a mínimo 0.5f):
       try {
           if (Build.VERSION.SDK_INT >= 23) {
               playbackParams = playbackParams.setSpeed(speed.coerceIn(0.5f, 2.0f))
           }
       } catch (e: Exception) { e.printStackTrace() }
 - El diálogo de config (F2) ya tiene la sección «Velocidad» (:792). Verifica que ese valor se
   guarde en SharedPreferences ("tts_speech_rate") y que se lea al reproducir (ya se lee en
   LiteratureScreen.kt:351). Si el selector no está cableado a la pref, cabléalo.

CRITERIO DE ACEPTACIÓN: con voz ElevenLabs, poner 1.25× acelera la lectura sin cambiar el tono ni
reiniciar el capítulo.

#####################################################################
##  F5 — TESTS DE VERDAD (prohibido assertTrue(true))
#####################################################################

⚠️ El archivo app/src/test/java/com/example/ui/LaVouteTests.kt que dejó el #12 son ~310 líneas de
`assertTrue(true) // Mocked logic here, just ensuring the test name is reported`. Eso NO es un test:
por eso el `when` descuadrado pasó verde. BÓRRALO y escribe tests que fallarían si el bug estuviera
presente:

  - Mapeo de pestañas (F1): una función pura `screenForTab(tab: Int): String` (o el mapa que use el
    when) tal que screenForTab(0)=="Flota", (1)=="Prompts", (2)=="Galería", (3)=="Relatos". El test
    verifica los 4. Debe fallar si se vuelve a intercambiar cualquier par.
  - Spinner (F3): con un ElevenLabsApiService falso lento, isBuffering sigue true hasta que el
    player queda preparado y se invoca onChunkStarted; ANTES, true; DESPUÉS, false.
  - Pausa durante carga (F3): pausar antes de onPrepared deja isPlaying en false y no arranca audio.
  - Velocidad (F4): playTextChunks recibe y conserva el speed pasado.

Corre con --rerun-tasks y pega la SALIDA REAL COMPLETA con los NOMBRES de los tests. Ningún test
puede ser `assertTrue(true)`. "BUILD SUCCESSFUL" suelto no cuenta.

#####################################################################
##  F6 — ENTREGA Y VERSIONADO
#####################################################################

1. Sube versionCode a 16 y versionName a "4.9" en build.gradle.kts (el #12 se olvidó de bumpear y
   quedó en 15/"4.8", igual que el #11). Es parte del entregable.
2. Verifica que la cabecera siga mostrando versionName + versionCode + hash de commit (ya existe,
   LaVouteApp.kt:72).
3. Commit + push reales. Pega la salida de `git rev-parse HEAD` y de `git log --oneline -5`.
4. Declara el keystore usado y si coincide con la entrega anterior.
5. El APK.
6. Sección final obligatoria "NO HECHO:" con una línea por punto no logrado. Vacía + un test de F5
   que falle = entrega no verificada.
```

---

## 📌 Nota de prioridad para la Ama

| Prioridad | Punto | Por qué |
|---|---|---|
| 🥇 | **F1** (navegación) | Es reordenar 4 líneas del `when`. Sin esto la app es inusable: «Relatos» no lleva al lector. |
| 🥈 | **F2** (engranaje) | Restaurar un botón. Sin esto no podés cambiar la voz ni la velocidad. |
| 🥉 | **F3** (spinner honesto) | Una línea. Sin esto el audio parece que nunca arranca. |
| 4 | **F4** (velocidad ElevenLabs) | Cierra lo que el #11 prometió y no hizo. |
| 5 | **F5 + F6** (tests reales + versión) | Para que esto no vuelva a pasar en silencio. |

**Lo honesto:** este prompt no agrega nada nuevo — repara lo que el #11 y el #12 rompieron. El
streaming con ExoPlayer (viejo #13 condicionado) queda para MÁS ADELANTE: primero hay que tener la
app usable y el spinner honesto para poder medir el TTFA de verdad (con el spinner roto esa medición
nunca fue real).
