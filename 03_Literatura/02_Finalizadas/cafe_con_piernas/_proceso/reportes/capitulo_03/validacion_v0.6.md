# Validación — Capítulo 3 «El Minuto Feliz» v0.6 (CIERRE DEL RELATO)
Validador Nivel 4 · 2026-08-31

**Veredicto:** APROBADO
**Inmersión:** ✅
**Continuidad:** ✅ (con un hallazgo no bloqueante, ver 1.5)
**Narrativa:** 9.0
**Temperatura:** 9.2
**Voz autoral:** ✅

> **Nota de vara.** `investigacion.md` existe (03/08/2026) pero su §9-§11 (rama "porn star + cámara + sí informado", mapa de 9 capítulos) quedó **derogado por instrucciones vivas de la Ama** entre el 14/08 y el 28/08/2026: el relato se comprimió a 3 capítulos, se eliminó la escena de la cámara y el "sí informado" formal, y el cierre pasa a ser el vector del vaso hacia Felipe. Esta derogación está documentada en `cronologia.md`, `walkthrough.md`, `canon_relato.md` §4b/§6b-bis y en el propio `validacion_v0.3.md` de este capítulo — no la trato como un hueco de investigación, la trato como jerarquía de autoridad ya resuelta (instrucción viva > documento de Fase 0). Mido T7 (motivos permanentes, curva de resistencia) contra §5/§6 de `investigacion.md` en lo que sigue vigente, y contra `canon_relato.md` §4b/§4c en lo que fue reescrito.
>
> **Vara de voz:** `01_Canon/voz_autoral.md` no tiene entradas propias de `cafe_con_piernas` (el archivo acumula tics de `esposa_servidumbre`). Medí continuidad de voz contra `capitulo_01_el_turno_de_prueba_v0.14.md` y `capitulo_02_la_segunda_persona_v0.8.md`, ya aprobados — es la vara correcta para este proyecto, igual que hizo `validacion_v0.3.md`.

---

## 1. Inmersión (anti-metadata)

✅ Limpio. Leí el archivo completo (598 líneas): título `# Capítulo 3: El Minuto Feliz` + prosa pura, separadores de escena `***` (12 usos, verificado con grep — corrige la inconsistencia de formato que `validacion_v0.3.md` había señalado, donde v0.3 usaba `---`). Sin bloques de autoverificación, sin listas M1-M17, sin etiquetas de beat, sin conteos visibles. La autoverificación vive correctamente separada en `reportes/capitulo_03/autoverificacion_v0.6.md`.

## 1b. 🩸 Humanización (anti-prosa-de-IA)

Conté de verdad sobre el archivo cerrado (grep + lectura completa), no sobre la tabla que declaró el Escritor. A diferencia de `validacion_v0.3.md` (donde H2 y H5 no coincidían con lo declarado), en esta versión **mis conteos coinciden con los del Escritor en las nueve métricas**.

