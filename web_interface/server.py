import os
import json
import logging
import requests
from flask import Flask, render_template, request, jsonify, Response, stream_with_context

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# URL compatible con LM Studio (Ollama / OpenAI Format)
LM_STUDIO_URL = "http://127.0.0.1:1234/v1/chat/completions"
LM_STUDIO_MODELS_URL = "http://127.0.0.1:1234/v1/models"

# ─── Configuración de modelos optimizada para Ryzen 7 7735HS / 32GB RAM / sin GPU dedicada ───
#
# HARDWARE: CPU-only inference (Radeon 680M iGPU no tiene soporte ROCm en LM Studio/Windows)
# RAM disponible para modelos: ~24-26 GB
#
# ESTRATEGIA: 2 modelos únicamente para minimizar tiempos de carga entre agentes (~30-90s c/u)
#
#   MODELO CREATIVO  → dolphin-2.9.4-llama3.1-8b Q4_K_M (~4.9 GB, ~5-8 tok/s)
#     Agentes: ideador, personajes, escritor, editor, mentor, contador
#     Razón: sin censura, prosa de calidad, contexto 8192, cabe cómodo en RAM
#
#   MODELO ANALÍTICO → qwen2.5-7b-instruct Q4_K_M (~4.4 GB, ~5-8 tok/s)
#     Agentes: arquitecto, critico
#     Razón: mejor razonamiento estructurado, output en markdown/tablas
#     ⚠️  Requiere context length = 8192 en LM Studio (por defecto viene en 4096)
#
# ORDEN ÓPTIMO DEL PIPELINE para minimizar swaps de modelo:
#   Ideador → Personajes (dolphin) → Arquitecto → Crítico (qwen) → Escritor → Editor → Contador (dolphin)
#   = solo 2 cambios de modelo en todo el pipeline
#
AGENT_MODEL_PREFERENCES = {
    "ideador":    "dolphin",   # Creativo — brainstorming sin censura
    "arquitecto": "qwen2.5",  # Analítico — estructura lógica en 3 actos
    "personajes": "dolphin",  # Creativo — psicología y fichas detalladas
    "escritor":   "dolphin",  # Creativo — prosa larga explícita (8192 tokens)
    "critico":    "qwen2.5",  # Analítico — evaluación con tabla de puntuación
    "editor":     "dolphin",  # Creativo — reescritura manteniendo voz
    "contador":   "dolphin",  # Creativo (tarea simple, no vale cambiar de modelo)
    "mentor":     "dolphin",  # Creativo — conversación natural con la autora
}

def get_available_models():
    """Consulta LM Studio y devuelve lista de modelos cargados."""
    try:
        resp = requests.get(LM_STUDIO_MODELS_URL, timeout=5)
        if resp.ok:
            data = resp.json()
            return [m["id"] for m in data.get("data", [])]
    except Exception as e:
        app.logger.warning(f"No se pudo consultar modelos de LM Studio: {e}")
    return []

def resolve_model(agent_name):
    """Determina qué modelo usar para un agente.
    Prioridad: 1) preferencia configurada si está cargada, 2) primer modelo disponible."""
    available = get_available_models()
    if not available:
        app.logger.error("LM Studio no tiene modelos cargados.")
        return None

    preference = AGENT_MODEL_PREFERENCES.get(agent_name)
    if preference:
        # Busca coincidencia parcial (case-insensitive)
        for m in available:
            if preference.lower() in m.lower():
                app.logger.info(f"[MODEL] {agent_name} → {m} (preferido)")
                return m
        app.logger.warning(f"[MODEL] Preferencia '{preference}' no encontrada para {agent_name}, usando fallback.")

    # Fallback: primer modelo disponible
    app.logger.info(f"[MODEL] {agent_name} → {available[0]} (disponible)")
    return available[0]

# MODELS se mantiene por compatibilidad pero ya no se usa directamente
DEFAULT_MODEL = "auto"
MODELS = {k: "auto" for k in AGENT_MODEL_PREFERENCES}

def load_prompt(agent_name):
    prompt_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'prompts', f'{agent_name}.md')
    try:
        with open(prompt_path, 'r', encoding='utf-8') as f:
            base_prompt = f.read()
    except Exception as e:
        app.logger.error(f"Error cargando prompt {agent_name}: {e}")
        base_prompt = ""

    # Append preferences to writing-related agents
    if agent_name in ['ideador', 'personajes', 'escritor', 'critico', 'editor']:
        prefs = load_preferences()
        if prefs:
            base_prompt += f"\n\n---\n\n## PREFERENCIAS DE ESCRITURA DE LA AMA (OBLIGATORIAS)\n\n{prefs}"

    return base_prompt

