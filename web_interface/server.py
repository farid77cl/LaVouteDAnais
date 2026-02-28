import os
import json
import logging
import requests
from flask import Flask, render_template, request, jsonify, Response, stream_with_context

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELS = {
    "ideador": "dolphin-mistral:7b",       # SIN CENSURA — brainstorming erótico
    "arquitecto": "qwen2.5:7b",            # Solo estructura, no necesita uncensored
    "personajes": "dolphin-mistral:7b",     # SIN CENSURA — fichas con fetiches
    "escritor": "dolphin-llama3:8b",        # SIN CENSURA — prosa erótica explícita
    "critico": "qwen2.5:7b",               # Solo análisis
    "editor": "dolphin-llama3:8b",          # SIN CENSURA — reescritura explícita
    "contador": "llama3.2:3b"               # Solo métricas
}

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
    model = MODELS[agent_name]
    max_tokens = 8192 if agent_name in ['escritor', 'editor'] else 4096

    payload = {
        "model": model,
        "system": system_prompt,
        "prompt": user_prompt,
        "stream": True,
        "options": {
            "num_predict": max_tokens,
            "temperature": 0.75,
            "repeat_penalty": 1.3,
            "repeat_last_n": 256
        }
    }

    app.logger.info(f"[STREAM] {agent_name} → {model}")

    def generate():
        try:
            with requests.post(OLLAMA_URL, json=payload, stream=True, timeout=600) as resp:
                resp.raise_for_status()
                for line in resp.iter_lines():
                    if line:
                        chunk = json.loads(line)
                        token = chunk.get('response', '')
                        done = chunk.get('done', False)
                        yield f"data: {json.dumps({'token': token, 'done': done})}\n\n"
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
