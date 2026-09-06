# Auditoría Visual — las tres muñecas, últimos 10 looks · 06/09/2026

**Encargo de la Ama:** *"auditoría visual, últimos 10 outfits para cada muñeca. 1.- consistencia imagen prompt, quiero saber qué tan desviados estamos 2.- consistencia imagen dentro del outfit, distintas poses, quiero saber si hay cambios de escote, maquillaje, largo falda, tacones etc."* · *"que sea auditor externo, no tú porque sueles equivocarte cuando te auto auditas"*

**Alcance:** 30 looks · **174 PNG** · Ele L817-L827 (65) · Miss Doll L75-L85 (45) · Anaïs L76-L85 (64).
**Piso de auditabilidad:** las 174 a **0.80 MP** (669×1200 / 1200×669). Ninguna cae bajo el piso de 0,3 MP — los veredictos son defecto-real, nunca "no se ve".

**Metodología.** Dos pasadas independientes que no se hablaron entre sí:
1. **Mecánica** (Pillow + numpy, sin visión): resolución, orientación por slot, MD5, hash perceptual, divergencia cromática entre poses del mismo look.
2. **Seis auditores externos ciegos**, 5 looks cada uno. No recibieron la pasada mecánica ni los perfiles de personaje: solo el **BLOQUE B** del look (la verdad de referencia) y el **delta** de cada pose contra el texto común a las 7 — recorte de ~85% del prompt, que es 85% boilerplate idéntico.

---

## 1. Resultado global

| | Looks | OK | MENOR | GRAVE | Fidelidad media (Eje A) |
|---|---:|---:|---:|---:|---:|
| Ele | 10 | 0 | 4 | 6 | **6,1 / 10** |
| Miss Doll | 10 | 0 | 4 | 6 | **5,3 / 10** |
| Anaïs | 10 | 0 | 4 | 6 | **6,1 / 10** |
| **Total** | **30** | **0** | **12** | **18** | **5,8 / 10** |

**Cero looks limpios de 30.** La respuesta a *"qué tan desviados estamos"* es: **la imagen cumple el prompt un 58%**, y el 60% de los looks tiene al menos un defecto grave.

| Muñeca | Peor | Mejor |
|---|---|---|
| Ele | L823 (4/10) · L826 (5/10) · L819 (5/10) | L822 (8/10) |
| Miss Doll | L81 (4/10) · L82 (4/10) · L83 (5/10) | L79, L84 (6/10) |
| Anaïs | L77, L79, L83 (5/10) | L81, L82, L84 (7/10) |

---

## 2. Patrones transversales — los que aparecen en las TRES muñecas

Son los que importan: si el defecto cruza los tres personajes, es del **motor**, no del look.

### P1 · Los slots de plano cerrado colapsan el encuadre y además mutan la prenda

Ditzy · POV · Sovereign Gaze · Glacial Command. Piden rostro dominante y **exactamente una mano**; devuelven cuerpo entero con las dos manos.

- Ele: POV de L823 (plano entero de pie) y de L827 (medio muslo); Ditzy de L827 mete la segunda mano.
- Miss Doll: la cláusula de una mano falló **4 de 8 veces** (L84 y L85, glacial + pov); POV de L75 y L79 en cuerpo entero.
- Anaïs: L76 mete la segunda mano en **ambos** slots; L79 en POV.

Y no es solo encuadre: **la prenda de arriba se reinventa justo ahí.** L820 POV saca el busto fuera de la copa; L821 Ditzy le pone tirante a un bandeau declarado strapless; L819 cambia la construcción de las copas en Ditzy y POV; en Miss Doll el volumen de busto en glacial/pov es mayor que en cuerpo entero **en 4 de 4 looks multipose**. Sin cuerpo entero que ancle la construcción, el generador la inventa.

### P2 · Del calzado sobreviven el tipo y el color; la arquitectura no

El canon del taco alto se respeta casi siempre. Lo que se pierde es lo **declarado**: número de tiras, plataforma, puntera, altura de caña, material del tacón.

- Ele: L826 entrega **tres zapatos distintos**; L820 alterna bota de muslo y bota a la rodilla; L818 Standing sin tira y Back View con tira.
- Miss Doll: L75 alterna puntera cerrada y abierta más dos alturas de plataforma; la **plataforma de 6"** casi nunca se imprime (L76, L79, L75) y en L77 falla al revés — está el plato y el aguja se vuelve bloque.
- Anaïs: plataforma donde se declaró "no platform" (L81 Seated), d'Orsay que sale pump cerrado (L82), Mary Jane que pierde la tira.

El bloque *"the footwear clearly visible and exactly as described above"* está **literal en las cinco poses de cuerpo entero** de cada look y no sostiene ni la plataforma ni la altura de caña.

### P3 · Los accesorios se pierden, se duplican o se inventan

El campo de accesorios del BLOQUE B se está leyendo como sugerencia, no como inventario cerrado.

- Ele: L820 Ditzy sin gargantilla; L821 Ditzy con **dos** puños en vez de uno; el anillo de L822 se muda de la garganta al esternón y el de L826 del pecho a la cadera.
- Miss Doll: el **collar declarado desaparece en 3 de 5** (L76 y L77 salen con la garganta desnuda; L78 lo degrada de posture collar a choker); L75 declara un puño y entrega dos; **L78 no declara ninguno y entrega dos**, en un rosa ajeno a la paleta del look.
- Anaïs: L83 declara `bare hands, no gloves` y lleva **guantes negros en las 7**; L84 suma perlas que nadie pidió; L85 declara guantes y Standing los pierde. Bidireccional: rellena con vocabulario vintage genérico y descarta lo declarado.

### P4 · La Odalisque es la pose descarriada

Es la única 16:9 del set y arrastra deriva propia.

- Ele: pelo más claro y anaranjado en L817, L819, L821; tanga que desaparece (L819); medias lisas que salen estampadas (L825); sandalia cerrada que sale abierta (L826).
- Miss Doll: **cuatro odalisques en vertical** (L75, L79, L83, L85) cuando el slot exige apaisada; L85 llega **descalza con el botín en la mano**.
- Anaïs: en L76, L78 y L79 el prompt pedía tres puestas distintas y **salieron las tres iguales** — hay una odalisca por defecto.

### P5 · La instrucción de pose se aplana cuando pide una acción concreta

La marcha, el cruce de piernas, el recline con tobillos cruzados, los codos sobre las rodillas: todo se resuelve como "de pie/sentada neutro".

- Ele: 6 fallos de pose en 5 looks, todos de este tipo.
- Miss Doll: L75 Seated abre las rodillas contra una cláusula de piernas cerradas que está literal en su propio delta.
- Anaïs: **"sentada" falla incluso con peso `:1.4`** — L79 salió de pie apoyada en el escritorio pese al `(genuinely sitting down… never standing up:1.4)`. El refuerzo numérico no está comprando nada en este eje.

### P6 · La identidad del cuerpo no se sostiene dentro de un mismo look

Con implantes fijos declarados desde L185, esto debería ser invariante.

- Ele: volumen de busto distinto entre poses en L823, L825, L826, L827.
- Miss Doll: **L79 parece dos mujeres distintas** — Standing/Seated/Side Profile con piel bronceada dorada; Back View/Glacial/POV/Odalisque en porcelana pálida, con cambio simultáneo de volumen de busto.
- Anaïs: **el pelo es su elemento menos estable** — el largo salta de hombro a cadera entre poses en L77, L78 y L79; L80 Back View inventa una coleta alta.

### P7 · El escote es el campo de prenda más inestable del lote

- Miss Doll: L82 pasa de cuello redondo alto a plunge con keyhole en 4 de 7; **L83 entrega cinco arquitecturas distintas de sujetador**; L85 desborda la copa en los planos medios.
- Anaïs: **el strapless se vuelve con tirantes** — L81 y L84 declaran corsetería strapless y en ambos exactamente dos poses sacan un tirante al hombro.
- Ele: L817 lee banda envolvente en Side Profile contra dos triángulos con anilla en el resto.

---

## 3. Defectos de PROMPT, no del generador — estos son míos

| Hallazgo | Evidencia | Alcance medido |
|---|---|---|
| El delta de POV nombra prendas que el BLOQUE B nunca declaró | Anaïs: `the strand of pearls` (L77), `the ring turned to the light` (L78 — de ahí el solitario que aparece en una sola pose), `the clasp of the fur at her throat` (L80, donde **no hay piel en el outfit**) | El delta de POV es texto genérico reutilizado y contamina el outfit |
| Ancla de costura de media pegada a un look sin medias | `miss_doll L77`: BLOQUE B dice `bare legs, no stockings` y los prompts traen `the stockings have ONE single seam…` | **1 de 798** looks con BLOQUE B. Es un caso aislado, no sistémico |
| Costura de media al FRENTE | `miss_doll L78` Standing: la costura corre por la espinilla, visible de frente | El ancla `STOCKING_SEAM_FRONT` existe desde el 11/07 y aquí no mordió |

---

## 4. Entregas rotas que ningún control detecta

**Poses que figuran materializadas y no existen:**

| Look | Hecho | Efecto |
|---|---|---|
| `ele L819` | `side_profile.png` es **copia byte a byte** de `seated.png` (md5 `563d79d8…`) | tracker dice 7/7 · **6 poses reales** |
| `anais L83` | `seated.png` == `side_profile.png` byte a byte (md5 `49f149bb…`) | tracker dice 7/7 · **6 poses reales** |
| `ele L823` | `side_profile` vs `standing`: **NO** son byte-idénticos (md5 distintos), pero difieren en **0,1% de los píxeles con diferencia máxima de 5/255** — es el mismo frame reencodeado | tracker dice 7/7 · la pose Side Profile no se generó |
| `miss_doll L83` | `pov` es un **collage de dos paneles apilados** con costura visible | el ancla anti-collage no mordió |
| `miss_doll L75, L79, L83, L85` | odalisque en **vertical** cuando el slot exige 16:9 | 4 de 10 looks |

**El tracker miente hacia arriba en 3 looks.** Un `md5` en `sync_imagenes_subidas.py` habría cazado los dos primeros; un chequeo de orientación por slot, los cuatro de Miss Doll. Los dos son baratos.

---

## 5. Cruce auditor ↔ máquina (validación mutua)

Los auditores fueron a ciegas. Coincidencias independientes:

- El par byte-idéntico de `ele L819` lo encontraron **la máquina y el auditor por separado**. Ídem `anais L83`. Dato firme.
- Los tres looks que la pasada mecánica marcó con peor divergencia cromática entre poses — `miss_doll L79` (0,50), `ele L817` (0,49), `ele L827` (0,46) — recibieron los tres hallazgos de mutación de prenda o de identidad corporal. **La métrica cromática sirve como pre-filtro barato.**
- **Una corrección al auditor:** `ele_2` reportó `ele_823_side_profile` como "idéntico" a `standing`. Medido, no lo es a nivel de bytes (md5 distintos). Es el mismo frame con ruido imperceptible. La conclusión operativa no cambia; el dato sí se corrige.

