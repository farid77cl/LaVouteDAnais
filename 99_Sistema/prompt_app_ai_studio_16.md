# 🎙️ Prompt #16 para AI Studio — Dos voces nuevas: Azure TTS (con acento chileno es-CL) y Google Cloud TTS

> **Base:** repo `farid77cl/LV-App` al día (después del #15). **Motivo:** ElevenLabs cobra (402 por cuota) y la voz del sistema suena robótica. Se agregan dos proveedores de TTS con tier gratis generoso y voces neuronales.
>
> **Idea rectora (léela antes de codear):** Azure y Google TTS devuelven **audio MP3**, igual que ElevenLabs. Por eso NO se toca la maquinaria de reproducción que ya existe en `ElevenLabsManager` (troceado, prefetch, MediaPlayer, spinner honesto, velocidad vía PlaybackParams, caché por hash). Lo ÚNICO nuevo es la llamada HTTP "texto → bytes MP3" por proveedor. Se generaliza esa llamada; el resto se REUSA.
>
> **Alcance:** el lector de audio + el diálogo de ajustes de voz. El flujo de subida de imágenes NO se toca.

---

## 🔍 Estado actual (verificado en el código)

- El proveedor se elige con un booleano `use_eleven_labs` (pref) → `PlaybackManager` usa TTS del sistema (Android) o `ElevenLabsManager`. El diálogo de ajustes (LiteratureScreen, ~:700-715) tiene el conmutador **Sistema / ElevenLabs**.
- `ElevenLabsManager.downloadAudio(text, voiceId, apiKey, modelId): File` (~:206-260) hace el POST, guarda el MP3 en caché (`tts_<hash>.mp3`) y lo devuelve. Todo lo demás (playFile → MediaPlayer, setOnPreparedListener con onChunkStarted + setSpeed, prefetch, spinner) es agnóstico del proveedor.
- La velocidad ya se aplica en `setOnPreparedListener` vía `PlaybackParams` (#13) → **funciona igual para Azure y Google sin trabajo extra**, porque reproducen por el mismo MediaPlayer.

---

```
Eres el desarrollador de LV-App (Kotlin / Jetpack Compose / Room / Retrofit / Moshi / Coil / OkHttp).
Trabaja sobre el repo al día (después del #15).

CONTEXTO: agrega dos proveedores de TTS (Azure y Google Cloud) que devuelven MP3. REUSA toda la
tubería de reproducción de ElevenLabsManager (troceado, prefetch, MediaPlayer, spinner, velocidad,
caché). Lo único nuevo es la llamada HTTP por proveedor. Si discrepas, dilo en "NO HECHO:".

⭐ INTOCABLE: el flujo de subida de imágenes. No se toca.

#####################################################################
##  A — GENERALIZAR EL PROVEEDOR (de booleano a enum de 4)
#####################################################################

A1. Reemplaza el booleano `use_eleven_labs` por una preferencia `tts_provider` (String) con 4
    valores: "SYSTEM", "ELEVENLABS", "AZURE", "GOOGLE". Default: "SYSTEM".
    - Mantén compatibilidad: si existe `use_eleven_labs=true` guardado, migra a "ELEVENLABS".
A2. En el punto donde hoy se decide `useElevenLabs && apiKey.isNotEmpty()` (LiteratureScreen
    :369,:447 y PlaybackManager.play), enруta por proveedor:
    - SYSTEM → TTS de Android (como hoy).
    - ELEVENLABS / AZURE / GOOGLE → la tubería de MediaPlayer de ElevenLabsManager (que pasa a ser
      el manager de audio remoto). Pásale el proveedor + sus credenciales.

#####################################################################
##  B — LA LLAMADA HTTP POR PROVEEDOR (lo único nuevo)
#####################################################################

Dentro de `ElevenLabsManager.downloadAudio(...)` (o extráelo a un `RemoteTtsManager`), ANTES de
guardar el MP3, ramifica por proveedor para obtener los bytes MP3. El hash de caché debe incluir el
proveedor + voz + velocidad para no mezclar audios.

B1. AZURE TTS (tiene voz chilena — la preferida)
    POST  https://{region}.tts.speech.microsoft.com/cognitiveservices/v1
    Headers:
      Ocp-Apim-Subscription-Key: {azureKey}
      Content-Type: application/ssml+xml; charset=utf-8
      X-Microsoft-OutputFormat: audio-24khz-48kbitrate-mono-mp3
      User-Agent: LVApp
    Body (SSML; ESCAPA <, >, & del texto):
      <speak version='1.0' xml:lang='es-CL'>
        <voice name='{azureVoice}'>{textoEscapado}</voice>
      </speak>
    Respuesta: bytes MP3 directos → guardar y reproducir.
    Voces a ofrecer en el selector (default la primera):
      es-CL-CatalinaNeural (♀ chilena) · es-CL-LorenzoNeural (♂ chileno) ·
      es-MX-DaliaNeural (♀) · es-ES-ElviraNeural (♀)
    Config en ajustes: campo Región (default "eastus"), campo Clave, selector de Voz.

B2. GOOGLE CLOUD TTS
    POST  https://texttospeech.googleapis.com/v1/text:synthesize?key={googleKey}
    Content-Type: application/json
    Body JSON:
      {
        "input": { "text": "{texto}" },
        "voice": { "languageCode": "es-US", "name": "{googleVoice}" },
        "audioConfig": { "audioEncoding": "MP3" }
      }
    Respuesta JSON: { "audioContent": "<base64>" } → Base64.decode → bytes MP3 → guardar y reproducir.
    Voces a ofrecer (default la primera):
      es-US-Neural2-A (♀) · es-US-Neural2-B (♂) · es-US-Neural2-C (♀) · es-ES-Neural2-F (♀)
    Config en ajustes: campo Clave API, selector de Voz.  (Auth por API key en la URL, sin OAuth.)

B3. Manejo de error uniforme: si cualquier proveedor responde ≠ 2xx, propaga a `onError` con
    "Proveedor Error: {código}" (como ya hace ElevenLabs). Si es 401/402/403 (auth/cuota), el
    mensaje debe sugerir "revisa la clave o cambia de voz en ⚙️".

#####################################################################
##  C — AJUSTES (el diálogo del engranaje)
#####################################################################

C1. En el diálogo de voz (LiteratureScreen ~:669), cambia el conmutador Sistema/ElevenLabs por un
    selector de 4: [ Sistema ] [ ElevenLabs ] [ Azure ] [ Google ].
C2. Muestra SOLO los campos del proveedor elegido:
    - ELEVENLABS: los de hoy (clave, modelo, voz).
    - AZURE: Región + Clave + Voz (lista B1).
    - GOOGLE: Clave + Voz (lista B2).
    - SYSTEM: nada extra.
C3. En la cabecera del lector, muestra en texto chico qué proveedor+voz está activo (ej.
    "Voz: Azure · es-CL-Catalina").

#####################################################################
##  D — VELOCIDAD (gratis: ya reusa PlaybackParams)
#####################################################################

Azure y Google reproducen por el mismo MediaPlayer que ElevenLabs, así que la velocidad del #13
(setSpeed en setOnPreparedListener) ya aplica. NO agregues control de velocidad por proveedor.
Verifica que 1.25× funcione con Azure y con Google (debería, sin tocar nada).

#####################################################################
##  E — TESTS Y ENTREGA
#####################################################################

Tests reales (con nombres, --rerun-tasks; PROHIBIDO assertTrue(true)):
  - El SSML de Azure escapa <, >, & del texto (un texto con "a < b & c" produce SSML válido).
  - El body JSON de Google se serializa con input.text, voice.name y audioEncoding=MP3.
  - La respuesta de Google (un audioContent base64 de prueba) se decodifica a los bytes esperados.
  - La clave de caché difiere entre proveedores/voces para el MISMO texto (no colisiona).
  - Migración: con use_eleven_labs=true guardado, tts_provider resuelve "ELEVENLABS".

Entrega:
  1. `git rev-parse HEAD` + `git log --oneline -5` (pega las salidas).
  2. Sube versionCode +1 y versionName +0.1 respecto a lo que haya en el repo. Hash de commit visible.
  3. Keystore usado y si coincide con el anterior.
  4. El APK.
  5. "NO HECHO:" obligatoria. Vacía + un test que falle = entrega no verificada.
```

---

## 📌 Nota de prioridad para la Ama

| Prioridad | Punto | Por qué |
|---|---|---|
| 🥇 | **B1 Azure** | Es la única con **voz chilena (es-CL)** y 500k chars/mes gratis. Tu mejor voz gratis. |
| 🥈 | **A + C** (enum de proveedor + ajustes) | Sin esto no hay dónde elegirlas. |
| 🥉 | **B2 Google** | 1M chars/mes gratis, buena voz (sin acento CL). El respaldo. |

**Lo honesto:** casi todo el trabajo es la config y dos requests HTTP. La reproducción, el troceado,
el spinner y la velocidad NO se tocan — Azure y Google entran por la misma puerta que ElevenLabs
(MP3 → MediaPlayer). Para Azure necesitas una **cuenta gratis de Azure Speech** (clave + región);
para Google, una **API key de Cloud Text-to-Speech**.