| # | Métrica | Umbral | Contado por mí | Declaró el Escritor | ¿Coincide? |
|---|---|---|---|---|---|
| H1 | Tricolones | ≤1/escena | Muestreo sobre apertura, Arturo, ambas escenas de Felipe y la escucha: cumple. Acepto la salvedad declarada (maratón final: 2 listas, ambas de contenido — inventario de qué queda puesto, no ritmo ternario) | 1/escena tras 6 correcciones, salvedad en el maratón | ✅ |
| H2 | «no era X, era Y» | ≤1/cap | **1** — "no fue por Ignacio, ni por la plata... Fue por la cara de Don Arturo" (L233). Verifiqué también L57 ("No era lindo. No era nada.") y L459 ("No fue lenta.") — ambas son negaciones factuales simples, no la antítesis evasiva del tell; no cuentan | 1 | ✅ |
| H3 | Frases-remate aforísticas | ≤2/cap | **2** — "Hacía falta, solamente, tomárselo entero." (L521) + "Estaba, por primera vez, del otro lado del mostrador." (L561). "Sal a vender café." es diálogo de cierre, no remate narrativo — no cuenta | 2 | ✅ |
| H4 | Abstractos que nombran el tema | 0 | **0** — grep específico sobre sumisión/dominación/humillación/fetiche/condicionamiento/objetivación/manipulación/hipnosis/trance/sugestión/programación/refuerzo: sin resultados | 0 | ✅ |
| H5 | «algo» como comodín | ≤2/cap | **2** — "Algo en el tono de las dos voces" (L371) + "algo en los hombros de Felipe se le aflojó" (L515). Grep case-insensitive encontró 6 apariciones más de "algo" (L209, L391×2, L393, L495, L511) — todas literales/idiomáticas ("sentir algo", "oír algo", "significaba algo", y L209 es ambigüedad deliberada anclada al mismo mecanismo de H12 en `cronologia.md`, no descuido) | 2 | ✅ |
| H6 | Dobletes de adjetivos | ≤3/cap | **3** — "pesadas y aceitadas" (L3), "dulce y barato" (L25), "rápida y aséptica" (L427) | 3 | ✅ |
| H7 | Cadenas de variación elegante | 0 | **0** — Cupcake, Felipe, Don Arturo/Arturo se repiten sin sinonimia; "Arturo" a secas es acortamiento, no variación elegante (mismo patrón ya usado en Cap 2, aprobado) | 0 | ✅ |
| H8 | Varianza de frase | ≥1 ≤5 y ≥1 ≥35 por 500 palabras | Cumple — frases de una palabra ("Trece.", "Los acercó.", "No.", "Se mojó de mirarse.") repartidas a lo largo del capítulo contra períodos largos en cada escena | cumple | ✅ |
| H9 | Lastre | L1/L2 por escena, L6 por cap | Presente — L1: la escoba subida y nunca bajada del privado (L289) + el paraguas del perchero que nadie reclama (L581); L2: el pensamiento del lavado cortado por el vaporizador (L333) + "si también la había encontrado así una mañana, parada frente a—" (L583); L6: el bloque de los doce días de recuperación (planta encargada de nadie, TV sin registrar) | presente | ✅ |

**Veredicto de humanización: ✅ LIMPIO.** Nueve de nueve dentro de umbral, y el reporte del Escritor resistió mi reconteo independiente — a diferencia de la v0.3 de este mismo capítulo, acá la autoverificación es evidencia confiable, no solo un reporte.

**Citas de los tells mejor resueltos (para que quede en registro, no son fallas):**
1. *"no fue por Ignacio, ni por la plata, ni siquiera por la promesa de la escalera. Fue por la cara de Don Arturo."* (L233) — la única antítesis del capítulo, y la más cargada temáticamente (el poder, no el sexo, como fuente del calor). Uso correcto del cupo.
2. *"algo en los hombros de Felipe se le aflojó, algo que llevaba meses sin aflojarse"* (L515) — comodín legítimo: el detalle físico exacto (qué músculo, qué tensión) sería sobre-especificación; la vaguedad es la textura correcta de un cambio que ni el propio personaje sabe nombrar.

## 1.5 Continuidad (cronología + costura + hechos plantados)

