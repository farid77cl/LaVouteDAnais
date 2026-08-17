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

```text
hyper-realistic high-end editorial glamour photography of Miss Doll, adult glamorous woman, (soft rounded oval face:1.1), smooth softly rounded jawline, (soft gently curved full cheekbones:1.1), small refined rounded chin, delicate refined features COMMANDING, sharp platinum blonde asymmetric angled bob, sleek straight razor-cut strands, ice platinum highlights, clear exposed forehead, NO BANGS, (small refined perky upturned nose:1.2), (huge oversized round almond-shaped cold pale steel grey eyes, wide open eye opening:1.4), pale icy grey iris with sharp dark limbal ring, (fixed dominant professional gaze zero warmth, slow appraising once-over gaze sweeping head to toe with cold superiority:1.3), chin elevated 5 degrees, (bold precisely filled brow makeup, dark smoky taupe-grey brow color noticeably darker than the platinum hair for maximum contrast, extremely high dramatic raised arch positioned high on brow bone, sharp clean tapered tail, thick clearly visible brow shape:1.5), HEAVY GLAMOUR editorial makeup with (thick sharp angular winged eyeliner upticked pointed wing tip:1.2), intense shimmer smokey eye technique (color exacto de sombra se fija en BLOQUE B por look, ver §5.5 — NUNCA repetir el mismo tono en looks consecutivos), (impossibly long mega XXL individual false lashes at outer corners dramatic cat-eye:1.2), (blinding chrome strobing highlight on cheekbones nose bridge and brow bone:1.2), (soft gentle contour warm shadow under cheekbone:1.0), (aggressively overlined voluminous ULTRA PLUMP high-gloss wet lips exaggerated cupid's bow full pillowy lips mirror-gloss finish:1.3) curved into a (subtle smug smirk, one corner of the mouth raised:1.2), human realistic face DOMINANT smirking expression, pale cold porcelain white skin, editorial realistic human skin texture subtle visible pores, cold undertone, sculptural EXTREME hourglass silhouette, (toned midriff, subtly defined abs with soft natural muscle separation, faint visible obliques:1.2), (slender delicate shoulders, long lean toned arms with soft subtle muscle tone, not bulky, feminine and graceful:1.2), (long lean slender toned legs, soft subtle thigh definition, not muscular, elegant model proportions:1.2), (massive full round chest, obviously artificial enhanced implants, perfectly spherical gravity-defying shape, high improbable profile, unmistakably augmented:1.4), dramatic alluring plunging neckline, deep prominent cleavage, aggressively narrow cinched waist, full wide hips, tall lean slender commanding figure, rigid upright posture, square shoulders pulled back, (impeccably manicured long glossy nails:1.1)
```
> Nota de uñas: la calidad (largas, impecables, gloss) es fija aquí; forma/largo exacto/color varían por look en BLOQUE B (§5.5).

> 💪 **Rediseño de cuerpo (Ama 11/08/2026, misma sesión que el rediseño de rostro):** cuerpo con **evidencia de gimnasio diario** — abdomen con definición suave y natural, pero **hombros/brazos/piernas delgados y esbeltos, NUNCA voluminosos** (primer intento salió "muy grueso", corregido a slender/lean/delicate/graceful). **Pecho aumentado a artificial obvio** — `massive, obviously artificial enhanced implants, perfectly spherical gravity-defying shape` — antes solo decía "extra full round chest". Aprobado explícito: *"mucho mejor, deja fijo estos cambios"*.
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
- **Pecho artificial obvio, masivo, perfectamente esférico** (rediseño 11/08/2026) — antes solo "extra full round chest", ahora explícitamente `obviously artificial enhanced implants`.
- **Uñas siempre impecablemente manicuradas, largas y cuidadas** (agregado 11/08/2026 — hueco real, no había ninguna mención de uñas en el ADN hasta hoy). La **calidad** (largas, impecables, gloss) es fija en BLOQUE A; la **forma exacta** (stiletto, coffin/ballerina, almond, square) y el **largo/color/acabado** varían por look y se fijan en BLOQUE B (§5.5) — nunca uñas cortas, descuidadas, ni un look sin mencionarlas.

