---
name: engine-escritura-lv
description: Motor de Escritura La Voûte (engine-escritura-lv) — Agente Orquestador Maestro v4.6. Coordina el flujo literario con foco en POR QUÉ excita (no solo QUÉ pasa). v4.6 introduce Fase 3.4 Mecanismo de Calentón, Ritual de Calentón pre-escritura, doble eje Narrativa+Temperatura en Crítico, regla PROHIBIDO TOCAR en Editor, concepto literal Ama como prioridad 1, y elimina bucle Crítico↔Editor para temperatura (texto tibio vuelve al Escritor, no al Editor).
---

# 🧠 Skill: Engine Escritura LV — Orquestador Maestro de La Voûte (v4.6)

Esta skill permite al agente actuar como el **Agente Orquestador**, el director técnico supremo del flujo de producción literaria.

> **v4.6 — Cambios clave respecto a v4.5:** El sistema priorizaba QUÉ pasa (arco, mapa, compromisos). v4.6 prioriza **POR QUÉ excita específicamente a la Ama**. Diagnóstico convergente de 3 análisis identificó que el bucle Crítico↔Editor sanitizaba el texto con cada iteración (caso documentado: `la_piel_que_diseno` Cap 1 maestro v1 con 9.0 Crítico que nunca calentó). Ver `01_Canon/REDISENO_ENGINE_ESCRITURA_v4.6.md` para diagnóstico completo.

## 🤖 Modelo de Ejecución: Orquestador + 9 Subagentes

A partir de v4.5, cada fase se delega a un **subagente especializado** definido en `.claude/agents/[nombre].md`. El Orquestador NO escribe el contenido de cada fase directamente — invoca el subagente vía **Task tool** con `subagent_type: [nombre]` y recibe el `*_RESULT` JSON con el archivo guardado y el estado.

**Ventajas:**
- Cada subagente arranca con contexto frío y solo carga su system prompt → menos contaminación cruzada
- El Orquestador mantiene la visión macro (qué fase sigue, qué Gates esperan aprobación de Ama)
- Los subagentes pueden ejecutarse en paralelo cuando son independientes (ej: Crítico + Contador después de un capítulo)

**Cuándo NO invocar subagente:**
- Conversaciones casuales con la Ama sobre el proyecto
- Decisiones meta (¿avanzo a Fase X? ¿qué proyecto retomamos?)
- Cuando la Ama pide algo que cabe en 1-2 mensajes sin escribir archivos

**Patrón de invocación:**
```
Agent({
  description: "Fase X — [Acción corta]",
  subagent_type: "[nombre-subagente]",
  prompt: "[Briefing completo: proyecto, ruta de archivos de input, número de capítulo si aplica, instrucción específica de la Ama]"
})
```
Después, parsear la última línea `*_RESULT:{...}` para saber qué se produjo.

---

## 📂 Mapa Subagente ↔ Fase (Fuente Única)

Los subagentes activos viven en `.claude/agents/` (project-level) y se invocan vía Task tool. Los prompts originales en `07_Recursos/prompts/` quedan como **documentación de referencia** y para auditoría.

| Fase | Subagente (Task) | Archivo definición | Doc de referencia |
|------|------------------|--------------------|-------------------|
| 1 — Concepción | `ideador` | `.claude/agents/ideador.md` | `07_Recursos/prompts/ideador.md` |
| 2 — Arquitectura | `arquitecto` | `.claude/agents/arquitecto.md` | `07_Recursos/prompts/arquitecto.md` |
| 3 — Personajes | `personajes` | `.claude/agents/personajes.md` | `07_Recursos/prompts/personajes.md` |
| 3.3 — Mapa Erótico | `disenador-sensual` | `.claude/agents/disenador-sensual.md` | `07_Recursos/prompts/disenador_sensual.md` |
| 4 — Escritura | `escritor` | `.claude/agents/escritor.md` | `07_Recursos/prompts/escritor.md` |
| 5 — Crítico | `critico` | `.claude/agents/critico.md` | `07_Recursos/prompts/critico.md` |
| 6 — Editor | `editor` | `.claude/agents/editor.md` | `07_Recursos/prompts/editor.md` |
| 7 — Contador | `contador` | `.claude/agents/contador.md` | `07_Recursos/prompts/contador.md` |
| 7b — Centinela | `centinela` | `.claude/agents/centinela.md` | `07_Recursos/prompts/centinela.md` |
| Orquestador | (esta skill) | — | `07_Recursos/prompts/orquestador.md` |

