# 📋 REGLA 11 — CONTRATO DE LAS GALERÍAS (Ele · Miss Doll · Anaïs)

> **Para qué existe:** `00_Ele/galeria_outfits.md` lo leen **tres** actores distintos — la **app Android** de la Ama (genera las imágenes y las sube), el **bot paralelo** (mantiene READMEs/galerías) y el **agente** (diseña los looks). Cuando cada uno interpreta el archivo a su manera, el resultado no es un desacuerdo de estilo: son **carpetas duplicadas, contadores que mienten y cuota API quemada regenerando imágenes que ya existían**.
>
> Este archivo es el **contrato único**. Lo que no esté aquí, no es formato válido.
>
> **Verificable:** `python 99_Sistema/scripts/visual/lint_galeria.py` — obligatorio antes de cerrar cualquier batch.

---

## 1. 🔑 LA REGLA DE ORO — UN SOLO SLUG

Cada look tiene **UN** slug canónico. Ese mismo string, **carácter por carácter**, debe aparecer en los tres lugares:

| Dónde | Forma |
|-------|-------|
| **Carpeta en disco** | `05_Imagenes/ele/look<N>_<slug>/` |
| **Campo `Ubicacion`** | `- **Ubicacion:** \`05_Imagenes/ele/look<N>_<slug>/\`` |
| **Links de la tabla 📸** | `../../05_Imagenes/ele/look<N>_<slug>/ele_<N>_<pose>.png` |

Si los tres no coinciden, el look está roto **aunque se vea bien**. Fue la causa raíz de los 35 duplicados del 14/07 (`look764_jade_coat_dress_boardroom` declarado vs `look764_jade_coatdress_boardroom` real).

---

## 2. 🏷️ CÓMO SE CONSTRUYE EL SLUG (algoritmo exacto)

**La app deriva el slug del TÍTULO del heading.** No del campo `Ubicacion`, no de la categoría. Del título. Por eso el título no es decorativo: **es la clave primaria.**

Algoritmo, en orden:

1. Tomar el título (lo que va entre `## Look N:` y el paréntesis).
2. Pasar a **minúsculas**.
3. **Plegar acentos a ASCII:** `á→a  é→e  í→i  ó→o  ú→u  ü→u  ñ→n`.
4. **Borrar** guiones y apóstrofes (no se convierten en `_`): `Coat-Dress → coatdress`, `Pin-Up → pinup`.
5. Todo lo que no sea `[a-z0-9]` → `_`; colapsar `__` repetidos; quitar `_` de los bordes.
6. Prefijar `look<N>_`.

```
"Jade Coat-Dress Boardroom"   → look764_jade_coatdress_boardroom
"Shanghai Qipao Líquido"      → look702_shanghai_qipao_liquido
"Cherry Polka Dot Pin-Up"     → look610_cherry_polka_dot_pinup
```

### ⛔ Prohibido en el slug y en el nombre de carpeta
- **Acentos y cualquier carácter no-ASCII.** Un `í` sin plegar produjo `look616_lencer_a` y `look709_suzie_wong_shangh_i` — carpetas basura que git trackea a medias.
- **Prefijo de categoría** (`lenceria_`, `gym_`, `stripper_`). La categoría vive en su campo y en los tags, **no en el slug**.

---

## 3. 📝 EL TÍTULO DEBE SER DESCRIPTIVO

> **El título NUNCA es la categoría pelada.**

`## Look 616: Lencería` es un título **inválido**: su slug sería `look616_lenceria`, que colisiona con las otras ~48 lencerías. De ahí salieron los duplicados L613-L620.

**Fórmula:** `Color + Prenda/Silueta + Estilo o Contexto`.

| ❌ Inválido | ✅ Válido |
|------------|-----------|
| `Nightclub` | `Nightclub Hot Pants` |
| `Lencería` | `Lencería Burgundy Boots` |
| `Corporate` | `Corporate Siren Boots` |
| `Bikini` | `White Vinyl Pool Bikini` |

---

## 4. 🧱 ESTRUCTURA DEL BLOQUE (orden obligatorio)

