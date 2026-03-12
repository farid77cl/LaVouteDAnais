import requests
import json
import os

# Configuración de archivos
prompts_dir = r'C:\Users\fabara\LaVouteDAnais\prompts'
literature_dir = r'C:\Users\fabara\LaVouteDAnais\03_Literatura\01_En_Progreso\smart_home_stepford'

files_to_load = {
    'centinela': os.path.join(prompts_dir, 'centinela.md'),
    'arco': os.path.join(literature_dir, 'arco_argumental.md'),
    'timeline': os.path.join(literature_dir, 'linea_de_tiempo.md'),
    'cap1': os.path.join(literature_dir, 'capitulo_01_el_diagnostico.md'),
    'cap2': os.path.join(literature_dir, 'capitulo_02_la_frecuencia.md'),
    'cap3': os.path.join(literature_dir, 'capitulo_03_las_unas.md')
}

contents = {}
for key, path in files_to_load.items():
    with open(path, 'r', encoding='utf-8') as f:
        contents[key] = f.read()

# Construcción del Payload
# Nota: Enviamos los 3 capítulos juntos para que el Centinela detecte contradicciones entre ellos.
system_prompt = contents['centinela']
audit_request = f"""
AUDITORÍA DE CONTINUIDAD: CAPÍTULOS 1, 2 Y 3.

### ARCO ARGUMENTAL DE REFERENCIA
{contents['arco']}

### LÍNEA DE TIEMPO MAESTRA
{contents['timeline']}

### TEXTOS A AUDITAR
---
CAPÍTULO 1:
{contents['cap1']}

---
CAPÍTULO 2:
{contents['cap2']}

---
CAPÍTULO 3:
{contents['cap3']}

---

Genera el reporte oficial del Centinela indicando cualquier error temporal o del arco.
"""

payload = {
    'model': 'qwen2.5-7b-instruct-1m',
    'messages': [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': audit_request}
    ],
    'temperature': 0.1, # Temperatura baja para mayor rigor lógico
    'max_tokens': 2048,
    'stream': False
}

print('Iniciando Auditoría del Centinela (Caps 1-3)...')
print('(Esto puede tardar un momento debido al volumen de texto...)')

try:
    resp = requests.post('http://127.0.0.1:1234/v1/chat/completions', json=payload, timeout=600)
    resp.raise_for_status()
    result = resp.json()
    
    answer = result['choices'][0]['message']['content']
    
    # Escribir a un archivo para evitar truncamiento por terminal
    report_path = os.path.join(os.getcwd(), 'audit_report_stepford.txt')
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write('='*40 + '\n')
        f.write(answer + '\n')
        f.write('='*40 + '\n')
    
    print(f'\n[EXITO] Auditoría completada. Reporte guardado en: {report_path}')
    print('\n' + '='*40)
    print(answer[:500] + '... [Ver archivo para reporte completo]')
    print('='*40)
    
except Exception as e:
    print('\nERROR en la auditoría:', str(e))
