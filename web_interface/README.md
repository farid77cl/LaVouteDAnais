# La Voûte Editor — Documentación Técnica

> *El pipeline literario de 7 agentes LLM con interfaz web premium.*

---

## 📋 Índice

- [¿Qué es?](#qué-es)
- [¿Por qué existe?](#por-qué-existe)
- [Arquitectura](#arquitectura)
- [Cómo funciona](#cómo-funciona)
- [Archivos del proyecto](#archivos-del-proyecto)
- [Modelos LLM](#modelos-llm)
- [API Endpoints](#api-endpoints)
- [Cómo levantar](#cómo-levantar)
- [Cómo usar](#cómo-usar)
- [Historial de decisiones](#historial-de-decisiones)
- [Pendientes](#pendientes)

---

## ¿Qué es?

**La Voûte Editor** es una interfaz web que orquesta 7 agentes LLM locales (vía Ollama) para generar relatos eróticos paso a paso, con intervención humana en cada checkpoint. Cada agente tiene un rol específico y un system prompt dedicado.

## ¿Por qué existe?

### El problema
Originalmente se diseñó un pipeline en **n8n** (herramienta de workflows visuales). Funcionaba, pero:
- La interfaz de n8n era técnica y "fea" para un proceso creativo
- No permitía editar las salidas fácilmente entre agentes
- Los checkpoints humanos eran incómodos (nodos de "Wait" en n8n)

### La decisión (27/Feb/2026)
Se decidió construir una **interfaz web propia** con:
- Streaming en tiempo real (ver al agente "pensar")
- Edición directa del texto antes de aprobarlo
- Diseño premium con la estética de La Voûte (negro, oro, púrpura)
- Botón para detener generación y guardar progreso en cualquier momento

### ¿Por qué Flask y no Node.js?
`npm` no estaba disponible en el sistema Windows del usuario. Python sí estaba instalado, así que se usó **Flask** como backend. La elección fue pragmática, no arquitectónica.

---

## Arquitectura

```
┌───────────────────────────────────────────────┐
│                  USUARIO                       │
│         http://localhost:4000                  │
│    ┌──────────────────────────────────┐       │
│    │    Frontend (HTML/CSS/JS)         │       │
│    │    - index.html (estructura)      │       │
│    │    - style.css  (estética Voûte)  │       │
│    │    - app.js     (máquina estados) │       │
│    └──────────┬───────────────────────┘       │
│               │ fetch() con streaming          │
│    ┌──────────▼───────────────────────┐       │
│    │    Backend (Flask - server.py)     │       │
│    │    - Lee prompts de ../prompts/    │       │
│    │    - Proxy SSE a Ollama           │       │
│    │    - Guarda .md en 03_En_progreso │       │
│    └──────────┬───────────────────────┘       │
│               │ HTTP POST (stream: true)       │
│    ┌──────────▼───────────────────────┐       │
│    │    Ollama (Docker :11434)          │       │
│    │    - dolphin-mistral:7b           │       │
│    │    - dolphin-llama3:8b            │       │
│    │    - qwen2.5:7b                   │       │
│    │    - llama3.2:3b                  │       │
│    └──────────────────────────────────┘       │
└───────────────────────────────────────────────┘
```

### Flujo de datos

1. **Usuario** escribe premisa en textarea
2. **app.js** envía POST a `/api/agent/ideador` con la premisa
3. **server.py** carga `prompts/ideador.md` como system prompt
4. **server.py** envía a Ollama con `stream: true`
5. Ollama genera tokens uno a uno → Flask los reenvía como SSE
6. **app.js** los muestra en el textarea de salida en tiempo real
7. **Usuario** edita, aprueba o regenera
8. El texto aprobado se usa como contexto para el siguiente agente
9. Repite para los 7 agentes

---

## Cómo funciona

### Los 7 Agentes (en orden)

| # | Agente | Modelo | Qué hace | System Prompt |
|---|--------|--------|----------|---------------|
| 1 | **Ideador** | dolphin-mistral:7b | Expande la premisa en una propuesta narrativa | `prompts/ideador.md` |
| 2 | **Arquitecto** | qwen2.5:7b | Estructura el arco argumental (3 actos, clímax) | `prompts/arquitecto.md` |
| 3 | **Personajes** | dolphin-mistral:7b | Fichas psicológicas, físicas y de transformación | `prompts/personajes.md` |
| 4 | **Escritor** | dolphin-llama3:8b | Escribe el capítulo completo (mín 3000 palabras) | `prompts/escritor.md` |
| 5 | **Crítico** | qwen2.5:7b | Evalúa tensión, ritmo, sensorialidad | `prompts/critico.md` |
| 6 | **Editor** | dolphin-llama3:8b | Aplica correcciones del crítico y reescribe | `prompts/editor.md` |
| 7 | **Contador** | llama3.2:3b | Verifica extensión y formato final | `prompts/contador.md` |

### Checkpoints humanos

En **cada paso** el usuario puede:
- **Editar** el texto directamente en el textarea
- **Re-generar** si no le gusta la salida
- **Detener** la generación a mitad de camino (AbortController)
- **Guardar** el progreso actual como `.md`
- **Aprobar** y pasar al siguiente agente

### Agentes auto-invocados vs manuales

- **Manuales** (usuario debe hacer clic): Ideador, Escritor
- **Auto-invocados** (se disparan automáticamente tras aprobar): Arquitecto, Personajes, Crítico, Contador

---

## Archivos del proyecto

```
web_interface/
├── server.py              # Backend Flask (135 líneas)
│   ├── MODELS{}           # Mapeo agente → modelo Ollama
│   ├── load_prompt()      # Lee ../prompts/{agente}.md
│   ├── /api/agent/<name>  # Endpoint SSE streaming
│   └── /api/save          # Guarda estado como .md
├── templates/
│   └── index.html         # Estructura HTML (7 tarjetas, progress tracker)
└── static/
    ├── style.css           # Estética La Voûte (Cinzel, gold, glassmorphism)
    └── app.js              # Máquina de estados JS (streaming, abort, save)

prompts/                   # System prompts (archivos .md)
├── ideador.md
├── arquitecto.md
├── personajes.md
├── escritor.md
├── critico.md
├── editor.md
└── contador.md
```

---

## Modelos LLM

### ¿Por qué Dolphin?

Los modelos estándar (Qwen, Llama) tienen filtros de seguridad que censuran contenido erótico explícito. Los modelos **Dolphin** son versiones "uncensored" entrenadas sin alignment restrictivo.

| Modelo | Tamaño | Uso | RAM aprox |
|--------|--------|-----|-----------|
| `dolphin-mistral:7b` | 4.1 GB | Brainstorming y personajes | ~6 GB |
| `dolphin-llama3:8b` | 4.7 GB | Escritura y edición de prosa | ~7 GB |
| `qwen2.5:7b` | 4.7 GB | Estructura y análisis (no necesita uncensored) | ~6 GB |
| `llama3.2:3b` | 2.0 GB | Solo métricas (ultraligero) | ~3 GB |

### Parámetros de generación

```python
"options": {
    "num_predict": 4096,      # 8192 para escritor/editor
    "temperature": 0.75,      # Creatividad moderada-alta
    "repeat_penalty": 1.3,    # Evita loops de texto repetido
    "repeat_last_n": 256      # Ventana de penalización
}
```

---

## API Endpoints

### `GET /`
Sirve la interfaz web.

### `POST /api/agent/<agent_name>`
Genera texto con el agente especificado.

**Request:**
```json
{ "prompt": "Una mujer descubre que su espejo..." }
```

**Response:** Server-Sent Events (SSE)
```
data: {"token": "El", "done": false}
data: {"token": " espejo", "done": false}
...
data: {"token": ".", "done": true}
```

### `POST /api/save`
Guarda el progreso actual del pipeline.

**Request:**
```json
{
  "step": 3,
  "agent": "escritor",
  "premisa": "Una mujer descubre...",
  "context": {
    "ideador": "...",
    "arquitecto": "...",
    "personajes": "...",
    "escritor": "..."
  }
}
```

**Response:**
```json
{ "ok": true, "path": "03_Literatura/03_En_progreso/una_mujer_descubre_20260228_0930.md" }
```

---

## Cómo levantar

### Requisitos previos
- Python 3.x con Flask y Requests instalados
- Docker Desktop corriendo
- Contenedor `voute_ollama` con los 4 modelos descargados

### Paso a paso

```powershell
# 1. Iniciar Docker Desktop (si no está corriendo)
Start-Process "C:\Program Files\Docker\Docker\Docker Desktop.exe"

# 2. Iniciar solo Ollama (los demás servicios no son necesarios)
docker start voute_ollama

# 3. Iniciar el servidor Flask
cd C:\Users\fabara\LaVouteDAnais\web_interface
python server.py

# 4. Abrir en navegador
# http://localhost:4000
```

### Verificar que los modelos están disponibles
```powershell
docker exec voute_ollama ollama list
```
Debe mostrar: `dolphin-mistral:7b`, `dolphin-llama3:8b`, `qwen2.5:7b`, `llama3.2:3b`

---

## Cómo usar

1. Abrir `http://localhost:4000`
2. Escribir la premisa en "Tu premisa oscura"
3. Clic en **"Invocar al Ideador"**
4. Ver cómo aparece el texto token por token
5. Editar el texto si se desea
6. **"Aprobar & Continuar →"** para avanzar (o **"↻ Re-generar"**)
7. El Arquitecto y Personajes se invocan automáticamente
8. El Escritor requiere clic manual (es el más importante)
9. Crítico se auto-invoca, Editor requiere clic
10. Al final, **"💾 Guardar"** persiste todo en `03_En_progreso/`

### Tips
- Use **"■ Detener"** si el agente se repite o pierde el rumbo
- Edite libremente el texto antes de aprobar — el siguiente agente usará SU versión
- La primera generación es lenta (~2-3 min) porque Ollama carga el modelo en RAM

---

## Historial de decisiones

| Fecha | Decisión | Motivo |
|-------|----------|--------|
| 27/Feb 16:14 | Pipeline en n8n con 14 nodos | Primera implementación rápida |
| 27/Feb 17:30 | **Pivot a Web App custom** | n8n era técnico, checkpoints incómodos, sin edición directa |
| 27/Feb 17:45 | Flask en vez de Express | `npm` no disponible en Windows, Python sí |
| 27/Feb 20:24 | Agregar streaming SSE | Usuario quería ver al agente "pensar" en tiempo real |
| 27/Feb 20:24 | Rediseño CSS completo | Primer diseño "aburrido", faltaba sello La Voûte |
| 27/Feb 20:52 | `repeat_penalty: 1.3` | Arquitecto se repetía en loops |
| 27/Feb 20:54 | Botones Stop y Save | Usuario necesitaba control sobre generación y persistencia |
| 27/Feb 21:01 | Modelos Dolphin sin censura | Qwen/Llama censuran contenido erótico explícito |
| 28/Feb 09:29 | Puerto cambiado a 4000 | El 5000 conflictuaba con otro servicio |
| 28/Feb 09:44 | Look sin corsé aceptado | Decisión estilística de la Señora para looks deportivos |

---

## Pendientes

- [ ] Guardar también en formato `.html` (usar Pandoc Docker)
- [ ] Implementar "Cargar sesión guardada" (reanudar pipeline desde `.md`)
- [ ] Respetar el formato exacto de `ESTRUCTURA_MAESTRA_RELATOS.md`
- [ ] Agregar selector de "capítulo" para relatos multi-capítulo
- [ ] Crear script `.bat` para levantar todo con un clic
- [ ] Generar imágenes `side_profile` y `ditzy` pendientes cuando la API se libere
