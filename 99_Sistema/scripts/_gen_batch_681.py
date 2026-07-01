# -*- coding: utf-8 -*-
"""
Inyector batch L681-L690 "Vampiresa Bimbo Sensual" (Ama 01/07/2026).
Tema del batch: VAMPIRESA glamorosa NO-GOTICA + bimbo sensual + lente fetish.
 - Restriccion anti-gotico LEVANTADA por orden expresa de la Ama SOLO para leer "vampiresa"
   como depredadora inmortal glamorosa (NO Helena gotica: nada de encaje victoriano, macabro,
   maquillaje de cuervo, cementerio).
 - CERO oxblood (la Ama saturada del color) -> variedad cromatica total (violeta/esmeralda/
   zafiro/magenta/marfil/obsidiana/cobalto/chrome-cristal/aquamarina/ciruela).
 - Cherry red SOLO pelo/labios (ADN). Colmillos glamour sutiles + mirada hipnotica en BLOQUE A.
 - Pelo SUELTO en cascada (default ADN) -> NO usa hair_up().

CORRECTO por diseno (mismo motor probado en _gen_batch_671):
 - IMPORTA rotate_poses de pose_rotation_v5 -> rota poses por nº de look (no clona plantilla).
 - Side Profile REPARADO (01/07): las 7 variantes son de pie, ninguna sentada.
 - POV = retrato IG. Ancla close-up sin imponer "two hands".
"""
import sys, os
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "visual"))
from pose_rotation_v5 import rotate_poses, check_setting_variety, HANDS_ANCHOR, FULL_ANCHOR

# BLOQUE A — ADN V3.5 Hard-Sync. Pelo SUELTO en cascada + colmillos glamour + mirada hipnotica
# (lectura vampiresa NO-gotica). Tokens ADN bloqueados intactos (ojos gris-verde, cherry XXXL
# hip-length, 1000cc, piel porcelana, uñas, tatuaje runas, piercings).
A = ("stunning woman with (bimbofied facial features, oval face, high prominent cheekbones, "
     "large almond-shaped grey-green eyes, straight slim upturned nose, overlined glossy hot pink lips "
     "slightly parted to reveal the delicate points of two small elegant vampire fangs, small pointed "
     "chin:1.3), a hypnotic half-lidded predatory gaze, flawless white porcelain skin, hyper-polished "
     "smooth skin texture, dramatic siren liner, dramatic lash extensions, dark cherry red hair of "
     "artificial XXXL hip-length extensions in voluminous center-parted waves cascading down, slender "
     "hourglass silhouette, massive 1000cc breast implants each side, ultra high-profile, perfectly "
     "spherical augmented bust, obviously fake gravity-defying shape, wide hips, visible arm tattoos "
     "blackwork style, subtle minimalist blackwork tattoos on upper back and outer thighs, delicate "
     "blackwork rune-glyph identity tattoo of abstract esoteric calligraphic symbols along one hip crease "
     "and bikini line, navel piercing, nipple piercings pressing against and visible under clothing, "
     "aggressive bimbomakeup, extra long French XXXL nails with white tips and pink base 5cm.")

CLOSE = ("Moonlit rim lighting to define silhouette, high-gloss specularity on latex and vinyl surfaces, "
         "a nocturnal luxe atmosphere.")

