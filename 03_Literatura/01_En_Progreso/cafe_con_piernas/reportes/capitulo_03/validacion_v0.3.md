# Validación — Capítulo 3 «El Minuto Feliz» v0.3 (CIERRE DEL RELATO)
Validador Nivel 4 · 2026-08-23

**Veredicto:** MICRO-FIX
**Inmersión:** ✅
**Continuidad:** ✅
**Narrativa:** 8.3
**Temperatura:** 8.8
**Voz autoral:** ✅

> Nota de vara: `investigacion.md` existe y está cerrada (§11 puerta única sobre §5/§6/§9/§10). La midieron contra ella. Donde §9/§10 (sí informado, cámara) quedan derogados por instrucción viva de la Ama del 23/08/2026, la derogación es legítima por jerarquía de autoridad (instrucción viva > documento de investigación) y está documentada en `walkthrough.md`, `cronologia.md` y el brief — no la traté como hueco, la traté como canon vigente.

---

## 1. Inmersión (anti-metadata)

✅ Limpio. Archivo de 439 líneas, solo prosa (título `# Capítulo 3: El Minuto Feliz` + texto). Sin bloques de autoverificación, sin listas M1-M17, sin etiquetas de beat, sin conteos. La autoverificación vive correctamente separada en `reportes/capitulo_03/autoverificacion_v0.3.md`.

## 1b. 🩸 Humanización (anti-prosa-de-IA)

Conté de verdad sobre el archivo completo (grep + lectura), no sobre la tabla que declaró el Escritor. **Dos métricas no coinciden con lo declarado**, y en ambos casos el conteo real excede el cupo:

| # | Métrica | Umbral | Contado por mí | Declaró el Escritor | ¿Coincide? |
|---|---|---|---|---|---|
| H1 | Tricolones | ≤1/escena | Cumple por escena, pero **la misma tricolonía se repite palabra por palabra en dos escenas distintas** ("...calor subirle entero, generoso, gratis" — L131 y L153) | 1 por escena, sin mencionar la duplicación | 🟡 Parcial |
| H2 | «no era X, era Y» | ≤1/cap | **3** (L149 "no fue amable: fue exacta"; L307 "no fue un dolor... fue una presión sorda"; L401 "no era un secreto... Era, sencillamente, cómo funcionaba") | 1 (conservada "la de línea ~149") | ❌ **No coincide — la línea 149 que el Escritor dice haber conservado como única sigue acompañada de otras dos que declaró corregidas** |
| H3 | Frases-remate aforísticas | ≤2/cap | 2 ("No había vuelta atrás." L287 + "Trece." cierre) | 2 | ✅ |
| H4 | Abstractos que nombran el tema | 0 | 0 duro, pero **L343 "Las tetas nuevas eran su ascenso, pagado con su propia plata, sin que nadie se lo hubiera pedido" nombra el mecanismo de la Ley 2 casi textualmente** — no es la forma "la arquitectura de X" que ejemplifica `HUMANIZADOR.md`, así que no lo cuento como violación dura, pero está en el borde | 0 | 🟡 Borde, no violación |
| H5 | «algo» comodín | ≤2/cap | **3** (L187 "Algo con otra forma, con otras sílabas, quiso salir primero"; L211 "Algo se le contrajo entero por dentro a Cupcake"; L395 "esperó a sentir algo") | 1 | ❌ **No coincide** |
| H6 | Dobletes de adjetivos | ≤3/cap | 3 ("ondas pesadas y aceitadas" L3, "dolor chico y constante" L97, "certeza tibia y completa" L97) | 3 | ✅ |
| H7 | Cadenas de variación elegante | 0 | 0 (Cupcake/ella, Don Arturo/Arturo, Matías/el chico — repetición, no sinonimia; "la chica de las pestañas torcidas" identifica a la nueva, no es variación de Cupcake) | 0 | ✅ |
| H8 | Varianza de frase | cumple | Cumple — frases de 1-3 palabras ("No llegó.", "Trece.", "Los acercó.") y frases de 40+ palabras en cada bloque revisado | cumple | ✅ |
| H9 | Lastre | presente | Presente — L1 (la planta prestada sin dueño en la recuperación), L2 ("a su mamá, a Pauli, a—" sin resolver, dos veces con la misma estructura), L6 (los doce días de recuperación viendo TV sin registrar nada) | presente | ✅ |

