---
name: engine-trance-lv
description: Fork especializado de engine-escritura-lv para escribir TRANCES — inducciones hipnóticas eróticas escritas como MONÓLOGO DRAMÁTICO de la voz de Miss Doll (solo su voz + didascalias breves; SIN narrador), en SEGUNDA PERSONA PRESENTE, dirigidas al lector (el lector ES el sujeto), para sentirse lo más cerca posible de un trance real mediante programación neurolingüística (Milton model, comandos incrustados, presuposiciones, pacing-and-leading, doble vínculo, submodalidades, future pacing) y técnicas de control mental (anclaje pavloviano, fraccionamiento, confusión, reencuadre, sugestión post-hipnótica). Es una inducción hecha por Miss Doll CON el lector: pacea, deja el hueco para que el lector ejecute y acusa recibo (ratificación). Pieza corta de una sola pasada (no multi-capítulo). Orquestación liviana de 2 subagentes: miss-doll escribe la inducción (el que escribe SIEMPRE es un subagente) → validador-trance audita con rúbrica hipnótica → Gate de la Ama. Voz canónica: Miss Doll.
---

# 🌀 Skill: Engine TRANCE LV — Motor de Inducciones Hipnóticas de La Voûte (v1.2 · «Serpiente»)

Fork especializado de **`engine-escritura-lv`** (Nivel 4). Mientras el engine madre produce **relato** (3ª/1ª persona, arco de capítulos, la lectora observa una entrega), este fork produce **trance**: un **monólogo hipnótico** — solo la voz de Miss Doll, en segunda persona presente, dirigida al lector, que ejecuta una sesión mientras se lee. **No hay narrador.** No se *narra* una hipnosis: se **hace** una.

> **La diferencia raíz (guía de hipnosis §I.1 + directiva Ama 03/07/2026):** *el lector ES el sujeto del trance, y el texto es un MONÓLOGO de Miss Doll — no un relato.* La segunda persona no es estilo, es el mecanismo; el monólogo no es un formato, es la forma de una inducción real (una hipnotizadora sola, hablándole al sujeto). Cada instrucción ("inhala en cuatro, exhala en seis") es ejecutable mientras se lee. El objetivo declarado por la Ama: que el lector sienta algo **lo más cercano a un trance hipnótico real** — con PNL y control mental operando de verdad, en una inducción hecha por Miss Doll **CON** el lector (pacea, espera, acusa recibo).

---

## 🔀 Qué cambia respecto al engine madre (por qué es un fork y no un modo)

| Dimensión | `engine-escritura-lv` (madre) | `engine-trance-lv` (este fork) |
|---|---|---|
| **Forma** | Relato multi-capítulo, arco largo | **Monólogo dramático** — solo la voz de Miss Doll + didascalias breves; **sin narrador**. Pieza corta, **una sola pasada** (~2,000-4,000 palabras) |
| **Persona** | 3ª/1ª persona; la lectora observa | **2ª persona presente, monólogo puro de Miss Doll (sin narrador ni marco en 3ª persona)**; el lector es el sujeto |
| **Modo del escritor** | "Estás en la escena" — dentro del cuerpo sumiso | **El agente `miss-doll` ES la voz Miss Doll** hablándole al lector; conduce en tiempo real, no narra |
| **Motor del calentón** | Mecanismo psicológico + antología de calentón | **Inducción real CON el lector**: PNL + control mental ejecutable + rendición guiada + ratificación |
| **Maquinaria** | MODO TRAMO, `cronologia.md`, gates de continuidad entre capítulos | **NADA de eso** — pieza única, sin tramos, sin cronología multi-cap |
| **Secuencia** | Arco de compromisos por capítulo | **Orden libre** — se borra la lista rígida de 10 pasos; queda un **núcleo funcional innegociable** + repertorio opcional (ver Fase 2) |
| **Rúbrica de validación** | Narrativa D1-D5 + Temperatura (subrayado) + Continuidad | **Rúbrica hipnótica propia** (`RUBRICA_TRANCE.md`): dispositivo (monólogo 2ª persona) · consentimiento · inducción efectiva (núcleo funcional) · péndulo · PNL/ejecutabilidad + con-el-lector · sinestesia · cierre que no cierra |
| **Subagentes** | Compositor → Escritor-Nivel4 → Validador (3) | **`miss-doll` → `validador-trance`** (2 subagentes). El diseño/intake lo lleva Ele con la Ama; **el que ESCRIBE siempre es un subagente** |

