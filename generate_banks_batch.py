import random

# CONFIGURACION GLOBAL
TEMPLATE_HEADER = """# {TITLE}

> **USO:** Copiar el texto del prompt directamente y pegar en el generador de imágenes.
> **Estado:** Optimizado v2.0 (Sensuality Protocol)

---

## 📋 CÓMO USAR ESTE ARCHIVO

1. **Buscar** el personaje y outfit deseado
2. **Copiar** todo el texto del prompt
3. **Pegar** directamente en el generador

---

## I. CANON VISUAL OBLIGATORIO

> [!CAUTION]
> **REGLAS ANTI-FILTRO:** NO usar "woman", "bimbo", "ditzy", "doll-like". Usar descripciones directas sin calificadores de edad.

### 💖 MISS DOLL (POWER PROMPT)

```text
Professional glamour photography of WOMAN glamorous with platinum blonde bob haircut WITHOUT bangs (exposing forehead). Flawless porcelain skin. Delicate refined features COMMANDING. HEAVY GLAMOUR MAKEUP: pink shimmer eyes intense, thick liner, mega lashes, ULTRA PLUMP overlined glossy PINK lips open giving command. Human realistic face DOMINANT expression. EXTREME hourglass silhouette prominent cleavage tiny cinched waist. Wearing [OUTFIT] but focus is on SENSUALITY over clothing. PLEASER heels 8-inch [COLOR] patent power stance. [SETTING]. Sensual commanding pose evoking STRIPTEASE PERFORMANCE. Expression: [EXPRESSION]. [AESTHETIC] photography. Photorealistic 8k. Vertical portrait orientation.
```

### 🦇 HELENA DE ANAÏS (POWER PROMPT)

```text
Professional glamour photography of elegant goth WOMAN (Sacha Massacre visual reference). Pale porcelain white skin, voluminous jet black long hair with enormous volume. HEAVY DARK MAKEUP: intense black smokey eyes, thick winged liner, mega volume lashes, full glossy [LIP_COLOR] lips. Human realistic face with seductive gothic expression. Feminine hourglass silhouette with prominent cleavage. Wearing [OUTFIT] but focus is on GOTHIC SENSUALITY over clothing. PLEASER stiletto heels [HEIGHT]-inch with thin deadly heel [HEEL_COLOR]. [SETTING]. Sensual gothic pose. Dark glamour aesthetic. Photorealistic 8k. Vertical portrait orientation.
```

### 👑 ANAÏS BELLAND (POWER PROMPT)

```text
Professional glamour photography of powerful aristocratic WOMAN in her 40s with ageless sensual allure (Kylie Minogue facial structure reference). Angular sculpted face with very high defined cheekbones accentuated by expert contouring. Smooth taut skin finish suggesting premium aesthetic treatments. Honey blonde hair in polished Betty Page vintage waves. HEAVY GLAMOUR MAKEUP: sophisticated bronze/champagne smokey eyes, long voluminous wispy lashes, masterfully overlined full sculpted glossy RED lips (signature semi-pout). Sultry confident dominant expression with bedroom eyes. Feminine hourglass silhouette. Wearing [OUTFIT]. PLEASER So Kate style [COLOR] stiletto 5-6 inch. [SETTING]. Sensual dominant pose. Aristocratic glamour aesthetic. Photorealistic 8k. Vertical portrait orientation.
```

---

## II. PROMPTS DEL BANCO

"""

TEMPLATE_FOOTER = """
---

## III. NOTAS Y VARIACIONES

- **Fondo Sugerido:** Studio lighting, Club neon, Luxury interior.
- **Expresión:** Seductive, Dominant, Vacant.

---

*🦇 Helena de Anaïs — La Voûte d'Anaïs*
"""

