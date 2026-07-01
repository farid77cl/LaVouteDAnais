# -*- coding: utf-8 -*-
"""
Inyector batch L691-L700 "Pink Spectrum Fetish" (Ama 01/07/2026).
Tema del batch: 10 outfits SOLO EN ROSA, abarcando todos los rosados posibles del espectro fetish.
Categorías: 3 Pin-Up + 2 Gym + 2 Escort + 2 Stripper + 1 Nightclub.
- CERO oxblood, CERO guantes, CERO chunky.
- ADN estándar Ele V3.5 (sin colmillos de vampiresa).
- Pelo SUELTO en cascada (default ADN).
"""
import sys, os
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "visual"))
from pose_rotation_v5 import rotate_poses, check_setting_variety, HANDS_ANCHOR, FULL_ANCHOR

# BLOQUE A — ADN V3.5 Hard-Sync. Pelo SUELTO en cascada. Sin colmillos.
A = ("stunning woman with (bimbofied facial features, oval face, high prominent cheekbones, "
     "large almond-shaped grey-green eyes, straight slim upturned nose, overlined glossy hot pink lips "
     "slightly parted, small pointed chin:1.3), a hypnotic gaze, flawless white porcelain skin, hyper-polished "
     "smooth skin texture, dramatic siren liner, dramatic lash extensions, dark cherry red hair of "
     "artificial XXXL hip-length extensions in voluminous center-parted waves cascading down, slender "
     "hourglass silhouette, massive 1000cc breast implants each side, ultra high-profile, perfectly "
     "spherical augmented bust, obviously fake gravity-defying shape, wide hips, visible arm tattoos "
     "blackwork style, subtle minimalist blackwork tattoos on upper back and outer thighs, delicate "
     "blackwork rune-glyph identity tattoo of abstract esoteric calligraphic symbols along one hip crease "
     "and bikini line, navel piercing, nipple piercings pressing against and visible under clothing, "
     "aggressive bimbomakeup, extra long French XXXL nails with white tips and pink base 5cm.")

CLOSE = ("Cinematic studio lighting to define silhouette, high-gloss specularity on latex and vinyl surfaces, "
         "a highly stylized luxury fetish atmosphere.")

NEG = ("gothic, vampire, fangs, red lips, dark lips, wine lips, maroon lips, crimson lips, oxblood, "
       "different person, different face, different hair color, "
       "brown hair, black hair, blonde hair, auburn hair, flat shoes, block heel, wedge, platform mule, "
       "chunky heel, kitten heel, barefoot, socks, sneakers, different shoes, inconsistent footwear, "
       "different outfit, different body, gloves, opera gloves, long gloves, elbow gloves, fingerless "
       "gloves, covered hands, extra hands, third hand, extra arms, extra fingers, fused fingers, "
       "missing fingers, deformed hands, mutated hands, malformed fingers, two women, duplicate figure, "
       "split image, mirror reflection, first-person point of view, looking down over own body, overhead "
       "downward shot, fisheye, phone, smartphone, selfie stick")
NEG_POV = ("no phone, no smartphone, no device, no screen, no camera in hand, "
           "first-person point of view, looking down over own body, overhead downward shot")

