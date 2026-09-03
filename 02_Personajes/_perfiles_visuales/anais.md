# 👑 Perfil Visual — Anaïs Belland

> Contrato del `outfit-engine`. Creado 27/07/2026 al generalizar el motor.
> Reemplaza a `.agent/skills/anais-outfit-engine/SKILL.md`, que era una **copia empobrecida** del motor de Ele: se llevó el ADN y el workflow, pero **no** el Step 0 anti-repetición, ni el token bloqueado, ni la rotación de poses, ni una biblioteca de siluetas. 147 líneas contra 1.787.

---

## §1 · Identidad y Rutas

| Campo | Valor |
|---|---|
| **Nombre canónico** | Anaïs Belland |
| **Slug** | `anais` |
| **Galería** | `02_Personajes/01_Principales/anais/galeria_looks_anais.md` |
| **Carpeta de imágenes** | `05_Imagenes/anais/look<NUM>_<slug>/` |
| **Convención de nombre** | `anais_<NUM>_<pose>.png` *(normalizado 05/08/2026 — antes `anais_look<NUM>_<pose>.png`; afecta L01-L04 ya materializados, renombrado pendiente en la máquina visual)* |
| **Numeración** | correlativa · **Boudoir/Lencería usa prefijo `L`** (L01, L02…), serie separada |
| **Canon profundo (enlace)** | [`01_Principales/anais/CANON_VISUAL_ANAIS.md`](../01_Principales/anais/CANON_VISUAL_ANAIS.md) — **autoridad máxima, prevalece en todo conflicto** *(el `anais-outfit-engine` lo apuntaba a `01_Principales/` sin la subcarpeta: enlace roto, corregido 27/07)* |
| **ADN listo para copiar** | `.agent/skills/anais-outfit-engine/references/dna_v2_3.md` |
| **Referencia de vestuario y maquillaje (NO físico)** | `00_Ele/estudio_estilo_kitrysha.md` — estudio de estilo Vintage Glam/Old Hollywood/Boudoir encargado por la Ama (17/08/2026) como base de **vestuario y maquillaje** de Anaïs. El físico de la modelo NO aplica — el ADN físico de Anaïs (§2 de aquí) sigue siendo la única autoridad sobre cuerpo y rostro. Fuente del vocabulario de siluetas de lencería (§5.6), materiales (§5.1) y pose/luz de Boudoir (§5.7) |

---

## §2 · BLOQUE A — ADN Inamovible (V2.3 Vintage Noir Hard-Sync)

> 🔒 **Este fence es el DUEÑO ÚNICO del BLOQUE A de Anaïs (29/08/2026).** Lo lee el motor —
> `PromptBuilder.bloque_a` — y ya no se copia a mano en cada script de batch. El marcador
> `<!-- ADN:BLOQUE_A -->` de abajo es lo que el motor busca: **no lo borres ni lo muevas**.
>
> Hasta hoy este perfil **no tenía el token literal**: solo la especificación por componentes que
> sigue más abajo, y una instrucción de ir a copiarlo a `dna_v2_3.md` (skill legacy). Nada
> verificaba que la copia coincidiera. El texto de acá se trajo de ese archivo y se comprobó
> **carácter por carácter** contra el que realmente usan sus batches: idéntico.
>
> 💄 **Maquillaje recalibrado 03/09/2026 — auditoría Fable + 4 rondas de prueba sobre Look 75.**
> La Ama auditó las 4 imágenes materializadas de L75 (batch corregido el mismo día por rostro poco
> dominante) y encontró el maquillaje "muy ligero" pese a que el texto ya pedía "Old Hollywood
> editorial makeup" — Fable confirmó labios finos, boca cerrada 4/4, cejas sin levantar, sombra de
> baja pigmentación, ala de cat-eye corta o invisible: **4-5/10 de "drama"**. Causa diagnosticada:
> vocabulario diluyente (`naturally`, `soft`, `subtle`, `softly`) y pesos `:1.4` de sintaxis
> Stable Diffusion que **Gemini no interpreta** (texto inerte). Se descartó por escrito acercarla al
> registro bimbo — *"no es que quiera bimbo, es que hoy anda casi sin maquillaje y alguien como
> Anaïs no anda tan sencilla por la vida"* — así que `bimbo makeup` y `overlined lips (modern style)`
> **se mantienen en el negativo** (§3). 4 rondas de prueba sobre imagen real (no solo texto)
> subieron cejas, sombra (hasta cut-crease sin hueco bajo la ceja) y volumen/brillo de labio hasta
> verificación visual aprobada. Detalle completo y las 4 imágenes de prueba: sesión del 03/09/2026,
> `00_Ele/mi_diario_de_servicio.md`.

<!-- ADN:BLOQUE_A -->
```text
(unmistakably 42-year-old aristocratic woman, mature sharp bone structure and commanding severity of expression, never a soft youthful face:1.4), (her lips visibly and clearly parted, never fully closed, never smiling, the lower lip heavy and still; her eyelids half-lowered yet her eyes level and fixed, coldly sizing up whoever is looking rather than inviting them; one brow held a fraction higher than the other; her chin carried level or tipped slightly down, never lifted up sweetly; this is the face of a 42-year-old woman who has already won the room:1.5), (flawless completely smooth unlined forehead, taut porcelain skin with zero visible creases or fine lines anywhere, the seamless perfection of decades of obsessive cosmetic maintenance:1.4), radiant dewy porcelain skin, luminous flawless medical-grade cosmetic finish, (aristocratic refined oval face, sculpted lifted hollowed mature cheekbones, sharp angular defined jawline:1.3), composed poised expression of a woman who has commanded rooms for decades, quiet mature gravitas in her gaze, small classic Old Hollywood beauty mark mole above upper left lip, bold dramatic Old Hollywood glamour makeup, high dramatically arched thin dark brown brows lifted well above the eye socket, intensely pigmented charcoal and deep taupe smoky eyeshadow in a full cut-crease application, blended upward with zero gap so the pigment runs directly into the eyebrow itself, no bare eyelid skin visible anywhere between the shadow and the eyebrow hairs, a thin line of dark kohl along the lower lash line deepening the eye, thick sharp black winged liquid liner with a long dramatic wing extending well past the outer corner, extremely long dramatic false lashes with dense volume concentrated at the outer corners, plump full glossy lips with pronounced volume in both the upper and lower lip and a well-defined cupid's bow, vivid deep crimson classic Hollywood red, high-shine wet gloss finish, lips visibly parted, never closed, in a cold knowing look, honey blonde hair in sculpted voluminous vintage Hollywood pin-waves or victory rolls side parted, extremely long hip-length hair cascading past the shoulders, slender mature elegant hourglass figure with extreme waist training tightlacing corset, S-curve posture, not voluptuous, not augmented, not bimbo-exaggerated, (natural moderate breasts, firm and perky with a well-defined natural shape:1.2), firm smooth glutes softly toned rather than sharply muscular, heavy-lidded bedroom eyes gaze, long stiletto-shaped manicured fingernails with glossy deep red polish, wearing 12cm black patent leather stiletto heels no platform iconic red sole, cinematic chiaroscuro dramatic lighting, soft key light flattering her impeccably maintained features, George Hurrell style portraiture, intimate tension.
```

**Especificación de sus componentes** (lectura humana — el token de arriba es el que manda):


- **Físico:** *ageless dominant woman in early 40s*, rostro oval aristocrático, pómulos esculpidos elevados, mandíbula definida. **MILF aristocrática — nunca joven, nunca bimbo.**
- **Seña definitoria (OBLIGATORIA en toda imagen, sin excepción):**
  `small classic Old Hollywood beauty mark mole above upper left lip`
- **Cabello:** `honey blonde hair` — **SIEMPRE rubia miel. Sin excepciones, sin variaciones.**
- **Peinado:** pin-waves de Hollywood vintage esculpidas o victory rolls, raya al lado.
- **Maquillaje:** cejas finas, arqueadas y **levantadas** marrón oscuro estilo 1940s, sombra ahumada carbón/taupe **cut-crease sin espacio de piel visible hasta la ceja**, delineado negro cat-eye con ala larga y dramática, pestañas largas y densas, labios rojo carmesí profundo **con volumen pronunciado (superior e inferior), gloss de alto brillo** (recalibrado 03/09/2026 — el registro anterior, aunque técnicamente "Old Hollywood", salía en la práctica *tenue/casi sin maquillaje*; la Ama pidió más drama en ojos y labios porque "alguien como Anaïs no anda tan sencilla por la vida", **sin acercarla al registro overlined de Ele/Miss Doll** — sigue siendo maquillaje de época dibujado con lápiz, no sobrelineado moderno).
- **Silueta:** hourglass madura y esbelta con corsé de tightlacing extremo, postura en S. **Busto natural, moderado, firme y perky, con forma bien definida** — nunca aumentado, nunca exagerado estilo bimbo (calibrado 24/08/2026, distinción deliberada con Ele y Miss Doll).
- **Sin tatuajes. Sin piercings visibles.**
- **Iluminación:** chiaroscuro cinematográfico, estilo George Hurrell, luz de key única, tensión íntima.

