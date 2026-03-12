import requests
import json

payload = {
    'model': 'qwen2.5-7b-instruct-1m',
    'messages': [
        {'role': 'system', 'content': 'Eres un crítico literario experto.'},
        {'role': 'user', 'content': 'Dime hola.'}
    ],
    'temperature': 0.7,
    'max_tokens': 100,
    'stream': False
}

try:
    print('Enviando request de prueba...')
    resp = requests.post('http://127.0.0.1:1234/v1/chat/completions', json=payload, timeout=30)
    print('Status:', resp.status_code)
    print('Response:', resp.json()['choices'][0]['message']['content'])
except Exception as e:
    print('Error:', str(e))
