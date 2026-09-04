# 🧬 ADN Canónico Ele V3.5 (Hard-Sync)

> 🔒 **ESTE ARCHIVO YA NO ES EL DUEÑO DEL BLOQUE A (29/08/2026).**
> El dueño único es **`02_Personajes/_perfiles_visuales/ele.md`** §2 — el fence marcado con `<!-- ADN:BLOQUE_A -->`,
> que es el que **lee el motor** (`PromptBuilder.bloque_a`). Este archivo vive en una
> skill legacy por personaje, de las que el `outfit-engine` genérico vino a reemplazar.
>
> El texto de abajo se dejó como estaba y se verificó idéntico al del perfil el 29/08/2026.
> **Si hay que cambiar el ADN, se cambia en el perfil, no acá.** Verificar con:
> `python 99_Sistema/scripts/visual/prompt_builder.py --adn`

---

Este documento contiene los bloques de texto maestros para la generación de prompts. Úsalos para garantizar consistencia absoluta.

## 🧬 BLOQUE A COMPLETO (copiar textualmente, sin modificar, en cada uno de los 7 prompts)

```
stunning woman with (bimbofied facial features, oval face, high prominent cheekbones, large almond-shaped grey-green eyes, straight slim upturned nose, overlined glossy hot pink lips, small pointed chin:1.3), flawless white porcelain skin, hyper-polished smooth skin texture, dramatic siren liner, dramatic lash extensions, intense shimmer smokey eyeshadow in cool jade-green and smoky pewter blended out at the outer corner, (defined groomed brows in muted dark cherry-brown, arched with a clean tapered edge, clearly visible against the porcelain skin:1.3), cool pearl highlight on the cheekbones and cupid's bow, soft cool rose-mauve blush placed high on the cheekbone, dark cherry red hair, artificial XXXL extensions hip-length, voluminous waves, center parted, slender hourglass silhouette, massive 1000cc breast implants each side, ultra high-profile, perfectly spherical augmented bust, obviously fake gravity-defying shape, wide hips, blackwork arm tattoos shown only on bare uncovered skin, subtle minimalist blackwork tattoos on upper back and outer thighs, delicate blackwork rune-glyph identity tattoo of abstract esoteric calligraphic symbols along one hip crease and bikini line, navel piercing, nipple piercings, every tattoo and piercing visible ONLY on genuinely bare skin and never through or over any garment, aggressive bimbomakeup, extra long French XXXL nails with white tips and pink base 5cm.
```

> 🩹 **MARCAS SOLO EN PIEL DESNUDA (Directiva Ama 13/07/2026 — DEROGA la regla vieja de "piercings prominentes a través del material"):** Los piercings (pezón, ombligo) y los tatuajes (brazo, runas de la cadera) son **ADN permanente del cuerpo**, pero se ven **únicamente donde la piel está genuinamente descubierta**. Bajo la tela **no existen**: nada de piercings marcándose a través del látex, ni pezones asomando bajo la prenda, ni tatuajes pintados encima de una manga.
> - **Qué cambió en el Bloque A:** `nipple piercings pressing against and visible under clothing` → `nipple piercings` + cláusula explícita de solo-piel-desnuda. `visible arm tattoos` → `blackwork arm tattoos shown only on bare uncovered skin`.
> - **Por qué:** el token viejo era una **orden directa** al generador de mostrarlos a través de la ropa — y ningún candado (`OPAQUE_LOCK`) le gana a una orden directa. Confirmado en el batch L761-L770: piercings dibujados sobre la columna de pitón (L762) y tatuajes del brazo pintados **sobre** la manga larga de vinilo (L763/L764).
> - **Refuerzo obligatorio:** el prompt lleva `SKIN_LOCK` y el negative `NEG_MARKS_THROUGH` (ambos en `99_Sistema/scripts/visual/pose_rotation_v5.py`). En lencería/bikini el ombligo y las runas **sí se lucen** — porque ahí la piel está descubierta de verdad, no por un hueco abierto en la prenda.
> - **Blindaje 13/07/2026 (auditoría de imágenes reales):** el batch L761-L770 se generó ANTES de este fix y confirmó el defecto con zoom en 3 looks (piercings marcados sobre látex/vinilo opaco). `garment_canon.py` ahora falla DURO si la frase-orden vieja reaparece en cualquier texto (`find_forbidden()`), si falta el bloque `Negative Prompt` (`audit_negative()`), o si un estampado animal (python/leopard/tiger/zebra) no lleva `animal_print_lock()` — los tres agujeros reales que dejaron pasar el batch fallido. Ver `feedback_marcas_solo_en_piel`.

> ⚠️ **LABIOS:** La frase `overlined glossy hot pink lips` es inamovible. Nunca se sustituye por `red lips`, `dark lips`, `wine lips` ni ninguna variante. Si el generador desvía el color de labios, añadir al negative prompt: `red lips, dark lips, wine lips, maroon lips`.

> ⚠️ **PELO:** `dark cherry red hair` es inamovible. Nunca se sustituye por `red hair`, `auburn`, `brown hair`. Negative prompt: `brown hair, black hair, blonde hair, auburn hair`.

