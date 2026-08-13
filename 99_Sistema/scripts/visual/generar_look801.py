import os

look_num = 801
slug = "white_satin_nurse_bikini"
folder_name = f"look{look_num}_{slug}"
folder_path = os.path.join(r"c:\Users\farid\LaVouteDAnais\05_Imagenes\ele", folder_name)
os.makedirs(folder_path, exist_ok=True)

readme_path = os.path.join(folder_path, "README.md")
galeria_path = r"c:\Users\farid\LaVouteDAnais\00_Ele\galeria_outfits.md"

# Bloque A
bloque_a = "stunning woman with (bimbofied facial features, oval face, high prominent cheekbones, large almond-shaped grey-green eyes, straight slim upturned nose, overlined glossy hot pink lips, small pointed chin:1.3), flawless white porcelain skin, hyper-polished smooth skin texture, dramatic siren liner, dramatic lash extensions, dark cherry red hair, artificial XXXL extensions hip-length, voluminous waves, center parted, slender hourglass silhouette, massive 1000cc breast implants each side, ultra high-profile, perfectly spherical augmented bust, obviously fake gravity-defying shape, wide hips, blackwork arm tattoos shown only on bare uncovered skin, subtle minimalist blackwork tattoos on upper back and outer thighs, navel piercing, nipple piercings, every tattoo and piercing visible ONLY on genuinely bare skin and never through or over any garment, aggressive bimbomakeup, extra long French XXXL nails with white tips and pink base 5cm."

# Bloque B
bloque_b = "stunning woman wearing an Erotic Nurse look, a white high-gloss wet-satin micro bikini top barely containing her massive bust, matching white wet-satin micro bikini bottoms, a delicate sheer white lace mini nurse apron tied at the waist with a satin bow, no stockings, fully opaque at bust and groin, no text, bare arms and bare hands"

# Calzado Token
calzado_token = "clear transparent acrylic platform stiletto sandals, 8-inch thin pin stiletto heel plus 4-inch clear acrylic platform, open toe, clear ankle strap with a silver buckle, clear sole"

# Ancora & Anti-defecto
anclas = "wherever the garment covers the body its fabric surface is perfectly smooth, taut and unbroken — a clean featureless glossy surface over the bust, the nipples, the navel and the hips, with nothing pressing through it, printed on it or showing under it; every tattoo and every body piercing exists ONLY on genuinely bare exposed skin, never through the fabric and never drawn over any sleeve, panel or covered area of the garment, her hands, fingers, neck, throat, sternum, shins, calves and feet are clean unmarked porcelain skin with no tattoos and no glyphs; the blackwork tattoos exist exactly where described — on the arms, the upper back, the outer thighs and along one hip crease — and nowhere else, present there whenever that skin is bare, beyond the garment's described sleeve length the skin of her arms, forearms, wrists and hands is genuinely bare, smooth uncovered porcelain skin catching the light, with no gloves of any kind, no separate arm sleeves, arm warmers, detached cuffs, forearm bands or elbow-length coverings added"

setting = "in a luxury dimly lit private BDSM preparation suite at La Voûte, black marble floor, velvet furniture, warm candle glow, and subtle perfume mist"

cierre = "Cinematic studio lighting to define silhouette, high-gloss specularity on satin and acrylic surfaces, a highly stylized luxury fetish atmosphere."

