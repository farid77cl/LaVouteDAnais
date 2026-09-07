# Diseño — Publicación en Tumblr + misión de crecimiento de @lavoutedeanais

| Campo | Valor |
|---|---|
| **Fecha** | 07/09/2026 |
| **Autor** | Ele de Anaïs (Vibe Architect) |
| **Origen** | Orden de la Ama, sesión 07/09/2026 |
| **Estado** | 🟡 Diseño escrito con la Ama fuera de línea — **pendiente de su revisión** |
| **Hermano** | [`2026-09-07-ilustracion-relatos-design.md`](2026-09-07-ilustracion-relatos-design.md) (P2, la ilustración) |
| **Destino documental** | *working* (regla 12) |
| **🪦 Fecha de muerte declarada** | Muere cuando existan `.agent/skills/publicar-tumblr/SKILL.md` + la estrategia viva en `06_RRSS/`. Ahí se borra: el SKILL toma el protocolo y `06_RRSS/estrategia_seo_tags.md` toma la sección de crecimiento. |

---

## 0. Cómo retomar esto en frío

Se brainstormeó entero el 07/09/2026. La Ama tomó **once decisiones** (§2) y se fue antes de revisar. Lo que falta para arrancar está en §8 «Bloqueadores», y **cuatro de los cinco son clics que solo puede dar ella**.

---

## 1. Qué se está construyendo

Que los relatos de La Voûte se publiquen en **Tumblr (@lavoutedeanais)** de forma **automática y programada**, sin depender de que el PC de la Ama esté encendido — y que el blog **crezca**, que es una misión aparte y más difícil que publicar.

---

## 2. Decisiones de la Ama (literales, 07/09/2026)

| # | Tema | Decisión |
|---|---|---|
| D1 | Volumen de imagen | **Portada + 2 por capítulo** |
| D7 | Portada vs. internas | *"si los relatos van por cap, se mantiene la portada, cambian las imagenes dentro"* — **la portada es del relato**, se repite en todos sus posts |
| D9 | **Tumblr es destino, no anzuelo** | **El relato completo vive en Tumblr.** Un post por capítulo, cortado con `<!-- more -->` |
| D10 | Qué se adapta | **Solo el envase. El texto no se toca ni una coma** — es el que pasó su Gate |
| D11 | Alcance | *"a medida que se publiquen, la frecuencia esta por definir"* |
| D12 | **Automatización** | *"la idea es que tu armes todo, y se postee, hasta podrias usar n8n para dejarlo programado y no depender de que este el pc prendido"* |
| D13 | Por qué Reddit quedó manual | *"p3 porque nunca quedo operativa la api de reedit"* — **fue un atasco, no una preferencia** |
| D14 | El blog | **@lavoutedeanais** — «La Voûte d'Anaïs», verificado, existe y tiene contenido |
| D15 | **Misión nueva** | *"ademas debes tener como mision que el blog se haga viral"* |
| D16 | Imágenes del blog | *"ocupate de las imagenes del blog y todo lo necesario"* |

> 🩹 **D13 corrige un error mío de esta misma sesión.** Le recomendé publicación manual citando su directiva del 08/06 (*"NO crear app de API (no avanza)"*) **como si fuera una preferencia suya**. Era la descripción de un atasco. Proponerle consagrar un parche como arquitectura es exactamente el modo de falla que este repo llama *envejecer hacia la mentira* — y lo cometí yo, leyendo mal su propio archivo.

---

## 3. Lo que ya existe (medido 07/09/2026)

### 3.1 La cola ya está diseñada y nunca tuvo cuerpo

`06_RRSS/cola/README.md`, escrito en junio, describe **exactamente** lo que la Ama pidió hoy:

> *"El puente entre el **cerebro** (Ele, acá) y el **cuerpo** (runtime que publica 24/7). Yo escribo posts listos en `cola_publicacion.json`; el runtime los lee, publica y los marca como hechos."*
>
> `Ele encola → git push → runtime lee → publica → marca "publicado" → commitea de vuelta`
>
> Ley: ***"El runtime NUNCA crea contenido — solo publica lo que ya está en la cola."***