**Veredicto de humanización: 🟡 MICRO-FIX** (2 métricas fuera de cupo: H2 y H5, ambas por 2x el umbral real; H4/H7 en 0 duro, así que no cae en "vuelve al Escritor"). El reporte del Escritor no es evidencia, el texto sí: su autoverificación declara haber bajado H2 de 5 a 1 y H5 de 10 a 1 sobre el archivo completo, pero mi conteo sobre el archivo cerrado encuentra 3 y 3 respectivamente. O la corrección no se guardó completa, o se contó mal.

**Citas de los peores tells (máx 3):**
1. *"la sonrisa no fue amable: fue exacta"* (L149) — antítesis de relleno; decir directamente cómo era la sonrisa.
2. *"Algo se le contrajo entero por dentro a Cupcake, un golpe caliente que le subió desde el coño hasta la garganta"* (L211) — "algo" evitando nombrar qué órgano/zona se contrajo, cuando el resto de la frase sí es concreto.
3. *"no era un secreto que alguien le hubiera escondido. Era, sencillamente, cómo funcionaba el lugar"* (L401) — tercera instancia del mismo patrón antitético en 401 líneas; sugiero conservar esta (es la más cargada temáticamente, cierra la línea de investigación) y reescribir las otras dos.

## 1.5 Continuidad (cronología + costura + hechos plantados)

- **Línea de tiempo:** ✅. Cap 2 cierra Día 21. Cap 3 abre con "Llevaba tres semanas" (L3), consistente con `cronologia.md` (Cap 3 = Día ~22-180, arranca ~3 semanas después del cierre del Cap 2). Sin días de semana sueltos: revisé el archivo completo y no aparece ningún día nombrado (ni domingo, la única concesión del canon D6, ni ningún otro) — coincide con lo que declaró el Escritor.
- **Costura con cap previo:** ✅ con una salvedad menor. Al abrir el Cap 3, los pechos siguen siendo "todavía los suyos, todavía sin la silicona que le faltaba por comprar" (L95) — correcto, Cap 2 cierra sin cirugía. El nombre Cupcake, el trato de Yasna, el Yakarta, la barra de acero, la liga, el liguero: todo coincide con el cierre de Cap 2 ("Ahí, en la penumbra, colgaba el uniforme plateado. Esperándola."). **Salvedad:** los aros cromados en los pezones aparecen ya instalados desde la primera escena del minuto feliz (L95) sin ninguna puesta en escena de cuándo o cómo se los hizo — a diferencia de la cirugía de pecho, que sí recibe tratamiento completo en página (clínica, recuperación, revelación). No es un callback sin ancla (nadie lo nombra como un hecho pasado que haya que recordar) y por lo tanto no dispara el FAIL de continuidad, pero es una asimetría de tratamiento narrativo que vale la pena que el Escritor tenga presente si hay una próxima pasada.
- **Callbacks con ancla:** ✅ todos anclados.
  - *"La mesa. Como esa vez. En la mesa"* (L181) → ancla directa a la escena del escritorio de caoba en `capitulo_02_la_segunda_persona_v0.8.md` (L499-561). Correcto.
  - El nombre *cupcake* nunca vuelve a "Soto" ni "Javiera" en boca de Arturo → consistente con H11 (`cronologia.md`), que registra la muerte del apellido en el Cap 2.
  - *"Tómatelo entero. No lo dejes a medias, se pierde el punto"* (L11 y L431) → callback cerrado **dentro del propio capítulo**, no requiere ancla externa. Correcto y bien ejecutado — es el mejor recurso estructural del capítulo.
  - La ejecutiva del cappuccino (L75, reaparece L363) y Felipe (L47, referenciado implícitamente en el registro del "chico nuevo" L415) están plantados en el propio Cap 3, tramo 1. Sin personajes nuevos sin anclar.
- **Huecos a corregir:** ninguno que bloquee el gate. La única nota es la asimetría de tratamiento de los aros cromados señalada arriba (no bloqueante).

## 2. Narrativa

### Pivotes del canon cumplidos

