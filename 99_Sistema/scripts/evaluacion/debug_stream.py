import requests
import json
import os
import sys

system_prompt_path = r'C:\Users\fabara\LaVouteDAnais\prompts\critico.md'
chapter_path = r'C:\Users\fabara\LaVouteDAnais\03_Literatura\01_En_Progreso\el_secreto_de_la_comoda\capitulo_1_maestro_v4.2.md'

with open(system_prompt_path, 'r', encoding='utf-8') as f:
    system_prompt = f.read()

with open(chapter_path, 'r', encoding='utf-8') as f:
    chapter_content = f.read()

# MUY TRUNCADO PARA DEBUG
chapter_truncated = chapter_content[:1000]

payload = {
    'model': 'google/gemma-4-26b-a4b',
    'messages': [
        {'role': 'system', 'content': "Responde con una sola palabra: OK"},
        {'role': 'user', 'content': "hola"}
    ],
    'temperature': 0.75,
    'max_tokens': 10,
    'stream': True
}

print('DEBUG: Solicitando completación simple...')
try:
    resp = requests.post('http://127.0.0.1:1234/v1/chat/completions', json=payload, stream=True, timeout=30)
    resp.raise_for_status()
    
    print('DEBUG: Analizando líneas de respuesta...')
    for line in resp.iter_lines():
        if line:
            decoded = line.decode('utf-8')
            print(f"RAW LINE: {decoded}")
            
except Exception as e:
    print('\nERROR DEBUG:', str(e))
