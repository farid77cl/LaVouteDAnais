# 🔬 Auditoría de prosa — «Café con Piernas», 4 capítulos publicados (07/09/2026)

> **Origen.** Ama, 07/09/2026: *"analiza la prosa de los 4 capitulos del café con piernas, dime porque suena rara para mí. usa un agente externo si lo crees necesario."*
> **Documento de EVIDENCIA** (regla 12): fechado, con `archivo:línea`, no se borra, no vive en la raíz. Su sucesor natural es la corrección que se decida sobre él.
> **Corpus:** `03_Literatura/02_Finalizadas/cafe_con_piernas/capitulo_[1-4]_*.md`, prosa sin cabecera de metadatos ni bloque de firma. 48.057 palabras.

## Método

Cinco auditores externos **ciegos** (sin acceso a reglas, canon, guías ni notas del repo — lectura limpia del texto) más medición propia:

| Auditor | Lente |
|---|---|
| A | Lector-crítico, caps 1-2 |
| B | Lector-crítico, caps 3-4 |
| C | Sintaxis y prosodia medida (parser propio) |
| D | Diálogo y voz chilena |
| E | Detector de prosa generada por modelo |
| Ele | `medir_capitulo.py` (Loreto) + estilometría entre capítulos |

**Solo se reporta como hallazgo lo que converge en ≥2 fuentes independientes, o lo que está medido dos veces.** Los desacuerdos van en §4.

---

## 1 · LA CAUSA RAÍZ — la cláusula está congelada

La unidad de respiración (lo que va entre coma, punto, punto y coma, dos puntos o raya) mide **lo mismo en los cuatro capítulos**:

| | cláusulas | media | mediana | ≤3 palabras |
|---|---|---|---|---|
| Cap 1 | 1.105 | 8,01 | 7 | 27,6 % |
| Cap 2 | 1.785 | 7,67 | 6 | 26,4 % |
| Cap 3 | 1.066 | 7,63 | 6 | 22,3 % |
| Cap 4 | 1.614 | 7,45 | 6 | 24,7 % |

Divergencia Jensen-Shannon entre las distribuciones: **0,008 – 0,023** (0 = idénticas). Medido dos veces, con parsers distintos (auditor C y Ele), con el mismo resultado.

**Qué significa.** La variedad de longitud de ORACIÓN es aparente: se consigue **encadenando más ladrillos idénticos** con comas y «y», no cambiando la forma del ladrillo. Por eso el histograma de oración parece variado y el texto suena plano igual, página tras página. Es el mecanismo que la Ama percibe como «raro» y que ningún control del repo mide hoy.

**Consecuencia medida — la banda media vaciada** (oraciones de narración):

| | ≤6 palabras | 10–20 palabras | ≥31 palabras |
|---|---|---|---|
| Cap 1 | 21,5 % | 30,2 % | 22,2 % |
| Cap 4 | **38,0 %** | **17,4 %** | 24,4 % |

La prosa oscila entre el golpe seco y la trenza larga, sin frase de tamaño normal que amortigüe. **El énfasis constante es ningún énfasis.**

---

## 2 · LOS SEIS HALLAZGOS CONVERGENTES

### H1 · El narrador explica la escena que acaba de escribir  *(A · B · E)*

Tres auditores independientes llegaron a esto por su cuenta. Formatos:

- **El recibo de excitación** — el párrafo cierra certificando que se mojó, como el total de una boleta. **26 casos en el Cap 4.** `cap4:313` «*y eso también la mojó*» · `cap4:295` «*el número chico la mojó más que la verga*» · `cap3:145` «*ese pensamiento solo la mojó un poco más*».
- **La tesis dicha cuatro veces.** Que la vergüenza alimenta la calentura está enunciada en `cap1:347`, `cap1:353`, `cap1:365` y `cap1:409` — tres de ellas en dieciocho líneas.
- **«No era X. Era Y.»** ×9 en el Cap 1 (`:21`, `:61`, `:145`, `:163`…), ×2 en el Cap 2, 0 en el Cap 4. El molde no es malo en sí: `cap1:311` «*No con admiración. Con inventario.*» funciona, porque comprime en vez de explicar. El defecto es la inflación.
- **Los dos puntos revelatorios: 178 en total**, 2,7–4,9 por mil palabras en los cuatro (la prosa narrativa española ronda 0,5–1). Enunciado neutro → dos puntos → revelación. **Es el único tic que sobrevive a todas las correcciones aplicadas hasta hoy.**

### H2 · Los motivos permanentes están COPIADOS, no re-escritos  *(Ele · A · C · D · E)*

El hallazgo con más fuentes. La regla §5 del motor («motivos permanentes: presentes en cada escena») se está cumpliendo **pegando la misma frase**.

