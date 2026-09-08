# Validación — Capítulo 1 «El cajón» v0.3
Validador Nivel 4 · 2026-09-08

**Veredicto:** MICRO-FIX
**Medición mecánica (Fase 2.5):** 🟡 AVISOS (`medicion_v0.3.md`) — sin duros; los 6 tramos M4 son 🟡, ninguno 🔴
**Casos de la Ama que reinciden:** C17 (habla real — atendido, no reincide) · C1 (rozado, no fallado — pase de visita / baño del servicio / valle cocina-limón, todos ≤2 párrafos y por debajo del umbral duro) · C3 (atendido — ver §0 abajo) · C14 (atendido — parlamentos largos de Renée subieron de 4 a ~8 en el capítulo) · C7 (origen del rework completo — sigue atendido, no reincide)
**Inmersión:** ✅
**Continuidad:** ✅
**Narrativa:** 8.8
**Temperatura:** 8.8
**Voz autoral:** ✅

---

## 0. Contexto que gobernó esta lectura

Esta versión NO es un rework sobre una nota de rechazo: es un **append estructural** ordenado en vivo por la Ama (*"lo leo"* → 41 segundos después, orden de meter la Sesión 2 como tramo 4). El `brief_v0.3_tramo4.md` es explícito: *"Archivo a editar: ya existe: es copia exacta del v0.2 aprobado... NO re-emitir una sola línea de lo anterior."* Verificado con diff mental línea por línea: los tramos 1-3 (líneas 1-363) son idénticos al v0.2 que yo mismo validé como MICRO-FIX. El tramo 4 (líneas ~323/331-442, la Sesión 2) es prosa nueva.

**§1c — chequeo de reciclaje:** no aplica en el sentido de C3-05 (material RECHAZADO reciclado con retoques). v0.2 nunca fue rechazado ni tuvo Gate de la Ama — salió MICRO-FIX mío y la Ama interrumpió su propia lectura para ordenar la restructuración. No hay pasaje rechazado que esté volviendo disfrazado.

**Lo que sí encontré, y que reporto con la misma honestidad:** de los 4 micro-fixes que yo mismo receté sobre v0.2 (`validacion_v0.2.md` §5), **2 fueron resueltos por el efecto colateral del tramo 4** y **2 siguen sin tocar**, porque el brief ordenó explícitamente no tocar S1:
- ✅ **Resuelto** — H14/C17 (habla real): la medición fresca de Loreto sobre el archivo completo da 15,1% (13/86), sobre el piso de 10%. Hice conteo manual sobre el texto completo (no solo confié en el número) y encontré bastantes más interrupciones reales de las que mi propio reporte de v0.2 había contado a mano (*"—Desde… no. Estoy bien..."*, *"—A que no puedo. Sí puedo, o sea, puedo..."*, *"—Es que si no la cambio yo—"*, *"—No, o sea… ¿para qué?... —Se calló."*, *"La taza, digo."*, *"No, no te la seques, pobrecita..."*) — mi propio conteo anterior de 3,1% estaba mal, no el texto. Dejo la nota para Loreto: el script no subió el conteo absoluto de 13 a pesar de que el tramo 4 agrega interrupciones reales nuevas (*"prefiero no tener que… es más eficiente. Nomás."*, *"Tenía una tesis que… tenía que"*), así que su detector de habla real tiene un techo o un patrón que no está cazando — pero el contenido real está bien, así que no bloqueo por esto.
- ✅ **Resuelto** — voz_autoral §4 (parlamentos de Renée ≥45 palabras): subió de 4 a ~8 en el capítulo completo (elogio, taza, hombros, vergüenza son las 4 nuevas), tocando el piso exacto que exige la regla.
- 🟡 **Sin resolver** — M1 tics (*"la doctora sintió"* ×4, *"la doctora se quedó"* ×4, *"el labio de abajo"* ×4): siguen en S1, sin variar. Aviso, no duro.
- 🟡 **Sin resolver** — el valle cocina/limón (línea ~85-93 y ~217): sigue siendo el tramo más frío del capítulo. Releído con cuidado, no es trámite puro (el muslo y la mirada a la boca corren por debajo mientras habla de la cocina), pero mecánicamente es la zona con menos cuerpo por cien palabras del capítulo, igual que en v0.2.