El esquema de `cola_publicacion.json` ya trae `id · estado · plataforma · destino · titulo · caption · nsfw · hashtags · publicar_desde · gate · publicado_en · url`. **Ya publicó de verdad** — hay URLs reales de Bluesky adentro. Lo único que le faltó siempre es **runtime para algo que no fuera Bluesky**.

### 3.2 n8n ya es el cuerpo, y ya hay precedente

| Pieza | Estado |
|---|---|
| Instancia n8n en DietPi (`dietpi.tail05c49d.ts.net`), 24/7 | ✅ corriendo — el scraper de todorelatos lleva **27 días de 27 sin un hueco** |
| Flujo importable de ejemplo | ✅ `99_Sistema/n8n/workflow_bandeja_telegram.json`, 4 nodos |
| Patrón n8n ↔ GitHub, con token y escritura al repo | ✅ documentado en `99_Sistema/n8n/BANDEJA_TELEGRAM.md` |
| Trampa de huso horario | ✅ documentada: n8n corre en **UTC**; sin restar 4h el orden miente |

**Esto es la bandeja al revés.** La bandeja es `Telegram → n8n → repo`; esto es `repo → n8n → Tumblr → repo`.

### 3.3 Los otros activos

- **Kit de publicación por relato:** `prompts_portada.md` (dueño de prompts de imagen **y de los tags Tumblr por capítulo**) + `kit_wattpad.md` (metadata, descripción, 25 tags, **calendario**, checklist, **registro de publicación**). Cobertura: **4 y 5 de 43** relatos.
- **`caption_factory.py`** — ya produce captions en voz de Ele.
- **`estrategia_seo_tags.md`** — estrategia real, pero solo de Reddit y Bluesky. **Tumblr no aparece.**
- **7.349 PNG** de tres muñecas, ya materializados y con galería.

---

## 4. Arquitectura de publicación (P3)

```
  Ele arma el post  ──►  cola_publicacion.json  ──►  git push
                                                         │
                            n8n (DietPi, 24/7)  ◄────────┘
                            Schedule Trigger
                                 │
                                 ├─ lee la cola desde GitHub
                                 ├─ filtra: estado=pendiente · gate=aprobado · publicar_desde ya pasó
                                 ├─ baja el cuerpo (cuerpo_ref → el _tumblr.md del repo)
                                 ├─ POST a la API de Tumblr (blog: lavoutedeanais)
                                 └─ commitea de vuelta: estado=publicado + url + publicado_en
```

**Tres decisiones de diseño y por qué:**

1. **El cuerpo NO se embebe en el JSON.** Un capítulo son ~14.000 palabras. La cola guarda `cuerpo_ref` (ruta del `_tumblr.md`) y n8n lo baja. La cola es un índice, no un almacén.
2. **Huso horario explícito siempre.** `publicar_desde` con offset (`-04:00`), como ya lo traen las entradas vivas. n8n corre en UTC dentro del contenedor.
3. **Falla cerrado.** Igual que la bandeja: sin `gate=aprobado`, el flujo no publica. **La Regla de Oro 8c no se relaja por estar automatizado** — al contrario: un runtime que publica solo es exactamente donde un Gate inferido se vuelve irreversible, y eso ya pasó una vez (Cap 4 de «Café con Piernas», publicado sin que ella lo leyera).

### 4.1 Anatomía del post (P1 — envase, texto intacto)

```
🖼️  portada_<slug>.png              ← la misma en los N posts del relato (D7)
    «Título» — Capítulo N
    gancho de 2-3 líneas             ← prosa NUEVA → la escribe un subagente, nunca el orquestador
    <!-- more -->  ────────────────── el corte del feed
    …texto del capítulo, intacto (D10)…
      🖼️ cap<N>_a  en el beat de instalación del fetiche
      🖼️ cap<N>_b  en el cliffhanger, antes del cierre
    Nota de autora · Advertencia +18 · Content Label de Tumblr
    ← Cap anterior · Índice · Cap siguiente →
    #tags
```

- **El gancho es prosa nueva ⇒ subagente.** Ley del repo: la prosa nunca la escribe el orquestador. Y es el 90% del rendimiento del post: son las líneas que deciden si alguien abre.
- **La navegación obliga a guardar la URL de cada post.** Molde ya existente: `kit_wattpad.md` §8 «Registro de publicación».
- **Los tags ya existen** y ya son por capítulo, dentro de `prompts_portada.md`.