NEG = ("red lips, dark lips, wine lips, maroon lips, crimson lips, oxblood, gothic, victorian lace, "
       "cobweb, cemetery, macabre, corpse makeup, different person, different face, different hair color, "
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
        "num": 681, "slug": "amethyst_moonlit_countess", "nombre": "Amethyst Moonlit Countess",
        "cat": "Gala", "subcat": "Gala Vampiress",
        "tags": "#gala #vampiress #amethyst #violet #liquidlame #wetlook #slit #batchL681-L690 #V5poses",
        "concepto": "Gala vampiresa. Column gown de liquid lamé amatista wet-look, halter con plunge al ombligo, cuello alto y tajo al muslo. Depredadora glamorosa a la luz de la luna.",
        "B": ("stunning woman wearing a Gala vampiress look, an amethyst-violet liquid-lamé wet-look "
              "floor-length column gown, a deep plunging halter neckline running to the navel with a "
              "high standing collar at the throat, a molded boned bodice cinching an extreme hourglass "
              "waist, an open back, a long column skirt with a deep front thigh-slit on the left, no "
              "stockings, fully opaque at bust and groin, no text, bare arms and bare hands"),
        "calzado": ("single-sole pointed-toe stiletto pumps in amethyst-violet patent vinyl, 15cm thin pin "
                    "stiletto heel, sharp closed pointed toe, slip-on no strap, silver heel cap"),
        "setting": ("on the moonlit rooftop terrace of a glass penthouse at midnight, city lights glittering "
                    "below, a full silver moon, and sleek black marble planters"),
        "seat": "a sleek black marble terrace bench", "wall": "a floor-to-ceiling glass penthouse panel",
        "surface": "a polished black marble parapet",
        "ambientacion": "terraza-rooftop de penthouse de vidrio a medianoche con luna llena",
        "color": "amatista violeta — Monoblock",
    },
    {
        "num": 682, "slug": "emerald_venom_boudoir", "nombre": "Emerald Venom Boudoir",
        "cat": "Lenceria", "subcat": "Lenceria Vampiress Boudoir",
        "tags": "#lingerie #boudoir #vampiress #emerald #latex #stockings #choker #batchL681-L690 #V5poses",
        "concepto": "Lencería vampiresa. Longline bra de latex esmeralda con thong, medias humo-esmeralda y choker con colgante de gota. Punta cerrada por las medias.",
        "B": ("stunning woman wearing a Lingerie Boudoir vampiress look, an emerald high-gloss latex "
              "longline balconette bra with opaque molded cups and a straight neckline, six emerald "
              "suspender clips at the hem sculpting the waist, a matching emerald high-gloss latex "
              "high-cut thong, sheer smoke-emerald stockings clipped to the suspenders, a black latex "
              "choker with a single teardrop emerald pendant at the throat, fully opaque at bust and "
              "groin, no text, bare arms and bare hands"),
        "calzado": ("closed-toe platform stiletto pumps in emerald patent vinyl, 14cm thin pin stiletto "
                    "heel plus 3cm emerald platform, closed pointed toe, ankle strap with a silver buckle, "
                    "emerald platform matching the shoe"),
        "setting": ("in an emerald-velvet boudoir at night, dark green damask walls, a candlelit vanity "
                    "with a gilded frame, and a deep-green tufted chaise longue"),
        "seat": "a deep-green tufted chaise longue", "wall": "a dark green damask wall panel",
        "surface": "a candlelit gilded vanity table",
        "ambientacion": "boudoir de terciopelo esmeralda de noche con paredes de damasco verde",
        "color": "esmeralda — Monoblock",
    },
    {
        "num": 683, "slug": "sapphire_frost_seductress", "nombre": "Sapphire Frost Seductress",
        "cat": "Escort", "subcat": "Escort Vampiress",
        "tags": "#escort #vampiress #sapphire #silver #wetsatin #chainmail #slit #batchL681-L690 #V5poses",
        "concepto": "Escort vampiresa. Gown wet-satin zafiro one-shoulder con cascada de cota de malla de plata sobre el busto y tajo extremo. Seductora de hielo.",
        "B": ("stunning woman wearing an Escort vampiress look, a deep-sapphire wet-satin floor-length "
              "gown with an asymmetric one-shoulder neckline, a fine silver chainmail drape cascading "
              "from the single shoulder across the décolleté, a boned bodice cinching the waist, a long "
              "skirt with an extreme high thigh-slit on the right exposing the full leg, no stockings, "
              "fully opaque at bust and groin, no text, bare arms and bare hands"),
        "calzado": ("single-sole pointed-toe slingback stiletto pumps in sapphire patent vinyl, 15cm thin "
                    "pin stiletto heel, sharp closed pointed toe, slingback strap with a silver buckle, "
                    "silver heel cap"),
        "setting": ("in a private opera box at night, sleek silver-and-glass balustrades, deep-blue velvet "
                    "seats, and cool stage light rising from the auditorium below"),
        "seat": "a deep-blue velvet opera seat", "wall": "a brushed-silver opera balustrade",
        "surface": "a glass opera-box ledge",
        "ambientacion": "palco de ópera moderno de noche con balaustrada de plata y vidrio",
        "color": "zafiro + plata — Contraste",
    },
    {
        "num": 684, "slug": "magenta_hypnosis_club", "nombre": "Magenta Hypnosis",
        "cat": "Nightclub", "subcat": "Nightclub Vampiress",
        "tags": "#nightclub #vampiress #magenta #black #vinyl #harness #minidress #batchL681-L690 #V5poses",
        "concepto": "Nightclub vampiresa. Mini bodycon de vinilo magenta eléctrico con dos aberturas en cintura y keyhole bajo la clavícula (opaco en busto/pubis) + arnés O-ring negro. Hipnosis en la pista.",
        "B": ("stunning woman wearing a Nightclub vampiress look, an electric-magenta high-gloss vinyl "
              "mini bodycon dress with two symmetric teardrop cutouts at the waist sides and a single "
              "keyhole opening just below the collarbone, all cutouts edged in black piping, the bust "
              "panel and groin fully opaque, a black vinyl O-ring harness framing the neckline, a fitted "
              "mini skirt hemming high on the thigh, no stockings, fully opaque at bust and groin, no "
              "text, bare arms and bare hands"),
        "calzado": ("platform stiletto ankle boots in electric-magenta patent vinyl, 6.5-inch thin pin "
                    "stiletto heel plus 2-inch magenta platform, closed pointed toe, inner zip, "
                    "magenta platform matching the boot, black heel cap"),
        "setting": ("in a neon-magenta nightclub VIP lounge, black lacquered walls, a haze of pink laser "
                    "light, and a glowing acrylic bar"),
        "seat": "a black lacquered VIP banquette", "wall": "a black lacquered club wall",
        "surface": "a glowing acrylic bar top",
        "ambientacion": "VIP de nightclub en neón magenta con paredes de laca negra y láser rosado",
        "color": "magenta eléctrico + negro — Contraste",
    },
    {
        "num": 685, "slug": "pale_immortal_executive", "nombre": "Pale Immortal Executive",
        "cat": "Corporate", "subcat": "Corporate Vampiress Domme",
        "tags": "#corporate #vampiress #ivory #pearl #gunmetal #leather #coatdress #domme #batchL681-L690 #V5poses",
        "concepto": "Corporate vampiresa. Coat-dress de cuero marfil-perla con hombros arquitectónicos, solapa en plunge (nada debajo), cinturón gunmetal y tajo central. Inmortal pálida de directorio.",
        "B": ("stunning woman wearing a Corporate Domme vampiress look, a pearl-ivory high-gloss leather "
              "belted coat-dress, sharp architectural shoulders, a deep plunging lapel neckline with "
              "nothing beneath, a nipped waist cinched by a gunmetal buckle belt, a knee-length pencil "
              "skirt with a center front slit, gunmetal hardware throughout, fully opaque at bust and "
              "groin, no text, bare arms and bare hands"),
        "calzado": ("single-sole pointed-toe stiletto pumps in pearl-ivory patent leather, 13cm thin pin "
                    "stiletto heel, sharp closed pointed toe, slip-on no strap, gunmetal heel cap"),
        "setting": ("in a glass corner office at night, floor-to-ceiling windows over a lit skyline, a "
                    "pale marble desk, and cool minimalist lighting"),
        "seat": "a white leather executive chair", "wall": "a floor-to-ceiling office glass wall",
        "surface": "a pale marble desk edge",
        "ambientacion": "oficina de esquina de vidrio de noche con skyline y escritorio de mármol",
        "color": "marfil perla + gunmetal — Contraste",
    },
    {
        "num": 686, "slug": "obsidian_sculptural_nocturne", "nombre": "Obsidian Sculptural Nocturne",
        "cat": "HF Editorial", "subcat": "HF Vampiress Sculptural",
        "tags": "#hfeditorial #vampiress #black #obsidian #latex #bodysuit #panniers #batchL681-L690 #V5poses",
        "concepto": "HF editorial vampiresa. Bodysuit escultórico de latex negro obsidiana con hombros alados arquitectónicos + panniers de cadera sobre brief alto. Nocturno escultórico.",
        "B": ("stunning woman wearing a High-Fashion Editorial vampiress look, an obsidian-black high-gloss "
              "latex sculptural bodysuit, a rigid architectural molded high-neck bodice with sharp winged "
              "shoulders, a steel-boned waist, sculptural black high-gloss latex hip panniers flaring over "
              "a high-cut latex brief, a mirror-gloss finish throughout, fully opaque at bust and groin, "
              "no text, bare arms and bare hands"),
        "calzado": ("single-sole pointed-toe stiletto pumps in obsidian-black patent, 15cm thin pin "
                    "stiletto heel, sharp closed pointed toe, slip-on no strap, black heel cap"),
        "setting": ("in a black marble sculpture gallery at night, spotlit obsidian statues in niches, a "
                    "coffered dark ceiling, and a polished black stone floor"),
        "seat": "a black marble gallery plinth", "wall": "a black stone niche frame",
        "surface": "a polished obsidian pedestal",
        "ambientacion": "galería de escultura de mármol negro de noche con estatuas de obsidiana",
        "color": "obsidiana negro — Monoblock",
    },
    {
        "num": 687, "slug": "cobalt_midnight_bombshell", "nombre": "Cobalt Midnight Bombshell",
        "cat": "Pin-Up", "subcat": "Pin-Up Vampiress Bombshell",
        "tags": "#pinup #vampiress #cobalt #black #vinyl #wiggle #seamed #halter #batchL681-L690 #V5poses",
        "concepto": "Pin-up vampiresa. Wiggle dress halter de vinilo cobalto con moño de satén y medias con costura negra. Bombshell de medianoche. Punta cerrada por las medias.",
        "B": ("stunning woman wearing a Pin-Up bombshell vampiress look, a cobalt-blue high-gloss vinyl "
              "halter wiggle dress, a sweetheart bust with a halter tie at the neck, a nipped waist, a "
              "fitted wiggle skirt to mid-thigh, a black satin bow at the hip, sheer black seamed nylon "
              "stockings with a straight black back seam, fully opaque at bust and groin, no text, bare "
              "arms and bare hands"),
        "calzado": ("single-sole pointed-toe stiletto pumps in cobalt-blue patent vinyl, 13cm thin pin "
                    "stiletto heel, sharp closed pointed toe, slip-on no strap, black heel cap"),
        "setting": ("in a midnight cocktail lounge, cobalt velvet booths, a polished chrome bar, and warm "
                    "low amber light"),
        "seat": "a cobalt velvet cocktail booth", "wall": "a dark panelled lounge wall",
        "surface": "a polished chrome bar counter",
        "ambientacion": "lounge de cócteles de medianoche con booths de terciopelo cobalto y barra de cromo",
        "color": "cobalto + negro — Contraste",
    },
    {
        "num": 688, "slug": "crystal_chrome_vampire_stage", "nombre": "Crystal Chrome Vampire Stage",
        "cat": "Stripper", "subcat": "Stripper Pole Vampiress",
        "tags": "#stripper #pole #vampiress #chromegold #crystal #rhinestone #harness #clearpleaser #batchL681-L690 #V5poses",
        "concepto": "Stripper pole vampiresa. Corset-bra de rhinestones cristal/oro-cromo + cincher de vinilo + micro-thong + arnés de cadena de cristal. Pleasers transparentes.",
        "B": ("stunning woman wearing a Stripper Pole vampiress look, a chrome-gold and crystal "
              "rhinestone-encrusted corset bra with rigid boned cups densely paved in clear crystal and "
              "gold rhinestones, a structured underbust waist cincher in chrome-gold high-gloss vinyl, a "
              "matching clear-crystal rhinestone micro-thong sitting low on the hips, a fine silver "
              "crystal chain body harness draping the torso, no stockings, fully opaque at bust and "
              "groin, no text, bare arms and bare hands"),
        "calzado": ("clear transparent acrylic platform stiletto sandals, 8-inch thin pin stiletto heel "
                    "plus 4-inch clear acrylic platform, open toe, clear ankle strap with a silver buckle, "
                    "clear sole"),
        "setting": ("on a chrome-and-glass pole stage at night, a polished steel pole catching cool blue "
                    "spotlight, dark reflective flooring, and a backlit glass wall"),
        "seat": "a chrome pole-stage stool", "wall": "a backlit frosted-glass stage wall",
        "surface": "the polished dark stage floor",
        "ambientacion": "escenario de caño de cromo y vidrio de noche con foco azul frío",
        "color": "chrome gold + cristal — Contraste",
    },
    {
        "num": 689, "slug": "aquamarine_ice_nymph", "nombre": "Aquamarine Ice Nymph",
        "cat": "Bikini", "subcat": "Bikini Vampiress Fetish",
        "tags": "#bikini #vampiress #aquamarine #teal #latex #onepiece #bodychain #clearpleaser #batchL681-L690 #V5poses",
        "concepto": "Bikini vampiresa fetish. One-piece high-leg de latex aquamarina con plunge halter y body chain de plata. Ninfa de hielo a la luz de la luna. Pleasers transparentes.",
        "B": ("stunning woman wearing a Bikini vampiress look, an icy aquamarine high-gloss latex high-leg "
              "one-piece, a deep plunging halter neckline, high-cut legs exposing the full hip and bikini "
              "line, a fine silver body chain looping once at the waist, no stockings, fully opaque at "
              "bust and groin, no text, bare arms and bare hands"),
        "calzado": ("clear transparent acrylic platform stiletto sandals, 7-inch thin pin stiletto heel "
                    "plus 3-inch clear acrylic platform, open toe, clear ankle strap with a silver buckle, "
                    "clear sole"),
        "setting": ("beside a moonlit infinity pool on a glass terrace at night, aqua-lit water rippling, "
                    "sleek loungers, and tall dark palms"),
        "seat": "a sleek white poolside lounger", "wall": "a frosted-glass terrace balustrade",
        "surface": "the aqua-lit marble pool edge",
        "ambientacion": "piscina infinita a la luz de la luna en terraza de vidrio con agua turquesa",
        "color": "aquamarina — Monoblock",
    },
    {
        "num": 690, "slug": "plum_sovereign_domme", "nombre": "Plum Sovereign",
        "cat": "Lenceria", "subcat": "Lenceria Fetish Vampiress Domme",
        "tags": "#lingerie #fetish #vampiress #plum #black #leather #corset #seamed #collar #domme #batchL681-L690 #V5poses",
        "concepto": "Lencería fetish domme vampiresa. Underbust corset de cuero ciruela con longline bra, thong, medias con costura y collar O-ring. Soberana inmortal. Punta cerrada por las medias.",
        "B": ("stunning woman wearing a Lingerie Fetish Domme vampiress look, a deep-plum high-gloss "
              "leather underbust corset with rigid steel-boned panels sculpting the waist, an opaque "
              "molded deep-plum leather longline bra above with a straight neckline, six black suspender "
              "clips at the hem, a matching deep-plum leather high-cut thong, sheer black seamed stockings "
              "clipped to the suspenders, a black latex O-ring collar at the throat, fully opaque at bust "
              "and groin, no text, bare arms and bare hands"),
        "calzado": ("closed-toe single-sole pointed-toe stiletto pumps in deep-plum patent leather, 14cm "
                    "thin pin stiletto heel, sharp closed pointed toe, slip-on no strap, black heel cap"),
        "setting": ("in an opulent plum-velvet chamber at night, deep-purple upholstered walls, a carved "
                    "dark-wood four-poster, and a warm amber glow from wall sconces"),
        "seat": "a plum velvet fainting couch", "wall": "a deep-purple upholstered wall panel",
        "surface": "a carved dark-wood chest",
        "ambientacion": "cámara opulenta de terciopelo ciruela de noche con cama de dosel",
        "color": "ciruela + negro — Contraste",
    },
]