> 📏 **MÁXIMA DESCRIPTIVIDAD A+B (Directiva Ama 08/06/2026):** para que **cuerpo + outfit + calzado salgan IDÉNTICOS en las 7 poses**, el Bloque A (ADN) y el Bloque B (outfit + Token de Calzado de 8 atributos) se redactan **lo más detallados y explícitos posible** y se pegan VERBATIM en los 7 prompts. Nada de abreviar ni dejar a interpretación (ni el zapato, ni el material, ni la cobertura — ver Token de Vestuario Bloqueado). **Lo único que varía entre los 7 prompts es el Bloque C (pose + ángulo)**, y el mueble de la pose debe ser del setting (props contextuales `{seat}/{wall}/{surface}` del módulo de rotación).

## 🚫 Negative Prompt Obligatorio (va DENTRO del registro de cada look, no "en el generador")

> 🔴 **FUENTE ÚNICA (Ama 13/07/2026):** el negative **ya no se escribe a mano**. Se construye con `build_negative(...)` de `99_Sistema/scripts/visual/pose_rotation_v5.py` y se registra **como bloque `**Negative Prompt:**` en cada look de `galeria_outfits.md`**.
> **Por qué:** desde el **L711 los looks entraron a la galería SIN bloque negativo** (191 bloques para 400 looks — el último es el L710). 60 looks / **420 poses generadas con el negative vacío**: por eso volvieron la costura al frente, los cortes y las marcas a través de la tela, aunque las anclas del positive estuvieran puestas. El inyector pegaba el positive desde el módulo (al día) pero el negative lo tipeaba cada uno a mano… hasta que alguno dejó de hacerlo y nada lo detectó. Ahora el linter `garment_canon.py` **falla** si un look nuevo entra sin negative.

```python
from pose_rotation_v5 import build_negative
neg = build_negative(seam=True, covered=True, stockings=True, gloss_risk=False, lingerie=False)
```

| Flag | Cuándo | Qué añade |
|------|--------|-----------|
| `seam` | medias con costura | veta la raya al frente / línea en la canilla |
| `stockings` | medias de cualquier tipo | veta la deriva de color/estampado entre poses |
| `covered` | prenda que cubre busto/torso | veta keyhole/cutout/underboob para exponer marcas |
| `gloss_risk` | silueta que primea tela mate (sastrería, rib, satén) | veta el mate |
| `lingerie` | **solo** Lencería | **NO** veta el mule (único arquetipo donde el canon lo permite, platform ≥4") |
| `extra` | accesorios ajenos al Bloque B (bag, clutch, belt…) | los veta |

`NEG_MARKS_THROUGH` (piercings/tatuajes a través de la tela) va **siempre**, es el par negativo del `SKIN_LOCK`.

> 🧤 **GUANTES PROHIBIDOS (Directiva Ama 03/06/2026 — CANON ABSOLUTO):** Ele **ya no usa guantes de ningún tipo**. `gloves, opera gloves, long gloves, elbow gloves, fingerless gloves, wrist gloves, covered hands` van SIEMPRE en el negative base. Las manos van **siempre desnudas** para lucir las uñas French XXXL. Esto deroga por completo el antiguo "Glove Canon" (ver abajo). Antes de cerrar cualquier batch: `grep glove` en los prompts debe dar **0** en el positive.

Añadir al negative prompt cualquier accesorio NO incluido en el BLOQUE B (ej: `bag`, `clutch`, `belt` si no están en el look diseñado).

> **Pose POV = RETRATO SENSUAL DE INSTAGRAM (redef. Ama 09/06/2026, reforzada 30/06/2026):** La POV de Ele **NO es un point-of-view literal**. Es una toma de influencer sexual de IG (thirst-trap): el sujeto **mira a la cámara**, retrato de medio cuerpo, una sola mano en cuadro, cara protagonista. ⛔ **PROHIBIDO** `first-person POV`, `point of view`, `looking down over own body`, `high-angle overhead shot looking down`, `camera tilted 60 degrees downward`, `converging to pointed stiletto tips`, `selfie`, `phone` — el generador los lee LITERAL y sale un point-of-view (cámara mirando el propio cuerpo hacia los tacones), no el retrato. La vieja "solución overhead 60°" de abril **queda derogada** (seguía siendo POV literal). **Fuente de verdad:** las 8 variantes `POV` de `99_Sistema/scripts/visual/pose_rotation_v5.py` (todas IG sensual, ancladas `a single woman alone`). Negative ya incluye `first-person point of view, looking down over own body, overhead downward shot, two women, duplicate figure`.

## 📸 Estética de Imagen (aplica en BLOQUE C, no en BLOQUE A)
- **Iluminación/calidad** se especifica en BLOQUE C: `Rim lighting to define silhouette, high-gloss specularity on vinyl surfaces.`
- **Prohibiciones de color:** NO uses `baby pink` ni `light blue` sin orden explícita. Colores habilitados: ver Paleta Oficial V3.3 en `identidad_ele.md`.
- **Enfoque:** ~~Asegura que los `nipple piercings` sean prominentes a través del material (látex/vinilo).~~ ⛔ **DEROGADO (Ama 13/07/2026).** Era la orden que producía el defecto: piercings y tatuajes atravesando la ropa. Las marcas se ven **solo en piel desnuda** (ver `SKIN_LOCK` arriba). Donde la prenda cubre, la tela va **opaca y sin marcas**.

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