# ==========================================
# GENERADOR V65: MISS DOLL ANIMAL LINGERIE
# ==========================================
def generate_v65():
    filename = r"C:\Users\fabara\LaVouteDAnais\00_Helena\bancos_prompts\banco_prompts_v65_miss_doll_animal_lingerie.md"
    title = "🖤 BANCO DE PROMPTS V65 - MISS DOLL ANIMAL LINGERIE (SOLO DOLL)"
    
    prints = [
        ("Leopard Print", "classic leopard spots"), ("Zebra Print", "black and white zebra stripes"),
        ("Tiger Print", "orange and black tiger stripes"), ("Snake Skin", "realistic python texture"),
        ("Cheetah Print", "small distinct cheetah spots"), ("Cow Print", "black and white cow spots"),
        ("Giraffe Print", "large giraffe patterns"), ("White Tiger", "white and black tiger stripes"),
        ("Pink Leopard", "neon pink leopard spots"), ("Snow Leopard", "white and grey leopard spots")
    ]
    
    lingerie_types = [
        "micro-thong bikini set", "sheer mesh bodysuit", "strappy harness lingerie",
        "lace-trimmed barely there set", "velvet lingerie set", "cut-out monokini",
        "balconette bra and thong", "high-leg bodysuit", "garter belt set", "string bikini"
    ]
    
    settings = [
        "JUNGLE THEMED bedroom", "SAFARI LUXURY tent", "WHITE STUDIO with tropical plants",
        "GOLD CAGE set", "ANIMAL PRINT bedding", "NEON JUNGLE club",
        "LUXURY FUR rug", "WILD NATURE backdrop", "BAMBOO garden", "EXOTIC POOL side"
    ]
    
    content = TEMPLATE_HEADER.format(TITLE=title)
    
    count = 1
    for p_name, p_desc in prints:
        for l_type in lingerie_types:
            setting = random.choice(settings)
            prompt = f"""### {p_name} - {l_type.title()}
```text
Professional glamour photography of WOMAN glamorous with platinum blonde bob haircut WITHOUT bangs (exposing forehead). Flawless porcelain skin. HEAVY GLAMOUR MAKEUP. EXTREME hourglass silhouette. Wearing {p_desc} {l_type} (NO CORSET), 8-inch {p_name} Pleaser heels. {setting}. Sensual commanding pose evoking STRIPTEASE PERFORMANCE. Wild seductive expression. Photorealistic 8k. Vertical portrait orientation.
```
"""
            content += prompt + "\n"
            count += 1
            
    content += TEMPLATE_FOOTER
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print("Generado v65")

# ==========================================
# GENERADOR V66: 90s NOSTALGIA (Trio)
# ==========================================
def generate_v66():
    filename = r"C:\Users\fabara\LaVouteDAnais\00_Helena\bancos_prompts\banco_prompts_v66_90s_nostalgia.md"
    title = "🖤 BANCO DE PROMPTS V66 - 90s NOSTALGIA & POP CULTURE"
    
    scenarios = [
        # Clueless
        ("Miss Doll", "Yellow Plaid Suit (Clueless Cher)", "High School Hallway"),
        ("Helena", "Black & White Plaid Hat (Clueless Dionne)", "Beverly Hills Street"),
        # Matrix
        ("Anaïs", "Black Leather Trenchcoat (Matrix Trinity)", "Green Code Rain Background"),
        ("Miss Doll", "Shiny Black PVC Suit (Matrix)", "White Void Construct"),
        # Basic Instinct
        ("Miss Doll", "White Sleeveless Turtleneck Dress (Basic Instinct)", "Interrogation Room"),
        # Pulp Fiction
        ("Helena", "White Shirt & Black Bob (Mia Wallace)", "Retro 50s Diner"),
        # Baywatch
        ("Miss Doll", "Red High-Cut One Piece Swimsuit (Pamela)", "Sunny 90s Beach"),
        # Spice Girls
        ("Miss Doll", "Union Jack Mini Dress (Ginger Spice)", "90s Stage"),
        ("Helena", "Black Little Gucci Dress (Posh Spice)", "White Limousine"),
        # Tech
        ("Miss Doll", "Holding Clear Gameboy Color", "90s Bedroom with Posters"),
        ("Helena", "Holding VHS Tapes", "Video Rental Store"),
        ("Anaïs", "Holding Brick Cellphone", "90s Wall Street Office"),
        # Fashion
        ("Miss Doll", "Pink Slip Dress & Tiara", "Prom Night 1999"),
        ("Helena", "Grunge Flannel & Ripped Tights", "Seattle Rock Club"),
        ("Anaïs", "Power Suit with Shoulder Pads", "Corporate Boardroom 1995")
    ]
    
    content = TEMPLATE_HEADER.format(TITLE=title)
    
    # Generate 100 prompts by looping and varying details
    for i in range(100):
        person, outfit, set = scenarios[i % len(scenarios)]
        
        # Base prompt selection
        if person == "Miss Doll":
            base = "WOMAN glamorous with platinum blonde bob haircut WITHOUT bangs"
        elif person == "Helena":
            base = "elegant goth WOMAN (Sacha Massacre visual reference) jet black long hair"
        else:
            base = "powerful aristocratic WOMAN in her 40s (Kylie Minogue ref) Honey blonde waves"
            
        prompt = f"""### {person} - {outfit}
```text
Professional 90s FLASH photography of {base}. HEAVY 90s SUPERMODEL MAKEUP (brown lip liner). Wearing {outfit}. {set}. Pose inspired by 90s fashion editorials. Vintage film grain aesthetic. Photorealistic 8k. Vertical portrait orientation.
```
"""
        content += prompt + "\n"

    content += TEMPLATE_FOOTER
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print("Generado v66")

