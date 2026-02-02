import random

file_path = r"C:\Users\fabara\LaVouteDAnais\00_Helena\bancos_prompts\banco_prompts_v64_miss_doll_animal_fashion.md"

base_header = """# 🐆 BANCO DE PROMPTS V64: Miss Doll - Animal Print Fashion (EXTREME CANON - Standard v38)

**Referencia Visual:** Miss Doll (Persona de Élite de La Voûte, 28+).
**Estética:** High Fashion Animal Print (Leopardo & Serpiente ONLY).
**Prendas:** Vestidos, Pantalones, Faldas, Abrigos, Trajes. (NO BIKINIS, NO LENCERÍA).
**Formato:** 8k Vertical Portrait (ALWAYS).

> [!IMPORTANT]
> **PROTOCOLO DE ALTA FIDELIDAD (AUDITED):** SENSUALITY > RULES. Corsets are OPTIONAL. Focus on "Eye Candy" & High Fashion. Includes age (28+), refined features.

---
"""

# Base characteristics
intro = "Professional High-Detail Glamour photography of woman 28+ years old mature glamorous with platinum blonde bob haircut WITHOUT bangs (exposing forehead). Flawless porcelain skin with satin finish (NO rosy cheeks). Delicate refined nose, high cheekbones."
makeup = "HEAVY GLAMOUR MAKEUP: bronze/champagne smokey eyes with shimmer inner corners, thick cat-eye winged liner, mega volume wispy false lashes, defined arched brows, ULTRA PLUMP overlined glossy PINK lips (bee-stung lips)."
expression = "Human realistic face with pouting parted lips and seductive expression."
body = "EXTREME hourglass silhouette with large high-profile silicon breast implants creating prominent cleavage."
shoes = "PLEASER platform heels 18cm (8-inch) black patent."
footer = "Photorealistic 8k. Vertical portrait."

# Garment Templates (50 Leopard, 50 Snake)
garments_leopard = [
    "Wearing a floor-length LEOPARD PRINT silk wrap dress with a plunging neckline and thigh-high slit.",
    "Wearing a tight LEOPARD PRINT pencil skirt and a matching cropped blazer. No shirt underneath, revealing cleavage.",
    "Wearing a LEOPARD PRINT faux fur coat open over a black latex mini dress (non-lingerie style).",
    "Wearing high-waisted LEOPARD PRINT wide-leg trousers and a tight black velvet turtleneck.",
    "Wearing a LEOPARD PRINT latex catsuit (fully covered legs and arms) with a high collar.",
    "Wearing a LEOPARD PRINT silk slip dress (outerwear style) with a heavy leather jacket draped over shoulders.",
    "Wearing a structured LEOPARD PRINT suit with sharp shoulder pads and a deep V-neck (no shirt).",
    "Wearing a LEOPARD PRINT mini skater dress with long sleeves and a low chest cut.",
    "Wearing a LEOPARD PRINT PVC trench coat belted tightly as a dress.",
    "Wearing a LEOPARD PRINT velvet evening gown with an open back and mermaid train."
] * 5  # 50 items

garments_snake = [
    "Wearing a EMERALD GREEN SNAKESKIN PVC trench coat buttoned up to the waist, revealing legs.",
    "Wearing a GREY SNAKESKIN leather mini skirt and a matching corset-style top (outerwear).",
    "Wearing a RED SNAKESKIN latex bodycon dress with long sleeves and a high neck.",
    "Wearing a PYTHON PRINT silk blouse unbuttoned deeply and tight black leather trousers.",
    "Wearing a SNAKESKIN PRINT suit vest and matching trousers, boss lady aesthetic.",
    "Wearing a BLUE SNAKESKIN vinyl tube dress that hits below the knee.",
    "Wearing a GOLDEN SNAKESKIN texture ballgown with a massive skirt.",
    "Wearing a SNAKESKIN PRINT denim jacket and matching ultra-short shorts.",
    "Wearing a SILVER SNAKESKIN chainmail dress draped loosely but revealing.",
    "Wearing a PYTHON PRINT maxi dress with side cut-outs exposing the waist."
] * 5 # 50 items

# Environments
environments = [
    "Luxury hotel lobby with marble floors.", 
    "High-end fashion boutique.", 
    "Red carpet event with paparazzi flashes.", 
    "Executive office with city view.", 
    "Private jet leather interior.", 
    "Parisian street cafe terrace.", 
    "Modern art gallery white room.", 
    "Luxury penthouse balcony at night.", 
    "Dark limousine interior.", 
    "Backstage at a fashion show."
]

prompts = []

# Generate 50 Leopard
for i in range(50):
    garment = garments_leopard[i]
    env = random.choice(environments)
    prompts.append(f"""
### Prompt {i+1}: Leopard Fashion {i+1}
```text
{intro} {makeup} {expression} {body} {garment} {shoes} {env} {footer}
```
""")

# Generate 50 Snake
for i in range(50):
    garment = garments_snake[i]
    env = random.choice(environments)
    prompts.append(f"""
### Prompt {i+51}: Snake Fashion {i+1}
```text
{intro} {makeup} {expression} {body} {garment} {shoes} {env} {footer}
```
""")

# Write file
with open(file_path, "w", encoding="utf-8") as f:
    f.write(base_header)
    f.write("\n## 🐆 SECCIÓN 1: Leopard Luxury (Prompts 1-50)\n")
    f.write("".join(prompts[:50]))
    f.write("\n## 🐍 SECCIÓN 2: Snake Elegance (Prompts 51-100)\n")
    f.write("".join(prompts[50:]))

print("File generated successfully.")