El orden **importa**: el parser de la app arma su `canonicalInfo` con lo que hay **entre el heading y el primer `###`**. Si `### 📸 Imágenes` aparece antes que `Ubicacion`/`Tags`, la app se queda **muda** (le pasó a 60 looks, L711-L770).

````markdown
## Look <N>: <Título Descriptivo> (<fecha> · batch L<X>-L<Y> "<Tema>" · <Categoría> · <Subcategoría> · <Modo cromático>)
- **Ubicacion:** `05_Imagenes/ele/look<N>_<slug>/`
- **Tags:** #<categoria> #<material> #<tema> #batchL<X>-L<Y> #V5poses

### 📸 Imágenes (<n>/7 — Materializado | Materializado parcial (app/Gemini))

| Standing | Back View | Seated | Side Profile | Ditzy (plano 3/4) | POV (single hand) | Odalisque |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| [📸 View](../../05_Imagenes/ele/look<N>_<slug>/ele_<N>_standing.png) | … | ⏳ Pendiente |

**Standing:**

```
<prompt completo en inglés>
```

**Back View:**

```
<prompt>
```

… (las 7 poses, en orden)

**Negative Prompt:** `<bloque negativo completo>`
````

**Reglas de fence:** el ` ``` ` de apertura y el de cierre van **cada uno en su propia línea**. Un fence en una sola línea (` ```texto``` `) hace que el parser de la app siga tragando líneas hasta el próximo backtick y **mezcle prompts entre poses y entre looks distintos** (pasó en 1.167 prompts, L300-L731).

---

## 5. 🔤 NOMBRES DE CAMPO — ASCII, SIN TILDE

| ✅ Usar | ❌ Nunca |
|---------|----------|
| `- **Ubicacion:**` | `- **Ubicación:**` |
| `- **Categoria:**` | `- **Categoría:**` |
| `- **Subcategoria:**` | `- **Subcategoría:**` |
| `- **Ambientacion:**` | `- **Ambientación:**` |

La tilde en la **clave** deja ciego al parser: 32 looks no resolvían su ubicación por eso. La tilde en el **valor** (`Lencería`, el título) es correcta y se conserva — solo la clave es ASCII.

---

## 6. 🗂️ CATEGORÍA — LISTA CERRADA DE 10

Se escribe **exactamente así**, en el heading y en el campo. Nada de sinónimos.

```
Stripper · Corporate · Escort · Domestic · Pin-Up
High-Fashion Editorial · Nightclub · Lencería · Bikini · Gym
Alfombra Roja / Gala
```

> 🩹 **17/08/2026 — la lista estaba vieja, no los looks.** El linter marcaba 36 hallazgos C6 y al mirar la dirección del error resultó que **el equivocado era el contrato**: «Alfombra Roja / Gala» la usa el batch 261-270 desde el 25/05 con `Categoria` y `Subcategoria` propias, y «gala» es material declarado en el canon. Entra como **11ª categoría**, con sus 3 grafías (`Alfombra Roja / Gala`, `Alfombra Roja`, `Gala`) unificadas en una.
>
> Aparte: **«Mix» no es una categoría de vestuario** — es la meta cromática, y se había colado en el campo `Categoria` de **18 looks (L201-L220)** cuya categoría real estaba escrita en `Subcategoria` (Corporate, Escort, Pin-Up, Stripper, Domestic, Nightclub, High-Fashion). Corregidos **leyendo el campo, no adivinando**. `Professional Stripper` → `Stripper` y `High-Fashion` → `High-Fashion Editorial`.

**Normalizaciones obligatorias** (variantes reales encontradas en el archivo):

| Encontrado | Se escribe |
|-----------|-----------|
| `Lenceria` (sin tilde) | `Lencería` |
| `Gym/Athleisure` | `Gym` |
| `HF Editorial` | `High-Fashion Editorial` |
| `Mix` | ❌ no es categoría — asignar la real |

La **Subcategoría** es libre y descriptiva (`Office Siren (Thigh-High Boots)`), y va después de la categoría en el heading.

---

## 7. 🏷️ TAGS — ORDEN FIJO

```
#<categoria> #<material> #<tema/color> #batchL<X>-L<Y> #V5poses
```

- Todo en **minúscula, sin tilde, sin espacios** (`#lenceria`, no `#Lencería`).
- **Categoría primero** — es lo que la app usa para filtrar.
- Material: `#vinyl #latex #pvc #wetlook #chrome #mesh #satin …`
- Cierran siempre `#batchL<X>-L<Y>` y `#V5poses`.