- **Línea de tiempo:** ✅ con un hallazgo que reporto en detalle. `cronologia.md` marca Cap 3 = "~Día 22-180", sin días de semana, y el propio capítulo abre con "Llevaba tres semanas" (L3) — coherente, tiempo relativo narrado en prosa, no en tabla. **Hallazgo:** L235 tiene diálogo de Cupcake — *"Vuelva el jueves, mi rey"* — un día de la semana suelto en el texto. La regla vigente (Ama 25/08/2026) dice literalmente que **ningún** día de la semana debe soltarse en el capítulo, "aunque cuadre aritméticamente". Lo reporto como violación de la letra de la regla. **Por qué no lo uso para tumbar el gate a DISCONTINUO:** (1) no ancla ningún hecho de `cronologia.md` ni contradice ninguna cuenta de días — es una frase de atención al cliente, no un anclaje temporal estructural; (2) el capítulo 2 ya aprobado (`capitulo_02_la_segunda_persona_v0.8.md`) usa la misma construcción sin corregir — "Lo necesito el lunes a primera hora" (L471) y "el jueves" aparece seis veces más como referencia activa ("hasta el jueves no le había pedido explicaciones", "el mismo del jueves", "se hizo el jueves en el camarín") — de modo que fallar solo a v0.6 por este patrón sería un doble estándar mío, no una aplicación pareja de la regla. Dejo la decisión de fondo (¿aplica retroactivamente al patrón ya establecido, o solo hacia adelante?) a la Ama, y sugiero la corrección de una palabra como opcional, no como condición de Gate.
- **Costura con cap previo:** ✅. Al abrir, "todavía los suyos, todavía sin la silicona que le faltaba por comprar" (L95) es consistente con el cierre de Cap 2 (sin cirugía). Nombre Cupcake, trato de Yasna, Yakarta, barra de acero, liga/liguero, aros cromados ya instalados: todo coincide con `cronologia.md` §4 (Cap 2). El pelo platinado y el maquillaje ya asentados al abrir el capítulo son consistentes con el peldaño 4 (pelo/pestañas) que canónicamente ocurre en el salto de ~3 semanas entre capítulos — no es una prenda/rasgo que aparezca sin anclar, es una transición fuera de página del mismo tipo que ya se usó entre Cap 1 y Cap 2.
- **Callbacks con ancla:** ✅ todos anclados.
  - *"La mesa. Como esa vez. En la mesa"* (L203) → ancla directa y verificada línea por línea contra `capitulo_02_la_segunda_persona_v0.8.md` (L499-557: la caoba, el informe del arbitraje, el fajo tomado delante de Roberto y las abogadas). Coincide en cada detalle.
  - *"Ja..."* de Don Arturo (L129) → consistente con H12 de `cronologia.md`: inquietud deliberadamente sin resolver, no un hecho que exija pago. El capítulo no la explica ni la vuelve a mencionar — correcto.
  - El nombre *cupcake* nunca vuelve a "Soto"/"Javiera" en boca de nadie → consistente con H8/H11 (Cap 2).
  - Los rasgos andróginos de Felipe (hombros que no llenan la camisa, cuello fino sin sombra de afeitada, pestañas largas, manos finas) sembrados en su primera aparición (L49) y cobrados en el cierre (L577) → auto-contenido dentro del propio capítulo, sin dependencia externa.
  - La cadenita/pelo/uñas de Felipe en el salto de tiempo final no tienen ancla previa específica, pero el propio texto las trata como la misma clase de anomalía-sin-explicación que el café servido antes de pedirlo (H9 del Cap 1) — es un recurso ya canonizado en este relato (Ley 3/4/5: el local no explica nada), no un callback fantasma a una escena inexistente.
  - `cronologia.md` ya está actualizado para reflejar v0.6 (H7, H13, H14 y el estado del cuerpo de Felipe) — no hay deuda documental pendiente de este capítulo.
- **Huecos a corregir:** ninguno bloqueante. Único hallazgo: el "jueves" de L235 (ver arriba) — recomendación, no condición de Gate.

## 2. Narrativa

### Pivotes del canon cumplidos

> Evalúo contra la versión vigente del arco (3 capítulos, sin cámara ni "sí informado" formal — ver nota de vara arriba), documentada en `cronologia.md` y en las instrucciones vivas del 23-28/08.

- ✅ **P3 — se le muere la coartada en la boca:** ejecución textual casi perfecta. *"Tenía una frase para esto, una que llevaba meses teniendo lista, con sujeto y verbo y coma en el medio: si averiguaba lo suficiente, si subía un peldaño más, si aguantaba un poco más, iba a poder— No se acordó de cómo terminaba."* (L393-397) es el Estado 4 (silencio) de M5 ejecutado al pie de la letra, disparado por la escucha accidental en la bodega, no por confrontación ni castigo — exactamente como pide `investigacion.md` §4.9.4 y §9.3.
- ✅ **Giro envidia → poder (directiva viva 23/08 y nota v0.5 §2e):** verificado en el texto — *"Camila era de alguien. Cupcake tenía a todos, y tenerlos le gustaba tanto que la boca se le hizo agua ahí mismo"* (L401) reemplaza limpiamente la envidia de v0.5. No hay ni un resto de autocompasión ni de "la pobre no sabía" (Cementerio §8).
- ✅ **Bajar es subir, cerrado en dos cuerpos:** la imagen final (ella con el pecho asentado, Felipe estrenando el top plateado, los dos frente al mismo espejo) ejecuta el mandato del canon sin una sola línea de moraleja ni rescate — cumple el Cementerio §8 punto final ("ni una línea que le dé permiso al lector de sentirse bien").

### Calidad técnica