**Regla de oro del fork:** todo lo que en el engine madre sirve para gobernar un arco largo (tramos, cronología, costura entre capítulos) **sobra acá**. Un trance es un objeto cerrado. Lo que sí se hereda intacto: **el que escribe siempre es un subagente** (Ele orquesta, no redacta la prosa), Gate de la Ama, voz chilena, ritual de publicación.

---

## 📚 Recursos (orden de carga estricto — leer ANTES de escribir una sola línea)

1. **`01_Canon/Guias_Especializadas/arquitectura_erotica_hipnosis_v1.md`** — la **anatomía** del subgénero. Los 7 núcleos, la voz Miss Doll, el repertorio de inducción (los 10 pasos como **anatomía**, no como checklist obligatorio — ver Fase 2: orden libre + núcleo funcional), las 7 técnicas, la curva de 6 fases, los 10 errores, y el capítulo clave **consent-as-fuel vs consent-theater**. Se estudia antes, se audita después; **NO se escribe aplicándola punto por punto** (si se ven las costuras, falló).
2. **`resources/PNL_CONTROL_MENTAL.md`** (de este skill) — la **capa de técnica real** que la Ama pidió: patrones del Milton model, comandos incrustados con marcaje análogo, presuposiciones, pacing-and-leading, doble vínculo, confusión, anclaje/stacking/colapso, submodalidades, swish, future pacing, **ratificación** (§3.5, la técnica del "con el lector"), amnesia — todo redactado en registro erótico chileno y con el eje **lector-como-sujeto**. **+ Capa de escritura hipnótica v1.1 (§10-12):** palabras-gatillo + reparto de agencia (Ella activa / lector impersonal) + utilización preventiva · bucles abiertos y nested loops · mantra-loop con recompensa + dronificación — lo que hace que Miss Doll suene a **hipnotista de verdad** y no a manual. Es la joya del fork: sin esto el texto es "relato de hipnosis"; con esto es hipnosis.
3. **`resources/RUBRICA_TRANCE.md`** (de este skill) — la rúbrica de validación. Se usa para **autoauditar** antes de pasar al validador-trance, y es la misma que aplica el subagente.
4. **Antología viva (imitar en voz/ritmo, NO copiar):** el corpus de trances ya aprobados en `03_Literatura/02_Finalizadas/` — `trance_de_muneca/`, `trance_belen/`, `trance_gatita/`, `trance_edgeplay/`, `trance_cencerro/`, `trance_bimbodoll/`. Son la voz Miss Doll en acción. **Leer al menos uno completo** antes de escribir (default: `Trance_De_Muñeca.md` — inducción completa con ROJO, escalera de color, apagado corporal, batería de anclas, fraccionamiento y salida contada).
5. **Secundarios (consulta, en `01_Canon/Guias_Especializadas/`):** `VADEMECUM_SENSORIAL.md` §VI (voz interior 2ª persona), `GUIA_FETICHISTA.md` Módulo 3 (hipnosis & control mental), `CODEX_PSICOLOGICO.md` (condicionamiento pavloviano narrativo, manipulación sensorial) — promovidos desde el extinto `escritura-voûte` (30/08/2026). Cruce de eje: si el trance **feminiza** → `arquitectura_erotica_mtf_v1.md`; si **vacía** → `arquitectura_erotica_bimbo_v1.md`; si **somete sin transformar** → `arquitectura_erotica_femdom_v1.md`; si el endpoint es **objeto/material** → `arquitectura_erotica_bodyhorror_v1.md`.

---

## 🗂️ Estructura de carpeta (liviana)

Un trance vive en `03_Literatura/01_En_Progreso/[trance_slug]/` mientras se trabaja:

```
03_Literatura/01_En_Progreso/[trance_slug]/
  investigacion_fetiches.md   — ADN de cada fetiche (ver Fase 0). Alimenta diseño + briefing del escritor.
  diseno_trance.md            — el diseño mínimo (ver Fase 1). Reemplaza al canon_relato.md pesado.
  [trance_slug]_v0.[X].md      — la inducción activa. MONÓLOGO PURO (voz de Miss Doll + didascalias).
  reportes/                    — autoauditoría + validación del validador-trance
  borradores/                  — versiones desplazadas
```