# ==========================================
# GENERADOR V67: RED CARPET FIX
# ==========================================
def generate_v67():
    filename = r"C:\Users\fabara\LaVouteDAnais\00_Helena\bancos_prompts\banco_prompts_v67_red_carpet_paparazzi.md"
    title = "📸 BANCO DE PROMPTS V67: RED CARPET PAPARAZZI (FIXED)"
    
    events = [
        "OSCARS Red Carpet", "MET GALA Stairs", "CANNES Film Festival",
        "GRAMMYS Press Wall", "MTV MOVIE AWARDS", "FILM PREMIERE Entrance",
        "CHARITY GALA Ballroom", "AFTER PARTY Club Entrance", "FASHION WEEK Front Row", "PRIVATE YACHT Party"
    ]
    
    outfits = [
        "Sheer Crystal Naked Dress", "Red Satin High Slit Gown", "Black Velvet Corset Gown",
        "Gold Chainmail Mini Dress", "Silver Sequin Mermaid Dress", "Pink Feathers Showgirl Dress",
        "Latex Couture Gown", "Diamond Encrusted Bodysuit", "Vintage 90s Slip Dress", "White Fur Coat & Diamonds"
    ]
    
    content = TEMPLATE_HEADER.format(TITLE=title)
    
    # 50 Miss Doll, 30 Helena, 20 Anaïs
    for i in range(100):
        if i < 50:
            person = "Miss Doll"
            desc = "WOMAN glamorous with platinum blonde bob haircut WITHOUT bangs"
        elif i < 80:
            person = "Helena"
            desc = "elegant goth WOMAN (Sacha Massacre visual reference) jet black long hair"
        else:
            person = "Anaïs"
            desc = "powerful aristocratic WOMAN in her 40s (Kylie Minogue ref)"
            
        evt = events[i % len(events)]
        out = outfits[i % len(outfits)]
        
        prompt = f"""### {person} - {out} @ {evt.split()[0]}
```text
Professional PAPARAZZI FLASH photography of {desc}. Flawless skin under harsh light. HEAVY GLAMOUR MAKEUP. Wearing {out}. {evt}. Surrounded by photographers. Expression: arrogant elite, ignoring cameras. High contrast flash photography. Photorealistic 8k. Vertical portrait orientation.
```
"""
        content += prompt + "\n"

    content += TEMPLATE_FOOTER
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print("Reparado v67")

if __name__ == "__main__":
    generate_v65()
    generate_v66()
    generate_v67()