- **POV:** estable. Tercera persona pegada a Cupcake, sin fugas, en las 598 líneas.
- **Vocabulario chileno:** ✅. Verificado con grep: cero voseo verbal chileno, cero artículo antes de nombre propio, cero léxico de España (`polla/follar/joder/coche/piso/móvil/bragas/vale/tío`), cero voceo argentino, cero léxico clínico (`vagina/pene/glúteos/senos`). El color local vive en sustantivos de oficio (la barra, la tarima, el turno, el casero, la cuota, el minuto, el privado, la liga, las lucas) — dentro del 5% que exige `canon_relato.md` §7.
- **Veto léxico de la Ama:** ✅ cero "degradación"/"hipersexualizada" y variantes, cero vocabulario del mecanismo (hipnosis/trance/sugestión/condicionamiento/refuerzo/manipulación/programación) fuera de diálogo — y tampoco aparece en diálogo.
- **Buzzwords AI:** ninguna detectada (crucial, tapiz, intrincado, profundizar: 0 apariciones).
- **Formato:** separadores `***` consistentes con Cap 1/2 — corrige la inconsistencia que `validacion_v0.3.md` había señalado.

### Score Narrativa: 9.0

Sube frente a v0.3 (8.3) porque los dos focos de aquella validación —la discrepancia de conteo H2/H5 y el pivote P4 mal escenificado— ya no están: acá los conteos de humanización coinciden con lo declarado, y el arco de 3 capítulos no necesita ya el "tramo ciego" de P4 (derogado junto con el mapa de 9 capítulos). No llega más alto por el hallazgo de continuidad del "jueves" (cosmético, no bloqueante) y por la extensión considerable del capítulo (~11.000 palabras estimadas, ver Notas) — extensión que la propia Ama autorizó en vivo al agregar las dos escenas de Felipe sobre la marcha, así que no lo penalizo como error, solo como techo del puntaje.

## 3. 🔥 Temperatura — ¿es erótico? ¿está caliente?

| # | Medida | Resultado |
|---|--------|-----------|
| T1 | **¿Es erótico?** | ✅ erótico. Quitado el contenido sexual (minuto feliz, corbata/muñeca de Arturo, privado de Ignacio, masturbación post-cirugía, las dos escenas de Felipe, el maratón de 4 privados) no queda estructura suficiente para un capítulo — es un relato erótico con una línea de investigación que se cierra como subtexto administrativo (la escucha de la bodega), no al revés. |
| T2 | **¿Calienta?** (¿se desean, o uno solo se excita?) | ✅ sí, y de forma explícita mutua en el eje central (Felipe): él tiembla, obedece, pide ("Lo que tú quieras. Lo que tú me quieras hacer."), se corre dos veces con reacción física completa, y ella se moja, decide, se corre primero mirándolo. No es un personaje caliente solo mientras el otro ejecuta — ambos cuerpos reaccionan en escena. En el eje de control (Arturo/Ignacio) el diseño es deliberadamente asimétrico por canon (ella decide, ellos desean) y funciona como está pedido: el calor de ella viene del poder, no de que Arturo/Ignacio también gocen simétricamente — y eso es exactamente lo que pide `canon_relato.md` §8. |
| T3 | Explicitud léxica | ✅. Los seis términos del léxico sucio autorizado aparecen 23 veces combinadas (verga/coño/culo/coger/mojar/tetas, verificado con grep). Cero eufemismos evasivos de la lista fija. Grep específico de la ampliación 05/08 ("calor difuso/repartido/sin punto fijo/sin centro", Fragmento 7 de `antologia_calenton.md`): **0 coincidencias** — no clona el fragmento prohibido. |
| T4 | Suciedad del registro vs `antologia_calenton.md` | ✅. El registro de los privados y las dos escenas de Felipe está tan sucio como el material de referencia, sin pulir el clímax en prosa literaria. Las órdenes de control ("Mírame. No cierres los ojos.", "Todavía. No.", "Di mi nombre.") replican el registro de mando seco que la antología premia en Valeria, adaptado a esta voz. |
| T5 | Descarga real en escena | ✅. Al menos seis descargas completas en página, sin elipsis ni corte de cámara: masturbación post-cirugía (L459-461), el tercer privado del maratón (L479), la ejecutiva (L483), Felipe #1 (ella reserva su descarga a propósito — decisión de ritmo narrativo, no elisión: Felipe sí termina, en escena, L555), Felipe #2 (ella se corre primero, L553, él después, L555 [sic, ver numeración real: L553/555 del bloque de cierre]). |
| T6 | Densidad de subrayables | Estimado ~8/1000 palabras (capítulo largo y saturado). Anclaje anatómico fuerte: bien por encima de la mitad de las imágenes citables usan léxico anatómico o de acción sexual directa (aros cromados, silicona, uñas fucsias clavadas, verga/coño en los privados) y no solo atmósfera. |
| T7 | Motivos permanentes por escena · curva de resistencia | ✅. M1 (mirada) y M4 (la cuenta) en cada escena de barra. M3 (olor) presente al abrir cada bloque de local (café quemado, aceite de coco, acetona y laca en el camarín). M2 (taco) más encarnado que en la v0.3 de este capítulo — el callo, la plataforma clavándose en el empeine, el Pleaser. M5 (coartada) llega correctamente a Estado 4 (silencio, P3). M7 (el otro yo) correctamente en silencio total — cero apariciones de voz separada, consistente con étape 4 declarada en `cronologia.md`. **Curva de resistencia:** correcta para el punto del arco — resistencia casi nula es lo que corresponde a este tramo tardío, no una falla. |
| T8 | Apertura | ✅. El contraste pelo platinado/pelo de oficina, la chica nueva midiéndose el escote, y a Cupcake calculando su propio reflejo en vez de mirar a la nueva enganchan desde la primera página. |