Esto no bloquea el capítulo — son avisos, no umbrales duros — pero es la razón de que este veredicto sea MICRO-FIX y no un APROBADO limpio: hay fixes concretos, ya recetados una vez, todavía pendientes.

---

## 1. Inmersión (anti-metadata)
✅ Archivo `capitulo_1_el_cajon_v0.3.md` completo (442 líneas, 11.486 palabras) es prosa pura de principio a fin. Sin autoverificación, sin listas M1-M17, sin etiquetas de beat, sin conteos visibles, ni en las líneas de S1 ni en las de S2.

## 1b. 🩸 Humanización (anti-prosa-de-IA)

| # | Métrica | Umbral | Contado por mí | Declaró el Escritor | ¿Coincide? |
|---|---|---|---|---|---|
| H1 | Tricolones (relleno) | ≤2/escena | ~7 repartidos en 4-5 escenas reales (ascensor 1, living S1 2, casa/lavatorio 2, living S2 2) — dentro de cupo. El "×63" que reporta Loreto es el mismo fallo de segmentación ya señalado en v0.2 (ve "1 escena(s)" en un capítulo con al menos 4 ambientes) | 2 en la S2 (uno podado) | Parcial — Loreto sigue sin segmentar escenas para este tipo de capítulo largo de sesión única; no es una falla real del texto |
| H2 | «no era X, era Y» | ≤1 por cap | 1 (*"no fue por el ruido. Fue por el muslo"*, S1) | 1 | ✅ |
| H3 | Frases-remate (relleno) | ≤6 | 4 (*"No vino eso."* · *"Sin manos encima."* · *"Cerró la llave."* · *"Se la puso."*, esta última nueva de S2 y funciona como imagen-ancla, no relleno) | 2 en el tramo | ✅ dentro de cupo |
| H4 | Abstractos del tema | 0 | 0 — grep de *alivio/permiso/rendición/control/sumisión/degradación* en narración: cero | 0 | ✅ |
| H5 | «algo» comodín | ≤2 | 2 reales fuera de diálogo (*"Es algo acotado"*, *"¿Tiene algo antes?"*) | 0 en el tramo | ✅ |
| H6 | Dobletes de adjetivos | ≤3 | 3 (*"tibia y espesa"*, *"corto, descuidado"*, *"tibias y blandas"* — nueva de S2) | 1 en el tramo | ✅ dentro de cupo, justo en el límite |
| H7 | Variación elegante | 0 | 0 | 0 | ✅ |
| H8 | Varianza de frase | cumple | cumple en todas las ventanas de 500 (confirmado por Loreto: "Cumple en todas las ventanas. ✅") | cumple | ✅ |
| H9 | Lastre (L2/L4) | presente | presente (*"a veces el… a veces pedimos"*, L2; *"Y que ella no sabía qué hacía Renée con las manos…"*, L2 nueva de S2) | presente | ✅ |
| H10 | Ritmo de cláusula (M13) | JSD ≥0,02 vs previos | no medible — Cap 1 del relato, sin capítulo previo | — | N/A, no aplica todavía |
| H11 | Dos puntos revelatorios (M14) | ≤1,5/1000 | 0 | 0 | ✅ |
| H12 | Símil-molde (M15) | ≤1,0/1000 | 0 | 0 | ✅ |
| H13 | Recibo de excitación (M16) | ≤2/cap | 0 | 0 | ✅ |
| H14 | Habla real (M17) | ≥10% | 15,1% (13/86) — ver §0 arriba sobre la discrepancia de conteo | 3 interrupciones nuevas declaradas en el tramo | ✅ (corrige mi propio error de conteo en v0.2) |

**Veredicto de humanización:** ✅ LIMPIO. Todos los umbrales duros (H4, H7) en cero; el resto dentro de cupo o con explicación de falso positivo de Loreto documentada arriba.

