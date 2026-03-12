import requests
import json
import os

# Configuración
prompts_dir = r'C:\Users\fabara\LaVouteDAnais\prompts'
literature_dir = r'C:\Users\fabara\LaVouteDAnais\03_Literatura\01_En_Progreso\smart_home_stepford'

with open(os.path.join(literature_dir, 'arco_argumental.md'), 'r', encoding='utf-8') as f:
    arco = f.read()

with open(os.path.join(literature_dir, 'capitulo_04_la_peluqueria.md'), 'r', encoding='utf-8') as f:
    cap4 = f.read()

with open(os.path.join(prompts_dir, 'critico.md'), 'r', encoding='utf-8') as f:
    system_prompt = f.read()

audit_request = f"""
AUDITORÍA CRÍTICA LITERARIA: CAPÍTULO 4.

### ARCO ARGUMENTAL (REFERENCIA)
{arco}

### TEXTO A AUDITAR: CAPÍTULO 4
{cap4}

---

Genera el reporte oficial del Agente Crítico para el Capítulo 4. 
Enfócate en la sensorialidad del salón de belleza, el peso de las extensiones, el colapso emocional (Sub Drop) y la voz "Loyaltty" de Clara.
"""

payload = {
    'model': 'qwen2.5-7b-instruct-1m',
    'messages': [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': audit_request}
    ],
    'temperature': 0.7,
    'max_tokens': 1500,
    'stream': False
}

print('Iniciando Auditoría del Agente CRÍTICO (Cap 4)...')

try:
    resp = requests.post('http://127.0.0.1:1234/v1/chat/completions', json=payload, timeout=600)
    resp.raise_for_status()
    result = resp.json()
    
    answer = result['choices'][0]['message']['content']
    
    report_path = os.path.join(os.getcwd(), 'reporte_critico_cap4_final.md')
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(answer)
    
    print(f'\n[EXITO] Reporte guardado en: {report_path}')
    print('\n--- REPORTE ---\n')
    print(answer)
    
except Exception as e:
    print('\nERROR en la auditoría del crítico:', str(e))
