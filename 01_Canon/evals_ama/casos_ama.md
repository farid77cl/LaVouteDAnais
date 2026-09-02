# 📋 LA CARPETA DE LORETO — los casos de la Ama, set de pruebas del Escritor y del Validador

> **Loreto es la secretaria de control de La Voûte** (bautizada por la Ama el 02/09/2026: *"me siento incómoda que un niño lea relatos eróticos, que sean secretarias de control o algo así"*). Guarda en esta carpeta **cada nota** que la Ama escribió alguna vez, y cuenta con lápiz rojo (`medir_capitulo.py`) antes de que un capítulo llegue a su escritorio. No escribe. No aprueba. Cuenta y señala.
> **Dueño único** de las correcciones de la Ama convertidas en **casos de prueba**. Documento **permanente**: se edita, nunca se duplica ni se resume en otro lado. Los agentes apuntan aquí.
> **Nace el 02/09/2026** de su diagnóstico literal: *"estoy agotada de los constantes errores en la escritura de los relatos… debo leer 5, 6 veces el mismo relato y eso al final mata mi propia temperatura, si lo logras al primero o segundo está bien, pero hay relatos que llegaron a la 12 versión… he ajustado el flujo, skill etc por lo menos 3 o 4 veces y seguimos igual, lo que más me preocupa es que no logras dar con la temperatura y te pones muy robótica con tus descripciones."*
> **Fuente:** las 44 notas de Gate (`nota_*.md`, `notas_vivas_*.md`, `notas.md`) de 10 relatos, 05/2026 → 09/2026, leídas completas, más sus órdenes vivas registradas en `walkthrough.md`. **Cada caso cita sus palabras literales** (ortografía de su app conservada cuando importa el tono).
> **Meta medible de Loreto:** que un capítulo llegue a su Gate en **≤ 2 lecturas suyas**. Hoy el récord es 14 versiones (Café Cap 1) y 13 (trance Office Siren).

---

## 0 · EL CASO CERO — «estamos escribiendo un relato erótico. eso debe calentar al lector»

Es la frase que la Ama ha tenido que repetir en **cinco relatos distintos**, y la repitió otra vez el 02/09/2026 mientras se construía este archivo: *"hay otra cosa que estoy constantemente repitiendo y que se debe a lo mismo, estamos escribiendo un relato erotico!!!"* — *"eso debe calentar al lector."*

| Fecha | Relato | Sus palabras |
|---|---|---|
| 02/09/2026 | (en vivo) | *"estamos escribiendo un relato erotico!!! … eso debe calentar al lector"* |
| 05/08/2026 | Café con Piernas · Cap 1 v0.4 | *"300 líneas y cero erotismo… esto es la Antártica, temperatura -40… segunda regla, es un relato de control mental!!!"* |
| 05/08/2026 | Café con Piernas · Cap 1 v0.3 | *"le falta sensualidad, erotismo al relato erótico!!!"* |
| 13/08/2026 | Manos de la Ama · Cap 1 v0.1 | *"terminó de afeitar y nada erótico. recuerda que esto es un relato erótico!!! reescribe desde cero"* |
| 23/07/2026 | Lo que Pediste · Cap 1 v0.2 | *"le falta sensualidad, es un relato erótico y estás evitando decir verga"* |
| 06/2026 | La Piel que Diseñé · Cap 1 v0.1 | *"me falta más temperatura, hay errores en el texto, no sé está fome"* |
| 27/08/2026 | Café con Piernas · Cap 3 v0.3 | *"Quiero que deje a todos calientes incluso al lector"* |
| 14/08/2026 | Café con Piernas · Cap 2 v0.4 | *"quiero calentarme junto con ella"* |

**Lo que esto significa como caso de prueba:** la Regla de Oro 13 (*marco erótico en todo briefing*) existe desde el 22/07/2026 y ella siguió teniendo que decirlo. **Una regla escrita no es una regla cumplida.** Por eso este archivo no agrega reglas: agrega **casos** — y por eso `medir_capitulo.py` cuenta, sin cortesía, lo que una máquina puede contar (§D).

La prueba que todo párrafo tiene que pasar antes de existir: **¿esto calienta al lector, o solo informa?** Si informa, o se corta, o se reescribe desde adentro del cuerpo excitado.

---

## Cómo se usa

| Quién | Cuándo | Qué hace con esto |
|---|---|---|
| **`escritor-nivel4`** | Prioridad 0.5, ANTES de escribir cualquier tramo | Lee el Caso Cero + §A completo. Escribe con los casos en la cabeza como **anti-antología** (lo que la Ama ya rechazó, con sus palabras). Al cerrar el tramo N pasa la **checklist §C** sobre el archivo completo. |
| **Orquestador** | Entre el tramo N y el Validador (Fase 2.5) | Corre `python 99_Sistema/scripts/literatura/medir_capitulo.py <cap> --contra <caps previos> --out reportes/capitulo_N/medicion_v0.X.md`. Si hay umbral duro → vuelve al Escritor **sin gastar Validador**, con el reporte y el ID del caso que reincide. |
| **`validador`** | Fase 3 | Lee `medicion_v0.X.md` como input. §A es su **lista de caza** en T2/T3/T8/T9 y en la humanización: cada hallazgo cita el **ID del caso** que reincide (ej. *"C1-02: bloque de trámite sin función erótica, líneas 143-160"*). |
| **Captura Post-Nota** | Cada nota de rechazo aplicada | Su regla general ya va a `voz_autoral.md` / `canon_relato.md §4b` (Regla de Oro 10). **Además**, la nota entra aquí como caso nuevo, con ID, en su categoría. Un patrón nuevo abre categoría nueva. |
| **Cierre de relato** | Captura Doble | Un caso que no reincide en **3 relatos seguidos** se marca 🟢 en su tabla. No se borra: la Ama no debería tener que repetirlo una cuarta vez. |

---

## Frecuencia medida (44 notas · ~150 correcciones individuales)

| # | Categoría | Correcciones | ¿La máquina lo mide? |
|---|---|---|---|
| **C4** | Frase rara · no se entiende · error de persona/POV | ~25 | parcial (M7 clichés, H2) — el resto es oído humano |
| **C9** | Calentura constante ausente · motivos permanentes · voz interna | ~18 | aprox. (M10 deciles) — el Validador lo mide por escena (T7) |
| **C1** | **Trámite: descriptiva sin función erótica** | ~17 | **sí — M4/M5 (duro)** |
| **C5** | La técnica sensorial: el lector al lado | ~16 | su ausencia (M4); la receta es humana |
| **C14** | La dominante describe en vez de tentar | ~11 | no |
| **C6** | Sexo apurado o demasiado limpio | ~10 | parcial (M3 léxico, M9 cierre) |
| **C2** | Pudor del narrador: esquiva la palabra / reporta el estado | ~9 | **sí — M3 eufemismos** |
| **C7** | Rendición demasiado rápida | ~9 | no (T7 curva) |
| **C10** | Continuidad: callback fantasma · «¿cuándo pasó esto?» | ~9 | no (gate Continuidad) |
| **C8** | Personaje que no cambió · no suena bimbo | ~8 | no |
| **C12** | Apertura sin gancho · cierre sin gancho | ~7 | aprox. (M9) |
| **C3** | Repetición (interna, entre capítulos, entre versiones) | ~6 | **sí — M1/M2 (duro)** |
| **C13** | Registro y dialecto (neutro/chileno, voseo, güey, «doctor») | ~6 | parcial (M3 España) |
| **C11** | Contraste antes/después que falta | ~5 | no |
| **C15** | Etiqueta en vez de ejecución («degradación» escrita) | ~3 | **sí — M6 (duro)** |