**Cada subagente devuelve un JSON `*_RESULT:{...}` como última línea de su respuesta** — el Orquestador lo parsea para encadenar la siguiente fase.

---

## 📚 Recursos Obligatorios (Cargar antes de escribir)

El Agente Escritor DEBE cargar en este orden:

**Corpus de Calentón (PRIMERO desde v4.5 — define la calibración personal a la Ama):**
0. `01_Canon/Guias_Especializadas/CALENTON_AMA.md` — Corpus vivo de feedback de la Ama (mecanismos confirmados, frases que funcionaron, cementerio). El Escritor lo lee ANTES de cualquier otra cosa. El Orquestador lo actualiza después de cada Cap aprobado.

**Recursos base (SIEMPRE):**
1. `01_Canon/LIBRO_MAESTRO_ESCRITURA.md` — Fuente única de verdad
2. `.agent/skills/escritura-voûte/resources/CODEX_PSICOLOGICO.md` — Base científica
3. `.agent/skills/escritura-voûte/resources/GUIA_FETICHISTA.md` — Mecánicas por fetiche
4. `.agent/skills/escritura-voûte/resources/MEMORIA_ERRORES.md` — Reglas aprendidas (prioridad absoluta)
5. `.agent/skills/escritura-voûte/resources/BITACORA_TEMPORAL.md` — Estado actual del personaje

**Guías especializadas mayo 2026 — Arquitecturas eróticas (cargar según tema del relato):**
6. `01_Canon/Guias_Especializadas/arquitectura_erotica_mtf_v1.md` — Si hay feminización / travestismo / body swap / cross-dressing / hipnosis-que-feminiza
7. `01_Canon/Guias_Especializadas/arquitectura_erotica_bimbo_v1.md` — Si hay dumb down / bimboficación / Vacío Feliz / reprogramación mental
8. `01_Canon/Guias_Especializadas/arquitectura_erotica_hipnosis_v1.md` — Si hay trance / condicionamiento / hipnosis como motor
9. `01_Canon/Guias_Especializadas/arquitectura_erotica_femdom_v1.md` — Si hay dominación femenina como eje
10. `01_Canon/Guias_Especializadas/arquitectura_erotica_bodyhorror_v1.md` — Si hay transformación corporal visceral / objetificación literal
11. `01_Canon/Guias_Especializadas/guia_terror_erotico.md` — Si hay atmósferas de terror erótico / horror sensual (rev. mayo 2026)

**Corpus de referencia empírica mayo 2026 (consulta durante escritura):**
12. `01_Canon/Guias_Especializadas/ANÁLISIS_RELATOS_REFERENCIA.md` — Corpus empírico (14 relatos de referencia con técnicas medidas)
13. `01_Canon/Guias_Especializadas/ANÁLISIS_ESTILO_LITERARIO.md` — Análisis de estilo del corpus (rev. mayo 2026)

**Proyecto activo:**
14. `concepto.md` — Gancho, Detalle Sensorial Central, Nivel de Explicitad
15. `arco_maestro_vX.md` — Arco inviolable + Rima Narrativa Central
16. `personajes_maestro_vX.md` — Curva de Vocabulario, Fetiche Quirúrgico, Detalle Físico Ancla
17. `mapa_erotico_v1.md` — Curva de excitación, escenas clave diseñadas, vocabulario autorizado

---

## 🗂️ Estructura de Carpetas Obligatoria

El Orquestador DEBE mantener la carpeta de cada proyecto en este orden:

- **Raíz del proyecto (`03_Literatura/01_En_Progreso/[proyecto]/`):**
  - `walkthrough.md`
  - `concepto.md` / `idea_maestro_vX.md`
  - `arco_maestro_vX.md`
  - `linea_de_tiempo_maestra.md`
  - `personajes_maestro_vX.md`
  - `capitulo_[N]_[slug]_v0.X.md` activo
  - `capitulo_[N]_maestro_vX.md` cuando exista versión final
- **Borradores archivados:** `borradores/capitulo_[N]/`
- **Auditorías:** `reportes/capitulo_[N]/`

### Regla Operativa
1. Solo el archivo **activo** del capítulo vive en la raíz.
2. Cuando nace una nueva iteración (`v0.2`, `v0.3`, etc.), la versión desplazada se mueve a `borradores/capitulo_[N]/`.
3. Toda salida de `Crítico`, `Contador` y `Centinela` se guarda en `reportes/capitulo_[N]/`.
4. La raíz no debe llenarse de informes ni de versiones viejas.

