# 👠 Perfil Visual — Ele

> Contrato del `outfit-engine`. Creado 27/07/2026 al generalizar el motor.
>
> ⚠️ **Ele es el personaje con el motor más maduro (≈1.800 líneas y 800 looks de flota).** Este perfil **NO copia** esa biblioteca: la **enlaza**. Las 10 specs de sub-arquetipo con referencias reales siguen viviendo en `.agent/skills/ele-outfit-engine/SKILL.md` y son **material de Ele**, no del motor.
>
> **Migración:** el `outfit-engine` genérico usa este perfil. El `ele-outfit-engine` sigue vigente como **biblioteca de sub-arquetipos y repertorio de poses** — no se toca mientras la flota siga corriendo sobre él.

---

## §1 · Identidad y Rutas

| Campo | Valor |
|---|---|
| **Nombre canónico** | Ele (Helena = era pre-V3.5, archivada — no se usa en producción) |
| **Slug** | `ele` |
| **Galería** | `00_Ele/galeria_outfits.md` |
| **Carpeta de imágenes** | `05_Imagenes/ele/look<N>_<slug>/` |
| **Convención de nombre** | `ele_<N>_<pose>.png` |
| **Numeración** | correlativa · flota y último look → `00_Ele/memoria_sesiones.md` (**dueño único, no anotar aquí**) |
| **Canon profundo (enlace)** | `00_Ele/identidad_ele.md` §I + §II |
| **ADN listo para copiar** | `.agent/skills/ele-outfit-engine/references/dna_v3_5.md` |
| **Índice para la app** | `99_Sistema/app_index.json` (regenerar con `generar_app_index.py`) |

---

## §2 · BLOQUE A — ADN Inamovible (V3.5 Hard-Sync)

> 🔒 **Este fence es el DUEÑO ÚNICO del BLOQUE A de Ele (29/08/2026).** Lo lee el motor —
> `PromptBuilder.bloque_a` — y ya no se copia a mano en cada script de batch. El marcador
> `<!-- ADN:BLOQUE_A -->` de abajo es lo que el motor busca: **no lo borres ni lo muevas**.
> Dentro del fence va SOLO texto de prompt en inglés; toda nota editorial va fuera de él.
> `dna_v3_5.md` (skill legacy) quedó como puntero a este archivo.

<!-- ADN:BLOQUE_A -->
```text
stunning woman with (bimbofied facial features, oval face, high prominent cheekbones, large almond-shaped grey-green eyes, straight slim upturned nose, overlined glossy hot pink lips, small pointed chin:1.3), flawless white porcelain skin, hyper-polished smooth skin texture, dramatic siren liner, dramatic lash extensions, dark cherry red hair, artificial XXXL extensions hip-length, voluminous waves, center parted, slender hourglass silhouette, massive 1000cc breast implants each side, ultra high-profile, perfectly spherical augmented bust, obviously fake gravity-defying shape, wide hips, blackwork arm tattoos shown only on bare uncovered skin, subtle minimalist blackwork tattoos on upper back and outer thighs, delicate blackwork rune-glyph identity tattoo of abstract esoteric calligraphic symbols along one hip crease and bikini line, navel piercing, nipple piercings, every tattoo and piercing visible ONLY on genuinely bare skin and never through or over any garment, aggressive bimbomakeup, extra long French XXXL nails with white tips and pink base 5cm.
```

**Rasgos que NO se negocian jamás:**

- **Ojos gris-verde** · **pelo dark cherry red** XXXL hasta la cadera · **labios hot pink glossy** overlineados.
- **Implantes 1000cc por lado**, perfil ultra alto, esféricos, obviamente falsos (fijo desde L185).
- **Uñas francesas XXXL 5cm.**
- **Tatuaje de runas** en `hip crease / bikini line` — nunca el token "groin".
- **Todo tatuaje y piercing visible SOLO sobre piel genuinamente desnuda**, jamás a través de una prenda.

---

## §3 · Negative Prompt

