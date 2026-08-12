# 🎥 Repertorio de Cámara y Escenarios — Anaïs Belland

> **Creado 12/08/2026** tras la auditoría visual (`99_Sistema/auditoria_visual_anais_20260812.md`).
> **Dueño único** de las variaciones de encuadre por slot y de los escenarios por look.
> El perfil visual (`02_Personajes/_perfiles_visuales/anais.md` §4) **apunta aquí**, no copia.
>
> ⚠️ **Este archivo NO cae en el filtro de LV-App** (no contiene `galeria_looks_anais` ni `looks_anais` en la ruta). Verificado contra la regla 11 §9bis. No renombrarlo a algo que sí caiga.

---

## 🔴 Por qué existe

La Ama lo dijo mirando la app: *"las imágenes de ditzy de Anaïs salen casi todas iguales"*. Tenía razón, y era medible.

El perfil §4 decía *"rotar al menos el ángulo, el nivel de contacto y la relación con el mobiliario"* — pero **no existía ningún repertorio del cual rotar**. Ele tiene el suyo (`pose_repertoire_v5.md`, 9 Standing × 7 Back × 6 Seated…); Anaïs no tenía ninguno, así que cada look repetía la misma frase de cámara.

**Medido sobre los 98 prompts (12/08/2026) — similitud media del texto de pose+setting entre los 14 looks:**

| Slot | Similitud | Veredicto |
|---|---|---|
| 1 · Standing | 33% | ✅ sano |
| 2 · Back View | **57%** | 🔴 clonado |
| 3 · Seated | 38% | ✅ sano |
| 4 · Side Profile | **78%** | 🔴 clonado |
| 5 · Sovereign Gaze | **59%** | 🔴 clonado |
| 6 · POV | **87%** | 🔴 el peor de todos |
| 7 · Odalisque | 63% | 🟡 tolerable — se conserva, ver nota de formato |

Los prompts del slot 5 de **L05, L06 y L07 eran idénticos carácter por carácter**; también los de L08/L09/L10 y los de L11/L12. Con el mismo texto sale la misma foto: encuadre simétrico frontal, misma distancia, mismo gesto, pelo cayendo igual a los dos lados. Lo único que cambiaba era el color en el borde inferior del cuadro.

**Y un error aparte, del mismo slot:** el Ditzy del **L08 salió en cuerpo entero**, no en primer plano — duplicando su propio Standing. El slot 5 es `extreme close-up from the chest up`; ese encuadre se perdió.

---

## 📐 Regla de rotación

Cada look toma su variación con `índice = (número_de_look - 1 + desplazamiento_de_slot) mod 7`, con desplazamientos distintos por slot. Consecuencia:

- **Dos looks consecutivos nunca comparten variación en el mismo slot.**
- **Dentro de un mismo look, los cuatro slots rotados usan índices distintos** — el set no se siente como la misma foto siete veces.
- Con 14 looks, cada variación aparece exactamente dos veces por slot, y nunca seguidas.

Desplazamientos vigentes: Back View `+0` · Side Profile `+2` · Sovereign Gaze `+4` · POV `+6`.

> **Slots 1 (Standing), 3 (Seated) y 7 (Odalisque) NO se rotan desde aquí:** su texto ya es propio de cada look (la acción, el objeto en la mano, el mueble) y midió sano. Lo que sí se les cambió fue el escenario, que sale de la tabla de más abajo.

---

## 2 · BACK VIEW — 7 variaciones

| # | Variación |
|---|---|
| B1 | `seen from directly behind at full height, both shoulders square to the lens, the head turned barely a quarter so that only the line of her cheekbone and the beauty mark catch the light, her honey blonde hair gathered forward over the far shoulder to leave the back bare` |
| B2 | `seen from behind at a low three-quarter angle from her right, the camera below the line of her hips, her chin dropped toward the near shoulder in a cold sidelong glance, her hair swept entirely off the back` |
| B3 | `seen from behind in a tight waist-up crop, the camera close enough to read the seam, lacing or fastening of the garment across her spine, her face turned in profile at the frame's edge, one hand lifting the weight of her hair off the nape` |
| B4 | `seen from behind from an elevated angle looking down the length of her back and along the fall of the garment to the floor, her face tilted up over the shoulder to find the lens with a cold appraising gaze` |
| B5 | `seen from behind at a wide three-quarter angle from her left, caught mid-stride with the weight already on the forward foot and the garment trailing, her head turned sharply back over the shoulder` |
| B6 | `seen from behind standing in a lit doorway or against a lit window, her silhouette rimmed by the light, the camera at eye level, only a sliver of her cheek and the beauty mark visible past the fall of her hair` |
| B7 | `seen from behind leaning forward from the waist against a table, rail or back of a chair, the spine curved and the shoulder blades drawn together, her head turned back and down toward the lens with a cold half-lidded look` |

## 4 · SIDE PROFILE — 7 variaciones

