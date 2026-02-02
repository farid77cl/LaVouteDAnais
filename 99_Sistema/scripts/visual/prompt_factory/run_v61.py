import sys
import os

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from factory import PromptFactory

def main():
    # Caminos relativos al script
    config_path = os.path.join(os.path.dirname(__file__), 'configs', 'v61_corporate_plastic.json')
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '00_Helena', 'bancos_prompts'))
    
    factory = PromptFactory(config_path)
    factory.generate(output_dir)

if __name__ == "__main__":
    main()
