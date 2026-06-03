# 🧬 ADN Canónico Ele V3.5 (Hard-Sync)

Este documento contiene los bloques de texto maestros para la generación de prompts. Úsalos para garantizar consistencia absoluta.

## 🧬 BLOQUE A COMPLETO (copiar textualmente, sin modificar, en cada uno de los 7 prompts)

```
stunning woman with (bimbofied facial features, oval face, high prominent cheekbones, large almond-shaped grey-green eyes, straight slim upturned nose, overlined glossy hot pink lips, small pointed chin:1.3), flawless white porcelain skin, hyper-polished smooth skin texture, dramatic siren liner, dramatic lash extensions, dark cherry red hair, artificial XXXL extensions hip-length, voluminous waves, center parted, slender hourglass silhouette, massive 1000cc breast implants each side, ultra high-profile, perfectly spherical augmented bust, obviously fake gravity-defying shape, wide hips, visible arm tattoos blackwork style, subtle minimalist blackwork tattoos on upper back and outer thighs, navel piercing, nipple piercings pressing against and visible under clothing, aggressive bimbomakeup, extra long French XXXL nails with white tips and pink base 5cm.
```

> ⚠️ **LABIOS:** La frase `overlined glossy hot pink lips` es inamovible. Nunca se sustituye por `red lips`, `dark lips`, `wine lips` ni ninguna variante. Si el generador desvía el color de labios, añadir al negative prompt: `red lips, dark lips, wine lips, maroon lips`.

> ⚠️ **PELO:** `dark cherry red hair` es inamovible. Nunca se sustituye por `red hair`, `auburn`, `brown hair`. Negative prompt: `brown hair, black hair, blonde hair, auburn hair`.

## 🚫 Negative Prompt Obligatorio (configurar en el generador antes de cada batch)

```
red lips, dark lips, wine lips, maroon lips, crimson lips, different person, different face, different hair color, brown hair, black hair, blonde hair, auburn hair, flat shoes, block heel, wedge, platform mule, chunky heel, kitten heel, barefoot, socks, sneakers, gloves, opera gloves, long gloves, elbow gloves, fingerless gloves, wrist gloves, leather gloves, satin gloves, lace gloves, covered hands
```

> 🧤 **GUANTES PROHIBIDOS (Directiva Ama 03/06/2026 — CANON ABSOLUTO):** Ele **ya no usa guantes de ningún tipo**. `gloves, opera gloves, long gloves, elbow gloves, fingerless gloves, wrist gloves, covered hands` van SIEMPRE en el negative base. Las manos van **siempre desnudas** para lucir las uñas French XXXL. Esto deroga por completo el antiguo "Glove Canon" (ver abajo). Antes de cerrar cualquier batch: `grep glove` en los prompts debe dar **0** en el positive.

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

## 🧤 GUANTES PROHIBIDOS (Directiva Ama 03/06/2026 — DEROGA el antiguo Glove Canon)

**Ele NO usa guantes. De ningún tipo, en ningún arquetipo, en ninguna pose.**

El antiguo "Glove Canon" (4 tipos autorizados: fingerless opera, claw cut-out, transparent fingertip, wrist-length) queda **completamente derogado**. La razón original era proteger las uñas French XXXL del conflicto con el guante; la solución definitiva de la Ama es más simple: **eliminar el guante**. Las manos van **siempre desnudas**, mostrando las uñas sin obstáculo.

- ❌ Prohibido en el BLOQUE B (outfit): `opera gloves`, `elbow gloves`, `wrist gloves`, `fingerless gloves`, `claw gloves`, `latex/satin/lace/leather gloves`, cualquier prenda que cubra las manos.
- ✅ Negative base ya incluye: `gloves, opera gloves, long gloves, elbow gloves, fingerless gloves, wrist gloves, leather gloves, satin gloves, lace gloves, covered hands`.
- 🔁 **Sustitución al diseñar:** si una silueta de referencia (Newton, Bettie Page, Versace S&M, Dita, etc.) llevaba guantes como accesorio dominatrix/courtesan, se reemplaza por otro accesorio canónico **que no cubra las manos**: `riding crop`, `whip-belt`, `choker O-ring`, `body chains`, `officer cap`, `Bayonetta glasses`, `seamed stockings`, `waist cincher`. Nunca por otro guante.
- ✔️ **Chequeo pre-batch:** `grep -i glove` sobre los prompts del positive debe dar **0**. Si aparece, se borra del outfit antes de generar.