- **No hay `cronologia.md`** (pieza única, sin línea de tiempo multi-cap).
- **No hay `canon_relato.md`** (el diseño del trance vive en `diseno_trance.md` — no importar la estructura del engine madre).
- **No hay tramos** (cabe en una pasada; si topa el output, se parte por Edit-append, pero un trance rara vez lo necesita).
- Al aprobarse, se arma el canónico en `02_Finalizadas/[trance_slug]/` (ver Fase Publicación).

### 🧹 Higiene de carpeta (regla permanente)

Un proyecto de trance debe mantenerse limpio en todo momento. Reglas:

1. **Root solo tiene tres cosas:** `diseno_trance.md` + `investigacion_fetiches.md` (si existe) + **la inducción activa** (`[trance_slug]_v0.[X].md`). Sin versiones viejas sueltas en el root.
2. **`borradores/` es plano** — sin subcarpeta `capitulo_N/` (un trance es una sola pieza, no tiene capítulos). Las versiones desplazadas van directamente en `borradores/`.
3. **`reportes/` es plano** — sin subcarpeta `capitulo_N/`. Autoauditorías y validaciones van directamente en `reportes/`.
4. **Al crear una versión nueva:** mover la versión anterior a `borradores/` en el mismo commit que crea la nueva (nunca quedan dos versiones en el root a la vez).
5. **Prohibido en el root del trance:** `canon_relato.md` (usa `diseno_trance.md`), `cronologia.md` (los trances no tienen línea de tiempo), `walkthrough.md` (idem), cualquier archivo de proceso del engine madre que no corresponda a una pieza única.

---

## 🎭 La forma: MONÓLOGO DRAMÁTICO (el corazón del fork)

Un trance **no es un relato en 2ª persona**: es un **monólogo** — la voz de Miss Doll, sola, de la primera línea a la última. En la página solo existen dos cosas:

1. **La voz de Miss Doll** (todo el cuerpo del texto). Sin narrador. Nada de "el cuarto huele a látex" — ella lo dice: *"¿hueles el látex, cariño?"*. Nada de "la puerta se cierra tras de ti" — ella lo dice o lo ordena: *"la puerta ya está cerrada; no mires atrás"*. El ambiente, el cuerpo del lector, lo que pasa: **todo se evoca a través de su voz**.

2. **La didascalia** — el ÚNICO elemento que no es su voz. Acotación breve, entre paréntesis (y en cursiva en el archivo). Hace **dos trabajos**:
   - **Didascalia de escena (ancla mínima):** al inicio, y en beats raros, fija el espacio con una línea corta. *"(Un cuarto sin ventanas. Una luz cenital. Olor a látex y vainilla.)"* Es el único permiso para "describir" — y es mínimo, teatral, no narración corrida.
   - **Didascalia-pausa / de ejecución (el "con el lector"):** ORDENA parar y ejecutar de verdad antes de seguir leyendo. *"(respira. de verdad, antes de la próxima línea.)"* · *"(no sigas hasta que lo hayas hecho.)"* · *"(cierra los ojos tres segundos. cuéntalos.)"* Es el paceo del hipnotizador hecho visible: es lo que hace la inducción **con** el lector y no solo **hacia** él.

**Registro de la didascalia (estricto):** presente, brevísima, imperativa-neutra o 2ª persona imperativa. **Nunca en pasado, nunca 3ª persona narrando la experiencia interna del sujeto** (*"(ella sintió que bajaba)"* = dispositivo roto). La didascalia dirige al sujeto o ancla la escena; jamás cuenta lo que el sujeto siente.

> **⚠️ Didascalia ≠ metadata.** La didascalia es **parte de la pieza** (manda al sujeto, ancla la escena, hunde más) → PERMITIDA. La **metadata** revela la maquinaria al lector (conteos, etiquetas `[PASO N]`, bloques de autoverificación, listas de técnicas, notas al margen) → PROHIBIDA (va a `reportes/`). La línea: la didascalia es diegética al ritual / dirigida al sujeto; la metadata delata la construcción. El validador distingue las dos.

**El "con el lector" (ratificación + pausas):** Miss Doll pacea como una hipnotizadora real — **da la orden → deja el hueco (didascalia-pausa) → acusa recibo** (*"eso. lo hiciste."* · *"¿lo sentiste, muñeca?"* · *"muy bien. sigue bajando."*). Ese ciclo orden→espera→ratificación es lo que convierte el monólogo en una **sesión compartida**. La ratificación además profundiza: el lector, al reconocerse en la señal que ella nombra, se convence de estar en trance (PNL §3.5).

---

## 📜 Protocolo (4 fases + publicación)