- «*con la misma parte de la cabeza que contaba plazos y honorarios*» — **6 veces**: `cap2:93`, `cap2:255`, `cap2:323`, `cap2:487`, `cap2:649`, `cap3:147`.
- **Dos bloques de 29 y 23 palabras verbatim** entre `cap2:149` y `cap2:291` — el mismo párrafo, dos veces, a 142 líneas de distancia.
- **51 tipos de 10-gramas repetidos internamente en el Cap 2** (contra 0 en el Cap 1).
- «*un segundo más de lo necesario*» y variantes ×13 · «*con dos dedos*» ×16 · «*sobre el acero*» ×31 · «*las dos manos*» ×24 · «*se dio vuelta*» ×19.
- Cap 4: «*La cabeza llegó después y le puso número*» (`:85`) / «*La cabeza llegó después, con el número*» (`:253`) / «*La cabeza llegó después y no le puso número*» (`:519`). La tercera invierte a propósito y se salva; las dos primeras son duplicado.

**Diagnóstico:** un motivo se reconoce por lo que evoca; acá se reconoce porque es el mismo párrafo pegado dos veces. Se siente como déjà vu, no como eco. **La regla escrita fabricó el tic.**

### H3 · El vocabulario se estrecha en línea recta  *(C · Ele, dos cálculos independientes)*

Riqueza léxica normalizada por longitud (ventana móvil de 1.000 palabras):

| | MATTR (Ele) | MSTTR (auditor C) | hapax |
|---|---|---|---|
| Cap 1 | 47,0 % | 47,0 % | 61,7 % |
| Cap 2 | 42,3 % | 42,4 % | 52,7 % |
| Cap 3 | 40,7 % | 40,7 % | 51,7 % |
| Cap 4 | **36,3 %** | **36,3 %** | **46,7 %** |

**El Cap 4 tiene 39 % más texto que el Cap 1 y 795 palabras distintas menos.** Cuando la lectora llega al capítulo 4 ya vio el inventario completo.

### H4 · El Capítulo 1 pertenece a otro protocolo de escritura  *(A · D · E)*

| | Cap 1 | Cap 2 | Cap 3 | Cap 4 |
|---|---|---|---|---|
| Eufemismos (miembro/falo/glande) | **23** | 4 | 4 | 1 |
| Léxico directo (verga/coño/culo/teta) | 7 | 25 | 15 | **124** |
| Puntos suspensivos en narración | **41** | 0 | 0 | 0 |
| Adverbios en `-mente` /1000 | 3,9 | 1,2 | 1,6 | **0,0** |
| Sustantivo abstracto como sujeto | **11** | 6 | 2 | **0** |
| Tríadas de adjetivos /1000 | **2,37** | 0,50 | 0,10 | 0,14 |
| Adjetivos intensificadores /1000 | **5,7** | **0,0** | 0,5 | 0,4 |

Ratio eufemismo:directo — **Cap 1 = 3,3 a 1 · Cap 4 = 1 a 124.**

**Lo más grave:** en `cap1:379` la felación se corta con puntos suspensivos y el acto no ocurre en página. El Cap 2 vuelve sobre esa misma escena y **sí la escribe** (`cap2:143`: «*la boca llena de golpe, y el grosor contra el paladar, y la arcada subiendo*»). El Cap 2 estaba reparando la elipsis del Cap 1 sin que nadie lo pidiera.

**Causa documentada:** los cuatro capítulos los escribieron modelos distintos (Cap 1 pre-A/B, con 14 versiones · Cap 2 v0.8 Escritor-Fable · Cap 3 salido del A/B de tres bandas del 19-25/08 · Cap 4 v0.2 en Opus por orden puntual de la Ama, v0.3+ en Fable). Ver `walkthrough.md`, filas del Cap 4. **No es deriva de estilo: es costura entre protocolos.**

### H5 · No hay diálogo: hay un monólogo con réplicas de servicio  *(D · B)*

Sobre 257 parlamentos:

| Personaje | Parlamentos | Palabras | Media |
|---|---|---|---|
| Cupcake | **115 (45 %)** | **1.853 (53 %)** | 16,1 |
| Felipe | 18 | 55 | **3,1** |
| «Hombre nuevo» | 6 | 18 | **3,0** |

