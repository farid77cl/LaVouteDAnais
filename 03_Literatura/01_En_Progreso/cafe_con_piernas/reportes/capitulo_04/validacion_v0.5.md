# Validación — Capítulo 4 «La Entrega» v0.5
Validador Nivel 4 · 2026-09-04 · rework quirúrgico por nota viva de la Ama · CIERRE DEL RELATO (4/4)

**Veredicto:** MICRO-FIX
**Medición mecánica (Fase 2.5):** 🟡 AVISOS (`reportes/capitulo_04/medicion_v0.5.md`) — auditados uno por uno abajo; la mayoría de los avisos de H1/T3/M1 son falsos positivos del detector (ola confundida con tricolon, eufemismo con ancla anatómica cercana no detectada). Ningún 🔴 duro.
**Casos de la Ama que reinciden:** **C1-13** (inventario físico en un solo bloque — el paseo de Felipe en el cierre, ver Narrativa) · patrón C4 genérico de "frase rara" (la personificación de la apertura). Ninguno de los casos graves (C1 trámite, C2 eufemismo en pico, C3 clon de coreografía, C14 cuarta pared contable, C16 narrador poético) reincide — revisados explícitamente abajo por ser el foco que la propia nota de la Ama pide cazar.
**Inmersión:** ✅
**Continuidad:** ✅
**Narrativa:** 8.8
**Temperatura:** 9.4
**Voz autoral:** ✅

## 1. Inmersión (anti-metadata)

✅ Archivo de 592 líneas, prosa pura de principio a fin. Único encabezado: `# Capítulo 4: La Entrega`. Sin autoverificación embebida, sin listas M1-M17, sin etiquetas `[BEAT ERÓTICO]`, sin conteos de subrayables visibles. Limpio.

## 1b. 🩸 Humanización (anti-prosa-de-IA)

Auditoría manual sobre el texto, no sobre el reporte del Escritor ni sobre Loreto en crudo — la Ama pidió explícitamente que se cace la reincidencia de "frases raras", así que este eje se leyó completo en voz alta.

| # | Métrica | Umbral | Contado por mí | Declaró el Escritor | ¿Coincide? |
|---|---|---|---|---|---|
| H1 | Tricolones (relleno) | ≤2/escena | Los "×24/×17/×35/×8" de Loreto por escena son en su enorme mayoría **ola acumulativa de dos-tres miembros** (`voz_autoral.md` §2), no enumeración-de-tres de relleno — mismo hueco de detector ya señalado en `validacion_v0.4.md`. Tras descartar los falsos positivos, ninguna escena supera 2 genuinos. | "cumple" (implícito, no tabulado en autoverif. — usa H1/H3/H6 solo en el resumen final) | Parcial — el Escritor no re-auditó H1 por escena en esta versión; yo sí, y el resultado real cumple |
| H2 | «no era X, era Y» | ≤1/cap | 0 (no encontré ninguna instancia literal ni variante "no… sino" en el material nuevo o heredado) | — | ✅ |
| H3 | Remates aforísticos | ≤6/cap | **≤3 genuinos tras descartar falsos positivos**: *"No se la acomodó"* es el refrán central del motivo permanente (triángulo que apenas aguanta, GATE 5 §3) repetido a propósito, no relleno · *"Y había vuelto"* paga el callback de *"Vuelve, chiquito. Vuelve con más"* · *"Nunca duraba vacío"* es la anomalía deliberada del Cementerio §8. Quedan como relleno real: *"Recién ahí salió"*, *"Exacto, como la caja"*, *"La abrió"* — 3. | 5 (declarado en autoverif. como conteo bruto de Loreto) | El conteo bruto de Loreto (6, al tope) sobre-cuenta motivo y anomalía como relleno; tras el descarte, hay margen |
| H4 | Abstractos del tema | 0 | 0 — confirmado por Loreto (M6) y por lectura | 0 | ✅ |
| H5 | «algo» comodín | ≤2 | 0 fuera de diálogo | 0 | ✅ |
| H6 | Dobletes de adjetivos | ≤3 | **1** (`blanca, dura`, l. 57, Don Manuel) — Loreto lo marca en 0 (mismo hueco de regex ya documentado en v0.4). `duras, torpes` y `sin ninguna fuerza y sin ninguna delicadeza` cayeron con el bloque cortado (O1) y con la reescritura de Marcela (O4), tal como preveía el brief §3/MF4. | "1/3" | ✅ — coincide, y con margen de sobra |
| H7 | Variación elegante | 0 | 0 — verga/coño/tetas/mojada se repiten sin sinonimizar | 0 | ✅ |
| H8 | Varianza de frase | cumple | Confirmado por Loreto en todas las ventanas | cumple | ✅ |
| H9 | Lastre (L2/L4) | presente | Presente: L2 en *"—¿Puedo… ¿Puedo subir?"* y *"No voy a poder, no voy a…"* · L4 en *"Los dientes también. Le mordió el borde…"* | presente | ✅ |