**Citas de los peores tells (máx 3):**
- *"la doctora sintió"* / *"la doctora se quedó"* — tic de M1, no de H1-H14, pero repetido 4 veces cada uno en 11.486 palabras. No es un tell de IA, es un hábito de redacción que conviene variar en la próxima pasada (ver micro-fixes).
- El fallo de segmentación de `medir_capitulo.py` ("1 escena(s)" para un capítulo con ascensor + living S1 + casa/lavatorio + living S2) sigue sin corregirse desde que lo señalé en `validacion_v0.2.md`. Recomiendo a Loreto tratarlo antes de que el próximo capítulo de sesión larga vuelva a inflar H1.

## 1.5 Continuidad (cronología + costura + hechos plantados)
- **Línea de tiempo:** ✅ Cero días marcados en las 442 líneas. Verificado con lectura completa: ni "martes/lunes", ni conteos ("+N días"), ni fechas de calendario. Anclas usadas: *"esa misma noche"*, *"a la una y media"* (hora de reloj, no día), *"a las tres"*, *"la luz de las cuatro"*, *"la hora pedida"* — todas relativas por evento u hora del día, tal como exige `cronologia.md` §1.
- **Costura con cap previo:** N/A formal (es el Cap 1). Costura interna verificada entre las cuatro escenas: el estado con que abre S2 (credencial sacada en el auto y repuesta en el ascensor, mismo pantalón del hospital, blusa de seda nueva, labial puesto y sacado) coincide exactamente con el cierre de "esa misma noche" (mensaje enviado a la 1:32, cita confirmada "mañana a las cuatro"). `cronologia.md` §4 registra correctamente el estado de cierre de la S2.
- **Callbacks con ancla:** ✅ Verifiqué los Hechos Plantados nuevos/pagados de esta versión contra el texto real: H24 (*"la prueba... con variable y todo"* → *"La otra vez fue una prueba, con variable y todo, y hoy entraste y lo guardaste antes de sentarte"*, línea 341, verbatim) · H26 (*"¿Y con quién consultó? Lo del segundito"* → *"Con quien tengo que consultar, linda. Esa no es tuya todavía"*, línea 359-363, verbatim) · H21 (escalera de cariños: *corazón* pasa entero en línea 371-373, *mi niña* pasa sin reacción en línea 419) · H18 (voz de abajo escala a *no lo suelto.* y *gracias.*, líneas 401 y 411, consistente con la secuencia declarada) · H19 (el refrán *"Jefa de turno..."* pierde la edad, línea 439, consistente con la escalada declarada) · H9/H26 (roce de Anaïs, coherente con Roce 1/1bis de la noche anterior). Ningún callback sin origen escrito.
- **Huecos a corregir:** ninguno. El único punto que queda deliberadamente abierto (qué contestó Renée a *"¿Cuándo puedo volver?"* y qué pasa con la hora ya agendada de S1) está correctamente documentado en `cronologia.md` H29 como decisión pendiente para el Escritor del Cap 2, no como hueco de este capítulo.

## 2. Narrativa

### Pivotes del canon cumplidos
- ✅ **Pivote 1 — La custodia cambia de manos** (S1, sin cambios respecto a v0.2, ya validado): rampa de tres movimientos cumplida.
- ✅ **Pivote 2 — El cuerpo cede antes que la cabeza** (S2, nuevo — el motivo real de este tramo): *"Se le mojó el coño. Sentada, vestida, con la taza de té en las manos y las manos de Renée recién sacadas de encima de las suyas y nadie tocándola en ninguna parte, se le mojó."* El error fatal que el canon prohíbe explícitamente (*"que ella lo decida primero. Si decide y el cuerpo obedece, es sumisión de guion, no de alivio"*) se evita con precisión de relojería: es Renée quien decide (*"Fideos."*), la doctora dice *ya*, y **recién después** viene el aflojar del cuerpo (aire, mandíbula, ojos, y por último la humedad) — nunca al revés. Emoción objetivo cumplida: descanso + humillación íntima + un calor que empieza en la garganta y baja (*"Ahí. En la garganta, donde había estado el aire, un calor redondo que le bajó por el esternón..."*).
- No aplican Pivotes 3-5 (capítulos posteriores).