| # | Variación |
|---|---|
| S1 | `a true side profile at full height, nose and chin drawn as a clean silhouette against the key light, her gaze forward and away from the lens, the hourglass line unbroken from shoulder to ankle` |
| S2 | `a side profile cropped from the thigh up, the near shoulder rolled toward the lens, her chin dropped and her eyes lifted back into the camera through the lashes` |
| S3 | `a side profile with the torso in true profile and the head turned fully back to the lens over the near shoulder, one hand resting at the crest of the hip` |
| S4 | `a side profile from a low angle at hip height looking up the length of her, the jaw and throat drawn long, her gaze cast down the line of her nose at the lens` |
| S5 | `a side profile seated or perched, knees together and angled away from the lens, the spine long and the shoulders open, her face turned back a quarter toward the camera` |
| S6 | `a side profile leaning with one shoulder against a wall, column or doorframe, the near arm hanging loose, her gaze level and cold out past the lens` |
| S7 | `a side profile from three-quarters behind the shoulder, the camera reading the back of the arm and the curve of the waist, her profile edge-lit and her lashes lowered` |

## 5 · SOVEREIGN GAZE — 7 variaciones

| # | Variación |
|---|---|
| G1 | `a tight head-and-shoulders portrait with the face filling the frame, her gaze locked dead into the lens, the key light raking from one side so that half the face falls into shadow` |
| G2 | `a chest-up portrait at a three-quarter turn, her chin lifted and turned away while only the eyes come back to the lens, the beauty mark catching a highlight` |
| G3 | `a chest-up portrait from slightly below, her chin dropped so that she looks down the line of her nose into the lens, the throat and jaw drawn long` |
| G4 | `an extreme close-up on the mouth and the eyes, the lips parted just enough to break the line, the gaze half-lidded and unhurried, the top of the garment only a band of colour at the frame's edge` |
| G5 | `a chest-up portrait with one hand risen to the jaw or the throat, the fingers deliberate and unhurried, her gaze steady and unimpressed into the lens` |
| G6 | `a chest-up portrait shot past a foreground element thrown out of focus in front of her — a candle flame, the lip of a glass, the edge of a mirror frame — her face sharp behind it` |
| G7 | `a chest-up portrait in near profile with the head turned back over the shoulder, her eyes cutting to the lens at the very edge of their range, the neck and décolleté fully lit` |

> 🔒 **Los siete son de PECHO PARA ARRIBA, sin excepción.** El Ditzy del L08 salió en cuerpo entero por no tener el encuadre anclado. Cada variación nombra su recorte explícitamente.

## 6 · POV — 7 variaciones

| # | Variación |
|---|---|
| P1 | `a low-angle point of view from the floor as though the viewer kneels at her feet, the camera below her knee looking up the full length of her, her face small and far above with her gaze falling down the frame` |
| P2 | `a low-angle point of view from hip height as though the viewer kneels close in front of her, the garment filling the lower frame, her chin dropped and her eyes down into the lens` |
| P3 | `a low-angle point of view from just below her waist with her leaning in over the lens, one hand braced on a surface beside the camera, her face large and close above` |
| P4 | `a low-angle point of view taken from her side as though the viewer kneels beside her rather than before her, her head turning down and across to find the lens` |
| P5 | `a low-angle point of view with her seated above the camera on the edge of a desk, chaise or chair, one leg crossed over the other at the level of the lens, her gaze cast down` |
| P6 | `a low-angle point of view from the floor with one hand extended down toward the lens, palm open and unhurried, her face behind and above it with a level cold gaze` |
| P7 | `a low-angle point of view from very low and very close, the camera almost at the floor, the vertical of her body rising the full height of the frame with the ceiling behind her head` |

---

## 🏛️ Escenarios por look — dueño único

> **Por qué específicos:** en la auditoría, los looks con setting genérico (`dark chamber`, `La Voûte interior`) **cambiaban de habitación entre poses del mismo look** — el L01 pasó de salón de baile a sala de piedra a panelado de madera a arcos góticos. El L14, cuyo setting nombraba mobiliario concreto, **mantuvo la misma habitación en las 7 poses**. El generador no es caprichoso: rellena lo que no se le dice.
>
> Regla: **el escenario se describe con el mismo nivel de detalle que el vestuario.** Mínimo: el espacio + tres piezas de mobiliario u objetos nombrados + la fuente de luz.

