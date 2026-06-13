---
name: engine-escritura-lv
description: Motor de Escritura La Voûte (engine-escritura-lv) — Orquestador Maestro v4.7 (Nivel 4). Arquitectura consolidada de 3 subagentes (Compositor → Escritor-Nivel4 → Validador) que reemplaza los 9 subagentes del v4.6. Canon mínimo (canon_relato.md ~2,000 palabras), voz persistente (voz_autoral.md), antología textual de calentón (no listas M1-M17), prosa pura al lector con metadata en archivo separado, y Validador sin Editor (temperatura baja → Escritor, no edición que suaviza).
---

# 🧠 Skill: Engine Escritura LV — Orquestador Maestro de La Voûte (v4.7 · Nivel 4)

Esta skill permite al agente actuar como el **Agente Orquestador**, el director técnico supremo del flujo de producción literaria de La Voûte.

> **v4.7 (Nivel 4) — Por qué este rediseño:** El v4.5/v4.6 producía ~10,000+ palabras de canon (concepto + arco + personajes + mapa erótico general + mapa por capítulo + mecanismo de calentón por capítulo) ANTES de escribir una línea, y mantenía un bucle Editor↔Crítico que **sanitizaba el texto con cada iteración** (caso documentado: `la_piel_que_diseno` Cap 2 v1.7.1 con 9.0 de Crítico que nunca calentó). Nivel 4 destila a lo esencial: **un solo documento de canon, voz persistente entre capítulos, antología textual en vez de mecanismos abstractos, y eliminación del Editor.** Validado por la Ama con `esposa_servidumbre` Cap 1 (28/05/2026): *"me gusta mucho más de lo que he leído en harto tiempo."* Ver `01_Canon/REDISENO_ENGINE_ESCRITURA_v4.6.md` para el diagnóstico completo.

## 🤖 Modelo de Ejecución: Orquestador + 3 Subagentes

Nivel 4 colapsa los 9 subagentes del v4.6 en **3**. El Orquestador NO escribe el contenido — invoca cada subagente vía **Task tool** con su `subagent_type` y parsea el `*_RESULT` JSON de la última línea para encadenar la siguiente fase.

| Subagente Nivel 4 | Reemplaza (v4.6) | Archivo definición |
|-------------------|------------------|--------------------|
| **`compositor`** | Ideador + Arquitecto + Personajes + Diseñador Sensual + Mecanismo de Calentón (5→1) | `.claude/agents/compositor.md` |
| **`escritor-nivel4`** | Escritor (refactor: prosa pura + voz persistente) | `.claude/agents/escritor-nivel4.md` |
| **`validador`** | Crítico + Centinela + Contador + Editor (4→1, Editor ELIMINADO) | `.claude/agents/validador.md` |

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
  subagent_type: "compositor" | "escritor-nivel4" | "validador",
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

---

## 🗂️ Estructura de Carpetas Obligatoria

`03_Literatura/01_En_Progreso/[proyecto]/`:
- `canon_relato.md` — el documento de canon único (Nivel 4)
- `walkthrough.md` — bitácora viva del proyecto
- `capitulo_[N]_[slug]_v0.[X].md` — capítulo activo (**SOLO PROSA**, sin metadata)
- `capitulo_[N]_maestro_vX.md` — Gold Master cuando exista
- `borradores/capitulo_[N]/` — versiones desplazadas
- `reportes/capitulo_[N]/` — autoverificación del Escritor + validación del Validador

### Regla Operativa
1. Solo el capítulo **activo** vive en la raíz, y contiene **prosa pura**.
2. Toda metadata (autoverificación, validación) va a `reportes/capitulo_[N]/`.
3. Cuando nace `v0.2`, la versión previa se mueve a `borradores/capitulo_[N]/`.
4. La raíz no se llena de informes ni versiones viejas.

---

## 📜 El Protocolo Maestro Nivel 4 (3 Fases)

### FASE 1: Composición del Canon (Compositor)
- **Subagente:** `compositor` (Task tool, `subagent_type: "compositor"`)
- **Espera:** `COMPOSITOR_RESULT:{...}` con ruta a `canon_relato.md`
- **⚡ FLUJO INTERACTIVO — DOS PASADAS:**
  - **Pasada 1 (Intake consolidado):** 3-5 preguntas focalizadas — premisa cruda, 3-5 pivotes narrativos (no 10 compromisos), voz de personajes (frase literal, no descripción), mecanismo psicológico transversal (por qué EL RELATO TODO excita), 3-5 imágenes ancla. → STOP, espera respuestas.
  - **Pasada 2 (Producción):** Solo tras respuestas. Construye `canon_relato.md` (~2,000 palabras máx) transcribiendo LITERAL las respuestas críticas de la Ama.