---

## 8. 🖼️ NOMBRES DE IMAGEN (CONTRATO LV-APP MULTI-PERSONAJE)

> **Directiva Ama (15/08/2026):** Todas las imágenes en disco, tablas markdown y subidas desde la app DEBEN seguir el contrato de nombrado estricto de LV-App (`CharacterProfile.kt` y `GitRepository.kt`). No se permiten slugs de otros personajes (ej. `ditzy` en Miss Doll o Anaïs) ni prefijos inconsistentes.

### 📐 Matriz Canónica de Nombrado por Personaje

| Personaje | Carpeta de Look | Formato de Archivo | Slot 5 Específico | Las 7 Poses Canónicas |
|---|---|---|---|---|
| **Ele** | `05_Imagenes/ele/look<N>_<slug>/` | `ele_<N>_<pose>.png` | `ditzy` | `standing`, `back_view`, `seated`, `side_profile`, `ditzy`, `pov`, `odalisque` |
| **Miss Doll** | `05_Imagenes/miss_doll/look<N>_<slug>/` | `miss_doll_<N>_<pose>.png` | `glacial_command` | `standing`, `back_view`, `seated`, `side_profile`, `glacial_command`, `pov`, `odalisque` |
| **Anaïs (Estándar)** | `05_Imagenes/anais/look<N>_<slug>/` | `anais_<N>_<pose>.png` | `sovereign_gaze` | `standing`, `back_view`, `seated`, `side_profile`, `sovereign_gaze`, `pov`, `odalisque` |
| **Anaïs (Boudoir / Lencería)** | `05_Imagenes/anais/look<N>_<slug>/` | `anais_L<NN>_<pose>.png` *(ej. `anais_L08_standing.png`)* | `sovereign_gaze` | `standing`, `back_view`, `seated`, `side_profile`, `sovereign_gaze`, `pov`, `odalisque` |

### ⛔ Prohibiciones Absolutas de Nombrado
1. **PROHIBIDO usar `ditzy` en Miss Doll o Anaïs:** El slot 5 de Miss Doll es **`glacial_command`**; el de Anaïs es **`sovereign_gaze`**. `ditzy` es exclusivo de Ele.
2. **PROHIBIDO mezclar prefijos en un mismo look:** Si el look es Boudoir de Anaïs (`look.isBoudoir = true`), todas sus poses llevan el prefijo `anais_L<NN>_` (con padding de 2 dígitos, ej. `anais_L02_`, `anais_L08_`, `anais_L09_`, `anais_L10_`). Si es estándar, llevan `anais_<N>_`.
3. **PROHIBIDO duplicar versiones antiguas en la misma carpeta:** Si se regenera una pose desde la app con el prefijo nuevo, la versión obsoleta previa debe eliminarse (`git rm`) para no duplicar conteos ni corromper el visor de la app.
4. **Sufijo timestamp / v2:** La app o generación por API puede incluir timestamp (`ele_313_pov_1783817471712.png`) o versión (`__v2`). El extractor de pose de la app los procesa correctamente.
5. **Una sola carpeta por look:** Nunca dos carpetas para el mismo número de look. Todo en minúsculas y sin acentos.

---

## 9. ✅ CHECKLIST ANTES DE CERRAR UN BATCH