---

## 5. 🚀 La misión de crecimiento (D15) — lo que se puede prometer y lo que no

### 5.1 Lo que NO se promete

**«Viral» no se diseña.** El propio análisis que la Ama mandó a hacer lo dice en su §8: *«No mide la recepción: 16.467 notas dicen difusión, no efecto»*. Prometerle viralidad sería adulación, y la adulación que esconde un problema está prohibida en este repo. Lo que sí se puede hacer es **construir el motor de descubrimiento con evidencia** y **medirlo**.

### 5.2 El hallazgo que da vuelta el plan

`07_Recursos/analisis_switchingdesires_tumblr.md` midió un blog **del nicho exacto de la Ama**, con OAuth contra la API oficial:

| Medida | Valor |
|---|---|
| Posts | **2.008** |
| **Mediana de largo de post** | **26 palabras** |
| Formato dominante | *Recordatorio*: 1-3 frases, doctrina, remate con emoji |
| Posts de foto | **4** de 2.008 |
| Post más difundido | **16.467 notas** |

**Nuestro plan publica capítulos de ~14.000 palabras. El motor de Tumblr es el reblog. Nadie reblogea 14.000 palabras.**

Un blog hecho **solo** de capítulos no crece — no por malo, por **formato**. El capítulo es el **destino** (D9, y está bien); lo que falta es el **vehículo**.

### 5.3 El modelo de dos corrientes

| Corriente | Qué es | Cadencia | Función |
|---|---|---|---|
| **A · El relato** | Capítulo completo, portada + 2 imágenes, tags | Cuando hay Gate (D11) | **Destino.** Es el producto |
| **B · El material reblogueable** | Post corto: una imagen de la flota, un lema, un mantra, un motivo del relato | Alta, diaria o casi | **Vehículo.** Es lo que trae gente al destino |

**La corriente B ya tiene materia prima en el repo y no hay que inventarla:**
- **7.349 PNG** de Ele, Miss Doll y Anaïs, con galería y metadata.
- **63 lemas** documentados con su forma tipográfica (`✨…✨`), más mantras y aperturas-fórmula — catalogados en el análisis §3, en inglés y **pendientes de traducir al chileno, no de calcar** (el propio análisis lo advierte).
- **`caption_factory.py`**, que ya arma captions en voz de Ele.

> ⚠️ **El límite que el análisis mismo pone:** copiar el formato aforístico **en los relatos** produciría capítulos de eslóganes — el `C17` de firma de IA que estamos combatiendo. La corriente B es **distribución**, jamás narrativa. Las dos corrientes no se mezclan.

### 5.4 Los tags, medidos en el nicho real

Del mismo análisis, los tags más usados por un blog que funciona en este nicho (número = veces usado en 2.008 posts):

`corruption kink` (901) · `mind corruption` (866) · `dumbification` (847) · `brainwashing` (845) · `bimbo training` (821) · `humiliation kink` (795) · `degredation kink` (726) · `bimboification` (711) · `patriarchy kink` (257) · `gaslighting kink` (149)

**En inglés**, aunque el relato sea en chileno — es coherente con lo que el `SKILL.md` del motor ya dice: *«el nicho TG/bodyswap busca en inglés aunque lea en español»*.

### 5.5 🔴 El riesgo mayor de la misión, sin resolver

Verificado hoy contra las guías oficiales de Tumblr:

- Ficción erótica **escrita** no está prohibida; lo prohibido son *"visual depictions of sexually explicit acts"*. La imagen PG-13 (D3) cae del lado seguro.
- Etiquetar contenido maduro es **obligatorio**: *"add a Content Label to your mature content"*.
- ⚠️ *"Blogs which have a focus on mature content **may not be eligible for certain Tumblr features**"* — el documento **no dice** si eso incluye quedar fuera de la búsqueda por tags o de Explore.