### Calidad técnica
- **POV:** estable, tercera persona limitada en la doctora, sin fugas, en las cuatro escenas.
- **Vocabulario chileno:** ✅ Verificado en el tramo nuevo: *"po"* (×2, chilenismo correcto, no España), *"nomás"*, *"al tiro"*, tú pleno sin una sola forma de voceo (querís/tenís/sabís/podís/estái/vos).
- **Buzzwords AI:** ninguna detectada.
- **Tics a podar (M1, aviso, no duro):** *"la doctora sintió"* ×4, *"la doctora se quedó"* ×4, *"el labio de abajo"* ×4 — sin variar desde v0.2 porque S1 no se tocó. No son duros (ninguno llega a 9 palabras verbatim) pero siguen pendientes del micro-fix anterior.

### Score Narrativa: 8.8
Prosa técnicamente sólida en las cuatro escenas, Pivote 2 ejecutado con el orden exacto que exigía el canon (cuerpo antes que decisión), Renée consistente y ahora con el peso de parlamento que le faltaba. No llega a 9.0 porque dos de los cuatro micro-fixes que receté sobre v0.2 (tics de M1, valle cocina/limón) siguen sin aplicarse — son detalles menores, pero son detalles ya identificados y no ejecutados, y "ya está identificado" no es lo mismo que "ya está resuelto".

---

## 3. 🔥 Temperatura — ¿es erótico? ¿está caliente?

