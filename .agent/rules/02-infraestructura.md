# 🏗️ REGLA 2: INFRAESTRUCTURA ACTIVA

El sistema literario y visual funciona **dentro de Claude Code**, sin servicios locales adicionales.

### Lo que ya NO existe (desmantelado hace meses)

- ❌ `web_interface/` (Flask `:4000`) — eliminado
- ❌ Ollama Docker (`:11434`) — eliminado
- ❌ Contenedores `voute_n8n`, `voute_postgres`, `voute_redis`, `voute_biblioteca`, `voute_pandoc` — eliminados
- ❌ Modelos locales (`dolphin-mistral`, `dolphin-llama3`, `qwen2.5`, `llama3.2`) — fuera de uso

Cualquier referencia a estos servicios en scripts antiguos (`99_Sistema/scripts/bat/`, `99_Sistema/scripts/setup/`) es **legacy histórico** — no se ejecuta.

### Lo que SÍ funciona hoy

| Componente | Ubicación | Función |
|------------|-----------|---------|
| **Claude Code** | terminal / VSCode extension | Motor de ejecución de todos los agentes (literarios y visuales) |
| **System prompts** | `07_Recursos/prompts/*.md` | Definición de rol y conducta de cada agente; Claude los carga manualmente al asumir cada rol |
| **Skills** | `.agent/skills/` (proyecto) + `~/.claude/skills/` (global) | Procedimientos reutilizables (escritura-voûte, ele-outfit-engine, etc.) |
| **Generación visual** | Antigravity / IA externa | Disparado bajo demanda, no requiere infraestructura local |

### Reglas operativas

1. **Cero levantamiento de servicios.** Si un script `.bat` o `.ps1` intenta arrancar Docker u Ollama, está obsoleto.
2. **Roles via system prompts.** Para invocar un agente (Ideador, Crítico, Termómetro, etc.), el operador carga el prompt correspondiente como contexto y asume el rol.
3. **Persistencia en archivos.** Todo output canónico se guarda como `.md` en su carpeta de proyecto; no hay servicios de cola ni base de datos.

*Actualizado: 13/05/2026 — sincronizado con la realidad operativa post-Ollama.*