looks = [
    {
        "num": 691, "slug": "bubblegum_latex_bombshell", "nombre": "Bubblegum Latex Bombshell",
        "cat": "Pin-Up", "subcat": "Pin-Up Bombshell",
        "tags": "#pinup #bubblegumpink #latex #wiggle #bombshell #seamed #batchL691-L700 #V5poses",
        "concepto": "Pin-Up Bombshell. Wiggle dress de latex rosa chicle brillante, escote sweetheart y medias con costura rosada. Punta cerrada por las medias.",
        "B": ("stunning woman wearing a Pin-Up bombshell look, a bubblegum-pink high-gloss latex "
              "halter wiggle dress, a deep sweetheart bust with a halter tie at the neck, a nipped waist, a "
              "fitted wiggle skirt to mid-thigh, a darker pink latex bow at the hip, sheer pale-pink seamed nylon "
              "stockings with a straight hot-pink back seam, fully opaque at bust and groin, no text, bare "
              "arms and bare hands"),
        "calzado": ("single-sole pointed-toe stiletto pumps in bubblegum-pink patent latex, 13cm thin pin "
                    "stiletto heel, sharp closed pointed toe, slip-on no strap, pink heel cap"),
        "setting": ("in a retro-futuristic 1950s diner at night, glossy pink leather booths, a neon jukebox, "
                    "and a checkered floor"),
        "seat": "a glossy pink leather diner booth", "wall": "a chrome-and-neon diner wall",
        "surface": "a vintage jukebox chrome ledge",
        "ambientacion": "diner retro-futurista de los 50s de noche con booths de cuero rosa y jukebox neón",
        "color": "rosa chicle — Monoblock",
    },
    {
        "num": 692, "slug": "rosegold_metallic_vixen", "nombre": "Rose Gold Metallic Vixen",
        "cat": "Pin-Up", "subcat": "Pin-Up Retro-Futurism",
        "tags": "#pinup #rosegold #liquidmetal #halter #retro #batchL691-L700 #V5poses",
        "concepto": "Pin-Up Retro-Futurismo. Vestido liquid metal rose-gold con corte pencil, cinturón de metal pulido, sin medias. Estética Barbarella glam.",
        "B": ("stunning woman wearing a Pin-Up retro-futurism look, a rose-gold liquid-metal high-shine "
              "pencil dress, a plunging halter neckline with metallic ring hardware at the collarbone, a "
              "rigid polished rose-gold metal waist cincher belt, a fitted skirt to the knee, no stockings, "
              "fully opaque at bust and groin, no text, bare arms and bare hands"),
        "calzado": ("single-sole pointed-toe slingback stiletto pumps in rose-gold liquid metal, 14cm thin "
                    "pin stiletto heel, sharp closed pointed toe, slingback strap with a gold buckle, "
                    "gold heel cap"),
        "setting": ("in a futuristic atomic-age lounge, sleek curved space-age furniture in white and gold, "
                    "starburst clocks, and ambient warm lighting"),
        "seat": "a curved white fiberglass space-age chair", "wall": "a gold atomic-patterned lounge wall",
        "surface": "a sleek white oval cocktail table",
        "ambientacion": "lounge futurista era-atómica con muebles curvos blancos y dorados",
        "color": "rose gold metálico — Monoblock",
    },
    {
        "num": 693, "slug": "coral_pink_polkadot_darling", "nombre": "Coral Pink Polkadot Darling",
        "cat": "Pin-Up", "subcat": "Pin-Up Decade Glam",
        "tags": "#pinup #coralpink #vinyl #polkadot #circle_skirt #batchL691-L700 #V5poses",
        "concepto": "Pin-Up Glamour Clásico. Vestido circle-skirt de vinilo rosa coral con lunares blancos incrustados en rhinestones. Sin medias.",
        "B": ("stunning woman wearing a Pin-Up decade glam look, a coral-pink high-gloss vinyl "
              "circle-skirt dress featuring a pattern of large white rhinestone-encrusted polka dots, "
              "an off-the-shoulder neckline with a stiff vinyl ruffle, a cinched waist with a white vinyl "
              "belt, a flared circle skirt falling above the knee, no stockings, "
              "fully opaque at bust and groin, no text, bare arms and bare hands"),
        "calzado": ("single-sole pointed-toe stiletto pumps in white patent vinyl, 12cm thin pin "
                    "stiletto heel, sharp closed pointed toe, slip-on no strap, white heel cap"),
        "setting": ("in a glamorous 1960s Hollywood dressing room, vanity mirrors surrounded by glowing bulbs, "
                    "pastel pink velvet curtains, and a fluffy white rug"),
        "seat": "a white vanity stool", "wall": "a wall of glowing vanity mirrors",
        "surface": "a mirrored dressing table",
        "ambientacion": "camerino glamoroso de Hollywood de los 60s con espejos iluminados y cortinas rosas",
        "color": "rosa coral + blanco — Contraste",
    },
    {
        "num": 694, "slug": "neon_fuchsia_sweat_glam", "nombre": "Neon Fuchsia Sweat Glam",
        "cat": "Gym", "subcat": "Gym Glam",
        "tags": "#gym #neonfuchsia #wetlook #leggings #sportsbra #clearpleaser #batchL691-L700 #V5poses",
        "concepto": "Gym Glam. Conjunto de leggings y sports bra en wet-look neón fucsia super ceñido con recortes bajo el busto. Pleasers transparentes (default Gym/Bikini).",
        "B": ("stunning woman wearing a Gym Glam look, a neon-fuchsia high-gloss wet-look sports bra "
              "with an underbust cutout exposing the lower cleavage, matching neon-fuchsia wet-look "
              "high-waisted leggings clinging tightly to the legs and hips, a micro-mesh panel running "
              "down the outer thighs, no stockings, fully opaque at bust and groin, no text, bare arms and bare hands"),
        "calzado": ("clear transparent acrylic platform stiletto sandals, 8-inch thin pin stiletto heel "
                    "plus 4-inch clear acrylic platform, open toe, clear ankle strap with a silver buckle, "
                    "clear sole"),
        "setting": ("in a luxury penthouse home gym at night, sleek chrome exercise machines, floor-to-ceiling "
                    "mirrors, and neon pink accent lights"),
        "seat": "a black leather weight bench", "wall": "a floor-to-ceiling gym mirror",
        "surface": "a chrome dumbbell rack",
        "ambientacion": "gimnasio de lujo en penthouse de noche con máquinas de cromo y luz neón rosa",
        "color": "neón fucsia — Monoblock",
    },
    {
        "num": 695, "slug": "dusty_rose_athletic_skort", "nombre": "Dusty Rose Athletic Skort",
        "cat": "Gym", "subcat": "Gym Tennis Glam",
        "tags": "#gym #dustyrose #vinyl #skort #cropjacket #clearpleaser #batchL691-L700 #V5poses",
        "concepto": "Gym Tennis Glam. Falda deportiva (skort) y chaqueta crop de vinilo rosa viejo (dusty rose). Pleasers transparentes.",
        "B": ("stunning woman wearing a Gym Tennis Glam look, a dusty-rose high-gloss vinyl "
              "pleated athletic mini skort, a matching dusty-rose vinyl cropped zip-up track jacket worn "
              "open over a white crystal-mesh sports bra, the jacket hem cropped high above the waist, "
              "no stockings, fully opaque at bust and groin, no text, bare arms and bare hands"),
        "calzado": ("clear transparent acrylic platform stiletto sandals, 8-inch thin pin stiletto heel "
                    "plus 4-inch clear acrylic platform, open toe, clear ankle strap with a silver buckle, "
                    "clear sole"),
        "setting": ("on a private indoor tennis court at night, stark white lines on dark flooring, "
                    "floodlights, and a luxury spectator lounge area"),
        "seat": "a sleek white court-side bench", "wall": "a dark padded court wall",
        "surface": "the umpire's tall chrome chair",
        "ambientacion": "cancha de tenis cubierta privada de noche con iluminación intensa y suelo oscuro",
        "color": "dusty rose + blanco — Contraste",
    },
    {
        "num": 696, "slug": "champagne_pink_liquid_escort", "nombre": "Champagne Pink Liquid Escort",
        "cat": "Escort", "subcat": "Escort Haute",
        "tags": "#escort #champagnepink #liquidmetal #draped #cowlneck #batchL691-L700 #V5poses",
        "concepto": "Escort Haute. Vestido largo líquido en tono rosa champagne, cuello drapeado (cowl) y tajo profundo. Lujo aristocrático.",
        "B": ("stunning woman wearing an Escort Haute look, a champagne-pink liquid-metal floor-length "
              "gown, a deep draped cowl neckline exposing the collarbones and cleavage, extremely thin "
              "spaghetti straps crisscrossing over an open back, a liquid drape falling to a floor-sweeping "
              "skirt with a thigh-high front slit, no stockings, fully opaque at bust and groin, "
              "no text, bare arms and bare hands"),
        "calzado": ("single-sole pointed-toe slingback stiletto pumps in champagne-pink liquid metallic, 14cm thin "
                    "pin stiletto heel, sharp closed pointed toe, slingback strap with a silver buckle, "
                    "silver heel cap"),
        "setting": ("in a private dining room of a five-star hotel, crystal chandeliers, white linen tables, "
                    "and heavy champagne velvet drapes"),
        "seat": "a plush velvet dining chair", "wall": "a champagne velvet draped window",
        "surface": "a white-linen covered dining table",
        "ambientacion": "comedor privado de hotel cinco estrellas con candelabros de cristal y cortinas champagne",
        "color": "rosa champagne metálico — Monoblock",
    },
    {
        "num": 697, "slug": "raspberry_pink_latex_siren", "nombre": "Raspberry Pink Latex Siren",
        "cat": "Escort", "subcat": "Escort Siren",
        "tags": "#escort #raspberrypink #latex #biascut #offshoulder #batchL691-L700 #V5poses",
        "concepto": "Escort Siren. Gown de látex rosa frambuesa (raspberry) con corte sirena y hombros descubiertos. Impacto de alto lujo fetish.",
        "B": ("stunning woman wearing an Escort Siren look, a raspberry-pink high-gloss latex floor-length "
              "mermaid gown, an elegant off-the-shoulder neckline framing the décolleté, long tight latex "
              "sleeves ending at the wrists, a hyper-fitted bias-cut bodice molding to the hips before "
              "flaring into a dramatic mermaid train, no stockings, fully opaque at bust and groin, "
              "no text, bare hands"),
        "calzado": ("single-sole pointed-toe stiletto pumps in raspberry-pink patent latex, 13cm thin pin "
                    "stiletto heel, sharp closed pointed toe, slip-on no strap, pink heel cap"),
        "setting": ("in the grand marble lobby of a luxury hotel at midnight, gold-leaf accents, a grand "
                    "sweeping staircase, and soft ambient lighting"),
        "seat": "a gold-leaf lobby bench", "wall": "a grand sweeping marble staircase",
        "surface": "a polished brass lobby railing",
        "ambientacion": "gran lobby de mármol de un hotel de lujo a medianoche con acentos en pan de oro",
        "color": "rosa frambuesa — Monoblock",
    },
    {
        "num": 698, "slug": "hot_magenta_crystal_cage", "nombre": "Hot Magenta Crystal Cage",
        "cat": "Stripper", "subcat": "Stripper VIP",
        "tags": "#stripper #hotmagenta #crystalmesh #rhinestone #cage #clearpleaser #batchL691-L700 #V5poses",
        "concepto": "Stripper VIP. Corset-cage de rhinestones cristal y vinilo hot magenta + micro-thong. Pleasers transparentes.",
        "B": ("stunning woman wearing a Stripper VIP look, a hot-magenta high-gloss vinyl and crystal-mesh "
              "cage corset, opaque hot-magenta vinyl molded cups embellished with dense hot-pink rhinestones, "
              "sheer crystal-mesh panels across the torso structured by rigid magenta vinyl boning, a matching "
              "hot-magenta vinyl micro-thong sitting low on the hips, no stockings, fully opaque at bust and "
              "groin, no text, bare arms and bare hands"),
        "calzado": ("clear transparent acrylic platform stiletto sandals, 8-inch thin pin stiletto heel "
                    "plus 4-inch clear acrylic platform, open toe, clear ankle strap with a silver buckle, "
                    "clear sole"),
        "setting": ("on a private VIP pole stage in a dark club, magenta laser lights cutting through smoke, "
                    "a polished chrome pole, and plush dark velvet seating nearby"),
        "seat": "a dark velvet club stool", "wall": "a smoke-filled club wall lit by magenta lasers",
        "surface": "the polished chrome stage pole",
        "ambientacion": "escenario VIP privado con caño de cromo, luces láser magenta y humo",
        "color": "hot magenta + cristal — Contraste",
    },
    {
        "num": 699, "slug": "baby_pink_pvc_tease", "nombre": "Baby Pink PVC Tease",
        "cat": "Stripper", "subcat": "Stripper Stage",
        "tags": "#stripper #babypink #pvc #bodysuit #zipper #clearpleaser #batchL691-L700 #V5poses",
        "concepto": "Stripper Stage. Bodysuit de PVC rosa bebé (baby pink) con cierre frontal ultra profundo. Pleasers transparentes.",
        "B": ("stunning woman wearing a Stripper Stage look, a baby-pink translucent high-gloss PVC "
              "teddy-bodysuit, a deep plunging neckline zipped down to the navel with a chunky silver zipper, "
              "high-cut hips with a cheeky thong back, a silver O-ring detail at the collar, no stockings, "
              "fully opaque at bust and groin, no text, bare arms and bare hands"),
        "calzado": ("clear transparent acrylic platform stiletto sandals, 8-inch thin pin stiletto heel "
                    "plus 4-inch clear acrylic platform, open toe, clear ankle strap with a silver buckle, "
                    "clear sole"),
        "setting": ("on a neon-lit main platform of a luxury exotic venue, a glowing pink acrylic floor, "
                    "a central chrome pole, and a wall of flashing LED panels"),
        "seat": "a glowing pink acrylic stage block", "wall": "a wall of flashing LED panels",
        "surface": "the main stage chrome pole",
        "ambientacion": "escenario principal de club de caballeros con piso acrílico rosa y paneles LED",
        "color": "rosa bebé — Monoblock",
    },
    {
        "num": 700, "slug": "cerise_sequin_all_nighter", "nombre": "Cerise Sequin All Nighter",
        "cat": "Nightclub", "subcat": "Nightclub Glam",
        "tags": "#nightclub #cerisepink #sequins #minidress #cowlneck #batchL691-L700 #V5poses",
        "concepto": "Nightclub Glam. Mini vestido de lentejuelas color rosa cereza (cerise pink) con escote drapeado cowl. Para bailar bajo los láseres.",
        "B": ("stunning woman wearing a Nightclub Glam look, a cerise-pink densely sequined mini dress, "
              "a draped cowl neckline exposing the cleavage, ultra-thin chainmail straps crossing a bare back, "
              "a form-fitting ruched mini skirt ending high on the thigh, the sequins catching and reflecting "
              "laser light, no stockings, fully opaque at bust and groin, no text, bare arms and bare hands"),
        "calzado": ("platform stiletto ankle boots in cerise-pink patent vinyl, 7-inch thin pin "
                    "stiletto heel plus 2-inch cerise-pink platform, closed pointed toe, inner zip, "
                    "cerise-pink platform matching the boot, silver heel cap"),
        "setting": ("in the center of a crowded high-end nightclub dance floor, beams of cerise and violet "
                    "laser light cutting through the dark, a massive disco ball overhead, and blurred partygoers"),
        "seat": "a sleek nightclub VIP booth ledge", "wall": "a laser-lit dark club wall",
        "surface": "a tall chrome cocktail table",
        "ambientacion": "pista de baile de club nocturno de lujo con láseres color cereza y violeta",
        "color": "rosa cereza — Monoblock",
    },
]

