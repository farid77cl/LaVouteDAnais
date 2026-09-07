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

### 6.1 🔴 Decisión suya: ¿quién es la cara del blog?

El blog se llama **«La Voûte d'Anaïs»**, así que la recomendación es **Anaïs** — es la regenta, el lugar lleva su nombre y es la única de las tres que **no** es una modelo sino la dueña. La alternativa es **Miss Doll**, que es la de la imagen de referencia que la Ama entregó y la más reconocible del catálogo. Los prompts de abajo están escritos para Anaïs; cambiarla es reemplazar el bloque de identidad, nada más.

### 6.2 Prompts listos (Anaïs) — pendientes de que la Ama congele el BLOQUE ESTILO (A2)

**Identidad de Anaïs en registro ilustración** — reescrita en inglés declarativo plano, sin pesos `:1.4` (§4.1 del estilo) y sin vocabulario fotográfico:

```
a 42-year-old aristocratic woman, never young and never girlish: mature sharp bone
structure, sculpted lifted cheekbones, a defined angular jawline, refined oval face.
Honey-blonde hair worn sleek. Warm honey amber eyes, lids half-lowered, the gaze level
and cold, sizing up whoever is looking. High thinly arched dark brown brows, one held a
fraction higher than the other. Charcoal cut-crease smoky eye. Deep red lips, the lower
lip heavy, visibly parted, never smiling. A small beauty mark above her upper left lip.
Chin carried level, never lifted sweetly.
```

**AVATAR — 1:1, legible a 64 px**
```
[BLOQUE ESTILO]
[identidad de Anaïs, arriba]
Head-and-shoulders portrait, tightly cropped, her face filling most of the frame,
turned three-quarters toward the lens with her eyes to the camera. SHE IS WEARING a
high-necked black gown — worn on her body, closed, opaque — covering her chest and
shoulders completely from the base of her throat downward. Flat bubblegum pink
background field with halftone dots, no scene and no props. Square 1:1 composition.
```

**HEADER — 16:9, recortable a 3:1**
```
[BLOQUE ESTILO]
[identidad de Anaïs, arriba]
Wide horizontal composition. She stands at the left third of the frame, full body,
turned toward the camera. SHE IS WEARING a floor-length black column gown — worn on her
body, closed, opaque — covering her from the base of her throat to the floor, with long
sleeves. Behind her, to the right, the empty interior of a cabaret: rows of small round
tables, a low stage, heavy drawn curtains, all rendered flat with halftone shading in
pink and cream. The upper fifth and lower fifth of the frame are empty background so the
image can be cropped to a narrow band without cutting her. Aspect ratio 16:9.
```

> **Por qué la gala cerrada y no la lente fetish:** el avatar y el header son **la portada de la casa** y los ve todo el que llega, incluido el filtro de Tumblr. Es el mismo criterio que ya rige las portadas de Wattpad: *la lente fetish vive en material, silueta y luz, nunca en piel*. El calor va adentro, en las internas de cada capítulo.

**Falta el post fijado** (índice del catálogo + qué es La Voûte + advertencia +18): es texto, no imagen, y se escribe cuando exista la lista de relatos publicados.

---

## 7. Orden de construcción propuesto

| # | Qué | Depende de |
|---|---|---|
| 1 | **Línea base del blog** — capturarla antes de tocar nada (§5.6) | Acceso al blog |
| 2 | Avatar + header + post fijado (§6) | BLOQUE ESTILO congelado |
| 3 | `estilo_comic_pop_v1.md` + activar la §10 de la ficha del personaje | — |
| 4 | Adaptador de post: el `_tumblr.md` completo del capítulo (P1 §4.1) | 3 |
| 5 | Extender `cola_publicacion.json` con `plataforma: "tumblr"` + `cuerpo_ref` | — |
| 6 | Workflow n8n `repo → Tumblr → repo` | B2-B5 de §8 |
| 7 | Corriente B: generador de posts cortos desde la flota + los lemas | 1, 3 |

---

## 8. 🔴 Bloqueadores — cuatro de cinco son clics que solo puede dar la Ama

| # | Bloqueador | Medido |
|---|---|---|
| B1 | **¿`bdsmeros-cl` es suya?** El fetch del blog reporta contenido publicado por ese usuario. Hay que saber si es su identidad de posteo o material ajeno reblogueado | Verificado hoy contra el blog |
| B2 | **El Funnel de Tailscale publica solo `/mcp`.** No llego a la API de administración de n8n ⇒ **no puedo importar ni verificar el flujo yo.** Ella lo importa a mano, como la bandeja (§2.3 de su doc) | Su API key nueva da **404**, no 401 — la diferencia lo es todo |
| B3 | La credencial **dentro** del workflow MCP está en **401**; solo se arregla en su interfaz | Las 5 herramientas MCP rebotan |
| B4 | **Credenciales de app de Tumblr (OAuth)** para que n8n publique | Tumblr no aparece en `checklist_cuentas.md` ni en `.env.example` |
| B5 | **Token de GitHub** para que n8n commitee de vuelta | Mismo que ya necesita la bandeja (§2.4) |

> 🔐 **El repo es público** (decisión suya del 05/09, tomada sabiéndolo). Ningún token entra acá: viven en n8n o en `06_RRSS/.env`, que está en `.gitignore`.

> ⚠️ **El riesgo que no se esconde:** con B2 vivo, el workflow se entrega **escrito y no probado punta a punta**. Funcionó así con la bandeja, pero no se declara operativo hasta que ella lo encienda y se vea un post real con su URL de vuelta en la cola.

---

## 9. Decisiones abiertas

| # | Qué | ¿Bloquea? |
|---|---|---|
| A1 | **Frecuencia de publicación** (D11, ella la dejó por definir) | No — el disparador es el Gate, no un calendario |
| A2 | **BLOQUE ESTILO definitivo** — calibrar contra su imagen de referencia | Sí para producir |
| A3 | ¿Estrena con «¿Cuánto es?» (47,8% de sus lecturas, ya publicado, ya tiene `prompts_portada.md`)? | No |
| A4 | **Corriente B: ¿cuánto es «alta cadencia»?** El referente postea a diario hace 4 años | No, pero define la meta |
| A5 | Los 63 lemas **hay que inventarlos en chileno, no traducirlos** (el análisis lo advierte). ¿Los escribe un subagente? | No |