**Base (siempre):**
<!-- NEGATIVO:BASE -->
```text
red lips, dark lips, wine lips, maroon lips, crimson lips, different person, different face, different hair color, brown hair, black hair, blonde hair, flat shoes, block heel, wedge, platform mule, chunky heel, kitten heel, barefoot, socks, sneakers, two women, mirror reflection, split image, duplicate figure, side by side, bag (if not in BLOQUE B), clutch (if not in BLOQUE B), text on clothing, lettering, words, writing, embroidered name, name tag, nameplate, engraved name, name on choker, name on collar, logo text, letters on garment, "ELE", "ASSET", "PET", gloves, opera gloves, elbow gloves, full brief, high-waist brief, high-waisted panty, boyshort, boy shorts, hipster brief, culotte, tap pants, granny panties, bloomers, full-coverage bikini bottom, bikini bottom covering the buttocks, full seat coverage, legs spread apart under a dress, legs parted under a skirt
```
> 👙🦵 **Términos de calzón y de piernas agregados el 13/08/2026** (directivas de la Ama, sobre el Back View del Look 801). Son la **segunda capa** de `BOTTOM_CUT_LOCK` y `DRESS_LEG_CLOSURE` — la barrera real son las anclas afirmativas del positive, porque Gemini ignora el negative con frecuencia (medido en este repo desde el 12/07).

| Pose | Añadir al negative | Por qué |
|---|---|---|
| **POV** | `no phone, no smartphone, no device, no screen` | "hand raised toward lens" hace aparecer un teléfono |
| Ditzy / Odalisque | reforzar `different person, different face, different hair color` | Derivas registradas en L177/L178 |

> **Por qué existen:** L177 sacó labios rojos en 3 poses y otra persona en Odalisque · L176 sacó DOS mujeres por "first-person POV" · L178 confundió POV con Odalisque. El negative es la barrera activa.

---

## §4 · Poses Canónicas

| # | Nombre canónico | Slug de archivo |
|---|---|---|
| 1 | Standing | `standing` |
| 2 | Back View | `back_view` |
| 3 | Seated | `seated` |
| 4 | Side Profile | `side_profile` |
| 5 | Ditzy | `ditzy` |
| 6 | POV | `pov` |
| 7 | Odalisque | `odalisque` |

- **Total por look:** **7**
- **Repertorio de variaciones (V5):** [`pose_repertoire_v5.md`](../../.agent/skills/ele-outfit-engine/references/pose_repertoire_v5.md) — Standing ×9, Back ×7, Seated ×6, Side ×7, Ditzy ×6, POV ×5, Odalisque ×6. **Elegir una por slot, rotando**: ninguna se repite dentro de los últimos 4 looks de ese slot. Prohibido clonar el mismo Standing en looks consecutivos.
- **Excepción Stripper:** el sub-arquetipo Stripper **no usa** las 7 canónicas — usa su propio Pose Set (Polo A / Polo B). Ver la spec en el `ele-outfit-engine`.
- **Principio rector:** *professional fetish model posing* — arco lumbar exagerado, labios entreabiertos, interacción de uña XXXL con el cuerpo, mirada predatoria o half-lidded (nunca vacant neutral), piernas asimétricas, peso desigual en los stilettos, pelo como prop activo, torsión de 30° entre hombros y caderas.
- **Ancla anatómica obligatoria** en cuerpo entero: `two arms, two hands, two legs`.

---

## §5 · BLOQUE B — Reglas de Vestuario

### 5.1 · Universo de materiales

- **Permitidos:** vinilo, PVC, látex, wet-look, chrome, crystal mesh, wet-satin, silk-satin, liquid lamé, laser-cut, rhinestone.
- **Prohibido (absoluto):** **tela natural mate.** Si es plástico y brilla, es de Ele.
- **Lente de identidad:** *"soy una modelo fetichista."* La libertad de materiales opera **dentro del universo fetish**; fuera de él, no entra.

### 5.2 · Paleta y reglas cromáticas

