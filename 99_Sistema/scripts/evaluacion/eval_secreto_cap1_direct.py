import requests
import json
import os

system_prompt_path = r'C:\Users\fabara\LaVouteDAnais\prompts\critico.md'
chapter_path = r'C:\Users\fabara\LaVouteDAnais\03_Literatura\01_En_Progreso\el_secreto_de_la_comoda\capitulo_1_maestro_v4.2.md'
output_path = r'C:\Users\fabara\LaVouteDAnais\03_Literatura\01_En_Progreso\el_secreto_de_la_comoda\critica_cap1_ULTRA.md'

with open(system_prompt_path, 'r', encoding='utf-8') as f:
    system_prompt = f.read()

with open(chapter_path, 'r', encoding='utf-8') as f:
    chapter_content = f.read()

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
        {'role': 'user', 'content': f'Evalúa este borrador del capítulo:\n\n{chapter_content}'}
    ],
    'temperature': 0.7,
    'max_tokens': 3000,
    'stream': False
}

print('Iniciando petición DIRECTA (No-Stream)... esto puede tardar minutos...')
try:
    resp = requests.post('http://127.0.0.1:1234/v1/chat/completions', json=payload, timeout=900)
    resp.raise_for_status()
    
    data = resp.json()
    if 'choices' in data and len(data['choices']) > 0:
        content = data['choices'][0].get('message', {}).get('content', '')
        if content:
            with open(output_path, 'w', encoding='utf-8') as out_file:
                out_file.write(content)
            print('\n[EXITO] Crítica guardada exitosamente.')
        else:
            print('\nERROR: Respuesta vacía del modelo.')
    else:
        print('\nERROR: Formato de respuesta inesperado.')
    
except Exception as e:
    print('\nERROR:', str(e))
