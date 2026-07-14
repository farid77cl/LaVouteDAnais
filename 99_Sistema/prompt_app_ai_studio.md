# 📱 Prompt para Google AI Studio — App LV-App (`farid77cl/LV-App`)

> **Uso:** copiar el bloque de abajo y pegarlo en AI Studio.
> **Base:** lectura del código real (Kotlin/Compose) el 14/07/2026 — no inferencia.
> **Repo app:** https://github.com/farid77cl/LV-App · **Repo contenido:** `farid77cl/LaVouteDAnais`
> **Contrato del `.md`:** `.agent/rules/11-contrato-galeria.md` · **Linter:** `99_Sistema/scripts/visual/lint_galeria.py`

## Cómo funciona la app hoy (verificado en el código)

La app **no genera imágenes**. `GeminiApiService` solo expone `generateContent` (texto, `gemini-1.5-pro-latest`). El flujo real es:

1. `GitRepository.parseMarkdown()` lee `00_Ele/galeria_outfits.md` → `LookEntity` + `PromptEntity`.
2. `PromptFilterScreen` muestra el prompt de la pose y la Ama lo **copia** (`ClipboardManager`).
3. La Ama lo pega en Gemini (app aparte), genera la imagen y la guarda en el teléfono.
4. Vuelve a la app, la elige con el picker (`GetContent()`), y `saveImageToGithub()` la sube.

**Consecuencia crítica:** lo que no esté en el texto copiado, **no llega al generador**.

## Los 7 bugs reales, con ubicación

| # | Dónde | Qué pasa |
|---|-------|----------|
| **1** | `parseMarkdown()` + `Entities.kt:22` | **El `Negative Prompt` NUNCA se lee.** `PromptEntity` solo tiene `promptText`; la palabra `negative` no existe en el código. El negativo nunca se copia → **todas las imágenes se generaron sin él.** |
| **2** | `GitRepository.kt:127` | `replace(Regex("[^a-z0-9]"), "_")` sin plegar acentos → `"Lencería"` = **`lencer_a`**. |
| **3** | `PromptFilterScreen.kt:164` | `existingPath` solo se reutiliza si ya hay imagen de **la misma pose** → la 1ª pose inventa carpeta nueva → **duplicados**. |
| **4** | `parseMarkdown()` | El campo **`Ubicacion` nunca se parsea**. Va crudo dentro de `canonicalInfo` y se ignora. |
| **5** | `GitRepository.kt:128` | `String.format("%03d")` → el look 99 sería `look099_` / `ele_099_`. El canon es `look99_` / `ele_99_`. |
| **6** | `GitRepository.kt:373-387` | La categoría **se adivina por keywords** (13 categorías propias) en vez de leer el campo `Categoría`. `"platform"` → Stripper, y *todos* los looks llevan platform. |
| **7** | `GitRepository.kt:462-482` | Un fence mal formado deja `isReadingCodeBlock=true` y **se traga líneas hasta el próximo backtick** → prompts mezclados entre poses y looks. |

---

