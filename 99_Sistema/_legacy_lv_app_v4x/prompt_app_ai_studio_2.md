# 📱 Prompt #2 para AI Studio — LV-App: **implementa el código, los tests ya están**

> **Contexto:** en el commit `bc32f6d` AI Studio escribió los tests (`ParserTest.kt`) pero **no implementó el código**. Los tests llaman a `repo.slugify()` y leen `looks[0].negativePrompt`, y **ninguno de los dos existe** → el módulo de test **no compila**.
> **Lo bueno:** los tests son correctos y sirven de especificación ejecutable.

---

```
En el commit bc32f6d agregaste los tests a app/src/test/java/com/example/ParserTest.kt,
pero NO implementaste el código que esos tests necesitan. El módulo de test NO COMPILA:

  - ParserTest llama a `repo.slugify(...)`  ->  GitRepository NO tiene ese método.
  - ParserTest lee `looks[0].negativePrompt` -> LookEntity NO tiene ese campo.

NO escribas más tests. Los tests ya son la especificación. Implementa el código de producción
hasta que `./gradlew test` pase en verde.

Estos son los 5 tests que hay que hacer pasar, y lo que cada uno exige:

---------------------------------------------------------------------
1. testSlugify
---------------------------------------------------------------------
Exige: un método `slugify(name: String): String` en GitRepository (visible para el test).

    assertEquals("lenceria_burgundy_boots", repo.slugify("Lencería Burgundy Boots"))
    assertEquals("jade_coatdress_boardroom", repo.slugify("Jade Coat-Dress Boardroom"))
    assertEquals("shanghai_qipao_liquido",  repo.slugify("Shanghai Qipao Líquido"))
    assertEquals("cherry_polka_dot_pinup",  repo.slugify("Cherry Polka Dot Pin-Up"))

Implementación: plegar los acentos a ASCII ANTES de sustituir, y BORRAR los guiones
(no convertirlos en "_"):

    fun slugify(name: String): String {
        val folded = java.text.Normalizer.normalize(name, java.text.Normalizer.Form.NFD)
            .replace(Regex("\\p{Mn}+"), "")            // í -> i, ñ -> n
        return folded.lowercase()
            .replace("-", "").replace("'", "").replace("’", "")   // "Coat-Dress" -> "coatdress"
            .replace(Regex("[^a-z0-9]+"), "_")
            .trim('_')
    }

Y ÚSALO en saveImageToGithub (GitRepository.kt línea ~127), que hoy tiene:

    val slug = look.name.lowercase().replace(Regex("[^a-z0-9]"), "_").replace(Regex("_+"), "_")

Esa línea es la que creó carpetas reales como `look616_lencer_a` y `look709_suzie_wong_shangh_i`.
Reemplázala por `val slug = slugify(look.name)`.

En esa misma función, línea ~128: `String.format("%03d", look.number)` produce `look099_` /
`ele_099_standing.png` para el look 99. El canon es `look99_` / `ele_99_`. Usa
`look.number.toString()`.

---------------------------------------------------------------------
2. testParseMarkdown_CapturesNegativePrompt
3. testParseMarkdown_NoNegativePrompt_IsNull
---------------------------------------------------------------------
Exigen: campo `negativePrompt: String?` en LookEntity (data/local/Entities.kt) + su
migración de Room, y que parseMarkdown lo capture.

En el markdown, cada look termina con esta línea (INLINE, entre backticks simples):

    **Negative Prompt:** `ugly, bad hands, missing fingers`

Ese negativo es POR LOOK (aplica a las 7 poses), no por pose. Captúralo en el LookEntity actual.
Si el look no lo trae, `negativePrompt` debe quedar en null.

CUIDADO: esa línea mide >100 caracteres y contiene la palabra "prompt", así que hoy cae en la
rama de detección de poses (GitRepository.kt ~línea 486) y se descarta en silencio.
Detéctala ANTES de esa rama.

Este es el bug más caro del proyecto: la app NO GENERA imágenes — muestra el prompt, la usuaria
lo COPIA al portapapeles y lo pega en Gemini a mano. Como el negativo nunca se parseó, nunca se
copió, y por lo tanto NUNCA llegó al generador. Todas las imágenes se hicieron sin negativo.

---------------------------------------------------------------------
4. testParseMarkdown_UbicacionWithAndWithoutTilde
---------------------------------------------------------------------
Exige: parsear los campos `- **Clave:** valor` que van entre el heading del look y el primer
`###` (hoy se guardan crudos en `canonicalInfo` y nunca se leen).

    - **Ubicacion:** `05_Imagenes/ele/look787_gold_marquee_bodycon/`
    - **Categoria:** Nightclub
    - **Tags:** #glamrock #nightclub #gold #batchL781-L790 #V5poses