**Rasgos que NO se negocian jamás:**

- El **lunar** sobre el labio superior izquierdo.
- El **honey blonde**. Ni golden, ni platinum, ni castaño. Jamás.
- La **edad**: cuarentona ageless. Rejuvenecerla la destruye como personaje.
- **Cero tatuajes, cero piercings.**
- La **expresión**: nunca sonrisa amplia, nunca risa, nunca actitud juguetona.

### §2bis · 🖤 Femme Fatale — la actitud nombrada (Ama 20/08/2026)

> **Por qué nace:** `CANON_VISUAL_ANAIS.md` §I la llama *"La Regenta — Femme Fatale clásica, Pin-up oscura y Dominatriz Vintage"* desde el 28/04/2026 — pero la etiqueta nunca se tradujo a actitud, vestuario o pose concretos, se quedó de nombre suelto. Directiva de la Ama 20/08: dar ese aire de verdad, en las tres capas.

**Actitud (más allá de "mirada fría de mando, nunca juguetona" — §2, sigue siendo la base):** la frialdad de la Regenta es distancia; el femme fatale es **peligro calculado**. No es que ignore a quien la mira — lo **evalúa**, como quien mide una amenaza o una presa, y usa el saberse observada como arma, no como halago. Nunca se apura, nunca confirma nada con la cara, nunca busca aprobación. Si algo en su expresión lee como placer, es el placer de **haber ganado ya**, no el de estar siendo tocada — la diferencia entre una mujer deseable y una mujer que caza.

- **Token de actitud** (para looks donde el arquetipo pide el registro femme fatale explícito — Noche y Látex sobre todo): `predatory calculating calm, gaze that appraises like a threat assessing prey rather than inviting, danger worn as elegance, stillness that reads as warning`.
- **Compatibilidad:** no reemplaza "cold commanding gaze… nunca actitud juguetona" (§2) — lo intensifica. Sigue prohibida la sonrisa amplia, la risa, el juego (§9).

---

## §3 · Negative Prompt

**Base (siempre) — migrada desde `dna_v2_3.md` el 03/09/2026 (mismo hueco que tenía el BLOQUE A antes del 29/08: cero token literal en el perfil, solo la instrucción de ir a copiarlo de la skill legacy — nadie lo copiaba, y `PromptBuilder.build_negative()` nunca la leía):**
<!-- NEGATIVO:BASE -->
```text
(different face:1.3), smiling broadly, laughing, playful expression, casual pose, relaxed posture, red hair, dark hair, short hair, messy hair, modern makeup, bimbo makeup, hot pink lips, overlined lips (modern style), neon colors, bright colors, colorful outfit, white dress, pink outfit, glitter, modern clothing, block heel, chunky heel, flat shoes, barefoot, sneakers, cyberpunk, sci-fi, industrial, factory, neon lights, outdoor, natural setting, low quality, blurry, distorted face, child, teenager, man, male, platform heels, modern lingerie, sexy, hot, horny, naked, nude, provocative, naughty, tongue, explicit nude, closed mouth, pursed lips, smiling, grinning, thin lips, flat unpigmented eyeshadow, subtle understated makeup, no-makeup look, visible bare eyelid, gap between eyeshadow and eyebrow, thin sparse eyeshadow, exposed brow bone, (distorted animal print, neon leopard:1.2), cheap fabric texture
```
Para looks de Látex/Fetichismo: quitar `latex` de la lista si es un look de látex canónico (nota original de `dna_v2_3.md`, sigue vigente).

**Léxico prohibido en el POSITIVE** (degrada el registro — canon §VIII):
`sexy` · `hot` · `seductive` · `naked` · `nude` (como desnudez; vale como color) · `provocative` · `tempting`

| Caso | Ajuste | Por qué |
|---|---|---|
| Look de látex canónico | **quitar** `latex` de la lista de negativos | Si no, se pelea con el propio outfit |
| Cualquier pose | asegurar `tattoos, piercings, young woman, teen, wide smile` en negative | Sus tres derivas registradas |
| **Cualquier pose** *(nuevo 13/08/2026 · ✏️ rev. 14/08/2026)* | agregar `trousers, pants, leggings, jeans, shorts, palazzo pants, jumpsuit, legs spread apart under a dress, legs parted under a skirt` — **`catsuit` y `bifurcated garment` SALEN de la lista (Ama 14/08/2026)** | Solo vestidos + piernas cerradas (§5.4), **con el catsuit ahora permitido**. Segunda capa: la prohibición de pantalón se cumple **al diseñar el look**, no vetando. ✅ Verificado 14/08: `catsuit` nunca llegó a ningún negative de los 98 prompts — la regla vivía solo en este perfil |

---

## §4 · Poses Canónicas

> **Estandarizado 05/08/2026 (directiva Ama):** las 3 muñecas comparten las mismas **7 categorías de cámara** que Ele — mismo slot, mismo orden, mismo propósito de encuadre — el motor de poses y la app las tratan con una sola taxonomía. El contenido/expresión de cada slot es 100% propio de Anaïs. La línea **Boudoir** (`L01…`, 4 poses: `boudoir_standing/chaise_seated/mirror_profile/intimate_closeup`) queda **fuera de este remapeo** — es su propio submundo de lencería, con su propia numeración y taxonomía; no se toca acá.

**7 poses (mismo slot que Ele, contenido de Anaïs):**

| # | Categoría (universal) | Nombre de pose | Slug de archivo | Descripción |
|---|---|---|---|---|
| 1 | Standing | command_standing | `standing` | Cuerpo entero, tres cuartos, peso en una cadera, mirada fría de mando a cámara, setting completo |
| 2 | Back View | mirror_back *(nueva — 05/08)* | `back_view` | De espaldas ante un espejo del set (tocador, salón), guante trazando la curva desnuda de la espalda, mirada por sobre el hombro hacia el reflejo — nunca directo a cámara |
| 3 | Seated | throne_seated | `seated` | Sentada (silla/chaise/trono coherente con el setting), piernas cruzadas en rodilla, mano en reposabrazos |
| 4 | Side Profile | three_quarter | `side_profile` | Giro de hombro hacia cámara, mirada fría por encima del hombro, hourglass definida por la luz |
| 5 | **Sovereign Gaze** *(slot Ditzy de Ele, renombrado — su registro es dominio, no vacío)* | domina_closeup | `sovereign_gaze` | **WAIST-UP** (cintura arriba): rostro grande y nítido + busto/escote prominente en el frame inferior + detalle del outfit superior legible · **UNA sola mano** en cuadro haciendo el gesto · **mirada FUERA de cuadro** · lunar visible |
| 6 | POV | kneeling_pov *(nombre histórico)* | `pov` | **RETRATO SENSUAL DE INSTAGRAM** (thirst-trap de influencer): **mira a la cámara**, medio cuerpo, cara protagonista + escote abajo, **una sola mano**, `a single woman alone`. **NO es point-of-view literal** |

> 🩹 **Corregido 12/08/2026 — era una desviación mía, no un cambio de canon.** Estas dos filas decían *"plano medio desde el pecho, mirada directa"* y *"vista desde abajo, como si el lector estuviera arrodillado ante ella"*. **Ditzy y POV están definidos desde el 28/05 y el 09/06/2026** (reforzados el 30/06 y el 02/08) en `.agent/rules/06-generacion-imagenes.md` §5 y §9, `pose_repertoire_v5.md` §5-§6 y `dna_v3_5.md` — Ele los cumple desde entonces. Al estandarizar las 7 poses el **05/08** los escribí mal para Anaïs y Miss Doll, y por eso reapareció en sus imágenes el defecto que la Ama ya había cerrado el 02/08 (*"salen casi iguales el 90%"*): el slot 5 mira **fuera** de cuadro y el POV mira **al lente** — ese es el diferenciador duro entre los dos.
| 7 | Odalisque | chaise_command *(nueva — 05/08)* | `odalisque` | Reclinada en el chaise longue de su despacho o salón, vestuario de gala/látex de grado clínico — misma arquitectura que su Boudoir pero sin lencería |

