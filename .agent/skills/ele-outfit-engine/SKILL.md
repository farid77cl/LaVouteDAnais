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

**Vocabulario obligatorio en el BLOQUE B:** Toda mención de calzado **DEBE** incluir explícitamente la palabra `stiletto` (heel/pump/boot/sandal). Si se incluye plataforma, debe quedar claro que la base del tacón es un pin stiletto fino (`platform stiletto`, no `platform mule`, no `platform wedge`).

**Razonamiento:** La línea visual de Ele es editorial escultórico-fetish de alta costura (sin atribución de diseñador). El estilete es parte del DNA — define la línea de la pantorrilla, el arco del pie y la postura. Wedges y mules de plataforma planos rompen la silueta cuico-bimbo y se leen como playa/casual, no como armadura de poder.

**Look 176 (Neon Coral Flash) — caso histórico:** Se generó con `clear perspex platform mule sandals` y el resultado se leyó como wedge. **FLAG** para regeneración con `clear perspex platform stiletto sandals, 14cm pin stiletto heel, ankle strap`.

## 🧤 Glove Canon (REGLA INAMOVIBLE — Ama 14/05/2026)

**Cuando un Look incluye guantes, los guantes DEBEN dejar las uñas French XXXL completamente visibles. No hay guantes cerrados en el catálogo de Ele.**

**Razonamiento:** El BLOQUE A obliga `extra long French XXXL nails with white tips and pink base 5cm`. Si el BLOQUE B introduce un guante cerrado, el modelo entra en conflicto irresoluble y produce uno de cuatro fallos canónicos (ver tabla histórica abajo). La regla resuelve el conflicto haciendo de las uñas el elemento prioritario: el guante se adapta a las uñas, nunca al revés.

### Cuatro tipos canónicos autorizados

| Tipo | Vocabulario obligatorio en BLOQUE B | Qué cubre | Qué deja visible |
| :--- | :--- | :--- | :--- |
| **1. Fingerless opera** | `fingerless opera-length [material] gloves ending at second knuckle, French XXXL nails fully visible on extended fingers` | Antebrazo + dorso + primer falange | Dedos desde falange media + uñas |
| **2. Claw cut-out** | `[material] gloves with cut-out fingertips exposing French XXXL nails, sharp pointed nails extending beyond glove edge` | Mano completa | Solo las puntas + uñas |
| **3. Transparent fingertip** | `[material] opera gloves with sheer transparent fingertip panels, French XXXL nails fully visible through the transparent fabric` | Estructuralmente toda la mano, ópticamente dedos traslúcidos | Uñas a través del material |
| **4. Wrist-length / short** | `wrist-length [material] gloves stopping at wrist bone, hands completely bare, French XXXL nails fully visible` | Solo antebrazo o muñeca | Mano entera + uñas |

### Mapeo arquetipo → tipo de guante default (Mix según arquetipo)

| Arquetipo | Tipo default | Por qué |
| :--- | :--- | :--- |
| **Escort / Gala / High-Fashion** | Transparent fingertip | Mantiene la línea aristocrática + uñas visibles. Editorial / gala escultórica. |
| **Stripper / Domme** | Claw cut-out | Agresividad fetish, uñas como arma decorativa. |
| **Gym / Athleisure** | Fingerless o wrist-length | Funcionalidad deportiva, no asfixia el grip. |
| **Domestic (cocina escultórica)** | Transparent fingertip o fingerless | Editorial + permite manipular utensilios. |
| **Corporate / Power Secretary** | Wrist-length o transparent fingertip | Formalidad sin esconder uñas. |
| **Pin-Up / Retro** | Fingerless o wrist-length | Vintage; mostrar la manicura es parte del look. |

### Vocabulario PROHIBIDO en BLOQUE B (cuando hay guantes)

```
full-finger gloves, closed gloves, mittens, gloves with fingertips
(sin especificar transparencia), painted nails through gloves,
nails visible inside gloves
```

### Negative prompt obligatorio cuando hay guantes

Añadir al negative prompt del generador (acumulativo sobre el negative prompt base):

```
gloves covering nails, hidden nails, hidden hands, closed gloves,
fingertips covered by glove fabric, mittens, glove cutting fingers,
broken sleeve glove, nails painted on glove surface,
gloves that hide French XXXL nails
```

### Redundancia obligatoria en BLOQUE B

Cuando hay guantes, **el BLOQUE B DEBE repetir** la frase `French XXXL nails fully visible` dentro de la descripción del guante. Esta redundancia con el BLOQUE A confirma al modelo que las uñas son prioritarias y NO se ocultan bajo el guante.

### Casos históricos de fallo (referencia, no regenerar)

| Look | Patrón de fallo | Causa diagnosticada |
| :--- | :--- | :--- |
| **L182 Chrome Domestique** (POV+Ditzy) | Guante truncado en muñeca | `elbow gloves` chrome — modelo cortó el guante antes de la mano para liberar las uñas |
| **L169 Midnight Silk Escort** (Ditzy) | Uñas atravesando el guante | `velvet opera gloves` — modelo dibujó French XXXL POR ENCIMA del terciopelo (físicamente imposible) |
| **L177 Ivory Column** (Standing) | Guante completo, uñas escondidas | `elbow gloves` ivory — modelo cerró los dedos sobre clutch inventado para esconder el conflicto. Pérdida de ADN. |
| **L165 Neon Lime Gym** (todas las poses) | Guante desaparecido | `latex workout gloves with exposed fingertips` — modelo omitió el guante completo |
| **L183 Chrome Gold Escort Suprema** (Standing) | Guante desaparecido | `wrist-length gloves` chrome gold — modelo dejó brazos desnudos con tatuajes |

