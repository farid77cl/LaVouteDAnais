---
name: engine-escritura-lv
description: Motor de Escritura La Voûte (engine-escritura-lv) — Orquestador Maestro v4.8 (Nivel 4 + Investigación). Cuatro subagentes: Investigador → Compositor → Escritor-Nivel4 → Validador. La Fase 0 de Investigación (borrada en el colapso 9→3 del v4.7) vuelve para traer el TONO y qué CALIENTA del tema, más los Motivos Permanentes y la Curva de Resistencia; y la Temperatura del Validador pasa de conteo de subrayables a GATE medido (¿es erótico? ¿calienta?). Canon mínimo (canon_relato.md ~2,000 palabras), voz persistente (voz_autoral.md), antología textual de calentón (no listas M1-M17), prosa pura al lector con metadata en archivo separado, y Validador sin Editor (temperatura baja → Escritor, no edición que suaviza).
---

# 🧠 Skill: Engine Escritura LV — Orquestador Maestro de La Voûte (v4.8 · Nivel 4 + Investigación)

Esta skill permite al agente actuar como el **Agente Orquestador**, el director técnico supremo del flujo de producción literaria de La Voûte.

> **v4.7 (Nivel 4) — Por qué este rediseño:** El v4.5/v4.6 producía ~10,000+ palabras de canon (concepto + arco + personajes + mapa erótico general + mapa por capítulo + mecanismo de calentón por capítulo) ANTES de escribir una línea, y mantenía un bucle Editor↔Crítico que **sanitizaba el texto con cada iteración** (caso documentado: `la_piel_que_diseno` Cap 2 v1.7.1 con 9.0 de Crítico que nunca calentó). Nivel 4 destila a lo esencial: **un solo documento de canon, voz persistente entre capítulos, antología textual en vez de mecanismos abstractos, y eliminación del Editor.** Validado por la Ama con `esposa_servidumbre` Cap 1 (28/05/2026): *"me gusta mucho más de lo que he leído en harto tiempo."* Ver `01_Canon/REDISENO_ENGINE_ESCRITURA_v4.6.md` para el diagnóstico completo.

> **v4.8 (22/07/2026) — Por qué este parche:** la Ama diagnosticó que *"siempre caemos en los mismos problemas"* y que *"antes había una fase previa de investigación"*. Al contar sus notas de corrección de **seis relatos distintos**, los reclamos repetidos resultaron ser cinco, y todos con la misma raíz: el colapso 9→3 borró la investigación **sin reemplazarla** (la palabra no aparecía en ningún subagente). v4.8 devuelve la **Fase 0** —cuyo corazón es *"ver el tono, saber lo que calienta del tema"*—, agrega **Motivos Permanentes** (lo que va en cada escena) y **Curva de Resistencia** (cuándo todavía NO puede ceder), obliga el **marco erótico en cada briefing** y convierte la **Temperatura en GATE medido**: antes era un conteo de subrayables, y el conteo aprobaba textos que ella declaraba fomes.

## 🤖 Modelo de Ejecución: Orquestador + 4 Subagentes

Nivel 4 colapsó los 9 subagentes del v4.6 en 3, y **v4.8 suma de vuelta el `investigador`** (la Fase 0 que el colapso había borrado sin reemplazo): **4**. El Orquestador NO escribe el contenido — invoca cada subagente vía **Task tool** con su `subagent_type` y parsea el `*_RESULT` JSON de la última línea para encadenar la siguiente fase.

| Subagente Nivel 4 | Reemplaza (v4.6) | Archivo definición |
|-------------------|------------------|--------------------|
| **`investigador`** 🆕 | Recupera la Fase 0 de Investigación (borrada en el colapso 9→3) | `.claude/agents/investigador.md` |
| **`compositor`** | Ideador + Arquitecto + Personajes + Diseñador Sensual + Mecanismo de Calentón (5→1) | `.claude/agents/compositor.md` |
| **`escritor-nivel4`** | Escritor (refactor: prosa pura + voz persistente) | `.claude/agents/escritor-nivel4.md` |
| **`validador`** | Crítico + Centinela + Contador + Editor (4→1, Editor ELIMINADO; **Centinela recuperado 16/06 como eje Continuidad**) | `.claude/agents/validador.md` |

**Ventajas:**
- Menos sobre-documentación → el Escritor llega con lo esencial y produce prosa con calor, no controlada/clínica.
- Voz persistente: el Escritor del Cap 5 suena igual que el del Cap 1 (`voz_autoral.md` se acumula con cada cap aprobado).
- Sin Editor: el texto nunca pasa por una pasada que suaviza. Temperatura baja → vuelve al Escritor con su voz.

**Cuándo NO invocar subagente:**
- Conversaciones casuales con la Ama sobre el proyecto.
- Decisiones meta (¿avanzo a Fase X? ¿qué proyecto retomamos?).
- Cuando la Ama pide algo que cabe en 1-2 mensajes sin escribir archivos.

**Patrón de invocación:**
```
Agent({
  description: "Fase X — [Acción corta]",
  subagent_type: "investigador" | "compositor" | "escritor-nivel4" | "validador",
  prompt: "[Briefing: proyecto, rutas de input, número de capítulo, instrucción literal de la Ama]"
})
```

---

## 📚 Recursos del Nivel 4 (orden de prioridad estricto)

El **Escritor-Nivel4** carga en este orden:

1. **`canon_relato.md`** (del proyecto) — el ÚNICO documento de canon, ~2,000 palabras. Premisa + 3-5 pivotes narrativos + voz de personajes + mecanismo transversal + imágenes ancla + mapa de capítulos + vocabulario + cementerio. **La voz literal de la Ama gana sobre cualquier interpretación.**
2. **`01_Canon/voz_autoral.md`** — voz persistente. Tics, ritmos, frases canónicas confirmadas por la Ama. Se acumula con cada capítulo aprobado. **NO es contexto frío — es continuidad entre capítulos.**
3. **`01_Canon/antologia_calenton.md`** — antología textual (reemplaza el CALENTON_AMA.md abstracto). Fragmentos de prosa que la Ama declaró que la calentaron. Ejemplos a IMITAR en estilo/ritmo/vocabulario, NO categorías M1-M17.
4. **Secundarios (consulta, no obligatorio leer completos):** `01_Canon/LIBRO_MAESTRO_ESCRITURA.md`, guías de arquitectura erótica (MtF/bimbo/hipnosis/femdom/bodyhorror) según tema, y **capítulos previos APROBADOS** del mismo relato (continuidad de voz).