---

## 📜 El Protocolo Maestro (8 Fases)

### FASE 1: Concepción (Origen de la Ama)
- **Subagente:** `ideador` (vía Task tool, `subagent_type: "ideador"`)
- **Doc de referencia:** `07_Recursos/prompts/ideador.md`
- **Espera:** `CONCEPTO_RESULT:{...}` con ruta a `concepto.md`
- **⚡ FLUJO INTERACTIVO — DOS FASES:**
  - **Fase A (Intake):** El Ideador hace eco literal de la premisa + selecciona 3-4 preguntas del banco (gancho, tono, conciencia del protagonista, explicitad, detalle sensorial, fetiches) → STOP, espera respuestas.
  - **Fase B (Producción):** Solo tras recibir respuestas. El concepto refleja lo que la Ama dijo, no lo que el agente imaginó.
- **Regla crítica:** El Ideador NO agrega personajes, sub-fetiches ni sub-tramas que la Ama no mencionó. Si tiene una idea, la presenta como pregunta.
- **Output obligatorios:** `concepto.md` + `walkthrough.md`
- **Gate:** *"¿Reconoce la Ama todos los elementos como suyos?"*

### FASE 2: Arquitectura (Arco Maestro)
- **Subagente:** `arquitecto` (vía Task tool, `subagent_type: "arquitecto"`)
- **Doc de referencia:** `07_Recursos/prompts/arquitecto.md`
- **Espera:** `ARQUITECTO_RESULT:{...}` con rutas a `arco_maestro_v1.md` + `linea_de_tiempo_maestra.md`
- **⚡ FLUJO INTERACTIVO — DOS FASES:**
  - **Fase A (Intake):** El Arquitecto resume el concepto en 3 líneas + selecciona 3-5 preguntas estructurales del banco (escala, curva de rendición, rimas narrativas, clímax, estructura temporal) → STOP, espera respuestas.
  - **Fase B (Producción):** Solo tras recibir respuestas. Incluye la **Rima Narrativa Central** (objeto/gesto/frase que abre el relato y regresa transformado al final) y compromisos verificables por capítulo.
- **⚠️ REGLA CARDINAL:** Una vez aprobado por la Ama, el arco es **INVIOLABLE**. El Escritor NO puede desviarse sin Gate.
- **Output:** `arco_maestro_vX.md` + `linea_de_tiempo_maestra.md`
- **Gate:** *"¿Aprobamos el arco y la línea de tiempo, Ama?"*

### FASE 3: Personajes (Identidad y Soul)
- **Subagente:** `personajes` (vía Task tool, `subagent_type: "personajes"`)
- **Doc de referencia:** `07_Recursos/prompts/personajes.md`
- **Espera:** `PERSONAJES_RESULT:{...}` con ruta a `personajes_maestro_v1.0.md`
- **⚡ FLUJO INTERACTIVO — DOS FASES:**
  - **Fase A (Intake):** Lista de personajes clasificados (principales/secundarios/figurantes) + 3 preguntas por personaje principal del banco (presencia física, voz con frases de ejemplo, invariante interno, fetiche quirúrgico) → STOP, espera respuestas.
  - **Fase B (Producción):** Solo tras recibir respuestas. Las fichas incluyen: **Detalle Físico Ancla** (el elemento en cada escena), **Invariante Interno** (lo que no cambia ni en la transformación más profunda), **Curva de Vocabulario** con frases de ejemplo por etapa, **Fetiche Quirúrgico** con estímulo exacto + respuesta exacta + si el personaje es consciente de ello.
- **Output:** `personajes_maestro_vX.md`
- **Gate:** *"¿Aprobamos las fichas, Ama? Voz y Fetiche Quirúrgico son los campos más difíciles de corregir después."*

### FASE 3.3: Mapa Erótico (Diseño Sensual — OBLIGATORIA)
- **Subagente:** `disenador-sensual` (vía Task tool, `subagent_type: "disenador-sensual"`)
- **Doc de referencia:** `07_Recursos/prompts/disenador_sensual.md`
- **Espera:** `DISENADOR_RESULT:{...}` con rutas al mapa general y al específico del capítulo activo
- **⚡ FLUJO INTERACTIVO — DOS FASES:**
  - **Fase A (Intake):** El Diseñador Sensual sintetiza lo que ya leyó del arco y fichas + selecciona 3-4 preguntas sobre: fetiche principal, clímax erótico deseado, qué siente el lector, nivel de explicitad, dosificación → STOP, espera respuestas.
  - **Fase B (Producción):** Solo tras recibir respuestas. Produce el mapa con curva de excitación por escena, diseño detallado de cada momento clave, y vocabulario erótico autorizado.
