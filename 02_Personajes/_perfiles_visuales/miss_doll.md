# 🎀 Perfil Visual — Miss Doll

> Contrato del `outfit-engine`. Creado 27/07/2026 al generalizar el motor.
> **Antes de esto Miss Doll no tenía motor**: solo una regla de canon (`.agent/rules/05-canon-miss-doll.md`) y un sistema de poses. No tenía Step 0 anti-repetición, ni token bloqueado, ni arquetipos con metas.

---

## §1 · Identidad y Rutas

| Campo | Valor |
|---|---|
| **Nombre canónico** | Miss Doll |
| **Slug** | `miss_doll` |
| **Galería** | `02_Personajes/01_Principales/miss_doll/GALERIA_OUTFITS_MISS_DOLL.md` |
| **Carpeta de imágenes** | `05_Imagenes/miss_doll/look<N>_<slug_del_título>/` — **sin cero a la izquierda**; el slug sale del **título** con el algoritmo de la regla 11 §2 (ej. *Neon Pink Cage* → `look1_neon_pink_cage`) |
| **Convención de nombre** | `miss_doll_<N>_<pose>.png`, **N sin cero a la izquierda** ⚠️ ver §9 |
| **Numeración** | correlativa. El encabezado de la galería se escribe `Look 01`…`Look 14` (legibilidad), pero **carpeta y archivo van sin padding** — igual que Ele y Anaïs. *(Corregido 12/08/2026: el perfil decía `look001` a 3 dígitos, ninguna carpeta real usaba ese formato, y el uploader de la app construye el nombre con `look.number % 10000` **sin** `padStart` → escribiría `miss_doll_1_standing.png` dentro de una carpeta `look01_`. Mismatch evitado.)* |
| **Quién manda sobre la carpeta** | El campo `- **Ubicacion:**` del look. El uploader usa `look.location` si existe y solo cae al patrón por defecto si falta (`GitRepository.kt:140-143`). Por eso `Ubicacion` no es decorativo: **es la orden**. |
| **Canon profundo (enlace)** | [`CANON_VISUAL_MISS_DOLL.md`](../01_Principales/miss_doll/CANON_VISUAL_MISS_DOLL.md) — **manda sobre este perfil en caso de conflicto** |
| **Sistema de poses** | [`SISTEMA_POSES_VESTUARIO_MISS_DOLL.md`](../01_Principales/miss_doll/SISTEMA_POSES_VESTUARIO_MISS_DOLL.md) |

---

## §2 · BLOQUE A — ADN Inamovible

