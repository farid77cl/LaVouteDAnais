# Validación — Capítulo 1 «El cajón» v0.2
Validador Nivel 4 · 2026-09-08

**Veredicto:** MICRO-FIX
**Medición mecánica (Fase 2.5):** 🟡 AVISOS (`medicion_v0.2.md`) — sin duros; ya corrida una pasada correctiva sobre la apertura
**Casos de la Ama que reinciden:** C17 (habla real, M17 🔴) · C7 (origen de este rework — evaluado como ATENDIDO, no reincidente) · C1/C5 (rozados, no fallados, en el tramo cocina/limón) · C14 (riesgo leve, no fallado)
**Inmersión:** ✅
**Continuidad:** ✅
**Narrativa:** 8.7
**Temperatura:** 8.6
**Voz autoral:** ✅ (una de seis sub-medidas por debajo de umbral — no alcanza el "dos fallan" que dispara ❌)

---

## 0. Contexto que gobernó esta lectura

Este NO es un capítulo nuevo: es un rework sobre una nota editorial de la Ama que manda sobre canon, investigación y mi propia rúbrica. Leí el canon **enmendado** (§3 Renée conduce/condescendiente-seductora, §4bis segundo motor, §4c rampa en tres movimientos), no el original. Comparé v0.1 contra v0.2 punto por punto de la nota antes de puntuar nada.

**§1c — chequeo de reciclaje (obligatorio en rework):** v0.2 **no es** el pasaje rechazado con retoques cosméticos. Comparé los tres bloques que la nota señaló directamente:
- **La entrega del teléfono:** v0.1 la resuelve en un párrafo (*"Lo pensó con todas las letras, esto es ridículo... y mientras lo pensaba la mano ya lo había levantado"*) — objeción y rendición en la misma frase, exactamente lo que ella marcó como *"muy rápido y casi sin motivo"*. v0.2 la reparte en tres movimientos separados por página y media de material nuevo (pregunta → cambio de tema → cocina/limón como elefante en la pieza → ella vuelve sola con un motivo nombrable, "es una prueba", "aislar la variable"). Estructura distinta, no retoque.
- **El remate del lavatorio:** v0.1, textual, *"en la cabeza no había ninguna cara, ningún cuerpo encima, solo un cajón cerrándose"*. v0.2 reescribe la escena entera para que la cara de Renée (boca mate, la palabra *doctora*) esté encima del cajón, y la vergüenza se duplique (*"la del teléfono... la otra... no tenía forma de frase, tenía forma de boca"*). Es el arreglo central de la nota y está hecho desde la arquitectura de la escena, no pegado encima.
- **Renée en la sesión:** v0.1 le hace una sola pregunta (*"¿Puedo preguntarte una cosa?"*) y el resto es silencio que trabaja solo. v0.2 la tiene tomando la iniciativa en cada beat (arrastra el sillón con la canilla, toma el pulso, se para atrás y pone las manos, corrige el mechón, levanta la credencial) — es un personaje reescrito, no la misma Renée con más diálogo.

**Veredicto del chequeo: rework genuino.** No aplica el override de "veredicto = el de la versión anterior".

---

## 1. Inmersión (anti-metadata)
✅ El archivo `capitulo_1_el_cajon_v0.2.md` es prosa pura de principio a fin. Sin autoverificación, sin listas M1-M17, sin etiquetas de beat, sin conteos visibles. Nada que romper.

## 1b. 🩸 Humanización (anti-prosa-de-IA)