**Veredicto humanización:** ✅ **LIMPIO** en la tabla dura H1-H9. Pero la nota de la Ama (*"el humanizador aún le falta cariño, las frases aún salen un poco raras"*) no se resuelve solo con la tabla — pide una relectura de oído, no de conteo, y encontré dos candidatas reales que la tabla no captura porque no son tics repetidos, son giros aislados:

**Citas de los peores tells (máx 3):**
1. **L. 5, apertura (sin tocar en este rework — heredada de v0.1):** *"golpeando la piel tirante desde adentro como si tuvieran apuro por salir a trabajar."* Personificar las tetas con ganas de ir a trabajar es un giro ingenioso que se nota como giro — exactamente el registro que la Ama caza. Fix de una línea: *"golpeando la piel tirante desde adentro, insistente."* — pierde el ingenio, gana el cuerpo.
2. **L. 563, cierre (nueva en este tramo):** *"el top plateado de la casa, dos triángulos sobre el pecho liso con el nudo de la nuca bien hecho; la muñeca de la mano libre quebrada hacia adentro, con las uñas brillantes hacia afuera para que no rozaran nada; el cuello fino más largo sin la corbata, con una cadenita que se le movía en el hueco de la garganta cuando tragaba"* — **esto es C1-13 reincidiendo** (*"la descripción del cuerpo... hazla de a poco, no en un solo párrafo"*): tres rasgos de Felipe encadenados con punto y coma en una sola oración, inventario en bloque en vez de goteo. Es exactamente el paseo que el brief O6 pedía mostrar "en gesto", y el gesto se pierde cuando se lista. Fix: partir en 2-3 frases cortas repartidas en el párrafo (la cadera primero, después la muñeca dos líneas más abajo, la cadenita al final), no las tres en la misma respiración.
3. *(Sin tercera candidata dura — el resto del capítulo, incluido todo el material nuevo de Marcela y del privado de Felipe, pasa la prueba de lectura en voz alta.)*

## 1.5 Continuidad (cronología + costura + hechos plantados)