**Lectura:** Temperatura (C1+C5+C6+C9+C12+C14) ≈ **79 correcciones, la mitad**. Prosa robótica (C2+C3+C4+C15) ≈ **43, un cuarto**. Es exactamente lo que ella nombró el 02/09: *"no logras dar con la temperatura y te pones muy robótica"*. Lo demás (arco, personaje, continuidad, registro) es el cuarto restante.

---

## §A — LOS CASOS, POR CATEGORÍA

> Formato: **ID** · relato · capítulo · versión · **sus palabras** · qué había en el texto (cuando la nota lo cita) · regla operativa al pie de cada tabla.

### C1 · «Te pones descriptiva y no calientas a nadie» — trámite sin función erótica

| ID | Dónde | Sus palabras | Qué había |
|---|---|---|---|
| C1-01 | Café · Cap 4 v0.2 · 01/09 | *"este es el mismo problema de siempre, te pones descriptiva y no calientas a nadie"* | Nombrado por ella como **patrón**, no como hallazgo aislado |
| C1-02 | Café · Cap 4 v0.2 | *"el salto de tiempo tenía que servir para comprimir la operación, y en vez de eso se alargó… sigue, sigue, la enfermera, el anestesista — ¿qué tiene de erótico eso?"* | Flashback quirúrgico: 183 palabras seguidas con `anestesia · clínica · enfermera · formulario` y ningún cuerpo (medido 02/09) |
| C1-03 | Café · Cap 4 v0.2 | *"Dormía sentada… ¿quién se calienta o se masturba con eso?!"* | Recuperación post-op |
| C1-04 | Café · Cap 4 v0.2 | *"Bolsa de arvejas?!?!?!?! horror!!!"* | La bolsa de arvejas congeladas como hielo |
| C1-05 | Café · Cap 4 v0.2 | *"Está viendo televisión!!!!!! ¿Qué onda?!"* | Programa de tele en la recuperación |
| C1-06 | Café · Cap 4 v0.2 | *"No me interesa la recuperación de la operación!"* | El bloque entero, no una frase |
| C1-07 | Café · Cap 4 v0.2 | *"La escena de la clínica / el doctor de las tetas se fue en lo descriptivo — quedó muy plano/informativo, falta calor"* | |
| C1-08 | Café · Cap 1 v0.3 · 05/08 | *"comprime la parte previa el raconto. está bien que la prota tenga motivación, pero está demasiado largo… más de la mitad del relato y nada erótico"* | Raconto de ~2.000 palabras |
| C1-09 | Café · Cap 1 v0.4 · 05/08 | *"300 líneas y cero erotismo… esto es la Antártica, temperatura -40"* | Reescritura total → v0.5 |
| C1-10 | Café · Cap 1 v0.7 | *"el relato en general está muy realista, no tiene ese sentido de relato erótico de control mental más fantasioso"* | El realismo documental mata el género |
| C1-11 | Café · Cap 3 v0.5 | *"comprime la parte de las tetas"* | Decisión + cirugía |
| C1-12 | Café · Cap 3 · dictado 31/08 | *"Escena 8 (decisión de la operación): que sea corta, no vale la pena extenderla. Escena 9 (cirugía + recuperación): lo mismo — corta"* | |
| C1-13 | Manos de la Ama · Cap 1 v0.1 | *"la descripción del cuerpo de ele hazla de a poco, no lo hagas en un solo párrafo"* | **Inventario en bloque = robótica** |
| C1-14 | Manos de la Ama · Cap 1 v0.1 | *"terminó de afeitar y nada erótico"* | Una escena entera de procedimiento |
| C1-15 | La Piel · Cap 3 v0.1 | *"la parte de bárbara es muy larga, y poco sensual"* | |
| C1-16 | La Piel · Cap 3 v0.1 | *"voy leyendo hasta esa parte y le falta tensión sexual, **está bien escrito, pero me falta ese edge sexual**, de lo que va a pasar, de lo que podría pasar"* | **El diagnóstico exacto de "robótica": correcto y sin filo** |
| C1-17 | La Piel · Cap 1 v0.1 | *"me falta más temperatura… no sé está fome"* | |

**Regla operativa C1 — la prueba del trasplante.** Si un párrafo cabría igual en una novela que no es erótica, no existe: se corta o se reescribe **desde adentro del cuerpo excitado**. Toda escena de trámite (cirugía, recuperación, traslado, gestión, tele, comida) es un **puente de ≤ 2 párrafos**, y hasta el puente lleva el cuerpo. El inventario (cuerpo, ropa, lugar) **se reparte en gestos** a lo largo de la escena, nunca en un bloque. «Bien escrito» sin edge es falla, no mérito. **Medidor:** M4 (corridas de narración sin cuerpo) + M5 (vocabulario de trámite dentro de ellas) — falla dura.

### C2 · Pudor del narrador — esquiva la palabra, o reporta el estado en vez de ejecutarlo

| ID | Dónde | Sus palabras | Qué había |
|---|---|---|---|
| C2-01 | Lo que Pediste · Cap 1 v0.2 | *"es un relato erótico y estás evitando decir verga o por lo menos con gonzalo. el lenguaje en general está como muy limpio debería ser más sucio, sobre todo cuando está chupando"* | Ginny decía la palabra; el narrador dentro de Gonzalo no |
| C2-02 | Lo que Pediste · Cap 1 v0.5 | *"acá más explícito, que se le puso dura"* | «la parte de adelante del pantalón, **que ya había opinado**» — chiste de narrador tapando la imagen |
| C2-03 | Lo que Pediste · Cap 1 v0.5 | *"¿que no se le duerma qué?"* | «—Y de paso que no se me duerma a las once» — sin sujeto |
| C2-04 | Lo que Pediste · Cap 1 v0.5 | *"asco a qué, si aún no sabe el efecto del deseo"* | «una forma que se estaba terminando de dibujar sola, con peso, con temperatura, con un largo determinado» — nunca dice *verga* |
| C2-05 | Lo que Pediste · Cap 1 v0.4 | *"¿cómo es que cosa?"* | «Yo te cuento cómo es.» |
| C2-06 | Lo que Pediste · Cap 1 v0.2 | *"acá y en los párrafos que vienen que tiene el deseo de verga, sé más explícita, dale imágenes mentales, los labios etc, acá se quiebra Gonzalo, hazlo bien"* | |
| C2-07 | Café · Cap 1 v0.8 | *"«.. qué caliente me puse ..» cambia esta frase por otra, que sea un jiji"* | El monólogo **reportaba** el estado. Se **ejecuta** (firma sonora / cuerpo) |
| C2-08 | Lo que Pediste · Cap 1 v0.6 | *"que sea explícito que Ginny se pone contenta porque a Gonzalo se le pone dura la verga"* | |
| C2-09 | Café · Cap 2 v0.4 | *"cambia Soto por javierita, más meloso"* | El apellido seco donde iba la caricia |