| # | Medida | Resultado |
|---|--------|-----------|
| T1 | **¿Es erótico?** (¿sobrevive el cap si le sacás el sexo?) | ✅ **erótico.** Sin la respuesta física (muslo, pulso, aflojar, humedad, descarga) esto es una doctora cansada contándole su día a una desconocida dos veces. El mecanismo entero —custodia del teléfono, la taza puesta en las manos, la humedad de puro alivio— es sexual desde la raíz |
| T2 | **¿Calienta?** (juicio directo; ¿el deseo se lee en las dos, o solo se excita una?) | ✅ **sí, y el tramo nuevo sube el promedio del capítulo.** Sobre la sub-medida del deseo mutuo: acá el diseño es **deliberadamente asimétrico** (`canon_relato.md` §4bis, `investigacion.md` §2b: *"Renée aporta el permiso... la paciente aporta el calor"*) — no es el defecto de "Lo que Pediste" (donde el diseño exigía mutualidad y no la tenía). Renée sí tiene su propio motor visible aunque no sexual hacia la doctora: el gesto de tocarse las perlas *"igual que se toca un anillo que no se saca"* al esquivar la pregunta sobre Anaïs es su propio cuerpo delatando ALGO, aunque no sea deseo por la paciente. Esto es coherente con el encargo, no un hueco |
| T3 | Explicitud léxica (¿nombra o esquiva?) | ✅ Nombra en el pico: *coño*×15, *tetas*×6, *mojado/mojada*×7, *clítoris*×2, *correrse*×2 (4,9/1000 total). 2 eufemismos evasivos reales (*"la humedad"* ×2, S1, ambos después de *"chorreando"* explícito en la misma frase — variación de registro, no evasión). El tercero que marca Loreto (*"ahí abajo"*) sigue siendo falso positivo — se refiere a los tacos, no al cuerpo |
| T4 | Suciedad del registro vs `antologia_calenton.md` | ✅ El registro se ensucia en el pico (coño, mojada, clítoris) y vuelve a lo táctil-tierno entre picos — exactamente el tono que `investigacion.md` §2b pide para ESTE relato ("tierno hasta en lo duro", nunca el registro de burdel de otros relatos de la casa). La densidad más baja que el piso de `voz_autoral.md` (8,5-13,6/1000) es apropiada al registro de esta historia específica, no una falla transversal |
| T5 | Descarga real en escena (no elipsis) | ✅ La masturbación del lavatorio (S1) está completa, en página, contando contracciones, sin corte de cámara. El Pivote 2 (S2) no es una descarga/orgasmo — por diseño no lo es (`canon_relato.md` §2, Pivote 2: "el cuerpo se adelanta", no un clímax) — así que no aplica el requisito de descarga completa ahí |
| T6 | Densidad de subrayables | 4,9/1000 (mínimo 4) — con anclaje anatómico real en más de la mitad de las citas (coño, mojada, tetas, clítoris aparecen directamente, no solo atmósfera) |
| T7 | Motivos permanentes **por escena** · curva de resistencia | ✅ Verifiqué los 6 motivos en la escena nueva (S2) uno por uno: credencial erosionándose (sacada y repuesta) ✓ · cansancio físico escalando (mandíbula que se suelta y **duele** al soltarse, primera vez en el capítulo) ✓ · cero órdenes directas (revisé cada parlamento de Renée; los imperativos que quedan son del mismo registro ya aceptado en v0.2 — "no los muevas", "no te la seques" — correcciones de detalle físico, nunca el acto de rendición en sí, consistente con la confirmación de la Ama del 08/09) ✓ · diminutivo en las 15 intervenciones de Renée ✓ · hambre de la conversa/Anaïs (Roce 2bis: *"con quien tengo que consultar... esa no es tuya todavía"*) ✓ · pregunta con respuesta adentro (*"¿Y quién te pidió cada una de esas cosas?... Nadie y todos"*) ✓. **Curva:** correctamente sin cruzar — trata a Renée de usted toda la hora, sigue funcionando bien en el pase de visita, ninguna frase de rendición dicha; el cruce sigue reservado para Cap 2/S3 tal como exige §4c |
| T8 | Apertura (primeras 500 palabras enganchan) | ✅ sin cambios respecto a v0.2 (la apertura es S1, no tocada): *"El muslo le avisó antes que el teléfono"* sigue siendo un gancho de cuerpo desde la primera línea |
| T9 | Distribución erótica + cierre-gancho | ✅ **Este es el punto donde el tramo nuevo rinde más.** Carga distribuida en 4 escenas (ascensor, S1, esa noche, S2), no comprimida al final. Dentro de S2 misma hay progresión (elogio envenenado con calor que "baja" en vez de subir a la cara → la decisión de los fideos → el aflojar completo → la humedad). **Cierre:** *"...y la doctora se quedó en el pasillo esperando la respuesta con las rodillas blandas y el coño mojado debajo del pantalón del hospital, igual que había esperado frente al espejo, con el dedo quieto, que alguien la dejara moverse."* Cumple las dos exigencias de T9b: es el beat más caliente en imagen (callback directo y anclado al orgasmo del lavatorio) Y es un gancho real sin resolver (Renée no contesta en página si puede volver) — mejora incluso el diseño del canon, que preveía la respuesta de Renée en el cierre y acá queda deliberadamente fuera de página, subiendo la tensión hacia el Cap 2 |

### Las 3 frases MÁS CALIENTES del capítulo
1. *"Se le mojó el coño. Sentada, vestida, con la taza de té en las manos y las manos de Renée recién sacadas de encima de las suyas y nadie tocándola en ninguna parte, se le mojó."* — Pivote 2, el entregable central de este tramo.
2. *"Mojada de que le hubieran abierto los dedos con una taza y le hubieran dicho fideos."* — combina humillación íntima (la decisión que no tomó) con la imagen física en ocho palabras.
3. *"El pulgar de Renée se movió. Un centímetro, hacia arriba por la cara interna del antebrazo, un roce que no hacía falta para contar nada, [...] y el pantalón le pasó por el coño con el apretón, seco, una sola vez, y le dejó ahí un calor que no se fue con el pulgar."* (S1, sigue siendo de lo más caliente del capítulo completo).