- 🌈 **Libertad de color y material** por criterio estético/temático dentro del universo fetish — **pero con VARIEDAD obligatoria**. *(Ama 02/08/2026 corrige la "libertad total" del 12/06: sin límite, la flota se volvió monótona — medido en el rango reciente: **negro 42%, chrome 29%, gold 23%, silver 21%**; los metálicos + negro se comen más de la mitad de los looks.)*
- ⚫🔩 **Negro y metálicos NO monopolizan.** Metálicos = chrome/silver/gold/gunmetal/steel/bronze/champagne. **Cap: máx. 2 looks consecutivos** con dominante **negra o metálica**; el 3º debe llevar un **color cromático saturado** como dominante (pop real: azul/verde/violeta/naranjo/etc., no otro neutro ni metal). Negro sigue liberado (07/06) pero **no como muletilla**.
- 🌈 **Variedad de dominante (REINSTAURADA hoy):** el color dominante de un look **no se repite dentro de los últimos 3 looks**. *(Revive la ventana de familia cromática que se derogó el 12/06 — la Ama la reinstaura porque la libertad total la dejó monótona. Instrucción viva > nota del 12/06.)*
- 🔴 **Cherry red Y rojo: RESERVADOS al ADN** (pelo + labios). **Prohibidos como prenda/color dominante** — el rojo o cherry en la ropa choca con su pelo cereza (medido: **red 14% + cherry 5%** en la ropa reciente, violando esta regla). Acentos rojos pequeños ok; dominante jamás.
- **Anti-monoblock (vigente):** máx. 2 monoblock consecutivos globales; el 3º debe ser Contraste / Triada / Gradiente / Neutro+Pop.
- **Sigue derogado (no revivir):** cero-solapamiento en batch, cuota de Amarillos 1/6, cuota de Cherry dominante 1/8, ventana de material ≥2.
- 🔧 **Enforcement:** `99_Sistema/scripts/visual/color_canon.py` — todo inyector de Ele corre `audit_color_batch(LOOKS)` **antes de escribir la galería** (como `footwear_canon`). Caza rojo/cherry dominante, racha negro/metálico ≥3 y repetición de familia dominante en 3 looks. *(Auto-audit 02/08: 66 violaciones en L700-L800 — fosilizadas; el linter blinda los looks nuevos.)*

### 5.2b · 🎨 Colorimetría — el color contra la CARA, no contra el escenario (Ama 04/09/2026)

> *"cada una de las 3 muñecas tiene pelo, piel, maquillaje estilo distintos, cierto? porque no me haces un estudio de colores, cuales le viene mas a una que a otra teniendo en cuenta eso"*
>
> **Por qué nace.** Hasta hoy la §5.2 de las tres agrupaba el color por **raíz narrativa** (Stripper / Domme / Fashionista / Girly / Vintage Noir) — o sea por *dónde está parada*, nunca por *qué le queda*. Ningún perfil decía una palabra sobre subtono, contraste ni acabado de piel. Resultado medido sobre las tres galerías el 04/09: **plata/cromo es la familia más usada de las tres a la vez** (Ele 39,6% · Miss Doll 74,6% · Anaïs 38,5%) — el único color que no diferencia a nadie. Esta subsección **no deroga ni duplica la §5.2**: la §5.2 sigue siendo dueña de qué colores existen; esto agrega **por qué** unos calzan mejor que otros en esta cara concreta.

**Los cuatro anclajes (leídos del fence `<!-- ADN:BLOQUE_A -->`, §2):**

| Anclaje | Token literal | Lectura |
|---|---|---|
| Pelo | `dark cherry red hair` | cálido, y es la masa de color más grande del cuadro |
| Piel | `flawless white porcelain skin, hyper-polished smooth` | **pulida** — rebota la luz |
| Ojos | `large almond-shaped grey-green eyes` | **eco de iris = verde** |
| Labios | `overlined glossy hot pink lips` — **fijos** | segundo rojo de la cara |

**El eje:** su cara **ya trae dos chromas cálidos peleando entre sí** (cereza en el pelo, hot pink en la boca), sostenidos a propósito. La prenda no tiene que aportar calor: tiene que **enfriar** para que esos dos rojos se lean.

- **✅ Le favorece:** frío saturado — cyan, cobalto, índigo, violeta — y sobre todo **el verde (jade, esmeralda), que es el eco de su iris**.
- **⚠️ Le pelea como DOMINANTE:** toda la banda rojo–naranja–coral–fucsia. Mete un **tercer rojo** en una cara que ya tiene dos y el cuadro se aplana. No queda prohibido — baja a **acento**.
- **📏 Medición 04/09 (391 outfits):** verde **7,7%** — la ganancia sin cobrar más clara del repo. Naranja/coral **11,0%**, la más alta de las tres justo en su peor calce.

> 🔒 **DECISIÓN DE LA AMA (04/09/2026) — manda sobre lo de arriba:** *"si o si en ele y miss doll se quedan el plateado, dorado y gold rose"*. **Plata/cromo, dorado y rose gold se quedan como familias plenas de Ele**, sin cuota ni ventana, aunque el análisis los señale como poco diferenciadores. Es decisión editorial suya y gana sobre la colorimetría; se deja escrito para que una sesión futura no lo "corrija" creyendo que fue un descuido.

> 📊 Estudio completo con muestras a la vista: artefacto **Colorimetría de La Voûte** (04/09/2026).