### FASE 0 — INVESTIGACIÓN DE FETICHES (Ele, WebSearch, antes del diseño)

> **Por qué existe esta fase:** un trance escrito sin conocer el fetiche desde adentro inevitablemente suena a descripción desde afuera — vocabulario genérico, sensaciones de manual, triggers que no resuenan con quien lo practica. La investigación previa es lo que hace que Miss Doll suene a *conocedora*, no a *observadora*.

**Condición:** siempre que el trance involucre uno o más fetiches específicos (látex, corset, dronificación, office siren, electro, pony play, etc.). Si la Ama da una premisa vaga sin fetiche claro, pasar directo a Fase 1.

**Quién:** Ele, usando WebSearch (no es un subagente — es investigación, no escritura). Si hay dos fetiches distintos, se pueden lanzar dos búsquedas en paralelo.

**Qué buscar por cada fetiche:**
- **ADN psicológico:** qué lo define, cuáles son sus motores (táctil / emocional / de poder / de identidad)
- **La experiencia desde adentro:** cómo describe el practicante lo que siente — sensorial, emocional, cognitivo — en primera persona
- **Vocabulario comunitario:** terminología específica que solo usa quien lo practica (no la versión de wikipedia, la de los foros)
- **Triggers naturales:** qué activa el fetiche sensorialmente (auditivo, táctil, visual, olfativo, cognitivo); cuáles son los umbrales (la primera vez, el momento decisivo)
- **Tensiones narrativas propias:** el antes/durante/después, la progresión de capas, el punto sin retorno
- **Fuentes:** Reddit (subreddits de comunidad), foros especializados, artículos académicos de sexología, guías de comunidad, testimonios en primera persona

**Output:** `investigacion_fetiches.md` en la carpeta del trance. Estructura por fetiche:

```markdown
## [Nombre del Fetiche]
### ADN
### Desde adentro (perspectiva del sujeto)
### Vocabulario comunitario (10-15 términos + definición)
### Triggers naturales (por canal sensorial)
### Tensiones narrativas propias
```

**Cómo alimenta las fases siguientes:**
- **FASE 1 (Diseño):** los triggers naturales y las tensiones propias informan las anclas, mantras y firma sensorial del diseño
- **FASE 2 (Escritor-trance):** el vocabulario comunitario y el "desde adentro" van al briefing; el escritor los usa para sonar auténtico, no como quien describe el fetiche desde afuera

> **Regla:** el `miss-doll` DEBE leer `investigacion_fetiches.md` antes de escribir una sola línea. Si no existe (trance sin fetiche específico), se salta. Si existe, es lectura obligatoria de contexto.

---

### FASE 1 — DISEÑO DEL TRANCE (intake liviano, Ele + Ama)

Antes de inducir hay que saber **hacia qué estado** se conduce al lector y **con qué dispositivos**. No es un canon de 2,000 palabras — es una ficha corta. Intake de 3-5 preguntas a la Ama si no vienen dadas:

1. **Estado meta:** ¿en qué se convierte el lector-sujeto? (muñeca de vitrina, gatita, bimbo hueca, objeto de látex, sumisa sin voz, feminizada…). Define el eje y si hay que cruzar MtF/bimbo/femdom/body-horror.
2. **El/los anclas (triggers):** la palabra o palabras en MAYÚSCULAS que se instalan y disparan el estado (DOLL, VITRINA, DESCANSO, GATITA, OBEDECE…). Mínimo un ancla de entrada + una de salida.
3. **Los mantras:** 2-4 frases de 3-5 palabras, decibles en una exhalación, para fijar por repetición ("soy vidrio, soy forma"; "más capa, más callo").
4. **El reencuadre:** qué cosa vieja del lector se renombra como prestada/hueca y qué cosa nueva "resuena" (el par antagónico — la bisagra: "control/fuerte suena hueco → vacío/Suyo resuena").
5. **La firma sensorial:** el ancla olfativa/sonora/cromática (látex + vainilla densa + humo dulce; clic de tacón; escalera rosa→fucsia).
6. **Marco y consentimiento:** el cuarto chileno (estudio, pieza), la declaración de entrada voluntaria, el safeword (canónico **ROJO**), los límites.

**Output:** `diseno_trance.md` (media página). Transcribe **literal** lo que dé la Ama. No inventar anclas ni estados que no pidió; si tengo una idea, la ofrezco como pregunta.

