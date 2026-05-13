# 📝 System Prompts — Pipeline Literario

System prompts para los agentes que componen el pipeline de escritura de **La Voûte d'Anaïs**, ejecutados como roles dentro de Claude Code.

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