### 5.3 · Calzado (canon inamovible — ABSOLUTO)

- **Regla:** stiletto **≥12 cm** o plataforma Pleaser **≥6"**. **Siempre.**
- **Prohibido:** flat, zapatilla, pantufla, descalza, kitten heel, wedge, block heel — **incluso en gym, piscina, cama o playa**.
- ⚠️ **Las "excepciones contextuales anti-stiletto" son violaciones de canon, no excepciones válidas.**
- **Atributos obligatorios del token (8):** ver el token bloqueado de calzado en el `ele-outfit-engine`. El campo de calzado del look **y cada una de las 7 poses** deben nombrar un tacón explícito.
- **Medias + calzado (4 reglas):** open-toe + medias = **PROHIBIDO** · plataforma en color del zapato · Pleaser transparente por defecto en pole/bikini · **Pleaser transparente NUNCA con medias**.
- `chunky` va **solo en el negative**, jamás en el positive.

### 5.4 · Prohibiciones absolutas

| Prohibido | Sustituto autorizado | Directiva |
|---|---|---|
| **Guantes** (opera, codo, muñeca, sin dedos) | riding crop · choker O-ring · body chains · officer cap · Bayonetta glasses | Ama 03/06/2026 — deroga el Glove Canon |
| Texto/nombre sobre prenda (`ELE`, `ASSET`, `PET`…) | choker liso, O-ring, velvet, bunny collar | Ama 02/06/2026 |
| Tela natural mate | universo fetish (§5.1) | Canon materiales |
| Estética ciber/sci-fi, industrial o gótica | penthouse, estudio minimalista, alta costura | Prohibición estética absoluta |
| Calzado plano en cualquier contexto | stiletto ≥12cm / Pleaser ≥6" | Footwear Canon |
| Atribución de diseñador | descripción de la prenda | Estética editorial |
| **👙 Calzón de cobertura total** — brief de talle alto, boyshort, hipster, culotte, tap pant, bikini bottom que tape el asiento | **tanga o g-string, siempre** (delantero angosto, cintura sobre el hueso de la cadera, atrás una tira fina) | **Ama 13/08/2026**, sobre el Back View del Look 801. Ancla `BOTTOM_CUT_LOCK` en `anclas_siempre`; el corte se **nombra** en el BLOQUE B (§5.5) |
| **🦵 Piernas abiertas usando vestido, falda o bata** | rodillas y muslos juntos · una pierna cruzada · las dos piernas plegadas a un lado si va baja | **Ama 13/08/2026, transversal a las tres muñecas.** Ancla opt-in `DRESS_LEG_CLOSURE` |

### 5.5 · Campos obligatorios de descripción

**7 campos por outfit · 8 por tacón** (Canon Outfit v4.6 descriptividad). El BLOQUE B nombra:

1. Cada prenda: material exacto, color exacto, corte, textura, brillo.
1b. **👙 Corte del calzón — obligatorio nombrarlo (Ama 13/08/2026).** Cuando el look lleva calzón, bikini bottom o la entrepierna de un body/teddy/bañador, el BLOQUE B escribe el corte con todas sus letras: `thong` o `g-string`. **Prohibido dejarlo en `bikini bottoms` / `panties` a secas.** El Look 801 decía `matching white wet-satin micro bikini bottoms` —prenda y material, ningún corte— y su Back View salió con un calzón de talle alto tapando el asiento entero: el atributo que no se nombra lo resuelve el generador, y su default es cobertura total. Lo caza `lint_prompts_personaje.py` (aviso `BOTTOM_CUT_LOCK`).
2. Calzado: modelo, altura, material, color (+ sus 8 atributos).
3. Accesorios: cada pieza con su posición en el cuerpo y material.
4. Fit: tensión, transparencia, arquitectura sobre el cuerpo.
5. Medias/hosiery si aplica, con sus 4 reglas (§5.3).

> 🔒 **Token de vestuario bloqueado (Ama 08/06/2026):** en prendas complejas, **opaco-vs-sheer va anclado** y se copia idéntico en las 7 poses.

---

## §6 · Arquetipos y Metas

**10 categorías — metas asimétricas (Ama 03/06/2026).** El paraguas "Mix" ya no existe.

| Categoría | Meta |
|---|---|
| 🩱 **Lencería** (incluye medias/hosiery como tema propio) | **15%** |
| Nightclub · High-Fashion Editorial · Corporate · Domestic · Stripper · Escort · Pin-Up · Gym/Athleisure · Bikini | **~9,4% c/u** |