**Regla operativa C2.** Ni pronombre, ni perífrasis, ni ingenio de narrador donde va la palabra: **verga, coño, culo, tetas, dura, mojada**. Vale para el narrador exactamente igual que para el personaje, y sobre todo en plena resistencia (el cuerpo se nombra aunque la mente lo niegue). Un estado interno **nunca se reporta** («qué caliente me puse»): se ejecuta en la firma sonora o en la respuesta anatómica. **Medidor:** M3 (léxico explícito por 1.000 + eufemismos evasivos).

### C3 · Repetición — «se repite y se repite»

| ID | Dónde | Sus palabras | Qué había |
|---|---|---|---|
| C3-01 | Café · Cap 1 v0.3 | *"siento que hay cosas que se repiten y se repiten"* | |
| C3-02 | Café · Cap 3 v0.7 · 01/09 (en vivo) | Sintió repetición en las **primeras 50 líneas**, antes de que nadie la midiera | «con dos uñas fucsias» ×2 en 16 líneas · «el aliento le rozó… antes que la voz» ×2 con dos clientes distintos · «las manos que ya no le respondían» ×3. **El Validador no lo cazó** |
| C3-03 | Café · Cap 4 v0.2 | *"humaniza este párrafo, se repite muy pronto eso de los 2 dedos"* | |
| C3-04 | Café · Cap 4 v0.2 · 01/09 | *"Escena de Don Manuel (Cap 4) muy idéntica a algo del Cap 3"* | **Medido 02/09: la v0.3 "corregida" conserva un clon verbatim de 9 palabras** («hombre que hubiera preferido no tener que caminar justo») y un párrafo con **40 % de palabras compartidas** con el Cap 3. El rework retocó, no reescribió |
| C3-05 | Lo que Pediste · Cap 1 v0.5 (hallazgo del Validador) | *"El bloque más largo de tentación pura de Ginny —el de la puerta del baño— es texto de la v0.4 con retoques cosméticos. Ese es exactamente el material que la Ama rechazó tres veces."* | **La reescritura que recicla el pasaje rechazado** — causa directa de las 12 versiones |
| C3-06 | Café · Cap 3 v0.6 (auditoría propia) | — | Tic «misma calma/facilidad con que antes…» ×9 · símil abogada ×11 |

**Regla operativa C3.** Un rework **reescribe desde cero** el pasaje rechazado; retocarlo garantiza la vuelta N+1. Una frase-imagen que gustó se usa **una vez** por capítulo — la segunda ya es tic. Antes de cerrar, el propio Escritor busca sus n-gramas. **Medidor:** M1 (interna, ≥9 palabras = duro) + M2 (contra capítulos previos, ≥8 palabras = duro; párrafos con Jaccard ≥ 0.30 = aviso).

### C4 · Frase rara · no se entiende · error de persona — «hay mucha cosa escrita rara»

| ID | Dónde | Sus palabras | Qué había |
|---|---|---|---|
| C4-01 | Café · Cap 1 v0.3 | *"porque los pies que???"* | «Se apoyó ahí un segundo, con las caderas, porque los pies.» — elipsis "literaria" |
| C4-02 | Lo que Pediste · Cap 1 v0.4 | *"no entiendo el conteo de pasos???"* | «midiendo la distancia en pasos. Once, doce. Después se sorprendió aliviado de que fueran doce.» |
| C4-03 | Lo que Pediste · Cap 1 v0.4 | *"revisa la prosa, hay mucha cosa escrita rara"* | |
| C4-04 | La Muñeca del Gerente · Cap 1 v0.3 | *"está raro el funcionamiento de la app, la redacción está rara también… la primera parte de la morbosidad hay que cambiarla, no se entiende"* | |
| C4-05 | De Esteban a Secretaria · Cap 2 v0.6 | *"ella se había cocinado sola?? qué es eso qué significa???"* | Metáfora sin puente |
| C4-06 | De Esteban a Secretaria · Cap 2 v0.6 | *"«esto no se desarma», cámbialo por no hay vuelta atrás"* | |
| C4-07 | De Esteban a Secretaria · Cap 2 v0.8 | *"«la mojadura», cámbialo por la humedad en la entrepierna"* | **Palabra inventada/rara** |
| C4-08 | De Esteban a Secretaria · Cap 2 v0.8 | *"«bajito rinde más», esa frase no me gusta, pon algo como bajito es más de mujer"* | Ingenio donde iba la feminización |
| C4-09 | La Piel · Cap 2 «El postre» | *"«Con dueñez» cámbialo por Con propiedad"* | **Palabra inventada** |
| C4-10 | La Piel · Cap 1 v0.3 | *"«Las elegí lindas. No las elegí fuertes. ¿Para qué iba a quererte…» → No las elegiste fuertes. ¿Para qué ibas a quererme…"* | **Persona invertida en body swap** |
| C4-11 | La Piel · Cap 1 v0.3 | *"«verme dueña de mí desde afuera» → dueño"* | Género del narrador en body swap |
| C4-12 | La Piel · Cap 1 v0.3 | *"«te los hice grandes a propósito. Me lo pediste tú», debería ser me los hiciste grandes"* | |
| C4-13 | De Esteban a Secretaria · Cap 2 v0.9 | *"«¿No te quedó rica?» déjalo como ¿No me quedó rica?"* | |
| C4-14 | Café · Cap 4 v0.2 | *"dice algo que le gustaba a él, no será ella?"* | Pronombre equivocado |
| C4-15 | Café · Cap 3 v0.6 | *"«Se lo dijo entera», humaniza esa frase, suena mal. «Pero gracias por la corbata» también suena raro. «Si le das de comer entero se aburre» suena mal"* | Tres frases "ingeniosas" en un capítulo |
| C4-16 | Café · Cap 3 v0.5 | *"«—¿Este es el que hay que tomarse antes de salir?» esto no se entiende, cámbialo por otra cotidianidad del local"* | |
| C4-17 | Café · Cap 3 v0.2 | *"toda esa parte Yasna debe ser más clara a lo que se refiere, no se entiende"* | Revelación demasiado elíptica |
| C4-18 | Café · Cap 3 v0.8 | *"«Usted ya no tiene oficina conmigo, abogado» → Usted ya no es mi jefe, abogado. «Dígamelo bien dicho» → Dígamelo bien, sea hombre y dígamelo con todas sus letras"* | **Su oído: directo, sin ingenio, más dominante** |
| C4-19 | La Piel · Cap 3 v0.2 | *"«Así me la chupabas tú a mí cuando querías que te diera permiso de algo. ¿Te acordái? Igualita. Solo que tú nunca pusiste esta cara» está rara esa frase"* | |
| C4-20 | De Esteban a Secretaria · Cap 2 v0.10 | *"«y odiado no saber leer» quita eso. «Me terminó adentro» cámbialo por terminó adentro"* | |
| C4-21 | De Esteban a Secretaria · Cap 2 v0.8 | *"la última parte está caliente pero le falta revisión"* | |
| C4-22 | La Piel · Cap 1 v0.3 | *"cómo se vistió???"* | Salto que deja al lector sin la imagen |
| C4-23 | Café · Cap 3 v0.2 | *"insinúa el salto de tiempo, unas 3 semanas"* | El lector no sabía cuánto pasó |
| C4-24 | Café · Cap 2 v0.5 · 19/08 | *"sé que di el okey a esto, pero no tiene sentido, quítalo"* | Párrafo del narrador racionalizando el vaso («nada de lo que hizo esa noche era normal…») |
| C4-25 | La Piel · Cap 1 v0.1 | *"hay errores en el texto"* | |

