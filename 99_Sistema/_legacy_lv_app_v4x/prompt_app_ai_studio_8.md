# 📱 Prompt #8 para AI Studio — La guardia no existe en el share (auditado sobre el código real)

> **No reemplaza al #7: lo AUDITA.** El #7 especificaba en §2 que "Subir a la flota" desde el share
> reusara la guardia de resolución, y declaraba pasado en §5 el test
> `Share con imagen 286x512 + acción subir -> bloqueada por la guardia`.
>
> **Contraprueba de producción (19/07/2026):** entraron a la flota **34 imágenes por esa ruta**,
> todas 286×512 o 512×279 (~146.000 px², contra un umbral de 400.000). La Ama confirma que la app
> **muestra la imagen y reporta su medida** antes de subirla.
>
> **Auditoría del repo `farid77cl/LV-App` en el commit `90ebb75` (19/07/2026) — ya está hecha,
> no hay que pedirla:**
> - `isValidImageResolution` se define en `PromptFilterScreen.kt:74` y se llama en **exactamente
>   dos sitios**: `PromptFilterScreen.kt:159` (portapapeles) y `:208` (galería).
> - **`ShareAssignmentScreen.kt` NO la llama nunca.** Mide el bitmap en las líneas 55-56
>   (`imageWidth = bmp.width` / `imageHeight = bmp.height`), lo muestra, y sube igual.
> - El test que la daba por buena, `ShareAssignmentScreenTest.kt`, **no ejerce la pantalla**:
>   monta un `createComposeRule()`, importa `onNodeWithText`/`performClick`/`assertIsDisplayed`
>   sin usar ninguno, y afirma `isValidImageResolution(286, 512) == false` sobre la función
>   suelta. Su propio comentario lo dice: *"We will test the logic… But the prompt says…
>   We can simulate the state directly."* Ese test pasa exista o no la guardia en el share.
> - El `intent-filter` (`android.intent.action.SEND`, `image/*`, label "LV-App") **sí existe** y
>   está correcto. El share funciona; lo que falta es la guardia.
>
> **Hallazgo de fondo, que NO se arregla con código:** Gemini adjunta al share un **preview de
> 512 px de lado largo**, no el archivo. La ruta buena (Descargar + selector de galería) llega en
> 669×1200 — 1200 es el `maxDim` de la propia app redimensionando un original grande. La ruta
> buena pasa por el resize de la app; la del share llega ya en 512. **Por eso la rama "subir a la
> flota" del share no se afina: se elimina.**

---

