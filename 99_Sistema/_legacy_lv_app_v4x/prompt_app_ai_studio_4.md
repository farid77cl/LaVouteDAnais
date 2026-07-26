# 📱 Prompt #4 (DEFINITIVO) para AI Studio — LV-App

> **Uso:** abrir el proyecto LV-App en AI Studio (con el código cargado, **no** un chat en blanco) y pegar TODO el bloque de abajo, de una sola vez.
>
> **Por qué reemplaza al #2 y al #3:** es **autocontenido**. No asume que lo pedido antes esté hecho: si ya está, AI Studio solo tiene que mostrarlo. Si no está, lo hace. Incluye además las **mejoras nuevas** (registro de descartes, eliminación de `generateMissingPrompt`, un toque para abrir Gemini, voz canónica de Ele).
>
> **Lo único que no se puede fabricar** y por eso se exige: los tests corridos con `--rerun-tasks`, el código pegado en la respuesta, el push al repo con hash, y el APK instalado.

---

```
Eres el desarrollador de LV-App (Kotlin / Jetpack Compose / Room / Retrofit / Moshi).

Antes de escribir una línea, entiende QUÉ ES esta app, porque de esto depende todo lo demás:

    LA APP NO GENERA IMÁGENES.
    La app muestra un prompt -> la usuaria lo COPIA al portapapeles -> lo PEGA a mano en Gemini
    -> Gemini genera la imagen -> la usuaria guarda la imagen -> la app la SUBE a GitHub.

    Es un VISOR + PORTAPAPELES + UPLOADER. El portapapeles ES el generador.
    Todo lo que no se copie al portapapeles, NUNCA llega a Gemini y no existe.

Esto no es teoría: por este motivo el bloque negativo de los prompts (que existe en el markdown
desde hace meses) NUNCA llegó al generador, y todas las imágenes del proyecto se hicieron sin él.

=====================================================================
CÓMO QUIERO LA ENTREGA (léelo primero, aplica a TODO lo de abajo)
=====================================================================
En un intento anterior me diste como prueba esta salida:

    > Task :app:testDebugUnitTest UP-TO-DATE
    BUILD SUCCESSFUL in 1s
    32 actionable tasks: 32 up-to-date

"UP-TO-DATE" significa que Gradle NO EJECUTÓ nada: saltó las tareas por caché. Esa salida no
demuestra que un solo test pase. No la repitas.

Para CADA punto de este encargo quiero:
  1. El CÓDIGO REAL pegado en la respuesta (no una descripción de lo que hace).
  2. Si el punto ya estaba implementado, dímelo explícitamente y pégame el código que lo prueba.
  3. Al final: la salida literal de `./gradlew test --rerun-tasks` (si aparece "UP-TO-DATE",
     no sirve).
  4. Commit + push a origin/main del repo farid77cl/LV-App, y el HASH del commit. Ese repo es
     el respaldo: mientras el código no esté ahí, nadie más que tú puede leerlo.
  5. El APK compilado, para instalarlo y probarlo con los ojos.

Un test rojo declarado es infinitamente mejor que un BUILD SUCCESSFUL inventado.

=====================================================================
1. EL NEGATIVO TIENE QUE LLEGAR A GEMINI  ⭐ (el bug más caro del proyecto)
=====================================================================
En el markdown `galeria_outfits.md`, cada look termina con una línea así (INLINE, backticks
simples):

    **Negative Prompt:** `ugly, bad hands, missing fingers, flat shoes, sneakers, barefoot, ...`

Ese negativo es POR LOOK (aplica a las 7 poses), no por pose. Hoy los 591 looks lo tienen.

1.1 · PARSEARLO
    - Agrega el campo `negativePrompt: String?` a `LookEntity` (data/local/Entities.kt) con su
      migración de Room.
    - Captúralo en `parseMarkdown` (GitRepository.kt).
    - CUIDADO: esa línea mide más de 100 caracteres y contiene la palabra "prompt", así que hoy
      cae en la rama de detección de poses (GitRepository.kt ~línea 486) y se descarta EN SILENCIO.
      Detéctala ANTES de esa rama.
    - Si el look no lo trae, `negativePrompt` queda en null.

1.2 · COPIARLO — UN SOLO BOTÓN, Y COPIA TODO
    NO quiero dos botones ("copiar positivo" / "copiar negativo").
    Quiero UN SOLO botón de copiar —el de siempre— que copie el prompt COMPLETO de un toque:

        <prompt positivo tal cual>

        Do not include: <negative prompt tal cual>

    Razón: si el negativo depende de que la usuaria se acuerde de apretar un segundo botón, algún
    día no lo va a apretar, y se genera otra vez sin negativo — que es EXACTAMENTE el bug que
    estamos arreglando. Lo que se puede olvidar, se olvida. Un solo botón lo hace imposible.

    IMPORTANTE — NO uses la sintaxis `--no <negativo>`. Ese formato es de Midjourney / Stable
    Diffusion. El destino aquí es GEMINI, que es CONVERSACIONAL: leería "--no" como texto literal
    y podría dibujar justo lo que se quiere evitar. Tiene que ir en lenguaje natural y en inglés
    (los prompts están en inglés): "Do not include: ...".

    Si `negativePrompt == null`, el botón copia solo el positivo, SIN agregar una línea
    "Do not include:" vacía. Y marca ese look de forma visible en la UI (le falta el negativo).

=====================================================================
2. BLOQUEA LAS MINIATURAS  ⭐ (el daño más silencioso)
=====================================================================
Descubrimiento del 14/07: 1.701 imágenes del repositorio (el 40% de la flota) están subidas como
MINIATURAS de ~286x512 px (0,15 MP). Las que se subieron por otra vía están en 1024x1024 (1,05 MP).
Se perdió la resolución de meses de trabajo, y nadie se dio cuenta porque en pantalla chica se ven
bien.

La causa NO es tu código de resize (ese está bien: `maxDim = 1200` solo achica lo que ya es MAYOR
a 1200; una imagen de 1024 pasa intacta). La causa es la ruta de PEGAR DESDE EL PORTAPAPELES
(PromptFilterScreen.kt, el FilledIconButton que hace
`clipboard.primaryClip` -> `item.uri` -> `BitmapFactory.decodeStream`):

    Cuando la usuaria aprieta "Copiar" en Gemini, Android NO pone la imagen original en el
    portapapeles — pone un PREVIEW REDUCIDO (el portapapeles tiene límite de tamaño). La app lee
    ese preview fielmente y sube una miniatura.

2.1 · VALIDA la resolución ANTES de subir, en LAS DOS rutas (el selector de galería y el pegado
      del portapapeles). Si `width < 800 && height < 800` (o el total de píxeles es < 500.000):
        - NO subas la imagen.
        - Muestra un diálogo claro:
             "⚠️ Esta imagen es una MINIATURA (<width>x<height>).
              El botón 'Copiar' de Gemini entrega un preview reducido, no el original.
              Descarga la imagen en Gemini ('Guardar imagen') y súbela con el selector de galería."
        - Deja un botón secundario "Subir igual" por si es un caso legítimo, pero que NO sea el
          botón por defecto.

2.2 · MUESTRA SIEMPRE la resolución de la imagen elegida antes de confirmar la subida:
      "1024x1024 ✓" en verde, o "286x512 ⚠️ miniatura" en rojo. Que se vea, siempre.

2.3 · Si puedes: al pegar desde el portapapeles, intenta primero resolver la URI a su archivo
      original (por ejemplo si el ClipData trae también un `item.text` con una URI de archivo, o
      si el ContentProvider expone un stream mayor). Si no se puede recuperar el original, aplica
      2.1 y manda a la usuaria al selector de galería.

Una imagen mal generada se regenera. Una imagen subida en miniatura se pierde en silencio.

=====================================================================
3. REGISTRAR LOS DESCARTES  ⭐⭐ (LA MEJORA MÁS IMPORTANTE DE TODO EL ENCARGO)
=====================================================================
Contexto — por qué esto vale más que cualquier otra cosa:

    La usuaria genera una pose. Sale mal (el zapato equivocado, la costura de la media al frente,
    el material sale mate en vez de brillante...). La borra y la regenera. A veces 5, 8 veces.
    Su dolor declarado, textual, es: "regenerar la misma pose mil veces".

    Y hoy, cuando borra la imagen fallada, EL DATO SE PIERDE PARA SIEMPRE. El repositorio guarda
    solo las SOBREVIVIENTES. Nadie sabe cuántos intentos costó cada pose, ni POR QUÉ falló.
    El motor de prompts se corrige a ciegas: se escribe una regla y no hay forma de saber si sirvió.

    Cuando el punto 1 quede hecho y el negativo por fin llegue a Gemini, NO VAMOS A PODER
    DEMOSTRAR QUE SIRVIÓ, porque no tenemos con qué comparar. Este punto crea ese "antes".

3.1 · EL DIÁLOGO
Hoy existe una acción de borrar imagen (los commits dicen "Delete image via Voute App").
Cuando la usuaria borre una imagen, ANTES de borrarla, la app pregunta POR QUÉ.
Botones de un toque, NO texto libre (la usuaria tiene uñas de 5 cm: escribir es un impuesto):

    ¿Por qué la descartas?
    [ Costura de la media al frente ]    [ Zapato incorrecto ]
    [ Marcas/piercings sobre la tela ]   [ Corte no pedido en la ropa ]
    [ Anatomía (manos / piernas) ]       [ Material mate, no brilla ]
    [ Pose equivocada ]                  [ La bloqueó el filtro (safe) ]
    [ Outfit distinto a las otras poses ][ Otro ]
    [ Saltar ]

  - Un solo toque cierra el diálogo Y borra la imagen. No pidas confirmar dos veces.
  - "Otro" abre un campo de texto corto (opcional).
  - "Saltar" borra sin registrar motivo (pero igual registra el descarte, con motivo = "sin_motivo").
    Nunca bloquees el borrado por esto.
  - Códigos internos exactos (no los traduzcas, los voy a leer con scripts):
        costura_frente · zapato_incorrecto · marcas_sobre_tela · corte_no_pedido · anatomia ·
        material_mate · pose_equivocada · filtro_safe · outfit_inconsistente · otro · sin_motivo

3.2 · DÓNDE SE GUARDA (importante: local primero, repo después)
  - Crea una tabla Room `DescarteEntity`:

        @Entity(tableName = "descartes")
        data class DescarteEntity(
            @PrimaryKey(autoGenerate = true) val id: Long = 0,
            val fechaIso: String,      // "2026-07-14T18:32:05"
            val lookNumber: Int,
            val poseName: String,      // nombre canónico: standing, back_view, seated,
                                       // side_profile, ditzy, pov, odalisque
            val motivo: String,        // uno de los códigos de arriba
            val notaLibre: String?,    // solo si motivo == "otro"
            val intento: Int,          // ver 3.3
            val sincronizado: Boolean = false
        )

  - La tabla Room es la FUENTE DE VERDAD y se escribe SIEMPRE, aunque no haya red. Un descarte
    NUNCA se pierde por un fallo de conexión.
  - Sincronización al repo: un botón (o junto al sync existente) que REGENERA el archivo
    `99_Sistema/descartes.csv` en GitHub a partir de la tabla completa, y lo sube con PUT usando
    el SHA actual. NO hagas un append ciego por cada borrado (te vas a pelear con el SHA y vas a
    perder registros). Regenerar el archivo entero desde la tabla es idempotente y a prueba de
    fallos. Al terminar, marca las filas como `sincronizado = true`.

  - Formato exacto del CSV (cabecera incluida, UTF-8 sin BOM, separador coma):

        fecha,look,pose,motivo,intento,nota
        2026-07-14T18:32:05,785,odalisque,zapato_incorrecto,3,
        2026-07-14T18:41:12,785,odalisque,material_mate,4,
        2026-07-14T19:02:44,786,standing,otro,1,"el fondo salió con texto"

3.3 · EL CONTADOR DE INTENTOS
  - `intento` = (cantidad de descartes ya registrados para ese look + esa pose) + 1.
  - En la ficha de cada pose, MUESTRA ese número cuando sea > 0: un badge discreto que diga
    "3 intentos" o "⚠️ 5 intentos". Así la usuaria ve al instante qué poses son problemáticas, y
    yo veo qué prompts hay que reescribir.
  - Si una pose ya tiene imagen subida y no tiene descartes, no muestres nada.

Esto es barato de implementar (un diálogo + una tabla + una subida) y es lo que convierte el
proyecto de "arreglar a ciegas" a "medir y corregir". Es el punto que más quiero de toda la lista.

=====================================================================
4. ELIMINA `generateMissingPrompt()`  🔴 (está rompiendo el canon)
=====================================================================
MainViewModel.kt:780 ->

    fun generateMissingPrompt(look: LookEntity, poseName: String, onComplete: (String) -> Unit) {
        val newPromptText = geminiRepository.generatePrompt(look.canonicalInfo, poseName)

Cuando falta el prompt de una pose, la app le pide a GEMINI QUE LO INVENTE a partir de
`canonicalInfo`. Pero en los looks nuevos `canonicalInfo` es solo `Ubicacion` + `Tags`: NO
contiene el "Bloque A" del ADN del personaje (rasgos físicos fijos), ni el token de vestuario
bloqueado, ni el de calzado, ni las anclas de pose. Un prompt así produce un personaje que NO es
el personaje. Rompe la consistencia entre las 7 poses de un mismo look, que por canon deben
compartir el bloque físico IDÉNTICO, palabra por palabra.

Además ya no hace falta: desde el 14/07 los 591 looks tienen sus 7 prompts completos.
Es riesgo puro, sin beneficio.

ACCIÓN: elimina el botón y la función.
Si insistes en conservar la funcionalidad, entonces que NO INVENTE: que construya el prompt
copiando el Bloque A + outfit + calzado DE OTRA POSE DEL MISMO LOOK y cambie solo la dirección
de la pose. La IA nunca redacta el ADN.

=====================================================================
5. LAS CARPETAS: UN LOOK, UNA SOLA CARPETA
=====================================================================
Resultado real de los bugs de abajo: 35 looks con DOS carpetas y las poses repartidas entre ambas.

5.1 · `slugify()` — GitRepository.kt línea ~127 tiene hoy:

        val slug = look.name.lowercase().replace(Regex("[^a-z0-9]"), "_").replace(Regex("_+"), "_")

    Esa línea creó carpetas reales como `look616_lencer_a` (de "Lencería") y
    `look709_suzie_wong_shangh_i` (de "Shanghái"): la tilde no es [a-z0-9], así que se convierte
    en "_" y parte la palabra.

    Reemplázala por `val slug = slugify(look.name)`, con:

        fun slugify(name: String): String {
            val folded = java.text.Normalizer.normalize(name, java.text.Normalizer.Form.NFD)
                .replace(Regex("\\p{Mn}+"), "")                        // í -> i, ñ -> n
            return folded.lowercase()
                .replace("-", "").replace("'", "").replace("’", "")  // "Coat-Dress" -> "coatdress"
                .replace(Regex("[^a-z0-9]+"), "_")
                .trim('_')
        }

    Debe cumplir:
        slugify("Lencería Burgundy Boots")  == "lenceria_burgundy_boots"
        slugify("Jade Coat-Dress Boardroom")== "jade_coatdress_boardroom"
        slugify("Shanghai Qipao Líquido")   == "shanghai_qipao_liquido"
        slugify("Cherry Polka Dot Pin-Up")  == "cherry_polka_dot_pinup"

5.2 · Línea ~128: `String.format("%03d", look.number)` produce `look099_` / `ele_099_standing.png`
    para el look 99. El canon es `look99_` / `ele_99_`. Usa `look.number.toString()`.

5.3 · RESOLUCIÓN DE LA CARPETA DESTINO, EN ESTE ORDEN ESTRICTO:
        a) ¿Existe alguna imagen de ESTE LOOK, de CUALQUIER pose? -> usa su carpeta padre.
        b) ¿El markdown declara `Ubicacion` para este look?       -> usa esa carpeta.
        c) Si no                                                   -> `look<N>_<slugify(titulo)>`.

    Hoy PromptFilterScreen.kt línea ~164 hace:
        val existingImage = matchedImages.firstOrNull { matchesPose(selectedPose, it.poseName) }
    o sea, solo reutiliza la carpeta si ya existe una imagen de LA MISMA POSE. Para la primera
    imagen de cada pose, `existingPath` es null y `saveImageToGithub` inventa la carpeta desde el
    slug del título. Si esa carpeta no coincide con la que el look ya tiene -> segunda carpeta.

    NUNCA crear un segundo directorio para un número de look que ya tiene uno.

5.4 · `extractLookNumber()` (GitRepository.kt ~741) hace `"\\d+".toRegex().find(path)`: toma el
    PRIMER número de la ruta. Ánclalo: `^ele/look0*(\d+)_` (o equivalente sobre la ruta completa).

=====================================================================
6. LEE LA CATEGORÍA, NO LA ADIVINES
=====================================================================
GitRepository.kt ~373-403 adivina la categoría por keywords, con 13 categorías propias
("Moda Elegante", "Gótico & Dark") que NO son las del canon. Y falla feo: la keyword "platform"
manda el look a "Stripper & Pole"... cuando TODOS los looks llevan plataforma, y TODOS son fetish.
Los filtros de la app están filtrando por categorías falsas.

El markdown declara la categoría explícitamente, entre el título del look y el primer `###`:

    - **Ubicacion:** `05_Imagenes/ele/look787_gold_marquee_bodycon/`
    - **Categoria:** Nightclub
    - **Tags:** #glamrock #nightclub #gold #batchL781-L790 #V5poses

  - Parsea esos campos `- **Clave:** valor` (hoy se guardan crudos en `canonicalInfo` y nunca se
    leen). Expón al menos `ubicacion` y `categoria` en LookEntity.
  - En el archivo conviven claves CON y SIN tilde (`**Ubicación:**` y `**Ubicacion:**`).
    Normaliza la CLAVE quitando diacríticos antes de compararla, o vas a encontrar solo la mitad.
  - Lista cerrada de 10 categorías válidas:
        Stripper · Corporate · Escort · Domestic · Pin-Up
        High-Fashion Editorial · Nightclub · Lencería · Bikini · Gym
    Normaliza al leer: "Lenceria"->"Lencería", "Gym/Athleisure"->"Gym",
    "HF Editorial"->"High-Fashion Editorial". "Mix" NO es una categoría válida.
  - Usa la inferencia por keywords SOLO como fallback cuando el campo no exista.

