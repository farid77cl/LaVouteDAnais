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
            
    def generate(self, output_dir):
        # Sanitize title for console output
        safe_title = self.config.get('title', 'Unknown').encode('ascii', 'ignore').decode('ascii')
        print(f"Iniciando PromptFactory para: {safe_title}")
        
        prompts_output = ""
        total_generated = 0
        
        # Estrategia: Generar combinaciones
        # Si 'strategies' está definido en JSON, usarlo. Si no, random mix básico.
        
        characters = self.config.get('characters', ['Miss Doll'])
        variables = self.config.get('variables', {})
        
        # Generar 100 prompts por defecto o lo que diga config
        target_count = self.config.get('target_count', 100)
        
        for i in range(target_count):
            char = random.choice(characters)
            
            # Seleccionar variables random
            outfit = random.choice(variables.get('outfits', ['black latex dress']))
            setting = random.choice(variables.get('settings', ['dark studio']))
            expression = random.choice(variables.get('expressions', ['seductive']))
            aesthetic = random.choice(variables.get('aesthetics', ['glamour']))
            
            # Variables especificas por personaje para rellenar huecos
            color = random.choice(variables.get('colors', ['pink', 'black'])) # For Miss Doll / Anais
            heel_height = random.choice(variables.get('heel_heights', ['8'])) # For Helena
            lip_color = random.choice(variables.get('lip_colors', ['black'])) # For Helena
            
            # Hair selection
            if char.lower() == "miss doll":
                hair = random.choice(CanonValidator.MISS_DOLL_HAIR_OPTIONS)
                makeup_color = random.choice(variables.get('makeup_colors', ['pink', 'red', 'nude', 'dark']))
            else:
                hair = "" # Helena and Anais have static hair in their templates currently
                makeup_color = "dark" # Default fallback
            
            # Obtener base power prompt
            base_prompt = CanonValidator.get_power_prompt(char)
            
            # Rellenar template
            # Usamos safe_substitute o replace manual para flexibilidad
            try:
                final_prompt = base_prompt.format(
                    OUTFIT=outfit,
                    SETTING=setting,
                    EXPRESSION=expression,
                    AESTHETIC=aesthetic,
                    COLOR=color,
                    HEIGHT=heel_height,
                    LIP_COLOR=lip_color,
                    HEEL_COLOR=color,
                    HAIR=hair,
                    MAKEUP_COLOR=makeup_color
                )
            except KeyError as e:
                # Si falta alguna key en el format string del power prompt, manejamos
                # Esto pasa porque diferentes power prompts tienen diferentes keys.
                # Estrategia simple: rellenar lo que se pueda
                final_prompt = base_prompt.replace("{OUTFIT}", outfit)
                final_prompt = final_prompt.replace("{SETTING}", setting)
                final_prompt = final_prompt.replace("{EXPRESSION}", expression)
                final_prompt = final_prompt.replace("{AESTHETIC}", aesthetic)
                final_prompt = final_prompt.replace("{COLOR}", color)
                final_prompt = final_prompt.replace("{HEIGHT}", heel_height)
                final_prompt = final_prompt.replace("{LIP_COLOR}", lip_color)
                final_prompt = final_prompt.replace("{HEEL_COLOR}", color)
                final_prompt = final_prompt.replace("{HAIR}", hair)
                final_prompt = final_prompt.replace("{MAKEUP_COLOR}", makeup_color)
            
            # Validar y Corregir
            final_prompt = CanonValidator.validate_and_fix(final_prompt)
            
            # Formatear salida Markdown
            prompts_output += f"### {char} - {outfit} - {i+1:03d}\n"
            prompts_output += "```text\n"
            prompts_output += final_prompt + "\n"
            prompts_output += "```\n\n"
            
            total_generated += 1
            
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
        output_path = os.path.join(output_dir, filename)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_content)
            
        print(f"Banco generado exitosamente: {output_path}")

if __name__ == "__main__":
    # Ejemplo de uso directo
    # factory = PromptFactory("configs/v70_pilot.json")
    # factory.generate("../../../00_Helena/bancos_prompts/")
    pass