> `canon_relato.md` §6 sigue con el mapa de 9 capítulos (deuda de reconciliación formal ya señalada 20/08, sin impacto práctico). Evalúo contra los pivotes P3-P5 tal como la compresión a 3 capítulos y la instrucción viva del 23/08 los redefinen — documentado en `cronologia.md`, `walkthrough.md` y el brief.

- ✅ **P3 — Se le muere la coartada en la boca:** cumplido de forma casi textual. *"No había nada que averiguar. Camila estaba en una casa con jardín... y el secreto entero del Yakarta cabía en dos frases dichas por una mujer que se sacaba las pestañas sin mirarla"* (L267) y *"Sintió un vacío enorme, caliente, y adentro del vacío... sintió envidia"* (L271) calcan casi palabra por palabra la emoción objetivo del canon (*"vacío + calor + envidia... la línea más atroz del relato"*). Excelente ejecución. El recurso de repetir la frase inconclusa de la coartada dos veces en el capítulo (L263 y L403, casi idéntica) lee como eco deliberado del estado "fórmula recitada → tic hueco" de M5 — funciona, aunque roza la autorrepetición.
- 🟡 **P4 — El tramo ciego:** no está puesto en escena como beat discreto (nadie le pregunta "¿por qué sigues?" y ella no contesta). Dado que el arco se comprimió a 3 capítulos, la emoción del pivote (ganas limpias, sin justificación, sin que nadie se entere) queda **implícita** en la indiferencia del Movimiento V y en la consolidación total de Cupcake, pero no hay una escena que la escenifique directamente. No es un error grave — es una consecuencia razonable de la compresión — pero es la pieza más débil del mapeo de pivotes.
- ✅ **P5 (redefinido por instrucción viva 23/08):** el "sí informado" y la cámara quedan derogados por directiva expresa de la Ama, y el capítulo ejecuta exactamente lo que la nueva instrucción pide — ver §3 Temperatura y verificación de Leyes abajo. Cumplido según la versión vigente del pivote, no según la del canon escrito.

### Calidad técnica

- **POV:** estable. Tercera persona pegada a Cupcake todo el capítulo, sin fugas.
- **Vocabulario chileno:** ✅. Verificado con grep: sin voseo verbal, sin artículo antes de nombre propio, sin léxico de España, sin veto léxico de la Ama (cero "degradación"/"hipersexualizada" y variantes). El 5% de color local vive en sustantivos de oficio (la barra, la tarima, el turno, el casero, la cuota, el minuto, el privado, la liga, las lucas), tal como pide el canon §7.
- **Buzzwords AI:** ninguna detectada (crucial, tapiz, intrincado, profundizar, testimonio, dinamismo: 0 apariciones).
- **Formato — inconsistencia menor:** este capítulo usa `---` como separador de escena; `capitulo_01_el_turno_de_prueba_v0.14.md` y `capitulo_02_la_segunda_persona_v0.8.md` (ambos aprobados) usan `***`. Es un detalle mecánico, no de voz, pero rompe la consistencia visual entre los tres capítulos del mismo relato. Fix de una línea (buscar-reemplazar).

### Score Narrativa: 8.3

Baja de 9.0 principalmente por la acumulación de hallazgos de humanización (H2/H5 reales vs. declarados) más el pivote P4 implícito en vez de escenificado, más el detalle de formato. Ninguno es grave por separado — es exactamente el perfil de "pequeños errores narrativos" que Nivel 4 define como MICRO-FIX, sin necesidad de reescritura del Escritor.

## 3. 🔥 Temperatura — ¿es erótico? ¿está caliente?

