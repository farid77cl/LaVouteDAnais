import requests

models = [
    'pixtral-12b',
    'mistralai/mistral-nemo-instruct-2407',
    'qwen2.5-7b-instruct-1m',
    'meta-llama-3-8b-instruct',
    'qwen/qwen2.5-vl-7b',
    'dolphin-2.8-mistral-7b-v02',
    'dolphin-2_6-phi-2'
]

for model in models:
    print(f"Probando modelo: {model}...")
    try:
        resp = requests.post('http://127.0.0.1:1234/v1/chat/completions', 
                           json={'model': model, 'messages': [{'role': 'user', 'content': 'hi'}], 'max_tokens': 5},
                           timeout=5)
        if resp.status_code == 200:
            print(f">>> MODELO ACTIVO DETECTADO: {model}")
            break
        else:
            print(f"Error {resp.status_code}: {resp.text}")
    except Exception as e:
        print(f"Fallo de conexión para {model}: {str(e)}")
else:
    print("Ningún modelo parece estar cargado en LM Studio.")