=====================================================================
7. UN BLOQUE DE CÓDIGO NUNCA CRUZA EL LÍMITE DE UN LOOK
=====================================================================
GitRepository.kt ~462-482 y ~559-565: al ver una línea que empieza con ``` se pone
`isReadingCodeBlock = true` y se acumula hasta encontrar OTRA línea que empiece con ```.
Si el fence está mal formado, sigue tragando y MEZCLA prompts entre poses y entre looks.

Cierra el bloque también cuando, estando dentro de él, aparezca lo primero de:
    - una línea `**<Pose>:**`
    - un heading `##` o `###`
    - el inicio de otro look

=====================================================================
8. MENOS TOQUES POR IMAGEN
=====================================================================
8.1 · Botón "Abrir Gemini": UN toque que copia el prompt completo (positivo + "Do not include:")
      Y abre la app de Gemini. Hoy son cuatro pasos (copiar -> salir -> abrir Gemini -> pegar),
      multiplicados por 7 poses por look. Usa un Intent a la app de Gemini si está instalada, con
      fallback al navegador.

8.2 · Marcar un look como "cerrado" para no volver a mirarlo.

=====================================================================
9. LA VOZ DE ELE EN EL CHAT NO ES LA CANÓNICA
=====================================================================
`GeminiRepository.chatWithEle()` define una Ele que "habla de sí misma en tercera persona o como
'esta bimbo' / 'madame'". Eso no es el personaje. El canon es: chilena cuica, habla de TÚ (jamás
voceo argentino: nada de "vos/podés/mirá"), trata a la usuaria de "cariño", primera persona,
sensual y lenta. Corrige el system prompt.