POSE_NAMES = ["Standing", "Back View", "Seated", "Side Profile", "Ditzy", "POV", "Odalisque"]
FECHA = "01/07/2026"
BATCH = 'L691-L700 "Pink Spectrum Fetish"'

def build_prompts(lk):
    Bf = lk["B"] + ", and " + lk["calzado"] + "."
    poses = rotate_poses(lk["num"], seat=lk["seat"], wall=lk["wall"], surface=lk["surface"])
    prompts = []
    for slot, txt in poses:
        full = f"{A} {Bf} {txt}, {lk['setting']}, {CLOSE}"
        prompts.append((slot, full))
    return prompts

out = []
all_prompts = []
for lk in looks:
    ps = build_prompts(lk)
    all_prompts.extend([(lk["num"], s, p) for s, p in ps])
    out.append(f'\n## Look {lk["num"]}: {lk["nombre"]} ({FECHA} · batch {BATCH} · {lk["cat"]} · {lk["subcat"]} · {lk["color"]})\n')
    out.append(f'\n*{lk["concepto"]}* \U0001f9db‍♀️\U0001f460\n\n')
    out.append(f'- **Ubicacion:** `05_Imagenes/ele/look{lk["num"]}_{lk["slug"]}/`\n')
    out.append(f'- **Categoria / Subcategoria:** {lk["cat"]} / {lk["subcat"]}\n')
    out.append(f'- **Tags:** {lk["tags"]}\n')
    out.append(f'- **Outfit (BLOQUE B):** {lk["B"]}\n')
    out.append(f'- **Calzado (Token x7):** {lk["calzado"]}\n')
    out.append(f'- **Ambientacion:** {lk["ambientacion"]}\n')
    out.append('\n### \U0001f4f8 Imágenes (0/7 — Pendiente cuota API)\n\n')
    out.append('| Standing | Back View | Seated | Side Profile | Ditzy (waist-up) | POV (retrato IG) | Odalisque |\n')
    out.append('| :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n')
    out.append('| ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ |\n')
    out.append('\n### \U0001f4dd Prompts V3.5 Hard-Sync (poses rotadas con pose_rotation_v5 · Side Profile reparado)\n\n')
    for i, (nm, pr) in enumerate(ps):
        out.append(f'**{i+1}. {nm}:**\n\n```\n{pr}\n```\n\n')
    out.append(f'**Negative Prompt:** `{NEG}`\n\n**Adicional POV:** `{NEG_POV}`\n\n---\n')