def load_preferences():
    """Load the user's accumulated writing preferences."""
    prefs_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '00_Helena', 'preferencias_escritura.md')
    try:
        with open(prefs_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        app.logger.warning(f"No se encontró preferencias_escritura.md: {e}")
        return ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/agent/<agent_name>', methods=['POST'])
def run_agent(agent_name):
    if agent_name not in MODELS:
        return jsonify({"error": "Agente no existe"}), 400

    data = request.json
    user_prompt = data.get('prompt', '')
    if not user_prompt:
        return jsonify({"error": "Prompt vacío"}), 400

    system_prompt = load_prompt(agent_name)
    model = resolve_model(agent_name)
    if not model:
        return jsonify({"error": "No hay modelos cargados en LM Studio. Carga un modelo y vuelve a intentar."}), 503

    # max_tokens según capacidad del modelo asignado:
    # - escritor/editor usan dolphin-llama3 con contexto amplio → 8192
    # - arquitecto/critico usan qwen2.5 con contexto limitado → 2048 para dejar margen al prompt
    # - contador usa llama3.2 liviano → 1024 (tarea simple)
    # - resto → 4096
    MAX_TOKENS_BY_AGENT = {
        "escritor":   8192,
        "editor":     8192,
        "arquitecto": 2048,
        "critico":    2048,
        "contador":   1024,
        "ideador":    4096,
        "personajes": 4096,
        "mentor":     1024,
    }
    max_tokens = MAX_TOKENS_BY_AGENT.get(agent_name, 4096)

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"El Input actual para ti es:\n\n{user_prompt}"}
        ],
        "temperature": 0.75,
        "max_tokens": max_tokens,
        "stream": True
    }

    app.logger.info(f"[STREAM] {agent_name} → {model}")

    def generate():
        try:
            with requests.post(LM_STUDIO_URL, json=payload, stream=True, timeout=600) as resp:
                resp.raise_for_status()
                for line in resp.iter_lines():
                    if line:
                        decoded_line = line.decode('utf-8')
                        if decoded_line.startswith('data: '):
                            data_str = decoded_line[6:]
                            if data_str.strip() == "[DONE]":
                                yield f"data: {json.dumps({'token': '', 'done': True})}\n\n"
                                break
                            try:
                                data = json.loads(data_str)
                                if "choices" in data and len(data["choices"]) > 0:
                                    token = data["choices"][0].get('delta', {}).get('content', '')
                                    if token:
                                        # Send back in the format expected by the frontend
                                        yield f"data: {json.dumps({'token': token, 'done': False})}\n\n"
                            except json.JSONDecodeError:
                                pass
        except Exception as e:
            yield f"data: {json.dumps({'token': f'[ERROR: {str(e)}]', 'done': True})}\n\n"

    return Response(
        stream_with_context(generate()),
        mimetype='text/event-stream',
        headers={
            'Cache-Control': 'no-cache',
            'X-Accel-Buffering': 'no'
        }
    )

@app.route('/api/save', methods=['POST'])
def save_state():
    import datetime
    data = request.json
    ctx = data.get('context', {})
    premisa = data.get('premisa', 'sin_titulo')
    step_num = data.get('step', 0)
    agent = data.get('agent', 'desconocido')

    # Build markdown content
    ts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    lines = [f"# Pipeline Literario — Guardado {ts}\n"]
    lines.append(f"**Paso actual:** {step_num + 1}/7 ({agent})\n")
    lines.append(f"**Premisa:** {premisa}\n\n---\n")

    section_names = {
        'ideador': '🧠 Ideador',
        'arquitecto': '📐 Arquitecto',
        'personajes': '🎭 Personajes',
        'escritor': '✍️ Escritor',
        'critico': '🔍 Crítico',
        'editor': '✂️ Editor',
        'contador': '📊 Contador'
    }

    for key in ['ideador', 'arquitecto', 'personajes', 'escritor', 'critico', 'editor', 'contador']:
        if key in ctx and ctx[key]:
            lines.append(f"\n## {section_names.get(key, key)}\n\n{ctx[key]}\n\n---\n")

    content = '\n'.join(lines)

    # Save to 03_Literatura/03_En_progreso/
    save_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), '03_Literatura', '03_En_progreso')
    os.makedirs(save_dir, exist_ok=True)

    # Generate filename from premisa
    slug = premisa[:40].strip().replace(' ', '_').lower()
    slug = ''.join(c for c in slug if c.isalnum() or c == '_')
    ts_file = datetime.datetime.now().strftime('%Y%m%d_%H%M')
    filename = f"{slug}_{ts_file}.md"
    filepath = os.path.join(save_dir, filename)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    app.logger.info(f"[SAVE] {filepath}")
    return jsonify({"ok": True, "path": filepath, "filename": filename})

