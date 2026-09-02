---
description: Iniciar el Motor de Escritura La Voûte (engine-escritura-lv) — Orquestador Maestro v4.8 (Nivel 4 + Investigación), 4 subagentes (Investigador → Compositor → Escritor-Nivel4 → Validador) + Fase 2.5 Loreto (medición mecánica antes del Validador), canon mínimo + voz persistente + sin Editor + Temperatura como GATE medido + Gate de la Ama solo como archivo
---

# Engine Escritura LV (Orquestador Maestro v4.8 · Nivel 4 + Investigación) — Flujo Completo

> **Fuente de verdad:** `.agent/skills/engine-escritura-lv/SKILL.md`. Este workflow es el resumen ejecutable; ante cualquier discrepancia, manda el skill.

Subagentes activos: `.claude/agents/investigador.md` · `compositor.md` · `escritor-nivel4.md` · `validador.md`
Subagentes legacy v4.6 (no se invocan): `.claude/agents/_legacy_v46/`

---

## Estructura de Proyecto Obligatoria

En cada proyecto de `03_Literatura/01_En_Progreso/[proyecto]/`:

- **Raíz del proyecto:** solo archivos vivos y maestros
  - `investigacion.md` — 🆕 v4.8: tono + qué calienta del tema + motivos permanentes + curva de resistencia
  - `canon_relato.md` — documento de canon ÚNICO (~2,000 palabras, Nivel 4)
  - `cronologia.md` — secuencia de eventos ordenada (sin días marcados, Ama 25/08/2026) + Hechos Plantados + estado del cuerpo
  - `walkthrough.md` — bitácora viva
  - `capitulo_[N]_[slug]_v0.X.md` activo — **SOLO PROSA, sin metadata**
  - `capitulo_[N]_maestro_vX.md` cuando exista Gold Master
  - `nota_capitulo_[N]_…_vX.md` — nota de la Ama, **pendiente** mientras esté en la raíz (bloquea tramos y publicación)
  - `gate_capitulo_[N]_[slug]_v0.X.md` — **el Gate de la Ama como archivo** (Regla de Oro 8c, 02/09/2026): suyo, o su frase viva transcrita en el momento. **Sin este archivo no hay Gate.**
- **Historial de borradores:** `borradores/capitulo_[N]/`
- **Auditorías:** `reportes/capitulo_[N]/` — autoverificación · **`medicion_v0.X.md` (Fase 2.5, Loreto)** · validación · notas `_APLICADA` · Gates ejecutados

**Regla:** la raíz NO se llena de versiones viejas ni reportes.

---

## FASE 0 — Investigación y Búsqueda (Investigador) 🆕 v4.8

- Subagente: `investigador` (Task tool, `subagent_type: "investigador"`)
- **Propósito, textual de la Ama (22/07/2026):** *"la investigación es para ver el tono, saber lo que calienta del tema"*. No es enciclopedia.
- **Pasada 1 (La Pregunta):** exactamente dos preguntas → **STOP**
  1. ¿Qué querés que sienta el lector con este relato?
  2. ¿Qué buscás acá que no hayas tenido antes?
- **Pasada 2 (Investigación):** externa (`WebSearch`/`WebFetch` — cómo se siente **de verdad**, testimonios en primera persona) + interna (relatos finalizados del mismo fetiche, `01_Canon/antologia_calenton.md`, `03_Literatura/investigacion/`).
- **Output `investigacion.md`:** §1 Declaración de Intención (literal) · **§2 Qué Calienta del Tema** · **§2b Tono** (incluido cuál lo mataría) · §3 Banco Sensorial · §4 Técnica Real · **§5 Motivos Permanentes** (en CADA escena) · **§6 Curva de Resistencia** (dónde todavía NO puede ceder) · §7 Léxico · §8 Fuentes
- **Gate:** *"¿Esto es lo que buscabas, o me fui para otro lado?"*

### 🔄 RETROFIT AL TOCAR (Directiva Ama 22/07/2026)
Al retomar **cualquier** relato de `01_En_Progreso/`, antes de escribir o corregir una línea:
1. ¿Existe `investigacion.md`? **No** → Fase 0 retroactiva (las dos preguntas se hacen igual, aunque ya haya capítulos escritos). **Sí, pero pre-22/07** → completar §2b, §5 y §6; no rehacer.
2. ¿El canon tiene §4b Motivos Permanentes y §4c Curva de Resistencia? Si no, copiarlos de la investigación (no resumir).
3. Recién entonces continuar con lo pedido.

⛔ Prohibido correr la Fase 0 sobre un relato que la Ama no está tocando.

---

