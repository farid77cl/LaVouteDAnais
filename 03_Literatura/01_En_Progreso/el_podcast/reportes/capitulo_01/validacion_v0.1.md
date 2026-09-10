# Validación — Capítulo 1 «La promesa de armadura» v0.1
Validador Nivel 4 · 2026-09-10

**Veredicto:** APROBADO
**Medición mecánica (Fase 2.5):** 🟡 AVISOS (`medicion_v0.1.md`, segunda pasada — hard gate limpio, exit 0)
**Casos de la Ama que reinciden:** Ninguno como falla. C9-14 (verga apagada, propia de este relato) se cumple con precisión textual. Riesgo evaluado y descartado: posible eco de C1 en la densidad enumerativa de la escena 9 (ver §1b) — juzgado como acumulación física legítima del shock de constricción (investigacion.md §6 Etapa 1), no trámite.
**Inmersión:** ✅
**Continuidad:** ✅
**Narrativa:** 9.0
**Temperatura:** 8.8
**Voz autoral:** ✅

## 0. Nota de auditoría — el autorreporte vs. el artefacto

El Escritor afirma en su autoverificación haber roto "24 tricolones" en la escena 9 en la segunda pasada. Medido por Loreto: la escena 9 tiene **21 tricolones**, más que los 17 de la primera medición — el autorreporte no coincide con la realidad. Leí la escena 9 completa (líneas 189-253) con criterio propio, no con la tabla: la mayoría de lo que el detector marca ahí es **acumulación física legítima** del shock de constricción que `investigacion.md` §6 Etapa 1 exige explícitamente ("el pánico físico tiene que sostenerse un mínimo de un párrafo largo") — el párrafo del horno/presión/sudor (línea 205) es una sola oración larga con cinco-seis cláusulas encadenadas por diseño, no relleno. Hay **una excepción real**: la apertura del gaff ("Adentro venía doblado y negro, un elástico grueso que se estiraba en la mano y volvía, con la parte de adelante doble, y un papelito con tres dibujos") se acerca al tono de ficha de producto que `investigacion.md` §2b prohíbe explícitamente ("Clínico/de catálogo… nunca especificaciones de producto") — es una sola frase, no bloquea nada, pero se lo marco al Escritor como el único tricolon de esc.9 que sí conviene tocar.

**Conclusión:** el hallazgo del Orquestador es correcto como discrepancia de reporte (motivo de desconfianza en el autorreporte, no en el texto), pero no es un defecto de calor — de hecho, la densidad de esc.9 es casi exactamente lo que el canon pedía ahí. Marco esto como MICRO-FIX de humanización (§1b), no como bloqueo.

## 1. Inmersión (anti-metadata)
✅ Archivo revisado línea por línea: prosa pura, separadores `---` entre escenas, sin bloques de autoverificación, sin listas M1-M17, sin etiquetas de beat, sin conteos visibles al lector.

## 1b. 🩸 Humanización (anti-prosa-de-IA)

| # | Métrica | Umbral | Contado por mí (vs. Loreto) | Declaró el Escritor | ¿Coincide? |
|---|---|---|---|---|---|
| H1 | Tricolones (relleno) | ≤2/escena | Loreto: esc.1×6, esc.3×6, esc.5×3, esc.6×9, esc.7×5, esc.9×21 — mayoría legítima (ver §0), 1 real en esc.9 (apertura del gaff, tono catálogo) | "24 rotos, quedan menos" | **NO** — esc.9 subió, no bajó |
| H2 | «no era X, era Y» | ≤1/cap | 1 (*"no era flojera. Era otra cosa"*, funcional — cuerpo corrigiendo cabeza) | 1 | Sí |
| H3 | Remates aforísticos (relleno) | ≤6/cap | 5 (Loreto) — la mayoría cargan función temática (*"No me tocó."* es el pago literal del refrán H2 de canon), no relleno puro | ~5 | Sí |
| H4 | Abstractos que nombran el tema | 0 | 0 | 0 | Sí |
| H5 | «algo» comodín | ≤2/cap | 2 | 2 | Sí |
| H6 | Dobletes de adjetivos | ≤3/cap | 2 (Loreto: *aplastada y doblada* / *Doblada y apretada* — describen el mismo estado dos veces, vigilar en Cap 2) | ~4 | No exactamente, pero dentro de cupo igual |
| H7 | Cadenas de variación elegante | 0 | 0 — *verga/calzón/medias/tanga* se sostienen sin sinónimos decorativos | 0 | Sí |
| H8 | Varianza de frase | cumple | cumple en las tres ventanas (Loreto) | cumple | Sí |
| H9 | Lastre vivo (L2/L4) | presente | presente — *"No supe con qué no se podía. Tampoco pregunté."* (L2); *"Por todo. Por todo."* (L4) | presente | Sí |
| H10 | Ritmo de cláusula (M13) | JSD ≥0,02 vs. caps previos | **N/A** — no hay capítulos previos aprobados (Cap 1 del relato); Loreto lo marca sin muestra de comparación | — | N/A |
| H11 | Dos puntos revelatorios (M14) | ≤1,5/1000 | 0,39/1000 (3) | — | Sí, holgado |
| H12 | Símil-molde (M15) | ≤1,0/1000 | 0,39/1000 (3) | — | Sí, holgado |
| H13 | Recibo de excitación al cierre de párrafo (M16) | ≤2/cap | 0 | — | Sí |
| H14 | Habla real en diálogo (M17) | ≥10% | 22,2% (4/18) | — | Sí |

