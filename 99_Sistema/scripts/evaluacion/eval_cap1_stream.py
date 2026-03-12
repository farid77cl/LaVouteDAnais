import requests
import json
import os
import sys

system_prompt_path = r'C:\Users\fabara\LaVouteDAnais\prompts\critico.md'
chapter_path = r'C:\Users\fabara\LaVouteDAnais\03_Literatura\01_En_Progreso\smart_home_stepford\capitulo_01_el_diagnostico.md'
output_path = r'C:\Users\fabara\LaVouteDAnais\critica_cap1.md'

with open(system_prompt_path, 'r', encoding='utf-8') as f:
    system_prompt = f.read()

with open(chapter_path, 'r', encoding='utf-8') as f:
    chapter_content = f.read()

# Enviar el capítulo completo porque la Ama ya subió el límite en LM Studio.
chapter_truncated = chapter_content

payload = {
    'model': 'qwen2.5-7b-instruct-1m',
    'messages': [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': f'Evalúa este borrador del capítulo:\n\n{chapter_truncated}'}
    ],
    'temperature': 0.75,
    'max_tokens': 2048,
    'stream': True
}

print('Iniciando stream desde LM Studio...')
try:
    resp = requests.post('http://127.0.0.1:1234/v1/chat/completions', json=payload, stream=True, timeout=600)
    resp.raise_for_status()
    
    with open(output_path, 'w', encoding='utf-8') as out_file:
        for line in resp.iter_lines():
            if line:
                decoded = line.decode('utf-8')
                if decoded.startswith('data: '):
                    data_str = decoded[6:]
                    if data_str.strip() == '[DONE]':
                        break
                    try:
                        data = json.loads(data_str)
                        if 'choices' in data and len(data['choices']) > 0:
                            token = data['choices'][0].get('delta', {}).get('content', '')
                            if token:
                                sys.stdout.write(token)
                                sys.stdout.flush()
                                out_file.write(token)
                    except json.JSONDecodeError:
                        pass
                        
    print('\n\n[EXITO] Crítica completada y guardada en', output_path)
    
except Exception as e:
    print('\nERROR:', str(e))