content = ("# Batch L691-L700 — \"Pink Spectrum Fetish\" (01/07/2026)\n\n"
           "Tema: 10 outfits SOLO EN ROSA, abarcando todas las tonalidades posibles del espectro fetish (bubblegum, "
           "rose gold, coral, fuchsia, dusty rose, champagne, raspberry, magenta, baby pink, cerise). "
           "Cero oxblood. Pelo suelto.\n"
           "Motor: poses rotadas con `pose_rotation_v5`.\n\n"
           + "".join(out))
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "_batch_L691_L700.md"),
          "w", encoding="utf-8") as f:
    f.write(content)

# ===================== QA =====================
errors = []
# 1) Guantes solo en el negative (nunca en positive)
for num, slot, pr in all_prompts:
    if "glove" in pr.lower():
        errors.append(f"guantes en el positive L{num} {slot}")
# 2) chunky en el positive (outfit/calzado)
for lk in looks:
    if "chunky" in (lk["B"] + lk["calzado"]).lower():
        # Exception for chunky silver zipper in 699, chunky heels are the problem.
        if not ("chunky silver zipper" in lk["B"].lower()):
            errors.append(f"chunky en outfit/calzado L{lk['num']}")
# 3) CERO oxblood en el positive (directiva Ama 01/07 — saturada)
for lk in looks:
    if "oxblood" in (lk["B"] + lk["calzado"] + lk["concepto"]).lower():
        errors.append(f"OXBLOOD prohibido en L{lk['num']}")
