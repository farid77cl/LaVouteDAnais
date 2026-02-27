import os
import json
import logging
import requests
from flask import Flask, render_template, request, jsonify, Response, stream_with_context

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELS = {
    "ideador": "qwen2.5:7b",
    "arquitecto": "qwen2.5:7b",
    "personajes": "qwen2.5:7b",
    "escritor": "qwen2.5:14b",
    "critico": "qwen2.5:7b",
    "editor": "qwen2.5:14b",
    "contador": "llama3.2:3b"
}

def load_prompt(agent_name):
    prompt_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'prompts', f'{agent_name}.md')
    try:
        with open(prompt_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        app.logger.error(f"Error cargando prompt {agent_name}: {e}")
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
