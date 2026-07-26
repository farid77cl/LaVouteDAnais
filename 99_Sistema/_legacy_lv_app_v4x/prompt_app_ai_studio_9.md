# 📱 Prompt #9 para AI Studio — El visor a pantalla completa de verdad + ElevenLabs deja de hacer esperar

> **Base:** repo `farid77cl/LV-App` en el commit **`6a26f70`** ("feat: enhance image upload tracking
> and validation" = el #8 ya integrado).
>
> **El #8 quedó BIEN — verificado leyendo el código, no la promesa** (auditoría 20/07/2026):
> - `enum class ImageSource { CLIPBOARD, GALLERY, SHARE }` → `MainViewModel.kt:32` ✅
> - Guardia como **precondición de `uploadImageToGithub`** (`MainViewModel.kt:362`,
>   `if (width * height < 400_000) { onComplete(false); return }`) — vive **debajo de la UI**,
>   así que ninguna ruta nueva puede saltársela por olvido ✅
> - El origen viaja al mensaje de commit: `"Upload image Look ${look.number} $poseName
>   [${source.name.lowercase()} ${width}x${height}]"` (`GitRepository.kt:156`) ✅
> - `ShareAssignmentScreen.kt` ya no ofrece subir a la flota; queda el texto explicativo ✅
> - Los tests ahora llaman a `uploadImageToGithub` de verdad, no a la función suelta ✅
>
> **Nada de esto se toca en el #9.** Este prompt es sobre otras dos cosas: el **visor de imágenes**
> (no está a pantalla completa de verdad y es pesado de navegar) y el **lector de relatos**
> (ElevenLabs tarda demasiado en empezar a sonar).
>
> **Los dos diagnósticos de abajo están hechos sobre tu código real, con archivo y línea.
> No hay que investigarlos: hay que ejecutarlos.**

---

## 🔍 Diagnóstico A — por qué el visor NO está a pantalla completa

`LightboxViewer.kt:69-72` abre un `Dialog` con `usePlatformDefaultWidth = false`. Eso quita el ancho
máximo del diálogo, **pero no lo saca de los system insets**: un `Dialog` de Compose por defecto
respeta la barra de estado y la de navegación, así que la imagen nunca ocupa la pantalla entera —
queda enmarcada arriba y abajo. Falta `decorFitsSystemWindows = false` **y** esconder las barras.

Encima, el header (`LightboxViewer.kt:132-141`) es un `Row` fijo con un degradado negro al 70 %
pegado arriba **permanentemente sobre la imagen**: se come el 15 % superior de cada foto y no hay
forma de quitarlo. Y `ZoomableImage` usa `ContentScale.Fit` (`ZoomableImage.kt:84`), que en una foto
vertical de 669×1200 sobre una pantalla de teléfono deja franjas negras a los lados.

## 🔍 Diagnóstico B — por qué ElevenLabs tarda tanto en empezar

**La causa raíz:** `ElevenLabsApiService.kt` sí llama al endpoint correcto
(`v1/text-to-speech/{voice_id}/stream`, anotado `@Streaming`) — **pero `ElevenLabsManager.kt:113-117`
tira ese beneficio a la basura**:

```kotlin
body.byteStream().use { input ->
    FileOutputStream(file).use { output -> input.copyTo(output) }   // ← drena TODO
}
```
…y recién **después** llama a `playFile(file)` (`:88`). O sea: se pide un stream y se espera hasta el
**último byte** antes de que suene la primera sílaba. El streaming está anulado por el consumidor.

Y sobre esa causa raíz se apilan cinco agravantes, todas verificadas:

1. **El primer trozo mide 1.500 caracteres** (`LiteratureScreen.kt:335`, `maxLen = 1500`) ≈ 90 s de
   audio. La espera inicial es la síntesis completa de esos 90 segundos.
2. **El modelo es el más lento del catálogo**: `model_id = "eleven_multilingual_v2"`
   (`ElevenLabsApiService.kt:15`). `eleven_flash_v2_5` y `eleven_turbo_v2_5` soportan español y
   bajan el time-to-first-byte de segundos a decenas de milisegundos.
3. **No hay prefetch**: `setOnCompletionListener { currentChunkIndex++; playNextChunk() }`
   (`ElevenLabsManager.kt:133-136`) recién dispara la petición del trozo siguiente **cuando el actual
   terminó de sonar**. O sea que el silencio no pasa solo al principio: pasa **entre cada párrafo**.
4. **`prepare()` es síncrono y corre en el hilo principal**: `playFile` se invoca desde
   `scope.launch` con `Dispatchers.Main` (`:25`, `:85`) y llama `prepare()` (`:141`), no
   `prepareAsync()`. Congela la UI en cada trozo.
5. **Pausar cuesta una re-síntesis completa**: `PlaybackManager.pause()` (`:166`) llama a
   `elevenLabsManager.stop()`, que cancela el job, libera el MediaPlayer y vacía `textChunks`
   (`:60-61`); `resume()` (`:173`) vuelve a `playTextChunks(...)` **desde el inicio del trozo**. Cada
   pausa = descargar de nuevo ese trozo entero, pagar la latencia otra vez, y volver a oír el párrafo
   desde el principio. Además se paga de nuevo en créditos de ElevenLabs.
6. **Cero caché, y fuga de archivos**: el nombre es
   `"eleven_labs_tts_chunk_${System.currentTimeMillis()}.mp3"` (`:112`), así que **nunca se reutiliza**
   (releer el mismo capítulo re-sintetiza todo) y **nunca se borra** (el `cacheDir` crece sin techo).

---

```
Eres el desarrollador de LV-App (Kotlin / Jetpack Compose / Room / Retrofit / Moshi / Coil).
Trabaja sobre el repo al día (base: commit 6a26f70).

CONTEXTO: los dos defectos de abajo ya están diagnosticados sobre TU código, con archivo y
línea. No investigues, no expliques por qué pasó: ejecuta. Si discrepas de un diagnóstico,
dilo al final bajo "NO HECHO:" con la evidencia, no lo ignores en silencio.

⭐ INTOCABLE en todo este prompt: el flujo de subida de imágenes (portapapeles, selector de
galería, guardia de 400.000 px², ImageSource en el mensaje de commit, pantalla de share
recortada). Eso se acaba de arreglar en el #8 y funciona. No se refactoriza, no se "mejora
de paso", no se toca ni un archivo de esa ruta.

#####################################################################
##  PARTE A — EL VISOR DE IMÁGENES A PANTALLA COMPLETA DE VERDAD
#####################################################################

=====================================================================
A1. PANTALLA COMPLETA REAL (INMERSIVO) — es el punto principal
=====================================================================
En LightboxViewer.kt:69-72, el Dialog debe salir de los system insets:

      Dialog(
          onDismissRequest = onDismissRequest,
          properties = DialogProperties(
              usePlatformDefaultWidth = false,
              decorFitsSystemWindows = false      // ← FALTA HOY
          )
      )

Y además esconder las barras del sistema mientras el visor está abierto, restaurándolas al
cerrar (DisposableEffect, para que no queden escondidas si se sale por el botón atrás):

      val view = LocalView.current
      DisposableEffect(Unit) {
          val window = (view.parent as? DialogWindowProvider)?.window
          val controller = window?.let { WindowInsetsControllerCompat(it, it.decorView) }
          controller?.hide(WindowInsetsCompat.Type.systemBars())
          controller?.systemBarsBehavior =
              WindowInsetsControllerCompat.BEHAVIOR_SHOW_TRANSIENT_BARS_BY_SWIPE
          onDispose { controller?.show(WindowInsetsCompat.Type.systemBars()) }
      }

Resultado esperado: la foto ocupa el 100 % del alto físico de la pantalla, sin barra de
estado ni barra de navegación.

=====================================================================
A2. EL HEADER SE ESCONDE SOLO — un toque lo trae de vuelta
=====================================================================
Hoy el header con su degradado negro (LightboxViewer.kt:132-141) tapa permanentemente la
parte de arriba de cada imagen. Cámbialo a "chrome" que se autooculta:

- Estado `var chromeVisible by remember { mutableStateOf(true) }`.
- Un TOQUE SIMPLE sobre la imagen alterna `chromeVisible` (hoy el toque simple no hace
  nada; el doble toque, que ya hace zoom, se conserva tal cual).
- El header entra/sale con AnimatedVisibility (fade + slide, 200 ms).
- Arranca visible y se esconde solo a los 2,5 segundos si no hubo interacción.
- Al esconderse el chrome, el fondo queda negro puro y SOLO la imagen a la vista.

=====================================================================
A3. BOTÓN "LLENAR PANTALLA" (Fit ⇄ Fill)
=====================================================================
ZoomableImage.kt:84 usa ContentScale.Fit fijo, que deja franjas negras en las verticales de
669×1200. Agrega un icono en el header (Icons.Default.Fullscreen /
Icons.Default.FullscreenExit) que alterne entre:
      - AJUSTAR (ContentScale.Fit): se ve la foto completa, con franjas. ← default
      - LLENAR  (ContentScale.Crop): la foto cubre toda la pantalla, recortando lo que sobre.
El default sigue siendo AJUSTAR (para auditar hay que ver la imagen entera), y la elección
se recuerda en SharedPreferences entre sesiones.

=====================================================================
A4. LAS MINIATURAS DE LA GRILLA PESAN LO MISMO QUE LA FOTO GRANDE
=====================================================================
SkeletonImage.kt:60-66 construye el ImageRequest SIN tamaño, así que cada tarjeta de ~160 dp
decodifica el PNG completo (669×1200). Con miles de imágenes en la grilla eso es la razón de
que hacer scroll se sienta pesado.

- Agrega un parámetro opcional a SkeletonAsyncImage para el tamaño de decodificación y úsalo
  en ImageCard (grilla) con `.size(coil.size.Size(400, 720))`. El visor a pantalla completa
  sigue pidiendo la imagen a resolución nativa (sin .size()).
- Quita `allowHardware(false)` del caso general de SkeletonImage.kt:63. Esa bandera fuerza
  bitmaps por software en TODA la app (mucha más RAM y dibujado más lento) y solo hace falta
  cuando hay que leer los píxeles de vuelta. Consérvala ÚNICAMENTE en la descarga a galería
  de ImageGalleryScreen.kt:610, que sí lee el bitmap.

=====================================================================
A5. LA ANIMACIÓN DE ENTRADA SE REPITE EN CADA RECICLADO
=====================================================================
ImageCard (ImageGalleryScreen.kt:700-720) tiene un LaunchedEffect con key `image.path` que
hace `delay(index * 50L)` y tres animaciones de 600 ms. Como la grilla recicla, **cada vez
que una tarjeta vuelve a entrar en pantalla se reanima**: la foto aparece tarde, escalando
y trepando. Eso es lo que hace que la ficha se sienta lenta al desplazarse.

- Que la animación corra SOLO la primera vez que esa imagen se ve en la sesión (un Set de
  paths ya animados recordado a nivel de pantalla, con rememberSaveable), o elimínala.
- Borra el bloque `pointerInput` de detección de hover (ImageGalleryScreen.kt:731-741): los
  eventos Enter/Exit no existen en pantalla táctil, así que `isHovered` es siempre false y
  ese bucle infinito `awaitPointerEvent` corre por cada tarjeta sin producir nada.

=====================================================================
A6. LIMPIEZA DE CÓDIGO MUERTO EN ImageGalleryScreen.kt
=====================================================================
Al extraer LightboxViewer quedó atrás medio overlay. En el bloque de las líneas 577-591 hay
estado declarado que NO se usa en ninguna parte: copyConfirmedUrl, copyConfirmedPath,
dragAmountAccumulated, scrollState, isDeleting, isEditingTags, editableTags, lookDetails.
También `imageRatings` (línea 97) se colecta y nunca se lee, y hay imports muertos
(HorizontalPager, rememberPagerState, detectTransformGestures, detectHorizontalDragGestures,
ArrowBack, ArrowForward, LazyVerticalGrid, GridCells, GridItemSpan, Dialog, DialogProperties,
ClipData, ClipboardManager, Offset).
Bórralos. No agregues funcionalidad para justificarlos.

=====================================================================
A7. LA BARRA DE FILTROS RÁPIDOS ES INNAVEGABLE
=====================================================================
ImageGalleryScreen.kt:232-321 mete en UN SOLO LazyRow horizontal: 7 poses + todas las
categorías + todos los colores + todas las etiquetas. Con el catálogo real eso son más de
cien chips en una tira que hay que barrer con el dedo para llegar al final.

Reorganízalo en filas separadas con su rótulo, cada una desplazable por su cuenta:
      POSE      [Standing] [Back View] [Seated] …
      ESTILO    [🥋 …] [🥋 …]
      COLOR     [🎨 …] [🎨 …]
      ETIQUETA  [🏷️ …] [🏷️ …]
El chip "Limpiar" queda arriba de todo y solo aparece si hay algún filtro activo (como hoy).
Muestra las filas COLOR y ETIQUETA colapsadas si tienen más de 12 chips, con un
"＋N más" que las expande.

=====================================================================
A8. DENSIDAD DE GRILLA DE 3 PASOS
=====================================================================
Hoy el botón de ImageGalleryScreen.kt:169 alterna binario entre 1 columna y Adaptive(160.dp).
Cámbialo por un ciclo de tres: 1 columna (detalle) → 2 columnas → 4 columnas (contacto).
Recuerda la elección en SharedPreferences. El icono refleja el modo actual.

=====================================================================
A9. DESCARTAR DESDE EL VISOR, NO SOLO BORRAR
=====================================================================
El visor (LightboxViewer.kt:167-191) solo ofrece 🗑️ Eliminar, que es destructivo y no deja
rastro del motivo. El registro de descartes con evidencia YA EXISTE en la app (lo hizo el
#7: descartes.csv + JPEG de evidencia). Agrega junto al de eliminar un botón
"🚫 Registrar descarte" que reuse exactamente ese flujo ya construido — mismo diálogo de
motivo, misma escritura de evidencia. No escribas un pipeline nuevo: llama al que hay.

#####################################################################
##  PARTE B — ELEVENLABS: QUE EMPIECE A SONAR YA
#####################################################################

El objetivo medible: **desde que la usuaria toca Reproducir hasta que se oye la primera
palabra deben pasar menos de 2 segundos** con red normal. Hoy son muchos segundos porque se
espera la síntesis completa de 1.500 caracteres antes de emitir sonido.

=====================================================================
B1. EL PRIMER TROZO TIENE QUE SER CHICO (arreglo de mayor impacto)
=====================================================================
En LiteratureScreen.kt:335 el troceado usa maxLen = 1500 para TODOS los trozos, incluido el
primero. La latencia de síntesis crece con el largo del texto, así que la primera espera es
la peor de todas.

Trocea con tamaño creciente: el primer trozo ~250 caracteres, el segundo ~600, y del tercero
en adelante los 1.500 de ahora. Se corta igual por límite de párrafo/frase que hoy (no
partas palabras). El oído no nota el cambio de tamaño; sí nota los segundos de silencio.

=====================================================================
B2. PREFETCH DEL TROZO SIGUIENTE MIENTRAS SUENA EL ACTUAL
=====================================================================
ElevenLabsManager.kt:133-136 pide el trozo N+1 recién cuando el N terminó de sonar, así que
hay un bache de silencio ENTRE CADA PÁRRAFO, no solo al principio.

Apenas empieza a reproducirse el trozo N, lanza en paralelo la descarga del N+1 y guárdala
(un `Deferred<File?>` o un mapa índice→File). Cuando el N termine, el N+1 ya está en disco y
arranca instantáneo. Mantén como máximo UN trozo adelantado (no precargues el capítulo
entero: son créditos de ElevenLabs y megas de caché).

=====================================================================
B3. MODELO RÁPIDO, ELEGIBLE POR LA USUARIA
=====================================================================
ElevenLabsApiService.kt:15 fija model_id = "eleven_multilingual_v2", el de mayor latencia del
catálogo. Haz el modelo parametrizable y agrega en el panel de ajustes de voz de
LiteratureScreen (donde ya están los radio buttons Android TTS / ElevenLabs) un selector:

      ( ) Calidad máxima   — eleven_multilingual_v2   (más lento en arrancar)
      (•) Rápido           — eleven_flash_v2_5        ← default nuevo

Ambos soportan español. Guarda la elección en SharedPreferences ("eleven_labs_model").
Agrega también `output_format=mp3_22050_32` como query param para el modelo Rápido: menos
bytes que descargar, y para voz hablada en un teléfono la diferencia no se escucha.

=====================================================================
B4. prepareAsync() EN VEZ DE prepare()
=====================================================================
ElevenLabsManager.kt:141 llama `prepare()` (síncrono) desde una corrutina que corre en
Dispatchers.Main (:25, :85). Cambia a `prepareAsync()` + `setOnPreparedListener { start();
onChunkStarted?.invoke(currentChunkIndex) }`. La UI deja de congelarse en cada trozo.

=====================================================================
B5. PAUSA DE VERDAD (hoy pausar re-descarga el párrafo entero)
=====================================================================
PlaybackManager.pause() (:166) llama a elevenLabsManager.stop(), que cancela el job, libera
el MediaPlayer y vacía textChunks (ElevenLabsManager.kt:60-61). Y resume() (:173) reinicia
con playTextChunks(...) desde el comienzo del trozo. Consecuencia: cada pausa cuesta la
latencia completa otra vez, se vuelve a oír el párrafo desde el principio, y se vuelve a
pagar en créditos.

Agrega a ElevenLabsManager métodos de pausa REALES:
      fun pause()  { mediaPlayer?.takeIf { it.isPlaying }?.pause() }
      fun resume() { mediaPlayer?.start() }
y que PlaybackManager los use cuando isElevenLabs == true, en vez de stop()/playTextChunks().
`stop()` se reserva para detener de verdad (cerrar el relato o cambiar de archivo).

=====================================================================
B6. CACHÉ POR CONTENIDO + PURGA (hoy no reutiliza nada y no borra nada)
=====================================================================
ElevenLabsManager.kt:112 nombra el archivo con System.currentTimeMillis(), así que ningún
audio se reutiliza jamás y ninguno se borra nunca.

- Nombra por hash estable del contenido:
      "tts_${(text + voiceId + modelId).hashCode()}.mp3"
  en un subdirectorio `context.cacheDir/tts/`.
- Antes de pedir a la red, si el archivo existe y pesa > 0, úsalo y NO llames a la API.
  (Releer un capítulo pasa a ser instantáneo y gratis.)
- Purga por antigüedad al iniciar reproducción: borra los .mp3 de esa carpeta con más de
  7 días, o los más viejos hasta bajar de 200 MB, lo que ocurra primero.

=====================================================================
B7. QUE SE VEA QUE ESTÁ TRABAJANDO
=====================================================================
Mientras se sintetiza el primer trozo no hay ninguna señal en pantalla y parece colgado.
En LiteratureScreen, mientras isElevenLabs esté activo y aún no suene el primer audio,
muestra en el control de reproducción un indicador con texto:
      ⏳ "Preparando la voz…"
que desaparece en cuanto empieza a sonar. Si la API falla (response no exitosa o excepción),
muestra un Toast con el motivo real en vez del silencio actual — hoy ElevenLabsManager.kt:119-125
devuelve null y la reproducción simplemente termina sin decir nada, y la usuaria no puede
distinguir "sin crédito" de "sin internet" de "clave mala".

=====================================================================
C. TESTS — QUE EJERZAN LA RUTA, NO LA FUNCIÓN SUELTA
=====================================================================
Vale la lección del #8: un test que llama a una función aislada no prueba el comportamiento.

  - Troceado (B1): un texto de 5.000 caracteres produce un primer trozo <= 250 y un segundo
    <= 600, ninguno corta una palabra a la mitad, y la concatenación de todos los trozos
    reproduce el texto original sin pérdida.
  - Caché (B6): con el archivo ya en cacheDir/tts/, reproducir NO ejecuta ninguna llamada de
    red (verifícalo con un ElevenLabsApiService falso que cuente invocaciones: debe ser 0).
  - Pausa (B5): pausar y reanudar NO produce ninguna llamada de red nueva (mismo contador: la
    cuenta después de reanudar es igual a la de antes de pausar).
  - Prefetch (B2): al empezar el trozo 0 el contador de llamadas llega a 2 (el 0 y el 1), y
    NO a 3 — o sea, se adelanta uno, no el capítulo entero.
  - Visor (A1): el LightboxViewer se compone con decorFitsSystemWindows = false.
  - Chrome (A2): un toque simple sobre la imagen oculta el header
    (onNodeWithContentDescription("Cerrar").assertIsNotDisplayed() tras el tap); otro lo trae.

Corre con --rerun-tasks y pega la SALIDA REAL COMPLETA con los NOMBRES de los tests
ejecutados. "BUILD SUCCESSFUL" suelto o "N up-to-date" no cuentan como evidencia.

=====================================================================
D. ENTREGA
=====================================================================
Commit + push reales, con el hash pegado desde `git rev-parse HEAD` (no describas el
comando: pega su salida). Y el APK.

Si algo no se pudo hacer, escríbelo al final bajo el título "NO HECHO:" con una línea por
punto. Un pendiente declarado vale más que un test verde inventado.
```

---

## 📌 Nota de prioridad para la Ama

Si AI Studio se corta a medio camino o hay que recortar el alcance, el orden de valor es:

| Prioridad | Punto | Por qué |
|---|---|---|
| 🥇 | **A1** (inmersivo) | Es literalmente lo que pediste: la foto a pantalla completa. Son ~10 líneas. |
| 🥈 | **B1 + B2** (primer trozo chico + prefetch) | Se llevan la mayor parte de la espera de ElevenLabs sin cambiar de arquitectura ni de modelo. |
| 🥉 | **B3** (modelo flash) | El resto de la espera. Único con contrapartida: la voz suena un pelo menos rica. Por eso queda elegible, no impuesto. |
| 4 | **A2 + A4 + A5** | Lo que hace que la ficha se sienta ágil en vez de pesada. |
| 5 | **B5 + B6** | Ahorro de créditos y de espera al pausar/releer. |
| 6 | El resto | Comodidad y limpieza. |

**Lo que NO propuse, y por qué:** el arreglo teóricamente perfecto de B es reproducir el audio
*mientras* llega (streaming progresivo real, sin esperar el archivo completo). Con `MediaPlayer` no
se puede hacer de forma confiable; exigiría migrar a Media3/ExoPlayer con un `DataSource` que haga
POST con cuerpo. Es una obra bastante mayor y con riesgo de romper el `PlaybackService` en primer
plano que hoy funciona. **B1+B2+B3 dejan la espera bajo los 2 segundos sin esa cirugía** — si
después de aplicarlo sigue sintiéndose lento, ahí sí vale la pena discutir la migración.
