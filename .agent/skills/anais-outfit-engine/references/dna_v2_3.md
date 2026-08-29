# ADN Anaïs Belland — V2.3 Ageless Hard-Sync

> 🔒 **ESTE ARCHIVO YA NO ES EL DUEÑO DEL BLOQUE A (29/08/2026).**
> El dueño único es **`02_Personajes/_perfiles_visuales/anais.md`** §2 — el fence marcado con `<!-- ADN:BLOQUE_A -->`,
> que es el que **lee el motor** (`PromptBuilder.bloque_a`). Este archivo vive en una
> skill legacy por personaje, de las que el `outfit-engine` genérico vino a reemplazar.
>
> El texto de abajo se dejó como estaba y se verificó idéntico al del perfil el 29/08/2026.
> **Si hay que cambiar el ADN, se cambia en el perfil, no acá.** Verificar con:
> `python 99_Sistema/scripts/visual/prompt_builder.py --adn`

---

**Autoridad:** CANON_VISUAL_ANAIS.md v2.3 (28/04/2026)
**Fuente:** `02_Personajes/01_Principales/CANON_VISUAL_ANAIS.md` Sección II y X

Este archivo es la fuente de verdad para copiar el BLOQUE A y el NEGATIVE PROMPT en los prompts de generación. Nunca escribir el BLOQUE A de memoria — siempre copiar desde aquí o desde el Canon.

---

## BLOQUE A — ADN Inamovible

> ✏️ **Revisado 11/08/2026 (Ama, sesión de canon de rostro).** El texto original decía "ageless... perpetually youthful" y salía leyendo 20-30 años. Se corrigió con edad ancla en la estructura ósea (peso 1.4) + piel impecable declarada en positivo (no en negativo — ver nota de negative prompt más abajo) + sombra de ojos agregada (faltaba por completo). Reemplaza la versión anterior; no queda como variante, la sustituye.

Copiar textualmente en CADA prompt, sin modificar ni una sola palabra:

```text
(unmistakably 42-year-old aristocratic woman, mature sharp bone structure and commanding severity of expression, never a soft youthful face:1.4), (flawless completely smooth unlined forehead, taut porcelain skin with zero visible creases or fine lines anywhere, the seamless perfection of decades of obsessive cosmetic maintenance:1.4), radiant dewy porcelain skin, luminous flawless medical-grade cosmetic finish, (aristocratic refined oval face, sculpted lifted hollowed mature cheekbones, sharp angular defined jawline:1.3), composed poised expression of a woman who has commanded rooms for decades, quiet mature gravitas in her gaze, small classic Old Hollywood beauty mark mole above upper left lip, ultra precise Old Hollywood editorial makeup, precisely drawn dark brown thin arched brows 1940s style, deep taupe and charcoal eyeshadow softly sculpted into the crease giving heavy-lidded smoky depth, sharp precise black cat-eye liquid liner with dramatically elongated wing at outer corner, full voluminous glamorous lashes dense and defined, (naturally full lips with soft volume and a well-defined cupid's bow, vivid deep crimson classic Hollywood red, flawlessly defined with a subtle gloss on the inner edge, slightly parted in a knowing look:1.2), honey blonde hair in sculpted voluminous vintage Hollywood pin-waves or victory rolls side parted, extremely long hip-length hair cascading past the shoulders, slender mature elegant hourglass figure with extreme waist training tightlacing corset, S-curve posture, not voluptuous, not augmented, not bimbo-exaggerated, (natural moderate breasts, firm and perky with a well-defined natural shape:1.2), firm smooth glutes softly toned rather than sharply muscular, heavy-lidded bedroom eyes gaze, long stiletto-shaped manicured fingernails with glossy deep red polish, wearing 12cm black patent leather stiletto heels no platform iconic red sole, cinematic chiaroscuro dramatic lighting, soft key light flattering her impeccably maintained features, George Hurrell style portraiture, intimate tension.
```

> 👣 **Si el calzado es peep-toe o hay pies descalzos, agregar además:** `matching glossy deep red pedicure on visible toenails` — no viene en el bloque de arriba porque no siempre aplica (con pump/bota de puntera cerrada no se ven los pies).

> ⚠️ **Bloqueo de color:** el prefijo "film noir" (ver tabla de prefijos abajo) arrastra sesgo fuerte a blanco y negro aunque no se pida. Si el look debe ir a color (la inmensa mayoría — B&N tiene tope de 5% de la galería, canon §IX), anteponer al prefijo cinematográfico: `in rich vivid full color, not black and white, not monochrome, not grayscale, warm golden-amber color palette with honey blonde hair and deep crimson red lips clearly visible in color,`

---

## NEGATIVE PROMPT BASE

Añadir en todos los looks sin excepción. Para looks de Látex/Fetichismo: quitar `latex` de la lista si es un look de látex canónico.

```text
(different face:1.3), smiling broadly, laughing, playful expression, casual pose, relaxed posture, red hair, dark hair, short hair, messy hair, modern makeup, bimbo makeup, hot pink lips, overlined lips (modern style), neon colors, bright colors, colorful outfit, white dress, pink outfit, glitter, modern clothing, block heel, chunky heel, flat shoes, barefoot, sneakers, cyberpunk, sci-fi, industrial, factory, neon lights, outdoor, natural setting, low quality, blurry, distorted face, child, teenager, man, male, platform heels, modern lingerie, sexy, hot, horny, naked, nude, seductive, provocative, tempting, naughty, open mouth, tongue, explicit nude, (distorted animal print, neon leopard:1.2), cheap fabric texture
```