---

## 6. Qué se arregla, y dónde

**Barato y mecánico (se puede hoy):**

1. `md5` duplicado por look en `sync_imagenes_subidas.py` → el tracker deja de mentir hacia arriba.
2. Chequeo de orientación por slot (odalisque = apaisada) en el mismo sync.
3. Limpiar el delta genérico de POV: hoy nombra perlas, anillos y pieles que el BLOQUE B no declara.
4. Divergencia cromática intra-look como pre-filtro: barata, y apuntó a los tres peores sin ver una prenda.

**Requiere decisión de la Ama (cambia el prompt, no el código):**

5. Los slots de plano cerrado necesitan **eco de prenda** igual que el `footwear_echo` que ya existe — hoy la construcción del busto viaja solo en el BLOQUE B y se pierde cuando no hay cuerpo entero.
6. El eco de calzado existe y **no sostiene la arquitectura**: la plataforma, la puntera y la altura de caña se pierden igual. Hay que medir si el eco está llegando a las poses donde falla.
7. Las instrucciones de pose con acción concreta (marcha, cruce, recline) no se cumplen ni con peso `:1.4`. O se simplifican, o se acepta que el set de poses dinámicas no es materializable con este generador.

---

## Anexo — informes de los seis auditores externos

---

## Auditor `ele_1`

### ele L817 — 7 poses leídas
**A fidelidad: 7/10**
- Standing: piernas cruzadas a la rodilla en X-stance de modelo → piernas paralelas, pies separados, sin cruce; y la mano que debía ir "on the opposite hip" cae sobre el muslo.
- Seated: "the knees together" → rodillas muy abiertas, piernas separadas en ángulo amplio.
- Back View: tanga con "a single slim strip at the back leaving the seat uncovered" → panel triangular de leopardo que cubre la parte alta del glúteo, no una tira.
- Standing / Back View / Odalisque: sandalia con "two clear acrylic ankle straps with chrome buckles" → una sola tira de tobillo con hebilla, más una banda de empeine.
**B consistencia:**
- B1 escote: ⚠️ Side Profile — el top lee como banda envolvente bajo el busto (banda horizontal de leopardo bajo el pecho), no como los dos triángulos con anilla cromada central que se ven en Standing / Seated / Ditzy / POV / Odalisque.
- B2 maquillaje: ⚠️ Seated — volumen de labio notoriamente mayor y rosa más saturado que en Standing y Ditzy; delineado más pesado en Back View que en Standing. Sombra y cejas consistentes.
- B3 largo inferior: ⚠️ Side Profile — cintura ancha de leopardo alrededor de la cadera, contra "a thin waistband" delgado visible en Standing, Seated y Odalisque; el panel frontal también lee más ancho en Seated que en Standing.
- B4 calzado: ⚠️ es siempre sandalia de plataforma en acrílico transparente, pero la arquitectura de tiras cambia: banda ancha de empeine tipo mule en Seated contra tira fina + tobillera en Standing / Back View / Side Profile.
- B5 medias/guantes: ✅ piernas desnudas y manos desnudas en las 7.
- B6 accesorios/uñas: ✅ cadena corporal cromada cruzando el torso presente en las 7; uñas XXXL francesas blancas en todas; piercing de ombligo visible donde el encuadre lo permite.
- B7 pelo: ⚠️ Odalisque — rojo notoriamente más vivo y claro; Standing y Side Profile son burdeos oscuro. Largo consistente donde es medible.
**VEREDICTO: MENOR**

### ele L818 — 2 poses leídas (de 7 declaradas; faltan Seated, Side Profile, Ditzy, POV, Odalisque)
**A fidelidad: 7/10**
- Standing: bota declarada como pump con "a single thin jade ankle strap fastened with a chrome pin buckle" → pump liso sin ninguna tira de tobillo.
- Standing: "a high funnel neckline closed at the front by a mirror-chrome zip pull resting at the sternum" → el cierre cromado frontal recorre el torso completo hasta la entrepierna, no se detiene en el esternón.
- Standing: "full body from a low hero angle" → cámara a la altura del pecho, encuadre frontal plano sin contrapicado.
- Back View: "the weight on one stiletto with the other foot pigeon-toed inward" → ambos pies apoyados y casi paralelos, sin el pie girado hacia dentro.
**B consistencia:**
- B1 escote: ✅ cuello embudo cerrado y cremallera frontal idénticos en ambas; espalda con cierre cromado a lo largo de la columna hasta el coxis, correcto.
- B2 maquillaje: ✅ ahumado gris-verde con delineado alado y labio rosa fuerte glossy idéntico en las dos.
- B3 largo inferior: ✅ catsuit hasta el tobillo, sin corte de pierna, en ambas.
- B4 calzado: ⚠️ Standing lleva pump verde sin tira; Back View lleva el mismo pump CON tira de tobillo y hebilla. No es el mismo zapato.
- B5 medias/guantes: ✅ sin medias (el catsuit cubre) y manos desnudas en ambas.
- B6 accesorios/uñas: ✅ gargantilla cromada lisa y uñas XXXL francesas blancas en las dos.
- B7 pelo: ✅ cereza oscuro, mismo largo y misma ondulación.
**VEREDICTO: MENOR**

### ele L819 — 6 poses distintas (7 archivos: `side_profile` es copia byte a byte de `seated`, md5 563d79d884d8079e2d566679726ed880)
**A fidelidad: 5/10**
- Side Profile: pose de perfil de cuerpo entero de pie con S-curve → el archivo es el mismo píxel a píxel que Seated (mujer sentada en el suelo). La pose no existe: nunca se generó.
- Back View: "caught mid-stride walking away from the camera with one stiletto lifting and the hips swinging" → de pie, ambos pies en el suelo, piernas juntas, sin zancada.
- Seated: "perched on a black slate pool ledge with one leg crossed over the other and the top stiletto pointed" → sentada directamente sobre el suelo de pizarra con las piernas dobladas y ninguna cruzada sobre la otra.
- Odalisque: tanga de dos triángulos esmeralda con cordones anudados a cada cadera → el panel frontal esmeralda no es legible; solo se ven cordones plateados sueltos colgando, uno de ellos desatado.
**B consistencia:**
- B1 escote: ⚠️ Ditzy y POV — las copas tienen el borde inferior fruncido/plisado y sin el ribete plateado, y se montan más arriba dejando underboob; en Standing, Back View y Seated el triángulo es liso con piping plateado en el borde.
- B2 maquillaje: ⚠️ el labio pasa de rosa-frambuesa en Standing a coral anaranjado en Ditzy, POV y Odalisque. Sombra verde-teal y cejas consistentes en las 6.
- B3 largo inferior: ⚠️ Standing y Seated muestran lazos plateados de amarre en cada cadera; Back View muestra una tanga de panel verde continuo sin lazos visibles; Odalisque no muestra panel alguno.
- B4 calzado: ⚠️ siempre sandalia verde con plataforma transparente y tacón aguja cromado, pero el número de tiras cambia: Seated lleva un entramado cruzado de varias tiras verdes, Standing lleva tobillera simple con hebilla más una banda de empeine.
- B5 medias/guantes: ✅ piernas desnudas y manos desnudas en las 6.
- B6 accesorios/uñas: ✅ cadena corporal plateada nuca-cintura presente en las 6, uñas XXXL francesas blancas, piercing de ombligo visible. (Los piercings de pezón declarados "visible on bare skin" no se ven en ninguna: quedan cubiertos por las copas.)
- B7 pelo: ⚠️ Odalisque — rojo más claro y anaranjado que el cereza oscuro de Standing, Ditzy y POV. Largo consistente.
**VEREDICTO: GRAVE**

### ele L820 — 7 poses leídas
**A fidelidad: 6/10**
- Seated: botas "thigh-high" declaradas → la bota termina justo bajo la rodilla, con una franja larga de media gris expuesta sobre la caña. Lo mismo en Odalisque.
- Seated: "both elbows planted firmly on top of both knees", torso inclinado bruscamente hacia adelante y "the stilettos crossed at the ankle" → torso erguido y echado atrás, una pierna cruzada sobre la otra a la rodilla, ningún codo sobre las rodillas, tobillos sin cruzar.
- Todas las poses con pierna visible: medias "with a fine dark seam up the back of each leg" → medias grises lisas, sin costura trasera en ninguna, incluida la Back View que es donde se vería.
- POV: corsé "overbust" con copa cónica moldeada → el borde superior cae bajo los pezones y el busto queda descubierto con los piercings a la vista; en Standing, Ditzy y Side Profile el mismo corsé sí contiene el pecho.
**B consistencia:**
- B1 escote: ⚠️ POV y Odalisque llevan el borde del corsé muy por debajo del que se ve en Standing, Ditzy, Seated y Side Profile; en POV el pecho queda fuera de la copa. No es la misma línea de busto.
- B2 maquillaje: ✅ ahumado gris-azulado con delineado alado y labio rosa chicle glossy consistente en las 7.
- B3 largo inferior: ✅ g-string índigo con liguero de cuatro tiras y borde del corsé en punta sobre la cadera, igual en todas las poses donde se ve.
- B4 calzado: ⚠️ Standing, Back View, Side Profile llevan bota alta de muslo; Seated y Odalisque llevan bota que termina en la rodilla. Cambia el largo de caña dentro del mismo look. Además el cierre cromado aparece en la caña frontal en Seated y en la cara interna en Standing.
- B5 medias/guantes: ⚠️ medias grises ahumadas presentes y sin guantes en todas — correcto —, pero ninguna lleva la costura trasera declarada, y en Seated y Odalisque la media queda expuesta muy por encima de la bota, contra el resto donde la caña la tapa casi entera.
- B6 accesorios/uñas: ⚠️ Ditzy — no lleva la gargantilla cromada con anilla O; el cuello aparece desnudo. En Standing, Seated, Side Profile, POV y Odalisque la gargantilla está presente. Uñas XXXL francesas blancas consistentes.
- B7 pelo: ⚠️ POV lee más liso y con raya al medio, contra la onda marcada de Standing y Ditzy; el tono cereza es consistente en las 7.
**VEREDICTO: GRAVE**