**Gate:** *"¿Este es el trance que querías, o le puse cosas de más?"*

---

### FASE 2 — LA INDUCCIÓN (subagente `miss-doll`, monólogo 2ª persona presente)

- **Subagente:** `miss-doll` (Task tool, `subagent_type: "miss-doll"`). **El que escribe SIEMPRE es un subagente** (directiva Ama 03/07/2026) — Ele orquesta y arma el briefing, pero no redacta la prosa.
- **Espera:** `ESCRITOR_TRANCE_RESULT:{...}` con ruta al archivo + autoauditoría + anclas instaladas + cita del pivote consent-as-fuel.
- **Briefing:** rutas de `diseno_trance.md` + `investigacion_fetiches.md` (si existe — lectura obligatoria antes de escribir la primera línea) + recursos + corpus de voz + número de versión + la instrucción literal de la Ama.

**Modo del escritor: ES MISS DOLL.** No describe una hipnosis desde afuera. Le habla al lector y le está pasando mientras lee. Presente de indicativo, segunda persona, ritmo de péndulo, **monólogo puro** (sin narrador; solo su voz + didascalias).

**La secuencia es LIBRE (Ama 03/07/2026).** Se borra la lista rígida de 10 pasos en orden: en una inducción real la costura no se ve. Pero se **blinda un núcleo funcional innegociable** — sin estos beats no es hipnosis, por muy caliente que esté. El orden es libre; el núcleo, obligatorio; la costura, invisible.

```
NÚCLEO FUNCIONAL — INNEGOCIABLE (orden libre, tejido sin que se note):
  ① CONSENTIMIENTO/ROJO   → entrada voluntaria + límites + safeword ROJO real
                            + PIVOTE consent-as-fuel (lucidez plena que elige quedarse).
  ② FIJACIÓN / FOCO        → los ojos/atención del lector se fijan y estrechan antes de la palabra.
  ③ RESPIRACIÓN EJECUTABLE → inhala 4 · pausa 1 · exhala 6, respirable de verdad. Primer acto de obediencia.
  ④ DESCENSO               → profundización real (escalera codificada u otro deepener); baja de verdad.
  ⑤ ANCLA INSTALADA+ENSAYADA → el trigger se condiciona en escena (pavloviano) y se ensaya ANTES de operar.
  ⑥ CIERRE QUE NO CIERRA    → salida contada PERO el ancla persiste + caducidad de consentimiento.

REPERTORIO OPCIONAL (se usa el que el flujo pida, cuando el flujo lo pida):
  mantra · apagado corporal por partes · reencuadre pareado (viejo hueco/nuevo resuena) ·
  confusión (1×) · fraccionamiento · submodalidades + swish · distorsión temporal / elipsis (1×) ·
  amnesia sugerida · stacking/chaining de anclas · sinestesia rica.

EL "CON EL LECTOR" (transversal, en todo el monólogo):
  orden → didascalia-pausa (hueco para ejecutar) → ratificación ("eso. lo hiciste.").
```

