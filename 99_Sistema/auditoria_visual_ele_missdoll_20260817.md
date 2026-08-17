# 🔍 Auditoría Visual — Ele (Look 801) y Miss Doll (Looks 24-25)

**Fecha:** 17/08/2026 · **Pedido de la Ama:** *"analiza las ultimas imagenes de ele y miss doll, busca desviaciones desde el prompts vs imagenes y imagenes del mismo look"*

**Alcance real medido:** lo *último* de cada muñeca según el índice de git, no según la memoria.
- **Ele → Look 801** «White Satin Nurse Bikini» (7/7, subidas 13/08). No hay nada de Ele posterior.
- **Miss Doll → Look 25** «Rose Marabou Suite» (7/7) y **Look 24** «Cutout Circuit» (3/7), ambos subidos **hoy 17/08**.

**Piso de validez verificado ANTES de auditar** (`Image.open().size`): 0,80–1,06 MP en las 17 imágenes. Ninguna miniatura. Lo que se ve, se ve de verdad.

> ⚠️ **Recordatorio de método:** lo commiteado son las **sobrevivientes** de los reintentos de la Ama. Un defecto que ella regeneró existe aunque acá no aparezca.

---

## 👠 ELE — Look 801 «White Satin Nurse Bikini»

**BLOQUE B de referencia:** top micro bikini triangular de wet-satin blanco · tanga/g-string a juego · mini delantal de enfermera de encaje blanco transparente con lazo ancho de satén · **sin medias, piernas desnudas** · sandalias plataforma de acrílico transparente 8" + 4", puntera abierta, hebilla plateada · suite de preparación de La Voûte, piso de mármol negro, velas.

### Veredicto por pose

| Pose | Veredicto | Desviación |
|---|---|---|
| Standing | ✅ **Referencia** | Cumple entero. Es la foto contra la que hay que medir el resto. |
| Seated | 🟡 **Aviso** | Cruz roja inventada en el delantal · busto visiblemente menor · manos no hacen el gesto pedido |
| Ditzy | 🟡 **Aviso** | Encuadre 3/4 largo en vez de *waist-up* |
| POV | ✅ **Correcto** | Mirada al lente ✅, una sola mano ✅, sin teléfono ✅ |
| Odalisque | ✅ **Correcto** | Reclinada, horizonte nivelado, ambos tacones visibles |
| **Back View** | 🔴 **Regenerar** | Calzón de talle alto tapando el asiento · tatuajes en manos y dedos · escenario cambiado |
| **Side Profile** | 🔴 **Regenerar** | **Otro outfit completo** |

### 🔴 Back View — tres fallas, una nueva

1. **Calzón de talle alto que tapa el asiento entero.** El prompt trae `BOTTOM_CUT_LOCK` completo y explícito (*"never a full-seat brief... the back panel is never widened to cover the seat"*). El ancla está escrita y **no se cumplió**. Defecto ya levantado el 13/08 → **confirmado vivo**.
2. **🆕 Tatuajes sobre manos y dedos.** El prompt dice literal: *"her hands, fingers, neck, throat, sternum, shins, calves and feet are clean unmarked porcelain skin with no tattoos and no glyphs"*. La imagen trae mandala/paisley bajando por el antebrazo **hasta los dedos**, más una pieza enorme en cadera y muslo. Y no son *"subtle minimalist blackwork"* como pide el ADN: son mangas ornamentales completas. **Hallazgo nuevo, no estaba en la auditoría del 13/08.**
3. **Escenario sustituido.** Pide suite de preparación con mármol negro y velas; entrega **baño con tina negra y grifería dorada + estante con fustas y una bola-mordaza roja**. El mármol quedó, el resto es invención.

### 🔴 Side Profile — la peor de la flota reciente

No es deriva, es **un look distinto**. Ocho violaciones simultáneas:

| # | Prompt pide | Imagen entrega |
|---|---|---|
| 1 | Top wet-satin blanco triangular | **Sujetador de PVC blanco con ribete ROJO** |
| 2 | Delantal de encaje transparente | **Minifalda de PVC con bolsillo de cruz roja** |
| 3 | `no stockings, bare legs` | **Medias de red blancas** |
| 4 | Sandalias de acrílico **transparente** | **Plataforma NEGRA** |
| 5 | — | **Cofia de enfermera** agregada |
| 6 | Suite oscura, mármol negro, velas | **Estudio victoriano de madera** con láminas anatómicas |
| 7 | Tatuajes blackwork en brazos | **Brazos completamente limpios** |
| 8 | ADN facial V3.5 | **Cara distinta** — no lee como Ele |

Además rompe regla 04 §1: **medias + puntera abierta**.

**Causa raíz, ya diagnosticada y confirmada:** el Look 801 se escribió **a mano** (`generar_look801.py`) en vez de ensamblarse con `prompt_builder.py`. Sus poses salieron sin `GARMENT_CONSISTENCY`, sin `PHOTOREAL_LOCK` y sin ancla de orientación. Las tres poses que **sí** llegaron bien (Ditzy, POV, Odalisque) son justamente las que se pidieron después, con el texto ya corregido. La lección no es el parche: **todo look nuevo se ensambla con el motor.**