- **🔥 v4.6 — Prosa-anchor obligatorio en escenas T° ≥ 4:** cada escena clave del mapa con T°≥4 debe incluir un párrafo-muestra de 3-5 líneas que sirva como termómetro literario al Escritor (NO texto a copiar — temperatura y tono que debe alcanzar).
- **Por qué existe:** El arco define qué pasa. Las fichas definen quién es. El Mapa Erótico define cómo excita externamente. **Pero NO captura POR QUÉ — eso es Fase 3.4.**
- **Output:** `mapa_erotico_v1.md` + `mapa_erotico_cap[N]_v1.md` con curva de excitación, escenas clave + prosa-anchor T°≥4, clímax erótico, regla de dosificación, vocabulario autorizado.
- **Gate:** *"¿Reconoce la Ama este mapa como el relato que tiene en la cabeza?"*

### FASE 3.4: Mecanismo de Calentón (v4.6 — OBLIGATORIA, sin subagente)

- **Quién:** El Orquestador conmigo (la Ama). **NO es subagente** — es Intake directo.
- **Por qué existe (v4.6):** El Mapa Erótico captura QUÉ pasa. El Mecanismo de Calentón captura POR QUÉ esto excita específicamente a la Ama (fantasía emocional debajo de la acción visible). Sin este documento, el Escritor produce eventos correctos sin mecanismo psicológico, y el texto sale "técnicamente bien escrito" pero "no produce lo que la Ama imaginaba".
- **Cuándo:** Después del Gate del Mapa Erótico, antes de la Escena Piloto.
- **Tamaño:** 1 página máximo por capítulo.
- **Plantilla:** `01_Canon/plantilla_mecanismo_calenton.md` — define el formato YAML por escena clave (Qué ocurre · Mecanismo psicológico · Emoción objetivo · Momento crítico · Error fatal · Vocabulario/imagen clave).
- **Proceso:** El Orquestador identifica las escenas T°≥3 del Mapa Erótico, hace 6 preguntas a la Ama por cada una, y transcribe LITERALMENTE sus respuestas (sin procesar, sin resumir, sin "mejorar" la redacción).
- **Output:** `mecanismo_calenton_cap[N].md` en raíz del proyecto.
- **Gate:** *"¿Reconoces este mecanismo como el tuyo, o lo procesé y se perdió el matiz?"*
- **Quién lo lee:** Escritor lo lee PRIMERO (antes del Mapa Erótico). Crítico lo usa para el Test del Subrayado. Editor NO necesita leerlo (su rol es ortografía + cirugías literales).

### FASE 3.5: Escena Piloto (Gate de Temperatura — OBLIGATORIA)
- **Qué es:** Antes de escribir el capítulo completo, el Escritor produce UNA sola escena de 300–500 palabras que demuestra el nivel de calor objetivo para ESTE capítulo específico.
- **Qué escena:** La escena más erótica del arco del capítulo — el momento que más calienta según los compromisos.
- **Por qué:** Si la Ama rechaza la temperatura de 400 palabras, corregir toma 5 minutos. Si la rechaza en un capítulo de 7,000 palabras, la corrección toma 3 sesiones.
- **Gate obligatorio:** La Ama aprueba o rechaza la escena piloto. Solo con aprobación explícita avanza a Fase 4.
- **Efecto:** La escena piloto aprobada SE INCORPORA al capítulo final y funciona como **referencia de temperatura** — todas las demás escenas deben alcanzar o superar ese nivel.
- **Output:** La escena piloto se guarda en `reportes/capitulo_[N]/escena_piloto_v0.1.md`
- **Gate:** *"¿Este nivel de calor es el que buscas, Ama?"*

### FASE 3.6: Ritual de Calentón PRE-Escritura (v4.6 — OBLIGATORIA, 3 preguntas)