| Look | Arquetipo | Escenario |
|---|---|---|
| **01** Terciopelo y Sangre | Noche | `the main salon of La Voûte — floor-to-ceiling burgundy velvet drapes, a crystal chandelier hanging low, gilt-framed mirrors along the panelled walls, small marble tables with lit candelabra, formally dressed guests blurred deep in the background, a single hard key spotlight from above over warm amber fill` |
| **02** Rosa y Látex | Boudoir | `her private boudoir — a deep red velvet chaise longue, an oversized gilt-framed dressing mirror, a marble side table crowded with lit pillar candles, heavy damask curtains drawn shut, warm low candlelight as the only source` |
| **03** Esmeralda de Alto Brillo | Látex | `a dark minimalist private chamber — black lacquered cabinetry, polished dark stone floor, bare charcoal walls with no ornament, one low black bench, a single hard directional accent light raking across the latex` |
| **04** Tinta Rosa | Sesión Literaria | `her private study — floor-to-ceiling leather-bound bookshelves, a mahogany writing desk with a brass inkwell and a green banker's lamp, an open journal and a fountain pen, a worn Persian rug, warm lamplight and candlelight` |
| **05** Zafiro de Medianoche | Noche | `the mezzanine landing of La Voûte overlooking the floor below — a carved balustrade of dark wood, brass sconces along the panelled wall, a narrow console table with a silver tray, the crowd a warm blur far beneath, cool blue-grey light from above meeting the amber from below` |
| **06** Bronce Líquido | Noche | `the private box of La Voûte — buttoned oxblood leather banquette, a low brass drinks table with a decanter, a heavy velvet curtain half drawn across the opening, the stage light spilling in from one side` |
| **07** Perla Fría | Noche | `the entrance hall of La Voûte — a broad stone arch, wrought-iron candle sconces down the wall, a black-and-white marble floor, a mirrored console with white orchids, one cold key spotlight from directly above with candlelight as fill` |
| **08** Champagne y Plata | Boudoir | `her dressing room — a tufted green velvet settee, twin gilt mirrors facing each other, a low table with a silver hand mirror and crystal scent bottles, a bank of lit candles along the wall, warm candlelight only` |
| **09** Esmeralda Íntima | Boudoir | `her bedchamber — a four-poster bed with heavy emerald silk hangings drawn back, a carved wooden screen, a nightstand with a single lit oil lamp, a fur throw folded over the foot of the bed, low warm lamplight` |
| **10** Terciopelo y Boning | Boudoir | `her boudoir at the vanity — a black lacquered dressing table with a triptych mirror, an upholstered stool in black velvet, jewellery loose across the tabletop, a candelabra at each end of the mirror, warm candlelight bouncing off the glass` |
| **11** Cuero y Carmesí | Látex | `a private fetish salon — oxblood leather upholstered walls, a low steel-framed bench, a rack of polished dark wood, a single caged bulb throwing hard light straight down, everything else in deep shadow` |
| **12** Bronce Clínico | Látex | `a clinical private chamber — brushed steel cabinetry, a white lacquered examination bench, polished concrete floor, a single articulated lamp on a steel arm, cold neutral light with one warm accent raking the latex` |
| **13** Kimono de Medianoche | Sesión Literaria | `her night study — leather-bound bookshelves to the ceiling, a mahogany writing desk with an open journal and a brass candlestick, a velvet reading daybed against the wall, a glass of dark wine on the desk, candlelight and one low lamp` |
| **14** Sastrería Borgoña | Ejecutivo | `her dark wood-panelled private office — a mahogany desk with an inkwell and a fountain pen, leather-bound bookshelves floor to ceiling, a buttoned leather armchair, heavy drapes at the window, a cool key light from the side` |

---

## 📐 Nota de formato — el Odalisque va APAISADO (Ama 12/08/2026)

Las 7 imágenes Odalisque materializadas salieron en **1200×669 (horizontal)** contra el 669×1200 vertical del resto. La auditoría lo levantó como posible defecto de rotación; **la Ama confirmó que es deliberado**: se lo pide así a Gemini porque la figura reclinada **se aprecia mejor en horizontal**.

**No es un error y no se corrige.** El slot Odalisque de Anaïs es el único horizontal de su set. Cualquier auditoría futura que lo marque está equivocada.

---

## 🔒 Anclas de prenda que la auditoría obligó a agregar

Defectos fotografiados que el negative no frenó — van como **ancla afirmativa en el positive**, junto al BLOQUE B:

| Ancla | Cuándo | Texto |
|---|---|---|
| `BARE_LEGS_LOCK` | Todo look cuyo BLOQUE B diga `bare legs` | `her legs completely bare from the hem down, uncovered skin with no stockings, no tights, no hosiery of any kind` |
| `GLOVE_LENGTH_LOCK` | Guantes que no sean de ópera | `the gloves ending exactly where described and no further, the forearms above them left bare and uncovered` |
| `EMBROIDERY_LOCK` | Prenda con bordado localizado | `the embroidery confined strictly to the places named and nowhere else, every other panel of the fabric left plain and unembroidered, with no additional motif, figure, animal or scene added anywhere on the garment` |
| `CLOSURE_LOCK` | Prenda definida por su cierre | `the closure described reading clearly and completely in this frame — its line, its pull and its exact placement on the body — never smoothed away, never replaced by a plain uninterrupted neckline or panel` |

**Origen:** L13 Standing salió con medias negras tupidas teniendo `bare legs` escrito · L14 salió con guantes hasta el codo pidiendo `wrist-length` · L13 Back View salió con **dragones dorados inventados** por toda la espalda cuando el spec dice oro *solo en puños y ruedo*.