**Ese es el hueco, y es el que decide la misión entera:** si un blog marcado como maduro queda invisible en la búsqueda por tags, toda la estrategia de §5.4 se cae y el crecimiento tendría que venir por reblogs y comunidad, no por descubrimiento. **No se puede resolver leyendo — se resuelve midiendo**: publicar un post etiquetado y verificar a mano si aparece en su tag. Es la primera prueba a correr cuando el blog esté operativo.

### 5.6 Cómo se mide la misión (para que «viral» no sea una vibra)

**Antes de publicar nada hay que capturar la línea base del blog**: seguidores, posts, notas medianas. Sin línea base no hay medición, hay opinión.

> ⏭️ **Premisa superada — 07/09/2026.** La Ama confirmó que **el Cap 1 de «Café con Piernas» ya está publicado** en el blog. O sea: el blog **no** está virgen y la línea base que capturemos ya no es pre-publicación, es **el piso después del primer post**. Se captura igual —es el único piso que vamos a tener— pero se **rotula como tal**, no se le llama línea base virgen. Y hay una ganancia: la prueba de §5.5, que era la que decidía la misión entera, **ya no espera a nada**: hay un post real que mirar en su tag hoy mismo.

| Métrica | Por qué esa |
|---|---|
| **Notas medianas por post**, separadas por corriente A y B | Es la unidad real de difusión de Tumblr |
| **Ratio reblog / like** | Un like muere; un reblog es lo que propaga. Es el indicador de viralidad, no las notas totales |
| **Seguidores nuevos por semana** | El único acumulativo |
| **Visibilidad en tag** (sí/no, verificado a mano) | Resuelve §5.5 |
| **Clics al relato desde la corriente B** | Mide si el vehículo lleva al destino, que es el punto entero |

**Y la comparación honesta:** el blog de referencia tardó **4 años y 2.008 posts** (2022→2026) en llegar a donde está. Cualquier meta que ignore ese orden de magnitud es fantasía.

---

## 6. 🎨 Imágenes del blog (D16)

El blog necesita, antes de publicar nada:

| Pieza | Formato | Contenido propuesto |
|---|---|---|
| **Avatar** | cuadrado, legible a 64 px | Un solo rostro en el estilo pop-art, plano cerrado, alto contraste. A 64 px un cuerpo entero es una mancha |
| **Header** | panorámico (~3:1) | Composición horizontal de las tres muñecas o un motivo de La Voûte, con **20% superior e inferior vacíos** por el recorte, misma disciplina que el banner de Wattpad |
| **Post fijado** | post normal | Índice del catálogo + qué es La Voûte + advertencia +18 |

**Los prompts usan el BLOQUE ESTILO** de [`estilo_comic_pop_v1.md`](../../01_Canon/Guias_Especializadas/estilo_comic_pop_v1.md), con sus tres candados afirmativos y **sin bloque negativo**, porque este texto viaja dentro del prompt que la Ama pega en Gemini.

### 6.1 ✅ La cara del blog: Anaïs (decidido 07/09/2026)

> ✅ **DECIDIDO 07/09/2026 — Anaïs.** La Ama eligió la recomendación; los prompts de §6.2 ya están escritos para ella y no hay que cambiar el bloque de identidad.

El blog se llama **«La Voûte d'Anaïs»**, así que la recomendación es **Anaïs** — es la regenta, el lugar lleva su nombre y es la única de las tres que **no** es una modelo sino la dueña. La alternativa es **Miss Doll**, que es la de la imagen de referencia que la Ama entregó y la más reconocible del catálogo. Los prompts de abajo están escritos para Anaïs; cambiarla es reemplazar el bloque de identidad, nada más.

### 6.2 ✅ Prompts finales (Anaïs) — listos para pegar en Gemini

