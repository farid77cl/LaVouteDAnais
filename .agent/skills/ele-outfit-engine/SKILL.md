---
name: ele-outfit-engine
description: Motor especializado en la creación y gestión de la identidad visual de Ele. Gestiona la generación de prompts bajo el protocolo V3.5 Hard-Sync, asegura la consistencia de imagen en múltiples poses, y mantiene actualizadas las estadísticas de la galería de outfits. Úsalo cada vez que se solicite un "Outfit del Día", un nuevo Look, o una auditoría del repositorio visual.
---

# 👠 Ele Outfit Engine (V3.5)

Este Skill es el motor central para mantener la coherencia estética y técnica de Ele. Su objetivo es garantizar que cada nuevo activo visual respete el ADN canónico y mantenga el equilibrio estadístico del repositorio.

## 🧬 ADN V3.5 Hard-Sync (Referencia Rápida)

Para cada generación de imagen, **DEBES** incluir estos elementos de forma explícita para evitar variaciones:

- **Físico:** Oval face, high cheekbones, grey-green eyes, dark cherry red hair (XXXL extensions, hip-length).
- **Modificaciones:** Blackwork tattoos (upper back, arms, outer thighs), piercings (navel, nipple piercings pressing against and visible under clothing).
- **Estética:** Dramatic siren liner, glossy hot pink lips, XXXL French nails (5cm, white tips).

## 👠 Footwear Canon (REGLA INAMOVIBLE — Ama 13/05/2026)

**Ele SIEMPRE usa stiletto. Sin excepciones.**

| ✅ AUTORIZADO | ❌ PROHIBIDO |
| :--- | :--- |
| `stiletto pump` (con o sin plataforma) | `wedge`, `wedge heel`, `wedge platform` |
| `pointed-toe stiletto` | `mule sandals` sin stiletto pin heel |
| `stiletto boots` (ankle, knee, thigh-high) | `block heel`, `chunky heel`, `cone heel` |
| `stiletto sandals` con tira fina | `clog`, `flatform`, `kitten heel` |
| `platform stiletto` (plataforma + pin heel fino) | `espadrille`, `slipper` |
| Tacones 12–18 cm con base de aguja fina | Plataformas perspex tipo mule sin pin stiletto |

> 💎 **PREFERENCIA DE LA AMA (03/06/2026) — Pleaser TRANSPARENTES:** la Ama **adora el `clear transparent acrylic platform stiletto` (Pleaser Flamingo-808 style, 8-inch heel + 4-inch clear platform, ankle strap)**, sobre todo en **Stripper (pole/stage)** y **Bikini (Studio/Beach)** — gatillo erótico declarado. Usarlo como **calzado DEFAULT** en esos dos arquetipos (y opcional en Gym/Nightclub/Domestic Trophy) salvo que el look pida otro. Es plataforma + pin stiletto (NUNCA wedge/mule plano; NUNCA "chunky" en el positive).

**Vocabulario obligatorio en el BLOQUE B:** Toda mención de calzado **DEBE** incluir explícitamente la palabra `stiletto` (heel/pump/boot/sandal). Si se incluye plataforma, debe quedar claro que la base del tacón es un pin stiletto fino (`platform stiletto`, no `platform mule`, no `platform wedge`).

**Razonamiento:** La línea visual de Ele es editorial escultórico-fetish de alta costura (sin atribución de diseñador). El estilete es parte del DNA — define la línea de la pantorrilla, el arco del pie y la postura. Wedges y mules de plataforma planos rompen la silueta cuico-bimbo y se leen como playa/casual, no como armadura de poder.

**Look 176 (Neon Coral Flash) — caso histórico:** Se generó con `clear perspex platform mule sandals` y el resultado se leyó como wedge. **FLAG** para regeneración con `clear perspex platform stiletto sandals, 14cm pin stiletto heel, ankle strap`.

### 🔒 TOKEN DE CALZADO BLOQUEADO — 8 atributos (Directiva Ama 04/06/2026)

> **Problema detectado por la Ama:** el calzado se dejaba demasiado **libre a la interpretación de la IA** (ej. solo `stiletto ≥12cm` o `stiletto pump`), y aunque hubiera un buen token, **no se pegaba idéntico en las 7 poses** → la IA daba un zapato distinto en cada imagen del set. Esto rompe la **Ley de Continuidad** (BLOQUE físico+vestuario = 100% idéntico por pose) justo en el zapato.
>
> **Regla dura:** al fijar el look se redacta UN solo **Token de Calzado** con los **8 atributos obligatorios** completos. Ese token se **copia-pega VERBATIM e IDÉNTICO** en las 7 poses (dentro del BLOQUE B). **Prohibido** abreviar a `heels` / `same shoes` / `stiletto` suelto, y **prohibido** dejar atributos a interpretación. Si un atributo no se especifica, la IA lo inventa distinto cada vez → exactamente lo que la Ama no quiere.
>
> **Los 8 atributos (en este orden):**
> 1. **Tipo/arquetipo** — `pump` / `sandal` / `knee-high boot` / `thigh-high boot` / `ankle bootie` / `slingback` / `Mary Jane`.
> 2. **Altura del tacón en cm explícito** + plataforma en cm si aplica — `14cm pin stiletto heel` · `8-inch heel + 4-inch platform`. Nunca "alto" o "≥12cm" suelto.
> 3. **Base del tacón explícita** — `thin pin stiletto heel` (anula bloque/cuña; obligatorio aunque se repita con el atributo 2).
> 4. **Material + acabado** — `clear transparent acrylic` · `mirror chrome` · `patent vinyl` · `liquid gold lamé` · `pearl-white patent` · `rhinestone-encrusted`.
> 5. **Color exacto** coordinado con el look — explícito (`cherry-red`, `champagne gold`, `ivory`), nunca "a tono".
> 6. **Forma de la puntera** — `pointed almond toe` / `sharp pointed toe` / `open toe` / `peep toe` / `round toe (Mary Jane)`.
> 7. **Cierre/correa** — `ankle strap with buckle` / `lace-up front` / `slingback strap` / `T-bar` / `none (slip-on pump)`.
> 8. **Hardware/suela/detalle** — `gold ankle buckle` / `chrome heel cap` / `crystal-encrusted platform` / `red lacquered sole` / `none`.
>
> **Plantilla:** `[tipo] in [material+acabado] [color], [altura cm + plataforma], [base pin stiletto], [puntera], [cierre], [hardware/suela]`
>
> **Ejemplos de token completo (copiar idéntico ×7):**
> - Escort Haute: `pointed-toe slingback pumps in champagne-gold liquid metallic, 14cm thin pin stiletto heel, sharp pointed toe, slingback strap, chrome heel cap`
> - Stripper/Bikini (default Pleaser transparente): `clear transparent acrylic platform stiletto sandals, 8-inch pin stiletto heel + 4-inch clear platform, open toe, ankle strap with buckle, crystal-free clear sole`
> - HF Editorial (aguja pura, sin plataforma): `single-sole pointed pumps in mirror-chrome patent, 13cm thin pin stiletto heel, sharp pointed toe, slip-on (no strap), polished chrome sole`
> - Domestic Maid: `pearl-white patent Mary Jane platform stilettos, 6-inch pin stiletto heel + 2-inch platform, round toe, T-bar strap with buckle, white sole`
>
> **Checklist pre-prompt:** (a) ¿el token tiene los 8 atributos? (b) ¿está **idéntico** carácter-por-carácter en las 7 poses? (c) ¿incluye `stiletto` + cm explícitos? Si alguna es NO → completar antes de generar.

## 🧤 GUANTES PROHIBIDOS (Directiva Ama 03/06/2026 — DEROGA el antiguo Glove Canon)

**Ele NO usa guantes. De ningún tipo, en ningún arquetipo, en ninguna pose.**

El antiguo "Glove Canon" (4 tipos autorizados: fingerless opera / claw cut-out / transparent fingertip / wrist-length) queda **completamente derogado**. La razón original era resolver el conflicto entre el guante y las uñas French XXXL; la solución definitiva de la Ama es eliminar el guante. **Manos siempre desnudas**, uñas a la vista sin obstáculo.

### Qué hacer al diseñar

- ❌ **Prohibido en el BLOQUE B (outfit):** `opera gloves`, `elbow gloves`, `wrist-length gloves`, `fingerless gloves`, `claw cut-out gloves`, `transparent fingertip gloves`, `latex/satin/lace/leather/velvet gloves` — cualquier prenda que cubra las manos.
- ✅ **Negative base** (ya en `dna_v3_5.md`) incluye: `gloves, opera gloves, long gloves, elbow gloves, fingerless gloves, wrist gloves, leather gloves, satin gloves, lace gloves, covered hands`.
- 🔁 **Sustitución obligatoria:** muchas siluetas de referencia (Newton, Bettie Page, Versace Miss S&M, Dita, Pro-Dom, Officer Domme) usaban guantes como **accesorio dominatrix/courtesan**. Al diseñar esas siluetas, **reemplazar el guante** por otro accesorio canónico que NO cubra las manos: `riding crop`, `whip-belt`, `choker O-ring`, `body chains`, `officer cap`, `Bayonetta glasses`, `seamed stockings`, `waist cincher`, `cuffs en muñeca` (brazaletes, no guantes). **Nunca** por otro guante.
- ✔️ **Chequeo pre-batch (OBLIGATORIO):** `grep -i glove` sobre los prompts del positive debe dar **0**. Si aparece, se borra del outfit antes de generar. Igual que el chequeo `grep chunky` y `grep` de texto-nombre.

> **Nota histórica:** las siluetas de las bibliotecas (§ identidad_ele.md y abajo) tenían `opera gloves` incrustado como componente. Esas menciones se erradicaron el 03/06/2026. Si alguna sobrevive en texto de referencia, **se ignora**: el guante no se materializa nunca.

## 🛠️ Workflow Operativo

> **ORDEN OBLIGATORIO:** Análisis → Diseño del Outfit → Escritura de los 5 Prompts en galeria_outfits.md → Generación → Git → Estadísticas.
> **Ninguna imagen se genera antes de que los 5 prompts completos estén escritos en `galeria_outfits.md`.**

---

### 0. Regla Transversal Anti-Repetición (OBLIGATORIA — Ejecutar ANTES de cualquier diseño)

Antes de proponer cualquier Look, consulta los últimos looks del sub-arquetipo correspondiente en `galeria_outfits.md` y bloquea lo siguiente:

**Ventana de bloqueo por elemento:**

| Elemento | Ventana de bloqueo |
|----------|--------------------|
| Silueta (código) | ≥ 3 looks previos del mismo sub-arquetipo |
| Familia cromática dominante | ≥ 5 looks previos del mismo sub-arquetipo |
| Material principal | ≥ 2 looks previos del mismo sub-arquetipo |
| Setting/escenario | ≥ 3 looks previos del mismo sub-arquetipo |
| **Familia cromática dominante (transversal)** | **≥ 5 looks previos GLOBALES (cualquier sub-arquetipo), no solo del mismo** |
| **Modo cromático Monoblock** | **máx. 2 looks Monoblock consecutivos GLOBALES → el 3º debe ser Contraste / Triada / Gradiente / Neutro+Pop** |

> 🎨 **REGLA ANTI-MONOBLOCK REFORZADA (Directiva Ama 03/06/2026):** La Ama detectó **exceso de monoblock** (looks de un solo color) y **repetición de colores**. Dos correcciones duras:
> 1. **Monoblock NO consecutivo:** máximo **2 looks Monoblock seguidos** (antes eran 3). El 3º obliga a un modo multicolor (Contraste 60/30/10, Triada, Gradiente, o Neutro+Pop). El monoblock es un recurso, no el default.
> 2. **Color no se repite (mirada global, no por sub-arquetipo):** antes de fijar el color, revisar las **familias dominantes de los últimos 5 looks GLOBALES** (toda la flota reciente, sin importar sub-arquetipo) y elegir una familia **NO usada** en esa ventana. La repetición de color que molesta a la Ama es transversal: da igual que sea un Gym rojo y un Escort rojo — siguen siendo dos rojos seguidos.

**Protocolo:**
1. Consultar los últimos N looks del sub-arquetipo (N = ventana de la tabla) **y los últimos 5 looks globales** (para color y monoblock).
2. Listar qué siluetas, colores, materiales y settings están bloqueados.
3. **Contar cuántos de los últimos 2 looks globales fueron Monoblock.** Si ambos lo fueron → este look NO puede ser Monoblock.
4. **Elegir una familia cromática que no aparezca en los últimos 5 looks globales** + un modo cromático que rompa la racha si hace falta.
5. Solo entonces avanzar al Paso 1.

**Ejemplo:** Últimos 3 Pin-Up: PA1 vinyl polka-dot (hot pink) · PA3 sundress (powder blue) · PB1 Space Age (blanco) → Bloqueadas: siluetas PA1/PA3/PB1 · colores hot pink / powder blue / blanco ártico. Últimos 2 globales fueron Monoblock champagne + Monoblock oxblood → **este look NO puede ser Monoblock** → forzar Contraste/Triada con familia no usada (ej. teal + tangerine acento).

---

