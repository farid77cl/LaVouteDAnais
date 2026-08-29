# 📱 Prompt #20.4 · LV-App 2.0 — PASO 4.1: Audio Player Multivoz + Karaoke Sync

> **Continuación de P4** (Literatura). Requiere P4 verde (Reader funcionando).
> **Este paso:** convertir el capítulo a voz (TTS multivoz) y reproducirlo con resaltado karaoke.
> **Si aterriza roto:** patch como **Prompt #20.4.x**.

---

## ⚠️ REGLAS
1. Genera SOLO los archivos listados. Añade media3-exoplayer, media3-session, retrofit + converter-gson.
2. Debe compilar y reproducir. **OJO Retrofit:** en las interfaces de servicio, NUNCA pongas un `@Query`
   antes de un `@Path` (rompe la construcción del método — es el bug que ya nos costó una sesión).
3. Troceado y llamadas de red SIEMPRE fuera del hilo principal (coroutines/Dispatchers.IO).

---

```markdown
PASO 4.1 de LV-App 2.0. Añade audio al Reader de P4.

## ARCHIVOS A GENERAR (SOLO ESTOS)
1. data/tts/TtsProvider.kt (interface) — `suspend fun synthesize(text: String, voice: String): ByteArray /*MP3*/`.

2. data/tts/AzureTts.kt — es-CL (voz chilena), tier gratis (~500k chars/mes). Provider por defecto.
   data/tts/GoogleTts.kt — respaldo (~1M/mes).
   data/tts/ElevenLabsTts.kt — opcional (voz premium; cuota baja ~10k/mes, avisar si 402).
   Retrofit con orden de parámetros correcto (@Path antes que @Query).

3. data/tts/TtsPipeline.kt
   - Trocea el capítulo en frases/párrafos (chunks), sintetiza cada chunk en IO, y los encola.
   - Expone la lista de chunks con offsets de texto para el resaltado.

4. service/PlaybackService.kt — MediaSessionService + ExoPlayer (Media3). Reproduce la cola de MP3.
   Notificación de reproducción con controles.

5. ui/screens/lit/AudioController.kt / mini-player flotante
   - Botón play/pause/stop, selector de voz (Azure es-CL / Google / ElevenLabs), control de velocidad.
   - Barra de progreso del capítulo.

6. ui/screens/lit/ReaderScreen.kt (editar)
   - Resaltado KARAOKE: a medida que suena cada chunk, resalta ese fragmento de texto y auto-scroll
     suave hacia él. El resaltado se ancla a los offsets del TtsPipeline.

7. TtsRetrofitTest.kt — test real: verifica que la interfaz de servicio se construye (sin excepción de
   Retrofit por orden de parámetros) y que el troceado de 5.000 chars da chunks correctos.

## CRITERIO DE ÉXITO
Compila · tocar "Escuchar" sintetiza y reproduce el capítulo · el texto se resalta estilo karaoke y
auto-scrollea · cambiar de voz funciona · si ElevenLabs da 402, muestra aviso y no crashea.

Entrega SOLO estos 7 puntos. Siguiente: P5 (La Constelación / Bluesky).
```