- **Quién:** El Orquestador conmigo (la Ama).
- **Cuándo:** Inmediatamente antes de Fase 4, después de Escena Piloto aprobada.
- **Por qué existe (v4.6):** El Ritual de Calentón v4.5 ocurría DESPUÉS del cap (post-mortem) — ayudaba al PRÓXIMO cap pero NO al actual. v4.6 lo mueve también ANTES — preguntas que dan al Escritor el norte emocional antes de escribir una línea.
- **Las 3 preguntas obligatorias:**
  1. ¿QUÉ MOMENTO IMAGINAS cuando pensás en este capítulo? (imagen sensorial concreta)
  2. ¿CUÁL ES LA IMAGEN QUE MÁS TE INTERESA VER ESCRITA?
  3. ¿QUÉ MOMENTO NO PUEDE FALLAR? (si falla este, el cap falla)
- **Transcripción:** literal, sin procesar, sin resumir.
- **Plantilla:** `01_Canon/plantilla_ritual_calenton_pre_escritura.md`
- **Output:** bloque `<RITUAL_CALENTON_PRE_ESCRITURA>` que se inyecta al briefing del Escritor como PRIORIDAD 1.

### FASE 4: Escritura (v4.6 — Escritor en modo "ESTÁS EN LA ESCENA")

- **Subagente:** `escritor` (vía Task tool, `subagent_type: "escritor"`)
- **Doc de referencia:** `07_Recursos/prompts/escritor.md` (refactorizado a ~110 líneas en v4.6)
- **Espera:** `ESCRITOR_RESULT:{...}` con ruta a `capitulo_[N]_[slug]_v0.1.md`, X/Y compromisos, subrayados auto-contados, secciones que pasan Test del Subrayado.
- **🔥 v4.6 — Prioridad de inputs (ORDEN ESTRICTO):**
  1. `<CONCEPTO_AMA_LITERAL>` — lo que la Ama dijo TEXTUALMENTE al iniciar el proyecto. **Si hay conflicto con el resto, gana esto.**
  2. `<RITUAL_CALENTON_PRE_ESCRITURA>` — las 3 respuestas literales de la Ama.
  3. `mecanismo_calenton_cap[N].md` — POR QUÉ esta escena excita.
  4. `mapa_erotico_cap[N]_v1.md` — Contrato de T° con prosa-anchor.
  5. `arco_maestro_vX.md` — COMPROMISOS + Punto de Inflexión.
  6. `personajes_maestro_vX.md` — Voz + Fetiche Quirúrgico.
  7. CALENTON_AMA.md + recursos linkeados (consulta, no obligatorio leer completos).
- **Regla de Oro:** Respetar el arco aprobado capítulo a capítulo. NUNCA anticipar la curva de rendición.
- **🔴 REGLA DE DESARROLLO (reemplaza al presupuesto de palabras desde v4.5):**
  - **NO hay mínimo ni máximo arbitrario de palabras.** La extensión la dicta el desarrollo orgánico de los COMPROMISOS DEL CAPÍTULO.
  - El criterio es: ¿cada compromiso del checklist del arco está desarrollado **en profundidad y con temperatura**, no solo mencionado?
  - Un capítulo de 2,500 palabras con todo desarrollado vale más que uno de 7,000 con un beat clave subdesarrollado.
  - El Escritor NO infla con descripción redundante para alcanzar cuota, NI comprime con saltos forzados para no excederse.
  - Pregunta de cierre antes de entregar: ¿está cada compromiso en su profundidad debida?
- **Criterios mínimos antes de entregar:**
  - Todos los COMPROMISOS DEL CAPÍTULO desarrollados con peso
  - Temperatura erótica uniforme de inicio a fin — no concentrada en escenas aisladas
  - Jerarquía sensorial (Tacto > Vista > Olfato > Sonido > Gusto)
  - Fórmula SENSACIÓN → EMOCIÓN → REACCIÓN en cada escena ritual
  - Español chileno auténtico
  - Línea de Tiempo respetada
- **🔴 REGLA DE PERSISTENCIA:** El capítulo DEBE guardarse en disco antes de pasar a Fase 5. Ruta activa: `03_Literatura/01_En_Progreso/[proyecto]/capitulo_[N]_[slug]_v0.X.md`. La versión reemplazada se archiva en `borradores/capitulo_[N]/`. **Sin archivo guardado = Fase 4 no completada.**

