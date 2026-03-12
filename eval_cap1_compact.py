import requests
import json
import os

system_prompt_path = r'C:\Users\fabara\LaVouteDAnais\prompts\critico.md'
chapter_path = r'C:\Users\fabara\LaVouteDAnais\03_Literatura\01_En_Progreso\smart_home_stepford\capitulo_01_el_diagnostico.md'
output_path = r'C:\Users\fabara\LaVouteDAnais\critica_cap1.md'

with open(system_prompt_path, 'r', encoding='utf-8') as f:
    system_prompt = f.read()

with open(chapter_path, 'r', encoding='utf-8') as f:
    chapter_content = f.read()

# Reducir drásticamente para evitar el lag de LM Studio en inferencia larga
chapter_truncated = chapter_content[:4000]

payload = {
    'model': 'qwen2.5-7b-instruct-1m',
    'messages': [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': f'Evalúa este inicio de capítulo (resumen ejecutivo de 500 palabras):\n\n{chapter_truncated}'}
    ],
    'temperature': 0.7,
    'max_tokens': 1000,
    'stream': False
}

print('Enviando request COMPACTO a LM Studio...')
try:
    resp = requests.post('http://127.0.0.1:1234/v1/chat/completions', json=payload, timeout=300)
    resp.raise_for_status()
    
    data = resp.json()
    output = data['choices'][0]['message']['content']
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output)
        
    print('[EXITO] Crítica compacta completada.')
    
except Exception as e:
    print('ERROR:', str(e))