> 🔒 **Este fence es el DUEÑO ÚNICO del BLOQUE A de Miss Doll (29/08/2026).** Lo lee el motor —
> `PromptBuilder.bloque_a` — y ya no se copia a mano en cada script de batch. El marcador
> `<!-- ADN:BLOQUE_A -->` de abajo es lo que el motor busca: **no lo borres ni lo muevas**.
> Dentro del fence va SOLO texto de prompt en inglés. Hasta hoy llevaba una nota en castellano
> incrustada en la cláusula de sombra de ojos (*"color exacto de sombra se fija en BLOQUE B por
> look, ver §5.5…"*): los scripts la omitían a mano, pero cualquiera que copiara el fence entero
> le metía castellano al prompt. Movida abajo, donde vive el resto de las notas.

<!-- ADN:BLOQUE_A -->
```text
hyper-realistic high-end editorial glamour photography of Miss Doll, adult glamorous woman, (soft rounded oval face:1.1), smooth softly rounded jawline, (soft gently curved full cheekbones:1.1), small refined rounded chin, delicate refined features COMMANDING, sharp platinum blonde asymmetric angled bob, sleek straight razor-cut strands, ice platinum highlights, clear exposed forehead, NO BANGS, (small refined perky upturned nose:1.2), (huge oversized round almond-shaped cold vivid blue eyes, wide open eye opening:1.4), (richly pigmented deep cobalt blue iris, clearly saturated blue with visible colour, never grey and never pale and never washed out to white, sharp dark navy limbal ring:1.4), (fixed dominant professional gaze zero warmth, slow appraising once-over gaze sweeping head to toe with cold superiority:1.3), chin elevated 5 degrees, (bold precisely filled brow makeup, dark smoky taupe-grey brow color noticeably darker than the platinum hair for maximum contrast, extremely high dramatic raised arch positioned high on brow bone, sharp clean tapered tail, thick clearly visible brow shape:1.5), HEAVY GLAMOUR editorial makeup with (thick sharp angular winged eyeliner upticked pointed wing tip:1.2), intense shimmer smokey eye technique, (impossibly long mega XXL individual false lashes at outer corners dramatic cat-eye:1.2), (blinding chrome strobing highlight on cheekbones nose bridge and brow bone:1.2), (soft gentle contour warm shadow under cheekbone:1.0), (aggressively overlined voluminous ULTRA PLUMP high-gloss wet lips exaggerated cupid's bow full pillowy lips mirror-gloss finish:1.3) curved into a (subtle smug smirk, one corner of the mouth raised:1.2), human realistic face DOMINANT smirking expression, pale cold porcelain white skin, editorial realistic human skin texture subtle visible pores, cold undertone, sculptural EXTREME hourglass silhouette, (toned midriff, subtly defined abs with soft natural muscle separation, faint visible obliques:1.2), (slender delicate shoulders, long lean toned arms with soft subtle muscle tone, not bulky, feminine and graceful:1.2), (long lean slender toned legs, soft subtle thigh definition, not muscular, elegant model proportions:1.2), (colossal oversized massive chest, extreme high-profile artificial breast implants, impossible gravity-defying spherical shape, ultra-high profile silicone augmentation, overt bolted-on projection, unmistakably fake implants:1.5), dramatic alluring plunging neckline, deep prominent cleavage, aggressively narrow cinched waist, full wide hips, tall lean slender commanding figure, rigid upright posture, square shoulders pulled back, (impeccably manicured long glossy nails:1.1)
```
> Nota de uñas: la calidad (largas, impecables, gloss) es fija aquí; forma/largo exacto/color varían por look en BLOQUE B (§5.5).
>
> Nota de sombra de ojos (sacada del fence el 29/08/2026): la **técnica** (`intense shimmer smokey eye`) es fija aquí; el **color exacto** se fija en el BLOQUE B por look — ver §5.5 — y **nunca se repite el mismo tono en looks consecutivos**.

> 💪 **Rediseño de pecho y cuerpo (Ama 19/08/2026):** pecho aumentado a **colosal, ultra-alto perfil, esférico y abiertamente artificial/fake** (`colossal oversized massive chest, extreme high-profile artificial breast implants, impossible gravity-defying spherical shape, ultra-high profile silicone augmentation, overt bolted-on projection, unmistakably fake implants:1.5`). Mantiene cuerpo con evidencia de gimnasio y extremidades esbeltas.
>
> 🔙 **Experimento "base Tiffany Stratton" — REVERTIDO el mismo día (Ama 17/08/2026).** Se probaron 3 calibraciones sucesivas (atlético-tonificado → fisicoculturista → tonificado-moderado, cada una verificada contra una imagen real generada) buscando trasladar el físico de la luchadora de WWE Tiffany Stratton al cuerpo de Miss Doll. Ninguna cuadró a satisfacción de la Ama — la última nota fue *"no, déjala como estaba antes el cuerpo de Miss Doll"*. **El BLOQUE A de arriba es el original del 11/08/2026, restaurado sin cambios.** Se deja este párrafo como registro de que el experimento se intentó y se descartó — para que una futura sesión no repita las mismas 3 pasadas sin saber que ya se probaron.

> ⚠️ El prompt base histórico de la regla 05 mezclaba en un solo bloque el ADN **y** un outfit concreto (bodysuit rosa neón + botas de 8"). Aquí se separan: lo de arriba es **BLOQUE A puro** (cuerpo, cara, pelo, maquillaje, postura). El outfit va en el BLOQUE B de cada look. **Mezclarlos es lo que hace que todos sus looks salgan iguales.**
>
> 🔄 **Rediseño de rostro (Ama 11/08/2026):** el rostro cambió de "sharp angular heart-shaped" a **suave y ovalado** — proceso iterativo de 3 pasadas sobre la misma imagen de referencia hasta aprobación explícita ("queda perfecta"). Cambios acumulados: cara ovalada/suave (no angular), pómulos suaves curvos (no razor-sculpted), mentón redondeado, contour suave/cálido (no fuerte/angular), **ojos huge oversized doll-like** (antes narrow/hooded) y **cejas de arco muy alto** (antes sharp cold arch). Lo demás del ADN (bob platinado, labios ultra-plump, piel, cuerpo reloj de arena) no se tocó. Este prompt reemplaza al anterior como base vigente.

**Rasgos que NO se negocian jamás:**

- **Platinum blonde asymmetric bob**, corte navaja. Nunca oscuro, nunca coleta, nunca moño.
- **Frente despejada** — `clear exposed forehead, NO BANGS`. El flequillo es violación de canon.
- **Labios ULTRA PLUMP, overlined, high-gloss wet, cupid's bow** — la **forma** es inviolable. El **maquillaje (ojos + labios) se elige según la OCASIÓN del look** (rojo, humo negro, bronce, nude-glam…) y se fija en el BLOQUE B. **El rosa es firma de Ele, NO de Miss Doll.** Nunca nude natural, nunca mate, nunca maquillaje "sin producto". *(Ama 02/08/2026: derogado el "labios rojos SIEMPRE"; físico canónico = el del banco que le gusta, maquillaje por ocasión.)*
- **Ojos gris hielo, grandes, redondos** (rediseño 11/08/2026, antes "narrow slightly hooded"; **corrección misma sesión:** el token literal `doll-like` — junto con `doll nose` en la nariz — empujaba el render hacia cara de muñeca/maniquí, justo lo que el negative prohíbe. Se sacó la palabra "doll" de ambos tokens, se conservó el tamaño grande/redondo del ojo) con la *Face of the Pole*: disociación profesional, cero calidez pese al tamaño. **Recalibrado el mismo día (Ama 11/08/2026):** cero calidez ya NO es cara seria/plana — es **smirk + un repaso de arriba a abajo con superioridad**, actitud, no cara de piedra. La frialdad vive en el desprecio activo, no en la ausencia de expresión. **Única excepción explícita:** en el arquetipo **Girly Girl** (§6) la expresión SÍ se suaviza a cálida/sonriente — quiebre real de personaje, no error. Fuera de ese arquetipo, el smirk + repaso de superioridad es el default.
- **Cejas de arco muy alto, SIEMPRE rellenas/definidas con maquillaje** (rediseño 11/08/2026, dos pasadas: "microbladed" invisible → "ash-grey pomade" TODAVÍA invisible ("quedó idéntico a los anteriores") → corregido final a `dark smoky taupe-grey, noticeably darker than the hair, peso 1.5`, confirmado en primer plano real: *"queda perfecto"*). El maquillaje fijo de Miss Doll incluye ojos + labios + **cejas** — no solo los dos primeros.
- **Rostro ovalado suave** (rediseño 11/08/2026, antes "sharp angular heart-shaped").
- **Piel porcelana fría** con textura humana real y poros visibles — nunca cera, nunca maniquí.
- **Sin tatuajes** por defecto (blackwork solo si la Ama pide variante legacy explícita).
- **Barbilla 5-10° arriba, torso erguido, hombros atrás.** Nunca hombros caídos.
- **Cuerpo de gimnasio diario** (rediseño 11/08/2026; el experimento "base Tiffany Stratton" del 17/08/2026 se probó y se revirtió el mismo día, ver nota en §2): abdomen con definición suave y visible, pero **hombros/brazos/piernas siempre esbeltos y delgados** — nunca musculatura voluminosa/fisicoculturista.
- **Pecho artificial obvio, colosal, ultra-alto perfil, esférico y abiertamente implantado** (rediseño Ama 19/08/2026: "más grandes, más falsos, con perfil muy muy alto") — `colossal oversized massive chest, extreme high-profile artificial breast implants, impossible gravity-defying spherical shape, ultra-high profile silicone augmentation, overt bolted-on projection, unmistakably fake implants:1.5`.
- **Uñas siempre impecablemente manicuradas, largas y cuidadas** (agregado 11/08/2026 — hueco real, no había ninguna mención de uñas en el ADN hasta hoy). La **calidad** (largas, impecables, gloss) es fija en BLOQUE A; la **forma exacta** (stiletto, coffin/ballerina, almond, square) y el **largo/color/acabado** varían por look y se fijan en BLOQUE B (§5.5) — nunca uñas cortas, descuidadas, ni un look sin mencionarlas.

---

## §3 · Negative Prompt

**Base (siempre) — ampliado 11/08/2026 con los fallos reales detectados en el rediseño de rostro/cuerpo, y 20/08/2026 con veto de mules y batas cortas:**
<!-- NEGATIVO:BASE -->
```text
bangs, fringe, covered forehead, dark hair, brunette, ponytail, bun, coral eyeshadow, peach eyeshadow, terracotta lips, coral lips, pastel eyeshadow, low-pigment eyeshadow, washed-out eyeshadow, grey eyes, steel grey iris, pale washed-out iris, colourless iris, white eyes, blank white iris, glowing white eyes, albino eyes, childish face, teen, natural makeup, subtle makeup, nude lips, matte lips, rosy cheeks, warm natural skin tone, wax skin, plastic mannequin skin, tattoos, casual outfit, flat shoes, sneakers, block heel, chunky heel, vulgar cheap costume, slouched shoulders, warm smile, laughing, sharp angular face, angular jawline, thin invisible eyebrows, sparse pale blonde eyebrows, barely visible brows, faint eyebrows, eyebrows blending into skin, bodybuilder physique, overly muscular, bulky muscles, veiny muscles, grotesque six-pack, masculine muscle mass, thick bulky arms, thick muscular shoulders, wide muscular legs, thick calves, muscular bulky thighs, small chest, natural breasts, flat chest, corset, waist cincher, bustier, doll face, mannequin face, uncanny doll-like appearance, glassy doll eyes, porcelain doll aesthetic, full brief, high-waist brief, high-waisted panty, boyshort, boy shorts, hipster brief, culotte, tap pants, granny panties, bloomers, full-coverage bikini bottom, bikini bottom covering the buttocks, full seat coverage, legs spread apart under a dress, legs parted under a skirt, mule, mules, platform mule, mule sandals, slide sandals, backless heels, short robe, mini robe
```
> ⚠️ El `corset/waist cincher/bustier` va en negative BASE porque el corsé ya no es obligatorio (§5.5) — si el look de hoy sí lo lleva, sacar esos 3 términos del negative de ese prompt puntual.
> 🔙 **El experimento de cuerpo "base Tiffany Stratton" (17/08/2026) se revirtió el mismo día** — este negative es el original del 11/08, restaurado sin cambios. Ver nota en §2.
> 👙🦵 **Los términos de calzón y de piernas se agregaron el 13/08/2026** (directivas de la Ama) como **segunda capa** de `BOTTOM_CUT_LOCK` y `DRESS_LEG_CLOSURE`. La barrera real son las anclas afirmativas del positive: Gemini ignora el negative con frecuencia y ya está medido en este repo. Vetar sin anclar no arregla nada.

| Pose | Añadir al negative | Por qué |
|---|---|---|
| Cualquier POV / cámara en mano | `no phone, no smartphone, no device, no screen` | El encuadre POV invita al modelo a añadir un teléfono |
| Poses con barra | `two women, duplicate figure, mirror reflection` | El reflejo del club genera figuras dobles |

---

## §4 · Poses Canónicas

> **Estandarizado 05/08/2026 (directiva Ama):** las 3 muñecas (Ele/Miss Doll/Anaïs) comparten las mismas **7 categorías de cámara** — mismo slot, mismo orden, mismo propósito de encuadre — para que el motor de poses y la app las traten con una sola taxonomía. El contenido/expresión de cada slot sigue siendo 100% propio de cada personaje. **Retirado en este cambio:** Hip Carry contra Barra, Pie en Hombro y Caminata Circular (poses de acción del rediseño 02/08, ninguna corresponde a una categoría de cámara) — quedan fuera del canon vigente.

**7 poses (mismo slot que Ele, contenido de Miss Doll):**

| # | Categoría (universal) | Nombre de pose | Slug de archivo | Nota |
|---|---|---|---|---|
| 1 | Standing | Cruel Contrapposto | `standing` | Cuerpo entero de pie, contrapposto agresivo, peso cargado en una cadera |
| 2 | Back View | Espalda Total | `back_view` | Espalda completa a cámara, arquitectura de corsé visible, mirada por sobre el hombro |
| 3 | Seated | Trono de Costado | `seated` | Sentada de costado con **las dos piernas plegadas al mismo lado, rodillas y muslos apretados, tobillos apilados**, torso girado de frente al lente, antebrazo sobre el respaldo, barbilla apoyada, smirk frío |
| 4 | Side Profile | Tres Cuartos Arrogante | `side_profile` | Giro ¾ hacia cámara, peso en una cadera, mirada fría de perfil |
| 5 | **Glacial Command** *(slot Ditzy de Ele, renombrado — no encaja una mirada vacía en su dominancia)* | Close Up Fría | `glacial_command` | **WAIST-UP** (cintura arriba): rostro grande y nítido + pecho prominente en el frame inferior + detalle del outfit superior legible · **UNA sola mano** en cuadro haciendo el gesto · **mirada FUERA de cuadro**, fría e indiferente |
| 6 | POV | Command POV *(nombre histórico)* | `pov` | **RETRATO SENSUAL DE INSTAGRAM** (thirst-trap de influencer): **mira a la cámara**, medio cuerpo, cara protagonista + escote abajo, **una sola mano**, `a single woman alone`. **NO es point-of-view literal** |
| 7 | Odalisque | Floorwork de Alta Escuela | `odalisque` | Suelo, **rodillas recogidas y juntas contra el pecho, tobillos cruzados** — o cualquiera de las otras 8 variantes de floorwork del repertorio (gateo felino, sirena angular, cobra, escorpión, diosa reclinada, cenital, arrodillada, camel backbend). Crop en mano cuando el look lo pide |

> 🦵 **PIERNAS ABIERTAS ELIMINADAS — orden de la Ama, 29/08/2026.** *"quita definitivamente la pose de piernas abiertas de miss doll"*, y confirmó el alcance: **las dos** poses firma que las llevaban. Cae la **Monarch Throne** del Seated (*piernas 60-90°*, ahora Trono de Costado) y cae la **V abierta** del Throne en Suelo del Odalisque.
>
> **Esto deroga el arreglo parcial del 13/08/2026**, que solo prohibía la V cuando el look llevaba falda o vestido y la dejaba viva para calzón, bikini y catsuit. Ya no hay excepción por prenda: no va en ningún look. Con ella cae también la excepción que `prompt_builder.build()` le hacía a `DRESS_LEG_CLOSURE` en su slot Seated (existía solo para que el ancla no peleara con la Monarch Throne dentro del mismo prompt).
>
> **Las sub-poses se reescribieron, no se borraron.** El slot Seated conserva sus 7 variantes y el Odalisque sus 9 — borrar una empobrece la rotación, y la variedad es canon. Dueño único de las sub-poses reales: `repertorios_pose.json`.
>
> ⚠️ **Rechazar una pose son DOS pasos** (lección del 17/08/2026, `feedback_corregir_el_look_no_corrige_el_repertorio`): el texto del look **y** el repertorio que lo sirve. Corregir solo el look hace que la rotación se la sirva al siguiente en cuestión de horas.

> 🎥 **Repertorio de cámara — dueño único:** [`01_Principales/miss_doll/repertorio_camara_miss_doll.md`](../01_Principales/miss_doll/repertorio_camara_miss_doll.md). 7 variaciones para los slots 5 y 6, con rotación por número de look.
>
> 🩹 **Corregido 12/08/2026 — era una desviación mía, no un cambio de canon.** Estas dos filas decían *"plano medio/primer plano, mirada fría de mando directo a cámara"* y *"cámara a la altura de un sub arrodillado"*. **Ditzy y POV están definidos desde el 28/05 y el 09/06/2026** (reforzados el 30/06 y el 02/08) en `.agent/rules/06-generacion-imagenes.md` §5 y §9, `pose_repertoire_v5.md` §5-§6 y `dna_v3_5.md`. Al estandarizar las 7 poses el **05/08** los escribí mal, y el POV arrodillado es exactamente el *point-of-view literal* que el canon prohíbe desde junio porque el generador lo lee literal.
>
> ✅ **PENDIENTE CERRADO 13/08/2026 (esta línea decía otra cosa y ya era falsa).** Decía: *"los otros cinco slots están clonados al 79-83%… no cuesta nada todavía: está 0/98 materializado"*. Ambas mitades caducaron el mismo día: los **149 repertorios de sub-pose** se escribieron el 13/08 en `99_Sistema/scripts/visual/repertorios_pose.json` (49 de Miss Doll, pole + burlesque) y sus 98 prompts se reensamblaron con 7/7 variaciones distintas por slot; y la materialización va en **52/98**, no en 0. Otro estado sin fecha de re-medición que envejeció hacia la mentira.

- **Total por look:** 7
- **Repertorio de variaciones:** el vocabulario completo (de pie / pole / floorwork / silla / con sub) está en `SISTEMA_POSES_VESTUARIO_MISS_DOLL.md` §2 — sigue vigente como banco de detalle para redactar cada slot, ya no como poses standalone.
- **Principio rector de pose:** *dispensa sensualidad como poder, no como oferta.* Un movimiento donde otras hacen tres. Pausas de 4+ segundos. La mirada se posa 2-4 s y **abandona deliberadamente**.

### 4bis · 🕺 Vocabulario de pose — Pole / Floor Dance / Burlesque (Ama 17/08/2026)

> **Directiva explícita:** las poses de Miss Doll se inspiran en **tres escenarios reales**, no uno solo — `repertorios_pose.json` (13/08/2026) ya declara `registro_estetico: "POLE DANCE + BURLESQUE"`, pero se quedó corto de **floor dance/floorwork de stripper** como tercera fuente propia (no un sinónimo de burlesque). Los tres se combinan, ninguno reemplaza a los otros dos:

1. **Pole dance:** agarre en la barra (aunque la barra no esté en cuadro, el brazo/torso recuerdan la tracción), arco lumbar largo, rodilla girada hacia afuera, extensión de pierna vertical, spin congelado a media vuelta, invert parcial.
2. **Floor dance / floorwork de stripper (el que faltaba nombrar aparte):** trabajo a nivel del suelo con **movimiento**, no solo sentada estática — gateo felino sobre manos y rodillas, arco de espalda con las palmas y los talones apoyados (backbend), split o straddle en el piso, cadera rodando contra el suelo (floor grind), transición de rodillas a sentada con el peso rodando. Es lo que debe reforzarse en **Odalisque** (§4, *Throne en Suelo*) para que no quede solo en variantes de sentada-con-piernas-en-V: alternar con al menos una sub-pose de gateo o de arco dorsal por rotación.
3. **Burlesque:** tease progresivo — guante a medio quitar, tirante que resbala, mano que recorre el propio cuerpo antes de detenerse, abanico o boa como atrezzo, mirada por sobre el hombro con una pausa deliberada antes de mirar a cámara.

**Cómo se reparte entre slots:** Standing/Side Profile tiran más hacia pole (verticalidad, extensión de pierna); Seated/Odalisque tiran más hacia floorwork (nivel bajo, movimiento en el suelo); Glacial Command/POV tiran más hacia burlesque (el tease de cerca, la mano en el propio cuerpo). Back View puede tomar cualquiera de las tres según el look.

**Dónde vive esto en el motor:** `repertorios_pose.json` → `personajes.miss_doll` es el dueño único de las sub-poses reales; este vocabulario es la **referencia** contra la que se auditan y se escriben nuevas variantes. ✅ **Retrofit completado 19/08/2026 (Ama):** el slot `odalisque` cuenta con 9 poses dinámicas de floorwork de alta escuela (Throne en Suelo, Feline Crawl, Sirena Angular, Cobra Tease, Scorpion Floor Hook, Diosa Reclinada, Zenithal S-Curve, Knee Crawl Autoritario y Camel BDSM Backbend).

---

## §5 · BLOQUE B — Reglas de Vestuario

### 5.1 · Universo de materiales (recalibrado 11/08/2026 — filtro: stripper + domme + fashionista)

- **Permitidos:** látex (acabado líquido/wet-look, nunca mate), PVC, vinilo (acabado soft-touch/segunda piel), **nylon sheer/semi-transparente** (no estructural rígido), **mesh semi-transparente**, **fashion bondage** — correas finas, hebillas delicadas, chrome hardware fino tipo joyería (referencia Bordelle/Atsuko Kudo, NUNCA rigging pesado de calabozo).
- **🔻 Sacado del canon:** neopreno técnico, nylon estructural rígido, black bondage webbing pesado/industrial, hardware tipo ferretería. Todo lo que lea "utilería técnica" en vez de "prenda" queda fuera.
- **Cuero:** **solo** en corsés, accesorios y arneses — **nunca como pieza principal**.
- **Prohibidos (absoluto):** tela natural mate, algodón, denim, punto casual.
- **Lente de identidad (recalibrado 11/08/2026):** las tres capas de su fondo narrativo mandan sobre el material — **stripper** (sensual, se mueve, se muestra), **domme** (control y bondage, pero de diseño — correas finas como joyería, no rigging), **fashionista** (pulido editorial, nunca utilitario). *"Parece uniforme privado real, no disfraz"* sigue vigente, pero ahora leído como **alta costura fetichista**, no industrial. Si la prenda se sentiría cómoda en una ferretería o un taller, no es de Miss Doll; si se sentiría cómoda en una pasarela de Bordelle, sí.

### 5.1b · 👘 Bata abierta — silueta recurrente en VIP/Penthouse (Ama 12/08/2026)

Auditado sobre los 4 looks VIP/Privado + Penthouse/Off-duty existentes: **2 de 4 llevan bata abierta** sobre el bralette (L04 mesh negro sobre dusty rose, L06 satén perla sobre pearl white) y **2 de 4 van de slip-dress de una pieza sin bata** (L11, L13 — sus propios conceptos dicen textual *"robe+bralette ya usado → slip dress"*, es Step 0 alternando silueta). **Directiva: ese 50% es un piso, no un promedio — no puede bajar hacia adelante.**

> 📏 **Largo obligatorio de bata (Ama 20/08/2026):** **PROHIBIDAS las batas cortas.** Las batas de Miss Doll deben ser **mínimo al tobillo o más largas (ankle-length o floor-length / trailing)** para mantener la elegancia dramática y el arrastre de tela en el suelo.

- **Token:** `sheer/satin/mesh <color> floor-length open robe left open and draped off one shoulder` — material coherente con la paleta del look, bralette+brief o slip a juego debajo.
- **Regla de silueta:** bata **siempre abierta**, nunca cerrada — el abdomen tonificado (§2) es el foco, una bata cerrada lo tapa igual que un corsé mal puesto.
- **🟠 Riesgo conocido en Back View:** prenda de frente abierto en Back View tiende a re-decorarse o cerrarse mal (mismo defecto documentado en Anaïs `anais.md` §5.1c/§9) — verificar que el ancla de espalda esté puesta cuando la bata aparezca en esa pose.
- **🩱 Material por defecto DESDE 17/08/2026: semitransparente, no opaco.** Auditado el Look 25 (Rose Marabou Suite): la bata estaba en `silk charmeuse` (opaco) y el `BACK_ANCHOR` funcionaba perfecto — cerraba bien por detrás — pero la sensualidad seguía muriendo en Back View, porque una bata opaca bien cerrada tapa la lencería igual de bien que una mal cerrada. **El riesgo de arriba no era solo de anclaje: era de material.** Corrección de fondo, no parche: el token por defecto pasa a ser `sheer <material> open robe, semi-transparent fabric that reveals the lingerie beneath from every angle including from behind, falling loose off one/both shoulder(s), dramatic wide bell-shaped cuffs, cinched loosely at the waist with a thin sash` — chiffon/georgette/mesh translúcido, nunca satén o charmeuse opacos, y **puños anchos** (`wide bell-shaped cuffs`) como firma nueva de silueta. Con esto la lencería se lee en las 7 poses, back view incluido, sin depender de que el ancla de espalda salga perfecta. Retrofit al tocar (no migración masiva): se aplica a todo look nuevo con bata desde ahora; los looks ya materializados con bata opaca no se regeneran salvo que la Ama lo pida.

### 5.2 · Paleta y reglas cromáticas (ampliada 11/08/2026 — agrupada por raíz narrativa)

- **Firma inamovible:** el **rosa** (neon / hot / dusty / magenta — cualquier tono de la raíz Stripper) **SIEMPRE presente** en algún punto del look. Es su cuota cromática permanente.
- **🎪 Raíz Stripper** (neón, vivo, de escenario): Hot Pink Neon, Electric Magenta, Cyber Blue, UV Violet, Acid Chartreuse *(acento, nunca dominante — el neón dominante es más de Ele)*.
- **⛓️ Raíz Domme** (oscuro, poder, calabozo con clase): Carbon Black, Oxblood/Deep Wine, Dark Plum, Gunmetal Chrome, Midnight Navy.
- **👑 Raíz Fashionista** (editorial, pulido, alta costura): Champagne, Pearl White, Rose Gold, Chrome Silver, Lavender, Mint, Coral, Turquesa.
- **🎀 Raíz Girly** *(nueva 11/08/2026, exclusiva del arquetipo Girly Girl — §6 · redefinida 03/09/2026)*: **Hot Pink, Fuchsia, Magenta, Rose Gold, Champagne Gold, White.** El pastel suave/tono-bebé (baby pink, cotton-candy, lavanda pastel) queda **fuera por defecto** — es el registro que más se lee como infantil en cualquier generador, mucho más que un rosa saturado. La feminidad exagerada vive en el **saturado y el brillo** (glam adulto, Barbie-editorial), no en el tono apagado/suave. Un pastel puntual solo si la Ama lo pide explícito para un look concreto — nunca el default del arquetipo.
- **Reservado al ADN:** el **rojo** de los labios. No usar rojo como color dominante de prenda (compite con la firma facial).
- **Anti-monoblock:** máx. 2 looks monoblock consecutivos.
- **Uso:** cada look puede inclinarse hacia una raíz (club-neón / calabozo-oscuro / editorial-pulido) según el arquetipo (§6), pero el rosa firma cruza las tres siempre.

### 5.2b · 🎨 Colorimetría — el color contra la CARA, no contra el escenario (Ama 04/09/2026)

> *"cada una de las 3 muñecas tiene pelo, piel, maquillaje estilo distintos, cierto? porque no me haces un estudio de colores, cuales le viene mas a una que a otra teniendo en cuenta eso"*
>
> **Por qué nace.** Hasta hoy la §5.2 de las tres agrupaba el color por **raíz narrativa** (Stripper / Domme / Fashionista / Girly / Vintage Noir) — o sea por *dónde está parada*, nunca por *qué le queda*. Ningún perfil decía una palabra sobre subtono, contraste ni acabado de piel. Resultado medido sobre las tres galerías el 04/09: **plata/cromo es la familia más usada de las tres a la vez** (Ele 39,6% · Miss Doll 74,6% · Anaïs 38,5%) — el único color que no diferencia a nadie. Esta subsección **no deroga ni duplica la §5.2**: la §5.2 sigue siendo dueña de qué colores existen; esto agrega **por qué** unos calzan mejor que otros en esta cara concreta.

**Los cuatro anclajes (leídos del fence `<!-- ADN:BLOQUE_A -->`, §2):**

| Anclaje | Token literal | Lectura |
|---|---|---|
| Pelo | `sharp platinum blonde asymmetric bob` | frío |
| Piel | `pale cold porcelain white skin`, `cold undertone` | **subtono frío declarado**, acabado pulido |
| Ojos | `richly pigmented deep cobalt blue iris` — **cambiado hoy** | **eco de iris = azul** |
| Labios | color **por ocasión** (§5.5.8) | la única de las tres sin labio fijo |

**👁️ Cambio de iris (Ama 04/09/2026):** *"miss doll que sean azules solamente, el steel grey a veces le salen los ojos blancos, como un white walker"*. El token anterior era `cold pale steel grey eyes` + `pale icy grey iris` con peso `:1.4` — o sea el prompt **pedía pálido a gritos** y el generador lo llevaba hasta el blanco. Sustituido por azul cobalto **saturado y pigmentado**, con la negación dentro del propio positivo (`never grey and never pale and never washed out to white`) y ocho términos nuevos en el negative base §3 (`grey eyes, steel grey iris, pale washed-out iris, colourless iris, white eyes, blank white iris, glowing white eyes, albino eyes`). **Vetar sin anclar no arregla nada** — por eso va en los dos lados.

**El eje:** era la única de las tres **sin ancla de color** — platinado, porcelana fría e iris gris, todo sobre el mismo eje neutro. Eso la volvía el **lienzo** del universo (aguanta saturados que las otras dos no) **y a la vez** la dejaba sin nada que un color pudiera encender. Con el iris azul eso cambia: ahora tiene un eco propio.

- **✅ Le favorece:** frío saturado — magenta eléctrico, rosa neón, UV violeta, gunmetal, carbon black, oxblood — y ahora **el azul, que es el eco de su iris nuevo**.
- **⚠️ Ojo con:** el cálido claro y amarillento (champán pálido, coral, peach) contra un subtono frío y un platinado tira el pelo a latón. Si se usa dorado, va **desaturado/oscurecido** (antique gold, oro viejo), nunca champán brillante.
- **📏 Medición 04/09 (59 outfits):** rosa **78,0%** + cromo **74,6%** — su ventaja de lienzo se estaba gastando en **una sola combinación**, y cromo en la prenda + strobing de cromo en la cara + pelo platinado funden el look en una masa plateada. Azul solo **8,5%**: su jugada más barata desde hoy.

> 🔒 **DECISIÓN DE LA AMA (04/09/2026) — manda sobre lo de arriba:** *"si o si en ele y miss doll se quedan el plateado, dorado y gold rose"*. **Plata/cromo, dorado y rose gold se quedan como familias plenas de Miss Doll**, incluido el dorado que el análisis marca como su peor calce. Es decisión editorial suya y gana; lo único que se conserva del análisis es la **recomendación técnica** de preferir el dorado oscurecido al champán pálido — recomendación, no regla.

> 📊 Estudio completo con muestras a la vista: artefacto **Colorimetría de La Voûte** (04/09/2026).

### 5.2c · 💄 Colorimetría del MAQUILLAJE (Ama 04/09/2026)

> *"lo que quiero que quede hoy es la colorimetria para la ropa, y maquillaje de las muñecas"*
>
> Hermana de la §5.2b, que gobierna el color de la **prenda**. Esta gobierna el color de la **cara**: sombra, ceja, labio, iluminador, rubor y uñas. Nace del mismo estudio del 04/09/2026, medido sobre **618 looks de Ele · 75 de Miss Doll · 75 de Anaïs**. Los cuatro anclajes de cara (pelo · piel · ojos · labios) están en la §5.2b y **no se repiten aquí**: esta subsección los usa.

**Su eje (§5.2b):** subtono **frío declarado**, platinado, e iris cobalto desde el 04/09. Es la única con **labio variable** de las tres — tiene 3 grados de libertad de maquillaje (sombra · labio · uñas) contra 1 de Anaïs y 1 de Ele.

**🪞 Su colisión real es de CARA CONTRA PRENDA, no de vestuario.** Medido el 04/09:

| Plano plateado | Frecuencia |
|---|---|
| `blinding chrome strobing` en el ADN | **75/75 looks** |
| Sombra gris / cromo / plata | **41%** (31 de 74) |
| Cromo/plata en la prenda (§5.2b) | **74,6%** |
| Pelo platinado | siempre |

Cuatro planos del mismo metal sobre la misma cara: **el ojo desaparece dentro del strobing.** La §5.2b midió tres y no contó el cuarto, que es el maquillaje.

- **🔒 REGLA DE DOS PARTES (nueva, 04/09/2026)** — no es un token, es un candado:
  1. Si la **sombra** del look es gris / cromo / plata → el iluminador baja a `soft pearl strobing highlight on cheekbones and brow bone` (se declara con `adn_overrides` sobre `blinding chrome strobing highlight`).
  2. Si la **prenda dominante** es cromo / plata → la sombra **no** puede ser gris / cromo / plata.
- **✅ Le favorece:** frío saturado — magenta eléctrico, UV violeta, gunmetal — y sobre todo **el azul cobalto y el zafiro, eco de su iris nuevo**. Sombra azul hoy: **4 de 74 looks (5%)**. Es su jugada más barata, igual que el 8,5% de azul en vestuario. Labio **vino / oxblood / berry / rojo azulado**: el 43% de vino que ya lleva es su mejor calce — sobre subtono frío, el rojo azulado es el único que no amarillea la piel.
- **⛔ Vetado desde hoy:** `coral eyeshadow` · `peach eyeshadow` · `terracotta lips` · `coral lips` · `pastel eyeshadow` · `low-pigment eyeshadow` · `washed-out eyeshadow`. La baja pigmentación entraba **por el positive** pese a que su negative ya prohibía `natural/subtle makeup`: seis looks seguidos (L25-L30, 55 poses) con `soft pastel pink shimmer`.
  > 🔒 **El dorado NO está vetado**, aunque el análisis lo marque como su peor calce cálido. Decisión de la Ama del 04/09 (*"si o si en ele y miss doll se quedan el plateado, dorado y gold rose"*). Recomendación técnica que sí se conserva: si va dorado, **oscurecido** (antique gold), nunca champán pálido.
- **✅ Bien tomado, no tocar:** la ceja `dark smoky taupe-grey` deliberadamente **más oscura que el pelo** es la mejor decisión colorimétrica de las tres — es lo único que le da estructura a una cara sin contraste natural.

**⚠️ Incumplimientos medidos de su propia §5.5.8, sin corregir (looks materializados):** tres labios violan la prohibición dura de §5.4 — **L14** `hot pink magenta` y **L66** `bubblegum pink` (el rosa es firma de Ele, no suya) y **L23** `nude-glam` (el nude está prohibido). Y **10 pares consecutivos** repiten tono de labio (L25-L31 `deep red`, L48-L51 `blood-red`) más 5 de sombra. No se regeneran; quedan como registro de que **la regla existía y nadie la medía**.

> 📊 Estudio completo con muestras a la vista: artefacto **Colorimetría de La Voûte** (04/09/2026).

### 5.3 · Calzado (canon inamovible — lo único 100% obligatorio del vestuario, 11/08/2026)

- **Regla:** cualquier tipo de calzado sirve — stiletto pump, bota, sandalia — pero **SIEMPRE con plataforma**. `tacones/botas/sandalias siempre con plataforma` (directiva Ama 11/08/2026, tras derogar el corsé obligatorio: esto pasa a ser la única pieza inamovible del BLOQUE B).
- **Altura mínima:** plataforma 6" o superior (el canon histórico usa 8").
- **Prohibido:** flats, block heel, **chunky heel**, kitten heel, wedge, descalza, sandalia/tacón/bota **sin plataforma**, **mules / tacones destalonados sin sujeción al talón**, **Mary Jane (correa al empeine estilo colegial)** — prohibido en TODOS los arquetipos, no solo Girly Girl (Ama 03/09/2026, ver §6).
- **🔻 Mules — PROHIBICIÓN ABSOLUTA (Ama 20/08/2026):** quedan terminantemente **PROHIBIDOS los tacones/sandalias estilo mule** (destalonados o sin sujeción en el talón/tobillo). Solo calzado con sujeción segura: pumps cerrados con plataforma, sandalias de tiras con pulsera al tobillo o botas altas.
- **🔻 Botines/ankle boots — FUERA de la rotación (Ama 11/08/2026):** cuando el calzado elegido es bota, solo **knee-high (bajo rodilla)** o **thigh-high/over-the-knee (sobre rodilla)** — nunca ankle boot corto.
- **Atributos obligatorios del token** (nombrar los 5 en cada pose): altura · tipo de plataforma · material/acabado · color · tipo de tacón (`razor-thin metal needle heel`).
- ⚠️ La palabra `chunky` y `mule` van **solo en el negative**, jamás en el positive.

### 5.4 · Prohibiciones absolutas

| Prohibido | Sustituto autorizado | Directiva |
|---|---|---|
| Flequillo / frente cubierta | frente despejada, `NO BANGS` | Canon V3.5 Stealth |
| Labios **rosados** (rosa = firma de Ele), nude o mate | maquillaje elegido por la ocasión del look, alto brillo | Lo inviolable es la **forma** (ultra-plump, overlined, cupid's bow, high-gloss wet), no el color — §2 (Ama 02/08) |
| Cuero como pieza principal | látex/PVC/vinilo; cuero solo en corsé/arnés/accesorio | Canon materiales |
| **Tacones / sandalias estilo mule** | pumps con plataforma, sandalias con pulsera al tobillo, botas altas | **PROHIBICIÓN ABSOLUTA (Ama 20/08/2026).** Mules prohibidos |
| **Batas cortas / mini robes** | batas al tobillo o arrastrando hasta el suelo (`floor-length` / `ankle-length`) | **PROHIBICIÓN ABSOLUTA (Ama 20/08/2026).** Mínimo al tobillo |
| Tatuajes | piel limpia | Salvo variante legacy pedida por la Ama |
| Texto/nombre sobre prenda | choker liso, O-ring, hardware sin letras | Regla transversal del repo |
| Sonrisa amplia / actitud juguetona | Face of the Pole | Principio de registro — **excepción única: arquetipo Girly Girl (§6), ver ahí las reglas** |
| **Cualquier prop/setting/tono de infancia** (peluches, dollhouse, cuarto de niña, "playful giggly" infantil) — incluso en Girly Girl | Glamour adulto exagerado: boudoir/penthouse/salón de belleza de lujo, sonrisa radiante/sensual de mujer adulta | **PROHIBICIÓN ABSOLUTA (Ama 11/08/2026).** Hiperfem ≠ niñita rosada. Ver nota en §6 |
| **🎀 Vocabulario de vestuario infantilizante** — moños/lazos decorativos como accesorio de prenda, charms o prints en forma de corazón, mangas abullonadas (puffed sleeves), medias/calcetines cortos con volados, calzado **Mary Jane** — incluso en Girly Girl | Silueta bodycon/plunge/cut-outs, hardware cromado o dorado tipo joyería, pumps o botas con plataforma del §5.3 (nunca Mary Jane) | **PROHIBICIÓN ABSOLUTA (Ama 03/09/2026).** Misma deriva que la fila de arriba, esta vez por el lado del accesorio de prenda, no del prop. Diagnosticado sobre imagen real (Look 66) — ver nota en §6 |
| **👙 Calzón de cobertura total** — brief de talle alto, boyshort, hipster, culotte, tap pant, bikini bottom que tape el asiento | **tanga o g-string, siempre** (delantero angosto, cintura sobre el hueso de la cadera, atrás una tira fina) | **Ama 13/08/2026.** Ancla `BOTTOM_CUT_LOCK` en `anclas_siempre`. Su corte se **nombra** en el BLOQUE B (§5.5) — no basta con "bikini bottoms" |
| **🦵 Piernas abiertas usando vestido, falda, bata o túnica** | rodillas y muslos juntos · una pierna cruzada sobre la otra · las dos piernas plegadas a un lado si va baja | **Ama 13/08/2026, transversal a las tres muñecas.** Ancla opt-in `DRESS_LEG_CLOSURE`. ⚠️ **La cláusula «cuando el look es de falda» quedó SUPERADA el 29/08/2026:** las piernas abiertas de Miss Doll se eliminaron en todos sus looks, lleve o no falda (§4). Esta fila sigue vigente como regla transversal de las tres muñecas |

### 5.5 · Campos obligatorios de descripción

El BLOQUE B debe nombrar, sin excepción:

1. **Corsé — OPCIONAL, no obligatorio** (derogado 11/08/2026, ver nota abajo). Cuando aparece, sigue siendo el centro del look; cuando no, el abdomen tonificado queda al descubierto como el foco.
2. Prenda principal: material exacto, color exacto, corte, acabado (gloss/matte), fit.
3. Hardware: chrome, anillas, hebillas, webbing — tipo y posición en el cuerpo.
3b. **👙 Corte del calzón — obligatorio nombrarlo (Ama 13/08/2026).** Cuando el look lleva calzón, bikini bottom o la entrepierna de un body/teddy/bañador, el BLOQUE B escribe el **corte** con todas sus letras: `thong` o `g-string`. **Prohibido dejarlo en `bikini bottoms` / `panties` a secas** — nombrar la prenda y no su corte es exactamente lo que produjo el calzón de talle alto del Look 801 de Ele (13/08/2026): el atributo que no se nombra lo resuelve el generador, y su default es cobertura total. El linter lo caza (`lint_prompts_personaje.py`, aviso `BOTTOM_CUT_LOCK`).
4. Medias/hosiery **si aplica** — y con frecuencia NO debe aplicar (corrección 11/08/2026: 5 de los primeros 7 looks llevaron medias, la Ama lo notó como repetitivo). **Ventana anti-repetición nueva:** no más de 2 looks consecutivos con medias; alternar con piernas desnudas, fishnet, o tratamiento distinto (leggings, botas altas que cubren la pierna). Cuando sí aplica: denier, tipo, color.
5. **Calzado con plataforma, sus 5 atributos (§5.3) — esto SÍ es obligatorio siempre.**
6. Accesorios: cada pieza con su posición.
7. Dónde aparece el **rosa firma** (§5.2).
8. **Maquillaje de color** (agregado 11/08/2026 — hueco real: se estaba copiando "intense shimmer smokey eye" fijo en TODOS los looks, violando la regla de variar por ocasión): color exacto de sombra de ojos + color exacto de labios, coordinados con la paleta del look. La **técnica** (winged eyeliner, smokey blending, mega lashes, strobing, forma ultra-plump de labios) es fija en BLOQUE A; el **color** es 100% variable y va en BLOQUE B. Labios: nunca rosado (firma de Ele), nunca nude natural, nunca mate. **No repetir el mismo tono de sombra en dos looks consecutivos.**
9. **Uñas** (agregado 11/08/2026): forma (stiletto/coffin-ballerina/almond/square), largo y color/acabado — coordinado con la paleta del look. Nunca se omite; la calidad base (largas, impecables, gloss) ya viene en BLOQUE A, esto solo fija la variante del día. **🔒 Sujeto al mismo Token Bloqueado que el vestuario (Ama 11/08/2026):** la forma/largo/color de uñas se fija UNA vez por look y se copia idéntica en las 7 poses — incluidas Glacial Command y POV, donde las manos quedan más cerca de cámara y es más tentador "afinar" la descripción. Ninguna pose describe las uñas distinto a las otras.

> 🔓 **Corsé derogado como obligatorio (Ama 11/08/2026):** hasta hoy el corsé era "centro del look, ningún outfit de Miss Doll carece de él" (§8, §9 viejos). Con el nuevo abdomen tonificado (§2, rediseño de cuerpo del mismo día) la Ama pidió dejarlo de exhibir sin corsé cuando el look lo pida — el corsé sigue siendo válido y sigue siendo su pieza de firma más reconocible, pero ya no es un campo obligatorio en cada BLOQUE B. **Lo único que sigue siendo 100% inamovible es el calzado con plataforma (§5.3).**

### 5.6 · 👗 Biblioteca de arquitecturas de prenda (Ama 18/08/2026)

> **Por qué nace, medido antes de escribirla.** La Ama levantó sobre el batch L21-L25: *"¿por qué salieron puros bikini y bodysuit?"*. Se auditaron los 25 looks contra su BLOQUE B y su lectura era correcta y además corta: **desde el Look 15 hasta el 25 van once looks seguidos sin un solo vestido, falda ni pantalón**. Último vestido L13, última falda L09, último pantalón L12 — todo lo cubierto vive en la primera era y nada después. Flota completa: **72% arquitectura de piel** (lencería 8 · bodysuit 5 · bikini 3 · catsuit 2) contra **28% cubierta**, y ese 28% entero está en L01-L14.
>
> **La causa NO fue el déficit de arquetipos:** se midió y está impecable (Club 20% vs meta 18 · Bikini 16% vs 15 · Calabozo 12% vs 13 · VIP 12% vs 12 · Gym 12% vs 12 · Girly 12% vs 12 · Penthouse 8% vs 9 · Editorial 8% vs 9). El log del motor (`99_Sistema/logs/outfit_engine.jsonl`) confirma 50 builds el 17/08 con **0 fallas**. Nada falló técnicamente.
>
> **Las tres causas reales:**
> 1. **§6 gobierna el ESCENARIO, no la PRENDA.** Los ocho arquetipos dicen *dónde está*, nunca *qué arquitectura lleva puesta*. La prenda quedaba a mano alzada en cada look, y a mano alzada un personaje de club sale siempre en segunda piel.
> 2. **§7 tenía la ventana mal alcanzada:** *"silueta ≥3 looks del mismo arquetipo"*. Como el batch rota arquetipo en cada look, **la ventana no se disparaba nunca**. En Ele la misma regla sí ata porque tiene ~50 looks por sub-arquetipo; con 25 repartidos en 8, no.
> 3. **Cuatro reglas empujaban al mismo lado y ninguna de vuelta:** arquetipo Bikini/Lencería al 15% (13/08) · `BOTTOM_CUT_LOCK` de tanga universal (13/08) · corsé derogado con el abdomen como foco (11/08) · piso de bata abierta en VIP/Penthouse (12/08).
> 4. **Y la raíz:** Ele tiene `00_Ele/biblioteca_siluetas.md`; Anaïs tiene dos (§5.6a vestidos D1-D10 + §5.6 lencería). **Miss Doll no tenía ninguna.** Su vestuario no rotaba porque no había de dónde rotar — el mismo modo de falla que su repertorio de cámara antes del 13/08 (§4).

**Las diez arquitecturas. La columna que manda es COBERTURA, no el estilo:**

| # | Arquitectura | Cobertura | Descripción | Arquetipos naturales |
|---|---|---|---|---|
| **M1** | **Bodysuit segunda piel** | 🔥 piel | Una pieza ceñida de vinilo/látex, cutouts geométricos, escote plunge, fondo en tanga | Club · Editorial · Calabozo |
| **M2** | **Bikini / micro dos piezas** | 🔥 piel | Triangle top + tanga, crystal mesh o vinilo, la prenda ES el sujeto de la toma | Bikini/Lencería · Gym |
| **M3** | **Conjunto de lencería** | 🔥 piel | Sujetador (demi/balconette/plunge/halter) + tanga + liguero + medias opcional | Bikini/Lencería · VIP · Girly |
| **M4** | **Corsetería + tanga** | 🔥 piel | Corsé overbust/underbust estructurado como pieza central, pierna libre | Calabozo · Editorial · VIP |
| **M5** | **Arnés / fashion-bondage sobre piel** | 🔥 piel | Correas finas tipo joyería como prenda principal, mínima tela | Calabozo · Club |
| **M6** | **Vestido de segunda piel** | 👗 **cubierta** | Mini o midi de vinilo/látex/wet-satin, ceñido, con tajo alto o espalda descubierta | Penthouse · Editorial · VIP · Club |
| **M7** | **Minifalda + top** | 👗 **cubierta** | Dos piezas cubiertas: falda de vinilo/PVC + crop top, bralette estructurado o corsé encima | Club · Girly · Editorial |
| **M8** | **Pantalón / legging + top** | 👗 **cubierta** | Legging de látex, bike short alto, pantalón de vinilo — con top o bra deportivo | Gym · Club · Penthouse |
| **M9** | **Catsuit / unitard de pierna completa** | 👗 **cubierta** | Cuerpo entero **hasta el tobillo**. El BLOQUE B **debe nombrar el largo de pierna** (`full-length legs to the ankle`) — si no lo nombra, no cuenta como cubierta | Calabozo · Gym · Editorial |
| **M10** | **Slip dress / vestido de malla sobre lencería** | 👗 **cubierta** | Vestido translúcido o de malla que deja leer el conjunto debajo — cubre la silueta sin tapar el morbo | VIP · Penthouse · Girly |

> 🚫 **La bata abierta y la capa NO son arquitectura cubierta — son capa.** Esto es exactamente lo que pasó en L22 (bralette + capa de vinilo) y L25 (lencería + bata de chiffon): las dos se leen como lencería porque la pieza abierta **enmarca, no cubre**. La bata sigue siendo obligatoria donde §5.1b la manda; simplemente no paga la cuota de §8. Se cuenta lo que hay **debajo**.

> 🔒 **Nombrar el largo es parte del ancla, igual que en `BOTTOM_CUT_LOCK`.** M9 solo cuenta como cubierta si el BLOQUE B escribe el largo de pierna con todas sus letras. El atributo que no se nombra lo resuelve el generador — y su default acá es cortar en la cadera y devolver otro bodysuit.

---

## §6 · Arquetipos y Metas (rediseñado 11/08/2026 — filtro stripper + domme + fashionista + cuerpo de gimnasio)

| Arquetipo | Descripción | Meta |
|---|---|---|
| **Club / Escenario** | Pole, tarima, luz neón, revue | 18% |
| **👙 Bikini / Lencería Erótica** *(nuevo 13/08/2026 — Ama)* | **La prenda ES el look.** Conjunto de dos piezas como sujeto de la toma: micro bikini, triangle top, conjunto de lencería (sujetador + tanga + liguero), bodysuit de tiras, teddy, bañador de recortes — en vinilo/PVC/látex/wet-satin/crystal mesh. Escenarios de **piel y agua o de tocador**: borde de piscina, cabana de beach club, spa privado, boudoir, backstage de sesión. **Sin capa que lo tape**: nada de abrigo, blazer ni bata cerrada encima (la bata abierta sí, si deja ver el conjunto entero). **El calzón va SIEMPRE en tanga o g-string** (§5.4). | 15% |
| **Calabozo / Dungeon** | Sesión de dominación, bondage de diseño, mobiliario elegante *(desc. suavizada 11/08 — ver recalibrado de materiales §5.1, ya no "arneses, mobiliario de dominación" industrial)* | 13% |
| **VIP / Privado** *(nuevo 11/08, reemplaza a Uniforme Privado)* | Sesión exclusiva uno-a-uno, lencería-fetiche lounge, energía de sala privada — distinto de Calabozo (no es dominación) y de Penthouse (es *con* alguien, no ella sola) | 12% |
| **Gym / Athletic** *(nuevo 11/08 — justificado por el cuerpo de gimnasio del §2)* | Sujetador deportivo de vinilo + sudor glam + plataforma deportiva son la base fija; **la pierna NO siempre va en leggings** (corrección 11/08, Look 05 default a leggings sin variar) — rotar entre leggings, bike shorts, unitard con cutouts, piernas desnudas con calcetín corto cromado, etc. | 12% |
| **🎀 Girly Girl** *(nuevo 11/08 — ÚNICO arquetipo con excepción de expresión, ver §2 · redefinido 03/09/2026)* | **Hiperfem ADULTA — feminidad exagerada de MUJER, no "cosa rosa".** El concepto no es rosa+pastel, es curva extrema, glamour sexual sin filtro, actitud bombshell — hiperfem es un grado de feminidad, no una paleta. Se expresa en vinyl/PVC gloss saturado (raíz Girly redefinida §5.2 — hot pink/fucsia/magenta, nunca pastel/baby-tone por defecto), silueta bodycon/sensual de alta costura (plunge, cut-outs, hardware cromado/dorado), ambientes de boudoir/penthouse/salón de belleza de lujo. **Expresión cálida y sonriente** — quiebre real de personaje, contraste deliberado con su registro habitual. **La feminidad exagerada vive en la silueta, la actitud y el color saturado — nunca en el accesorio decorativo ni en el tono suave** — ver prohibición de vocabulario abajo. | 12% |

> ⚠️ **Corrección de fondo (Ama 11/08/2026, misma sesión):** el primer intento de este arquetipo (Look 02 v1) confundió "hiperfem" con "niñita rosada sexualizada" — metió peluches, dollhouse y un tono "playful giggly" que leía infantil. **Esa lectura queda PROHIBIDA explícitamente.** Hiperfem = feminidad adulta exagerada (glamour, poder, lujo, sensualidad de mujer adulta), nunca estética o props de infancia/guardería. Ver prohibición dura en §5.4.
>
> ⚠️ **Segunda corrección de la misma deriva, esta vez de VESTUARIO no de props (Ama 03/09/2026).** La primera corrección cerró props/setting/tono; la deriva volvió por el lado del **accesorio de prenda**. Auditado el Look 66 "Bubblegum Bow Couture" (29/08) contra la imagen real generada: *"el bottom es como un calzón de niña gigante... este girly girl se va más por esas cosas como medias de niñas pequeñas y no me gusta"*. Su BLOQUE B llevaba `oversized architectural bow`, `pink enamel heart charm`, `short puffed cap sleeves` y **`Mary Jane stiletto pumps`** — el moño, el corazón, la manga abullonada y el Mary Jane (literalmente el zapato-código de colegiala en moda) combinados leen como disfraz infantil sin importar que el texto pidiera tanga; el generador termina resolviendo el conjunto entero hacia bloomers/calzón cubierto para que combine con la silueta que "ve". **Se saca del vocabulario del arquetipo, con prohibición dura en §5.4:** moños/lazos decorativos, charms/prints en forma de corazón, mangas abullonadas (puffed sleeves), medias/calcetines cortos con volados, y calzado Mary Jane. Lo que SÍ carga la feminidad exagerada de Girly Girl: el color saturado (§5.2, redefinido el mismo día — hot pink/fucsia, no pastel/baby-tone), el gloss/wet-look, la silueta bodycon/plunge, y el hardware cromado o dorado como joyería — nunca el adorno de mercería ni el tono suave. **Corrección de raíz el mismo día (Ama, en vivo):** *"hiper fem no quiere decir necesariamente rosa y pasteles y cosas de menores... quiero hiper fem de adultas"* — el pastel salió del default de la raíz cromática (§5.2) porque es el registro que más se lee como infantil en cualquier generador. Hiperfem = grado de feminidad exagerada (curva, actitud, glamour sexual), no una paleta.
| **Penthouse / Off-duty** | Su espacio, registro frío fuera del trabajo | 9% |
| **Editorial / Portada** | Sesión de foto pura, fondo controlado | 9% |

> ❌ **Uniforme Privado — eliminado 11/08/2026:** "protocolo, de servicio, latex couture estructurado" leía como el residuo industrial que se sacó de §5.1. Reemplazado por VIP/Privado, que cubre el mismo nicho de sesión exclusiva sin el tono de utilería.

> 👙 **Bikini/Lencería Erótica vs. VIP/Privado — dónde está la frontera (13/08/2026).** Los dos usan conjunto de dos piezas, y sin frontera escrita se canibalizan (ya pasó con Uniforme Privado). **VIP es una ESCENA:** hay alguien más implícito, la energía es de sala privada, la bata y el lounge mandan, la lencería es contexto. **Bikini/Lencería Erótica es un OBJETO:** ella sola, el conjunto es el sujeto de la foto, el cuerpo y la prenda ocupan el cuadro, el escenario existe para lucirlos (agua, mármol, tocador). Si la toma funcionaría igual sin el escenario, es Bikini/Lencería; si el escenario es la mitad del morbo, es VIP.

- **Regla de déficit:** el arquetipo bajo meta manda sobre el gusto.
- **Prioridad de desempate:** Club > Bikini/Lencería > Calabozo > VIP > Gym > Girly Girl > Penthouse > Editorial.
- **Suma verificada 13/08/2026:** 18 + 15 + 13 + 12 + 12 + 12 + 9 + 9 = **100%**. El 15% del arquetipo nuevo salió prorrateado de los siete existentes, no de uno solo.
- **⚠️ Excepción de negative prompt SOLO en Girly Girl:** el negative base (§3) incluye `warm smile, laughing` porque el resto de sus arquetipos exige cero calidez. En un prompt de Girly Girl, **sacar esos dos términos** del negative — de lo contrario el prompt se contradice a sí mismo.

---

## §7 · Ventanas Anti-Repetición

| Elemento | Ventana |
|---|---|
| **Arquitectura de prenda (§5.6, M1-M10)** | **≥ 3 looks GLOBALES — no por arquetipo** ⚠️ ver nota |
| Silueta (detalle: escote, corte, estructura) | ≥ 3 looks del mismo arquetipo |
| Setting / escenario | ≥ 3 looks del mismo arquetipo |
| Modo cromático monoblock | máx. 2 consecutivos globales |

> ⚠️ **La ventana de arquitectura es GLOBAL a propósito (Ama 18/08/2026).** Las otras dos filas están alcanzadas *por arquetipo*, y ese alcance es exactamente lo que dejó pasar once looks seguidos sin prenda cubierta (§5.6): como el batch rota arquetipo en cada look, dos vecinos casi nunca comparten arquetipo y la ventana no se disparaba **jamás**. La arquitectura de prenda se mide contra los **3 looks anteriores del roster completo**, sin importar dónde esté parada.

- **Outfit único:** sí. Miss Doll no repite outfit.
- **La rotación aplica también DENTRO de la familia de piel.** La Ama lo dijo explícito (18/08/2026): *"me gusta el bikini y bodysuit, pero quiero ver variedad de outfits"*. La cuota de §8 le pone piso a lo cubierto; **esta ventana obliga a que M1-M5 tampoco se repitan entre sí** — tres bodysuits en cuatro looks viola la regla igual que tres vestidos seguidos. Ninguna de las dos reglas saca el bikini ni el bodysuit del repertorio: los ordena.

---

## §8 · Cuotas Vivas

| Cuota | Frecuencia | Alcance |
|---|---|---|
| **Rosa firma presente** | **todos los looks** | Cualquier prenda, calzado o accesorio |
| **Calzado con plataforma** | **todos los looks, sin excepción** | La única pieza 100% inamovible del vestuario (11/08/2026) |
| ~~Arquitectura de corsé visible~~ | ~~todos los looks~~ | **Derogada 11/08/2026 — ahora opcional, ver §5.5** |
| **👗 Silueta cubierta** *(nueva 18/08/2026)* | **≥ 1 de cada 4 looks nuevos** | Global, cualquier arquetipo. "Cubierta" = **M6-M10** de §5.6 (vestido · falda+top · pantalón/legging · catsuit de pierna completa · slip dress). **La bata abierta y la capa NO pagan esta cuota** — enmarcan, no cubren: se cuenta lo que hay debajo. Vigente **desde el Look 26**; el roster L01-L25 no se retrofitea (convención retrofit-al-tocar) |
| **👘 Bata abierta** *(nueva 12/08/2026)* | **≥ 1 de cada 2 looks nuevos de VIP/Privado y Penthouse/Off-duty** | Exclusiva de esos dos arquetipos — no aplica a Club/Calabozo/Gym/Girly Girl/Editorial. Piso medido sobre el roster actual (2/4); no baja hacia adelante. Alterna con slip-dress de una pieza. Ver §5.1b |

---

## §9 · Banderas Rojas Específicas

- ✅ **RESUELTO 05/08/2026:** el histórico `C-1.png…C-6.png` se renombra a `miss_doll_<N>_<pose>.png` con los slugs de §4 (`standing/back_view/seated/side_profile/glacial_command/odalisque` — sin `pov`, no existía esa toma en el set legacy). Script: `99_Sistema/scripts/mantenimiento/renombrar_legacy_multipersonaje.py`, corre en la máquina visual (0 PNG en disco acá).
- El BLOQUE A y el outfit vienen mezclados en el prompt base histórico (regla 05) → si al escribir un look aparece el bodysuit rosa neón "de fábrica", **es contaminación del Bloque A**: sepáralo.
- ~~Look sin arquitectura de corsé → no es Miss Doll~~ **derogado 11/08/2026** — el corsé es opcional ahora, ver §5.5.
- **Look sin calzado de plataforma → sí sigue siendo violación de canon.** Es la pieza que reemplazó al corsé como el único campo 100% inamovible.
- Look sin rosa en ninguna parte → viola su cuota firma.
- Labios **rosados** (el rosa es firma de Ele, no suya), **nude** o **mate** → viola canon. El **color** se elige según la ocasión del look (§2, Ama 02/08); lo inviolable es la **forma**: ultra-plump, overlined, cupid's bow, high-gloss wet.

---

## §10 · Ensamblado y Anclas (contrato con el motor)

> 🔧 **Agregado 12/08/2026 con el `outfit-engine` v2.0.** Esta sección NO define nada nuevo del personaje: declara **cómo se ensamblan sus prompts** y qué anclas anti-defecto le aplican. El texto literal de las anclas vive en `99_Sistema/scripts/visual/anclas_universales.json` (dueño único) — aquí se **apunta**, jamás se copia.

| Campo | Valor |
|---|---|
| **Registro en el motor** | `anclas_universales.json` → `personajes.miss_doll` |
| **Nombre del slot 5** | `Glacial Command` |
| **Ensamblador** | `PromptBuilder("miss_doll").build(bloque_a, bloque_b, slot, pose, setting)` |
| **Negative del look** | `PromptBuilder("miss_doll").build_negative(<base del §3 de arriba>)` — base propia **+ capa universal** anti-collage/anatomía/selfie |
| **Verificación obligatoria** | `python 99_Sistema/scripts/visual/lint_prompts_personaje.py miss_doll` |

**Anclas por slot:** las del mapa por defecto del motor, con **un override**:

| Slot | Ancla del motor | Sustituto | Por qué |
|---|---|---|---|
| Odalisque | `RECLINE_ANCHOR` | **`FLOOR_SEAT_ANCHOR`** | Su Odalisque es **floorwork de alta escuela** (§4): trabaja a nivel del suelo — sentada con las rodillas recogidas y juntas, gateo felino, sirena, cobra, backbend—, **no reclinada**. Aplicar el ancla de recumbencia de Ele contradiría su propio canon de pose. *(Decía «sentada en el piso con piernas en V» hasta el 29/08/2026, cuando la Ama eliminó las piernas abiertas.)* |

**📐 Orientación de Odalisque — la única que ALTERNA (Ama 17/08/2026):** Ele y Anaïs tienen Odalisque reclinado, así que `ASPECT_HORIZONTAL` va fijo en el mapa por defecto del motor. El de Miss Doll es sentado en el piso (Throne en Suelo) — ninguna orientación es "la" natural del encuadre, y la Ama pidió variedad: *"Miss Doll debe tener Odalisque en vertical y horizontal"*. Por eso su Odalisque **no lleva** `ASPECT_VERTICAL` ni `ASPECT_HORIZONTAL` fijos en `anclas_universales.json` — se resuelve con `PromptBuilder("miss_doll").orientacion_odalisque(look_number)` (alterna por paridad del número de look) y se pasa a `build()` vía `extra_anclas=[...]`. Es el único slot de las tres muñecas que se decide así; todo el resto sigue fijo en el mapa.

> 🩹 **Cicatriz del 11/08/2026:** sus 98 prompts se escribieron con `[BLOQUE A] + [BLOQUE B], …, [BLOQUE C setting]` **literales**, sin `Ubicacion`, sin `Tags` y con el negativo etiquetado de una forma que el parser de la app no reconoce. Medido sobre el archivo commiteado: **98/98 prompts con placeholder · 0/14 looks con negativo · 0/14 con ubicación**. Reescritos el 12/08/2026.

🚨 **Cada prompt de la galería va FINAL Y EXPANDIDO.** El ADN completo, el outfit completo, las anclas y el setting, uno detrás de otro dentro del bloque de código. Un `[BLOQUE A]` entre corchetes dentro de un prompt no es una abreviatura: es un prompt roto que la app manda tal cual al generador.