- **Los hombres son intercambiables.** Toda su diferenciación está en la narración; ninguna en lo que dicen.
- **Cero interrupciones en 257 parlamentos.** Una sola marca de duda (`cap3:105`). Tres frases cortadas. Nadie habla mal — y hablar mal es lo que hace que un diálogo suene a persona.
- **15 parlamentos de ≥60 palabras, 12 en el Cap 4**, todos con el mismo molde: imperativo de percepción («mire cómo se le…») más descripción del cuerpo del propio hombre. En 5 de 7 ella le informa al tipo que tiene una erección: el tipo no lo necesita, **el lector sí**. Definición de parlamento que existe para informar. `cap4:79`, `:201`, `:233`, `:291`, `:443`, `:605`.
- **Personajes-llave** que existen solo para abrir la clase magistral: la chica nueva (3 intervenciones, las tres son la pregunta) y el médico (3 parlamentos, todos exposición).
- **Una sola coreografía repetida con tres hombres distintos** en el Cap 4 (`:67-85`, `:193-203`, `:425-445`): se dobla sobre el acero → habla al oído más bajo que la música → con dos dedos/dos uñas → un segundo más de lo necesario → él traga y baja los ojos.

### H6 · La plantilla de escena y la muletilla comparativa  *(B · E)*

- **Plantilla del cliente corrida seis veces** en el mismo orden: entra → tres rasgos con guiones → «el rodeo largo» → el perfume llega antes que la voz → «mi rey» al oído → él traga → paga → **el gesto omitido** («y no se lo acomodó», ×14) → cursiva con la cuenta.
- **«como si / como quien»: 109 en total** (11/37/31/30). El molde «como quien + oración» ×23. Cada gesto se explica comparándolo con otro gesto en vez de bastarse. Registro culto-escrito que choca con el chileno oral del diálogo.
- **Polisíndeton en el pico** (Cap 4): 90 oraciones con ≥3 «y», 18 con ≥5. La oración más larga del relato son **132 palabras** — `cap4:505` — **y es el orgasmo**. El clímax tiene la misma métrica que sacar la billetera.
- **Armazón temporal a la vista**: el Cap 3 está estampado como hoja de turno («A las diez y veinte», «A las diez y media», «A las once menos veinte»…). La escena no avanza por deseo: avanza porque son las once y veinte.

---

## 3 · LO QUE NO SE TOCA

Los auditores señalaron, por separado, los mismos pasajes como genuinamente humanos:

- **La escena de Marcela**, `cap4:317-407` — la única que rompe la plantilla. Cupcake se queda sin frase y el texto **no lo rellena**: `cap4:353` «*No tengo nada que decirle. Ninguna de las mías le sirve.*» · en `cap4:399` suelta su línea y se va, sin una sola línea de glosa detrás. Único intercambio del relato donde el diálogo hace el trabajo solo.
- **El tiempo muerto**, `cap3:139` — el troquel corrido de las servilletas. No vuelve, no significa, no calienta, no cierra ningún arco — y por eso el local existe.
- **La ducha del Cap 2**, `cap2:21-31` — «*Lo primero que no se fue fue el coco*». El tropiezo sintáctico de esa línea es justo lo que da voz; cualquier pasada de modelo lo habría alisado. Y la costra se **mide** («dos centímetros»), no se adjetiva.
- **El erotismo por ausencia**, `cap2:557` — «*Ningún nombre. En veinte minutos nadie la había nombrado ni una vez.*» Levanta más temperatura que las tres páginas del reservado, sin una palabra explícita.
- **La frase rota por el mundo**, `cap3:445` — «*iba a tener que subir a lavarse antes de— abajo silbó el vaporizador, alguien pidió un cortado, y el pensamiento se quedó ahí, sin terminar*».
- **El detalle físico observado**: el callo nuevo en el meñique donde aprieta la plataforma (`cap3:63`) · despegar el billete «*con la punta, nunca con la yema*» (`cap3:451`) · la cinta doble faz (`cap4:31-37`).

---

## 4 · DESACUERDOS Y CORRECCIONES — lo que NO se acepta del informe

**4.1 · El léxico sexual.** El auditor D propone cambiar `verga`→pico, `coño`→chucha, `coger`→culiar porque no son chilenas. Lingüísticamente tiene razón sobre el uso chileno. **No se ejecuta:** es una orden escrita de la Ama. `casos_ama.md:113` — *"Ni pronombre, ni perífrasis, ni ingenio de narrador donde va la palabra: **verga, coño, culo, tetas, dura, mojada**"* — nacida de su nota del 23/07/2026 (*"es un relato erótico y estás evitando decir verga"*). **Un subagente no deroga una instrucción suya.** Queda como decisión abierta a ella, no como defecto.

**4.2 · Lo que SÍ queda en pie del mismo informe:** la morfología. **0 «po», 0 «cachai», 0 «weón», 0 «o sea»** en 257 parlamentos; **un solo voseo verbal chileno** en 48.000 palabras (`cap1:357`). `CLAUDE.md:233` nombra «weón» explícitamente y aparece 0 veces. Los chilenismos de habla (`al tiro`, `regia`, `porfi`, `guatita`, `cabra`) están en el Cap 1 y **desaparecen del Cap 2 en adelante**. Lo chileno quedó en los sustantivos, no en la boca.

