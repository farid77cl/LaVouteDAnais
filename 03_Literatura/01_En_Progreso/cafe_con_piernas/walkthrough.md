# Walkthrough — Café con Piernas

*Bitácora viva del proyecto. Engine Escritura LV v4.8 · Nivel 4.*
*Slug: `cafe_con_piernas` · Eje: **control mental** + bimboficación · **Lengua: espanol neutro (~5% de color local, Gate 04/08).***

---

## Estado

| Fase | Artefacto | Estado |
|---|---|---|
| 0 · Investigación | `investigacion.md` | ✅ Cerrada 03/08/2026 (~18.000 palabras, §11 = puerta única) · 🔄 **Enriquecida 05/08/2026** con 3 fuentes nuevas de la Ama (Reddit r/Santiago, La Vanguardia, BBC vía espejo t13) — ver `referencias/05-07_*.md` y §8/§7.1/§3.7 de `investigacion.md` |
| 0b · Referencias | `referencias/INFORME_ESCRITOR_referencias.md` | ✅ REF-01 + REF-02 analizadas |
| 1 · Composición | `canon_relato.md` + `cronologia.md` | ✅ 03/08/2026 — **EN REVISIÓN (Gate de la Ama)** |
| 2 · Escritura | `capitulo_01_el_turno_de_prueba_v0.7.md` | ✅ **05/08/2026 — Cap 1 v0.7, quinta vuelta: eje de lenguaje separado del eje psicológico.** El agente `escritor-nivel4.md` sumó una corrección de método el 05/08 (justo tras §6 Curva de Resistencia): la resistencia gobierna solo si Javiera *reconoce conscientemente* el placer (eso sigue sin ceder), nunca si el texto lo *describe* con anatomía explícita (eso nunca debe estar contenido). v0.6 fallaba ahí: los tres momentos de calor reciclaban la misma imagen difusa ("sin punto fijo, repartido... válvula") — léxico clonado de `esposa_servidumbre`, ya marcado con advertencia junto al Fragmento 7 de `antologia_calenton.md`. v0.7 reescribe esos tres momentos con anatomía distinta cada vez (pezones/tela del sostén, muslos/ingle, tanga/labios), agrega dos anomalías de `cronologia.md` §3 en su primera aparición real (bloque de 40 min no reconstruible, frase idéntica de Yasna repetida por otra compañera sin comentario) y recomprime el raconto de apertura a 4 imágenes concretas. Estructura, vestuario, curva de resistencia y léxico sin cambios. Ver `reportes/capitulo_01/autoverificacion_v0.7.md`. v0.6 archivado en `borradores/capitulo_01/`.
| 2 · Escritura (superado) | `capitulo_01_el_turno_de_prueba_v0.6.md` | 🔄 **Superado por v0.7 (05/08/2026).** Registro histórico: 05/08/2026 — Cap 1 v0.6, pasada de intensidad real. v0.5 mantenía estructura/vestuario correctos pero la Ama la repudió otra vez, más duro: *"nada erótico... si alguien lee este primer capítulo no va a querer leer el resto"*, más dos correcciones puntuales ignoradas en v0.5 (mención de "café con vestidito" y escena de medias, ambas sacadas). Diagnóstico contra `01_Canon/antologia_calenton.md`: la sensación se nombraba y se apagaba con una excusa boba en la misma respiración, sin que el lector la sintiera completa. v0.6 reescribe la textura física de cada escena (cuerpo antes que mente, sensación fundida no diluida, excusa después y aparte) y agrega — nuevo, no existía antes — signos físicos de habituación al mecanismo en Yasna y las compañeras del camarín, nunca nombrados. Estructura, vestuario, curva de resistencia y léxico intactos. v0.3-v0.5 archivados en `borradores/capitulo_01/`. Autoverificación con citas antes/después en `reportes/capitulo_01/autoverificacion_v0.6.md`.
| 2 · Escritura (superado) | `capitulo_01_el_turno_de_prueba_v0.5.md` | 🔄 **Superado por v0.6 (05/08/2026).** Registro histórico: comprimió el raconto a 3 párrafos + 1 línea y corrigió vestuario/mecanismo/ambiente, pero la textura sensorial seguía diluida — ver fila de arriba.
| 2 · Escritura (superado) | `capitulo_01_el_turno_de_prueba_v0.4.md` | 🔄 **Superado por v0.5 (05/08/2026).** Registro histórico: 05/08/2026 — Cap 1 v0.4 completo. La Ama leyó el v0.3 completo y su veredicto real fue más duro que el MICRO-FIX del Validador automático: raconto largo, Camila insuficientemente extrema, escena de las medias nunca escrita (discrepancia ya marcada abajo), erotismo concentrado solo en las puntas. Reescrito en 2 tramos: tramo 1 (escenas 1-3, cold open + raconto recomprimido + confrontación) y tramo 2 (escenas 4-5, este cierre — café del paseo mencionado, entrada al Yakarta con el aparato mostrado funcionando antes de que trabaje ahí, contratación con don Nelson, camarín con Yasna incl. **medias gruesas + "traer finas mañana" ahora sí escrito**, luquita, "no enamorarse", el vaso; cierre del turno con mirada sostenida, contracción, pago del día completo, marcas del cuerpo, olor a café). v0.3 archivado en `borradores/capitulo_01/`. Pasada de `HUMANIZADOR.md` corrida sobre el archivo completo (ambos tramos): tricolones excedentes recortados en escenas 2-4, un doblete de adjetivo y el comodín "algo" llevados a cupo. Autoverificación en `reportes/capitulo_01/autoverificacion_v0.4.md` |
| 3 · Validación | `reportes/capitulo_01/validacion_v0.3.md` | 🔄 **Superada dos veces.** El MICRO-FIX automático de v0.3 (Temperatura 8.8) quedó sin efecto ante la lectura completa de la Ama (05/08), y a su vez v0.4 fue repudiado en duro por la misma Ama ("cero erotismo... Antártica -40"). v0.5 reescribe el capítulo entero — pendiente nueva pasada de `validador` sobre v0.5 antes del Gate final. |

