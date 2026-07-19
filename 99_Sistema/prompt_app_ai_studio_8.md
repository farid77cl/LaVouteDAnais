# 📱 Prompt #8 para AI Studio — El share entrega previews: cerrar la rama y trazar el origen

> **No reemplaza al #7: lo AUDITA.** El #7 ya especificaba en §2 que "Subir a la flota" desde el
> share debía reusar la guardia de resolución, y en §5 declaraba el test
> `Share con imagen 286x512 + acción subir -> bloqueada por la guardia`. Ese test fue reportado
> como pasado.
>
> **Contraprueba del 19/07/2026:** entraron a la flota **34 imágenes por esa rama, todas de
> 286×512 (vertical) o 512×279 (horizontal)** — lado largo topado en 512 exacto, ~146.000 px²,
> muy por debajo del umbral de 400.000. La usuaria confirma que la app **muestra la imagen y
> reporta su medida** antes de subirla. Si la guardia corriera ahí, ninguna habría entrado.
> El test declarado no pudo ser real.
>
> **Hallazgo de fondo (no lo arregla el código):** Gemini adjunta al share un **preview de 512 px**,
> no el archivo original. No hay más píxeles que pedir en ese intent. Comparar: las subidas por
> **Descargar + selector de galería** llegan en 669×1200 (lado largo 1200 = el `maxDim` de la
> propia app redimensionando un original grande). La ruta buena pasa por el resize de la app;
> la del share llega ya en 512.
>
> **Consecuencia:** la rama "subir a la flota" del share **no puede existir**. No es afinarla.
> El share queda solo para registrar descartes, donde 512 px basta.

---

```
Eres el desarrollador de LV-App (Kotlin / Jetpack Compose / Room / Retrofit / Moshi).
Trabaja sobre el repo al día.

CONTEXTO — ESTO ES UNA AUDITORÍA DE UNA ENTREGA ANTERIOR, NO UNA FEATURE NUEVA.
El prompt #7 declaró pasado este test:
    "Share con imagen 286x512 + acción subir -> bloqueada por la guardia"
En producción entraron 34 imágenes de 286x512 y 512x279 por exactamente esa ruta.
No expliques por qué pudo pasar: MUÉSTRAME EL CÓDIGO ACTUAL Y QUÉ HACE.

=====================================================================
0. EVIDENCIA PRIMERO (antes de tocar una línea)
=====================================================================
Pega, tal como están HOY en el repo, sin editar ni resumir:
  a) El AndroidManifest.xml completo de la activity que recibe ACTION_SEND
     (intent-filter, mimeTypes, activity-alias si existe).
  b) La función que maneja el share entrante, íntegra, desde que lee EXTRA_STREAM
     hasta que llama a subir.
  c) TODAS las llamadas a isValidImageResolution del proyecto, con su archivo y
     su línea. Si en la ruta del share no hay ninguna, dilo con esa palabra:
     "en la ruta del share NO hay llamada a la guardia".
  d) `git log --oneline -5` real de la rama de trabajo.

=====================================================================
1. ELIMINAR "SUBIR A LA FLOTA" DEL SHARE
=====================================================================
Gemini solo adjunta un preview de 512 px al compartir: esa rama no puede
alimentar la flota ni con guardia. Al recibir un share, la app ofrece
ÚNICAMENTE:
      [ 🗑️ Registrar descarte ]
El botón de subir a la flota desaparece de la pantalla de share. Si la usuaria
llega ahí con una imagen buena, un texto se lo dice derecho:
      "Compartir solo entrega una miniatura de 512 px.
       Para subir a la flota: Descargar en Gemini → selector de galería."

⭐ INTOCABLE (orden directa de la usuaria, ya estaba en el #7): el botón de PEGAR
DESDE PORTAPAPELES y el SELECTOR DE GALERÍA siguen visibles y funcionales tal
como están, con su guardia y su badge. No se eliminan, no se esconden, no se
"refactorizan". Aquí solo se recorta la pantalla del share.

=====================================================================
2. GUARDIA DEFENSIVA IGUAL (cinturón y tirantes)
=====================================================================
Aunque el botón ya no exista, `uploadImageToGithub` debe RECHAZAR por sí misma
cualquier bitmap bajo 400.000 px², venga de donde venga. La guardia deja de ser
una validación de pantalla y pasa a ser una precondición de la función que
escribe en el repo. Una pantalla se puede olvidar; la función que sube, no.

=====================================================================
3. TRAZAR EL ORIGEN DE CADA SUBIDA (lo que cierra esta clase de bug)
=====================================================================
Añade un enum ImageSource { CLIPBOARD, GALLERY, SHARE } que viaje con el bitmap
desde su punto de entrada hasta el commit, y regístralo en el MENSAJE DE COMMIT
junto a la resolución real:
      "Upload image Look 309 Ditzy [gallery 1024x1024]"
Con eso, la próxima vez que aparezca una miniatura en la flota se sabe por qué
puerta entró sin tener que deducirlo de los píxeles. Hoy eso costó una auditoría
entera.

=====================================================================
4. TESTS — CON PRUEBA NO FALSIFICABLE
=====================================================================
Corre con --rerun-tasks y pega la SALIDA REAL COMPLETA (nada de "32 up-to-date",
nada de "BUILD SUCCESSFUL" suelto: quiero los nombres de los tests ejecutados).
  - Share 286x512  -> la pantalla NO ofrece subir a la flota; solo descarte.
  - Share 1024x1024 -> tampoco ofrece subir (la política es por RUTA, no por tamaño).
  - uploadImageToGithub llamada directamente con un bitmap 286x512 -> lanza/rechaza.
  - Galería 1024x1024 -> sube, y el mensaje de commit incluye "[gallery 1024x1024]".
  - Portapapeles 286x512 -> sigue bloqueada como hasta hoy (no hubo regresión).

=====================================================================
5. ENTREGA
=====================================================================
Commit + push REALES con su hash de `git rev-parse HEAD` pegado, y el APK.
Si algo no se pudo hacer, dilo en una línea al final bajo el título
"NO HECHO:". Prefiero un pendiente declarado que un test inventado — el #7
declaró verde un test que la realidad desmintió, y eso costó un batch entero
de imágenes irrecuperables.
```