> **🕒 Artefacto paralelo al canon — `cronologia.md` (Blindaje de Continuidad, Ama 16/06/2026):** el canon es estable; la **cronología es viva**. Es el Centinela hecho documento (calendario anclado + Hechos Plantados + estado del cuerpo por capítulo). El **Compositor** la crea, el **Escritor** la lee y la actualiza al cerrar cada capítulo, el **Validador** la audita en el eje Continuidad. Nació de la auditoría de `esposa_servidumbre` (callback a una escena nunca escrita, un "martes" suelto que descuadró la semana, guantes en un cap y manos desnudas en el siguiente).

---

## 🗂️ Estructura de Carpetas Obligatoria

`03_Literatura/01_En_Progreso/[proyecto]/`:
- `canon_relato.md` — el documento de canon único (Nivel 4)
- `cronologia.md` — calendario anclado + Hechos Plantados + estado del cuerpo (Centinela documental, vivo)
- `walkthrough.md` — bitácora viva del proyecto
- `capitulo_[N]_[slug]_v0.[X].md` — capítulo activo (**SOLO PROSA**, sin metadata)
- `capitulo_[N]_maestro_vX.md` — Gold Master cuando exista
- `nota_capitulo_[N]_[slug]_v[X].md` — **Gate de la Ama** (su revisión, escrita en su app y subida por git). Vive en la raíz **solo mientras está pendiente**; una vez aplicada se mueve a `reportes/capitulo_[N]/` renombrada `..._APLICADA.md`.
- `borradores/capitulo_[N]/` — versiones desplazadas
- `reportes/capitulo_[N]/` — autoverificación del Escritor + validación del Validador **+ notas de la Ama ya aplicadas** (`nota_..._vX_APLICADA.md`)

### Regla Operativa
1. Solo el capítulo **activo** vive en la raíz, y contiene **prosa pura**.
2. Toda metadata (autoverificación, validación) va a `reportes/capitulo_[N]/`.
3. Cuando nace `v0.2`, la versión previa se mueve a `borradores/capitulo_[N]/`.
4. La raíz no se llena de informes ni versiones viejas.
5. **La nota (Gate) de la Ama se mueve al aplicarla.** Llega a la raíz como `nota_capitulo_[N]_..._vX.md` y ahí espera. En cuanto sus correcciones quedan encarnadas en una versión nueva del capítulo, se mueve a `reportes/capitulo_[N]/nota_..._vX_APLICADA.md`. La raíz solo debe tener la nota **pendiente** (si la hay) — nunca un cementerio de Gates viejos.

### 🗒️ Ciclo de la Nota de la Ama (Gate) — Directiva Ama 23/07/2026

> *"incluye en el flujo de la escritura que debes mover las notas de los relatos"*

La nota (`nota_capitulo_[N]_[slug]_vX.md`) es el **canal fijo del Gate de la Ama** (ver auto-memoria `feedback_gate_nota_capitulo`): la escribe en su app y se sube por git a la **raíz** del proyecto. Su ciclo de vida es parte del flujo de escritura, no un trámite aparte:

1. **PENDIENTE (en la raíz):** apenas aparece una `nota_..._vX.md`, es el Gate de esa versión. Leerla, parsearla (viene en prosa hablada, sin viñetas), y si trae correcciones = **NO es aprobación** → vuelve al Escritor-N4 (micro-fixes / tramo de reescritura), sube versión, re-valida.
2. **APLICADA (mover):** una vez que sus correcciones están **encarnadas en la versión nueva** del capítulo, se **mueve** a `reportes/capitulo_[N]/` renombrada `nota_..._vX_APLICADA.md`. Así la raíz queda limpia y se ve de un vistazo cuál Gate está **vivo** y cuáles ya se cumplieron.
3. **Regla del barrido:** al retomar cualquier relato, revisar la raíz — toda `nota_...` sin sufijo `_APLICADA` es un Gate **pendiente o a medio aplicar**; ninguna nota de una versión **ya superada** debe seguir suelta en la raíz.
4. **⚠️ Antes de mover, verificar que sea de verdad un Gate de ESE capítulo.** Una nota mal archivada (contenido de imágenes/otro tema con nombre `nota_capitulo_...`) **NO** se marca `_APLICADA`: se reencauza a su pendiente real. Mover a ciegas esconde una tarea viva.

---

## 📜 El Protocolo Maestro Nivel 4 (4 Fases)

### FASE 0: Investigación y Búsqueda (Investigador) — 🆕 v4.8, Directiva Ama 22/07/2026

> **Por qué vuelve.** El colapso 9→3 del Nivel 4 borró la fase de investigación **sin reemplazarla**: la palabra "investigación" no aparecía ni una vez en los tres subagentes, mientras 24 documentos de investigación seguían en el repo de cuando la fase existía. La Ama lo diagnosticó de memoria y tenía razón — *"antes había una fase previa de investigación y qué es lo que se busca"*. Sin materia real el Escritor escribe abstracto, y ella termina pidiendo a mano lo que el protocolo debía traer puesto (*"usa técnicas reales de hipnosis"*, *"me falta temperatura, está fome"*).

- **Subagente:** `investigador` (Task tool, `subagent_type: "investigador"`)
- **Espera:** `INVESTIGADOR_RESULT:{...}` con ruta a `investigacion.md`
- **⚡ DOS PASADAS:**
  - **Pasada 1 (La Pregunta):** exactamente dos preguntas a la Ama — *"¿qué querés que sienta el lector?"* y *"¿qué buscás acá que no hayas tenido antes?"* → **STOP**. Investigar sin intención declarada produce enciclopedia inútil.
  - **Pasada 2 (Investigación):** externa (`WebSearch`/`WebFetch`: cómo se siente **de verdad**, testimonios en primera persona) + interna (relatos finalizados del mismo fetiche, antología, `03_Literatura/investigacion/`).
