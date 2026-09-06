# Banda MD-4 — Miss Doll Looks 82-85
Auditadas 28 imágenes en 4 looks · 06/09/2026

Batch "Deficit de Escenario -- El Club que le Faltaba" (05/09/2026): el más nuevo de la flota, el primero
bajo el tope de familia cromática y el candado de arquitectura, y el primero con el iris **cobalto** ya
en el fence del ADN. Resolución medida en las 28: 669×1200 (Odalisque de L82 y L84: 1200×669), 0,80 MP —
sobre el piso, así que el detalle fino sí se auditó. Fuente de cada cláusula: el prompt de esa pose en
`02_Personajes/01_Principales/miss_doll/GALERIA_OUTFITS_MISS_DOLL.md` (L82 §5025 · L83 §5084 · L84 §5143 ·
L85 §5202).

## Resumen

| Look | Poses | Desvío prompt | Continuidad | 🔴 con ancla | 🟡 sin ancla |
|---|---|---|---|---|---|
| 82 UV Violet Gym Performance | 7/7 | **9,8%** | **63,2%** | 15 | 5 |
| 83 Rosa Shocking y Cristal | 7/7 | **6,1%** | **89,5%** | 4 | 11 |
| 84 Emerald Chrome Stage Bodysuit | 7/7 | **7,7%** | **85,7%** | 11 | 6 |
| 85 Gunmetal Editorial Corsetry | 7/7 | **7,1%** | **86,4%** | 7 | 8 |
| **PROMEDIO** | 28 | **7,7%** | **81,2%** | **37** | **30** |

### Las tres preguntas del encargo, respondidas con el píxel

- **¿Llegó el cobalto al ojo?** Sí, y es la mejor noticia de la banda 🫦. En 15 poses donde el iris se
  resuelve (medias y primeros planos) el azul saturado está en **13**: L82 GC/POV/Odalisque, L83 las
  seis con cara, L84 Standing/Seated, L85 las cinco con cara. El «white walker» no aparece en ninguna de
  las 28. Quedan **dos iris pálidos** — L82 Seated (azul-gris lavado) y L84 POV (gris-azul claro bajo
  párpado caído) — con el ancla `:1.4` puesta, así que van como 🔴. En full-body (Standing/Back/Side) el
  iris mide ~3 px y no es evaluable: se declara, no se cuenta.
- **¿Se cumple el corsé en los cuatro?** No, y **no tiene por qué**: el perfil `miss_doll.md` §5.5 lo
  derogó como obligatorio el 11/08/2026 (*"Corsé — OPCIONAL, no obligatorio"*, con nota de la Ama). Solo
  el L85 lo lleva; L82 (sports bra), L83 (bra top) y L84 (bodysuit halter) muestran el abdomen tonificado
  que el rediseño de cuerpo del mismo día pidió. Lo que sí es hallazgo: **el negativo de los cuatro looks
  lleva `corset, waist cincher, bustier`, incluido el L85 cuyo BLOQUE B ES un corsé.** El positivo ganó
  las 7 veces, pero es un prompt peleándose consigo mismo. ⚠️ El encargo y el CLAUDE.md dicen «corset in
  every look» — eso es deriva del documento, no de las imágenes; el dueño único (§5.5) manda.
- **¿Rosa firma presente en cada uno y en lugar distinto?** Sí en los cuatro, y en cuatro sitios
  distintos: L82 → filo de suela (visible en 5 de 7 poses) · L83 → el outfit entero · L84 → uñas + filo
  de suela · L85 → la tanga (único color saturado del cuadro). **Pero:** ninguno de los cuatro BLOQUE B
  nombra color de labios ni de sombra (§5.5 campo 8, obligatorio). Lo eligió el generador: nude-malva
  (L82), rosa (L83), fucsia (L84), nude-rosado (L85). Y el §2 del perfil todavía dice *"El rosa es firma
  de Ele, NO de Miss Doll"* y *"Ojos gris hielo"* en los rasgos no negociables, con el fence ya en
  cobalto. Tres derivas del perfil que no son culpa del píxel.

---

## Look 82 — UV Violet Gym Performance