> 🔒 Usan el **BLOQUE ESTILO congelado** el 07/09/2026 (paleta de Anaïs) — dueño único:
> [`estilo_comic_pop_v1.md`](../../01_Canon/Guias_Especializadas/estilo_comic_pop_v1.md) §2.
> Van **completos y autocontenidos** a propósito: se pegan enteros, sin ensamblar nada a mano.
>
> ⚠️ **Estas dos copias del bloque son literales y verificadas** (`diff` contra la valla del dueño el
> 07/09/2026). No son una excepción a dueño-único: el propio estilo manda copiarlo verbatim a cada
> prompt. Pero si el bloque cambia alguna vez, **estas dos se regeneran desde el dueño**, no se editan
> a mano acá.
>
> **Detalle alto por decisión de la Ama (07/09/2026):** *«altos en detalles para que Gemini no
> invente»*. Todo lo que el generador podría rellenar solo está dicho: lado del peinado, lado del
> lunar, dirección de la mirada, qué NO se lleva puesto, color exacto del fondo y de los puntos,
> qué hay dentro de las bandas vacías del header, y que cada superficie de la sala va en blanco.
> Sin pesos `:1.4` (§4.1 del estilo: en Gemini son texto inerte) y sin vocabulario fotográfico
> (acá se ilustra, no se fotografía).
>
> 🖤 **Por qué el vestido es negro con paleta miel:** el negro es el **primer color de su §5.2** y
> el que sostiene el avatar a 64 px — a ese tamaño lo único que se lee es el contraste entre dos
> masas. Oro/bronce/marfil viven en el fondo y en la sala; ella es la mancha oscura.

**AVATAR — cuadrado 1:1, legible a 64 px**

```
1960s romance comic book illustration, vintage newsprint aesthetic, bold black ink
outlines of even confident weight around every figure and object, flat cel-shaded
colour with no gradients and no soft shading, visible Ben-Day halftone dot texture
carried through the shadows and the background field, limited palette built on old
gold, antique bronze and dusty rose with deep burgundy accents over a warm ivory
ground, slight off-register print misalignment, clean single comic panel with a thin
dark border, NO TEXT ANYWHERE, every label, sign, poster and garment surface
completely blank

A single woman, 42 years old, aristocratic and severe, never young and never girlish.
Mature sharp bone structure: high sculpted cheekbones hollowed underneath, a defined
angular jawline, a refined oval face, a completely smooth unlined forehead.
HAIR: honey-blonde, warm golden honey, never platinum and never brown and never red,
set in sculpted vintage Hollywood pin-waves with a deep side parting on her right, the
waves rolled back off her forehead and falling long past her shoulders.
EYES: medium almond eyes with a warm honey amber iris, clearly golden-honey coloured
with a dark ring around the iris, never blue and never grey and never washed out. Lids
half-lowered, the gaze level and cold, fixed on whoever is looking.
BROWS: high thinly arched dark brown brows lifted well above the eye socket, the right
one held a fraction higher than the left.
EYE MAKEUP: charcoal and deep taupe smoky shadow in a full cut-crease carried all the
way up into the brow with no bare skin left between, a warm old-gold shimmer laid on
the lid inside the cut-crease, a sharp black winged liner with a long wing extending
well past the outer corner, a thin dark line along the lower lash line, extremely long
dense lashes weighted at the outer corners.
LIPS: full plump lips with a well-defined cupid's bow, painted a vivid deep crimson
red with a high-shine finish, the lower lip heavy, the lips visibly parted, never
closed and never smiling.
A small dark beauty mark sits above her upper LEFT lip — this asymmetry must be obvious.
Warm peach-bronze blush swept along the top of the cheekbone.
Chin carried level or tipped slightly down, never lifted sweetly.

Single comic panel, square 1:1 composition, built to stay readable when it is shrunk
to a 64-pixel square: very large simple shapes, strong contrast, no fine detail
anywhere, nothing important near the corners.
Head-and-shoulders portrait, cropped tight: her head fills roughly three quarters of
the frame height, the top of her hair just touching the upper border, her shoulders cut
off by the lower border. Her head is turned three quarters toward the camera and her
eyes look straight out at the viewer.
SHE IS WEARING a high-necked long-sleeved black gown — worn on her body, closed,
opaque — covering her throat, chest and shoulders completely from directly under her
chin down past the bottom edge of the frame. The neckline is a plain closed band at the
base of her jaw. Nothing else is worn: no necklace, no earrings, no hat, no veil, no
hands in frame.
BACKGROUND: one single flat field of warm ivory behind her, filled evenly with old-gold
Ben-Day halftone dots. No scene, no furniture, no props, no window, no second person,
no cast shadow.
Her black gown and the ivory background must read as two clean separate shapes.
```

