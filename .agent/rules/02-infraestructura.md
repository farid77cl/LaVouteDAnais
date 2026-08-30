# 🏗️ REGLA 2: INFRAESTRUCTURA ACTIVA

El sistema literario y visual funciona **dentro de Claude Code**, sin servicios locales adicionales.

### Lo que ya NO existe (desmantelado hace meses)

- ❌ `web_interface/` (Flask `:4000`) — eliminado
- ❌ Ollama Docker (`:11434`) — eliminado
- ❌ Contenedores `voute_n8n`, `voute_postgres`, `voute_redis`, `voute_biblioteca`, `voute_pandoc` — eliminados
  > ⚠️ **`voute_n8n` ≠ el n8n de hoy.** Aquel murió. La Ama tiene **otra** instancia viva, en otra máquina — ver §n8n más abajo. Leer solo esta línea lleva a concluir que n8n no existe, y es falso.
- ❌ Modelos locales (`dolphin-mistral`, `dolphin-llama3`, `qwen2.5`, `llama3.2`) — fuera de uso

Cualquier referencia a estos servicios en scripts antiguos (`99_Sistema/scripts/bat/`, `99_Sistema/scripts/setup/`) es **legacy histórico** — no se ejecuta.

### 🔌 n8n — instancia viva (medido 29-30/08/2026)

**No es el `voute_n8n` desmantelado.** Es una instancia nueva de la Ama, en una Raspberry (DietPi) con Docker, expuesta con Tailscale Funnel.

| Dato | Valor | Estado |
|---|---|---|
| Por Tailscale | `https://dietpi.tail05c49d.ts.net` | ✅ **viva** — responde en 0,58 s |
| En red local | `http://192.168.1.200:5678` | — |
| Autenticación REST | cabecera `X-N8N-API-KEY` | — |
| API key en `credenciales-privadas.txt` | 🔴 **devuelve 401** | revocada, o la instancia se reinstaló |
| Workflows en la instancia | ❓ ilegibles sin key válida | — |
| Endpoint MCP (`/mcp/ayunka`) | 🔴 **404** (también `/mcp-test/` y `/webhook/`) | no activo |
| Definiciones locales | `C:\Users\farid\negocio\n8n\` — **21 workflows**, uno con nodo `mcpTrigger` (ruta `ayunka`, **0 herramientas**) | fuera de este repo |

> 🔴 **La API REST de n8n NO dispara workflows** — solo administra (listar, crear, activar, leer ejecuciones). Para dispararlos desde fuera hace falta un **nodo Webhook por workflow, activado**. Confundir ambas puertas es la trampa documentada por la Ama.

**Para revivirlo:** generar key nueva en *Settings → n8n API* y reimportar los workflows (`PUT` para reemplazar; `POST` duplica — así se llegó a tener 37 en vez de 9).

**Detalle completo:** `LV-App/.planning/reference/n8n-conexion.md` (otro repo, privado). Las credenciales viven en `G:\Otros ordenadores\Mi portátil\negocio-accesorios-3d-costura\credenciales-privadas.txt` — **nunca en este repo, que es público**.

### Lo que SÍ funciona hoy

| Componente | Ubicación | Función |
|------------|-----------|---------|
| **Claude Code** | terminal / VSCode extension | Motor de ejecución de todos los agentes (literarios y visuales) |
| **System prompts** | `07_Recursos/prompts/*.md` | Definición de rol y conducta de cada agente; Claude los carga manualmente al asumir cada rol |
| **Skills** | `.agent/skills/` (proyecto) + `~/.claude/skills/` (global) | Procedimientos reutilizables (engine-escritura-lv, ele-outfit-engine, etc.) |
| **Generación visual** | Antigravity / IA externa | Disparado bajo demanda, no requiere infraestructura local |

### Reglas operativas

1. **Cero levantamiento de servicios.** Si un script `.bat` o `.ps1` intenta arrancar Docker u Ollama, está obsoleto.
2. **Roles via system prompts.** Para invocar un agente (Ideador, Crítico, Termómetro, etc.), el operador carga el prompt correspondiente como contexto y asume el rol.
3. **Persistencia en archivos.** Todo output canónico se guarda como `.md` en su carpeta de proyecto; no hay servicios de cola ni base de datos.

*Actualizado: 13/05/2026 — sincronizado con la realidad operativa post-Ollama.*