---

## Decisiones tomadas por el Compositor (03/08/2026)

Todo lo de abajo **no venía decidido** por la Ama. Lo elegí yo a partir de `investigacion.md` y del informe de referencias. Cualquiera de estas se cae sin tocar la arquitectura si la Ama prefiere otra cosa.

### D1 · Nombres y oficio del reparto
- **Protagonista: Javiera Soto, «la Javi», 29, contadora auditora** en una oficina del centro. Elegida así por tres razones: (a) el oficio choca de frente con el motivo M4 —el número, la cuota, contar— y la degradación se vuelve medible; (b) `investigacion.md` §4.9.4 ya escribió su coartada estado 1 como *"voy a poder ver el libro de contabilidad"*, que es un pensamiento de auditora, no de periodista; (c) **una periodista habría empujado el relato al thriller**, que §2b prohíbe explícitamente. Además pone la ironía en su lugar: era del mundo de los oficinistas que ahora la miran.
- **La amiga: Camila Reyes, «la Cami».** Adentro del local le decían **«Ivanna»** — eso hace funcionar la grieta de §11.3 (la nombran por su nombre real, no por el del local).
- **El dueño: don Nelson**, 62, camisa arremangada, paño al hombro, calculadora de mesa. Administrador, no amo. Regla propia: no dice más de dos frases seguidas en todo el relato.
- **La veterana: la Yasna**, 38, doce años en la pega. Toda la sugestión indirecta entra por su boca. Regla propia: **nunca insiste** — dice la cosa una vez y cambia de tema.
- **La Yoli** se conserva como figura citada y ausente (viene de §4.4 como ejemplo de bucle anidado). No aparece nunca y nunca se explica adónde fue.
- **Nombre nuevo del peldaño 6: «Malú».** Dos sílabas, chileno, dicho rápido, y funciona para el remate de §9.4 (alguien lo dice al otro lado de la pieza y ella se da vuelta antes de pensarlo).