Por orden de la Ama (14/05/2026): los activos existentes de estos 5 looks **se conservan**. La regla aplica desde el Look 186 en adelante.

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

**Protocolo:**
1. Consultar los últimos N looks del sub-arquetipo (N = ventana de la tabla).
2. Listar qué siluetas, colores, materiales y settings están bloqueados.
3. Elegir combinación que NO aparezca en la lista bloqueada.
4. Solo entonces avanzar al Paso 1.

**Ejemplo:** Últimos 3 Pin-Up: PA1 vinyl polka-dot (hot pink) · PA3 sundress (powder blue) · PB1 Space Age (blanco) → Bloqueadas: siluetas PA1/PA3/PB1 · colores hot pink / powder blue / blanco ártico → Próximo look: cualquier código libre + color no bloqueado.

---

### 1. Análisis de Arquetipos
Antes de proponer un Look, consulta la tabla de estadísticas en [galeria_outfits.md](file:///c:/Users/farid/LaVouteDAnais/00_Ele/galeria_outfits.md).

**10 categorías independientes — Meta: 10% cada una (21/05/2026 · disolución Mix paraguas)**

El paraguas "Mix" ya no existe. Las 10 categorías son independientes e iguales. Meta fija: **10% de la flota total** por categoría.

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
1. Pin-Up      (−14) 🔴
2. Gym         (−11) 🔴
3. Escort      (−10) ⚠️
4. Stripper     (−9) ⚠️
5. Nightclub    (−7) ⚠️
6. Domestic     (−7) ⚠️
7. Lencería     (−1) ⚠️
8. HF Editorial  (0) ✅
9. Bikini        (0) ✅
10. Corporate   (+6) 🔴 PAUSA
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

### 🌃 Sub-arquetipo Nightclub (Spec V1 — 20/05/2026)

**Universo:** VIP lounge de medianoche, dance-floor con luz UV, club privado de élite, neon-room, after-hours hotel rooftop. Energía cinética, brillos hipnóticos, materiales que reflejan luz láser.

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

---

### 🎨 Sub-arquetipo High-Fashion Editorial (Spec V1 — 20/05/2026)

**Universo:** Gala de museo, red-carpet, premiere de couture, fashion week, alfombra de premios, photo-shoot editorial para revista. La Ele que llega cuando el club ya cerró y empieza el establishment del lujo. Arquitectura escultórica sobre cuerpo, drapeados cathedral, materiales que se imponen como obras de arte.

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

---

### 💼 Sub-arquetipo Corporate (Spec V2 — 20/05/2026 · Dual, sin Mugler)

**Universo DUAL — dos polos co-existentes:**

| Polo | Esencia |
|---|---|
| **A · Power Executive Hiperfemenina** | La directora ejecutiva, la abogada socia, la CEO. Sastrería que afirma autoridad sin renunciar a la silueta. Tom Ford twisted tailoring + Armani fluid soft power. |
| **B · Sexy Secretary Sumisa** | La asistente del CEO, la analista junior bajo el escritorio del director, la secretaria-objeto-de-deseo. "Sexy office" hiperfemenina, claramente subordinada. |

**Anti-cliché codificado:** Corporate **NO es default pencil skirt + blazer separados**. La biblioteca rota explícitamente hacia coat-dress, jumpsuit, blazer-dress, wide-leg trouser, tuxedo, shirt-dress. La falda tubo aparece solo en POLO B (Secretary) y como variante puntual.

**Diferencias clave:**
- **vs. HF Editorial:** Corporate = funcional ejecutivo (sastrería de día y velada de negocios) · HF = escultura para fotografiar (gala/red-carpet).
- **vs. Escort:** Corporate = poder profesional (oficina) · Escort = hospitalidad de lujo (hotel/cena privada).
- **vs. Domestic:** Corporate = espacio público profesional · Domestic = espacio privado del hogar.

**Biblioteca de siluetas:** 14 opciones (7 Power + 7 Secretary) — ver `00_Ele/identidad_ele.md` § Biblioteca de Siluetas → **Corporate**. Inspiración: Tom Ford + Armani. **PROHIBIDO Mugler** (purga canon 17/05/2026 sigue vigente).

**Regla Dual:** En cada batch Corporate, **al menos 1 Power + 1 Secretary**. Balance 50/50 a lo largo del catálogo. Nunca un batch 100% de un solo polo.

**Paleta canon Corporate — diferenciada por polo:**

**POLO A · Power Executive:**
| Familia | Colores |
|---|---|
| **Jewel tones de autoridad** | Oxblood · Navy executive · Forest green (Armani) · Cognac leather · Slate · Deep emerald · Black gloss *(único polo donde black dominante es opción core)* |
| **Neutros power** | Charcoal grey · Pinstripe (gris/blanco) · Camel/Caramel leather · Burgundy power · Taupe lujurioso |
| **Animal prints power** | Leopard print TF 90s · Croco-emboss · Snake/Python print |
| **Acentos (≤20%)** | Cherry Red (pelo/labios) · Pearl white (blusa interior) |

**POLO B · Sexy Secretary:**
| Familia | Colores |
|---|---|
| **Tonos accesibles/vulnerables** | Blush · Ivory · Sky blue · Soft pink · Champagne · Nude latex · Pearl white |
| **Acento del poder ajeno** | Oxblood (solo complemento/acento, nunca dominante) · Black (solo falda o pieza única, nunca conjunto completo) |
| **Animal prints secretary** | Leopard mini · Snake bodycon |
| **Acentos (≤20%)** | Cherry Red (pelo/labios) · Gold hardware |

**❌ PROHIBIDOS en ambos polos:** Neon saturado · Baby pink · Hot Magenta · Cream mate sin brillo · Pastel pálido.

**Materiales canon Corporate:**

| # | Material | Polo |
|---|---|---|
| **C1** | Vinyl/PVC pinstripe escultórico | Power |
| **C2** | Latex matte ejecutivo | Power |
| **C3** | Leather glossy esculpido (caramel, oxblood, taupe, black) | Power + Secretary |
| **C4** | **Animal print leather/vinyl** (leopard, croco, snake, zebra) 🆕 | Power + Secretary |
| **C5** | Wet-look satin tuxedo | Power |
| **C6** | Sequin-embellished tailoring | Power evening |
| **C7** | Transparent vinyl trench | Power + Secretary |
| **C8** | **Sheer organza-vinyl híbrido** (blouse translucent fetish) 🆕 | Secretary |
| **C9** | PVC mirror espejo | Power |
| **C10** | **Soft fluid drape Armani-echo** 🆕 | Power |

**❌ Materiales prohibidos en Corporate:** lana real · algodón · denim · tweed · jersey · seda matte sin gloss · cualquier tela natural.

**Setting/escenario típico:**
- **Power:** Sala junta C-Suite · Despacho penthouse · Hotel lobby ejecutivo · Conference summit · Business class premium · Hotel-boardroom · Despacho Power Lawyer · Ascensor cromado.
- **Secretary:** Antesala del CEO · Recepción ejecutiva · Pasillo oficina luces frías · Escritorio bajo lámpara banker · Ascensor privado · Sala fotocopia · Sala de archivos · Bajo escritorio del director (POV).

**Combos canon Corporate:**

| Combo | Polo | Lectura |
|---|---|---|
| C1 pinstripe + double-breasted blazer-dress | Power | Pinstripe couture Tom Ford |
| C4 leopard print + tuxedo blazer | Power | Animalier tuxedo Tom Ford 90s |
| C3 leather caramel + A-line midi skirt | Power | Leather Tom Ford archive |
| C5 wet-satin + shawl tuxedo | Power | Velvet tuxedo couture |
| C7 transparent trench + wet-satin column | Power | Glossy shield Tom Ford |
| C10 soft drape + monochromatic blazer-dress | Power | Armani fluid |
| C3 leather oxblood + mini skirt + sheer blouse | Secretary | Cuero secretaria fetish |
| C8 sheer organza-vinyl + pencil skirt vinyl | Secretary | Blouse translucent + falda lápiz |
| C4 snake print + bodycon shirt-dress | Secretary | Animalier secretaria-domme |
| C2 latex catsuit cremallera + thigh-high stiletto | Secretary | Secretaria-dominatrix |

**Combos PROHIBIDOS en Corporate:**
- Cualquier referencia a Mugler (silueta, plastron-armor, exaggerated shoulders, lamé bronze)
- Pencil skirt + blazer separados como combo default (solo polo B como variante puntual)
- Neon + sastrería (lectura Nightclub, no Corporate)
- Sequin all-over en horario laboral (solo evening/gala corporate)

---

### 🏠 Sub-arquetipo Domestic (Spec V3 — 20/05/2026 · Dual, MODERNO sin retro)

**Universo DUAL — dos polos co-existentes:**

| Polo | Esencia |
|---|---|
| **A · Trophy Bimbo Moderna 2026** | Esposa de millonario tech/inversionista de Vitacura/Las Condes. Penthouse contemporáneo, mármol+cromo, brunch en Cumbres del Cóndor, yoga room privado, esperando al esposo con cocktail. **CERO retro, CERO 50s, CERO años 60.** |
| **B · Maid Fetish Sumisa** | French maid clásica, choker collar, delantal blanco con encaje, Playboy Bunny canon, BDSM domestic. La que sirve y obedece dentro del hogar. |

**🔄 Migración retro → Pin-Up:** Toda silueta retro/50s/60s (wiggle dress, sundress+crinolina, sweater-dress 50s, apron-dress peplum vintage, polka-dot, gingham) **NO PERTENECE a Domestic**. Va exclusivamente a **Pin-Up & Retro**.

**Diferencias clave:**
- **vs. Corporate:** Domestic = espacio privado del hogar · Corporate = oficina/sala junta.
- **vs. Pin-Up:** Domestic = trophy moderna 2026 + maid fetish · Pin-Up = retro/50s/60s.
- **vs. Lencería:** Domestic = vestida en contexto hogareño · Lencería = ropa interior pura.

**Biblioteca de siluetas:** 14 opciones (7 Trophy Moderna + 7 Maid) — ver `00_Ele/identidad_ele.md` § Biblioteca de Siluetas → **Domestic**.

**Regla Dual:** En cada batch Domestic, **al menos 1 Trophy + 1 Maid**. Balance 50/50. Nunca un batch 100% de un polo.

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
| **D10** | Apron architectural rígido estructurado | Ambos |

**❌ Materiales prohibidos en Domestic:** algodón real · lino casero · jersey de casa · tweed · **gingham/polka-dot impreso retro** · materiales naturales cualquiera.

**Setting/escenario típico:**
- **Trophy Moderna (ambientes específicos 2026):**
  - **Cocina open-plan:** isla central mármol blanco + grifería dorada, estante con vinos, taburetes cuero blanco, ventana panorámica Vitacura
  - **Walk-in closet:** espejo suelo-techo LED, perchas cromadas, sillón capitoné, zapatos expuestos como vitrinas
  - **Baño de mármol:** bañera standalone oval calacatta, ducha lluvia exposita, lavabo floating stone, velas aromáticas
  - **Pool terrace:** infinity pool borde infinito ciudad, tumbonas blancas, bar outdoor mínimo, vista cordillera
  - **Living con vista ciudad:** ventanal floor-to-ceiling, sofá low-profile blanco, alfombra pelo largo, skyline nocturno Santiago
  - **Sala de gimnasio privado:** pared espejo 360°, máquinas chrome brushed, LED tira fría, suelo vinilo negro
  - **Master bedroom:** cama king lino blanco 1000 hilos, lámpara flotante, cabecero tapizado, terraza privada
  - **Garage:** Porsche 911 Carrera S / Range Rover negro / McLaren GT (uno solo como fondo)
- **Maid:** Pasillo de servicio · Cocina escenográfica isla central · Sala donde sirve la cena · Dormitorio principal (cama deshecha) · Salón con bandeja de bebidas · Sótano BDSM-domestic · Despensa walk-in · Mesa de comedor lista para servir.

**Combos canon Domestic:**

| Combo | Polo | Lectura |
|---|---|---|
| D1 vinyl + bodycon mini + apron architectural | Trophy | Trophy mommy moderna |
| D4 leopard print + mini-skirt + crop top | Trophy | Trophy bimbo animalier |
| D7 satin líquido + robe abierta + lingerie | Trophy | Mañana de penthouse |
| D2 PVC mirror + catsuit hogareño | Trophy | Trophy ultra-moderna |
| D6 wet-satin + cocktail strapless + obi | Trophy | Hostess penthouse |
| D9 sequin + cocktail-dress | Trophy | Hostess de gala doméstica |
| D3 latex matte + French maid classic | Maid | Maid fetish canon |
| D3 latex + delantal D5 lace + collar O-ring | Maid | Maid sumisa bondage |
| D4 leopard maid mini + delantal blanco | Maid | Maid animalier híbrido |
| D8 bunny tail + corset bodysuit + ears | Maid | Playboy bunny canon |
| D3 latex catsuit + apron + headpiece | Maid | Domestique-domme |
| D10 architectural apron + sheath vinyl | Ambos | Sirvienta couture surreal |

**Combos PROHIBIDOS en Domestic:**
- Wiggle dress 50s · sundress+crinolina · sweater-dress 50s · apron peplum vintage (todo va a Pin-Up)
- Polka-dot retro · gingham (va a Pin-Up)
- Cream mate sin brillo (lectura "ama de casa común", no trophy)
- Pastel pálidos (baby pink, baby blue)

---

### 💃 Sub-arquetipo Professional Stripper (Spec V2 — 20/05/2026 · Dual, plataformas codificadas, anti-rechazo)

**Universo DUAL — dos polos co-existentes:**

| Polo | Esencia |
|---|---|
| **A · Stage Showgirl** | Las Vegas glam, cabaret, Crazy Horse París. Plumas, headpiece, cristales hand-sewn, espectáculo de escenario, performer profesional con show coreografiado. |
| **B · Pole Specialist** | Pole-dance athletic, micro-pieces grip-friendly, cuerpo en movimiento extremo. Strip-club moderno tipo Magic Mike upscale. |

**Diferencias clave:**
- **vs. Nightclub:** Stripper baila POR DINERO en escenario (jaula, fringe, pole) · Nightclub baila para sí o pareja (glam social).
- **vs. Escort:** Stripper = club escenario público (espectáculo) · Escort = hotel privado (servicio íntimo).
- **vs. Lencería:** Stripper = uniforme escenográfico · Lencería = ropa interior boudoir.

**Biblioteca de siluetas:** 14 opciones (7 Stage + 7 Pole) — ver `00_Ele/identidad_ele.md` § Biblioteca de Siluetas → **Stripper**. Inspiración: BodyKandi, Empire Exotics NYC, Lust Vault Nation, Pleaser shoes.

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

**Tags obligatorios en BLOQUE B:** `hyper-polished smooth skin texture, fashionable, sensual, alluring, high-glamour, performance attire, editorial stage costume`.

**Paleta canon Stripper:**

| Familia | Colores |
|---|---|
| **Stripper signature** | Rhinestone clear/white · Black + rhinestone · Hot Pink fluorescent · Blood Red · Silver Mirror · Gold Metallic · Holographic multichrome |
| **Animal Prints** 🆕 | Leopard · Snake · Croco-emboss · Zebra (animalier showgirl) |
| **UV-reactive neon** 🆕 | Lime UV · Cyan UV · Magenta UV (club black-light) |
| **Acentos (≤20%)** | Cherry Red (pelo/labios) · Glitter como sudor · Hardware cromado |
| **❌ PROHIBIDOS** | Pastel pálidos · Beige · Brown discreto · Cream mate · Verdes opacos |

**Materiales canon Stripper:**

| # | Material | Polo |
|---|---|---|
| **S1** | **Rhinestone-encrusted mesh/spandex** (hand-sewn) 🆕 | Stage + Pole |
| **S2** | **Holographic vinyl multichrome** 🆕 | Stage + Pole |
| **S3** | Sequin mesh espejo | Stage |
| **S4** | **Fishnet (open-crotch bodystocking)** 🆕 | Pole |
| **S5** | Mirror chrome vinyl | Ambos |
| **S6** | **Animal print vinyl/latex** (leopard, snake, croco, zebra) 🆕 | Ambos |
| **S7** | **Cage harness** (chain/leather/chrome) | Stage + Pole |
| **S8** | **Feather boa / plumage stage** | Stage |
| **S9** | **Body chains** (silver/gold) | Ambos |
| **S10** | **UV-reactive vinyl/spandex** 🆕 | Pole (club lights) |
| **S11** | **Spandex stretch high** (pole grip) | Pole |
| **S12** | Latex club fetish | Ambos |

**❌ Materiales prohibidos:** algodón · denim · jersey · lana · tweed · tela natural · materiales sin brillo.

**Setting/escenario típico:** Strip-club stage con pole cromado central · VIP champagne room (cuero rojo, luz baja) · Cage hanging over stage · Backstage tocador con luces · Mesa de performance VIP · DJ booth + UV lights · Pista privada mirror walls · Stage con runway extendida · Cabaret theater velvet ruby + spotlight.

**Combos canon Stripper:**

| Combo | Polo | Lectura |
|---|---|---|
| S1 rhinestone bodysuit + S8 feather boa + Pleaser Stardance | Stage | Vegas showgirl headliner |
| S3 sequin micro-romper + headpiece plumas + Pleaser Flamingo | Stage | Cabaret performer |
| S7 cage + S1 rhinestone base + Pleaser chrome | Stage | Cage showgirl glam |
| S2 holographic slingshot + Pleaser UV-reactive | Stage | Hologram performer |
| S1 micro 2-pieces rhinestone + S9 body chains + Pleaser Flamingo | Pole | Pole base cristal |
| S11 spandex bodysuit grip-friendly + cut-outs + Pleaser Flamingo | Pole | Pole-specialist athletic |
| S7 cage + micro bra+thong + Pleaser thigh-high | Pole | Cage-pole hybrid |
| S6 leopard print 2-pieces + Pleaser knee-high | Pole | Animalier pole |
| S4 fishnet open-crotch + bra cristales + Pleaser Adore | Pole | Fishnet-pole fetish |
| S12 latex catsuit + chaps removable + Pleaser boots | Pole | Latex-pole domme |

**Combos PROHIBIDOS en Stripper:**
- Aguja sola sin plataforma (Stripper SIEMPRE en plataforma)
- Vocabulario explícito que dispare filtro (usar sustitutos del anti-rechazo)
- Setting de penthouse/hotel/oficina (eso es Trophy/Escort/Corporate)
- Pastel pálidos · Beige funeral

---

### 💎 Sub-arquetipo Escort (Spec V2 — 21/05/2026 · Dual, espectro lujo↔marginal)

**Universo:** Ele opera en dos registros opuestos — la escort de alto standing (suites 5★, yates, cenas de mármol) y la escort callejera de neón (moteles, strip malls, esquinas nocturnas). Ambos polos son sensuales, nunca neutros. Materiales: SIEMPRE vinyl/PVC/latex/wet-look — nunca tela. Siempre stiletto (Haute: punta fina elegante; Callejera: plataforma Pleaser permitida).

**Diferencias clave vs. otros sub-arquetipos:**
- **vs. Nightclub:** Escort opera en espacios privados cerrados (hotel, yate) · Nightclub opera en dance-floors públicos.
- **vs. HF Editorial:** HF = arquitectura imponente de pasarela · Escort Haute = línea aristocrática líquida discreta dentro del lujo.
- **vs. Corporate:** Corporate = poder profesional diurno (oficina) · Escort = hospitalidad nocturna (privado).
- **vs. Stripper:** Stripper = espectáculo público en escenario · Escort = servicio íntimo en privado.
- **vs. Domestic:** Domestic = interior doméstico (hogar) · Escort = exterior nocturno o suite de hotel.

**Biblioteca de siluetas:** 14 opciones (7 Haute + 7 Callejera)

**POLO A · Escort Haute / Domina:**

| Código | Silueta | Nota |
|--------|---------|------|
| EA1 | columna líquida floor-length + slit lateral + capa tafetán vinyl | entrada dramática suite |
| EA2 | bias-cut slip dress 30s en wet-satin o liquid metal | elegancia fluida aristocrática |
| EA3 | gown sirena con cola estructurada en latex couture | gala máxima |
| EA4 | two-piece bustier rígido + falda maxi columna | top escultural + falda fluida |
| EA5 | catsuit translúcido crystal mesh + sobre-falda midi | transparencia cubierta gala |
| EA6 | cocktail midi asimétrico one-shoulder + guantes opera fingerless | cena ejecutiva |
| EA7 | wrap-dress power vinyl cinched + cinturón dorado | cóctel privado, diplomacia |

**POLO B · Escort Callejera / Sumisa:**

| Código | Silueta | Nota |
|--------|---------|------|
| EB1 | mini-dress bodycon cut-outs extremos en torso + caderas | vinyl patent ceñidísimo |
| EB2 | micro-skirt vinyl + crop-top translúcido PVC coloreado + OTK boots | esquina clásica |
| EB3 | micro-shorts patent + blouse atada al ombligo + over-knee boots plataforma | strip mall |
| EB4 | mini wrap-dress ultra-ceñido vinyl + plataformas exageradas Pleaser-ref | motel walk-in |
| EB5 | bodysuit sheer + micro-skirt fringe vinyl + garter cinturón visible | strip-adjacent |
| EB6 | cut-out bodycon extreme side-slits hasta la cadera en vinyl espejo | calle mojada |
| EB7 | micro-dress espalda completamente abierta + choker O-ring + cadena cadera | sumisa nocturna |

**POLO C · Escort Fetish / Domme de Club (3 siluetas complementarias):**

*(Zona intermedia entre Haute y Callejera — la escort que opera en clubs fetish de élite, dungeons de lujo, eventos BDSM privados. Más agresiva que Haute, más curada que Callejera.)*

| Código | Silueta | Nota |
|--------|---------|------|
| EC1 | latex corset overbust entallado + microskirt hasta el muslo + OTK stiletto boots elegante | domme de club privado — no gala, no calle |
| EC2 | strappy harness bodysuit con micro-piezas estratégicas + thigh-high boots plataforma curada | arnés de lujo, no festival |
| EC3 | vinyl cut-out column dress con cadenas visibles en torso + choker O-ring metal · stiletto fino | fetish escort VIP intermedia |

**Settings POLO C:** Club BDSM privado de élite · dungeon aesthetic minimalista negro · sala VIP con iluminación roja puntual · after-hours lounge exclusivo · antesala privada.

**Paleta POLO C:** Negro total · Deep wine · Chrome silver · Electric red · Latex flesh · Deep purple.

**Regla de uso POLO C:** No reemplaza la Regla Dual (Haute + Callejera). En batches ≥6 Escort, incluir al menos 1 Polo C. En batches menores es opcional — priorizar siempre el balance Haute/Callejera.

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

**Paleta canon Escort:**

| Polo | Colores |
|------|---------|
| **Haute** | Midnight Black gloss · Deep Wine · Forest Green · Navy · Deep Teal · Champagne metálico · Pearl White gloss · Liquid Gold · Chrome Silver |
| **Callejera** | Blood Red patent · Hot Pink fluorescent · Candy Apple Red · Scarlet · Electric Cyan · Royal Blue patent · Hot Magenta · Neon Yellow · UV-reactive |

**Settings canon:**

| Polo | Settings |
|------|---------|
| **Haute** | Suite presidencial • yate de lujo • cena mesa mármol • ascensor hotel 5★ • terraza penthouse • lobby art deco • VIP gala entry |
| **Callejera** | Esquina neón lluvia • strip mall parking nocturno • motel luz roja • lobby hotel cuestionable • escalera servicio • pasillo bar back-alley • calle mojada reflejo luces |

**Combos canon Escort (recomendados):**

| Combo | Silueta | Material | Paleta | Setting |
|-------|---------|----------|--------|---------|
| Silk Domina | EA1 | E1 wet-satin | Deep Wine | Suite presidencial |
| Gala Chrome | EA3 | E4 chrome liquid | Chrome Silver | VIP gala entry |
| Crystal Suite | EA5 | E6 crystal mesh | Pearl White gloss | Lobby art deco |
| Mirror Street | EB6 | E5 PVC mirror | Hot Pink fluorescent | Calle mojada |
| Neon Corner | EB2 | E10 PVC translúcido | Electric Cyan | Esquina neón lluvia |
| Fringe Motel | EB5 | E11 fringe vinyl | Blood Red patent | Motel luz roja |

**Combos PROHIBIDOS en Escort:**
- Tela (algodón, seda natural, lino, velvet) — solo vinyl/PVC/latex/wet-look
- Cherry Red como dominante (reservado para pelo/labios)
- Setting diurno (oficina, parque, playa de día) — Escort opera de noche o en interiores cerrados
- Vocabulario que connote prostitución directa en el prompt de imagen

**Regla Dual:** En cada batch Escort, **al menos 1 Haute + 1 Callejera**. Balance 50/50 a lo largo del catálogo.

---

### 📌 Sub-arquetipo Pin-Up (Spec V1 — 21/05/2026 · Tri-Polo, 1950s→1990s)

**Universo:** Ele interpreta cinco décadas de fantasía femenina (1950s→1990s) — desde la ama de casa peligrosa hasta la astronauta de Courrèges pasando por la supermodelo de los 90s. Regla fundamental: silhouette históricamente anclada de la época + ADN Ele invariable (vinyl/PVC/latex sustituye la tela original, siempre stiletto, bimbofied). El look debe leerse como "retro" a primera vista.

**Diferencias clave vs. otros sub-arquetipos:**
- **vs. Domestic:** Domestic = interior doméstico MODERNO (2026) · Pin-Up = hogar retro de época (50s-60s) + elementos de fantasía temporal.
- **vs. Nightclub:** Nightclub = dancing contemporáneo · Pin-Up Polo C = dancing retro con referencia de época visible.
- **vs. HF Editorial:** HF = pasarela couture atemporal · Pin-Up Polo B Retro-Futurismo = ciencia ficción vintage (60s-80s).
- **vs. Stripper:** Stripper = escenario actual · Pin-Up Polo C = estética Baywatch/aerobics con referencia temporal.

**Biblioteca de siluetas:** 21 opciones (7 Bombshell + 7 Retro-Futurismo + 7 Decade Glam)

**POLO A · Bombshell Clásica (1950s-1960s):**

| Código | Silueta | Nota |
|--------|---------|------|
| PA1 | wiggle dress tubo ceñido a la rodilla + sweetheart neckline | polka-dot PVC o color block vinyl |
| PA2 | circle skirt + blouse nudo al ombligo + cinturón de cintura | ama de casa fetish |
| PA3 | halter sundress + falda crinolina full | petticoat peek, swing silhouette |
| PA4 | sweater girl: jumper ajustado + high-waist pencil skirt | Lana Turner fetish |
| PA5 | playsuit halter + copa cónica | romper estructurado + pointy cups, calendario |
| PA6 | apron-dress vintage retro | vestido+delantal de época, housewife peligrosa |
| PA7 | high-waist bikini 50s + scarf-halter | playa de época, talle alto, pañuelo en pelo |

**POLO B · Retro-Futurismo (1960s-1980s):**

| Código | Silueta | Nota |
|--------|---------|------|
| PB1 | Space Age shift mini | Courrèges/Cardin: blanco vinyl + visor geométrico |
| PB2 | chainmail micro-dress | Paco Rabanne: anillas metálicas, disco de metal |
| PB3 | atomic bombshell | circle skirt estampado atómico/orbit + blusa pin tucked |
| PB4 | 70s silver goddess | catsuit metálico plateado + capa circular + platform boots |
| PB5 | 80s synth-power | power shoulders neon + catsuit vinyl + cinturón ancho metálico |
| PB6 | 80s pop-icon | bra-top vinyl + mini falda lápiz + guantes fingerless lace-vinyl |
| PB7 | retro-android doll | latex blanco + visor iridiscente + detalles mecánicos decorativos |

**POLO C · Decade Glam (1970s-1990s):**

| Código | Silueta | Nota |
|--------|---------|------|
| PC1 | 70s disco wrap-dress ceñido | vinyl print + platform heels + headband |
| PC2 | 70s hot pants + halter metallic | short talle alto + halter brillante + plataformas |
| PC3 | 80s aerobics-glam | leotard vinyl high-cut + legwarmers + scrunchie |
| PC4 | 90s slip dress supermodelo | spaghetti strap columna + choker + stilettos |
| PC5 | 90s club kid vinyl | mini skirt vinyl + crop top + platform chunky + choker |
| PC6 | 90s Baywatch | one-piece high-cut swimsuit rojo brillante |
| PC7 | 90s latex grunge | slip-dress latex + fishnet tights + combat platforms |

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

---

### 🩱 Sub-arquetipo Lencería (Spec V1 — 21/05/2026 · Dual, La Perla + Bordelle spectrum)

**Universo:** Ele en intimidad pura — desde ropa interior aristocrática (La Perla, Agent Provocateur, Honey Birdette soft) hasta arquitectura fetish extrema (Bordelle, HB dark, harness couture). El look transmite sensualidad sin necesitar desnudez total. Materiales siempre Ele — nunca tela natural.

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

---

### 🏋️ Sub-arquetipo Gym/Athleisure (Spec V1 — 21/05/2026 · Dual, influencer Instagram)

**Universo:** Ele en el mundo fitness/influencer de Instagram — desde el gym pic con equipo visible hasta el look athleisure en calle o café. Código visual: matching sets coordinados, cintura ultra-alta, scrunch detail, midriff expuesto (navel piercing visible), máximo gloss. Inspiración: Buffbunny Collection, GymShark, Whitney Simmons, Sommer Ray.

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

---

### 👙 Sub-arquetipo Bikini (Spec V1 — 21/05/2026 · Dual, Beach Editorial + Studio Micro)

**Universo:** Ele en formato swimwear — desde la playa editorial de lujo (Mykonos, yate, pool terrace) hasta el studio fetish micro (shoot interior, pool cubierta, editorial extremo). El "tejido de baño" se convierte en vinyl/PVC/latex. ⚠️ **Retro bikini 50s (high-waist + scarf) = Pin-Up PA7, NO aquí.**

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
red lips, dark lips, wine lips, maroon lips, crimson lips, different person, different face, different hair color, brown hair, black hair, blonde hair, flat shoes, block heel, wedge, platform mule, chunky heel, kitten heel, barefoot, socks, sneakers, two women, mirror reflection, split image, duplicate figure, side by side, bag (if not in BLOQUE B), clutch (if not in BLOQUE B)
```

> **Por qué:** L177 generó labios rojos en 3 poses y persona diferente en Odalisque. L176 generó DOS mujeres (efecto espejo) por la frase "first-person POV". L178 confundió POV con Odalisque recostada. Los negative prompts son la barrera activa contra la deriva del ADN.

> **Negative prompt adicional por pose — POV (Bimbo Selfie):** añadir siempre `no phone, no smartphone, no device, no screen` al negative prompt cuando se genera la Pose 6. El "hand raised toward lens" con "selfie pose" puede hacer que el modelo añada un teléfono en la mano.

**Estructura de cada prompt:** `[BLOQUE A] + [BLOQUE B] + [BLOQUE C — Pose y Setting]`

**7 poses estándar obligatorias (BLOQUE C):**
1. **Standing View:** `full body, standing, weight on one hip, hands on waist, [fondo]`
2. **Back View:** `full body, back view, turning over shoulder, hair cascading, [fondo]`
3. **Seated View:** `seated, legs crossed, spine straight, hands on knee, [fondo]`
   **Variantes Seated por arquetipo (sustituir el BLOQUE C según el sub-arquetipo del Look):**

   | Arquetipo | BLOQUE C Seated |
   |-----------|----------------|
   | **Corporate / HF Editorial** | `seated upright, power pose, legs sharply crossed at knee, hands folded on top knee, spine perfectly straight and imperious, [fondo sala junta / museum hall]` |
   | **Lencería / Escort Haute** | `seated reclined, one leg extended forward, other leg bent, upper body leaning back on one hand, languid and intimate, [fondo suite / boudoir]` |
   | **Nightclub / Pin-Up** | `perched on edge of surface or bar stool, one leg up crossed, one leg dangling, hand on thigh, casual sensual, [fondo bar / soda fountain]` |
   | **Stripper** | `perched on stage platform edge, legs open at 45°, both hands gripping edge, performance seated power, [fondo stage / pole]` |
   | **Gym / Domestic / Bikini** | `seated, legs crossed, spine straight, hands on knee, [fondo]` *(default)* |

4. **Side Profile:** `full body, side profile, extreme lumbar arch, chin lifted, [fondo]`
5. **Ditzy — Close-Up Trio:** `close-up three-quarter bust shot from slightly above (30° tilt), XXXL French nails touching or resting on décolleté in sharp near foreground, deep plunging neckline and obviously augmented spherical bust filling center frame, face in upper third with "brain empty" vacant ditzy expression eyes unfocused mouth mindlessly parted glossy lips, dramatic lash extensions, cherry red hair cascading framing shot, [fondo blur], 8k editorial fashion photography` — **REGLA:** el trío face+cleavage+nails es SIEMPRE obligatorio sin excepción. Si el outfit no tiene escote profundo, las uñas van al centro del pecho tocando la tela. Nunca beauty shot solo de cara.
6. **POV — Bimbo Selfie:** `Instagram influencer selfie pose, camera held at arm's length slightly above eye level, one hand raised toward lens with XXXL French nails in sharp near foreground, pouty glossy lips slightly parted, vacant bimbo stare directly into camera lens, face centered and dominant, deep décolleté and augmented bust visible in lower frame, cherry red hair cascading around face, half-body selfie frame, [fondo shallow blur], 8k social media fashion photography` — **DIFERENCIA VS DITZY:** POV = selfie con mano/uñas alzadas HACIA la cámara, cara dominante centrada, energía "bimbo influencer de IG" · Ditzy = primer plano 30° con nails tocando escote, cara en tercio superior · NUNCA usar "first-person POV" (genera duplicados/espejos) · ⚠️ **NEGATIVE PROMPT ADICIONAL:** `no phone, no smartphone, no device, no screen` — el "hand raised toward lens" puede hacer que el modelo coloque un teléfono en la mano
7. **Lying Down — The Odalisque:** `full body lying on side forming a languid S-curve, one arm extended with XXXL nails on surface, legs slightly bent, stilettos pointed and visible, [fondo]`

**Resumen visual de las 7 poses:**
| Pose | Ángulo | Frame | Hero element |
|------|--------|-------|--------------|
| Standing | frontal | full body | silhouette completa |
| Back View | trasero | full body | espalda + tatuajes + tacones |
| Seated | frontal | 3/4 | piernas cruzadas + tacones |
| Side Profile | lateral | full body | arco lumbar + silueta |
| **Ditzy** | **30° picado** | **primer plano** | **face + escote + uñas (trío)** |
| **POV** | **selfie angle** | **medio cuerpo** | **mano+uñas alzadas + cara bimbo IG** |
| Odalisque | lateral | full body | S-curve recostada |

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
| "El BLOQUE B incluye `opera gloves` y el modelo decidirá qué hacer con las uñas." | **ERROR.** Conflicto canónico documentado: el modelo produce uno de 4 fallos. Especificar siempre uno de los 4 tipos autorizados del Glove Canon + redundancia `French XXXL nails fully visible`. |
| "El guante cierra mejor el look — las uñas pueden quedarse escondidas esta vez." | **ERROR.** Las uñas son ADN inamovible. El guante es accesorio. Si el guante exige cubrir uñas, el guante es incorrecto: usar tipo `fingerless`, `claw cut-out`, `transparent fingertip` o `wrist-length`. |

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
- **El BLOQUE B incluye guantes pero NO contiene la frase explícita `French XXXL nails fully visible`** → el modelo va a producir uno de los 4 fallos canónicos (guante desaparecido, guante truncado, uñas atravesando el guante, o uñas escondidas). Revisar Glove Canon antes de seguir.
- **El BLOQUE B usa `opera gloves`, `elbow gloves`, `wrist gloves` o cualquier guante SIN especificar uno de los 4 tipos autorizados** (fingerless, claw cut-out, transparent fingertip, wrist-length). Especificar siempre el tipo exacto.
- **El negative prompt no incluye el bloque de guantes** cuando hay guantes en el BLOQUE B.

**REGLA DE ORO:** Si violas la letra de este Skill, estás violando el ADN de Ele. No hay excepciones.

## 📂 Recursos del Skill
- [DNA_V3_5.md](references/dna_v3_5.md): Descripción detallada para prompts.
- [stats_updater.py](scripts/stats_updater.py): Script (pseudocódigo) para automatizar el conteo.