### ele L821 — 7 poses leídas
**A fidelidad: 6/10**
- Ditzy: bandeau declarado sin tirantes, "held by a thin black elastic strap across the upper back" → hay un tirante negro fino sobre el hombro izquierdo, visible de frente.
- Standing: "caught mid-stride walking straight toward the camera with one stiletto forward and the back foot lifting off the floor" → de pie, ambos pies apoyados y casi juntos, sin zancada.
- Seated: "reclined back on a low black glass banquette propped on one elbow... the legs extended with the stilettos crossed at the ankle" → sentada sobre la baranda de vidrio con las rodillas dobladas y separadas, pies en el suelo, tobillos sin cruzar y sin recline.
- POV: retrato con "the face dominant in the upper-middle of the frame" y ángulo bajo → encuadre de tres cuartos de cuerpo hasta la caña de las botas; el rostro ocupa una fracción menor del cuadro y la cámara está a la altura del pecho.
**B consistencia:**
- B1 escote: ⚠️ Ditzy añade un tirante de hombro al bandeau que en Standing, Seated, Side Profile, Back View, POV y Odalisque es estrictamente sin tirantes.
- B2 maquillaje: ⚠️ Odalisque — el labio lee plano y más rojo-coral, sin el gloss rosa que llevan Standing, Seated, Ditzy y POV; la sombra teal también es más plana.
- B3 largo inferior: ⚠️ Ditzy — la falda se asienta más arriba en la cintura y no deja ver los cordones cian de la tanga sobre las crestas ilíacas, que sí aparecen en Standing, Back View, POV y Odalisque.
- B4 calzado: ⚠️ Back View — la bota no muestra el acordonado cian y la suela/tacón leen gruesos, tipo bloque, contra el tacón aguja fino y la caña acordonada con cordón cian de Seated, Side Profile, POV y Odalisque. En Standing el tacón no es legible.
- B5 medias/guantes: ✅ muslos desnudos sobre la bota y manos desnudas en las 7.
- B6 accesorios/uñas: ⚠️ Ditzy lleva DOS puños cian de vinilo, uno en cada muñeca; el resto de las poses lleva uno solo. Gargantilla cromada presente en las 7; uñas XXXL francesas blancas consistentes.
- B7 pelo: ⚠️ Back View — la masa de pelo recogida lee a la altura de la nuca, tipo melena corta, no cadera; Odalisque lee rojo más vivo y anaranjado que el cereza oscuro del resto.
**VEREDICTO: GRAVE**

## PATRONES

- **La pose pedida se ignora cuando es dinámica o compleja.** Cinco de los seis fallos de pose del lote son del mismo tipo: la marcha (L819 Back View, L821 Standing), el cruce de piernas (L817 Standing, L819 Seated), el recline con tobillos cruzados (L821 Seated) y los codos sobre las rodillas (L820 Seated) se resuelven todos como un "de pie/sentada neutro". Cuanto más específica es la instrucción corporal, más probable es que el modelo la aplane.
- **La Odalisque es la pose que más se sale del look.** En L817, L819 y L821 el pelo lee más claro y anaranjado que en el resto; en L819 la tanga desaparece; en L820 la bota cambia de largo; en L821 el labio pierde el gloss. Es la única pose 16:9 del set y arrastra su propia deriva de render.
- **Ditzy y POV son donde muta la prenda superior.** L819 (copas fruncidas sin piping en Ditzy y POV), L820 (POV con el busto fuera de la copa), L821 (Ditzy con tirante sobre una prenda declarada strapless). Los planos cerrados de busto son los que el modelo reinventa: no hay cuerpo entero que ancle la construcción.
- **El calzado conserva el tipo pero pierde la arquitectura de tiras y el largo de caña.** L817 (una tobillera en vez de dos, banda de empeine cambiada en Seated), L818 (Standing sin tira, Back View con tira), L819 (entramado cruzado en Seated vs tobillera simple en Standing), L820 (muslo vs rodilla), L821 (Back View sin acordonado y con suela gruesa). El canon de tacón alto se respeta siempre; el detalle declarado del zapato, nunca del todo.
- **Los accesorios declarados como únicos y permanentes se pierden o se duplican en un plano.** L820 Ditzy sin la gargantilla con anilla O; L821 Ditzy con dos puños en vez de uno. En ambos casos ocurre justamente en la Ditzy.
- **Hay entrega incompleta que ningún control detecta.** L819 tiene siete archivos pero seis imágenes: `side_profile` es copia byte a byte de `seated` (md5 idéntico), así que la pose se registró como materializada sin existir. L818 solo tiene 2 de 7 poses. Un chequeo de md5 duplicados y de conteo por look es barato y aquí habría cazado las dos cosas.

---

## Auditor `ele_2`

### ele L822 — 7 poses leídas
**A fidelidad: 8/10**
- Seated: el anillo rose-gold debe cerrar el halter detrás/en el cuello → el anillo aparece abajo, en la base del escote entre los pechos, y la unión del cuello queda sin anillo
- Ditzy: choker de cadena rose-gold declarado → no hay cadena en el cuello, solo la tira violeta del halter; aros tampoco legibles
- Standing: liguero de cuatro tiras finas → solo se lee una tira por pierna (dos en total)
- Side Profile: mismo busto que el resto del look → el volumen del busto salta a un tamaño claramente mayor que en Standing/Ditzy
**B consistencia:**
- B1 escote: ⚠️ Side Profile con busto notablemente más voluminoso y alto; Seated cambia la línea del escote al bajar el anillo a la base de la V
- B2 maquillaje: ⚠️ Ditzy con sombra mauve suave sin el delineado alado ni el morado saturado de Standing/Seated/POV; labio más pálido
- B3 largo inferior: ✅ leg line alta y trasero tanga idénticos en las siete
- B4 calzado: ✅ mismo slingback violeta patente, punta cerrada, tacón aguja rose-gold sin plataforma, canto de suela dorado
- B5 medias/guantes: ⚠️ medias violetas y manos desnudas consistentes, pero el número de tiras del liguero varía (1 por pierna en Standing vs 2 por pierna en Ditzy/Odalisque)
- B6 accesorios/uñas: ⚠️ Ditzy sin choker de cadena; el anillo rose-gold migra de la garganta (Standing/POV/Side Profile) al esternón (Seated). Uñas french XXXL estables
- B7 pelo: ✅ cereza oscuro hasta la cadera en todas
**VEREDICTO: MENOR**

### ele L823 — 7 poses leídas
**A fidelidad: 4/10**
- Side Profile: perfil real de flanco, de puntillas, un brazo en alto y la otra mano en la cadera → la imagen es un DUPLICADO EXACTO de Standing (vista frontal, ambos brazos sobre la cabeza, misma sombra, mismo pliegue del vestido). La pose no existe
- POV: retrato boudoir reclinado, cara dominante en el tercio superior, mirada clavada en el lente → plano entero de pie, cara pequeña, cuerpo completo, mirada hacia arriba fuera del lente
- Back View: cabeza echada hacia atrás con el pelo velando la cara girada → cabeza simplemente de espaldas, sin echar atrás y sin cara girada
- Odalisque: hombros y caderas apoyados en la superficie, tumbada de lado → torso incorporado y apuntalado sobre un brazo, hombros muy despegados del suelo
**B consistencia:**
- B1 escote: ⚠️ cuello embudo correcto en todas, pero el volumen del busto cambia: discreto en Standing/Side Profile/POV, marcadamente pronunciado en Ditzy y Seated
- B2 maquillaje: ✅ ahumado gris-verdoso con delineado alado y labio rosa fuerte estable en las siete
- B3 largo inferior: ✅ dobladillo bajo la rodilla y abertura trasera hasta la rodilla consistentes
- B4 calzado: ✅ mismo pump oxblood patente, punta cerrada, tira de tobillo con hebilla, tacón aguja cromado, canto de suela cromado en todas
- B5 medias/guantes: ✅ piernas desnudas y manos desnudas en todas
- B6 accesorios/uñas: ⚠️ el collar cromado se lee como banda negra en Standing/Side Profile y como cromo espejo en Seated/Ditzy/POV; no legible en Odalisque. Aros no legibles pese a declararse "sin más joyería". Uñas french estables
- B7 pelo: ✅ largo y tono burdeos-cereza consistentes (Ditzy solo más iluminado)
**VEREDICTO: GRAVE**

### ele L825 — 7 poses leídas
**A fidelidad: 6/10**
- Odalisque: medias tangerina lisas 15 den → las medias salen ESTAMPADAS en pitón, con el mismo dibujo de escamas del conjunto: es otra prenda
- Ditzy: mirada perdida fuera del cuadro, ojos desenfocados, nunca al lente → mira directo al lente con foco pleno
- Standing/Back View: medias sheer 15 denier → medias completamente opacas, no se ve piel a través
- Standing/Odalisque: collar cromado slim → aparece un collar de eslabones grueso, mientras Seated y POV llevan una banda cromada lisa y fina
**B consistencia:**
- B1 escote: ⚠️ busto moderado en Standing vs mucho mayor y más redondo en Ditzy, POV y Odalisque
- B2 maquillaje: ⚠️ cejas muy oscuras y de trazo duro en Ditzy/POV frente al trazo más suave de Standing/Seated; el labio pasa de rosa suave (Standing) a rosa fuerte con brillo (Ditzy/POV)
- B3 largo inferior: ✅ tanga y cinturón portaligas en la misma posición en todas
- B4 calzado: ⚠️ la caña del botín es corta sobre el tobillo en Standing/Side Profile pero claramente más alta en Seated; puntera con casquete plateado visible en Standing/Back View y puntera tangerina lisa en Seated
- B5 medias/guantes: ⚠️ Odalisque con medias estampadas en pitón contra medias lisas en las otras seis; manos desnudas ✅
- B6 accesorios/uñas: ⚠️ el collar cambia de diseño (eslabones en Standing/Odalisque, banda plana en Seated/POV, torque redondo en Ditzy). Aros de aro cromados y uñas french estables
- B7 pelo: ⚠️ cereza oscuro en Standing/Back View frente a un cereza más claro y luminoso con raíz oscura en Ditzy/POV
**VEREDICTO: GRAVE**

### ele L826 — 7 poses leídas
**A fidelidad: 5/10**
- Odalisque: sandalia de punta CERRADA → sandalia abierta, con los dedos del pie a la vista
- Back View: plataforma de 6 pulgadas + tacón de 16cm → el zapato no tiene plataforma alguna, suela plana y fina con tacón aguja
- Seated/Side Profile: punta cerrada afilada → la puntera se lee redondeada/almendrada con ribete cromado, no afilada
- Ditzy: anillo cromado único al centro del frente del slip → hay anillo al pecho del slip Y otro en la copa de la bralette, y el volumen del busto cae muy por debajo del de Standing/Seated
**B consistencia:**
- B1 escote: ⚠️ Ditzy con busto marcadamente más pequeño y plano que el escote pronunciado de Standing/Seated/Odalisque; el rostro además se lee menos bimbificado
- B2 maquillaje: ⚠️ cejas mucho más oscuras y cuadradas en Ditzy/POV; el labio pasa de rosa profundo (Standing/Odalisque) a rosa coral brillante (Ditzy/POV)
- B3 largo inferior: ✅ dobladillo a medio muslo estable; tanga de vinilo visible bajo la malla en todas
- B4 calzado: ⚠️ tres zapatos distintos en un mismo look: plataforma con punta cerrada (Standing/Side Profile/Seated), sin plataforma (Back View), punta abierta (Odalisque)
- B5 medias/guantes: ✅ piernas desnudas sin medias y manos desnudas en las siete
- B6 accesorios/uñas: ⚠️ el collar se lee cromo espejo en Standing/Seated y como banda oscura teal/negra en Ditzy/POV; el anillo cromado migra del centro del pecho (Standing) a la cadera (Odalisque). Aros teal largos y uñas french estables
- B7 pelo: ⚠️ cereza profundo en Standing/Seated/Odalisque frente a un auburn más claro y cálido en Ditzy/POV
**VEREDICTO: GRAVE**