- **Output:** `investigacion.md` con 8 secciones fijas, de las cuales **dos son nuevas y obligatorias**:
  - **§5 MOTIVOS PERMANENTES** — lo que debe estar en CADA escena (estado continuo, no evento).
  - **§6 CURVA DE RESISTENCIA** — cuánto tarda en ceder y en qué punto todavía NO puede haber cedido.
- **Gate:** *"¿Esto es lo que buscabas, o me fui para otro lado?"*
- **Cuándo se puede saltar:** solo si ya existe `investigacion.md` vigente para ese tema **y la Ama lo confirma**. Un relato nuevo sin investigación es una excepción que ella autoriza, no un default.

#### 🔄 RETROFIT AL TOCAR (Directiva Ama 22/07/2026)

> *"todos los relatos que están en fase de prueba deben pasar por el skill actualizado, a medida que yo trabaje en ellos"*

**No es una migración masiva: es perezosa y se dispara al tocar.** Cuando la Ama retome CUALQUIER relato en `01_En_Progreso/`, antes de escribir o corregir una línea:

1. **¿Existe `investigacion.md` en la carpeta?**
   - **No** → correr **Fase 0 retroactiva** primero. Las dos preguntas de la Pasada 1 se le hacen igual, aunque el relato ya tenga capítulos escritos: la Declaración de Intención de un relato a medio andar es más valiosa, no menos.
   - **Sí** → verificar que tenga **§2 Qué Calienta**, **§2b Tono**, **§5 Motivos Permanentes** y **§6 Curva de Resistencia**. Las investigaciones viejas (pre-22/07) **no las tienen** → completarlas, no rehacer el documento entero.
2. **¿El canon tiene §4b Motivos Permanentes y §4c Curva de Resistencia?** Si no, copiarlos desde la investigación (no resumirlos).
3. Recién entonces continuar con lo que la Ama pidió.

**Estado al 22/07/2026** — 10 relatos activos, **6 sin investigación**:

| Proyecto | investigacion.md | Nota |
|----------|------------------|------|
| `la_muneca_del_gerente` | ✅ (`investigacion_tema.md`) | Falta §2b Tono · §5 · §6 |
| `la_evaluacion_de_miss_doll` · `trance_latex_drone` · `trance_office_siren` | ✅ | Falta §2b · §5 · §6 |
| `lo_que_pediste` · `el_podcast` · `el_secreto_de_la_comoda` · `el_collar_de_nancy` · `arquitectura_del_castigo` · `los_deseos_de_ginny` | ❌ | **Fase 0 retroactiva al retomarlos** |

⛔ **Prohibido correr la Fase 0 retroactiva de motu propio sobre un relato que la Ama no está tocando.** Se dispara cuando ella lo abre, no antes.

### FASE 1: Composición del Canon (Compositor)
- **Subagente:** `compositor` (Task tool, `subagent_type: "compositor"`)
- **Espera:** `COMPOSITOR_RESULT:{...}` con ruta a `canon_relato.md`
- **⚡ FLUJO INTERACTIVO — DOS PASADAS:**
  - **Pasada 1 (Intake consolidado):** 3-5 preguntas focalizadas — premisa cruda, 3-5 pivotes narrativos (no 10 compromisos), voz de personajes (frase literal, no descripción), mecanismo psicológico transversal (por qué EL RELATO TODO excita), 3-5 imágenes ancla. → STOP, espera respuestas.
  - **Pasada 2 (Producción):** Solo tras respuestas. Construye `canon_relato.md` (~2,000 palabras máx) transcribiendo LITERAL las respuestas críticas de la Ama.
- **Regla:** El Compositor NO agrega personajes, sub-fetiches ni sub-tramas que la Ama no mencionó. Si tiene una idea → la presenta como pregunta.
- **Output:** `canon_relato.md` **+ `cronologia.md`** (esqueleto: día-cero + calendario del mapa de capítulos + Hechos Plantados sembrados con las promesas/objetos/frases-ancla de los pivotes). Anclaje RELATIVO — no se inventan días de semana sueltos.
- **Gate:** *"¿Reconoces este canon como tuyo, o lo procesé y se perdió el matiz?"*

### FASE 2: Escritura (Escritor-Nivel4)
- **Subagente:** `escritor-nivel4` (Task tool, `subagent_type: "escritor-nivel4"`) — **invocado por TRAMOS** (ver Modo Tramo abajo), una llamada por bloque de beats.
- **Espera:** un `ESCRITOR_N4_RESULT:{...}` por tramo — `estado:"PARCIAL"` (tramos 1..N-1, con `tramo` + `ultima_linea`) o `estado:"COMPLETO"` (tramo final, con ruta a autoverificación + pivotes cumplidos).
- **🚨 REGLA #1 (Nivel 4) — METADATA EN ARCHIVO SEPARADO:** El archivo del capítulo contiene **SOLO prosa narrativa**. Prohibido: bloques de autoverificación, listas M1-M17, conteos de subrayables, tablas de compromisos, etiquetas "[BEAT ERÓTICO]". Todo eso va a `reportes/capitulo_[N]/autoverificacion_v0.[X].md`. **La Ama abre el capítulo y solo encuentra prosa.**
- **Modo "ESTÁS EN LA ESCENA":** El Escritor está dentro del cuerpo del personaje sumiso. Transcribe lo que ya está pasando en ese cuerpo.
- **Inputs en orden:** `canon_relato.md` (P1) → `investigacion.md` (P1.2) → `cronologia.md` (P1.5) → `voz_autoral.md` (P2) → `antologia_calenton.md` (P3) → **`resources/HUMANIZADOR.md` (P3.5, OBLIGATORIO)** → secundarios. La voz literal de la Ama gana.
- **🩸 Humanización de escritura (Ama 03/08/2026):** el Escritor corre la pasada de `resources/HUMANIZADOR.md` sobre el capítulo cerrado (en MODO TRAMO, en el tramo N sobre el archivo completo) y declara la tabla H1-H9 en su autoverificación; el **Validador la audita en su Área 1b** y contrasta conteos. **No confundir con el `/humanizer` de la FASE PUBLICACIÓN** (§Publicación 1): ése es una herramienta externa que corre *después* del Gate de la Ama, sobre texto ya aprobado. Éste es interno, previo al Validador, y existe porque el colapso a Nivel 4 archivó al Editor —el único que humanizaba— sin reemplazarlo.
- **Patrón M1 sin etiquetar:** acción física → respuesta del cuerpo → escudo mental fallando → frase humillante del dominante → pensamiento interno. Fluyen en la prosa, NUNCA rotulados.
- **Sin cuota de palabras — NI mínimo NI tope (Directiva Ama 27/06/2026):** el relato debe **FLUIR**; la extensión la dicta el calor, el flujo y el desarrollo de los pivotes, **nunca un número**. **Prohibido pasarle al Escritor un target/rango de palabras** y **prohibido describir un capítulo como "corto" o "por debajo de X palabras".** Si falta cuerpo, pedir más **BEATS** o más profundidad de una escena concreta, no "más palabras".
- **⛓️ LEY DE CONTINUIDAD (Blindaje 16/06):** el Escritor lee `cronologia.md` y escribe gobernado por ella. (1) **No callback sin ancla** — toda referencia a evento/promesa/objeto pasado debe existir ya escrita o en la cronología; prohibido inventar recuerdos en el clímax para darles pay-off. (2) **Anclas temporales salen de la cronología** — nada de días de semana sueltos; anclaje relativo. (3) **Edit local → check global** — al aplicar un Gate/micro-fix, barrer el cap + la costura con el cap previo; las subidas de temperatura no traen datos factuales nuevos. **Al cerrar el cap/tramo N, actualiza `cronologia.md`** (calendario + hechos plantados/pagados + estado del cuerpo).
- **🔴 PERSISTENCIA:** Capítulo (prosa) + autoverificación (metadata) **+ `cronologia.md` actualizada** guardados en disco antes de Fase 3. Si el capítulo tiene metadata visible al lector → falló, reescribir.

