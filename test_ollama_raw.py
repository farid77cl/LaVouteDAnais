import requests
import json
import time

url = "http://localhost:11434/api/generate"
# Generar un prompt gigante simulando el pipeline
massive_prompt = "Esta es una historia. " * 5000 
payload = {
    "model": "qwen2.5:7b",  # El modelo que usa personajes
    "prompt": massive_prompt + "\n\nAhora, dime una palabra corta:",
    "stream": True,
    "options": {
        "num_ctx": 16384,
        "num_predict": 100
    }
}

print("Enviando petición a Ollama en crudo (5000+ words)...")
start_time = time.time()

try:
    with requests.post(url, json=payload, stream=True, timeout=120) as r:
        r.raise_for_status()
        print(f"Server response started in {time.time() - start_time:.2f}s")
        for line in r.iter_lines():
            if line:
                data = json.loads(line.decode('utf-8'))
                print(data.get('response', ''), end='', flush=True)
                if data.get('done'):
                    print(f"\nTerminado en {time.time() - start_time:.2f}s")
                    break
except Exception as e:
    print(f"\nError: {e}")