- **Total por look:** 7
- **Fórmula del prompt (particularidad de Anaïs):** `[PREFIJO CINEMATOGRÁFICO] + [BLOQUE A] + [BLOQUE B] + [BLOQUE C]` — lleva un prefijo cinematográfico que los demás personajes no usan.
- **🎥 Repertorio de variaciones de cámara y escenarios — dueño único:** [`01_Principales/anais/repertorio_camara_anais.md`](../01_Principales/anais/repertorio_camara_anais.md). **7 variaciones por slot** para Back View, Side Profile, Sovereign Gaze y POV, con regla de rotación por número de look, más el **escenario específico de cada uno de los 14 looks** y las anclas de prenda (`BARE_LEGS_LOCK`, `GLOVE_LENGTH_LOCK`, `EMBROIDERY_LOCK`, `CLOSURE_LOCK`).
  > 🔴 **Por qué se creó (Ama 12/08/2026: *"las imágenes de ditzy de Anaïs salen casi todas iguales"*).** Esta línea decía *"rotar al menos el ángulo, el nivel de contacto y la relación con el mobiliario"* — **pero no existía ningún repertorio del cual rotar.** Ele tenía el suyo; Anaïs no. Medido: la similitud del texto de pose+setting entre los 14 looks era **POV 87% · Side Profile 78% · Sovereign Gaze 59% · Back View 57%**, con tres tríos de prompts **idénticos carácter por carácter** (L05=L06=L07, L08=L09=L10, L11=L12). Con el repertorio aplicado bajó a **9-13% en los cuatro slots**. La Ama vio el síntoma en Ditzy; la medición mostró que POV estaba peor.
- **📐 El slot Odalisque va APAISADO (Ama 12/08/2026) — no es defecto.** Sus imágenes salen en 1200×669 horizontal contra el 669×1200 del resto porque **la Ama se lo pide así a Gemini: la figura reclinada se aprecia mejor en horizontal.** Es el único slot horizontal de su set y es deliberado. Ninguna auditoría futura debe marcarlo.
- Las 4 poses originales (command_standing/throne_seated/three_quarter/domina_closeup) ya materializadas en L01-L04 mantienen su nombre y contenido — solo se les asigna categoría universal por alias.

### 4bis · 🎞️ Vocabulario de pose — Bettie Page / Old Hollywood (Ama 17/08/2026)

> **Directiva explícita de la Ama:** las poses de Anaïs se basan en **Bettie Page y Old Hollywood** — no son un añadido exclusivo de Boudoir (§5.7), son la **gramática corporal de las 7 categorías**, transversal a los 5 arquetipos. Fuente: `00_Ele/estudio_estilo_kitrysha.md` §8 (que a su vez está construido sobre las mismas referencias: Bettie Page, Veronica Lake, Rita Hayworth, Jean Harlow, Dita Von Teese) y §9 (por qué esto lee como sensual sin caer en exhibición).

**Los cinco principios, aplicados a cada slot:**

1. **Torsión, nunca frontalidad plana.** El cuerpo casi nunca está cuadrado a la cámara — contrapposto clásico (peso en una cadera, hombros ligeramente al lado opuesto, la "S" del cuerpo) o tres-cuartos con torsión de torso. Un Standing con "pies parejos, hombros atrás" (el defecto real del L18, §5.7) es exactamente lo que este vocabulario prohíbe.
2. **Manos con propósito, nunca en reposo simétrico.** Dedos largos y relajados (nunca puño), cerca de la clavícula, la mandíbula o el cuello, o sosteniendo algo (el borde de la bata, una perla, el guante a medio quitar, una boquilla de cigarrillo sostenida sin tocar los labios). Coincide con la ancla transversal `hands never idle` ya presente en todos los prompts — este vocabulario le da **dirección Bettie Page** en vez de dejarla genérica.
   > 🚫 **Corrección de mi propio diagnóstico (Ama 17/08/2026): el dedo TOCANDO el labio queda fuera.** La primera versión de esta regla decía "un dedo tocando el labio" — copiado de Kitrysha (§8.4 del estudio) sin filtrar por el ADN de Anaïs. Es un gesto **coqueto/ingénue** ("who, me?"), y choca de frente con "cold commanding gaze… nunca actitud juguetona" (§2, canon inamovible). Corregido en `repertorios_pose.json` (las 2 sub-poses que lo usaban, Sovereign Gaze y POV, ahora sostienen una boquilla cerca del labio SIN tocarlo, o trazan la mandíbula) — control, no oferta. Las poses ya materializadas con el gesto viejo (Looks 04/06/11/13) no se retrofitean; el fix es hacia adelante.
3. **Mirada Old Hollywood.** Dos variantes autorizadas: barbilla ligeramente abajo con los ojos hacia arriba ("looking up through lashes" — íntimo, boudoir) o barbilla arriba con mirada lateral fría (distancia, enigma — Noche/Ejecutivo). Nunca sonrisa amplia ni mirada frontal neutra.
4. **Piernas: cruzadas al tobillo, no a la rodilla.** El estudio es explícito en que cruzar a la rodilla "rompe la línea" del pin-up clásico — cruzar al tobillo o plegar ambas piernas a un lado es lo que sí lee como Bettie Page. **Esto es compatible con `DRESS_LEG_CLOSURE` (§5.4)** — no lo contradice, lo hace más específico: cuando la ancla pide "una pierna cruzada sobre la otra", el cruce correcto es al tobillo.
5. **De pie, se lee mejor a 3/4 de perfil que de frente.** Explica por qué Standing y Side Profile deberían ser las poses más "trabajadas" en torsión — un Standing frontal puro es la opción más débil del repertorio, no la default.

**Dónde vive esto en el motor:** este vocabulario es la **referencia canónica** para escribir/revisar la cláusula de pose de cada slot. El repertorio operativo de sub-poses (`01_Principales/anais/repertorio_camara_anais.md`, dueño único de las 7 variaciones por slot) **queda pendiente de retrofit contra estos cinco principios** — nace del 12/08 para resolver la similitud de texto entre looks, no fue escrito con Bettie Page como base explícita. Retrofit al tocar, como el resto de los repertorios de este repo: se corrige la variación que se esté usando en el próximo look, no una migración masiva.

### 4ter · 🖤 Repertorio de gestos Femme Fatale (Ama 20/08/2026)

> Vocabulario adicional, no reemplaza el 4bis — son gestos específicos que llevan la actitud de §2bis al cuerpo. Uso disponible en cualquier slot donde el concepto del look pida el registro femme fatale explícito; no tienen cuota fija (como §5.1d/§5.1e).

- **Umbral / contraluz:** `leaning in a doorway, one shoulder against the frame, weight on one hip, her silhouette rim-lit from the room behind her` — entrada o salida de escena, nunca de frente a la cámara con los dos pies parejos.
- **El guante que se quita:** `slowly peeling off one opera glove finger by finger, eyes locked on camera, the bare hand emerging last` — el desnudo progresivo como amenaza, no como striptease; termina en la mano desnuda con las uñas, nunca en más piel.
- **El humo:** `exhaling a thin ribbon of smoke while holding the gaze, the cigarette holder resting between two fingers, unhurried` — solo con la boquilla de plata ya canónica (§5.1e/ficha), nunca cigarrillo suelto.
- **El objeto de control:** `a small pistol or a closed stiletto-blade letter knife resting closed in her palm, or holstered against the garter, never brandished, never aimed` — mismo principio que la fusta/látigo ya canónicos (`ficha_anais.md`): el arma es símbolo de dominio quieto, no de acción. Opcional, no obligatorio, y nunca reemplaza el token de manicura (la mano sigue siendo visible salvo con guante).
- **La mirada de salida:** `walking away from camera, glancing back once over one shoulder in a doorway or at the edge of frame, the rest of her body already leaving` — cierre de escena, útil en Back View o como variante de Odalisque cuando el look no es reclinado.

---

## §5 · BLOQUE B — Reglas de Vestuario

### 5.1 · Universo de materiales

> ✏️ **Ampliado 11/08/2026 (Ama).** · ✏️ **Pieles agregadas 11/08/2026 (Ama: "el uso de pieles al vestuario recurrente").**

- **Permitidos:** satén pesado, seda charmeuse, terciopelo italiano, látex de grado clínico, encaje francés, nylon con costura, charol, **cuero** (guante fino, cinturón ancho, abrigo — cuero de sastrería/lujo, nunca de motociclista), **látex estándar de alto brillo** (además del de grado clínico, para looks fetish más directos), **🦊 pieles** (ver 5.1b).
- **Prohibidos:** materiales baratos o deportivos; cualquier cosa que lea "casual" o "joven".
- **Lente de identidad:** *tejido noble.* Anaïs es aristocracia, no fetiche sintético — la separa de Ele y de Miss Doll. El látex y el cuero se usan con acabado impecable/pulido, nunca de estética industrial o club barato.