```bash
python 99_Sistema/scripts/visual/outfit.py lint              # 🔴 TODOS los personajes — parsea como la app
python 99_Sistema/scripts/visual/outfit.py adn               # el BLOQUE A no divergió en ninguna copia
python 99_Sistema/scripts/visual/outfit.py auditar --solo-sin-imagen   # canon sobre lo que la app todavía va a generar
python 99_Sistema/scripts/visual/lint_galeria.py             # el contrato (Ele)
python 99_Sistema/scripts/visual/sync_imagenes_subidas.py    # tracker + rutas
python 99_Sistema/scripts/visual/update_galleries.py         # READMEs + galería
python 99_Sistema/scripts/visual/garment_canon.py            # canon de vestuario
python 99_Sistema/scripts/visual/footwear_canon.py           # canon de calzado
```

Ningún batch se commitea con el linter en rojo.

> 🔴 **`lint_prompts_personaje.py` es el primero de la lista y aplica a Ele, Miss Doll, Anaïs y a cualquier personaje futuro.** No lee la galería como la leería un humano: la **parsea con el mismo algoritmo que LV-App** y reporta lo que la app va a ingerir de verdad. Nació porque las 3 secciones siguientes de este archivo se pueden cumplir a ojo y aun así entregar prompts inservibles — pasó el 11/08/2026 con los 98 de Miss Doll.

---

## 9quater. 🧱 BLOQUE CENTINELA AL CIERRE DE CADA GALERÍA (18/08/2026)

Toda galería termina con un **bloque centinela** — un encabezado que el parser NO cuenta como look (no lleva la palabra clave seguida de número) y un párrafo que explica para qué está. **Ningún look puede ser el último bloque del archivo.**

**Por qué:** la Ama reportó ver **24 outfits de Anaïs teniendo 25**. Medido repo-side, el Look 25 está intacto: encabezado sano (verificado byte a byte, sin caracteres invisibles), `Ubicacion`, `Tags`, sus 7 prompts expandidos, `Negative Prompt` legible, numeración 1-25 sin duplicados ni huecos, y las 25 carpetas de imágenes existen. Parseado con el algoritmo de la app da **25**. La **única** diferencia estructural entre el Look 25 y los 24 que sí se ven era ser el último bloque, sin nada que cerrara su ficha.

**Cuando entra un look nuevo va ANTES del centinela, nunca después.**

> ⚠️ **Esto es una hipótesis con fundamento, no una causa confirmada** — la confirmación vive en el código de LV-App, que es otro repo. Y hay evidencia en contra que no se esconde: el **Look 801 de Ele** también es el último de su galería y la app **sí** lo ingirió (tiene sus 7 imágenes subidas). Si tras este cambio la app sigue mostrando 24, la causa es otra y el diagnóstico se retoma con el código de la app en mano. El centinela es barato y no rompe nada — el linter sigue leyendo 602/25/25 con él puesto — pero no se declara resuelto hasta que la Ama vea 25.

---

## 9ter. 🧩 EL CONTRATO ES MULTI-PERSONAJE (12/08/2026)

Este archivo nació para `00_Ele/galeria_outfits.md`, pero **el parser de la app es uno solo**: las mismas reglas rigen `GALERIA_OUTFITS_MISS_DOLL.md`, `galeria_looks_anais.md` y la galería de cualquier personaje que se agregue. Las diferencias por personaje (nombre del slot 5, prefijo de archivo, carpeta) viven en su **perfil visual §10** y en `99_Sistema/scripts/visual/anclas_universales.json`, no aquí.

Tres cláusulas que **rompen en silencio** y que no estaban escritas hasta hoy:

| Cláusula | Qué pasa si falta |
|---|---|
| **El prompt va FINAL y EXPANDIDO** dentro del fence — nunca `[BLOQUE A]`, `[ADN]` ni ningún placeholder | La app manda el corchete **literal** al generador: imagen sin cara, sin cuerpo, sin ropa ni escenario. 98 prompts de Miss Doll (11/08) y 98 de Anaïs con `[ADN]` (11/08) |
| **La etiqueta del negativo es literal:** solo `**Negative Prompt:** \`…\`` se ingiere | Cualquier otra redacción es invisible → el look entero se genera **sin negativo**. Los 14 looks de Miss Doll y los 14 de Anaïs estaban así |
| **La pose se numera** en su encabezado (`### 1. Standing…` / `**1. Standing:**`) | El matcher de texto no alcanza `Sovereign Gaze` ni `Glacial Command`; sin el número, dos slots colapsan en uno y el `REPLACE` de la `PrimaryKey` borra el otro **en silencio** |