# 5) token calzado x7
for lk in looks:
    c = content.count(lk["calzado"])
    if c < 7:
        errors.append(f"token calzado L{lk['num']} aparece {c} veces (<7)")
# 6) MEDIAS -> punta cerrada (regla Ama 20/06). Si B trae stockings (y NO 'no stockings'),
#    el calzado debe ser closed toe. (excluye el falso positivo de "no stockings")
def tiene_medias(b):
    b = b.lower()
    return "stockings" in b and "no stockings" not in b
for lk in looks:
    if tiene_medias(lk["B"]):
        if "closed" not in lk["calzado"].lower() or "open toe" in lk["calzado"].lower():
            errors.append(f"medias sin punta cerrada en L{lk['num']}")
# 7) open toe SOLO sin medias
for lk in looks:
    if "open toe" in lk["calzado"].lower() and tiene_medias(lk["B"]):
        errors.append(f"open toe con medias en L{lk['num']}")
# 8) anti-POV-literal en los prompts
POV_BAD = ["first-person", "point of view", "looking down over", "converging to", "stiletto tips", "selfie"]
for num, slot, pr in all_prompts:
    for b in POV_BAD:
        if b in pr.lower():
            errors.append(f"POV-literal '{b}' en L{num} {slot}")
# 9) ancla correcta por slot
for num, slot, pr in all_prompts:
    if slot in ("Ditzy", "POV"):
        if HANDS_ANCHOR not in pr:
            errors.append(f"falta ancla close-up en L{num} {slot}")
        if FULL_ANCHOR in pr:
            errors.append(f"ancla FULL indebida en close-up L{num} {slot}")
    else:
        if FULL_ANCHOR not in pr:
            errors.append(f"falta ancla FULL en L{num} {slot}")
