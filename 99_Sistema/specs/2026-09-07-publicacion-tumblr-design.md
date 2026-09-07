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

### 6.-1 🚧 Lo que NO se puede automatizar nunca — verificado en la API (07/09/2026)

La Ama preguntó si Ele podía hacerlo todo. Medido contra la documentación oficial de la API v2, no
de memoria:

| Acción | ¿Por API? | Quién |
|---|---|---|
| **Subir el avatar del blog** | ❌ **No existe endpoint.** Solo hay `/avatar` de **lectura** | La Ama, en la web |
| **Subir el header / cambiar el tema** | ❌ **No existe endpoint.** `/info` *devuelve* el tema pero no lo modifica | La Ama, en la web |
| Crear la app de Tumblr y autorizarla | ❌ Necesita su sesión de navegador | La Ama |
| Contar seguidores | ✅ `/blog/{id}/followers` → `total_users` — **exige OAuth como dueña** | Ele, con B4 |
| Posts, títulos, notas | ✅ `/blog/{id}/info` y `/posts` | Ele, con B4 |
| Prueba de visibilidad por tag (§5.5) | ✅ `/tagged` | Ele, con B4 |
| Publicar un capítulo | ✅ `/posts` (NPF) | Ele, **con su okey por post** |

**Conclusión para no volver a prometer de más:** la identidad visual del blog **se sube a mano y
siempre**, no es un pendiente que se resuelva consiguiendo llaves. Todo lo demás —medir, publicar,
leer asks— sí se automatiza en cuanto exista B4.

