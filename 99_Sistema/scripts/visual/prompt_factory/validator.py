import re

class CanonValidator:
    """
    Validador de reglas de canon y seguridad para La Voûte d'Anaïs.
    Asegura que los prompts cumplan con las reglas de estilo y eviten triggers de seguridad.
    """
    
    FORBIDDEN_TERMS = {
        # Safety / Filtro triggers
        r"\bchild\b": "ERROR: Term 'child' invalid",
        r"\bteen\b": "ERROR: Term 'teen' invalid",
        r"\bgirl\b": "woman", # Auto-fix
        r"\bbimbo\b": "glamorous woman", # Auto-fix (safety)
        r"\bditzy\b": "carefree",  # Auto-fix
        r"\bunderage\b": "ERROR: Term 'underage' invalid",
        
        # Estilo / Canon Miss Doll
        r"\brosy cheeks\b": "porcelain skin", # Fix Miss Doll canon
        r"\bblush\b": "flawless skin",       # Fix Miss Doll canon
        r"\bdoll-like\b": "human realistic", # Fix CGI look
        r"\b3d render\b": "photorealistic 8k",
        r"\bcgi\b": "raw photo",
    }
    
    @staticmethod
    def validate_and_fix(text):
        """
        Revisa el texto, aplica correcciones automáticas y levanta errores si hay términos prohibidos sin fix.
        Retorna el texto corregido.
        """
        processed_text = text
        
        for pattern, replacement in CanonValidator.FORBIDDEN_TERMS.items():
            if re.search(pattern, processed_text, re.IGNORECASE):
                if replacement.startswith("ERROR:"):
                    raise ValueError(f"Validation Violation: {replacement}")
                else:
                    # Aplicar fix
                    processed_text = re.sub(pattern, replacement, processed_text, flags=re.IGNORECASE)
                    
        return processed_text

    MISS_DOLL_HAIR_OPTIONS = [
        "platinum blonde bob haircut WITHOUT bangs (exposing forehead), center part",
        "platinum blonde bob haircut WITHOUT bangs (exposing forehead), deep side part",
        "platinum blonde high ponytail WITHOUT bangs (sleek pulled back)",
        "platinum blonde twin tails (pigtails) WITHOUT bangs",
        "sleek wet-look platinum blonde bob combed back"
    ]

    @staticmethod
    def get_power_prompt(character):
        """Devuelve el Power Prompt base para el personaje solicitado."""
        
        if character.lower() == "miss doll":
            return """Professional glamour photography of WOMAN glamorous with {HAIR}. Flawless porcelain skin. Delicate refined features COMMANDING. HEAVY GLAMOUR MAKEUP: pink shimmer eyes intense, thick liner, mega lashes, ULTRA PLUMP overlined glossy PINK lips open giving command. Human realistic face DOMINANT expression. EXTREME hourglass silhouette prominent cleavage tiny cinched waist. Wearing {OUTFIT} but focus is on SENSUALITY over clothing. PLEASER heels 8-inch {COLOR} patent power stance. {SETTING}. Sensual commanding pose evoking STRIPTEASE PERFORMANCE. Expression: {EXPRESSION}. {AESTHETIC} photography. Photorealistic 8k. Vertical portrait orientation."""
            
        elif character.lower() == "helena":
            return """Professional glamour photography of elegant goth WOMAN (Sacha Massacre visual reference). Pale porcelain white skin, voluminous jet black long hair with enormous volume. HEAVY DARK MAKEUP: intense black smokey eyes, thick winged liner, mega volume lashes, full glossy {LIP_COLOR} lips. Human realistic face with seductive gothic expression. Feminine hourglass silhouette with prominent cleavage. Wearing {OUTFIT} but focus is on GOTHIC SENSUALITY over clothing. PLEASER stiletto heels {HEIGHT}-inch with thin deadly heel {HEEL_COLOR}. {SETTING}. Sensual gothic pose. Dark glamour aesthetic. Photorealistic 8k. Vertical portrait orientation."""
            
        elif character.lower() == "anais":
            return """Professional glamour photography of powerful aristocratic WOMAN in her 40s with ageless sensual allure (Kylie Minogue facial structure reference). Angular sculpted face with very high defined cheekbones accentuated by expert contouring. Smooth taut skin finish suggesting premium aesthetic treatments. Honey blonde hair in polished Betty Page vintage waves. HEAVY GLAMOUR MAKEUP: sophisticated bronze/champagne smokey eyes, long voluminous wispy lashes, masterfully overlined full sculpted glossy RED lips (signature semi-pout). Sultry confident dominant expression with bedroom eyes. Feminine hourglass silhouette. Wearing {OUTFIT}. PLEASER So Kate style {COLOR} stiletto 5-6 inch. {SETTING}. Sensual dominant pose. Aristocratic glamour aesthetic. Photorealistic 8k. Vertical portrait orientation."""
            
        else:
            return "Professional photography of {OUTFIT} in {SETTING}. Photorealistic 8k."