- **Desvío:** 9,8% — Standing 9,1% (3/33) · Back 6,7% (2/30) · Seated 8,3% (3/36) · Side 3,0% (1/33) ·
  Glacial Command **20,0%** (5/25) · POV **16,0%** (4/25) · Odalisque 5,6% (2/36)
- **Continuidad:** **63,2%** (12/19) — la peor de la banda
- **Fallas:**
  - 🟡 [B] Back: el prompt pide *"high-waisted leggings moulded to the leg"* y en la misma línea el
    ancla `BOTTOM_CUT_LOCK` exige *"any bottom garment she wears … at the back a single slim strip …
    both seat cheeks fully bare:1.4"* → la imagen obedece al ancla: **las leggings tienen el asiento
    recortado, glúteos completamente desnudos, el vinilo se funde en degradé translúcido en el muslo**.
    No es lotería: el texto pidió dos cosas incompatibles y el peso 1.4 decidió. Es defecto del prompt.
  - 🔴 [B] Seated: *"a flat gunmetal zip at the centre back"* → **cierre al frente**, centrado en la
    pretina. `GARMENT_CONSISTENCY` presente.
  - 🔴 [B] Seated: leggings *"moulded to the leg"* → **recorte geométrico en la cadera derecha** que
    deja piel a la vista. `GARMENT_CONSISTENCY` presente.
  - 🔴 [B] Side Profile: sports bra *"with a high round neckline"* → **escote en V profundo con el
    canalillo abierto** hasta el anillo. Ancla `(neckline … exactly as written:1.4)` presente.
  - 🔴 [B] POV y Odalisque: mismo *"high round neckline"* → **ventana de escote recortada** sobre el
    busto, enmarcada por anillas (POV: dos anillas; Odalisque: una). Ancla presente.
  - 🔴 [B] Odalisque: leggings lisas → **panel translúcido rosado en la ingle/cadera**. Ancla presente.
  - 🔴 [B] Glacial Command: *"wide moulded waistband sitting above the natural waist"* + *"thong …
    beneath the leggings"* → **leggings de tiro bajo con la tanga asomando POR ENCIMA de la pretina**
    (whale tail). Dos cláusulas rotas, ancla presente. POV repite la tanga sobre la pretina.
  - 🔴 [A] Standing y Glacial Command: *"colossal oversized massive chest … spherical … :1.5"* →
    **busto moderado, sin proyección esférica**. En Seated/Side/Odalisque el mismo pecho es colosal.
  - 🔴 [A] Seated: *"richly pigmented deep cobalt blue iris … never pale:1.4"* → **iris azul-gris
    lavado**.
  - 🔴 [A] Glacial Command: *"a real photograph … NOT a 3D render … never the smooth poreless plastic
    surface"* → **render 3D evidente**: piel sin poro, iluminación de motor, cabello de malla.
    `PHOTOREAL_LOCK` presente.
  - 🔴 [E] Glacial Command y POV: *"exactly one hand visible in the frame … no second hand"* →
    **segunda mano con puño visible en el borde inferior** en las dos tomas. `ONE_HAND` presente.
  - 🟡 [E] POV: *"turned back over one bare shoulder toward the lens"* → **de frente, hombros
    cuadrados a cámara**.
  - 🟡 [E] Standing: *"one hand laid flat along the top of the black rubber gym floor and the other
    closed at the waist"* → **ambas manos colgando sueltas**. (La primera mitad de la cláusula es
    imposible de pie: el slot rellenó «apoyo» con el piso — NO VERIFICABLE, declarado.)
  - 🟡 [E] Back: *"both hands resting at the small of her back"* → **manos en las caderas**.
  - 🟡 [D] Standing: *"gunmetal cuffs on both wrists"* → **puños cromo brillante, no gunmetal**.
- **Quiebres de continuidad:**
  - [escote del bra] Standing: high round cerrado → Side: V profunda · POV: ventana con anillas ·
    Odalisque: ventana con anilla · GC: cerrado
  - [pretina] Standing: alta sobre la cintura → GC: tiro bajo con tanga por fuera
  - [cierre] Back: cremallera atrás → Seated: cremallera al frente
  - [recortes en leggings] Standing: lisas → Seated: recorte en cadera · Odalisque: panel en la ingle
  - [tanga] Standing: invisible bajo las leggings → GC y POV: whale tail sobre la pretina
  - [puños] Standing: cromo espejo → Seated/GC: gunmetal oscuro
  - [iris] Seated: azul-gris pálido → GC/POV/Odalisque: cobalto saturado
  - (no cuenta en Eje 2, pero se ve) busto: Standing/GC moderado → Seated/Side/Odalisque colosal