- **Línea de tiempo:** ✅ — grep confirma cero marcadores de día en todo el archivo. Sin marca de días (regla 25/08 intacta).
- **Costura con cap previo:** ✅ — coincide con `cronologia.md` §2b/§4 fila "Cap 4 v0.5": mapa de sensibilidad descubierto en la apertura (no en el espejo del baño, que ya no existe), única descarga previa a la clínica en el espejo del clóset, sin cinta desde la apertura, medialunas de Felipe correctamente ausentes (esa coreografía se reescribió), Felipe en plataformas al cierre.
- **Callbacks con ancla — el foco explícito de esta validación (O3):**
  - **O3.1 verificado con grep:** cero apariciones de "espejo del baño" en todo el archivo; las dos referencias que antes apuntaban ahí ahora dicen **"espejo del clóset"** — Marcela (l. 373: *"igual que en el espejo del clóset la primera vez"*) y Felipe (l. 487: *"como en el espejo del clóset"*). Ningún callback fantasma.
  - **O3.2 verificado:** el "doble" del borde del aro se planta en la escena 1 (l. 11: *"a un dedo del metal el mismo apretón le llegó doble"*), antes de que Marcela (l. 371) y Felipe (l. 459, 475) lo cobren. Ancla escrita, no inferida.
  - **O3.3 / `Setecientos por lado`:** no necesitaba replante — sigue en la primera línea del capítulo (l. 5), correcto según el brief.
  - **El vaso (H13):** verificado que no está plantado ni referido en su ubicación anterior (la barra) antes de la escena del privado; l. 151 confirma que en el mediodía "la mano le pasa por delante y sigue hasta la leche sin tocarlo" — el vaso sigue detrás del vaporizador intacto hasta que ella lo sube a la escalera en la escena 8. Sin callback sin ancla.
  - **H15:** ella no bebe el vaso en ningún punto del capítulo (confirmado por lectura completa) — GATE 5 intacto.
- **Huecos a corregir:** ninguno.

## 2. Narrativa

### Pivotes del canon cumplidos

- ✅ **H13 — el vaso a Felipe, en el medio del polvo, orgasmo simultáneo.** Cita literal, orden exacto pedido por la Ama: *"—Tómate esto, mi amor. Ahora... Es un líquido maravilloso. Va a hacer que todo sea mejor. Entero."* → *"Felipe abrió la boca contra el vidrio y se lo tomó... con la verga adentro del coño y a un segundo de venirse... el último trago y el último golpe fueron el mismo. Se corrieron juntos."* La sustancia jamás se nombra. El sí se lo saca la calentura, no un engaño frío — exactamente el mecanismo que la Ama pidió proteger.
- ✅ **H14 — cierre con la técnica de la entrega, ahora en tacones.** Cupcake le da sus plataformas (*"Con estas. Hoy."*), Felipe sube y baja la escalera con el taco sonando en el cemento, ejecuta la técnica sobre ella con la cadera tirada por el taco y la voz más fina, y a ella le cuesta quedarse quieta. Última línea intacta: *"—Ya. Sal a vender café."*
- ✅ **H15 — no se toca (GATE 5).** Confirmado por lectura y por grep.

### Calidad técnica

- **POV:** estable, tercera persona pegada a Cupcake, sin fugas, en las diez escenas.
- **Vocabulario chileno:** ✅ — sin España, sin voseo.
- **Buzzwords AI detectadas:** ninguna.

### Lo que baja el score

1. **C1-13 reincidente en el cierre** (ver Humanización, cita 2) — el paseo de Felipe descrito en un bloque de tres rasgos con punto y coma, exactamente el patrón que la Ama corrigió en otro relato con la misma nota (*"hazla de a poco, no en un solo párrafo"*). Es un fix de una edición, pero es real y es nuevo en este tramo.
2. **La apertura conserva un giro "ingenioso"** (ver Humanización, cita 1) heredado sin tocar de v0.1 — no era parte del encargo de este rework, pero es exactamente el tipo de frase que la Ama señaló como "rara" en su nota más reciente, y como el Escritor pasó el Humanizador "sobre el archivo completo" (brief §6), este giro debería haber caído en esa pasada y no cayó.
3. **La consulta médica (flashback) sigue siendo el tramo más de trámite del capítulo**, aunque redimido con calor propio (*"Decirlo la mojó"*) — no es una falla, es el segundo pasaje más frío (ver Temperatura).

### Score Narrativa: 8.8

## 3. 🔥 Temperatura — ¿es erótico? ¿está caliente?

