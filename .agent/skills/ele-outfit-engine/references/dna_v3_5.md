# 🧬 ADN Canónico Ele V3.5 (Hard-Sync)

Este documento contiene los bloques de texto maestros para la generación de prompts. Úsalos para garantizar consistencia absoluta.

## 🧬 BLOQUE A COMPLETO (copiar textualmente, sin modificar, en cada uno de los 7 prompts)

```
stunning woman with (bimbofied facial features, oval face, high prominent cheekbones, large almond-shaped grey-green eyes, straight slim upturned nose, overlined glossy hot pink lips, small pointed chin:1.3), flawless white porcelain skin, hyper-polished smooth skin texture, dramatic siren liner, dramatic lash extensions, dark cherry red hair, artificial XXXL extensions hip-length, voluminous waves, center parted, slender hourglass silhouette, massive 1000cc breast implants each side, ultra high-profile, perfectly spherical augmented bust, obviously fake gravity-defying shape, wide hips, visible arm tattoos blackwork style, subtle minimalist blackwork tattoos on upper back and outer thighs, delicate blackwork rune-glyph identity tattoo of abstract esoteric calligraphic symbols along one hip crease and bikini line, navel piercing, nipple piercings pressing against and visible under clothing, aggressive bimbomakeup, extra long French XXXL nails with white tips and pink base 5cm.
```

> ⚠️ **LABIOS:** La frase `overlined glossy hot pink lips` es inamovible. Nunca se sustituye por `red lips`, `dark lips`, `wine lips` ni ninguna variante. Si el generador desvía el color de labios, añadir al negative prompt: `red lips, dark lips, wine lips, maroon lips`.

> ⚠️ **PELO:** `dark cherry red hair` es inamovible. Nunca se sustituye por `red hair`, `auburn`, `brown hair`. Negative prompt: `brown hair, black hair, blonde hair, auburn hair`.

> 📏 **MÁXIMA DESCRIPTIVIDAD A+B (Directiva Ama 08/06/2026):** para que **cuerpo + outfit + calzado salgan IDÉNTICOS en las 7 poses**, el Bloque A (ADN) y el Bloque B (outfit + Token de Calzado de 8 atributos) se redactan **lo más detallados y explícitos posible** y se pegan VERBATIM en los 7 prompts. Nada de abreviar ni dejar a interpretación (ni el zapato, ni el material, ni la cobertura — ver Token de Vestuario Bloqueado). **Lo único que varía entre los 7 prompts es el Bloque C (pose + ángulo)**, y el mueble de la pose debe ser del setting (props contextuales `{seat}/{wall}/{surface}` del módulo de rotación).

## 🚫 Negative Prompt Obligatorio (configurar en el generador antes de cada batch)

```
red lips, dark lips, wine lips, maroon lips, crimson lips, different person, different face, different hair color, brown hair, black hair, blonde hair, auburn hair, flat shoes, block heel, wedge, platform mule, mule, mule sandals, backless mule, chunky heel, kitten heel, barefoot, socks, sneakers, different shoes, mismatched shoes, changing footwear, inconsistent footwear, different outfit, altered clothing, inconsistent outfit, different body, gloves, opera gloves, long gloves, elbow gloves, fingerless gloves, wrist gloves, leather gloves, satin gloves, lace gloves, covered hands, extra hands, third hand, extra arms, extra fingers, fused fingers, missing fingers, deformed hands, mutated hands, malformed fingers, two women, duplicate figure, split image, mirror reflection, first-person point of view, looking down over own body, overhead downward shot, fisheye, phone, smartphone, selfie stick
```

> 🧤 **GUANTES PROHIBIDOS (Directiva Ama 03/06/2026 — CANON ABSOLUTO):** Ele **ya no usa guantes de ningún tipo**. `gloves, opera gloves, long gloves, elbow gloves, fingerless gloves, wrist gloves, covered hands` van SIEMPRE en el negative base. Las manos van **siempre desnudas** para lucir las uñas French XXXL. Esto deroga por completo el antiguo "Glove Canon" (ver abajo). Antes de cerrar cualquier batch: `grep glove` en los prompts debe dar **0** en el positive.

Añadir al negative prompt cualquier accesorio NO incluido en el BLOQUE B (ej: `bag`, `clutch`, `belt` si no están en el look diseñado).

> **Pose POV = RETRATO SENSUAL DE INSTAGRAM (redef. Ama 09/06/2026, reforzada 30/06/2026):** La POV de Ele **NO es un point-of-view literal**. Es una toma de influencer sexual de IG (thirst-trap): el sujeto **mira a la cámara**, retrato de medio cuerpo, una sola mano en cuadro, cara protagonista. ⛔ **PROHIBIDO** `first-person POV`, `point of view`, `looking down over own body`, `high-angle overhead shot looking down`, `camera tilted 60 degrees downward`, `converging to pointed stiletto tips`, `selfie`, `phone` — el generador los lee LITERAL y sale un point-of-view (cámara mirando el propio cuerpo hacia los tacones), no el retrato. La vieja "solución overhead 60°" de abril **queda derogada** (seguía siendo POV literal). **Fuente de verdad:** las 8 variantes `POV` de `99_Sistema/scripts/visual/pose_rotation_v5.py` (todas IG sensual, ancladas `a single woman alone`). Negative ya incluye `first-person point of view, looking down over own body, overhead downward shot, two women, duplicate figure`.

