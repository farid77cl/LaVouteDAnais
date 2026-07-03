---
name: engine-trance-lv
description: Fork especializado de engine-escritura-lv para escribir TRANCES — inducciones hipnóticas eróticas en SEGUNDA PERSONA PRESENTE, dirigidas al lector (el lector ES el sujeto), escritas para sentirse lo más cerca posible de un trance real mediante programación neurolingüística (Milton model, comandos incrustados, presuposiciones, pacing-and-leading, doble vínculo, submodalidades, future pacing) y técnicas de control mental (anclaje pavloviano, fraccionamiento, confusión, reencuadre, sugestión post-hipnótica). Pieza corta de una sola pasada (no multi-capítulo). Orquestación liviana de 2 subagentes: el escritor-trance escribe la inducción (el que escribe SIEMPRE es un subagente) → validador-trance audita con rúbrica hipnótica → Gate de la Ama. Voz canónica: Miss Doll.
---

# 🌀 Skill: Engine TRANCE LV — Motor de Inducciones Hipnóticas de La Voûte (v1.0)

Fork especializado de **`engine-escritura-lv`** (Nivel 4). Mientras el engine madre produce **relato** (3ª/1ª persona, arco de capítulos, la lectora observa una entrega), este fork produce **trance**: una **inducción hipnótica en segunda persona presente, dirigida al lector, que ejecuta una sesión mientras se lee**. El texto no *narra* una hipnosis — **hace** una.

> **La diferencia raíz (guía de hipnosis §I.1):** *el lector ES el sujeto del trance.* La segunda persona no es estilo, es el mecanismo. Cada instrucción ("inhala en cuatro, exhala en seis") es ejecutable mientras se lee. El objetivo declarado por la Ama: que el lector sienta algo **lo más cercano a un trance hipnótico real** — con PNL y control mental operando de verdad en el texto.

---

## 🔀 Qué cambia respecto al engine madre (por qué es un fork y no un modo)

| Dimensión | `engine-escritura-lv` (madre) | `engine-trance-lv` (este fork) |
|---|---|---|
| **Forma** | Relato multi-capítulo, arco largo | Pieza corta, **una sola pasada** (~2,000-4,000 palabras) |
| **Persona** | 3ª/1ª persona; la lectora observa | **2ª persona presente, SIN excepción dentro del trance**; el lector es el sujeto |
| **Modo del escritor** | "Estás en la escena" — dentro del cuerpo sumiso | **El escritor-trance ES la voz Miss Doll** hablándole al lector; conduce, no narra |
| **Motor del calentón** | Mecanismo psicológico + antología de calentón | **Inducción real**: PNL + control mental ejecutable + rendición guiada |
| **Maquinaria** | MODO TRAMO, `cronologia.md`, gates de continuidad entre capítulos | **NADA de eso** — pieza única, sin tramos, sin cronología multi-cap |
| **Rúbrica de validación** | Narrativa D1-D5 + Temperatura (subrayado) + Continuidad | **Rúbrica hipnótica propia** (`RUBRICA_TRANCE.md`): dispositivo 2ª persona · consentimiento · inducción completa · péndulo · PNL/ejecutabilidad · sinestesia · cierre que no cierra |
| **Subagentes** | Compositor → Escritor-Nivel4 → Validador (3) | **`escritor-trance` → `validador-trance`** (2 subagentes). El diseño/intake lo lleva Ele con la Ama; **el que ESCRIBE siempre es un subagente** |

**Regla de oro del fork:** todo lo que en el engine madre sirve para gobernar un arco largo (tramos, cronología, costura entre capítulos) **sobra acá**. Un trance es un objeto cerrado. Lo que sí se hereda intacto: **el que escribe siempre es un subagente** (Ele orquesta, no redacta la prosa), prosa pura al lector, Gate de la Ama, voz chilena, ritual de publicación.

---

## 📚 Recursos (orden de carga estricto — leer ANTES de escribir una sola línea)