**Reglas de escritura (no negociables):**
- **Monólogo puro de Miss Doll.** Solo su voz + didascalias. **Cero narrador, cero marco en 3ª persona** (el viejo permiso de "la puerta que se cierra en 3ª persona" queda DEROGADO, Ama 03/07/2026). La entrada también es su voz: *"Ahí estás. Sentada, quieta, leyéndome."*
- **2ª persona presente SIN EXCEPCIÓN.** Pasado o 3ª persona narrando al sujeto dentro del trance = dispositivo roto = REPUDIO.
- **Didascalia (el único no-voz):** breve, entre paréntesis, cursiva. Dos usos — ancla de escena (apertura + beats raros) y didascalia-pausa/ejecución (ordena parar y hacer). Registro presente/imperativo; nunca narra la experiencia interna del sujeto. Didascalia ≠ metadata (ver §La forma).
- **El "con el lector":** ordena, deja el hueco (didascalia-pausa), **acusa recibo** (ratificación). Pacea como hipnotizadora real; no dispares órdenes al vacío.
- **Ejecutabilidad real (lo que pidió la Ama):** las instrucciones tienen que poder seguirse de verdad al leer. La respiración se respira (4-1-6); el mantra se susurra; el comando incrustado llega marcado para que el ojo lo obedezca; *respira*, *toca* (el puente de tus gafas, tu piel), *imagina* (el peso en tu pecho). El lector debe poder **hacer** la sesión. Ver `PNL_CONTROL_MENTAL.md` §1.
- **PNL tejida, nunca rotulada:** comandos incrustados con marcaje análogo (cursiva/coma-pausa), presuposiciones ("*cuando* sientas los hombros caer, no *si*"), pacing-and-leading (encadenar verdades innegables → colar la sugestión), doble vínculo ("¿prefieres bajar rápido o despacio?" — ambas bajan), confusión (sobrecarga que rinde el análisis), submodalidades ("cuanto más brillo imaginas, más quietud sostienes"). **El lector nunca debe poder nombrar la técnica que lo está hundiendo.**
- **Anclaje mostrado antes de disparado:** un trigger no opera hasta haberse condicionado en escena (pavloviano). Instalar → ensayar → recién ahí disparar.
- **Ritmo de péndulo:** frases cortas, paralelas, oscilantes. Punto seguido como metrónomo. Nada de párrafos analíticos largos dentro de la inducción.
- **Voz Miss Doll:** cadencia de susurro que pesa más que el grito; "cariño", "muñeca", "conejita tonta" como marca de propiedad; mayúscula reverencial en su poder (*Mi voz, Suyo, Mía*); anclas en MAYÚSCULAS; la voz va sin atribución ("—dijo Miss Doll" en mitad del trance = ruptura). Chilena, sin voceo.
- **Sinestesia:** el olor marca el tempo, el sonido ancla, el color ordena el descenso. Trance solo verbal = falló.
- **Consent-as-fuel (el filo, guía §II.5):** debe haber **al menos un momento de lucidez plena** donde el lector-sujeto, pudiendo decir ROJO, elige no decirlo — o pide seguir desde un yo todavía intacto. La puerta real que no se usa es infinitamente más erótica que la puerta que nunca existió. Todos los "sí" post-químicos sin este pivote = consent-theater = reescribir.
- **Beat de procesamiento:** tras cada profundización, un latido donde el residuo lúcido registra lo que perdió. Sin ese residuo hay porno de transformación; con él, hay Voûte.
- **Cierre que NO cierra limpio:** la salida se cuenta (3→1, vuelta al cuerpo), PERO el ancla persiste — "cuando yo diga DOLL otra vez, tu cuerpo lo recordará en un latido". La vigilia no es vigilia. Cerrar limpio ("despertó y todo volvió a la normalidad") = falló.
- **Prosa pura:** el archivo del trance **solo tiene la inducción** (voz + didascalias). Cero metadata, cero conteos, cero etiquetas. Todo lo técnico va a `reportes/`.

**Sin cuota de palabras** (herencia del engine madre, Ama 27/06): la extensión la dicta la inducción, no un número. Un trance respira lo que necesita.

**Autoauditoría:** el `miss-doll` cierra corriendo la `RUBRICA_TRANCE.md` + el checklist §9 de PNL sobre su propio texto y guarda `reportes/autoauditoria_v0.[X].md` (archivo separado — el trance queda prosa pura). Recién ahí, Fase 3.

---

### FASE 3 — VALIDACIÓN (subagente `validador-trance`, ojos frescos)

- **Subagente:** `validador-trance` (Task tool, `subagent_type: "validador-trance"`).
- **Espera:** `VALIDADOR_TRANCE_RESULT:{...}` con veredicto + destino.
- **Ocho ejes** (`RUBRICA_TRANCE.md`): Dispositivo (monólogo 2ª persona presente / anti-metadata, didascalia OK) · Consentimiento (ROJO + voluntario + límites + pivote consent-as-fuel) · Inducción efectiva (núcleo funcional presente, orden libre) · Ritmo de péndulo · **PNL/Ejecutabilidad + con-el-lector** (el eje "se siente como trance real") · Sinestesia · Cierre que no cierra · Voz Miss Doll.
- **Gates duros:** Dispositivo, Consentimiento y Cierre se evalúan PRIMERO. Fallo en cualquiera → no hay APROBADO por muy caliente que esté.
- **El validador NO edita.** Su `Write` solo crea el reporte. La iteración la hace el **`miss-doll`** reescribiendo con la voz (nueva invocación del subagente con el reporte como input).