```
Estás corrigiendo la app Android LV-App (Kotlin + Jetpack Compose + Room + Retrofit).
Su repo es farid77cl/LV-App. Lee y escribe contra el repo de contenido farid77cl/LaVouteDAnais.

La app NO genera imágenes: parsea prompts desde `00_Ele/galeria_outfits.md`, los muestra para
copiar al portapapeles (la usuaria los pega en Gemini a mano), y luego sube el PNG resultante
a GitHub. Por lo tanto: LO QUE NO SE COPIA, NO LLEGA AL GENERADOR.

Corrige los siguientes 7 bugs. Están localizados. No refactorices de más.

=====================================================================
BUG 1 (CRÍTICO) — EL BLOQUE NEGATIVO NUNCA SE LEE NI SE COPIA
=====================================================================
Archivos: data/repository/GitRepository.kt (parseMarkdown), data/local/Entities.kt,
          ui/PromptFilterScreen.kt

Hoy `PromptEntity` solo tiene `promptText`. La palabra "negative" no existe en el código.
En el markdown, cada look termina con una línea así (INLINE, entre backticks simples):

    **Negative Prompt:** `gothic, vampire, flat shoes, gloves, chunky heel, ...`

Ese negativo aplica a LAS 7 POSES del look. Como nunca se captura, la usuaria nunca lo pega
en Gemini y TODAS las imágenes se han generado sin negativo. Ese es el bug más caro del proyecto.

Qué hacer:
 1.1 Añadir `negativePrompt: String?` a `LookEntity` (es por look, no por pose).
     Migración de Room correspondiente.
 1.2 En `parseMarkdown()`, detectar la línea que empieza con `**Negative Prompt:**` y capturar
     el contenido entre los backticks simples. Guardarlo en el LookEntity actual.
     OJO: esa línea mide >100 caracteres y contiene la palabra "prompt", así que hoy entra en la
     rama de detección de poses (línea ~486) y se descarta en silencio. Detéctala ANTES de esa rama.
 1.3 En `PromptFilterScreen`, mostrar el negativo y darle su propio botón "Copiar negativo".
     Además, el botón de copiar principal debe ofrecer copiar POSITIVO + NEGATIVO juntos,
     en el formato que espera el generador:

         <prompt positivo>

         --no <negative prompt>

 1.4 Si un look NO tiene bloque `Negative Prompt`, márcalo visualmente en la UI (badge rojo
     "SIN NEGATIVO") y no lo ofrezcas como listo para generar. Hoy hay ~300 looks así.

=====================================================================
BUG 2 — EL SLUG DESTRUYE LOS ACENTOS
=====================================================================
Archivo: data/repository/GitRepository.kt, línea ~127 (saveImageToGithub)

Código actual:
    val slug = look.name.lowercase().replace(Regex("[^a-z0-9]"), "_").replace(Regex("_+"), "_")

La "í" de "Lencería" no está en [a-z0-9], así que se convierte en "_" y produce la carpeta
`look616_lencer_a`. Lo mismo con `look709_suzie_wong_shangh_i` y `look702_..._l_quido`.
Son carpetas reales que existen en el repo por este bug.

Reemplázalo por un slugify que PLIEGUE los acentos a ASCII antes de sustituir:

    fun slugify(name: String): String {
        val folded = java.text.Normalizer.normalize(name, java.text.Normalizer.Form.NFD)
            .replace(Regex("\\p{Mn}+"), "")      // quita los diacríticos: í -> i, ñ -> n
        return folded.lowercase()
            .replace("-", "").replace("'", "").replace("’", "")   // "Coat-Dress" -> "coatdress"
            .replace(Regex("[^a-z0-9]+"), "_")
            .trim('_')
    }

Casos de control (deben dar EXACTAMENTE esto):
    "Lencería Burgundy Boots"   -> lenceria_burgundy_boots
    "Shanghai Qipao Líquido"    -> shanghai_qipao_liquido
    "Jade Coat-Dress Boardroom" -> jade_coatdress_boardroom
    "Cherry Polka Dot Pin-Up"   -> cherry_polka_dot_pinup

=====================================================================
BUG 3 — CARPETAS DUPLICADAS POR LOOK
=====================================================================
Archivos: ui/PromptFilterScreen.kt línea ~164, data/repository/GitRepository.kt línea ~129

Código actual:
    val existingImage = matchedImages.firstOrNull { matchesPose(selectedPose, it.poseName) }
    viewModel.uploadImageToGithub(..., existingPath = existingImage?.path)

Solo reutiliza la ruta si YA existe una imagen de LA MISMA POSE. Para la primera imagen de cada
pose, `existingPath` es null y `saveImageToGithub` inventa la carpeta desde el slug del título.
Si esa carpeta no coincide con la que ya tiene el look, se crea una SEGUNDA carpeta.
Resultado real: 35 looks con dos carpetas y las poses repartidas entre ambas.

Qué hacer — resolución de carpeta destino, EN ESTE ORDEN:
    a) ¿Existe alguna imagen de ESTE LOOK (cualquier pose) en la BD?
       -> usa SU `parentFolder`.  (esto solo, ya mata el bug)
    b) Si no, ¿el markdown declara `Ubicacion` para el look? -> usa esa carpeta (ver BUG 4).
    c) Si no, recién ahí construye `look<N>_<slugify(titulo)>`.
Nunca crear un segundo directorio para un número de look que ya tiene uno.

=====================================================================
BUG 4 — EL CAMPO `Ubicacion` SE IGNORA
=====================================================================
Archivo: data/repository/GitRepository.kt (parseMarkdown)

Entre el heading del look y el primer `###` viene la metadata, que hoy se guarda cruda en
`canonicalInfo` y nunca se parsea:

    - **Ubicacion:** `05_Imagenes/ele/look787_gold_marquee_bodycon/`
    - **Tags:** #glamrock #nightclub #gold #batchL781-L790 #V5poses
    - **Categoria:** Nightclub

Parsea esas líneas como campos `- **Clave:** valor` y expón al menos `Ubicacion`, `Categoria`
y `Tags` en `LookEntity`.
IMPORTANTE: en el archivo conviven claves con y sin tilde (`**Ubicación:**` y `**Ubicacion:**`).
Normaliza la CLAVE quitando diacríticos antes de comparar, o no encontrarás la mitad.