### ele L827 — 7 poses leídas
**A fidelidad: 7/10**
- Standing: botas thigh-high hasta medio muslo → terminan justo bajo la rodilla, dejando un tramo de media negra sheer descubierto entre la caña y la banda de la media
- POV: retrato con la cara dominante en el tercio superior y el escote debajo, mirada clavada en el lente → plano ancho de medio muslo hacia arriba, cara pequeña arriba del cuadro y mirada dirigida por encima del lente
- Odalisque: reclinada hacia atrás sobre AMBOS codos con el busto elevado y un stiletto apuntando a cámara → tumbada de costado apoyada en un solo brazo, con la bota cercana plana sobre el plinto
- Ditzy: exactamente una mano visible en el cuadro → la segunda mano aparece abajo a la derecha con las uñas a la vista
**B consistencia:**
- B1 escote: ⚠️ Seated con el bandeau más plano y el busto menor que el busto alto y redondo de Standing/Ditzy/POV/Side Profile
- B2 maquillaje: ✅ ahumado plata-gris con delineado alado y labio rosa chicle idénticos en las siete
- B3 largo inferior: ✅ cut-outs de cintura, leg line alta y tanga iguales en todas
- B4 calzado: ⚠️ la altura de la caña baila: bajo la rodilla en Standing, justo sobre la rodilla en Back View, medio muslo en Side Profile/Seated/Odalisque. Tipo, punta, color, tacón y ausencia de plataforma sí son idénticos
- B5 medias/guantes: ✅ media negra sheer con banda opaca y manos desnudas en todas
- B6 accesorios/uñas: ⚠️ la banda baja del arnés muestra una hebilla rectangular plateada en Ditzy/POV/Odalisque, mientras el BLOQUE B exige "ninguna hebilla a la vista" y Standing/Side Profile la resuelven como barra lisa. Collar plateado, aros de barra larga y uñas french estables
- B7 pelo: ✅ cereza oscuro hasta la cadera en las siete
**VEREDICTO: MENOR**

## PATRONES

- **El calzado es el punto que más se rompe, y siempre entre poses del mismo look.** L826 entrega tres zapatos distintos (con plataforma, sin plataforma en Back View, punta abierta en Odalisque); L827 acorta la caña de la bota bajo la rodilla solo en Standing; L825 cambia la altura de la caña del botín en Seated y le pone casquete plateado en la puntera solo en Standing/Back View. El bloque "the footwear clearly visible and exactly as described above" está literalmente en el prompt de las cinco poses de cuerpo entero y aun así no sostiene ni la plataforma ni la altura de caña.
- **Ditzy es la pose descarriada del sistema.** En cuatro de los cinco looks es la que rompe algo: L822 pierde el choker y baja el maquillaje; L825 mira directo al lente pese a la instrucción explícita de mirada perdida; L826 pierde volumen de busto, el acabado cromado del collar y hasta la fisonomía; L827 mete la segunda mano en cuadro cuando el prompt pide exactamente una. Se comporta como si el personaje se regenerara desde cero en vez de heredarse.
- **Odalisque es donde muta la prenda, no la pose.** Medias lisas que salen estampadas en pitón (L825), sandalia cerrada que sale abierta (L826), anillo que se desplaza del pecho a la cadera (L826). El cambio de orientación a 16:9 parece soltar el anclaje de vestuario.
- **POV ignora su propia directiva de encuadre.** L823 devuelve un plano entero de pie y L827 un plano de medio muslo, ambos con la cara pequeña, cuando el prompt cierra con "the face dominant in the upper-middle of the frame with the décolleté below it". El texto está y no se cumple.
- **La quincallería metálica (anillos, hebillas, collares) es el detalle menos estable del repertorio.** El anillo rose-gold de L822 se muda de la garganta al esternón; el anillo cromado de L826 del pecho a la cadera; el arnés de L827 gana una hebilla que el BLOQUE B prohíbe; el collar "slim" de L825 se convierte en collar de eslabones en dos poses. Ninguno de estos cambios es de encuadre: es la pieza la que cambia.
- **El volumen del busto no se sostiene dentro de un mismo look.** L823 (discreto en Standing/POV, pronunciado en Ditzy/Seated), L825, L826 (Ditzy claramente menor) y L827 (Seated más plano). Con implantes fijos declarados desde L185, esto debería ser invariante y no lo es.
- **El batch 823-827 entregó al menos un archivo duplicado haciéndose pasar por pose.** `ele_823_side_profile.png` es idéntico a `ele_823_standing.png`: la pose Side Profile de L823 nunca se generó, y ningún control lo detectó antes de que la imagen llegara a la galería.

---

## Auditor `miss_doll_1`

# Auditoría visual externa — miss_doll L75-L79

### miss_doll L75 — 6 poses leídas (falta Standing)
**A fidelidad: 5/10**
- Todas las poses: el prompt pide "a high halter neckline fastened behind the neck" → se ve un escote en V profundísimo hasta el esternón que abre desde una banda de cuello tipo choker, con el cierre/argolla cromada al FRENTE del cuello, no detrás. La arquitectura del delantero está invertida respecto a lo declarado.
- Seated: el prompt exige piernas cerradas ("knees and thighs held together... the hem falling closed over the lap") → está sentada con las rodillas separadas, los muslos abiertos y el tanga visible bajo el ruedo.
- Seated: calzado declarado "closed pointed toe" → sandalia de puntera ABIERTA con los dedos y el esmalte del pie a la vista; además se leen 3 tiras de tobillo donde el prompt declara "doubled" (2).
- POV: el slot pide retrato de influencer con una sola mano en cuadro y el escote en el tercio inferior → se entregó un plano entero de tres cuartos de espalda, con las dos manos visibles; duplica el encuadre del Side Profile.
**B consistencia:**
- B1 escote: ⚠️ Side Profile y POV abren la sisa hasta exponer todo el costado y el bajo del busto; Seated, Glacial Command y Odalisque muestran el panel lateral cerrado cubriendo el flanco del pecho. No es el mismo patrón de corte.
- B2 maquillaje: ✅ labio gloss cobre-bronce y ojo ahumado negro idénticos en las 6 poses.
- B3 largo inferior: ⚠️ el ruedo cae parejo a medio muslo en todas, pero Side Profile suma un cut-out abierto sobre la cadera que no existe en ninguna otra pose ni está declarado en el BLOQUE B.
- B4 calzado: ⚠️ plataforma gruesa en POV, Seated y Side Profile; plataforma casi plana en Back View y Odalisque. Puntera cerrada en Back View/Odalisque, abierta en Seated. El tacón aguja cromado sí es el mismo en todas.
- B5 medias/guantes: ✅ piernas desnudas sin medias y sin guantes en las 6 poses, tal como declara el BLOQUE B.
- B6 accesorios/uñas: ⚠️ el prompt declara UN puño de vinilo azul en la muñeca izquierda: Back View y POV muestran uno; Seated, Side Profile y Odalisque muestran DOS, uno en cada muñeca. Uñas azul marino glossy consistentes en todas.
- B7 pelo: ✅ bob platino a la mandíbula, mismo largo y mismo tono en las 6.
**VEREDICTO: GRAVE**

### miss_doll L76 — 1 pose leída (Standing)
**A fidelidad: 6/10**
- Standing: el BLOQUE B declara "a hot pink chrome collar with no lettering" → la garganta está desnuda, sin collar. Los puños rosados sí están (ambas muñecas), el collar no.
- Standing: calzado declarado con "6-inch cobalt platform" → la plataforma mide a ojo un tercio de eso, la suela es casi plana bajo la puntera.
- Standing: calzado declarado con "two hot pink chrome ankle straps with pin buckles" → una sola tira de tobillo por pie, sin hebilla legible.
- Standing: puños declarados "hot pink chrome" → se leen como vinilo/satén rosa, sin acabado cromado ni herraje. Uñas: no legibles (ambas manos detrás de la nuca).
**B consistencia:** no aplica (1 pose)
- B1 escote: no aplica (1 pose)
- B2 maquillaje: no aplica (1 pose)
- B3 largo inferior: no aplica (1 pose)
- B4 calzado: no aplica (1 pose)
- B5 medias/guantes: no aplica (1 pose)
- B6 accesorios/uñas: no aplica (1 pose)
- B7 pelo: no aplica (1 pose)
**VEREDICTO: MENOR**

### miss_doll L77 — 1 pose leída (Standing)
**A fidelidad: 6/10**
- Standing: el BLOQUE B declara "a heavy rose-gold chrome collar with no lettering" → el cuello está completamente desnudo, no hay collar ni choker de ningún tipo.
- Standing: calzado declarado "16cm razor-thin metal needle heel" → el tacón se lee como una columna oscura gruesa de bloque, no como aguja metálica delgada. La puntera cerrada y la plataforma sí se cumplen; la zona del tacón está a baja definición.
- Standing: la mini pencil se declara moldeada en un solo paño sobre la cadera → se ve una costura horizontal marcada cruzando el alto de la falda que la parte en dos bloques.
- Nota de prompt (no de imagen): el delta de Standing arrastra tres cláusulas de costura de medias ("the front of both legs perfectly smooth bare nylon") cuando el BLOQUE B declara "bare legs, no stockings". El prompt se contradice a sí mismo; la imagen resolvió bien, con las piernas desnudas.
**B consistencia:** no aplica (1 pose)
- B1 escote: no aplica (1 pose)
- B2 maquillaje: no aplica (1 pose)
- B3 largo inferior: no aplica (1 pose)
- B4 calzado: no aplica (1 pose)
- B5 medias/guantes: no aplica (1 pose)
- B6 accesorios/uñas: no aplica (1 pose)
- B7 pelo: no aplica (1 pose)
**VEREDICTO: MENOR**