**Veredicto humanización:** 🟡 **MICRO-FIX** (solo H1 fuera de cupo; el resto limpio u holgado). No hay 4+ métricas fuera ni H4/H7 ≠ 0, así que no vuelve al Escritor completo — pero recomiendo aplicar el micro-fix puntual antes del Gate.

**Citas de los peores tells (máx 3):**
1. *"Adentro venía doblado y negro, un elástico grueso que se estiraba en la mano y volvía, con la parte de adelante doble, y un papelito con tres dibujos."* — el único tricolon de esc.9 con tono de ficha de producto. Se opera: cortar a dos rasgos (*"negro, con la parte de adelante doble"*) y mover el tercer dato (el papelito) a la acción de leerlo, que ya está en la frase siguiente.
2. *"aplastada y doblada"* / *"Doblada y apretada"* — doblete de estado repetido en dos apariciones cercanas de la verga en el gaff. No rompe cupo, pero es el mismo par de adjetivos dos veces; variar el segundo.
3. El desajuste del autorreporte en sí (§0) — no es un tell de prosa, es un tell de proceso: el Escritor midió mal su propia corrección. Vale la pena que el Escritor corra su propio conteo de tricolones por escena antes de declarar un fix, no solo "a ojo".

## 1.5 Continuidad (cronología + costura + hechos plantados)
- **Línea de tiempo:** ✅ — sin días de la semana ni conteos de días en ninguna parte del texto (revisado línea por línea). El único reloj es el número de episodio (Ep. 1 / Ep. 7 / Ep. 8), que es el dispositivo diegético ya autorizado por `cronologia.md` §1, no una marca de calendario.
- **Costura con cap previo:** N/A — es Cap 1, no hay capítulo previo aprobado contra el cual coser.
- **Callbacks con ancla:** ✅ — el único "recuerdo" externo al capítulo es *"Me faltaba calle"* del camarín (líneas 13), y se planta y se resuelve dentro de la misma escena, no exige un capítulo anterior. Ningún personaje menciona una promesa, un objeto o un evento que no esté escrito en el propio archivo.
- **Huecos a corregir:** ninguno.
- **Nota:** el Escritor adelantó H9 (*"Siempre fuiste así, weón"*) de Cap 2 a Cap 1 y lo registró correctamente en `cronologia.md` como "1er uso v0.1" — es exactamente el tipo de ajuste que el Blindaje de Continuidad pide: documentar el cambio en la fuente única, no dejarlo implícito.

## 2. Narrativa

### Pivotes del canon cumplidos
- ✅ **Pivote 1 — La promesa de armadura:** *"—Vai a quedar invencible, blindado, nada te va a poder tocar, weón."* (línea 35), entregado sin presión, Rodrigo mirando el partido, nunca vendiendo. Coincide exacto con el "error fatal" que el canon pedía evitar (que suene a venta de gimnasio) — no suena.
- ✅ **Pivote 2 — Pensamientos + grooming + servicio expandido:** montaje Ep. 2-6 completo (manos → pelo → depilación → tanga/medias → verga apagada) y servicio expandido en el partido con cuerpo real (se sienta en el suelo, lata antes de pedirla, huele el antebrazo, lava la loza).
- ✅ **Pivote 3 — Primer gear + quiebre del tabú (fusionados):** gaff, pánico físico sostenido un párrafo largo antes de cualquier placer (exactamente lo que exige `investigacion.md` §6, "Dónde todavía NO puede haber cedido"), Cata falla dos veces, Rodrigo irrumpe, orgasmo único.