| # | Medida | Resultado |
|---|--------|-----------|
| T1 | **¿Es erótico?** | ✅ sin ambigüedad. Diez escenas, todas transacción erótica encadenada. Sacado el sexo no queda nada. |
| T2 | **¿Calienta?** | ✅ sí, con margen amplio — más que v0.4. Ver 3 frases abajo. **Sub-medida deseo mutuo:** pasa en Don Manuel (nueva marca de excitación propia, MF2 aplicado: *"la tanga se le pegó a la piel, mojada"*), pasa fuerte en Felipe (él reacciona en cuerpo en cada escena, el efecto post-vaso es visible y compartido) y pasa en Marcela **por la vía correcta para una femme fatale**: su deseo no se muestra en su propio cuerpo (eso sería "calidez", lo que la Ama prohibió) sino en el control — la media sonrisa al ver moverse el aro, el pulgar que se detiene "dejándola con las ganas de que apretara". Es deseo mostrado, no confesado, tal como pedía la nota. No hay ningún personaje excitándose solo mientras el otro solo ejecuta. |
| T3 | Explicitud léxica | ✅ **mejor que v0.4.** 15,8/1000 (Loreto), muy sobre el piso de referencia. De los 3 eufemismos que Loreto marcó, **los 3 son falsos positivos** verificados a mano: *"ahí abajo"* (Don Manuel, l. 63) tiene *"verga"* dos líneas antes · *"la humedad"* (l. 239-241) remata en *mojada* en cursiva dos líneas después · *"ahí abajo"* (Marcela, l. 361) tiene *"coño"* dos líneas antes. Cero eufemismos evasivos genuinos — el único que quedaba en v0.4 (la escalera de Marcela) se cerró con MF3 (*"el coño se le fue mojando escalón a escalón, mojada"*, l. 325). |
| T4 | Suciedad del registro vs antología | ✅ — Don Manuel, Marcela y Felipe hablan largo y sucio al oído, modelo Fragmentos 11/12. Ningún clímax narrado en prosa limpia. |
| T5 | Descarga real en escena | ✅ — clóset, Marcela, Felipe (con el vaso en el medio) ocurren completas y en página. La no-descarga con el hombre nuevo sigue siendo restricción profesional escrita en el cuerpo, no elipsis. |
| T6 | Densidad de subrayables | ~5-6/1000 estimado, sobre el mínimo 4/1000, con más de la mitad anclado en léxico anatómico directo (verga, coño, aro, tetas), no solo atmosférico. |
| T7 | Motivos permanentes por escena · curva de resistencia | ✅ — M1 (mirada), M2 (taco, con el pago explícito en Felipe), M3 (olor), M4 (cuenta obsesiva de plata, motor de todo el capítulo) presentes y activos en cada escena. M5/M6/M7 correctamente silenciosos (arco ya cerrado en capítulos previos). Curva de resistencia apropiada para el cierre: cero resistencia de Cupcake (ganada antes), arco propio de Felipe resuelto dentro del capítulo. |
| T8 | Apertura | ✅ fuerte — 44,0% de narración con cuerpo en las primeras 500 palabras (Loreto), abre con el cuerpo ya activo (*"Las tetas nuevas le latían"*). |
| T9 | Distribución + cierre (última cap., sin gancho) | (a) ✅ — calor genuino y distribuido en las diez escenas: Don Manuel, hombre nuevo, Marcela, Felipe×2. Nada comprimido en un solo tramo. (b) ✅ — el cierre real (Felipe ejecutando la técnica de vuelta, en tacones) tiene carga física alta y creciente hasta la última línea (*"las uñas fucsias clavadas en el borde del asiento"*, *"el aire del camarín le llegó al coño abierto"*); Loreto mide 44,4% de cuerpo en las últimas 500 palabras, comparable a la apertura. El tramo de Yasna/máquina sigue siendo el más frío inmediatamente antes del cierre, pero ya viene comprimido (~32%, según autoverificación) y cumple su función de "nadie comenta" (Ley 3/4/5) sin robarle temperatura al tramo final. |

### Las 3 frases MÁS CALIENTES del capítulo

