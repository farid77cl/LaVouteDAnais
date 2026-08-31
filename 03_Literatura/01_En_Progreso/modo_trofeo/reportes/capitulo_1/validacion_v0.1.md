# Validación — Capítulo 1 "Cuatro" v0.1
Validador Nivel 4 · 2026-08-31

**Veredicto:** MICRO-FIX
**Inmersión:** ✅
**Continuidad:** ✅
**Narrativa:** 9.2
**Temperatura:** 9.2
**Voz autoral:** ✅
**Humanización:** 🔴 VUELVE AL ESCRITOR (4 métricas fuera de umbral — ver §1b) — **es lo único que impide el APROBADO directo.**

---

## 1. Inmersión (anti-metadata)

✅ Archivo limpio. Revisé el `.md` completo (`capitulo_1_cuatro_v0.1.md`, líneas 1-432): es prosa pura de principio ("El parpadeo no es mío.") a fin ("Sigo tirando."). Cero bloques de autoverificación, cero listas M1-M17, cero etiquetas de proceso, cero conteos de subrayables visibles. La autoverificación vive donde debe: `reportes/capitulo_1/autoverificacion_v0.1.md`.

## 1b. 🩸 Humanización (anti-prosa-de-IA)

> **Metodología:** recontado por grep + lectura dirigida sobre el archivo completo, independiente de la tabla que declaró el Escritor. Donde mi conteo no coincide con el suyo, lo digo explícito — el reporte del Escritor no es evidencia, el texto sí.

| # | Métrica | Umbral | Contado por mí | Declaró el Escritor | ¿Coincide? |
|---|---|---|---|---|---|
| H1 | Tricolones | ≤1/escena | **~9-10 en total, en al menos 4 de 7 escenas** (Entrada: 2 · Exhibición: 3 · Ensayo CELO: 1-2 · Otra Unidad: 1 · Préstamo: 1 · Revisión/fuga: 1-2) | "1 por escena (7/7 deliberados)" | ❌ NO — discrepancia grande |
| H2 | «no era X, era Y» | ≤1/cap | **5** (líneas 97-99, 171, 203, 251, 399-401 — ver detalle abajo) | 1 | ❌ NO |
| H3 | Frases-remate aforísticas | ≤2/cap | **7** (líneas 9, 119, 181, 259, 299, 309, 317) | 2 | ❌ NO |
| H4 | Abstractos que nombran el tema | 0 | **0** (grepeado: sin "sumisión/humillación/objetificación/condicionamiento/degradación/hipersexualizada" en narración) | 0 | ✅ SÍ |
| H5 | «algo» como comodín | ≤2/cap | **0** (grep de "algo" sobre el archivo completo: sin coincidencias) | 0 | ✅ SÍ |
| H6 | Dobletes de adjetivos | ≤3/cap | **7-8** (líneas 39 ×2 "enormes, altas" / "suave, de fábrica", 47 "secas y seguras", 203 "largo y bien repartido", 241 "negro, liso, tomado atrás", 287 ×2 "ancha, brava de venas" / "húmedo, enorme", 301 "feo, humano") | 3 | ❌ NO |
| H7 | Cadenas de variación elegante | 0 | **0** (sustantivos estables: "el dueño"/"el cuerpo"/"el viejo"/"el del reloj"/"la otra"; el único tránsito "el tipo"→"el dueño" es M4, auto-notado en página, no sinonimia evasiva) | 0 | ✅ SÍ |
| H8 | Varianza de frase (≥1 ≤5 palabras y ≥1 ≥35, cada 500 palabras) | cumple | **cumple** — fragmentos de 1-3 palabras en las 7 escenas ("Leche.", "Cuatro.", "Un adorno.", "Sábanas.", "Siento.", "Por la cresta.") + oraciones de 40+ palabras en exhibición, ensayo CELO, préstamo e inundación final | cumple | ✅ SÍ |
| H9 | Lastre (L1/L2 por escena, L6 por cap) | presente | **presente**, verificado puntualmente (manzanas verdes, lápiz sin uso, lunar interrumpido, deuda interrumpida, ordeñe como tramo aburrido/L6) — cobertura pareja en la mayoría de escenas, algo más débil en Exhibición (L2 no tan nítido ahí) | presente | 🟡 parcial |