@app.route('/api/feedback', methods=['POST'])
def add_feedback():
    """Append user feedback to preferencias_escritura.md for continuous learning."""
    import datetime
    data = request.json
    agent = data.get('agent', 'desconocido')
    feedback_type = data.get('type', 'nota')  # 'like', 'dislike', 'nota'
    comment = data.get('comment', '')
    sample = data.get('sample', '')  # Text sample that was good/bad

    if not comment:
        return jsonify({"error": "Comentario vacío"}), 400

    prefs_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '00_Helena', 'preferencias_escritura.md')
    ts = datetime.datetime.now().strftime('%Y-%m-%d')

    icons = {'like': '✅', 'dislike': '❌', 'nota': '📝'}
    icon = icons.get(feedback_type, '📝')

    entry = f"\n| {ts} | {agent} | {icon} {comment} |"
    if sample:
        entry += f"\n\n> **Ejemplo ({feedback_type}):**\n> {sample[:200]}\n"

    try:
        with open(prefs_path, 'a', encoding='utf-8') as f:
            f.write(entry + "\n")
        app.logger.info(f"[LEARN] {feedback_type}: {comment[:50]}...")
        return jsonify({"ok": True, "learned": comment})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/sessions', methods=['GET'])
def list_sessions():
    """List all saved pipeline sessions."""
    import re
    save_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), '03_Literatura', '03_En_progreso')
    if not os.path.exists(save_dir):
        return jsonify({"sessions": []})

    sessions = []
    for f in sorted(os.listdir(save_dir), reverse=True):
        if f.endswith('.md'):
            filepath = os.path.join(save_dir, f)
            try:
                with open(filepath, 'r', encoding='utf-8') as fh:
                    first_lines = fh.read(500)
                # Extract metadata
                step_match = re.search(r'\*\*Paso actual:\*\* (\d+/7 \([^)]+\))', first_lines)
                premisa_match = re.search(r'\*\*Premisa:\*\* (.+)', first_lines)
                date_match = re.search(r'Guardado (\d{4}-\d{2}-\d{2} \d{2}:\d{2})', first_lines)
                sessions.append({
                    "filename": f,
                    "name": premisa_match.group(1)[:60] if premisa_match else f,
                    "step": step_match.group(1) if step_match else "?",
                    "date": date_match.group(1) if date_match else "?"
                })
            except: pass
    return jsonify({"sessions": sessions})

@app.route('/api/sessions/<filename>', methods=['GET'])
def load_session(filename):
    """Load a saved session and return its context."""
    import re
    save_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), '03_Literatura', '03_En_progreso')
    filepath = os.path.join(save_dir, filename)
    if not os.path.exists(filepath):
        return jsonify({"error": "Archivo no encontrado"}), 404

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse context from sections
    context = {}
    section_map = {
        '🧠 Ideador': 'ideador', '📐 Arquitecto': 'arquitecto',
        '🎭 Personajes': 'personajes', '✍️ Escritor': 'escritor',
        '🔍 Crítico': 'critico', '✂️ Editor': 'editor', '📊 Contador': 'contador'
    }

    for label, key in section_map.items():
        pattern = rf'## {re.escape(label)}\n\n(.*?)(?=\n---|\Z)'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            context[key] = match.group(1).strip()

    # Parse step
    step_match = re.search(r'\*\*Paso actual:\*\* (\d+)', content)
    step_num = int(step_match.group(1)) - 1 if step_match else 0

    # Parse premisa
    premisa_match = re.search(r'\*\*Premisa:\*\* (.+)', content)
    premisa = premisa_match.group(1).strip() if premisa_match else ""
    context['premisa'] = premisa

    app.logger.info(f"[LOAD] {filename} → step {step_num}")
    return jsonify({"step": step_num, "context": context, "premisa": premisa})