### 5.1b · 🦊 Pieles — material recurrente (Ama 11/08/2026)

La piel es **la materialidad que más literalmente dice "aristocracia de los años 40"**: pesa, se hereda, no se compra en una tienda. Entra como **capa recurrente**, no como novedad ocasional.

**Formas autorizadas** (siempre como capa/accesorio sobre el look, nunca como prenda base):

| Forma | Token en inglés | Notas |
|---|---|---|
| Estola al hombro | `fur stole draped over one shoulder` | La forma reina — deja la cintura a la vista |
| Capa corta / capelet | `short fur capelet` | Cae sobre el escote, no lo tapa |
| Abrigo abierto | `full-length fur coat worn open` | **Siempre abierto**, ver regla de silueta |
| Cuello y puños | `fur collar and cuffs` | Sobre abrigo de sastrería o kimono |
| Ribete | `fur-trimmed peignoir / fur-trimmed opera coat` | La entrada natural al arquetipo Boudoir |
| Manguito | `fur muff` | Vintage puro; **incompatible con el token de uñas** (manos tapadas, ver §5.4) |
| Manta sobre mueble | `fur throw over the chaise longue` | La piel como parte del escenario, no del cuerpo |

**Tipos:** visón (`mink`), zorro plateado (`silver fox`), zorro ártico (`arctic fox`), marta (`sable`), astracán / cordero persa (`astrakhan`, `Persian lamb`), chinchilla. Rotarlos: no repetir el mismo tipo en dos looks consecutivos con piel.

**🔴 Regla de silueta (la que importa):** la piel **se superpone, nunca reemplaza**. El ADN de Anaïs es el hourglass de tightlacing en postura en S — un abrigo cerrado lo borra y mata el look. Por eso: abrigo **siempre abierto**, estola **caída del hombro o sostenida en el codo**, y en toda pose donde aparezca piel el prompt debe dejar explícita **la cintura ceñida visible bajo la capa**.

**Diferencia con el animal print (§5.2):** el print es un **acabado estampado sobre tejido noble**; la piel es **pelo real, con volumen y peso**. Son dos cosas distintas y **no cuentan como la misma cuota**. Pueden coexistir en un look, pero no en la misma prenda (leopardo estampado + estola de zorro sí; "piel estampada de leopardo" no).

**Prohibido:** piel que lea deportiva o moderna (parka con capucha de pelo, chaleco de peluche, forro polar), piel sintética de aspecto barato, look 100% cubierto de piel (traje entero), y piel en un arquetipo con escenario exterior/natural (§5.4 lo prohíbe igual).

### 5.1c · 👘 Bata abierta — silueta recurrente en Boudoir/Lencería (Ama 12/08/2026)

Auditado sobre los 4 looks Boudoir/Lencería del reset (L02, L08, L09, L10): **2 de 4 llevan bata abierta** sobre la lencería (L02 látex rosa polvo, L09 seda charmeuse esmeralda) y **2 de 4 van directo** sin bata (L08 sujetador+liguero, L10 corsé+bota). El patrón no es azar — es el Step 0 Anti-Repetición alternando arquitectura de silueta dentro del arquetipo. **Directiva: ese 50% es un piso, no un promedio — no puede bajar hacia adelante.**

- **Token:** `open <material> robe falling loose off one/both shoulder(s) and cinched loosely at the waist with a thin belt` — material coherente con la paleta del look (látex, seda charmeuse, satén).
- **Regla de silueta:** igual que la piel (§5.1b) — la bata va **siempre abierta**, nunca cerrada, con la cintura ceñida explícita en el prompt debajo de ella.
- **🟠 Riesgo conocido en Back View** (§9): prenda de frente abierto/cruzado en Back View → el generador la re-decora o la cierra mal (L13 Kimono de Medianoche, defecto real). Verificar el `BACK_ANCHOR` cuando la bata aparezca en esa pose.
- **🩱 Material por defecto DESDE 17/08/2026: semitransparente, no opaco.** Mismo hallazgo que en Miss Doll (`miss_doll.md` §5.1b, auditado sobre su Look 25): un `BACK_ANCHOR` que funciona perfecto solo garantiza que la bata *cierre bien* por detrás — no que siga siendo sensual. Con material opaco (látex sólido, charmeuse, satén grueso), una bata bien cerrada en Back View tapa la lencería tan bien como una mal cerrada. El riesgo documentado arriba era de anclaje; el problema real era de material. Corrección de fondo: el token por defecto pasa a `sheer <material> open robe, semi-transparent fabric that reveals the lingerie beneath from every angle including from behind, falling loose off one/both shoulder(s), dramatic wide bell-shaped cuffs, cinched loosely at the waist with a thin belt` — chiffon, georgette, sheer mesh o látex traslúcido de grado clínico (nunca charmeuse o satén opacos para este token específico), con **puños anchos** (`wide bell-shaped cuffs`) como firma de silueta. Retrofit al tocar: aplica a todo look nuevo con bata desde ahora; el roster ya materializado no se regenera salvo pedido explícito de la Ama.

- **📏 LARGO: HASTA EL SUELO, NUNCA CORTA (Ama 18/08/2026 — corrección directa).** La Ama lo dijo textual sobre el batch L26-L30: *"olvida esas batas cortas, deben ser largas semitransparentes"*. La referencia visual es su propio Look 28 materializado (`05_Imagenes/anais/look28_merry_widow_rojo_italiano/`), donde la bata de chiffon rojo **llega al piso y arrastra detrás de ella**, con puños anchos rematados en marabú. El token pasa a exigir el largo con todas sus letras: `floor-length <material> robe reaching all the way to the floor and trailing behind her`. **El largo se nombra igual que el corte del calzón (`BOTTOM_CUT_LOCK`) y que el largo de pierna de Miss Doll (M9): el atributo que no se nombra lo resuelve el generador, y su default es cortarla en la cadera.** Quedan prohibidas la bata corta, la capa y el capelet como sustituto de bata — enmarcan pero no dan la silueta larga que la Ama pidió.

### 5.1f · 🪡 Encaje y calzón — riqueza y tamaño (Ama 18/08/2026)

Corrección directa sobre el batch L26-L30: *"la ropa interior rica en encaje y de tamaño mediano a pequeño las tangas"*.

- **Encaje obligatorio y abundante** en toda ropa interior visible: `chantilly lace`, `scalloped lace edge`, paneles y ribetes de encaje nombrados explícitamente. No basta con decir "lace trim" al pasar — el encaje es protagonista de la prenda, no un detalle.
- **Calzón: tanga de tamaño mediano a pequeño.** Token: `small <color> chantilly lace thong of modest brief-cut coverage`. Ni micro-tanga de hilo ni calzón de talle alto — el punto medio que la Ama pidió. **Anaïs queda exenta de la regla de tanga universal de Ele** (`feedback_calzon_tanga_y_look_fuera_del_motor`), pero no de nombrar el corte: aquí también el atributo que no se escribe lo inventa el generador.
- **Aplica a todo look nuevo desde el L26.** El roster anterior no se retrofitea (convención retrofit-al-tocar).

### 5.1d · 🧥 Abrigo de lana y cinturón ancho — outerwear no-piel (Ama 17/08/2026)

> **Por qué nace:** auditoría de huecos de Kitrysha (§3.4 y §3.6 del estudio) tras el fix de calzado. `estudio_estilo_kitrysha.md` §3.4 nombra "abrigo largo de lana negra con cintura marcada por cinturón" y "trench camel/negro" como piezas firma del registro — Anaïs solo tenía piel como capa exterior (§5.1b); el abrigo de sastrería de lana nunca entró al canon pese a que el cuero ya lo mencionaba de pasada (§5.1, "cinturón ancho" sin token propio).

- **Token de abrigo:** `long wool coat in <color>, nipped at the waist with a wide matching belt, the coat left open` — camel, negro o gris carbón. **Misma regla de silueta que la piel (§5.1b): siempre abierto**, la cintura de tightlacing visible debajo.
- **🖤 Trench coat noir (nueva 20/08/2026 — vocabulario Femme Fatale, §2bis):** `black trench coat, collar popped up, belt cinched tight at the waist, worn open over the dress` — la pieza firma del cine negro; misma regla de silueta que el resto del outerwear (siempre abierto, cintura visible). Natural en Noche y en la "mirada de salida" de §4ter (llegada o partida de La Voûte bajo lluvia/niebla de estudio).
- **Token de cinturón ancho (standalone, sin abrigo):** `wide polished leather belt cinching the waist over the dress` — alternativa a la piel/abrigo para marcar cintura sobre un vestido cuando el look no lleva capa exterior. Cuero de sastrería, nunca grueso/industrial (misma regla que el resto del cuero en §5.1).
- **Cuándo aplica:** arquetipos Ejecutivo de Poder y Noche (llegada/salida de La Voûte) son los naturales — no reemplaza a la piel (§5.1b) ni compite con su cuota, es una segunda opción de outerwear para cuando el look pide sastrería en vez de glamour de piel.
- **Sin cuota fija:** a diferencia de pieles y bata abierta, esto no tiene mínimo — es vocabulario disponible, no una pieza obligatoria por rotación.