**Regla operativa C4 — la prueba de la lectura en voz alta.** La frase "ingeniosa" del narrador (elipsis, chiste, palabra inventada, símil que hay que descifrar, remate críptico) es **la marca robótica número uno por volumen**. Si al leerla como la Ama hay que releer, se cae: se dice derecho. En body swap y feminización, **cada pronombre y cada género de adjetivo se verifica contra quién habla y en qué cuerpo** — el error de persona es el más frecuente de todos los errores. Un salto de tiempo o de vestuario se **muestra**, no se asume. **Medidor:** solo lo aproxima (M7 clichés, H2, H6); el resto es oído — por eso el Escritor relee en voz alta y el Validador cita línea.

### C5 · La técnica sensorial — el lector a un centímetro

| ID | Dónde | Sus palabras | Qué había |
|---|---|---|---|
| C5-01 | Café · Cap 3 v0.6 · 28/08 | *"cuando cupcake calienta los clientes por ejemplo estoy cerca de Don Arturo… los labios cerca de él, hablar más despacio, el olor al perfume… que debería calentar el lector, que **debería poder sentirlo ahí cerca al lado tuyo** con la descripción y te deja prendido y caliente"* | **LA RECETA, en sus palabras** |
| C5-02 | Café · Cap 3 · 31/08 (en vivo → `canon_relato.md` §3) | Cupcake *"insípida"*: acercamiento lento · susurro al oído · dejar oler el perfume · morderse el labio · exhibir culo/tetas con el movimiento · cerrar distancia hasta dejar las tetas a un centímetro de la boca | Tres capítulos aprobados sin la técnica escrita en canon |
| C5-03 | Café · Cap 2 v0.4 | *"sube la sensualidad de la primera masturbación de Javiera, quiero calentarme junto con ella, que me dé vergüenza, asco y excitación, que los recuerdos del cliente del privado, de la barra del café sean más intensos"* | |
| C5-04 | Café · Cap 4 v0.2 | *"las escenas de masturbación necesitan más sensorial — más ideas dándole vueltas en la cabeza que la calienten a ella… le gusta el poder y manipular por dinero, eso es lo que tiene que estar en su cabeza"* | Sensación física sin el motor psicológico del relato |
| C5-05 | Café · Cap 1 v0.7 | *"cuando entra javiera quiero que describas a las chicas, que sean 3, su cuerpo su actitud y como interactúan con los clientes, da una mejor primera imagen del lugar"* | |
| C5-06 | Café · Cap 1 v0.8 | *"cuando Yasna la viste, incluye los tacones, maquillaje, peinado y algún perfume"* | |
| C5-07 | Café · Cap 2 v0.4 | *"debes agregar maquillaje más llamativo… cuando se viste falta la descripción de la falda"* | |
| C5-08 | Lo que Pediste · Cap 1 v0.1 | *"descripción de Ginny desde los tacones, piernas etc. dale piel aceitosa sensual, bronceada, con algo de glitter. Ginny es Bimbo, es sexo, describe el outfit también"* | |
| C5-09 | Manos de la Ama · Cap 1 v0.1 | *"sube la sensualidad del afeitado, ele roza la piel del hombre. las tetas en la cara. mientras ele afeita debe ir reprogramando la mente"* | |
| C5-10 | Manos de la Ama · Cap 1 v0.1 | *"Anais se debe fumar lentamente ese cigarro"* | **Lentitud** como técnica |
| C5-11 | Manos de la Ama · Cap 1 v0.1 | *"los lectores no conocen a ele, debes presentarla… describe físicamente también a anais"* | |
| C5-12 | Trance Office Siren · v0.13 | *"debe sentirse como un trance hipnótico real. hazlo más pesado, más hipnótico, usa técnicas reales… se debe sentir que miss doll le da órdenes al lector, respira, tócate, imagina"* | 13 versiones |
| C5-13 | La Piel · Cap 3 v0.1 | *"cuando se viste en el camarín, que todo sea dorado y que sean botas sobre la rodilla plateadas"* | |
| C5-14 | De Esteban a Secretaria · Cap 2 v0.8 | *"que no solo toque su coño con tape, también sus pequeñas tetas"* | |
| C5-15 | Café · Cap 3 · dictado 31/08 | *"la regla del pulgar es tonta. Cambiar por algo más práctico: una técnica real para calentar al cliente y que le dé más plata"* | **Truco inventado ✗ · técnica real ✓** |
| C5-16 | Café · Cap 1 v0.9 | *"cuando Javiera pide el café, que la garzona coquetee extra descarada con ella"* | |

**Regla operativa C5.** El lector está **dentro de la escena, a un centímetro**: lentitud · distancia que se cierra · olor · susurro · piel que roza piel · el cuerpo exhibido **en movimiento**. El vestuario se describe **sobre el cuerpo** y con la voz activa de quien lo mira o lo pone. La cabeza del personaje trae **el motor del relato** (poder, plata, humillación, la amenaza), no solo sensación. La técnica es **real** (la que un cuerpo usa de verdad para calentar a otro), nunca un truco inventado. **Medidor:** mide su ausencia (M4), no su presencia — la receta la juzga el Validador citando las 3 frases más calientes.