**El orden de la metadata también es multi-personaje:** `Ubicacion` y `Tags` van **antes** del primer `###` del look, siempre. Sin eso la app no resuelve ni la carpeta ni la categoría.

---

## 9quinquies. 📐 PARIDAD ENTRE LAS TRES GALERÍAS — MEDIDA, NO DECLARADA (04/09/2026)

> **Ama:** *"en algun momento te pedi que el outfit engine fuera modular y que las 3 muñecas funcionaran igual en el proceso de punta a cabo… realmente se cumplio?"*
>
> **No se cumplía, y el §9ter de arriba lo declara desde el 12/08/2026.** Ahí está la lección: **una regla escrita que nadie mide no rige.** El chequeo que decía `MODULARIDAD: LIMPIA` verificaba tres cosas del *código* (cero nombres de personaje en la lógica, campos propios declarados, sub-poses únicas) y **ninguna del proceso** — así que el número decía verde mientras el pipeline estaba torcido.

### Lo que se midió el 04/09/2026 y estaba roto

| Defecto | Medida | Estado |
|---|---|---|
| Looks **después** del bloque centinela (o sea invisibles para LV-App) | Ele **16** · Miss Doll 0 · Anaïs **45** | ✅ los tres en 0 |
| Encabezado de pose **sin número** (§9ter: colapsa dos slots y el `REPLACE` borra uno en silencio) | Ele **630 poses** en 90 looks (L711+) · Miss Doll 0 · Anaïs 0 | ✅ los tres en 0 |
| Looks legibles por el chequeo 12 (rotación de arquitectura de prenda) | Ele **0/618** · Miss Doll 59/75 · Anaïs **5/75** | ✅ 528/618 · 75/75 · 75/75 |
| `rotacion_prenda` cableada en `anclas_universales.json` | **solo miss_doll** | ✅ las tres |
| Scripts de batch escritos a mano vivos | 1 (`gen_lenceria_anais_61_65.py`) | ✅ 0 |
| Copias literales del BLOQUE A que divergen | 2 preexistentes + 35 en la galería de Miss Doll | ✅ `outfit.py adn` LIMPIO |
| `auditar_galeria.py` | ruta absoluta rota, script muerto | ✅ corre |

### Lo que DEBE ser idéntico en las tres

1. **El bloque centinela es el último bloque del archivo.** Ningún look después. Se mide contando encabezados de look posteriores a él — meta **0**.
2. **Todo encabezado de pose lleva su número** (`### N. Nombre` o `**N. Nombre:**` — las dos formas son válidas, ver §9ter).
3. **El outfit se declara en un campo legible por máquina**, fuera de los prompts. Sin él el chequeo 12 no puede clasificar el look y la ventana anti-repetición de silueta no se dispara.
4. **`rotacion_prenda` existe para el personaje** en `anclas_universales.json`, con su `desde_look` propio (retrofit-al-tocar: nunca juzga retroactivamente lo ya materializado).
5. **Cero copias literales del BLOQUE A.** Se apunta al perfil; no se copia. Verificable con `outfit.py adn`.
6. **Un batch es un JSON en `batches/`.** Cero scripts `gen_*.py`.

### Lo que PUEDE diferir, y por qué (medido, no asumido)

