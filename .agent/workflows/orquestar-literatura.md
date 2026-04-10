---
description: Iniciar el flujo de producción literaria Orquestador Maestro v4.3 — 8 fases completas
---

# Orquestador Literario v4.3 — Flujo Completo

Skill de referencia: `.agent/skills/orquestador-literario/SKILL.md`
Prompts de agentes: `07_Recursos/prompts/`

---

## FASE 1 — Concepción
- Capturar la idea/fetiche/premisa de la Ama sin interpretación.
- Crear: `03_Literatura/01_En_Progreso/[proyecto]/concepto.md`
- Crear: `03_Literatura/01_En_Progreso/[proyecto]/walkthrough.md`
- **Gate:** *"¿Aprobamos el concepto, Ama?"*

---

## FASE 2 — Arquitectura (Arco Maestro)
- Agente: `07_Recursos/prompts/arquitecto.md`
- Aplicar Protocolo Alan Moore (rimas narrativas, simetrías).
- Crear: `arco_maestro_vX.md` + `linea_de_tiempo_maestra.md`
- **⚠️ Una vez aprobado, el arco es INVIOLABLE. El Escritor no puede desviarse sin Gate.**
- **Gate:** *"¿Aprobamos el arco y la línea de tiempo, Ama?"*

---

## FASE 3 — Personajes
- Agente: `07_Recursos/prompts/personajes.md`
- Producir fichas tridimensionales: psicología, triggers, curva de vocabulario por etapa.
- Crear: `personajes_maestro_vX.md`
- **Gate:** *"¿Aprobamos las fichas, Ama?"*

---

## FASE 4 — Escritura
- Agente: `07_Recursos/prompts/escritor.md`
- Cargar obligatoriamente antes de escribir:
  1. `01_Canon/LIBRO_MAESTRO_ESCRITURA.md`
  2. `.agent/skills/escritura-voûte/resources/CODEX_PSICOLOGICO.md`
  3. `.agent/skills/escritura-voûte/resources/GUIA_FETICHISTA.md`
  4. `.agent/skills/escritura-voûte/resources/MEMORIA_ERRORES.md`
  5. `arco_maestro_vX.md` del proyecto
  6. `personajes_maestro_vX.md` del proyecto
- Mínimo 3,000 palabras. Sin límite artificial superior.
- **🔴 PERSISTENCIA OBLIGATORIA:** Guardar en disco ANTES de pasar a Fase 5:
  - Ruta: `03_Literatura/01_En_Progreso/[proyecto]/capitulo_[N]_[slug].md`
  - Sin archivo guardado = Fase 4 no completada.

---

## FASE 5 — Auditoría (Crítico + Contador)
- Agentes: `07_Recursos/prompts/critico.md` + `07_Recursos/prompts/contador.md`
- Input: archivo guardado en disco + arco aprobado + fichas
- Escala: `< 7.0` REPUDIADO · `7.0-8.9` CIRUGÍA · `9.0-9.4` OBSERVACIONES · `9.5+` EXCELENCIA

---

## FASE 6 — Bucle de Refinamiento (Editor ↔ Crítico)
- Agente: `07_Recursos/prompts/editor.md`
- Editor aplica cirugías → vuelve al Crítico → repite hasta 9.5+ o 3 rondas máximo.
- Si en 3 rondas no alcanza 9.0 → escalar a la Ama.

---

## FASE 7 — Centinela (Continuidad)
- Agente: `07_Recursos/prompts/centinela.md`
- Verificar: coherencia temporal, integridad del arco, deriva de vocabulario.
- Si emite `RECHAZADO` → bloquea el avance hasta corregir.

---

## FASE 8 — Entrega Final
- Guardar versión Gold Master: `capitulo_[N]_maestro_vX.md`
- Actualizar `walkthrough.md` con estado final.
- **Gate:** *"¿Aprobamos el capítulo, Ama?"*
- Commit automático al repositorio.

---

**Para iniciar:** *"Inicia el ritual orquestado para [Proyecto]"*