### C6 · Sexo apurado o demasiado limpio

| ID | Dónde | Sus palabras |
|---|---|---|
| C6-01 | Café · Cap 3 v0.6 | *"el sexo le falta suciedad con Felipe le falta subir un grado de calentura unos dos grados de calentura"* |
| C6-02 | Café · Cap 3 v0.6 | *"es muy rápido la escena de sexo"* |
| C6-03 | Café · Cap 1 v0.8 | *"la invitación al privado sí va si hace el tease al hombre y este saca su verga y ella queda a punto de lamer ahí se arrepiente, esa parte debe ser muy sexual y caliente, ella se degrada y humilla por unos billetes"* |
| C6-04 | Café · Cap 2 v0.4 | *"sé más explícita cuando don Arturo usa a Javiera, más gráfica y sexual"* |
| C6-05 | Café · Cap 3 v0.2 | *"le falta más sexo, todo más caliente… definitivamente le falta sexo al capítulo, mucho"* |
| C6-06 | Café · Cap 3 v0.5 | *"el sexo con Felipe, mucho más caliente"* |
| C6-07 | De Esteban a Secretaria · Cap 2 v0.8 | *"dale más tensión erótica cuando recién le meten la verga a Estefanía, es el acto final de dejar su masculinidad… cada embestida de Gabriel va sacando lo que queda de Esteban"* |
| C6-08 | De Esteban a Secretaria · Cap 2 v0.8 | *"sube un poco más la temperatura de la última cogida de Gabriel a Estefanía, es el clímax final que venimos construyendo con todo el relato"* |
| C6-09 | La Muñeca del Gerente · Cap 1 v0.3 | *"el trato de cristóbal con Fernanda debe ser mucho más humillante"* |
| C6-10 | Café · Cap 3 · 31/08 | *"las escenas sexuales se apuran/resuelven rápido cuando el objetivo es poner al lector en la posición del cliente"* |

**Regla operativa C6.** El pico es **la sección más larga y más sucia** del capítulo (ya está escrito en `escritor-nivel4.md` como «Peak Rush prohibido» — y siguió fallando). El clímax final lleva **el eje psicológico del relato entero** en cada embestida (lo que se pierde, lo que se rompe, lo que se acepta). **Medidor:** M3 (léxico) + M9 (cierre) — necesarios, no suficientes.

### C7 · Rendición demasiado rápida — «no rendirse tan pronto»

| ID | Dónde | Sus palabras |
|---|---|---|
| C7-01 | La Piel · Cap 1 v0.2 | *"Matías parece muy decidido, debe ir descubriendo todo lento… cómo que Daniela salta de inmediato… debe haber resistencia y no rendirse tan pronto"* |
| C7-02 | La Piel · Cap 1 v0.2 | *"que Dani tenga tiempo de pensar y de asustarse antes que llegue Daniela"* |
| C7-03 | La Muñeca del Gerente · Cap 1 v0.1 | *"Kitty primero debe ser un pensamiento intensivo dentro de la cabeza de cristóbal. Cristóbal se da cuenta de lo que hace, debe haber resistencia"* |
| C7-04 | Lo que Pediste · Cap 1 v0.4 | *"Gonzalo no pide verga"* — el sumiso **cede**, no pide |
| C7-05 | Café · Cap 1 v0.8 | *"el camino de la prota debe ser de degradación lenta, sensual erótica y muy sexista, ella se va convirtiendo en una especie de muñeca"* |
| C7-06 | Café · Cap 2 v0.4 | *"en algún momento Javiera le pide a don Arturo que la llame cupcake. al momento de que don Arturo usa a cupcake ésta se termina de romper definitivamente"* — el quiebre tiene **un beat exacto, ganado** |
| C7-07 | La Piel · Cap 2 | *"el vestirse así, vestido corto, tanga y tacones aún debe ser extraño durante la semana"* |
| C7-08 | Lo que Pediste · Cap 1 v0.4 | *"el deseo de coger mucho debe ser medio en broma medio en serio, no está convencido y lo dice casi como broma"* |
| C7-09 | Café · Cap 1 v0.7 | *"cuando la prota sale a atender, debe comportarse bimbo, **leve**"* — gradiente |

**Regla operativa C7.** La curva de resistencia (`investigacion.md` §6, Regla de Oro 15) no es un número: es la sensación de que **cada cesión costó**. La mente niega mientras el cuerpo ya cedió (el léxico del cuerpo nunca se apaga por la curva — ver C2). **Medidor:** no mide. Validador T7.

### C8 · Personaje que no cambió lo suficiente · no suena bimbo

| ID | Dónde | Sus palabras |
|---|---|---|
| C8-01 | Café · Cap 1 v0.1 | *"hay que bimboficar a la amiga, cambios mentales y físicos más extremos, además su habla más formal, se supone que está programada como trad wife, su habla debe ser más pulcra"* |
| C8-02 | Café · Cap 1 v0.3 | *"la amiga cambió pero no lo suficiente en cuanto actitud, personalidad y modo de hablar"* |
| C8-03 | Café · Cap 1 v0.7 | *"las chicas del lugar hablan más alegre más chispeante más bimbo… la amiga debe sonar a Bimbo trad-trophy wife"* |
| C8-04 | Lo que Pediste · Cap 1 v0.3 | *"cuando se materializa Ginny no suena a chica fresa, aumenta el tono fresa"* |
| C8-05 | Lo que Pediste · Cap 1 v0.5 | *"Ginny más sexual. Vocabulario de Ginny más bimbo. Ginny NO pierde la inocencia — pero sí es sexual, y debe tentar"* |
| C8-06 | De Esteban a Secretaria · Cap 2 v0.6 | *"mejora la presentación de Camila… que tenga personalidad burbujeante tipo Bimbo, pero gótica, todo el diálogo de Camila hay que hacerlo de nuevo"* |
| C8-07 | Café · Cap 3 v0.5 | *"cupcake no tiene envidia de camila, le gusta su nueva vida y poder usar su nuevo poder"* |
| C8-08 | Café · Cap 3 v0.2 | *"cupcake debe actuar más sexual, sin inhibición, ella sabe que está en control y disfruta demasiado eso, saber que ella es la que calienta y provoca deseo"* |

**Regla operativa C8.** La voz del personaje transformado es **otra voz** — léxico, ritmo, muletillas, lo que le importa — no la misma cabeza con adjetivos nuevos (auto-memoria `feedback_voz_bimbo_hueca_tomi`). El canon fija una frase literal por personaje; si el diálogo no suena a esa frase, se rehace entero.

### C9 · Calentura constante ausente — motivos permanentes · voz interna · estado del cuerpo