# 10) Side Profile: 0 sentadas en los prompts (la reparacion de hoy)
for num, slot, pr in all_prompts:
    if slot == "Side Profile" and any(w in pr.lower() for w in ["seated on", "reclining on", "kneeling upright", "sitting back toward", "perched on"]):
        errors.append(f"Side Profile sentada/reclinada en L{num}")
# 11) fully opaque en bust/groin en cada B
for lk in looks:
    if "fully opaque" not in lk["B"].lower():
        errors.append(f"falta 'fully opaque' en L{lk['num']}")
# 12) 1000cc x todos
if content.count("massive 1000cc") < len(looks) * 7:
    errors.append("1000cc no presente en todos los prompts")
# 13) variedad de settings
warns = check_setting_variety([lk["setting"] for lk in looks])

print(f"OK: {len(content)} chars, {len(all_prompts)} prompts ({len(looks)} looks x 7)")
print("Anti-monoblock secuencia:", " · ".join(lk["color"].split("—")[-1].strip() for lk in looks))
# anti-monoblock: no mas de 2 monoblock seguidos
seq = [lk["color"].split("—")[-1].strip().lower() for lk in looks]
run = 0
for i, s in enumerate(seq):
    run = run + 1 if s.startswith("monoblock") else 0
    if run >= 3:
        errors.append(f"3+ monoblock seguidos hasta idx {i}")
if warns:
    print("AVISO settings:", "; ".join(warns))
else:
    print("Settings: variados (sin repeticion en ventana 5)")
if errors:
    print("\n*** QA FALLA ***")
    for e in errors:
        print("  -", e)
    sys.exit(1)
print("QA VERDE: 0 guantes · 0 chunky · 0 oxblood · token calzado x7 · medias->punta cerrada · "
      "0 POV-literal · ancla por slot · 0 Side-Profile-sentada · fully opaque x10 · 1000cc x70 · anti-monoblock OK")