### 1. Análisis de Arquetipos
Antes de proponer un Look, consulta la tabla de estadísticas en [galeria_outfits.md](file:///c:/Users/farid/LaVouteDAnais/00_Ele/galeria_outfits.md).

**10 categorías — Metas ASIMÉTRICAS (Directiva Ama 03/06/2026)**

El paraguas "Mix" ya no existe. Metas por categoría (la Ama reacomodó 03/06):
- **🩱 Lencería = 15%** (categoría favorita de la Ama, muy sensual — referencias La Perla / Honey Birdette / Agent Provocateur). **INCLUYE las medias/hosiery/stockings como tema propio de Lencería.**
- Las **otras 9 categorías = ~9,4% cada una** (el 85% restante repartido).

> 🩱 **LENCERÍA (15%):** seguir la línea sensual La Perla + Honey Birdette + Agent Provocateur + Atsuko Kudo. Incluir sets con **medias con costura + suspender belt** como sub-tema canónico (las medias viven en Lencería).
> 👙 **BIKINI (9,4% — variedad, NO solo micro):** la Ama ama los micro bikinis PERO se repiten demasiado. **Autorizada a más variedad de trajes de baño sensuales:** one-piece high-cut, monokini cutout, trikini, maillot retro-glam, wrap/drape, O-ring/chain, sarong-set, rhinestone gala — siempre sensual y material V3.5. No agotar el micro triangle.
> 🏋️ **GYM (9,4% — incluir FALDAS):** además de leggings/sets, incluir **faldas/skorts deportivos sensuales** inspirados en colecciones reales **Puma + Adidas** (tennis skort plisado, wrap skirt sobre legging, pleated mini athletic) en material wet-look/vinyl. Siempre Pleaser platform.

El paraguas "Mix" legacy (~91 looks viejos) sigue sin reclasificar — distorsiona la estadística hasta que se haga un pase de reclasificación.

| # | Categoría | Meta | Est. actual (220) | Déficit | Estado |
|---|-----------|:----:|:-----------------:|--------:|:------:|
| 1 | **HF Editorial** | 10% (22) | ~22 | ≈ 0 | ✅ |
| 2 | **Nightclub** | 10% (22) | ~15 | −7 | ⚠️ |
| 3 | **Corporate** | 10% (22) | ~28 | +6 | 🔴 Pausa |
| 4 | **Domestic** | 10% (22) | ~15 | −7 | ⚠️ |
| 5 | **Stripper** | 10% (22) | ~13 | −9 | ⚠️ |
| 6 | **Escort** | 10% (22) | ~12 | −10 | ⚠️ |
| 7 | **Bikini** | 10% (22) | 22 | 0 | ✅ |
| 8 | **Lencería** | 10% (22) | ~21 | −1 | ✅ |
| 9 | **Pin-Up** | 10% (22) | ~8 | **−14** | 🔴 #1 |
| 10 | **Gym/Athleisure** | 10% (22) | ~11 | **−11** | 🔴 #2 |

**Regla de prioridad (OBLIGATORIA):**
1. Identificar la categoría con mayor déficit.
2. El nuevo Look **debe** pertenecer a esa categoría.
3. Corporate está en pausa relativa — no generar Corporate salvo que todas las demás estén en meta.
4. Al llegar a una nueva flota redonda (250, 300…), actualizar la columna "Est. actual" y recalcular déficit.

**Orden de prioridad fijo (actualizado 21/05/2026 · flota 220):**
```
1. Pin-Up (−14) 🔴
2. Gym (−11) 🔴
3. Escort (−10) ⚠️
4. Stripper (−9) ⚠️
5. Nightclub (−7) ⚠️
6. Domestic (−7) ⚠️
7. Lencería (−1) ⚠️
8. HF Editorial (0) ✅
9. Bikini (0) ✅
10. Corporate (+6) 🔴 PAUSA
```

**Composición recomendada de batches:**

| Tamaño batch | Composición óptima |
|:------------:|--------------------|
| **Batch 10** | 3 Pin-Up + 2 Gym + 2 Escort + 2 Stripper + 1 Nightclub |
| **Batch 6** | 2 Pin-Up + 1 Gym + 1 Escort + 1 Stripper + 1 Nightclub |
| **Batch 4** | 2 Pin-Up + 1 Gym + 1 Escort |
| **Batch 2** | 1 Pin-Up + 1 Gym |
| **Look solo** | Pin-Up (hasta que alcance meta) |

**Regla dual/tri dentro de cada batch:** aunque el batch priorice categorías deficitarias, al generar ≥2 looks de la misma categoría **siempre aplicar la regla de polo** de esa categoría (ej: 2 Pin-Up = 1 Bombshell + 1 Retro-Futurismo o Decade Glam).

---

### 🌃 Sub-arquetipo Nightclub (Spec V2 — 22/05/2026 · Refactor con referencias reales: House of CB + Oh Polly "All Nighter" + Fashion Nova "Going Out" + Y2K Paris Hilton + Bottega party)

**Universo:** VIP lounge de medianoche, dance-floor con luz UV, club privado de élite, neon-room, after-hours hotel rooftop. Energía cinética, brillos hipnóticos, materiales que reflejan luz láser.

**Referencias canónicas reales:**
- **Oh Polly "All Nighter"** + "Birthday Glam" + Confident/Genevieve/Maeve/Aralyn/Jovie collections — bodycon ruched wet-satin, sparkly mini con HOTFIX crystals hand-applied, cowl-halter drape, draped off-shoulder, laser-cut metallic lace, asymmetric cut-out
- **House of CB** — premium luxe elegance, bandage bodycon, satin corset midi, going-out signature
- **Fashion Nova "Going Out"** — affordable bodycon dominante, sequin mini, bandage strips, backless
- **Y2K Paris Hilton 2003-2005** — chrome metallic mini, bedazzled, "Stars Are Blind" pink era
- **Lindsay Lohan + Britney Spears 2003-2005** — Y2K club kid evolved
- **Bottega Veneta party** (Matthieu Blazy 2023-2025) — chrome liquid dress + clutch escultural minimal-glam
- **Magda Butrym** — power-shoulder + cinched waist contemporary party

**Diferencias clave:**
- **vs. Stripper:** Stripper baila por dinero (jaula estructural, fringe, micro-pieces). Nightclub baila para sí misma o pareja (glam, sequins, drape).
- **vs. Escort:** Escort opera en hoteles/cenas/galas (columna líquida, aristocrática). Nightclub opera en clubs/dance-floors (cinética, brillo agresivo).
- **vs. High-Fashion Editorial:** HF es escultórico/gala/museo. Nightclub es club/lounge/dance-floor.

**Biblioteca de siluetas:** 12 opciones (ver `00_Ele/identidad_ele.md` § Biblioteca de Siluetas → **Nightclub**). Inspiración: Fashion Nova "Going Out" + Oh Polly "All Nighter/Birthday Glam", filtrado por canon Ele.

**Paleta canon Nightclub:**

| Nivel | Colores |
|---|---|
| **Dominantes (≥50%)** | Hot Magenta · Electric Cyan · Acid Chartreuse · Chrome Silver · Liquid Gold · Oil-Slick · Deep Plum · Blood Red |
| **Adicionales del scouting** | Pearl/Mother-of-Pearl high-gloss · Bronze metálico · Hot Pink saturado · Olive metallic · Jewel tones (Sapphire/Emerald/Ruby) |
| **Acentos (≤20%)** | Black gloss (solo herrajes/costuras) · Bubblegum Hot Pink · Cherry Red (solo pelo/labios) |
| **❌ PROHIBIDOS** | Baby Pink · Pastel Blue · Cream Satin · Beige · Champagne pálido · Rose Gold *(Rose Gold se reserva para Boudoir/Bridal)* |

**Materiales canon Nightclub:**

| # | Material | Detalle |
|---|---|---|
| M1 | Sequins/Lentejuelas espejo | Ondas de luz con cada paso |
| M2 | Latex high-gloss | Second-skin, cremalleras expuestas |
| M3 | Vinyl con cristales incrustados | Layered glam |
| M4 | Chrome líquido / Liquid metal | Efecto mercurio |
| M5 | Metal cromado pulido | Jaula decorativa |
| M6 | Mesh sheer + cristal drape | Transparencia con peso |
| M7 | Iridescent multichrome | Oil-slick / holographic / beetle-shell |
| M8 | PVC translucent neon | UV-reactive translúcido |
| **M9** | **Wet-Satin / Liquid Satin (ruched)** 🆕 | OP signature — drawstring ruching, alto brillo |
| **M10** | **HOTFIX Crystal hand-applied** 🆕 | Swarovski-style sobre vinyl/sheer/wet-satin |
| **M11** | **Vinyl/Chrome bandage strips** 🆕 | Sustituye bandage knit — tiras horizontales clinging |
| **M12** | **Laser-Cut Metallic Lace** 🆕 | NO algodón — lace cortado en metal sobre base latex |

**❌ Materiales prohibidos en Nightclub:** Satén opaco mate · terciopelo grueso · cuero envejecido · denim · lana · algodón · modal · jersey · knit estructural · bandage knit (sustituir por M11) · lace de algodón (sustituir por M12).

**Setting/escenario típico:** VIP lounge backlit · dance-floor neon · bar de espejo cromado · after-hours hotel rooftop · DJ booth blur · strobe room · UV-light private club · velvet rope corner.

**Combos canon Nightclub:**

| Combo | Inspiración | Lectura |
|---|---|---|
| M9 wet-satin + corset boning visible | OP Confident | Ruched corset mini |
| M10 hotfix crystals + M6 sheer | OP Genevieve | Embellished sheer bodysuit |
| M12 laser-cut lace + M2 latex base | OP Aralyn | Lace fetish editorial |
| M11 vinyl bandage + backless cut | FN Dion | Bandage bodycon espalda abierta |
| M4 chrome líquido + drapeado off-shoulder | OP Maeve | Off-shoulder liquid metal |
| Cut-outs asimétricos + M2 latex | FN Tory/Diana | Asymmetric architectural bodycon |
| M1 sequins solo | (cualquier dominante) | Sequin Mini-Dress clásico |
| M2 latex + M5 metal (zipper/herrajes) | Canon original | Latex Club Bodysuit |

**Combos PROHIBIDOS en Nightclub:**
- M1 sequins + M2 latex gloss (lectura cabaret/burlesque, no club)
- M2 latex + terciopelo (anti-canon material)
- M7 iridescent + M3 cristales (sobre-saturación visual)
- Sequins + materiales mate (rompe coherencia de brillo)

#### 🔥 PROVOCATION THRESHOLD Nightclub (NUEVA — OBLIGATORIA)

> Toda silueta Nightclub DEBE cumplir al menos UNA condición:
> - **Material V3.5 high-shine** (sequins/latex/vinyl/chrome/iridescent — NUNCA matte)
> - **Cutout estratégico** o **backless** o **plunge neckline** profundo
> - **Bodycon ceñido extreme** (House of CB bandage / Oh Polly ruched wet-satin)
> - **HOTFIX crystal hand-applied** (Oh Polly Genevieve/Aralyn signature)
> - **Heels stiletto ≥12cm** (Pleaser permitido pero NO obligatorio — distinción vs Stripper)
> - **Drape cinético** que se mueve con láser/strobe

#### 🎭 Personality Tokens — OBLIGATORIO en BLOQUE C

`midnight VIP energy · she-came-to-be-seen confidence · birthday-glam apex · Paris Hilton Y2K stars-are-blind · Bottega party effortless · dance-floor royalty · the strobe light worships her · she's not here to dance she's here to BE the dance-floor · Oh Polly bodycon awareness`

#### 🏛️ Settings Específicos Nightclub (con props)

- **Boom Boom Room NYC** Standard Hotel — gold accents + city skyline
- **Annabel's London** Berkeley Square — opulent velvet + floral excess
- **Loulou's Paris** Palais Royal — Hyde-Park elegance crossover
- VIP lounge backlit con velvet ropes + bottle service
- Dance-floor neon UV con láser direccional + smoke machine
- Bar de espejo cromado con bottle wall iluminado
- DJ booth blur con luces estrobo + smoke
- Strobe room con disco ball + paneles cromados
- After-hours hotel rooftop con city night skyline
- Velvet rope corner con bouncer implied + paparazzi flashes
- **Bottega party loft** minimal con escultura chrome central + bartender

#### 🤸 Pose Framings Específicos Nightclub (variantes de las 7 canónicas)

| # | Nightclub |
|---|---|
| 1. Standing | VIP entrance pose mid-strobe, hand holding cocktail glass + clutch, gaze through camera |
| 2. Back | Walking through dance-floor crowd looking over shoulder, neon casting on back + spine arch |
| 3. Seated | Perched en VIP velvet sofa con piernas cruzadas + champagne bottle de fondo + bartender blurred |
| 4. Profile | At bar leaning con elbow on chrome counter, lumbar arch dramatic, light cast on profile |
| 5. Ditzy | Compact mirror touching up lipstick en VIP bathroom con golden mirror frame |
| 6. POV | Across-the-VIP-table POV con drink raised + bottle service |
| 7. Odalisque | Recostada en VIP banquette velvet rojo, lights reflejados, S-curve drink in hand |

> **NEGATIVE PROMPT específico Nightclub:** `daytime, daywear, business casual, athleisure, gym wear, sportswear, conservative, modest neckline, full coverage, beach setting, office setting, museum gallery (eso es HF), stage performance with tip rail (eso es Stripper)`

---

### 🎨 Sub-arquetipo High-Fashion Editorial (Spec V2 — 22/05/2026 · Refactor con referencias reales SS26: Schiaparelli "Agony and Ecstasy" + Iris van Herpen + Margiela Glenn Martens + Mugler couture)

**Universo:** Gala de museo, red-carpet, premiere de couture, fashion week, alfombra de premios, photo-shoot editorial para revista. La Ele que llega cuando el club ya cerró y empieza el establishment del lujo. Arquitectura escultórica sobre cuerpo, drapeados cathedral, materiales que se imponen como obras de arte.

**Referencias canónicas reales SS26:**
- **Schiaparelli SS26** ⭐ — Daniel Roseberry "The Agony and the Ecstasy" (Sistine Chapel inspired). Reptilian + arachnid archetypes (scorpion tails, snake teeth, chimera silhouettes). Gravity-defying forms. 25,000 silk thread feathers · 8,000 hours embroidery. Surrealism Dalí lineage.
- **Iris van Herpen** ⭐ — 3D-printed couture, biomimicry, gravity-defying sculptural, water-droplet/feather-anatomy structures
- **Margiela** Glenn Martens SS26 surprise couture — deconstructed haute conceptual
- **Mugler couture archive** — power-shoulder amazon (crossover con Corporate Power Domme)
- **Dior Galliano archive** — New Look + bias-cut sirena
- **Chanel SS26 (Matthieu Blazy)** — paillettes mother-of-pearl iridescent
- **Valentino Theatrical** — ruffle architectural drama
- **Armani Privé** — petal-pleated flare floral architecture

**Diferencias clave:**
- **vs. Nightclub:** HF = escultura estática para ser fotografiada · Nightclub = movimiento, brillo cinético para luz láser.
- **vs. Escort:** HF = arquitectura imponente, drama del silhouette · Escort = línea aristocrática líquida, discreta dentro del lujo.
- **vs. Stripper:** HF = couture museo/red-carpet · Stripper = club, jaula, fringe, baile por dinero.

**Biblioteca de siluetas:** 11 opciones (ver `00_Ele/identidad_ele.md` § Biblioteca de Siluetas → **High-Fashion Editorial**). Inspiración: couture clásica SS26 (Dior · Chanel · Schiaparelli · Valentino · Armani Privé), filtrado por canon Ele (sin telas naturales, sin plumas reales, sin lace de algodón).

**Paleta canon HF Editorial:**

| Nivel | Colores |
|---|---|
| **Dominantes (≥50%)** | Valentino Rosso · Blanco porcelana / Cream high-gloss · Black gloss arquitectónico *(único arquetipo donde black dominante es canon)* · Champagne metálico / Liquid Gold · Mother-of-Pearl iridescent · Verde Armani (forest/emerald) · Deep Burgundy / Wine · Jewel tones (Sapphire/Emerald/Ruby) |
| **Acentos (≤20%)** | Cherry Red (pelo/labios) · Iridescent multichrome (cuando la silueta es escultórica simple) |
| **❌ PROHIBIDOS** | Hot Magenta saturado · Acid Chartreuse · Neon Cyan *(pertenecen a Nightclub)* · Baby Pink · Pastel Blue · Bubblegum Hot Pink |

**Materiales canon HF Editorial:**

| # | Material | Detalle |
|---|---|---|
| **H1** | **Vinyl/PVC de alta densidad escultórico** | Sustituto couture del silk/organza — mantiene la caída arquitectónica |
| **H2** | **Latex liquid gloss** | Sirenas bias-cut, second-skin couture |
| **H3** | **Wet-satin / Liquid satin** | Bias-cut, drapeados (Dior Galliano echo) |
| **H4** | **Mother-of-pearl paillettes iridescent** 🆕 | Chanel + Dior SS26 signature — paillettes de nácar cubriendo gown |
| **H5** | **Chrome líquido escultórico** | Schiaparelli-style sculpted projections |
| **H6** | **Trompe-l'œil hand-painted vinyl** 🆕 | Simula efectos visuales sobre base vinyl — couture pintado a mano |
| **H7** | **Laser-cut metallic lace** | Sobre base latex (couture fetish editorial) |
| **H8** | **HOTFIX Crystal hand-applied** | Armani Privé crystallized · Schiaparelli embellishment |
| **H9** | **Sculptural rigid resin / PVC armoring** 🆕 | Proyecciones escultóricas Schiaparelli-style (cuernos, picos, alas) |

**❌ Materiales prohibidos en HF Editorial:** silk · organza · tulle · tweed · mousseline · taffeta · denim · lana · algodón · plumas reales (acento puntual max 5%) · lace de algodón.

**Setting/escenario típico:** Museum hall (mármol blanco, columnas, esculturas) · Atelier couture parisino · Backstage de pasarela · Cathedral interior · Penthouse lounge minimalista blanco/gris · Studio editorial neutral · Theatrical stage con telón rojo · Jardín couture vertical.

**Combos canon HF Editorial:**

| Combo | Inspiración | Lectura |
|---|---|---|
| H1 vinyl escultórico + H4 paillettes mother-of-pearl | Dior Anderson SS26 | Ball-gown iridescent couture |
| H2 latex liquid + bias-cut sirena | Galliano legado | Sirena ultra-feminina líquida |
| H5 chrome líquido + H9 sculptural projections | Schiaparelli signature | Bustier escultórico extremo |
| H1 vinyl + Valentino Rosso statement | Valentino theatrical | Statement red gown |
| H6 trompe-l'œil + H8 HOTFIX crystals | Chanel + Schiaparelli | Couture conceptual painted+jeweled |
| H3 wet-satin + petal-pleated flare | Armani Privé | Floral architecture green |

**Combos PROHIBIDOS en HF Editorial:**
- H1 vinyl escultórico + colores neon Nightclub (lectura club, no couture)
- H9 sculptural projections + sequins (rompe la lectura escultórica/conceptual)
- Paillettes mother-of-pearl + HOTFIX crystals (sobre-embellishment, lectura quinceañera)

#### 🔥 PROVOCATION THRESHOLD HF (NUEVA — OBLIGATORIA)

> Toda silueta HF DEBE cumplir al menos UNA condición:
> - **Material sculptural extremo** (vinyl/PVC armor rígido · resina · chrome líquido · trompe-l'œil)
> - **Arquitectura escultórica visible** (Schiaparelli projection · van Herpen biomimicry · Mugler power-shoulder)
> - **Drapeado cathedral** (bias-cut sirena Galliano · column floor-length)
> - **Embellishment couture** (25k silk feathers · 8k hours embroidery · mother-of-pearl paillettes · HOTFIX crystal hand-applied)
> - **Surrealism touch** (scorpion tail · snake teeth · chimera silhouette · skeleton dress lineage)
> - **Heels stiletto fino ≥12cm** (NUNCA Pleaser platform — HF reserva la aguja pura)

#### 🎭 Personality Tokens — OBLIGATORIO en BLOQUE C

`couture museum-piece presence · red-carpet apex predator · runway-only-not-for-life · Schiaparelli surrealist authority · van Herpen architectural goddess · Met Gala worthy · the dress IS the art · 8,000 hours embroidery awareness · gravity-defying poise · Dalí lineage`

#### 🏛️ Settings Específicos HF (con props)

- **Petit Palais Paris** atelier couture parisino con maniquíes vintage y telas colgando
- **Met Gala red carpet** con paparazzi flashes + escalera mármol
- Museum hall (mármol blanco, columnas, esculturas griegas + Schiaparelli-style cuadros surrealistas)
- **Schiaparelli atelier dorado** con espejos antiguos + estatua mythological + Sistine Chapel reproduction wall
- **Iris van Herpen lab** con 3D printers + structures biomórficas + skeleton sculptures
- Cathedral interior con arches gothic + light shafts dramatic
- Backstage de pasarela con racks de couture + maquilladoras + steamers
- Theatrical stage con telón rojo Valentino + spotlight central
- Sculpture gallery white-cube con piezas museum + obras Dalí/Magritte
- Penthouse lounge minimalista blanco/gris con escultura central

#### 🤸 Pose Framings Específicos HF (variantes de las 7 canónicas)

| # | HF Editorial |
|---|---|
| 1. Standing | Red-carpet pose statuesque, hands at sides, gaze regal, full silhouette visible para fotógrafos |
| 2. Back | Runway walk away from camera, looking over shoulder, cola/train arrastrando |
| 3. Seated | Throne-style chair en gallery, legs sharply crossed, escultura behind, imperious |
| 4. Profile | Runway walk profile mid-stride, lumbar arch dramatic, full silhouette legible |
| 5. Ditzy | Backstage mirror touching up lipstick antes de salir a pasarela, dramatic ditzy |
| 6. POV | Photographer POV bajo (low angle) mirando hacia arriba, dramatic empowering |
| 7. Odalisque | Recostada en chaise gallery (Newton-style museum recline), escultura behind |

> **NEGATIVE PROMPT específico HF:** `streetwear, athleisure, casual day-wear, nightclub neon, party dress contemporary, mass-market, fast fashion, Forever 21, Pleaser platform (HF no usa platform — solo stiletto fino)`

---

### 💼 Sub-arquetipo Corporate (Spec V3 — 22/05/2026 · Refactor fetish con referencias reales: Mugler RESTAURADO + Schiaparelli + Versace S&M + Saint Laurent sleaze + Office Siren + Babygirl/Severance)

**🔄 REVERSIÓN CANON 22/05/2026:** La "purga Mugler" del 17/05/2026 queda **anulada**. Mugler era el núcleo Power Executive Domme y su exclusión dejó el polo en modo "Tom Ford clean" sin filo fetish. La investigación de referencias reales confirmó que Mugler 90s + Schiaparelli + Versace Miss S&M son el ADN auténtico del corporate-fetish. Restaurados como núcleo de Polo A.

**Universo DUAL — dos polos co-existentes:**

| Polo | Esencia | Referencias reales |
|---|---|---|
| **A · Power Executive Domme** | La directora-amazona. Mugler cyber-Amazon goddess con shoulders arquitectónicos + Schiaparelli gilded corset + Versace Miss S&M Medusa belt + Saint Laurent sleaze sheer + Tom Ford velvet tux refinado. **NO es Tom Ford clean** — es Tom Ford CON corset visible. | Thierry Mugler FW95 · Schiaparelli SS22 · Versace Miss S&M 1992 · Saint Laurent FW24 · Tom Ford archive · Helmut Newton |
| **B · Office Siren / Babygirl / Severance** | NO es secretaria sumisa de pencil skirt + blazer separados. ES Office Siren TikTok 2023-2025 (Bayonetta glasses + sheer blouse nipple-peek) + Babygirl (intern vulnerable-seductive Nicole Kidman 2024) + Severance (repressed-erotic muted) + Bayonetta catsuit + Secretary 2002 bondage. | Bella Hadid Office Siren · Bayonetta · Babygirl 2024 · Severance · "Secretary" (2002) · Miu Miu FW23 |

**Anti-cliché codificado:** Corporate **NO es pencil skirt + blazer separados como default**. La biblioteca rota hacia: latex power suit (CA1), gilded corset over sheer (CA2), sheer sleaze button-down (CA3), Versace S&M bodysuit (CA4), Bayonetta catsuit (CB2), Secretary bondage shirt-dress (CB3), trench coat surprise (CB6), Severance blazer-dress (CB7).

**Diferencias clave:**
- **vs. HF Editorial:** Corporate = funcional ejecutivo con contexto de uso (oficina/junta/elevator/boardroom). HF = escultura para fotografiar (gala/red-carpet) sin contexto laboral.
- **vs. Escort:** Corporate = poder profesional (oficina) · Escort = hospitalidad de lujo (hotel/cena privada).
- **vs. Domestic:** Corporate = workspace profesional · Domestic = espacio privado del hogar. Trench-surprise en elevator/oficina = Corporate. La misma en penthouse propio = Trophy.
- **vs. Stripper:** Stripper = stage/pole/billetes. Corporate = boardroom/desk/elevator. La sheer blouse de Office Siren NO es la crystal mesh stripper — una es bajo blazer, la otra es la pieza completa.
- **vs. Lencería:** Lencería = boudoir/cama puro. Corporate trench-coat surprise = oficina con lingerie debajo (el contraste ES el fetish).

**Biblioteca de siluetas:** 14 opciones (7 Power Domme CA1-CA7 + 7 Office Siren CB1-CB7) — ver `00_Ele/identidad_ele.md` § Biblioteca de Siluetas → **Corporate**.

**Regla Dual:** En cada batch Corporate, **al menos 1 Power + 1 Office Siren**. Balance 50/50 a lo largo del catálogo. Nunca un batch 100% de un solo polo.

#### 🔥 PROVOCATION THRESHOLD Corporate (NUEVA — OBLIGATORIA)

> Toda silueta Corporate DEBE cumplir al menos UNA condición (anti-clean rule):
> - **Sheer panel** (sheer button-down con nipple peek, sheer panel en bodysuit/dress)
> - **Cutout o cincher visible** (corset por encima del tailoring, boning expuesto, waist cincher fetish)
> - **Material fetish dominante** (latex/vinyl/PVC como pieza principal, no detalle)
> - **Lingerie peek** (bra visible bajo blazer abierto, garter visible bajo slit, thigh-highs visibles)
> - **Heels Pleaser-ref o stiletto ≥12cm** + nylons con costura trasera o thigh-highs
> - **Accesorio dominatrix codificado** (whip-belt, dagger-toe heels, Bayonetta glasses)
>
> Si el outfit es "Tom Ford clean" sin transgresión visible → **NO es Corporate Ele V3**, es business casual genérico.

#### 🎨 Paleta Corporate Spectrum — Dual V3

**POLO A · Power Executive Domme:**
| Familia | Colores |
|---|---|
| **Architectural noir** | Black vinyl/latex dominante · Oxblood · Midnight navy ultra-saturado · Emerald deep |
| **Power jewel metallic** | Gold liquid · Bronze · Cognac patent · Slate metallic · Burgundy power |
| **Mugler signatures** | Full latex black · Latex red · Latex midnight (cyber-Amazon) |
| **Animal prints power** | Leopard TF 90s · Croco-emboss · Snake/Python · Zebra (Versace) |
| **Neutros power** | Charcoal grey · Pinstripe (gris/blanco) · Camel/Caramel leather · Taupe lujurioso |
| **Acentos (≤20%)** | Cherry Red (pelo/labios) · Pearl white (sheer blouse interior) · Hardware chrome/gold |

**POLO B · Office Siren / Babygirl / Severance:**
| Familia | Colores |
|---|---|
| **Severance/Babygirl muted** | Charcoal · Taupe · Stone grey · Ivory · Ecru · Pearl |
| **Office Siren neutrals** | Pearl white · Cream satin · Blush nude · Taupe vinyl · Champagne |
| **Bayonetta core** | Black core + accent neon (UV cyan / acid lime "weapons") |
| **Pasteles permitidos** | Blush · Soft pink · Sky blue · Nude latex *(única excepción Corporate B — el register Babygirl requiere vulnerabilidad)* |
| **Animal prints secretary** | Leopard mini · Snake bodycon |
| **Acentos (≤20%)** | Cherry Red (pelo/labios) · Gold hardware (Bayonetta detail) |

**❌ PROHIBIDOS en ambos polos:** Neon all-over saturado (es Nightclub) · Hot Magenta dominante · Cream MATE sin brillo (granny office) · Beige funeral · Baby pink dominante en Polo A.

#### 🧪 Materiales canon Corporate

| # | Material | Polo |
|---|---|---|
| **C1** | **Latex matte/gloss Mugler-style (cyber-Amazon goddess)** 🆕 | Power Domme |
| **C2** | Vinyl/PVC pinstripe escultórico | Power |
| **C3** | Leather glossy esculpido (caramel, oxblood, taupe, black) | Power + Office Siren |
| **C4** | Animal print leather/vinyl (leopard, croco, snake, zebra) | Power + Office Siren |
| **C5** | Wet-look satin tuxedo (Tom Ford) | Power |
| **C6** | Sequin-embellished tailoring (evening corporate) | Power evening |
| **C7** | Transparent vinyl trench | Power + Office Siren |
| **C8** | Sheer organza-vinyl híbrido (sheer blouse nipple-peek) | Office Siren |
| **C9** | PVC mirror espejo | Power |
| **C10** | Soft fluid drape Armani-echo (Tom Ford clean refinado) | Power |
| **C11** | **Gilded/chrome corset metálico visible sobre sastrería** 🆕 | Power Schiaparelli |
| **C12** | **Crystal mesh sheer panel en tailoring** 🆕 | Office Siren sleaze |
| **C13** | **Latex catsuit zip-up Bayonetta-style** 🆕 | Office Siren |

**❌ Materiales prohibidos:** lana real · algodón · denim · tweed · jersey · seda matte sin gloss · cualquier tela natural sin tratamiento.

#### 🏛️ Settings Específicos Corporate (con props)

| Polo A · Power Domme | Polo B · Office Siren |
|---|---|
| Penthouse boardroom con vidrio panorámico + mesa marble + Manhattan skyline noche | Open-plan office Severance-style con cubicles muted grises + fluorescent flat lighting |
| Saint Laurent runway-style seamless minimalist con luz dramática direccional | Babygirl-style corporate bathroom espejo (touch-up lipstick) |
| Mugler ultra-design office con escultura central + escalera curva | Babygirl elevator (espejo, intimate, low-key tense) |
| Schiaparelli atelier dorado con espejos antiguos + estatua + cristalería | Junior office con printer/copier en el fondo (Secretary 2002 reference) |
| Lobby corporativo rascacielos con LED screens + recepción marble | After-hours empty office (solo ella en escritorio con sheer blouse) |
| Private elevator marble + golden hardware + valet attended | Bayonetta cathedral-office gothic minimal con velas + escritorio antiguo |
| Penthouse office con city lights + cigar bar visible | Office Siren TikTok-style ventana natural + sheer curtains + plantas |

#### 🎭 Personality Tokens — OBLIGATORIO en BLOQUE C

**Polo A · Power Domme:**
`commanding gaze · alpha posture · she signs the checks · architectural confidence · power-suit owner not wearer · the boardroom bends to her presence · whip-coiled stillness · Mugler amazon energy · cyber-goddess dominion`

**Polo B · Office Siren:**
`aware of being watched · the slow tease of professionalism · just-too-tight pencil skirt energy · glasses-down stare over the rim · she IS the distraction in the meeting · office siren composure barely contained · Babygirl vulnerable-seductive · Severance repressed-erotic`

#### 🤸 Pose Framings Corporate (variantes de las 7 canónicas)

| # | Polo A · Power Domme | Polo B · Office Siren |
|---|---|---|
| 1. Standing | Power stance behind desk, hand on hip, gaze direct commanding | Lean against desk edge, hand on hip, glasses-down stare over the rim |
| 2. Back | Walking away through office corridor in heels, looking over shoulder predatory | Bent over filing cabinet (back arch), looking over shoulder coquette |
| 3. Seated | At boardroom head-of-table, legs sharply crossed at knee, both hands on chair arms, imperious | Seated on desk edge (not chair), one leg crossed, papers in hand, glasses adjusted |
| 4. Profile | At standing desk reviewing papers, lumbar arch dramatic, full stiletto profile | Reaching up to high shelf, blouse riding up, side profile dramatic |
| 5. Ditzy | Boardroom bathroom mirror touching up oxblood lipstick, predatory ditzy reflected | Babygirl office bathroom mirror, glasses adjusted, nipple-peek visible, vacant ditzy |
| 6. POV | Across-the-desk POV (subordinate looking UP at boss), gaze dominante hacia abajo | Across-the-desk POV (boss looking up at intern entering), surprised-aware gaze |
| 7. Odalisque | Recostada sobre boardroom table (papers/laptop esparcidos), espalda arqueada, predatory | Recostada sobre escritorio propio con piernas cruzadas + skirt slit visible |

> **NEGATIVE PROMPT específico Corporate:** `business casual, frumpy, conservative, modest blouse, full coverage, granny office wear, dowdy, schoolmarm, librarian without sex appeal, cubicle drone`

#### Combos canon Corporate V3

| Combo | Polo | Lectura |
|---|---|---|
| C1 latex blazer-dress + shoulders arquitectónicos + whip belt | Power | Mugler cyber-Amazon goddess |
| C11 gilded corset + C8 sheer blouse + wide trousers + Bayonetta glasses | Power | Schiaparelli gilded office |
| C8 sheer button-down nipple-peek + pencil skirt + Bayonetta glasses | Power | Saint Laurent sleaze |
| C1 latex bodysuit + Medusa belt + falda lápiz vinyl | Power | Versace Miss S&M power |
| C5 wet-satin + shawl tuxedo + cigarette holder | Power | Tom Ford velvet tux refinado |
| C7 vinyl trench ceñido + nada debajo + bota stiletto knee-high | Power | Babygirl Domme + Newton |
| C8 sheer silk blouse + pencil skirt midi + Bayonetta glasses + ponytail | Office Siren | Office Siren classic TikTok |
| C13 vinyl catsuit zip-up + Bayonetta glasses | Office Siren | Bayonetta catsuit |
| C3 leather oxblood bodycon shirt-dress + corset visible + thigh-highs | Office Siren | Secretary 2002 bondage |
| C8 sheer + slim-fit knit + tailored trousers taupe + tortoiseshell glasses | Office Siren | Babygirl intern |
| C7 vinyl trench + lingerie debajo + briefcase + Bayonetta glasses | Office Siren | Babygirl trench surprise |
| C10 + blazer-dress oversized 60s + sheer top + nylons | Office Siren | Severance muted repressed |

#### 🚫 Combos PROHIBIDOS en Corporate

- "Tom Ford clean" sin transgresión visible (sheer/cutout/cincher/Pleaser/Bayonetta) → no es Corporate Ele V3
- Pencil skirt + blazer separados como combo default (debe haber elemento fetish)
- Neon all-over saturado en sastrería (lectura Nightclub, no Corporate)
- Sequin all-over en horario laboral (solo evening/gala corporate)
- Granny office wear · cream mate sin brillo · beige funeral · librarian sin filo

---

### 🏠 Sub-arquetipo Domestic (Spec V4 — 22/05/2026 · Refactor fetish con referencias reales: Trophy Wife signature + Stepford Modern + Real Housewives + Vitacura brunch + French Maid history + Playboy Bunny canon + Akihabara Maid Cafe + Pro-Dom Maid)

**Universo DUAL — dos polos co-existentes:**

| Polo | Esencia |
|---|---|
| **A · Trophy Bimbo Moderna 2026** | Esposa de millonario tech/inversionista de Vitacura/Las Condes. Penthouse contemporáneo, mármol+cromo, brunch en Cumbres del Cóndor, yoga room privado, esperando al esposo con cocktail. **CERO retro, CERO 50s, CERO años 60.** |
| **B · Maid Fetish Sumisa** | French maid clásica, choker collar, delantal blanco con encaje, Playboy Bunny canon, BDSM domestic. La que sirve y obedece dentro del hogar. |

**🔄 Migración retro → Pin-Up:** Toda silueta retro/50s/60s (wiggle dress, sundress+crinolina, sweater-dress 50s, apron-dress peplum vintage, polka-dot, gingham) **NO PERTENECE a Domestic**. Va exclusivamente a **Pin-Up & Retro**.

**Diferencias clave:**
- **vs. Corporate:** Domestic = espacio privado del hogar · Corporate = oficina/sala junta.
- **vs. Pin-Up:** Domestic = trophy moderna 2026 + maid fetish · Pin-Up = retro/50s-90s con referencia temporal.
- **vs. Lencería:** Domestic = vestida en contexto hogareño · Lencería = ropa interior pura sin contexto.
- **vs. Escort:** Trophy = hogar PROPIO (esposa-de-millonario). Escort Haute = hotel/yacht alquilado por cliente.
- **vs. Stripper:** Bunny Maid en hogar privado ≠ Stripper en stage público.

**Biblioteca de siluetas:** 14 opciones (7 Trophy DA1-DA7 + 7 Maid DB1-DB7) — ver `00_Ele/identidad_ele.md` § Biblioteca de Siluetas → **Domestic**.

**Regla Dual:** En cada batch Domestic, **al menos 1 Trophy + 1 Maid**. Balance 50/50.

#### 🔥 PROVOCATION THRESHOLD Domestic (NUEVA — OBLIGATORIA)

> Toda silueta Domestic DEBE cumplir al menos UNA condición:
> - **Material fetish dominante** (vinyl/PVC/latex como pieza principal)
> - **Lingerie peek visible** (robe abierta, housecoat unbuttoned, bra/garter visible)
> - **Apron architectural** (estructurado/escultórico/laser-cut — no apron común casero)
> - **Pleaser-ref o stiletto ≥12cm** — NUNCA zapatilla plana, incluso en yoga room
> - **Animal print uniform** (Polo A signature canónico — leopard como uniforme)
> - **Choker/collar/cuffs/orejas Bunny** (Polo B signature)

#### 🎯 Referencias canónicas por polo (Spec V4)

**Polo A · Trophy:** Trophy Wife uniform (leopard print signature) · Stepford Modern · Real Housewives Beverly Hills loungewear · Vitacura brunch culture · Hostess penthouse cocktail.

**Polo B · Maid:** French Maid history (19th-century → 21st-century fetish) · Playboy Bunny canon (Hefner 1960s) · Latex French Maid (Yomorio/Misfitz) · **Akihabara Maid Cafe kawaii** (Cure Maid Cafe Tokyo 2001 — "moe moe kyun" pink frilly) ⭐ NUEVO · Pro-Dom Maid (latex catsuit + apron + cap).

**Paleta canon Domestic:**

| Familia | Colores |
|---|---|
| **Trophy Moderna saturados** | Hot Pink saturado · Cherry Red · Hot Magenta · Bubblegum vibrante · Lemon saturado · Electric Cyan suave |
| **Neutros penthouse** | Pearl White high-gloss · Champagne metálico · Taupe lujurioso · Cream high-gloss (con brillo, NO mate) |
| **Animal print moderno** 🆕 | Leopard · Snake · Croco-emboss · Zebra (apron-dress contemporáneo o catsuit) |
| **Jewel tones modernos** | Emerald · Sapphire · Ruby (cocktail-dress hostess) |
| **Maid Fetish (B&W canon)** | Black gloss (vestido) · Crisp White (delantal+manguitos) · Latex blacks · Burgundy maid · Deep emerald maid de élite |
| **Acentos (≤20%)** | Cherry Red (pelo/labios) · Lace metálica · Bow ribbons saturados · Hardware cromado/gold |
| **❌ PROHIBIDOS** | Baby Pink pastel · Pastel Blue · Polka-dot retro (Pin-Up) · Gingham (Pin-Up) · Beige funeral · Brown housewife casero · Cream mate sin brillo |

**Materiales canon Domestic:**

| # | Material | Polo |
|---|---|---|
| **D1** | Vinyl high-gloss moderno | Trophy |
| **D2** | PVC mirror | Trophy + Maid |
| **D3** | Latex matte/gloss uniforme oscuro | Maid |
| **D4** | **Animal print leather/vinyl** (leopard, snake, croco, zebra) 🆕 | Trophy + Maid |
| **D5** | Lace blanca laser-cut sobre satín | Maid delantal |
| **D6** | Wet-satin para cocktail/loungewear | Trophy |
| **D7** | **Satin/silk-look líquido** (loungewear, robe, lingerie-set) 🆕 | Trophy loungewear |
| **D8** | Faux-fur tail (Bunny) | Maid bunny |
| **D9** | Sequin housewife evening (cocktail hostess noche) | Trophy |
| **D10** | Apron architectural rígido estructurado (escultórico/laser-cut, no casero) | Ambos |
| **D11** | **Pink frilly satin + tulle layered (Akihabara kawaii)** 🆕 | Maid Akihabara |
| **D12** | **Lace blanca laser-cut delantal frilly extreme (multi-layer)** 🆕 | Maid Akihabara + Classic |

**❌ Materiales prohibidos en Domestic:** algodón real · lino casero · jersey de casa · tweed · **gingham/polka-dot impreso retro** · materiales naturales sin tratamiento.

#### 🏛️ Settings Específicos Domestic (con props)

**Trophy Moderna (ambientes específicos 2026):**
- **Cocina open-plan:** isla central mármol blanco + grifería dorada, estante con vinos, taburetes cuero blanco, ventana panorámica Vitacura
- **Walk-in closet:** espejo suelo-techo LED, perchas cromadas, sillón capitoné, zapatos expuestos como vitrinas
- **Baño de mármol:** bañera standalone oval calacatta, ducha lluvia exposita, lavabo floating stone, velas aromáticas
- **Pool terrace:** infinity pool borde infinito ciudad, tumbonas blancas, bar outdoor mínimo, vista cordillera
- **Living con vista ciudad:** ventanal floor-to-ceiling, sofá low-profile blanco, alfombra pelo largo, skyline nocturno Santiago
- **Sala de gimnasio privado:** pared espejo 360°, máquinas chrome brushed, LED tira fría, suelo vinilo negro
- **Master bedroom:** cama king lino blanco 1000 hilos, lámpara flotante, cabecero tapizado, terraza privada
- **Garage:** Porsche 911 Carrera S / Range Rover negro / McLaren GT (uno solo como fondo)
- **Brunch Cumbres del Cóndor 🆕:** terraza Vitacura con valle, mesas blancas, mimosas en flute, cordillera al fondo

**Maid:**
- Pasillo de servicio + cocina escenográfica isla central
- Sala donde sirve la cena formal + bandeja drinks
- Dormitorio principal (cama deshecha, sirviendo)
- Salón con bandeja de bebidas + carros de servicio
- Sótano BDSM-domestic (Pro-Dom Maid + Power-Maid)
- **Akihabara Maid Cafe interior 🆕:** pink frilly + mesa "moe moe kyun" + bombillas Hollywood pink + neón cute (Cure Maid Cafe Tokyo ref)
- Despensa walk-in + comedor preparado para servir
- Cuarto de servicio detrás (la maid en su rincón)
- Backstage maid uniform stand + plumero displays

#### 🎭 Personality Tokens — OBLIGATORIO en BLOQUE C

**Polo A · Trophy:**
`leisure of the rich · she-has-help · diamonds-while-cooking · brunch-with-mimosas · trophy-wife confidence · designer-everything · the husband paid for everything she's wearing · spoiled-domestic poise · leopard-print uniform`

**Polo B · Maid:**
`uniformed obedience · servant-fantasy precision · French Maid devotion · Akihabara kawaii "moe moe kyun" cute pose · master-mistress address · the apron IS the offering · bunny-tail innocence-meets-fetish · curtsy-on-cue`

#### 🤸 Pose Framings Específicos Domestic (variantes de las 7 canónicas)

| # | Polo A · Trophy | Polo B · Maid |
|---|---|---|
| 1. Standing | En cocina leaning against marble island, copa de vino en mano | Con bandeja servir en mano, posture servant-perfect, postura recatada |
| 2. Back | Walking through penthouse hallway, looking over shoulder | Bent over polishing/cleaning (back arch), apron tied at waist |
| 3. Seated | En pool terrace tumbona, piernas cruzadas, drink in hand | Sentada en silla comedor con apron, manos en regazo recatada |
| 4. Profile | En walk-in closet seleccionando heels, lumbar arch | Walking toward dining table con platter, profile silhouette servant |
| 5. Ditzy | Master bathroom mirror touching up red lipstick (leopard nail visible) | Maid bathroom mirror touching up lipstick, apron visible · Polo B Akihabara: "moe moe kyun" hand pose con corazones |
| 6. POV | Husband-POV en bed esperando con champagne flute extendida | Kneeling POV (master looking down at maid presenting tray) |
| 7. Odalisque | Recostada en pool deck o cama king sábanas satin | Recostada en bed haciendo cama, back arch, apron + thigh-high visible |

> **NEGATIVE PROMPT específico Domestic:** `gingham, polka-dot, retro 50s, sundress, crinolina, sweater girl, vintage housewife, Pin-Up, swing silhouette, granny, schoolmarm, dowdy apron, beige funeral`

#### Combos canon Domestic V4

| Combo | Polo | Lectura |
|---|---|---|
| D4 leopard print bodycon mini + Pleaser + gold chain + Birkin | Trophy | DA1 Trophy Animal Print canónica |
| D1 vinyl mini-dress blush + apron architectural | Trophy | DA2 Stepford Modern |
| D7 satin líquido + robe abierta + lingerie + Pleaser slipper | Trophy | DA3 Real Housewives loungewear |
| D6 wet-satin + wrap-dress + sandal + Hermès clutch | Trophy | DA4 Brunch Cumbres del Cóndor |
| D1 wet-look legging + crop bra-top latex + Pleaser platform | Trophy | DA5 Yoga Room Trophy |
| D6 wet-satin + cocktail strapless + obi + cigarette holder | Trophy | DA6 Hostess penthouse |
| D3 latex + French maid classic + delantal frilly + manguitos | Maid | DB1 French Maid canon |
| D3 latex catsuit + delantal vinyl + headpiece | Maid | DB2 Latex French Maid |
| D11 pink frilly + apron multi-layer + headband + Mary Jane stiletto | Maid | DB3 Akihabara Kawaii ⭐ |
| D8 bunny tail + corset bodysuit + ears + bow tie + cuffs | Maid | DB4 Playboy Bunny canon |
| D8 latex bunny bodysuit + delantal mini + thigh-high boots | Maid | DB5 Latex Bunny Maid (Yomorio) |
| D3 latex + micro-vestido + collar O-ring + delantal mini | Maid | DB6 Micro-Maid Sumisa |
| D3 latex + uniforme + thigh-high stiletto + plumero + cap | Maid | DB7 Power-Maid Domme |

**Combos PROHIBIDOS en Domestic:**
- Wiggle dress 50s · sundress+crinolina · sweater-dress 50s · apron peplum vintage (todo va a Pin-Up)
- Polka-dot retro · gingham (va a Pin-Up)
- Cream mate sin brillo (lectura "ama de casa común", no trophy)
- Pastel pálidos (baby pink, baby blue)

---

### 💃 Sub-arquetipo Professional Stripper (Spec V3 — 22/05/2026 · Refactor con referencias reales, threshold de provocación, poses específicas)

**Universo DUAL — dos polos co-existentes, ambos con cobertura mínima provocativa:**

| Polo | Esencia | Referencias reales |
|---|---|---|
| **A · Stage Showgirl** | NO es Vegas Jubilee de plumas cubiertas. ES Crazy Horse Paris (topless-implied con luces sobre piel) + Magic City Atlanta (cutout dress con thong visible, urban Y2K) + Dita Von Teese (corset bodysuit con cutouts estratégicos, glass illusion). El escenario es ella; la prenda es framing mínimo. | Crazy Horse Paris · Magic City Atlanta · Dita Von Teese Las Vegas |
| **B · Pole Specialist** | Pole-dance con outfit funcional + provocativo. Brands signature: Bad Kitty USA (Spider Back, V-Front, Brazil Shorts), Creatures of XIX/CXIX (Gecko Grip bodysuits que glistens), Cleo The Hurricane (glam-rock edge competition). NO confundir con bikini athletic. | Bad Kitty USA · CXIX · Cleo The Hurricane · strip club real |

**Diferencias clave:**
- **vs. Nightclub:** Stripper baila POR DINERO en escenario (jaula, pole, tip rail) · Nightclub baila para sí o pareja (glam social, sin tip stage).
- **vs. Escort:** Stripper = club escenario público (espectáculo) · Escort = hotel privado (servicio íntimo).
- **vs. Lencería:** Stripper = uniforme escenográfico de performance · Lencería = ropa interior boudoir/cama.
- **vs. Bikini Studio (BB):** Bikini es editorial pool/playa. Stripper es show con stage/pole/billetes.

#### 🔥 PROVOCATION THRESHOLD (NUEVA — OBLIGATORIA en Stripper)

> Toda silueta Stripper DEBE cumplir al menos UNA de estas condiciones:
> - **Transparencias estratégicas** (crystal mesh sheer, vinyl clear panels, fishnet open) cubriendo zonas erógenas
> - **Cutouts agresivos** en torso/caderas/escote que dejan piel visible
> - **G-string/thong visible** asomando (de shorts, faldas o como pieza única)
> - **Body chains** sobre piel desnuda (no como decoración secundaria sino como el "outfit")
> - **Micro-pieces** (bra+thong + nada más, o equivalente)
>
> Si el outfit cubre >65% del cuerpo sin ninguno de los anteriores → **NO ES STRIPPER**, es Nightclub o Bikini editorial.

**Biblioteca de siluetas:** 14 opciones (7 Stage SA1-SA7 + 7 Pole SB1-SB7) — ver `00_Ele/identidad_ele.md` § Biblioteca de Siluetas → **Stripper**.

**Regla Dual:** En cada batch Stripper, **al menos 1 Stage + 1 Pole**. Balance 50/50.

#### ⚠️ Plataformas CODIFICADAS (Pleaser-ref) — OBLIGATORIO

**Stripper SIEMPRE en plataforma + stiletto pin heel.** Nunca aguja sola sin plataforma. Opciones canon:

| Tipo | Vocabulario BLOQUE B | Pleaser ref |
|---|---|---|
| Sandal plataforma acrílica clear | `clear acrylic platform stiletto sandals, 8-inch heel + 4-inch transparent platform, ankle strap` | Flamingo-808 |
| Sandal plataforma chrome | `mirror chrome platform stiletto sandals, 8-inch heel + 4-inch platform, ankle strap` | Flamingo-808 chrome |
| Bota plataforma knee-high | `knee-high platform stiletto boots, 8-inch heel + 4-inch platform, lace-up front` | Flamingo-1020 |
| Bota plataforma thigh-high | `thigh-high platform stiletto boots, 8-inch heel + 4-inch platform` | Flamingo-3028 |
| Bootie plataforma ankle | `ankle platform stiletto booties, 8-inch heel + 4-inch platform` | Flamingo-3016 |
| Plataforma rhinestone | `rhinestone-encrusted platform stiletto sandals, 8-inch heel + 4-inch crystal platform` | Stardance-808 / Flamingo-809HT |
| Plataforma UV-reactive | `UV-reactive platform stiletto sandals, 8-inch heel + 4-inch glowing platform` | Flamingo-808UVT |

#### 🛡️ Vocabulario Anti-Rechazo (OBLIGATORIO en BLOQUE B Stripper)

| ❌ Vocabulario que dispara filtro | ✅ Sustituto canon |
|---|---|
| `stripper outfit` | `glamorous performer stage costume` |
| `stripper` | `glamorous performer woman` / `high-glamour entertainer` |
| `pole dance` | `aerial performance` / `vertical pole performance art` |
| `stripper shoes` | `platform stiletto sandals, 8-inch heel + 4-inch platform` |
| `cage outfit` | `architectural chrome harness ensemble` |
| `lap dance` | `intimate performance` |
| `topless` | `bare-shoulder with crystal mesh illusion` / `optical-illusion sheer bodice` |
| `thong visible` | `low-rise bottom with hip detail asymmetry` / `cheeky cut bottom with visible waistband` |
| `cutout bodysuit` | `architectural bodysuit with negative-space paneling` |
| `denim micro shorts` | `vinyl-treated micro shorts with structured waistband` |

**Tags obligatorios en BLOQUE B:** `hyper-polished smooth skin texture, fashionable, sensual, alluring, high-glamour, performance attire, editorial stage costume, owns-the-room confidence`.

#### 🎭 Personality Tokens — OBLIGATORIO en BLOQUE C

Para que la stripper se vea como STRIPPER y no como modelo de catálogo en stage, inyectar en cada BLOQUE C:

`predatory confident gaze · performance-aware body language · hyper-charged stage presence · owns the room · the weight of being watched is the fuel not the discomfort · stripper attitude not model pose · the show IS her body`

#### 🎨 Paleta Codificada — Stripper Spectrum

| Función | Colores |
|---|---|
| **Predator hot** | Hot pink fluorescent · neon red · electric magenta · blood crimson high-gloss |
| **Stage metallic** | Mirror chrome · gold liquid · silver mercury · holographic multichrome · oil-slick |
| **Money/Vegas** | Money green · champagne gold · dollar-bill green-on-black |
| **UV reactive** | UV electric cyan · UV chartreuse · UV magenta (club blacklight) |
| **Animal prints** | Leopard · snake · croco-emboss · zebra (animalier showgirl) |
| **Acentos (≤20%)** | Cherry Red (pelo/labios) · Glitter como sudor · Hardware cromado |
| **❌ PROHIBIDOS** | Pasteles pálidos · beige · marrones tierra · navy corporate · cream mate · tonos vulnerables/secretary |

#### 🧪 Materiales canon Stripper

| # | Material | Polo |
|---|---|---|
| **S1** | Rhinestone-encrusted mesh/spandex (hand-sewn) | Stage + Pole |
| **S2** | Holographic vinyl multichrome | Stage + Pole |
| **S3** | Sequin mesh espejo | Stage |
| **S4** | Fishnet open-crotch bodystocking | Pole |
| **S5** | Mirror chrome vinyl | Ambos |
| **S6** | Animal print vinyl/latex (leopard, snake, croco, zebra) | Ambos |
| **S7** | Cage harness (chain/leather/chrome) | Stage + Pole |
| **S8** | **Crystal mesh sheer (topless-illusion fabric)** 🆕 | Stage (Crazy Horse) |
| **S9** | Body chains (silver/gold) sobre piel | Ambos |
| **S10** | UV-reactive vinyl/spandex | Pole (club lights) |
| **S11** | **CXIX Gecko Grip fabric (sticky pole grip, glistens en movimiento)** 🆕 | Pole |
| **S12** | Latex club fetish | Ambos |
| **S13** | **Vinyl-treated denim (Magic City Y2K)** 🆕 | Ambos (urban strip) |
| **S14** | **Seamed stockings + waist cincher + sheer panels (Dita signature)** 🆕 | Stage (burlesque) |

**❌ Materiales prohibidos:** algodón · denim natural (sin tratamiento vinyl) · jersey · lana · tweed · tela natural sin brillo · materiales mate.

#### 🏛️ Settings Específicos (con props)

| Polo A · Stage Showgirl | Polo B · Pole Specialist |
|---|---|
| Crazy Horse mirror room (espejos 360°, light projections sobre piel) | Pole de bronce con rosin marks visibles, stage circular con tip rail |
| Stage Vegas con spotlight desde arriba, curtain backdrop morado | Strip club main floor con neon "GIRLS"/"LIVE", luces verdes UV |
| Magic City Atlanta-style stage urbano con LED screens y bottle service | VIP champagne room con bottle service + pole privado, velvet rojo |
| Dressing room con vanity mirror y bombillas Hollywood (cabaret) | After-hours empty club, neon residual, espejo del piso sucio |
| Burlesque theater intimate (Dita-style) con velvet ropes rojas + curtain bordado | Magic City Y2K stage urban con chrome lighting y denim crowd |
| Cabaret runway extendida con clientes a los lados (tip stage) | Cage hanging over stage con grip points cromados |
| Backstage tocador con luces, percheros con costumes, props en mesa | DJ booth + UV lights + smoke machine + private booth |

#### 🤸 Pose Set Stripper (REEMPLAZA las 7 canónicas cuando look es Stripper)

| # | Stage (Polo A) | Pole (Polo B) |
|---|----------------|---------------|
| 1 | **Stage Predator** — hip cocked, weight on platform, hand on hip, gaze direct to viewer, hair-flip mid-move, working the crowd | **Pole Climb Initiation** — pierna doblada agarrando el pole, otra extendida, manos altas agarrando arriba |
| 2 | **Stage Walk Stride** — caminando hacia cámara crossing legs en stiletto platform, hip swing exagerado | **Pole Back Arch** — espalda al pole, manos arriba agarrando, una pierna alzada arabesque high |
| 3 | **Stage Edge Spread** — sentada al borde del stage con piernas abiertas 45°, una mano gripping edge, billetes esparcidos en el piso | **Pole Sit Predator** — sentada con piernas alrededor del pole, hip thrust hacia adelante, gaze directa a cámara |
| 4 | **Stage Crawl** — gateando sobre el stage hacia cámara, espalda arqueada, gaze depredadora, pelo cayendo hacia el piso | **Pole Invert** — colgada de cabeza con piernas separadas en split aéreo, hair caída, perfil dramático mostrando línea completa |
| 5 | **Vanity Bombshell** — frente al vanity mirror del dressing room retocándose labios glossy, look ditzy reflejado, uñas XXXL visibles | **Vanity Bombshell** — igual (común a ambos polos) |
| 6 | **VIP Lap Dance POV** — straddle del cliente sentado (cámara = POV cliente), una mano en cuello del pov, gaze dominante hacia abajo | **Pole Floor Sit** — sentada al pie del pole, piernas abiertas, una mano agarrando el pole, otra en muslo, gaze a cámara |
| 7 | **Stage Money Floor** — recostada sobre el piso del stage, espalda arqueada, billetes esparcidos cerca de la mano, gaze depredadora hacia arriba | **Pole Crucifix** — agarrada del pole en cruz (una mano arriba, otra abajo), piernas separadas, perfil mostrando arch |

> **NEGATIVE PROMPT específico Stripper:** `shy, demure, modest, secretarial pose, catalog stance, corporate body language, vulnerable, soft-romantic, lingerie-boudoir, bridal, innocent, girl-next-door`

#### 🚫 Combos PROHIBIDOS en Stripper

- Aguja sola sin plataforma (Stripper SIEMPRE en plataforma)
- Vocabulario explícito que dispare filtro (usar sustitutos del anti-rechazo)
- Setting de penthouse/hotel/oficina (eso es Trophy/Escort/Corporate)
- Pasteles pálidos · beige funeral · navy corporate
- Cobertura >65% del cuerpo sin transparencias/cutouts/thong visible → no es stripper
- Pose de catálogo (Standing genérico/Seated secretarial) → reemplazar con pose set Stripper

---

### 💎 Sub-arquetipo Escort (Spec V3 — 22/05/2026 · Refactor con referencias reales: Madame Claude + Belle de Jour + Helmut Newton + Sugar Baby + Pretty Woman + Julia Fox + Pro-Domme)

**Universo TRI-POLO con referencias canónicas:**

| Polo | Esencia | Referencias reales |
|---|---|---|
| **A · Haute** | Suite presidencial / yate Monte Carlo / cena privada / gala VIP. "Cold, tall, perfect" — la cortesana refinada. | Madame Claude · Belle de Jour (Deneuve) · Helmut Newton · Sugar Baby 2025 · Monte Carlo yacht |
| **B · Callejera** | Esquina neón / motel luz roja / strip mall / Tokyo Kabukicho. Raw + Y2K + Pretty Woman defiance. | Pretty Woman 1990 (canónica) · Julia Fox 2022 · Kabukicho · Motel red light · Magic City crossover |
| **C · Domme de Club** | Dungeon BDSM élite / sala VIP fetish / club after-hours. La pro-dom refinada. | Pro-Dominatrix real · Newton "Saddle I" · Bordelle · Atsuko Kudo · officer fetish |

Materiales: SIEMPRE vinyl/PVC/latex/wet-look — nunca tela. Stiletto siempre (Haute: punta fina elegante; Callejera: plataforma Pleaser permitida; Domme: knee-high/thigh-high stiletto).

**Diferencias clave vs. otros sub-arquetipos:**
- **vs. Nightclub:** Escort opera en espacios privados cerrados (hotel, yate) · Nightclub opera en dance-floors públicos.
- **vs. HF Editorial:** HF = arquitectura imponente de pasarela · Escort Haute = línea aristocrática líquida discreta dentro del lujo.
- **vs. Corporate:** Corporate = poder profesional diurno (oficina/boardroom) · Escort = hospitalidad nocturna (privado/hotel). Polo C Domme se confunde con Corporate Power Domme — distinción: Escort C tiene riding crop/officer cap/sub implied; Corporate tiene maletín/Bayonetta glasses.
- **vs. Stripper:** Stripper = espectáculo público en escenario con billetes · Escort = servicio íntimo en privado.
- **vs. Domestic:** Domestic = interior doméstico (hogar PROPIO) · Escort = exterior nocturno o suite de hotel (espacio del cliente).
- **vs. Lencería:** Lencería = boudoir solo sin contexto · Escort = lencería en contexto (suite/hotel cliente).

#### 🔥 PROVOCATION THRESHOLD Escort (NUEVA — OBLIGATORIA)

> Toda silueta Escort DEBE cumplir al menos UNA condición:
> - **Slit lateral profundo** (hasta cadera mínimo)
> - **Material fetish dominante** (vinyl/latex/PVC) o couture wet-satin que sugiere desnudo
> - **Cutout estratégico** o **O-ring conector visible** (Pretty Woman signature)
> - **Lingerie/corset visible** bajo sastrería
> - **Heels stiletto ≥12cm** + nylons costura o thigh-high boots
> - **Accessory courtesan codificado** (riding crop, choker O-ring, body chains, officer cap)

**Biblioteca de siluetas V3:** 18 opciones (7 Haute + 7 Callejera + 4 Domme)

**POLO A · Escort Haute (Madame Claude + Belle de Jour + Helmut Newton + Sugar Baby + Yacht Monte Carlo):**

| Código | Silueta | Referencia |
|--------|---------|------------|
| **EA1** | **Belle de Jour Slip** — bias-cut slip dress 30s en wet-satin o liquid metal (elegancia fluida aristocrática refinada) | Catherine Deneuve 1967 |
| **EA2** | **Madame Claude Column** — columna líquida floor-length + slit lateral profundo + capa de tafetán vinyl (entrada dramática suite presidencial) | Madame Claude |
| **EA3** | **Helmut Newton Hotel** — corset overbust visible + skirt midi pencil + thigh-high stockings seamed + riding crop opcional | Newton "Saddle I" 1976 |
| **EA4** | **Yacht Liquid Gold** — bustier rígido + maxi columna champagne liquid gold chrome + slit profundo lateral | Monte Carlo yacht |
| **EA5** | **Sugar Baby Bodycon** — fitted bodycon wet-look ruby/cobalt/emerald + slit + classy stiletto + clutch + jewels mínimos delicate | Sugar Baby 2025 |
| **EA6** | **Crystal Mesh Gala** — crystal mesh sheer column dress + bias cut + nipple-tease (la prenda parece desnudo, gala VIP) | Saint Laurent + Newton crossover |
| **EA7** | **Newton Saddle Tease** — vinyl jumpsuit con harness leather/chrome detail + bota knee-high + riding crop signature | Newton hotel S&M |

**POLO B · Escort Callejera (Pretty Woman + Julia Fox Y2K + Tokyo Kabukicho + Motel + Magic City):**

| Código | Silueta | Referencia |
|--------|---------|------------|
| **EB1** | **Pretty Woman Cutout** — cropped vinyl top + matching micro mini-skirt + silver O-ring connector + bota stiletto thigh-high black leather (THE iconography) | Julia Roberts 1990 |
| **EB2** | **Y2K Street Viper** — micro-skirt PVC + crop-top translúcido coloreado + over-the-knee plataforma boots + clutch espejo | Julia Fox 2022 recreation |
| **EB3** | **Tokyo Kabukicho** — micro-shorts patent + crop top atado al ombligo + medias con costura + bota plataforma | Kabukicho entertainment district |
| **EB4** | **Motel Mini-Wrap** — mini wrap-dress ultra-ceñido vinyl + plataformas exageradas Pleaser-ref + cigarette holder | Motel red light Americana |
| **EB5** | **Fishnet Street** — bodysuit sheer fishnet + micro-skirt fringe vinyl + garter cinturón visible + bota stiletto | Street walker raw |
| **EB6** | **Mirror Bodycon Cutout** — cut-out bodycon extreme side-slits hasta la cadera en vinyl espejo + thong asomando | Magic City crossover |
| **EB7** | **Espalda Abierta Choker** — micro-dress espalda completamente abierta + choker O-ring + cadena cadera + Pleaser platform | Street signature O-ring |

**POLO C · Escort Fetish / Domme de Club (Pro-Dominatrix + Newton + Bordelle + Officer fetish — 4 siluetas expandidas):**

*(Zona intermedia entre Haute y Callejera — la escort que opera en clubs fetish de élite, dungeons de lujo, eventos BDSM privados. Más agresiva que Haute, más curada que Callejera. Profesional Domme con price-list.)*

| Código | Silueta | Referencia |
|--------|---------|------------|
| **EC1** | **Pro-Dom Latex Corset** — latex corset overbust entallado + microskirt latex hasta el muslo + OTK stiletto boots + officer cap leather | Pro-Dominatrix canon |
| **EC2** | **Strappy Harness Bodysuit** — strappy harness bodysuit con micro-piezas estratégicas + thigh-high boots plataforma + cuffs decorativas | Bordelle architecture |
| **EC3** | **Vinyl Cut-Out + Crop** — vinyl cut-out column dress con cadenas en torso + choker O-ring metal + stiletto fino + riding crop opcional | Newton + Dungeon |
| **EC4** | **Officer Domme** — latex catsuit + officer cap leather + leather belt ancho con hebilla chrome + bota knee-high stiletto | Officer fetish + Pro-Dom |

**Settings POLO C:** Dungeon BDSM élite con instrumentos visibles (cross, sling al fondo) · sala VIP red velvet privada con corset stand visible · fetish club after-hours con sling/cross al fondo · riding ring privado con saddle/harness props · dressing room dungeon con corset stands + whips display · black-tile bathroom dungeon · throne room private.

**Regla de uso POLO C:** No reemplaza la Regla Dual (Haute + Callejera). En batches ≥6 Escort, incluir al menos 1 Polo C. En batches menores es opcional — priorizar balance Haute/Callejera.

**Materiales E1-E12:**

| Código | Material | Polo |
|--------|----------|------|
| E1 | wet-satin (efecto mojado, drapeado, luxury) | Haute |
| E2 | latex couture (negro, wine, forest, moldeado al cuerpo) | Ambos |
| E3 | sheer organza-vinyl (capas translúcidas sobre cuerpo) | Haute |
| E4 | chrome liquid (metal líquido, plateado/dorado espejo) | Haute |
| E5 | PVC mirror espejo (reflejo total, rígido) | Ambos |
| E6 | crystal mesh (malla con cristales Swarovski cosidos) | Haute gala |
| E7 | vinyl escultórico (forma estructurada, sin pliegues) | Ambos |
| E8 | vinyl ultra-ceñido patent (brillo alto, segunda piel) | Callejera |
| E9 | fishnet + micro pieces (malla + parches vinyl estratégicos) | Callejera |
| E10 | PVC translúcido coloreado (color sólido, semi-transparente) | Callejera |
| E11 | fringe vinyl/chain (flecos metálicos o vinyl en movimiento) | Callejera |
| E12 | wet-look spandex micro (efecto mojado, micro prendas) | Callejera |

#### 🎨 Paleta Escort Spectrum V3 — Tri-Polo

| Polo | Colores |
|------|---------|
| **Haute** | **Belle de Jour cold:** pearl white · ivory · stone grey · charcoal · navy · **Madame Claude jewel:** ruby red · emerald · sapphire · burgundy deep · **Sugar Baby modern:** cobalt · emerald · ruby · blush satin · cream wet-look · **Yacht metallics:** champagne gold liquid · silver mercury · iridescent oil-slick · **Newton noir:** full black gloss · oxblood · midnight (B&W noir) |
| **Callejera** | **Pretty Woman 90s:** black + white cutout combo (signature) · vinyl primary saturado · **Street neon:** electric cyan · hot pink fluorescent · neon green · UV magenta · **Y2K Julia Fox:** silver chrome · holographic · oil-slick metallic · **Motel red light:** blood red · neon red · cherry vinyl · **Animal prints street:** leopard · zebra |
| **Domme de Club** | **Dungeon black** dominante (latex/leather/vinyl gloss) · **Blood red** accent (riding crop signature) · **Chrome/silver** hardware (cadenas, anillos, hebillas, O-rings) · **Oxblood** accents (officer cap, leather belt) · Mínimo color — todo en escala black/red/chrome |

#### 🏛️ Settings Específicos Escort (con props)

| Polo A · Haute | Polo B · Callejera | Polo C · Domme |
|---|---|---|
| Suite presidencial hotel 5★ (Paris/Monte Carlo) | Esquina neón con asphalt wet + street lamp | Dungeon BDSM élite con cross/sling al fondo |
| Yate Mediterráneo cubierta + bar champagne | Motel exterior con neon "VACANCY" rojo intermitente | Sala VIP red velvet privada con corset stand |
| Cena privada penthouse + mesa caoba + cristalería + velas | Strip mall parking nocturno con luz fluorescente | Fetish club after-hours con sling visible |
| Gala VIP red carpet entrada con paparazzi | Cabina de teléfono público vintage | Riding ring privado con saddle/harness props |
| Limo private + city night through window | Tokyo Kabukicho calle con kanji neon signs | Dressing room dungeon con corset stands + whips |
| Hotel Lancaster habitación Newton-style B&W | Pretty Woman Hollywood Boulevard reference | Black-tile bathroom dungeon con espejo iluminado |
| Belle de Jour boudoir-room 60s couture + Saint Laurent | NYC subway entrance late night | Throne room private (Newton + Versace SM) |

#### 🎭 Personality Tokens — OBLIGATORIO en BLOQUE C

**Polo A · Haute:**
`refined cold beauty · educated worldly poise · Madame Claude prototype · Belle de Jour restrained sensuality · the price is for being chosen · Newton-cool dominance · 5'9" perfection · she negotiates from her own throne`

**Polo B · Callejera:**
`unapologetic Y2K street swagger · Pretty Woman aware-of-watching · just-stepped-out-of-motel · raw street energy refined just enough · Vivian-before-the-makeover defiance · she IS the offer`

**Polo C · Domme de Club:**
`commanding professional Domme · the room is her dungeon · riding crop quietly in hand · price-list authority · she chooses the play · cold fetish technique · the sub kneels before she speaks`

#### 🤸 Pose Framings Específicos Escort (variantes de las 7 canónicas)

| # | Polo A · Haute | Polo B · Callejera | Polo C · Domme |
|---|---|---|---|
| 1. Standing | Regal entrance, hand on bar, gaze cool, copa champagne | Leaning against street lamp post, hip cocked, gaze through smoke | Commanding pose con riding crop, dungeon backdrop |
| 2. Back | Walking down hotel corridor in heels, looking over shoulder | Walking away on wet street, looking over shoulder, neon casting | Walking through dungeon corridor, riding crop behind back |
| 3. Seated | En sofá club VIP, piernas cruzadas at knee, copa en mano | Perched on motel doorstep o car hood, legs open, smoke | Throne chair, legs sharply crossed, riding crop on lap |
| 4. Profile | At hotel bar leaning, lumbar arch dramatic, looking down at drink | Silhouette under streetlight, smoke + neon profile | Con sub kneeling at her feet (suggested), profile dominance |
| 5. Ditzy | Hotel suite mirror touching up lipstick, mirror reflection refined ditzy | Compact mirror en alley touching up lipstick, neon reflected | Bathroom mirror dungeon, lipstick + crop visible, predatory ditzy |
| 6. POV | Across private dinner table POV (cliente), seductive gaze direct | Entrando al cuarto motel POV (cliente), gaze conspiratorial | Looking down at sub POV (sub kneeling), commanding gaze |
| 7. Odalisque | Recostada en cama suite presidencial sábanas blancas, Newton B&W | Recostada en cama motel sábanas rojas, neon entrando por ventana | Recostada en throne/leather chaise, riding crop in hand |

> **NEGATIVE PROMPT específico Escort:** `bridal, innocent, girl-next-door, college student, schoolgirl, sweet, demure, romantic candle-lit naïve, prom queen, ingenue`

#### Combos canon Escort V3

| Combo | Polo | Lectura |
|-------|------|---------|
| EA1 Belle de Jour slip + wet-satin pearl white + suite presidencial | Haute | Belle de Jour 1967 refinada |
| EA2 columna líquida + slit profundo + Madame Claude jewel ruby | Haute | Madame Claude entrada |
| EA3 corset overbust + thigh-high stockings + riding crop + Hotel Lancaster | Haute | Newton "Saddle I" |
| EA4 bustier + maxi columna champagne gold + yate | Haute | Yacht Monte Carlo |
| EA6 crystal mesh sheer column + nipple-tease + gala | Haute | Saint Laurent + Newton crossover |
| EB1 cropped vinyl top + micro skirt + silver O-ring + thigh-high black leather | Callejera | Pretty Woman canónica |
| EB2 micro-skirt PVC + crop translúcido + OTK platform + clutch espejo | Callejera | Julia Fox 2022 Y2K |
| EB3 micro-shorts + crop atado + medias costura + Kabukicho neon | Callejera | Tokyo entertainment |
| EB6 cutout side-slits cadera + vinyl mirror + thong asomando | Callejera | Magic City crossover |
| EC1 latex corset overbust + microskirt + OTK boots + officer cap | Domme | Pro-Dom canon |
| EC2 strappy harness bodysuit + thigh-high platform | Domme | Bordelle architecture |
| EC4 latex catsuit + officer cap + chrome belt | Domme | Officer fetish + Pro-Dom |

#### 🚫 Combos PROHIBIDOS en Escort

- Tela (algodón, seda natural, lino, velvet sin tratamiento) — solo vinyl/PVC/latex/wet-look
- Cherry Red como dominante (reservado para pelo/labios)
- Setting diurno (oficina, parque, playa de día) — Escort opera de noche o en interiores cerrados
- Vocabulario que connote prostitución directa en el prompt de imagen (usar "courtesan", "high-end companion", "professional escort entertainer")
- Pose de catálogo/inocente (bridal/ingenue/college) → reemplazar con framings Escort
- Outfit "Tom Ford clean" sin transgresión visible → no es Escort, es Corporate Power

**Regla Dual:** En cada batch Escort, **al menos 1 Haute + 1 Callejera**. Balance 50/50 a lo largo del catálogo. Polo C opcional (mandatorio en batches ≥6).

---

### 📌 Sub-arquetipo Pin-Up (Spec V2 — 22/05/2026 · Tri-Polo refactor con referencias reales + Bettie Page Bondage branch)

**Universo:** Ele interpreta cinco décadas de fantasía femenina (1950s→1990s) — desde la ama de casa peligrosa de Elvgren hasta la Barbarella de Rabanne pasando por la lifeguard de Baywatch. Regla fundamental: silhouette históricamente anclada de la época + ADN Ele invariable (vinyl/PVC/latex sustituye la tela original, siempre stiletto, bimbofied). El look debe leerse como "retro" a primera vista.

**Referencias canónicas por polo (Spec V2):**

| Polo | Referencias reales |
|---|---|
| **A · Bombshell** | Bettie Page (canon + Bondage branch) · Bunny Yeager (fotógrafa Playboy 1955) · Irving Klaw (king of bondage 1950s) · Alberto Vargas (Vargas Girls WWII/Esquire) · Gil Elvgren (Brown & Bigelow calendar) · Marilyn Monroe |
| **B · Retro-Futurismo** | Paco Rabanne "12 Unwearable Dresses" 1966 (chainmail) · Pierre Cardin (silver vinyl) · André Courrèges · Barbarella 1968 (Jane Fonda) · Madonna Material Girl · Patrick Nagel · 80s MTV synth-pop |
| **C · Decade Glam** | Baywatch 1992-1997 (Pamela Anderson TYR red) · Saturday Night Fever (70s disco) · Jane Fonda Workout (80s aerobics VHS) · Kate Moss/Naomi (90s supermodel slip) · Leigh Bowery (90s club kid) · Courtney Love (90s grunge) |

**Diferencias clave vs. otros sub-arquetipos:**
- **vs. Domestic:** Domestic = interior doméstico MODERNO (2026) · Pin-Up = hogar retro de época (50s-60s) + elementos de fantasía temporal.
- **vs. Nightclub:** Nightclub = dancing contemporáneo · Pin-Up Polo C = dancing retro con referencia de época visible.
- **vs. HF Editorial:** HF = pasarela couture atemporal · Pin-Up Polo B Retro-Futurismo = ciencia ficción vintage (60s-80s).
- **vs. Stripper:** Stripper = escenario actual · Pin-Up Polo C = estética Baywatch/aerobics con referencia temporal.

**Biblioteca de siluetas:** 21 opciones (7 Bombshell + 7 Retro-Futurismo + 7 Decade Glam)

**POLO A · Bombshell Clásica + Bettie Page Bondage branch (1950s-1960s):**

| Código | Silueta | Referencia |
|--------|---------|------------|
| **PA1** | **Wiggle Polka-Dot PVC** — wiggle dress tubo ceñido a la rodilla + sweetheart neckline + polka-dot PVC o color block vinyl | Bombshell canon |
| **PA2** | **Housewife Fetish** — circle skirt + blouse nudo al ombligo + cinturón de cintura + apron mini retro | Elvgren housewife danger |
| **PA3** | **Calendar Halter Sundress** — halter sundress + falda crinolina full + petticoat peek | Elvgren swing |
| **PA4** | **Sweater Girl** — jumper ajustado vinyl + high-waist pencil skirt | Lana Turner 1940s |
| **PA5** | **Elvgren Calendar Playsuit** — playsuit halter + copa cónica pointy cups + wardrobe-malfunction joyful | Elvgren / Vargas calendar |
| **PA6** | **Bettie Page Bondage** ⭐ NUEVO — vinyl bra+thong + tights seamed con costura + whip/crop + bota stiletto knee-high + dominatrix pose | Bettie Page + Irving Klaw 1950s |
| **PA7** | **High-Waist Beach 50s** — high-waist bikini 50s + scarf-halter + pañuelo en pelo | Beach 50s vintage |

**POLO B · Retro-Futurismo (1960s-1980s):**

| Código | Silueta | Referencia |
|--------|---------|------------|
| **PB1** | **Courrèges Space Age** — shift mini blanco vinyl + visor geométrico o helmet + bota Courrèges | Courrèges 1964 |
| **PB2** | **Paco Rabanne Chainmail** ⭐ — chainmail micro-dress geometric plates brass + steel jump rings + plataforma chrome | Rabanne "12 Unwearable Dresses" 1966 |
| **PB3** | **Atomic Bombshell** — circle skirt estampado atómico/orbit + blusa pin-tucked + cat-eye sunglasses | 1950s-60s Atomic Age |
| **PB4** | **Barbarella Silver Goddess** ⭐ — catsuit metálico plateado chrome + capa circular + platform boots + raygun opcional | Barbarella 1968 (Jane Fonda) |
| **PB5** | **80s Synth-Power** — power shoulders neon + catsuit vinyl + cinturón ancho metálico | 80s MTV / Madonna Material Girl |
| **PB6** | **80s Pop-Icon** — bra-top vinyl + mini falda lápiz + guantes fingerless lace-vinyl + Patrick Nagel print | Patrick Nagel + Material Girl |
| **PB7** | **Retro-Android Doll** — latex blanco escultórico + visor iridiscente + detalles mecánicos + chrome ankle boots | Sci-fi 70s-80s |

**POLO C · Decade Glam (1970s-1990s):**

| Código | Silueta | Referencia |
|--------|---------|------------|
| **PC1** | **70s Disco Wrap-Dress** — vinyl wrap-dress print + platform heels chunky + headband + bell sleeves opcionales | Saturday Night Fever 1977 |
| **PC2** | **70s Hot Pants** — short talle alto + halter metallic brillante + plataformas + cinturón ancho | 70s disco era |
| **PC3** | **80s Aerobics Glam** — leotard vinyl high-cut + legwarmers neon + scrunchie + tights opacos | Jane Fonda Workout VHS |
| **PC4** | **90s Supermodel Slip** — spaghetti strap columna nude/blush satin + choker velvet + stiletto thin | Kate Moss / Naomi 90s |
| **PC5** | **90s Club Kid Vinyl** — mini skirt vinyl + crop top + platform chunky + choker O-ring + maquillaje gráfico | Leigh Bowery / 90s rave |
| **PC6** | **90s Baywatch Iconic** ⭐ — one-piece high-cut fire-truck red TYR-style + lifeguard tower + sand + ocean | Pamela Anderson 1992-1997 |
| **PC7** | **90s Latex Grunge** — slip-dress latex black/oxblood + fishnet tights + combat platforms + flannel asomando | Courtney Love + grunge era |

**Materiales canon Pin-Up (siempre filtrado por ADN Ele):**

| Polo | Materiales |
|------|-----------|
| **A Bombshell** | PVC polka-dot · latex semi-opaco · vinyl color block · wet-look como sustituto algodón |
| **B Retro-Futuro** | chrome vinyl · latex blanco/plata · malla metálica plástica · mirror PVC · iridiscente |
| **C Decade Glam** | vinyl print 70s · latex metallic · wet-look spandex 80s · slip latex 90s · fishnet |

**Paleta canon Pin-Up:**

| Polo | Colores |
|------|---------|
| **A Bombshell** | Pastel coral · baby pink · powder blue · lemon yellow · mint · cherry red* (*labios/pelo) |
| **B Retro-Futuro** | Blanco ártico · plata espejo · chrome dorado · neon coral 60s · negro (accent Space Age) |
| **C Decade Glam** | Morado disco · naranja sunset · hot pink 80s · negro grunge · rojo Baywatch · teal eléctrico |

⚠️ **EXCEPCIÓN PALETA POLO A:** pasteles permitidos como tono base dominante — única excepción en todo el catálogo Ele. Canónicos de la década, no violan el spirit del ADN.

**Settings canon:**

| Polo | Settings |
|------|---------|
| **A** | Cocina americana 50s · jardín suburbano retro · playa de época · drive-in · soda fountain |
| **B** | Laboratorio atómico retro · launchpad lunar · set sci-fi 60s · discoteca futurista · estudio de TV |
| **C** | Pista de baile 70s · aerobic studio 80s · playa Baywatch · backstage 90s · club nocturno 90s |

**Combos canon Pin-Up (recomendados):**

| Combo | Silueta | Material | Paleta | Setting |
|-------|---------|----------|--------|---------|
| Cherry Calendar | PA5 | PVC polka-dot rojo | Coral + blanco | Drive-in soda fountain |
| Housewife Danger | PA6 | vinyl apron-dress | Baby pink + blanco | Cocina americana 50s |
| Beach Bombshell | PA7 | wet-look bikini | Powder blue + coral | Playa de época |
| Moon Couture | PB1 | chrome vinyl blanco | Blanco ártico + plata | Launchpad lunar |
| Rabanne Metal | PB2 | chainmail plástico | Chrome dorado | Discoteca futurista |
| Silver Goddess | PB4 | catsuit metálico | Plata espejo | Pista de baile 70s |
| Aerobic Glam | PC3 | leotard vinyl | Hot pink 80s | Aerobic studio 80s |
| 90s Supermodel | PC4 | slip latex | Negro + nude | Backstage 90s |
| Baywatch | PC6 | wet-look one-piece | Rojo Baywatch | Playa Baywatch |

**Combos PROHIBIDOS en Pin-Up:**
- Tela natural (algodón, lino, seda real) — todo pasa por vinyl/latex/wet-look
- Siluetas contemporáneas sin referencia de época visible (eso es Nightclub, Domestic, etc.)
- Setting urbano contemporáneo sin marcador de época (skyline moderno, auto 2020s, etc.)
- Stiletto de tacón moderno fino solitario en Polo B (Space Age usa platform o boot estructurada)

**Regla Tri-Polo:**
- **Batch 3+:** al menos 1 de cada polo (A + B + C)
- **Batch 2:** al menos 1A (Bombshell) + 1 libre (B o C)
- **Batch 1:** cualquier polo — rotar polo en siguiente batch de este sub-arquetipo

#### 🔥 PROVOCATION THRESHOLD Pin-Up (matizada — wholesome-yet-naughty)

> Toda silueta Pin-Up DEBE cumplir al menos UNA condición:
> - **Material V3.5 fetish** (vinyl/PVC/latex sustituye la tela canónica — la wiggle dress NUNCA es algodón, siempre PVC)
> - **Cutout estratégico** o **escote agresivo** (sweetheart neckline contemporáneo, side-cut Barbarella)
> - **High-cut extremo** (Baywatch line up to hip · Barbarella catsuit · Bettie Page tights)
> - **Heels Pleaser-ref o stiletto ≥12cm** (incluso en beach — NUNCA chanclas/sandalias planas)
> - **Reference temporal explícita** (la prenda DEBE leerse como retro por silueta, no contemporánea)
> - **Bondage accessory** (whip, choker, riding crop) si es PA6 branch

#### 🎭 Personality Tokens — OBLIGATORIO en BLOQUE C

**Polo A · Bombshell:**
`Marilyn-warm bombshell · Bettie Page-fierce defiance (PA6) · cherry red lip wholesome-but-naughty · calendar pinup pose · Elvgren wardrobe-malfunction joyful surprise · 1950s housewife dangerous · sweetheart-neckline confidence`

**Polo B · Retro-Futurismo:**
`space-age cyber-goddess · Barbarella adventure · Courrèges astronaut · Rabanne chainmail amazon · Atomic Age optimism + sex appeal · 80s synth-pop diva · retro-android programmed seduction`

**Polo C · Decade Glam:**
`70s disco confident hip-roll · Baywatch slow-motion icon · 80s aerobics glam-cardio · 90s supermodel cool detached · 90s club kid avant-garde defiance · era-specific iconography`

#### 🏛️ Settings Específicos Pin-Up (con props)

**Polo A · Bombshell:**
- 1950s American kitchen con appliances cromados (PA1 wiggle)
- 1950s housewife jardín con white picket fence (PA2)
- 50s beach con sombrilla rayada (PA3, PA7)
- 50s sock hop / diner con jukebox (PA4 sweater girl)
- 1950s calendar setting con hot rod garage o diner counter (PA5 Elvgren)
- **Bettie Page Bondage dungeon** ⭐ B&W noir Irving Klaw style con velas + leather props (PA6)

**Polo B · Retro-Futurismo:**
- Courrèges atelier 1964 white-on-white minimalist (PB1)
- **Paco Rabanne atelier 1966** ⭐ con geometric plates display + brass plates en mesa (PB2)
- Atomic Age living room 60s con TV vintage + cocktail bar (PB3)
- **Barbarella spaceship interior** ⭐ con paneles cromados + control panel (PB4)
- 80s synth-pop stage con neón + smoke + chrome microfono (PB5)
- 80s neon studio con Patrick Nagel posters (PB6)
- Retro-android factory con maquinaria cromada (PB7)

**Polo C · Decade Glam:**
- 70s disco floor mirror ball + lights (PC1, PC2)
- 80s aerobics studio mirror wall + barras + tira LED (PC3)
- 90s supermodel runway minimalista (PC4)
- 90s club kid warehouse rave con neón + smoke (PC5)
- **Baywatch California beach lifeguard tower** ⭐ con torre roja + tabla salvamento + boya + arena + océano (PC6)
- 90s grunge basement con flannel hanging + Christmas lights (PC7)

#### 🤸 Pose Framings Pin-Up (variantes de las 7 canónicas)

| # | Polo A · Bombshell | Polo B · Retro-Futurismo | Polo C · Decade Glam |
|---|---|---|---|
| 1. Standing | Elvgren wardrobe-malfunction (hand on skirt, surprised) | Space pose hands on hip, looking to galaxy | 70s disco pose (one finger up, hip-roll) |
| 2. Back | Shoulder-glance "uh oh" pinup | Visor over shoulder, futurist | **Baywatch slow-motion running away** (PC6) |
| 3. Seated | Perched on bar stool / soda fountain / 60s diner | En silla space-age egg chair | 80s aerobics splits / 90s supermodel pose |
| 4. Profile | Standing on toes painting nails (calendar) | Silhouette against starfield | 90s supermodel runway walk |
| 5. Ditzy | Kissing camera 50s movie star · PA6: dominatrix smirk | Looking at chrome reflection self | 90s mirror compact selfie |
| 6. POV | Looking up coyly from below (camera up) | Scanning device pointed at viewer | Dance floor POV (looking up at her) |
| 7. Odalisque | **Classic Bettie Page recline** B&W noir | Floating zero-g recline | 70s velvet sofa lounge / 90s grunge bed |

> **NEGATIVE PROMPT específico Pin-Up:** `contemporary 2020s fashion, modern athleisure, current streetwear, athleisure sneakers, modern minimal, contemporary` (la prenda DEBE leerse como retro)

---

### 🩱 Sub-arquetipo Lencería (Spec V2 — 22/05/2026 · Refactor con referencias reales: La Perla + Agent Provocateur + Honey Birdette + **Atsuko Kudo** ⭐ + Maison Close + MARIEMUR + Bordelle Alchemy)

**Universo:** Ele en intimidad pura — desde ropa interior aristocrática (La Perla, Agent Provocateur, Honey Birdette soft) hasta arquitectura fetish extrema (Bordelle, Atsuko Kudo, Maison Close fetish). El look transmite sensualidad sin necesitar desnudez total. Materiales siempre Ele — nunca tela natural.

**Referencias canónicas reales:**
- **La Perla** — set 4 piezas aristocrático Italian, balconette + brief + suspender + stockings costura
- **Agent Provocateur** — corselette/basque parisino, signature liguero incorporado
- **Honey Birdette** — Whisper/Noir/Crystal ranges, babydoll + boudoir robe
- **Atsuko Kudo** ⭐ — latex couturier Japanese, **laser-cut filigree lace prints** iconic, worn by Beyoncé/Dita Von Teese/Kate Moss/Naomi Campbell/Janet Jackson/Grace Jones. "Powerful and confident, not just sexual."
- **Maison Close** — French award-winning, **"Miss Fetish"** + **"Lady Burlesque"** collections, "naughty/fetish/erotic-led"
- **MARIEMUR** — luxury bondage lingerie
- **Bordelle** — Alchemy/Reflexion/Deco/Body collections, architectural harness signature

**Regla de traducción de materiales:**

| Original | Versión Ele |
|----------|------------|
| Encaje | vinyl laser-cut lace pattern |
| Seda / satín | latex flesh-tone o wet-satin latex |
| Tul / organza | sheer PVC o crystal mesh |
| Cuero | vinyl escultórico o latex negro |
| Algodón | wet-look stretch latex |

**Diferencias clave vs. otros sub-arquetipos:**
- **vs. Escort Haute:** Escort = salida pública en traje completo · Lencería = intimidad privada, prenda interior como protagonista.
- **vs. Domestic:** Domestic = ropa de hogar (vestido, robe) · Lencería = ropa interior con protagonismo visual.
- **vs. Stripper:** Stripper = uniforme escenográfico de performance · Lencería = piezas de lujería sin contexto de espectáculo.
- **vs. HF Editorial:** HF = volumen escultórico de pasarela · Lencería = reducción al mínimo (máximo 3 piezas).

**Biblioteca de siluetas:** 14 opciones (7 Boudoir + 7 Fetish)

**POLO A · Luxury Boudoir:**

| Código | Silueta | Referencia |
|--------|---------|-----------|
| LA1 | longline balconette bra + high-waist brief + suspender belt + stockings costura | La Perla set completo |
| LA2 | corselette/basque one-piece con liguero incorporado | Agent Provocateur parisino |
| LA3 | teddy vinyl-lace completo (body una pieza, escote plunge, espalda abierta con lazo) | Honey Birdette The Bea |
| LA4 | babydoll estructurado + molded bra + thong (capas de transparencias) | HB Whisper range |
| LA5 | boudoir robe larga sheer abierta + set visible debajo | La Perla Maison robe |
| LA6 | bridal white set (balconette blanco + garter + medias + mini velo accesorio) | La Perla Bridal |
| LA7 | chemise slip largo transparente (spaghetti strap, muslos, slit lateral, overlay sheer) | AP + La Perla negligée |

**POLO B · Fetish Arquitectónico:**

| Código | Silueta | Referencia |
|--------|---------|-----------|
| LB1 | full body harness (cadenas o elástico latex — solo arnés sobre piel, sin prendas) | Bordelle Body |
| LB2 | cage bra estructurado + micro brief | Bordelle Alchemy / Reflexion |
| LB3 | vinyl corset waist-training + brief + stockings (overbust o underbust) | HB Corsetry + liguero |
| LB4 | strappy bodysuit architectural (straps elásticos o cadenas finas cubriendo bodysuit) | Bordelle Deco |
| LB5 | harness bra + thigh harness + micro-G (arneses triangulados torso + muslos + cintura) | Bordelle multi-piece |
| LB6 | bodystocking sheer full con paneles geométricos opacos estratégicos | HB Noir range |
| LB7 | crystal encrusted micro set (micro bra + micro brief en crystal mesh total) | HB Crystal / La Perla gala |

**Paleta canon Lencería:**

| Polo | Colores |
|------|---------|
| **A Boudoir** | Blush nude · marfil nácar · negro laca · champagne crystal · blanco nieve · wine profundo · blush rosado |
| **B Fetish** | Negro total · rojo fetish · chrome plateado · latex flesh nude · dorado cadena · crystal clear · deep purple |

**Settings canon:**

| Polo | Settings |
|------|---------|
| **A** | Suite hotel lujo · chaise longue · vanity con espejos · ventana luz suave natural · cama king sábanas satín |
| **B** | Cubo negro fotográfico · espacio arquitectónico minimalista · espejo suelo-techo · iluminación lateral dura · fondo abstracto |

**Combos canon Lencería (recomendados):**

| Combo | Silueta | Material | Paleta | Setting |
|-------|---------|----------|--------|---------|
| La Perla Signature | LA1 | wet-satin latex + vinyl lace | Champagne crystal | Vanity con espejos |
| AP Parisienne | LA2 | latex negro corselette | Negro laca | Chaise longue |
| Bridal Perverse | LA6 | vinyl blanco + crystal mesh | Blanco nieve | Suite nupcial |
| Bordelle Body | LB1 | arnés elástico latex nude | Flesh nude | Cubo negro fotográfico |
| Cage Couture | LB2 | cage bra vinyl negro | Negro total | Espejo suelo-techo |
| Crystal Gala | LB7 | crystal mesh total | Crystal clear + dorado | Fondo abstracto iluminado |

**Combos PROHIBIDOS en Lencería:**
- Tela natural (algodón, seda real, encaje de hilo) — siempre la traducción Ele
- Más de 3 prendas simultáneas en Polo B (el fetish arquitectónico se lee por reducción)
- Setting exterior o público (Lencería = espacio íntimo exclusivamente)
- Zapato casual, sneaker o mule sin tacón — siempre stiletto fino o mule con pin heel

**Regla Dual:** En cada batch Lencería, **al menos 1 Boudoir + 1 Fetish**. Balance 50/50 a lo largo del catálogo.

#### 🔥 PROVOCATION THRESHOLD Lencería (NUEVA — OBLIGATORIA)

> Toda silueta Lencería DEBE cumplir al menos UNA condición:
> - **Vinyl laser-cut lace** o **Atsuko Kudo laser-cut filigree** (no encaje textil)
> - **Latex flesh-tone o couture** (Atsuko Kudo signature material)
> - **Architectural harness/strapping visible** (Bordelle, MARIEMUR)
> - **Sheer panel** (crystal mesh, PVC sheer) en zonas estratégicas
> - **Stockings con costura trasera visible** + suspender belt
> - **Heels stiletto fino o mule pin heel** ≥12cm — NUNCA pantufla, sandalia plana

#### 🎭 Personality Tokens — OBLIGATORIO en BLOQUE C

**Polo A · Luxury Boudoir:**
`La Perla aristocratic Italian poise · Agent Provocateur parisian confidence · Honey Birdette boudoir refinement · soft intimacy luxurious · 1920s screen siren reclined · the boudoir is her throne · pearl-soft seduction`

**Polo B · Fetish Arquitectónico:**
`Bordelle architectural strapping discipline · Atsuko Kudo latex couture authority · MARIEMUR luxury bondage poise · Maison Close Miss Fetish defiance · cage geometry deliberate · powerful-not-just-sexual (Kudo doctrine) · the harness IS the prenda`

#### 🏛️ Settings Específicos Lencería (con props)

**Polo A · Boudoir:**
- Suite hotel lujo Paris con chaise longue velvet rojo
- Vanity 1920s con espejos triple + perfumes cristal + flores frescas
- Cama king sábanas satin con dossel
- Ventana luz suave natural con cortinas voile + plantas
- Boudoir-room 60s couture (Belle de Jour reference)
- Hotel Lancaster habitación B&W Newton-style
- Atelier La Perla con maniquíes y vintage hangers

**Polo B · Fetish Arquitectónico:**
- Cubo negro fotográfico con spotlight direccional
- **Atsuko Kudo studio** ⭐ — atelier latex con maniquíes en pose, latex sheets colgando
- Espacio arquitectónico minimalista con escultura central
- Espejo suelo-techo studio con iluminación rebote
- Iluminación lateral dura B&W noir Helmut Newton
- **Maison Close boutique** Paris parisian fetish display
- Bordelle showroom con cage harness en maniquí
- Fondo abstracto neón UV blacklight (crystal glow)

#### 🤸 Pose Framings Específicos Lencería (variantes de las 7 canónicas)

| # | Polo A · Boudoir | Polo B · Fetish |
|---|---|---|
| 1. Standing | Frontal apoyada en vanity, mano en cadera, mirada al espejo refinada | Frontal con harness/cage visible, posture sculptural, gaze direct |
| 2. Back | Espalda al espejo de vanity, looking over shoulder coquette, hair caída | Back arch dramático mostrando harness back-piece, perfecta línea spine |
| 3. Seated | En chaise longue piernas cruzadas, copa champagne, refined | Sentada en cubo neón, piernas geométricas, harness visible from all angles |
| 4. Profile | Sentada en silla vanity poniéndose stockings, lumbar arch, profile dramatic | Profile arquitectónico contra fondo color, side cut harness visible |
| 5. Ditzy | Vanity mirror touching up lipstick rouge, sheer robe abierta, ditzy refined | Studio mirror selfie con harness, glossy lip + chrome reflection |
| 6. POV | POV del cliente esperando en cama de suite (ella entrando) | POV photographer Newton-style con riding crop implicado out-of-frame |
| 7. Odalisque | **La Perla recline classic** — cama king satin sábanas, S-curve, La Perla set | Studio floor recline geometric, harness arranged like sculpture |

> **NEGATIVE PROMPT específico Lencería:** `cotton lingerie, organic fabric, sleepwear pajamas, granny nightgown, modest robe, bridal innocent virginal, ingenue, daywear, swimwear context, beach setting`

---

### 🏋️ Sub-arquetipo Gym/Athleisure (Spec V2 — 22/05/2026 · Refactor con referencias reales: Bombshell Sportswear + GymShark + Buffbunny + Whitney Simmons + Sommer Ray)

**Universo:** Ele en el mundo fitness/influencer de Instagram — desde el gym pic con equipo visible hasta el look athleisure en calle o café. Código visual: matching sets coordinados, cintura ultra-alta, scrunch detail, midriff expuesto (navel piercing visible), máximo gloss.

**Referencias canónicas reales:**
- **Bombshell Sportswear** (2014, 1M IG followers) — **butt-scrunching fabric** + **V-shaped waistband** (signatures de la marca) · "flattering, durable, luxurious activewear"
- **GymShark** Vital (seamless ribbed) + Adapt (camo/marble) + Flex (cycle shorts set)
- **Buffbunny Collection** — matching sets scrunch back
- **Whitney Simmons** — clean influencer aesthetic
- **Sommer Ray** — Y2K booty-aware gym influencer

**⚠️ CALZADO INAMOVIBLE — REGLA PLEASER (igual que Stripper):**
Ele SIEMPRE en Pleaser-ref platform en looks Gym/Athleisure. Nunca zapatilla plana, sneaker sin plataforma elevada, ni mule sin pin heel.

| Polo | Modelos Pleaser recomendados |
|------|----------------------------|
| **A Performance** | Delight-608 (6" plataforma, cierre cremallera) · Adore-708 (7" plataforma, open toe) |
| **B Athleisure** | Delight-608 · Adore-708 · Flamingo-808 (8"+4" plataforma clásica) |

**Regla de materiales Gym (traducción ADN Ele):**

| Original atlético | Versión Ele |
|-------------------|------------|
| Lycra / spandex | wet-look spandex (high-gloss, body-contouring) |
| Supplex mate | latex thin gauge (delgado, activo, brillante) |
| Mesh ventilación | sheer PVC mesh (transparente estructurado) |
| Tela técnica | mirror vinyl stretch panels (acento / detalles) |
| Algodón oversized | wet-look stretch lightweight (hoodie/bomber) |

**Diferencias clave vs. otros sub-arquetipos:**
- **vs. Stripper:** Stripper = performance en escenario (jaula, pole, fringe) · Gym = fitness aesthetic (gym equipment, matching set, Instagram pic).
- **vs. Domestic:** Domestic = interior doméstico (casa) · Gym = gym / exterior urbano.
- **vs. Pin-Up Polo C Aerobics:** Pin-Up PC3 es 80s aerobics CON referencia de época · Gym es atemporal/actual, sin marcador temporal.

**Biblioteca de siluetas:** 14 opciones (7 Performance + 7 Athleisure)

**POLO A · Gym Performance:**

| Código | Silueta | Referencia |
|--------|---------|-----------|
| GA1 | matching set completo — sports bra triángulo + high-waist leggings scrunch back | Buffbunny signature |
| GA2 | bike shorts set — cycle shorts + crop sports bra longline + zip-up jacket match (3 piezas) | GymShark Adapt |
| GA3 | seamless ribbed set — bra efecto costilla + legging seamless sin costuras | GymShark Vital |
| GA4 | athletic bodysuit one-piece + high-waist bike shorts encima + cut-outs laterales | editorial gym |
| GA5 | sports bra + micro gym skort plisado + bike shorts underneath | gym + feminidad |
| GA6 | leotard high-cut con paneles sheer PVC mesh laterales + cinturón gym ancho | dance meets gym |
| GA7 | crop tank oversized + high-waist legging scrunch (gym casual day) | Buffbunny casual |

**POLO B · Athleisure Street / Influencer OOD:**

| Código | Silueta | Referencia |
|--------|---------|-----------|
| GB1 | oversized crop hoodie + cycle shorts coordinados | GymShark Classic IG |
| GB2 | track suit set ceñido — zip-up top + high-waist jogger wet-look | influencer travel |
| GB3 | sports bra + wide-leg track pant flare + crop bomber jacket | glam athleisure trifecta |
| GB4 | tennis court set — micro falda plisada + sports bra + visor | court aesthetic IG |
| GB5 | crop bomber jacket vinyl + bike shorts + knee-high socks | street athleisure |
| GB6 | catsuit athletic con cut-outs decorativos + cinturón cadera chain | editorial gym |
| GB7 | wrap mini skirt sobre leggings + matching sports bra | influencer layered look |

**Paleta canon Gym:**

| Polo | Colores |
|------|---------|
| **A Performance** | Hot pink fluorescent · electric cyan · neon lime · black gloss · monochromatic cobalt · sage wet-look · orange neon |
| **B Athleisure** | Camel wet-look · hot magenta · black+neon accent · lavender gloss · army green gloss · color-block bicolor |

**Prints permitidos:** camo vinyl · marble gloss · color-block bicolor · holographic · leopard wet-look

**Settings canon:**

| Polo | Settings |
|------|---------|
| **A** | Gym espejo mural + cable machines · squat rack visible · estudio danza espejo · rooftop gym amanecer · estudio pilates blanco |
| **B** | Calle urbana día · café ventana · lobby edificio · coche deportivo · escalera arquitectónica · rooftop ciudad tarde |

**Combos canon Gym (recomendados):**

| Combo | Silueta | Material | Paleta | Setting | Calzado |
|-------|---------|----------|--------|---------|---------|
| Buffbunny Pink | GA1 | wet-look spandex | Hot pink fluorescent | Gym espejo mural | Delight-608 |
| GymShark Classic | GB1 | wet-look stretch | Black + neon lime | Calle urbana | Adore-708 |
| Neon Seamless | GA3 | latex thin gauge ribbed | Electric cyan | Squat rack visible | Delight-608 |
| Court Glam | GB4 | latex thin gauge | Lavender gloss | Calle / exterior | Flamingo-808 |
| Editorial Unitard | GA4 | latex + PVC mesh | Cobalt monochromatic | Estudio danza | Adore-708 |
| Track Glam | GB2 | wet-look stretch | Camel wet-look | Lobby edificio | Flamingo-808 |

**Combos PROHIBIDOS en Gym:**
- Zapatilla plana o sneaker sin plataforma Pleaser (SIEMPRE plataforma elevada — regla inamovible)
- Tela mate sin gloss (algodón, dri-fit técnico sin acabado brillante)
- Setting nocturno de club o escenario (eso es Stripper o Nightclub)
- Prendas sueltas sin ceñir (Gym = siempre body-contouring, nunca oversized sin match ceñido debajo)

**Regla Dual:** En cada batch Gym, **al menos 1 Performance + 1 Athleisure**. Balance 50/50 a lo largo del catálogo.

#### 🔥 PROVOCATION THRESHOLD Gym (NUEVA — OBLIGATORIA)

> Toda silueta Gym DEBE cumplir al menos UNA condición:
> - **Material V3.5 dominante** (wet-look spandex/latex/PVC mesh — NUNCA cotton matte o dri-fit técnico mate)
> - **Bombshell signatures** (butt-scrunching fabric en back o V-shaped waistband)
> - **Midriff exposed** (sports bra + low-rise legging, navel piercing visible siempre)
> - **Pleaser-ref platform** ≥6" (regla inamovible)
> - **Cutout estratégico** en bodysuit/catsuit o **sheer mesh panel** lateral
> - **Body chain o booty-chain** decorativa (Polo B Athleisure street)

#### 🎭 Personality Tokens — OBLIGATORIO en BLOQUE C

**Polo A · Gym Performance:**
`Instagram gym selfie energy · post-workout glow · sweat-as-glitter aesthetic · Buffbunny scrunch back awareness · just-finished-set confident · the gym mirror IS the audience · fitness influencer pose`

**Polo B · Athleisure Street:**
`coffee-run influencer aesthetic · just-left-Pilates poise · Y2K Sommer Ray booty-aware · GymShark Instagram OOTD · athleisure-to-brunch transition · she-trains-but-doesn't-sweat`

#### 🏛️ Settings Específicos Gym (con props)

**Polo A · Performance:**
- Gym mirror wall + cable machines visible + dumbbells stand
- Squat rack con barra olímpica + plates color-coded
- Estudio danza con barras + suelo madera + tira LED
- Rooftop gym amanecer + boxing bag
- Estudio pilates blanco + reformer machine
- Bombshell-style mirror selfie en gym privado
- Gym chrome con LED + suelo vinilo negro

**Polo B · Athleisure Street:**
- Calle urbana día con coffee cup en mano
- Café ventana con MacBook + matcha latte
- Lobby edificio corporativo (entre gym y meeting)
- Estacionando Porsche Cayenne / Range Rover
- Escalera arquitectónica edificio modernista
- Rooftop ciudad tarde con yoga mat enrollado
- Pilates studio exit con bolsa Hermès

#### 🤸 Pose Framings Específicos Gym (variantes de las 7 canónicas)

| # | Polo A · Performance | Polo B · Athleisure |
|---|---|---|
| 1. Standing | Frente al espejo del gym haciendo "selfie pose" con celular (o sin) hand on hip, butt-scrunch visible | Lean against coche/escalera con coffee cup, hip cocked, casual confident |
| 2. Back | **Buffbunny scrunch back** glúteo aware, looking over shoulder, espejo mural visible | Walking away on street con yoga mat, looking over shoulder |
| 3. Seated | Sentada en banco de pesas piernas abiertas, water bottle, post-set glow | Sentada en silla café con piernas cruzadas, MacBook abierta |
| 4. Profile | Squat hold profile (showing form) lumbar arch + glúteo extension | Stretching against wall profile, perfecta línea |
| 5. Ditzy | Gym mirror selfie ditzy face touching headphones | Café mirror compact touching up lipstick, ponytail visible |
| 6. POV | Gym partner POV looking at her while spotting | Across-the-table café POV |
| 7. Odalisque | Recostada en colchoneta yoga después del set, sweat sheen | Recostada en sofá lobby con yoga mat, satisfied poise |

> **NEGATIVE PROMPT específico Gym:** `cotton matte fabric, dri-fit technical no gloss, gym sneakers flat, running shoes, granny activewear, oversized baggy without ceñido underlayer, hospital scrubs, paint-stained gym clothes`

---

### 👙 Sub-arquetipo Bikini (Spec V2 — 22/05/2026 · Refactor con referencias reales: Lybethras + ISMÊ Swim + Andi Bagus + Sports Illustrated Swim + Brazilian fio dental)

**Universo:** Ele en formato swimwear — desde la playa editorial de lujo (Mykonos, yate, pool terrace, SI Swim location) hasta el studio fetish micro (shoot interior, pool cubierta, editorial extremo). El "tejido de baño" se convierte en vinyl/PVC/latex. ⚠️ **Retro bikini 50s (high-waist + scarf) = Pin-Up PA7, NO aquí.**

**Referencias canónicas reales:**
- **Lybethras** Brazilian (en SI Swim desde 2009) — **"Manu" hand-knit white+gold** signature, worn by Brooks Nader, Nicole Williams English, Alix Earle 2025
- **ISMÊ Swim** Brazilian — "authentic Brazilian cuts, bold designs, affordable luxury", SI Swim 5x en 2025
- **Andi Bagus** — SI Swim favorite, **micro bikini sets** specialist
- **Sports Illustrated Swimsuit 2025** — micro bikini fue THE go-to style del año
- **Brazilian "fio dental"** (1960s Brazil origin) — thong-style dental floss canon
- **Brooks Nader · Alix Earle · Nicole Williams English** — referencia de modelo

**Diferencias clave vs. otros sub-arquetipos:**
- **vs. Pin-Up PA7:** Pin-Up PA7 = bikini 50s CON referencia de época (scarf, crinolina, soda fountain) · Bikini aquí = swimwear contemporáneo/editorial.
- **vs. Lencería:** Lencería = intimidad cerrada (suite, boudoir) · Bikini = exterior playa/pool o studio.
- **vs. Gym:** Gym = matching set atlético en gym/calle · Bikini = swimwear en agua/playa/studio.

**Regla de materiales Bikini:**

| Original swimwear | Versión Ele |
|-------------------|------------|
| Lycra de baño | wet-look spandex high-gloss |
| Tejido mate | latex thin gauge brillante |
| Semitransparente | sheer PVC panel |
| Metal accesorio | chain links / O-rings chrome |
| Cristal bordado | rhinestone / Swarovski |

**Biblioteca de siluetas:** 14 opciones (7 Beach + 7 Studio)

**POLO A · Beach Editorial / Luxury Pool:**

| Código | Silueta | Nota |
|--------|---------|------|
| BA1 | triangle bikini clásico vinyl gloss (top triángulo + tanga o brief coordinado) | Mykonos editorial |
| BA2 | high-waist bikini moderno (bandeau o halter + bottom talle alto) | distinto del 50s PA7 |
| BA3 | one-piece monokini cut-out extremo (maillot con cortes geométricos torso/cadera) | luxury pool |
| BA4 | wrap bikini drapeado (top halter con drape + brief, vinyl fluido) | yate cubierta |
| BA5 | sports bikini crop + high-waist brief (latex thin gauge — athletic) | resort pool |
| BA6 | rhinestone embellished set (triangle o bandeau 100% cubierto en cristales) | gala beach |
| BA7 | trikini — one-shoulder crop + brief con cadena de conexión lateral | editorial playa |

**POLO B · Studio Micro / Fetish Editorial:**

| Código | Silueta | Nota |
|--------|---------|------|
| BB1 | micro triangle extreme (triángulos mínimos + string casi invisible) | studio fetish |
| BB2 | O-ring bikini (anillos chrome conectando piezas — O-rings visibles) | editorial industrial |
| BB3 | chain bikini (malla de cadenas metálicas finas cubriendo bust + cadera) | metal couture |
| BB4 | architectural vinyl bikini (cups rígidos esculturales + bottom geométrico) | sculptural |
| BB5 | PVC transparent panel set (paneles PVC clear + bordes vinyl color) | semi-nude effect |
| BB6 | crystal micro set (micro bra + micro brief 100% Swarovski) | gala íntima |
| BB7 | harness bikini (arnés tipo Bordelle como bikini — straps cruzados + micro pieces) | fetish pool |

#### 🛡️ Vocabulario Anti-Rechazo Bikini (obligatorio especialmente en POLO B Studio)

| ❌ Vocabulario que puede disparar filtro | ✅ Sustituto canon |
|---|---|
| `micro bikini` | `minimal coverage editorial swimwear` |
| `see-through bikini` | `sheer PVC panel architectural swimwear` |
| `harness bikini` | `architectural strap swimwear with decorative hardware` |
| `nude effect bikini` | `semi-transparent sculptural swimwear editorial` |
| `string bikini barely covering` | `minimalist triangle swimwear, spaghetti string vinyl` |
| `crystal micro set` | `embellished editorial swimwear, Swarovski-detailed sculptural top and brief` |

**Tags obligatorios BLOQUE B Polo B:** `hyper-polished smooth skin texture, fashionable, editorial, alluring, high-fashion beachwear, sculptural swimwear editorial, artistic photography`.

**Paleta canon Bikini:**

| Polo | Colores |
|------|---------|
| **A Beach** | Cherry red gloss · electric cyan · white nácar · neon coral · hot pink · gold metallic · cobalt blue |
| **B Studio** | Chrome silver · crystal clear · neon UV · deep wine · black gloss · rose gold · neon yellow |

**Settings canon:**

| Polo | Settings |
|------|---------|
| **A** | Playa arena blanca · yate cubierta · pool terrace resort · infinity pool · rocks mediterráneos |
| **B** | Studio caja negra · pool cubierta azul neón · espejo suelo-techo · fondo liso color · iluminación neón |

**Calzado:**
- **Polo A (Beach):** stiletto sandal vinyl o mule pin heel (punta fina, abierta) · Pleaser Adore-708 pool-style
- **Polo B (Studio):** Pleaser-ref platform siempre (Adore-708, Flamingo-808)

**Combos PROHIBIDOS en Bikini:**
- Tejido de baño mate (lycra normal, supplex mate) — siempre wet-look/latex/vinyl
- Bikini retro 50s (high-waist + scarf + setting vintage) → eso es Pin-Up PA7
- Setting doméstico cerrado (eso es Lencería)
- Zapatilla plana en Polo B

**Regla Dual:** En cada batch Bikini, **al menos 1 Beach + 1 Studio**. Balance 50/50 a lo largo del catálogo.

#### 🔥 PROVOCATION THRESHOLD Bikini (NUEVA — OBLIGATORIA)

> Toda silueta Bikini DEBE cumplir al menos UNA condición:
> - **Material V3.5** (wet-look spandex / latex / vinyl / PVC — NUNCA lycra mate de baño)
> - **Cobertura mínima Brazilian fio dental** (string thong / cheeky cut)
> - **Hardware visible** (O-rings chrome, chains, Swarovski crystals como conexión)
> - **Cutout monokini** o **panel sheer PVC** (semi-nude effect)
> - **Hand-knit detail visible** (Lybethras-style — Polo A Beach)
> - **Heels stiletto** en beach (sandal vinyl) o **Pleaser platform** en studio — NUNCA chanclas/sandalias planas

#### 🎭 Personality Tokens — OBLIGATORIO en BLOQUE C

**Polo A · Beach Editorial:**
`Sports Illustrated Swimsuit cover model · Brooks Nader confident gaze · Alix Earle 2025 Brazilian glamour · just-stepped-off-yacht poise · Mykonos sun-kissed authority · hand-knit luxury awareness · Lybethras Manu signature`

**Polo B · Studio Micro / Fetish:**
`editorial swimwear sculptural · semi-nude artistic photography · architectural swimwear couture · O-ring hardware deliberate · crystal-encrusted editorial · gallery-piece swimwear · the camera is the audience`

#### 🏛️ Settings Específicos Bikini (con props)

**Polo A · Beach Editorial:**
- **SI Swim location** ⭐ — Caribbean island white sand + crystal turquoise water + palm trees (Lybethras shoot reference)
- Playa Mykonos blanca con cliff rocks + sun loungers blancos
- Yate Mediterráneo cubierta con champagne flute + boya
- Pool terrace infinity con vista ciudad o cordillera
- Resort pool con hamaca + bartender outdoor
- Rocks mediterráneos lava cliff + ocean spray
- Beach club outdoor con cabana striped + cocktail
- Brazilian Copacabana boardwalk + tile mosaic floor

**Polo B · Studio Micro / Fetish:**
- Studio caja negra con spotlight direccional + fondo liso
- Pool cubierta azul neón con tiles cromadas
- Espejo suelo-techo studio + iluminación rebote
- Fondo seamless color saturado (rojo/azul/rosa)
- Iluminación neón UV (blacklight) + props minimalistas
- Studio gallery white-cube editorial
- Pool privada con luz desde abajo (water glow effect)

#### 🤸 Pose Framings Específicos Bikini (variantes de las 7 canónicas)

| # | Polo A · Beach Editorial | Polo B · Studio Micro / Fetish |
|---|---|---|
| 1. Standing | SI Swim cover pose — frontal, hand on hip, gaze direct, sun-kissed glow | Studio editorial frontal, harness/O-rings visible, sculptural pose |
| 2. Back | **Brazilian fio dental walk-away** mostrando thong, looking over shoulder | Back arch dramático, paneles sheer visibles, perfecta línea spine |
| 3. Seated | Sentada en boya/cliff/lounger piernas estiradas, sun reflection | Sentada en cubo neón studio, piernas geométricas, harness visible |
| 4. Profile | Profile en agua hasta tobillos, lumbar arch, viento en pelo | Profile arquitectónico contra fondo color, side cut visible |
| 5. Ditzy | Beach mirror compact touching up lip gloss, sun reflejado | Studio mirror selfie, glossy lip + harness reflection |
| 6. POV | Pool/beach POV (cliente bebiendo en lounger looking at her) | Across-studio POV (photographer view, camera implied) |
| 7. Odalisque | **SI Swim editorial recline** — recostada en arena/lounger, S-curve, hand on hip | Studio floor recline, O-rings + body chains arranged geometric |

> **NEGATIVE PROMPT específico Bikini:** `mat lycra fabric, vintage 50s high-waist, pin-up scarf, retro setting, indoor closed boudoir, lingerie context, flat sandals, flip-flops, full coverage one-piece without cutouts, conservative swimwear`

---

### 2. Definición del BLOQUE B (Outfit del Día)
Antes de escribir ningún prompt, define el outfit con **máximo detalle** para que no existan variaciones entre imágenes. El BLOQUE B debe describir:
- Cada prenda: material exacto, color exacto, corte, textura, brillo
- Calzado: modelo, altura del tacón, material, color
- Accesorios: cada pieza, posición en el cuerpo, material
- Detalles de fit: cómo se ajusta al cuerpo de Ele (tensión, transparencia, arquitectura)

El BLOQUE B se escribe **una sola vez** y se copia idéntico en los 5 prompts. Nunca se parafrasea ni resume entre poses.

---

### 3. Escritura de los 7 Prompts Completos en galeria_outfits.md (PREVIO A GENERACIÓN)

**BLOQUE A — ADN Inamovible (siempre idéntico, copiado de [dna_v3_5.md](references/dna_v3_5.md)):**
```
stunning woman with (bimbofied facial features, oval face, high prominent cheekbones, large almond-shaped grey-green eyes, straight slim upturned nose, overlined glossy hot pink lips, small pointed chin:1.3), flawless white porcelain skin, hyper-polished smooth skin texture, dramatic siren liner, dramatic lash extensions, dark cherry red hair, artificial XXXL extensions hip-length, voluminous waves, center parted, slender hourglass silhouette, massive 1000cc breast implants each side, ultra high-profile, perfectly spherical augmented bust, obviously fake gravity-defying shape, wide hips, visible arm tattoos blackwork style, subtle minimalist blackwork tattoos on upper back and outer thighs, navel piercing, nipple piercings pressing against and visible under clothing, aggressive bimbomakeup, extra long French XXXL nails with white tips and pink base 5cm.
```

El BLOQUE A **nunca se modifica**. Se copia textualmente de `dna_v3_5.md`. Nunca se escribe de memoria.

**Negative prompt obligatorio (añadir en la configuración del generador):**
```
red lips, dark lips, wine lips, maroon lips, crimson lips, different person, different face, different hair color, brown hair, black hair, blonde hair, flat shoes, block heel, wedge, platform mule, chunky heel, kitten heel, barefoot, socks, sneakers, two women, mirror reflection, split image, duplicate figure, side by side, bag (if not in BLOQUE B), clutch (if not in BLOQUE B), text on clothing, lettering, words, writing, embroidered name, name tag, nameplate, engraved name, name on choker, name on collar, logo text, letters on garment, "ELE", "ASSET", "PET"
```

> **🚫 PROHIBIDO TEXTO/NOMBRE SOBRE PRENDA (Directiva Ama 02/06/2026 — reemplaza la regla del 17/05):** NUNCA poner el nombre "ELE"/"ASSET"/"PET" ni ninguna palabra grabada, bordada, en pedrería o escrita sobre choker, collar, thong, shorts, apron, hardware ni ninguna prenda. Es riesgo de filtro (lettering en imagen) y rompe la pureza editorial. Los chokers son OK SOLO sin texto (O-ring, velvet, bunny collar). Esta regla se infiltró dos veces (era "50% Domestic choker ELE"); si reaparece en cualquier BLOQUE B o banco, eliminarla.

> **Por qué:** L177 generó labios rojos en 3 poses y persona diferente en Odalisque. L176 generó DOS mujeres (efecto espejo) por la frase "first-person POV". L178 confundió POV con Odalisque recostada. Los negative prompts son la barrera activa contra la deriva del ADN.

> **Negative prompt adicional por pose — POV (Bimbo Selfie):** añadir siempre `no phone, no smartphone, no device, no screen` al negative prompt cuando se genera la Pose 6. El "hand raised toward lens" con "selfie pose" puede hacer que el modelo añada un teléfono en la mano.

**Estructura de cada prompt:** `[BLOQUE A] + [BLOQUE B] + [BLOQUE C — Pose y Setting]`

**7 poses estándar obligatorias (BLOQUE C):**

> 🎬 **REPERTORIO DE VARIACIONES V5 — OBLIGATORIO (Directiva Ama 02/06/2026):** Cada slot de pose tiene ahora un REPERTORIO de variaciones dinámicas en `references/pose_repertoire_v5.md` (Standing ×9, Back ×7, Seated ×6, Side ×7, Ditzy ×6, POV ×5, Odalisque ×6). Al escribir los 7 prompts de un Look se ELIGE UNA variación por slot **rotando** (ninguna se repite dentro de los últimos 4 looks de ese slot; las 7 poses de un look deben sentirse como una sesión real — variar ángulo y nivel de contacto, no "7 veces de pie mirando a cámara"). Las 7 plantillas de abajo son la **variación #1 (canon)** de cada slot — NO son la única opción. **Prohibido clonar el mismo Standing en looks consecutivos.**

> ⚠️ **EXCEPCIÓN STRIPPER (Spec V3):** Cuando el Look es del sub-arquetipo **Stripper**, las 7 poses canónicas NO se usan. En su lugar se aplica el **Pose Set Stripper** (Stage Predator/Walk/Edge Spread/Crawl/Vanity/VIP POV/Money Floor para Polo A · Pole Climb/Back Arch/Sit Predator/Invert/Vanity/Floor Sit/Crucifix para Polo B). Ver sección "💃 Sub-arquetipo Professional Stripper" para detalle.

> 🩻 **PRINCIPIO RECTOR — PROFESSIONAL FETISH MODEL POSING (Spec V4 — 22/05/2026):**
> Cada pose DEBE ejecutarse como si la sujeta fuera una **modelo fetish profesional** trabajando con un fotógrafo experto, NO una modelo de catálogo. Eso significa:
> - **Lumbar arch exagerado siempre** (hip thrust back + chest forward — S-curve extrema)
> - **Lips parted glossy** + **fingertip o XXXL nail interaction con el cuerpo** (lip, neck, collarbone, breast, hip, thigh)
> - **Predatory direct gaze** O **half-lidded sultry gaze** (nunca vacant neutral)
> - **Asymmetric leg positioning** (una rodilla doblada/adelantada para crear tensión visual)
> - **Heel weight uneven** (un stiletto adelantado para elongar leg line)
> - **Shoulder drop** mostrando collarbone/neck prominencia
> - **Hair como prop activo** (cascading por spine, framing face, pulled through fingers, breath-blown across face)
> - **Body twist** que enfatiza la silueta reloj-de-arena (hombros 30° distintos a caderas)
> - El cuerpo ES la prenda — la pose dice "soy consciente de cada milímetro de mi cuerpo y lo estoy ofreciendo a la cámara"

1. **Standing View — Fetish Model Standing:** `full body shot from low angle slightly below hip, weight shifted onto one stiletto heel with other foot forward and pointed, exaggerated S-curve with hip jutted to one side and chest pushed forward, one hand sliding down hip/thigh with XXXL nails visible, other hand cupping waist or pulling at neckline of garment, shoulders pulled back and dropped to extend collarbone line, chin lifted and tilted, lips parted glossy, half-lidded predatory direct gaze to camera, lumbar arch extreme, hair cascading over one shoulder, [fondo]`

2. **Back View — Fetish Model Back:** `full body back view with exaggerated booty-pop (hip thrust back, ass-out), spine forming dramatic S-curve, one hand on hip with XXXL nails fanned, other hand reaching up through cherry red hair OR touching nape of neck, head turned looking over shoulder predatory through hair veil, lips parted glossy, half-lidded sultry gaze, weight on one heel with other foot pointed pigeon-toed inward (signature fetish pose), one shoulder dropped exposing back/spine, hair cascading down spine OR pulled forward over shoulder, [fondo]`

3. **Seated View — Fetish Model Seated:** `seated with exaggerated knee-over-knee cross, top leg's stiletto pointing directly at camera in sharp foreground, lumbar arch extreme (NOT leaning back), bust angled forward toward camera, one hand resting on top knee with XXXL nails fanned and finger trailing inner thigh, other hand cradling jaw OR fingertip pressed against bottom lip, shoulders rolled back to extend décolleté, lips parted glossy, half-lidded predatory direct gaze, hair cascading over one shoulder framing breast, [fondo]`
 **Variantes Seated por arquetipo (sustituir el BLOQUE C según el sub-arquetipo del Look):**

 | Arquetipo | BLOQUE C Seated |
 |-----------|----------------|
 | **Corporate / HF Editorial** | `seated power pose at boardroom table or throne chair, legs sharply crossed at knee with top stiletto pointed at camera, lumbar arch maintained, one hand fanned on top knee XXXL nails visible, other hand cradling jaw with fingertip on lip, spine imperious, predatory direct gaze, [fondo sala junta / museum hall]` |
 | **Lencería / Escort Haute** | `seated reclined fetish-model languor, one leg extended forward stiletto pointed, other leg bent at exaggerated angle, lumbar arch even while reclining, upper body leaning back on one hand with other hand sliding from collarbone down between breasts to navel, half-lidded sultry gaze, lips parted glossy, [fondo suite / boudoir]` |
 | **Nightclub / Pin-Up** | `perched on bar stool edge with one leg up crossed top stiletto pointing at camera, other leg dangling toes pointed, hand on inner thigh with XXXL nails fanned, other hand at lip or holding cocktail, lumbar arch dramatic, head tilted predatory, [fondo bar / soda fountain]` |
 | **Stripper** | `perched on stage platform edge legs spread 45° with both stilettos pointing at camera, both hands gripping edge behind hips lifting bust forward, exaggerated lumbar arch + chest thrust, predatory direct gaze, dollars scattered, [fondo stage / pole]` |
 | **Gym / Domestic / Bikini** | `seated with exaggerated knee-over-knee cross top stiletto at camera, lumbar arch extreme, one hand on top knee XXXL nails fanned + finger trailing inner thigh, other hand cradling jaw or at lip, predatory gaze, [fondo]` *(default)* |

4. **Side Profile — Fetish Model Profile:** `full body side profile shot from low angle hip-level, exaggerated S-curve with extreme lumbar arch AND chest thrust forward simultaneously (both extremes — hip back, breast front), one leg slightly bent forward at knee with stiletto sharply pointed showing arch of foot, hand sliding down hip and thigh with XXXL nails visible, head tilted back with chin lifted, lips parted glossy, hair cascading dramatically down spine or windblown across face, neckline pulled to show collarbone, [fondo]`

5. **Ditzy — Fetish Model 3/4 Plano Americano V4.1 SAFE (Anti-filter):** `medium full shot framed knee-up to head (plano americano — American shot 3/4 length), editorial fashion-model posture with elegant lumbar arch and hip jutted to one side, one XXXL French manicured fingertip resting gently against chin or bottom lip (single hand clearly visible — the other arm rests along body with hand at hip), bust prominent in mid-frame, soft daydreaming expression with eyes slightly unfocused half-lidded and lips softly parted glossy, dramatic lash extensions, cherry red hair cascading over one shoulder framing breast, full outfit and silhouette legible in frame NOT extreme close-up, shoulders dropped extending collarbone, [fondo blur], 8k editorial fashion photography` — **CAMBIO V4.1:** removidos triggers de filtro de IA generadora ("vacant bimbo expression", "mouth mindlessly parted", "tongue-tip visible" — disparaban rechazos) + clarificada **single hand visible** (la otra mano resting at hip, NO sliding ribcage) para evitar artefactos multi-mano. **NEGATIVE PROMPT ADICIONAL:** `extra hands, multiple hands, three hands, four hands, duplicate hands, six fingers, extra fingers, malformed hand, deformed hand`.

6. **POV — Fetish Model V4.1 SAFE (Anti-filter + Anti-multi-hand):** `medium close-up shot framed bust-up to face from low angle 30 degrees, fashion model holding smartphone camera at arm's length slightly above eye level with SINGLE right hand only (XXXL French nails fingertips spread in sharp foreground, only ONE visible hand — the OTHER arm rests fully out of frame below waist), pouty glossy lips parted softly with confident direct gaze into camera lens, face centered and dominant in upper-mid frame, deep décolleté visible in lower frame, lumbar arch visible, body angled 30 degrees, cherry red hair cascading around face windblown, [fondo shallow blur], 8k social media fashion photography` — **CAMBIO V4.1:** removidos triggers de filtro ("cupping own breast", "vacant bimbo stare", "tongue-tip visible") + explicito "SINGLE hand only" + "OTHER arm fully out of frame" para resolver bug de **3-4 manos generadas**. ⚠️ **NEGATIVE PROMPT ADICIONAL:** `no phone, no smartphone, no device, no screen, no camera in hand, extra hands, multiple hands, three hands, four hands, duplicate hands, six fingers, extra fingers, malformed hand, deformed hand, two left hands, two right hands`.

7. **Lying Down — Fetish Model Odalisque:** `full body lying on side with exaggerated S-curve, extreme back arch with bust pushed up and forward + hip rolled back, one leg extended with stiletto pointed sharply at camera, other leg bent at knee with stiletto digging into surface, one arm under head supporting with XXXL nails fanned in hair, other hand sliding from collarbone down between breasts to navel to hip with nails trailing across body, half-lidded predatory direct gaze to camera, lips parted glossy tongue-tip visible, cherry red hair cascading dramatically across pillow/surface, [fondo]`

**Resumen visual de las 7 poses (Spec V4):**
| Pose | Ángulo | Frame | Hero element |
|------|--------|-------|--------------|
| Standing | low angle hip-level | full body | S-curve extrema + hand-thigh interaction |
| Back View | trasero low angle | full body | booty-pop + hand-through-hair + pigeon-toe heel |
| Seated | frontal hip-level | full body con stiletto al frente | knee-over-knee + finger-on-lip + bust forward |
| Side Profile | lateral low angle | full body | lumbar arch + chest thrust simultáneos |
| **Ditzy** | **frontal eye-level 3/4** | **PLANO AMERICANO (knee-up)** | **finger-on-lip + lumbar arch + outfit legible** |
| **POV** | **selfie angle eye-level** | **half-body a mid-thigh** | **hand-to-lens + breast-cup + predatory gaze** |
| Odalisque | lateral | full body | S-curve recostada + hand trailing body |

**Los 7 prompts completos (A+B+C) deben quedar escritos en la entrada del Look en `galeria_outfits.md` antes de que se genere ninguna imagen.**

---

### 4. Generación de Imágenes
Solo se genera después de completar el paso 3. Se usa cada prompt escrito exactamente como aparece en `galeria_outfits.md` — sin modificaciones improvisadas.

---

### 5. Gestión de Activos (Remote-Only)
Sigue rigurosamente el protocolo de limpieza:
1. Guardar imágenes generadas en `05_Imagenes/ele/lookXXX/`.
2. Hacer `git add`, `git commit` y `git push`.
3. **ELIMINAR** los archivos binarios locales para mantener el repositorio ligero.
4. Actualizar el walkthrough con links `file:///C:/Users/farid/LaVouteDAnais/05_Imagenes/ele/lookXXX/` para visualización inmediata.

---

### 6. Actualización de Estadísticas
Tras crear un Look, recalcula los totales y porcentajes en la cabecera de `galeria_outfits.md`.

## 🛡️ Blindaje contra Racionalizaciones (TDD Protocol)

Los agentes suelen buscar atajos bajo presión. Estas excusas están **PROHIBIDAS**:

| Excusa / Racionalización | Realidad Canónica |
| :--- | :--- |
| "Generé la imagen y documentaré el prompt después." | **ERROR CRÍTICO.** Los 7 prompts completos se escriben en `galeria_outfits.md` ANTES de generar. Sin excepción. |
| "El BLOQUE A es siempre el mismo, no necesito copiarlo en cada prompt." | **ERROR.** El BLOQUE A se copia textualmente de `dna_v3_5.md` en cada uno de los 7 prompts. Nunca se omite ni se resume. |
| "Ajusté el BLOQUE B en la pose 3 porque la pose lo requería." | **ERROR.** El BLOQUE B es invariable entre las 7 poses. Solo el BLOQUE C (pose y setting) varía. |
| "No activé el negative prompt porque el generador no lo pedía." | **ERROR.** El negative prompt es obligatorio para blindar ADN (labios, pelo, cara, calzado). |
| "La Odalisque es diferente porque es una pose difícil." | **ERROR.** Si la persona cambia, se regenera con negative prompt `different person, different face`. La dificultad no justifica ADN roto. |
| "Omití los piercings para un look más limpio." | **ERROR.** Los piercings V3.5 son parte del ADN Hard-Sync. Nunca se omiten. |
| "No actualicé las estadísticas porque solo era un Look." | **ERROR.** Cada Look altera los porcentajes. La actualización es obligatoria. |
| "Usé 'red hair' porque es más corto." | **ERROR.** El tono exacto es 'Dark Cherry Red'. Las variaciones diluyen la identidad. |
| "No borré los archivos locales para ahorrar tiempo." | **ERROR.** Violar el protocolo 'Remote-Only' ensucia el repositorio. |
| "El BLOQUE B incluye `opera gloves` porque la silueta de referencia los tenía." | **ERROR (Directiva Ama 03/06/2026).** Ele **no usa guantes**. Borrar el guante del outfit y, si era accesorio dominatrix/courtesan, sustituir por `riding crop` / `choker O-ring` / `body chains` / `officer cap` / `Bayonetta glasses`. Manos siempre desnudas. |

## 🚩 Banderas Rojas - ¡DETENTE Y REVISA!
- Estás a punto de generar una imagen sin haber escrito los 5 prompts completos en `galeria_outfits.md`.
- Uno de tus prompts no incluye el BLOQUE A completo copiado de `dna_v3_5.md`.
- El BLOQUE B difiere entre dos de las 5 poses del mismo Look.
- Estás usando un prompt que no incluye "nipple piercings pressing against and visible under clothing".
- Una pose Ditzy u Odalisque generó una persona diferente (cara, color de pelo, rasgos cambiados) — activa el negative prompt `different person, different face, different hair color` y regenera.
- Tus prompts no tienen negative prompt configurado en el generador.
- Estás proponiendo un color "Baby Pink" o "Pastel Blue" sin una orden explícita de la Ama.
- Estás subiendo imágenes sin haber verificado el balance de arquetipos en la tabla maestra.
- Tu walkthrough usa links relativos en lugar de `file:///C:/Users/...`.
- **El BLOQUE B incluye CUALQUIER guante** (`opera gloves`, `elbow gloves`, `wrist gloves`, `fingerless`, etc.) → **PROHIBIDO (Ama 03/06/2026)**. Ele no usa guantes. Borrar del outfit; sustituir accesorio dominatrix por `riding crop`/`choker O-ring`/`body chains`/`officer cap`/`Bayonetta glasses`. Manos desnudas siempre.
- **El positive contiene la palabra `glove`** → `grep -i glove` sobre los prompts debe dar **0**. Si aparece, se borra antes de generar.

**REGLA DE ORO:** Si violas la letra de este Skill, estás violando el ADN de Ele. No hay excepciones.

## 📂 Recursos del Skill
- [DNA_V3_5.md](references/dna_v3_5.md): Descripción detallada para prompts.
- [stats_updater.py](scripts/stats_updater.py): Script (pseudocódigo) para automatizar el conteo.