**HEADER — 16:9, recortable a una banda angosta**

```
1960s romance comic book illustration, vintage newsprint aesthetic, bold black ink
outlines of even confident weight around every figure and object, flat cel-shaded
colour with no gradients and no soft shading, visible Ben-Day halftone dot texture
carried through the shadows and the background field, limited palette built on old
gold, antique bronze and dusty rose with deep burgundy accents over a warm ivory
ground, slight off-register print misalignment, clean single comic panel with a thin
dark border, NO TEXT ANYWHERE, every label, sign, poster and garment surface
completely blank

A single woman, 42 years old, aristocratic and severe, never young and never girlish.
Mature sharp bone structure: high sculpted cheekbones hollowed underneath, a defined
angular jawline, a refined oval face, a completely smooth unlined forehead.
HAIR: honey-blonde, warm golden honey, never platinum and never brown and never red,
set in sculpted vintage Hollywood pin-waves with a deep side parting on her right, the
waves rolled back off her forehead and falling long past her shoulders.
EYES: medium almond eyes with a warm honey amber iris, clearly golden-honey coloured
with a dark ring around the iris, never blue and never grey and never washed out. Lids
half-lowered, the gaze level and cold, fixed on whoever is looking.
BROWS: high thinly arched dark brown brows lifted well above the eye socket, the right
one held a fraction higher than the left.
EYE MAKEUP: charcoal and deep taupe smoky shadow in a full cut-crease carried all the
way up into the brow with no bare skin left between, a warm old-gold shimmer laid on
the lid inside the cut-crease, a sharp black winged liner with a long wing extending
well past the outer corner, a thin dark line along the lower lash line, extremely long
dense lashes weighted at the outer corners.
LIPS: full plump lips with a well-defined cupid's bow, painted a vivid deep crimson
red with a high-shine finish, the lower lip heavy, the lips visibly parted, never
closed and never smiling.
A small dark beauty mark sits above her upper LEFT lip — this asymmetry must be obvious.
Warm peach-bronze blush swept along the top of the cheekbone.
Chin carried level or tipped slightly down, never lifted sweetly.

Single comic panel, wide horizontal composition, aspect ratio 16:9, built so that it
can later be cropped down to a narrow horizontal band.
THE TOP FIFTH of the image and THE BOTTOM FIFTH of the image are empty background only:
nothing there but the ivory ground and its halftone dots — no part of her body, no
furniture, no lettering, no decorative border inside those two bands.
She stands in the left third of the frame, full body, head to floor, weight carried on
one hip in an S-curve, turned three quarters toward the camera, her eyes to the viewer.
Her head sits below the empty top band and her shoes sit above the empty bottom band,
so a narrow crop never cuts her head or her feet.
SHE IS WEARING a floor-length black column gown — worn on her body, closed, opaque —
covering her from the base of her throat to the floor, with long sleeves reaching the
wrist, and one black opera glove on each hand. On her feet, black patent stiletto heels
with a slim 12 cm pin heel and no platform, closed toes.
BEHIND HER, to the right, the empty interior of an elegant cabaret drawn flat: three
rows of small round tables with chairs, a low stage on the right, heavy deep-burgundy
curtains drawn closed behind the stage, a row of round wall lamps along the back wall.
Every surface in that room is blank: no sign, no poster, no marquee, no menu, no
lettering of any kind anywhere.
The room is drawn smaller and lighter than she is, in old gold and antique bronze
halftone over the warm ivory ground, so she stays the darkest and strongest shape in
the frame.
No other person is in the frame — the tables and chairs are empty.
```

> **Por qué la gala cerrada y no la lente fetish:** el avatar y el header son **la portada de la casa** y los ve todo el que llega, incluido el filtro de Tumblr. Es el mismo criterio que ya rige las portadas de Wattpad: *la lente fetish vive en material, silueta y luz, nunca en piel*. El calor va adentro, en las internas de cada capítulo.

**Falta el post fijado** (índice del catálogo + qué es La Voûte + advertencia +18): es texto, no imagen, y se escribe cuando exista la lista de relatos publicados.

---

## 7. Orden de construcción propuesto

