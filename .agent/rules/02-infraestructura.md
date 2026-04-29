# 🏗️ REGLA 2: INFRAESTRUCTURA ACTIVA

### Servicios de Escritura (La Voûte Editor)

| Servicio | Puerto | Cómo Levantar |
|----------|--------|--------------|
| **La Voûte Editor** | `:4000` | `cd web_interface && python server.py` |
| **Ollama** (Docker) | `:11434` | `docker start voute_ollama` |

### Modelos LLM Configurados

| Agente Pipeline | Modelo | Tipo |
|----------------|--------|------|
| Ideador, Personajes | `dolphin-mistral:7b` | 🔓 Sin censura |
| Escritor, Editor | `dolphin-llama3:8b` | 🔓 Sin censura |
| Arquitecto, Crítico | `qwen2.5:7b` | Estándar |
| Contador | `llama3.2:3b` | Ligero |

### Docker: Solo lo Necesario

- **Mantener activo:** Ollama (`voute_ollama`)
- **Pausar si no se usan:** n8n, PostgreSQL, Redis, Biblioteca, Pandoc
- Comando para pausar innecesarios: `docker stop voute_n8n voute_postgres voute_redis voute_biblioteca voute_pandoc`