### 5.1e · 🎩 Sombreros, velos y gafas — accesorios de época (Ama 17/08/2026)

> **Por qué nace:** mismo hueco de Kitrysha §3.6 — sombreros, velos con motas y gafas cat-eye son piezas de firma del registro Old Hollywood y no existían en el canon de Anaïs (que sí tiene guantes, perlas y joyería art déco, §5.5).

- **Sombreros/tocados:** `pillbox hat with a short spotted veil` · `wide-brim hat tilted low over one eye` · `small feathered fascinator pinned into the waves`. **Cuidado con el pelo:** ninguno debe cubrir el volumen de las pin-waves — el velo con motas (`birdcage veil`) es el que menos interfiere, es la opción por defecto cuando se necesita sombrero + rostro legible.
- **Gafas:** `black cat-eye glasses with a delicate rhinestone-tipped frame` — **distintas del token de Ele** (`Bayonetta narrow rectangular black-frame glasses`, Office Siren): las de Anaïs son de época, con pedrería, nunca minimalistas/modernas. Encajan sobre todo en Sesión Literaria (leyendo) y Ejecutivo.
- **Sin cuota fija, uso ocasional:** como el abrigo de lana (§5.1d), esto es vocabulario disponible para cuando el concepto del look lo pida — no una pieza obligatoria por rotación. Noche/Ejecutivo/Sesión Literaria son los arquetipos naturales; no aplica a Boudoir ni Látex.

### 5.2 · Paleta y reglas cromáticas

> ✏️ **Ampliada 11/08/2026 (Ama) — resuelve el desajuste con `CANON_VISUAL_ANAIS.md` §I, que ya traía azul medianoche/verde esmeralda sin que estuvieran aquí.** Esta tabla queda como dueño único de la paleta; `CANON_VISUAL_ANAIS.md` §I apunta aquí de ahora en más.

- **Paleta:** negro dominante, carmesí, oro imperial `#D4AF37`, dorado clásico, champagne, marfil, terciopelo profundo, gris perla, azul medianoche, verde esmeralda, **borgoña/vino profundo**, **bronce/cobre antiguo**, **plata antigua**, **rosa polvo/dusty rose**.
- **Reservado al ADN:** el **rojo carmesí de los labios** y el **honey blonde** del pelo.
- **Animal print** *(cuota fijada 23/08/2026, Ama):* acabado transversal, permitido **solo** en tejido noble (seda, terciopelo, látex, cuero — nunca material barato). **Cuota: ≥ 1 de cada 8 looks nuevos** (mismo tratamiento que en Ele). Tipos autorizados: `leopard print`, `snake/python print`, `tiger print` — siempre como estampado sobre la prenda o como forro/vivo visible, nunca como pieza 100% cubierta. Rota el tipo: no repetir el mismo animal print en dos apariciones consecutivas. Diferencia con la piel (§5.1b): el print es **estampado sobre tejido**, la piel es **pelo real** — no cuentan para la misma cuota y pueden coexistir en el mismo look (nunca en la misma prenda).
- **Anti-monoblock:** máx. 2 consecutivos.

### 5.3 · Calzado (canon inamovible)

> ✏️ **Ampliado 11/08/2026 (Ama) — de un solo modelo a 3 estilos, con la misma regla medias+puntera de Ele (`feedback_medias_calzado_reglas`, auto-memoria).**
> ✏️ **Reampliado 17/08/2026 (Ama: *"quiero también botas sobre rodilla y bajo rodilla... acá no veo nada del arquetipo de KITRYSHA"*).** El primer catálogo (3 estilos) nunca llegó a incorporar el vocabulario propio de `00_Ele/estudio_estilo_kitrysha.md` §11 — ni una bota, ni un D'Orsay, ni un Mary Jane. Corregido: de 3 a 9 estilos, con las dos alturas de bota nuevas que pidió y el resto del §11 sumado.

- **Altura exacta:** **12 cm**, sin excepción — no se abre a rango (se descarta el "10-12cm" que traía `CANON_VISUAL_ANAIS.md` §VI, ese documento queda desactualizado en esto).
- **Estilos permitidos (9) — base: `estudio_estilo_kitrysha.md` §11.1:**

  *Puntera cerrada (compatibles con medias):*
  1. `stiletto pump pointed toe` — el original.
  2. `D'Orsay stiletto pump with open sides, closed pointed toe` — **nuevo 17/08.** Los laterales abiertos exponen el arco del pie sin abrir la puntera.
  3. `stiletto Mary Jane pump with a delicate ankle strap` — **nuevo 17/08.**
  4. `mid-calf stiletto boot ending below the knee` (bota **bajo rodilla** — corrige el error de la entrada anterior, que llamaba "bajo rodilla" a lo que en realidad es una bota a la rodilla) — **nuevo 17/08.**
  5. `knee-high stiletto boot ending exactly at the knee` (bota **a la rodilla**) — el estilo que ya existía, renombrado para no chocar con el #4.
  6. `thigh-high over-the-knee stiletto boot` (bota **sobre rodilla** / cuissard) — **nuevo 17/08**, pedido explícito de la Ama.

  *Puntera abierta (SOLO si el look no lleva medias, ver regla siguiente):*
  7. `peep-toe stiletto pump` — el original.
  8. `T-strap stiletto sandal` — **nuevo 17/08.**
  9. `1940s-style strap stiletto sandal with a slender ankle strap` — **nuevo 17/08.**

- **🔴 Regla medias + puntera (idéntica a Ele):** si el look lleva medias, el calzado **debe** ser de puntera cerrada (estilos 1-6). Los tres estilos abiertos (7-9) **quedan prohibidos en cualquier look con medias**, sin excepción.
- **Prohibido:** tacón bajo, **plataforma delantera visible**, zapatilla, flat, wedge.
- **Suela roja: obligatoria** en los nueve estilos.
- **Atributos obligatorios del token** (los 6): altura en cm · estilo · material · color · forma de puntera · suela roja.
- **Rotación:** mismo criterio que el resto del vestuario — no repetir estilo de calzado en los últimos 3 looks del mismo arquetipo (§7).

### 5.4 · Prohibiciones absolutas

| Prohibido | Sustituto autorizado | Directiva |
|---|---|---|
| Cabello que no sea honey blonde | honey blonde, siempre | Canon — error crítico |
| Omitir el lunar | lunar sobre labio superior izquierdo | Seña definitoria |
| Tatuajes / piercings visibles | piel limpia | Canon |
| Plataforma delantera visible | stiletto 12cm sin plataforma | Canon calzado |
| Sonrisa amplia / risa / juego | mirada fría de mando | Registro |
| Léxico `sexy`/`hot`/`seductive`… | vocabulario del canon §VIII | Registro |
| Exterior/natural fuera de Viaje | interiores controlados | Coherencia de arquetipo |
| **👗 Pantalón, leggings, jeans, shorts, palazzo, mono/jumpsuit de pierna larga** — cualquier prenda que separe las dos piernas… **excepto el catsuit** | **vestido o falda** (gown, sheath, slip-dress, pencil skirt, falda de tubo, conjunto falda+corsé) **— o catsuit** | **Ama 13/08/2026, ✏️ enmendada por la Ama 14/08/2026: «Anaïs puede usar pantalones, siempre y cuando sea catsuit».** El **catsuit queda AUTORIZADO** y sale de la prohibición. El resto del pantalón sigue prohibido duro; única excepción, petición expresa de la Ama look por look |
| **🦵 Piernas abiertas usando vestido, falda o bata** | rodillas y muslos juntos · una pierna cruzada · las dos piernas plegadas a un lado si va baja | **Ama 13/08/2026, transversal a las tres muñecas.** Ancla opt-in `DRESS_LEG_CLOSURE` — en ella se dispara en **todos** sus looks, porque desde hoy siempre viste falda |