### Las 3 frases MÁS CALIENTES del capítulo

1. *"El poder le sabía mejor que cualquier verga que hubiera tenido adentro en toda su vida, y lo sabía con una certeza tan limpia que no necesitaba compararlo con nada para estar segura."* (L233) — el calor viene del control, no de la penetración: ejecución exacta del Cementerio §8 del canon.
2. *"Se corrió ella primero, apretada alrededor de la verga de Felipe, mojada hasta los muslos, con los ojos abiertos sobre la cara obediente que la miraba correrse como si mirar también fuera un trabajo que ella le hubiera asignado."* (L553) — deseo mutuo explícito, con la inversión de poder (de condicionada a condicionadora) como fuente del morbo.
3. *"No hacía falta ser mujer para que funcionara. No hacía falta el taco, ni la tarima, ni las ocho horas de pie. Hacía falta, solamente, tomárselo entero."* (L521) — el remate que cierra el eje temático (M8) en la misma escena donde ocurre, no como explicación posterior.

### Los 2 pasajes MÁS FRÍOS

1. *"Fueron doce días fuera del turno. Doce días sin el neón violeta, sin el beat subiéndole por la planta de los pies... y viendo la televisión sin registrar ni un solo programa entero."* (L429-435) — frío por diseño (es el lastre L6 exigido por `HUMANIZADOR.md` y el silencio de M7 que necesita space para notarse), pero es, objetivamente, el tramo de menor temperatura del capítulo.
2. *"—¿Y cómo anda? [...] —Como todas. No se acuerda de la semana. Ni un turno entero."* (L367-369) — la escucha de la bodega, correctamente escrita en registro administrativo/seco (Ley 4-5), pero es la escena de menor carga sensorial de todo el capítulo por diseño: es donde se cierra la línea de investigación, no una escena erótica.

### Eufemismos evasivos detectados

Ninguno.

### Score Temperatura: 9.2

