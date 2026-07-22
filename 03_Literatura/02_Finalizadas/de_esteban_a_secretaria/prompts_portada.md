# De Esteban a Secretaria — Tags y Prompts de Portada

> 📕 **Calibración Wattpad (22/07/2026):** reglas verificadas en `07_Recursos/guia_publicacion_wattpad.md` · metadata de publicación en [`kit_wattpad.md`](kit_wattpad.md).
> **Regla dura de Wattpad:** prohibida la exposición completa de genitales, pechos y glúteos, y toda representación de acto sexual — borran la imagen sin aviso.
>
> ⚠️ **CORRECCIÓN 22/07 (probado en producción):** la primera versión de esta nota mandaba pegarle a cada prompt una línea `STRICTLY: no nudity, no exposed nipples…`. **Eso era un error y hacía rebotar el prompt** (*"Sorry, I can't generate unsafe images"*): el filtro **no procesa la negación, lee los tokens**. Nombrar lo prohibido lo dispara aunque vaya precedido de "no".
>
> **Doctrina vigente — tres reglas:**
> 1. **La cobertura se consigue en positivo:** `She is wearing a [prenda] — closed, opaque — covering [zona] from [borde] to [borde].` Nunca por implicación, nunca por negativo.
> 2. **Nunca se nombra lo prohibido**, ni para prohibirlo. Registro léxico en clave **editorial / cine de época**, no erótica (`Editorial book cover`, no `Erotic novel cover`). La lista `STRICTLY` sigue viva como **checklist mío antes de entregar**, no como texto para el generador.
> 3. **Si el cuerpo sigue saliendo desnudo, el problema es la CÁMARA, no el vocabulario.** Ver la historia de la portada del Cap 1 más abajo.
>
> **Nota técnica:** Gemini no genera 2:3 nativo → pedir **3:4** y recortar. El texto largo es lotería (salió «Secretaia»): el default es generar **sin texto** y componer la tipografía después.

---

## Tags

### Relato completo
`#Feminización` `#MTF` `#Transformación` `#Sumisión` `#Hormonas` `#Sissy` `#CuckoldInverso` `#Trío` `#Humillación` `#Control` `#Femdom` `#Dependencia` `#SecretariaForzada` `#IdentidadFluida` `#EncargoDeEsposa` `#LaVoûtedAnaïs`

### Capítulo 1 — La Semana
`#Feminización` `#MTF` `#Transformación` `#Sumisión` `#Hormonas` `#Sissy` `#DomesticFemdom` `#Cera` `#Corsé` `#Maquillaje` `#EspejoDeOtro`

### Capítulo 2 — La verga que coge a Valeria
`#Feminización` `#MTF` `#CuckoldInverso` `#Sumisión` `#Hormonas` `#Trío` `#Humillación` `#DeseoVsIdentidad` `#LoftEjecutivo` `#Descubrimiento` `#TriánguloTóxico`

---

## Prompts de portada (English — para Gemini)

> **Formato:** 512 × 800 px · portrait vertical (2:3) · portada de novela adulta literaria. Título y autora renderizados en la imagen por el generador. Composición con focal claro al centro — debe leerse a 256 px de ancho (miniatura móvil Wattpad). Fondo oscuro dominante + texto blanco/crema de alto contraste. Sensualidad: calor, piel, postura cargada — sin ser explícito.
>
> **Identidad visual LVA — Anaïs Belland:** Fondo negro caoba o caoba profundo · acento dorado cálido para título y barra · autora en small-caps · serif clásica (Palatino, Garamond, Book Antiqua). No mezclar con el rosa caliente de Miss Doll ni el rojo cereza de Ele.

---

### Portada general — el relato completo