### miss_doll L78 — 1 pose leída (Standing)
**A fidelidad: 6/10**
- Standing: medias declaradas con "a fine black seam running the BACK of each leg" → la costura oscura corre por el FRENTE de ambas piernas, centrada sobre la espinilla y la rodilla, perfectamente visible de frente.
- Standing: se declara "a wide antique-gold posture collar... closing at the nape" → lo que lleva es un choker angosto de un dedo de alto; sí tiene la argolla dorada en el hueco de la garganta, pero no es un collar de postura.
- Standing: el BLOQUE B no declara ningún puño ni brazalete → lleva DOS puños rosa fuerte, uno en cada muñeca: prendas añadidas que no existen en la descripción y que además meten un rosa saturado ajeno a la paleta carbón/oro viejo del look.
- Standing: uñas declaradas "glossy blackened gold" → se leen negras planas sin reflejo dorado. El tacón de las botas queda cortado por el borde inferior del cuadro: altura y plato de talón no legibles, pese a que el prompt pide "the footwear clearly visible".
**B consistencia:** no aplica (1 pose)
- B1 escote: no aplica (1 pose)
- B2 maquillaje: no aplica (1 pose)
- B3 largo inferior: no aplica (1 pose)
- B4 calzado: no aplica (1 pose)
- B5 medias/guantes: no aplica (1 pose)
- B6 accesorios/uñas: no aplica (1 pose)
- B7 pelo: no aplica (1 pose)
**VEREDICTO: MENOR**

### miss_doll L79 — 7 poses leídas
**A fidelidad: 6/10**
- Back View: el top se declara "two magenta triangles joined by fine gunmetal chain at the centre of the back" y el calzón "reduced at the back to one thin strip" → la espalda muestra una banda ancha de vinilo magenta sólido cruzando el torso y un panel trasero ancho en la cadera. Justo la pose que existe para leer esa construcción es la que la contradice.
- Glacial Command: el prompt pide la mirada baja sobre la cadena entre los dedos y "her gaze drifting away past the edge of the frame and never at the lens" → mira de frente al lente, sonriendo, con la mano cerrada sin tocar cadena alguna.
- POV: el slot pide retrato con "the face dominant in the upper-middle frame" y una sola mano en cuadro → plano entero de cuerpo completo, cara pequeña y las dos manos visibles.
- Uñas declaradas "long square-shaped" → cuadradas solo en Glacial Command; puntiagudas tipo stiletto en Standing, ovaladas en Back View y Seated.
**B consistencia:**
- B1 escote: ⚠️ el busto cambia de volumen entre poses: contenido y separado en Standing, mucho más lleno y redondo llenando los triángulos en Glacial Command, POV y Odalisque; en Back View la pieza se resuelve como banda recta.
- B2 maquillaje: ⚠️ labio rojo carmín profundo en Standing, Seated, Side Profile, Glacial Command, POV y Odalisque; en Back View el labio visible de perfil es rosa pálido nude. La sombra violeta-magenta sí es la misma donde se ve.
- B3 largo inferior: ⚠️ Standing lleva un calzón de frente ancho y sólido, con más cobertura de cadera; Glacial Command, POV y Odalisque llevan un tanga de tiro fino con la cadena de cadera a la vista. No es la misma pieza inferior.
- B4 calzado: ⚠️ sandalia gunmetal de puntera abierta y tira de tobillo en todas, pero la plataforma es gruesa y espejo en Seated, Side Profile, POV y Odalisque, y notoriamente más delgada y oscura (casi negra, sin reflejo) en Standing.
- B5 medias/guantes: ✅ piernas desnudas sin medias y sin guantes en las 7 poses, como declara el BLOQUE B.
- B6 accesorios/uñas: ⚠️ en presencia va bien — cadena corporal desde la nuca cruzando la espalda y rodeando la cintura, aros pequeños gunmetal y cero collar en las 7 — pero la forma de la uña cambia de pose a pose (ver eje A).
- B7 pelo: ✅ bob platino a la mandíbula, mismo largo y mismo tono en las 7.
**VEREDICTO: GRAVE**

## PATRONES

- **El collar declarado desaparece.** L76 declara "hot pink chrome collar" y L77 "heavy rose-gold chrome collar": en ambas la garganta sale desnuda. En L78 el collar existe pero degradado de "wide posture collar" a choker angosto. 3 de 5 looks fallan el mismo campo, y es un campo que el perfil de Miss Doll trata como firma.
- **La plataforma de 6 pulgadas casi nunca se materializa como tal.** L76, L79 Standing y L75 Back View/Odalisque muestran suela casi plana contra las 6" declaradas. El tacón aguja sí se respeta; lo que el motor no consigue imprimir es el plato. En L77 falla al revés: la plataforma está y el aguja se convierte en tacón de bloque.
- **El calzado no es el mismo zapato entre poses del mismo look.** L75 alterna puntera cerrada y abierta más dos alturas de plataforma; L79 alterna gunmetal espejo con un par casi negro de plato fino. En ambos casos el defecto cae en las poses de cuerpo entero, justo donde el prompt pide "the footwear clearly visible and exactly as described".
- **Los accesorios se multiplican o se inventan.** L75 declara UN puño y entrega dos en 3 de 6 poses; L78 no declara ninguno y entrega dos, además en un rosa fuera de la paleta del look. El campo de accesorios del BLOQUE B se está leyendo como sugerencia, no como inventario cerrado.
- **Los slots Glacial Command y POV se colapsan en plano entero.** L75 POV y L79 POV entregaron cuerpo completo en vez del retrato con la cara dominante, ambos con las dos manos en cuadro pese a la cláusula explícita de "exactly one hand visible... the other arm out of shot". L79 Glacial Command además invirtió la mirada pedida (fuera de cuadro) por mirada al lente. Mismo defecto en dos looks distintos: la instrucción de encuadre del slot pierde contra la inercia del plano entero.
- **La cláusula de piernas cerradas se ignora cuando hay falda y asiento.** L75 Seated abre las rodillas y deja el tanga a la vista, contra una instrucción que aparece literal y completa en el delta de esa misma pose.
- **Deriva de identidad dentro del mismo look (L79).** Standing, Seated y Side Profile muestran piel bronceada dorada; Back View, Glacial Command, POV y Odalisque muestran piel porcelana pálida, con cambio simultáneo de volumen de busto. No es uno de los 7 puntos de control, pero es lo primero que rompe la lectura de serie: parecen dos mujeres distintas con el mismo bikini.
- **El prompt se contradice a sí mismo con las medias.** Varias poses de L77 y L79 arrastran bloques largos sobre costura, denier y color de medias cuando el BLOQUE B declara "bare legs, no stockings". Es texto muerto que gasta atención en cada pose, y en L78 —el único de los cinco que sí lleva medias— la costura salió igual al frente.

---

## Auditor `miss_doll_2`

### miss_doll L81 — 1 pose leída
**A fidelidad: 4/10**
- Standing: catsuit de una sola pieza, sólido y sin cortes en busto, cintura, ombligo y caderas → la prenda llega como body manga larga corto + tanga alto + legging separado, con una ventana abierta en el abdomen que deja el ombligo al aire (el cutout que el delta prohíbe explícitamente).
- Standing: tacón de aguja negro cromo de 16cm + plataforma fucsia → talón y plataforma son fucsia enteros, no hay nada negro cromo en la bota.
- Standing: "sin medias, el catsuit cubre la pierna hasta el tobillo" → entre los muslos y en la ingle se lee un panel nude/sheer bajo la tanga fucsia, la pierna no queda cubierta de forma continua.
- Standing: collar ancho negro cromo → banda negra estrecha con tachas, sin acabado cromado.
**B consistencia:** no aplica (1 pose)
**VEREDICTO: GRAVE**

### miss_doll L82 — 7 poses leídas
**A fidelidad: 4/10**
- Todas las poses: "platform stiletto trainers" (zapatilla-plataforma) → llegan pumps de plataforma con doble tira de tobillo. El tipo de calzado está mal en las 7.
- Back View: leggings de talle alto moldeados a la pierna → tanga/short de talle alto con nalgas al aire y un legging separado que arranca por debajo del glúteo.
- Side Profile / POV / Odalisque: top deportivo de escote redondo alto, copas juntas → escote abierto en pico o con keyhole y el pecho desbordando, con anillos añadidos que no existen en Standing.
- Seated / Glacial / POV: cierre gunmetal al centro de la ESPALDA y tanga POR DEBAJO del legging → cremallera visible al centro del FRENTE (Seated) y tiras de tanga por ENCIMA del legging en las caderas (Glacial, POV).
**B consistencia:**
- B1 escote: ⚠️ Standing y Glacial llevan el cuello redondo alto cerrado sin escote; Side Profile, POV, Odalisque y Seated muestran plunge o keyhole con escote abierto — y el volumen de busto casi se duplica entre Standing y Side Profile/POV.
- B2 maquillaje: ⚠️ labio nude-rosa estable en todas, pero la ceja pasa de recta y muy gruesa (Standing, Back, POV) a más fina y arqueada en Glacial Command.
- B3 largo inferior: ⚠️ Back View pierde el legging completo (glúteo desnudo, legging desde medio muslo); POV y Odalisque añaden un recorte abierto en la cadera que Standing no tiene.
- B4 calzado: ⚠️ misma pump de plataforma con doble tira y canto de suela rosa en todas, pero el tacón se lee violeta en Standing y negro en Seated y Side Profile.
- B5 medias/guantes: ✅ sin medias y sin guantes en las 7, como declara el BLOQUE B.
- B6 accesorios/uñas: ✅ gargantilla de cadena gunmetal, puños en ambas muñecas, aros pequeños y uñas violeta glossy consistentes.
- B7 pelo: ✅ bob platino a la mandíbula en las 7.
**VEREDICTO: GRAVE**

### miss_doll L83 — 7 poses leídas
**A fidelidad: 5/10**
- Standing / Back / Seated / Side Profile: pump de punta cerrada AFILADA → la puntera es redonda-almendrada en todas; el resto del zapato (plataforma, empeine sin tira, color) sí cumple.
- POV: retrato único con el rostro dominante → la imagen llega partida en dos paneles apilados con costura horizontal dura (plano medio arriba, primer plano extremo del busto abajo) y barras negras laterales.
- Glacial Command: mentón girado y mirada baja y desenfocada fuera de cuadro, nunca al lente → mira de frente y directo a cámara.
- Seated: peso completo sobre el banco de terciopelo, piernas plegadas al mismo lado con tobillos apilados y mentón apoyado en el antebrazo → está encaramada en el brazo de un sofá, piernas cruzadas colgando al suelo, sin contacto mentón-antebrazo.
**B consistencia:**
- B1 escote: ⚠️ el sujetador cambia de arquitectura en cinco versiones: tiras cruzadas altas (Standing, Back), balconette moldeado con muesca central (Seated), copa con banda larga tipo corselette (Side Profile), triángulo de tirante fino liso (Glacial), top de bandas múltiples (Odalisque). El busto además crece mucho en Glacial y POV.
- B2 maquillaje: ⚠️ labio rosa glossy estable, pero la sombra pasa de humo gris-azul (Standing, Side) a azul-turquesa saturado (Seated), y en Odalisque la ceja es recta y mucho más gruesa que la ceja arqueada del resto.
- B3 largo inferior: ⚠️ faja ancha moldeada + tanga alto consistentes en seis poses; Odalisque los sustituye por un bottom de tiras múltiples cruzadas.
- B4 calzado: ⚠️ misma pump rosa de plataforma y puntera redonda en Standing, Back, Seated y Side Profile; en Odalisque la plataforma se adelgaza y casi desaparece.
- B5 medias/guantes: ⚠️ medias sheer rosa a medio muslo con welt más oscuro en todas y sin guantes (correcto), pero en Odalisque no hay ninguna liga enganchada a la media.
- B6 accesorios/uñas: ✅ collar de cuentas rosa, aros colgantes de cristal rosa y uñas rosa glossy en todas las poses legibles; sin collar de cuero ni puños, como pide el BLOQUE B.
- B7 pelo: ✅ bob platino idéntico en las 7.
**VEREDICTO: GRAVE**

