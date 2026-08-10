# Validación — Capítulo 1 v0.1 «Las Manos de la Ama»
Validador Nivel 4 · 2026-08-10

**Veredicto:** APROBADO
**Inmersión:** ✅
**Continuidad:** ✅
**Narrativa:** 9.3
**Temperatura:** 8.7
**Voz autoral:** ✅

> Nota de proceso verificada: cero ocurrencias de "culete" en el archivo del capítulo (grep dedicado) — ya reemplazado por "culo" en todo el texto, tal como se reportó. No queda pendiente.

## 1. Inmersión (anti-metadata)

✅ Archivo 100% prosa. Se leyeron las 539 líneas completas: título, diálogo, narración y pensamientos en cursiva del sujeto — cero bloques de autoverificación, cero listas M1-M17, cero etiquetas "[BEAT ERÓTICO]", cero conteos de subrayables visibles. La metadata vive exclusivamente en `reportes/capitulo_1/autoverificacion_v0.1.md`, donde corresponde.

## 1b. 🩸 Humanización (anti-prosa-de-IA)

Conté yo mismo contra `HUMANIZADOR.md` (Grep dedicado + lectura completa), no acepté el conteo del Escritor sin verificar.

| # | Métrica | Umbral | Contado por mí | Declaró el Escritor | ¿Coincide? |
|---|---|---|---|---|---|
| H1 | Tricolones | ≤1/escena | 0 violaciones claras — los catálogos de estado (líneas ~333, ~505) son inventarios de 5-6 ítems, no tricolones de relleno, y sirven al motivo canónico de "revisión acumulada" | "sin violaciones evidentes" | ✅ |
| H2 | «no era X, era Y» | ≤1 | **1** — línea 443: *"No es suya. Es un arnés."* (grep confirmado, única instancia en todo el archivo) | 1 | ✅ Coincide |
| H3 | Frases-remate aforísticas | ≤2 | **4-5**, no 2-3: *"Está en el primer peldaño"* (L11, defendible — es imagen canónica del propio Pivote 5, no tell gratuito), *"Y va a estar tan equivocado como entonces"* (L125), *"Sirven para tocar. Para que las miren."* (L319), *"No dolía. Eso es lo que más lo asusta: que no dolía"* (L385), y el cierre del capítulo *"...como quien cierra una puerta que sabe, con toda certeza, que va a volver a abrir"* (L539) | "~2-3, zona límite" | ❌ NO coincide — mi conteo es más alto. El Escritor subestimó (probablemente no contó el remate de cierre del capítulo ni "Sirven para tocar..."). Sigue en el rango 1-3 fuera de umbral → no cambia el veredicto de humanización, pero corrijo el número. |
| H4 | Abstractos que nombran el tema | 0 | **0** — sin "la arquitectura de", "el mecanismo de" ni equivalentes | 0 | ✅ |
| H5 | «algo» comodín | ≤2 | **2** — L75 *"algo se le cae adentro"*, L209 *"Eso fue el final de algo"*. L113 (*"pide algo en un mesón"*) y L319 (*"abrocharse algo, cualquier cosa"*) son idiomáticos, correctamente excluidos | 2 | ✅ Coincide |
| H6 | Dobletes de adjetivos | ≤3 | ~1-2 (ej. "pasada corta y firme") | ~1-2 | ✅ |
| H7 | Cadenas de variación elegante | 0 | **0** — "el hombre"/"Ele"/"Anaïs" repetidos consistentemente en los 4 tramos | 0 | ✅ |
| H8 | Varianza de frase | cumple | Cumple — fragmentos de una palabra ("Cae.", "Clic.", "Lo encuentra.", "Grita.") intercalados con cláusulas largas encadenadas en cada tramo | cumple | ✅ |
| H9 | Lastre | presente | L1 (copa de Anaïs, L3→L357, sin más mención después), L2 (*"No puedo correrme... Pero esto..."*, L491, no se retoma), L6 (*"Pasa un rato. Bastante rato..."*, L373) — los tres presentes | presente | ✅ |