### Los 2 pasajes MÁS FRÍOS (a reescribir o apretar)
> Ninguno de los seis tramos M4 de Loreto llega a 🔴 (todos son 🟡; ninguno trae vocabulario de trámite ni pasa de 300 palabras). Elijo los dos más planos por lectura directa, no por umbral duro.
1. *"A las tres se encerró en el baño del servicio con la cartera. Se sacó la blusa del turno y se puso la otra, la de seda... y se lo sacó con papel al tiro, y le quedó el color igual, más bajo..."* — el cambio de blusa y el labial son un motivo importante (H28, el segundo motor en gesto), pero leído solo es logística de vestuario sin cuerpo encima; sería más fuerte con una frase de garganta/mandíbula/mirada en medio del gesto, igual que el resto del capítulo hace en cada trámite. Caso C1 rozado, no fallado.
2. *"Renée la escuchaba con la taza entre los dedos. Asentía. No anotaba. [...] La doctora sintió el talón libre recién cuando Renée lo dijo."* (S1, sin cambios) — sigue siendo el mismo valle que señalé en `validacion_v0.2.md` y que el brief de tramo 4 no tocó por diseño (no se editó S1). No bloquea, pero es el candidato más claro para una pasada futura si se vuelve a tocar S1.

### Eufemismos evasivos detectados
2 reales: *"la humedad"* ×2 (S1, ambas después de *"chorreando"* explícito en la misma frase). El tercero marcado por Loreto (*"ahí abajo"*) es falso positivo — se refiere a los tacos bajo el sillón.

### Score Temperatura: 8.8
T1 y T2 pasan con margen. Sube sobre el v0.2 (8.6) porque el Pivote 2 —que faltaba— es exactamente el que el canon diseñó como el más caliente del capítulo, y el cierre nuevo mejora el gancho hacia el Cap 2. No sube más por el valle repetido de S1 (sin tocar) y porque la densidad léxica global (4,9/1000) sigue en el piso de lo aceptable para el registro de este relato específico, sin margen de sobra.

---

## 4. Voz Autoral

### Tics canónicos activados
Circuito cuerpo→cabeza→escudo-que-cae corriendo ≥2 veces en la escena nueva (sonrisa antes de entender el elogio → escudo *Me está felicitando por guardar el teléfono. Y estoy sonriendo.* ; *ya* antes de la objeción que nunca llega → escudo *Fideos. Me dijo fideos y yo dije ya.* ; mojada antes de la frase → escudo *Estoy mojada con una taza de té en las manos y nadie me ha tocado.*) · voz de abajo escalando sin repetirse (*no sueltes. → quédate. → mírate. → déjame a mí. → doctora. → no lo suelto. → gracias.*) · el refrán de la cabeza pierde datos en cada repetición (*"Tengo cuarenta y un años, soy jefa de turno, y estoy descalza..."* → *"Cuarenta y un años, jefa de turno, sopesándome las tetas..."* → *"Jefa de turno. En un pasillo, con los tacos puestos..."*, sin la edad).

**Perfil medido §0:** cursiva 2,4/1000 (referencias 2,3-5,3 — dentro del piso de la referencia más baja, no un fallo real) · parlamentos ≥45 palabras de Renée ≈8 en el capítulo completo (toca el piso exacto de la regla, gracias a los 4 nuevos del tramo: elogio, taza, hombros, vergüenza) · circuito cuerpo-antes-que-cabeza ≥2 veces en la escena erótica nueva ✓ · palabra cruda en el pico de la descarga (lavatorio) y del Pivote 2 (*coño* en la frase misma de la humedad) ✓ · espejo con las manos encima (S1, sin cambios) ✓ · cuarta pared no aplica a este relato (tercera persona sin dirección directa al lector — diseño estructural, no hueco). Menos de dos criterios reales por debajo de umbral → Voz ✅.

**La prueba de la Declaración ("hacer sentir que está ahí"):** cumplida en la escena nueva — la taza tibia, el aire que sale largo, la mandíbula que duele al soltarse, las perlas con la luz de las cuatro, el labial sacado con papel. Se afloja en el mismo tramo que Temperatura marca como valle (cambio de blusa en el baño del servicio), consistente con el patrón ya visto en v0.2.

