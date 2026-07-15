# 📱 Prompt #5 para AI Studio — LV-App (post batch de prueba 15/07/2026)

> **Uso:** abrir el proyecto LV-App en AI Studio (con el código cargado, **no** un chat en blanco) y pegar TODO el bloque de abajo, de una sola vez.
>
> **Contexto:** el #4 ya se aplicó y **funciona lo esencial** — el botón único copia positivo + `Do not include:` + negativo, y la Ama da fe de que el negativo llega pegado a Gemini. Pero el #4 trajo **un cambio dañino** (abrir Gemini automáticamente después de copiar), que la Ama ya revirtió a mano y commiteó. Este prompt: (1) prohíbe reintroducir ese comportamiento, (2) recupera el **pegado desde portapapeles** en la subida — que era más cómodo que descargar+esperar+subir — pero con la **guardia de resolución** que evita volver a llenar la flota de miniaturas de 286px.
>
> **Estado del repo:** los commits están al día (la reversión de la Ama incluida). Trabaja sobre lo que hay, no sobre lo que recuerdes del #4.

---

```
Eres el desarrollador de LV-App (Kotlin / Jetpack Compose / Room / Retrofit / Moshi).

Recordatorio de qué es esta app (no cambió):

    LA APP NO GENERA IMÁGENES.
    La app muestra un prompt -> la usuaria lo COPIA al portapapeles -> lo PEGA a mano en Gemini
    -> Gemini genera la imagen -> la usuaria la trae de vuelta -> la app la SUBE a GitHub.

    Es un VISOR + PORTAPAPELES + UPLOADER. El portapapeles ES el generador.

=====================================================================
CÓMO QUIERO LA ENTREGA (igual que el #4 — no negociable)
=====================================================================
  1. El CÓDIGO REAL pegado en la respuesta (no una descripción de lo que hace).
  2. Si un punto ya estaba implementado, dímelo explícitamente y pégame el código que lo prueba.
  3. Al final: la salida literal de `./gradlew test --rerun-tasks`. Si aparece "UP-TO-DATE",
     Gradle no ejecutó nada y esa salida no sirve como prueba.
  4. Commit + push a origin/main del repo farid77cl/LV-App, y el HASH del commit.
  5. El APK compilado, para instalarlo y probarlo con los ojos.

Un test rojo declarado es infinitamente mejor que un BUILD SUCCESSFUL inventado.

=====================================================================
0. LO QUE NO SE TOCA (léelo antes de escribir nada)
=====================================================================
0.1 · EL BOTÓN DE COPIA ES COPY-ONLY. PROHIBIDO abrir Gemini (o cualquier app) después de
     copiar. Nada de startActivity / Intent / launchUrl encadenado a la copia. El #4 pidió
     "un toque para abrir Gemini" y ROMPIÓ el flujo real de la usuaria; ella ya lo revirtió
     y ese revert está commiteado. Si ves código que abre Gemini tras la copia, es una
     REGRESIÓN: elimínala. El botón copia y no hace nada más.

0.2 · El FORMATO de lo copiado no se toca: un solo botón, un solo bloque al portapapeles =
     prompt positivo + salto de línea + "Do not include: " + el negativo del look. Está
     funcionando en producción (verificado con los ojos pegándolo en Gemini).

0.3 · parseMarkdown() no se toca. Los fences y la metadata de galeria_outfits.md ya están
     saneados del lado de los datos.

=====================================================================
1. RECUPERAR EL PEGADO DESDE PORTAPAPELES EN LA SUBIDA ⭐ (con guardia)
=====================================================================
Antes la usuaria podía COPIAR la imagen en Gemini y PEGARLA en la app para subirla. Era el
camino cómodo: dos toques. El problema NUNCA fue el pegado en sí — fue que el botón "Copiar"
de Gemini entrega un PREVIEW reducido (~286×512 px, porque Android limita el tamaño del
portapapeles) y la app lo subía fielmente: así se llenó el repo con 1.701 miniaturas
irrecuperables (el 40% de la flota).

Quiero el pegado DE VUELTA, pero con guardia de resolución:

1.1 · En la pantalla de subida, junto al selector de galería (que se queda como está),
     restaura el botón de PEGAR DESDE PORTAPAPELES (clipboard.primaryClip -> item.uri ->
     BitmapFactory.decodeStream, como existía antes).

1.2 · GUARDIA DE RESOLUCIÓN (el corazón de este encargo): después de decodificar el bitmap
     (venga del portapapeles O de la galería), calcula width * height.

       - Si width * height < 400_000 píxeles (≈ menos de 0.4 MP):
           BLOQUEA la subida. No hay botón de "subir igual".
           Muestra un diálogo claro, en el tono de la app:
             "Esta imagen mide {w}×{h}: es el PREVIEW que entrega el botón Copiar de Gemini,
              no la imagen real. Descárgala en Gemini y súbela con el selector de galería."
       - Si width * height >= 400_000: la subida sigue normal.

     Referencia real: las miniaturas malas miden 286×512 (0.15 MP); las imágenes sanas
     miden 669×1200 (0.80 MP) o 1024×1024 (1.05 MP). El umbral 0.4 MP separa limpio.

1.3 · BADGE DE RESOLUCIÓN: en la confirmación previa a la subida, muestra siempre la
     resolución de lo que se va a subir (ej. "1024×1024 ✓"). La usuaria valida con los
     ojos sin tener que confiar en la guardia.

1.4 · TEST UNITARIO de la guardia: un caso con 286×512 (debe bloquear) y un caso con
     669×1200 (debe pasar). Correr con --rerun-tasks y pegar la salida.

=====================================================================
2. NO HAY PUNTO 2. Entrega corta y quirúrgica.
=====================================================================
Este encargo es UN solo feature con su guardia y sus tests. No aproveches de refactorizar,
renombrar, ni "mejorar" nada que no esté en el punto 1. Cada línea fuera de alcance es
riesgo de regresión en una app que hoy funciona.
```