**Veredicto de humanización:** 🟡 **MICRO-FIX** (solo H3 fuera de umbral — 1 métrica sola nunca cruza a 🔴, que exige 4+ o H4/H7≠0). No bloquea APROBADO: es un ajuste de pulido, no un motivo de devolución.

**Citas de los peores tells (máx 3):**
1. *"Sirven para tocar. Para que las miren."* (L319) — remate aforístico de dos fragmentos, la variante más "IA" de los cinco porque generaliza sin anclar a nada nuevo. Se opera fusionándolo con la frase anterior o cortándolo.
2. *"...como quien cierra una puerta que sabe, con toda certeza, que va a volver a abrir"* (L539, cierre del capítulo) — el aforismo-metáfora de cierre es el tell más reconocible del género (final "profundo"). Funciona narrativamente como cliffhanger, pero el envoltorio es de manual. Sugerido: cortar en *"...sale de la habitación sin apurar el paso."* y dejar que el silencio cierre solo.
3. *"No dolía. Eso es lo que más lo asusta: que no dolía."* (L385) — roza también T5 (explicar la emoción después de mostrarla): ya se mostró el gemido y el "¿ves que no dolía?" de Ele: la glosa siguiente es redundante.

No amerita devolver el capítulo — son 3 cortes puntuales, aplicables por el Escritor sin re-tramo.

## 1.5 Continuidad (interna, tramo a tramo, contra `cronologia.md`)

- **Línea de tiempo:** ✅ — es una escena continua sin marcas de reloj ni día de semana, tal como exige la cronología ligera. Los avances de tiempo usan solo anclaje relativo interno (*"Un rato después"*, *"Pasa un rato. Bastante rato, en realidad"*, *"minutos después"*) — nunca reloj ni día.
- **Costura tramo a tramo (estado del cuerpo/vestuario, §4 cronología):** ✅ verificado en las 4 transiciones:
  - Cierre T1 (torso descubierto, sin tacones/cinturón) — coincide con el texto justo antes de *"Tetas, Ele. Tacones. Y el cinturón."*
  - Cierre T2 (breast plate + tacones + cinturón cerrado, pantalón y ropa interior fuera) — coincide con el texto justo antes de *"Ahora la cabeza."*
  - Cierre T3 (+ maquillaje + peluca + uñas + tanga sobre el cinturón) — coincide con el texto justo antes de *"Ahora vamos a ver qué más tienes ahí atrás."*
  - Cierre T4 (entrenado analmente, orgasmo consumado, cinturón nunca abierto, nada se retira) — coincide con el cierre del capítulo.
- **Callbacks con ancla (Hechos Plantados H1-H8):** ✅ los 8 verificados uno a uno contra el texto:
  - H1 (barba) plantada y pagada T1 (afeitado). ✅
  - H4 (cinturón cerrado con llave de Anaïs) pagado en T4 exactamente como describe la tabla (metal "se aprieta y se suelta", estallido real viene de atrás). ✅
  - H5 ("Yo fui como tú") plantada L101 T1, pagada L341 T3 (*"¿te acuerdi? Te lo dije. Y mira. Mírame."*). ✅ — sin invención de escena nueva.
  - H6 (mantras): confirmé que T3 solo pronuncia literalmente "no pienso"/"soy muñeca"/"soy de la Ama" (L247, L255, L265) y que "mi cosita no es mía" aparece recién en T4 (L469-473) junto con "me gusta por el culo" (L419) y "soy un agujero con tetas" (L479) — coincide exactamente con la corrección de continuidad anotada en `cronologia.md`.
  - H7 (strapon = arnés, nunca anatomía de Ele) pagado L441-443 con la línea explícita. ✅
  - H8 (escalada NO consumada) — ver §6 abajo.
  - No se encontró **ningún** callback sin ancla — no hay referencias a escenas no escritas.
- **Huecos a corregir:** ninguno.

## 2. Narrativa

### Pivotes del canon cumplidos