=====================================================================
10. EL TOKEN DE GITHUB VA COMPILADO DENTRO DEL APK (hazlo al final, o dime si complica)
=====================================================================
`BuildConfig.GITHUB_PAT` y `BuildConfig.GEMINI_API_KEY` quedan dentro del APK y son extraíbles con
herramientas triviales. Si el APK sale del teléfono, cualquiera puede escribir en el repositorio.
Ideal: moverlos a EncryptedSharedPreferences, pegados una sola vez desde una pantalla de ajustes.
Mínimo aceptable: un PAT con alcance mínimo (solo `contents:write` de ese repo) y rotable.
Si esto complica la entrega de lo demás, déjalo para el final y avísame — pero no lo omitas en
silencio.

=====================================================================
QUÉ VOY A COMPROBAR CON LOS OJOS AL INSTALAR EL APK
=====================================================================
  · Aprieto el botón de copiar UNA vez, pego en cualquier parte, y aparece el positivo Y el
    "Do not include: ...".
  · Los looks sin negativo salen marcados.
  · Si intento subir una imagen chica, la app me FRENA y me dice que es una miniatura.
  · Veo la resolución de la imagen ANTES de confirmar la subida.
  · Al borrar una imagen, me pregunta POR QUÉ con botones de un toque.
  · Veo "N intentos" en las poses que ya descarté varias veces.
  · Subo una pose nueva a un look que ya tiene carpeta, y NO se crea una carpeta gemela.