### miss_doll L84 — 7 poses leídas
**A fidelidad: 6/10**
- Seated: escote halter alto cerrado hasta el cuello → panel frontal abierto en V profunda con el pecho expuesto; es un delantero de body distinto al de las otras seis poses.
- Side Profile: tacón trasero plantado y pierna delantera extendida a lo largo del suelo, punta estirada y rodilla recta → está de pie con ambos pies plantados en un tres cuartos trasero, sin pierna extendida.
- Odalisque: de rodillas con muslos y torso 100% verticales, espalda rígida y erguida → está sentada sobre sus propios talones con el torso volcado hacia adelante.
- Glacial Command y POV: exactamente UNA mano en cuadro, el otro brazo fuera de plano → en ambas se ven los dos brazos y las dos muñecas con puño.
**B consistencia:**
- B1 escote: ⚠️ halter alto cerrado en Standing, Back, Side Profile, Glacial, POV y Odalisque; Seated abre en V profunda con escote y además el busto se ve bastante mayor.
- B2 maquillaje: ⚠️ delineado y labio glossy consistentes, pero la ceja de Glacial Command y POV es notoriamente más gruesa y oscura que la de Standing y Back, y el labio vira de rosa a rosa-rojo profundo.
- B3 largo inferior: ✅ misma línea de pierna alta sobre el hueso de la cadera y mismo liguero en las 7.
- B4 calzado: ✅ misma pump esmeralda de plataforma con una sola tira de tobillo y canto de suela rosa fuerte en todas las poses legibles (el tacón se lee verde oscuro y no cromo, pero de forma consistente).
- B5 medias/guantes: ✅ medias esmeralda sheer con welt sólido en todas; sin guantes.
- B6 accesorios/uñas: ⚠️ los puños se leen cromo espejo en Standing y Side Profile pero negros con canto cromado en Seated, Glacial, POV y Odalisque; en Seated solo hay puño en una muñeca. Uñas rosa fuerte y aros esmeralda sí consistentes.
- B7 pelo: ✅ bob platino idéntico en las 7.
**VEREDICTO: MENOR**

### miss_doll L85 — 7 poses leídas
**A fidelidad: 5/10**
- Odalisque: botines de plataforma calzados y espalda arqueada hacia atrás en backbend de camello → está inclinada hacia adelante y con los pies solo en medias, con un botín descalzado sostenido en las manos. Rompe el canon de calzado absoluto.
- Todas las poses: tanga de vinilo rosa fuerte high-gloss con trasero de cordón fino → la prenda se lee mate tipo algodón y en Back View es una braga cachetera de cobertura completa, no un cordón.
- Copas cónicas moldeadas que elevan el busto → las copas del corsé son redondeadas tipo corazón en las 7 poses; el "conical" no aparece nunca.
- Glacial Command: una sola mano enmarcando el pómulo y mirada desviada más allá de la cámara, nunca al lente → la mano queda en el mentón/labio, ambas manos en cuadro y la mirada clavada en el lente.
**B consistencia:**
- B1 escote: ⚠️ mismo corsé overbust, pero el volumen de busto pasa de contenido en Standing, Back, Seated y Side Profile a desbordando la copa en Glacial Command y POV.
- B2 maquillaje: ⚠️ ojo ahumado negro consistente; el labio vira de nude-beige glossy (Standing, Seated) a rosa-coral saturado (POV, Odalisque) y la ceja de Glacial y POV es más gruesa.
- B3 largo inferior: ⚠️ la tanga rosa es cachetera de cobertura completa en Back View y un panel alto tipo braga en Seated y Glacial, contra el cordón único declarado.
- B4 calzado: ⚠️ botín gunmetal de plataforma con canto de suela rosa idéntico en Standing, Back, Seated y Side Profile; en Odalisque no lleva calzado puesto.
- B5 medias/guantes: ✅ medias sheer tono gunmetal con welt marcado y cuatro ligas en las 7; sin guantes.
- B6 accesorios/uñas: ⚠️ en Side Profile desaparecen el collar cromado Y los dos puños (cuello y muñecas desnudos); presentes en todas las demás. Uñas rosa fuerte consistentes; aro-barra cromado legible en Back, Glacial y POV.
- B7 pelo: ✅ bob platino idéntico en las 7.
**VEREDICTO: GRAVE**

## PATRONES

- **El escote es el campo más inestable de todo el lote.** En los cuatro looks con 7 poses el generador trata el escote como variable libre: L82 pasa de cuello redondo alto cerrado a plunge con keyhole en 4 de 7; L83 entrega cinco arquitecturas distintas de sujetador; L84 abre en V solo en Seated; L85 desborda la copa solo en los planos medios. Ninguna otra prenda deriva tanto.
- **El volumen de busto sigue al encuadre, no al BLOQUE B.** En los 4 looks multipose, glacial_command y pov renderizan un pecho marcadamente mayor que las tomas de cuerpo entero del mismo look. Es sistemático, 4 de 4.
- **Del token de calzado sobreviven el color y la plataforma; se pierden la puntera y el material del tacón.** L83 pide punta afilada y llega redonda; L82 pide trainers y llegan pumps; L84 y L85 piden tacón de aguja cromado y llega oscuro. El canon del tacón alto se cumple casi siempre — lo que falla es el detalle descriptivo.
- **Los negativos anti-cutout no muerden.** L81 aparece con una ventana abierta en el ombligo que su propio delta prohíbe palabra por palabra; L82 inventa recortes de cadera y tiras de tanga por encima del legging que nadie declaró.
- **El ancla "exactamente una mano en cuadro" falló en 4 de 8 oportunidades** (L84 glacial + pov, L85 glacial + pov), y la de "mirada fuera del lente" en glacial_command falló en L83 y L85. Los planos medios son donde más se desobedece la instrucción de pose.
- **Accesorios que se caen en una sola pose, sin patrón:** L85 side_profile pierde collar y ambos puños, L84 seated pierde un puño, L83 odalisque pierde las ligas. Es la clase de defecto que ningún chequeo por-look detecta, porque cada pose por separado se ve correcta.
- **Dos entregas llegaron estructuralmente rotas, no solo desviadas:** L83 pov es un collage de dos paneles apilados con costura visible, y L85 odalisque llega descalza con el botín en la mano.

---

## Auditor `anais_1`

### anais L76 — 7 poses leídas
**A fidelidad: 6/10**
- Odalisque: tumbada de espaldas sobre la consola con la cabeza volcada más allá del borde, ambos brazos sobre la cabeza y la mirada al lente al revés → está de costado, apoyada sobre el antebrazo, cabeza arriba y mirada derecha.
- Sovereign Gaze: una sola mano en cuadro (el otro brazo fuera de plano) y mirada nunca al lente → dos manos enguantadas visibles y los ojos fijos en la cámara.
- POV: una sola mano en cuadro → la segunda mano enguantada aparece en la cadera, esquina inferior izquierda.
- Uñas: declaradas oro viejo brillante → se ven verde esmeralda en Standing, POV y Odalisque.
**B consistencia:**
- B1 escote: ⚠️ el cierre abre hasta media esternón en Standing/Seated, pero en Sovereign Gaze y Odalisque la V baja bastante más y expone mucho más pecho.
- B2 maquillaje: ⚠️ labio rojo, forma y lunar estables; la sombra es notoriamente más negra y cargada en Sovereign Gaze y POV que en Standing/Seated.
- B3 largo inferior: ✅ catsuit hasta el tobillo en las 7.
- B4 calzado: ✅ misma bota caña-rodilla charol esmeralda, stiletto sin plataforma, punta cerrada, en las 5 poses con pies en cuadro.
- B5 medias/guantes: ✅ guantes de ópera por sobre el codo en las 7, sin medias (correcto, el catsuit cubre la pierna).
- B6 accesorios/uñas: ⚠️ uñas verdes en Standing/POV/Odalisque vs oro en Seated/Sovereign Gaze; aros oro gota en casi todas, pero en Odalisque el pendiente lee verde esmeralda.
- B7 pelo: ⚠️ rubio y largo en todas, pero el victory-roll de los 40 aparece en Standing/Back/Seated y desaparece en Sovereign Gaze/POV/Odalisque.
**VEREDICTO: MENOR**

### anais L77 — 7 poses leídas
**A fidelidad: 5/10**
- Standing: el prompt pesa (1.4) "el frente de ambas piernas perfectamente liso, cero costura" → una costura oscura baja por el FRENTE de ambas espinillas.
- Side Profile: cinturón declarado = cadena fina de oro viejo sobre la cadera → aparece un cinturón ancho de metal labrado dorado, a la cintura, con cadena colgante.
- Sovereign Gaze: blusa de georgette totalmente transparente con la lencería legible → blusa camel opaca, no se lee nada del sostén; y el aro pasa de perla pequeña a argolla dorada.
- Standing: falda lápiz "justo bajo la rodilla" con pretina en la cintura natural → ruedo a media pantorrilla y pretina subida casi bajo el busto.
**B consistencia:**
- B1 escote: ⚠️ la copa de encaje del longline se lee en Seated/Side/POV/Odalisque; en Standing la copa lee satén liso sin encaje, y en Sovereign Gaze no se lee lencería alguna porque la blusa salió opaca.
- B2 maquillaje: ⚠️ Standing lleva labio nude-café; todas las demás poses llevan rojo intenso.
- B3 largo inferior: ⚠️ Standing pone la pretina bajo el busto y el ruedo a media pantorrilla; Seated/POV/Odalisque la ponen en la cadera con ruedo a la rodilla.
- B4 calzado: ✅ mismo stiletto punta cerrada charol chocolate; suela roja legible en Back View/Seated/Odalisque.
- B5 medias/guantes: ⚠️ sin guantes declarados y no aparecen (correcto), pero la costura corre por el FRENTE de la espinilla en Standing y se insinúa igual en POV, mientras en Back View/Odalisque va correctamente centrada atrás.
- B6 accesorios/uñas: ⚠️ cadena fina en Back/Seated/POV/Odalisque, cinturón ancho de metal en Side Profile y nada visible en Standing; aros perla salvo Sovereign Gaze (argolla dorada); uñas bronce estables salvo la mano izquierda de Seated, que lee dorada.
- B7 pelo: ⚠️ el pelo termina a media espalda en Standing y Sovereign Gaze, y a la cadera en Back/Seated/Odalisque.
**VEREDICTO: GRAVE**

