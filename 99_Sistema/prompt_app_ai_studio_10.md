# 📱 Prompt #10 para AI Studio — La galería se rehace por OUTFIT + pase de imágenes + el spinner que nunca para + el versionado

> **Base:** repo `farid77cl/LV-App` en el commit **`7d36560`** ("build: bump version to 4.6 and fix
> list key collisions"), `versionCode = 13`, `versionName = "4.6"`.
>
> **Todo lo de abajo está verificado leyendo el código clonado de ese commit, con archivo y línea.**
> No hay que investigarlo: hay que ejecutarlo.

---

## 🔍 AUDITORÍA DEL #9 — qué llegó de verdad y qué no

AI Studio reportó el #9 completo. Al leer el código, la realidad es esta:

| Punto #9 | Estado real | Evidencia |
|---|---|---|
| A1 Pantalla completa inmersiva | 🐞 **ESCRITO PERO NO FUNCIONA** | `LightboxViewer.kt:79-86` — el `DisposableEffect` está **fuera** del `Dialog` |
| A2 Chrome que se autooculta | ✅ Hecho | `LightboxViewer.kt:99-106`, `157` |
| A3 Botón Fit ⇄ Fill | ✅ Hecho | `LightboxViewer.kt:98`, `204-217` |
| A4 Miniaturas con `.size()` | ⚠️ **A MEDIAS** | `SkeletonImage.kt:61` acepta `size`… y `ImageGalleryScreen.kt:867` **no se lo pasa nunca** |
| A4 Quitar `allowHardware(false)` global | ✅ Hecho | solo queda en la descarga (`ImageGalleryScreen.kt:652`), que es lo correcto |
| A5 Animación que se repite al reciclar | ❌ **NO HECHO** | `ImageGalleryScreen.kt:806-826` sigue igual |
| A5 Borrar el bucle de hover | ❌ **NO HECHO** | `ImageGalleryScreen.kt:837-847` sigue igual |
| A6 Limpieza de código muerto | ⚠️ A medias | el estado se borró; siguen 12 imports muertos + `imageRatings` (`:97`) |
| A7 Filtros en filas | ✅ Hecho | `ImageGalleryScreen.kt:264-364` |
| A8 Densidad 3 pasos | ✅ Hecho | `ImageGalleryScreen.kt:170-187` |
| A9 Descartar desde el visor | ✅ Hecho | `LightboxViewer.kt:220-227` |
| B1 Primer trozo chico | ✅ Hecho | `LiteratureScreen.kt:339-346` (250 / 600 / 1500) |
| B2 Prefetch | ✅ Hecho | `ElevenLabsManager.kt:176-192`, `249-256` |
| B3 Modelo flash elegible | ✅ Hecho | `LiteratureScreen.kt:661-678`, default `eleven_flash_v2_5` |
| B4 `prepareAsync()` | ✅ Hecho | `ElevenLabsManager.kt:257` |
| B5 Pausa real | ✅ Hecho | `ElevenLabsManager.kt:107-123` |
| B6 Caché por hash + purga | ✅ Hecho… **con una trampa** (ver C3) | `ElevenLabsManager.kt:194-200`, `53-85` |
| B7 "Preparando la voz…" + errores visibles | 🐞 **ROTO / NO HECHO** | ver C1 y C2 |

**Traducción:** lo que la Ama pidió y sigue sin ver —**pantalla completa de verdad**, **fluidez al
desplazar**, y **que ElevenLabs arranque**— es exactamente lo que quedó roto o sin hacer.

---

## 🔍 Diagnóstico C — los cuatro defectos vivos, con línea

### C1 · El botón de reproducir se queda cargando PARA SIEMPRE (esto es lo que se siente como "no arranca")

`PlaybackManager.kt:153` y `:180` ponen `_isBuffering.value = true` al empezar a reproducir.
Solo vuelve a `false` en `pause()` (`:168`) y `stop()` (`:190`).
**`onChunkStarted` (`:66-73`) NUNCA lo apaga.**

Y `LiteratureScreen.kt:393-401` dibuja el botón así: si `isBuffering` → `CircularProgressIndicator`;
si no → Play/Pause. O sea: **desde el primer toque el botón es un spinner eterno**, aunque el audio ya
esté sonando. No hay ninguna señal de que empezó, y el botón nunca vuelve a ser Pausa.

### C2 · Los errores de ElevenLabs son mudos

`ElevenLabsManager` expone `onError` (`:37`) y lo invoca bien (`:169`, `:223`, `:230`).
**`PlaybackManager` nunca se lo asigna** — en `init` (`:65-77`) solo conecta `onChunkStarted` y
`onPlaybackFinished`. Resultado: sin crédito, sin internet y clave mala se ven **exactamente igual**:
spinner eterno y silencio. La usuaria no puede distinguir un fallo de una espera.

### C3 · La caché se puede envenenar sola (y entonces ese párrafo queda roto para siempre)

`ElevenLabsManager.kt:196` escribe **directo al archivo final** `tts_<hash>.mp3` y `:198` acepta como
válido cualquier archivo que exista y pese más de 0 bytes.
Si el job se cancela a mitad de descarga (`stop()`, cerrar el relato, cambiar de capítulo — todos
llaman a `currentJob?.cancel()`), queda un **mp3 truncado** que a partir de ahí se sirve como bueno.

Peor: `playNextChunk` (`:150-173`) y `prefetchNextChunk` (`:176-192`) pueden pedir **el mismo índice a
la vez** (si el trozo N termina antes de que el prefetch de N+1 baje). Son **dos `FileOutputStream`
sobre el mismo archivo** → audio corrupto y el doble de créditos gastados.

### C4 · Pausar mientras carga no pausa nada

Si se toca pausa durante la síntesis del primer trozo: `PlaybackManager.pause()` (`:166`) llama a
`elevenLabsManager.pause()`, que hace `mediaPlayer?.pause()` — pero `mediaPlayer` **todavía es null**.
La descarga sigue viva y, al terminar, `playFile` **arranca el audio igual**, con `_isPlaying` en
`false`. La app queda sonando mientras la UI dice que está pausada.

---

## 🔍 Diagnóstico D — EL VERSIONADO (lo que pidió revisar la Ama)

Esto no es cosmético: **es la razón por la que nunca se puede confirmar qué APK está instalado**, que
ya costó una auditoría entera (el batch de miniaturas L791-L800: 38 imágenes subidas chicas *después*
de la guardia, sin poder saber si el teléfono tenía el APK con la guardia o el anterior).

1. **El `versionCode` 12 está repetido.** `ae37798` y `5350266` son builds distintos y ambos declaran
   `versionCode = 12`, `versionName = "4.5"`. Dos APK diferentes que se presentan como el mismo.
2. **Los commits que importaron no bumpearon nada.** `6a26f70` (#8, la guardia de resolución) y
   `2831d1d` (#9, caché TTS + grilla) **no tocaron `build.gradle.kts`**: los dos salieron al teléfono
   diciendo **"4.5"**, el mismo string que el APK anterior al arreglo. Por eso no se pudo verificar.
3. **Saltos sin explicación en el `versionCode`:** 1 → 3 → 7 → 9 → 10 → 12 → 13. Hay bumps hechos
   fuera de git.
4. **La UI solo muestra `versionName`** (`LaVouteApp.kt:69`: "Vault de d'Anaïs v4.6"). Sin
   `versionCode`, sin hash de commit, sin fecha de build. Desde el teléfono es **imposible** saber qué
   código está corriendo.
5. **La firma no está garantizada.** `debug.keystore` está en `.gitignore` y `my-upload-key.jks` no
   existe en el repo (`build.gradle.kts:23-34`). Cada entorno que reconstruye firma con una llave
   distinta → Android rechaza la instalación ("aplicación no instalada") y obliga a **desinstalar**,
   lo que borra prefs, la base Room, las etiquetas de outfit y el progreso de lectura.
6. **`applicationId = "com.aistudio.lavoute.yznxt"`** (`:14`) tiene pinta de generado con sufijo
   aleatorio. Si alguna regeneración lo cambia, el APK se instala **al lado** del anterior como app
   distinta, y va a parecer que "la actualización no se aplicó".
7. **La raíz del repo tiene 133 archivos, 119 de ellos scripts `fix_*.py` desechables**, más
   `tailwind.config.js`, `theme.css`, `TestParse.kt`, `test_gesture.kt`, `app/RegexTest.kt`,
   `app/RegexTest2.kt` y un módulo duplicado completo en `app/applet/app/src/…`. Basura de andamiaje
   commiteada.

---

```
Eres el desarrollador de LV-App (Kotlin / Jetpack Compose / Room / Retrofit / Moshi / Coil).
Trabaja sobre el repo al día (base: commit 7d36560, versionCode 13, versionName 4.6).

CONTEXTO: los defectos de abajo están diagnosticados sobre TU código, con archivo y línea.
No investigues ni expliques por qué pasó: ejecuta. Si discrepas de un diagnóstico, dilo al
final bajo "NO HECHO:" con la evidencia. No lo ignores en silencio.

⭐ INTOCABLE: el flujo de subida de imágenes (portapapeles, selector de galería, guardia de
400.000 px² como precondición de uploadImageToGithub, ImageSource en el mensaje de commit,
pantalla de share recortada). Se arregló en el #8 y funciona. No se refactoriza, no se
"mejora de paso", no se toca ni un archivo de esa ruta.

⚠️ AVISO: en el #9 se reportaron como hechos varios puntos que no lo estaban (A4 a medias,
A5 sin tocar, A1 escrito en el lugar equivocado). En este prompt cada punto tiene un criterio
de aceptación verificable. Si no se cumple, va en "NO HECHO:".

#####################################################################
##  PARTE A — LA GALERÍA SE REHACE: NAVEGAR POR OUTFIT, NO POR FOTOS SUELTAS
#####################################################################

La pantalla de Galería hoy es un río plano de miles de fotos sueltas con cuatro filas de
chips permanentes arriba. La dueña de la app no busca "una foto": busca UN OUTFIT y quiere
verlo entero. La unidad de navegación tiene que ser el LOOK.

=====================================================================
A1. MODO OUTFIT — la grilla pasa a ser una tarjeta por look (nuevo, es el corazón del prompt)
=====================================================================
Agrega a ImageGalleryScreen un modo de vista con dos estados, guardado en SharedPreferences
("gallery_view_mode", default = OUTFITS):

    👗 OUTFITS  (default) — una tarjeta por look
    🖼️ FOTOS            — el río plano de hoy, tal cual está

En modo OUTFITS:
- Agrupa `filteredImages` por `lookNumber` (los que tengan lookNumber != null).
- Una tarjeta por look, ordenada por número descendente (lo más nuevo primero) salvo que el
  selector de orden diga otra cosa.
- Portada de la tarjeta: la imagen con poseName "standing" (comparación case-insensitive);
  si no existe, la primera del grupo.
- Sobre la portada, abajo, un degradado y dos líneas:
      L### · <nombre del look>            ← de LookEntity.name
      <N>/7 fotos · <outfitType>          ← N = tamaño del grupo
- Toque en la tarjeta = abre el LightboxViewer **con las imágenes de ESE look**, ordenadas por
  el orden canónico de poses: standing, back, seated, profile, ditzy, pov, odalisque, y al
  final cualquier otra.
- El contador de arriba pasa a decir "Mostrando X outfits · Y fotos".

CRITERIO DE ACEPTACIÓN: al abrir la Galería se ven tarjetas de outfit, una por look, no fotos
sueltas repetidas del mismo look.

=====================================================================
A2. PASE DE IMÁGENES (SLIDESHOW) DENTRO DEL VISOR — pedido explícito
=====================================================================
En LightboxViewer, junto a los botones del chrome, agrega ▶ "Pase de imágenes":

- Al activarlo, avanza solo a la página siguiente del pager cada N segundos
  (`pagerState.animateScrollToPage`), con la transición suave que ya existe.
- N configurable: toque largo en el botón abre un menú 2 s / 4 s / 7 s. Default 4 s,
  guardado en SharedPreferences ("slideshow_interval_ms").
- Da la vuelta al llegar al final (vuelve a la primera del look) y sigue hasta que se detenga.
- Cualquier interacción de la usuaria (toque, swipe, zoom) DETIENE el pase. El botón cambia a
  ⏸ mientras corre.
- Mientras el pase está activo: el chrome se oculta a los 2,5 s como ya hace, y la pantalla NO
  se debe apagar — pon `keepScreenOn = true` en la ventana del diálogo mientras dure el pase, y
  devuélvelo a false al detenerlo o al cerrar el visor (en el mismo onDispose).
- Precarga la imagen siguiente antes de mostrarla, para que nunca aparezca el esqueleto en
  medio del pase:
      LaunchedEffect(pagerState.currentPage) {
          images.getOrNull(pagerState.currentPage + 1)?.let { next ->
              context.imageLoader.enqueue(ImageRequest.Builder(context).data(next.downloadUrl).build())
          }
      }

CRITERIO DE ACEPTACIÓN: abro un outfit, toco ▶, y las 7 poses pasan solas cada 4 segundos a
pantalla completa sin que yo toque nada y sin que la pantalla se apague.

=====================================================================
A3. PANTALLA COMPLETA DE VERDAD — el #9 puso el arreglo en el lugar equivocado
=====================================================================
LightboxViewer.kt:79-86 tiene el DisposableEffect que esconde las barras del sistema, pero está
ARRIBA del `Dialog(...)` de la línea 88. Ahí `LocalView.current.parent` es la ventana de la
Activity, NO un DialogWindowProvider: el cast da null, `controller` queda null, y las barras
**no se esconden nunca**. Por eso la foto sigue enmarcada.

MUEVE ese bloque completo DENTRO del contenido del Dialog (después de la línea 91, junto a
`var visible by remember`), sin cambiar una letra de su cuerpo. Ahí `LocalView.current` sí es
la vista del diálogo y el cast resuelve.

CRITERIO DE ACEPTACIÓN: con el visor abierto no se ve ni la barra de estado ni la de
navegación, y la foto ocupa el alto físico completo. Al cerrar, las barras vuelven.

=====================================================================
A4. LOS FILTROS SE COLAPSAN (pedido explícito) — hoy comen media pantalla
=====================================================================
ImageGalleryScreen.kt:242-366 dibuja CUATRO filas de chips (POSE, ESTILO, COLOR, ETIQ) siempre
visibles, más el bloque "FILTROS ACTIVOS" (:369-561). Antes de ver la primera foto hay que
pasar por todo eso.

Reemplázalo por UNA sola barra fija de una línea:

    [🔍 Buscar…]  [⚙️ Filtros ③]  [👗/🖼️]  [▦ densidad]

- El botón "Filtros" abre un ModalBottomSheet con TODO lo que hoy está suelto: POSE, ESTILO,
  COLOR, ETIQUETA, Carpeta y Orden — cada grupo con su rótulo y sus chips, y un botón
  "Limpiar todo" abajo. El sheet es desplazable; las filas COLOR y ETIQUETA siguen colapsadas
  con "+N más" si pasan de 12 chips, como ya funciona.
- El número en el botón (③) es la cantidad de filtros activos. Sin filtros activos, sin badge.
- Los chips ya NO viven en la grilla. La primera fila de imágenes tiene que quedar visible
  apenas se abre la pestaña.
- El bloque "VISOR DE IMÁGENES" colapsable de :141-238 se va: su única información útil (el
  contador) se muestra como texto chico en la barra.

CRITERIO DE ACEPTACIÓN: al entrar a Galería, la primera fila de outfits se ve sin desplazar.

=====================================================================
A5. FLUIDEZ — "dale fluidez a las imágenes" (esto es A4+A5 del #9, que no se hicieron)
=====================================================================
Tres causas medidas de que la grilla se sienta pesada y salte:

a) Cada tarjeta decodifica el PNG completo (669×1200). `SkeletonAsyncImage` ya acepta el
   parámetro `size` (SkeletonImage.kt:61) pero ImageCard no se lo pasa (ImageGalleryScreen.kt:867).
   Pásalo: `.size(coil.size.Size(400, 720))` en la grilla. El visor sigue pidiendo nativa.

b) ImageGalleryScreen.kt:806-826: un LaunchedEffect con key `image.path` que hace
   `delay(index*50)` + tres animaciones de 600 ms. Como la grilla recicla, **cada tarjeta que
   vuelve a entrar en pantalla se reanima**: aparece tarde, escalando y trepando. BÓRRALO
   entero (las tres Animatable incluidas). La grilla ya tiene `animateItem()`, que basta.

c) ImageGalleryScreen.kt:837-847: un `pointerInput` con `while(true) awaitPointerEvent()` por
   tarjeta esperando eventos Enter/Exit que **no existen en pantalla táctil**. `isHovered` es
   siempre false. BÓRRALO junto con `isHovered` y `imageScale`.

Y una cuarta, del layout: la tarjeta usa `wrapContentHeight()` + `ContentScale.FillWidth` con
`defaultMinSize(200.dp)` (:859-875). La altura real solo se conoce cuando llega el bitmap, así
que la grilla **salta y se recalcula** mientras carga. Pon relación fija:
`Modifier.fillMaxWidth().aspectRatio(2f/3f)` + `ContentScale.Crop`. El layout deja de moverse.

CRITERIO DE ACEPTACIÓN: desplazar la grilla de arriba a abajo y de vuelta no re-anima ninguna
tarjeta ni cambia la altura de las filas ya vistas.

=====================================================================
A6. LIMPIEZA REAL EN ImageGalleryScreen.kt (el #9 la dejó a medias)
=====================================================================
`imageRatings` (:97) se colecta y no se usa en ninguna parte. Imports muertos que quedaron:
HorizontalPager, rememberPagerState, detectTransformGestures, detectHorizontalDragGestures,
ArrowBack, ArrowForward, LazyVerticalGrid, ClipData, ClipboardManager, FilterDropdown,
verticalScroll/rememberScrollState, foundation.Image y coil AsyncImage. Bórralos. No agregues
funcionalidad para justificarlos.

#####################################################################
##  PARTE B — ELEVENLABS: QUE SE VEA QUE ARRANCÓ, Y QUE ARRANQUE
#####################################################################

El #9 ya hizo lo estructural (trozo inicial de 250, prefetch, flash, prepareAsync, caché).
Lo que queda es lo que hace que SE SIENTA colgado y lo que lo puede dejar roto de verdad.

=====================================================================
B1. EL SPINNER QUE NUNCA PARA (arreglo de mayor impacto de esta parte)
=====================================================================
`_isBuffering` se enciende en PlaybackManager.kt:153 y :180 y solo se apaga en pause() (:168)
y stop() (:190). `onChunkStarted` (:66-73) no lo apaga. Y LiteratureScreen.kt:393 dibuja un
CircularProgressIndicator mientras esté encendido. O sea: el botón queda cargando para siempre
aunque el relato ya se esté oyendo.

- En el callback `onChunkStarted` de PlaybackManager, agrega `_isBuffering.value = false`.
- Mientras esté en true, muestra junto al botón el texto "⏳ Preparando la voz…" (hoy solo hay
  un spinner mudo), y quítalo en cuanto se apague.

CRITERIO DE ACEPTACIÓN: al empezar a oírse la primera palabra, el botón muestra el icono de
Pausa, no un spinner.

=====================================================================
B2. LOS FALLOS DEJAN DE SER MUDOS
=====================================================================
`ElevenLabsManager.onError` (:37) se invoca correctamente en :169, :223 y :230, pero
PlaybackManager nunca lo asigna (init, :65-77). En init, conéctalo:

      elevenLabsManager?.onError = { msg ->
          _isBuffering.value = false
          _isPlaying.value = false
          // Toast con el mensaje real en el hilo principal
      }

Sin crédito, sin internet y clave inválida tienen que verse distinto entre sí. Hoy los tres son
silencio.

=====================================================================
B3. LA CACHÉ NO SE PUEDE ENVENENAR
=====================================================================
`downloadAudio` (ElevenLabsManager.kt:194-235) escribe directo sobre `tts_<hash>.mp3` y :198
acepta como válido cualquier archivo con length > 0. Si se cancela la corrutina a mitad
(stop / cerrar relato / cambiar de capítulo), queda un mp3 truncado servido como bueno para
siempre.

- Descarga a `tts_<hash>.mp3.part` y haz `renameTo(destino final)` SOLO al terminar de copiar.
- En catch/finally, si la corrutina se canceló, borra el `.part`.
- Al iniciar (purgeOldCache), borra todos los `.part` que hayan quedado de sesiones anteriores.

=====================================================================
B4. NO PEDIR EL MISMO TROZO DOS VECES
=====================================================================
`playNextChunk` (:150-173) y `prefetchNextChunk` (:176-192) pueden pedir el mismo índice a la
vez si el trozo N termina antes de que baje el prefetch de N+1: dos descargas y dos escritores
sobre el mismo archivo.

Cambia `prefetchCache: MutableMap<Int, File>` por `MutableMap<Int, Deferred<File?>>`:
- prefetch guarda el `Deferred` (async), no el File.
- `playNextChunk`, si hay un Deferred para ese índice, hace `await()` en vez de lanzar una
  descarga nueva.
- Mantén como máximo UN trozo adelantado, como ya hace.

=====================================================================
B5. PAUSAR MIENTRAS CARGA TIENE QUE PAUSAR
=====================================================================
Si se toca pausa durante la síntesis del primer trozo, `mediaPlayer` todavía es null: el
`pause()` no hace nada, la descarga sigue y al terminar `playFile` arranca el audio igual, con
la UI diciendo "pausado".

Agrega a ElevenLabsManager una bandera `pausedByUser`:
- `pause()` la pone en true (además del `mediaPlayer?.pause()`).
- `resume()` la pone en false; si `mediaPlayer` es null y hay un chunk pendiente, reanuda la
  reproducción de ese chunk.
- En `setOnPreparedListener`, si `pausedByUser` es true: NO llames a `start()`; deja el player
  preparado esperando.

=====================================================================
B6. EL TROCEADO SALE DEL HILO PRINCIPAL
=====================================================================
LiteratureScreen.kt:332-379 hace todo el troceado dentro del onClick del botón: dos Regex sobre
el texto completo (los capítulos reales pesan 70-100 KB), un split, y un bucle con
`replace(Regex("\\s+"))` por párrafo. Todo en el hilo principal, antes de que salga el primer
byte a la red.

- Muévelo a `withContext(Dispatchers.Default)` dentro de un `rememberCoroutineScope().launch`,
  y enciende "Preparando la voz…" apenas se toca el botón.
- Cachea los chunks calculados por `file.path` en el ViewModel: volver a tocar Reproducir sobre
  el mismo capítulo no debe recalcularlos.

=====================================================================
B7. DEJAR DE ROMPER LA CACHÉ DEL TEXTO
=====================================================================
LiteratureScreen.kt:297 arma la URL con `?v=${System.currentTimeMillis()}`, así que cada vez que
se abre un capítulo se re-descarga entero desde raw.githubusercontent, siempre. Usa el `sha` del
LiteratureEntity como parámetro (`?v=${file.sha}`): misma frescura cuando el archivo cambia,
caché de verdad cuando no.

=====================================================================
B8. MEDIR, NO ADIVINAR
=====================================================================
Registra en Logcat con tag "TTFA" los milisegundos entre el toque de Reproducir y el primer
`onChunkStarted`. Pega en la entrega el valor real de una corrida sobre un capítulo de más de
10.000 palabras. El objetivo sigue siendo **menos de 2 segundos**.

#####################################################################
##  PARTE C — VERSIONADO Y TRAZABILIDAD (pedido explícito de la Ama)
#####################################################################

Problema de fondo: desde el teléfono es imposible saber qué código está instalado, y ya pasó
que dos APK distintos se presentaran como "4.5" (los commits 6a26f70 y 2831d1d no bumpearon
nada; ae37798 y 5350266 comparten versionCode 12). Eso costó una auditoría entera de imágenes
que no se pudo concluir.

C1. TODO commit que cambie código de la app sube `versionCode` en 1 y `versionName` en 0.1.
    Sin excepciones. Es parte del entregable, no un paso opcional al final.

C2. `versionCode` estrictamente monotónico y sin repetir. Parte de 14 en este prompt
    (versionName "4.7").

C3. La app tiene que decir QUÉ build es. Agrega en build.gradle.kts:

        val gitSha = providers.exec { commandLine("git","rev-parse","--short","HEAD") }
            .standardOutput.asText.get().trim()
        buildConfigField("String", "GIT_SHA", "\"$gitSha\"")
        buildConfigField("String", "BUILD_DATE", "\"${java.time.LocalDate.now()}\"")

    Y en LaVouteApp.kt:69, donde hoy dice "Vault de d'Anaïs v4.6", muestra:
        v${BuildConfig.VERSION_NAME} (${BuildConfig.VERSION_CODE}) · ${BuildConfig.GIT_SHA}
    Con toque largo sobre ese texto: copiar al portapapeles esa línea + BUILD_DATE. Así una
    captura de pantalla basta para saber qué está instalado.

C4. `applicationId = "com.aistudio.lavoute.yznxt"` queda CONGELADO. Ninguna regeneración puede
    cambiarlo: si cambia, el APK se instala al lado del anterior como app distinta y parece que
    la actualización no se aplicó. Si alguna herramienta lo cambia, revertirlo es obligatorio.

C5. Firma estable. `debug.keystore` está en .gitignore y `my-upload-key.jks` no existe en el
    repo (build.gradle.kts:23-34), así que cada entorno firma distinto y Android rechaza la
    instalación encima ("aplicación no instalada"), obligando a desinstalar y perder base de
    datos, etiquetas y progreso de lectura. En la entrega, DECLARA con qué keystore se firmó el
    APK y si es la misma de la entrega anterior. Si no lo es, avísalo en grande: hay que
    desinstalar primero.

C6. Limpieza de raíz: la raíz tiene 133 archivos, 119 de ellos scripts `fix_*.py` de andamiaje,
    más tailwind.config.js, theme.css, TestParse.kt, test_gesture.kt, app/RegexTest.kt,
    app/RegexTest2.kt y un módulo duplicado entero en app/applet/app/src/. Bórralos en un commit
    aparte, titulado "chore: limpiar andamiaje de la raíz", sin mezclarlo con los cambios
    funcionales. Si alguno de esos scripts es necesario para el build, dilo en NO HECHO en vez
    de borrarlo.

#####################################################################
##  PARTE D — TESTS QUE EJERZAN LA RUTA
#####################################################################

  - Buffering (B1): tras invocar onChunkStarted, PlaybackManager.isBuffering.value == false.
  - Error (B2): con un ElevenLabsApiService falso que devuelva 401, isBuffering e isPlaying
    quedan en false y el mensaje de error llega al callback (no queda en silencio).
  - Caché parcial (B3): un archivo `tts_x.mp3.part` en cacheDir NO se sirve como audio válido;
    tras una descarga cancelada no queda ningún .mp3 en la carpeta.
  - Doble pedido (B4): al empezar el trozo 0, el contador de llamadas del servicio falso llega
    a 2 y NO a 3; y si el trozo 0 termina antes que baje el 1, sigue siendo 2 (no 3).
  - Pausa durante carga (B5): pausar antes de que el player esté preparado deja isPlaying en
    false y NO arranca audio al completarse la descarga.
  - Troceado (B6): un texto de 5.000 caracteres da primer trozo <= 250 y segundo <= 600, sin
    cortar palabras, y la concatenación reproduce el original.
  - Agrupación por outfit (A1): dada una lista de ImageEntity de 3 looks con 7, 4 y 1 imágenes,
    la agrupación produce 3 tarjetas y la portada del primero es la pose "standing".
  - Orden canónico (A1): las poses de un look se ordenan standing, back, seated, profile,
    ditzy, pov, odalisque.
  - Visor inmersivo (A3): el LightboxViewer se compone con decorFitsSystemWindows = false Y el
    DisposableEffect está dentro del Dialog (verificable porque el controller no es null).

Corre con --rerun-tasks y pega la SALIDA REAL COMPLETA con los NOMBRES de los tests ejecutados.
"BUILD SUCCESSFUL" suelto o "N up-to-date" no cuentan como evidencia.

#####################################################################
##  PARTE E — ENTREGA
#####################################################################

1. Commit + push reales. Pega la SALIDA de `git rev-parse HEAD` (no describas el comando).
2. Pega la salida de `git log --oneline -5`.
3. Declara versionCode y versionName finales (deben ser 14 y "4.7").
4. Declara con qué keystore se firmó el APK y si coincide con la entrega anterior.
5. El APK.
6. Sección final obligatoria "NO HECHO:" con una línea por punto que no se pudo hacer. Un
   pendiente declarado vale más que un test verde inventado. Si esta sección viene vacía y
   algún punto de la Parte D falla, la entrega completa se considera no verificada.
```

---

## 📌 Nota de prioridad para la Ama

Si AI Studio se corta a medio camino, el orden de valor es:

| Prioridad | Punto | Por qué |
|---|---|---|
| 🥇 | **A3** (mover el DisposableEffect) | Es literalmente mover un bloque de 8 líneas y recupera la pantalla completa que pidió en el #9 y no llegó. |
| 🥈 | **B1** (el spinner que nunca para) | Es una línea. Es lo que hace que ElevenLabs *parezca* que nunca arranca aunque ya esté sonando. |
| 🥉 | **A1 + A2** (modo outfit + pase de imágenes) | El cambio que pidió: elegir un outfit y verlo pasar solo a pantalla completa. |
| 4 | **A5** (fluidez) | Las tres causas medidas de que la grilla se sienta pesada. Son borrados, no código nuevo. |
| 5 | **A4** (filtros colapsados) | Devuelve la pantalla a las fotos. |
| 6 | **C1-C3** (versionado + hash en la UI) | Sin esto seguimos sin poder verificar ninguna entrega, incluida esta. |
| 7 | **B3-B7** | Caché sana, pausa correcta, menos créditos quemados. |

**Lo que NO propuse, y por qué:** sigue sin proponerse el streaming progresivo real (reproducir
mientras llega el audio). Con `MediaPlayer` no es confiable y exigiría migrar a Media3/ExoPlayer con
un `DataSource` que haga POST con cuerpo, arriesgando el `PlaybackService` en primer plano que hoy
funciona. Con B1 arreglado, lo más probable es que la espera real ya esté bajo los 2 segundos y lo
único roto fuera la señal en pantalla — por eso B8 pide **medirla** antes de decidir cirugía.
