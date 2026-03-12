import requests
import json
import os

# Configuración
prompts_dir = r'C:\Users\fabara\LaVouteDAnais\prompts'
literature_dir = r'C:\Users\fabara\LaVouteDAnais\03_Literatura\01_En_Progreso\smart_home_stepford'

# Leer archivos sin splitting complejo
with open(os.path.join(literature_dir, 'arco_argumental.md'), 'r', encoding='utf-8') as f:
    arco = f.read()[:2000] # Primeras 2k chars para reglas generales

with open(os.path.join(literature_dir, 'linea_de_tiempo.md'), 'r', encoding='utf-8') as f:
    timeline = f.read()

with open(os.path.join(literature_dir, 'capitulo_04_la_peluqueria.md'), 'r', encoding='utf-8') as f:
    cap4 = f.read()

with open(os.path.join(prompts_dir, 'centinela.md'), 'r', encoding='utf-8') as f:
    system_prompt = f.read()

# Request enfocado
audit_request = f"""
AUDITORÍA DE CONTINUIDAD: CAPÍTULO 4.

### ARCO (REGLAS Y OBJETIVOS)
{arco}

### TEXTO A AUDITAR: CAPÍTULO 4
{cap4}

---

Genera el reporte oficial del Centinela para el Capítulo 4.
Reporta cualquier error de estética (Blueprint Loyaltty: pelo rojo XXL, vibra urbana) o del arco (Sub Drop).
"""

payload = {
    'model': 'qwen2.5-7b-instruct-1m',
    'messages': [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': audit_request}
    ],
    'temperature': 0.1,
    'max_tokens': 1000,
    'stream': False
}

print('Iniciando Auditoría NANO-LITE del Centinela (Cap 4)...')

try:
    resp = requests.post('http://127.0.0.1:1234/v1/chat/completions', json=payload, timeout=300)
    resp.raise_for_status()
    result = resp.json()
    
    answer = result['choices'][0]['message']['content']
    
    report_path = os.path.join(os.getcwd(), 'reporte_centinela_cap4_nano_lite.txt')
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(answer)
    
    print(f'\n[EXITO] Reporte guardado en: {report_path}')
    print('\n--- REPORTE ---\n')
    print(answer)
    
except Exception as e:
    print('\nERROR en la auditoría:', str(e))
