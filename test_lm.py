import requests
import json

api_url = 'http://127.0.0.1:1234/v1/chat/completions'
payload = {
    'model': 'qwen2.5-7b-instruct-1m',
    'messages': [{'role': 'user', 'content': 'hola, responde con un test'}],
    'temperature': 0.75,
    'max_tokens': 10,
    'stream': False
}

try:
    response = requests.post(api_url, json=payload, timeout=10)
    print(response.json())
except Exception as e:
    print(e)
