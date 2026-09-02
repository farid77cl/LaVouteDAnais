# Validación — Capítulo 4 «La Entrega» v0.4
Validador Nivel 4 · 2026-09-02 · rework GATE 5 · CIERRE DEL RELATO (4/4)

**Veredicto:** MICRO-FIX
**Medición mecánica (Fase 2.5):** 🟡 AVISOS (`reportes/capitulo_04/medicion_v0.4.md`) — sin umbral duro. Varios de sus avisos son falsos positivos (ver detalle abajo); los confirmo/descarto uno por uno, no los repito de memoria.
**Casos de la Ama que reinciden:** C2 (muy menor, 1 instancia aislada, línea ~341: "la humedad" sin ancla anatómica en radio de 2-3 frases) · eco mínimo de C3 (tic "con la boca abierta" ×5 — el resto de las repeticiones flageadas por Loreto son refranes deliberados de `voz_autoral.md` §2, no tics). Ninguno de los casos graves (C1, C4, C5, C14, C16 — los que hundieron la v0.3) reincide: los reviso uno por uno abajo porque son exactamente lo que la Ama corrigió en vivo el 02/09.
**Inmersión:** ✅
**Continuidad:** ✅
**Narrativa:** 8.8
**Temperatura:** 9.1
**Voz autoral:** ✅

## 1. Inmersión (anti-metadata)

✅ Archivo de 576 líneas, prosa pura de principio a fin. Sin autoverificación embebida, sin listas M1-M17, sin etiquetas `[BEAT ERÓTICO]`, sin conteos de subrayables visibles. El único encabezado es `# Capítulo 4: La Entrega`. Limpio.

## 1b. 🩸 Humanización (anti-prosa-de-IA)

Auditado contra `HUMANIZADOR.md` vigente (recalibrado 02/09/2026: L1/L6 derogados, H1 ≤2/escena, H3 ≤6/cap) y contra el conteo mecánico de Loreto, con **relectura manual de cada ítem flageado** — el reporte del Escritor no es evidencia, el texto sí, y en varios puntos ni el Escritor ni Loreto tenían razón.

| # | Métrica | Umbral | Contado por mí | Declaró el Escritor | ¿Coincide? |
|---|---|---|---|---|---|
| H1 | Tricolones (relleno) | ≤2/escena | Esc.1: **1 genuino** ("Duras, altas, calientes de tan estiradas") — los otros dos "tricolones" que Loreto marcó en esc.1 son cadenas acumulativas de la "ola" canónica (`voz_autoral.md` §2), no enumeraciones de tres. Mismo patrón en esc.3/4/5: Loreto sobre-cuenta la ola como tricolon. Tras descartar los falsos positivos, ninguna escena pasa de 2. | "Máx. 2 en una escena… cumple" | Parcial — el Escritor no distinguió ola de tricolon; yo sí, y el resultado real es más limpio de lo que Loreto reportó |
| H2 | «no era X, era Y» | ≤1/cap | 1 (Marcela, forma "no… sino", variante válida) | 1 | Loreto marcó 0 (no detecta la variante "no… sino"); no importa, ambos ≤1 |
| H3 | Frases-remate (relleno) | ≤6/cap | **≤4 tras descartar 3 falsos positivos**: "Seguía funcionando" y "Y había vuelto" son el golpe que cierra una ola/paga un callback (voz, no relleno — `HUMANIZADOR.md` T3 excluye explícitamente "el golpe que cierra una ola"); "Nunca duraba vacío" es la anomalía deliberadamente irresuelta (Cementerio §8 de `canon_relato.md`), carga temática, no aforismo vacío. Quedan como relleno real: "Recién ahí salió", "Exacto, como la caja", "La abrió" — 3, quizá 4 con alguno borderline. | 6 ("al tope, no arriba") | El Escritor contó bien la cifra bruta de Loreto pero no aplicó el criterio de descarte que exige el propio Humanizador |
| H4 | Abstractos del tema | 0 | 0 — confirmado por Loreto (M6, "ninguna fuera de diálogo") y por mi lectura | 0 | ✅ |
| H5 | «algo» comodín | ≤2 | 0 | 0 | ✅ |
| H6 | Dobletes de adjetivos | ≤3 | **3, al tope**: "blanca, dura" (l.261) · "duras, torpes" (l.149) · "sin ninguna fuerza y sin ninguna delicadeza" (l.363) — verificados en el texto; Loreto los marcó en 0 (su regex no los detectó, probablemente por la coma sin conjunción o la estructura "sin X y sin Y") | 3 | El Escritor contó bien; Loreto tiene un hueco de detección acá |
| H7 | Variación elegante | 0 | 0 — verga/coño/tetas/mojada se repiten sin sinonimizar en todo el capítulo | 0 | ✅ |
| H8 | Varianza de frase | cumple | Confirmado por Loreto en todas las ventanas | cumple | ✅ |
| H9 | Lastre (L2/L4) | presente | Presente: L2 en "—Me dijeron que acá había una que…" (pensamiento/frase que se corta) · L4 en la acumulación "Contó… Contó… Contó…" y en "y no lo aguantó, y no lo contó" (frase que se estira a la sexta hora del turno) | presente | ✅ |