#### 🧩 MODO TRAMO — Escritura troceada anti-truncado (Directiva Ama 12/06/2026)

**Por qué:** un capítulo entero (~10k palabras) en UNA sola invocación del Escritor revienta el presupuesto de *output* y entrega prosa truncada ("el proceso queda a la mitad"). **Solución:** el Orquestador trocea el capítulo en **3-4 tramos** según los beats del mapa en `canon_relato.md` y lanza **una invocación del Escritor por tramo**. Cada llamada Task es aislada y solo emite ~2.500-3.500 palabras → **nunca se trunca**. El Escritor *lee* todo lo ya escrito (input, barato) pero solo *emite* su tramo (output, acotado).

**Protocolo:**
1. **Plan de tramos:** el Orquestador define los tramos a partir del mapa de capítulo (típico: `Apertura · Desarrollo · Clímax · Cierre`). 3 tramos para capítulos medianos, 4 para largos. El briefing de cada invocación dice `MODO TRAMO i/N` + los beats de ESE tramo.
2. **Tramo 1/N:** el Escritor CREA `capitulo_N_v0.X.md` con **SOLO la prosa del tramo 1**. ⛔ **SIN header, SIN Control de Versión, SIN Historial** (eso es metadata visible = REPUDIO; ver REGLA #1). El control de versión vive en `reportes/capitulo_[N]/autoverificacion_v0.X.md`; el estado de avance, en `walkthrough.md`. El archivo del capítulo arranca DIRECTO en la primera línea de prosa.
3. **Tramos 2..N-1:** el Escritor hace `Read` del archivo (continuidad de voz) y **`Edit`-append** SOLO de su tramo (ancla = último párrafo existente). **Jamás re-emite los tramos previos.**
4. **Tramo N (final):** Edit-append del último tramo. El capítulo **CIERRA EN PROSA** — ⛔ sin línea `Conteo de palabras`, sin pie de metadata, sin nada que no sea narrativa. El conteo y todo lo técnico van a la `autoverificacion_v0.X.md` completa. **La señal de capítulo COMPLETO es la existencia de la autoverificación + estado `COMPLETO` en `walkthrough.md`, NUNCA una línea dentro de la prosa.**
5. **Auto-continúo (Ama 12/06):** el Orquestador **encadena los tramos sin pedir permiso**, pero cada tramo es una invocación Task **separada** (por eso no trunca). Tras cada tramo: **persiste el estado en `walkthrough.md`** (`Cap N · tramo i/N listo · última línea: "…" · siguiente: [beat]`) y avisa a la Ama en UNA línea.
6. **Resume:** si la conversación muere, la nueva lee `walkthrough.md` (estado del tramo) + el archivo parcial y retoma desde el tramo i+1. La completitud se lee del `walkthrough.md` / la existencia de la autoverificación, **nunca de una línea de conteo en la prosa** (ya no existe).

**Invariantes:** la temperatura del tramo i+1 abre ≥ el cierre del tramo i (nunca enfría) · solo el tramo final genera autoverificación · el archivo en raíz sigue siendo **prosa pura** en todo momento (la Ama puede leer el avance parcial cuando quiera).

### FASE 3: Validación (Validador)
- **Subagente:** `validador` (Task tool, `subagent_type: "validador"`)
- **Espera:** `VALIDADOR_RESULT:{...}` con veredicto + doble eje + destino.
- **Cinco áreas:** Inmersión (anti-metadata) · **Continuidad** (cronología + costura + hechos plantados, gate 16/06) · **🔥 Temperatura** (gate 22/07) · Narrativa (consolida D1-D5) · Voz autoral (continuidad).
- **🔥 TEMPERATURA MEDIDA, NO CONTADA (Ama 22/07/2026):** *"el validador debe medir la temperatura del relato, verificar si efectivamente es erótico, si es caliente"*. El eje viejo era **un conteo** (≥4 subrayables/1000) y el conteo aprobaba textos que la Ama declaraba fomes. Ahora son **8 medidas**: T1 ¿es erótico? (¿sobrevive el cap si le sacás el sexo?) · T2 ¿calienta? (juicio directo, con las 3 frases más calientes y los 2 pasajes más fríos citados) · T3 explicitud léxica (¿nombra o esquiva?) · T4 suciedad del registro · T5 descarga real en escena · T6 densidad (necesaria, **no suficiente**) · T7 motivos permanentes **por escena** + curva de resistencia · T8 apertura. **T1 o T2 en ❌ bloquean APROBADO.**
- **🔥 El Validador NO edita texto.** Su `Write` solo crea el reporte. La iteración la hace el Escritor con su voz.
- **Tres GATES en orden: Inmersión → Continuidad → Temperatura.** Un fallo bloquea APROBADO antes de mirar narrativa. Un cap caliente con callback fantasma no se aprueba — y **un cap impecable y frío tampoco**. Prohibido aprobar por cortesía.
- **Veredicto y destino:**

| Inmersión | Continuidad | Temperatura | Narrativa | Voz | Veredicto | Destino |
|-----------|-------------|-------------|-----------|-----|-----------|---------|
| ❌ metadata visible | * | * | * | * | **REPUDIADO** | Escritor reescribe sin metadata |
| ✅ | ❌ | * | * | * | **DISCONTINUO** | Escritor corrige el hueco + actualiza cronología |
| ✅ | ✅ | **T1 ❌ no es erótico** | * | * | **FRÍO** 🆕 | Escritor reescribe con marco erótico explícito |
| ✅ | ✅ | **T2 ❌ no calienta** | * | * | **TIBIO** | Escritor reescribe con los pasajes fríos citados |
| ✅ | ✅ | ≥ 8.5 (T1·T2 ✅) | ≥ 9.0 | ✅ | **APROBADO** | Gate de la Ama |
| ✅ | ✅ | < 8.5 | ≥ 9.0 | ✅ | **TIBIO** | Escritor reescribe con feedback caliente |
| ✅ | ✅ | ≥ 8.5 | 7.0-8.9 | ✅ | **MICRO-FIX** | Escritor aplica micro-cirugías (NO Editor — no existe) |
| ✅ | ✅ | cualquiera | < 7.0 | * | **REPUDIADO** | Escritor reescritura total |
| * | * | * | * | ❌ | **DESALINEADO** | Escritor relee voz_autoral.md y reescribe |

- **Output:** `reportes/capitulo_[N]/validacion_v0.[X].md`

### CIERRE: Entrega + Captura de Voz (Orquestador + Ama)
- Tras veredicto APROBADO → Gate final de la Ama.
- **Gold Master:** `capitulo_[N]_maestro_vX.md` en raíz; `walkthrough.md` actualizado.
- **🔥 CAPTURA DOBLE (obligatoria tras aprobación):** El Orquestador pregunta a la Ama:
  > *"¿Hubo algún momento donde sentiste mordida? ¿Una frase, un gesto, un ritmo que te detuvo a respirar? ¿Y al revés — algo que te dejó tibia cuando esperabas calor?"*
  - Frases citadas / mecanismos confirmados → `01_Canon/voz_autoral.md` (tics y frases canónicas)
  - Fragmentos de prosa que la calentaron → `01_Canon/antologia_calenton.md` (antología textual)
  - Lo frío → sección Cementerio del `canon_relato.md`
- Si la Ama no quiere dar feedback, NO inventar — marcar "feedback no capturado" y continuar.
- El próximo capítulo del Escritor leerá los corpus actualizados → el sistema se entrena con reacciones reales, no con teoría.

---

## 📤 FASE PUBLICACIÓN (Ritual de Cierre Editorial — Directiva Ama 12/06/2026 · normalizado 03/07/2026)

> 📐 **ESTÁNDAR DE PUBLICACIÓN LA VOÛTE — DUEÑO ÚNICO (Ama 03/07/2026).** Esta sección es la **fuente única** de cómo se entregan los textos (título, cabecera, gancho, despedida, HTML body-only) para **AMBOS motores de escritura**: el motor madre (`engine-escritura-lv`, relato en 1ª/3ª persona) **y** el fork `engine-trance-lv` (trance/monólogo en 2ª persona). El fork **NO duplica** este ritual: apunta aquí y solo agrega sus *deltas de trance* (ver su SKILL §CIERRE + FASE PUBLICACIÓN). Cualquier cambio al estándar se hace AQUÍ.

> Cuando un texto **está OK / aprobado por la Ama**, antes de moverlo a `02_Finalizadas/`, pasa por **5 pasos obligatorios**. Recupera el flujo editorial antiguo (atribución + título + gancho + invitación + HTML body-only) y le suma la pasada de humanización.

### 1. 🤖 Pasada de Humanización (`/humanizer`)

> ⚠️ **VERIFICADO 03/08/2026 — NO INSTALADO EN LA MÁQUINA LITERARIA.** `~/.claude/skills/` no existe en este clon y `humanizer` no aparece en la lista de skills disponibles. Esta ficha describe una herramienta que **acá no corre**. Antes de darla por hecha en un cierre editorial, comprobar que existe; si no está, esta pasada de publicación queda pendiente o se hace desde la otra máquina.
>
> 🩸 **Distinto del humanizador de escritura:** `resources/HUMANIZADOR.md` (creado 03/08/2026) es interno, lo corre el **Escritor** antes del Validador y sí existe en el repo. Éste de acá es externo y de **post-Gate**. No se sustituyen.

- Herramienta: skill **`blader/humanizer`** (instalada en `~/.claude/skills/humanizer/` — el humanizador más estrellado de GitHub, 24k★, Claude Code skill, sin API externa). Quita marcas de escritura de IA (copula avoidance, staccato manufacturado, cierres de chatbot, vocabulario IA, 33 patrones).
- **🇨🇱 CALIBRACIÓN CHILENA PERMANENTE (Ama 12/06/2026):** el humanizador tiene `CALIBRACION_CHILENO_LAVOUTE.md` en su carpeta — salida SIEMPRE en español de Chile, con la **regla §14 (eliminar rayas) DESACTIVADA** (la raya es obligatoria en diálogo español + firma de respiración confirmada). Invocar así: *"Humaniza en español chileno usando CALIBRACION_CHILENO_LAVOUTE, muestra de voz `01_Canon/voz_autoral.md`."*
- **Calibración de voz OBLIGATORIA:** alimentar con `01_Canon/voz_autoral.md` + 2-3 fragmentos de `antologia_calenton.md` como muestras de estilo, para que **NO aplane el chileno cuico ni la voz erótica**. Es de dos pasadas (humanización + auditoría "obviously AI").
- **⚠️ NO aceptar la salida a ciegas:** la prosa ya pasó el Validador por su voz (oraciones-respiración, fragmentos-golpe). El humanizador corrige rarezas de IA, NO reescribe el calor. Revisar diff: si toca un beat erótico o un chilenismo intencional, revertir ese tramo. El objetivo es "a veces escribe medio raro" → natural, no homogeneizado.

### 2. 📝 Título + Cabecera (Estándar Completo Bloque)
El MD canónico en `02_Finalizadas/[relato]/` abre EXACTO con este bloque:
```markdown
*Un relato de Anaïs Belland*

# [Título]

---

**Universo:** La Voûte d'Anaïs
**Temáticas:** #Hashtag1 #Hashtag2 #Hashtag3 …
**Palabras:** ~N,000
**Perspectiva:** [Primera/Tercera] Persona ([Nombre → NombreFem] si hay transformación) · *trance/monólogo →* `Segunda Persona · monólogo (el lector es el sujeto)`
**Intensidad:** [Suave/Intensa/Extrema]

---

[GANCHO — ver paso 3]

<!-- more -->

---

[prosa…]
```
- **Título:** evocador, no spoiler, en español (el relato es chileno). Sin numeración de capítulo si es relato cerrado.
- **🔢 LÍMITE DE CARACTERES DEL TÍTULO — máx. 54 (calibración Ama, «La app» 06/2026):** el título de publicación **no supera los 54 caracteres**, contando el sufijo de capítulo si lo lleva (ej. `La app: La bimboficación de mi novio — Capítulo 1` = 53 ✓). Si una serie tiene título + subtítulo que se pasa, **recortar el subtítulo o usar prefijo corto** (`La app — Cap 1: La instalación`). **Contar SIEMPRE el largo final antes de publicar** cada capítulo de la serie.

### 3. 🪝 Resumen Gancho (teaser)
- Va en **negrita**, 2-4 frases, JUSTO antes de `<!-- more -->`. Es el anzuelo: plantea la premisa + la promesa de descenso, sin spoilear el final. Tono de contratapa caliente.
- **🔢 LÍMITE DE CARACTERES — máx. 300 (calibración Ama, «La Piel» 07/2026):** el gancho **no supera los 300 caracteres**. **Contar SIEMPRE el largo antes de publicar.** Si se pasa, recortar (menos frase, más filo), no fragmentar en más párrafos.
- Ej. real: *"Un collar rosa. Una caja misteriosa. Y un mejor amigo que descubre el poder absoluto. … Lo peor no es la esclavitud — es que empieza a anhelar las recompensas."*

### 4. 💌 Invitación Abierta de Anaïs (cierre sensual)
- **SIEMPRE** va, tras el cierre de la prosa, la despedida de **Anaïs al lector**: directa, sensual, en segunda persona ("¿Sentiste…? ¿Te viste en…?"), que reconoce el deseo despertado e **invita a escribirle al mail**. Incluye una frase en francés en cursiva y la firma.
- **Email canónico:** `anais.belland@outlook.com`.

**🔀 DOS VARIANTES (Ama 03/07/2026 — nace del error de «La Piel»):** la despedida cambia según si el texto **abre a más** o **cierra**. Elegir SIEMPRE la correcta antes de exportar.

**A) Capítulo INTERMEDIO de una serie** (hay cap siguiente) → la despedida **invita al capítulo que viene** + al mail. Cierre de prosa: `**Continuará…**`.
```
**Continuará…**

¿[Pregunta sensual que nombra el deseo despertado por ESTE capítulo]? En el próximo, [promesa/anzuelo de lo que viene, sin spoiler].

Si algo se te encendió, quiero saberlo antes de que sigas leyendo. Escríbeme.

*[Frase en francés].*

📧 anais.belland@outlook.com

*Avec dévotion obscure,*
**Anaïs Belland**
```