- ✅ Pivote 1 (El filo): *"con la espuma todavía tibia y el filo real a centímetros de la yugular, sostenido por una mano que no es la suya, el hombre traga saliva"* (L39) — indefensión física real antes de nada erótico, ejecutado como acción sensorial, nunca como manual.
- ✅ Pivote 2 (El primer peso): frío→pesado→"vivo" del breast plate (L139-159) + clic de cierre del cinturón narrado como sonido, no solo objeto (L203-209).
- ✅ Pivote 3 (La voz que se presta): mantras escalados con dolor real de pronunciación (*"—No... —el hombre traga saliva otra vez, y la palabra le sale rota"*, L247) + espejo doble (*"Somos dos [...] Dos muñecas de la Ama"*, L341).
- ✅ Pivote 4 (El descubrimiento atrás): progresión real dedo→dos dedos→strapon sin saltos, con reinicio de tensión en cada escalón, descarga explícita en escena sin elipsis (L497-513).
- ✅ Pivote 5 (cliffhanger): *"Quiero tetas de verdad"* (L521-525) nace de él, sin orden previa; Anaïs sella y corta (*"Anótalo [...] Todavía no"*, L537) — la escalada NO se materializa en la página.

### Calidad técnica

- **POV:** estable con licencia deliberada de narrador omnisciente acotado — el texto revela en 2-3 momentos la sensación de Ele que "el hombre... no lo sabe" (L425, L503). No es un desliz de foco: es la ejecución del Motivo Permanente #2 (el calentón de Ele como motor legible), coherente con el diseño triangular del canon. No lo cuento como falla de POV.
- **Vocabulario chileno:** ✅ — "¿Cachai?", "¿sabís?", "¿te acuerdi?", "ricura", "po" ausente pero no forzado; cero léxico España (sin "vale", "tío", "coche", "polla", "follar").
- **Buzzwords AI detectadas:** ninguna (sin "crucial", "tapiz", "intrincado", "profundizar").
- **Voseo argentino:** cero — "sabís"/"cachai" son voseo verbal chileno canónico, no el pronombre "vos"; tú se usa siempre.
- **Arquetipo del sujeto:** sin nombre, sin trabajo, sin biografía extensa en las 539 líneas — el Motivo Permanente #6 se sostiene sin fisuras.

### Score Narrativa: 9.3

## 3. 🔥 Temperatura — ¿es erótico? ¿está caliente?

| # | Medida | Resultado |
|---|--------|-----------|
| T1 | **¿Es erótico?** (¿sobrevive el cap si le sacás el sexo?) | ✅ erótico — el capítulo ES el proceso de feminización + entrenamiento sexual de principio a fin; sacarle el contenido sexual no deja nada (no hay subtrama, ni otro conflicto, ni otra escena) |
| T2 | **¿Calienta?** (juicio directo) | ✅ sí |
| T3 | Explicitud léxica (¿nombra o esquiva?) | ⚠️ mayormente ✅, con una falla puntual real: **"virilidad" usado 3 veces (L181, L201, L499) para el sexo del hombre, incluida la línea EXACTA del clímax (L499)**, en vez del "verga" que el vocabulario autorizado habilita. Cero otros eufemismos (sin "su sexo", "su intimidad", "aquello", "zona íntima", "miembro"). "Culo" aparece 15 veces, "coño" (Ele) 4 veces, mantras 100% crudos. Es un hallazgo puntual, no sistemático — pero pega justo en el momento de mayor carga. |
| T4 | Suciedad del registro vs `antologia_calenton.md` | ✅ — dirty talk directo (*"Vente, ricura... vente por el culo... la Ama quiere verlo"*, L495) comparable en crudeza a Fragmentos 6/9 de la antología; sin clonar frases (verificado: "mientras más lo trataba como cosa" NO aparece; "calor difuso/sin centro" del Fragmento 7 NO aparece — grep dedicado, cero coincidencias) |
| T5 | Descarga real en escena (no elipsis) | ✅ — orgasmo completo narrado en escena, sin corte de cámara, con las tres reacciones simultáneas exigidas por la Curva de Resistencia (grita, llora, ríe) |
| T6 | Densidad de subrayables | Estimado ≥6/1000 (cap ~9.000 palabras — sin herramienta de conteo automático disponible, estimación manual por densidad de línea, igual que reportó el Escritor). Cumple ampliamente el mínimo de 4/1000. Anclaje anatómico: más de la mitad de los subrayables citados abajo tienen léxico anatómico/acción sexual directa, no solo imagen atmosférica. |
| T7 | Motivos permanentes **por escena** · curva de resistencia | ✅ — los 6 motivos permanentes verificados presentes en los 4 tramos (manos de Ele ejecutando sin pausa, calentón de Ele en cada tramo — L99, L273-277, L425, L441-445, L503 —, autoridad de Anaïs saturando vía "Bien"/observación, anatomía femenina de Ele sin excepción, presión acumulada sin picos que bajan, arquetipo sin biografía). Curva de resistencia con **7 reinicios** documentados con cita (llegada, afeitado, cinturón, mantras, primer dedo, segundo dedo — reinicio extra no exigido pero bien ejecutado —, antes del strapon), orgasmo no resuelto limpio |
| T8 | Apertura (primeras 500 palabras enganchan) | ✅ — triangulación de autoridad establecida en la primera línea de diálogo (*"Hazlo, Ele. Me gustas así, extra morbosa y caliente"*), navaja contra la garganta y primer traga-saliva real ya ocurridos dentro de las primeras ~500 palabras |