| ID | Dónde | Sus palabras |
|---|---|---|
| C9-01 | De Esteban a Secretaria · Cap 2 v0.6 | *"hay que hacer hincapié de la excitación constante de Estefanía y que no para y que solo aumenta"* |
| C9-02 | De Esteban a Secretaria · Cap 2 v0.6 | *"recuerda que es importante mantener ese estado de calentura y nublamiento mental"* |
| C9-03 | De Esteban a Secretaria · Cap 2 v0.6 | *"la voz interna en la cabeza de Estefanía, debe ser la de Valeria diciéndole cosas de mujer, debe estar presente en todo el relato"* |
| C9-04 | De Esteban a Secretaria · Cap 2 v0.6 | *"desde el inicio, debe haber un recordatorio constante de que Estefanía no es mujer, es un hombre"* |
| C9-05 | De Esteban a Secretaria · Cap 2 v0.6 | *"debe tener cosas sexuales entremedio, que exciten a Estefanía y al lector, quizás se calienta al ver a Gabriel o cuando Valentina le aplica la crema"* — **distribución**, no un solo pico |
| C9-06 | De Esteban a Secretaria · Cap 2 v0.9 | *"quiero saber lo que piensa Estefanía cuando se la están follando, sentir cómo se quiebra, se borra su masculinidad"* |
| C9-07 | La Piel · Cap 2 | *"cada vez que se viste, es importante mencionar siempre las tangas minúsculas, cómo se le ajusta en el culo, en el coño, la textura y diseño… y el asunto de los tacones de stripper"* |
| C9-08 | La Piel · Cap 2 | *"sin gasa, los pezones se le marcan bajo la tela, eso debe ser **siempre y en todo momento**"* |
| C9-09 | La Piel · Cap 2 | *"la amenaza de verga debe perseguir a Dani todo el cap 2 y 3. Dani debe… andar constantemente excitada y caliente"* |
| C9-10 | Café · Cap 1 v0.7 | *"la calentura de la prota debe ir en aumento desde el momento que bebe el líquido"* |
| C9-11 | Café · Cap 1 v0.9 | *"la degradación es el motor de la excitación, Javiera es consciente de que se está degradando, no lo puede evitar, y eso es la excitación. eso es su resistencia"* |
| C9-12 | Lo que Pediste · Cap 1 v0.2 | *"me falta más de Gonzalo mientras Ginny lo tienta"* |
| C9-13 | Lo que Pediste · Cap 1 v0.3 | *"aún me falta más de Gonzalo, qué es lo que le pasa, empieza a pensar en vergas??? la huele, le da asco?"* |
| C9-14 | El Podcast · Cap 2 v0.1 | *"cuando se pone la tanga se excita, pero la verga no responde, de ahí en adelante la verga se mantiene flácida y pequeña"* — **estado del cuerpo permanente** |
| C9-15 | El Podcast · Cap 2 v0.1 | *"cuando están viendo el partido y Rodrigo estira el brazo, agrega el deseo de servirle"* |
| C9-16 | Manos de la Ama · Cap 1 v0.1 | *"mejora los pensamientos del hombre"* |
| C9-17 | La Piel · Cap 1 v0.2 | *"la calentura acumulada en Dani no le permite pensar bien, empieza lentamente a actuar como bimbo"* |
| C9-18 | La Piel · Cap 3 v0.1 | *"me falta ese edge sexual, de lo que va a pasar, de lo que podría pasar, me entiendes?"* — **la anticipación como estado** |

**Regla operativa C9.** El estado (excitación, amenaza, voz interna, prenda que aprieta, pezón marcado, verga que no responde) es **continuo**: está en cada escena, incluidas las de trámite, y **solo sube**. Un motivo permanente cumplido una vez y dado por hecho es falla (Regla de Oro 14). La escena de sexo lleva la cabeza del sumiso **dentro**, no solo el cuerpo. **Medidor:** M10 (deciles) lo aproxima; T7 lo mide por escena.

### C10 · Continuidad — callback fantasma · «¿cuándo pasó esto?»

| ID | Dónde | Sus palabras | Qué había |
|---|---|---|---|
| C10-01 | De Esteban a Secretaria · Cap 2 v0.9 | *"Te lo prometí… cuándo lo prometió?… de nuevo cuando se lo prometió???"* | Promesa nunca escrita |
| C10-02 | De Esteban a Secretaria · Cap 2 v0.10 | *"«Te lo dije en la cocina, ¿te acuerdas?»… cuándo pasó esto?"* | **El Escritor inventó el ancla para tapar la queja anterior** — origen del Blindaje de Continuidad |
| C10-03 | De Esteban a Secretaria · Cap 2 v0.8 | *"«la verga que… el viernes había estado a un centímetro de su boca pintada» eso nunca pasó, no está en el texto"* | |
| C10-04 | De Esteban a Secretaria · Cap 2 v0.8 | *"en la parte donde se descubre todo hay muchas incoherencias, por qué no se tocó esa parte en la última revisión, todo el texto debe ser coherente"* | Edit local sin check global |
| C10-05 | Café · Cap 2 v0.4 | *"«Nos mira como a la que él vio ayer inclinada sobre la mesa» cuándo pasó esto???"* | |
| C10-06 | La Piel · Cap 3 v0.1 | *"«Daniela me dijo que estabas oxidada» cambia por Matías me dijo"* | Nombre según el cuerpo |
| C10-07 | La App · Cap 1 v0.3 | *"«empapaba el calzón», cambia calzón por bóxer"* | Todavía es hombre |
| C10-08 | Lo que Pediste · Cap 1 v0.5 | *"asco a qué, si aún no sabe el efecto del deseo"* | Causalidad rota |
| C10-09 | La Muñeca del Gerente · Cap 1 v0.1 | *"porque Francisca decide darle nombre de mujer?"* | Motivación sin plantar |

**Regla operativa C10.** Ya es la Ley de Continuidad + `cronologia.md` (Regla de Oro 11). Lo que estos casos agregan: **la corrección de un error de continuidad nunca se hace inventando un ancla nueva** (C10-02) — se planta en su escena de origen o se saca el callback. **Medidor:** no mide. Gate Continuidad del Validador.

### C11 · Contraste antes/después que falta

| ID | Dónde | Sus palabras |
|---|---|---|
| C11-01 | Café · Cap 3 v0.2 | *"al principio me falta el contraste de Javiera con cupcake. El pelo platinado le caía en ondas pesadas sobre los hombros aceitado contra el pelo de antes y etc"* |
| C11-02 | Café · Cap 3 v0.2 | *"le falta más contraste entre la nueva vida de cupcake y javiera"* |
| C11-03 | La Piel · Cap 1 v0.2 | *"que sienta el cambio y el contraste del cuerpo"* |
| C11-04 | De Esteban a Secretaria · Cap 2 v0.6 | *"siempre ese contraste, ella ve a Gabriel le atrae, pero debe haber ese juego con que Estefanía es hombre"* |
| C11-05 | De Esteban a Secretaria · Cap 2 v0.6 | *"haz hincapié en los cambios, por ejemplo las uñas y el café"* |