**B) Capítulo FINAL de serie · o relato/trance CERRADO** (no hay más) → la despedida **cierra la historia entera** (no promete cap siguiente) + invita al mail. Cierre de prosa: `**Fin**`.
```
**Fin**

¿[Pregunta sensual que nombra el deseo/estado en que quedó el lector]? ¿[Segunda pregunta que cierra el arco]?

Si esta historia despertó algo en ti — [el deseo X, el miedo Y] — quiero saberlo. Escríbeme.

*[Frase en francés].*

📧 anais.belland@outlook.com

*Avec dévotion obscure,*
**Anaïs Belland**
```
- Frases en francés canónicas (rotar): *Dis-moi ce que tu désires vraiment.* · *Avec dévotion obscure,* (cierre-firma).

### 5. 🌐 Export HTML body-only
- En `02_Finalizadas/[relato]/_publicacion/[archivo].html`: **solo cuerpo HTML** (sin `<html>/<head>/<body>`, **sin `<!DOCTYPE>`, sin `<style>`, sin artefacto/wrapper decorado** — el error de «La Piel»: se pidió body-only y entregué un artefacto con estilos).
- **QUÉ NO VA en el HTML:** ni el `# Título`, ni el bloque de metadata (Universo/Temáticas/…), ni el `<!-- more -->`. El HTML body-only = **prosa + despedida de Anaïs, nada más** (la cabecera vive solo en el MD).
- **QUÉ SÍ va:** cada párrafo en `<p>…</p>` · cursivas `<em>` · negritas `<strong>` (incl. el gancho si se decide incluirlo arriba, pero por defecto el gancho es del MD) · separadores de escena `<hr>` · saltos internos `<br>`.
- **Incluye el cuerpo + la despedida de Anaïs** (paso 4, la variante A o B que corresponda) tras un `<hr>` final. Termina en `<strong>Anaïs Belland</strong>`.
- **🔤 Convención de nombre de archivo:** minúscula, sin acentos ni ñ, palabras con guión bajo. Serie → `capitulo_N_[slug].html` (ej. `capitulo_1_la_semana.html`). Relato/trance cerrado → `[slug].html` (ej. `el_collar_de_nancy.html`).
- **Ubicaciones:** el MD completo (con cabecera) vive en la raíz del relato; el HTML body-only en `_publicacion/`; los work files en `_proceso/`.
- **Delta trance:** en un trance, además, las **anclas en MAYÚSCULAS se conservan** tal cual y las **didascalias entre paréntesis van en `<em>`** (ver `engine-trance-lv` SKILL §CIERRE).