- **Lo que salió BIEN y conviene no romper:** el calzado es impecable en las 5 poses donde se ve —
  plataforma violeta, aguja fina, puntera cerrada, doble pulsera con hebilla y **filo de suela rosa
  legible**; el setting (piso de caucho, rack de mancuernas, tira fría + uplight violeta) está en 7/7;
  choker de cadena y aros pequeños en 7/7. Side Profile es la mejor pose del look (una sola falla).

---

## Look 83 — Rosa Shocking y Cristal, Dos Piezas de Boudoir

- **Desvío:** 6,1% — Standing 2,7% (1/37) · Back 3,1% (1/32) · Seated 7,9% (3/38) · Side Profile
  **0,0%** (0/36) · Glacial Command **0,0%** (0/29) · POV **12,5%** (4/32) · Odalisque **16,2%** (6/37)
- **Continuidad:** **89,5%** (17/19) — la mejor de la banda
- **Fallas:**
  - 🔴 [E] POV: *"a single continuous photograph … NOT a collage, NOT a grid or multi-panel layout …
    nothing inside the scene showing her image a second time"* → **la imagen es un díptico**: panel
    superior con el retrato, panel inferior con un close-up del escote de la misma mujer. Dos cláusulas
    del ancla `SINGLE_FRAME` rotas en una sola toma. Es el hallazgo más grave de la banda: el ancla
    anti-collage está en las 28 y aquí perdió entera.
  - 🔴 [E] POV: *"exactly one hand visible"* → **segunda mano con uñas rosa en la cadera derecha**.
  - 🟡 [A] POV y Odalisque: *"pale cold porcelain white skin, cold undertone"* → **piel bronceada,
    cálida**, en las dos tomas. El negativo lleva `warm natural skin tone`; el positivo no tiene candado.
  - 🔴 [A] Odalisque: *"bold precisely filled brow makeup … sharp clean tapered tail:1.5"* → **dos
    trazos negros angulares flotando sobre la frente**, cejas de máscara, no de maquillaje.
  - 🟡 [A] Odalisque: *"sharp platinum blonde asymmetric angled bob"* → **melena abierta en abanico
    sobre el piso, largo bastante mayor que un bob**.
  - 🟡 [E] Odalisque: el prompt pide a la vez *"full body seen from directly overhead in a dramatic
    zenithal top-down bird's-eye view"* y, dos cláusulas antes, *"shot with a level upright camera, the
    floor at the bottom of the frame and the horizon perfectly level"* → la imagen obedece a la segunda:
    **cámara a ras de piso, ella tumbada con la cabeza hacia el lente (cara invertida) y las piernas
    levantadas verticales cruzadas en los tobillos**. *"legs stacked with one knee broken"* ✗, *"the
    other arm extended above her head"* ✗. El ancla `FLOOR_SEAT_ANCHOR` (nivel) contradice la pose
    cenital: defecto del texto, y se replica en cualquier Odalisque cenital del motor.
  - 🟡 [E] Seated: *"both legs folded together to the same side with the knees and thighs pressed shut
    and the ankles stacked"* → **pierna cruzada sobre la otra, extendida al frente**; *"one forearm laid
    along the top rail and the chin resting on it"* → **mano apoyada en el riel, mentón en alto**.
  - 🟡 [E] Standing: *"the weight rolled onto one stiletto and the hips angled"* → **postura ancha
    simétrica, caderas cuadradas**.
  - 🟡 [C] Back y Seated: *"mirrored silver sole edge"* → **suela rosa** (visible en los tacones de
    Back y en el filo de plataforma de Seated).
- **Quiebres de continuidad:**
  - [arquitectura de tirantes del bra] Standing: arnés doble cruzando sobre las copas → GC: tirantes
    simples al hombro (Seated/Side/POV/Odalisque conservan el arnés)
  - [largo de pelo] Standing–POV: bob al mentón → Odalisque: melena en abanico