En el archivo conviven claves CON y SIN tilde (`**Ubicación:**` y `**Ubicacion:**`).
Normaliza la CLAVE quitando diacríticos antes de compararla, o no encontrarás la mitad.
Expón al menos `ubicacion` y la categoría en LookEntity.

Y ÚSALO: hoy la categoría se ADIVINA por keywords (GitRepository.kt ~373-403: "platform" ->
Stripper & Pole, "fetish" -> Domestic & Fetish). Es poco fiable — TODOS los looks llevan
plataforma y TODOS son fetish. Lee el campo `Categoria`; usa la inferencia solo como fallback.
Lista cerrada de 10 categorías válidas:
    Stripper · Corporate · Escort · Domestic · Pin-Up
    High-Fashion Editorial · Nightclub · Lencería · Bikini · Gym
Normalizar al leer: "Lenceria"->"Lencería", "Gym/Athleisure"->"Gym",
"HF Editorial"->"High-Fashion Editorial". "Mix" no es válida.

---------------------------------------------------------------------
5. testParseMarkdown_UnclosedFenceDoesNotContaminate
---------------------------------------------------------------------
Exige: que un bloque de código mal cerrado NO se derrame al look siguiente.

Hoy (GitRepository.kt ~462-482 y ~559-565) al ver una línea que empieza con ``` se pone
`isReadingCodeBlock = true` y se acumula hasta encontrar OTRA línea que empiece con ```.
Si el fence está mal formado, sigue tragando y mezcla prompts entre poses y entre looks.

Cierra el bloque de código también cuando, estando dentro de él, aparezca cualquiera de:
    - una línea `**<Pose>:**`
    - un heading `##` o `###`
    - el inicio de otro look
Lo que ocurra primero. Un bloque NUNCA cruza el límite de un look.

=====================================================================
ADEMÁS (no tiene test, pero es el bug de las carpetas duplicadas)
=====================================================================
ui/PromptFilterScreen.kt línea ~164:

    val existingImage = matchedImages.firstOrNull { matchesPose(selectedPose, it.poseName) }
    viewModel.uploadImageToGithub(..., existingPath = existingImage?.path)

Solo reutiliza la carpeta si YA existe una imagen de LA MISMA POSE. Para la primera imagen de
cada pose, `existingPath` es null y saveImageToGithub inventa la carpeta desde el slug del título.
Si esa carpeta no coincide con la que el look ya tiene, se crea una SEGUNDA carpeta.
Resultado real: 35 looks con dos carpetas y las poses repartidas entre ambas.

Resolución de carpeta destino, EN ESTE ORDEN:
    a) ¿existe alguna imagen de ESTE LOOK (cualquier pose)? -> usa su `parentFolder`
    b) ¿el markdown declara `Ubicacion`? -> usa esa carpeta
    c) si no -> `look<N>_<slugify(titulo)>`
Nunca crear un segundo directorio para un número de look que ya tiene uno.

Y en la UI: mostrar el negativo con su propio botón "Copiar negativo", y que el botón principal
ofrezca copiar POSITIVO + NEGATIVO juntos como:

    <prompt positivo>

    --no <negative prompt>

=====================================================================
ENTREGA
=====================================================================
- Los diffs de: GitRepository.kt, Entities.kt (+ migración Room), PromptFilterScreen.kt,
  MainViewModel.kt.
- La salida de `./gradlew test` con los 5 tests en VERDE.
- NO agregues tests nuevos. Implementa.
```
