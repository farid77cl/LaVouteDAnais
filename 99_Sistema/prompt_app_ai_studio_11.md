# 📱 Prompt #11 para AI Studio — El relato hablado deja de tomar siglos (arreglo cierto + medición) + velocidad, auto-scroll y nota con versión

> **Base:** repo `farid77cl/LV-App` en el commit **`0b4b9b5`** ("fix: improve gallery scroll reset and state flow"), `versionCode = 14`, `versionName = "4.7"`.
>
> **Todo lo de abajo está verificado leyendo el código clonado de ese commit, con archivo y línea.** No hay que investigarlo: hay que ejecutarlo.
>
> **Alcance:** SOLO el lector de relatos / audio. La galería y el flujo de subida de imágenes NO se tocan.

---

## 🔍 AUDITORÍA DEL #10 — qué llegó de verdad al audio y qué no

El #10 tocó ElevenLabs (sus puntos B1-B8). Leyendo el código de hoy:

| Punto #10 | Estado real | Evidencia |
|---|---|---|
| B2 errores visibles (onError cableado) | ✅ Hecho | `PlaybackManager.kt:78-84` asigna `onError` con Toast |
| B3 descarga atómica `.part` + rename | ✅ Hecho | `ElevenLabsManager.kt:225-232` |
| B4 prefetch con `Deferred` (no doble pedido) | ✅ Hecho | `ElevenLabsManager.kt:35`, `160-165`, `195-202` |
| B7 caché de texto por `sha` | ✅ Hecho | `LiteratureScreen.kt:298` (`?v=${file.sha}`) |
| Trozo escalado + modelo flash + caché | ✅ Hecho | `LiteratureScreen.kt:340-346`, `:154` default `eleven_flash_v2_5` |
| **B1 el spinner honesto** | 🐞 **ROTO POR UN INVOKE PREMATURO** | ver C1 |
| **B5 pausar mientras carga** | ⚠️ **A MEDIAS — la bandera existe y NADIE la cablea** | ver C2 |
| **B6 troceado fuera del hilo principal** | ❌ **NO HECHO** | ver C3 |
| Streaming progresivo real | ⛔ **Nunca se propuso** (el #10 lo pospuso a propósito) | — |

**Traducción:** lo que la Ama sigue sintiendo —*"toma siglos"*— NO es principalmente falta de streaming. Son tres defectos concretos que hacen que la espera se sienta infinita y se congele la UI, más el riesgo de que esté corriendo el modelo lento. Eso es lo que arregla este prompt. El streaming queda para un #13 **solo si la medición (Parte D) demuestra que hace falta**.

---

## 🔍 Diagnóstico — los defectos vivos, con línea

### C1 · La ruedita de "cargando" se apaga ANTES de que suene nada (esto es lo que se siente como "eterno")

`PlaybackManager.kt:161` enciende `_isBuffering` al reproducir con ElevenLabs, y el callback `onChunkStarted` (`:66-74`) lo apaga. **El problema:** `ElevenLabsManager.kt:156` invoca `onChunkStarted` **de forma síncrona al principio de `playNextChunk`, ANTES de lanzar la corrutina que descarga el audio**. Resultado: tocas Reproducir → el spinner se apaga al instante → **silencio muerto** varios segundos mientras se sintetiza y baja el trozo → recién ahí suena. La espera real existe, pero **sin ninguna señal en pantalla**, que es lo que la hace sentir infinita. (El segundo `onChunkStarted` correcto está en `:275`, dentro de `setOnPreparedListener`, que sí se dispara cuando el audio arranca.)

Además el botón (`LiteratureScreen.kt:394-395`) muestra solo un `CircularProgressIndicator` mudo — sin texto que diga qué está pasando.

### C2 · Pausar mientras carga no pausa nada

`ElevenLabsManager` declara `pausedByUser` (`:34`), pero **nadie la usa**: `pause()` (`:109-117`) solo hace `mediaPlayer?.pause()` y **no** pone la bandera; `setOnPreparedListener` (`:273-282`) llama a `start()` **incondicionalmente**. Si se toca pausa durante la síntesis del primer trozo (cuando `mediaPlayer` aún es null), la descarga sigue viva y al terminar **arranca el audio igual**, con la UI diciendo "pausado".

### C3 · El troceado corre en el hilo principal, antes del primer byte

`LiteratureScreen.kt:333-380` hace TODO el troceado dentro del `onClick` del botón: dos `Regex` sobre el texto completo (los capítulos reales pesan 70-100 KB), un `split`, y un bucle con `replace(Regex("\\s+"))` por párrafo. Todo **síncrono en el hilo principal**, antes de que salga el primer byte a la red → la UI se congela un instante perceptible justo al tocar Reproducir.

### C4 · El modelo lento puede activarse sin que se note (hoy NO es la causa)

El selector (`LiteratureScreen.kt:661-678`) ofrece `eleven_multilingual_v2`, **el de mayor latencia del catálogo**, y cuando está activo `downloadAudio` (`:215`) NO usa el formato liviano `mp3_22050_32` (baja ~4× más bytes antes de sonar). **Confirmado con la Ama (23/07): hoy está marcado Flash v2.5** → el modelo NO explica su lentitud actual. A5 queda por **higiene** (que ninguna ruta ni descuido caiga en el lento) y **transparencia** (mostrar el modelo activo), no como arreglo del síntoma de hoy. La causa real, entonces, se concentra en C1 (señal rota) y C3 (hilo congelado).

---

```
Eres el desarrollador de LV-App (Kotlin / Jetpack Compose / Room / Retrofit / Moshi / Coil).
Trabaja sobre el repo al día (base: commit 0b4b9b5, versionCode 14, versionName 4.7).

CONTEXTO: los defectos de abajo están diagnosticados sobre TU código, con archivo y línea.
No investigues ni expliques por qué pasó: ejecuta. Si discrepas de un diagnóstico, dilo al
final bajo "NO HECHO:" con la evidencia. No lo ignores en silencio.

⭐ INTOCABLE: la galería y TODO el flujo de subida de imágenes (portapapeles, selector de
galería, guardia de 400.000 px² como precondición de uploadImageToGithub, ImageSource en el
mensaje de commit, pantalla de share). No se toca ni un archivo de esa ruta. Este prompt es
SOLO el lector de relatos / audio.

⚠️ AVISO: en el #10 se reportó como hecho el arreglo del spinner (B1) y quedó roto por un
invoke prematuro; B5 se dejó a medias (bandera sin cablear) y B6 sin hacer. Cada punto de este
prompt tiene un criterio de aceptación verificable. Si no se cumple, va en "NO HECHO:".

#####################################################################
##  PARTE A — QUE SE VEA QUE ARRANCÓ, Y QUE NO SE CONGELE
#####################################################################

=====================================================================
A1. EL SPINNER HONESTO (arreglo de mayor impacto)
=====================================================================
En ElevenLabsManager.kt, BORRA el `onChunkStarted?.invoke(currentChunkIndex)` de la línea 156
(el que está al principio de `playNextChunk`, antes de lanzar la corrutina de descarga). El
único `onChunkStarted` que debe quedar es el de `setOnPreparedListener` (:275), que se dispara
cuando el audio DE VERDAD empieza a sonar.

Así `_isBuffering` (que se apaga en el callback onChunkStarted de PlaybackManager, :66-74) se
mantiene en true durante toda la descarga y se apaga exactamente cuando suena la primera sílaba.

Y en LiteratureScreen.kt (junto al botón, ~:393-402), mientras `isBuffering` esté en true,
muestra el texto "⏳ Preparando la voz…" al lado del spinner; quítalo en cuanto se apague.

CRITERIO DE ACEPTACIÓN: al tocar Reproducir, el spinner + "Preparando la voz…" se mantienen
hasta que se oye la primera palabra; en ese momento (no antes) el botón pasa a icono de Pausa.

=====================================================================
A2. PAUSAR MIENTRAS CARGA TIENE QUE PAUSAR (cablear la bandera que ya existe)
=====================================================================
`pausedByUser` está declarada (ElevenLabsManager.kt:34) y nadie la usa.
- `pause()` (:109-117): además de `mediaPlayer?.pause()`, pon `pausedByUser = true`.
- `resume()` (:119-130): pon `pausedByUser = false` al entrar (ya lo hace en :120); si
  `mediaPlayer` es null y hay chunk pendiente, reanuda ese chunk (ya lo intenta).
- `setOnPreparedListener` (:273-282): si `pausedByUser` es true, NO llames a `start()`; deja el
  player preparado esperando, y NO dispares onChunkStarted todavía (para que el spinner no mienta).

CRITERIO DE ACEPTACIÓN: tocar Pausa durante "Preparando la voz…" deja `isPlaying` en false y NO
suena audio al terminar la descarga; al tocar Reproducir de nuevo, arranca ese mismo trozo.

=====================================================================
A3. EL TROCEADO SALE DEL HILO PRINCIPAL
=====================================================================
LiteratureScreen.kt:333-380 hace el troceado (dos Regex sobre 70-100 KB + bucle) dentro del
onClick, en el hilo principal, antes del primer byte.
- Muévelo a `withContext(Dispatchers.Default)` dentro de un `rememberCoroutineScope().launch`.
- Enciende "Preparando la voz…" APENAS se toca el botón (antes de trocear), y recién cuando los
  chunks estén listos llama a `PlaybackManager.play(...)`.
- Cachea los chunks por `file.path` (en el ViewModel): volver a tocar Reproducir sobre el mismo
  capítulo no debe recalcularlos.

CRITERIO DE ACEPTACIÓN: tocar Reproducir sobre un capítulo de >10.000 palabras no congela ni un
frame la UI; el spinner aparece de inmediato.

=====================================================================
A4. TROZO 0 = LA PRIMERA FRASE (arranque en frío más corto)
=====================================================================
Hoy `getMaxLenForChunk(0)` = 250 (LiteratureScreen.kt:343). Bájalo: el PRIMER trozo debe cortar
en el primer punto disponible dentro de ~140 caracteres (si no hay punto, en el primer espacio
antes de 140). Trozo 1 = 600 y el resto 1500, como ya están. Menos texto en el trozo 0 = menos
síntesis antes de la primera palabra.

CRITERIO DE ACEPTACIÓN: para un capítulo cualquiera, el primer trozo mide ≤ 140 caracteres y no
corta una palabra por la mitad.

=====================================================================
A5. FORZAR Y MOSTRAR EL MODELO RÁPIDO
=====================================================================
El modelo por defecto ya es `eleven_flash_v2_5` (bien). Pero el selector ofrece
`eleven_multilingual_v2`, el lento, sin advertirlo.
- En el selector (LiteratureScreen.kt:661-678), etiqueta la opción multilingual como
  "Multilingual v2 (más lento)" y deja Flash como "Flash v2.5 (rápido, recomendado)".
- En la cabecera del lector, muestra en texto chico qué modelo está activo (ej. "Voz: Flash
  v2.5"), leyendo el pref `eleven_labs_model`. Que la Ama pueda VER si está en el lento.
- Corrige también el default del data class: `ElevenLabsApiService.kt:15` tiene
  `model_id = "eleven_multilingual_v2"`. Cámbialo a `"eleven_flash_v2_5"` para que ninguna ruta
  que olvide pasar el modelo caiga en el lento.

CRITERIO DE ACEPTACIÓN: la cabecera del lector dice qué voz/modelo está activo; el default en
todo el código es Flash.

#####################################################################
##  PARTE B — FUNCIONES NUEVAS DEL LECTOR (aprobadas por la Ama)
#####################################################################

=====================================================================
B1. VELOCIDAD DE LECTURA — que aplique también a ElevenLabs
=====================================================================
Hoy `ttsSpeechRate` (LiteratureScreen.kt:389) se aplica solo a la voz del sistema
(PlaybackManager.kt:151, `tts?.setSpeechRate`). ElevenLabs (MediaPlayer) la ignora.
- MediaPlayer soporta velocidad desde API 23 vía `PlaybackParams`. En `setOnPreparedListener`
  (ElevenLabsManager.kt:273), antes de `start()`, aplica la velocidad guardada:
      playbackParams = playbackParams.setSpeed(speed)   // el tono se preserva (time-stretch)
  Pasa el `speed` desde PlaybackManager.play(...) a ElevenLabsManager (hoy solo lo recibe el TTS
  del sistema).
- Control en la UI: un selector 0.75× / 1× / 1.25× (default 1×), guardado en SharedPreferences,
  visible en el lector (no escondido en Ajustes). Cambia la velocidad del trozo en curso o del
  siguiente sin reiniciar el capítulo.

CRITERIO DE ACEPTACIÓN: con voz ElevenLabs, poner 1.25× acelera la lectura sin cambiar el tono
ni volver al principio.

=====================================================================
B2. AUTO-SCROLL — pulir el que ya existe
=====================================================================
Ya existe (LiteratureScreen.kt:451-461): al cambiar de trozo, `animateScrollToItem(matchIndex-1)`.
El match por `contains` falla cuando un párrafo largo se partió en varios trozos (el trozo no
"contiene" el párrafo entero). Mejóralo:
- Guarda, al trocear, el índice del párrafo de origen de cada trozo (mapea chunk→párrafo). Usa
  ese índice para el scroll en vez del match por substring, que es frágil.
- Deja un margen: scrollea de modo que el párrafo activo quede en el tercio superior, no pegado
  al borde.

CRITERIO DE ACEPTACIÓN: mientras suena el relato, el texto se desplaza solo siguiendo la voz, y
el párrafo que se está leyendo queda siempre visible aunque venga de un párrafo largo partido.

=====================================================================
B3. LA NOTA DE "COMENTARIOS" LLEVA LA VERSIÓN DEL CAPÍTULO
=====================================================================
El botón Comentarios (LiteratureScreen.kt:411) sube la nota como `nota_${generatedFileTitle}.md`
(MainViewModel.kt:264, :281). Hoy NO refleja la versión del capítulo que se está revisando, así
que dos revisiones de versiones distintas chocan en el mismo archivo.
- Al armar el nombre de la nota, incluye la versión del capítulo activo, parseándola del nombre
  del archivo del capítulo (patrón `capitulo_<N>_<slug>_v0.<X>.md`). Resultado esperado:
  `nota_capitulo_<N>_<slug>_v0.<X>.md`, en la misma carpeta del capítulo.
- Si el capítulo no trae versión en el nombre, cae al comportamiento actual (no rompas nada).
- En el diálogo de Comentarios, muestra arriba qué versión se está comentando ("Comentando:
  Capítulo 1 · v0.4").

CRITERIO DE ACEPTACIÓN: comentar el `capitulo_1_el_deseo_v0.4.md` crea/actualiza
`nota_capitulo_1_el_deseo_v0.4.md`; comentar una v0.5 crea un archivo aparte, no pisa el de v0.4.

#####################################################################
##  PARTE C — MEDIR (para decidir si hace falta cirugía de streaming)
#####################################################################

Registra en Logcat con tag "TTFA" los milisegundos entre el toque de Reproducir y el primer
`onChunkStarted` REAL (el de setOnPreparedListener, cuando suena). Pega en la entrega el valor
de DOS corridas sobre un capítulo de más de 10.000 palabras, con voz Flash v2.5 y caché vacía
(primera reproducción):
  - TTFA arranque en frío (trozo 0 sin caché).
  - TTFA con caché (segunda vez sobre el mismo capítulo).

Objetivo del arranque en frío: **menos de 1,5 s**. Este número decide si el #13 (streaming
progresivo con ExoPlayer) es necesario o no. No optimices el streaming en este prompt: mídelo.

#####################################################################
##  PARTE D — TESTS QUE EJERZAN LA RUTA
#####################################################################

  - Spinner (A1): tras invocar onChunkStarted, isBuffering==false; y ANTES de que se invoque
    (durante la descarga simulada), isBuffering==true. Con un ElevenLabsApiService falso lento,
    isBuffering sigue true hasta que el player queda preparado.
  - Pausa durante carga (A2): pausar antes de que el player esté preparado deja isPlaying en
    false y NO arranca audio al completarse la descarga (pausedByUser respetado en onPrepared).
  - Troceado 1ª frase (A4): un texto cuyo primer párrafo mide 400 caracteres produce trozo 0
    ≤ 140 cortado en un punto o espacio, sin partir palabras.
  - Chunk→párrafo (B2): el mapa chunk→índice de párrafo apunta, para cada trozo, al párrafo del
    que salió (verificable sobre un texto con un párrafo largo partido en 3 trozos).
  - Nombre de nota con versión (B3): para un capítulo `capitulo_1_el_deseo_v0.4.md`, el nombre
    generado de la nota es `nota_capitulo_1_el_deseo_v0.4.md`; para `_v0.5.md`, otro archivo.
  - Default de modelo (A5): ElevenLabsRequest sin model_id explícito usa eleven_flash_v2_5.

Corre con --rerun-tasks y pega la SALIDA REAL COMPLETA con los NOMBRES de los tests ejecutados.
"BUILD SUCCESSFUL" suelto o "N up-to-date" no cuentan como evidencia.

#####################################################################
##  PARTE E — ENTREGA Y VERSIONADO
#####################################################################

1. Commit + push reales. Pega la SALIDA de `git rev-parse HEAD` (no describas el comando).
2. Pega la salida de `git log --oneline -5`.
3. Sube versionCode a 15 y versionName a "4.8" (todo commit que cambie código de la app bumpea:
   es parte del entregable, no un paso opcional). Verifica que la app siga mostrando en pantalla
   versionName + versionCode + hash de commit (si el #10 no dejó el GIT_SHA en la UI, agrégalo:
   buildConfigField GIT_SHA y mostrarlo en LaVouteApp.kt donde dice la versión).
4. Declara con qué keystore se firmó el APK y si coincide con la entrega anterior.
5. Pega los dos valores de TTFA de la Parte C.
6. El APK.
7. Sección final obligatoria "NO HECHO:" con una línea por punto que no se pudo hacer. Un
   pendiente declarado vale más que un test verde inventado. Si esta sección viene vacía y algún
   punto de la Parte D falla, la entrega completa se considera no verificada.
```

---

## 📌 Nota de prioridad para la Ama

Si AI Studio se corta a medio camino, el orden de valor es:

| Prioridad | Punto | Por qué |
|---|---|---|
| 🥇 | **A1** (spinner honesto) | Es borrar una línea (`ElevenLabsManager:156`) + agregar un texto. Es lo que hace que ElevenLabs *parezca* que nunca arranca aunque la espera real sea corta. |
| 🥈 | **A3** (troceado fuera del hilo) | Quita el congelamiento de la UI justo al tocar Reproducir en capítulos largos. |
| 🥉 | **C** (medir el TTFA) | La medición decide si hace falta el ExoPlayer del #13. (A5 es higiene/transparencia: la Ama ya confirmó que está en Flash, así que el modelo no es el síntoma de hoy.) |
| 4 | **A2 + A4** (pausa correcta + trozo 0 corto) | Arranque más corto y sin audio fantasma. |
| 5 | **B1** (velocidad en ElevenLabs) | Función pedida; casi gratis vía PlaybackParams. |
| 6 | **B2 + B3** (auto-scroll pulido + nota con versión) | Pulido del lector; la nota con versión cierra el ciclo con la convención de notas del engine. |

**Lo que este prompt NO hace, a propósito:** el streaming progresivo real (reproducir mientras
llega el audio, con ExoPlayer/Media3). El #10 lo pospuso y pidió medir primero (su B8), y esa
medición nunca fue real porque el spinner estaba roto. Con A1-A5 arreglados y el TTFA medido, lo
más probable es que el arranque en frío ya baje de 1,5 s y el ExoPlayer sea innecesario. Si el
número dice lo contrario, ahí sí lo hacemos en el #13 — con evidencia, no por fe.