**4.3 · Tics que el repo persigue y que NO existen** (auditor C, medido sobre 48.057 palabras): «no X, sino Y» = **0 apariciones** · gerundio inicial de oración = **1** · participio absoluto inicial = **2** · «sustantivo abstracto + de + sustantivo» **no está sobreusado** (1,4–2,4/1000, casi todo literal). El genitivo que sí sobra es el **locativo concreto**: `sobre el acero` ×31, `el filo de la barra` ×10, `el dorso de la mano` ×8.

**4.4 · Falso positivo de mi propio medidor.** `medir_capitulo.py` sobre el archivo publicado completo marca «etiqueta de tema en voz de narrador» — está leyendo la cabecera (`**Temáticas:** #ControlMental #Sumisión…`), no la prosa. Y sus «clones de 29 palabras entre capítulos» son la **despedida de Anaïs**, que va en los cuatro a propósito. Ninguno de los dos es defecto.

**4.5 · Error de medición mío, corregido.** Reporté primero una caída de riqueza léxica de 25,0 % a 12,4 %. Esa cifra es sensible al largo del texto y los caps 2 y 4 son más largos: **el número era mío, no del relato**. Normalizada (MATTR/MSTTR), la caída sigue existiendo y es 47,0 % → 36,3 %.

---

## 5 · ERRORES DE HECHO ENCONTRADOS DE PASO

1. **Edad imposible.** Javiera tiene 29 años (`cap1:387`), lleva 4 años en el estudio (`cap2:63`, `:411`, `:491`), conoce a Don Arturo hace 3 años (`cap2:601`) — y en `cap2:429` lleva «**doce años** sumando fojas y honorarios». Habría empezado a los 17.
2. **Dos Marcelas.** Una recepcionista (`cap2:59`, `:73`, `:389`, `:633`) y una clienta (`cap4:335` en adelante). El texto nunca las une ni las separa.
3. **«Chinelas»** (`cap1:185`) es rioplatense y significa pantufla plana — describiendo una plataforma de 18 cm. En las otras menciones el propio texto dice «plataformas».
4. **La mejor frase del relato, repetida por el narrador.** `cap3:487` («*No hace falta que les guste. Solo hace falta que se les olvide que no les gustaba*») vuelve literal en cursiva 40 líneas después (`cap3:527`), por si no se entendió.

---

## 6 · QUÉ HACER — ranking, y de quién es cada decisión

| # | Acción | Impacto | Decide |
|---|---|---|---|
| 1 | **Romper la cláusula congelada.** Es la causa raíz y no la mide ningún control. Necesita una medida nueva en `medir_capitulo.py` (distribución de cláusula, no de oración) y una instrucción al Escritor que no sea «varía el ritmo» sino un objetivo medible. | Máximo | Ele propone, Ama aprueba |
| 2 | **Prohibir el recibo de excitación y los dos puntos revelatorios.** ~200 puntos de fricción en 48.000 palabras, con regla operativa simple: la calentura se ejecuta dentro de la escena, no se certifica al final del párrafo. | Muy alto | Ele propone |
| 3 | **Cambiar cómo se cumplen los Motivos Permanentes.** La regla §5 pide presencia en cada escena y se está cumpliendo con copy-paste. Debe pedir explícitamente **re-visión, no repetición literal** — y `medir_capitulo.py` ya lo caza (M1/M2), solo que nadie corrió el medidor sobre estos cuatro. | Muy alto | Ele propone |
| 4 | **Darles boca a los hombres, o dejarlos callados.** Es más honesto que hacerlos decir «Sí. Sí. Perdón» dieciocho veces. | Alto | Ama |
| 5 | **Léxico sexual chileno** (`verga`/`coño`/`coger`). Contradice su regla C2 escrita. | — | **Solo la Ama** |
| 6 | **Los 4 apartes al lector** (`cap3:327`, `cap4:57`, `:241`, `:511`), que usan la misma cursiva que los pensamientos de ella y conviven con la despedida de Anaïs, que también es segunda persona: dos voces rompiendo la misma cuarta pared. | Medio | Ama |
| 7 | **Los cuatro errores de hecho** de §5. Los capítulos están publicados y con Gate; corregirlos es decisión editorial suya. | Medio | **Solo la Ama** |

> **Nota de alcance.** Nada de esto se ejecuta sobre los capítulos publicados sin orden suya: los cuatro están cerrados y el Cap 4 tiene Gate (`gate_capitulo_04_cuanto_es_v0.5.md`). Lo que sí es trabajo propio, si ella lo aprueba, es llevar los hallazgos 1-3 al motor para que el **próximo** relato no nazca con esto puesto.
