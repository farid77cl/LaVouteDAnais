# 🚑 Prompt #15 para AI Studio — HOTFIX de 2 líneas: el audio revienta con «A @Path parameter must not come after a @Query»

> **Base:** repo `farid77cl/LV-App` al día (después del #13, HEAD `2461b13`).
>
> **Síntoma:** al reproducir un relato aparece un Toast rojo «Error: … A @Path parameter must not come after a @Query.» y no suena nada. Verificado en el código.
>
> **Causa (con archivo y línea):** en `ElevenLabsApiService.kt:30-35`, el parámetro `@Query("output_format")` está declarado ANTES del `@Path("voice_id")`. Retrofit prohíbe que un `@Path` venga después de un `@Query`, así que **el service method nunca se construye** y lanza IllegalArgumentException en la primera llamada (que cae en el `catch` de `downloadAudio` → `onError` → Toast). No depende de la cuenta ni del modelo: falla siempre. Quedó latente desde que se agregó el `output_format`; recién ahora que el #13 arregló la navegación se llega al player y se dispara.
>
> **Alcance:** SOLO `ElevenLabsApiService.kt`. Nada más se toca.

---

```
Eres el desarrollador de LV-App. Este es un hotfix de una línea de firma.

En app/src/main/java/com/example/data/remote/ElevenLabsApiService.kt, reordena los parámetros de
`synthesizeSpeech` para que el @Path venga ANTES de cualquier @Query (regla de Retrofit). Déjalo así:

    interface ElevenLabsApiService {
        @Streaming
        @POST("v1/text-to-speech/{voice_id}/stream")
        suspend fun synthesizeSpeech(
            @Path("voice_id") voiceId: String,
            @retrofit2.http.Query("output_format") outputFormat: String?,
            @Header("xi-api-key") apiKey: String?,
            @Body request: ElevenLabsRequest
        ): Response<ResponseBody>
    }

NO cambies el que llama: `ElevenLabsManager.downloadAudio` ya usa argumentos NOMBRADOS
(`api.synthesizeSpeech(voiceId = ..., apiKey = ..., outputFormat = ..., request = ...)`), así que
reordenar la firma no rompe la llamada. No toques nada más.

TEST (real, prohibido assertTrue(true)): un test que instancie el Retrofit con esta interfaz y
llame (o cree) el service method sin que lance IllegalArgumentException. Basta con que
`retrofit.create(ElevenLabsApiService::class.java)` + invocar el método NO explote al construirlo.

ENTREGA:
 1. `git rev-parse HEAD` (pega la salida) + `git log --oneline -3`.
 2. Sube versionCode +1 y versionName a "4.9" respecto a lo que haya en el repo (el #13 se quedó en
    15/"4.8"). Mantén el hash de commit visible en la cabecera.
 3. El APK.
 4. Confírma en el emulador/dispositivo: al tocar Reproducir en un relato, YA NO sale el Toast rojo
    y empieza a sonar (con el spinner honesto del #13 apagándose al oír la primera palabra).
 5. Sección "NO HECHO:" si algo no se pudo.
```

---

## 📌 Nota para la Ama

Es el arreglo más chico de todos: **swap de dos líneas**. Con esto la reproducción debería quedar
funcional de punta a punta (navegación del #13 + engranaje + spinner honesto + este). Después de
esto ya podés pegar el **#14** (notas sobre imágenes + portada frontal + quitar el texto de la
esquina). Orden sugerido: **#15 ahora (desbloquea el audio) → #14 después**.
