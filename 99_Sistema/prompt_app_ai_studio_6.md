# 📱 Prompt #6 para AI Studio — LV-App (Compartir desde Gemini = comodidad + calidad)

> **Contexto:** la guardia de resolución del #5 funciona, pero le agregó fricción al flujo de la Ama: "Copiar" en Gemini entrega un preview de 286px (bloqueado por la guardia, correctamente), y el camino bueno (Descargar → galería) son demasiados toques.
>
> **La salida que elimina el dilema:** el menú **Compartir** de Android pasa la imagen REAL (un content URI al archivo completo), no el preview del portapapeles. Si LV-App se registra como destino de compartir, el flujo queda: en Gemini tocar **Compartir → LV-App** → la app se abre con la imagen full-res lista para asignar a la pose. **Dos toques, cero descargas, cero miniaturas.**
>
> **Pegar en AI Studio SOLO UNO de los dos bloques según lo que decida la Ama.**

---

## Bloque A — RECOMENDADO: LV-App como destino de "Compartir"

```
Eres el desarrollador de LV-App (Kotlin / Jetpack Compose / Room / Retrofit / Moshi).
Trabaja sobre el repo al día. Entrega igual que siempre: código real pegado, tests con
--rerun-tasks (nada de UP-TO-DATE), commit+push con hash, APK.

REGLA INTOCABLE: el botón de copiar prompt sigue copy-only (nada de abrir apps tras copiar).
La guardia de resolución del #5 NO se toca — este encargo la complementa.

ÚNICO PUNTO — LV-APP COMO SHARE TARGET DE IMÁGENES:

1. Registra la MainActivity (o una activity-alias) con un intent-filter ACTION_SEND
   (mimeType "image/*") en el AndroidManifest, con label "Subir a LV-App".

2. Al recibir el share: lee el EXTRA_STREAM (content URI), decodifica el bitmap y
   entra DIRECTO al flujo de subida existente de PromptFilterScreen:
   - la usuaria elige (o confirma) look y pose como siempre;
   - corre la MISMA guardia de resolución del #5 (isValidImageResolution) y el MISMO
     diálogo de confirmación con badge de resolución;
   - la subida usa el MISMO uploadImageToGithub. Cero lógica duplicada.

3. Si el share llega sin look/pose seleccionable (app recién abierta), navega a la
   pantalla de selección con la imagen ya cargada en memoria — nunca la descartes.

4. TEST: un test unitario del handler que recibe un URI y valida que (a) una imagen
   286x512 dispara el bloqueo, (b) una 1024x1024 llega al diálogo de confirmación.

Por qué esto y no el portapapeles: Android limita el tamaño de lo copiado (el "Copiar"
de Gemini entrega un preview ~286x512), pero COMPARTIR pasa el archivo real completo.
Este feature le devuelve a la usuaria el flujo de dos toques sin volver a llenar el
repo de miniaturas irrecuperables.
```

## Bloque B — SOLO si la Ama prefiere la vía rápida asumiendo miniaturas

```
Eres el desarrollador de LV-App. Trabaja sobre el repo al día. Entrega igual que siempre:
código real, tests con --rerun-tasks, commit+push con hash, APK.

ÚNICO PUNTO — SUAVIZAR LA GUARDIA DE BLOQUEO A ADVERTENCIA CONSCIENTE:

En el diálogo "Imagen Demasiado Pequeña" del #5, agrega un botón secundario
"Subir igual (queda en baja calidad)" que continúe la subida con la imagen tal cual.
El texto del diálogo debe seguir mostrando la resolución real y la advertencia.
El botón primario sigue siendo "Entendido" (cancelar). La decisión queda registrada:
loguea un DescarteEntity con motivo "subida_baja_resolucion" NO — mejor: agrega el
sufijo "_lowres" al mensaje del commit de subida, para poder auditar después cuántas
miniaturas entraron conscientemente.

NADA MÁS. La guardia, el badge y los tests del #5 quedan intactos.
```
