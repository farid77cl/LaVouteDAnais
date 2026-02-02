import sys
import os

# Add parent directory to path to import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from factory import PromptFactory

def main():
    print("Iniciando PromptFactory para:  BANCO DE PROMPTS V71 - VIP ESCORT & STRIPPER")
    
    # Initialize factory with V71 config
    factory = PromptFactory('99_Sistema/scripts/visual/prompt_factory/configs/v71_vip_escort.json')
    
    # Generate prompts
    output_dir = "C:/Users/fabara/LaVouteDAnais/00_Helena/bancos_prompts/"
    output_file = factory.generate(output_dir)
    
    print(f"Banco generado exitosamente: {output_file}")

if __name__ == "__main__":
    main()