T1 y T2 ambos ✅. Sube frente a v0.3 (8.8) porque T7/M2 (el taco) está más encarnado y el eje de deseo mutuo con Felipe queda mucho más explícito y físico que en v0.3 (que solo llegaba hasta el vaso servido, sin escena). No llega a 9.5+ porque los dos pasajes fríos, aunque correctos por diseño, siguen restando densidad al promedio, y porque la coexistencia de la escena de mayor explicitud (Felipe #2, con penetración) junto a la regla del Cementerio §8 exige una lectura fina (el calor está en el control, no en el acto) que un lector desprevenido podría no distinguir tan nítido como en la escena de Arturo/Ignacio.

## 4. Voz Autoral

`01_Canon/voz_autoral.md` no tiene entradas propias de este proyecto — medí contra Cap 1/2 aprobados.

### Tics canónicos activados (verificados contra Cap 1/2)
- La cuenta mental heredada de la abogada — "contaba con la misma parte de la cabeza con la que antes contaba plazos procesales, y esa parte, ahora, solo servía para esto" (L89) — podado a 3 apariciones (mañana/privado/cierre) según la propia auditoría de tics del brief, consistente con el pedido de la Ama de bajar la repetición.
- El paréntesis físico-objetivo en vez de la explicación emocional (línea rosada de la barra, callo del meñique, costra) — consistente con el "lente 1" transversal del corpus.
- Yasna dice la cosa una vez y cambia de tema — "Bien hecho... A ese hay que tenerlo con hambre" seguido inmediato de "¿Cuánto llevas hoy?" (L347-351) — respeta al pie de la letra el "nunca insiste" del canon.
- "Mi rey"/"mi amor" de Cupcake hacia los clientes — consistente con Cap 1 y con el registro de coqueteo transaccional ya establecido.

### Frases nuevas candidatas para incorporar a `voz_autoral.md` / `antologia_calenton.md`
- *"No hacía falta ser mujer para que funcionara [...] Hacía falta, solamente, tomárselo entero."* (L521) — condensa el eje M8 (el vector cruzando de mujer a hombre) en una frase, sin nombrar el mecanismo.
- *"Ponte el pulgar acostado abajo del hueso del medio del pecho [...] Donde termina el pulgar, va el borde."* — la "regla del pulgar" funciona como bisagra estructural (abre y cierra el capítulo, primero enseñada a ella y después por ella) — candidata más como técnica de construcción (callback físico medible) que como frase suelta.
- *"Camila era de alguien. Cupcake tenía a todos, y tenerlos le gustaba tanto que la boca se le hizo agua ahí mismo, sin ningún casero al frente."* (L401) — resuelve en una frase el giro envidia→poder que pidió la Ama, sin explicarlo.

## 5. Micro-fixes sugeridos

No aplica — el veredicto es APROBADO, no MICRO-FIX. Dejo registrado, solo como sugerencia opcional y no vinculante a criterio de la Ama, el cambio de una palabra en L235: *"Vuelva el jueves, mi rey"* → *"Vuelva pronto, mi rey"* (o equivalente sin día de semana), por la regla de continuidad del 25/08 — ver detalle y mi razonamiento para no bloquear el Gate por esto en la sección 1.5.

## 6. Notas

- **Verificación independiente de las Cinco Leyes (`canon_relato.md` §1b):**
  - **Ley 1 (nadie la obliga):** ✅. Felipe vuelve solo, paga sin que se lo pidan, toma el vaso porque se lo ofrecen "con la naturalidad de quien pone un vaso de agua" (L503) — nunca se le impone.
  - **Ley 2 (bajar es subir):** ✅. La transformación de Felipe se narra como soltura ganada ("una economía de movimientos que antes no tenía", L579), nunca como pérdida; "Sal a vender café" es ascenso, no castigo.
  - **Ley 3 (el local sabe y no hace nada distinto):** ✅. La escucha es accidental — no hay señal de que Yasna o don Nelson supieran que Cupcake estaba en el pasillo. Nadie en el Yakarta comenta el tránsito de Felipe.
  - **Ley 4 (nadie explica el mecanismo):** ✅. Cero léxico clínico o del mecanismo, verificado con grep. La escucha de la bodega describe efectos ("no hace que les guste... hace que se les olvide que no les gustaba") sin nombrar nunca una sustancia o técnica — dentro de lo ya autorizado por `canon_relato.md` §6b-bis.
  - **Ley 5 (nadie es villano):** ✅. Registro amable transversal sostenido hasta el final; el "horror" queda entero del lado del lector.
- **Extensión del capítulo:** no pude ejecutar un conteo de palabras exacto (este entorno de Validador no tiene herramienta de shell). El Escritor declara ~10.980 palabras en su autoverificación; no lo tomo como dato verificado por herramienta, pero es plausible dada la extensión visible (598 líneas de prosa densa). El criterio 7 del brief original (bajar de ~9.750 palabras) quedó derogado de facto por la orden viva §0ter, que agregó dos escenas completas de Felipe sobre la marcha — coherente con `feedback_relato_fluir_no_word_count.md` (el relato fluye, no se restringe por conteo).
- **Decisión de autoría no fijada por el brief, señalada por el propio Escritor:** Felipe termina *dentro* del local (acomodando tazas, top de la casa) en vez de solo como cliente transformado. El Escritor lo sostiene en la directiva viva sobre "abrir nuevos públicos, en el café" y en el "a su lado" literal de la orden §0ter. Es una lectura razonable del texto vivo, pero es una decisión creativa con espacio de interpretación — si la Ama la lee distinto, es un fix acotado a los últimos dos párrafos, no una reescritura.
- **Es el cierre del relato completo, no de un capítulo intermedio:** verificado que no hay epílogo, rescate ni moraleja (Cementerio §8) — termina en acción y diálogo ("Sal a vender café"), con la imagen de los dos cuerpos frente al espejo sosteniendo el "bajar es subir" del canon en ambos personajes a la vez.