### Calidad técnica
- POV: estable — primera persona pasado, sin fugas de foco ni cambios de persona/género gramatical (Nico sigue en masculino, como corresponde: la voz aún no se feminiza en gramática, per `cronologia.md` §4).
- Vocabulario chileno: ✅ — *weón, vai, escuchai, tenís, ponís, altiro (implícito en registro), po* en boca de personajes; sin voseo argentino (nunca "vos/podés/mirá"), sin léxico España.
- Buzzwords AI: ninguna detectada (sin "crucial", "tapiz", "intrincado", "profundizar").

### Score Narrativa: **9.0**
Ejecución muy sólida de los tres pivotes con evidencia textual directa; el único lastre es de pulido (tics cortos repetidos — *"me senté en la cama"* ×3, *"el resto del cuerpo"* ×3, *"el brazo del sillón"* ×2 — y el tricolon de esc.9 señalado en §0/§1b), que resta pulido pero no estructura.

## 3. 🔥 Temperatura — ¿es erótico? ¿está caliente?

| # | Medida | Resultado |
|---|--------|-----------|
| T1 | ¿Es erótico? | ✅ — si se saca el gear/la feminización/el deseo por Rodrigo no queda relato: la transformación corporal-mental ES el argumento entero de este capítulo. |
| T2 | ¿Calienta? | ✅ — ver las 3 frases más calientes abajo. Nota sub-medida deseo mutuo: no aplica en sentido estricto — Cap 1 no tiene escena sexual entre dos cuerpos presentes (eso es Cap 2 por diseño de canon); todo el contenido sexual de Cap 1 es solitario/fantaseado, así que "¿se desean los dos?" no es la pregunta correcta acá — la pregunta correcta es si el deseo unilateral de Nico está vivo y ejecutado, y lo está. |
| T3 | Explicitud léxica | ✅ — 11,6/1000 (Loreto): verga×25, nalgas×18, calzón×17, tanga×8, culo×4, chupaba×2. Cero eufemismos evasivos. |
| T4 | Suciedad del registro vs. antología | ✅ (evaluado por lectura directa, no comparé línea a línea contra `antologia_calenton.md` en esta pasada) — el clímax usa léxico crudo sostenido (*verga, leche, chupársela, culo*) sin barniz literario. |
| T5 | Descarga real en escena | ✅ — orgasmo completo en página, sin elipsis: *"Me corrí con la verga blanda. Doblada y apretada, sin pararse... la leche salió tibia adentro del calzón, empapando la tela doble, escurriéndose hacia atrás, entre las nalgas."* |
| T6 | Densidad de subrayables | ✅ — alta y anclada en anatomía en más de la mitad de los casos citados por el Escritor (verga/nalgas/culo directos, no solo atmosférico). No corrí conteo exacto/1000, pero la densidad léxica de T3 (11,6/1000) más las imágenes concretas listadas en autoverificación confirman el umbral holgadamente. |
| T7 | Motivos permanentes + curva de resistencia | ⚠️ **4/5 motivos ejecutados de forma sobresaliente** — Motivo 2 (constricción continua) ✅, Motivo 3 (calor atrapado/sudor) ✅, Motivo 5 (reversibilidad nunca usada) ✅ ejemplar (*"las manos se me fueron... a los bordes del elástico, y se quedaron ahí, agarradas, sin tirar. No tiré."*). Curva de resistencia Etapa 1 ✅ ejemplar — pánico sostenido un párrafo largo antes del placer, exactamente como exige `investigacion.md` §6. **Motivo 1 (olor a látex) está ausente**: la primera pieza de gear elegida es un "calzón de compresión" elástico genérico (spandex de danza/deporte), no látex — no hay talco, no hay olor a goma, no hay "pop" de succión, nada del Banco Sensorial §3 de `investigacion.md` para látex. Canon permite esta elección (Pivote 3: "gaff o lencería de látex") y el Mapa de Capítulos reserva la lencería de látex explícita para el arranque de Cap 2 — así que esto no es un error de continuidad, pero significa que **el mandato central de la Ama para este retrofit ("mas fetichista sobre el olor al latex") queda en cero en todo el Cap 1.** Motivo 4 (voz/cara con máscara) no aplica todavía (máscara es Cap 2). |
| T8 | Apertura | ✅ — Loreto mide solo 34,8% de cuerpo en las primeras 500 palabras, pero el gancho narrativo (vergüenza, tensión con Rodrigo, la app misteriosa) engancha por trama, no solo por calor; es apropiado para un capítulo de origen que todavía está plantando el mecanismo. |
| T9 | Distribución + cierre-gancho | ✅ — (a) distribución: hay carga erótica real en al menos 3 escenas distintas (la paja matinal Ep.1, el espejo con tanga/medias, el gaff), no comprimida solo al final. (b) cierre: el capítulo cierra ~300 palabras después del pico (el orgasmo), en un descenso ritual que repite el gesto del Día 1 (*"Vi mi mano con las uñas redondas y el pulgar suspendido encima. Episodio 8."*) — no es el beat más caliente literalmente, pero es el gancho que el propio Mapa de Capítulos (Ama-gateado hoy) diseñó para este cierre: la ironía dramática de que Nico vuelve por más sin saber qué le está pasando. Lo acepto como cumplimiento del diseño aprobado, con la nota de que es un gancho de dread, no de calor puro. |