```
Book cover, portrait vertical (2:3 ratio). Editorial book cover, sensual and elegant. Dramatic chiaroscuro lighting, deep shadows, warm amber glow.

FIGURE: A glamorous, alluring woman, full body centered in frame. She stands in a doorway with her back slightly toward camera, face turned over her shoulder — looking directly at the viewer with dark, heavy-lidded eyes and dark red lips slightly parted. Her ivory silk blouse is tucked into a body-hugging black pencil skirt that emphasizes the curve of her hips; the blouse is open two buttons at the collar, revealing her collarbone and the base of her throat. Her dark caramel hair falls loose in soft waves past her shoulders. She wears dark burgundy stiletto pumps. One hand rests on the doorframe at hip level. Her posture: back subtly arched, weight on one hip, the body aware it is being watched.

BACKGROUND: behind her, split world — warm amber vanity light on the left with perfume bottles and a small wax pot; Santiago city lights through floor-to-ceiling glass on the right, night, the edge of an executive caoba desk visible.

TYPOGRAPHY (rendered in image): At the top, elegant serif title in warm cream or deep gold — high contrast against the dark background, legible at thumbnail size: "De Esteban a Secretaria". Immediately below the title, a thin horizontal accent rule in warm gold, left-aligned, the width of the longest title word. At the very bottom, small-caps lettering in warm gold: "ANAÏS BELLAND". Both elements flush with the figure, clean and readable at 256px wide.

Mood: heat, ownership, a woman made by another's hands who does not yet know it. Photo-realistic, hyper-polished, 8k.
```

---

### Capítulo 1 — La Semana ✅ **v4 (usar ESTE — cambia la CÁMARA, no las palabras)**

> **Tres intentos, tres lecciones distintas. Vale la pena leerlas antes de tocar cualquier otro prompt:**
>
> **v1 → topless.** El prompt decía *"shoulders are bare, upper chest visible"* y **nunca declaró una prenda sobre el cuerpo**. El corsé quedó en **un torso aparte**, el espejo inventó **una tercera mujer**, los dos ojos salieron iguales y el frasco trajo texto inventado.
>
> **v2 → no se generó:** *"Sorry, I can't generate unsafe images."* La mató **la línea que le puse para protegerla**. El filtro no procesa la negación: lee los tokens. `no nudity, no topless, no exposed nipples…` son palabras rojas seguidas, y da lo mismo el "no" delante.
>
> **v3 → seguía rara**, porque el defecto no estaba en el vocabulario sino en la **cámara**. Pedir *"vista frontal tres cuartos"* + *"le aprietan los cordones por la espalda"* es pedir dos cosas incompatibles: el corsé que se lacea está **detrás** de la figura, así que el modelo lo dibuja detrás — como objeto suelto — y deja el frente sin nada. Ninguna cantidad de adjetivos arregla una geometría imposible.
>
> **v4 = la cámara se pone DETRÁS.** La toma canónica del corsé laceado es de espaldas: así el cuerpo queda cubierto **por construcción**, no por promesa, y el rostro (con el maquillaje a medio hacer, que es el corazón de la escena) vuelve por el **espejo del tocador**. Es además la imagen más fiel al capítulo: Estefanía mirándose ser fabricada.

```
Editorial book cover portrait, vertical 2:3 ratio. Cinematic period-drama styling, refined and restrained. Warm chiaroscuro, deep mahogany and cream tones, a single warm lamp on the left. One single female subject in the room.

COMPOSITION — THE CAMERA IS BEHIND HER: A glamorous woman sits on a low stool at an antique vanity, her back to the camera, seen from behind and slightly above. The center of the frame is the back of a structured ivory corset with steel boning — worn on her body and fully laced up the spine, the crossed laces and the boning channels clearly visible, covering her from the shoulder blades down over the hips. Only her shoulders, upper back and arms fall outside the garment. Her caramel hair is swept forward over one shoulder to leave the lacing clear.

HER FACE COMES BACK IN THE MIRROR: the vanity mirror directly in front of her returns her face to the camera, frontal and sharp. It is in this reflection that the makeup reads as deliberately half-finished, and the asymmetry should be obvious at a glance: one eye fully made up with a sharp black liner flick and heavy false lashes, the other entirely undone — clean skin, no liner, no shadow, no mascara. Dark red lipstick, lips softly parted, an expression caught between resolve and apprehension. The mirror shows her and nobody else.

THE OTHER PERSON: a pair of elegant feminine forearms and hands enters the frame from the left, gripping the corset laces at her spine and drawing them tight. No face, no head, no torso, no second body — only the arms and the hands.

EDGES: left — a man's dark suit jacket over the back of a chair, a plain men's wristwatch lying face-down on the seat; right — a small lilac candle jar with a completely blank label, sheer stockings spilling over the edge of the vanity, one black stiletto tipped on its side on the parquet floor.

No text anywhere in the image: no title, no lettering, no watermark, no writing on the candle jar or any object — every label blank. Leave the top 25% as calm dark negative space for typography to be added later.

Mood: a transformation in progress — formal, quiet, cinematic, watched by the one being made. Photo-realistic, high-fashion editorial, 8k.
```

