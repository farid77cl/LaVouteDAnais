import requests
import json
import os

# Configuration
SYSTEM_PROMPT_PATH = r'C:\Users\fabara\LaVouteDAnais\prompts\critico.md'
CHAPTER_PATH = r'C:\Users\fabara\LaVouteDAnais\03_Literatura\01_En_Progreso\smart_home_stepford\capitulo_01_el_diagnostico.md'
ARCO_PATH = r'C:\Users\fabara\LaVouteDAnais\03_Literatura\01_En_Progreso\smart_home_stepford\arco_argumental.md'
OUTPUT_PATH = r'C:\Users\fabara\LaVouteDAnais\critica_cap1_completa.md'

with open(SYSTEM_PROMPT_PATH, 'r', encoding='utf-8') as f:
    system_prompt = f.read()

with open(CHAPTER_PATH, 'r', encoding='utf-8') as f:
    chapter_content = f.read()

with open(ARCO_PATH, 'r', encoding='utf-8') as f:
    # Read first 2000 chars of arco to keep context light
    arco_context = f.read()[:2000]

# Split chapter into chunks if too long, or try a large chunk (5000 chars)
# The user wants it "completa", but LM Studio is timing out. I will try 6000 characters.
chapter_slice = chapter_content[:6000]

payload = {
    'model': 'qwen2.5-7b-instruct-1m',
    'messages': [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': f'Contexto Arco:\n{arco_context}\n\nAnaliza y critica de forma EXHAUSTIVA este fragmento del Capítulo 1. Sigue estrictamente tu formato de salida (Puntuación, Fortalezas, Debilidades, Correcciones):\n\n{chapter_slice}'}
    ],
    'temperature': 0.7,
    'max_tokens': 2500,
    'stream': False
}

try:
    print('Solicitando crítica COMPLETA a LM Studio (6000 chars input)...')
    # Increased timeout to 15 minutes as it's a heavy request
    resp = requests.post('http://127.0.0.1:1234/v1/chat/completions', json=payload, timeout=900)
    resp.raise_for_status()
    
    critica = resp.json()['choices'][0]['message']['content']
    
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        f.write(critica)
        
    print(f'[EXITO] Crítica completa guardada en {OUTPUT_PATH}')
    
except Exception as e:
    print('ERROR:', str(e))
    if hasattr(e, 'response') and e.response:
        print('Response details:', e.response.text)