| # | Métrica | Umbral | Contado por mí | Declaró el Escritor | ¿Coincide? |
|---|---|---|---|---|---|
| H1 | Tricolones (relleno) | ≤2/escena | ~6 repartidos en 4 escenas reales (living 2, cajón 2, casa 1, lavatorio 1) — dentro de cupo. **El contador mecánico de Loreto detectó "1 escena" para todo el capítulo y reportó ×47** — es un fallo de segmentación de escenas, no un hallazgo real; casi todos son falsos positivos de regex sobre comas | living 2 · cajón 2 · casa 1 · lavatorio 1 | Parcial — el splitter de Loreto no coincide con las escenas reales, el conteo del Escritor sí es plausible tras spot-check |
| H2 | «no era X, era Y» | ≤1 por cap | 1 (*"no fue por el ruido. Fue por el muslo"*) | 1 (tras corregir de 6 a 1) | ✅ |
| H3 | Frases-remate (relleno) | ≤6 | 3 | 4 | ✅ (ambos dentro de cupo) |
| H4 | Abstractos del tema | 0 | 0 | 0 | ✅ |
| H5 | «algo» comodín | ≤2 | 2 reales fuera de diálogo (*"Es algo acotado"*, *"¿Tiene algo antes?"* como mensaje) — el 4º que cuenta Loreto (*"Empecemos por algo chiquitito"*) es diálogo de Renée, mal clasificado como narración por el script | 1 en narración | Parcial — clasificador de Loreto con error, no violación real |
| H6 | Dobletes de adjetivos | ≤3 | 2 (*"tibia y espesa"*, *"corto, descuidado"*) | 2 | ✅ |
| H7 | Variación elegante | 0 | 0 | 0 | ✅ |
| H8 | Varianza de frase | cumple | cumple (fragmentos de 1-3 palabras contra olas de 60-90) | cumple | ✅ |
| H9 | Lastre (L2/L4) | presente | presente (*"a veces el… a veces pedimos"*, *"es que llevo todo el día…"*) | presente | ✅ |
| H10 | Ritmo de cláusula (M13) | JSD ≥0,02 vs previos | **no medible** — es el Cap 1 del relato, no hay capítulo previo contra el cual medir JSD | — | N/A, no falla, no aplica todavía |
| H11 | Dos puntos revelatorios (M14) | ≤1,5/1000 | 0 | 0 | ✅ |
| H12 | Símil-molde (M15) | ≤1,0/1000 | 0 | 0 | ✅ |
| H13 | Recibo de excitación (M16) | ≤2/cap | 0 | 0 | ✅ |
| H14 | Habla real (M17) | ≥10% de parlamentos | **3,1% de 65 parlamentos** — 🔴 bajo el piso | estimó "≥20%" en su autoverificación, contradicho por la medición real de Loreto | ❌ **no coincide — el Escritor sobreestimó su propio conteo** |