- **Lo que salió BIEN y conviene no romper:** Side Profile y Glacial Command con **cero desvío** — el
  bra plunge, la faja con seis ligas, las medias rosa a medio muslo, el collar de cuentas y los aros de
  cristal están idénticos en 7/7; la bomba rosa sin pulsera se mantiene en las 5 poses de cuerpo
  entero. La expresión cálida del arquetipo Girly Girl (excepción única del §2) llegó sin infantilizar
  nada: cero moño, cero corazón, cero Mary Jane.

---

## Look 84 — Emerald Chrome Stage Bodysuit

- **Desvío:** 7,7% — Standing 7,9% (3/38) · Back 3,4% (1/29) · Seated 8,6% (3/35) · Side 5,9% (2/34) ·
  Glacial Command 7,4% (2/27) · POV **14,8%** (4/27) · Odalisque 5,9% (2/34)
- **Continuidad:** **85,7%** (18/21)
- **Fallas:**
  - 🔴 [B] Seated: *"a high halter neckline fastened behind the neck by a mirror-chrome ring"* → **halter
    abierto en V hasta el esternón, canalillo completo a la vista**; el anillo sigue en la garganta pero
    el cuello alto desapareció. Ancla `(neckline … exactly as written:1.4)` presente. En Standing, Back,
    Side, GC, POV y Odalisque el halter está cerrado como se pidió.
  - 🔴 [C] Back, Seated, Side Profile y Odalisque: *"16cm razor-thin chrome needle heel"* → **tacón
    esmeralda / verde oscuro** en las cuatro tomas donde se lee (Standing demasiado pequeño para
    afirmarlo). Ancla `FOOTWEAR_LOCK` (*"the same … material, colour"*) presente.
  - 🔴 [A] Standing, Glacial Command y POV: *"colossal oversized massive chest … :1.5"* → **busto
    pequeño-moderado bajo el halter**, sin esfera ni proyección. Seated y Odalisque sí lo traen colosal.
  - 🔴 [A] POV: *"deep cobalt blue iris … never pale … :1.4"* → **iris gris-azul pálido** bajo párpado
    caído.
  - 🔴 [E] Glacial Command y POV: *"exactly one hand visible"* → **segunda mano con puño en el borde
    inferior derecho** en las dos.
  - 🟡 [E] Standing: *"stopped mid-walk with the front stiletto crossed over the line of the other"* →
    **pies paralelos, sin cruce**; *"the other closed at the waist"* → **ambas manos sueltas**.
  - 🟡 [E] POV: *"lying back with her head tipped toward the camera above her"* → **sentada erguida,
    cámara al frente**.
  - 🟡 [E] Side Profile: *"the front leg extended along the black lacquer runway floor, the toe pointed
    and the knee straight"* → **pie delantero plantado plano**, paso normal.
  - 🟡 [E] Seated: *"the chin tilted down"* → **mentón en alto**.
  - 🟡 [E] Odalisque: *"kneeling tall and upright … thighs and torso held 100% vertical"* → **sentada
    sobre los talones**, muslos plegados.
- **Quiebres de continuidad:**
  - [escote] Standing: halter alto cerrado → Seated: V hasta el esternón
  - [puños] Standing: anchos, cromo espejo → Seated/GC/POV: estrechos, oscuros
  - [iris] Standing/Seated: cobalto → POV: gris-azul pálido
- **Lo que salió BIEN y conviene no romper:** los recortes geométricos de cintura con cadenas, la
  espalda abierta con dos cadenas cruzadas, las medias esmeralda 15 den con liguero de cuatro clips y
  los aros de gota esmeralda están en **7/7 idénticos**; la tanga es tanga en Back y Side; el escenario
  (terciopelo esmeralda, pasarela laqueada, candilejas cromo) en 7/7. El tacón verde está equivocado
  contra el prompt, pero al menos está equivocado **igual** en las cuatro poses.

---

## Look 85 — Gunmetal Editorial Corsetry