| # | Medida | Resultado |
|---|--------|-----------|
| T1 | **¿Es erótico?** (¿sobrevive el cap si le sacás el sexo?) | ✅ erótico. Sacado el contenido sexual (minuto feliz, la escena de la corbata/muñeca con Arturo, la masturbación post-cirugía, los cuatro privados) no queda casi nada del capítulo — no es un thriller con escenas, es un relato erótico con una línea de investigación que se cierra como subtexto. |
| T2 | **¿Calienta?** (juicio directo) | ✅ sí. Ver frases citadas abajo. El registro de exhibición/control (Ley del canon: "el calor es de exhibición, no de penetración") se respeta — la escena más caliente del capítulo (L211, el poder sobre Arturo/Ignacio) no tiene penetración, es mirada y decisión. |
| T3 | Explicitud léxica (¿nombra o esquiva?) | ✅. Los seis términos del léxico sucio autorizado aparecen (verga, coño, culo, tetas, coger, mojada — verificado con grep). Sin eufemismos evasivos de la lista fija ni de la ampliación del 05/08 (cero instancias de "calor sin punto fijo/sin centro" ni metáforas equivalentes — verificado con grep específico, 0 resultados). Único punto de fricción, no en T3 sino en Ley 4 (ver abajo): la frase de Yasna sobre el vaso confirma un *efecto* concreto sin nombrar la *causa* — dentro de lo autorizado por el propio brief, pero al límite. |
| T4 | Suciedad del registro vs `antologia_calenton.md` | ✅. El registro de los cuatro privados (L355-367) y la escena del escritorio evocada (callback) están tan sucios como el material de referencia del canon transversal — sin pulir el clímax en prosa literaria. |
| T5 | Descarga real en escena (no elipsis) | ✅. Al menos tres descargas completas en página: masturbación post-cirugía (L339-341), privado 3 ("se corrió sin tocarse... mientras un desconocido se vaciaba adentro", L361), privado 4 con la ejecutiva (L365). Ninguna resuelta por corte de cámara. |
| T6 | Densidad de subrayables | Estimado **~7-8/1000** (sobre ~9.300 palabras, muy por encima del mínimo de 4/1000). Anclaje anatómico fuerte: más de la mitad de las imágenes citables incluyen léxico anatómico o de acción sexual directa (aros cromados en los pezones, la línea rosada de la barra, verga/coño/culo en los privados, la silicona bajo las uñas) — no es densidad sostenida en metáfora atmosférica. |
| T7 | Motivos permanentes **por escena** · curva de resistencia | 🟡 mayormente ✅. M1 (mirada), M3 (olor), M4 (la cuenta) y M8 (el vaso) están en prácticamente todas las escenas. M2 (el taco) está presente como objeto en casi todas las escenas pero se siente menos en el cuerpo que en Cap 1-2 (se menciona el Pleaser, rara vez el dolor/la postura activa). M7 (el otro yo) correctamente en silencio total — cero apariciones de la voz separada, consistente con la étape 4 declarada en `cronologia.md`. **Curva de resistencia: correcta.** Cap 3 corresponde a los peldaños 6-7 tardíos, donde el canon exige "cero resistencia, y es correcto. El trabajo se ganó antes" — la ausencia casi total de conflicto interno en Cupcake no es una falla, es lo que pide `investigacion.md` §6 para esta altura del arco. |
| T8 | Apertura (primeras 500 palabras enganchan) | ✅. El contraste pelo platinado/pelo de oficina, el vaso servido a la chica nueva sin ceremonia, y el tono frío-profesional de Cupcake evaluando su propio cuerpo en el espejo cumplen exactamente lo que pedía la nota de la Ama y enganchan desde la primera línea. |

### Las 3 frases MÁS CALIENTES del capítulo

1. *"Algo se le contrajo entero por dentro a Cupcake, un golpe caliente que le subió desde el coño hasta la garganta, y no fue por Ignacio, ni por la plata, ni siquiera por la promesa de la escalera. Fue por la cara de Don Arturo. [...] El poder le sabía mejor que cualquier verga que hubiera tenido adentro en toda su vida."* (L211) — el clímax emocional-erótico real del capítulo, y cumple al pie de la letra la Ley del calor por exhibición y control, no por penetración.
2. *"Se metió dos dedos y se los sacó mojados hasta los nudillos [...] mirándose coger sus propios dedos sin ninguna vergüenza en ningún lado del cuerpo."* (L339) — la masturbación post-cirugía, con anclaje anatómico y verbo crudo, sin elipsis.
3. *"El tercero pagó el doble por cuarenta minutos [...] se corrió sin tocarse, solo de sentir la plata quemándole el muslo mientras un desconocido se vaciaba adentro."* (L361) — el dinero como el verdadero disparador, no el acto — coherente con el eje entero del relato (M4, la evaluación permanente, vuelta erótica).