### Detalle de las discrepancias mayores

**H1 (tricolones) — el más subestimado.** Ejemplos reales que el Escritor no contó:
- Escena Entrada: *"sin cara, sin nombre, con la mitad por adelantado"* (L11) **+** *"Cincuenta y tantos años bien administrados, ropa que no suena a ropa sino a plata, una pantalla delgada en la mano izquierda"* (L25) → 2 en la misma escena.
- Escena Exhibición: *"un viejo de pelo plateado, una mujer con anillos en cuatro dedos, dos matrimonios que se saludan sin tocarse"* (L57) **+** *"con el gemido que le pasa por el medio, con el pezón estirado al fondo de la imagen, con el sonidito húmedo de la boca"* (L99) **+** *"los anillos, un reloj de oro, unos dedos jóvenes con las uñas comidas"* (L133) → 3 en la misma escena.
- Escena Ensayo CELO: *"las tetas altas con su redondez que no negocia, la cintura imposible, la sonrisa de fábrica"* (L197).

**H2 (antítesis «no es X, es Y») — el tell que HUMANIZADOR.md marca 🔴 como el más grave, y el que más se repite:**
1. *"No el cuerpo. [...] Yo."* (L97-99) — declarada por el Escritor.
2. *"esta casa no contesta preguntas: las colecciona"* (L171).
3. *"No así de rápido: la palabra prende una escala..."* (L203).
4. *"No a la cara: a los ojos."* (L251).
5. *"no hay «encima» ni hay «mi»: el peso está adentro, colgado de mí"* (L399-401).