## 📸 Estética de Imagen (aplica en BLOQUE C, no en BLOQUE A)
- **Iluminación/calidad** se especifica en BLOQUE C: `Rim lighting to define silhouette, high-gloss specularity on vinyl surfaces.`
- **Prohibiciones de color:** NO uses `baby pink` ni `light blue` sin orden explícita. Colores habilitados: ver Paleta Oficial V3.3 en `identidad_ele.md`.
- **Enfoque:** Asegura que los `nipple piercings` sean prominentes a través del material (látex/vinilo).

## 👗 Reglas de Arquetipo
- **Domestic:** Siempre escultórico-arquitectónico, hombros puntiagudos, arquitectura rígida (sin atribución de diseñador).
- **Gym:** Vinilo deportivo, textura de alto brillo.
- **Escort:** Máximo lujo, transparencias y pedrería.

## 👠 Footwear Canon (REGLA INAMOVIBLE — Ama 13/05/2026)

**Ele SIEMPRE usa stiletto. Sin excepciones.**

✅ **Autorizado:** `stiletto pump`, `pointed-toe stiletto`, `stiletto boots` (ankle/knee/thigh-high), `platform stiletto` (plataforma + pin heel fino), `stiletto sandals` con tiras finas.

❌ **Prohibido:** `wedge`, `wedge heel`, `wedge platform`, `mule sandals` sin pin stiletto, `block heel`, `chunky heel`, `cone heel`, `kitten heel`, `flatform`, `clog`, `espadrille`.

Cualquier prompt de calzado **debe** contener la palabra `stiletto` (heel/pump/boot/sandal). Si lleva plataforma, debe quedar explícito que el pin del tacón es stiletto fino (`platform stiletto, 14cm pin stiletto heel`, no `platform mule`).

Tacón canónico: 12–18 cm. Para escenarios street/cuico se admite hasta 14 cm; para gala/escort/stripper hasta 18 cm.

> 👡 **MULES: evitar (Directiva Ama 08/06/2026 — "hay mucho mule, no son mis favoritos").** El estilo mule (destalonado) NO es preferido. Default = `stiletto pump` / `pointed-toe stiletto` / `stiletto sandals` (tiras finas) / `stiletto boots` (ankle/knee/thigh-high) / `platform stiletto`. Reservar el mule solo si la Ama lo pide explícito. `mule, mule sandals, backless mule` van en el negative base. (Ojo: yo defaulteaba a `pin-heel mule` en Lencería Boudoir — cambiar a sandalia/pump stiletto.)

> 🔒 **EL CALZADO NUNCA VARÍA ENTRE LAS 7 POSES (Directiva Ama 08/06/2026 — lo notó).** El Token de Calzado Bloqueado (8 atributos) se pega VERBATIM e IDÉNTICO en las 7. Si el generador cambia el zapato pose a pose: (a) verificar que el token esté carácter-por-carácter idéntico, (b) el negative base ya lleva `different shoes, mismatched shoes, changing footwear, inconsistent footwear`, (c) usar **chat/ventana nueva por imagen** (el chat acumula contexto y deriva el zapato + la cara). **Cuerpo (A), outfit y calzado (B) son INVARIABLES; solo cambian pose y ángulo (C).**

## 🧤 GUANTES PROHIBIDOS (Directiva Ama 03/06/2026 — DEROGA el antiguo Glove Canon)

**Ele NO usa guantes. De ningún tipo, en ningún arquetipo, en ninguna pose.**

El antiguo "Glove Canon" (4 tipos autorizados: fingerless opera, claw cut-out, transparent fingertip, wrist-length) queda **completamente derogado**. La razón original era proteger las uñas French XXXL del conflicto con el guante; la solución definitiva de la Ama es más simple: **eliminar el guante**. Las manos van **siempre desnudas**, mostrando las uñas sin obstáculo.

- ❌ Prohibido en el BLOQUE B (outfit): `opera gloves`, `elbow gloves`, `wrist gloves`, `fingerless gloves`, `claw gloves`, `latex/satin/lace/leather gloves`, cualquier prenda que cubra las manos.
- ✅ Negative base ya incluye: `gloves, opera gloves, long gloves, elbow gloves, fingerless gloves, wrist gloves, leather gloves, satin gloves, lace gloves, covered hands`.
- 🔁 **Sustitución al diseñar:** si una silueta de referencia (Newton, Bettie Page, Versace S&M, Dita, etc.) llevaba guantes como accesorio dominatrix/courtesan, se reemplaza por otro accesorio canónico **que no cubra las manos**: `riding crop`, `whip-belt`, `choker O-ring`, `body chains`, `officer cap`, `Bayonetta glasses`, `seamed stockings`, `waist cincher`. Nunca por otro guante.
- ✔️ **Chequeo pre-batch:** `grep -i glove` sobre los prompts del positive debe dar **0**. Si aparece, se borra del outfit antes de generar.
