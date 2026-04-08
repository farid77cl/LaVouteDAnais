import requests
import json
import os
import sys

system_prompt_path = r'C:\Users\fabara\LaVouteDAnais\prompts\critico.md'
chapter_path = r'C:\Users\fabara\LaVouteDAnais\03_Literatura\01_En_Progreso\el_secreto_de_la_comoda\capitulo_1_maestro_v4.2.md'
output_path = r'C:\Users\fabara\LaVouteDAnais\03_Literatura\01_En_Progreso\el_secreto_de_la_comoda\critica_cap1_ULTRA.md'

with open(system_prompt_path, 'r', encoding='utf-8') as f:
    system_prompt = f.read()

with open(chapter_path, 'r', encoding='utf-8') as f:
    chapter_content = f.read()

# TRUNCADO DIAGNÓSTICO (Primeros 1500 palabras aprox)
chapter_truncated = chapter_content[:8000] 

project_context = """
NOTA PARA EL CRÍTICO: Este relato pertenece al proyecto 'El Secreto de la Cómoda'. 
IGNORA las instrucciones sobre 'Nacho' y 'Titi'. En su lugar, vigila:
1. El Contraste: Ricardo debe ser arrogantemente patético. Su omnipotencia ejecutiva DEBE ser el combustible para su rendición masiva.
2. La Muerte del Arquitecto: La transición de hombre de negocios a 'Rocío' (el objeto) debe sentirse como un alivio traumático.
3. El Sabor de Zapallar: Exige Old Money Chileno, olor a talco rancio, látex 60s y el peso de las fajas Rago.
"""

payload = {
    'model': 'google/gemma-4-26b-a4b',
    'messages': [
        {'role': 'system', 'content': system_prompt + "\n" + project_context},
        {'role': 'user', 'content': f'Evalúa este borrador del capítulo (TRUNCADO PARA DIAGNÓSTICO):\n\n{chapter_truncated}'}
    ],
    'temperature': 0.75,
    'max_tokens': 2000,
    'stream': True
}

print('Iniciando stream (Truncated Diagnostic Mode)...')
try:
    resp = requests.post('http://127.0.0.1:1234/v1/chat/completions', json=payload, stream=True, timeout=300)
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
                                out_file.write(token)
                                out_file.flush()
                                sys.stdout.write(token)
                                sys.stdout.flush()
                    except json.JSONDecodeError:
                        pass
                        
    print('\n\n[EXITO] Crítica (Truncada) completada.')
    
except Exception as e:
    print('\nERROR FATAL:', str(e))