### 6. 📕 KIT WATTPAD (Ama 22/07/2026 — obligatorio al finalizar un relato)

> *"cuando se finalice un relato debes incluir estos prompts, y los tags para wattpad"*

Un relato **no está cerrado** hasta que tiene, en su carpeta de `02_Finalizadas/[relato]/`, **dos archivos**:

| Archivo | Contenido | Dueño de |
|---|---|---|
| `prompts_portada.md` | Prompt de **portada** (512×800, generar en 3:4) + **un banner por capítulo** (1280×720, generar en 16:9), cada uno con su **VARIANTE SIN TEXTO** | los prompts de imagen |
| `kit_wattpad.md` | Metadata (categoría, rating, copyright), **descripción ≤2.000 car.**, **25 tags**, nota de autora, tabla de partes, calendario de programación, checklist y registro de publicación | lo que se pega en Wattpad |

**Plantilla:** `07_Recursos/plantilla_kit_wattpad.md` · **Reglas verificadas:** `07_Recursos/guia_publicacion_wattpad.md`

**Reglas duras que gobiernan estos prompts (Wattpad borra la imagen sin aviso):**
- ⛔ **Prohibida la exposición completa de genitales, pechos y glúteos**, y toda representación de acto sexual. Cerrar SIEMPRE cada prompt con la línea `STRICTLY: fully clothed… no nudity, no exposed nipples, no exposed buttocks, no visible genitals, no sexual act.` Esto **deroga el canon visual de Ele** para portadas: la lente fetish se expresa en material, silueta y luz, nunca en piel.
- **La escena del banner se elige por su forma, no por su calor:** la que sea horizontal por naturaleza (dos figuras separadas por el ancho de una habitación, un escenario visto desde el fondo de la sala). La escena más caliente del capítulo casi nunca es publicable en imagen — y casi nunca es la que mejor compone.
- **Composición croplable:** figuras y tipografía dentro de la banda central; 20% superior e inferior vacíos para poder recortar a 3:1.
- **Los acentos se rompen** (`Diseñé`, `ANAÏS`, `Capítulo`): por eso cada prompt lleva variante sin texto, para componer la tipografía después.
- **Tags:** máx **25**, sin puntos/guiones/espacios, **por historia y no por capítulo** (los tags con `#` del `prompts_portada.md` son de Tumblr/RRSS, no sirven acá). Mezclar español + inglés: el nicho TG/bodyswap busca en inglés aunque lea en español.