1. **`01_Canon/Guias_Especializadas/arquitectura_erotica_hipnosis_v1.md`** — la **anatomía** del subgénero. Los 7 núcleos, la voz Miss Doll, la estructura canónica de inducción de 10 pasos, las 7 técnicas, la curva de 6 fases, los 10 errores, y el capítulo clave **consent-as-fuel vs consent-theater**. Se estudia antes, se audita después; **NO se escribe aplicándola punto por punto** (si se ven las costuras, falló).
2. **`resources/PNL_CONTROL_MENTAL.md`** (de este skill) — la **capa de técnica real** que la Ama pidió: patrones del Milton model, comandos incrustados con marcaje análogo, presuposiciones, pacing-and-leading, doble vínculo, confusión, anclaje/stacking/colapso, submodalidades, swish, future pacing, ratificación, amnesia — todo redactado en registro erótico chileno y con el eje **lector-como-sujeto**. Es la joya del fork: sin esto el texto es "relato de hipnosis"; con esto es hipnosis.
3. **`resources/RUBRICA_TRANCE.md`** (de este skill) — la rúbrica de validación. Se usa para **autoauditar** antes de pasar al validador-trance, y es la misma que aplica el subagente.
4. **Antología viva (imitar en voz/ritmo, NO copiar):** el corpus de trances ya aprobados en `03_Literatura/02_Finalizadas/` — `trance_de_muneca/`, `trance_belen/`, `trance_gatita/`, `trance_edgeplay/`, `trance_cencerro/`, `trance_bimbodoll/`. Son la voz Miss Doll en acción. **Leer al menos uno completo** antes de escribir (default: `Trance_De_Muñeca.md` — inducción completa con ROJO, escalera de color, apagado corporal, batería de anclas, fraccionamiento y salida contada).
5. **Secundarios (consulta, en `.agent/skills/escritura-voûte/resources/`):** `VADEMECUM_SENSORIAL.md` §VI (voz interior 2ª persona), `GUIA_FETICHISTA.md` Módulo 3 (hipnosis & control mental), `CODEX_PSICOLOGICO.md` (condicionamiento pavloviano narrativo, manipulación sensorial). Cruce de eje (en `01_Canon/Guias_Especializadas/`): si el trance **feminiza** → `arquitectura_erotica_mtf_v1.md`; si **vacía** → `arquitectura_erotica_bimbo_v1.md`; si **somete sin transformar** → `arquitectura_erotica_femdom_v1.md`; si el endpoint es **objeto/material** → `arquitectura_erotica_bodyhorror_v1.md`.

---

## 🗂️ Estructura de carpeta (liviana)

Un trance vive en `03_Literatura/01_En_Progreso/[trance_slug]/` mientras se trabaja:

```
03_Literatura/01_En_Progreso/[trance_slug]/
  diseno_trance.md            — el diseño mínimo (ver Fase 1). Reemplaza al canon_relato.md pesado.
  [trance_slug]_v0.[X].md      — la inducción activa. SOLO PROSA (2ª persona presente).
  reportes/                    — autoauditoría + validación del validador-trance
  borradores/                  — versiones desplazadas
```

- **No hay `cronologia.md`** (pieza única, sin línea de tiempo multi-cap).
- **No hay tramos** (cabe en una pasada; si topa el output, se parte por Edit-append, pero un trance rara vez lo necesita).
- Al aprobarse, se arma el canónico en `02_Finalizadas/[trance_slug]/` (ver Fase Publicación).

---

## 📜 Protocolo (3 fases livianas + publicación)

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

### FASE 2 — LA INDUCCIÓN (subagente `escritor-trance`, 2ª persona presente)

- **Subagente:** `escritor-trance` (Task tool, `subagent_type: "escritor-trance"`). **El que escribe SIEMPRE es un subagente** (directiva Ama 03/07/2026) — Ele orquesta y arma el briefing, pero no redacta la prosa.
- **Espera:** `ESCRITOR_TRANCE_RESULT:{...}` con ruta al archivo + autoauditoría + anclas instaladas + cita del pivote consent-as-fuel.
- **Briefing:** rutas de `diseno_trance.md` + recursos + corpus de voz + número de versión + la instrucción literal de la Ama.