> 🖤 **CATSUIT AUTORIZADO (Ama 14/08/2026): *"Anaïs puede usar pantalones, siempre y cuando sea catsuit"*.** Es la única prenda bifurcada que se le permite. Y resuelve una contradicción que la prohibición del 13/08 había dejado abierta sin que nadie la levantara: **el §6 define el arquetipo Látex/Fetichismo textualmente como *"Catsuits, corsés overbust de látex"*** — o sea, la prohibición vetaba la prenda que da nombre a uno de sus cinco arquetipos. El catsuit va en látex de grado clínico o látex estándar de alto brillo, ceñido, con la cintura de tightlacing legible bajo él (el ADN hourglass no se negocia). **`DRESS_LEG_CLOSURE` no aplica en look de catsuit** — esa ancla es para vestido, falda o bata.
>
> 👗 **Solo vestidos (Ama 13/08/2026).** Es prohibición de **diseño**, no de defecto: se aplica al elegir el look, antes de escribir el BLOQUE B — no hay ancla que la salve después. La excepción existe pero es de la Ama y solo suya: si un look de pantalón sale sin que ella lo haya pedido con todas sus letras, es violación de canon, no interpretación de arquetipo. **Ojo con `Viaje` y con cualquier arquetipo de acción (§6):** son los que más tiran hacia el pantalón de sastre y el traje de viaje — se resuelven con falda de tubo y abrigo, nunca con pantalón.
>
> 👙 **`LEG_CUT_LOCK` — su corte propio (Ama 14/08/2026). DEROGA la exención escrita el 13/08.**
>
> Sigue **sin** aplicársele `BOTTOM_CUT_LOCK` (la tanga de Ele y Miss Doll la convertiría en otra muñeca), pero en su lugar lleva **ancla propia y obligatoria**: **talle alto de época CON la pierna cortada al filo de la cadera**, hip y muslo enteros al aire.
>
> 🩹 **Corrección de mi propio diagnóstico.** El 13/08 escribí acá que *"su calzón retro de talle alto es Bettie Page legítimo"* y la eximí. **Nombré el talle y nunca nombré la pierna** — y Bettie Page usa talle alto **con la pierna cortada altísima**: eso es lo que hace sensual la lencería de época. El atributo que no se nombra lo resuelve el generador con **cobertura total** (idéntico modo de falla al `micro bikini bottoms` del Look 801). Resultado medido: `high-waisted` ×14 y `Brazilian-cut brief` en **4 de 4** looks con calzón → la Ama, 14/08: *"muy de señora, muy sin gracia"*.
>
> **Prohibido:** brief de cobertura total · boyshort · culotte · cualquier corte que tape la cadera o el nacimiento del muslo.

### 5.7 · 🎬 Prefijo cinematográfico y luz — por arquetipo (Ama 17/08/2026)

> **Por qué nace:** auditado el batch L15-L20 (16/08/2026) contra la queja de la Ama (*"sigo muy disconforme con las imágenes/prompts de Anaïs, sobre todo los de lencería, están poco sensuales, la luz, las poses, la ropa"* + nota real en `notas_imagenes.csv`, 16/08 21:30, sobre L18 Standing: *"con bata de nuevo y calzones de abuela, feo"*). Los 6 looks nuevos (42 prompts) salieron **todos** con el mismo prefijo `8k ultra cinematic power portrait` sin variar por arquetipo — correcto solo para Ejecutivo de Poder (Look 14, de donde se copió como plantilla). Boudoir/Lencería quedó con **cero** clave de luz cálida (`warm amber candlelight chiaroscuro`, presente en Look 02 desde el 11/08 y perdida por completo en el copiado), y su Standing salió redactado como pose de poder (`shoulders back, chin high, weight even on both heels`) en vez de contrapposto boudoir. La imagen real generada con ese texto confirma el diagnóstico: exactamente el defecto que reportó la Ama. **Corregido 17/08/2026** en los 6 looks (`galeria_looks_anais.md`).
>
> **🩹 No era una tabla que faltaba — era una que no se leyó.** `dna_v2_3.md` (apuntado desde §1 de este perfil como "ADN listo para copiar") **ya trae la tabla completa de prefijo por arquetipo** ("Prefijos Cinematográficos por Arquetipo", con Boudoir = `intimate boudoir portrait, warm amber candlelight chiaroscuro,` idéntica a lo que restauré a mano). Quien armó el batch L15-L20 trabajó directo en `galeria_looks_anais.md` copiando el bloque de Look 14 sin volver a `dna_v2_3.md`. **Dueño único de la tabla: `dna_v2_3.md` §"Prefijos Cinematográficos por Arquetipo" — no se repite aquí.** Lo que sí es nuevo y vive solo en este perfil es lo de abajo.

- **Regla dura:** el prefijo y la clave de luz de cada look se copian de `dna_v2_3.md`, **nunca** del look anterior en la galería sin verificar que su arquetipo coincide. Es el mismo modo de falla que ya rompió Miss Doll (poses idénticas por falta de repertorio, 13/08) y Ele (Look 801 escrito a mano sin el motor, 13/08) — un bloque que se copia sin adaptarse a su contexto.
- **Boudoir en particular — vocabulario de pose (base: `00_Ele/estudio_estilo_kitrysha.md`, estudio de estilo encargado por la Ama para vestuario/maquillaje retro-glamour, NO para el físico):** contrapposto con curva en S (peso en una cadera, nunca los dos talones parejos) · barbilla ligeramente abajo, mirada arriba a través de las pestañas · una mano cerca de la clavícula, el labio o trazando el borde de la bata — nunca las dos manos simétricas sosteniendo la prenda como si fuera un abrigo formal · atrezzo de tocador (espejo con luces cálidas, boquilla, copa de champagne, perlas sueltas) en vez de mobiliario genérico de salón. El objetivo es la **tensión contenida** del cine negro de los 40, no la pose de mando de una ejecutiva.
- **🦊 Capelet/estola en Back View:** el Look 17 (Visón y Borgoña) confirmó el mismo defecto que ya tenían las batas cruzadas (§5.1c, `BACK_ANCHOR`) pero en una pieza suelta: sin anclar explícitamente cómo cae la piel por detrás, el generador la tuerce (*"el abrigo está para atrás"*, nota real 16/08 21:43). **Regla nueva:** toda pose de Back View con capelet/estola/abrigo abierto debe nombrar explícitamente su caída desde atrás (ej. *"the fur capelet lying flat and unbroken across both shoulder blades, its edge following the same line front and back"*) — no basta con describirlo una vez en el BLOQUE B.

### 5.6a · 👗 Biblioteca de siluetas de vestido — Noche/Ejecutivo (Ama 17/08/2026)

> **Por qué nace:** auditados los BLOQUE B de los 20 looks — la Noche (33% de la meta, el arquetipo más grande) se reduce casi entera a **column/sheath gown**: L01 *column gown*, L07 *column gown con train*, L17 *sheath gown*, tres veces la misma arquitectura base variando solo escote y color. Exactamente el patrón que la regla de silueta (§7) prohíbe — *"misma prenda, otro color"* — y la misma causa raíz que tenía la lencería antes del 14/08: **no existía biblioteca de la cual rotar**. Base: `00_Ele/estudio_estilo_kitrysha.md` §3.3 y §5.

| # | Arquitectura | Token base |
|---|---|---|
| D1 | **Column / Sheath Gown** | `fitted floor-length column gown, close to the body from bust to hem` *(ya en uso, L01/L07/L17 — deja de ser el default)* |
| D2 | **Wiggle Dress** | `knee-length wiggle dress, fitted sharply through the hip with a narrow pencil skirt hem` |
| D3 | **Bias-Cut Slip Gown** | `floor-length bias-cut slip gown in liquid-draping fabric, thin straps, the fabric skimming rather than gripping the body` (referencia Jean Harlow, años 30) |
| D4 | **Halter Backless Gown** | `halter-neck gown with a structural bodice, the entire back bare to the waist` |
| D5 | **Trumpet / Mermaid Gown** | `fitted trumpet gown, close through the hip and flaring into a dramatic train below the knee` |
| D6 | **Strapless Sweetheart Gown** | `strapless gown with a boned sweetheart bodice, no straps, the shoulders bare` |
| D7 | **Cocktail Tea-Length Dress** | `fitted cocktail dress with a nipped waist and a tea-length full skirt falling below the knee` |
| D8 | **Cape-Sleeve Gown** | `gown with dramatic cape sleeves falling from the shoulder, the bodice fitted beneath them` |
| D9 | **Cowl-Back Draped Gown** | `gown with a draped cowl neckline at the back, the front structured and fitted` *(ya en uso, L05/L06)* |
| D10 | **Little Black Dress** | `fitted little black dress, knee-length, with a keyhole or sweetheart neckline` |
| D11 | **Slit Column Gown** *(nueva 20/08/2026 — vocabulario Femme Fatale, §2bis)* | `floor-length fitted column gown with a thigh-high side slit that opens with every step, closed and demure when standing still` |