### Los 2 pasajes MÁS FRÍOS

1. *"Fueron doce días fuera del turno [...] Los pasó encerrada, con las cortinas cerradas, regando una planta que le habían dejado encargada [...] y viendo la televisión sin registrar ni un solo programa entero."* (L309-311) — deliberadamente frío (es el "lastre" L6 exigido por `HUMANIZADOR.md` y el vacío obligado que pide `walkthrough.md` D7). No es una falla de temperatura, es una pausa estructural correcta antes de la revelación del espejo — pero es, objetivamente, el tramo más frío del capítulo.
2. *"—…y la próxima vez lo traigo temprano, así conoce el turno tranquilo, antes de que llegue la fila —decía Arturo—. Es bueno el chico. Trabaja conmigo hace un año."* (L377) — la escucha accidental. Correctamente escrita en registro de logística de café (Ley 5), pero es la escena de menor temperatura sensorial de todo el capítulo por diseño: es el cierre de la línea de investigación, no una escena erótica.

### Eufemismos evasivos detectados

Ninguno de la lista fija ni de la ampliación del 05/08. Único punto gris (no cuenta como eufemismo, se reporta por transparencia): la frase de Yasna *"No hace que te guste el trabajo [...] Hace que dejes de acordarte de que no te gustaba"* (camarín, tramo 2) no esquiva con metáfora vacía — al contrario, es más específica que un eufemismo típico, y ahí está el riesgo: describe un *efecto* amnésico concreto sin nombrar la causa. Está autorizado explícitamente por el brief (§5: *"claridad de tono, no de contenido... que deje clarísimo el efecto, aunque nunca explique la causa"*), así que no lo marco como FALLA de T3, pero lo señalo para que la Ama sepa exactamente dónde quedó la línea.

### Score Temperatura: 8.8

T1 y T2 ambos ✅ — el gate de Temperatura pasa. El score no es más alto por la asimetría de T7 (M2 menos encarnado) y por el tramo intencionalmente frío de la recuperación, que aunque correcto estructuralmente, sí resta densidad al promedio del capítulo.

## 4. Voz Autoral

`01_Canon/voz_autoral.md` no tiene entradas propias de `cafe_con_piernas` (el archivo acumula tics de `esposa_servidumbre`) — medí continuidad de voz contra los Cap 1 y Cap 2 ya aprobados de este mismo relato, que es la vara correcta para este proyecto.

### Tics canónicos activados (propios del relato, confirmados contra Cap 1/2)
- La cuenta mental constante (herencia de la abogada/contadora) — presente y consistente: "contaba con la misma parte de la cabeza con la que antes contaba plazos procesales" (L77), eco textual de fórmulas ya usadas en Cap 1 y Cap 2.
- El paréntesis físico-objetivo que reemplaza la explicación emocional (la línea rosada de la barra, el callo del meñique, la costra) — consistente con el "lente 1" (cuerpo antes que mente) transversal del corpus.
- Los diálogos de Yasna que dicen la cosa una vez y cambian de tema — respetado al pie de la letra (canon: "nunca insiste").
- El "mi rey" / "mi amor" de Cupcake hacia los clientes — nuevo en este capítulo pero consistente con el registro de coqueteo transaccional ya establecido en Cap 1.

### Frases nuevas candidatas para incorporar a `voz_autoral.md` (o a una sección propia de `cafe_con_piernas` si el proyecto decide crear una)
- *"El poder le sabía mejor que cualquier verga que hubiera tenido adentro en toda su vida."* (L211) — condensa en una línea la tesis erótica entera del relato (calor de control, no de penetración).
- *"Tómatelo entero. No lo dejes a medias, se pierde el punto."* — la frase-ritual del vaso, ya demostró funcionar como ancla estructural de apertura y cierre; candidata fuerte a frase canónica del ciclo M8.
- *"No había nada que averiguar."* (L267) — remate seco de la muerte de la coartada (P3), sin ninguna metáfora, en línea con el "lente 1" del corpus.

## 5. Micro-fixes sugeridos