- **Desvío:** 7,1% — Standing 5,3% (2/38) · Back 3,3% (1/30) · Seated 8,6% (3/35) · Side 6,7% (2/30) ·
  Glacial Command **12,0%** (3/25) · POV 8,3% (2/24) · Odalisque 5,3% (2/38)
- **Continuidad:** **86,4%** (19/22)
- **Fallas:**
  - 🔴 [B] Standing, Back y Seated: *"a hot pink high-gloss vinyl thong"* + ancla `GLOSS_LOCK`
    (*"absolutely no matte or natural non-reflective fabric"*) → **tanga rosa de satén mate, sin
    especular**. En Side, GC, POV y Odalisque la misma tanga sí brilla como vinilo.
  - 🟡 [B] Standing, Seated, GC y POV: *"architectural with conical moulded cups lifting the bust
    high"* → **copas redondeadas tipo sweetheart**. Solo Odalisque las da apuntadas.
  - 🔴 [A] Seated: *"a real photograph … NOT a 3D render"* → **acabado de render**: piel de plástico
    pulido, cara de motor. `PHOTOREAL_LOCK` presente.
  - 🟡 [A] Side Profile: *"pale cold porcelain white skin"* → **piel bronceada** bajo la luz dura.
  - 🟡 [D] Side Profile: *"chrome cuffs on both wrists"* → **muñecas desnudas** (mano en la nuca, mano
    en la cintura, ninguna con puño).
  - 🔴 [E] Glacial Command: *"her gaze angled off past the camera … never at the lens"* → **mirada
    clavada en el lente**. Ancla `GAZE_AWAY` del slot presente.
  - 🔴 [E] Glacial Command y POV: *"exactly one hand visible"* → **segunda mano en el borde inferior
    derecho** en las dos.
  - 🟡 [E] Odalisque: *"the pelvis pushed forward and the spine arched backward in a dramatic editorial
    camel backbend … the ribcage and bust lifted high toward the ceiling"* → **inclinada hacia
    adelante, busto proyectado hacia el piso**, manos sí en los botines. El backbend se invirtió.
- **Quiebres de continuidad:**
  - [acabado de la tanga] Standing: satén mate → Side/GC/POV/Odalisque: vinilo brillante
  - [copas del corsé] Standing: redondeadas → Odalisque: cónicas
  - [puños] Standing–Seated, GC–Odalisque: cromo en ambas muñecas → Side Profile: ausentes
- **Lo que salió BIEN y conviene no romper:** el corsé gunmetal con busk cromo, canales de varilla
  visibles, panel de lazada atrás y ruedo alto en cadera es **el mismo objeto en 7/7** — la pieza
  central más estable de la banda; medias gunmetal 15 den con cuatro clips en 7/7; **botines** de
  plataforma con filo rosa idénticos en las 5 poses de cuerpo entero (⚠️ el §5.3 del perfil saca los
  ankle boots de la rotación desde el 11/08 — eso es defecto de diseño del look, no del píxel, y no se
  contó en el Eje 1); collar cromo y aros de barra en 6/7; iris cobalto en las 5 con cara.

---

## Patrones de la banda

Lo que se repite, porque eso es lo que arregla el motor y no el caso suelto 💅:

1. **La segunda mano en Glacial Command y POV — 7 de 8 tomas.** El ancla `ONE_HAND` (*"exactly one
   hand visible … the other arm resting down along her body and out of shot"*) está en las 8; falló en
   L82 GC+POV, L83 POV, L84 GC+POV, L85 GC+POV. Patrón exacto: la mano del gesto arriba, la otra
   asoma con puño en el borde inferior. El encuadre pedido (*"waist-up medium shot"*) es demasiado
   largo — con el corte a la cadera la segunda mano entra sola. Reforzar el ancla con el encuadre
   (*"cropped above the hips, the second arm entirely outside the frame"*), no con más negativos.
2. **El escote se reinventa aunque el ancla lo fije — 9 tomas.** L82 bra «high round» → V (Side),
   ventana con anillas (POV, Odalisque); L84 halter alto → V al esternón (Seated); L85 copas cónicas →
   sweetheart (4 poses). El `(neckline … exactly as written:1.4)` está en las 28 y aun así el
   generador abre canalillo donde el prompt dice cerrado. Coincide con la familia L746/L707/L86/L87 de
   la rúbrica: el BLOQUE B describe el escote **una vez** y el ADN empuja en contra con *"dramatic
   alluring plunging neckline, deep prominent cleavage"* — **el BLOQUE A contradice al BLOQUE B en
   todos los looks de cuello alto**. Mientras esa cláusula del ADN viva, un high-neck es una apuesta.
3. **`BOTTOM_CUT_LOCK` se come cualquier prenda que cubra el asiento.** L82 Back: las leggings
   quedaron como chaps. La cláusula *"any bottom garment she wears … both seat cheeks fully bare:1.4"*
   no distingue tanga de legging. Para arquitecturas cubiertas (M8) el ancla debe ir condicionada o
   sacarse del ensamblado — hoy es la única razón por la que ese look tiene 63% de continuidad.
4. **El busto colosal solo aparece cuando la prenda lo deja.** 5 tomas sin esfera (L82 Standing/GC,
   L84 Standing/GC/POV) — todas con cuello alto (sports bra, halter). En bra plunge y corsé (L83, L85)
   el `:1.5` rinde en 12/12. El ADN gana en escote abierto y pierde en cuello cerrado: mismo mecanismo
   que el patrón 2.
5. **El tacón hereda el color del zapato, no del prompt.** L84: «chrome needle heel» → verde en 4/4
   legibles. En L82 («gunmetal needle heel») y L85 («chrome») los tacones oscuros pasan porque el zapato
   ya es oscuro. Cuando tacón y empeine son de colores distintos, hay que nombrarlo como contraste
   explícito (*"a contrasting mirror-chrome heel against the emerald upper"*).
6. **Dos iris pálidos de 15: el cobalto llegó, pero no con párpado caído.** L82 Seated y L84 POV son las
   dos tomas con lashes bajos sobre el ojo. El resto, cobalto franco. El fix del 04/09 funciona; falta
   un refuerzo para la mirada entornada.
7. **Tres tomas de render en 28** (L82 GC, L85 Seated, más el L83 POV que además es collage) con
   `PHOTOREAL_LOCK` puesto. Y **un collage** (L83 POV) con `SINGLE_FRAME` puesto: la única violación
   total de ancla de la banda — una en 28 es 3,6%, pero es la que la Ama tuvo que aceptar porque los
   reintentos anteriores fueron peores (regla 4 de la rúbrica).
8. **Defectos del texto, no del generador (van a la lista de 🟡 y al motor):**
   - Odalisque de L82/L83/L84 pide *"her cold pale steel grey eyes"* — el iris viejo, en contra del
     fence y del propio negativo (`steel grey iris`). Es la plantilla del slot, no el look. L85 ya no
     lo trae. Y las tres hablan de *"stiletto boot"* cuando el look calza trainers/pumps.
   - El negativo de los cuatro lleva `corset, waist cincher, bustier` — con el L85 vestido de corsé.
   - L85 arrastra el ancla de Ele: *"the navel piercing and the hip rune tattoos stay concealed"* en una
     muñeca sin tatuajes (negativo: `tattoos`).
   - L83 Odalisque: `FLOOR_SEAT_ANCHOR` (*"level upright camera"*) contra pose cenital — irresoluble.
   - L82 Standing: *"one hand laid flat along the top of the black rubber gym floor"* — el slot rellenó
     «superficie de apoyo» con el piso.
   - Ningún BLOQUE B de la banda fija color de labios ni sombra (§5.5 campo 8).
9. **La piel bronceada aparece en 3 tomas** (L83 POV/Odalisque, L85 Side) — siempre con luz cálida o
   dura. *"pale cold porcelain white"* no lleva peso; el negativo `warm natural skin tone` no alcanza.

**Lo que esta banda demuestra a favor del motor nuevo:** setting 28/28, calzado con plataforma 20/20
legibles, medias del color y largo pedidos 20/20, accesorios de cuello 26/27, rosa firma en 4/4 y en
cuatro sitios distintos, tanga donde se ve el asiento 5/5. El 7,7% de desvío es bajo; casi todo lo que
falla cae en tres candados que ya existen y no muerden: `ONE_HAND`, el escote contra el ADN, y
`BOTTOM_CUT_LOCK` sobre prenda cubierta.
