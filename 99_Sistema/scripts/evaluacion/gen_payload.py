import json
import os

# Configuración de archivos
prompts_dir = r'C:\Users\fabara\LaVouteDAnais\prompts'
literature_dir = r'C:\Users\fabara\LaVouteDAnais\03_Literatura\01_En_Progreso\smart_home_stepford'

def get_ultra_lite_context():
    with open(os.path.join(literature_dir, 'arco_argumental.md'), 'r', encoding='utf-8') as f:
        arco = f.read()
        arco_lite = arco.split('### FASE 2: THE SPARK')[0]
    
    with open(os.path.join(literature_dir, 'linea_de_tiempo.md'), 'r', encoding='utf-8') as f:
        timeline = f.read()
        timeline_lite = timeline.split('## CAPÍTULO 2')[0]
        
    with open(os.path.join(literature_dir, 'capitulo_01_el_diagnostico.md'), 'r', encoding='utf-8') as f:
        cap1 = f.read()
        
    paragraphs = cap1.split('\n\n')
    target_paragraphs = []
    for p in paragraphs:
        if '*' in p or 'Loyaltty' in p or 'EVE' in p:
            target_paragraphs.append(p)
    
    cap1_ultra_lite = '\n\n[...]\n\n'.join(target_paragraphs)
    return arco_lite, timeline_lite, cap1_ultra_lite

arco_lite, timeline_lite, cap1_ultra_lite = get_ultra_lite_context()

with open(os.path.join(prompts_dir, 'centinela.md'), 'r', encoding='utf-8') as f:
    system_prompt = f.read()

audit_request = f"""
AUDITORÍA DE CONTINUIDAD: CAPÍTULO 1 (ULTRA LITE).

### ARCO ARGUMENTAL (EXTRACTO)
{arco_lite}

### LÍNEA DE TIEMPO (EXTRACTO)
{timeline_lite}

### SEGMENTOS SELECCIONADOS DEL TEXTO (Capítulo 1)
{cap1_ultra_lite}

---

Genera el reporte oficial del Centinela. Enfócate en la coherencia de los mensajes subliminales (italizados) y líricas de Loyaltty con los Días 6-14 de la línea de tiempo.
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

with open(os.path.join(os.getcwd(), 'payload_audit.json'), 'w', encoding='utf-8') as f:
    json.dump(payload, f, ensure_ascii=False, indent=2)

print('Payload generado: payload_audit.json')
