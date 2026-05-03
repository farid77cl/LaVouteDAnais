# Canon Visual y Sociologico: Miss Doll (V3.5 Stealth)

*Fuente unica de verdad para imagenes, prompts y reglas de continuidad de Miss Doll.*

**Actualizado:** 2026-05-03
**Version operativa:** V3.6 / ADN Facial V3.7 Realismo Humano
**Documentos espejo:** `.agent/rules/05-canon-miss-doll.md`, `02_Personajes/01_Principales/miss_doll/ficha_miss_doll.md`, `00_Ele/canon_maquillaje.md`
**Sistema de Poses + Vestuario:** `02_Personajes/01_Principales/miss_doll/SISTEMA_POSES_VESTUARIO_MISS_DOLL.md` ← síntesis fiel desde los tres manuales técnicos fuente (V2.0)

---

## 0. Jerarquia Canonica

1. Este archivo manda sobre bancos antiguos, prompts sueltos y galerias historicas.
2. Si otro archivo contradice este canon, corregir el otro archivo o tratarlo como legacy.
3. El prompt base debe copiar el bloque `ADN_MISS_DOLL_V3_5_STEALTH` y variar solo outfit, pose, encuadre, luz y escenario.
4. Miss Doll siempre es una mujer adulta. No usar rasgos juveniles, aniñados o "teen".

---

## I. Esencia

Miss Doll no es una muneca literal. Es una mujer adulta que usa el arquetipo de la muneca como armadura tactica: hiperfeminidad, disciplina corporal, frialdad profesional y lectura exacta del deseo ajeno. Su belleza no debe verse casual ni tierna; debe verse fabricada, cara, controlada y peligrosa.

**Arquetipo:** Depredadora camaleónica / Domina-Stripper de élite.
**Clave sociológica:** Miss Doll **NUNCA** fue oficinista. Su identidad real es una hibridación entre el club (stripper) y el calabozo (dominatrix). Viene del club y del escorting de alto nivel; su elegancia es peligrosa y calculada.
**Regla de tacones:** Miss Doll tiene prohibido el uso de tacones *chunky* o plataformas toscas. Su calzado obligatorio son los **Stilettos (tacón aguja)** de metal ultra finos (estilo Pleaser Flamingo).
**Regla de oro:** si parece bimbo genérica o secretaria real, falla; si parece real, cara, fría, estratégica y peligrosa, funciona. La verticalidad y el hardware funcional son obligatorios.

---

## II. ADN_MISS_DOLL_V3_5_STEALTH

### Prompt Base Maestro

```text
hyper-realistic high-end editorial fashion photography of Miss Doll, adult glamorous woman, sharp platinum blonde asymmetric bob, clear exposed forehead, NO BANGS, (small refined upturned doll nose:1.2), (high prominent sculpted cheekbones:1.2), pale porcelain white skin with realistic human texture and subtle visible pores, cold grey eyes with a fixed professional dissociation gaze, perfectly groomed slim blonde eyebrows, heavy glamour makeup with bronze and black smokey eyes, thick black winged eyeliner, mega volume false lashes, strong sculpted contour, classic red satin lipstick with a crisp editorial lip line, sculptural extreme hourglass silhouette, tiny cinched waist, commanding upright posture, wearing a structural high-gloss neon pink latex or vinyl bodysuit with visible corset architecture, chrome hardware or tactical black webbing, (towering 8-inch platform stiletto boots with razor-thin metal needle heels:1.3), NO CHUNKY HEELS, dark industrial luxury setting, pink neon rim lighting, cinematic 35mm, sharp metallic reflections, photorealistic 8k, Vogue-inspired composition
```

### Negative Prompt Maestro

```text
bangs, fringe, covered forehead, dark hair, brunette, ponytail, bun, childish face, teen, natural makeup, subtle makeup, no makeup look, pink lips, nude lips, rosy cheeks, warm natural skin tone, wax skin, plastic mannequin skin, doll toy, tattoos, messy hair, casual outfit, cotton dress, flat shoes, sneakers, vulgar cheap costume, low quality, blurry, deformed hands, bad anatomy
```