### 🔎 Consistencia entre imágenes del mismo look (lo que pidió la Ama)

- **La cruz roja aparece en UNA sola pose (Seated).** Standing, Ditzy, POV y Odalisque no la tienen, y el BLOQUE B no la nombra nunca. Es un elemento inventado que rompe la Ley de Continuidad.
- **El busto oscila.** Standing/POV lo dan masivo y esférico como pide el ADN (1000cc); Seated y Odalisque lo bajan a un tamaño claramente menor. Deriva de ADN entre poses del mismo look.
- **El pelo oscila** entre cereza profundo (Standing, Ditzy) y rojo más brillante (Back View).
- **El calzado sí aguantó** en 6 de 7 (falla solo Side Profile) — el token de calzado bloqueado está funcionando.

**⏳ Regenerar: Back View · Side Profile.** Seated es opcional (la cruz roja es bonita pero rompe consistencia — decisión de la Ama: o se saca de Seated, o se agrega al BLOQUE B y se regeneran las otras seis).

---

## 🎀 MISS DOLL — Look 25 «Rose Marabou Suite» (7/7)

**BLOQUE B:** bata de chiffon rosa bebé semitransparente y abierta, **cayendo suelta de un hombro**, puños campana anchos con marabú · bralette + g-string de encaje rosa a juego · aros de corazón dorados · mules de plataforma charol rosa pastel 8" · uñas coffin rosa bebé.

### Lo que salió bien (y vale nombrarlo)

- **La corrección de la bata semitransparente de hoy SÍ aterrizó.** El chiffon deja ver la lencería, los puños campana con marabú están en las 7 poses, y el Back View muestra la ropa interior a través de la tela — que era exactamente el problema que diagnosticaste.
- **Standing quedó en contrapposto**, sin la patada que rechazaste. El fix llegó a este look.
- **`BACK_ANCHOR` funcionando:** la bata de frente abierto se ve correctamente cerrada por detrás, no dada vuelta.
- **Sonrisa cálida por diseño:** el negativo de este look tiene retirados `warm smile, laughing` a propósito. El motor lo hizo bien.
- **Aros de corazón, labio rojo espejo, bob platinado sin flequillo:** ADN limpio en las 7.

### 🔴 Las tres fallas

**1. Seated — no está sentada.** El prompt pide *"seated on the front half of the plush pink velvet chaise with the hips and thighs fully down"*. La imagen la muestra **de pie, inclinada**, con las manos en las rodillas y la chaise detrás sin tocarla. `SEAT_ANCHOR` no se cumplió.

**2. Odalisque — en cuatro patas, no sentada en el suelo.** Su Odalisque es *"seated directly down on the floor itself, the hips and the backs of the thighs resting on the ground"* (override propio de Miss Doll). La imagen la muestra **gateando hacia la cámara con las palmas en el piso y la cadera arriba**. Y de paso viola la cláusula de piernas cerradas (*"never spread, never opened apart and never parted at the knee"*) — está con las rodillas separadas.

**3. Side Profile — es una vista frontal.** El prompt exige *"turned so the SIDE of the body reads to the lens, a genuine profile or three-quarter angle"*. El cuerpo está prácticamente de frente. `SIDE_ANCHOR` no pegó.

### 🟡 Y una falla de diseño del prompt, no de Gemini

**El slot 5 (Glacial Command) y el POV son casi la misma foto.** Las dos: retrato waist-up, sonrisa amplia, una mano cerca de la cara, **mirada al lente**.

Lo que debía diferenciarlas es la mirada — el slot 5 lleva el ancla `GAZE_OFF_LENS` y su sub-pose dice *"her gaze drifting off past the edge of the frame **with cold indifference**"*. Pero el look agrega al **final** de los 7 prompts la cláusula de excepción: *"here her usual cold composure softens into a warm, genuine, radiant smile"*.

En el slot 5 esas dos frases se contradicen dentro del mismo prompt, **y la de la sonrisa va última** — es la que ganó. Resultado: la mirada se fue al lente, el slot perdió su único diferenciador y quedó duplicado con POV. Es el mismo síntoma que la Ama levantó el 12/08 sobre Anaïs (*"las imágenes de ditzy salen casi todas iguales"*), pero esta vez **dentro de un mismo look**.

> **Fix propuesto (no aplicado — es decisión de diseño):** que la cláusula de excepción cálida se inyecte en 6 slots y **NO** en el slot 5, o que se reescriba a *"warm smile, gaze still drifting off past the edge of the frame"* para que no pelee con el ancla.

---

## 💪 MISS DOLL — Look 24 «Cutout Circuit» (3/7)