**Tipografía (componer después, no pedírsela a la IA):** título `De Esteban a Secretaria` en serif dorada arriba, filete fino debajo, `Capítulo 1 · La Semana` en cursiva menor, y `ANAÏS BELLAND` en small-caps al pie.

**Si igual la quiere con texto renderizado**, reemplazar el bloque `NO TEXT ANYWHERE` por una sola línea corta — mientras menos letras, menos lotería:
`TYPOGRAPHY: at the top, elegant deep-gold serif, one single line, large and clean: "De Esteban a Secretaria". Nothing else written anywhere in the image; every object label blank.`
…y revisar letra por letra antes de subirla.

> 🗑️ **La v1 y la v2 fueron BORRADAS de este archivo, a propósito.** La Ama volvió a generar con la v1 porque estaba archivada aquí abajo, a la vista y copiable — un prompt malo guardado donde se puede copiar **se va a copiar**. Queda el registro de qué fallaron; no queda el texto.

---

### Capítulo 2 — La verga que coge a Valeria

```
Book cover, portrait vertical (2:3 ratio). Editorial book cover, sensual and tension-saturated. High-contrast single overhead pendant light, deep shadows.

FIGURE: A glamorous, alluring woman stands at a heavy open door, back partially to camera, face turning in sharp profile — cat-eye makeup immaculate, dark burdeos lips, pearl earring, caramel hair swept back and pinned. Her black pencil skirt is tight against her hips and thighs; her silk blouse is slightly disheveled at the collar. Her posture is taut, aware — back straight, heels (black stilettos) pressing into the floor, one hand gripping the doorframe. Her expression: caught between desire and knowledge.

UPPER FRAME: A tall man's dark silhouette fills the open doorway above her — broad-shouldered, face in shadow, gaze directed downward at her body. His presence dominates the upper half of the image.

LOWER FRAME EDGE: At bottom left, barely in frame — a woman's hand holding a ceramic coffee cup, dark nail polish, the edge of burgundy lips in shadow. Watching.

TYPOGRAPHY (rendered in image): At the top, elegant serif in warm cream or deep gold, legible at thumbnail size: "De Esteban a Secretaria — Capítulo 2". A thin gold accent rule immediately below the main title, left-aligned. Smaller italic below the rule: "La verga que coge a Valeria". At the very bottom, small-caps in warm gold: "ANAÏS BELLAND".

Mood: arrival, desire, the moment of discovery, the triangle closing around her. Luxurious executive loft, caoba paneling, single pendant overhead. Photo-realistic, hyper-polished editorial, 8k.
```

---
---

# 🎞️ BANNERS DE CAPÍTULO (1280 × 720 · generar en 16:9 · recortables a 1200 × 400)

> Van como *header image* al inicio de cada parte en Wattpad. Máx 20 imágenes por parte, < 10 MB, JPG/PNG.
> La escena se elige por su **forma horizontal**, no por su calor: la más caliente del capítulo casi nunca es publicable en imagen.

## Capítulo 1 — La Semana

> Escena elegida: **el tocador**. El ancho del cuadro cuenta el tránsito — a la izquierda lo que Esteban deja, al centro la transformación en curso, a la derecha lo que Estefanía va a ser.

