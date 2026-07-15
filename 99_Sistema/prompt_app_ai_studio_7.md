# 📱 Prompt #7 (DEFINITIVO) para AI Studio — Compartir desde Gemini: subir O descartar

> **Reemplaza al #6.** Idea de la Ama (15/07): el share de Android pasa la imagen REAL (no el
> preview del portapapeles) → un solo destino "LV-App" con DOS acciones adentro: **subir al repo**
> (la buena) o **registrar descarte** (la fallada, con motivo + evidencia visual). Esto cierra el
> punto ciego histórico del motor: hasta hoy los descartes ocurrían dentro de Gemini y nadie los
> veía — el motor se corregía a ciegas.
>
> **Dónde queda cada cosa:** la buena → `05_Imagenes/` (la flota, como siempre). La fallada →
> `99_Sistema/descartes/` como evidencia REDUCIDA (JPEG ~512px) + fila en `descartes.csv`.
> Nunca se mezclan.

---

```
Eres el desarrollador de LV-App (Kotlin / Jetpack Compose / Room / Retrofit / Moshi).
Trabaja sobre el repo al día. Entrega como siempre: código real pegado, tests con
--rerun-tasks (nada de UP-TO-DATE), commit+push con hash, APK.

REGLAS INTOCABLES:
- El botón de copiar prompt sigue copy-only (nada de abrir apps tras copiar).
- La guardia de resolución del #5 sigue intacta PARA SUBIDAS A LA FLOTA. (Para descartes
  NO aplica — ver punto 4.)
- ⭐ EL SISTEMA ANTERIOR SE QUEDA COMO RESPALDO (orden directa de la usuaria): el botón
  de PEGAR DESDE PORTAPAPELES y el SELECTOR DE GALERÍA (subida directa) permanecen
  visibles y funcionales exactamente como están hoy, con su guardia y su badge.
  El share es un camino ADICIONAL, no un reemplazo. PROHIBIDO eliminar, esconder,
  deshabilitar o "refactorizar" los flujos existentes: si Compartir falla algún día,
  la usuaria vuelve al flujo viejo sin depender de nadie.

=====================================================================
1. LV-APP COMO DESTINO DE "COMPARTIR" (ACTION_SEND)
=====================================================================
- Registra la MainActivity (o una activity-alias) con intent-filter ACTION_SEND,
  mimeType "image/*", label "LV-App" en el AndroidManifest.
- Al recibir el share: lee EXTRA_STREAM (content URI), decodifica el bitmap y llévalo
  a la pantalla de asignación: la usuaria elige (o confirma) LOOK y POSE como siempre.
- Con look+pose elegidos, muestra DOS acciones grandes e inconfundibles:
      [ ✅ Subir a la flota ]        [ 🗑️ Registrar descarte ]

=====================================================================
2. ACCIÓN "SUBIR A LA FLOTA" (la imagen buena)
=====================================================================
- Reusa EXACTAMENTE el flujo existente: guardia isValidImageResolution (bloqueo si
  <400.000 px²) + diálogo de confirmación con badge de resolución + uploadImageToGithub.
  Cero lógica duplicada. La imagen queda en 05_Imagenes/ como cualquier subida de hoy.

=====================================================================
3. ACCIÓN "REGISTRAR DESCARTE" (la imagen fallada)
=====================================================================
- Pide el MOTIVO con chips de un toque (obligatorio uno) + nota libre opcional:
      collage/grilla · guantes/mangas · marcas sobre la tela · costura al frente ·
      calzado mutado · anatomía (manos/piernas) · pose desviada · outfit mutado ·
      cara/ADN · otro
- Crea el DescarteEntity con el DAO YA EXISTENTE (fechaIso, lookNumber, poseName
  canónica, motivo, notaLibre, intento = count+1) y sincroniza a 99_Sistema/descartes.csv
  con el syncDescartes YA EXISTENTE.
- EVIDENCIA VISUAL (lo nuevo): reduce la imagen a máx 512px en su lado largo, comprime
  JPEG calidad 70 (~40-80 KB) y súbela vía el mismo putFile de GitRepository a:
      99_Sistema/descartes/L{look}_{pose}_i{intento}_{motivo}.jpg
  Agrega la columna `evidencia` (ruta del jpg) al CSV.
- PROHIBIDO que un descarte toque 05_Imagenes/, el tracker de la galería o cualquier
  estructura de la flota. El descarte vive SOLO en 99_Sistema/descartes/ + el CSV.

=====================================================================
4. GUARDIA Y DESCARTES
=====================================================================
- La guardia de resolución NO bloquea descartes: una evidencia de 286px sirve igual
  (el defecto grueso se ve, y el punto es registrar el fallo, no coleccionar arte).
  El badge de resolución sí se muestra, informativo.

=====================================================================
5. TESTS (con --rerun-tasks, pegar salida real)
=====================================================================
- Share con imagen 1024x1024 + acción subir -> pasa guardia, llega al diálogo con badge.
- Share con imagen 286x512 + acción subir -> bloqueada por la guardia.
- Share con imagen 286x512 + acción descarte -> NO bloqueada; genera DescarteEntity con
  intento correcto y nombre de archivo de evidencia con el patrón especificado.

Por qué la evidencia va REDUCIDA: el repo de contenido ya pesa mucho y la Ama decidió
no usar LFS ni reescrituras. Un JPEG de 512px basta para ver collage/guantes/cortes/
calzado; miles de PNG completos de descartes inflarían el repo sin retorno.
```