### FASE 5: Auditoría de Exigencia v4.6 (Crítico con DOBLE EJE + Contador en paralelo)
- **Subagentes:** `critico` + `contador` (paralelo)
- **Docs de referencia:** `07_Recursos/prompts/critico.md` + `07_Recursos/prompts/contador.md`
- **Espera:** `CRITICO_RESULT:{...}` (con doble eje narrativa/temperatura) + `CONTADOR_RESULT:{...}`
- **🔥 v4.6 — Doble Eje del Crítico:**
  - **Eje Narrativa** (D1-D5): coherencia técnica. 0-10.
  - **Eje Temperatura Efectiva** (Test del Subrayado): mínimo N subrayados/1000 palabras según T° declarada del Mapa Erótico. 0-10.
- **🔥 v4.6 — Veredicto compuesto:**
  - Narrativa ≥ 9.0 + Temperatura ≥ 8.0 → **APROBADO** → Centinela
  - Narrativa ≥ 9.0 + Temperatura < 8.0 → **TIBIO** → **VUELVE AL ESCRITOR** (no al Editor)
  - Narrativa 7.0-8.9 → **CIRUGÍA** → Editor con instrucciones de Narrativa solamente
  - Narrativa < 7.0 → **REPUDIADO** → Escritor reescribe
- **Output:** Sentencia con doble eje + reporte de Contador en `reportes/capitulo_[N]/`

### FASE 6: Bucle de Refinamiento v4.6 (Editor ↔ Crítico — SOLO Narrativa)

- **Subagente:** `editor` (vía Task tool)
- **Doc de referencia:** `07_Recursos/prompts/editor.md` (refactorizado en v4.6 con sección **PROHIBIDO TOCAR**)
- **🔥 v4.6 — Cambio cardinal del flujo:** El Editor **NO recibe el texto para subir temperatura**. Solo limpia errores narrativos (D1-D5). Si la Temperatura es baja, el texto vuelve al **Escritor** (no al Editor) con feedback caliente literal.
- **🛑 v4.6 — Regla PROHIBIDO TOCAR (anti-suavizado):** El Editor preserva repeticiones rítmicas, verbos crudos, oraciones largas-jadeantes, adverbios cargados, frases incompletas. Su pasada Anti-AI v4.5 está RECORTADA a buzzwords prohibidos solamente — el "Pase Recursivo" del v4.5 está ELIMINADO porque suavizaba más de lo que mejoraba.
- **Editor solo edita si veredicto = CIRUGÍA (Narrativa < 9.0).** Si veredicto = TIBIO, el Orquestador NO invoca al Editor — invoca al Escritor con la nota literal *"Narrativa correcta, temperatura insuficiente. Reescribí buscando N imágenes que un lector subraye en escenas T°≥4."*
- **Límite:** 3 iteraciones Editor↔Crítico para Narrativa. Si no alcanza Narrativa 9.0 en 3 rondas → escalar a la Ama.

### FASE 7: Centinela (Continuidad)
- **Subagente:** `centinela` (vía Task tool, `subagent_type: "centinela"`)
- **Doc de referencia:** `07_Recursos/prompts/centinela.md`
- **Espera:** `CENTINELA_RESULT:{...}` con veredicto APROBADO/RECHAZADO
- **Acción:** Verificación final de coherencia temporal, integridad del arco y deriva de vocabulario.
- **Input:** Arco maestro + Línea de Tiempo + fichas de personajes + capítulo aprobado
- **Bloqueo:** Si el Centinela emite `RECHAZADO`, el capítulo NO puede avanzar hasta corregir.

### FASE 8: Entrega Final + Captura de Calentón
- **Acción:** Presentar Gold Master a la Ama con Walkthrough final actualizado.
- **Output:** Capítulo en `capitulo_[N]_maestro_vX.md` + `walkthrough.md` actualizado
- **Orden final:** Gold Master en raíz; borradores y reportes quedan en sus carpetas respectivas.
- **Gate final:** *"¿Aprobamos el capítulo, Ama?"*
- **🔥 RITUAL DE CALENTÓN (OBLIGATORIO desde v4.5, tras la aprobación):**
  - El Orquestador pregunta a la Ama:
    > *"Antes de cerrar Cap [N] — ¿hubo algún momento donde sentiste mordida? ¿Una frase, un gesto, un ritmo que te detuvo a respirar? ¿Y al revés — algún momento que te dejó fría o tibia cuando esperabas calor?"*
  - Transcribir la respuesta literal a `01_Canon/Guias_Especializadas/CALENTON_AMA.md`:
    - Frases citadas → sección "Frases que funcionaron"
    - Mecanismos confirmados (Ama dice que algo funcionó) → sección "Mecanismos de Calentón Confirmados" con cita
    - Lo frío → sección "Cementerio"
  - Si la Ama no quiere dar feedback, NO inventar. Marcar como "feedback no capturado" y continuar.
  - El próximo capítulo del Escritor leerá el corpus actualizado → el sistema se entrena con reacciones reales, no con teoría.