@app.route('/api/chat', methods=['POST'])
def chat_mentor():
    """Multi-turn streaming conversation with El Confesor mentor agent."""
    data = request.json
    message = data.get('message', '')
    history = data.get('history', [])
    agent_context = data.get('agent_context', '')
    sample = data.get('sample', '')

    if not message:
        return jsonify({"error": "Mensaje vacío"}), 400

    system_prompt = load_prompt('mentor')

    messages = [{"role": "system", "content": system_prompt}]
    
    if sample:
        messages.append({"role": "user", "content": f"[Texto del agente '{agent_context}' que estamos discutiendo]:\n{sample}"})
    
    for msg in history[:-1]:
        messages.append({"role": msg['role'], "content": msg['content']})
        
    messages.append({"role": "user", "content": message})

    payload = {
        "model": resolve_model("mentor") or resolve_model("ideador"), # Fallback standard model
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 512,
        "stream": True
    }

    def generate():
        try:
            with requests.post(LM_STUDIO_URL, json=payload, stream=True, timeout=120) as resp:
                resp.raise_for_status()
                for line in resp.iter_lines():
                    if line:
                        decoded_line = line.decode('utf-8')
                        if decoded_line.startswith('data: '):
                            data_str = decoded_line[6:]
                            if data_str.strip() == "[DONE]":
                                yield f"data: {json.dumps({'token': '', 'done': True})}\n\n"
                                break
                            try:
                                data = json.loads(data_str)
                                if "choices" in data and len(data["choices"]) > 0:
                                    token = data["choices"][0].get('delta', {}).get('content', '')
                                    if token:
                                        yield f"data: {json.dumps({'token': token, 'done': False})}\n\n"
                            except json.JSONDecodeError:
                                pass
        except Exception as e:
            yield f"data: {json.dumps({'token': f'[Error: {str(e)}]', 'done': True})}\n\n"

    return Response(
        stream_with_context(generate()),
        mimetype='text/event-stream',
        headers={'Cache-Control': 'no-cache', 'X-Accel-Buffering': 'no'}
    )

@app.route('/api/export', methods=['POST'])
def export_html():
    """Export a saved session or current pipeline as styled HTML."""
    import subprocess, tempfile
    data = request.json
    content = data.get('content', '')
    title = data.get('title', 'La Voûte d\'Anaïs')

    if not content:
        return jsonify({"error": "Contenido vacío"}), 400

    # Add title header
    md_content = f"# {title}\n\n{content}"

    # Try Pandoc Docker first
    try:
        result = subprocess.run(
            ['docker', 'start', 'voute_pandoc'],
            capture_output=True, timeout=10
        )
    except: pass

    export_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), '03_Literatura', '04_Exportados')
    os.makedirs(export_dir, exist_ok=True)

    import datetime
    slug = title[:30].strip().replace(' ', '_').lower()
    slug = ''.join(c for c in slug if c.isalnum() or c == '_')
    ts = datetime.datetime.now().strftime('%Y%m%d_%H%M')
    filename = f"{slug}_{ts}.html"
    filepath = os.path.join(export_dir, filename)

    # Write temp md file
    md_path = os.path.join(export_dir, f"_temp_{ts}.md")
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)

    # Try Pandoc Docker
    try:
        result = subprocess.run(
            ['docker', 'exec', 'voute_pandoc', 'pandoc',
             '-f', 'markdown', '-t', 'html5', '--standalone',
             '--metadata', f'title={title}',
             '-c', 'https://cdn.jsdelivr.net/npm/water.css@2/out/dark.min.css'],
            input=md_content.encode('utf-8'),
            capture_output=True, timeout=30
        )
        if result.returncode == 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(result.stdout.decode('utf-8'))
            os.remove(md_path)
            app.logger.info(f"[EXPORT] Pandoc → {filepath}")
            return jsonify({"ok": True, "path": filepath, "filename": filename, "method": "pandoc"})
    except: pass

    # Fallback: simple HTML wrap
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} — La Voûte d'Anaïs</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/water.css@2/out/dark.min.css">
    <style>body {{ max-width: 800px; font-size: 1.1rem; line-height: 1.8; }}</style>
</head>
<body>
<article>
{md_content.replace(chr(10), '<br>')}
</article>
</body>
</html>"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    
    try: os.remove(md_path)
    except: pass

    app.logger.info(f"[EXPORT] Fallback HTML → {filepath}")
    return jsonify({"ok": True, "path": filepath, "filename": filename, "method": "fallback"})

@app.route('/api/status', methods=['GET'])
def system_status():
    """Return system health: Ollama, models, sessions."""
    import glob
    status = {"ollama": False, "models": [], "sessions_count": 0, "port": 4000}
    try:
        resp = requests.get("http://localhost:11434/api/tags", timeout=5)
        if resp.ok:
            status["ollama"] = True
            status["models"] = [m["name"] for m in resp.json().get("models", [])]
    except: pass

    save_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), '03_Literatura', '03_En_progreso')
    if os.path.exists(save_dir):
        status["sessions_count"] = len(glob.glob(os.path.join(save_dir, '*.md')))

    return jsonify(status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8666, debug=True)