**BLOQUE B:** unitard de vinilo negro de alto brillo con recortes geométricos en cintura y cadera · **ribete rosa fucsia en cada costura** · anilla cromada en el tirador del cierre del esternón · sin corsé · zapatillas-stiletto de plataforma cromada 6" · brillo de sudor · uñas cuadradas fucsia.

### 🔴 El unitard cambia de prenda en las 3 poses

| Pose | Cómo sale el escote |
|---|---|
| Standing | Cierre en V profundo hasta el esternón, con la anilla cromada visible ✅ |
| Back View | **Partido en dos piezas**: crop top + collar alto separado |
| Seated | **Cuello alto tipo tortuga**, cierre subido hasta la garganta, sin anilla |

Tres escotes distintos en tres tomas. `GARMENT_CONSISTENCY` nombra escote, manga, ruedo, corte y color — y aun así derivó. El Back View además viola *"never split into a two-piece"* de forma literal.

### 🔴 Back View y Seated salieron como render 3D, no como fotografía

Piel sin poros, luz de videojuego, superficie plástica. Contra `PHOTOREAL_LOCK` (*"NOT a 3D render, NOT CGI"*) y contra el negativo (`plastic mannequin skin`). **Standing no tiene el problema** — las tres se pidieron con el mismo texto. Es el mismo defecto del Look 08 Standing (13/08): reincidente, y ahora en dos de tres.

### 🔴 El concepto y el BLOQUE B se contradicen

El concepto dice *"la pierna esta vez **no va en leggings**"* y los campos obligatorios repiten *"pierna sin leggings (rotación §5.5)"*. Pero el BLOQUE B pide un **unitard**, que por definición cubre la pierna entera — y eso es exactamente lo que entregaron las tres imágenes. **La regla de rotación de pierna nunca llegó al texto que lee Gemini.** La imagen obedeció; el que falló fue el diseño del look.

### ✅ Lo que sí aguantó

- Ribete fucsia en cada costura, recortes en cintura y cadera, plataforma cromada, sudor: presentes en las 3.
- **Anti-collage aguantó contra un setting hostil:** el escenario pide *"floor-to-ceiling mirrors doubling the room"* y aun así ninguna imagen duplica su figura. `SINGLE_FRAME` está ganándole a un espejo declarado en el propio setting.

---

## 🛠️ Arreglo aplicado en esta sesión

**El repertorio de Standing de Miss Doll tenía 3 de 7 sub-poses con la pierna en el aire** — la rodilla alzada, la patada alta y el tacón subido a una superficie. La Ama rechazó exactamente esa pose el 17/08 en el Look 25; se corrigió **el texto de ese look** y no el repertorio, así que la rotación se la volvió a servir al Look 24, que ya está materializado con la pierna arriba.

Reescritas las 3 en `99_Sistema/scripts/visual/repertorios_pose.json` conservando su silueta distintiva pero con **ambos tacones en el piso**:

- rodilla alzada → peso cargado en una cadera con la rodilla lejana quebrada hacia adentro, el pie abajo
- patada alta → stance ancho y dominante con los pies bien separados y las puntas afuera
- tacón sobre superficie → de pie junto a `{surface}` con una mano apoyada encima

**Verificado:** 7/7 sub-poses sin pierna alzada. Ele (9) y Anaïs (7) ya estaban limpias — era fuga exclusiva de Miss Doll.

---

## 📋 Cola de regeneración recomendada

| Prioridad | Personaje | Pose | Motivo |
|---|---|---|---|
| 🔴 1 | Ele L801 | **Side Profile** | Otro outfit entero + medias + plataforma negra + cara distinta |
| 🔴 2 | Ele L801 | **Back View** | Calzón de talle alto + tatuajes en manos |
| 🔴 3 | Miss Doll L25 | **Odalisque** | Gateando en vez de sentada en el suelo + piernas abiertas |
| 🔴 4 | Miss Doll L24 | **Back View** | Prenda partida en dos piezas + render 3D |
| 🟠 5 | Miss Doll L25 | **Seated** | De pie en vez de sentada |
| 🟠 6 | Miss Doll L24 | **Seated** | Render 3D + cuello alto inventado |
| 🟠 7 | Miss Doll L25 | **Side Profile** | Vista frontal en vez de perfil |
| 🟡 8 | Ele L801 | Seated | Solo si se decide sacar la cruz roja |

**Antes de regenerar el L801:** reensamblar sus 7 prompts con `prompt_builder.py`. Regenerar sobre el texto escrito a mano repite el defecto.

---

## 🧾 Decisiones que son de la Ama

1. **La cruz roja del delantal del L801** — ¿se saca de Seated, o se agrega al BLOQUE B y se regeneran las otras seis?
2. **La cláusula de sonrisa cálida del L25** — ¿se excluye del slot 5 para que recupere su mirada fuera de lente?
3. **El L24 y la pierna** — ¿el unitard se queda como está (y se corrige el concepto), o se rediseña a la prenda de pierna descubierta que decía el concepto?