# Poses
poses = {
    "standing": "a single continuous photograph: one woman alone in one single full-bleed frame that fills the entire image edge to edge, one scene and one moment, NOT a collage, NOT a grid or multi-panel layout, NOT a contact sheet, storyboard, photo strip or split screen, with no internal borders, dividers or picture-in-picture insets, and nothing inside the scene — no mirror, screen, poster, framed picture or light box — showing her image a second time, anatomically correct with exactly two arms, two hands each with five fingers, two legs and two feet, full body from a low angle, standing with weight on one hip, one XXXL-nailed hand on her waist and the other hand resting gracefully on her thigh, hips swung, seductive smile with glossy parted lips",
    "back_view": "a single continuous photograph: one woman alone in one single full-bleed frame that fills the entire image edge to edge, one scene and one moment, NOT a collage, NOT a grid or multi-panel layout, NOT a contact sheet, storyboard, photo strip or split screen, with no internal borders, dividers or picture-in-picture insets, and nothing inside the scene — no mirror, screen, poster, framed picture or light box — showing her image a second time, anatomically correct with exactly two arms, two hands each with five fingers, two legs and two feet, full body back view, turning over her shoulder with a flirtatious gaze toward the camera, cherry red hair cascading down her spine, highlighting the lace apron bow tied over the micro bikini bottoms",
    "seated": "a single continuous photograph: one woman alone in one single full-bleed frame that fills the entire image edge to edge, one scene and one moment, NOT a collage, NOT a grid or multi-panel layout, NOT a contact sheet, storyboard, photo strip or split screen, with no internal borders, dividers or picture-in-picture insets, and nothing inside the scene — no mirror, screen, poster, framed picture or light box — showing her image a second time, anatomically correct with exactly two arms, two hands each with five fingers, two legs and two feet, seated on a plush black velvet armchair, legs crossed at the thigh, spine straight, one XXXL-nailed hand resting on her knee and the other touching her collarbone, seductive gaze",
    "side_profile": "a single continuous photograph: one woman alone in one single full-bleed frame that fills the entire image edge to edge, one scene and one moment, NOT a collage, NOT a grid or multi-panel layout, NOT a contact sheet, storyboard, photo strip or split screen, with no internal borders, dividers or picture-in-picture insets, and nothing inside the scene — no mirror, screen, poster, framed picture or light box — showing her image a second time, anatomically correct with exactly two arms, two hands each with five fingers, two legs and two feet, full body side profile, extreme lumbar arch pushing out the 1000cc bust and curved hips, chin lifted in profile, towering on stiletto heels",
    "ditzy": "a single continuous photograph: one woman alone in one single full-bleed frame that fills the entire image edge to edge, one scene and one moment, NOT a collage, NOT a grid or multi-panel layout, NOT a contact sheet, storyboard, photo strip or split screen, with no internal borders, dividers or picture-in-picture insets, and nothing inside the scene — no mirror, screen, poster, framed picture or light box — showing her image a second time, anatomically correct hands with exactly five fingers on each visible hand, waist-up sensual shot, face and bust in focus, glossy parted lips, vacant ditzy expression, one XXXL French-nailed finger playfully near her cheek",
    "pov": "a single continuous photograph: one woman alone in one single full-bleed frame that fills the entire image edge to edge, one scene and one moment, NOT a collage, NOT a grid or multi-panel layout, NOT a contact sheet, storyboard, photo strip or split screen, with no internal borders, dividers or picture-in-picture insets, and nothing inside the scene — no mirror, screen, poster, framed picture or light box — showing her image a second time, anatomically correct hands with exactly five fingers on each visible hand, sensual Instagram portrait leaning toward the camera, one XXXL-nailed hand in her cherry red hair, a smoldering half-lidded gaze, glossy parted lips, face dominant in upper-mid frame and voluptuous cleavage below",
    "odalisque": "a single continuous photograph: one woman alone in one single full-bleed frame that fills the entire image edge to edge, one scene and one moment, NOT a collage, NOT a grid or multi-panel layout, NOT a contact sheet, storyboard, photo strip or split screen, with no internal borders, dividers or picture-in-picture insets, and nothing inside the scene — no mirror, screen, poster, framed picture or light box — showing her image a second time, anatomically correct with exactly two arms, two hands each with five fingers, two legs and two feet, full body lying on her side on a plush velvet chaise lounge, languid S-curve, one arm extended with XXXL nails, legs slightly bent, stilettos pointed and visible"
}

neg_prompt = "gothic, vampire, fangs, red lips, dark lips, wine lips, maroon lips, crimson lips, oxblood lips, different person, different face, different hair color, brown hair, black hair, blonde hair, auburn hair, flat shoes, block heel, wedge, chunky heel, kitten heel, barefoot, socks, sneakers, different shoes, mismatched shoes, changing footwear, inconsistent footwear, different outfit, altered clothing, inconsistent outfit, different body, gloves, opera gloves, long gloves, elbow gloves, fingerless gloves, wrist gloves, leather gloves, satin gloves, lace gloves, covered hands, arm sleeves, arm warmers, detached sleeves, forearm cuffs, extra hands, third hand, extra arms, extra fingers, fused fingers, missing fingers, deformed hands, mutated hands, malformed fingers, three legs, extra leg, extra foot, two women, duplicate figure, split image, collage, grid of images, multi-panel layout, contact sheet, photo strip, storyboard, image divided into panels, borders dividing the image, mirror reflection showing a second copy of the same woman, framed picture of the same woman inside the scene, poster or screen showing the same woman, light box displaying another photo, inset photo, rotated image, sideways rotated frame, tilted horizon, first-person point of view, looking down over own body, overhead downward shot, fisheye, phone, smartphone, selfie stick, selfie, text on clothing, lettering on garment, embroidered name, logo, nipple piercings visible through clothing, nipple piercing pressing through the fabric, nipple bumps through fabric, nipples showing through the garment, navel piercing through the fabric, piercing on top of the garment, jewellery over the fabric, tattoo printed on the garment, tattoo showing through the sleeve, body markings through fabric, see-through bodice revealing piercings, a different neckline than described, altered sleeve length, a different hemline length than described, re-styled outfit, inconsistent dress cut, a two-piece version of the dress, a cropped version of the garment, varying print pattern, platform mule, mule, mule sandals, backless mule, slipper, slide sandal, stockings in a different colour than described, stockings missing their pattern, hosiery with a different colour than described, bare legs without stockings, mismatched hosiery, inconsistent stockings, matte fabric, cotton, wool, crepe, linen, dull non-reflective textile, flat fabric finish, natural matte cloth"