### D2 · Los dos locales, con nombre inventado y calle real
Según §3.7 (nombres inventados, geografía real):
- **Café Trinidad** — Paseo Estado con Huérfanos, a pie de calle. Peldaño 1.
- **Café Yakarta** — pasaje interior de una galería de Bandera, a tres cuadras de La Moneda.

**Decisión estructural asociada:** los peldaños 2, 3 y 4 pasan **dentro del mismo edificio** (salón de arriba → sótano por escalera interna → cubículo), no en tres locales distintos. Es lo que hace verdad la directiva de la Ama de que *"la frontera se cruza una sola vez"*, y evita que el arco parezca una gira de locales.

### D3 · Nueve capítulos
No lo pedía nadie; lo impone el material. `investigacion.md` §6.2 exige capítulo entero para el peldaño 0→1 y **dos capítulos** para el 2→3, y §10.5 llama al tramo ciego *"la firma del relato"*, así que no puede ir comprimido. Reparto: Cap 1 peldaño 0→1 · Cap 2 peldaño 1→2 · Cap 3 peldaño 2 · Caps 4-5 peldaño 3 · Cap 6 peldaño 4 · Cap 7 tramo ciego · Cap 8 revelación · Cap 9 cámara.

**Por qué la revelación y la cámara van separadas:** la revelación transcurre con el aparato apagado —sin música, sin penumbra, sin taco— y ése es, por definición, el escenario menos sensorial del relato. Metida en el mismo capítulo que la cámara, se la come. Separadas, el Cap 8 calienta por el sí en sí mismo y el Cap 9 se queda con la descarga, y la regla de temperatura ascendente se cumple sin trampas.

### D4 · 🔴 Dónde se apagó el aparato (lo pedía el informe de referencias §6)
El informe obligaba al Compositor a fijar el punto exacto, y recomendaba *"entre el 1 y el 2"*. **Fijado: el día que deja de tirarse la falda para abajo, ~Día 40, final del Cap 2.**

Es la mejor marca posible porque ya era un evento canónico del relato (§2 punto 4, §6.2) y ella no lo registra como nada. Traducción sin una gota de ciencia ficción: el aparato es **frontal** —opera sobre la que es nueva: la desorientación del turno, el ancla del olor, el espejo, la habituación a la mirada, el cansancio—; cuando deja de ser nueva, ya no queda nada que hacerle. De ahí al final, **todo lo hizo ella**: el Yakarta, el sótano, las uñas, los labios, las tetas, el privado, la cámara.

Consecuencias que hay que respetar al escribir:
- El lector no lo sabe hasta el Cap 8, y lee siete capítulos de decisiones propias creyendo que ve inducción. La revelación **reordena el relato entero hacia atrás**.
- Blinda §10.4 por construcción: si el ambiente ya no operaba, el último sí es limpio sin que el Escritor tenga que cuidarlo.
- No contradice §11.3: el local no "apagó" nada a propósito ni hizo nada especial con ella. Simplemente la máquina tiene una sola configuración y se le acabó el trabajo.

### D5 · Ubicación del *like* (termómetro §11.4)
Estado 4 (el like) al cierre del **Cap 5**; la coartada muere en el **Cap 6**. Van cerca pero no juntos: son el mismo gesto en dos registros y pegados se anulan. Estado 5 (ya no las abre, sin comentario) desde el Cap 7.