### Frases nuevas candidatas para incorporar a `voz_autoral.md`
- *"No se la ofreció. Se la puso."* — ejecuta la imagen ancla del canon (§5, la taza) en cuatro palabras exactas.
- *"Fideos. Me dijo fideos y yo dije ya."* — la decisión que no tomó, dicha con la economía justa.
- *"Qué rico que te dé vergüenza, doctora [...] La vergüenza es la única que te avisa que vas avanzando, ¿sabías? Cuando no te dé vergüenza vamos a tener que preocuparnos."* — el reencuadre del canon (`investigacion.md` §2, punto 2) ejecutado en Renée con la calma exacta que le corresponde.

---

## 5. Micro-fixes sugeridos

1. **M1 — tics de S1 (heredado de `validacion_v0.2.md`, sin aplicar):** variar 2 de las 4 repeticiones de *"la doctora sintió"* / *"la doctora se quedó"* / *"el labio de abajo"*. No afecta estructura ni curva.
2. **Valle cocina/limón (S1, líneas ~85-93 y ~217, heredado de `validacion_v0.2.md`):** sumar una frase de cuerpo (postura, mandíbula, mirada) dentro del bloque donde Renée escucha sin anotar, para que ese tramo no quede solo informativo — igual que el resto del capítulo intercala cuerpo en cada trámite.
3. **Baño del servicio (S2, línea ~319, nuevo hallazgo):** el cambio de blusa y el labial son un motivo importante (H28) pero se leen como logística de vestuario; una frase de garganta/mirada al espejo en medio del gesto (como ya hace el resto del capítulo) lo sube de temperatura sin agregar largo.

Ninguno de los tres requiere tocar estructura, curva, candados ni pivotes — son ediciones locales que el Escritor puede aplicar directo sobre el archivo, sin nueva vuelta completa de Validador, salvo que la Ama prefiera una relectura de Loreto para confirmar que los tics de M1 bajaron.

## 6. Notas

- El tramo nuevo (Sesión 2) es el trabajo más sólido de esta versión: ejecuta el Pivote 2 con el orden exacto que el canon exige (cuerpo antes que decisión, nunca al revés), sube el peso de parlamento de Renée al piso que pedía `voz_autoral.md`, y mejora el cierre-gancho del capítulo entero sobre lo que el propio mapa de capítulos preveía.
- Corrijo un error propio: en `validacion_v0.2.md` conté H14 a mano como 3,1% y lo marqué como fallo duro. Con una relectura más cuidadosa del texto completo confirmo que el conteo mecánico de Loreto (13/65 entonces, 15,1% ahora) estaba más cerca de la realidad que mi conteo manual. Quede registrado para que el próximo Validador no repita mi subestimación.
- Los dos micro-fixes de v0.2 que no se aplicaron no son un incumplimiento del Escritor: el brief de tramo 4 ordenó explícitamente no tocar S1. Es una decisión válida del Orquestador (priorizar el tramo nuevo, dejar el pulido de S1 para una pasada posterior), pero como Validador la reporto igual porque sigue siendo trabajo pendiente antes del Gate.
- Destino recomendado: el Escritor aplica los 3 micro-fixes de arriba directamente sobre el archivo (ediciones locales, no estructurales) y el capítulo puede pasar a Gate de la Ama sin una nueva vuelta completa por Validador, salvo que ella prefiera confirmar con una relectura de Loreto.

---

VALIDADOR_RESULT:{"veredicto":"MICRO-FIX","inmersion":"OK","continuidad":"OK","es_erotico":"SI","calienta":"SI","narrativa":8.8,"temperatura":8.8,"voz":"OK","subrayables":4.9,"eufemismos_evasivos":2,"motivos_permanentes_faltantes":0,"micro_fixes_n":3,"huecos_continuidad_n":0,"destino":"escritor","reporte":"reportes/capitulo_1/validacion_v0.3.md"}
