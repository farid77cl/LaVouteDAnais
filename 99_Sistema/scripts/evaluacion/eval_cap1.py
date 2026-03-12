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

# Truncar el capítulo para asegurar que no exceda el límite de n_ctx=4096 de LM Studio.
# 10000 caracteres son ~2500 tokens, más ~600 del system prompt, deja ~1000 para la respuesta.
chapter_truncated = chapter_content[:10000]

payload = {
    'model': 'qwen2.5-7b-instruct-1m',
    'messages': [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': f'Evalúa este borrador del capítulo (truncado por límites de contexto):\n\n{chapter_truncated}'}
    ],
    'temperature': 0.75,
    'max_tokens': 1000,
    'stream': False
}

print('Enviando request a LM Studio. Caracteres del capítulo enviados:', len(chapter_truncated))
try:
    resp = requests.post('http://127.0.0.1:1234/v1/chat/completions', json=payload, timeout=600)
    resp.raise_for_status()
    
    data = resp.json()
    output = data['choices'][0]['message']['content']
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output)
        
    print('[EXITO] Crítica completada y guardada en', output_path)
    
except Exception as e:
    print('ERROR:', str(e))
    if hasattr(e, 'response') and e.response:
        print('RESPONSE:', e.response.text)
