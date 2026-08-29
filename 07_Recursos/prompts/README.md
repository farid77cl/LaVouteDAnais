# 📝 System Prompts — Pipeline Literario (ARCHIVO, era v4.5/v4.6)

> 🔒 **DEPRECADO 29/08/2026 — el pipeline vigente vive en [`../../.agent/skills/engine-escritura-lv/SKILL.md`](../../.agent/skills/engine-escritura-lv/SKILL.md).** Estos 12 prompts describen los agentes del **Engine v4.5/v4.6 (Nivel 3)**, sustituidos el 28/05/2026 por Nivel 4. Este README los presentaba como si siguieran corriendo.
>
> **El pipeline vivo es v4.8, con cuatro subagentes:** `investigador` → `compositor` → `escritor-nivel4` → `validador`, definidos en [`../../.claude/agents/`](../../.claude/agents/) y especificados en [`../../.agent/skills/engine-escritura-lv/SKILL.md`](../../.agent/skills/engine-escritura-lv/SKILL.md).
>
> Sus antecesores archivados —los mismos roles de aquí, ya como definición de agente— viven en [`../../.claude/agents/_legacy_v46/`](../../.claude/agents/_legacy_v46/) y **no deben invocarse**.

**Qué sigue valiendo de esta carpeta:** son el registro de cómo se pensaba cada rol antes del colapso 9→3. `mentor.md`, `orquestador.md` y `termometro.md` ni siquiera tienen equivalente moderno — el diagnóstico de por qué desaparecieron está en [`../../01_Canon/REDISENO_ENGINE_ESCRITURA_v4.6.md`](../../01_Canon/REDISENO_ENGINE_ESCRITURA_v4.6.md).

---

*Material histórico. Ejecutados como roles dentro de Claude Code en la era v4.5/v4.6.*

> **Histórico:** Estos prompts originalmente alimentaban un pipeline Ollama + `web_interface/server.py`. Esa infraestructura fue desmantelada hace meses. Hoy cada prompt funciona como **definición de rol** que el operador (Claude) asume manualmente al invocar la fase correspondiente.

## Agentes

| Archivo | Agente | Función |
|---------|--------|---------|
| `ideador.md` | 🧠 Ideador | Expande premisas en propuestas narrativas |
| `arquitecto.md` | 📐 Arquitecto | Estructura arcos argumentales + Línea de Tiempo Maestra |
| `personajes.md` | 🎭 Personajes | Fichas psicológicas, triggers y biblia visual |
| `disenador_sensual.md` | 🔥 Diseñador Sensual | **Fase 3.3** — Mapa erótico general + específico por capítulo (v2.0) |
| `escritor.md` | ✍️ Escritor | Prosa erótica explícita (mín 3000 palabras) |
| `critico.md` | 🔍 Crítico | Evalúa tensión, ritmo y sensorialidad (D1-D6) |
| `termometro.md` | 🌡️ Termómetro | **Fase 5.5** — Auditoría post-escritura de temperatura vs. mapa específico |
| `centinela.md` | 🛡️ Centinela | Control de continuidad temporal y de arco |
| `editor.md` | ✂️ Editor | Corrección y reescritura manteniendo voz |
| `contador.md` | 📊 Contador | Verificación de extensión, formato y vocabulario |

## Pipeline

```
Ideador → Arquitecto → Personajes → 🔥 Diseñador Sensual (general + cap N)
        → Escritor (cap N) → [🔍 Crítico + 🌡️ Termómetro + 🛡️ Centinela]
        → ✂️ Editor → 📊 Contador → maestro
```

**Diseñador Sensual (Fase 3.3) — v2.0:**
- Primera vez: produce `mapa_erotico_v1.md` (general) + `mapa_erotico_cap1_v1.md` (específico).
- Capítulo siguiente: produce solo `mapa_erotico_cap[N]_v1.md` reusando el general aprobado.
- El Escritor lee AMBOS antes de escribir.

**Crítico + Termómetro + Centinela (Fase 5)** operan en paralelo sobre el borrador. El Editor recibe los tres reportes en un único ciclo de cirugías.

## Uso

Cada `.md` se carga como contexto en Claude Code cuando se asume el rol correspondiente. No hay servicio que los lea automáticamente — el operador invoca la fase, carga el prompt y opera.

## Directiva Común

Todos los prompts incluyen la directiva **SIN CENSURA** para contenido adulto explícito.
