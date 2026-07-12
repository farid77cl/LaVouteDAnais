---
paths: 05_Imagenes/ele/**/*, 00_Ele/galeria_outfits.md
---

# 🫦 ESTÉTICA CANÓNICA DE ELE

## 👠 TACONES ELE (OBLIGATORIO)

Ele SIEMPRE usa tacones **PLEASER** de 8-11 pulgadas con tacón fino y mortal en TODAS las imágenes y descripciones. Nunca descalza. Modelos preferidos:
- FLAMINGO-808 (8", clear PVC)
- ADORE-1020 (7-8", lace-up platform)
- EXTREME-11 (11", clear platform stiletto)

### 🧦 REGLAS DE MEDIAS + CALZADO (Directiva Ama 20/06/2026 — INQUEBRANTABLES)

Cuando un look lleva **medias de cualquier tipo** (nylon, red/fishnet, costura, opacas), el calzado obedece:

1. **🚫 MEDIAS + PUNTA ABIERTA = PROHIBIDO.** Nada de `peep toe` ni `open toe` con medias — la costura/refuerzo de la punta asomando se ve barato. El zapato va siempre de **punta cerrada** (`closed pointed toe`). Aplica a stiletto, plataforma y botas.
2. **🚫 MEDIAS NEGRAS + MINI FALDA BLANCA = NO ABSOLUTO.** La media negra parte la pierna en seco bajo la falda blanca. Si la falda es blanca/crema → la media va de otro color (o nude/transparente), o se quita la media.
3. **👠 MEDIAS + (donde iría Pleaser) = PLATFORM PUMP de punta cerrada.** El clear Pleaser open-toe que la Ama adora (default pole/bikini) **solo se usa en looks SIN medias**. En cuanto hay medias, ese Pleaser se reemplaza por un **platform pump cerrado** (mismo platform stiletto ≥6", `closed pointed toe`).
4. **🎨 PLATAFORMA = MISMO COLOR DEL ZAPATO (Ama 20/06/2026).** La plataforma NUNCA es de un color distinto al cuerpo del zapato (tiendo a hacer la plataforma de un color y el zapato de otro = ERROR). El token de calzado debe nombrar **explícitamente el color de la plataforma igual al del zapato** (ej. `cherry-red patent platform stiletto pumps … with a matching 2-inch cherry-red platform`). Excepción única: el **clear/transparent acrylic** (plataforma + zapato ambos transparentes = ya son "el mismo color").

> **Chequeo de batch (obligatorio antes de cerrar):** si un prompt contiene `fishnet`/`nylon stocking`/`stockings`, NO puede contener `open toe`/`peep toe`. grep cruzado = 0 conflictos. Y `white skirt` + `black stockings` = 0. **Linter:** `footwear_canon.py` (calzado) + `garment_canon.py` (vestuario) — obligatorios por batch.

## 🖥️ FIDELIDAD PROMPT→IMAGEN (Directiva Ama 11-12/07/2026 — auditorías L691-L760, L729-L760/Seated y Standing)

Seis desvíos sistemáticos detectados mirando la imagen final vs el prompt. Todos blindados en el motor (`pose_rotation_v5.py` + `garment_canon.py`); el inyector DEBE aplicarlos:

1. **🧵 RAYA DE LA MEDIA SIEMPRE POR DETRÁS.** `back-seam stockings` es relativo a la cámara → en poses de frente Gemini pinta la costura por delante (confirmado L691/L752/L748). Si el look usa **medias con costura**, pasar `rotate_poses(..., seam=True)` (ancla pose-aware: frente liso, costura solo atrás; Back View costura visible atrás) y añadir `NEG_FRONT_SEAM` al negative.
2. **🚫 PRENDA CUBIERTA = SÓLIDA, SIN CORTES.** Los tokens de ADN (`navel piercing`, `visible under clothing`, `rune tattoo along hip crease and bikini line`) hacen que Gemini **le abra ventanas** a la prenda para exponerlos, rompiendo el `fully opaque at bust and groin` (confirmado L706 hueco en la cadera sobre la runa, L699 teddy cortado). En arquetipos **cubiertos** (traje/gala/maid/catsuit) pegar `OPAQUE_LOCK` + `NEG_CUTOUT`. El `wherever the garment covers` deja que runas/ombligo SÍ se luzcan en lencería/bikini/alto-corte (ahí es on-brand) — solo prohíbe cortar una prenda que debía cubrir. **Bloque A NO se toca.**
3. **✨ REGLA ANTI-MATE (siluetas de riesgo).** En siluetas que primean tela mate (**sastrería de lana/crepé, rib atlético, satén nupcial plano**), el sesgo del arquetipo le gana al token `vinyl/latex` y Gemini rinde tela natural mate, prohibida (confirmado L732 traje mate, L750 rib mate). Tener `vinyl` en el texto **NO basta** (L732 lo tenía). Dos capas: **(a)** preferir siluetas que NO primeen mate (bodysuit>rib, catsuit>blazer); **(b)** si la silueta de riesgo es obligada, pegar `GLOSS_LOCK` (token fuerte redundante) + `NEG_MATTE`. Contraste que lo prueba: L759 (gym) usó bodysuit `liquid latex` y salió brillante.
4. **📐 CONSISTENCIA DE PRENDA ENTRE POSES (escote/manga/largo).** El Token de Vestuario Bloqueado se pega idéntico ×7, pero si deja el **escote, el largo de manga o el ruedo sin fijar**, Gemini reinventa el corte en cada pose (confirmado L746: sin-mangas-cuello-alto/tiritas-escote-bajo/manga-larga en 3 poses del MISMO vestido; L707 mangas cap vs sin mangas; L693 lunares sólidos vs con espiral). Dos capas: **(a)** el token DEBE nombrar explícito **neckline + sleeve length + hemline** (ej. `off-shoulder bardot neckline, long fitted sleeves to the wrist, floor-length mermaid hem`); **(b)** pegar `CONSISTENCY_LOCK` + `NEG_INCONSISTENT`. El linter `garment_canon.py` marca vestidos/gowns cuyo token no fije escote/manga/ruedo. Enlaza con el [Token de Vestuario Bloqueado](../../00_Ele/...) (nada `strategic/various/cutouts` sin ubicar).
5. **🪑 SEATED — MUEBLE EQUIVOCADO Y POSTURA IGNORADA (Directiva Ama 11/07/2026 — auditoría L729-L760).** Dos patrones en la pose Seated: **(a)** si el setting trae una segunda superficie plana cerca del asiento (mesa de directorio, isla de cocina), Gemini apoya el cuerpo en ESA superficie en vez del asiento nombrado (confirmado L732: silla vacía al lado, ella perchada en el escritorio; L754: apoyada en la isla en vez de reclinada en el taburete) — fix: `SEATED_ANCHOR` en `pose_rotation_v5.py` ancla el peso al asiento y prohíbe apoyarse en mobiliario vecino, pegado a las 6 variantes Seated. **(b)** instrucciones de postura dinámica se aplanaban a la sentada genérica segura — "leaning forward with elbows on the knees" nunca aparecía (L729/L741/L759) y "seated REVERSED... chin resting on forearms" (straddle mirando el respaldo) rendía sentada normal de frente (L755, el más grave). Fix: variante reescrita con la instrucción al frente de la oración (primacía) + variante reversed/straddle reemplazada por un arco hacia atrás sobre el respaldo sin straddle (pariente del token `straddling` ya proscrito en el anti-safe check).

6. **🧍 STANDING — LA POSE DE FRENTE SALE DE ESPALDA (Directiva Ama 12/07/2026).** El slot Standing era el **único sin ancla de orientación**: Back nombra `back view` en sus 7 variantes, Side fuerza `side profile standing`, Odalisque y Seated ya tenían la suya — Standing solo decía `full body`, así que la orientación quedaba a criterio del generador y cualquier token débil de giro la arrastraba fuera del frente. Dos variantes del pool lo disparaban: **(a)** una era una **Back View infiltrada** (`the body turned three-quarters away ... looking back over the shoulder`) — el `torso twisted back so the bust returns to camera` es una torsión que el generador aplana al giro simple, y rendía espalda pura (confirmado L751 y L760: culo a cámara, indistinguibles del slot Back View); **(b)** otra mezclaba `walking straight toward the camera` con `head turned over the shoulder` (contradicción interna resoluble por el lado malo). Fix: **`STANDING_ANCHOR`** prepende frontalidad explícita (primacía) + las 2 variantes reescritas sin tokens de giro-de-espalda + self-check que veta esos tokens en el pool. **La Standing es la pose HERO**: es el único registro frontal del outfit completo — perderla no solo desvía la pose, **duplica la Back View** y el set queda sin frente. ⚠️ **NO** se arregla con el negative: el negative es uno solo por look y compartido por las 7 poses, así que pelearía con la Back View (que legítimamente ES de espalda). El lever es el ancla en el POSITIVE.

> 🔁 **Los prompts fosilizan.** Cada fix protege a los batches *futuros*, pero los prompts ya registrados conservan el texto de su época. Al cerrar un fix, **auditar los prompts sin imagen** y refrescarlos (los que YA tienen imagen no se tocan). El refresco masivo del 12/07 (looks 300+) encontró 1.167 poses incumpliendo fixes anteriores: 952 sin ancla anatómica, 242 odaliscas sin ancla de recumbencia, 108 con tokens anti-safe (rebotaban el filtro y quemaban cuota) y 96 POV literales que salían **selfie** (confirmado con imagen en L315 y L316).

## 💋 MAQUILLAJE Y ESTÉTICA (OBLIGATORIO)

Ele SIEMPRE usa el maquillaje **Aggressive Bimbo Makeup**:
`dramatic siren liner, dramatic lash extensions, overlined glossy hot pink lips, defined cupid's bow, flawless white porcelain skin, hyper-polished smooth skin texture`

**Reglas inquebrantables:**
- Uñas: `extra long French XXXL nails with white tips and pink base 5cm`
- Pelo: `dark cherry red hair, artificial XXXL extensions hip-length, voluminous waves`
- Vestuario: 100% **High-Gloss** (Vinyl, Latex, PVC). Negro **liberado** — es un color más de la paleta (rojo cherry, azul cyan, oro cromo, plata, neón, **negro**). Sigue prohibida la tela natural mate; el negro va siempre en material gloss.

## 🎨 COLOR FREEDOM
Paleta totalmente abierta: Rojo Cherry, Azul Cyan, Oro Cromo, Plata, Verde Neón, **Negro** y toda la Spectrum Expansion. **Deroga la anti-black rule (Directiva Ama 07/06/2026):** el negro dejó de estar restringido a acento — se usa igual que cualquier otro color, incluso dominante/monoblock.

🌈 **LIBERTAD TOTAL DE COLOR Y MATERIALES (Directiva Ama 12/06/2026):** derogadas **todas las ventanas y cuotas cromáticas** — ventana de familia dominante 1-de-5 (global y por sub-arquetipo), cero-solapamiento de color en batch, cuota Amarillos 1/6, cuota Cherry dominante 1/8 — **y la ventana de material (≥2 looks) del Step 0**. Color y material se eligen libremente por criterio estético/temático. El límite es de identidad, no de rotación: **Ele es una modelo fetichista** — la libertad de materiales opera dentro del universo fetish (vinyl, PVC, látex, wet-look, chrome, crystal mesh, wet-satin, laser-cut, rhinestone…); la tela natural mate sigue prohibida. **Siguen vigentes:** **anti-monoblock** (máx 2 monoblock seguidos — regla de composición) · cherry red de **pelo/labios** como ADN inamovible.

---

### Identidad Visual
- Referencia: **Sacha Massacre / Bimbo Aesthetic Plástica**
- Personalidad: Vinyl Cuico-Bimbo devota, voz chillona, adicta al shopping y a servir a su Ama. Usa muletillas ("O sea", "tipo", "heavy") y emojis 🫦💅👠🎀.