### D6 · Calendario y modo de anclaje
Día cero = el día que ve la cuenta nueva de la Camila. Arco total ~ocho meses y medio. **Anclaje relativo puro**, con una sola concesión declarada en `cronologia.md`: los cafés cierran el domingo, y **«domingo» es el único día de la semana nombrable en la prosa**, siempre con el mismo significado (día sin turno). Esto sale directo de la lección `esposa_servidumbre` (un "martes" suelto descuadró la cuenta de la semana).

### D7 · Modificaciones corporales y recuperación real
Orden de §4.7: uñas → pelo → pestañas → labios → tetas. Decidí el **platinado** para el pelo (es el marcador de "ya no puedo volver a la oficina") y metí **doce días fuera del turno** después de las tetas. Ese hueco no es realismo decorativo: es un vacío obligado a mitad del Cap 6 donde ella está en su casa, sin mirada, sin cuota y sin nada que contar — y lo que hace con ese vacío la delata más que cualquier escena de barra.

---

## Lo que el Escritor NO puede tocar (viene de la Ama, no de mí)

- Nadie la obliga nunca a nada · bajar es subir · el local sabe y no hace nada distinto · nadie explica el mecanismo · nadie es villano.
- Ella no cae por la escalera: la sube a propósito. La resistencia está en el precio del ascenso, no en el ascenso.
- Ninguna cesión ocurre en la escena donde se propone.
- El calor es de exhibición, no de penetración.
- Cierre sin epílogo, sin rescate, sin moraleja.

---

## Bitácora

- **03/08/2026 — Fase 0.** Investigación cerrada por el Investigador (~18.000 palabras). §11 agregada por directiva de la Ama esa misma tarde y declarada puerta única sobre §5, §6, §9 y §10.
- **03/08/2026 — Fase 0b.** Informe de referencias compilado (REF-01 «The Hands That Lead», REF-02 «Stripclub Bimbos»). Abre dos deudas para el Compositor: fijar dónde se apagó el aparato (→ D4) y decidir cuándo aparece la amiga (ya resuelto por la Ama en §11: capítulo 1).
- **03/08/2026 — Fase 1.** `canon_relato.md` (~2.150 palabras) y `cronologia.md` creados. Sin intake: la Ama cerró toda la arquitectura en conversación y en la investigación. Siete decisiones propias registradas arriba. **Pendiente: Gate de la Ama sobre el canon.**
- **04/08/2026 — Fase 2, Cap 1 v0.3 (Gate 2, reestructuración de ritmo).** Reescrito completo como in medias res + flashback: esc. 1 (cold open, mid-turno, gancho = pierde la cuenta de los cafés) → esc. 2 (flashback comprimido ~830 palabras contra ~2.000 del v0.2, corte real verificado) → esc. 3 (la casa, P1, trim ligero, sustancia intacta) → esc. 4 (café del paseo mencionado + entra al Yakarta + contratación + camarín con Yasna + el vaso, H32) → esc. 5 (vuelve al frame y cierra el mismo turno: mirada sostenida, contracción, don Nelson, tanga, olor). Escrito en 2 tramos (MODO TRAMO). Pasada completa del `HUMANIZADOR.md` sobre el archivo cerrado: se detectaron y corrigieron excesos de tricolon (T1) y dobletes de adjetivo (T7) heredados de reutilizar prosa del v0.2 en varias escenas a la vez, y se inyectó lastre (L1/L2 por escena, L6 en el lull de la esc. 5) que no traía el v0.2. Un error de continuidad propio detectado y corregido en la marcha: "tres días después subió el cerro" contradecía la cronología (Día 2 → Día 3 son consecutivos) — corregido a "al día siguiente". Un hecho plantado (H28, los puntitos del vaporizador) se había perdido en la compresión de la esc. 2 original — restituido en la esc. 5. Un hecho plantado (H36, el hospital por la hernia) no sobrevivió la compresión y se derogó formalmente en `cronologia.md` (el payoff sigue en pie vía H35). `cronologia.md` actualizada: tabla de remapeo de escenas v0.2→v0.3, y los orígenes de H25/H27/H32/H33/H35/H36 corregidos a la numeración nueva.
- **03/08/2026 — Fase 2, Cap 1 (v0.1/v0.2, superado).** `capitulo_01_el_turno_de_prueba_v0.1.md` (~6.250 palabras). Cinco escenas: desaparición · RRSS · la casa del barrio alto · el Trinidad · el primer turno. Primera aplicación del `HUMANIZADOR.md` (pasada final sobre el capítulo cerrado, 21 correcciones, veredicto LIMPIO 9/9). Tres decisiones del Escritor que el Compositor no había fijado y que quedan en `cronologia.md`: (a) la dirección de la casa la regala la **mamá** de la Camila por teléfono —mata el thriller sin matar el motor—; (b) **la Javi pide la pega ella misma** (§11.2 desde el primer peldaño, y blinda §11.3); (c) **«Ivanna» se revela en el Cap 1**, no en el 3, para que la grieta H12 tenga contra qué contrastar. Diez hechos plantados nuevos (H21-H30) y estación del arco fijada por implicación (Día 1 = otoño → Cap 9 = verano).
  - *Nota de honestidad sobre el largo:* el techo del Nivel 4 son ~2.000 palabras y el canon quedó ~150 arriba. El excedente es §4b y §4c, que el protocolo v4.8 obliga a **copiar** de la investigación y no a resumir. Recorté todo lo demás (premisa, pivotes, personajes, cementerio) antes de dejarlo pasar. Si la Ama lo quiere más corto, lo que sobra de verdad son las Cinco Leyes de §1b, que se solapan con el Cementerio.