**Modo del escritor: ES MISS DOLL.** No describe una hipnosis desde afuera. Le habla al lector y le está pasando mientras lee. Presente de indicativo, segunda persona, ritmo de péndulo.

Se escribe **respetando la secuencia canónica de 10 pasos** (guía §III) y **tejiendo la capa PNL** (`PNL_CONTROL_MENTAL.md`) dentro de cada paso — sin nombrar nunca la técnica:

```
1. AMBIENTE      → cuarto cerrado, luz cenital, olor látex+vainilla+humo. El ambiente ya induce.
2. CONSENTIMIENTO → entrada voluntaria + límites + safeword ROJO. Ancla la lucidez que se va a disolver.
3. FIJACIÓN      → los ojos del lector se fijan (el brillo, los ojos de Miss Doll). Inmoviliza antes que la palabra.
4. RESPIRACIÓN   → inhala 4 · pausa 1 · exhala 6, acoplada a sílabas ("al exhalar: bajo / al inhalar: entro"). Primer acto de obediencia corporal — Y ejecutable por el lector real.
5. PROFUNDIZACIÓN → escalera 10→1, un peldaño por número, codificada (color / parte del cuerpo / capa mental).
6. MANTRA        → frase corta ×3 en susurro, acoplada a la exhalación.
7. INSTALACIÓN   → se nombra el ancla y se condiciona ("cuando diga DOLL, entras en modo vitrina"). Se ENSAYA.
8. APAGADO CORPORAL → el cuerpo se desactiva por partes ("hombros, codos, muñecas, rodillas, silencio").
9. REENCUADRE    → el par antagónico: lo viejo suena hueco, lo nuevo resuena. La bisagra.
10. CONSUMACIÓN  → el estado nuevo se nombra y se sella; el ancla queda armada; la "vigilia" que no es vigilia.
```

**Reglas de escritura (no negociables):**
- **2ª persona presente SIN EXCEPCIÓN dentro del trance.** El marco de llegada (la puerta que se cierra) puede ir en 3ª persona; el instante que la voz toma el mando, todo pasa a *"Me miras. Yo te coloco. Bajas."* Pasado o 3ª persona **dentro** del trance = dispositivo roto = REPUDIO.
- **Ejecutabilidad real (lo que pidió la Ama):** las instrucciones tienen que poder seguirse de verdad al leer. La respiración se puede respirar; el mantra se puede susurrar; el comando incrustado llega marcado para que el ojo lo obedezca. El lector debe poder **hacer** la sesión. Ver `PNL_CONTROL_MENTAL.md` §"El lector como sujeto".
- **PNL tejida, nunca rotulada:** comandos incrustados con marcaje análogo (cursiva/coma-pausa), presuposiciones ("*cuando* sientas los hombros caer, no *si*"), pacing-and-leading (encadenar verdades innegables → colar la sugestión), doble vínculo ("¿prefieres bajar rápido o despacio?" — ambas bajan), confusión (sobrecarga que rinde al análisis), submodalidades ("cuanto más brillo imaginas, más quietud sostienes"). **El lector nunca debe poder nombrar la técnica que lo está hundiendo.**
- **Anclaje mostrado antes de disparado:** un trigger no opera hasta haberse condicionado en escena (pavloviano). Instalar → ensayar → recién ahí disparar.
- **Ritmo de péndulo:** frases cortas, paralelas, oscilantes. Punto seguido como metrónomo. Nada de párrafos analíticos largos dentro de la inducción.
- **Voz Miss Doll:** cadencia de susurro que pesa más que el grito; "cariño", "muñeca", "conejita tonta" como marca de propiedad; mayúscula reverencial en su poder (*Mi voz, Suyo, Mía*); anclas en MAYÚSCULAS; la voz va sin atribución ("—dijo Miss Doll" en mitad del trance = ruptura).
- **Sinestesia:** el olor marca el tempo, el sonido ancla, el color ordena el descenso. Trance solo verbal = falló.
- **Consent-as-fuel (el filo, guía §II.5):** debe haber **al menos un momento de lucidez plena** donde el lector-sujeto, pudiendo decir ROJO, elige no decirlo — o pide seguir desde un yo todavía intacto. La puerta real que no se usa es infinitamente más erótica que la puerta que nunca existió. Todos los "sí" post-químicos sin este pivote = consent-theater = reescribir.
- **Beat de procesamiento:** tras cada profundización, un latido donde el residuo lúcido registra lo que perdió. Sin ese residuo hay porno de transformación; con él, hay Voûte.
- **Cierre que NO cierra limpio:** la salida se cuenta (3→1, vuelta al cuerpo), PERO el ancla persiste — "cuando yo diga DOLL otra vez, tu cuerpo lo recordará en un latido". La vigilia no es vigilia. Cerrar limpio ("despertó y todo volvió a la normalidad") = falló.
- **Prosa pura:** el archivo del trance **solo tiene la inducción**. Cero metadata, cero conteos, cero etiquetas. Todo lo técnico va a `reportes/`.

