import requests
import json
import os

# Configuración de archivos
prompts_dir = r'C:\Users\fabara\LaVouteDAnais\prompts'
literature_dir = r'C:\Users\fabara\LaVouteDAnais\03_Literatura\01_En_Progreso\smart_home_stepford'

def get_lite_context():
    # Solo las partes relevantes para el Cap 1
    with open(os.path.join(literature_dir, 'arco_argumental.md'), 'r', encoding='utf-8') as f:
        arco = f.read()
        # Tomar solo Acto I / Cap 1 y reglas generales
        arco_lite = arco.split('### FASE 2: THE SPARK')[0]
    
    with open(os.path.join(literature_dir, 'linea_de_tiempo.md'), 'r', encoding='utf-8') as f:
        timeline = f.read()
        # Tomar solo Cap 1 (Días 1-15)
        timeline_lite = timeline.split('## CAPÍTULO 2')[0]
        
    with open(os.path.join(literature_dir, 'capitulo_01_el_diagnostico.md'), 'r', encoding='utf-8') as f:
        cap1 = f.read()
        
    return arco_lite, timeline_lite, cap1

arco_lite, timeline_lite, cap1 = get_lite_context()

with open(os.path.join(prompts_dir, 'centinela.md'), 'r', encoding='utf-8') as f:
    system_prompt = f.read()

audit_request = f"""
AUDITORÍA DE CONTINUIDAD: CAPÍTULO 1 (LITE).

### ARCO ARGUMENTAL (EXTRACTO CAP 1)
{arco_lite}

### LÍNEA DE TIEMPO (EXTRACTO CAP 1)
{timeline_lite}

### TEXTO A AUDITAR: CAPÍTULO 1
{cap1}

---

Genera el reporte oficial del Centinela. Asegura que los mensajes de Loyaltty y las italizaciones coincidan con los Días 6-14 de la línea de tiempo.
"""

payload = {
    'model': 'qwen2.5-7b-instruct-1m',
    'messages': [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': audit_request}
    ],
    'temperature': 0.1,
    'max_tokens': 1024, # Reducido para evitar timeouts
    'stream': False
}

print('Iniciando Auditoría LITE del Centinela para el CAPÍTULO 1...')

try:
    # Timeout largo por si el modelo está procesando mucho
    resp = requests.post('http://127.0.0.1:1234/v1/chat/completions', json=payload, timeout=300)
    resp.raise_for_status()
    result = resp.json()
    
    answer = result['choices'][0]['message']['content']
    
    report_path = os.path.join(os.getcwd(), 'reporte_centinela_cap1_lite.txt')
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(answer)
    
    print(f'\n[EXITO] Reporte guardado en: {report_path}')
    print('\n--- REPORTE ---\n')
    print(answer)
    
except Exception as e:
    print('\nERROR en la auditoría:', str(e))