1. *"—Tómate esto, mi amor. Ahora. —Con la voz de la barra, dulce, encima de él—. Es un líquido maravilloso. Va a hacer que todo sea mejor. Entero."* seguido de *"Se corrieron juntos."* — la escena que la Ama pidió explícitamente, ejecutada palabra por palabra en el orden que fijó, y es el pico real del capítulo.
2. *"—Ahí estás —dijo Marcela, bajito... Así, callada y con el aro moviéndose, estás más rica que con ellos."* / *"Cierra las piernas si quieres. Con eso no te tapas: te lo aprietas. Y lo que te aprietas ahí abajo también me lo pagué."* — la femme fatale que la nota pedía, con la calma como amenaza y el silencio como herramienta, en escena.
3. *"—Se le está poniendo dura la verga contra mi barra, la veo desde este lado del acero, y todavía no ha tocado la taza. Tómese el cortado. Despacio. Y no deje de mirármelas..."* — Don Manuel, la voz al oído nombrando lo que le pasa al hombre.

### Los 2 pasajes MÁS FRÍOS

1. *"Yasna, en el espejo de al lado, se pintaba la boca y hablaba de la máquina, que otra vez perdía presión... —Si se queda sin presión, le tiras vapor antes y la dejas —le dijo Yasna a Cupcake, cerrando el labial—. Ya me voy, que arriba está lleno."* (l. 543-547) — el tramo de menor carga corporal del capítulo, justo antes del cierre. Ya viene comprimido un 32% por orden del brief (O6); funcional (Ley 3/4/5), no urge más recorte.
2. *"Al médico le llegó con las uñas fucsias, los tacos de quince y una blusa cerrada hasta el cuello, y él le miró las uñas primero, y después la blusa..."* (l. 119-137) — el flashback de la consulta médica, el tramo de más trámite del capítulo, aunque redimido con calor propio (*"Decirlo la mojó"*, *"los muslos se le apretaron solos"*) — coincide con el único 🟡 M4 de Loreto (línea 49 de su medición, dentro de esta misma zona). No es una falla, es el segundo más frío por comparación relativa.

### Eufemismos evasivos detectados

Ninguno genuino (ver T3 — los 3 marcados por Loreto son falsos positivos con ancla anatómica dentro del radio de 2-3 frases).

### Score Temperatura: 9.4

> T1 y T2 ambos ✅ — el gate pasa con holgura. Mejora real sobre v0.4 (9.1): T3 queda en cero eufemismos genuinos (antes 1) y Marcela ejecuta la corrección explícita de la nota sin perder el control que la define. No es 10 porque el cierre, aunque fuerte, sigue precedido por el tramo más frío del capítulo (Yasna/máquina), y la consulta médica es trámite redimido pero trámite.

## 4. Voz Autoral

### Tics canónicos activados

- **§1 el cuerpo contesta antes que la cabeza** — corre ≥2 veces: Marcela (*"el cuerpo le contestó a la palabra antes que la cabeza"*, l. 501), Felipe (*"el coño se le apretó con la pregunta"*, l. 437), cierre (*"los muslos se le apretaron en el banco... y recién después le ardieron las mejillas"*, l. 569).
- **§2 ola y golpe** — confirmado por H8 y por lectura.
- **§3 cursiva en dos registros** — 3,7/1000 (Loreto), dentro de 2,3-5,3; cabeza explícita (*"Esto lo hice yo. Con un vaso y tres frases"*) y voz de abajo en minúscula (*"sí. sí. dame."*).
- **§4 la dominante habla largo** — 14 parlamentos ≥45 palabras (Loreto), dentro de 9-32; Don Manuel, Marcela y Felipe reciben cada uno al menos uno.
- **§5 la cruda en el pico** — verga/coño/tetas/mojada en cada clímax, sin rodeo (ver T3, 0 eufemismos genuinos).
- **§6 el espejo con las manos** — cumplido en el espejo del clóset (l. 101-107, ambas manos sobre el cuerpo) y en el espejo del camarín del cierre.
- **§7 cuarta pared al cuerpo del lector** — sensual, no contable: l. 37-39 (*"Y tú. Sí, tú, el de la taza a medio camino..."*), l. 223 (escalera del hombre nuevo), l. 489-493 (*"Tú también te lo habrías tomado así..."*).