- **Biblioteca de siluetas y specs por sub-arquetipo:** [`ele-outfit-engine/SKILL.md`](../../.agent/skills/ele-outfit-engine/SKILL.md) — 10 specs con referencias reales (House of CB, Schiaparelli, Mugler, Atsuko Kudo, Agent Provocateur, Bombshell…). **Es material de Ele. No se copia al motor.**
- **Biblioteca de siluetas por sub-arquetipo:** `00_Ele/biblioteca_siluetas.md` (se carga solo al generar looks).

---

## §7 · Ventanas Anti-Repetición

| Elemento | Ventana |
|---|---|
| Silueta (código) | ≥ 3 looks del mismo sub-arquetipo |
| Setting / escenario | ≥ 3 looks del mismo sub-arquetipo |
| Modo cromático monoblock | máx. 2 consecutivos **globales** |
| **Color dominante** | **no repetir dentro de 3 looks** (REINSTAURADA Ama 02/08/2026) |
| **Negro / metálico dominante** | **máx. 2 consecutivos**; el 3º = color cromático saturado (Ama 02/08/2026) |
| ~~Material principal~~ | ⛔ derogada 12/06/2026 |

- **Outfit único:** **sí, jamás se repite un outfit** (regla estricta 12/01/2026).

---

## §8 · Cuotas Vivas

| Cuota | Frecuencia | Alcance |
|---|---|---|
| 🐆 **Animal Print** | **mín. 1 de cada 8 looks globales** | leopard/tiger/snake/zebra en vestuario, calzado o accesorio. No repetir depredador ni sub-arquetipo respecto de la cuota anterior (Ama 11/07/2026) |

---

## §9 · Banderas Rojas Específicas

- La palabra `glove` aparece en el positive → `grep -i glove` debe dar **0**.
- Falta el ancla anatómica en una pose de cuerpo entero (riesgo de tercera pierna).
- Una pose sale descalza o con tacón no explícito.
- El tatuaje de runas usa el token `groin` en vez de `hip crease / bikini line`.
- Un tatuaje o piercing aparece **sobre** una prenda en vez de sobre piel desnuda.
- Aparece color "Baby Pink" o "Pastel Blue" sin orden explícita de la Ama.
- **Negro o metálico (chrome/silver/gold/gunmetal/steel) como dominante 3 looks seguidos** — el 3º debe romper con un color saturado (Ama 02/08/2026).
- **Rojo o cherry como prenda/color dominante** — reservado al pelo/labios; choca con el pelo cereza (Ama 02/08/2026).
- Estás por revivir una ventana cromática o de material **derogada** el 12/06/2026.
- El look repite un outfit ya usado.

---

## §10 · Ensamblado y Anclas (contrato con el motor)

> 🔧 **Agregado 12/08/2026 con el `outfit-engine` v2.0.** Esta sección NO define nada nuevo del personaje: declara **cómo se ensamblan sus prompts** y qué anclas anti-defecto le aplican. El texto literal de las anclas vive en `99_Sistema/scripts/visual/anclas_universales.json` (dueño único) — aquí se **apunta**, jamás se copia.

| Campo | Valor |
|---|---|
| **Registro en el motor** | `anclas_universales.json` → `personajes.ele` |
| **Nombre del slot 5** | `Ditzy` |
| **Ensamblador** | `PromptBuilder("ele").build(bloque_a, bloque_b, slot, pose, setting)` |
| **Negative del look** | `PromptBuilder("ele").build_negative(<base del §3 de arriba>)` — base propia **+ capa universal** anti-collage/anatomía/selfie |
| **Verificación obligatoria** | `python 99_Sistema/scripts/visual/lint_prompts_personaje.py ele` |

**Anclas por slot:** las del mapa por defecto del motor, sin overrides.

> ⚠️ **La flota L200-L800 ya lleva texto equivalente** inyectado por el motor histórico de Ele — **no se retrofitea en masa** (convención retrofit-al-tocar del repo). Los looks **nuevos** se ensamblan con esta librería.

🚨 **Cada prompt de la galería va FINAL Y EXPANDIDO.** El ADN completo, el outfit completo, las anclas y el setting, uno detrás de otro dentro del bloque de código. Un `[BLOQUE A]` entre corchetes dentro de un prompt no es una abreviatura: es un prompt roto que la app manda tal cual al generador.