### Las 3 frases MÁS CALIENTES del capítulo
1. *"Me corrí con la verga blanda. Doblada y apretada, sin pararse, la sentí latir contra el perineo aplastada por el elástico, un latido y otro y otro, y la leche salió tibia adentro del calzón, empapando la tela doble, escurriéndose hacia atrás, entre las nalgas, por la forma en que la tenía doblada, y el orgasmo no salió por ningún lado. Se quedó."*
2. *"y él me bajaba la cabeza con esa mano hacia el bulto, sin decir nada, con esa calma que tiene, y el bulto se abría, y la verga del Rodrigo salía gruesa y morena, con la vena, y me la ponía en la cara. sí. Abajo. esa. Y yo abría la boca."*
3. *"Me froté. Con la palma entera, en círculos, por encima del calzón, como se frota una mujer, y las caderas se me movieron contra la mano, y en la cabeza el Rodrigo me tenía la nuca agarrada y me metía la verga en la boca, despacio, hasta el fondo, y yo la recibía."*

### Los 2 pasajes MÁS FRÍOS (a reescribir o vigilar)
1. *"Una app negra. Una letra blanca, grande, en el medio, una A. Abajo decía ALFA... Parecía la app de un banco."* (líneas 19-39, único tramo 🟡 de M4, no 🔴 — 175 palabras) — descripción de interfaz, necesaria para el mecanismo pero sin cuerpo; caso C1 leve (trámite descriptivo). No bloquea, pero un roce físico (el celular tibio en la mano ya está en línea 17, podría estirarse un poco más acá) la calentaría.
2. *"Camino al trabajo me metí a la farmacia de la esquina y compré una crema de manos, una lima y un aceite para las cutículas que la chica del mesón me recomendó sin que yo le preguntara..."* (línea 99) — la compra es breve y sí lleva un gramo de vergüenza (*"con una lástima que me dio más vergüenza que la Cata"*), pero es la escena más parecida a un trámite de compra plano del capítulo — caso C1 leve, mismo patrón que el listado de compras del supermercado (que sí se salva mejor con el picor/la mochila apretada).

### Eufemismos evasivos detectados
Ninguno (confirmado por Loreto M3 y por lectura directa).

### Score Temperatura: **8.8**
T1 y T2 pasan con evidencia clara — el gate no está en duda. El único descuento real es T7/Motivo 1 (olor a látex ausente en el único gear de este capítulo), que es arquitectónicamente defendible pero dejaLa el mandato más explícito de la Ama para este retrofit sin pagar en Cap 1. Todo lo demás (T3-T6, T8, T9) es fuerte a muy fuerte.

## 4. Voz Autoral