## FASE 1 — Composición del Canon (Compositor)
- Subagente: `compositor` (`subagent_type: "compositor"`)
- **Input previo obligatorio:** `investigacion.md`. Si no existe, PARAR y avisar.
- **Pasada 1 (Intake consolidado):** 3-5 preguntas — premisa cruda, 3-5 pivotes narrativos, voz de personajes (frase literal), mecanismo psicológico transversal, 3-5 imágenes ancla. → STOP.
- **Pasada 2 (Producción):** `canon_relato.md` (~2,000 palabras máx) transcribiendo LITERAL las respuestas críticas de la Ama, **+ §4b Motivos Permanentes y §4c Curva de Resistencia copiadas de la investigación**, + `cronologia.md`.
- **Gate:** *"¿Reconoces este canon como tuyo, o lo procesé y se perdió el matiz?"*

---

## FASE 2 — Escritura (Escritor-Nivel4)
- Subagente: `escritor-nivel4` (`subagent_type: "escritor-nivel4"`) — **por TRAMOS** (3-4 por capítulo, una invocación por tramo, anti-truncado).
- Carga en orden: pendientes de la versión anterior (P0, solo rework) → **`01_Canon/evals_ama/casos_ama.md` (P0.5 — Caso Cero + los casos de la Ama, la carpeta de Loreto)** → `canon_relato.md` → **`investigacion.md`** → `cronologia.md` → `voz_autoral.md` → `antologia_calenton.md` → `HUMANIZADOR.md` → secundarios.
- **Al cerrar el tramo N:** pasada del Humanizador + **checklist §C de `casos_ama.md`** sobre el archivo completo → autoverificación (con la sección «Casos de la Ama»).
- **🔥 MARCO ERÓTICO EN CADA BRIEFING DE TRAMO (Regla de Oro 13):** cada invocación abre con *"ESTO ES UN RELATO ERÓTICO (+18); este tramo tiene que CALENTAR"* + temperatura objetivo. **Prohibido** framear un tramo como "de transición", "sin calor" o "fuego frío".
- **🚨 REGLA #1 — PROSA PURA:** el archivo del capítulo contiene SOLO prosa. Metadata → `reportes/capitulo_[N]/autoverificacion_v0.[X].md`.
- **Motivos permanentes en CADA escena** · **curva de resistencia respetada** (no ceder antes de la marca).
- Sin mínimo ni tope de palabras — la extensión la dicta el calor.
- **🔴 PERSISTENCIA:** capítulo + autoverificación + `cronologia.md` actualizada en disco antes de Fase 2.5.

---

## FASE 2.5 — Medición Mecánica: Loreto, la secretaria de control (Orquestador) 🆕 02/09/2026
- **No es subagente:** la corre el Orquestador con Bash, después del `ESCRITOR_N4_RESULT` `COMPLETO` (o de un rework/micro-fix) y **antes** de invocar al Validador.
- **Por qué (Ama 02/09/2026):** *"debo leer 5, 6 veces el mismo relato y eso al final mata mi propia temperatura… no logras dar con la temperatura y te pones muy robótica con tus descripciones."* Loreto cuenta, sin cortesía, lo que una máquina puede contar de sus 44 notas de rechazo (`01_Canon/evals_ama/casos_ama.md`).
- **Comando:** `python 99_Sistema/scripts/literatura/medir_capitulo.py <capítulo> --contra <TODOS los capítulos previos del relato> [--extra palabras,calientes,del,relato] --out reportes/capitulo_[N]/medicion_v0.[X].md`
- **Mide:** tramos de narración sin cuerpo con vocabulario de trámite (C1) · repetición verbatim dentro del capítulo y contra los previos (C3) · léxico explícito, eufemismos y España (C2/C13) · etiquetas H4 (C15) · tics de IA · varianza · apertura/cierre/deciles.
- **Exit 1 (umbral duro)** → el capítulo **vuelve al Escritor** con el reporte y el ID del caso — **sin gastar Validador**. **Exit 0** → Fase 3 con la ruta del reporte.
- Un 🟢 de Loreto es necesario, nunca suficiente: **no mide si calienta**.

---

