import requests
try:
    resp = requests.get('http://127.0.0.1:1234/v1/models', timeout=5)
    if resp.status_code == 200:
        models = resp.json()
        print("Modelos disponibles:")
        for model in models['data']:
            print(f"- {model['id']}")
    else:
        print(f"Error {resp.status_code}: {resp.text}")
except Exception as e:
    print(f"Error de conexión: {str(e)}")
