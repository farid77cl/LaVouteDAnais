import os
import json
import logging
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

OLLAMA_URL = "http://localhost:11434/api/generate"
# Nombres de los modelos basados en la infreaestructura dictada por el usuario
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
    """Carga el system prompt desde el directorio ../prompts/"""
    prompt_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'prompts', f'{agent_name}.md')
    try:
        with open(prompt_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        app.logger.error(f"Error cargando prompt {agent_name}: {e}")
        return ""

def call_ollama(model, system_prompt, user_prompt, override_max_tokens=None):
    """Realiza la llamada a Ollama"""
    payload = {
        "model": model,
        "system": system_prompt,
        "prompt": user_prompt,
        "stream": False,
        "options": {
            "num_predict": override_max_tokens if override_max_tokens else 4096,
            "temperature": 0.75
        }
    }
    
    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=600)  # 10 min timeout
        response.raise_for_status()
        return response.json().get('response', '')
    except Exception as e:
        app.logger.error(f"Ollama API Error: {e}")
        return f"Error: No se pudo contactar al agente. Detalles: {str(e)}"

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
    
    # Escritor y Editor necesitan más tokens para un capítulo de 3000 palabras
    max_tokens = 8192 if agent_name in ['escritor', 'editor'] else 4096

    app.logger.info(f"Llamando a {agent_name} usando modelo {model}...")
    result = call_ollama(model, system_prompt, user_prompt, override_max_tokens=max_tokens)
    
    return jsonify({"output": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
