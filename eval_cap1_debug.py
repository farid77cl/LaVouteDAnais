import requests
import json
import sys
import os

system_prompt_path = r'C:\Users\fabara\LaVouteDAnais\prompts\critico.md'
chapter_path = r'C:\Users\fabara\LaVouteDAnais\03_Literatura\01_En_Progreso\smart_home_stepford\capitulo_01_el_diagnostico.md'
output_path = r'C:\Users\fabara\LaVouteDAnais\critica_cap1_debug.md'
log_path = r'C:\Users\fabara\LaVouteDAnais\eval_debug_log.txt'

def log(msg):
    with open(log_path, 'a', encoding='utf-8') as f:
        f.write(msg + '\n')
    print(msg)

if os.path.exists(log_path):
    os.remove(log_path)

log("Iniciando evaluación robusta...")

try:
    with open(system_prompt_path, 'r', encoding='utf-8') as f:
        system_prompt = f.read()
    with open(chapter_path, 'r', encoding='utf-8') as f:
        chapter_content = f.read()

    log(f"Prompt leído ({len(system_prompt)} chars). Capítulo leído ({len(chapter_content)} chars).")

    payload = {
        'model': 'qwen2.5-7b-instruct-1m',
        'messages': [
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': f'Evalúa este borrador del capítulo:\n\n{chapter_content}'}
        ],
        'temperature': 0.75,
        'max_tokens': 2048,
        'stream': True
    }

    log("Enviando request a LM Studio (stream=True)...")
    resp = requests.post('http://127.0.0.1:1234/v1/chat/completions', json=payload, stream=True, timeout=900)
    resp.raise_for_status()
    log(f"Status recibido: {resp.status_code}. Empezando a leer stream...")

    full_response = ""
    with open(output_path, 'w', encoding='utf-8') as out_file:
        for line in resp.iter_lines():
            if line:
                decoded = line.decode('utf-8')
                if decoded.startswith('data: '):
                    data_str = decoded[6:]
                    if data_str.strip() == '[DONE]':
                        log("Stream finalizado vía [DONE]")
                        break
                    try:
                        data = json.loads(data_str)
                        if 'choices' in data and len(data['choices']) > 0:
                            token = data['choices'][0].get('delta', {}).get('content', '')
                            if token:
                                out_file.write(token)
                                full_response += token
                                sys.stdout.write(token)
                                sys.stdout.flush()
                    except json.JSONDecodeError as e:
                        log(f"Error decodificando JSON: {e} en línea: {decoded}")
                else:
                    log(f"Línea no esperada: {decoded}")

    if full_response:
        log(f"Éxito. Respuesta total: {len(full_response)} caracteres.")
    else:
        log("Fracaso: Respuesta vacía.")

except Exception as e:
    log(f"ERROR CRÍTICO: {str(e)}")
    if hasattr(e, 'response') and e.response:
        log(f"Response text: {e.response.text}")
