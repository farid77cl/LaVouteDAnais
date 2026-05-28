---
description: Iniciar el Motor de Escritura La Voûte (engine-escritura-lv) — Orquestador Maestro v4.7 (Nivel 4), 3 subagentes consolidados (Compositor → Escritor-Nivel4 → Validador), canon mínimo + voz persistente + sin Editor
---

# Engine Escritura LV (Orquestador Maestro v4.7 · Nivel 4) — Flujo Completo

Skill de referencia: `.agent/skills/engine-escritura-lv/SKILL.md`
Subagentes activos: `.claude/agents/compositor.md` · `escritor-nivel4.md` · `validador.md`
Subagentes legacy v4.6 (no se invocan): `.claude/agents/_legacy_v46/`

---

## Estructura de Proyecto Obligatoria

En cada proyecto de `03_Literatura/01_En_Progreso/[proyecto]/`, el orquestador DEBE mantener este orden:

- **Raíz del proyecto:** solo archivos vivos y maestros
  - `walkthrough.md` — bitácora viva
  - `canon_relato.md` — documento de canon ÚNICO (~2,000 palabras, Nivel 4)
  - `capitulo_[N]_[slug]_v0.X.md` activo — **SOLO PROSA, sin metadata**
  - `capitulo_[N]_maestro_vX.md` cuando exista Gold Master
- **Historial de borradores:** `borradores/capitulo_[N]/` — versiones desplazadas (`v0.1`, `v0.2`, etc.)
- **Auditorías:** `reportes/capitulo_[N]/` — autoverificación del Escritor + validación del Validador

**Regla:** la raíz NO se llena de versiones viejas ni reportes. El capítulo activo (prosa pura) vive en raíz; su metadata y auditorías viven en carpetas.

---

## FASE 1 — Composición del Canon (Compositor)
- Subagente: `compositor` (Task tool, `subagent_type: "compositor"`)
- **Pasada 1 (Intake consolidado):** 3-5 preguntas — premisa cruda, 3-5 pivotes narrativos, voz de personajes (frase literal), mecanismo psicológico transversal, 3-5 imágenes ancla. → STOP, espera respuestas.
- **Pasada 2 (Producción):** Construye `canon_relato.md` (~2,000 palabras máx) transcribiendo LITERAL las respuestas críticas de la Ama. Reemplaza concepto + arco + personajes + mapa erótico + mecanismo de calentón (5 documentos del v4.6 colapsados en 1).
- **Gate:** *"¿Reconoces este canon como tuyo, o lo procesé y se perdió el matiz?"*

---

## FASE 2 — Escritura (Escritor-Nivel4)
- Subagente: `escritor-nivel4` (Task tool, `subagent_type: "escritor-nivel4"`)
- Carga en orden de prioridad:
  1. `canon_relato.md` (la voz literal de la Ama gana)
  2. `01_Canon/voz_autoral.md` (voz persistente acumulada)
  3. `01_Canon/antologia_calenton.md` (antología textual a imitar)
  4. Secundarios: `LIBRO_MAESTRO_ESCRITURA.md`, guías de arquitectura erótica según tema, capítulos previos APROBADOS
- **🚨 REGLA #1 — PROSA PURA:** El archivo del capítulo contiene SOLO prosa. Autoverificación/metadata va a `reportes/capitulo_[N]/autoverificacion_v0.[X].md`.
- Sin mínimo arbitrario de palabras — la extensión la dicta el calor y el desarrollo de los pivotes.
- **🔴 PERSISTENCIA:** Guardar capítulo (prosa) + autoverificación (metadata) en disco antes de Fase 3.

---

## FASE 3 — Validación (Validador)
- Subagente: `validador` (Task tool, `subagent_type: "validador"`)
- Evalúa 4 áreas: Inmersión (anti-metadata) · Narrativa (D1-D5 consolidadas) · Temperatura efectiva (mín. 4 subrayables/1000 palabras) · Voz autoral (continuidad).
- **NO edita texto** — solo emite veredicto. El Editor NO existe en Nivel 4.
- Veredicto → destino:
  - **APROBADO** (Narr ≥9.0 + Temp ≥8.5) → Gate de la Ama
  - **TIBIO** (Narr ≥9.0 + Temp <8.5) → vuelve al Escritor con feedback caliente
  - **MICRO-FIX** (Narr 7.0-8.9) → Escritor aplica las cirugías indicadas
  - **REPUDIADO** (metadata visible o Narr <7.0) → Escritor reescribe
  - **DESALINEADO** (voz falla) → Escritor relee voz_autoral.md y reescribe
- Guardar reporte: `reportes/capitulo_[N]/validacion_v0.[X].md`

---

## CIERRE — Entrega Final + Captura de Voz
- Tras veredicto APROBADO → Gate final de la Ama.
- Gold Master: `capitulo_[N]_maestro_vX.md` en raíz; actualizar `walkthrough.md`.
- **🔥 CAPTURA DOBLE (obligatoria):** preguntar a la Ama por mordidas y frialdades, y alimentar:
  - `01_Canon/voz_autoral.md` — tics y frases canónicas confirmadas
  - `01_Canon/antologia_calenton.md` — fragmentos de prosa que la calentaron
  - Cementerio del `canon_relato.md` — lo que dejó tibia
- Commit automático al repositorio.

---

## Resumen de Fases v4.7 (Nivel 4)

```
1   Composición   [Compositor]       → canon_relato.md (~2,000 palabras) → Gate Ama
2   Escritura     [Escritor-Nivel4]  → capitulo_v0.X.md (PROSA PURA) + autoverificacion (aparte)
3   Validación    [Validador]        → veredicto doble eje (sin Editor)
CIERRE  Entrega + Captura → Gold Master + voz_autoral + antologia_calenton
```

---

**Para iniciar:** *"Inicia el ritual orquestado para [Proyecto]"*
