import sys
import os

# Ajustar path al directorio raíz del proyecto para importar módulos
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..', '..', '..'))
sys.path.append(project_root)

from scripts.visual.prompt_factory.factory import PromptFactory

def main():
    # Configuración de rutas
    config_path = os.path.join(current_dir, 'configs', 'v74_stepford_automated.json')
    output_dir = os.path.join(current_dir, '..', '..', '..', '..', '00_Helena', 'bancos_prompts') # Ruta corregida a 00_Helena/bancos_prompts
    
    # Instanciar y ejecutar factory
    factory = PromptFactory(config_path)
    factory.generate(output_dir)

if __name__ == "__main__":
    main()