### Frases nuevas candidatas para incorporar a `voz_autoral.md` §9

- *"Cierra las piernas si quieres. Con eso no te tapas: te lo aprietas."* (Marcela)
- *"¿Sabes lo que hago con el que aguanta? Lo dejo aguantar un poquito más."* (Cupcake)
- *"Es un líquido maravilloso. Va a hacer que todo sea mejor. Entero."* (fórmula ritual nueva del vaso, reemplaza la de v0.4)

## 5. Micro-fixes sugeridos

1. **Línea 5 (apertura, heredada sin tocar):** *"golpeando la piel tirante desde adentro como si tuvieran apuro por salir a trabajar"* → cortar la personificación ingeniosa. Sugerido: *"golpeando la piel tirante desde adentro, insistente."*
2. **Línea 563 (cierre, nueva):** el inventario de tres rasgos de Felipe encadenado con punto y coma en una sola oración (C1-13) → partir en 2-3 frases repartidas en el párrafo, no todas en la misma respiración: primero la cadera, dos líneas después la muñeca, al final la cadenita — igual que el resto del capítulo introduce los rasgos de Felipe, de a uno.

## 6. Notas

- **Reciclaje en rework (§1c):** verificado explícitamente. El cierre y el privado de Felipe reutilizan líneas de v0.4 (*"Se ven compradas"/"Son compradas"*, *"Perdí la cuenta"*, *"¿Cuánto es?/Nada"*, *"Esto lo hice yo"*) — pero **no es el caso C3-05**: esas líneas no fueron rechazadas por la Ama, el brief O5 pide explícitamente reusarlas (*"Reusa esas imágenes; ahora llegan encima de él ya corrido"*), y la reubicación de la escena (vaso ahora en medio del polvo) es un cambio estructural real, no un retoque cosmético de material vetado. El único material efectivamente cortado por la Ama (el espejo del baño, l. 133-141 de v0.4) no reaparece en ninguna forma en v0.5 — verificado por grep.
- **Las seis órdenes de la nota, ejecutadas de verdad, no cosméticamente:** O1 (corte) ✅ con puente correcto · O2 (paja única, contenido mental fijado: cómo la van a ver + plata, fusión plantada) ✅ · O3 (los tres re-anclajes) ✅ verificado por grep, sin callback fantasma · O4 (Marcela femme fatale, no simpática — la calma, el silencio, la mirada que abandona, el deseo mostrado no confesado, el cuerpo económico) ✅, y específicamente **no se pasó al otro lado** (no hay calidez, sigue midiendo) · O5 (vaso en el medio del polvo, orden 1-2-3-4 exacto, consentimiento sacado por la calentura) ✅ literal · O6 (Felipe en tacones, más amanerado en gesto nunca nombrado, Yasna comprimida) ✅.
- **La línea suelta de la Ama sobre el humanizador** (*"aún le falta cariño, las frases aún salen un poco raras"*) fue la vara de la sección 1b de este reporte. La tabla H1-H9 pasa limpia, pero encontré dos frases concretas que justifican esa queja incluso en v0.5 — una heredada (apertura) y una nueva (cierre, y además caso C1-13 reincidente). Por eso el veredicto es MICRO-FIX y no APROBADO: son dos ediciones de una línea cada una, no una reescritura, pero son reales y la Ama las va a sentir si no se tocan antes de que le llegue.
- **Sobre el detector de Loreto:** persiste el mismo hueco ya señalado en `validacion_v0.4.md` — sobre-cuenta ola acumulativa como tricolon y no detecta dobletes con estructura "sin X y sin Y" ni eufemismos con ancla a 2-3 frases de distancia. Ninguno de los dos huecos cambió el veredicto acá, pero sigue valiendo la pena que se revise `medir_capitulo.py`.