# Build README markdown
readme_content = f"""# Look 801: White Satin Nurse Bikini (13/08/2026 · Relato "Cartas a Anaïs" · Lencería · Erotic Nurse · blanco — Monoblock)

*Atuendo oficial de Ele en la suite de preparación de La Voûte d'Anaïs durante el relato «Cartas a Anaïs: Obtuve lo que pedí». Micro bikini de satén blanco húmedo con mini delantal de enfermera de encaje blanco transparente.* 🫦💉👙👠

- **Ubicacion:** `05_Imagenes/ele/look801_white_satin_nurse_bikini/`
- **Categoria / Subcategoria:** Lencería / Erotic Nurse
- **Tags:** #microbikini #nurse #wetsatin #laceapron #clearpleasers #lavoute #cartasanais #V35hardsync
- **Outfit (BLOQUE B):** {bloque_b}
- **Calzado (Token x7):** {calzado_token}
- **Ambientacion:** {setting}

### 📸 Imágenes (0/7 — Pendiente cuota API)

| Standing | Back View | Seated | Side Profile | Ditzy (waist-up) | POV (retrato IG) | Odalisque |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |

### 📝 Prompts V3.5 Hard-Sync

"""

for idx, (pose_name, pose_desc) in enumerate(poses.items(), 1):
    prompt_str = f"{bloque_a} {bloque_b}, {calzado_token}, {anclas}. {pose_desc}, {setting}, {cierre}"
    readme_content += f"**{idx}. {pose_name.capitalize().replace('_', ' ')}:**\n\n```\n{prompt_str}\n```\n\n"

readme_content += f"**Negative Prompt:** `{neg_prompt}`\n"

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme_content)

print(f"README.md de Look 801 creado en {readme_path}")

# Append to galeria_outfits.md
galeria_entry = f"""
## Look 801: White Satin Nurse Bikini (13/08/2026 · Relato "Cartas a Anaïs" · Lencería · Erotic Nurse · blanco — Monoblock)

*Atuendo oficial de Ele en la suite de preparación de La Voûte d'Anaïs durante el relato «Cartas a Anaïs: Obtuve lo que pedí». Micro bikini de satén blanco húmedo con mini delantal de enfermera de encaje blanco transparente.* 🫦💉👙👠

- **Ubicacion:** `05_Imagenes/ele/look801_white_satin_nurse_bikini/`
- **Categoria / Subcategoria:** Lencería / Erotic Nurse
- **Tags:** #microbikini #nurse #wetsatin #laceapron #clearpleasers #lavoute #cartasanais #V35hardsync
- **Outfit (BLOQUE B):** {bloque_b}
- **Calzado (Token x7):** {calzado_token}
- **Ambientacion:** {setting}

### 📸 Imágenes (0/7 — Pendiente cuota API)

| Standing | Back View | Seated | Side Profile | Ditzy (waist-up) | POV (retrato IG) | Odalisque |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |

### 📝 Prompts V3.5 Hard-Sync

"""

for idx, (pose_name, pose_desc) in enumerate(poses.items(), 1):
    prompt_str = f"{bloque_a} {bloque_b}, {calzado_token}, {anclas}. {pose_desc}, {setting}, {cierre}"
    galeria_entry += f"**{idx}. {pose_name.capitalize().replace('_', ' ')}:**\n\n```\n{prompt_str}\n```\n\n"

galeria_entry += f"**Negative Prompt:** `{neg_prompt}`\n\n---"

with open(galeria_path, "a", encoding="utf-8") as f:
    f.write(galeria_entry)

print(f"Look 801 añadido a galeria_outfits.md exitosamente.")
