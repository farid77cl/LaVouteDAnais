import requests
import json

# Rutas de los componentes del motor (Ahora usando CRITICO como prompt base)
system_prompt_path = r'C:\Users\fabara\LaVouteDAnais\prompts\critico.md'
arco_path = r'C:\Users\fabara\LaVouteDAnais\03_Literatura\01_En_Progreso\smart_home_stepford\arco_argumental.md'
biblia_path = r'C:\Users\fabara\LaVouteDAnais\03_Literatura\01_En_Progreso\smart_home_stepford\BIBLIA_STORY.md'

# Cargar contenidos
with open(system_prompt_path, 'r', encoding='utf-8') as f:
    system_prompt = f.read()

with open(arco_path, 'r', encoding='utf-8') as f:
    arco_content = f.read()

with open(biblia_path, 'r', encoding='utf-8') as f:
    biblia_content = f.read()

# Definir contexto completo
context_payload = f"""
CONFIGURACIÓN DE GUARDIDÁN DEL ARCO - AGENTE CRÍTICO:
Has sido cargado con el ARCO ARGUMENTAL y la BIBLIA del relato 'Smart Home Stepford'.
Tu misión es vigilar que la transformación de Clara sea gradual y que el condicionamiento sensorial siga las reglas de la casa.

### ARCO ARGUMENTAL
{arco_content}

### BIBLIA DEL RELATO
{biblia_content}

Confirma que estás listo para auditar el Capítulo 1 y verificar si los nuevos mensajes subliminales y la integración de Loyaltty respetan la curva de rendición.
"""

payload = {
    'model': 'qwen2.5-7b-instruct-1m',
    'messages': [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': context_payload}
    ],
    'temperature': 0.7,
    'max_tokens': 1024,
    'stream': False
}

print('Cargando Motor CRITICO en LM Studio...')
try:
    resp = requests.post('http://127.0.0.1:1234/v1/chat/completions', json=payload, timeout=600)
    resp.raise_for_status()
    result = resp.json()
    
    answer = result['choices'][0]['message']['content']
    print('\n[RESPUESTA DEL CRÍTICO]:\n')
    print(answer)
    print('\n[EXITO] Guardián del Arco configurado.')
    
except Exception as e:
    print('\nERROR al conectar con LM Studio:', str(e))