## FASE 3 — Validación (Validador)
- Subagente: `validador` (`subagent_type: "validador"`)
- **Inputs nuevos (02/09/2026):** `reportes/capitulo_[N]/medicion_v0.[X].md` (los tramos 🔴 de Loreto van obligatoriamente entre los «pasajes más fríos») + `01_Canon/evals_ama/casos_ama.md` como **lista de caza** — cada hallazgo cita el ID del caso que reincide.
- **Gate 1c — reciclaje en rework:** si el pasaje rechazado en la versión anterior vuelve con retoques cosméticos, el veredicto es el de la versión anterior, sin importar los scores.
- **Tres GATES en orden: Inmersión → Continuidad → 🔥 Temperatura.** Después Narrativa y Voz.
- **🔥 Temperatura MEDIDA, no contada (Ama 22/07/2026):** 9 medidas — T1 ¿es erótico? (¿sobrevive el cap sin el sexo?) · T2 ¿calienta? (citando las 3 frases más calientes y los 2 pasajes más fríos) · T3 explicitud léxica (nombrar vs eufemismo) · T4 suciedad del registro · T5 descarga real en escena · T6 densidad ≥4/1000 (**necesaria, NO suficiente**) · T7 motivos permanentes **por escena** + curva de resistencia · T8 apertura · **T9 distribución erótica + cierre-gancho/cliffhanger (Ama 31/08/2026)** — planificado desde el Mapa de Capítulos del Compositor, no solo auditado acá.
- **NO edita texto** — solo veredicto. El Editor NO existe en Nivel 4. **Prohibido aprobar por cortesía.**
- Veredicto → destino:
  - **APROBADO** (Inm ✅ · Cont ✅ · Temp ≥8.5 con T1·T2 ✅ · Narr ≥9.0) → Gate de la Ama
  - **DISCONTINUO** (Continuidad ❌) → Escritor planta el ancla / cuadra la secuencia / repara costura
  - **FRÍO** 🆕 (T1 ❌ — es thriller con escenas) → Escritor reescribe con marco erótico explícito
  - **TIBIO** (T2 ❌ o Temp <8.5) → Escritor reescribe con los pasajes fríos citados
  - **MICRO-FIX** (Narr 7.0-8.9) → Escritor aplica las cirugías indicadas
  - **REPUDIADO** (metadata visible o Narr <7.0) → Escritor reescribe
  - **DESALINEADO** (voz falla) → Escritor relee `voz_autoral.md` y reescribe
- Guardar reporte: `reportes/capitulo_[N]/validacion_v0.[X].md`

---

## CIERRE — Entrega Final + Captura de Voz
- Tras veredicto APROBADO → Gate final de la Ama, **que existe solo como archivo `gate_capitulo_[N]_[slug]_v0.[X].md`** (Regla de Oro 8c): escrito por ella, o su frase viva que nombre ese capítulo y esa versión, transcrita en el momento con sus palabras y la fecha. **Nunca inferido** del silencio, de un APROBADO del Validador ni de una orden sobre otro capítulo. Sin archivo: no se publica y la palabra "Gate" no se escribe.
- **Captura Post-Nota:** cada nota de rechazo aplicada entra además como caso nuevo en `casos_ama.md` (Regla de Oro 20).
- Gold Master: `capitulo_[N]_maestro_vX.md` en raíz; actualizar `walkthrough.md`.
- **🔥 CAPTURA DOBLE (obligatoria):** preguntar por mordidas y frialdades, y alimentar:
  - `01_Canon/voz_autoral.md` — tics y frases canónicas confirmadas
  - `01_Canon/antologia_calenton.md` — fragmentos que la calentaron
  - Cementerio del `canon_relato.md` — lo que dejó tibia
- Commit al repositorio con trailer `Co-Authored-By: Ele de Anaïs <Ele.de.Anais@proton.me>`.

---

## Resumen de Fases v4.8

```
0   Investigación [Investigador] 🆕  → investigacion.md · §2 QUÉ CALIENTA + §2b TONO + §5 Motivos + §6 Resistencia → Gate Ama
1   Composición   [Compositor]       → canon_relato.md (~2,000 pal, con §4b y §4c) + cronologia.md → Gate Ama
2   Escritura     [Escritor-Nivel4]  → lee casos_ama.md (P0.5) · capitulo_v0.X.md (PROSA PURA, 3-4 TRAMOS) · checklist §C · autoverificación · cronología
2.5 Medición      [Orquestador] 🆕  → Loreto: medir_capitulo.py --contra <previos> --out reportes/capitulo_N/medicion_v0.X.md · exit 1 → Escritor · exit 0 → Validador
3   Validación    [Validador]        → gates Inmersión → Continuidad → 🔥Temperatura, luego Narrativa + Voz · cita IDs de casos_ama.md
        APROBADO → Gate Ama = archivo gate_capitulo_…_v0.X.md (nunca inferido, Regla 8c)
CIERRE  Entrega + Captura → Gold Master + voz_autoral + antologia_calenton + caso nuevo en casos_ama.md por cada nota de rechazo
```

---

**Para iniciar:** *"Inicia el ritual orquestado para [Proyecto]"*