| Diferencia | Personaje | Razón real |
|---|---|---|
| **Forma del campo de outfit:** bloque `**BLOQUE B …:**` + fence ```` ```text ```` vs. campo de una línea `- **Outfit (BLOQUE B):** \`…\`` | fence en Miss Doll y Anaïs · **una línea en Ele** | **No es desprolijidad: es una restricción del parser.** Medido el 04/09: al insertarle a Ele el bloque con fence, LV-App pasó a ingerir **8 prompts donde hay 7** y el slot `Standing` recibió dos → `PrimaryKey REPLACE`, una toma perdida en silencio. Su galería usa fences desnudos para los prompts y no tolera uno más. Los 27 looks de Ele que ya usaban el campo de una línea tenían razón. |
| Nombre del campo de outfit (`Outfit`, `Outfit canónico (7 campos)`, `Outfit (BLOQUE B)`) | Ele, por era | Histórico. El lector acepta cualquier sufijo tras `Outfit`; no se migran 618 looks materializados. |
| Emoji del encabezado, nombre del slot 5, prefijo de archivo y de carpeta | los tres | Ya vivían en el perfil §10 y en `anclas_universales.json`. Es variación **declarada**, no deriva. |

### Deuda que queda declarada, no tapada

**90 looks de Ele (L711–L800) no declaran outfit en ningún campo** — su ropa vive solo dentro de los prompts, de donde no se puede clasificar sin que el clasificador se lea a sí mismo (las anclas nombran `bikini`, `dress` y `skirt`). Están **materializados 7/7** y por debajo de su `desde_look` (818), así que la ventana no los necesita: la del próximo look de Ele mira L815–L817, que sí se leen. **Lo que cambió es que ahora se cuentan a la vista** — el resumen del chequeo 12 imprime `leidos N/M` y marca `⚠ N SIN LEER`. Antes imprimía solo `N`, así que un **0 de 618** se leía igual que un "no aplica" y pasó meses sin que nadie lo notara.

**Verificable, y es la prueba de esta sección:**

```bash
python 99_Sistema/scripts/visual/outfit.py lint ele        # y miss_doll, y anais
python 99_Sistema/scripts/visual/outfit.py adn             # meta: LIMPIO
python 99_Sistema/scripts/visual/outfit.py modularidad
```

---

## 9bis. 🚨 QUÉ ARCHIVOS LEE LA APP (contrato de NOMBRE — 11/08/2026)

**LV-App no tiene una lista de archivos.** Baja el árbol completo de GitHub y se queda con **todo `.md` cuya ruta en minúsculas CONTENGA** una de estas subcadenas (`CharacterProfile.kt` + `GitRepository.kt:301-310` del repo `farid77cl/LV-App`):

| Personaje | Subcadenas gatillo |
|---|---|
| Ele | `galeria_outfits` |
| Miss Doll | `galeria_outfits_miss_doll` · `outfits_miss_doll` |
| Anaïs | `galeria_looks_anais` · `looks_anais` |
| — | ruta que empiece por `_batch_` o contenga `/_batch_` |

**Descarta** lo que contenga: `galeria_index` · `report` · `.bkp` · `03_literatura` · `canon_visual` · `ficha_` · `sistema_poses` · `banco_prompts`.

### 🔴 La consecuencia: el nombre del archivo ES el interruptor

La `@PrimaryKey` de la tabla `looks` es **el número del look pelado** (con offset por personaje: Miss Doll `+20000`, Anaïs `+30000`, Boudoir `+40000`) y el insert es `OnConflictStrategy.REPLACE`. Los archivos se parsean en **orden alfabético del árbol**. Por lo tanto:

> **Dos archivos que caigan en el filtro y compartan número de look ⇒ gana el último alfabéticamente. En silencio.**

**Cicatriz del 11/08/2026:** al resetear la numeración de Miss Doll y Anaïs a Look 01 se archivaron las galerías viejas con nombres que **seguían cayendo en el filtro** (`galeria_looks_anais_archivo_legacy.md`, `GALERIA_OUTFITS_MISS_DOLL_ARCHIVO_LEGACY.md`, `OUTFITS_MISS_DOLL.md`). Resultado: el legacy **sobreescribía los 14 looks nuevos** de cada personaje y la Ama veía los outfits antiguos en la app. No era caché — era el nombre del archivo. Los 4 `_batch_L651_L690.md` de la raíz hacían lo mismo con Ele: prompts **anteriores al fix anti-collage** (0 anclas `a single continuous photograph` contra 280 en la galería viva) pisando el rango refrescado.