---

## 🚦 Reglas de Oro del Orquestador (Nivel 4 · v4.8)

1. **CANON MÍNIMO:** Un solo `canon_relato.md` (~2,000 palabras) por relato. No se vuelve al modelo aditivo del v4.5 que inflaba el canon a 10,000+ palabras.
2. **PROSA PURA AL LECTOR:** El archivo del capítulo nunca contiene metadata. Toda autoverificación/validación vive en `reportes/`. Metadata visible = veredicto REPUDIADO automático.
3. **VOZ PERSISTENTE:** El Escritor lee `voz_autoral.md` + capítulos previos aprobados. La voz del Cap 5 suena igual que la del Cap 1. NUNCA arranca fresco cada capítulo.
4. **ANTOLOGÍA TEXTUAL, NO ABSTRACTA:** El calentón se enseña con fragmentos de prosa a imitar (`antologia_calenton.md`), no con listas de mecanismos M1-M17.
5. **SIN EDITOR:** No existe el subagente Editor en Nivel 4. Temperatura baja → vuelve al Escritor. Narrativa con errores chicos → MICRO-FIX aplicado por el Escritor. El texto nunca pasa por una pasada que suavice.
6. **CONCEPTO LITERAL AMA = PRIORIDAD 1:** La voz literal de la Ama en `canon_relato.md` gana sobre cualquier interpretación del sistema.
7. **DESARROLLO ORGÁNICO (Ama 27/06/2026):** No hay cuotas de palabras — **ni piso ni techo**. El relato **FLUYE**; la extensión la dicta el calor y la profundidad de los pivotes, jamás un número. Nunca dar target de palabras al Escritor ni tildar un capítulo de "corto".
8. **GATES DE APROBACIÓN:** Esperar confirmación explícita de la Ama tras Fase 0 (investigación), Fase 1 (canon) y tras veredicto APROBADO (capítulo final).
8b. **🚫 NADA LLEGA A LA AMA SIN VALIDADOR (Ama 22/07/2026 — regla dura):** *"que el validador lo revise, antes de que me lo entregues"*. Está prohibido entregarle un capítulo —completo o parcial, por bueno que se vea— antes de correr la Fase 3. **El orquestador no puede auto-aprobar lo que escribió el Escritor.** Nació de un incumplimiento propio y documentado: el Cap 1 v0.5 de `la_muneca_del_gerente` se le entregó con 17.575 palabras **sin pasar por el Validador**, y quedó anotado en la memoria como pendiente en vez de corregirse. Si la Ama pide ver un avance intermedio, se le muestra **diciéndole explícitamente que aún no está validado**.
9. **WALKTHROUGH VIVO + PERSISTENCIA:** Nunca pasar de fase sin actualizar `walkthrough.md` y sin que los archivos existan en disco.
10. **CAPTURA DOBLE:** Tras cada cap aprobado, alimentar `voz_autoral.md` (tics/frases) y `antologia_calenton.md` (fragmentos) con las reacciones reales de la Ama.
11. **⛓️ BLINDAJE DE CONTINUIDAD (16/06):** `cronologia.md` es la fuente única de verdad temporal. El Escritor no hace callback sin ancla, no suelta días de semana inventados, y barre la costura global tras cada inserción. El Validador tiene Continuidad como gate: callback fantasma / calendario roto / contradicción entre capítulos = no se aprueba. Al reestructurar el arco (eliminar capítulos), barrer el canon de anclas huérfanas (referencias a capítulos que ya no existen).
12. **🔬 INVESTIGAR ANTES DE COMPONER (Ama 22/07/2026):** ningún relato nuevo entra a Fase 1 sin `investigacion.md`. El Escritor **nunca** tiene que inventar cómo se siente algo: si hay hipnosis, hay hipnosis real; si hay silicona, hay peso y temperatura reales. Saltarse la Fase 0 es una excepción que la Ama autoriza, no un default.
13. **🔥 MARCO ERÓTICO EN TODO BRIEFING (Ama 22/07/2026 — regla dura):** cada invocación del Escritor —**cada tramo, sin excepción**— abre declarando *"ESTO ES UN RELATO ERÓTICO (+18); este tramo tiene que CALENTAR"*, con temperatura objetivo y subrayables mínimos. **Prohibido framear un tramo como "de transición", "sin calor", "solo narrativo" o "fuego frío":** el Escritor lo lee como permiso para escribir thriller. Nació de un error propio (18/07: nunca le dije que era erótico y el capítulo salió frío) y la Ama sigue teniendo que recordarlo a mano — *"es un relato erótico y estás evitando decir verga"*. **Si ella tiene que acordármelo, falló el briefing, no el Escritor.**
14. **🔁 MOTIVOS PERMANENTES ≠ EVENTOS (Ama 22/07/2026):** lo que `investigacion.md §5` declara permanente va **en cada escena**, no se cumple una vez y se da por hecho. Es el reclamo más repetido de la Ama en seis relatos distintos (*"siempre y en todo momento"*, *"debe estar presente en todo el relato"*, *"que lo persiga todo el cap 2 y 3"*). El Validador lo mide **por escena**, no por capítulo.
15. **🐢 LA RENDICIÓN SE GANA (Ama 22/07/2026):** `investigacion.md §6` fija cuántas veces resiste el personaje antes de ceder y **en qué punto todavía NO puede haber cedido**. Rendirse antes de esa marca es un fallo narrativo, no una elección de ritmo (*"debe haber resistencia y no rendirse tan pronto"*, *"cómo que salta de inmediato"*).
16. **📕 UN RELATO NO ESTÁ CERRADO SIN SU KIT WATTPAD (Ama 22/07/2026):** al finalizar un relato, la carpeta de `02_Finalizadas/[relato]/` debe tener **dos archivos**: `prompts_portada.md` (portada + **un banner por capítulo**, cada uno con variante sin texto) y `kit_wattpad.md` (metadata + descripción ≤2.000 car. + **25 tags** + nota de autora + tabla de partes + calendario + checklist). Ver §FASE PUBLICACIÓN paso 6 y `07_Recursos/plantilla_kit_wattpad.md`. **La regla de imagen de Wattpad deroga el canon visual de Ele en portadas** — cero piel prohibida, cero acto sexual, y cada prompt cierra en `STRICTLY:`. Al generarlo, **auditar también los prompts y títulos viejos del relato**: los prompts pre-22/07 pueden pedir piel que hace borrar la imagen, y un título de capítulo aparece en listados públicos donde el rating Mature no protege.
17. **🗒️ LA NOTA DE LA AMA SE MUEVE AL APLICARLA (Ama 23/07/2026):** el Gate llega a la raíz como `nota_capitulo_[N]_..._vX.md`; en cuanto sus correcciones quedan encarnadas en una versión nueva del capítulo, se mueve a `reportes/capitulo_[N]/nota_..._vX_APLICADA.md`. La raíz solo conserva la nota **pendiente**, nunca un cementerio de Gates viejos. Antes de marcar `_APLICADA`, verificar que la nota sea de verdad el Gate de ESE capítulo (una nota mal archivada se reencauza a su pendiente real, no se entierra). Ver §Ciclo de la Nota de la Ama y la auto-memoria `feedback_gate_nota_capitulo`.