- **05/08/2026 — Reescritura TOTAL v0.4 → v0.5.** La Ama leyó v0.4 completo y su veredicto fue más duro que cualquier Gate anterior: *"300 líneas y cero erotismo... esto es la Antártica, temperatura -40... segunda regla, es un relato de control mental!!!"*. v0.5 reemplaza a v0.4 con cinco correcciones ejecutadas: (1) raconto entero comprimido a 3 párrafos + 1 línea de diálogo sobreviviente — el capítulo deja de ser sobre la amiga y pasa a ser, en la enorme mayoría de su extensión, sobre Javiera entrando y trabajando en el Yakarta; (2) vestuario corregido — Javiera de prueba en minifalda (excepción), compañeras ya contratadas en el uniforme real (microbikini/pieza de tiras entrepierna-pechos-cuello, día temático), registradas por Javiera con juicio y fascinación no reconocida; (3) el aroma a café y el pulso bajo la música mostrados actuando de forma perceptible y progresiva sobre el cuerpo/cabeza de Javiera, siempre atribuidos por ella a causas normales, nunca nombrados por el narrador; (4) escena completa y explícita de coqueteo-por-propina, con el saludo de dos besos como único contacto físico permitido en todo el capítulo; (5) densidad erótica repartida en todas las escenas. Pasada de `HUMANIZADOR.md`: LIMPIO. `cronologia.md` actualizada (estado del cuerpo Cap 1, H27). v0.4 archivado en `borradores/capitulo_01/`. Pendiente: correr `validador` sobre v0.5 antes del Gate final.
- **05/08/2026 — Gate real de la Ama sobre v0.3, aplicado.** `nota_capitulo_01_el_turno_de_prueba_v0.3.md` llegó por push de la app a la raíz del proyecto (Regla de Oro 17) con un veredicto mucho más duro que el MICRO-FIX del Validador automático del 04/08: frase confusa ("porque los pies"), raconto demasiado largo, Camila insuficientemente extrema, y sobre todo "más de la mitad del relato y nada erótico… le falta sensualidad, erotismo al relato erótico". Se aplicó el canon-vocab nuevo de `investigacion.md` (enriquecida 05/08: luquita, café con vestidito, "el único cuidado es no enamorarse") y se reescribió el capítulo completo como v0.4 en 2 tramos — ver fila de Fase 2 arriba. Nota archivada en `reportes/capitulo_01/nota_capitulo_01_el_turno_de_prueba_v0.3_APLICADA.md`. Pendiente: correr `validador` sobre v0.4 antes de subir a Gate final.