=====================================================================
BUG 5 — PADDING DE 3 DÍGITOS
=====================================================================
Archivo: data/repository/GitRepository.kt, línea ~128

    val lookNumStr = String.format("%03d", look.number)

Para el look 99 produce `look099_...` y `ele_099_standing.png`. El canon del repo es `look99_`
y `ele_99_standing.png`, sin padding. Usa `look.number.toString()`.
(Hoy no muerde porque la app opera sobre looks >= 291, pero rompe en cuanto toque uno antiguo.)

=====================================================================
BUG 6 — LA CATEGORÍA SE ADIVINA POR KEYWORDS
=====================================================================
Archivo: data/repository/GitRepository.kt, líneas ~373-403

`outfitType` se infiere buscando substrings en el título ("platform" -> Stripper & Pole,
"fetish" -> Domestic & Fetish, "siren" -> Bikini & Playa, "vow" -> Bikini...). Es poco fiable:
TODOS los looks llevan plataforma y TODOS son fetish, así que la categoría sale mal seguido.

El markdown YA trae la categoría, en el heading y en el campo `Categoria`:

    ## Look 787: Gold Marquee Bodycon (13/07/2026 · batch ... · Nightclub · Rock Marquee Alley ... )

Qué hacer:
 6.1 Leer la categoría del campo `Categoria` (BUG 4); si falta, tomarla de los segmentos
     separados por "·" del heading.
 6.2 Lista CERRADA de 10 valores válidos:
        Stripper · Corporate · Escort · Domestic · Pin-Up
        High-Fashion Editorial · Nightclub · Lencería · Bikini · Gym
     Normalizar al leer: "Lenceria" -> "Lencería" ; "Gym/Athleisure" -> "Gym" ;
     "HF Editorial" -> "High-Fashion Editorial". "Mix" no es válida -> "Sin categoría".
 6.3 Usar la inferencia por keywords SOLO como último recurso, y marcarla como "inferida".

=====================================================================
BUG 7 — UN FENCE ROTO SE TRAGA EL LOOK SIGUIENTE
=====================================================================
Archivo: data/repository/GitRepository.kt, líneas ~462-482 y ~559-565

Al ver una línea que empieza con ``` se pone `isReadingCodeBlock = true` y se acumulan líneas
hasta encontrar OTRA línea que empiece con ```. Si el markdown trae un fence mal formado
(apertura y cierre en la misma línea, o sin cerrar), el parser sigue tragando y mezcla prompts
entre poses e incluso entre looks distintos.

Qué hacer: cerrar el bloque de código también cuando aparezca, estando dentro de él, cualquiera de:
    - una línea `**<Pose>:**`
    - un heading `##` o `###`
    - el inicio de otro look
Lo que ocurra primero. Nunca dejes que un bloque cruce el límite de un look.

=====================================================================
NOMBRES CANÓNICOS (esto YA lo hace bien — no lo rompas)
=====================================================================
- Poses al subir: standing · back_view · seated · side_profile · ditzy · pov · odalisque
  (`formattedPose` en saveImageToGithub ya es correcto)
- Archivo: ele_<N>_<pose>.png
- Se aceptan sufijos de timestamp (ele_313_pov_1783817471712.png): misma pose, generada por API.
  Al detectar la pose de un archivo, trátalos como equivalentes.
- Nunca sobrescribir un PNG en silencio: si el nombre existe y es una imagen distinta, sube
  como ele_<N>_<pose>__v2.png.
- La app NO debe escribir galeria_outfits.md. Ese archivo lo mantienen los scripts del repo.

=====================================================================
QUÉ QUIERO DE VUELTA
=====================================================================
1. Los diffs de: GitRepository.kt, Entities.kt, PromptFilterScreen.kt, MainViewModel.kt
   (+ la migración de Room por el campo nuevo).
2. Tests unitarios en app/src/test/java/com/example/ParserTest.kt que cubran:
   - slugify("Lencería Burgundy Boots") == "lenceria_burgundy_boots"
   - slugify("Jade Coat-Dress Boardroom") == "jade_coatdress_boardroom"
   - parseMarkdown captura el Negative Prompt de un look y lo asocia a las 7 poses.
   - un look SIN Negative Prompt queda marcado como incompleto.
   - clave "**Ubicación:**" (con tilde) y "**Ubicacion:**" (sin tilde) resuelven igual.
   - un look con un fence mal formado NO contamina el look siguiente.
   - subir la 1ª pose de un look que ya tiene carpeta REUTILIZA esa carpeta.
```
