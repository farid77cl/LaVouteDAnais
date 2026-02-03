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
        "platinum blonde asymmetric bob haircut (platinum blonde hair ONLY)",
        "sleek wet-look platinum blonde bob combed back",
        "sharp geometric platinum blonde bob",
        "chin-length platinum blonde bob with shaved nape"
    ]

    MISS_DOLL_MAKEUP_COLORS = [
        "pink", "hot pink", "fuchsia", "nude", "red", "rose gold"
    ]

    HELENA_HAIR_OPTIONS = [
        "long sleek straight jet black hair, center part",
        "tight high jet black ponytail, sleek pulled back",
        "long jet black hair with sharp straight bangs",
        "wet-look jet black hair combed back",
        "voluminous 80s goth backcombed jet black hair"
    ]

    HELENA_LIP_COLORS = [
        "blood red", "black matte", "dark chrome", "toxic green", "deep purple", "oxblood"
    ]

    HELENA_AESTHETICS = [
        "Modern Industrial Goth",
        "Severely Elegant Corporate Goth",
        "Futuristic Cyber Noir",
        "Architectural Minimalist Neo-Goth",
        "Vanguard High Fashion Goth",
        "Vampiric Aristocrat"
    ]

    # New standard poses for variety
    UNIVERSAL_POSES = [
        "standing in a powerful model stance",
        "sitting elegantly with legs crossed",
        "lounging seductively on a piece of luxury furniture",
        "leaning against a surface with a playful gaze",
        "walking towards the camera with a confident stride",
        "captured in a candid 3/4 side profile view",
        "back view looking over her shoulder with a smirk",
        "kneeling with an arched back and seductive posture",
        "sprawled on her side in a glamorous pose",
        "close shot showing a dazed and happy facial expression"
    ]

    @staticmethod
    def get_power_prompt(character):
        """Devuelve el Power Prompt base para el personaje solicitado con soporte para {POSE}."""
        
        if character.lower() == "miss doll":
            return """Professional glamour photography of glamorous WOMAN with {HAIR}. ABSOLUTELY NO DARK HAIR. PLATINUM BLONDE HAIR ONLY. Flawless porcelain skin. {POSE}. Delicate refined features COMMANDING. HEAVY GLAMOUR MAKEUP: {MAKEUP_COLOR} shimmer eyes intense, thick liner, mega lashes, ULTRA PLUMP overlined glossy {MAKEUP_COLOR} lips open giving command. Human realistic face DOMINANT expression. EXTREME hourglass silhouette prominent cleavage tiny cinched waist. Wearing {OUTFIT} (fetish aesthetic) but focus is on SENSUALITY over clothing. PLEASER heels 8-inch {COLOR} patent. {SETTING}. Sensual pose. Expression: {EXPRESSION}. {AESTHETIC} photography. Photorealistic 8k. Vertical portrait orientation."""
            
        elif character.lower() == "helena":
            return """Professional glamour photography of elegant goth WOMAN (Sacha Massacre visual reference). Pale porcelain white skin, {HAIR}. {POSE}. HEAVY DARK MAKEUP: intense black smokey eyes, sharp liner, full glossy {LIP_COLOR} lips. Human realistic face with seductive submissive expression. Feminine hourglass silhouette with prominent cleavage. Wearing {OUTFIT} but focus is on {AESTHETIC} SENSUALITY over clothing. PLEASER stiletto heels {HEIGHT}-inch with thin deadly heel {HEEL_COLOR}. {SETTING}. Sensual pose. {AESTHETIC} aesthetic. Photorealistic 8k. Vertical portrait orientation."""
            
        elif character.lower() == "anais":
            return """Professional glamour photography of powerful aristocratic WOMAN in her 40s with ageless sensual allure (Kylie Minogue facial structure reference). Angular sculpted face with very high defined cheekbones. {POSE}. Smooth taut skin. Honey blonde hair in polished vintage waves. HEAVY GLAMOUR MAKEUP: sophisticated bronze smokey eyes, masterfully overlined glossy RED lips. Sultry confident dominant expression. Feminine hourglass silhouette. Wearing {OUTFIT}. PLEASER So Kate style {COLOR} stiletto 5-6 inch. {SETTING}. Aristocratic glamour aesthetic. Photorealistic 8k. Vertical portrait orientation."""
            
        else:
            return "Professional photography of {OUTFIT} in {SETTING}. {POSE}. Photorealistic 8k."