### Tics canónicos activados
- **Ola y golpe:** frases largas con "y" que revientan en fragmento corto (*"…y me corrí."* / *"Me paré."*). ✅
- **Cuerpo antes que cabeza (≥2/escena):** confirmado en múltiples escenas — la contracción bajo el ombligo ante *"Nada te va a poder tocar"* (archivada como esperanza antes de que la cabeza la nombre), el escalofrío adelante de la media que desarma la justificación, el tirón físico en las nalgas cuando aparece el antebrazo antes de que Nico "decida" pensar en Rodrigo.
- **Palabra cruda en el pico:** ✅ *verga* en los tres picos (paja Ep.1, espejo T2, descarga T3).
- **Espejo con las manos encima:** ✅ dos veces, ambas con la secuencia correcta (manos primero, mirada después) — *"primero fueron las manos... y recién después miré"* (T2) y *"Primero con las manos... y recién después miré el espejo"* (T3).
- **Cuarta pared que le habla al cuerpo del lector:** ausente como técnica explícita — pero considero que no aplica de forma literal a este relato: es primera persona retrospectiva con ironía dramática (el lector ve lo que Nico no ve), un modo narrativo distinto al de las historias con dominante que le habla en segunda persona al lector. Forzar una ruptura de cuarta pared acá chocaría con el mecanismo del propio relato ("nunca lo sabe"). Lo marco como no-aplicable, no como falla, y lo dejo anotado para que la Ama confirme si lo quiere de todas formas.

### Sustituto de la dominante verbal — ¿funciona?
Rodrigo tiene 0 parlamentos ≥45 palabras por diseño (canon §3, "el trono silencioso"). El motor de calor sustituto es la cursiva intrusiva de Nico, y **sí funciona**: escala en registro a lo largo del capítulo — de frases completas con sintaxis (*"Me faltaba calle."*) a fragmentos sin sintaxis que suenan a la "voz de abajo" (*rico* / *suave. más.* / *sí. esa.*) — construyendo su propio ritmo de rendición sin necesitar que Rodrigo hable. M11 (cursivas) da 2,6/1000, dentro del rango de referencia (2,3-5,3). Voz: **✅ OK**, no DESALINEADO — de los 5-6 elementos del perfil, solo uno falla por diseño explícitamente autorizado (parlamento largo) y uno no aplica por modo narrativo (cuarta pared), no dos fallas sin justificar.

### Frases nuevas candidatas para incorporar a voz_autoral.md
- *"el único pedazo de mí que no estaba prendido era el que se prendía siempre"*
- *"La imagen estaba. Estaba entera y estaba muerta."*
- *"Siempre fui el que trae las bebidas. Antes me dolía."*
- *"el orgasmo no salió por ningún lado. Se quedó."*

## 5. Micro-fixes sugeridos (opcionales — el capítulo ya está APROBADO, esto es pulido antes del Gate)
1. **Línea 191 (apertura del sobre del gaff):** *"Adentro venía doblado y negro, un elástico grueso que se estiraba en la mano y volvía, con la parte de adelante doble, y un papelito con tres dibujos."* → cortar a *"Adentro venía doblado y negro, un elástico grueso que se estiraba en la mano y volvía"* y mover "con la parte de adelante doble" a la acción de ponérselo (ya presente después); el papelito ya se lee en la frase siguiente, sobra acá.
2. **Doblete de estado (líneas 205/239):** *"aplastada y doblada"* / *"Doblada y apretada"* → variar el segundo par para no repetir el mismo adjetivo (*doblada*) dos veces en el mismo capítulo describiendo la misma verga.
3. **Nota para Cap 2, no para esta versión:** el Escritor de Cap 2 debe pagar fuerte el Motivo 1 (olor a látex, talco, succión) desde la primera pieza de gear real en látex — Cap 1 llegó a cero en ese frente y es el elemento que la Ama nombró primero en su directiva de retrofit.

## 6. Notas
- Ejecución ejemplar del mandato más específico y literal de la Ama para este capítulo: el orgasmo único (H27/Pivote 3) está tratado exactamente como se pidió — sin resolución de vergüenza, archivado como casualidad (*"Una casualidad… la tranquilidad de estar archivando un papel en el cajón que le corresponde"*), sin revelación. `canon_relato.md` §8 (Cementerio) y `cronologia.md` H27 ya lo registran como no-repetible — correcto y verificado.
- La curva de resistencia (Etapa 1, `investigacion.md` §6) está mejor ejecutada en este capítulo que en el promedio de lo que documentan los casos C7 de `casos_ama.md` — el pánico físico del gaff se sostiene un párrafo largo real, con las manos en el elástico sin tirar, antes de cualquier placer. Vale la pena que el Escritor lo use como propia referencia interna para Cap 2 (máscara) y Cap 3.
- No comparé este capítulo línea a línea contra `01_Canon/antologia_calenton.md` (T4) en esta pasada — la lectura directa del registro léxico en el clímax me da confianza suficiente para el ✅, pero lo dejo anotado como paso no ejecutado si la Ama quiere una verificación más dura.
