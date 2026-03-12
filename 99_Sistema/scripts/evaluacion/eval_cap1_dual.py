import requests
import json
import os

# Paths
BASE_PATH = r'C:\Users\fabara\LaVouteDAnais'
CHAPTER_PATH = os.path.join(BASE_PATH, r'03_Literatura\01_En_Progreso\smart_home_stepford\capitulo_01_el_diagnostico.md')
ARCO_PATH = os.path.join(BASE_PATH, r'03_Literatura\01_En_Progreso\smart_home_stepford\arco_argumental.md')
TIMELINE_PATH = os.path.join(BASE_PATH, r'03_Literatura\01_En_Progreso\smart_home_stepford\linea_de_tiempo.md')
OUTPUT_PATH = os.path.join(BASE_PATH, 'critica_cap1_dual.md')

def run_eval(prompt_file, custom_user_prompt):
    with open(os.path.join(BASE_PATH, 'prompts', prompt_file), 'r', encoding='utf-8') as f:
        system_prompt = f.read()
    
    payload = {
        'model': 'qwen2.5-7b-instruct-1m',
        'messages': [
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': custom_user_prompt}
        ],
        'temperature': 0.7,
        'max_tokens': 1500,
        'stream': False
    }

    try:
        print(f"Enviando request a LM Studio ({prompt_file})...")
        resp = requests.post('http://127.0.0.1:1234/v1/chat/completions', json=payload, timeout=600)
        resp.raise_for_status()
        return resp.json()['choices'][0]['message']['content']
    except Exception as e:
        return f"Error en {prompt_file}: {str(e)}"

# Read Context
with open(CHAPTER_PATH, 'r', encoding='utf-8') as f: chapter_text = f.read()[:4000] # Truncado para estabilidad
with open(ARCO_PATH, 'r', encoding='utf-8') as f: arco_text = f.read()
with open(TIMELINE_PATH, 'r', encoding='utf-8') as f: timeline_text = f.read()

# 1. Run Sentinel
sentinel_user_prompt = f"Contexto Arco Argumental:\n{arco_text}\n\nContexto Línea de Tiempo:\n{timeline_text}\n\nBorrador del Capítulo:\n{chapter_text}"
print("Iniciando fase Centinela...")
sentinel_report = run_eval('centinela.md', sentinel_user_prompt)

# 2. Run Critic
critic_user_prompt = f"Contexto Arco:\n{arco_text}\n\nBorrador del Capítulo:\n{chapter_text}"
print("Iniciando fase Crítica...")
critic_report = run_eval('critico.md', critic_user_prompt)

# Save result
with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
    f.write("# 🎭 Evaluación Dual: Centinela & Crítico\n\n")
    f.write(sentinel_report)
    f.write("\n\n---\n\n")
    f.write(critic_report)

print(f"[EXITO] Reporte dual guardada en {OUTPUT_PATH}")
