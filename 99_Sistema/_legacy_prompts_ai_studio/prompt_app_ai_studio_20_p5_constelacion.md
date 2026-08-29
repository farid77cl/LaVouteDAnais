# 📱 Prompt #20 · LV-App 2.0 — PASO 5: La Constelación (Bluesky Publisher)

> **Requiere P3 verde** (Room, con `PostQueueEntity` ya creada) y P2 (looks para publicar).
> **Este paso:** Caption Factory (voz cuica de Ele) + cola con Gate de la Ama + publicación a Bluesky en 1 toque.
> **Si aterriza roto:** patch como **Prompt #20.5.x**.

---

## ⚠️ REGLAS
1. Genera SOLO los archivos listados. Retrofit ya está (de P4.1). Credenciales por `BuildConfig`/entrada segura — NUNCA hardcodear.
2. Debe compilar: armar caption, encolar, aprobar (Gate) y publicar (o simular si no hay credenciales).

---

```markdown
PASO 5 de LV-App 2.0. Llena la pestaña LA CONSTELACIÓN (pestaña 3): publicador Bluesky.

## ARCHIVOS A GENERAR (SOLO ESTOS)
1. data/rrss/BlueskyClient.kt (AT Protocol)
   - `createSession(handle, appPassword)` → accessJwt.
   - `uploadBlob(image): BlobRef`. `createPost(text, blobRef?, altText)` → uri.
   - Manejo de error sin crash.

2. data/rrss/CaptionFactory.kt
   - Genera caption en la voz cuica-bimbo de Ele (tú chileno, po/cachai, emojis 🫦💅👠) a partir de los
     metadatos del look (material/color/silueta). 2-3 variantes. Hashtags configurables.

3. data/rrss/PostQueueRepository.kt — CRUD sobre PostQueueEntity: draft → pending → published. Flow de la cola.

4. ui/screens/rrss/ConstelacionScreen.kt (reemplaza placeholder)
   - Elegir look → generar caption (variantes) → editar → encolar como Draft.
   - Lista de cola con estados. Cada item pendiente muestra el **Gate de la Ama**:
     un botón "Aprobar y publicar" (1 toque) que dispara BlueskyClient.createPost y marca Published.

5. ui/screens/rrss/RrssViewModel.kt — estado de cola + generación de captions + publicación.

6. CaptionFactoryTest.kt — test real: un look de ejemplo produce caption no vacío, con emojis y sin voceo argentino.

## CRITERIO DE ÉXITO
Compila · genero caption en voz de Ele desde un look · lo encolo · el Gate de 1 toque publica a Bluesky
(o simula con credenciales vacías) y marca Published · sin credenciales, avisa y no crashea.

Entrega SOLO estos 6 puntos. Siguiente: P6 (Consola Ops + Git Live).
```
