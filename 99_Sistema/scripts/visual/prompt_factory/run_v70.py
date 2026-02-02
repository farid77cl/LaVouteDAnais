from factory import PromptFactory
import os

# Rutas relativas
current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, "configs", "v70_pilot.json")
output_dir = os.path.abspath(os.path.join(current_dir, "..", "..", "..", "..", "00_Helena", "bancos_prompts"))

# Ejecutar
factory = PromptFactory(config_path)
factory.generate(output_dir)
