import requests
import json

# Configuración
ENDPOINT = 'http://127.0.0.1:1234/v1/chat/completions'
MODEL = 'qwen2.5-7b-instruct-1m'

# Rutas
PROMPT_PATH = r'C:\Users\fabara\LaVouteDAnais\prompts\critico.md'
MAESTRO_PATH = r'C:\Users\fabara\.gemini\antigravity\brain\20f2584f-93e6-4fad-a72a-7bdaa4b0c293\smart_home_stepford_v3_maestro.md'
ARCO_PATH = r'C:\Users\fabara\LaVouteDAnais\03_Literatura\01_En_Progreso\smart_home_stepford\arco_argumental.md'
BIBLIA_PATH = r'C:\Users\fabara\LaVouteDAnais\03_Literatura\01_En_Progreso\smart_home_stepford\BIBLIA_STORY.md'

def load_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

# Cargar componentes
system_prompt = load_file(PROMPT_PATH)
maestro_content = load_file(MAESTRO_PATH)
arco_content = load_file(ARCO_PATH)
biblia_content = load_file(BIBLIA_PATH)

# Extraer Capítulo 2
start_marker = "## Capítulo 2"
end_marker = "## Capítulo 3"
try:
    start_idx = maestro_content.index(start_marker)
    end_idx = maestro_content.index(end_marker)
    cap2_content = maestro_content[start_idx:end_idx].strip()
except Exception:
    cap2_content = "ERROR: No se encontró el Capítulo 2"

# User Message
user_message = f"""
AUDITORÍA DE CAPÍTULO 2 REQUERIDA.
Actúa como el Agente Crítico de La Voûte d'Anaïs.

### CONTEXTO:
**ARCO ARGUMENTAL:**
{arco_content}

**BIBLIA STORY:**
{biblia_content}

---
### TEXTO A AUDITAR (CAPÍTULO 2):
{cap2_content}
"""

payload = {
    'model': MODEL,
    'messages': [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': user_message}
    ],
    'temperature': 0.7,
    'max_tokens': 3000,
    'stream': False
}

print(f"Enviando auditoría de Cap 2 a LM Studio (Modelo: {MODEL})...")
try:
    resp = requests.post(ENDPOINT, json=payload, timeout=600)
    if resp.status_code == 200:
        critique = resp.json()['choices'][0]['message']['content']
        print("\n[RESULTADO AUDITORÍA CAP 2]:")
        print(critique)
        with open(r'C:\Users\fabara\LaVouteDAnais\99_Sistema\reportes\audit_result_cap2.md', 'w', encoding='utf-8') as f:
            f.write(critique)
    else:
        print(f"Error {resp.status_code}: {resp.text}")
except Exception as e:
    print(f"Error de conexión: {str(e)}")