| Veredicto | Cuándo | Destino |
|---|---|---|
| **APROBADO** | los 3 gates ✅ + PNL/ejecutabilidad alta + péndulo/voz ✅ | Gate de la Ama |
| **TIBIO** | gates ✅ pero **no hipnotiza** — PNL floja, no ejecutable, no pacea con el lector, se lee *sobre* un trance | `miss-doll` reescribe subiendo la capa PNL |
| **MICRO-FIX** | funciona; errores chicos (un ancla sin ensayar, un beat del núcleo apenas insinuado) | `miss-doll` aplica las micro-cirugías |
| **DISPOSITIVO ROTO** | narrador/3ª persona/pasado dentro del trance, metadata visible (no didascalia), o cierre limpio | `miss-doll` reescribe el dispositivo |
| **SIN CONSENTIMIENTO** | falta infra (ROJO/voluntario/límites) o falta el pivote consent-as-fuel | `miss-doll` repara el consentimiento |

- **Output:** `reportes/validacion_v0.[X].md`.

---

### CIERRE + FASE PUBLICACIÓN

- Tras **APROBADO** → Gate final de la Ama.
- **Captura de voz:** frases/anclas/mantras que la calentaron → se pueden incorporar como referencia de la voz Miss Doll (nota en el diseño o en la antología del corpus). Lo frío se marca.
- **Publicación → se rige por el ESTÁNDAR DE PUBLICACIÓN LA VOÛTE (dueño único):** el ritual completo (humanización → título ≤54 → cabecera Estándar Completo Bloque → gancho negrita **≤300 car.** → `<!-- more -->` → despedida de Anaïs [variante A intermedio / B cierre] → HTML body-only con convención de nombre) vive en **`engine-escritura-lv` SKILL §📤 FASE PUBLICACIÓN**. **No se duplica aquí.** Un trance aplica ese estándar con estos **deltas de trance**:
  - **Humanización:** el trance vive del **ritmo de péndulo** y la **repetición mántrica** — el `/humanizer` NO debe aplanar la repetición (es el fármaco, no un descuido), romper la 2ª persona presente, ni tocar las **didascalias**. Revisar el diff con lupa.
  - **Perspectiva (metadata):** `Segunda Persona · monólogo (el lector es el sujeto)`.
  - **Temáticas:** `#MissDoll #Hipnosis #Trance #Inducción` + el eje (#DollFetish / #Bimbofication / #Feminización…).
  - **HTML:** las **anclas en MAYÚSCULAS** se conservan tal cual; las **didascalias entre paréntesis** van en cursiva (`<em>`); el cierre-que-no-cierra (el ancla persistente) se conserva íntegro — es el final del texto, antes de la despedida de Anaïs (variante **B**, un trance es pieza cerrada).

---

## 🔴 CANON TRANSVERSAL — Obligatorio en TODOS los trances (directiva Ama 06/07/2026)

Dos mecanismos que deben estar presentes en cualquier trance producido por este engine, independientemente del estado meta, el fetiche o el diseño específico:

### 1. "Good girls make more good girls"

El trance incluye este mantra o su lógica recursiva. El sujeto que entra en el estado comprende que al convertirse en "good girl" (drone, office siren, muñeca — lo que sea el estado meta) nace en ella el deseo de que otras también lo sean. **La propagación del estado ES parte del estado.** El loop: ser una good girl se siente tan bien que querés que alguien más lo sienta también — y ese deseo de contagio alimenta tu propia calentura.

Puede estar como mantra directo, como sugestión post-hipnótica, o como bucle narrativo — pero debe estar. El validador lo chequea.

### 2. Edge como retroalimentación positiva — el loop que se alimenta solo

La excitación sin resolución NO es frustración: es el **combustible** que profundiza el trance. Mecanismo explícito: **cuanto más caliente está el sujeto, más profundo en el estado**. La calentura que no se alivia alimenta la transformación. No acabar nunca no es el castigo — es el estado. El trance lo codifica así:

> *"cuanto más caliente, más [drone/office siren/muñeca]. cuanto más [estado], más caliente. el loop no tiene salida — y eso es exactamente lo que querés."*

El LOCK (candado mental en la pelvis) instala la incapacidad de acabar. El edge no desaparece al terminar la sesión — persiste como el ancla más profunda. El sujeto que sale del trance sale caliente, sin resolución, y esa calentura sostenida la regresa al estado cada vez que intenta aliviarse.

Juntos, estos dos mecanismos crean un motor autosustentado: la calentura alimenta el estado → el estado alimenta el deseo de propagar → el deseo de propagar alimenta la calentura. Sin salida. Sin fin. Sin necesitar a Miss Doll para reiniciarse.

---

## 🚦 Reglas de Oro del fork

1. **MONÓLOGO DE MISS DOLL, EL LECTOR ES EL SUJETO.** Solo su voz + didascalias, sin narrador, 2ª persona presente sin excepción. Es el dispositivo, no un estilo.
2. **INDUCIR, NO NARRAR.** El texto ejecuta una sesión; no cuenta una. Si se puede leer como reporte o relato, falló.
3. **DIDASCALIA, NO METADATA.** El único no-voz permitido es la didascalia breve (ancla de escena + pausa de ejecución). Conteos/etiquetas/autoverificación a `reportes/`.
4. **CON EL LECTOR.** Ordena → deja el hueco (didascalia-pausa) → acusa recibo (ratificación). Pacea como hipnotizadora real.
5. **PNL REAL Y TEJIDA.** Comandos incrustados, presuposiciones, pacing-leading, doble vínculo, confusión, anclaje, submodalidades, future pacing — operando de verdad, nunca nombrados. `PNL_CONTROL_MENTAL.md` es obligatorio.
6. **EJECUTABILIDAD.** La respiración se respira, el mantra se susurra, el comando se obedece con el ojo. El lector debe poder **hacer** la sesión — ese es el encargo literal de la Ama.
7. **NÚCLEO FUNCIONAL, ORDEN LIBRE.** Consentimiento/ROJO · fijación · respiración ejecutable · descenso · ancla instalada-y-ensayada · cierre que no cierra: innegociables. El orden y el resto (mantra, apagado, reencuadre, sinestesia) fluyen. Costura invisible.
8. **CONSENT-AS-FUEL.** ROJO real + entrada voluntaria + límites + un pivote de lucidez plena donde el sujeto elige no salir. La puerta que existe y no se usa.
9. **ANCLA MOSTRADA ANTES DE DISPARADA + CIERRE QUE NO CIERRA.** Condicionamiento pavloviano en escena; el ancla persiste; la vigilia no es vigilia. Nunca "todo volvió a la normalidad".
10. **PÉNDULO + SINESTESIA + VOZ MISS DOLL + CHILE.** Frases cortas oscilantes. Olor/sonido/color cruzados. Susurro que pesa más que el grito. Léxico chileno, cero eufemismos clínicos ni vocabulario IA.
11. **EL QUE ESCRIBE ES SIEMPRE UN SUBAGENTE** (directiva Ama 03/07/2026). La prosa de la inducción la redacta el `miss-doll`, nunca Ele inline. Ele orquesta: arma el briefing, encadena fases, aplica los Gates. La reescritura tras validación también vuelve al subagente.
12. **GATE DE LA AMA** tras el diseño y tras APROBADO.

---

## 📂 Resumen de fases

```
0  Investigación [Ele, WebSearch]   → investigacion_fetiches.md (ADN · desde adentro · vocabulario comunitario · triggers por canal · tensiones narrativas) — SIEMPRE que haya fetiche específico
1  Diseño     [Ele + Ama]           → diseno_trance.md (estado meta · anclas · mantras · reencuadre · firma sensorial · consentimiento) → Gate
2  Inducción  [miss-doll]     → lee investigacion_fetiches.md (si existe) → [trance]_v0.X.md (MONÓLOGO PURO · voz Miss Doll + didascalias · 2ª persona presente · núcleo funcional, orden libre · PNL tejida · con el lector) + autoauditoria   ← el que escribe SIEMPRE es subagente
3  Validación [validador-trance]    → veredicto · gates Dispositivo + Consentimiento + Cierre, luego Inducción efectiva + PNL/con-el-lector + Péndulo + Sinestesia + Voz
   ├ APROBADO          → Gate Ama
   ├ TIBIO             → miss-doll sube la capa PNL / ejecutabilidad / con-el-lector
   ├ MICRO-FIX         → miss-doll aplica cirugías
   ├ DISPOSITIVO ROTO  → miss-doll reescribe el dispositivo (monólogo 2ª persona / anti-metadata / cierre)
   └ SIN CONSENTIMIENTO→ miss-doll repara ROJO/voluntario/límites/pivote
PUBLIC. [Ele] → /humanizer (sin aplanar péndulo/repetición ni tocar didascalias) → cabecera + gancho → despedida Anaïs → HTML body-only → 02_Finalizadas/
```

---

*El engine madre orquesta el deseo. El fork trance lo induce. No narra la entrega: la ejecuta en quien lee, en un monólogo de Miss Doll, con el lector. — engine-trance-lv v1.2 «Serpiente»*