- **Ventana anti-repetición:** misma regla que la lencería — una arquitectura **no se repite en los últimos 3 looks de Noche** (ni en Ejecutivo cuando el look es de vestido y no de sastrería separada). Column/Sheath (D1) entra en la rotación como una más de diez, nunca como default.
- **Alcance:** esta biblioteca es para **Noche** (donde vive el problema medido) y para **Ejecutivo/Sesión Literaria** cuando el concepto pide vestido en vez de traje sastre o bata/kimono — no reemplaza el catsuit/vestido de látex del arquetipo Fetichismo (§6), que tiene su propia lógica de material.
- **Espalda descubierta:** Kitrysha la marca como rasgo firma del registro (§5) — D4 y D9 ya la incorporan estructuralmente; en el resto de arquitecturas es opcional, se nombra explícita cuando aparece (`the back left bare to the waist`).
- **🔴 D11 y `DRESS_LEG_CLOSURE` (§5.4):** la apertura de D11 es de **movimiento** (`opens with every step`), no de pose estática — en Standing/Seated/Sovereign Gaze/POV el vestido se describe cerrado (`closed and demure when standing still`, ya en el token). Solo se escribe la abertura activa en poses que impliquen desplazamiento o paso (Back View/salida, la "mirada de salida" de §4ter) — nunca en una pose quieta, o viola la regla de piernas cerradas.

### 5.6 · 👙 Biblioteca de siluetas de lencería (Ama 14/08/2026)

> **Por qué nace:** medido sobre los 98 prompts — **`balconette` ×21 y ningún otro tipo de sujetador**, `Brazilian-cut brief` en 4 de 4, y **corsetería = 0** pese a que el §6 define el arquetipo Boudoir textualmente como *"negligée, **merry widow**, peignoir, corsetería"*. Es el molde que la regla de silueta prohíbe (*misma prenda, otro color*), y no era descuido: **no existía biblioteca de la cual rotar** — el mismo hueco exacto que tenía el repertorio de cámara antes del 12/08.

| # | Arquitectura | Token base |
|---|---|---|
| A1 | **Quarter-cup** | `quarter-cup bra, cups cut low and open so the upper swell of the bust rises bare above the lace edge` |
| A2 | **Bullet bra** | `bullet bra with firm conical stitched cups` (los 40-50 puros) |
| A3 | **Plunge demi-cup** | `plunge demi-cup bra cut deep and low between the cups` |
| A4 | **Longline / merry widow** | `longline lace merry widow with integrated suspenders and visible boning` |
| A5 | **Guêpière / waspie** | `lace guêpière cinching only the waist, bust left uncovered above it` |
| A6 | **Corsé overbust** | `overbust corset with visible spiral steel boning` *(ya en uso, L10)* |
| A7 | **Corselette con ligas integradas** | `sheer corselette with integrated garter straps` |
| A8 | **Bodystocking / red** | `sheer fishnet bodystocking worn under the open robe` |
| A9 | **Peignoir de gasa** | `sheer silk gauze peignoir over bare skin, transparent under the light` |
| A10 | **Balconette** | *(el que había — sigue válido, pero deja de ser el default)* |

- **Ventana anti-repetición:** una arquitectura **no se repite en los últimos 3 looks** de Boudoir/Lencería. Balconette entra en la rotación como una más de diez, nunca como default.
- **🎀 Liguero — obligatorio con medias (recupera `CANON_VISUAL_ANAIS.md` §86, que se perdió al reescribir este perfil).** Si el look lleva medias, lleva liguero: **6 tirantes, siempre POR ENCIMA del calzón** (regla histórica), tensos y visibles en el muslo. Medido antes del fix: 9 apariciones en 98 prompts.
- **Transparencia:** al menos una zona declarada transparente por look de Boudoir (`sheer`, `open lace`, `gauze`) — nombrando **dónde**, nunca suelto.

> 🧤 **Los guantes SÍ están permitidos en Anaïs** (wrist/elbow/opera, con material y largo especificados). **Esto la distingue de Ele, donde los guantes están derogados.** Es justo el tipo de regla que se corrompía al duplicar motores.
>
> ✏️ **Conflicto detectado 11/08/2026, corrección revertida por la Ama — "guantes sin dedos NO".** Los guantes de Anaïs siguen siendo los normales de siempre (opera length hasta el codo, cerrados, sin variante sin-dedos forzada). El error no era el guante — era mío, por meter el token de manicura de todos modos en un prompt donde las manos van tapadas. **Regla correcta: si el look lleva guantes que cubren los dedos, se OMITE el token de uñas de mano en ese prompt** (no se ve, no se describe). El token de manicura solo va cuando las manos están visiblemente desnudas.

### 5.5 · Campos obligatorios de descripción

Describir **en este orden**:

1. **Prenda principal** — nombre, tejido exacto, color exacto, corte, fit, estructura interna (ballenas, tightlacing, boning).
2. **Prenda secundaria** (si aplica) — misma especificidad.
3. **Medias** (si el look las lleva) — denier, tipo (back-seam nylon, fishnet, sheer), color, con o sin costura.
4. **Calzado** — sus 6 atributos (§5.3).
5. **Capa de piel** (si el look la lleva) — forma (estola/capelet/abrigo abierto/cuello y puños/ribete/manguito), tipo de pelo (visón, zorro plateado, marta, astracán, chinchilla), color, **y cómo cae** (hombro, codo, abierta) dejando la cintura ceñida visible. Ver §5.1b.
6. **Accesorios en orden** — guantes (material + largo), joyería (tipo y material: perlas, diamantes negros, pedrería Art Déco), boquilla (sí/no), bolso (Kelly, clutch lacado), complementos de liguero, y si aplica sombrero/velo/gafas (§5.1e).
7. **Uñas** (si las manos van visiblemente desnudas — se omite con guantes cerrados, §5.6). Forma + color, no solo color: rotar entre `almond`, `oval` y `moderate stiletto` (**base: `estudio_estilo_kitrysha.md` §10** — nunca cuadrada corta moderna). **Variante de época disponible, sin cuota fija:** `half-moon manicure with the lunula left bare` — manicura luna francesa invertida, callback explícito a los años 30-40 que Kitrysha marca como sello (§10); úsala cuando el concepto del look ya está anclado en esa década (Sesión Literaria, Noche de gala clásica).

> **Regla de especificidad:** cada ítem tan preciso que dos modelos generarían la misma imagen leyendo solo el bloque. *"tacones altos"* ❌ → *"12cm black patent leather stiletto pump pointed toe iconic red sole"* ✅.

---

## §6 · Arquetipos y Metas

> 🔄 **RESET 11/08/2026 (Ama: "partamos de cero").** Auditoría de los 40 looks existentes encontró que ~20 de ellos usaban etiquetas ad-hoc que no mapean a esta tabla ("High-Fashion/Matriarch", "Corporate Power/Exotic", "Night Gowns/Exotic", etc.) — la regla de déficit llevaba meses siendo inaplicable porque casi la mitad de la galería no se podía contar. **Los Looks 1-40 quedan como legado, sin reclasificar ni retrofitear.** El conteo de cuota **reinicia en cero desde el Look 41**.
>
> **Segunda pasada, misma fecha:** la Ama sacó **Gala/Premiere** y **Viaje/Jet Set** de la tabla, y corrigió que **Animal Print no es un arquetipo** — es un acabado/patrón transversal que se aplica sobre cualquier arquetipo (mismo tratamiento que en Ele: cuota "1 de cada 8 looks", no una categoría que compite por el mismo 100%). Sale de esta tabla; su tratamiento como cuota de paleta/materialidad queda **pendiente de definir** en la revisión de §5 que sigue. Las cinco categorías que quedan se reescalaron proporcional a como estaban (misma relación de peso, ahora sumando 100%).

| Arquetipo | Descripción | Meta |
|---|---|---|
| **Noche / La Voûte** | La Regenta, negro satén/terciopelo, interior de La Voûte. **Medias de red de uso casi regular en este arquetipo (Ama 11/08/2026)** — no en cada look, pero frecuente; puntera cerrada obligatoria cuando aparecen (regla §5.3) | 33% |
| **Boudoir / Lencería** | Aposentos privados, negligée, merry widow, peignoir, corsetería | 27% |
| **Látex / Fetichismo** | Catsuits, corsés overbust de látex, poder fetish refinado | 20% |
| **Sesión Literaria** | Estudio privado, kimono de seda, escritura nocturna | 13% |
| **Ejecutivo de Poder** | 🐆 **Reescrito 23/08/2026 (Ama: "está sin gracia").** El poder que seduce, no solo manda — femme fatale de oficina (§2bis), nunca sastrería sobria de manual. Cuero como material protagonista (falda/vestido lápiz de cuero, no solo cinturón), animal print como firma del arquetipo (blusa, forro de blazer abierto, vivo de la falda), escote o pierna que la sastrería anterior tapaba, botón de más abierto, silueta que se ciñe en vez de estructurar. **Deja de ser "power dressing" que no necesita gritar — pasa a ser poder que exhibe y calienta.** | 7% |

