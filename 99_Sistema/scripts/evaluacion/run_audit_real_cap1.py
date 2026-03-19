import requests
import json
import os

# Configuración
ENDPOINT = 'http://127.0.0.1:1234/v1/chat/completions'
MODEL = 'meta-llama-3-8b-instruct'

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

# Extraer Capítulo 1 del Maestro
# Buscamos entre "## Capítulo 1" y "## Capítulo 2"
start_marker = "## Capítulo 1"
end_marker = "## Capítulo 2"
try:
    start_idx = maestro_content.index(start_marker)
    end_idx = maestro_content.index(end_marker)
    cap1_content = maestro_content[start_idx:end_idx].strip()
except Exception:
    cap1_content = maestro_content[:1000] # Fallback

# Construir User Prompt
user_message = f"""
AUDITORÍA DE CAPÍTULO 1 REQUERIDA.

### CONTEXTO DEL PROYECTO
**Arco Argumental:**
{arco_content}

**Biblia del Relato:**
{biblia_content}

---

### TEXTO A AUDITAR (CAPÍTULO 1)
{cap1_content}
"""

payload = {
    'model': MODEL,
    'messages': [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': user_message}
    ],
    'temperature': 0.7,
    'max_tokens': 4096,
    'stream': False
}

print(f"Enviando auditoría a LM Studio (Modelo: {MODEL})...")
try:
    resp = requests.post(ENDPOINT, json=payload, timeout=600)
    resp.raise_for_status()
    critique = resp.json()['choices'][0]['message']['content']
    print("\n" + "="*50)
    print("RESUMEN DE LA AUDITORÍA")
    print("="*50)
    print(critique)
    
    # Guardar reporte
    report_path = r'C:\Users\fabara\LaVouteDAnais\99_Sistema\reportes\audit_result_real.md'
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(critique)
    print(f"\nReporte guardado en: {report_path}")

except Exception as e:
    print(f"Error durante la auditoría: {str(e)}")