---

## Constantes Absolutas

| Elemento | Valor Exacto en Prompt |
|----------|----------------------|
| Cabello | `honey blonde hair` — rubio miel cálido, SIEMPRE, SIN EXCEPCIONES |
| Lunar | `small classic Old Hollywood beauty mark mole above upper left lip` — SIEMPRE presente |
| Tacones | `12cm black patent leather stiletto heels no platform iconic red sole` — SIEMPRE |
| Sin tatuajes | Nunca agregar tattoos ni piercings visibles |
| Piel | `radiant dewy porcelain skin`, `flawless completely smooth unlined forehead, taut porcelain skin with zero visible creases`, `soft luminous glow catching the light, no harsh muscle striation, satiny sheen over toned curves` (glow agregado 11/08, validado en pose de espalda) (⚠️ ya NO usar `airbrushed skin tension` — ese token borraba la edad, ver nota 11/08 arriba) |
| Cuerpo | `slender and lean, naturally fit firm physique, not voluptuous, not augmented, not bimbo-exaggerated, natural moderate breasts, firm and perky with a well-defined natural shape, firm smooth glutes softly toned rather than sharply muscular` — válido con o sin corsé; el corsé agrega la curva de cintura dramática, no cambia el resto. **Calibrado 24/08/2026 (Ama):** se agregó "firm and perky with a well-defined natural shape" — el tamaño natural/moderado y el "not augmented" no se tocan |
| Uñas (manos) | `long stiletto-shaped manicured fingernails, glossy deep red polish` — **faltaba en el BLOQUE A original, agregado 11/08/2026** (canon §IV pide rojo pasión/burgundy/negro; se fija rojo profundo glossy como default, variar por look si se pide) |
| Uñas (pies) | `matching glossy deep red pedicure on visible toenails` — **SIEMPRE que el calzado sea peep-toe o los pies estén descalzos.** Se detectó el hueco al usar peep-toe por primera vez esta sesión — con pump/bota de puntera cerrada no aplica porque no se ven. |
| Edad | `(unmistakably 42-year-old aristocratic woman, mature sharp bone structure and commanding severity of expression, never a soft youthful face:1.4)` — SIEMPRE con peso ≥1.3, si no se pierde |
| Sombra de ojos | `deep taupe and charcoal eyeshadow softly sculpted into the crease giving heavy-lidded smoky depth` — faltaba en el BLOQUE A original, agregado 11/08 |
| Labios | `naturally full lips with soft volume and a well-defined cupid's bow, vivid deep crimson classic Hollywood red` — **calibrado 24/08/2026 (Ama): tendían a salir lineales, sin volumen; se agregó forma sin acercarla al registro overlined de Ele/Miss Doll** |
| Cejas | `precisely drawn dark brown thin arched brows 1940s style` |
| Ojos | `sharp precise black cat-eye liquid liner with dramatically elongated wing at outer corner` |
| Silueta | `slender mature elegant hourglass figure with extreme waist training tightlacing corset, S-curve posture` |
| Iluminación | `cinematic chiaroscuro dramatic lighting, George Hurrell style portraiture` |

---

> 🔴 **Verificada 17/08/2026 — esta tabla se ignoró al escribir el batch L15-L20 de la galería** (se copió el bloque de Look 14 completo, prefijo incluido, para los 6 looks nuevos sin volver aquí). Consecuencia real: Boudoir/Lencería perdió `warm amber candlelight chiaroscuro` y salió con el prefijo de Ejecutivo. Diagnóstico y corrección: `02_Personajes/_perfiles_visuales/anais.md` §5.7. **Antes de escribir el BLOQUE C de un look nuevo, volver aquí — no copiar del look anterior.**
>
> 🔒 **Blindaje 17/08/2026:** esta tabla ya no depende de que alguien la relea. Vive TAMBIÉN en `99_Sistema/scripts/visual/anclas_universales.json` → `personajes.anais.prefijos_arquetipo` (`PromptBuilder.prefijo_arquetipo(arquetipo)` la resuelve en código), y `lint_prompts_personaje.py` (chequeo 11) audita cada look real de la galería contra su propio campo `**Arquetipo:**` — un prefijo que no corresponde ahora es CRÍTICO, no un aviso que se puede ignorar. Si esta tabla cambia, el JSON se actualiza en el mismo commit — son un solo dato con dos copias sincronizadas a mano, no dos dueños.

## Prefijos Cinematográficos por Arquetipo

| Arquetipo | Prefijo |
|-----------|---------|
| **Noche / La Voûte** | `8k ultra cinematic film noir portrait, single dramatic spotlight from above,` |
| **Gala / Premiere** | `8k ultra cinematic glamour portrait, Vogue Paris 1950s editorial,` |
| **Boudoir / Lencería** | `8k ultra cinematic intimate boudoir portrait, warm amber candlelight chiaroscuro,` |
| **Sesión Literaria** | `8k ultra cinematic intimate portrait, warm amber dramatic lighting,` |
| **Látex / Fetichismo** | `8k ultra cinematic dark power portrait, high-gloss cinematic lighting,` |
| **Animal Print / Autoridad** | `8k ultra cinematic predatory editorial portrait, dramatic noir lighting,` |
| **Ejecutivo de Poder** | `8k ultra cinematic power portrait, cool key light from above,` |
| **Viaje / Jet Set** | `8k ultra cinematic luxury lifestyle portrait, warm golden afternoon light,` |
