import json
import os
import random
import datetime
from validator import CanonValidator

class PromptFactory:
    def __init__(self, config_path):
        self.config_path = config_path
        self.load_config()
        self.template_path = os.path.join(os.path.dirname(__file__), 'templates', 'bank_template.md')
        
    def load_config(self):
        with open(self.config_path, 'r', encoding='utf-8') as f:
            self.config = json.load(f)

    def generate(self, output_dir, force_count=None):
        # Sanitize title for console output
        safe_title = self.config.get('title', 'Unknown').encode('ascii', 'ignore').decode('ascii')
        print(f"Iniciando PromptFactory para: {safe_title}")
        
        prompts_output = ""
        total_generated = 0
        
        # Estrategia: Generar combinaciones
        characters = self.config.get('characters', ['Miss Doll'])
        variables = self.config.get('variables', {})
        
        # Generar target_count o force_count
        target_count = force_count if force_count else self.config.get('target_count', 100)
        
        # Anti-duplicates tracking
        seen_combinations = set()
        attempts = 0
        max_attempts = target_count * 5  # Evitar ciclos infinitos

        
        while total_generated < target_count and attempts < max_attempts:
            attempts += 1
            char = random.choice(characters)
            
            # Seleccionar variables random
            outfit = random.choice(variables.get('outfits', ['black latex dress']))
            setting = random.choice(variables.get('settings', ['dark studio']))
            expression = random.choice(variables.get('expressions', ['seductive']))
            aesthetic = random.choice(variables.get('aesthetics', ['glamour']))
            
            # Dynamic Pose selection
            pose = random.choice(variables.get('poses', CanonValidator.UNIVERSAL_POSES))
            
            # Variables especificas por personaje para rellenar huecos
            # Default values initialization
            color = random.choice(variables.get('colors', ['pink', 'black'])) 
            heel_height = random.choice(variables.get('heel_heights', ['8']))
            
            # Character Specific Logic
            if char.lower() == "helena":
                lip_color = random.choice(CanonValidator.HELENA_LIP_COLORS)
                hair = random.choice(CanonValidator.HELENA_HAIR_OPTIONS)
                makeup_color = "dark"
                aesthetic = random.choice(CanonValidator.HELENA_AESTHETICS)
                
            elif char.lower() == "miss doll":
                lip_color = random.choice(variables.get('lip_colors', CanonValidator.MISS_DOLL_MAKEUP_COLORS))
                hair = random.choice(CanonValidator.MISS_DOLL_HAIR_OPTIONS)
                makeup_color = random.choice(variables.get('makeup_colors', CanonValidator.MISS_DOLL_MAKEUP_COLORS))
                makeup_color = random.choice(variables.get('makeup_colors', ['pink', 'red', 'nude', 'dark']))
                # If pose should be more specific for doll roles like stripper
                if "stripper" in self.config.get('theme', '').lower():
                    doll_poses = list(CanonValidator.UNIVERSAL_POSES) + [
                        "holding onto a brass dance pole",
                        "captured mid-spin during a performance",
                        "grinding against a velvet couch in a VIP room",
                        "bending over while checking her reflection"
                    ]
                    pose = random.choice(doll_poses)
            else:
                # Fallback for others (Anais)
                hair = "" 
                lip_color = "red"
                makeup_color = "dark"
            
            # Anti-Duplicate Check
            combo_key = f"{char}|{outfit}|{setting}|{pose}|{expression}"
            if combo_key in seen_combinations:
                continue
            seen_combinations.add(combo_key)

            # Obtener base power prompt
            base_prompt = CanonValidator.get_power_prompt(char)
            
            # Rellenar template
            format_args = {
                "OUTFIT": outfit,
                "SETTING": setting,
                "EXPRESSION": expression,
                "AESTHETIC": aesthetic,
                "COLOR": color,
                "HEIGHT": heel_height,
                "LIP_COLOR": lip_color,
                "HEEL_COLOR": color,
                "HAIR": hair,
                "MAKEUP_COLOR": makeup_color,
                "POSE": pose
            }
            
            try:
                final_prompt = base_prompt.format(**format_args)
            except KeyError:
                # Fallback replacement
                final_prompt = base_prompt
                for key, val in format_args.items():
                    final_prompt = final_prompt.replace(f"{{{key}}}", str(val))
            
            # Validar y Corregir
            final_prompt = CanonValidator.validate_and_fix(final_prompt)
            
            # Formatear salida Markdown
            # Improved header with more context
            header_title = f"{char} - {outfit} - {pose}"
            if len(header_title) > 60:
                header_title = header_title[:57] + "..."
                
            prompts_output += f"### {total_generated+1:03d}: {header_title}\n"
            prompts_output += "```text\n"
            prompts_output += final_prompt + "\n"
            prompts_output += "```\n\n"
            
            total_generated += 1
            
        print(f"Generated {total_generated} unique prompts (Attempts: {attempts})")

            
        # Leer Template Maestro
        with open(self.template_path, 'r', encoding='utf-8') as f:
            template_content = f.read()
            
        # Rellenar Archivo Final
        final_content = template_content.replace("{TITLE}", self.config.get('title'))
        final_content = final_content.replace("{TOTAL_PROMPTS}", str(total_generated))
        final_content = final_content.replace("{DATE}", datetime.datetime.now().strftime("%Y-%m-%d"))
        final_content = final_content.replace("{PROMPTS_CONTENT}", prompts_output)
        final_content = final_content.replace("{THEME}", self.config.get('theme'))
        final_content = final_content.replace("{CHARACTERS}", ", ".join(characters))
        
        # Guardar
        filename = f"banco_prompts_{self.config.get('id')}_{self.config.get('slug')}.md"
        output_path = os.path.normpath(os.path.join(output_dir, filename))
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_content)
            
        return output_path

        return output_path

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="PromptFactory CLI")
    parser.add_argument("--config", "-c", required=True, help="Path to config JSON file")
    parser.add_argument("--output", "-o", default="../../../00_Helena/bancos_prompts/", help="Output directory")
    parser.add_argument("--count", "-n", type=int, help="Override number of prompts to generate")
    
    args = parser.parse_args()
    
    if os.path.exists(args.config):
        factory = PromptFactory(args.config)
        output_file = factory.generate(args.output, args.count)
        print(f"✅ Banco generado en: {output_file}")
    else:
        print(f"❌ Config file not found: {args.config}")