Fuentes: [API v2 de Tumblr](https://www.tumblr.com/docs/en/api/v2) · [`total_users` en followers](https://github.com/tumblr/pytumblr/issues/12).

---

### 6.0 📐 El encuadre del header NO se le pide al generador — se corta después (07/09/2026)

Tres generaciones seguidas se le pidió a Gemini que dejara el quinto superior e inferior vacíos y
que la figura cupiera en los tres quintos centrales. Las tres fallaron, y **cada una de una forma
distinta**, lo que prueba que no era la redacción:

| v | Qué devolvió |
|---|---|
| v1 | La sala como **panel inset** con marfil arriba y abajo, y la figura **saliéndose** de él |
| v2 | Entendió «franjas vacías» como **viñetas**: tres paneles apilados, cada uno con su marco. La figura seguía cruzando los dos bordes |
| v3 | **Un solo marco** — lo único que sí se arregló por texto — pero la figura seguía ocupando **~85% del alto** en vez del 60% pedido |

**El diagnóstico es geométrico, no de prompt.** Un generador de imágenes no cuenta quintos. Y
encima el pedido era casi imposible: una figura **de cuerpo entero y de pie** dentro de una banda
3:1 obliga a dibujarla diminuta, y un header con una mujer chiquitita al fondo es un header débil.

**Regla que queda:** la composición se le pide al generador; **el encuadre se resuelve después, con
números** — [`99_Sistema/scripts/rrss/recortar_header_tumblr.py`](../scripts/rrss/recortar_header_tumblr.py).
Su anclaje por defecto es **arriba** y no al centro, por el criterio que sale de estas tres rondas:
**una cabeza cortada arruina un header; unos pies cortados no los echa de menos nadie.**

**Ejecutado el 07/09/2026 sobre el header real.** Medido antes de cortar: la figura ocupa
**y 53..730 de 768 = 88% del alto**, así que una banda centrada le corta la cabeza — confirmado con
números, no a ojo. El corte que quedó:

```bash
python 99_Sistema/scripts/rrss/recortar_header_tumblr.py 05_Imagenes/blog_tumblr/header_lavoutedeanais_v1.jpg   --ratio 2.844 --recorte-lateral 24 --anclaje fraccion --desde 0.0508 --ancho-final 3000   --salida 05_Imagenes/blog_tumblr/header_lavoutedeanais_v1_tumblr.jpg
```

- `--ratio 2.844` + `--ancho-final 3000` = la medida que recomienda Tumblr, **3000 × 1055**.
- `--recorte-lateral 24` se come el **marco de viñeta** que el BLOQUE ESTILO obliga a dibujar. Sin
  eso el header sale con borde impreso a los costados y cortado arriba y abajo, que se ve peor que
  no tener marco.
- `--desde 0.0508` apoya la banda **14 px sobre su pelo**: cabeza entera, y se pierden los pies y el
  piso vacío. Conserva el 60,8% del alto.

**Piezas del blog, con sus rutas:**

| Pieza | Archivo | Medida |
|---|---|---|
| Avatar | `05_Imagenes/blog_tumblr/avatar_lavoutedeanais_v1.jpg` | 1024 × 1024 |
| Header (fuente 16:9) | `05_Imagenes/blog_tumblr/header_lavoutedeanais_v1.jpg` | 1376 × 768 |
| **Header para subir** | `05_Imagenes/blog_tumblr/header_lavoutedeanais_v1_tumblr.jpg` | **3000 × 1055** |

---

### 6.1 ✅ La cara del blog: Anaïs (decidido 07/09/2026)

> ✅ **DECIDIDO 07/09/2026 — Anaïs.** La Ama eligió la recomendación; los prompts de §6.2 ya están escritos para ella y no hay que cambiar el bloque de identidad.

El blog se llama **«La Voûte d'Anaïs»**, así que la recomendación es **Anaïs** — es la regenta, el lugar lleva su nombre y es la única de las tres que **no** es una modelo sino la dueña. La alternativa es **Miss Doll**, que es la de la imagen de referencia que la Ama entregó y la más reconocible del catálogo. Los prompts de abajo están escritos para Anaïs; cambiarla es reemplazar el bloque de identidad, nada más.

### 6.2 ✅ Prompts finales v2 (Anaïs) — listos para pegar en Gemini

> 🔒 Usan el **BLOQUE ESTILO congelado** el 07/09/2026 (paleta de Anaïs) — dueño único:
> [`estilo_comic_pop_v1.md`](../../01_Canon/Guias_Especializadas/estilo_comic_pop_v1.md) §2.
> Van **completos y autocontenidos** a propósito: se pegan enteros, sin ensamblar nada a mano.
>
> ⚠️ **Estas dos copias del bloque son literales y verificadas** (`diff` contra la valla del dueño el
> 07/09/2026). No son una excepción a dueño-único: el propio estilo manda copiarlo verbatim a cada
> prompt. Pero si el bloque cambia alguna vez, **estas dos se regeneran desde el dueño**, no se editan
> a mano acá.
>
> **Detalle alto por decisión de la Ama (07/09/2026):** *«altos en detalles para que gemini no
> invente»*. Todo lo que el generador rellenaría solo está dicho: lado del peinado, lado del lunar,
> dirección de la mirada, qué NO se lleva puesto, color exacto del fondo y de los puntos, qué hay
> dentro de las bandas vacías del header, y que cada superficie de la sala va en blanco. Sin pesos
> `:1.4` (§4.1 del estilo: en Gemini son texto inerte) y sin vocabulario fotográfico.

#### 🩹 Qué cambió de la v1 a la v2 — medido sobre la primera generación real (07/09/2026)

La v1 se generó y el estilo salió perfecto (tinta, plano, Ben-Day, off-register, cero letras en las
dos). Estos cinco son los defectos que sí aparecieron, **leídos de la imagen, no supuestos**:

| # | Qué salió mal | Arreglo en v2 |
|---|---|---|
| 1 | 🔴 **Header inservible para su puesto.** Gemini dibujó la sala como **panel inset** con marfil arriba y abajo, y la dejó **salirse** del panel: cabeza sobre la banda superior, tacones bajo la inferior. Recortado a banda angosta, **le corta la cabeza y los pies** — que es exactamente lo que las bandas vacías existían para evitar | Prohibido el cuadro dentro del cuadro (`the room fills the entire width and height, edge to edge`) y ella confinada al **tercio medio de la altura**, dicho como regla y no como sugerencia |
| 2 | 🔴 **El avatar no mira.** Vista corrida a un costado pese a `eyes look straight out at the viewer` | Reescrito como el elemento más importante de la imagen: pupilas centradas, apuntando al lente, `not off to one side and not downward` |
| 3 | 🔴 **El avatar se desarma a 64 px, y la culpa es del prompt.** Cara pálida sobre fondo marfil: casi sin contraste, y el negro que lo sostenía vivía solo en el borde inferior | Fondo **borgoña profundo saturado** con puntos oro. Tres masas separadas: cara clara, vestido negro, campo oscuro |
| 4 | 🟡 **Se ve de treinta, no de 42** — la deriva histórica de Anaïs | Bloque de edad explícito: mejillas magras sin grasa de bebé, la edad se lee en el hueso y en la expresión, **nunca en arrugas** (su canon exige frente lisa: la edad no podía pedirse por líneas) |
| 5 | 🟡 **Cejas gruesas y bajas** y ala del delineado corta · **busto más marcado** que su canon (*natural, no aumentado*) | Cejas `THIN and sharply arched... never thick, never straight, never low-set`; ala como `long hard spike`; y campo FIGURE nuevo: `natural moderate bust — never exaggerated` |

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
She is unmistakably in her early forties and must NOT be drawn as a woman in her
twenties: lean hollowed cheeks with no baby fat anywhere in the face, the composed
face of someone who has commanded rooms for decades. Her skin is smooth and unlined —
her age reads in the bone structure and in the expression, never in wrinkles.
Mature sharp bone structure: high sculpted cheekbones hollowed underneath, a defined
angular jawline, a refined oval face, a completely smooth unlined forehead, a long
slender neck.
HAIR: honey-blonde, warm golden honey, never platinum and never brown and never red,
set in sculpted vintage Hollywood pin-waves with a deep side parting on her right, the
waves rolled back off her forehead and falling well below her shoulders.
EYES: medium almond eyes with a warm honey amber iris, clearly golden-honey coloured
with a dark ring around the iris, never blue and never grey and never washed out. Lids
half-lowered, the gaze level and cold.
BROWS: high, THIN and sharply arched dark brown brows lifted well above the eye socket,
the right one held a fraction higher than the left — never thick, never straight,
never low-set, never soft-edged.
EYE MAKEUP: charcoal and deep taupe smoky shadow in a full cut-crease carried all the
way up into the brow with no bare skin left between, a warm old-gold shimmer laid on
the lid inside the cut-crease, a sharp black winged liner drawn as a long hard spike
extending well past the outer corner of the eye, a thin dark line along the lower lash
line, extremely long dense lashes weighted at the outer corners.
LIPS: full plump lips with a well-defined cupid's bow, painted a vivid deep crimson
red with a high-shine finish, the lower lip heavy, the lips visibly parted, never
closed and never smiling.
A small dark beauty mark sits above her upper LEFT lip — this asymmetry must be obvious.
Warm peach-bronze blush swept along the top of the cheekbone.
Chin carried level or tipped slightly down, never lifted sweetly.
FIGURE: slender and elegant, a narrow waist and a natural moderate bust — never
exaggerated, never inflated, never a pin-up silhouette.

Single comic panel, square 1:1 composition, built to stay readable when it is shrunk
to a 64-pixel square: very large simple shapes, strong contrast, no fine detail
anywhere, nothing important near the corners.
Head-and-shoulders portrait, cropped tight: her head fills roughly three quarters of
the frame height, the top of her hair just touching the upper border, her shoulders cut
off by the lower border. Her head is turned three quarters toward the camera.
HER EYES LOOK STRAIGHT INTO THE LENS. Both pupils are centred in her eyes and aimed at
the viewer, not off to one side and not downward — she is staring directly out of the
picture at whoever is looking at it. This eye contact is the most important element of
the image.
SHE IS WEARING a high-necked long-sleeved black gown — worn on her body, closed,
opaque — covering her throat, chest and shoulders completely from directly under her
chin down past the bottom edge of the frame. The neckline is a plain closed band at the
base of her jaw. Nothing else is worn: no necklace, no earrings, no hat, no veil, no
hands in frame.
BACKGROUND: one single flat field of DEEP BURGUNDY behind her, dark and saturated,
filled evenly with old-gold Ben-Day halftone dots. No scene, no furniture, no props, no
window, no second person, no cast shadow.
The image must read as three clean separate masses even at thumbnail size: her pale
face and honey-blonde hair light, her gown black, the field behind her dark burgundy.
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
She is unmistakably in her early forties and must NOT be drawn as a woman in her
twenties: lean hollowed cheeks with no baby fat anywhere in the face, the composed
face of someone who has commanded rooms for decades. Her skin is smooth and unlined —
her age reads in the bone structure and in the expression, never in wrinkles.
Mature sharp bone structure: high sculpted cheekbones hollowed underneath, a defined
angular jawline, a refined oval face, a completely smooth unlined forehead, a long
slender neck.
HAIR: honey-blonde, warm golden honey, never platinum and never brown and never red,
set in sculpted vintage Hollywood pin-waves with a deep side parting on her right, the
waves rolled back off her forehead and falling well below her shoulders.
EYES: medium almond eyes with a warm honey amber iris, clearly golden-honey coloured
with a dark ring around the iris, never blue and never grey and never washed out. Lids
half-lowered, the gaze level and cold.
BROWS: high, THIN and sharply arched dark brown brows lifted well above the eye socket,
the right one held a fraction higher than the left — never thick, never straight,
never low-set, never soft-edged.
EYE MAKEUP: charcoal and deep taupe smoky shadow in a full cut-crease carried all the
way up into the brow with no bare skin left between, a warm old-gold shimmer laid on
the lid inside the cut-crease, a sharp black winged liner drawn as a long hard spike
extending well past the outer corner of the eye, a thin dark line along the lower lash
line, extremely long dense lashes weighted at the outer corners.
LIPS: full plump lips with a well-defined cupid's bow, painted a vivid deep crimson
red with a high-shine finish, the lower lip heavy, the lips visibly parted, never
closed and never smiling.
A small dark beauty mark sits above her upper LEFT lip — this asymmetry must be obvious.
Warm peach-bronze blush swept along the top of the cheekbone.
Chin carried level or tipped slightly down, never lifted sweetly.
FIGURE: slender and elegant, a narrow waist and a natural moderate bust — never
exaggerated, never inflated, never a pin-up silhouette.

Single comic panel, wide horizontal composition, aspect ratio 16:9, built so that it
can later be cropped down to a narrow horizontal band.
THE CABARET ROOM FILLS THE ENTIRE WIDTH AND HEIGHT OF THE PICTURE, edge to edge. Do
NOT draw the scene as a smaller framed panel sitting inside the image, and do NOT leave
a border of background colour around the scene — there is no picture within the picture.
SHE STANDS ENTIRELY INSIDE THE MIDDLE THREE FIFTHS OF THE FRAME HEIGHT. Nothing of her
— no hair, no head, no hand, no heel — reaches into the top fifth or the bottom fifth of
the image, so that a narrow horizontal crop through the centre never cuts her head or
her feet. The top fifth holds only the upper wall of the room and the bottom fifth only
the empty floor: no furniture, no lettering, no decoration in either band.
She stands in the left third of the frame, full body, head to floor, weight carried on
one hip in an S-curve, turned three quarters toward the camera, her eyes to the viewer.
SHE IS WEARING a floor-length black column gown — worn on her body, closed, opaque —
covering her from the base of her throat to the floor, with long sleeves reaching the
wrist, and one black opera glove on each hand. On her feet, black patent stiletto heels
with a slim 12 cm pin heel and no platform, closed toes.
BEHIND HER, to the right, the empty interior of an elegant cabaret drawn flat: three
rows of small round tables with bentwood chairs, a low stage on the right, heavy
deep-burgundy curtains drawn closed behind the stage, a row of round wall lamps along
the back wall. Every surface in that room is blank: no sign, no poster, no marquee, no
menu, no lettering of any kind anywhere.
The room is drawn lighter and less contrasted than she is, in old gold and antique
bronze halftone over the warm ivory ground, so she stays the darkest and strongest
shape in the frame.
No other person is in the frame — the tables and chairs are empty.
```

> **Por qué la gala cerrada y no la lente fetish:** el avatar y el header son **la portada de la casa** y los ve todo el que llega, incluido el filtro de Tumblr. Es el mismo criterio que ya rige las portadas de Wattpad: *la lente fetish vive en material, silueta y luz, nunca en piel*. El calor va adentro, en las internas de cada capítulo.

**Falta el post fijado** (índice del catálogo + qué es La Voûte + advertencia +18): es texto, no imagen, y se escribe cuando exista la lista de relatos publicados.

---

## 7. Orden de construcción propuesto

| # | Qué | Depende de |
|---|---|---|
| 1 | **Línea base del blog** — piso post-primer-post, ya no virgen (§5.6) **+ la prueba de tag de §5.5 sobre el post de Café que ya está arriba** | B4 (las 4 llaves de OAuth) |
| 2 | ✅ **Avatar + header hechos 07/09** (`05_Imagenes/blog_tumblr/`, header ya cortado a 3000×1055). Falta el post fijado | — |
| 3 | `estilo_comic_pop_v1.md` + activar la §10 de la ficha del personaje | — |
| 4 | ✅ **Adaptador hecho 07/09** — `99_Sistema/scripts/rrss/adaptar_capitulo_tumblr.py`, 23 pruebas en verde, escritas antes del código | — |
| 5 | ✅ **Cola ampliada 07/09** — `tumblr` + `cuerpo_ref`/`relato_ref`/`capitulo` documentados en `06_RRSS/cola/README.md` v0.2 | — |
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