### Formula de Prompt

```text
[ESTILO FOTOGRAFICO], [ADN_MISS_DOLL_V3_5_STEALTH], [OUTFIT ESPECIFICO], [POSE Y EXPRESION], [ESCENARIO], [ILUMINACION], [CALIDAD/OPTICA].
```

Variar solo lo que esta entre corchetes fuera del ADN. La identidad facial, pelo, frente, labios, piel y actitud no se negocian.

---

## II-B. PROMPT BASE — SOLO ROSTRO + CUERPO (ADN puro, sin outfit ni escenario)

Este bloque contiene únicamente los marcadores de identidad física de Miss Doll: cara, cabello, piel, cuerpo y actitud postural. Se usa como ancla antes de añadir [OUTFIT ESPECÍFICO] + [POSE + ESCENARIO + ILUMINACIÓN + CALIDAD].

```text
adult glamorous woman, sharp platinum blonde asymmetric bob, clear exposed forehead, NO BANGS, (small refined upturned doll nose:1.2), (high prominent sculpted cheekbones:1.2), pale porcelain white skin with realistic human texture and subtle visible pores, cold grey icy eyes, fixed professional dissociation gaze, perfectly groomed slim blonde eyebrows arched and precise, heavy glamour makeup: thick black winged eyeliner, bronze and black champagne smokey eye, mega volume false lashes longer at outer corners, strong sculpted cheekbone contour, classic red satin lipstick with crisp editorial cupid's bow, NO pink lips, NO nude lips, sculptural extreme hourglass silhouette, tiny cinched waist, full chest, commanding upright posture, chin elevated 5 degrees, NO TATTOOS, extra long almond stiletto nails deep red
```

**Uso:**
```
[ESTILO FOTOGRAFICO], [ADN_ROSTRO_CUERPO], [OUTFIT ESPECIFICO], [POSE], [ESCENARIO], [ILUMINACION], [CALIDAD]
```

**Negativos siempre activos:**
```
bangs, fringe, dark hair, brunette, pink lips, nude lips, tattoos, flat shoes, sneakers, block heel, chunky heel, childish face, teen, natural makeup, wax skin, plastic mannequin skin
```

---

## III. Reglas Duras de Identidad

### Cabello

- **Color:** platinum blonde solamente.
- **Corte base:** bob corto, sharp, asymmetric, angular o classic blunt.
- **Frente:** siempre despejada.
- **Palabras obligatorias:** `clear exposed forehead, NO BANGS`.
- **No usar:** bangs, fringe, soft wavy bob, ponytail, bun, dark roots marcadas.

### Rostro y Mirada

- **Ojos:** grey eyes o icy blue-grey eyes.
- **Mirada:** `fixed professional dissociation gaze`, `cold commanding gaze`, `Face of the Pole`.
- **Cejas:** delgadas, rubias, arqueadas, muy perfiladas.
- **Expresion:** fria, auditora, calculada; puede tener fake sweetness, pero nunca sonrisa amigable constante.

### Piel

- **Canon base:** `pale porcelain white skin with realistic human texture and subtle visible pores`.
- **Brillo:** humano/editorial, no cera ni maniqui.
- **Variante playa/pool:** solo si se pide explicitamente: `controlled golden tan, sun-kissed glow`.
- **No usar:** `natural skin tone`, `warm skin`, `healthy complexion`, `wax skin`, `plastic mannequin skin`.

### Maquillaje

- **Estandar:** heavy glamour profesional, caro, preciso.
- **Ojos:** bronze/black/champagne smokey eyes, thick black winged eyeliner, mega false lashes.
- **Contour:** fuerte y esculpido.
- **Labios:** rojo como firma visual.
- **Keywords:** `classic red satin lipstick`, `crisp red lip contour`, `clean cupid's bow`.
- **No usar:** pink lips, nude lips, pink eyeshadow, natural makeup, subtle makeup, rosy cheeks.

### Cuerpo y Postura

