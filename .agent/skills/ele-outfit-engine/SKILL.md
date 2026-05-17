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

### 1. Análisis de Mix de Arquetipos
Antes de proponer un Look, consulta la tabla de estadísticas en [galeria_outfits.md](file:///c:/Users/farid/LaVouteDAnais/00_Ele/galeria_outfits.md).

**Categorías principales (tipo de prenda):**
- **Mix** (Corporate / Domestic / High-Fashion / Escort / Stripper / Pin-Up): Meta 75%
- **Bikini:** Meta 10%
- **Lencería:** Meta 10%
- **Gym/Athleisure:** Meta 5%

**Sub-arquetipos dentro de Mix** (Meta: 16.6% cada uno — ver `ele_master_audit_v3_5.md`):
1. High-Fashion & Nightclub
2. Corporate
3. Domestic
4. Professional Stripper
5. Escort de Lujo
6. Pin-Up & Athleisure

Si una categoría o sub-arquetipo está bajo, el nuevo Look **debe** pertenecer a esa categoría.

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
stunning woman with (bimbofied facial features, oval face, high prominent cheekbones, large almond-shaped grey-green eyes, straight slim upturned nose, overlined glossy hot pink lips, small pointed chin:1.3), flawless white porcelain skin, hyper-polished smooth skin texture, dramatic siren liner, dramatic lash extensions, dark cherry red hair, artificial XXXL extensions hip-length, voluminous waves, center parted, slender hourglass silhouette, full bust, wide hips, visible arm tattoos blackwork style, subtle minimalist blackwork tattoos on upper back and outer thighs, navel piercing, nipple piercings pressing against and visible under clothing, aggressive bimbomakeup, extra long French XXXL nails with white tips and pink base 5cm.
```

El BLOQUE A **nunca se modifica**. Se copia textualmente de `dna_v3_5.md`. Nunca se escribe de memoria.

**Negative prompt obligatorio (añadir en la configuración del generador):**
```
red lips, dark lips, wine lips, maroon lips, crimson lips, different person, different face, different hair color, brown hair, black hair, blonde hair, flat shoes, block heel, wedge, platform mule, chunky heel, kitten heel, barefoot, socks, sneakers, two women, mirror reflection, split image, duplicate figure, side by side, bag (if not in BLOQUE B), clutch (if not in BLOQUE B)
```

> **Por qué:** L177 generó labios rojos en 3 poses y persona diferente en Odalisque. L176 generó DOS mujeres (efecto espejo) por la frase "first-person POV". L178 confundió POV con Odalisque recostada. Los negative prompts son la barrera activa contra la deriva del ADN.

**Estructura de cada prompt:** `[BLOQUE A] + [BLOQUE B] + [BLOQUE C — Pose y Setting]`

**7 poses estándar obligatorias (BLOQUE C):**
1. **Standing View:** `full body, standing, weight on one hip, hands on waist, [fondo]`
2. **Back View:** `full body, back view, turning over shoulder, hair cascading, [fondo]`
3. **Seated View:** `seated, legs crossed, spine straight, hands on knee, [fondo]`
4. **Side Profile:** `full body, side profile, extreme lumbar arch, chin lifted, [fondo]`
5. **Ditzy Expression:** `close-up beauty shot, slightly parted lips, vacant ditzy expression, lashes down then up, [fondo]`
6. **POV — Goddess Gaze:** `high-angle overhead shot looking down at standing figure, camera tilted 60 degrees downward, XXXL French nails resting on waist in sharp close foreground, décolleté and outfit filling midground, pointed stiletto heels visible at bottom edge of frame, slight perspective compression, one single woman, [fondo]` *(NUNCA usar "first-person POV" — genera duplicados y espejos)*
7. **Lying Down — The Odalisque:** `full body lying on side forming a languid S-curve, one arm extended with XXXL nails on surface, legs slightly bent, stilettos pointed and visible, [fondo]`

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
