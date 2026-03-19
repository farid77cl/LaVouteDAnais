import requests
import json

# Configuración
ENDPOINT = 'http://127.0.0.1:1234/v1/chat/completions'
MODEL = 'dolphin-2.8-mistral-7b-v02' # Usando Dolphin por su agilidad

# Rutas
PROMPT_PATH = r'C:\Users\fabara\LaVouteDAnais\prompts\critico.md'
MAESTRO_PATH = r'C:\Users\fabara\.gemini\antigravity\brain\20f2584f-93e6-4fad-a72a-7bdaa4b0c293\smart_home_stepford_v3_maestro.md'

def load_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

# Cargar componentes
system_prompt = load_file(PROMPT_PATH)
maestro_content = load_file(MAESTRO_PATH)

# Extraer Capítulo 1
start_marker = "## Capítulo 1"
end_marker = "## Capítulo 2"
try:
    start_idx = maestro_content.index(start_marker)
    end_idx = maestro_content.index(end_marker)
    cap1_content = maestro_content[start_idx:end_idx].strip()
except Exception:
    cap1_content = maestro_content[:1000]

# User Prompt
user_message = f"""
AUDITORÍA DE CAPÍTULO 1 REQUERIDA.
Agente Crítico: Evalúa el Capítulo 1 de 'Smart Home Stepford' v3.0.

TEXTO A AUDITAR:
{cap1_content}
"""

payload = {
    'model': MODEL,
    'messages': [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': user_message}
    ],
    'temperature': 0.7,
    'max_tokens': 2048,
    'stream': False
}

print(f"Enviando auditoría a LM Studio (Modelo: {MODEL})...")
try:
    resp = requests.post(ENDPOINT, json=payload, timeout=120)
    print(f"Status: {resp.status_code}")
    if resp.status_code != 200:
        print(f"Error: {resp.text}")
    else:
        critique = resp.json()['choices'][0]['message']['content']
        print("\n[RESULTADO DE LA AUDITORÍA]:")
        print(critique)
        
        # Guardar reporte
        report_path = r'C:\Users\fabara\LaVouteDAnais\99_Sistema\reportes\audit_result_real_dolphin.md'
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(critique)
        print(f"\nReporte guardado en: {report_path}")

except Exception as e:
    print(f"Error de conexión: {str(e)}")