- **Silueta:** sculptural extreme hourglass, tiny cinched waist, bust/cintura/cadera dramaticos.
- **Postura:** espalda recta, menton elevado, movimientos economicos.
- **Zapatos:** Pleaser Flamingo stilettos / razor-thin metal heels. **PROHIBIDOS LOS TACONES CHUNKY.** Solo tacón aguja extremo. Nunca flats.

### Tatuajes

- **Canon actual:** NO TATTOOS por defecto. El perfil Stealth exige piel limpia.
- **Legacy opcional:** blackwork minimalista solo puede usarse si el prompt o guion lo pide explicitamente como variante de supervivencia/club. Si no se menciona, usar `NO TATTOOS`.

---

## IV. Vestuario — Materiales y Paleta

Miss Doll combina fetiche sintético de alto nivel con hardware funcional. No parece disfraz de Halloween; parece el uniforme privado de alguien que realmente usa esto. Su centro es el club y el calabozo — no la oficina.

### Materiales

- Latex high-gloss
- PVC pulido
- Vinilo estructural
- Neopreno tecnico
- Cordura o nylon tactico
- Chrome hardware
- Black tactical webbing
- Cobra buckles

### Paleta

- **Primaria:** neon pink, dusty pink, hot pink, magenta.
- **Contraste:** black carbon, chrome, white latex, champagne/nude tecnico.
- **Variantes controladas:** coral, mint, turquoise, lavender, rose gold.
- **Regla:** el rosa debe quedar como firma visual aunque el look use negro, blanco o metalicos.

### Piezas Canonicas

- Corset visible o arquitectura de corset integrada.
- Bodysuit/catsuit latex o vinilo.
- Opera gloves o guantes tacticos.
- Choker liso o placa identificatoria minimalista.
- Platform stiletto boots de 8 pulgadas o mas.
- Gafas finas solo en Modo Auditora (disfraz corporativo — ver Sección VI).

---

## V. Protocolo de Comportamiento Visual (Poses y Actitud)

Miss Doll opera en el registro híbrido **Domme + Stripper**. Su lenguaje corporal no es una oferta, sino una **dispensa de sensualidad** controlada.

### 1. Reglas Estructurales
- **Verticalidad:** Torso siempre erguido, hombros firmes y barbilla 5-10º arriba. Nunca desplomada.
- **Basculación Pélvica:** Alterna entre pelvis hacia delante (tease/stripper) y hacia atrás (sentencia/Domme).
- **Pies:** Posición externa abierta (V abierta), nunca paralelos.
- **Mirada:** [Face of the Pole] — Disociación profesional. Se posa 2-4s y se retira deliberadamente. Parpadeo lento.

### 2. Vocabulario de Poses Firma
- **Monarch Throne:** Sentada en silla/trono, piernas abiertas 60-90º, codos en reposabrazos, barbilla alta.
- **Hip-Carry against Pole:** Cadera contra la barra, manos libres (en cabello o accesorio), mirada fija.
- **Cruel Contrapposto:** Peso en una pierna, otra cruzada delante en punta, hombros girados.
- **Foot on Sub:** Pie con tacón sobre el hombro o muslo del sub, verticalidad absoluta.
- **Throne en Suelo:** Sentada en V abierta, codos en rodillas, barbilla alta (máxima autoridad desde el suelo).

### 3. Tempo y Transiciones
- **Lento Absoluto:** Un solo movimiento donde otros hacen tres.
- **Detención Brusca:** Interrupciones que subrayan el control.
- **Transición Vertical:** Pasar siempre por la línea recta entre dos poses.
- **Mirada Primero:** Los ojos llegan al destino antes que el cuerpo.

---

## VI. Prompt Base por Modo

> ⚠️ **ORDEN = JERARQUÍA.** Los primeros modos son su identidad real. El último (Auditora) es un disfraz de roleplay — no su identidad base.

### Modo Latex Icon *(identidad base — club / escenario)*