**Veredicto humanización:** ✅ **LIMPIO** tras auditoría manual (el conteo bruto de Loreto sugería más ruido del que hay; varios de sus "tricolon"/"remate" son la ola y los callbacks deliberados de la voz de la casa, no tells de IA). Único punto a vigilar: H6 está **al tope** (3/3) — si hay otra pasada de edición, no agregar dobletes nuevos, y si se toca algo, cortar uno de los tres para dejar margen.

**Citas de los peores tells (máx 3):**
1. *"con la boca abierta"* — aparece 5 veces (l. 7, 199, 289, 491, 505) sin escalar ni variar; es el único candidato real a tic de utilería del capítulo (no está en la tabla H1-H9 estricta, pero es el tipo de repetición que la Ama caza a oído — caso C3). Se opera variando 2 de las 5 apariciones.
2. *"blanca, dura"* / *"duras, torpes"* / *"sin ninguna fuerza y sin ninguna delicadeza"* — los tres dobletes están al límite del cupo; ninguno urge, pero el margen es cero.
3. *"Recién ahí salió."* / *"Exacto, como la caja."* — los dos remates genuinamente de relleno; no dañan pero podrían fundirse con la frase anterior sin perder nada.

## 1.5 Continuidad (cronología + costura + hechos plantados)

- **Línea de tiempo:** ✅ — grep confirma **cero marcadores de día** en todo el archivo (sin "martes", "jueves", conteos de días, etc. — cumple la regla del 25/08). La secuencia de once escenas coincide exactamente con la tabla de `cronologia.md` §2b "Cap 4 v0.4" (apertura camarín → Don Manuel → flashback decisión → puente faja → espejo baño → vuelta mediodía → hombre nuevo+privado → Marcela → Felipe/vaso → Felipe/privado → cierre). El salto temporal interno (presente → flashback → presente) está señalizado con quiebre `***` y cambio de tiempo verbal, sin confusión.
- **Costura con cap previo:** ✅ — el Cap 3 v0.7 cerraba con Cupcake **pre-cirugía** (pechos propios, acaba de tomarse el vaso a sabiendas). El Cap 4 abre **después de un salto sin cuantificar**, explícitamente autorizado por `cronologia.md` ("el reloj es el cuerpo": aros reinsertados por agujeros medio cerrados, operación ya hecha y recuperada). No hay contradicción de vestuario/objeto: el microbikini, las Pleaser, la línea rosada de la barra, todo continúa igual que en Cap 3.
- **Callbacks con ancla:** ✅ — verificado con grep contra el Cap 3:
  - *"Vuelve, chiquito. Vuelve con más."* (Cap 4, l. 397) → anclado literal en Cap 3 v0.9 l. 95 (cursiva idéntica).
  - *"los hombros que no le llenaban la camisa"* → anclado en Cap 3 l. 355 ("los hombros que no la llenaban") y escala correctamente a "los hombros que ahora sí llenaban la camisa" (l. 457) y "se fue con los hombros llenando la camisa" (l. 529) — refrán que escala, canon.
  - *"pestañas largas que no le debían nada al rímel"* → anclado en Cap 3 l. 89, reutilizado como marca física de continuidad de Felipe, no como clon accidental.
  - *"el día que me lo tomé yo"* (l. 497) → referencia al cierre del Cap 3 (H15, ya pagado ahí). Correcto: no vuelve a bebérselo en este capítulo (GATE 5 cumplido, confirmado también por grep: no hay ninguna otra escena donde ella tome el vaso; en la escena 6 "la mano le pasó por delante y siguió hasta la leche sin tocarlo").
  - Ningún callback fantasma detectado — no encontré ninguna referencia a un evento sin origen escrito.
- **Huecos a corregir:** ninguno.