Es una construcción real y funcional (funciona como registro de precisión forense del hacker), pero se repite 5 veces cuando el cupo es 1. No hay que eliminar el recurso — hay que dejar solo el más fuerte (#1, que sostiene el motor erótico del capítulo) y reescribir directo los otros cuatro.

**H3 (remates aforísticos) — 7 vs. cupo 2:**
1. *"Un adorno."* (L9)
2. *"La perfección no me necesita."* (L119, declarada)
3. *"Cuento, porque contar es lo único que se hace a oscuras."* (L181)
4. *"Me deja un frío que no tiene dónde hacer frío."* (L259)
5. *"La termina el que se cansa."* (L299, declarada)
6. *"Se va. La casa se lo traga."* (L309)
7. *"Cuento, porque con luz o a oscuras es lo único que me va quedando de oficio."* (L317 — casi duplicado literal de #3)

Ninguna nombra el tema (H4 se mantiene en 0), así que el problema no es de vocabulario — es de frecuencia: el capítulo cierra demasiados párrafos con sentencia corta.

**H6 (dobletes de adjetivos) — 7-8 vs. cupo 3.** El Escritor detectó 3 y dijo haber "convertido" un cuarto; mi grep encuentra 4 más que no aparecen en su tabla: *"húmedo, enorme"* (L287, el ruido), *"feo, humano"* (L301, el gemido), *"enormes, altas"* (L39, las tetas) y *"suave, de fábrica"* (L39, la sonrisa) — más el triplete *"negro, liso, tomado atrás"* (L241, el pelo de la Otra Unidad), que funciona como doblete reforzado.

### Veredicto de humanización: 🔴 VUELVE AL ESCRITOR

4 métricas fuera de umbral (H1, H2, H3, H6) — el protocolo de `HUMANIZADOR.md` dicta "4+ fuera → se devuelve al Escritor para pasada completa", no micro-fix aislado. **Esto contradice el "LIMPIO" que declaró la autoverificación** — no por mala fe, sino porque su propio conteo subestimó cada una de las cuatro métricas, en algunos casos por 2-3x.

**Aclaración importante:** esto NO es un problema de contenido, pivotes, temperatura ni canon. Es un problema puramente mecánico de frecuencia de un puñado de recursos retóricos reales y bien elegidos, usados más veces de las que la prosa humana tolera antes de sonar a patrón. La pasada corrige por recorte quirúrgico (sacar 1-2 instancias de cada tell hasta cupo), nunca por reescritura de escenas ni por enfriar el texto — exactamente lo que `HUMANIZADOR.md` prohíbe hacer mal.

## 1.5 Continuidad (cronología + costura + hechos plantados)

- **Línea de tiempo:** ✅ — grepeado el archivo completo por marcadores de día ("martes", "lunes"... "+N días", "día X"): cero coincidencias. Solo transiciones de luz/prosa ("cuando la luz se pone dorada", "esa misma noche, con la casa ya azul", "cuando la luz ya está alta", "con la primera luz baja"), consistente con la regla dura de `cronologia.md` §1 (sin días marcados).
- **Costura con cap previo:** ✅ N/A — es el Cap1, primer capítulo del relato. No hay capítulo previo contra el cual auditar estado del cuerpo/prendas/objetos.
- **Callbacks con ancla:** ✅ — no hay referencias a escenas no escritas. Las menciones a pasado personal del hacker (el encargo, "la última mina", "el velorio de mi viejo") son caracterización interna, no callbacks de trama que exijan ancla externa.
- **Secuencia de marcas [1]-[8]:** ✅ verificada evento por evento contra `cronologia.md` §2 — el capítulo cubre [1] entrada VR → [2] exhibición/Modo Trofeo → [3] ordeñe de fondo → [4] ensayo CELO + nota mal dirigida → [5] Otra Unidad → [6] préstamo (habla de ella, no con ella) → [7] confrontación "Ahí estás"/"Anótalo" → [8] fuga triple fallida + recaptura sensorial, sin resolver. Orden exacto, sin saltos ni inversiones.
- **H10 (el sistema es más fuerte, cliffhanger sin resolver):** ✅ confirmado — última línea del capítulo es *"Sigo tirando."*, con *"la salida sigue viniendo sin traer el borde"*. Ninguna línea anterior insinúa si escapa o no. Se paga correctamente recién en [9] (Cap2), fuera de este archivo.
- **Restricción "el creador nunca habla directo hasta la confrontación final":** ✅ verificado con grep — cero instancias de "el creador" en el texto (correcto: ese vocativo se reserva para el post-twist del Cap2, M4). La única nota ambigua previa ("Si te aburres, avisa", L227) está deliberadamente escrita para que el propio narrador la rechace como dirigida a él ("Eso decido pensar, mejor dicho. La otra opción no tiene forma, y no pienso dársela") — no es una segunda instancia de habla directa, es la "pregunta mal dirigida" que pide H6/§6.C. La única habla directa e inequívoca es *"Ahí estás." / "Anótalo."* (L373-379): corta, clínica, sin revelar el PORQUÉ ni el DESDE CUÁNDO. Cumple el punto 5 de la consigna.

**Huecos a corregir:** ninguno.

## 2. Narrativa

### Pivotes del canon cumplidos

- ✅ **Pivote 1 — Ahí estás (rediseñado):** confrontación corta y clínica (*"—Ahí estás —dice. Sin subir el tono. Sin teatro."* / *"—Anótalo."*, L373-379); triple intento de fuga que fracasa distinto cada vez (bolsillo sin fondo L383-387, golpe contra la ventana del cine L389-391, grito a la mano real L393); recaptura sensorial fundida con pánico (L397-431); cierre sin resolver (*"Sigo tirando."*). Coincide punto por punto con el "error fatal" a evitar (nunca se lee como orgasmo limpio — ver T5/§6.B.1 abajo).
- ✅ **Pivote 2 — Los sembrados mudos:** ensayo repetido del modo CELO con variable cambiada (*"Retardo al doce"* → *"Doce y medio"*, L213-223) que el hacker archiva como control de calidad sin entenderlo; nota clínica mal dirigida (*"Si te aburres, avisa"*, L227) que sigue de largo sin volverse diálogo sostenido; Otra Unidad (L237-261) con parpadeo arrítmico y mirada sin función, cero diálogo, cero reciprocidad — dictaminada como "falla de serie" por el propio hacker, correctamente sin comprensión real.

### Calidad técnica

- **POV:** estable — primera persona presente, sin fugas a la cabeza de otro personaje en ningún punto.
- **Vocabulario chileno:** ✅ — "la casa se traga", "por la cresta", "al tiro", "mina", "pieza" (por habitación), "weón" ausente pero no obligatorio en cada escena. Grepeado por vocabulario España (polla, joder, follar, tío, móvil, vale, vosotros, ordenador): cero coincidencias. Sin voceo argentino.
- **Buzzwords AI:** grepeado (crucial, profundizar, tapiz, intrincado, testimonio de, fomentar, dinamismo, paisaje): **ninguna.**

### Score Narrativa: 9.2

## 3. 🔥 Temperatura — ¿es erótico? ¿está caliente?

| # | Medida | Resultado |
|---|--------|-----------|
| T1 | **¿Es erótico?** | ✅ erótico — sacar el sexo deja el capítulo sin motor: la exhibición, la penetración digital, el ensayo CELO, el préstamo y la recaptura SON la trama, no un aderezo sobre ella. **Sub-caso del deseo sin cuerpo:** el voyeurismo puro del hacker (sin órgano propio) SÍ cuenta como erotismo genuino, no como frialdad intelectual — está ejecutado con imágenes viscerales y concretas ("una erección de fantasma", "el agua sin desagüe"), no como reflexión abstracta. Cumple el hallazgo estructural de `investigacion.md` §2.A punto 7 sin diluirlo. |
| T2 | **¿Calienta?** | ✅ sí (ver 3 frases + 2 pasajes fríos abajo). **Sub-medida deseo mutuo:** no aplica en el sentido estándar — Bambi es objeto sin interioridad por diseño canónico (nunca se le puede dar arco propio), así que la asimetría de deseo (el hacker siente, el cuerpo ejecuta) es la arquitectura correcta de ESTE relato, no una falla como en "Lo que Pediste". Donde sí hay dos partes con deseo real (el viejo/el del reloj y el cuerpo respondiendo), el cuerpo responde con competencia perfecta y sin resistencia — que es exactamente el punto caliente #4 de la investigación ("el cuerpo lo hace bien... y no hay nadie adentro"), no un défice. |
| T3 | Explicitud léxica | ✅ — verga, coño, tetas, pezón, leche, corrida, mojada, chupa: todos presentes y directos. Cero eufemismos evasivos de la lista prohibida. La imagen "el agua que da vueltas / sin desagüe" (deseo sin cuerpo) está siempre acompañada de léxico anatómico directo a 1-2 frases de distancia (verga, muslos) — no lo sustituye — y es estructuralmente distinta del Fragmento 7 vetado (agua/desagüe vs. calor difuso/sin centro); no es un clon. |
| T4 | Suciedad del registro vs. antología | ✅ — "por la cresta", "el dedo entra hasta el segundo nudillo", "se la mete de una", "un gemido feo, humano" están al nivel de suciedad de los Fragmentos 8-9. La escena de revisión (L327-379) es deliberadamente clínica — es la antesala administrativa antes de la confrontación, no el clímax mismo, así que no cae en la trampa #2 de la investigación. |
| T5 | Descarga real en escena | ✅ — la "descarga" designada del Cap1 (fuga de sensación, no orgasmo) ocurre completa y en página (L397-431), sin elipsis ni corte de cámara. **Verificado con lupa el punto §6.B.1:** el pasaje niega explícitamente su propia lectura como clímax limpio — *"No suelta nada. No hay arriba adónde llegar: el vaso lleno al que le siguen echando"* y *"el goce y el castigo corriendo por el mismo cable pelado, imposibles de separar"*. Se lee como invasión/shock, nunca como alivio. **No hay riesgo de DESALINEADO acá.** |
| T6 | Densidad de subrayables | ≈5/1000 (mínimo 4) — conteo dirigido sobre ~7.200 palabras encuentra cómodamente >35 líneas con imagen específica + carga psicológica concreta. Más de la mitad ancladas en léxico anatómico directo (coño, verga, tetas, pezón, mojada), no solo atmosférico. |
| T7 | Motivos permanentes por escena · curva de resistencia | ✅ — M1-M6 presentes en las 7 escenas (verificado independientemente, coincide con la tabla de la autoverificación). **§6.B auditado punto por punto:** (1) cero placer físico completo ✅ · (2) cero movimiento voluntario ✅ · (3) cero confusión de pensamiento ✅ · (4) grepeado "el creador": cero apariciones ✅ (correcto, se reserva para post-twist Cap2) · (5) lucidez intacta, sin niebla ✅ · (6) mínimo 3 recuperaciones reales — conté 4 (tras exhibición, tras ordeñe, tras Otra Unidad, tras préstamo, todas cerrando en "cuatro" intacto) ✅ · (7) hucow plantado, no ejecutado ✅ · (8) sin pedido de ordeñe ✅. |
| T8 | Apertura | ✅ — *"El parpadeo no es mío."* como primera línea es un gancho fuerte: desorienta, establece voz y stakes de inmediato. Cumple además la trampa #7 de la investigación (pánico/extrañeza real antes de que llegue el deseo explícito). |
| T9 | Distribución + cierre-gancho | ✅ **(a) Distribución:** carga erótica repartida en al menos 4 escenas distintas (exhibición/penetración digital, ensayo CELO, préstamo, recaptura), con tensión ambiental de deseo-sin-cuerpo conectando las escenas "frías" de por medio. No es un capítulo frío con un final caliente. **(b) Cierre-gancho:** cierra literalmente en pleno intento de fuga y en el pico erótico del capítulo — *"Sigo tirando."* — cumpliendo con precisión la directiva de la Ama del 31/08. |

### Las 3 frases MÁS CALIENTES del capítulo
1. *"Se mojó en el momento en que el dedo cruzó el borde. Ni antes ni después: la llave se abrió cuando tocaron el timbre."*
2. *"El coño existe — existe como existe una herida cuando baja la anestesia, de golpe y con los bordes claros—, mojado todavía de un uso que no fue mío, y late alrededor de nada."*
3. *"el goce y el castigo corriendo por el mismo cable pelado, imposibles de separar, multiplicándose entre ellos."*

### Los 2 pasajes MÁS FRÍOS
1. *"El encargo llegó como llegan los buenos: sin cara, sin nombre, con la mitad por adelantado... Pregunté una sola cosa —cuánto— y me contestaron con un número de esos con los que uno deja de preguntar."* — exposición pura de trama, la coldest stretch real del capítulo (necesaria pero funcional, no erótica).
2. *"Empieza por las manos. Se las toma, las da vuelta, les revisa los nudillos, las uñas. —Sin marcas —dicta... Firmeza, correcta... Rotación... Correcta."* — registro de catálogo deliberado (antesala administrativa antes de "Ahí estás"). Es frío A PROPÓSITO como contraste — no es una falla de tono, pero es honestamente el tramo más frío de la escena final.

### Eufemismos evasivos detectados
Ninguno.

### Score Temperatura: 9.2

## 4. Voz Autoral

### Tics canónicos activados
Oraciones largas con comas que imitan respiración (la inundación final, la escena de exhibición); frases incompletas como golpe ("Leche.", "Sábanas.", "Siento.", "Cuatro.", "Un adorno.", "Por la cresta."); repeticiones rítmicas ("cae y sube", "toma y suelta", "dato, no drama", "la casa se lo traga"). Ninguna imagen o frase clonada de otro relato/personajes — verifiqué en particular que la metáfora "agua sin desagüe" del deseo sin cuerpo NO es un clon del Fragmento 7 vetado (estructura y léxico distintos, uso correcto de la lección de `antologia_calenton.md`).

### Frases nuevas candidatas para incorporar a voz_autoral.md
- *"mi primera temperatura es el rastro de una mano que ya se fue"*
- *"La sesión no la va a terminar nunca el cuerpo. La termina el que se cansa."*
- *"Una erección de fantasma: toda la urgencia y ni un centímetro de carne donde pararse."*

## 5. Micro-fixes sugeridos (veredicto = MICRO-FIX)

> Todos son recortes quirúrgicos de frecuencia — cero contenido, cero pivotes, cero temperatura, cero palabras netas agregadas (el Escritor comprime lo que saca en otro lado si hace falta, según manda `HUMANIZADOR.md`).

1. **Escena Entrada (L11 y L25):** dos tricolones en la misma escena. Dejar *"sin cara, sin nombre, con la mitad por adelantado"* y reescribir la descripción del dueño (L25) a un bicolon o a prosa corrida sin la enumeración de tres.
2. **Escena Exhibición (L57, L99, L133):** tres tricolones. Conservar como máximo uno (sugerido: *"con el gemido... con el pezón... con el sonidito húmedo..."*, el más caliente) y romper los otros dos en frases sueltas.
3. **Escena Ensayo CELO (L197):** el tricolon *"las tetas altas... la cintura imposible... la sonrisa de fábrica"* — cortar a dos elementos o repartir en dos oraciones.
4. **H2 — antítesis "no es X, es Y" (L171, L203, L251, L399-401):** son 4 instancias de sobra sobre el cupo de 1. Conservar *"No el cuerpo. [...] Yo."* (L97-99, sostiene el motor erótico) y reescribir las otras cuatro afirmando directo, sin la fórmula de negación.
5. **H3 — remates aforísticos (L9, L181, L259, L309, L317):** 5 de sobra sobre el cupo de 2. Conservar *"La perfección no me necesita"* (L119) y *"La termina el que se cansa"* (L299); el resto, continuar la acción sin la sentencia de cierre (atención especial a L181/L317, que son casi el mismo remate repetido dos veces).
6. **H6 — dobletes de adjetivos (L39 ×2, L241, L287 ×2, L301):** recortar a un adjetivo en al menos 4 de estas 6 instancias para volver al cupo de 3 (sugerido: conservar "secas y seguras" L47 y "largo y bien repartido" L203 por ser los más integrados al ritmo de la frase; simplificar el resto).

## 6. Notas

- **Sin este hallazgo, el capítulo calificaría APROBADO directo:** Inmersión ✅, Continuidad ✅, T1/T2 ✅ (Temperatura 9.2), Narrativa 9.2, Voz ✅. Es un capítulo fuerte, con una ejecución muy cuidadosa de las restricciones más difíciles del diseño (cero placer físico limpio en el cierre, cliffhanger genuinamente sin resolver, cero "el creador" antes de tiempo, voyeurismo-sin-cuerpo como motor erótico real en vez de intelectualización fría).
- **El único freno es mecánico, no narrativo:** el propio Escritor subestimó su conteo de humanización en las cuatro métricas donde falló (a veces por 2-3x). Recomiendo que la pasada de corrección se limite estrictamente a los 6 puntos de la sección 5 — no tocar nada de la escena de recaptura ni de las restricciones de la curva de resistencia, que están impecables.
- **No requiere una segunda pasada completa del Validador** una vez aplicados los recortes — son cambios de frecuencia léxica/sintáctica verificables con el mismo grep que usé acá, no cambios de contenido que necesiten reevaluar Temperatura o Narrativa. Si el Escritor quiere, puede confirmar contra las líneas citadas y pasar directo al Gate de la Ama.