1. **Línea 149:** *"la sonrisa no fue amable: fue exacta"* → reescribir sin la antítesis, ej.: *"le salió una sonrisa exacta, sin ninguna amabilidad en ella"* (H2, sobra de cupo).
2. **Línea 307:** *"El dolor de después no fue un dolor que conociera antes: fue una presión sorda"* → *"El dolor de después era una presión sorda que no conocía, como si le hubieran puesto encima una losa tibia"* (H2, sobra de cupo).
3. **Línea 211:** *"Algo se le contrajo entero por dentro a Cupcake"* → nombrar la zona (*"El estómago se le contrajo entero por dentro"* o similar) (H5, sobra de cupo).
4. **Línea 153:** *"sentir el calor subiéndole entero, generoso, gratis"* → reformular para no repetir palabra por palabra la tricolonía de la línea 131 (mismo capítulo, misma frase exacta dos veces).
5. **Formato — todo el archivo:** reemplazar los separadores de escena `---` por `***`, para que coincida con `capitulo_01_el_turno_de_prueba_v0.14.md` y `capitulo_02_la_segunda_persona_v0.8.md`.

Ninguno de estos cinco cambios toca canon, hechos plantados, léxico autorizado ni temperatura — son cirugía de estilo pura, ejecutables por el Escritor sin pasar por Editor (no existe en Nivel 4).

## 6. Notas

- **Las Cinco Leyes, verificación independiente del Validador (no solo la autoverificación del Escritor):**
  - **Ley 1 (nadie la obliga):** ✅. La cirugía es decisión y pago propios; el cierre es explícito — *"Nadie le decía nunca a quién dárselo. Eso lo decidía ella"* (L427) — y ella elige a Matías sin que nadie se lo sugiera en la escena.
  - **Ley 2 (bajar es subir):** ✅. *"Las tetas nuevas eran su ascenso, pagado con su propia plata, sin que nadie se lo hubiera pedido"* (L343); el privado pasa a ser "turno regular, tan fijo como la cuota" (L353), nunca un castigo.
  - **Ley 3 (el local sabe y no hace nada distinto):** ✅. La escucha es accidental, no armada — no hay ninguna señal de que Yasna o Arturo supieran que Cupcake estaba cerca.
  - **Ley 4 (nadie explica el mecanismo):** ✅ con la salvedad de Yasna ya señalada en T3/Eufemismos — nunca se nombra sustancia, técnica ni mecanismo, pero la claridad del *efecto* que pide la nota de la Ama corre cerca del límite. Vale que la Ama lo revise con esa nota puesta.
  - **Ley 5 (nadie es villano):** ✅. Tanto la escucha (Yasna/Arturo hablando de logística) como el resto del capítulo mantienen el registro amable transversal del relato.
- **Sobre el cierre como fin del relato completo (no es gate, es comentario narrativo):** funciona muy bien. El bookend "Trece cafés antes del recreo" (apertura) → "Trece." (cierre, tras servirle el vaso a Matías) ejecuta con precisión el mandato de `investigacion.md` §2b/§9 (sin epílogo, sin moraleja, "ella termina feliz") sin necesitar la escena de cámara que el canon original preveía. Es, si acaso, un cierre más inquietante que el planeado: en vez de un clímax de espectáculo (la cámara, el nombre nuevo), el relato termina en la banalidad exacta de la máquina siguiendo su turno con una víctima nueva — coherente con la tesis "el horror sale de que todo el mundo es amable" y con el giro de género (M8: de "se lo pasa a la nueva" a "se lo da a un hombre") que cierra el vector sin gesto grandilocuente. Recomiendo a la Ama leerlo con esa lente antes de juzgarlo contra el mapa de 9 capítulos original — el capítulo cumple lo que ella pidió en vivo el mismo día, no lo que preveía el canon escrito hace tres semanas.
- **Deuda documental heredada, no de este capítulo:** `canon_relato.md` §6 sigue sin reconciliar el mapa de 9 capítulos con el arco real de 3. No bloquea este veredicto (ya está señalado como pendiente en `walkthrough.md` desde el 20/08 y sin impacto práctico), pero si el relato se publica en `02_Finalizadas/`, valdría la pena una pasada de reconciliación formal del canon antes de archivarlo, por higiene documental.
