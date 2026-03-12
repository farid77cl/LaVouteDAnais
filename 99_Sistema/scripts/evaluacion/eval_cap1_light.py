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

# Primera parte: 4000 caracteres
chapter_slice = chapter_content[:4000]

payload = {
    'model': 'dolphin-2_6-phi-2',
    'messages': [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': f'Evalúa este inicio de capítulo (PRIMERA PARTE):\n\n{chapter_slice}'}
    ],
    'temperature': 0.7,
    'max_tokens': 1000,
    'stream': False
}

try:
    print('Enviando request a Dolphin Phi-2...')
    resp = requests.post('http://127.0.0.1:1234/v1/chat/completions', json=payload, timeout=300)
    resp.raise_for_status()
    critica = resp.json()['choices'][0]['message']['content']
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"# Crítica Parcial (Dolphin Phi-2)\n\n{critica}")
    
    print('[EXITO] Crítica con modelo ligero completada.')
except Exception as e:
    print('Error:', str(e))
