import requests
import json
import os

# Configuración de archivos
prompts_dir = r'C:\Users\fabara\LaVouteDAnais\prompts'
literature_dir = r'C:\Users\fabara\LaVouteDAnais\03_Literatura\01_En_Progreso\smart_home_stepford'

def get_ultra_lite_context():
    with open(os.path.join(literature_dir, 'arco_argumental.md'), 'r', encoding='utf-8') as f:
        arco = f.read()
        # Tomar Acto II y reglas
        arco_lite = arco.split('### FASE 1: THE SETUP')[0] + '\n' + arco.split('#### Capítulo 4:')[1].split('#### Capítulo 5:')[0]
    
    with open(os.path.join(literature_dir, 'linea_de_tiempo.md'), 'r', encoding='utf-8') as f:
        timeline = f.read()
        # Tomar Cap 4 (Días 46-55)
        timeline_lite = timeline.split('## CAPÍTULO 4')[0].split('## CAPÍTULO 3')[0] + '\n' + timeline.split('## CAPÍTULO 4')[1].split('## CAPÍTULOS 3-7')[0]
        
    with open(os.path.join(literature_dir, 'capitulo_04_la_peluqueria.md'), 'r', encoding='utf-8') as f:
        cap4 = f.read()
        
    return arco_lite, timeline_lite, cap4

arco_lite, timeline_lite, cap4 = get_ultra_lite_context()

with open(os.path.join(prompts_dir, 'centinela.md'), 'r', encoding='utf-8') as f:
    system_prompt = f.read()

audit_request = f"""
AUDITORÍA DE CONTINUIDAD: CAPÍTULO 4 (ULTRA LITE).

### ARCO ARGUMENTAL (REFERENCIA CAP 4)
{arco_lite}

### LÍNEA DE TIEMPO (REFERENCIA CAP 4)
{timeline_lite}

### TEXTO A AUDITAR: CAPÍTULO 4
{cap4}

---

Genera el reporte oficial del Centinela. Revisa especialmente:
1. Sincronización con el Día 47.
2. Integridad del Blueprint Loyaltty (estética urbana vs sacha).
3. Coherencia del Sub Drop y el rescate de EVE.
"""

payload = {
    'model': 'qwen2.5-7b-instruct-1m',
    'messages': [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': audit_request}
    ],
    'temperature': 0.1,
    'max_tokens': 1200,
    'stream': False
}

print('Iniciando Auditoría ULTRA LITE del Centinela para el CAPÍTULO 4...')

try:
    resp = requests.post('http://127.0.0.1:1234/v1/chat/completions', json=payload, timeout=300)
    resp.raise_for_status()
    result = resp.json()
    
    answer = result['choices'][0]['message']['content']
    
    report_path = os.path.join(os.getcwd(), 'reporte_centinela_cap4_ultra_lite_real.txt')
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(answer)
    
    print(f'\n[EXITO] Reporte guardado en: {report_path}')
    print('\n--- REPORTE ---\n')
    print(answer)
    
except Exception as e:
    print('\nERROR en la auditoría:', str(e))