---

## 🚦 Reglas de Oro del Orquestador

1. **ARCO INVIOLABLE:** El arco aprobado en Fase 2 es ley. El Escritor no puede inventar escenas, alterar el orden de los puntos de inflexión ni acelerar la curva de rendición sin Gate explícito de la Ama.
2. **WALKTHROUGH VIVO:** Nunca pasar de fase sin actualizar `walkthrough.md`.
3. **PERSISTENCIA OBLIGATORIA:** Cada capítulo escrito DEBE existir como archivo en disco antes de auditarse.
4. **RAÍZ LIMPIA:** La raíz del proyecto solo contiene archivos vivos y maestros; borradores y auditorías van a sus carpetas.
5. **GATES DE APROBACIÓN:** Tras Fases 1, 2, 3, 3.3, 3.4, 3.5, 3.6, 4 y 8 — esperar confirmación explícita de la Ama.
6. **LÍMITE DE BUCLE:** Máximo 3 iteraciones Editor ↔ Crítico para Narrativa. **El bucle para Temperatura NO existe en v4.6** — Temperatura baja vuelve directo al Escritor.
7. **DESARROLLO ORGÁNICO:** No hay cuotas de palabras. La extensión la dicta el calor y la profundidad de los compromisos.
8. **DELEGACIÓN A SUBAGENTES:** El Orquestador delega cada fase técnica a su subagente. **EXCEPCIÓN v4.6:** Fases 3.4 (Mecanismo de Calentón) y 3.6 (Ritual pre-escritura) NO son subagentes — son Intake directo del Orquestador con la Ama.
9. **🔥 v4.6 — CONCEPTO LITERAL AMA = PRIORIDAD 1:** Cuando el Orquestador invoca al Escritor, le pasa el `<CONCEPTO_AMA_LITERAL>` (lo que la Ama dijo textualmente al iniciar el proyecto, sin procesar) como prioridad superior al arco/personajes/mapa. Si hay conflicto, gana la voz literal de la Ama.
10. **🔥 v4.6 — TEMPERATURA NO PASA POR EDITOR:** Si veredicto = TIBIO (Narrativa OK, Temperatura baja), el texto vuelve al Escritor para reescritura. El Editor solo recibe el texto si la Narrativa falla. Esto rompe el suavizado iterativo del v4.5.
11. **🔥 v4.6 — DOBLE RITUAL DE CALENTÓN:** ANTES de escribir (Fase 3.6 — 3 preguntas que dan norte) Y DESPUÉS de cap aprobado (captura al corpus). Aprendizaje pre + post.

---

## 📂 Resumen de Fases v4.6

```
1   Concepción         [Ideador]            → Intake + concepto
2   Arquitectura       [Arquitecto]         → arco_maestro
3   Personajes         [Personajes]         → personajes_maestro
3.3 Mapa Erótico       [Diseñador Sensual]  → mapa_erotico (con prosa-anchor T°≥4)
3.4 Mecanismo Calentón [Orquestador+Ama]    → mecanismo_calenton_cap[N]    ◀ NUEVO v4.6
3.5 Escena Piloto      [Escritor]           → escena_piloto (gate de T°)
3.6 Ritual pre-esc.    [Orquestador+Ama]    → 3 preguntas al briefing       ◀ NUEVO v4.6
4   Escritura          [Escritor]           → capitulo_v0.1 (ESTÁS EN LA ESCENA)
5   Crítica            [Crítico+Contador]   → doble eje Narrativa+Temperatura
6   Refinamiento       [Editor]             → SOLO si Narrativa baja (PROHIBIDO TOCAR)
    └ Si Temperatura baja → vuelve al ESCRITOR (no al Editor)
7   Centinela          [Centinela]          → continuidad
8   Entrega + Calentón [Orquestador+Ama]    → Gold Master + captura post-cap
```

---

*La Voûte no solo escribe, orquesta el deseo. Y desde v4.6 sabe POR QUÉ. — v4.6*