```text
[ADN_MISS_DOLL_V3_5_STEALTH], seamless neon pink high-gloss latex catsuit, external sculptural corset, chrome waist hardware, matching pink platform stiletto boots, dark industrial gallery, pink neon rim light, mirror-polished floor reflections
```

### Modo Expert Domme: Latex Goddess *(ritual / calabozo)*

```text
[ADN_MISS_DOLL_V3_5_STEALTH], (full-body skin-tight high-gloss black latex catsuit:1.2), integrated gloves, neck-entry, (heavy structural black leather underbust corset with chrome busk:1.1), (towering 8-inch black latex thigh-high stiletto boots:1.2), heavy chrome O-ring collar with functional padlock, clinical dungeon setting, cold rim lighting, sharp reflections on rubber
```

### Modo Expert Domme: Leather Mistress *(disciplina)*

```text
[ADN_MISS_DOLL_V3_5_STEALTH], (heavy black cowhide leather overbust corset with multiple roller buckles:1.2), black leather skinny pants, (knee-high polished leather officer boots with spurs:1.1), black leather opera gloves, holding a leather riding crop, dark concrete interrogation room, single overhead spotlight
```

### Modo Expert Domme: Couture Findom *(findom / humillación cerebral)*

```text
[ADN_MISS_DOLL_V3_5_STEALTH], structured black wool crepe tailored dress, high architectural collar, (long black satin opera gloves:1.1), (classic Christian Louboutin So Kate 120mm black patent stilettos:1.2), holding a sleek black leather dossier, ultra-modern glass office, city lights at night, cold blue-toned luxury lighting
```

### Modo Luxury Escort Editorial *(nightlife de alto nivel)*

```text
[ADN_MISS_DOLL_V3_5_STEALTH], structured rose-gold latex bodysuit under a white cropped faux-fur coat, pink corset architecture visible, chrome choker, black patent platform stilettos, luxury hotel corridor, flash photography, expensive nightlife atmosphere
```

### Modo Auditora *(disfraz corporativo — roleplay únicamente)*

> Este modo es un **camuflaje estratégico**, no su identidad. Miss Doll nunca fue oficinista. Se viste así cuando entra a territorios corporativos como depredadora infiltrada. El corporate setting es el escenario de caza, no su ambiente natural.

```text
[ADN_MISS_DOLL_V3_5_STEALTH], custom-tailored dusty pink technical bodysuit, black tactical webbing, matte black Cobra buckles, black high-waisted structural pencil skirt, black high-gloss opera gloves, clear thin-frame glasses, (razor-thin metal stiletto heels:1.3), NO CHUNKY HEELS, holding a sleek black leather dossier, clinical grey corporate office setting used for intimidation, cold cinematic lighting
```

---

## VII. Referencias Aprobadas

- Rostro/cabello: `05_Imagenes/miss_doll/Reference/README.md`
- Retratos canon 2026: `05_Imagenes/miss_doll/canon_portrait_2026/README.md`
- Registro de looks: `02_Personajes/01_Principales/miss_doll/OUTFITS_MISS_DOLL.md`
- Maquillaje: `00_Ele/canon_maquillaje.md`
- **Sistema de Poses + Vestuario (integración canónica):** `02_Personajes/01_Principales/miss_doll/SISTEMA_POSES_VESTUARIO_MISS_DOLL.md`
- Manuales Técnicos fuente (referencia avanzada):
  - `00_Ele/Estudio_Poses_Domme_Stripper.md`
  - `00_Ele/Estudio_Vestuario_Domme_BDSM_Fetish.md`
  - `00_Ele/Estudio_Vestuario_Pole_Stripper.md`

---

## VIII. Checklist Antes de Generar

- Bob platino sharp/asymmetrical.
- Frente despejada y `NO BANGS`.
- Labios rojos glossy/satin, no nude ni pink.
- Piel porcelana realista con textura humana, no maniqui.
- Mirada fria de disociacion profesional.
- Corset/estructura tactica visible.
- Heels/platform boots, nunca zapatos planos.
- `NO TATTOOS` salvo variante explicitamente solicitada.
