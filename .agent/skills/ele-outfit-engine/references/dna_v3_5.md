# 🧬 ADN Canónico Ele V3.5 (Hard-Sync)

Este documento contiene los bloques de texto maestros para la generación de prompts. Úsalos para garantizar consistencia absoluta.

## 🧬 BLOQUE A COMPLETO (copiar textualmente, sin modificar, en cada uno de los 7 prompts)

```
stunning woman with (bimbofied facial features, oval face, high prominent cheekbones, large almond-shaped grey-green eyes, straight slim upturned nose, overlined glossy hot pink lips, small pointed chin:1.3), flawless white porcelain skin, hyper-polished smooth skin texture, dramatic siren liner, dramatic lash extensions, dark cherry red hair, artificial XXXL extensions hip-length, voluminous waves, center parted, slender hourglass silhouette, full bust, wide hips, visible arm tattoos blackwork style, subtle minimalist blackwork tattoos on upper back and outer thighs, navel piercing, nipple piercings pressing against and visible under clothing, aggressive bimbomakeup, extra long French XXXL nails with white tips and pink base 5cm.
```

> ⚠️ **LABIOS:** La frase `overlined glossy hot pink lips` es inamovible. Nunca se sustituye por `red lips`, `dark lips`, `wine lips` ni ninguna variante. Si el generador desvía el color de labios, añadir al negative prompt: `red lips, dark lips, wine lips, maroon lips`.

> ⚠️ **PELO:** `dark cherry red hair` es inamovible. Nunca se sustituye por `red hair`, `auburn`, `brown hair`. Negative prompt: `brown hair, black hair, blonde hair, auburn hair`.

## 🚫 Negative Prompt Obligatorio (configurar en el generador antes de cada batch)

```
red lips, dark lips, wine lips, maroon lips, crimson lips, different person, different face, different hair color, brown hair, black hair, blonde hair, auburn hair, flat shoes, block heel, wedge, platform mule, chunky heel, kitten heel, barefoot, socks, sneakers
```

Añadir al negative prompt cualquier accesorio NO incluido en el BLOQUE B (ej: `bag`, `clutch`, `belt` si no están en el look diseñado).

> **Pose POV — NUNCA usar "first-person POV":** Esta frase activa un patrón de espejo/duplicado en el modelo (ver L176: dos mujeres generadas). Sustituir siempre por: `high-angle overhead shot looking down at standing figure, camera tilted 60 degrees downward, XXXL French nails resting on waist in sharp foreground, décolleté and outfit filling midground, pointed stiletto heels visible at bottom edge of frame, one single woman`

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

## 🧤 Glove Canon (REGLA INAMOVIBLE — Ama 14/05/2026)

**Cuando un Look incluye guantes, los guantes DEBEN dejar las uñas French XXXL completamente visibles. No hay guantes cerrados en el catálogo de Ele.**

El BLOQUE A obliga `extra long French XXXL nails with white tips and pink base 5cm`. Si el BLOQUE B introduce un guante cerrado, el modelo entra en conflicto irresoluble. Resolución canónica: las uñas son prioritarias; el guante se adapta a ellas.

### Cuatro tipos autorizados

✅ **Fingerless opera** — `fingerless opera-length [material] gloves ending at second knuckle, French XXXL nails fully visible on extended fingers`

✅ **Claw cut-out** — `[material] gloves with cut-out fingertips exposing French XXXL nails, sharp pointed nails extending beyond glove edge`

✅ **Transparent fingertip** — `[material] opera gloves with sheer transparent fingertip panels, French XXXL nails fully visible through the transparent fabric`

✅ **Wrist-length / short** — `wrist-length [material] gloves stopping at wrist bone, hands completely bare, French XXXL nails fully visible`

❌ **Prohibido:** `full-finger gloves`, `closed gloves`, `mittens`, `gloves with fingertips` (sin especificar transparencia), `painted nails through gloves`, `nails visible inside gloves`.

### Mapeo arquetipo → tipo default (Mix según arquetipo)

| Arquetipo | Default |
| :--- | :--- |
| Escort / Gala / High-Fashion | Transparent fingertip |
| Stripper / Domme | Claw cut-out |
| Gym / Athleisure | Fingerless o wrist-length |
| Domestic (cocina escultórica) | Transparent fingertip o fingerless |
| Corporate / Power Secretary | Wrist-length o transparent fingertip |
| Pin-Up / Retro | Fingerless o wrist-length |

### Negative prompt obligatorio cuando hay guantes (acumular sobre el base)

```
gloves covering nails, hidden nails, hidden hands, closed gloves, fingertips covered by glove fabric, mittens, glove cutting fingers, broken sleeve glove, nails painted on glove surface, gloves that hide French XXXL nails
```

### Redundancia obligatoria

Cuando hay guantes, el BLOQUE B DEBE repetir `French XXXL nails fully visible` dentro de la descripción del guante. La redundancia con el BLOQUE A confirma prioridad de las uñas.
