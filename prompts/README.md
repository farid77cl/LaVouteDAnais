# 📝 System Prompts — Pipeline Literario

System prompts para los 7 agentes LLM que componen el pipeline de escritura de La Voûte Editor.

## Agentes

| Archivo | Agente | Modelo | Función |
|---------|--------|--------|---------|
| `ideador.md` | 🧠 Ideador | dolphin-mistral:7b | Expande premisas en propuestas narrativas |
| `arquitecto.md` | 📐 Arquitecto | qwen2.5:7b | Estructura arcos argumentales (3 actos) |
| `personajes.md` | 🎭 Personajes | dolphin-mistral:7b | Fichas psicológicas y de transformación |
| `escritor.md` | ✍️ Escritor | dolphin-llama3:8b | Prosa erótica explícita (mín 3000 palabras) |
| `critico.md` | 🔍 Crítico | qwen2.5:7b | Evalúa tensión, ritmo y sensorialidad |
| `editor.md` | ✂️ Editor | dolphin-llama3:8b | Corrección y reescritura manteniendo voz |
| `contador.md` | 📊 Contador | llama3.2:3b | Verificación de extensión y formato |

## Uso

Estos archivos se cargan automáticamente por `web_interface/server.py` como `system prompt` para cada agente vía Ollama.

## Directiva Común

Todos los prompts incluyen la directiva **SIN CENSURA** para contenido adulto explícito.