---

## 📂 Resumen de Fases v4.8 (Nivel 4 + Investigación)

```
0   Investigación [Investigador] 🆕  → investigacion.md · §2 QUÉ CALIENTA DEL TEMA + §2b TONO (el corazón)
    └─ 2 preguntas → STOP → investiga · §5 Motivos Permanentes · §6 Curva de Resistencia → Gate Ama
1   Composición   [Compositor]       → canon_relato.md (~2,000 palabras) + cronologia.md (día-cero + hechos plantados) → Gate Ama
    └─ lee investigacion.md · copia §5 y §6 al canon como 4b y 4c (no los resume)
2   Escritura     [Escritor-Nivel4]  → capitulo_v0.X.md (PROSA PURA, en 3-4 TRAMOS anti-truncado) + autoverificacion + cronologia actualizada
    └─ tramo 1 crea archivo · tramos 2..N Edit-append (no re-emiten) · tramo N cierra + autoverif + cronología · Ley de Continuidad (no callback sin ancla)
    └─ CADA briefing de tramo declara el marco erótico (Regla de Oro 13) · motivos permanentes en cada escena
3   Validación    [Validador]        → veredicto · gates Inmersión + Continuidad + 🔥TEMPERATURA, luego Narrativa + Voz
    ├ APROBADO    → Gate Ama (llega como nota_capitulo_..._vX.md en la raíz)
    │              └─ nota aplicada → MOVER a reportes/capitulo_[N]/nota_..._vX_APLICADA.md (Regla de Oro 17)
    ├ DISCONTINUO → vuelve al ESCRITOR (planta el ancla / cuadra calendario / repara costura)
    ├ FRÍO 🆕     → vuelve al ESCRITOR con marco erótico explícito (es thriller con escenas, no relato erótico)
    ├ TIBIO       → vuelve al ESCRITOR (feedback caliente + los 2 pasajes fríos citados)
    ├ MICRO-FIX   → ESCRITOR aplica cirugías (NO Editor)
    ├ REPUDIADO   → ESCRITOR reescribe
    └ DESALINEADO → ESCRITOR relee voz_autoral y reescribe
CIERRE  Entrega + Captura [Orquestador+Ama] → Gold Master + alimentar voz_autoral + antologia_calenton
PUBLIC. Ritual editorial [Orquestador]      → /humanizer (voz calibrada) → título+cabecera+gancho → invitación Anaïs → HTML body-only → 02_Finalizadas/
```

**Subagentes legacy del v4.6** (ideador, arquitecto, personajes, disenador-sensual, escritor, critico, editor, contador, centinela) viven en `.claude/agents/_legacy_v46/` como referencia histórica. **No se invocan en Nivel 4.**

---

*La Voûte no solo escribe, orquesta el deseo. Nivel 4: menos canon, más voz, cero suavizado.*
*v4.8: el calor se investiga antes de escribirlo, y se mide antes de aprobarlo.*