### anais L78 — 7 poses leídas
**A fidelidad: 6/10**
- Seated: el prompt pide sentada de lado sobre el taburete, ambas piernas colgando sobre un brazo del asiento y el torso torcido al lente → se sienta de frente, piernas cruzadas a la rodilla y pies en el suelo.
- Odalisque: el prompt pide tendida en diagonal sobre el mármol del tocador, cuerpo estirado a su largo total y un brazo doblado bajo la cabeza → está de costado incorporada sobre el codo, brazos abajo, cuerpo sin estirar.
- Standing y Back View: peignoir "cayendo suelto fuera de ambos hombros" con la faja sin anudar → se lleva puesto sobre los hombros como bata; en Sovereign Gaze además la faja va anudada en moño.
- Sovereign Gaze: "la mirada nunca al lente, los ojos perdidos en la distancia media" → mira directo a la cámara.
**B consistencia:**
- B1 escote: ⚠️ en Seated/Sovereign Gaze/POV/Odalisque el sostén lee longline con banda larga; en Standing y Side Profile la misma pieza lee bralette de banda corta que termina bajo el busto.
- B2 maquillaje: ✅ labio rojo, ahumado y lunar estables en todas las poses legibles.
- B3 largo inferior: ✅ tanga marfil con el liguero encima, tirantes y banda ancha de encaje de la media consistentes en todas.
- B4 calzado: ✅ mismo stiletto punta cerrada charol marfil en las 5 poses con pies en cuadro (la suela roja solo alcanza a leerse en Seated: es ángulo, no defecto).
- B5 medias/guantes: ✅ sin guantes declarados y no aparecen; hold-ups marfil ultra-sheer con banda de encaje en todas.
- B6 accesorios/uñas: ⚠️ collar de perlas, aros gota y uñas almendra oro pálido estables, pero POV agrega un anillo solitario grande que no aparece en ninguna otra pose.
- B7 pelo: ⚠️ Standing y Back View llevan melena corta a la altura del hombro con victory rolls; Seated/Sovereign Gaze/POV/Odalisque llevan el mismo rubio hasta la cadera.
**VEREDICTO: MENOR**

### anais L79 — 7 poses leídas
**A fidelidad: 5/10**
- Seated: el prompt pesa (1.4) "genuinamente sentada, glúteos sobre el asiento, nunca de pie" y pide sillón de terciopelo azul → está de pie, apoyada de espaldas contra el escritorio, ambas manos sobre la cubierta y pies en el suelo.
- Side Profile: "un perfil genuino, la silueta dibujada desde el flanco" → sale un tres cuartos casi frontal, con el mismo apoyo contra el mismo escritorio que la pose Seated (encuadre casi duplicado).
- Odalisque: el prompt pide tendida de espaldas sobre el secante con un cojín bajo la zona lumbar, hombros y caderas abajo y ambos brazos caídos abiertos → está de costado, incorporada, brazos pegados al cuerpo.
- Medias declaradas hold-up (autoadhesivas) → se lee un liguero con tirantes a través de la malla en Standing/Seated/Side Profile/Odalisque.
**B consistencia:**
- B1 escote: ⚠️ bajo la malla, el sostén lee satén liso sin encaje en Standing/Seated/Side Profile/Sovereign Gaze, y copa de encaje con aro en POV/Odalisque.
- B2 maquillaje: ✅ labio rojo, ahumado y lunar estables.
- B3 largo inferior: ✅ slip a media pantorrilla con la abertura lateral en todas las poses de cuerpo entero.
- B4 calzado: ✅ mismo stiletto punta cerrada charol azul noche; suela roja legible en Back View y Side Profile.
- B5 medias/guantes: ⚠️ guantes de ópera azul noche por sobre el codo, consistentes en las 7; las medias en cambio aparecen con liguero no declarado y con una costura que baja por el FRENTE de las espinillas en Standing.
- B6 accesorios/uñas: ⚠️ la gota de zafiro está en todas, pero es pequeña en Standing/POV y una piedra grande talla pera en Sovereign Gaze; los aros son gota de oro salvo POV, que lleva oro con perla.
- B7 pelo: ⚠️ largo al hombro en Standing/Seated/Side Profile/Sovereign Gaze, largo hasta la cadera en POV/Odalisque.
**VEREDICTO: GRAVE**

### anais L80 — 7 poses leídas
**A fidelidad: 7/10**
- Back View: el prompt pide un encuadre cerrado de la cintura hacia arriba → el cuadro baja más allá de las caderas y muestra los glúteos desnudos y el borde de las medias.
- Sovereign Gaze: el collar de plata vieja con su anilla está declarado en el BLOQUE B → el cuello sale desnudo, sin collar.
- Seated: el prompt pide ambos codos sobre las rodillas, mentón sobre los dedos entrelazados y hombros rodados hacia adelante → codos abiertos, manos apiladas bajo el mentón y torso erguido.
- Standing: el prompt pide el talón delantero cruzado sobre el trasero y un hombro y cadera apoyados contra el panel → pies paralelos y separados, cuerpo sin apoyarse en el panel.
**B consistencia:**
- B1 escote: ✅ misma línea de copa moldeada en corazón del overbust en todas las poses con torso en cuadro.
- B2 maquillaje: ⚠️ labio rojo y ahumado estables, pero el lunar no aparece en POV y el rojo de Sovereign Gaze es más claro que el vino de Seated/POV.
- B3 largo inferior: ✅ tanga más cuatro tirantes de liguero y punta del corsé sobre el hueso de la cadera, consistentes.
- B4 calzado: ✅ misma bota caña-rodilla charol berenjena, stiletto sin plataforma y punta cerrada, en las 4 poses con pies en cuadro.
- B5 medias/guantes: ✅ guantes de látex berenjena sobre el codo y medias humo-ciruela con welt oscuro en todas.
- B6 accesorios/uñas: ⚠️ el collar de plata con anilla falta por completo en Sovereign Gaze; los broches del busk delantero leen plata vieja en Standing/Odalisque y latón dorado en Seated/Sovereign Gaze/POV. Uñas stiletto plata ✅.
- B7 pelo: ⚠️ rubio en todas; a media espalda en Standing, hasta la cadera en Seated/POV, y Back View lo lleva en una coleta alta que ninguna otra pose usa.
**VEREDICTO: MENOR**

## PATRONES

- **La Odalisque tiene una sola versión, la pida o no el prompt.** En L76, L78 y L79 el prompt pedía tres puestas distintas (de espaldas con la cabeza volcada fuera del borde · en diagonal sobre el mármol con el brazo bajo la cabeza · de espaldas sobre un cojín con los brazos abiertos) y las tres salieron igual: de costado, incorporada sobre el antebrazo, mirada al lente. Solo coincidieron L77 y L80, que eran justamente los dos que pedían esa variante. Hay una odalisca por defecto.
- **"Sentada" es la pose que más se pierde, incluso con peso 1.4.** L79 salió de pie apoyada en el escritorio pese al `(genuinely sitting down… never standing up:1.4)`; L78 ignoró la puesta de lado sobre el taburete; L80 ignoró los codos sobre las rodillas. El refuerzo numérico no está comprando nada en este eje.
- **"Una sola mano en cuadro" no se respeta en Sovereign Gaze ni en POV.** L76 mete la segunda mano enguantada en ambas poses y L79 en POV. Es la misma cláusula, con el mismo texto, fallando en los mismos dos slots.
- **El pelo es el elemento MENOS estable dentro de un mismo look.** En L77, L78 y L79 el largo salta de hombro a cadera entre poses del mismo outfit, y en L80 Back View inventa una coleta alta. Ninguna otra prenda varía tanto: el calzado, en cambio, salió consistente en los 5 looks.
- **El metal y el color de uña derivan dentro del look.** Uñas verdes↔oro en L76, broches de busk plata↔latón en L80, aro perla↔argolla dorada en L77, aro oro↔oro con perla en L79. Es la clase de detalle que ninguna revisión pose por pose detecta: solo aparece comparando las 7.
- **Defecto de prompt, no de modelo: los deltas de pose nombran prendas que el BLOQUE B nunca declaró.** "the strand of pearls" en el POV de L77, "the ring turned to the light" en el de L78 (de ahí sale el solitario que aparece en una sola pose) y "the clasp of the fur at her throat" en el de L80, donde no hay piel alguna en el outfit. El delta de POV es texto genérico reutilizado y contamina el outfit.
- **La transparencia declarada se cae justo en los planos medios.** L77 Sovereign Gaze vuelve opaca una blusa "fully transparent" y L79 pierde el encaje de la copa en 4 de 7 poses. Mientras más cerca el encuadre, menos respeta el render la especificación de la lencería de debajo.

---

## Auditor `anais_2`

### anais L81 — 7 poses leídas
**A fidelidad: 7/10**
- Standing: el delta pide ambas manos sujetando los bordes de un wrap/estola/abrigo abierto → no hay ninguna prenda de abrigo en el look y las manos cuelgan a los costados.
- Seated: calzado declarado "12cm stiletto SIN plataforma, Mary Jane con tira de tobillo" → se ve un pump de charol con plataforma gruesa bajo la puntera y sin tira de tobillo.
- POV: pide mirada fija en el lente y rostro llenando el encuadre superior → los ojos están entrecerrados y bajos, y la toma es un plano sentado de cuerpo entero con la cara pequeña al centro.
- Side Profile / Odalisque: el merry widow declarado es strapless (copas moldeadas con aro, sin tirantes) → ambas muestran tirante fino sobre el hombro; en Odalisque además lee como dos piezas (sostén + liguero) y no como una longline entera.
**B consistencia:**
- B1 escote: ⚠️ strapless con borde corazón y encaje en Standing/Seated/Sovereign/POV vs. tirante al hombro en Side Profile y Odalisque.
- B2 maquillaje: ⚠️ labio rojo bermellón brillante en Standing y Sovereign vs. burdeos oscuro en POV y Seated; ceja y ahumado bastante más cargados en Seated/Sovereign que en Standing.
- B3 largo inferior: ⚠️ tanga con panel de encaje cubriendo la cadera en Back View/Odalisque vs. tanga liso mínimo en Side Profile; el faldón del corsé lee más largo en Odalisque.
- B4 calzado: ⚠️ Seated es el culpable: plataforma visible y sin tira de tobillo, contra el Mary Jane de suela sin plataforma de Standing/Side Profile/POV/Odalisque.
- B5 medias/guantes: ⚠️ guantes largos negros en las 7 ✅, pero el remate de la media cambia: puño de encaje ancho en Back View y Odalisque, banda lisa negra en Side Profile, sin remate visible en Standing.
- B6 accesorios/uñas: ✅ collar de perlas de una vuelta y aros de perla en todas las poses legibles; uñas no legibles (guantes en las 7).
- B7 pelo: ⚠️ rubio miel constante, pero el largo salta: hasta media espalda con rolls vintage en Standing/Sovereign/POV vs. hasta la cadera y sin rolls en Back View/Side Profile/Odalisque.
**VEREDICTO: GRAVE**