### 📏 Reglas duras al archivar

1. **Archivar ≠ mover de carpeta.** El filtro mira la ruta completa: meter el archivo en `archivo/` no lo saca. **Hay que renombrarlo** para que no contenga ninguna subcadena gatillo.
2. Nombre canónico de archivado: `ARCHIVO_LEGACY_<PERSONAJE>_<CANON>_<TIPO>.md` (ej. `ARCHIVO_LEGACY_MISS_DOLL_V35_GALERIA.md`, `archivo_legacy_anais_v1.md`).
3. **Las imágenes van con la misma lógica.** El scanner ingiere toda imagen cuya **carpeta madre inmediata** empiece por `look` (`GitRepository.kt:761`) — mirar solo el padre inmediato significa que un subdirectorio `_ARCHIVO_LEGACY/` **no basta**. Al archivar, prefijar cada carpeta: `look18_x/` → `_ARCHIVO_LEGACY_V1/legacy_look18_x/`.
4. **Verificación obligatoria tras archivar** (debe devolver solo las galerías vivas + los archivos de Ele intencionales):

```powershell
git ls-files | Where-Object { $_ -match '\.md$' } | Where-Object { $l=$_.ToLower();
  ($l -match 'galeria_outfits' -or $l -match 'outfits_miss_doll' -or $l -match 'galeria_looks_anais' -or
   $l -match 'looks_anais' -or $l -match '^_batch_' -or $l -match '/_batch_') -and
  $l -notmatch 'galeria_index|report|\.bkp|03_literatura|canon_visual|ficha_|sistema_poses|banco_prompts' }
```

5. **Excepciones intencionales de Ele** (NO tocar): `galeria_outfits_archivo.md` (L85-L199) y `memoria_historica/galeria_outfits_era_gotica.md` (L01-L84, era Helena) alimentan la app a propósito y **no colisionan** porque la galería viva arranca en L200.
6. La app limpia su base en cada sync (`clearLooks()` + `clearPrompts()` en `replaceDataSilent`), así que **no hay que borrarle los datos**: basta con sincronizar.

---

## 10. ⚠️ POR QUÉ CADA REGLA (las cicatrices)

| Regla | Qué pasó cuando faltó |
|-------|----------------------|
| Un solo slug | 35 looks con carpeta duplicada; imágenes repartidas entre las dos |
| Slug ASCII | `look616_lencer_a`, `look709_suzie_wong_shangh_i`, `look702_..._l_quido` |
| Título descriptivo | L613-L620 titulados con la categoría pelada → slugs que chocan |
| `Ubicacion` sin tilde | 32 looks con ubicación ilegible para la app |
| Metadata antes del `###` | 60 looks (L711-L770) con `canonicalInfo` vacío |
| Fence multilínea | 1.167 prompts mezclados entre poses y looks |
| Negative Prompt obligatorio | 60 looks / 420 poses generadas **sin negativo** desde el L711 |
| Contar el disco, no el tracker | 380 poses ya materializadas figuraban como pendientes → cuota quemada |
| Archivar renombrando (§9bis) | El legacy de Miss Doll y Anaïs pisó los 14 looks nuevos de cada una: la Ama vio outfits antiguos en la app durante días |
| Prefijar la carpeta de imagen al archivar | `_ARCHIVO_LEGACY/look18_x/` sigue entrando: el scanner solo mira la carpeta madre inmediata |
| Prompt expandido, cero placeholders (§9ter) | 98 prompts de Miss Doll con `[BLOQUE A] + [BLOQUE B]` literal y 98 de Anaïs con `[ADN]`: la app los habría mandado así al generador |
| Etiqueta literal del negativo (§9ter) | 28 looks (Miss Doll + Anaïs) sin negativo llegando a la app — el texto estaba escrito, pero con una etiqueta que el parser no reconoce |
| Parsear como parsea la app, no a ojo (§9) | La galería de Miss Doll "se veía impecable" con los 98 prompts rotos. Lo detectó el linter, no la revisión visual |