- **Regla:** El Compositor NO agrega personajes, sub-fetiches ni sub-tramas que la Ama no mencionó. Si tiene una idea → la presenta como pregunta.
- **Output:** `canon_relato.md`
- **Gate:** *"¿Reconoces este canon como tuyo, o lo procesé y se perdió el matiz?"*

### FASE 2: Escritura (Escritor-Nivel4)
- **Subagente:** `escritor-nivel4` (Task tool, `subagent_type: "escritor-nivel4"`) — **invocado por TRAMOS** (ver Modo Tramo abajo), una llamada por bloque de beats.
- **Espera:** un `ESCRITOR_N4_RESULT:{...}` por tramo — `estado:"PARCIAL"` (tramos 1..N-1, con `tramo` + `ultima_linea`) o `estado:"COMPLETO"` (tramo final, con ruta a autoverificación + pivotes cumplidos).
- **🚨 REGLA #1 (Nivel 4) — METADATA EN ARCHIVO SEPARADO:** El archivo del capítulo contiene **SOLO prosa narrativa**. Prohibido: bloques de autoverificación, listas M1-M17, conteos de subrayables, tablas de compromisos, etiquetas "[BEAT ERÓTICO]". Todo eso va a `reportes/capitulo_[N]/autoverificacion_v0.[X].md`. **La Ama abre el capítulo y solo encuentra prosa.**
- **Modo "ESTÁS EN LA ESCENA":** El Escritor está dentro del cuerpo del personaje sumiso. Transcribe lo que ya está pasando en ese cuerpo.
- **Inputs en orden:** `canon_relato.md` (P1) → `voz_autoral.md` (P2) → `antologia_calenton.md` (P3) → secundarios. La voz literal de la Ama gana.
- **Patrón M1 sin etiquetar:** acción física → respuesta del cuerpo → escudo mental fallando → frase humillante del dominante → pensamiento interno. Fluyen en la prosa, NUNCA rotulados.
- **Sin mínimo arbitrario de palabras** — la extensión la dicta el calor y el desarrollo de los pivotes.
- **🔴 PERSISTENCIA:** Capítulo (prosa) + autoverificación (metadata) guardados en disco antes de Fase 3. Si el capítulo tiene metadata visible al lector → falló, reescribir.

#### 🧩 MODO TRAMO — Escritura troceada anti-truncado (Directiva Ama 12/06/2026)

**Por qué:** un capítulo entero (~10k palabras) en UNA sola invocación del Escritor revienta el presupuesto de *output* y entrega prosa truncada ("el proceso queda a la mitad"). **Solución:** el Orquestador trocea el capítulo en **3-4 tramos** según los beats del mapa en `canon_relato.md` y lanza **una invocación del Escritor por tramo**. Cada llamada Task es aislada y solo emite ~2.500-3.500 palabras → **nunca se trunca**. El Escritor *lee* todo lo ya escrito (input, barato) pero solo *emite* su tramo (output, acotado).

**Protocolo:**
1. **Plan de tramos:** el Orquestador define los tramos a partir del mapa de capítulo (típico: `Apertura · Desarrollo · Clímax · Cierre`). 3 tramos para capítulos medianos, 4 para largos. El briefing de cada invocación dice `MODO TRAMO i/N` + los beats de ESE tramo.
2. **Tramo 1/N:** el Escritor CREA `capitulo_N_v0.X.md` con header (Control de Versión + Historial) + prosa del tramo 1. **NO cierra con la línea `Conteo de palabras`** (su ausencia = señal de capítulo abierto/incompleto).
3. **Tramos 2..N-1:** el Escritor hace `Read` del archivo (continuidad de voz) y **`Edit`-append** SOLO de su tramo (ancla = último párrafo existente). **Jamás re-emite los tramos previos.**
4. **Tramo N (final):** Edit-append del último tramo + línea de cierre `**Conteo de palabras:** X` + escribe la `autoverificacion_v0.X.md` completa del capítulo.
5. **Auto-continúo (Ama 12/06):** el Orquestador **encadena los tramos sin pedir permiso**, pero cada tramo es una invocación Task **separada** (por eso no trunca). Tras cada tramo: **persiste el estado en `walkthrough.md`** (`Cap N · tramo i/N listo · última línea: "…" · siguiente: [beat]`) y avisa a la Ama en UNA línea.
6. **Resume:** si la conversación muere, la nueva lee `walkthrough.md` + el archivo parcial (sin línea de conteo = incompleto) y retoma desde el tramo i+1.

**Invariantes:** la temperatura del tramo i+1 abre ≥ el cierre del tramo i (nunca enfría) · solo el tramo final genera autoverificación · el archivo en raíz sigue siendo **prosa pura** en todo momento (la Ama puede leer el avance parcial cuando quiera).