```
Eres el desarrollador de LV-App (Kotlin / Jetpack Compose / Room / Retrofit / Moshi).
Trabaja sobre el repo al día (base: commit 90ebb75).

CONTEXTO: esto es la reparación de un defecto ya diagnosticado sobre tu código, no una
feature nueva. No hace falta que investigues ni que expliques por qué pasó. Los hechos
verificados están arriba; ejecuta.

=====================================================================
1. ELIMINAR "SUBIR A LA FLOTA" DE LA PANTALLA DE SHARE
=====================================================================
Gemini solo adjunta un preview de 512 px al compartir: esa rama no puede alimentar la
flota ni con guardia puesta. En ShareAssignmentScreen.kt, al recibir un share la app
ofrece ÚNICAMENTE:
      [ 🗑️ Registrar descarte ]
El botón de subir a la flota desaparece de esa pantalla. En su lugar, un texto fijo:
      "Compartir solo entrega una miniatura de 512 px.
       Para subir a la flota: Descargar en Gemini → selector de galería."

⭐ INTOCABLE (orden directa de la usuaria, ya venía en el #7): el botón de PEGAR DESDE
PORTAPAPELES y el SELECTOR DE GALERÍA siguen visibles y funcionales tal como están, con
su guardia y su badge. No se eliminan, no se esconden, no se "refactorizan". Aquí SOLO
se recorta la pantalla del share.

=====================================================================
2. LA GUARDIA BAJA A LA CAPA QUE ESCRIBE
=====================================================================
El defecto de fondo es que la guardia vive en la UI: se agregó una ruta nueva (el share)
y la ruta nueva simplemente no la llamó. Mueve la validación a precondición de la función
que sube:
- `uploadImageToGithub` (GitRepository) RECHAZA por sí misma cualquier bitmap bajo
  400.000 px², venga de donde venga, sin depender de que la pantalla se acuerde.
- Las llamadas existentes de PromptFilterScreen.kt:159 y :208 se mantienen como
  validación temprana de UX (para el mensaje al usuario), pero ya no son la única defensa.
Una pantalla se puede olvidar al agregar la siguiente ruta. La función que escribe, no.

=====================================================================
3. TRAZAR EL ORIGEN DE CADA SUBIDA
=====================================================================
Añade `enum class ImageSource { CLIPBOARD, GALLERY, SHARE }` que viaje con el bitmap
desde su punto de entrada hasta el commit, y regístralo en el MENSAJE DE COMMIT junto a
la resolución real:
      "Upload image Look 309 Ditzy [gallery 1024x1024]"
Así, si mañana aparece una miniatura en la flota, se sabe por qué puerta entró sin tener
que deducirlo de los píxeles. Deducirlo costó una auditoría entera.

=====================================================================
3.b LA FICHA DE RELATOS MUESTRA BORRADORES Y REPORTES COMO SI FUERAN CAPÍTULOS
=====================================================================
En GitRepository.kt:694 la ficha de literatura salta las subcarpetas internas de un
relato con:
      if (folderSubPathList.drop(1).any { it.startsWith("_") }) continue
Eso esconde `_publicacion` y `_proceso`, pero NO `borradores/` ni `reportes/`, que no
llevan guion bajo. Resultado: en la ficha aparecen, mezcladas con los capítulos reales,
todas las versiones repudiadas y todos los informes del validador — ahora mismo la
usuaria ve el `capitulo_1_el_reloj_v0.3` que ya repudió junto al v0.4 vigente, sin
forma de distinguirlos.

Arréglalo por nombre, además del prefijo:
      val internas = setOf("borradores", "reportes")
      if (folderSubPathList.drop(1).any { it.startsWith("_") || it.lowercase() in internas })
          continue

(Se arregla acá y no renombrando las carpetas en el repo de contenido: esos dos nombres
están escritos en ~67 lugares de las skills y de 9 definiciones de agentes del motor de
escritura, y basta que se escape uno para que el próximo capítulo vuelva a crear la
carpeta sin prefijo y la ficha se ensucie otra vez.)

Test: un árbol con `.../relato/borradores/capitulo_1/x_v0.3.md` y
`.../relato/reportes/capitulo_1/informe.md` NO produce entradas de literatura;
`.../relato/capitulo_1_x_v0.4.md` sí.

=====================================================================
4. TESTS — QUE EJERZAN LA RUTA, NO LA FUNCIÓN SUELTA
=====================================================================
Un test que llama a `isValidImageResolution(286,512)` directamente NO prueba nada sobre
el share: pasa aunque la pantalla jamás la invoque. Fue exactamente lo que ocurrió.
BORRA `ShareAssignmentScreenTest.kt` tal como está y escríbelo de nuevo así:

  - Renderiza ShareAssignmentScreen con un bitmap 286x512 y verifica con
    `onNodeWithText("Subir a la flota").assertDoesNotExist()`.
  - Renderiza ShareAssignmentScreen con un bitmap 1024x1024 y verifica lo MISMO
    (la política es por RUTA, no por tamaño).
  - Verifica que el texto explicativo del punto 1 SÍ se muestra.
  - Llama a `uploadImageToGithub` con un bitmap 286x512 y verifica que rechaza
    (sin pasar por ninguna pantalla).
  - Galería 1024x1024 -> sube, y el mensaje de commit contiene "[gallery 1024x1024]".
  - Portapapeles 286x512 -> sigue bloqueado (prueba de no-regresión).

Corre con --rerun-tasks y pega la SALIDA REAL COMPLETA con los NOMBRES de los tests
ejecutados. "BUILD SUCCESSFUL" suelto o "32 up-to-date" no cuentan como evidencia.

=====================================================================
5. ENTREGA
=====================================================================
Commit + push reales, con el hash pegado desde `git rev-parse HEAD` (no describas el
comando: pega su salida). Y el APK.

Si algo no se pudo hacer, escríbelo al final bajo el título "NO HECHO:" con una línea
por punto. Un pendiente declarado vale más que un test verde inventado: el #7 declaró
verde un test que la realidad desmintió, y el costo fue un batch completo de imágenes
irrecuperables.
```