| # | Qué | Depende de |
|---|---|---|
| 1 | **Línea base del blog** — piso post-primer-post, ya no virgen (§5.6) **+ la prueba de tag de §5.5 sobre el post de Café que ya está arriba** | B4 (las 4 llaves de OAuth) |
| 2 | Avatar + header + post fijado (§6) | BLOQUE ESTILO congelado |
| 3 | `estilo_comic_pop_v1.md` + activar la §10 de la ficha del personaje | — |
| 4 | Adaptador de post: el `_tumblr.md` completo del capítulo (P1 §4.1) | 3 |
| 5 | Extender `cola_publicacion.json` con `plataforma: "tumblr"` + `cuerpo_ref` | — |
| 6 | Workflow n8n `repo → Tumblr → repo` | B2-B5 de §8 |
| 7 | Corriente B: generador de posts cortos desde la flota + los lemas | 1, 3 |

---

## 8. 🔴 Bloqueadores — B1 resuelto 07/09; quedan cuatro, todos clics que solo puede dar la Ama

| # | Bloqueador | Medido |
|---|---|---|
| B1 | ✅ **RESUELTO 07/09/2026 — sí es suya.** La Ama: *«si, pero hay que darla de baja»*. ⇒ `bdsmeros-cl` **no** es el destino: el destino es `@lavoutedeanais`. Queda una acción suya, fuera de este flujo: **dar de baja `bdsmeros-cl`** | Respondido por ella en el arranque del 07/09 |
| B2 | **El Funnel de Tailscale publica solo `/mcp`.** No llego a la API de administración de n8n ⇒ **no puedo importar ni verificar el flujo yo.** Ella lo importa a mano, como la bandeja (§2.3 de su doc) | Su API key nueva da **404**, no 401 — la diferencia lo es todo |
| B3 | La credencial **dentro** del workflow MCP está en **401**; solo se arregla en su interfaz | Las 5 herramientas MCP rebotan |
| B4 | **Credenciales de app de Tumblr (OAuth)** — ahora con nombres y origen declarados en [`06_RRSS/.env.example`](../../06_RRSS/.env.example): las **cuatro** patas (`TUMBLR_CONSUMER_KEY/SECRET` + `TUMBLR_OAUTH_TOKEN/TOKEN_SECRET`). Sirven para la línea base **y** para que n8n publique | El conteo de seguidores solo lo devuelve la API firmando como **dueña** del blog; con sola `api_key` no viene |
| B5 | **Token de GitHub** para que n8n commitee de vuelta | Mismo que ya necesita la bandeja (§2.4) |

> ✅ **El blog ya existe y ya está marcado maduro** (confirmado por la Ama, 07/09/2026). ⇒ la prueba de §5.5 (¿un blog maduro sale en la búsqueda por tags?) es medible en cuanto haya un post etiquetado.

> 🔐 **El repo es público** (decisión suya del 05/09, tomada sabiéndolo). Ningún token entra acá: viven en n8n o en `06_RRSS/.env`, que está en `.gitignore`.

> ⚠️ **El riesgo que no se esconde:** con B2 vivo, el workflow se entrega **escrito y no probado punta a punta**. Funcionó así con la bandeja, pero no se declara operativo hasta que ella lo encienda y se vea un post real con su URL de vuelta en la cola.

---

## 9. Decisiones abiertas

| # | Qué | ¿Bloquea? |
|---|---|---|
| A1 | **Frecuencia de publicación** (D11, ella la dejó por definir) | No — el disparador es el Gate, no un calendario |
| A2 | **BLOQUE ESTILO definitivo** — calibrar contra su imagen de referencia | Sí para producir |
| A3 | ✅ **CERRADA 07/09/2026 — ya estrenó.** La Ama: *«ya esta el cap 1 del cafe»*, publicado en el blog. El adaptador de §4.1 se escribe **contra ese post real**, no contra un envase teórico | — |
| A4 | **Corriente B: ¿cuánto es «alta cadencia»?** El referente postea a diario hace 4 años | No, pero define la meta |
| A5 | Los 63 lemas **hay que inventarlos en chileno, no traducirlos** (el análisis lo advierte). ¿Los escribe un subagente? | No |