Eso lo compruebo yo. No hace falta que me lo describas: hazlo, pégame el código, corre los tests
con --rerun-tasks, pushea, y dame el APK.
```

---

## ✅ Cómo verificar sin depender de lo que AI Studio diga

| Prueba | Qué significa |
|---|---|
| **Apretar «copiar» y pegar el portapapeles en cualquier parte** | Si aparece el positivo **y** el `Do not include: ...`, está implementado. Si sale solo el positivo, el reporte era humo. |
| **Borrar una imagen** | Si no pregunta «¿por qué la descartas?», el punto 3 no está. |
| **Elegir una imagen para subir** | Si no se ve la resolución antes de confirmar, el punto 2 no está. |
| **Subir una pose a un look que YA tiene carpeta** | Si crea una carpeta gemela (`look<N>_otro_slug/`), el punto 5 no está. |
| **`git log origin/main` en LV-App** | Si aparece un commit nuevo con implementación (no solo tests), se puede auditar línea por línea. |

> ⚠️ **`--no` NO sirve aquí.** Es sintaxis de Midjourney / Stable Diffusion. El destino es **Gemini**, que es conversacional y lo tomaría como texto literal — podría dibujar justo lo que se quiere evitar. El negativo va en lenguaje natural: `Do not include: ...`.

> 📊 **El punto 3 (descartes) es el que cambia el juego.** Sin él seguimos corrigiendo el motor a ciegas y, cuando el negativo por fin llegue a Gemini, **no vamos a poder demostrar que sirvió** — no existe el «antes» contra el cual comparar.
