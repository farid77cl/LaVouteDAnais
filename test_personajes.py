import requests
import json
import time

url = "http://localhost:4000/api/agent/personajes"
payload = {"prompt": "Esta es una prueba de conectividad rápida. Genera solo el nombre de 1 personaje y detente. Unas 5 palabras."}

print("Enviando petición a personajes...")
start_time = time.time()

try:
    with requests.post(url, json=payload, stream=True, timeout=10) as r:
        r.raise_for_status()
        print(f"Conexión establecida en {time.time() - start_time:.2f}s")
        for line in r.iter_lines():
            if line:
                decoded_line = line.decode('utf-8')
                if decoded_line.startswith('data: '):
                    data = json.loads(decoded_line[6:])
                    token = data.get('token', '')
                    print(token, end='', flush=True)
                    if data.get('done'):
                        break
        print(f"\nTerminado en {time.time() - start_time:.2f}s")
except Exception as e:
    print(f"\nError: {e}")