### Las 3 frases MÁS CALIENTES del capítulo
1. *"No es suya. Es un arnés. Y bajo el arnés, apretado contra el látex, el coño de Ele está tan mojado que la humedad ya le llegó hasta la parte interna de los muslos, un calor propio que no tiene nada que ver con tener nada nuevo entre las piernas y todo que ver con lo que acaba de hacerle a él con los dedos."* (L443) — paga en un solo golpe el invariante anatómico Y el motor erótico de Ele.
2. *"—¡Ahí! —Ele no grita, pero la palabra le sale con una urgencia distinta a todo lo anterior—. Ahí está, ricura. Eso. [...] Es un placer que llega de un lugar que él jamás catalogó como suyo para sentir placer."* (L399-403) — la traición del cuerpo en su forma más literal, exactamente el punto caliente #5 de `investigacion.md`.
3. *"Grita. Llora al mismo tiempo [...] y en medio del llanto se ríe [...] El horror de lo que acaba de pasar y el alivio de haberlo sentido conviven en el mismo segundo, sin pelearse, sin que uno gane."* (L501) — rendición con horror consciente, sin paz limpia, tal como exige §6 de la investigación.

### Los 2 pasajes MÁS FRÍOS (a reescribir, opcional — no bloquean)
1. *"Ahora los tacones. [...] Desliza el pump negro. El pie entra apretado, el arco forzado hacia arriba..."* (L163-173) — el paso más mecánico del capítulo; comparado con el resto, se siente como acción-trámite más que escena erótica. No es tono clínico (Ele sigue en registro), pero es la zona de menor carga sensorial de los 4 tramos.
2. *"Le acomoda una redecilla fina primero [...] baja la peluca sobre su cabeza con las dos manos"* (L303-315) — el bloque de la peluca prioriza la sensación de picazón/calor sobre el morbo; funciona como dato real (bien investigado, coincide con el Banco Sensorial), pero es más incómodo que caliente en sí mismo.

### Eufemismos evasivos detectados
"Virilidad" — 3 instancias (L181, L201, L499). Ninguna otra.

### Score Temperatura: 8.7
> T1 y T2 en ✅ — no hay bloqueo de gate. El descuento viene de T3 (euforismo puntual en el clímax) y los dos pasajes fríos citados, dentro de una ejecución por lo demás muy sólida de T5/T6/T7/T8.

## 4. Voz Autoral