## 2. Narrativa

### Pivotes del canon cumplidos

- ✅ **H13 — el vaso a Felipe, decisión propia, no por plata, efecto visible.** Cita: *"Cupcake la miró y no la tocó. No la quería. Esa noche no quería lo que había adentro. / Lo que quería estaba detrás del vaporizador."* Fórmula ritual única: *"Antes del café. Tómatelo entero, mi amor. Sin dejar ni la mitad."* Efecto en el mismo párrafo, sin nombrar la sustancia: *"los dedos le soltaron el borde del acero... los hombros le bajaron... la cara dejó de trabajar... la voz de otro: un tono más abajo."* Enmienda §6b-bis cumplida al pie de la letra.
- ✅ **H14 — cierre con ancla en la técnica de la entrega, no el pulgar.** Grep confirma **cero apariciones de "pulgar" en función de regla de medición** en todo el cierre; el único "pulgar" del capítulo es el de Marcela midiendo el mapa de sensibilidad (escena 8, función distinta y anterior). Felipe ejecuta la técnica completa (rodeo, taza que no suelta, aliento antes que la voz, monedas cerradas desde el meñique) y Cupcake lo corrige exactamente como corrigió a la chica nueva en Cap 3 (*"Y no me la dejes en la madera"* ↔ Cap 3 *"lo que le pones en la mano y le pides con la boca se queda contigo"*). Última línea: *"—Ya. Sal a vender café."* Sin epílogo, sin moraleja, sin frase que le explique al lector qué acaba de pasar.
- ✅ **H15 — no se toca en este capítulo (GATE 5).** Confirmado por lectura y por grep: cero instancias de ella bebiendo el vaso.

### Calidad técnica

- **POV:** estable, tercera persona pegada a Cupcake en las once escenas, sin fugas.
- **Vocabulario chileno:** ✅ — sin España (no hay *polla, follar, coche, vale, tío*), sin voseo argentino, sin *doctor* (la instrucción C13-06 de eliminar "doctor" con Don Arturo no aplica acá pero el patrón general se respeta: nadie usa registro peninsular).
- **Buzzwords AI detectadas:** ninguna (sin *crucial, tapiz, intrincado, profundizar*; sin abstractos de tema — ver H4 arriba).

### Lo que sí baja el score

1. **Don Manuel, escena 2 — la asimetría de deseo es real, aunque menor.** El cuerpo de Cupcake responde una sola vez en toda la escena (el pezón, l. 47); no hay marca de excitación propia adicional (coño/mojada) como sí la hay en las demás escenas del capítulo. Es defendible —la escena es sobre negocio y recuperar a un cliente viejo, no sobre pasión mutua— pero comparado con el resto del capítulo (donde la sub-medida "¿se desean, o uno solo se excita?" pasa con nota alta), esta escena queda la más asimétrica. No es una falla de T2 (el capítulo entero no depende de esta escena), pero es el punto más débil del eje.
2. **El tic "con la boca abierta" ×5** (ver Humanización) resta un poco de pulido, aunque no alcanza a ser un patrón grave.
3. **Cierre algo más frío en densidad de cuerpo** (ver T9 abajo) — no es un error de diseño (el beat de Yasna hablando de la máquina es Ley 3/4/5 en acción: "nadie comenta"), pero enfría el tramo inmediatamente anterior al cierre más de lo ideal para el último capítulo del relato.

### Score Narrativa: 8.8

## 3. 🔥 Temperatura — ¿es erótico? ¿está caliente?