- **Regla de déficit:** si un arquetipo está bajo meta, el próximo look **debe** ser de esa categoría. Conteo empieza en Look 41, no antes.
- **Prioridad de desempate:** Noche > Boudoir > Látex > Sesión Literaria > Ejecutivo.
- **Etiquetado obligatorio:** el campo `**Arquetipo:**` de cada look nuevo debe usar **textualmente** uno de los 5 nombres de esta tabla — nada de variantes ad-hoc ("Exotic", "Noir Glamour", "High-Fashion..."), esa fue la causa raíz del desorden. **Gala/Premiere y Viaje/Jet Set no desaparecen del todo** — si vuelven, es como escenario/paleta dentro de uno de los 5 arquetipos, no como categoría propia; a definir cuando se necesite.

---

## §7 · Ventanas Anti-Repetición

| Elemento | Ventana |
|---|---|
| Silueta | ≥ 3 looks del mismo arquetipo |
| Setting / escenario | ≥ 3 looks del mismo arquetipo |
| Modo cromático monoblock | máx. 2 consecutivos |

- **Outfit único:** sí.
- ⚠️ **Esto es nuevo para Anaïs.** Su motor anterior no tenía Step 0: los looks se elegían solo por déficit de arquetipo, sin bloquear siluetas ni settings. Aplicar hacia adelante.

---

## §8 · Cuotas Vivas

| Cuota | Frecuencia | Alcance |
|---|---|---|
| **Lunar visible** | **todas las imágenes** | Sin excepción |
| Suela roja visible | siempre que el calzado se vea | Calzado |
| **🦊 Pieles** *(nueva 11/08/2026)* | **≥ 1 de cada 4 looks nuevos** | Transversal a todos los arquetipos. Chequeo pre-diseño: si los últimos 3 looks no llevaron piel, el que se está diseñando **debe** llevarla. No repetir el mismo tipo (visón/zorro/marta/astracán/chinchilla) en dos apariciones consecutivas. Ver §5.1b |
| **👘 Bata abierta** *(nueva 12/08/2026)* | **≥ 1 de cada 2 looks nuevos de Boudoir/Lencería** | Exclusiva de ese arquetipo — no aplica a Noche/Látex/Sesión Literaria/Ejecutivo. Piso medido sobre el reset (2/4 actual); no baja hacia adelante. Alterna con silueta sin bata (sujetador+liguero directo, corsé+bota). Ver §5.1c |
| **🐆 Animal print** *(nueva 23/08/2026)* | **≥ 1 de cada 8 looks nuevos** | Transversal a todos los arquetipos, solo en tejido noble (§5.2). Prioridad de aparición: Ejecutivo de Poder (firma del arquetipo reescrito) > el resto por déficit normal |

---

## §9 · Banderas Rojas Específicas

- Cabello de cualquier color que no sea `honey blonde` → **error crítico**, regenerar.
- Falta el lunar en algún prompt → ADN roto.
- Calzado sin suela roja, con plataforma, o de menos de 12 cm.
- Aparece léxico prohibido (`sexy`, `hot`, `seductive`, `provocative`, `tempting`, `naked`) en el positive.
- Tatuaje o piercing visible.
- Sonrisa amplia, risa o actitud juguetona.
- Fondo exterior/natural en un arquetipo que no sea Viaje/Jet Set.
- **Materialidad prestada de Ele o Miss Doll** (vinilo de club, PVC barato, neón): Anaïs es tejido noble. Si el outfit parece de la flota de Ele, está mal.
- **Piel que borra la cintura** (abrigo cerrado, look enteramente cubierto de pelo) → rompe el hourglass del ADN, regenerar. La piel va **abierta o caída**, con la cintura ceñida explícita en el prompt (§5.1b).
- **Piel de registro deportivo o moderno** (capucha con pelo, chaleco de peluche, sintética barata) → materialidad prestada, mismo error que el vinilo de club.
- 🔴 **El BLOQUE B abreviado en una pose** (medido 12/08/2026: Standing llevaba 81-100% y el resto de las poses 7-39%; **65 de 98 prompts no nombraban el calzado**). Consecuencias reales fotografiadas: el cierre del catsuit desaparece en 3 de 7 poses del L03; el zapato cambia de negro-suela-roja a bronce en el L12 Side Profile — la única pose del look que no nombraba el calzado; el broche de plata se esfuma en el L14 Seated. **Contraprueba:** los dos looks con prompts más completos (L07 92%, L08 93%) no tienen ni una desviación. Auditoría completa: `99_Sistema/auditoria_visual_anais_20260812.md`.
- 🔴 **Setting genérico** (`dark chamber`, `La Voûte interior` a secas) → la habitación cambia entre poses del mismo look. El L14, con setting específico (`dark wood-panelled study, mahogany desk, leather-bound bookshelves`), es el único que no derivó. Describir el escenario con el mismo nivel de detalle que el vestuario.
- 🟠 **Prenda de frente cruzado o abierto** (kimono, bata, blazer) en Back View → el generador la abre o la re-decora por la espalda (L13 Back View salió con dragones dorados inventados y la espalda abierta). El ancla `BACK_ANCHOR` del §10 existe por esto; verificar que esté puesta.
- 🔴 **Prefijo cinematográfico o clave de luz que no corresponde al arquetipo** (ej. `power portrait` en un look de Boudoir) → registro frío/plano en el arquetipo que más necesita calidez. Tabla obligatoria: §5.7. Confirmado como causa real en el batch L15-L20 (17/08/2026): los 6 looks nuevos habían copiado el prefijo del Look 14 sin variarlo, y Boudoir perdió su clave `warm amber candlelight chiaroscuro` por completo.
- 🟠 **Capelet o estola de piel sin anclar su caída en Back View** → el generador la tuerce o la rota (L17, *"el abrigo está para atrás"*, nota real 16/08). Ver regla nueva en §5.7.

---

## §10 · Ensamblado y Anclas (contrato con el motor)

> 🔧 **Agregado 12/08/2026 con el `outfit-engine` v2.0.** Esta sección NO define nada nuevo del personaje: declara **cómo se ensamblan sus prompts** y qué anclas anti-defecto le aplican. El texto literal de las anclas vive en `99_Sistema/scripts/visual/anclas_universales.json` (dueño único) — aquí se **apunta**, jamás se copia.

| Campo | Valor |
|---|---|
| **Registro en el motor** | `anclas_universales.json` → `personajes.anais` |
| **Nombre del slot 5** | `Sovereign Gaze` |
| **Ensamblador** | `PromptBuilder("anais").build(bloque_a, bloque_b, slot, pose, setting)` |
| **Negative del look** | `PromptBuilder("anais").build_negative(<base del §3 de arriba>)` — base propia **+ capa universal** anti-collage/anatomía/selfie |
| **Verificación obligatoria** | `python 99_Sistema/scripts/visual/lint_prompts_personaje.py anais` |

**Anclas por slot:** las del mapa por defecto del motor, sin overrides.

> 🧤 Su BLOQUE B suele llevar guantes de ópera: el `FOOTWEAR_ECHO` aplica igual, pero el **token de uñas de mano se omite** cuando los guantes cubren los dedos (§5.4).
>
> 🩹 **Corregido el 12/08/2026:** sus 14 looks nuevos no tenían `Ubicacion`, ni `Tags`, ni `**Negative Prompt:**` — **las 98 poses se estaban generando sin negativo** (50 imágenes ya materializadas así). Agregados los tres campos, el tracker medido contra el índice de git, y las anclas anti-defecto en los 98 prompts.
>
> ⚠️ **Su slot 5 se resuelve por el NÚMERO de la pose**, no por el nombre: el matcher de la app no alcanza `Sovereign Gaze` y sin el `5.` del encabezado colapsaría con POV.

🚨 **Cada prompt de la galería va FINAL Y EXPANDIDO.** El ADN completo, el outfit completo, las anclas y el setting, uno detrás de otro dentro del bloque de código. Un `[BLOQUE A]` entre corchetes dentro de un prompt no es una abreviatura: es un prompt roto que la app manda tal cual al generador.