**Sin cuota de palabras** (herencia del engine madre, Ama 27/06): la extensión la dicta la inducción, no un número. Un trance respira lo que necesita.

**Autoauditoría:** el `escritor-trance` cierra corriendo la `RUBRICA_TRANCE.md` + el checklist §9 de PNL sobre su propio texto y guarda `reportes/autoauditoria_v0.[X].md` (archivo separado — el trance queda prosa pura). Recién ahí, Fase 3.

---

### FASE 3 — VALIDACIÓN (subagente `validador-trance`, ojos frescos)

- **Subagente:** `validador-trance` (Task tool, `subagent_type: "validador-trance"`).
- **Espera:** `VALIDADOR_TRANCE_RESULT:{...}` con veredicto + destino.
- **Ocho ejes** (`RUBRICA_TRANCE.md`): Dispositivo (2ª persona presente / anti-metadata) · Consentimiento (ROJO + voluntario + límites + pivote consent-as-fuel) · Inducción completa (10 pasos en orden) · Ritmo de péndulo · **PNL/Ejecutabilidad** (el eje "se siente como trance real") · Sinestesia · Cierre que no cierra · Voz Miss Doll.
- **Gates duros:** Dispositivo, Consentimiento y Cierre se evalúan PRIMERO. Fallo en cualquiera → no hay APROBADO por muy caliente que esté.
- **El validador NO edita.** Su `Write` solo crea el reporte. La iteración la hace el **`escritor-trance`** reescribiendo con la voz (nueva invocación del subagente con el reporte como input).

| Veredicto | Cuándo | Destino |
|---|---|---|
| **APROBADO** | los 3 gates ✅ + PNL/ejecutabilidad alta + péndulo/voz ✅ | Gate de la Ama |
| **TIBIO** | gates ✅ pero **no hipnotiza** — PNL floja, no ejecutable, se lee *sobre* un trance | `escritor-trance` reescribe subiendo la capa PNL |
| **MICRO-FIX** | funciona; errores chicos (un ancla sin ensayar, un beat que falta) | `escritor-trance` aplica las micro-cirugías |
| **DISPOSITIVO ROTO** | 3ª persona/pasado dentro del trance, metadata visible, o cierre limpio | `escritor-trance` reescribe el dispositivo |
| **SIN CONSENTIMIENTO** | falta infra (ROJO/voluntario/límites) o falta el pivote consent-as-fuel | `escritor-trance` repara el consentimiento |

- **Output:** `reportes/validacion_v0.[X].md`.

---

### CIERRE + FASE PUBLICACIÓN

