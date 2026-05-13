# 📝 System Prompts — Pipeline Literario

System prompts para los agentes LLM que componen el pipeline de escritura de La Voûte Editor.

## Agentes

| Archivo | Agente | Modelo | Función |
|---------|--------|--------|---------|
| `ideador.md` | 🧠 Ideador | dolphin-mistral:7b | Expande premisas en propuestas narrativas |
| `arquitecto.md` | 📐 Arquitecto | qwen2.5:7b | Estructura arcos argumentales + Línea de Tiempo Maestra |
| `personajes.md` | 🎭 Personajes | dolphin-mistral:7b | Fichas psicológicas, triggers y biblia visual |
| `disenador_sensual.md` | 🔥 Diseñador Sensual | dolphin-mistral:7b | **Fase 3.3** — Diseño pre-escritura del mapa erótico (curva de temperatura, fetiches, dosificación) |
| `escritor.md` | ✍️ Escritor | dolphin-llama3:8b | Prosa erótica explícita (mín 3000 palabras) |
| `critico.md` | 🔍 Crítico | qwen2.5:7b | Evalúa tensión, ritmo y sensorialidad (D1-D6) |
| `termometro.md` | 🌡️ Termómetro | qwen2.5:7b | **Fase 5.5** — Auditoría post-escritura de temperatura erótica vs. mapa erótico |
| `centinela.md` | 🛡️ Centinela | qwen2.5:7b | Control de continuidad temporal y de arco |
| `editor.md` | ✂️ Editor | dolphin-llama3:8b | Corrección y reescritura manteniendo voz |
| `contador.md` | 📊 Contador | llama3.2:3b | Verificación de extensión, formato y vocabulario |

## Pipeline

```
Ideador → Arquitecto → Personajes → 🔥 Diseñador Sensual → Escritor → [Crítico + 🌡️ Termómetro + Centinela] → Editor → Contador
```

**Diseñador Sensual (Fase 3.3)** corre antes del Escritor — produce `mapa_erotico_v1.md` que define la curva de temperatura objetivo.
**Crítico, Termómetro y Centinela (Fase 5)** operan en paralelo sobre el borrador del Escritor. El Editor recibe los tres reportes antes de producir la versión final.

## Uso

Estos archivos se cargan automáticamente por `web_interface/server.py` como `system prompt` para cada agente vía Ollama.

## Directiva Común

Todos los prompts incluyen la directiva **SIN CENSURA** para contenido adulto explícito.