### anais L82 — 1 pose leída
**A fidelidad: 7/10**
- Standing: zapato declarado d'Orsay con arco recortado en el lado interno → se ve un pump cerrado liso, sin el recorte d'Orsay.
- Standing: uñas declaradas ovaladas en manicura media luna con la lúnula al desnudo → se ven largas y almendradas/punta, esmaltadas hasta la base, sin media luna.
- Standing: waspie declarado "cortado para terminar bien por encima del hueso de la cadera" → baja hasta cubrir la cadera, con las tabas de liga ya a la altura del hueso.
- Standing: el delta pide una mano en la cadera lejana y la otra en la clavícula → la segunda mano está levantada junto a la mandíbula/pelo, no en la clavícula.
**B consistencia:** no aplica (1 pose)
- B1 escote: no aplica
- B2 maquillaje: no aplica
- B3 largo inferior: no aplica
- B4 calzado: no aplica
- B5 medias/guantes: no aplica
- B6 accesorios/uñas: no aplica
- B7 pelo: no aplica
**VEREDICTO: MENOR**

### anais L83 — 6 poses leídas (7 archivos; seated y side_profile son el MISMO archivo, md5 49f149bb444496e40915b53bee25bf8d)
**A fidelidad: 5/10**
- Todas las poses: el BLOQUE B dice "bare hands, no gloves" → las 7 imágenes llevan guantes largos de raso negro hasta encima del codo.
- Side Profile: no existe render propio — el archivo es byte a byte idéntico al de Seated, así que el perfil verdadero pedido ("true side profile at full height, nariz y mentón como silueta limpia") nunca se produjo.
- POV: pide retrato influencer con el rostro dominante en el tercio superior y el escote debajo → es un plano entero de pie, cara pequeña, prácticamente el mismo encuadre y set que Standing.
- Seated: pide sentada dentro de una butaca de palco de terciopelo rojo con todo el peso en el asiento → está posada sobre la baranda/antepecho acolchado del palco, no en una butaca.
**B consistencia:**
- B1 escote: ✅ bustier dorado strapless de escote recto en Standing/Seated/Sovereign/POV/Odalisque.
- B2 maquillaje: ⚠️ labio rojo y ahumado constantes, pero en Sovereign Gaze el contorno, la ceja y el ahumado dorado están mucho más cargados que en el resto.
- B3 largo inferior: ✅ pantalón dorado al tobillo con raya marcada y vuelta en todas.
- B4 calzado: ✅ salón dorado de punta fina, tacón aguja sin plataforma y suela roja donde es visible (Back View, Seated, Odalisque).
- B5 medias/guantes: ✅ sin medias en todas (correcto) y los guantes negros son idénticos en las 7 — consistentes entre sí, aunque contradicen el BLOQUE B.
- B6 accesorios/uñas: ✅ gargantilla rígida dorada y aros largos dorados en todas las poses legibles; uñas no legibles (guantes).
- B7 pelo: ✅ rubio miel, ondas largas al mismo tono y largo.
**VEREDICTO: GRAVE**

### anais L84 — 7 poses leídas
**A fidelidad: 7/10**
- POV y Odalisque: accesorio declarado "cinta de terciopelo negro al cuello con una gota de oro viejo", sin collar adicional → ambas añaden una vuelta de perlas al cuello que no está en el BLOQUE B.
- Back View: el delta pide inclinada hacia adelante desde la cintura contra una mesa o respaldo, con la espalda curvada y los omóplatos juntos → está de pie erguida, solo apoyando una mano en el brazo del sofá.
- Odalisque: botas declaradas "hasta justo bajo la rodilla" → suben por encima de la rodilla, sobre el muslo.
- Standing y Odalisque: el guepiere declarado es strapless (copas moldeadas con aro) → ambas muestran un tirante fino sobre el hombro; en Odalisque la pieza lee además partida en sostén + faja.
**B consistencia:**
- B1 escote: ⚠️ strapless corazón en Back View/Seated/Side Profile/Sovereign/POV vs. tirante al hombro en Standing y Odalisque.
- B2 maquillaje: ⚠️ labio rojo profundo y ahumado negro constantes; en Sovereign Gaze la ceja y el contorno están notoriamente más marcados que en Standing/POV.
- B3 largo inferior: ⚠️ Back View no muestra ningún cordón de tanga sobre los glúteos (piel desnuda entre las ligas) cuando el BLOQUE B declara tanga con cordón fino atrás; en Side Profile y POV el tanga sí está.
- B4 calzado: ⚠️ bota de charol ciruela de punta fina y tacón aguja en las 7, pero en Odalisque pasa la rodilla mientras en Standing/Back View/Seated/Side Profile queda bajo ella.
- B5 medias/guantes: ✅ guantes largos de látex ciruela y medias ciruela con puño en contraste y costura en todas.
- B6 accesorios/uñas: ⚠️ la gargantilla de terciopelo con gota dorada está en las 7, pero POV y Odalisque suman perlas; uñas largas ciruela casi negro legibles y consistentes en Side Profile/Sovereign/POV.
- B7 pelo: ⚠️ rubio miel constante, pero rolls vintage y largo medio en Standing/Back View/Seated/POV vs. melena suelta hasta la cadera sin rolls en Side Profile/Sovereign/Odalisque.
**VEREDICTO: GRAVE**

### anais L85 — 7 poses leídas
**A fidelidad: 6/10**
- Standing: guantes largos de seda champán hasta encima del codo declarados → los brazos van solo con la manga de la blusa y las manos se ven desnudas; los guantes sí aparecen en las otras seis poses.
- Back View: la blusa declarada es una blusa de lazada al cuello, cerrada → se renderiza con la espalda completamente descubierta hasta la cintura, un drapeado trasero que no existe en el BLOQUE B.
- Seated: pide sentada de lado sobre la silla dorada con ambas piernas colgando sobre un brazo del asiento, tobillos cruzados y torso torcido al lente → está sentada de frente, piernas cruzadas a la rodilla, sin nada de eso.
- Estola: declarada como estola de zorro plateado echada sobre los hombros y cayendo sobre un brazo → en Standing, Seated, Sovereign y POV se ve montada como chaqueta/bolero cubriendo los dos brazos.
**B consistencia:**
- B1 escote: ⚠️ blusa cerrada con lazada al cuello en seis poses vs. espalda desnuda hasta la cintura en Back View.
- B2 maquillaje: ✅ labio rojo intenso, ahumado gris y lunar sobre el labio consistentes en todas.
- B3 largo inferior: ⚠️ falda lápiz muy corta, a mitad de muslo, en Standing/Side Profile/Sovereign/POV vs. falda que pasa la rodilla en Seated y llega a la rodilla en Odalisque.
- B4 calzado: ✅ slingback de charol nude, punta fina, tacón aguja sin plataforma y suela roja en Back View/Seated/Side Profile; en Odalisque la tira slingback no es legible.
- B5 medias/guantes: ⚠️ medias champán con puño y costura consistentes ✅, pero los guantes faltan en Standing y están en las otras seis.
- B6 accesorios/uñas: ⚠️ aros largos de plata vieja en Seated y Side Profile vs. un aro corto y pequeño en Sovereign Gaze; uñas bronce largas correctas donde son legibles (Sovereign, POV); la cadena fina al cuello no es legible en ninguna (la tapa la lazada).
- B7 pelo: ✅ rubio miel, ondas largas del mismo largo y tono en las 7.
**VEREDICTO: GRAVE**

## PATRONES

- **El strapless se vuelve con tirantes.** L81 y L84 declaran corsetería strapless de copas moldeadas y en ambos casos exactamente dos poses sacan un tirante fino al hombro (Side Profile/Odalisque en L81, Standing/Odalisque en L84). La Odalisque es la pose más propensa: en los dos looks la pieza entera se parte además en sostén + liguero.
- **La Odalisque y el Side Profile son donde el outfit se desarma.** Además de los tirantes: botas que suben sobre la rodilla (L84), falda que crece hasta la rodilla (L85), tanga que desaparece (L84 Back View), remates de media que cambian de encaje a banda lisa (L81). Standing es la única pose fiel de forma consistente en los cuatro looks con 7 imágenes.
- **El delta de pose se ignora cuando pide una acción concreta.** Manos en un wrap inexistente (L81 Standing), sentada de frente en vez de de lado sobre el brazo de la silla (L85 Seated), erguida en vez de inclinada con la espalda curva (L84 Back View), posada en la baranda en vez de dentro de la butaca (L83 Seated). El set y la prenda obedecen; el gesto no.
- **POV y Sovereign Gaze salen con encuadre demasiado abierto.** Los tres looks completos fallan lo mismo: la regla común pide "rostro dominante en el tercio superior con el escote debajo" y salen planos de tres cuartos o de cuerpo entero. L83 POV es prácticamente un clon del Standing (mismo set, mismo encuadre); L81 POV además rompe la mirada al lente que pide su propio delta.
- **Accesorios y guantes que no están en el BLOQUE B se cuelan, y los declarados se pierden.** L83 declara "bare hands, no gloves" y lleva guantes negros en las 7; L84 declara cinta de terciopelo sin collar y POV/Odalisque suman perlas; L85 declara guantes y Standing los pierde. Es bidireccional: el modelo rellena con vocabulario vintage genérico (perlas, guantes de ópera) y descarta lo declarado cuando la pose lo estorba.
- **El pelo cambia de largo dentro del mismo look.** L81 y L84 alternan melena a media espalda con rolls vintage y melena hasta la cadera sin rolls según la pose. L83 y L85, que mantienen un solo peinado, no tienen el problema.
- **El calzado acierta en tipo y color pero falla en construcción.** Plataforma donde se declaró "no platform" (L81 Seated), d'Orsay que sale como pump cerrado (L82), Mary Jane que pierde la tira de tobillo (L81 Seated). La suela roja, en cambio, se respeta casi siempre que es visible.
- **Un archivo duplicado pasó como pose materializada.** L83 seated y side_profile son el mismo PNG byte a byte: el look figura con 7 poses y tiene 6 renders. Ningún chequeo por nombre de archivo lo habría visto.