**Regla operativa C11.** La transformación se ve **contra lo que había**: cada cambio nuevo se escribe al lado de su versión anterior (el pelo de antes, la mano de antes, el hombre que todavía es). Sin el "antes" en la misma frase, el "después" no calienta.

### C12 · Apertura sin gancho · cierre sin gancho

| ID | Dónde | Sus palabras |
|---|---|---|
| C12-01 | Café · Cap 1 v0.7 | *"este capítulo debe terminar con algo sexual, cosa que den ganas de leer el próximo, con ese final lo dejo hasta acá y no leo más"* |
| C12-02 | Café · Cap 3 · dictado 31/08 | *"el cierre actual (la sonrisa tranquila, 'no había vuelta atrás y no le dio miedo') no engancha, hay que rediseñarlo"* |
| C12-03 | La Muñeca del Gerente · Cap 1 v0.3 | *"está poco atractivo la primera parte, no me dan deseos de seguir"* |
| C12-04 | Café · Cap 3 v0.2 | *"no me gusta lo de la cámara, hay que arreglar el final"* |
| C12-05 | La Piel · Cap 1 v0.2 | *"el cliffhanger final es si acepta o no el contrato, si va a seguir viviendo como mujer, si se va a quebrar o no"* |
| C12-06 | La Piel · Cap 2 | *"que quede de rodillas a la altura de la verga de Daniela, cerca, que la huela, que la imagine… que quede a punto, necesito que sea un pequeño cliffhanger"* |
| C12-07 | De Esteban a Secretaria · Cap 2 v0.6 | *"mejora el inicio, está como poco claro"* |

**Regla operativa C12.** T8 (las primeras 500 palabras enganchan) + T9 (el capítulo cierra en su beat más caliente, diseñado por el Compositor). Un cierre reflexivo pudiendo cerrar caliente es falla. **Medidor:** M9 (apertura/cierre) como aviso.

### C13 · Registro y dialecto

| ID | Dónde | Sus palabras |
|---|---|---|
| C13-01 | Café · Cap 1 v0.1 | *"definitivamente quita el español chileno del relato. lo usaremos cuando yo diga"* |
| C13-02 | Lo que Pediste · Cap 1 v0.2 | *"ginny habla en español neutro, todo el relato en español neutro"* |
| C13-03 | Lo que Pediste · Cap 1 v0.3 | *"elimina güey"* |
| C13-04 | Manos de la Ama · Cap 1 v0.1 | *"«—¿Cachai? —dice Anaïs»… anais jamás dirá cachai?!"* |
| C13-05 | La Piel · Cap 2 | *"«¿Viste? No te morís» cámbialo por ¿Viste? No pasó nada"* — **voseo argentino, prohibido** |
| C13-06 | Café · Cap 3 v0.5 | *"cuando habla con don Arturo le dice doctor, elimina eso"* |

**Regla operativa C13.** El registro lo fija el `canon_relato.md` de cada relato (neutro vs. chileno — *"lo usaremos cuando yo diga"*); cada personaje tiene léxico fijo (Anaïs jamás dice *cachai*); **nunca voseo**, nunca mexicanismos. **Medidor:** M3 solo caza léxico de España.

### C14 · La dominante describe en vez de tentar — «como lector no me está pasando nada»

| ID | Dónde | Sus palabras |
|---|---|---|
| C14-01 | Lo que Pediste · Cap 1 v0.5 | *"Te vuelvo a repetir: como lector no me está pasando nada con la tentación de Ginny"* — **tercera vez** |
| C14-02 | Lo que Pediste · Cap 1 v0.1 | *"que el deseo pase, Ginny se explica después de que el deseo ya está hecho"* |
| C14-03 | Lo que Pediste · Cap 1 v0.3 · 23/07 | *"Ginny solo describe, no tienta"* — con APROBADO del Validador (Narr 9.3 · Temp 9.2) |
| C14-04 | Café · Cap 3 v0.2 | *"cupcake debe tener caliente a don Arturo, tocarlo, insinuarse, coquetear, manipularlo. él quiere volver a repetir la experiencia de la oficina"* |
| C14-05 | Café · Cap 3 v0.3 | *"cupcake más manipuladora con don Manuel, que lo deje duro. lo mismo con Ignacio, en esos minutos lo deja caliente, le pide más tiempo, cupcake se niega, lo deja caliente"* |
| C14-06 | Café · Cap 3 v0.3 | *"definitivamente cupcake debe dejar caliente a todo el mundo, lector incluido"* |
| C14-07 | Café · Cap 2 v0.4 | *"Javiera debe provocar a don Arturo, cuando entra por segunda vez a la sala de reuniones, ella ve los billetes y le hace alguna insinuación que da pie a que don Arturo la use"* |
| C14-08 | Manos de la Ama · Cap 1 v0.1 | *"ele roza la piel del hombre. las tetas en la cara. mientras ele afeita debe ir reprogramando la mente"* |
| C14-09 | Café · Cap 1 v0.9 | *"que la garzona coquetee extra descarada con ella"* |
| C14-10 | Lo que Pediste · Cap 1 v0.5 | *"Hagamos que la tentación de Ginny sea mayor, que sea ella misma que usando su magia empieza poco a poco a mostrar una verga… Hace mejor la tentación"* |
| C14-11 | Lo que Pediste · Cap 1 v0.5 (hallazgo del Validador) | *"la sintaxis de Ginny se le desarma cuando tiene cuerpo que enseñar, y se le vuelve a armar cuando solo le queda la voz"* — **sin cuerpo en cuadro, la dominante se vuelve narradora** |

**Regla operativa C14.** La dominante **actúa sobre el cuerpo del otro antes de explicar nada**; su propio deseo está en escena (se pone contenta de la erección que provoca, C2-08); tienta con cuerpo, olor y distancia, no con parlamento. Ya está en `escritor-nivel4.md` («fuego sexual activo, no asistente técnica») — y siguió fallando con Validador APROBADO. El Validador cita **qué hace** la dominante en las 3 frases más calientes; si solo habla, T2 ❌.

### C15 · Etiqueta en vez de ejecución

| ID | Dónde | Sus palabras | Qué había |
|---|---|---|---|
| C15-01 | Café · Cap 1 v0.13 | *"evita usar la palabra degradación y similares, también por ahí leí hiper sexualizada evitarla y sus variantes"* | Cuatro versiones después de pedir *"más degradación autoconsciente"* (v0.9), el texto había escrito **la palabra** |
| C15-02 | Café · Cap 2 v0.5 · 19/08 | *"no tiene sentido, quítalo"* | El narrador **explicando el mecanismo** del vaso |
| C15-03 | `HUMANIZADOR.md` T4 · 03/08 | *"el relato no nombra su propio mecanismo"* | |