POSE_NAMES = ["Standing", "Back View", "Seated", "Side Profile", "Ditzy", "POV", "Odalisque"]
FECHA = "01/07/2026"
BATCH = 'L681-L690 "Vampiresa Bimbo Sensual"'

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

content = ("# Batch L681-L690 — \"Vampiresa Bimbo Sensual\" (01/07/2026)\n\n"
           "Tema: vampiresa glamorosa NO-gotica + bimbo sensual + lente fetish. Colmillos glamour "
           "sutiles + mirada hipnotica en Bloque A. CERO oxblood. Colores variados (anti-monoblock).\n"
           "Motor: poses rotadas con `pose_rotation_v5` (Side Profile reparado 01/07 = 0 sentadas; "
           "POV = retrato IG; ancla close-up sin 'two hands').\n\n"
           + "".join(out))
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "_batch_L681_L690.md"),
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
        errors.append(f"chunky en outfit/calzado L{lk['num']}")
# 3) CERO oxblood en el positive (directiva Ama 01/07 — saturada)
for lk in looks:
    if "oxblood" in (lk["B"] + lk["calzado"] + lk["concepto"]).lower():
        errors.append(f"OXBLOOD prohibido en L{lk['num']}")
# 4) colmillos vampiresa presentes en todos los prompts (tema del batch)
if content.count("vampire fangs") < len(looks) * 7:
    errors.append("colmillos vampiresa no presentes en todos los prompts")
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
print("QA VERDE: 0 guantes · 0 chunky · 0 oxblood · colmillos x70 · token calzado x7 · medias->punta cerrada · "
      "0 POV-literal · ancla por slot · 0 Side-Profile-sentada · fully opaque x10 · 1000cc x70 · anti-monoblock OK")