| # | Medida | Resultado |
|---|--------|-----------|
| T1 | **¿Es erótico?** | ✅ erótico, sin ambigüedad. Sacado el contenido sexual no queda nada: no hay caso a resolver, no hay subtrama no-erótica corriendo en paralelo. Las once escenas son transacciones eróticas encadenadas; el capítulo entero ES la escalera del deseo. |
| T2 | **¿Calienta?** | ✅ sí, con margen. Ver las 3 frases citadas abajo. Sub-medida deseo mutuo: **pasa bien** en las escenas de Marcela y Felipe (ambos cuerpos reaccionan, documentado en la piel de los dos lados — el defecto exacto que hundió "Lo que Pediste" NO se repite acá); algo más asimétrica en Don Manuel (ver Narrativa arriba), pero no al punto de fallar el eje. |
| T3 | Explicitud léxica | ✅ con nota — 15,4 explícitas/1000 (Loreto), muy por encima del piso de referencia (8,5-13,6). De los 3 eufemismos que Loreto marcó, **2 son falsos positivos** ("ahí abajo" y una de las dos "humedad" tienen *verga*/*mojada* dentro del radio de 2-3 frases exigido); queda **1 genuino**: "la humedad crecerle entre las piernas" en la escalera de Marcela (sin ancla anatómica cercana) — aislado, en un tramo de tránsito, no en un pico. |
| T4 | Suciedad del registro vs antología | ✅ — Don Manuel, Marcela y Felipe hablan largo y sucio al oído, en el modelo exacto de los Fragmentos 11/12 de `antologia_calenton.md`. Ningún clímax se narra en prosa limpia. |
| T5 | Descarga real en escena | ✅ — las cuatro descargas explícitas del capítulo (espejo del clóset, espejo del baño, Marcela, Felipe) ocurren completas y en página, sin elipsis. La única "no-descarga" (ella con el hombre nuevo) es restricción profesional escrita en el cuerpo, no un corte de cámara. |
| T6 | Densidad de subrayables | ~5/1000 estimado (muy por encima del mínimo 4/1000), con más de la mitad de las imágenes ancladas en léxico anatómico directo, no solo atmosférico. |
| T7 | Motivos permanentes por escena · curva de resistencia | ✅ — M1 (mirada), M2 (taco/Pleaser vs pies planos de Marcela), M3 (olor), M4 (cuenta obsesiva de cafés/plata, el motor dominante de todo el capítulo) presentes y activos. M5/M6/M7 correctamente **silenciosos** — ya alcanzaron su estado terminal en capítulos previos y el canon exige que ese silencio no se comente; su ausencia acá es la ejecución correcta del arco, no un hueco. Curva de resistencia: apropiada para el capítulo de cierre (cero resistencia de Cupcake, ganada en capítulos anteriores; Felipe hace su propio arco de resistencia→cesión dentro de este capítulo, con ritmo coherente). |
| T8 | Apertura | ✅ fuerte. Primeras 500 palabras: 44,0% de narración con cuerpo (Loreto), la más alta de las diez ventanas salvo la novena. Abre con *"Las tetas nuevas le latían"* — el cuerpo ya activo desde la primera frase, exactamente el antídoto que pedía `voz_autoral.md` §2 contra la apertura fragmentada-abstracta que la Ama rechazó en v0.3. |
| T9 | Distribución + cierre (última cap., no gancho) | (a) ✅ — calor genuino en las once escenas, no comprimido en un solo tramo. (b) 🟡 — el cierre real (escena 11, técnica de la entrega devuelta) es correcto en diseño (H14 exige exactamente esto, no otra escena de sexo) y sí tiene carga física (el pecho que cae, la mano en la nuca, el perfume en el pecho de él), pero el tramo de Yasna hablando de la máquina justo antes (líneas 539-546) es la parte menos cargada de todo el capítulo — Loreto mide el último decile en 26,1% de cuerpo, el más bajo de los diez. No es un error de diseño (Ley 3/4/5: "nadie comenta" necesita ese respiro mundano), pero se puede comprimir un poco más sin perder la función. |

### Las 3 frases MÁS CALIENTES del capítulo

1. *"—Son compradas —dijo—. Con la plata que me dejaste tú, mi amor. Seis lucas cada mañana por mirármelas chiquitas de reojo y pedirme perdón. Tú las pagaste sin saber, capuchino a capuchino, y mírate ahora: con la boca en el aro y los dedos adentro mío, sin pedir permiso. Así te quería. Así las quería yo: que no le cupieran a nadie en los ojos. Ni a ti."* — el parlamento largo que exige `voz_autoral.md` §4, con la inversión de poder completa (Felipe pagó la transformación que ahora lo domina).
2. *"—Estás mojada desde la escalera —dijo, y le pasó los dedos una sola vez de abajo hacia arriba, sin entrar, y se los miró brillar—. Yo te vi subir. Arriba de las tetas no sientes nada, se te nota en la cara... y acá te abres entera, se te va la rodilla, se te moja el coño sin que yo haya bajado la mano todavía."* — Marcela leyendo el cuerpo de Cupcake en voz alta antes de tocarlo (modelo Fragmento 12).
3. *"—Se le está poniendo dura la verga contra mi barra, la veo desde este lado del acero, y todavía no ha tocado la taza. Tómese el cortado. Despacio. Y no deje de mirármelas, que para eso me las hice: para que usted se las tome con el café todas las mañanas, con la boca a esta distancia y sin poder morder."* — Don Manuel, la voz al oído nombrando lo que le pasa al hombre mientras cierra la trampa (C14 resuelto).

### Los 2 pasajes MÁS FRÍOS

> Ningún tramo M4 🔴 duro en `medicion_v0.4.md` (solo hay un 🟡 en escena 1, línea 49, que descarto abajo por lectura). Cito los dos tramos genuinamente más bajos en carga, por mi propia lectura:

1. *"Yasna, en el espejo de al lado, se pintaba la boca y hablaba de la máquina, que estaba perdiendo presión otra vez y que don Nelson no la iba a arreglar hasta que se muriera del todo... —Si se queda sin presión a las diez, le tiras vapor antes y la dejas —le dijo Yasna a Cupcake, cerrando el labial—. Ya me voy, que arriba está lleno."* — el tramo de menor carga corporal de todo el capítulo (coincide con el decile 10 al 26,1% de Loreto), justo antes del cierre. Funcional (Ley 3/4/5: el dispositivo de "nadie comenta" necesita este respiro mundano) pero se puede comprimir 20-30% sin perder la función — caso C1, versión leve.
2. *"Al médico le llegó con las uñas fucsias, los tacos de quince y una blusa cerrada hasta el cuello, y él le miró las uñas primero, y después la blusa, como si adivinara. Le pasó la huincha por debajo de las tetas con los dedos fríos, apuntó dos números..."* — el tramo más "trámite" del capítulo (consulta médica), aunque **ya viene bien resuelto**: se corta inmediatamente después de la negociación del tamaño (exactamente lo que pedía C1-18/C1-19), y trae calor propio ("Decirlo la mojó... los muslos se le apretaron solos"). Lo cito como el segundo más frío del capítulo por comparación relativa, no porque falle — es la escena de trámite mejor resuelta de las tres versiones del capítulo.

### Eufemismos evasivos detectados

1 genuino: *"sintiendo la humedad crecerle entre las piernas con cada escalón, sin ninguna mano encima"* (escena de Marcela, subida de la escalera) — sin léxico anatómico crudo en el radio de 2-3 frases. Los otros 2 que Loreto marcó ("ahí abajo" y la primera "humedad") tienen *verga* o *mojada* dentro del radio exigido y se descartan como falsos positivos.

### Score Temperatura: 9.1

> T1 y T2 ambos ✅ — el gate pasa. El score no es 10 por la asimetría menor de Don Manuel y la caída de densidad en el cierre, ninguna de las dos suficiente para bajar el gate.

## 4. Voz Autoral

### Tics canónicos activados

- **§1 el cuerpo contesta antes que la cabeza** — corre explícitamente ≥2 veces, con la fórmula casi textual: *"A Cupcake el cuerpo le contestó antes de que la cabeza terminara de oírlo"* (l. 437) y *"El cuerpo le contestó antes de que ella alcanzara a reírse"* (l. 553).
- **§2 ola y golpe** — confirmado por H8 (varianza de frase cumple en toda ventana) y por lectura directa: olas largas rematando en fragmentos cortos ("Lo miró." "Se sentó." "—Nada.").
- **§3 cursiva en dos registros** — 4,0/1000 (Loreto), dentro del rango de referencia 2,3-5,3; ambos registros presentes (cabeza nombrando explícito: *"Esto lo hice yo. Con un vaso y tres frases"*; voz de abajo en minúscula: *"sí. sí. dame."*).
- **§4 la dominante habla largo** — 13 parlamentos ≥45 palabras (Loreto), dentro de 9-32; Don Manuel, Marcela y Felipe reciben cada uno al menos un parlamento largo de Cupcake, y Felipe recibe uno simétrico de vuelta al cierre.
- **§5 la cruda en el pico** — verga/coño/tetas/mojada en cada clímax, sin rodeo, salvo la única excepción menor de T3 ya señalada.
- **§6 el espejo con las manos** — cumplido en el espejo del clóset (l. 101-107, ambas manos sobre el cuerpo) y en el espejo del baño (l. 137-151, manos antes que ojos); el espejo del cierre cambia de función deliberadamente (técnica compartida, no auto-contemplación) y sigue siendo canon correcto para lo que H14 pide.
- **§7 cuarta pared al cuerpo del lector** — 3 instancias, sensuales y no contables (ninguna explica quién pagó): l. 37-39, l. 183 (borderline, dirigida más al cliente en escena), l. 439.

### Frases nuevas candidatas para incorporar a `voz_autoral.md` §9 (Cupcake)

- *"Me lo pagó él, de a seis lucas, y me pide perdón."*
- *"Así las quería yo: que no le cupieran a nadie en los ojos. Ni a ti."*
- *"Cincuenta y tres. Este no cuenta. A este no lo vendí."*

## 5. Micro-fixes sugeridos

1. **Líneas 7, 199, 289, 491, 505 (todo el capítulo):** el tic "con la boca abierta" ×5 → variar al menos 2 instancias (ej. l. 491 "con los aros brillando entre los labios" en vez de repetir la fórmula).
2. **Escena 2, Don Manuel (párrafos 41-85):** agregar una marca de excitación propia de Cupcake más allá del pezón (una línea de "mojada"/"coño" bastaría) para emparejar la sub-medida de deseo mutuo con el resto del capítulo.
3. **Líneas 539-546 (Yasna y la máquina, justo antes del cierre):** comprimir 20-30% — mantener la función de "nadie comenta" pero acortar el tramo mundano para no enfriar el tramo inmediatamente anterior a la última escena del relato.
4. **Escena de Marcela, línea ~341 ("sintiendo la humedad crecerle entre las piernas"):** agregar un ancla anatómica cercana (ej. rematar con "*mojada*" en cursiva, como se hace en el resto del capítulo) para cerrar el único eufemismo evasivo genuino de T3.
5. **Opcional, sin urgencia:** si se vuelve a tocar el capítulo por cualquier otro motivo, no agregar más dobletes de adjetivos (H6 está al tope, 3/3) y revisar si "Recién ahí salió" / "Exacto, como la caja" pueden fundirse con la frase anterior.

## 6. Notas

- **Reciclaje en rework (§1c):** verificado explícitamente contra `borradores/capitulo_04/capitulo_04_la_entrega_v0.3.md` en los tramos que la Ama rechazó en vivo (apertura, escena de Don Manuel, espejos). **No hay reciclaje** — la apertura pasó de fragmentos abstractos ("Lo primero que aprendió del cuerpo nuevo fue el peso. No el tamaño. El peso.") a cuerpo activo desde la primera línea; Don Manuel pasó de un diálogo "¿Cómo era yo antes?" que la Ama calificó de inconexo a una seducción con motivo claro y las tetas mostradas en escena; los espejos pasaron de "solo piensa" a manos explícitamente sobre el cuerpo. Es una reescritura real, no un retoque cosmético — el caso C3-05 no aplica acá.
- **Todos los casos graves que hundieron la v0.3 están resueltos y verificados, no solo declarados:** C1 (clínica cortada justo tras la negociación del tamaño, con calor propio) · C4-26/C4-29 (Don Manuel ahora tiene causalidad clara: vino todos los días aunque ella no estuviera, y el motivo de que vuelva con más plata está en escena, no afirmado) · C5-17 (espejos con manos) · C9-19 (cinta doble faz removida deliberadamente, motivo permanente correcto) · C10-10 (ella ya no bebe el vaso, GATE 5 cumplido) · C14-12/C14-13 (Don Manuel ve las tetas en escena; la cuarta pared es sensual, no contable) · C16 (el registro "poético" del narrador desapareció; la voz suena a `voz_autoral.md`, no al motor).
- **Sobre la discrepancia Escritor/Loreto en H1/H3/H6:** el Escritor confió en el conteo bruto de Loreto para H1/H3 (sobre-contando) y no confió lo suficiente para H6 (Loreto tiene un hueco real de detección en dobletes con estructura "sin X y sin Y"). Para el Validador de este capítulo, ninguna de las dos discrepancias cambia el veredicto — pero vale la pena que quien mantenga `medir_capitulo.py` revise el detector de tricolon (distinguir ola-acumulativa de enumeración-de-tres) y el de dobletes (cubrir "sin X y sin Y").
- **La cita de la Ama sobre la meta de Loreto** ("que un capítulo llegue a su Gate en ≤2 lecturas") es la vara con la que puse el veredicto en MICRO-FIX y no en APROBADO: el capítulo está objetivamente muy por encima de la v0.3 rechazada y cumple los tres pivotes duros (H13/H14/H15) a la letra, pero los puntos señalados arriba (asimetría de Don Manuel, tic de "boca abierta", cierre algo frío, un eufemismo aislado) son exactamente el tipo de detalle que ella caza en una lectura atenta. Aplicarlos ahora, en una pasada quirúrgica sin relanzar al Escritor completo, es más barato que dejarlos para que los encuentre ella.