### Tics canónicos activados
- *"Bien."* como sello de autoridad de Anaïs (reutiliza el RITMO/CADENCIA de Valeria en `voz_autoral.md`, no una imagen específica — recanonizado explícitamente para Anaïs dentro de este relato, uso legítimo per la distinción de tics-de-ritmo vs. imágenes-clonadas).
- Frases incompletas como golpe rítmico: *"Cae."*, *"Clic."*, *"Lo encuentra."*, *"El hombre se viene."* — mismo patrón documentado en `voz_autoral.md`.
- Registro Ele (§III `identidad_ele.md`) sostenido incluso en el clímax: *"Vente, ricura... vente por el culo... la Ama quiere verlo... 🫦💋🔥"* (L495) — el "like"/diminutivos/emoticones no se apagan en la escena más explícita, cumple el requisito especial de este capítulo.
- Lente 1 (cuerpo antes que mente): patrón "*Esto no soy yo*" repetido y erosionado progresivamente — mecanismo transversal de La Voûte, aplicado con propiedad.

### Frases nuevas candidatas para incorporar a `voz_autoral.md` / `antologia_calenton.md`
- *"No es suya. Es un arnés."* — resuelve en una línea de prosa (no de explicación) la restricción de canon anatómico; reutilizable como plantilla de aclaración narrada.
- *"Anótalo. Va a querer más de lo que acaba de pedir. Todavía no."* — cierre de autoridad que sella sin consumar; útil para cualquier cliffhanger futuro del universo.
- *"Somos dos. Dos muñecas de la Ama."* — mecanismo de doble espejo/reconocimiento, reutilizable en cualquier relato de transformación con ejecutora-testigo.

**Check:** ✅ — la voz suena al canon acumulado y al registro específico de Ele §III; ningún tic detectado es en realidad una imagen clonada de otro relato/pareja (verificado explícitamente contra el Fragmento 7 de la antología — sin coincidencia).

## 5. Micro-fixes sugeridos (no bloquean APROBADO — el Escritor puede aplicarlos directo, sin nueva ronda de validación)

1. **L181, L201, L499:** reemplazar "virilidad" por "verga" (o dejar una de las tres como "virilidad" si se quiere variación léxica, pero **no la de L499** — el clímax necesita la palabra cruda, no la abstracta).
2. **L319:** cortar o fusionar *"Sirven para tocar. Para que las miren."* con la frase anterior para bajar el conteo de H3.
3. **L385:** cortar *"Eso es lo que más lo asusta: que no dolía."* — ya está mostrado, la glosa sobra (H3 + roza T5).
4. **L539 (cierre del capítulo):** opcional — cortar en *"...sale de la habitación sin apurar el paso"* y eliminar el símil final de la puerta, si se quiere bajar H3 a 2/2 exacto. No es obligatorio: el cliffhanger funciona igual sin el aforismo.

## 6. Notas

- **Restricción anatómica de Ele (corrección Ama 10/08/2026):** verificada línea por línea en las 10 apariciones del cuerpo de Ele a lo largo del capítulo (L7, L67, L99, L143-151, L171, L273-277, L425, L441-445, L467, L503) — 100% femenina, coño nunca pene/verga propios, incluida la escena del strapon con la línea explícita de aclaración. **Cero violaciones.** Es el hallazgo de máxima prioridad que se pidió verificar sin excepción, y pasa limpio.
- **Cierre cliffhanger (corrección Ama 10/08/2026):** verificado — la escalada queda como petición verbal (L521-525), reportada por Ele (L529), sellada por Anaïs sin materializarse (L537-539). Cero consumación en página.
- **Origen AMAB de Ele:** usado dentro del capítulo (*"Yo fui como tú"*, L101, L341) exclusivamente como canon interno de este relato — no se filtró a ninguna descripción que lo trate como hecho válido fuera de `manos_de_la_ama` (no aplica a este documento verificarlo contra `identidad_ele.md`, pero se confirma que el capítulo no hace ninguna declaración que pretenda universalizarlo).
- Sin `investigacion.md` faltante — el proyecto sí lo tiene, y se usó como vara de medición completa (§2, §2b, §5, §6, §8) tal como exige el protocolo.
- Palabras: sin herramienta de conteo automático disponible en este entorno tampoco para el Validador — se acepta la estimación del Escritor (~9.000 palabras) como orden de magnitud razonable dado el barrido línea a línea.