```
Wide cinematic banner, horizontal 16:9, letterbox composition. Cinematic editorial chapter header. A Santiago apartment bedroom at dusk, warm amber vanity light pooling in the center of the frame, the edges falling into deep caoba shadow.

CENTER: A person sits on a low stool at a vintage vanity, seen in three-quarter view. THEY ARE WEARING a steel-boned ivory corset — worn on the body, closed, opaque, fully laced — covering the torso completely from just below the armpits down over the hips; only the shoulders, collarbone and arms are bare above it. The face is caught mid-transformation, and the asymmetry must be obvious: the LEFT eye is finished with a sharp cat-eye and heavy lashes, the RIGHT eye is completely undone — no liner, no shadow, bare skin, slightly wide. Dark red lips, parted. Caramel hair loose and half-styled, one strand across the cheek. The hands rest on the thighs, palms up, still. From behind, only a pair of elegant feminine FOREARMS AND HANDS enters the frame — no face, no head, no torso, no second body — pulling the corset laces tight with an unhurried grip. The seated figure's spine straightens under the pull.

LEFT THIRD (what is being left): a man's dark suit jacket crumpled over a chair, a plain wristwatch face-down, a pair of worn men's sneakers, an unpaid bill on the floor. Cold blue light.

RIGHT THIRD (what is being made): a lilac-labeled wax pot, nude stockings pooled on the carpet, a black stiletto tipped on its side, a wig head on the dresser. Warm amber light.

TYPOGRAPHY (rendered in image, lower center over the dark carpet): elegant serif in deep gold, small: "Capítulo 1 — La Semana". A thin warm-gold rule beneath. Bottom right corner, tiny small-caps warm gold: "LA VOÛTE D'ANAÏS".

COMPOSITION NOTE: keep the figures and the typography inside the central horizontal band; leave the top and bottom 20% as empty ceiling and carpet so the frame crops cleanly to 3:1.

Photo-realistic, cinematic, warm editorial color grade, 8k.
```

**VARIANTE SIN TEXTO** — `No text, no lettering, no title, no watermark anywhere in the image. Keep the lower center clean for typography to be added later.`

---

## Capítulo 2 — La verga que coge a Valeria

> Escena elegida: **la recepción del loft**. Ella en el escritorio, la puerta cerrada de Gabriel al otro extremo del cuadro, y el pasillo entero de distancia entre las dos cosas. La envidia sucia se ve en la distancia, no en la piel.

```
Wide cinematic banner, horizontal 16:9, letterbox composition. Cinematic editorial chapter header. A luxury executive loft in Santiago, night. Caoba wall paneling running the full width of the frame, a single pendant lamp, floor-to-ceiling glass on the left with city lights. High contrast, deep shadow, one warm pool of light.

LEFT THIRD: A glamorous woman sits at a minimal reception desk, in profile, spine straight, knees together and angled, black pencil skirt, ivory silk blouse, black stilettos with the heels pressed into the floor. Immaculate cat-eye makeup, dark burgundy lips, caramel hair pinned back, a pearl earring. Her hands rest on the desk beside a closed laptop. She is not working. Her face is turned down the length of the room, and her expression is want with the shame still attached to it.

CENTER: a long empty stretch of polished floor. This emptiness is most of the image.

RIGHT THIRD: a heavy closed office door in cedar, a strip of warm light under it. Beside the door, on a side table: two glasses, one with lipstick on the rim.

FOREGROUND, BOTTOM LEFT CORNER (barely in frame, sharp): a woman's hand holding a ceramic coffee cup, dark nail polish. Someone else is in the room, watching, and has been the whole time.

TYPOGRAPHY (rendered in image, center of the frame over the empty floor): elegant serif in deep gold, small: "Capítulo 2 — La verga que coge a Valeria". A thin warm-gold rule beneath. Bottom right corner, tiny small-caps warm gold: "LA VOÛTE D'ANAÏS".

COMPOSITION NOTE: keep the desk, the door and the typography inside the central horizontal band; the top and bottom 20% must be empty ceiling and floor for a 3:1 crop.

Photo-realistic, cinematic, moody executive color grade, 8k.
```

**VARIANTE SIN TEXTO** — `No text, no lettering, no title, no watermark anywhere in the image. Keep the central floor area clean and dark for typography to be added later.`

---
---

# 🏷️ TAGS PARA WATTPAD

> ⚠️ Los tags de arriba (con `#`, por capítulo) son de **Tumblr/RRSS**. En Wattpad los tags son **de la historia**, máx **25**, y los puntos/guiones/espacios rompen el tag.

**25/25 — «De Esteban a Secretaria»:**

```
feminizacion
feminization
sissy
mtf
tgtf
genderbender
transformacion
crossdressing
hormonas
femdom
dominacion
sumision
humillacion
cuckold
secretaria
oficina
erotica
eroticaadulta
maduro
identidad
deudas
matrimonio
chile
lavoutedanais
anaisbelland
```

