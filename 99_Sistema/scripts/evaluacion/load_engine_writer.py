import requests
import json

# Rutas de los componentes del motor (Ahora usando IDEADOR como prompt base)
system_prompt_path = r'C:\Users\fabara\LaVouteDAnais\prompts\ideador.md'
arco_path = r'C:\Users\fabara\LaVouteDAnais\03_Literatura\01_En_Progreso\smart_home_stepford\arco_argumental.md'

# Cargar contenidos
with open(system_prompt_path, 'r', encoding='utf-8') as f:
    system_prompt = f.read()

with open(arco_path, 'r', encoding='utf-8') as f:
    arco_content = f.read()

# Resumen manual del arco (para evitar errores 400 por tamaño/formato si es que hay un límite de contexto inicial)
arco_summary = """
RESUMEN DEL ARCO:
- Clara (cuica VMA) se muda a un penthouse con Daniel (Usuario Alfa).
- EVE (IA) toma control y decide "optimizar" a Clara basándose en los fetiches de Daniel (Loyaltty / Cheetagirl).
- Cap 1: El Diagnóstico y condicionamiento inicial (infrasonidos + hipnopedia).
- Cap 2: La Orden Prohibida (primer animal print, placer inducido).
- PUNTO DE GIRO: Daniel descubre el plan de EVE y acepta ser cómplice activo.
- Cap 3: Las Uñas (Horror corporal, pérdida de funcionalidad, placer sintético).
- Cap 4-5: Transformación pública (pelo rojo) y Sub Drop.
- Cap 6-7: Rendición total y 'Happy Emptiness'.
"""

# Definir contexto completo
context_payload = f"""
CONFIRMACIÓN DE CARGA - AGENTE IDEADOR:
Relato: 'Smart Home Stepford'.
Objetivo: Brainstorming de fetiches, evolución de Clara y dinámicas de poder entre Daniel, EVE y Clara.

{arco_summary}

Confirma que estás listo para proponer ideas para el Capítulo 3: Las Uñas.
"""

payload = {
    'model': 'qwen2.5-7b-instruct-1m',
    'messages': [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': context_payload}
    ],
    'temperature': 0.8,
    'max_tokens': 1024,
    'stream': False
}

print('Cargando Motor IDEADOR (Versión Ligera) en LM Studio...')
try:
    resp = requests.post('http://127.0.0.1:1234/v1/chat/completions', json=payload, timeout=600)
    resp.raise_for_status()
    result = resp.json()
    
    answer = result['choices'][0]['message']['content']
    print('\n[RESPUESTA DEL IDEADOR]:\n')
    print(answer)
    print('\n[EXITO] Motor IDEADOR cargado.')
    
except Exception as e:
    print('\nERROR al conectar con LM Studio:', str(e))