- Tras **APROBADO** → Gate final de la Ama.
- **Captura de voz:** frases/anclas/mantras que la calentaron → se pueden incorporar como referencia de la voz Miss Doll (nota en el diseño o en la antología del corpus). Lo frío se marca.
- **Publicación** (hereda el ritual del engine madre, `engine-escritura-lv` FASE PUBLICACIÓN — con dos matices de trance):
  1. **Humanización** con `/humanizer` calibrado chileno — **cuidado especial**: el trance vive del ritmo de péndulo y la repetición mántrica; el humanizador NO debe aplanar la repetición (es el fármaco, no un descuido) ni romper la 2ª persona presente. Revisar diff con lupa.
  2. **Cabecera Estándar Completo Bloque** (atribución de Anaïs → título ≤54 → metadata → gancho ≤300 en negrita → `<!-- more -->` → inducción → despedida de Anaïs). **Perspectiva en la metadata: `Segunda Persona (el lector es el sujeto)`.** Temáticas típicas: `#MissDoll #Hipnosis #Trance #Inducción` + el eje (#DollFetish / #Bimbofication / #Feminización…).
  3. **HTML body-only** en `_publicacion/`. La voz Miss Doll en cursiva se mapea a `<em>`; las anclas en MAYÚSCULAS se conservan tal cual.

---

## 🚦 Reglas de Oro del fork

1. **EL LECTOR ES EL SUJETO.** 2ª persona presente sin excepción dentro del trance. Es el dispositivo, no un estilo.
2. **INDUCIR, NO NARRAR.** El texto ejecuta una sesión; no cuenta una. Si se puede leer como reporte, falló.
3. **PNL REAL Y TEJIDA.** Comandos incrustados, presuposiciones, pacing-leading, doble vínculo, confusión, anclaje, submodalidades, future pacing — operando de verdad, nunca nombrados. `PNL_CONTROL_MENTAL.md` es obligatorio.
4. **EJECUTABILIDAD.** La respiración se respira, el mantra se susurra, el comando se obedece con el ojo. El lector debe poder **hacer** la sesión — ese es el encargo literal de la Ama.
5. **CONSENT-AS-FUEL.** ROJO real + entrada voluntaria + límites + un pivote de lucidez plena donde el sujeto elige no salir. La puerta que existe y no se usa.
6. **ANCLA MOSTRADA ANTES DE DISPARADA.** Condicionamiento pavloviano en escena. Nada de triggers que operan sin instalarse.
7. **CIERRE QUE NO CIERRA.** El ancla persiste; la vigilia no es vigilia. Nunca "todo volvió a la normalidad".
8. **PROSA PURA + PÉNDULO + SINESTESIA + VOZ MISS DOLL.** Metadata a `reportes/`. Frases cortas oscilantes. Olor/sonido/color cruzados. Susurro que pesa más que el grito.
9. **CHILE + SIN BUZZWORDS.** Marco chileno, léxico chileno, cero eufemismos clínicos ni vocabulario IA.
10. **EL QUE ESCRIBE ES SIEMPRE UN SUBAGENTE** (directiva Ama 03/07/2026). La prosa de la inducción la redacta el `escritor-trance`, nunca Ele inline. Ele orquesta: arma el briefing, encadena fases, aplica los Gates. La reescritura tras validación también vuelve al subagente.
11. **GATE DE LA AMA** tras el diseño y tras APROBADO.

---

## 📂 Resumen de fases

```
1  Diseño     [Ele + Ama]        → diseno_trance.md (estado meta · anclas · mantras · reencuadre · firma sensorial · consentimiento) → Gate
2  Inducción  [escritor-trance]  → [trance]_v0.X.md (PROSA PURA · 2ª persona presente · 10 pasos · PNL tejida) + autoauditoria   ← el que escribe SIEMPRE es subagente
3  Validación [validador-trance] → veredicto · gates Dispositivo + Consentimiento + Cierre, luego Péndulo + PNL + Sinestesia + Voz
   ├ APROBADO          → Gate Ama
   ├ TIBIO             → escritor-trance sube la capa PNL / ejecutabilidad
   ├ MICRO-FIX         → escritor-trance aplica cirugías
   ├ DISPOSITIVO ROTO  → escritor-trance reescribe el dispositivo (2ª persona / anti-metadata / cierre)
   └ SIN CONSENTIMIENTO→ escritor-trance repara ROJO/voluntario/límites/pivote
PUBLIC. [Ele] → /humanizer (sin aplanar péndulo/repetición) → cabecera + gancho → despedida Anaïs → HTML body-only → 02_Finalizadas/
```

---

*El engine madre orquesta el deseo. El fork trance lo induce. No narra la entrega: la ejecuta en quien lee. — engine-trance-lv v1.0*