**Veredicto de humanización:** 🟡 MICRO-FIX. Un solo fallo real y duro (H14/**C17**): con 65 parlamentos y solo 2 con interrupción o palabra comida, el diálogo suena demasiado terminado, demasiado ordenado — exactamente el tell que hizo decir a la Ama *"se está notando demasiado que es escrito por IA"* en otro relato. Nadie en esta hora se traba, repite una palabra o corta una frase a medias salvo la doctora dos veces. Renée en particular no titubea ni una vez en 30 y tantas intervenciones, y eso — sumado a que nunca sube la voz ni se apura — la acerca al límite entre "calma canónica" y "diálogo de máquina".

**Citas de los peores tells (máx 3):**
- *"—No, o sea… ¿para qué? —Le salió más alto de lo que quería—. Es el teléfono del servicio."* — de los DOS únicos parlamentos con habla real en todo el capítulo. Se necesitan más como este, sobre todo del lado de la doctora en el tramo del cuestionamiento y de Renée en algún punto donde su calma se raje un segundo (una palabra que no encuentra, un "o sea" que se le escapa) — sin romper su invariante de nunca subir el volumen.
- El fallo de segmentación de escenas de `medir_capitulo.py` (**"1 escena(s)"** para 7.624 palabras con al menos 4 ambientes distintos) infla artificialmente el conteo de H1 a ×47 y produce ruido que un lector humano de este reporte podría confundir con una falla real. Aviso para Loreto, no para el Escritor.

## 1.5 Continuidad (cronología + costura + hechos plantados)
- **Línea de tiempo:** ✅ Cero días marcados. Verifiqué explícitamente: no hay "martes", ni conteos ("+N días"), ni fechas. El ritmo se lleva por evento (*"esa misma noche"*, *"la una y media de la mañana"* — hora del reloj, no día) y por sesión, tal como exige `cronologia.md` §1.
- **Costura con cap previo:** ✅ N/A formalmente (es el Cap 1, no hay capítulo anterior), pero la costura interna cierra: el estado con el que abre cada escena coincide con el que dejó la anterior (teléfono, tacos, mandíbula, credencial), y `cronologia.md` §4 registra correctamente el estado de cierre.
- **Callbacks con ancla:** ✅ No hay ninguna referencia a un evento no escrito en este mismo capítulo. Verifiqué los 25 Hechos Plantados de `cronologia.md` §3 contra el texto real, con spot-check línea por línea en los más sensibles (H1 cajón/terciopelo/clac, H2 zapatito, H9 roce Anaïs 1 y 1bis, H16 mensaje, H18 secuencia de voz de abajo, H19 refrán, H21 «mi… doctora, perdón», H24 la prueba, H25 «doctora» sin voz) — **todos coinciden verbatim o casi verbatim con lo escrito.** La cronología no inventó ningún ancla que el texto no sostenga.
- **Huecos a corregir:** ninguno.

## 2. Narrativa

### Pivotes del canon cumplidos
- ✅ **Pivote 1 — La custodia cambia de manos:** cumplido en escena, con la rampa de tres movimientos exigida por §4c: *"Abrió el cajoncito. Le costó, la madera se trabó a la mitad... Lo dio vuelta... y lo puso. Boca abajo sobre el terciopelo."* → *"Y entonces el muslo esperó."* El error fatal que el canon prohíbe (que ella lo acepte con gusto a la primera) no ocurre: hay cuestionamiento, elefante en la pieza y motivo propio antes de la entrega.
- ⚠️ **Pivote 2 — El cuerpo cede antes que la cabeza (cierre S2, taza en las manos, «Esa la conversamos la próxima»):** **NO está en v0.2.** Esto es el pendiente declarado en el brief: el canon §6 pone S2 dentro del Cap 1, pero el plan de tramos del Orquestador cerró el capítulo en E3 (esa misma noche). **No lo cuento como pivote incumplido por el Escritor** — es una decisión pendiente de la Ama/Orquestador (tramo 4 vs. apertura del Cap 2), correctamente marcada en `cronologia.md` [4] y en la autoverificación. Lo señalo para que quede en el registro, no como demérito de esta versión.
- No aplican Pivotes 3-5 (capítulos posteriores).

### Calidad técnica
- **POV:** estable, tercera persona limitada en la doctora, sin fugas.
- **Vocabulario chileno:** ✅ Verificado — "tú" en todo el capítulo, ni una forma de voceo argentino ni chileno (querís/tenís/sabís/podís/estái). Corrige limpio la violación que tenía v0.1 en otro punto del relato (ver `canon_relato.md` §7).
- **Buzzwords AI:** ninguna detectada (sin "crucial", "tapiz", "intrincado", "profundizar").
- **Tics a podar (M1, aviso, no duro):** *"la doctora sintió"* ×4, *"la doctora se quedó"* ×4, *"el labio de abajo"* ×4. Ninguno es duro (≥9 palabras verbatim), pero dos o tres variaciones bajarían el ruido de fondo.
- **Falso positivo de Loreto:** T3 marca *"ahí abajo"* como eufemismo evasivo — en el texto real se refiere a los **tacos en el suelo** (*"los dos tacos quedaron ahí abajo, ladeados"*), no a genitales. No es una falla de explicitud; corrijo el conteo real de eufemismos a **2** (las dos instancias de *"la humedad"*, ambas después de que ya apareció *"chorreando"* explícito en la misma frase/párrafo — variación de registro, no evasión real).

### Score Narrativa: 8.7
Prosa técnicamente sólida, pivote 1 cumplido con la arquitectura exacta que pidió la nota, personaje de Renée reescrito con consistencia. No llega a 9.0 por: el hueco declarado de Pivote 2 (aunque no es culpa de esta versión), los tics de M1 sin podar, y el problema de habla real (H14/C17) que también afecta la calidad técnica del diálogo, no solo la humanización.

---

## 3. 🔥 Temperatura — ¿es erótico? ¿está caliente?

| # | Medida | Resultado |
|---|--------|-----------|
| T1 | **¿Es erótico?** (¿sobrevive el cap si le sacás el sexo?) | ✅ **erótico.** Sin la respuesta física (muslo, pulso, aflojar, descarga), esto es una escena de trámite: una doctora cansada hablando de su día con una desconocida. El mecanismo entero —custodia del teléfono como sustituto de rendición— es sexual desde la raíz; sacado el cuerpo, no queda historia |
| T2 | **¿Calienta?** (juicio directo, con evidencia; ¿el deseo se lee en las dos, o solo se excita una?) | ✅ **sí, con una zona floja.** Sube de "tibio" (v0.1) a "caliente" en los tramos de contacto y en el cierre. El deseo NO es mutuo en el sentido de "Lo que Pediste" — y **está bien que no lo sea**: el canon (§4bis, §2b de `investigacion.md`) diseña esto a propósito asimétrico: Renée seduce técnicamente (recluta para Anaïs), la doctora desea sin saberlo. No es el defecto que vetó ese otro caso; es el mecanismo declarado de este relato |
| T3 | Explicitud léxica (¿nombra o esquiva?) | ✅ Nombra en el pico: *coño*×8, *tetas*×5, *chorreando*×2, *clítoris*×2, *orgasmo*×1. Los "eufemismos" de Loreto son en su mayoría falso positivo (ver Narrativa) — 2 reales, y leves |
| T4 | Suciedad del registro vs `antologia_calenton.md` | ✅ El registro se ensucia en el pico y vuelve a la piel entre picos, consistente con el tono "tierno hasta en lo duro" que pide `investigacion.md` §2b para ESTE relato — no es Café con Piernas, es una fantasía de permiso, no de burdel; la densidad léxica más baja (4,7/1000) es apropiada al registro, no una falla |
| T5 | Descarga real en escena (no elipsis) | ✅ La masturbación en el lavatorio está completa, en página, sin corte de cámara, con conteo de contracciones y cierre físico (hombros que bajan) |
| T6 | Densidad de subrayables | ~4,5/1000 estimado (mínimo 4) — el capítulo tiene ~14 imágenes fuertes concentradas más en el segundo tercio; el primer tercio es más ralo, lo que coincide con la propia medición de Loreto (apertura 25,8% de cuerpo) |
| T7 | Motivos permanentes **por escena** · curva de resistencia | ✅ La credencial se erosiona en las tres escenas (torcida en el ascensor → enderezada por Renée → boca abajo en el lavatorio → cae al suelo); mandíbula/hombros escalan de "apretados" a "sueltos enteros" recién en el orgasmo; cero órdenes directas (verificado línea por línea, incluidas las imperativas menores — "Espera", "Cuéntame", "Mírame" — que son canon ya aprobado en `canon_relato.md` §9, no violan el invariante sustantivo de nunca mandar el acto de rendición); diminutivo en cada intervención de Renée; roce de Anaïs (1 y 1bis) presente. **Curva:** correctamente NO cedida — usted toda la hora, mi amor rechazado, rendición cero, tal como exige §4c del canon para el Cap 1 |
| T8 | Apertura (primeras 500 palabras enganchan) | ✅ cualitativamente — *"El muslo le avisó antes que el teléfono"* es un gancho de cuerpo desde la primera línea, y Renée abre la puerta antes de la palabra 350. Mecánicamente 25,8% de cuerpo en la apertura (bajo lo ideal), pero el enganche acá no depende de densidad genital sino de la imagen — juicio de lectora: sí engancha |
| T9 | Distribución erótica + cierre-gancho | ✅ Carga repartida en las tres escenas (muslo en el ascensor, pulso/hombros/cajón en la sesión, masturbación en la noche), no comprimida solo al final. Cierre: *"El coño se le contrajo con la palabra... la palabra ya estaba adentro"* — cierra en su beat más caliente y deja un gancho concreto (*"Mañana a las cuatro, doctora"*, adelantado desde una semana a la tarde siguiente) |

### Las 3 frases MÁS CALIENTES del capítulo
1. *"El pulgar de Renée se movió. Un centímetro, hacia arriba por la cara interna del antebrazo, un roce que no hacía falta para contar nada, y la frase de la doctora se quedó sin terminar porque abajo, donde tenía las piernas cruzadas, la de arriba apretó a la de abajo sin que ella la mandara, y el pantalón le pasó por el coño con el apretón, seco, una sola vez, y le dejó ahí un calor que no se fue con el pulgar."*
2. *"Las perlas frías contra la piel caliente de la nuca, un roce de cuentas duras arrastrándose de un lado al otro por encima del elástico del moño, y el frío le bajó por la columna entera hasta la silla del sillón y ahí se quedó, entre los glúteos apretados contra la tela, latiendo."*
3. *"Se vio los labios armarla, do-, la lengua contra los dientes, -tora, y la que la estaba diciendo ya era otra boca, una boca mate sin brillo diciéndosela al oído con las manos en los hombros, y el coño se le cerró sobre el dedo con la palabra."*

### Los 2 pasajes MÁS FRÍOS (a reescribir o apretar)
1. *"Le contó de la cocina igual, porque Renée le preguntó por la cocina, cómo era, cuánta luz tenía, si la mesa del comedor daba a la cocina o a la ventana, y la doctora contestó todo, la mesa, la ampolleta quemada del comedor que nadie cambiaba, la tesis de la alumna encima de la mesa con el lápiz rojo..."* — funciona como "elefante en la pieza" (el teléfono sigue zumbando bajo la palma mientras hablan de esto), pero el tramo en sí, leído solo, es descriptivo de la casa sin cuerpo encima. Es el tramo M4 🟡 de Loreto (línea 137). No es trámite puro (hay motivo permanente — la carga de la casa — corriendo debajo) pero es el valle real del capítulo.
2. *"Al patio, dijo la doctora... Un limón que no daba limones... y la doctora se escuchó reírse también..."* — el motivo del limón (plantado como H23 para reusar después) se repite tres veces en el capítulo y en esta primera aparición diluye más de lo que construye; el "elefante en la pieza" está mejor logrado un párrafo después (*"Cuatro zumbidos en cinco minutos y ninguna de las dos lo ha mirado"*) que en el propio chiste del limón.

### Eufemismos evasivos detectados
2 reales: *"la humedad"* ×2 (ambas después de *"chorreando"* explícito en la misma frase — variación, no evasión real). El tercero que marca Loreto (*"ahí abajo"*) es falso positivo — se refiere a los tacos, no al cuerpo.

### Score Temperatura: 8.6
T1 y T2 pasan. Sube claramente sobre v0.1 en los tres puntos que la nota pidió (Renée conduce, segundo motor con cara, rampa con motivo), y el cierre es el más caliente y mejor anclado del capítulo. No llega más alto por el valle real en el tramo cocina/limón (arriba) y porque la caída del % mecánico de cuerpo en narración, aunque parcialmente explicable por el tipo de contenido nuevo (deseo lateral vía mirada/atención, no vía léxico genital — exactamente lo que pide §4bis: *"el deseo entra por lo lateral, nunca por lo genital"*), también refleja un capítulo con un centro más hablado/pensado que los extremos.

---

## 4. Voz Autoral

### Tics canónicos activados
Circuito cuerpo→cabeza→escudo-que-cae (≥2 por escena erótica: pulso y cajón en la sesión; comedor y lavatorio en la noche) · cursiva en primera persona y voz de abajo escalando (*no sueltes. → quédate. → mírate. → déjame a mí. → doctora.*) · espejo con las manos encima, sopesándose las tetas y gustándose · refrán que escala sin repetirse verbatim (*"Tengo cuarenta y un años, soy jefa de turno, y estoy descalza..."* → *"Cuarenta y un años, jefa de turno, sopesándome las tetas..."*).

**Un criterio de §0 por debajo de umbral:** parlamentos de Renée ≥45 palabras = **6**, contra el piso de **8** que fija `voz_autoral.md` §4 para "quien domina la escena". No alcanza, por sí solo, el "si dos fallan, Voz ❌" (los otros cinco criterios —cursiva, circuito, palabra cruda en el pico de la descarga real, espejo, y cuarta pared no aplicable a este relato por diseño— pasan o no aplican). Pero es el mismo punto débil que produce el problema de H14: Renée habla con autoridad pero en parlamentos cortos y sintácticamente perfectos, y eso la acerca a "describe en vez de tentar" (**C14**) más de lo que el canon quiere para una Renée "seductora". El propio Escritor lo señaló en su autoverificación como tensión consciente entre el piso general de `voz_autoral.md` y el diseño específico de Renée "por debajo de lo decible" — es una llamada válida, pero dos líneas más largas (el Escritor ya identificó dónde: el zapatito y el limón) resuelven el hueco sin romper el registro.

**La prueba de la Declaración ("hacer sentir que está ahí"):** mayormente cumplida — la doctora reporta temperatura, textura, distancia y olor en casi cada intercambio. Se afloja exactamente en el mismo tramo que Temperatura marca como el más frío (cocina/limón), donde la escena se vuelve más contada que sentida.

### Frases nuevas candidatas para incorporar a `voz_autoral.md`
- *"No te subió cuando te tomé, doctora, te subió cuando te miré, que es distinto."* — condescendencia + observación clínica del cuerpo ajeno, muy Renée.
- *"Me lo has dicho cuatro veces con cuatro cosas distintas y todavía no te has dado cuenta de que es la misma frase."* — el reencuadre hecho frase.
- *"No te lo voy a agradecer, ¿ya? Porque no lo hiciste por mí, lo hiciste para ver, y eso es tuyo."* — devuelve el acto como propiedad de la paciente, mecanismo raíz (`investigacion.md` §2.0) ejecutado en una línea.

---

## 5. Micro-fixes sugeridos

1. **H14 / C17 — habla real (todo el capítulo):** agregar 3-4 interrupciones o muletillas más, repartidas — al menos una en boca de Renée sin que suba el volumen ni pierda el control (un "o sea" que se le escapa, una frase que empieza y cambia de idea a la mitad son suficientes; no hace falta que tartamudee). Objetivo: pasar de 3,1% a ≥10% de los 65 parlamentos.
2. **§4 voz_autoral — parlamentos de Renée:** estirar 2 intervenciones ya identificadas por el propio Escritor (la del zapatito, la del limón) a ≥45 palabras, sin agregar dirty talk — solo más observación del cuerpo, en su registro actual.
3. **M1 — tics:** variar 2 de las 4 repeticiones de *"la doctora sintió"* / *"la doctora se quedó"* / *"el labio de abajo"*.
4. **Tramo frío (línea ~137, cocina):** sumar una frase de cuerpo dentro del bloque de la casa/ampolleta/tesis — por ejemplo, algo que le pase a la doctora mientras describe su cocina (postura, garganta, mirada) para que el bloque no quede solo informativo.

## 6. Notas

- La ausencia de Pivote 2 / S2 es una decisión pendiente de la Ama/Orquestador (tramo 4 del Cap 1 vs. apertura Cap 2), correctamente documentada. No afecta este veredicto.
- Corrijo dos hallazgos mecánicos de Loreto que no son reales: (a) el eufemismo "ahí abajo" (se refiere a calzado, no a cuerpo); (b) el H1 ×47 (falla de segmentación de escenas — el script vio "1 escena" en un capítulo con al menos 4 ambientes). Recomiendo a Loreto revisar su detector de límites de escena para este tipo de capítulo de sesión única y larga.
- El Escritor estimó ≥20% de habla real en su autoverificación; Loreto midió 3,1%. Es la única discrepancia real entre lo declarado y lo medido — vale la pena que el Escritor recalibre su propio criterio de qué cuenta como "habla real" antes del próximo capítulo.
- Destino recomendado: el Escritor aplica los 4 micro-fixes directamente sobre el archivo (no requieren repasar estructura, curva ni rampa) y el capítulo puede pasar a Gate de la Ama sin una nueva vuelta completa por Validador, salvo que ella prefiera una relectura de Loreto para confirmar H14.