---

## §3 · Negative Prompt

**Base (siempre) — ampliado 11/08/2026 con los fallos reales detectados en el rediseño de rostro/cuerpo:**
```text
bangs, fringe, covered forehead, dark hair, brunette, ponytail, bun, childish face, teen, natural makeup, subtle makeup, nude lips, matte lips, rosy cheeks, warm natural skin tone, wax skin, plastic mannequin skin, tattoos, casual outfit, flat shoes, sneakers, block heel, chunky heel, vulgar cheap costume, slouched shoulders, warm smile, laughing, sharp angular face, angular jawline, thin invisible eyebrows, sparse pale blonde eyebrows, barely visible brows, faint eyebrows, eyebrows blending into skin, bodybuilder physique, overly muscular, bulky muscles, veiny muscles, grotesque six-pack, masculine muscle mass, thick bulky arms, thick muscular shoulders, wide muscular legs, thick calves, muscular bulky thighs, small chest, natural breasts, flat chest, corset, waist cincher, bustier, doll face, mannequin face, uncanny doll-like appearance, glassy doll eyes, porcelain doll aesthetic, full brief, high-waist brief, high-waisted panty, boyshort, boy shorts, hipster brief, culotte, tap pants, granny panties, bloomers, full-coverage bikini bottom, bikini bottom covering the buttocks, full seat coverage, legs spread apart under a dress, legs parted under a skirt
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
| 3 | Seated | Monarch Throne | `seated` | Sentada, piernas 60-90°, codos en reposabrazos, barbilla ladeada |
| 4 | Side Profile | Tres Cuartos Arrogante | `side_profile` | Giro ¾ hacia cámara, peso en una cadera, mirada fría de perfil |
| 5 | **Glacial Command** *(slot Ditzy de Ele, renombrado — no encaja una mirada vacía en su dominancia)* | Close Up Fría | `glacial_command` | **WAIST-UP** (cintura arriba): rostro grande y nítido + pecho prominente en el frame inferior + detalle del outfit superior legible · **UNA sola mano** en cuadro haciendo el gesto · **mirada FUERA de cuadro**, fría e indiferente |
| 6 | POV | Command POV *(nombre histórico)* | `pov` | **RETRATO SENSUAL DE INSTAGRAM** (thirst-trap de influencer): **mira a la cámara**, medio cuerpo, cara protagonista + escote abajo, **una sola mano**, `a single woman alone`. **NO es point-of-view literal** |
| 7 | Odalisque | Throne en Suelo con Crop | `odalisque` | Suelo, piernas en V abierta, codos en rodillas, crop en mano. **⚠️ Con vestido/falda/bata la V queda PROHIBIDA (Ama 13/08/2026):** se resuelve con las dos piernas plegadas hacia un lado (sirena), rodillas juntas. Ver §5.4 y el ancla `DRESS_LEG_CLOSURE` |

> 🦵 **Conflicto resuelto el 13/08/2026, no silenciado.** La directiva transversal de la Ama (*piernas cerradas con vestido*) choca de frente con la V abierta que es firma del Throne en Suelo. **Gana la directiva** (instrucción viva > canon de pose). La V no se elimina: queda reservada a los looks de calzón, bikini o catsuit, donde no hay falda que cerrar. Registrado también en `anclas_universales.json` → `personajes.miss_doll.conflicto_resuelto_13_08_2026`.

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

**Dónde vive esto en el motor:** `repertorios_pose.json` → `personajes.miss_doll` es el dueño único de las 49 sub-poses reales; este vocabulario es la **referencia** contra la que se auditan y se escriben nuevas variantes — no reemplaza el archivo. El slot `odalisque` (7 variantes) queda **pendiente de retrofit** para sumar floorwork dinámico junto a las sentadas actuales — retrofit al tocar, no migración masiva.

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

- **Token:** `sheer/satin/mesh <color> robe left open and draped off one shoulder` — material coherente con la paleta del look, bralette+brief o slip a juego debajo.
- **Regla de silueta:** bata **siempre abierta**, nunca cerrada — el abdomen tonificado (§2) es el foco, una bata cerrada lo tapa igual que un corsé mal puesto.
- **🟠 Riesgo conocido en Back View:** prenda de frente abierto en Back View tiende a re-decorarse o cerrarse mal (mismo defecto documentado en Anaïs `anais.md` §5.1c/§9) — verificar que el ancla de espalda esté puesta cuando la bata aparezca en esa pose.

### 5.2 · Paleta y reglas cromáticas (ampliada 11/08/2026 — agrupada por raíz narrativa)

- **Firma inamovible:** el **rosa** (neon / hot / dusty / magenta — cualquier tono de la raíz Stripper) **SIEMPRE presente** en algún punto del look. Es su cuota cromática permanente.
- **🎪 Raíz Stripper** (neón, vivo, de escenario): Hot Pink Neon, Electric Magenta, Cyber Blue, UV Violet, Acid Chartreuse *(acento, nunca dominante — el neón dominante es más de Ele)*.
- **⛓️ Raíz Domme** (oscuro, poder, calabozo con clase): Carbon Black, Oxblood/Deep Wine, Dark Plum, Gunmetal Chrome, Midnight Navy.
- **👑 Raíz Fashionista** (editorial, pulido, alta costura): Champagne, Pearl White, Rose Gold, Chrome Silver, Lavender, Mint, Coral, Turquesa.
- **🎀 Raíz Girly** *(nueva 11/08/2026, exclusiva del arquetipo Girly Girl — §6)*: Baby Pink, Pastel Lavender, Cotton-Candy Blue, Soft Mint, White, Gold accents. Pasteles saturados y luminosos, nunca apagados/sucios.
- **Reservado al ADN:** el **rojo** de los labios. No usar rojo como color dominante de prenda (compite con la firma facial).
- **Anti-monoblock:** máx. 2 looks monoblock consecutivos.
- **Uso:** cada look puede inclinarse hacia una raíz (club-neón / calabozo-oscuro / editorial-pulido) según el arquetipo (§6), pero el rosa firma cruza las tres siempre.

### 5.3 · Calzado (canon inamovible — lo único 100% obligatorio del vestuario, 11/08/2026)

- **Regla:** cualquier tipo de calzado sirve — stiletto pump, bota, sandalia — pero **SIEMPRE con plataforma**. `tacones/botas/sandalias siempre con plataforma` (directiva Ama 11/08/2026, tras derogar el corsé obligatorio: esto pasa a ser la única pieza inamovible del BLOQUE B).
- **Altura mínima:** plataforma 6" o superior (el canon histórico usa 8").
- **Prohibido:** flats, block heel, **chunky heel**, kitten heel, wedge, descalza, sandalia/tacón/bota **sin plataforma**.
- **🔻 Botines/ankle boots — FUERA de la rotación (Ama 11/08/2026):** cuando el calzado elegido es bota, solo **knee-high (bajo rodilla)** o **thigh-high/over-the-knee (sobre rodilla)** — nunca ankle boot corto. Pump/sandalia/mule siguen permitidos como categorías aparte, esta restricción es específica de botas.
- **Atributos obligatorios del token** (nombrar los 5 en cada pose): altura · tipo de plataforma · material/acabado · color · tipo de tacón (`razor-thin metal needle heel`).
- ⚠️ La palabra `chunky` va **solo en el negative**, jamás en el positive.

### 5.4 · Prohibiciones absolutas

| Prohibido | Sustituto autorizado | Directiva |
|---|---|---|
| Flequillo / frente cubierta | frente despejada, `NO BANGS` | Canon V3.5 Stealth |
| Labios **rosados** (rosa = firma de Ele), nude o mate | maquillaje elegido por la ocasión del look, alto brillo | Lo inviolable es la **forma** (ultra-plump, overlined, cupid's bow, high-gloss wet), no el color — §2 (Ama 02/08) |
| Cuero como pieza principal | látex/PVC/vinilo; cuero solo en corsé/arnés/accesorio | Canon materiales |
| Tatuajes | piel limpia | Salvo variante legacy pedida por la Ama |
| Texto/nombre sobre prenda | choker liso, O-ring, hardware sin letras | Regla transversal del repo |
| Sonrisa amplia / actitud juguetona | Face of the Pole | Principio de registro — **excepción única: arquetipo Girly Girl (§6), ver ahí las reglas** |
| **Cualquier prop/setting/tono de infancia** (peluches, dollhouse, cuarto de niña, "playful giggly" infantil) — incluso en Girly Girl | Glamour adulto exagerado: boudoir/penthouse/salón de belleza de lujo, sonrisa radiante/sensual de mujer adulta | **PROHIBICIÓN ABSOLUTA (Ama 11/08/2026).** Hiperfem ≠ niñita rosada. Ver nota en §6 |
| **👙 Calzón de cobertura total** — brief de talle alto, boyshort, hipster, culotte, tap pant, bikini bottom que tape el asiento | **tanga o g-string, siempre** (delantero angosto, cintura sobre el hueso de la cadera, atrás una tira fina) | **Ama 13/08/2026.** Ancla `BOTTOM_CUT_LOCK` en `anclas_siempre`. Su corte se **nombra** en el BLOQUE B (§5.5) — no basta con "bikini bottoms" |
| **🦵 Piernas abiertas usando vestido, falda, bata o túnica** | rodillas y muslos juntos · una pierna cruzada sobre la otra · las dos piernas plegadas a un lado si va baja | **Ama 13/08/2026, transversal a las tres muñecas.** Ancla opt-in `DRESS_LEG_CLOSURE`. **Deroga las piernas en V del Throne en Suelo (§4) cuando el look es de falda** |

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

---

## §6 · Arquetipos y Metas (rediseñado 11/08/2026 — filtro stripper + domme + fashionista + cuerpo de gimnasio)

| Arquetipo | Descripción | Meta |
|---|---|---|
| **Club / Escenario** | Pole, tarima, luz neón, revue | 18% |
| **👙 Bikini / Lencería Erótica** *(nuevo 13/08/2026 — Ama)* | **La prenda ES el look.** Conjunto de dos piezas como sujeto de la toma: micro bikini, triangle top, conjunto de lencería (sujetador + tanga + liguero), bodysuit de tiras, teddy, bañador de recortes — en vinilo/PVC/látex/wet-satin/crystal mesh. Escenarios de **piel y agua o de tocador**: borde de piscina, cabana de beach club, spa privado, boudoir, backstage de sesión. **Sin capa que lo tape**: nada de abrigo, blazer ni bata cerrada encima (la bata abierta sí, si deja ver el conjunto entero). **El calzón va SIEMPRE en tanga o g-string** (§5.4). | 15% |
| **Calabozo / Dungeon** | Sesión de dominación, bondage de diseño, mobiliario elegante *(desc. suavizada 11/08 — ver recalibrado de materiales §5.1, ya no "arneses, mobiliario de dominación" industrial)* | 13% |
| **VIP / Privado** *(nuevo 11/08, reemplaza a Uniforme Privado)* | Sesión exclusiva uno-a-uno, lencería-fetiche lounge, energía de sala privada — distinto de Calabozo (no es dominación) y de Penthouse (es *con* alguien, no ella sola) | 12% |
| **Gym / Athletic** *(nuevo 11/08 — justificado por el cuerpo de gimnasio del §2)* | Sujetador deportivo de vinilo + sudor glam + plataforma deportiva son la base fija; **la pierna NO siempre va en leggings** (corrección 11/08, Look 05 default a leggings sin variar) — rotar entre leggings, bike shorts, unitard con cutouts, piernas desnudas con calcetín corto cromado, etc. | 12% |
| **🎀 Girly Girl** *(nuevo 11/08 — ÚNICO arquetipo con excepción de expresión, ver §2)* | **Hiperfem ADULTA** (raíz Girly §5.2) — glamour rosa exagerado, moños/corazones/ruffles en vinyl/PVC gloss como accesorio de alta costura (referencia Moschino/Chanel-runway, NUNCA de guardería), ambientes de boudoir/penthouse/salón de belleza de lujo en rosa. **Expresión cálida y sonriente** — quiebre real de personaje, contraste deliberado con su registro habitual. | 12% |

> ⚠️ **Corrección de fondo (Ama 11/08/2026, misma sesión):** el primer intento de este arquetipo (Look 02 v1) confundió "hiperfem" con "niñita rosada sexualizada" — metió peluches, dollhouse y un tono "playful giggly" que leía infantil. **Esa lectura queda PROHIBIDA explícitamente.** Hiperfem = feminidad adulta exagerada (glamour, poder, lujo, sensualidad de mujer adulta), nunca estética o props de infancia/guardería. Ver prohibición dura en §5.4.
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
| Silueta | ≥ 3 looks del mismo arquetipo |
| Setting / escenario | ≥ 3 looks del mismo arquetipo |
| Modo cromático monoblock | máx. 2 consecutivos globales |

- **Outfit único:** sí. Miss Doll no repite outfit.

---

## §8 · Cuotas Vivas

| Cuota | Frecuencia | Alcance |
|---|---|---|
| **Rosa firma presente** | **todos los looks** | Cualquier prenda, calzado o accesorio |
| **Calzado con plataforma** | **todos los looks, sin excepción** | La única pieza 100% inamovible del vestuario (11/08/2026) |
| ~~Arquitectura de corsé visible~~ | ~~todos los looks~~ | **Derogada 11/08/2026 — ahora opcional, ver §5.5** |
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
| Odalisque | `RECLINE_ANCHOR` | **`FLOOR_SEAT_ANCHOR`** | Su Odalisque es *Throne en Suelo* (§4): sentada en el piso con piernas en V, **no reclinada**. Aplicar el ancla de recumbencia de Ele contradiría su propio canon de pose. |

**📐 Orientación de Odalisque — la única que ALTERNA (Ama 17/08/2026):** Ele y Anaïs tienen Odalisque reclinado, así que `ASPECT_HORIZONTAL` va fijo en el mapa por defecto del motor. El de Miss Doll es sentado en el piso (Throne en Suelo) — ninguna orientación es "la" natural del encuadre, y la Ama pidió variedad: *"Miss Doll debe tener Odalisque en vertical y horizontal"*. Por eso su Odalisque **no lleva** `ASPECT_VERTICAL` ni `ASPECT_HORIZONTAL` fijos en `anclas_universales.json` — se resuelve con `PromptBuilder("miss_doll").orientacion_odalisque(look_number)` (alterna por paridad del número de look) y se pasa a `build()` vía `extra_anclas=[...]`. Es el único slot de las tres muñecas que se decide así; todo el resto sigue fijo en el mapa.

> 🩹 **Cicatriz del 11/08/2026:** sus 98 prompts se escribieron con `[BLOQUE A] + [BLOQUE B], …, [BLOQUE C setting]` **literales**, sin `Ubicacion`, sin `Tags` y con el negativo etiquetado de una forma que el parser de la app no reconoce. Medido sobre el archivo commiteado: **98/98 prompts con placeholder · 0/14 looks con negativo · 0/14 con ubicación**. Reescritos el 12/08/2026.

🚨 **Cada prompt de la galería va FINAL Y EXPANDIDO.** El ADN completo, el outfit completo, las anclas y el setting, uno detrás de otro dentro del bloque de código. Un `[BLOQUE A]` entre corchetes dentro de un prompt no es una abreviatura: es un prompt roto que la app manda tal cual al generador.
