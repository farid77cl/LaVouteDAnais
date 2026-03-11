import sys
import json
import requests
import io

# Forzar salida en UTF-8 para evitar errores en Windows con emojis
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Configuración
api_url = 'http://127.0.0.1:1234/v1/chat/completions'
prompt_path = r'C:\Users\fabara\LaVouteDAnais\prompts\critico.md'
chapter_path = r'C:\Users\fabara\LaVouteDAnais\03_Literatura\01_En_Progreso\smart_home_stepford\capitulo_03_las_unas.md'
output_path = r'C:\Users\fabara\LaVouteDAnais\critica_cap3.md'

# Leer prompt del sistema
with open(prompt_path, 'r', encoding='utf-8') as f:
    system_prompt = f.read()

# Leer capítulo
with open(chapter_path, 'r', encoding='utf-8') as f:
    chapter_content = f.read()

payload = {
    'model': 'qwen2.5-7b-instruct-1m',
    'messages': [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': f'Evalúa este borrador del capítulo 3:\n\n{chapter_content}'}
    ],
    'temperature': 0.75,
    'max_tokens': 2048,
    'stream': True
}

print("Iniciando stream desde LM Studio...", flush=True)

try:
    response = requests.post(api_url, json=payload, stream=True)
    response.raise_for_status()
    
    with open(output_path, 'w', encoding='utf-8') as outfile:
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode('utf-8')
                if decoded_line.startswith('data: '):
                    data_str = decoded_line[6:]
                    if data_str == '[DONE]':
                        break
                    
                    try:
                        data_json = json.loads(data_str)
                        if 'choices' in data_json and len(data_json['choices']) > 0:
                            delta = data_json['choices'][0].get('delta', {})
                            content = delta.get('content', '')
                            if content:
                                sys.stdout.write(content)
                                sys.stdout.flush()
                                outfile.write(content)
                                outfile.flush()
                    except json.JSONDecodeError:
                        pass
    print(f"\n\n[EXITO] Crítica completada y guardada en {output_path}")

except requests.exceptions.RequestException as e:
    print(f"\n[ERROR] Comunicación con LM Studio falló: {e}")
    sys.exit(1)