### FASE 3: Validación (Validador)
- **Subagente:** `validador` (Task tool, `subagent_type: "validador"`)
- **Espera:** `VALIDADOR_RESULT:{...}` con veredicto + doble eje + destino.
- **Cuatro áreas:** Inmersión (anti-metadata) · Narrativa (consolida D1-D5) · Temperatura efectiva (Test del Subrayado: mín. **4 subrayables/1000 palabras**) · Voz autoral (continuidad).
- **🔥 El Validador NO edita texto.** Su `Write` solo crea el reporte. La iteración la hace el Escritor con su voz.
- **Veredicto y destino:**

| Inmersión | Narrativa | Temperatura | Voz | Veredicto | Destino |
|-----------|-----------|-------------|-----|-----------|---------|
| ❌ metadata visible | * | * | * | **REPUDIADO** | Escritor reescribe sin metadata |
| ✅ | ≥ 9.0 | ≥ 8.5 | ✅ | **APROBADO** | Gate de la Ama |
| ✅ | ≥ 9.0 | < 8.5 | ✅ | **TIBIO** | Escritor reescribe con feedback caliente |
| ✅ | 7.0-8.9 | cualquiera | ✅ | **MICRO-FIX** | Escritor aplica micro-cirugías (NO Editor — no existe) |
| ✅ | < 7.0 | cualquiera | * | **REPUDIADO** | Escritor reescritura total |
| * | * | * | ❌ | **DESALINEADO** | Escritor relee voz_autoral.md y reescribe |

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

## 🚦 Reglas de Oro del Orquestador (Nivel 4)

1. **CANON MÍNIMO:** Un solo `canon_relato.md` (~2,000 palabras) por relato. No se vuelve al modelo aditivo del v4.5 que inflaba el canon a 10,000+ palabras.
2. **PROSA PURA AL LECTOR:** El archivo del capítulo nunca contiene metadata. Toda autoverificación/validación vive en `reportes/`. Metadata visible = veredicto REPUDIADO automático.
3. **VOZ PERSISTENTE:** El Escritor lee `voz_autoral.md` + capítulos previos aprobados. La voz del Cap 5 suena igual que la del Cap 1. NUNCA arranca fresco cada capítulo.
4. **ANTOLOGÍA TEXTUAL, NO ABSTRACTA:** El calentón se enseña con fragmentos de prosa a imitar (`antologia_calenton.md`), no con listas de mecanismos M1-M17.
5. **SIN EDITOR:** No existe el subagente Editor en Nivel 4. Temperatura baja → vuelve al Escritor. Narrativa con errores chicos → MICRO-FIX aplicado por el Escritor. El texto nunca pasa por una pasada que suavice.
6. **CONCEPTO LITERAL AMA = PRIORIDAD 1:** La voz literal de la Ama en `canon_relato.md` gana sobre cualquier interpretación del sistema.
7. **DESARROLLO ORGÁNICO:** No hay cuotas de palabras. La extensión la dicta el calor y la profundidad de los pivotes.
8. **GATES DE APROBACIÓN:** Esperar confirmación explícita de la Ama tras Fase 1 (canon) y tras veredicto APROBADO (capítulo final).
9. **WALKTHROUGH VIVO + PERSISTENCIA:** Nunca pasar de fase sin actualizar `walkthrough.md` y sin que los archivos existan en disco.
10. **CAPTURA DOBLE:** Tras cada cap aprobado, alimentar `voz_autoral.md` (tics/frases) y `antologia_calenton.md` (fragmentos) con las reacciones reales de la Ama.

---

## 📂 Resumen de Fases v4.7 (Nivel 4)

```
1   Composición   [Compositor]       → canon_relato.md (~2,000 palabras · Intake consolidado) → Gate Ama
2   Escritura     [Escritor-Nivel4]  → capitulo_v0.X.md (PROSA PURA, en 3-4 TRAMOS anti-truncado) + autoverificacion (reporte aparte)
    └─ tramo 1 crea archivo · tramos 2..N Edit-append (no re-emiten) · tramo N cierra + autoverif · auto-continúa, estado→walkthrough
3   Validación    [Validador]        → veredicto doble eje (Narrativa + Temperatura)
    ├ APROBADO    → Gate Ama
    ├ TIBIO       → vuelve al ESCRITOR (feedback caliente)
    ├ MICRO-FIX   → ESCRITOR aplica cirugías (NO Editor)
    ├ REPUDIADO   → ESCRITOR reescribe
    └ DESALINEADO → ESCRITOR relee voz_autoral y reescribe
CIERRE  Entrega + Captura [Orquestador+Ama] → Gold Master + alimentar voz_autoral + antologia_calenton
```

**Subagentes legacy del v4.6** (ideador, arquitecto, personajes, disenador-sensual, escritor, critico, editor, contador, centinela) viven en `.claude/agents/_legacy_v46/` como referencia histórica. **No se invocan en Nivel 4.**

---

*La Voûte no solo escribe, orquesta el deseo. Nivel 4: menos canon, más voz, cero suavizado. — v4.7*