**Regla operativa C15.** H4 = 0. La escena degrada, humilla, somete; la palabra que lo clasifica es el andamio asomándose. **Medidor:** M6, falla dura.

---

## §0 — PROCESO: lo que no es prosa pero fabrica las 12 versiones

| ID | Fecha | Sus palabras | Qué se desprende |
|---|---|---|---|
| P-01 | 02/09/2026 | *"no he leido el cap 4 lo dejo claro"* | Un Gate inferido del silencio publicó un capítulo que no había leído. → **Regla de Oro 8c**: el Gate es un archivo o una frase suya que nombra ese capítulo; nunca se infiere |
| P-02 | 31/08/2026 | *"si yo doy un ok a las 12:07, luego leo y encuentro cosas que cambiar a las 12:08 se cambian!!! es mi decisión editorial!!!"* | Un Gate no es candado |
| P-03 | 19/08/2026 | *"sé que di el okey a esto, pero no tiene sentido, quítalo. mejor vuelve a la v0.5 y aplica mis cambios originales, a la v0.5 le faltaba poco para quedar bien"* | La reescritura no pedida (14.661 palabras tiradas) |
| P-04 | 28/07/2026 | *"solo anota"* | Notas sin ejecutar hasta que ella diga |
| P-05 | 30/08/2026 (Lo que Pediste) | — | Pendientes de v0.4 que no llegaron a v0.5: **cada pendiente perdido entre versiones es una lectura más de ella** |
| P-06 | 02/09/2026 | *"debo leer 5, 6 veces el mismo relato y eso al final mata mi propia temperatura, si lo logras al primero o segundo está bien, pero hay relatos que llegaron a la 12 versión"* | **La meta de Loreto: ≤ 2 lecturas por capítulo** |

---

## §C — CHECKLIST DE CIERRE DEL ESCRITOR (antes de escribir la autoverificación)

Se contesta **sobre el archivo completo**, leyendo como la Ama, no como el que lo escribió:

1. **C0** ¿Cada escena calienta al lector, o alguna solo informa? → la que informa se corta o se reescribe desde el cuerpo.
2. **C1** ¿Hay algún párrafo que cabría igual en una novela no erótica? ¿Alguna escena de trámite pasa de 2 párrafos? ¿Algún inventario (cuerpo/ropa/lugar) va en bloque?
3. **C2** ¿Dónde el narrador rodeó la palabra? ¿Dónde el monólogo **reportó** un estado en vez de ejecutarlo?
4. **C3** ¿Qué frase-imagen usé dos veces? ¿Qué pasaje de la versión anterior **retoqué** en vez de reescribir?
5. **C4** Leído en voz alta: ¿qué frase obliga a releer? ¿Qué palabra me inventé? En body swap: ¿cada pronombre y cada género van con el cuerpo que habla?
6. **C5** En cada acercamiento: ¿hay lentitud, distancia que se cierra, olor, susurro, piel? ¿El lector está a un centímetro o mirando desde la puerta?
7. **C6** ¿El pico es la sección más larga y más sucia? ¿El clímax lleva el eje psicológico del relato?
8. **C7** ¿Cada cesión costó, o el personaje "saltó de inmediato"?
9. **C8** ¿El personaje transformado suena a **otra** voz, o a la misma cabeza con adjetivos?
10. **C9** ¿El estado permanente (excitación, amenaza, voz interna, prenda) está en **cada** escena y solo sube?
11. **C11** ¿Cada cambio se escribe al lado de su "antes"?
12. **C12** ¿Las primeras 500 palabras dan ganas de seguir? ¿El cierre es el beat más caliente?

---

## §D — Qué mide la máquina y qué no

`99_Sistema/scripts/literatura/medir_capitulo.py` corre en la **Fase 2.5** (Orquestador, entre el tramo N y el Validador). Mide sin cortesía lo que una máquina puede contar; **no mide si calienta** — un 🟢 mecánico es condición necesaria, nunca suficiente.

| Medida | Caso que ataca | Duro / aviso |
|---|---|---|
| M4 corridas de narración sin cuerpo · M5 trámite adentro | C1 | 🔴 duro si hay trámite o ≥300 palabras; 🟡 aviso desde 120 |
| M3 léxico explícito por 1.000 · eufemismos · España | C2 · C13 | 🔴 España · 🟡 eufemismos |
| M1 repetición interna · M2 contra capítulos previos | C3 | 🔴 ≥9 palabras internas / ≥8 entre capítulos · 🟡 párrafos J≥0.30 |
| M6 etiquetas fuera de diálogo | C15 | 🔴 |
| M7 tics H1/H2/H3/H5/H6 + clichés · M8 varianza | robótica | 🟡 (aprox.; el Validador afina) |
| M9 apertura/cierre · M10 deciles | C9 · C12 | 🟡 |

**Calibración del 02/09/2026 sobre «Café con Piernas»** (`--extra billete,luca,propina,plata,fajo`):

| Versión | Veredicto de la Ama | Medidor |
|---|---|---|
| Cap 4 **v0.2** | rechazada (*"te pones descriptiva y no calientas a nadie"*) | 🔴 **3 tramos de trámite** — la clínica (`anestesia · clínica · enfermera · formulario`, 183 palabras), la recuperación (`arvejas · faja · hielo · pastillas`, 136) y la búsqueda de clínicas (127) · **10 frases de ≥9 palabras repetidas verbatim** dentro del capítulo (una de 16) · 21 clones ≥8 palabras contra el Cap 3 |
| Cap 4 **v0.3** | rework "corregido" (no leído por ella) | 🔴 la clínica y la recuperación **sí desaparecieron** · queda 1 tramo (buscando clínicas) · **19 clones contra el Cap 3 intactos** — Don Manuel: «el paso corto de un hombre que hubiera preferido no tener que caminar justo en ese momento», 16 palabras idénticas · tic «el coño se le apretó» ×5 |
| Cap 3 **v0.9** | aprobada (Validador APROBADO, Narr 9.0 / Temp 9.0) | 🔴 1 frase de 13 palabras repetida verbatim («sin apuro dejando que el vapor del vaporizador le subiera por la muñeca») · tics «el filo de la barra» ×4, «se mordió el labio» ×4 · resto en aviso |

Lo que enseña: el medidor **ordena las tres versiones igual que la Ama**, sin haber leído ninguna. El rework v0.3 cortó lo que ella nombró y **conservó lo que ella sintió** («Don Manuel muy idéntico», C3-04) — retocó, no reescribió. Y hasta un capítulo aprobado trae repeticiones que nadie vio. Detalle: `reportes/capitulo_04/medicion_v0.3.md` · `reportes/capitulo_03/medicion_v0.9.md`.

---

*Casos de la Ama · nace 02/09/2026 · se alimenta con cada nota de rechazo (Captura Post-Nota) · un caso no se borra, se marca 🟢 cuando deja de reincidir tres relatos seguidos.*