---

## 🔴 Gate de la Ama — 04/08/2026 (nota + correccion en vivo)

Llego `nota_capitulo_01_el_turno_de_prueba_v0.1.md` por push de la app, y la Ama corrigio en vivo la misma manana. **El Cap 1 v0.1 queda superado; se reescribe entero como v0.2.**

### Lo que ordeno

1. **Espanol neutro** en toda la prosa y todos los dialogos. Motivo literal: *"lei a ambas amigas hablando y no es asi como hablarian, estas abusando de los chilenismos"*. Techo ~5%, y ese 5% vive en sustantivos del oficio, nunca en la gramatica. Prohibido el voseo verbal chileno y el articulo delante del nombre propio.
2. **Un solo local, y un solo salon.** Entra directo al cafe turbio de la galeria. **No hay sotano, no hay piso de abajo, no hay segundo local.** El cafe del paseo solo se menciona (es el que no tiene el vidrio polarizado).
3. **El ascenso es sobre ella:** *"el ascenso sera ir cambiandola lentamente"* — maquillaje, tacones cada vez mas altos, agradarles, unas, pelo, labios, cuerpo.
4. **La amiga, mucho mas extrema** de cuerpo y **mucho mas pulcra de habla** (trad wife programada).
5. **El ambiente y la mecanica se escriben en escena** — es la vitrina del fetiche.
6. 🥤 **La bebida de las chicas** que desinhibe y ablanda.
7. 🗣️ **El otro yo que se va formando y le pide cosas estando fuera** del local.

### Decisiones de orquestacion (mias, sobre su directiva)

- **D8 · Muere P2 y se reemplaza, no se relocaliza.** Primero intente bajar la frontera al sotano; la Ama corrigio que no hay sotano. Sin lugar que cruzar, P2 pasa a ser **la primera cosa que ella pide sola, fuera del local** (`canon_relato.md` §2). Conserva la funcion original del pivote —mision y mecanismo vueltos la misma accion— sin geografia.
- **D9 · El otro yo es el nuevo esqueleto del arco** (§6c). Reemplaza al peldano-de-lugar: cuatro estados (objetos → miradas → cuerpo → **silencio**), suena **solo fuera del turno**, se escribe **sin marcar** dentro del mismo parrafo del pensamiento normal, y ella **nunca lo reconoce como ajeno**. El silencio de los Caps 8-9 es el pago.
- **D10 · La bebida entra SIN confirmarse jamas** (§6b-bis). Le dije a la Ama el problema antes de escribirlo: una droga confirmada le regala a Javiera —y al lector— la excusa de *"me vencieron"*, que es exactamente el motor de REF-02 «Stripclub Bimbos», del que este relato se declaro el opuesto. La forma que respeta la directiva y no rompe la Ley 1 ni el si informado del Cap 8: existe, se ve, nadie explica que es, sus efectos son indistinguibles del calor + la musica + las ocho horas, **nadie se la impone** (se la sirve ella, y despues se la pasa a la nueva), y en el Cap 8 la respuesta **no la salva**. Queda como anomalia irresoluble, igual que H9.
- **D11 · El calendario NO se corre.** Las fechas del arco son las mismas; cambia que ocurre en ellas. Evita rehacer `cronologia.md` entera y mantiene los Hechos Plantados vivos.

### Estado de los Hechos Plantados

Ninguno se deroga salvo los de geografia (H10, H11, H30, ya corregidos). Todo lo marcado `escrito` con origen en el Cap 1 pasa a **re-escribiendose en v0.2**: el hecho sigue siendo canon, cambia su redaccion. Nuevos: **H31** (el otro yo) y **H32** (el vaso).
