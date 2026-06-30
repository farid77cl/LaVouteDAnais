# -*- coding: utf-8 -*-
"""
Inyector batch L671-L680 "Barroco Fetish" (Ama 30/06/2026).
Tema fijo del batch: estetica BARROCA + pelo EN ALTO (updo) + CORSET estructural en cada
look + lente fetish (latex/vinyl/leather/rhinestone — nunca tela natural mate).

CORRECTO por diseno (a diferencia de _gen_batch_651.py, que era el bug):
 - IMPORTA rotate_poses de pose_rotation_v5 -> cada look rota su set de poses por nº de look
   (NO clona una sola plantilla en los 10 looks).
 - POV = retrato sensual de Instagram (las 8 variantes del modulo), NUNCA point-of-view literal.
 - Ancla de close-up sin imponer "two hands" (fix manos fantasma 30/06).
 - hair_up(): pasa el texto de pose a updo barroco (el pelo del ADN va EN ALTO este batch).
"""
import sys, os, re
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "visual"))
from pose_rotation_v5 import rotate_poses, check_setting_variety, HANDS_ANCHOR, FULL_ANCHOR

# BLOQUE A — ADN V3.5 Hard-Sync con PELO EN ALTO (updo barroco) para este batch.
# Color/largo/material del pelo del ADN se conservan (cherry red, XXXL, hip-length); SOLO el
# peinado va en alto. Incluye el tatuaje de runas (canon ADN, Ama 20/06).
A = ("stunning woman with (bimbofied facial features, oval face, high prominent cheekbones, "
     "large almond-shaped grey-green eyes, straight slim upturned nose, overlined glossy hot pink lips, "
     "small pointed chin:1.3), flawless white porcelain skin, hyper-polished smooth skin texture, "
     "dramatic siren liner, dramatic lash extensions, dark cherry red hair of artificial XXXL hip-length "
     "extensions styled UP into a voluminous sculptural baroque high updo with an ornate teased crown and "
     "a few loose face-framing tendrils, slender hourglass silhouette, massive 1000cc breast implants "
     "each side, ultra high-profile, perfectly spherical augmented bust, obviously fake gravity-defying "
     "shape, wide hips, visible arm tattoos blackwork style, subtle minimalist blackwork tattoos on upper "
     "back and outer thighs, delicate blackwork rune-glyph identity tattoo of abstract esoteric "
     "calligraphic symbols along one hip crease and bikini line, navel piercing, nipple piercings pressing "
     "against and visible under clothing, aggressive bimbomakeup, extra long French XXXL nails with white "
     "tips and pink base 5cm.")

CLOSE = "Rim lighting to define silhouette, high-gloss specularity on baroque surfaces."

# Negative base enriquecido (manos + POV-literal + duplicado), alineado con dna_v3_5.md.
NEG = ("red lips, dark lips, wine lips, maroon lips, crimson lips, different person, different face, "
       "different hair color, brown hair, black hair, blonde hair, auburn hair, hair down, loose flowing hair, "
       "flat shoes, block heel, wedge, platform mule, chunky heel, kitten heel, barefoot, socks, sneakers, "
       "different shoes, inconsistent footwear, different outfit, different body, gloves, opera gloves, "
       "long gloves, elbow gloves, fingerless gloves, covered hands, extra hands, third hand, extra arms, "
       "extra fingers, fused fingers, missing fingers, deformed hands, mutated hands, malformed fingers, "
       "two women, duplicate figure, split image, mirror reflection, first-person point of view, "
       "looking down over own body, overhead downward shot, fisheye, phone, smartphone, selfie stick")
NEG_POV = ("no phone, no smartphone, no device, no screen, no camera in hand, "
           "first-person point of view, looking down over own body, overhead downward shot")

UPDO_REPL = ("cherry red hair swept up into the baroque high updo with a few loose face-framing tendrils")

def hair_up(txt):
    """Lleva cualquier referencia de pelo de la pose al updo barroco (el ADN va en alto este batch)."""
    return re.sub(r"cherry red hair[^,]*", UPDO_REPL, txt)


looks = [
    {
        "num": 671, "slug": "oxblood_baroque_empress", "nombre": "Oxblood Baroque Empress",
        "cat": "Gala", "subcat": "Gala Baroque Empress",
        "tags": "#gala #baroque #oxblood #gold #latex #corset #updo #batchL671-L680 #V5poses",
        "concepto": "Gala barroca. Gown de latex oxblood con corset overbust de ballenas y brocado barroco en relieve, tajo al muslo y filigrana de oro antiguo. Pelo en alto.",
        "B": ("stunning woman wearing a baroque Gala empress look, a structured oxblood high-gloss latex "
              "floor-length gown with an integrated rigid steel-boned overbust corset bodice embossed with "
              "raised baroque brocade scrollwork, a sweetheart neckline edged in antique-gold baroque filigree "
              "trim, vertical boned seams cinching an extreme hourglass waist, a long column skirt with a deep "
              "front thigh-slit on the left, gold baroque appliqué cascading down the hip, fully opaque, "
              "no text, bare arms and bare hands"),
        "calzado": ("single-sole pointed-toe stiletto pumps in oxblood patent vinyl, 15cm thin pin stiletto "
                    "heel, sharp closed pointed toe, slip-on no strap, antique-gold heel cap"),
        "setting": ("on the grand gilded staircase of a baroque palace, carved marble balustrades, antique-gold "
                    "scrollwork on the walls, and a crystal chandelier overhead"),
        "seat": "a gilded baroque throne chair", "wall": "a carved gilded baroque column",
        "surface": "a polished marble balustrade rail",
        "ambientacion": "escalera de palacio barroco con balaustradas de marmol y arana de cristal",
        "color": "oxblood + oro antiguo — Contraste",
    },
    {
        "num": 672, "slug": "gold_filigree_boudoir", "nombre": "Gold Filigree Boudoir",
        "cat": "Lenceria", "subcat": "Lenceria Boudoir Baroque",
        "tags": "#lingerie #boudoir #baroque #gold #ivory #latex #corset #stockings #updo #batchL671-L680 #V5poses",
        "concepto": "Lenceria boudoir barroca. Corset longline de latex oro antiguo con filigrana barroca, thong, medias marfil y choker de encaje. Punta cerrada por las medias.",
        "B": ("stunning woman wearing a baroque Lingerie Boudoir look, a structured antique-gold high-gloss "
              "latex longline overbust corset with raised baroque filigree embossing and rigid steel-boned "
              "panels sculpting the waist, opaque molded cups with a straight baroque-trimmed neckline, six "
              "gold suspender clips at the hem, a matching antique-gold latex high-cut thong, sheer ivory "
              "stockings clipped to the suspenders, an ivory baroque-lace choker at the throat, fully opaque "
              "at bust and groin, no text, bare arms and bare hands"),
        "calzado": ("closed-toe platform stiletto pumps in antique-gold patent, 14cm thin pin stiletto heel "
                    "plus 3cm antique-gold platform, closed pointed toe, ankle strap with a gold buckle, "
                    "gold heel cap"),
        "setting": ("in an opulent baroque boudoir, damask silk wallpapered walls, a tufted ivory chaise "
                    "longue, gilded rococo mirror frames, and warm candlelight"),
        "seat": "a tufted ivory baroque chaise longue", "wall": "a damask silk baroque wall panel",
        "surface": "a gilded rococo console table",
        "ambientacion": "boudoir barroco con paredes de damasco y chaise longue marfil",
        "color": "oro antiguo + marfil — Contraste",
    },
    {
        "num": 673, "slug": "emerald_versailles_courtesan", "nombre": "Emerald Versailles Courtesan",
        "cat": "Escort", "subcat": "Escort Baroque Courtesan",
        "tags": "#escort #baroque #emerald #wetsatin #corset #slit #updo #batchL671-L680 #V5poses",
        "concepto": "Escort cortesana barroca. Gown wet-satin esmeralda con corset de ballenas, escote off-shoulder, bordado de oro y tajo extremo al muslo. Pelo en alto.",
        "B": ("stunning woman wearing a baroque Escort courtesan look, a deep-emerald wet-satin floor-length "
              "gown with a rigid steel-boned baroque corset bodice, an off-shoulder straight baroque neckline "
              "framing the décolleté with bare shoulders and bare arms, gold baroque embroidery scrolling "
              "across the corset bust and waist, boned seams cinching the waist, a long skirt with an extreme "
              "high thigh-slit on the right exposing the full leg, no stockings, fully opaque, no text, "
              "bare arms and bare hands"),
        "calzado": ("single-sole pointed-toe slingback stiletto pumps in emerald patent vinyl, 15cm thin pin "
                    "stiletto heel, sharp closed pointed toe, slingback strap with a gold buckle, gold heel cap"),
        "setting": ("in a candlelit baroque mirrored hall, gilded rococo panelling, ornate gold-framed mirrors, "
                    "a marble floor, and tall white candles in gold candelabra"),
        "seat": "a carved gilded baroque settee", "wall": "a gilded rococo mirror panel",
        "surface": "a marble pier table",
        "ambientacion": "salon barroco de espejos con panelado rococo dorado y candelabros",
        "color": "esmeralda — Monoblock",
    },
    {
        "num": 674, "slug": "royal_purple_baroque_vinyl", "nombre": "Royal Purple Baroque Vinyl",
        "cat": "Nightclub", "subcat": "Nightclub Baroque Vinyl",
        "tags": "#nightclub #baroque #royalpurple #gold #vinyl #corset #minidress #updo #batchL671-L680 #V5poses",
        "concepto": "Nightclub barroco. Mini-vestido corset de vinilo purpura real con damasco barroco en relieve y trenza de oro. Botas plataforma a juego. Pelo en alto.",
        "B": ("stunning woman wearing a baroque Nightclub look, a royal-purple high-gloss vinyl baroque corset "
              "mini-dress, a rigid steel-boned overbust corset bodice embossed with raised baroque damask "
              "scrollwork, a strapless straight neckline edged in gold baroque braid, a fitted mini skirt "
              "section hemming high on the thigh, gold baroque trim tracing the bodice seams, no stockings, "
              "fully opaque, no text, bare arms and bare hands"),
        "calzado": ("platform stiletto ankle boots in royal-purple patent vinyl, 6.5-inch thin pin stiletto "
                    "heel plus 2-inch royal-purple platform, closed pointed toe, inner zip, gold heel cap"),
        "setting": ("in an opulent baroque nightclub VIP lounge, a gilded coffered ceiling, deep-purple velvet "
                    "banquettes, golden uplighting, and a haze of smoke"),
        "seat": "a purple velvet baroque banquette", "wall": "a gilded baroque relief wall",
        "surface": "a black lacquered baroque side table",
        "ambientacion": "VIP de nightclub barroco con techo artesonado dorado y butacas de terciopelo",
        "color": "purpura real + oro — Contraste",
    },
    {
        "num": 675, "slug": "onyx_baroque_coatdress", "nombre": "Onyx Baroque Coat-Dress",
        "cat": "Corporate", "subcat": "Corporate Baroque Domme",
        "tags": "#corporate #baroque #black #leather #corset #coatdress #domme #updo #batchL671-L680 #V5poses",
        "concepto": "Corporate domme barroca. Coat-dress de cuero negro con corset overbust de brocado barroco, hombros arquitectonicos y doble botonadura de plata. Pelo en alto.",
        "B": ("stunning woman wearing a baroque Corporate Domme look, a structured black baroque-embossed "
              "high-gloss leather corset coat-dress, a rigid steel-boned overbust corset bodice with raised "
              "baroque brocade tooling, sharp architectural shoulders, a double-breasted front with two rows "
              "of antique-silver baroque buttons, a nipped waist, a knee-length pencil-cut skirt with a "
              "center-back slit, nothing beneath the corset neckline, a thin black leather waist belt with a "
              "baroque silver buckle, fully opaque, no text, bare arms and bare hands"),
        "calzado": ("single-sole pointed-toe stiletto pumps in black patent leather, 13cm thin pin stiletto "
                    "heel, sharp closed pointed toe, slip-on no strap, antique-silver heel cap"),
        "setting": ("in a baroque-panelled executive study, dark walnut wainscoting with gold baroque moulding, "
                    "a leather chesterfield, tall bookcases, and a brass desk lamp"),
        "seat": "a black leather chesterfield armchair", "wall": "a carved walnut baroque panel",
        "surface": "a mahogany executive desk edge",
        "ambientacion": "estudio ejecutivo barroco con boiserie de nogal y moldura dorada",
        "color": "negro — Monoblock",
    },
    {
        "num": 676, "slug": "ivory_baroque_cuirass", "nombre": "Ivory Baroque Cuirass",
        "cat": "HF Editorial", "subcat": "HF Baroque Sculptural",
        "tags": "#hfeditorial #baroque #ivory #latex #corset #cuirass #panniers #updo #batchL671-L680 #V5poses",
        "concepto": "HF editorial barroco. Cuirass corset de latex marfil moldeado como peto barroco con relieve de acanto + panniers escultoricos. Pelo en alto.",
        "B": ("stunning woman wearing a High-Fashion Editorial baroque look, an ivory high-gloss latex "
              "sculptural corset cuirass bodice molded like a baroque breastplate with raised acanthus-scroll "
              "relief, strapless with a rigid architectural silhouette and a steel-boned waist, paired with "
              "matching ivory high-gloss latex high-waist sculptural panniers flaring at the hips over an "
              "ivory latex micro-short, gold baroque piping outlining every panel, fully opaque, no text, "
              "bare arms and bare hands"),
        "calzado": ("single-sole pointed-toe stiletto pumps in ivory patent, 15cm thin pin stiletto heel, "
                    "sharp closed pointed toe, slip-on no strap, gold heel cap"),
        "setting": ("in a white baroque sculpture museum gallery, marble statues in gilded niches, a coffered "
                    "white-and-gold ceiling, and a polished marble floor"),
        "seat": "a white marble baroque plinth", "wall": "a gilded baroque niche frame",
        "surface": "a carved marble pedestal",
        "ambientacion": "galeria de escultura barroca blanca con nichos dorados y marmol pulido",
        "color": "marfil — Monoblock",
    },
    {
        "num": 677, "slug": "crimson_baroque_bombshell", "nombre": "Crimson Baroque Bombshell",
        "cat": "Pin-Up", "subcat": "Pin-Up Baroque Bombshell",
        "tags": "#pinup #baroque #crimson #black #gold #vinyl #corset #wiggle #seamed #updo #batchL671-L680 #V5poses",
        "concepto": "Pin-up bombshell barroca. Wiggle dress corset de vinilo carmesi con brocado barroco negro, fajin de saten y medias con costura. Punta cerrada por las medias. Pelo en alto.",
        "B": ("stunning woman wearing a baroque Pin-Up bombshell look, a crimson high-gloss vinyl baroque "
              "corset wiggle dress, a rigid boned overbust corset bodice with raised black baroque brocade "
              "scrollwork, a sweetheart neckline trimmed in gold baroque braid, a fitted wiggle skirt to "
              "mid-thigh, a black satin baroque waist sash knotted at the hip, sheer black seamed nylon "
              "stockings with a straight black back seam, fully opaque, no text, bare arms and bare hands"),
        "calzado": ("single-sole pointed-toe stiletto pumps in crimson patent vinyl, 13cm thin pin stiletto "
                    "heel, sharp closed pointed toe, slip-on no strap, gold heel cap"),
        "setting": ("in a baroque rococo salon, a powder-pink and gold panelled wall, an ornate gilded chaise, "
                    "a marble fireplace, and soft warm light"),
        "seat": "a gilded rococo chaise", "wall": "a pink-and-gold rococo wall panel",
        "surface": "a marble fireplace mantel",
        "ambientacion": "salon rococo barroco rosa y oro con chaise dorada y chimenea de marmol",
        "color": "carmesi + negro + oro — Triada",
    },
    {
        "num": 678, "slug": "sapphire_baroque_stage", "nombre": "Sapphire Baroque Stage",
        "cat": "Stripper", "subcat": "Stripper Pole Baroque",
        "tags": "#stripper #pole #baroque #sapphire #gold #rhinestone #corset #harness #clearpleaser #updo #batchL671-L680 #V5poses",
        "concepto": "Stripper pole barroca. Corset bra de rhinestones zafiro/oro en patron barroco + cincher de vinilo + micro-thong + arnes de cadena de oro. Pleasers transparentes. Pelo en alto.",
        "B": ("stunning woman wearing a baroque Stripper Pole look, a sapphire-blue rhinestone-encrusted "
              "baroque corset bra with rigid boned cups densely paved in sapphire and gold rhinestones in a "
              "baroque scroll pattern, a structured underbust corset waist cincher in sapphire high-gloss "
              "vinyl with gold baroque embossing, a matching sapphire rhinestone micro-thong sitting low on "
              "the hips, a gold chain baroque body harness draping the torso, no stockings, fully opaque at "
              "bust and groin, no text, bare arms and bare hands"),
        "calzado": ("clear transparent acrylic platform stiletto sandals, 8-inch thin pin stiletto heel plus "
                    "4-inch clear acrylic platform, open toe, clear ankle strap with a gold buckle, clear sole"),
        "setting": ("on a baroque cabaret pole stage, a gilded proscenium arch, deep-blue velvet drapes drawn "
                    "back, a polished steel pole catching golden light, and a dark lacquered stage floor"),
        "seat": "a sapphire velvet baroque stage stool", "wall": "a gilded proscenium pillar",
        "surface": "the polished baroque stage floor",
        "ambientacion": "escenario de cabaret barroco con proscenio dorado y caño de acero",
        "color": "zafiro + oro + cromo — Contraste",
    },
    {
        "num": 679, "slug": "bronze_baroque_bath", "nombre": "Bronze Baroque Bath",
        "cat": "Bikini", "subcat": "Bikini Baroque Fetish",
        "tags": "#bikini #baroque #bronze #gold #latex #corset #onepiece #clearpleaser #updo #batchL671-L680 #V5poses",
        "concepto": "Bikini barroco fetish. One-piece high-leg de latex bronce con corset underwire de ballenas y scrollwork barroco, body chain de oro. Pleasers transparentes. Pelo en alto.",
        "B": ("stunning woman wearing a baroque Bikini look, a bronze baroque-embossed high-gloss latex "
              "corset-style high-leg one-piece, a rigid boned underwire corset bodice with raised baroque "
              "scrollwork pressing the waist, a deep plunge neckline edged in gold baroque trim, high-cut "
              "legs exposing the full hip and bikini line, a gold baroque body chain looping once at the "
              "waist, no stockings, fully opaque at bust and groin, no text, bare arms and bare hands"),
        "calzado": ("clear transparent acrylic platform stiletto sandals, 7-inch thin pin stiletto heel plus "
                    "3-inch clear acrylic platform, open toe, clear ankle strap with a gold buckle, clear sole"),
        "setting": ("in a baroque marble bath orangerie, gilded arches, a sunken marble pool, potted palms, "
                    "and soft daylight through tall arched windows"),
        "seat": "a carved marble baroque bath ledge", "wall": "a gilded baroque arch column",
        "surface": "a marble pool edge",
        "ambientacion": "baño-orangerie barroco de marmol con arcos dorados y piscina hundida",
        "color": "bronce + oro — Monoblock",
    },
    {
        "num": 680, "slug": "wine_baroque_domme", "nombre": "Wine Baroque Domme",
        "cat": "Lenceria", "subcat": "Lenceria Fetish Baroque Domme",
        "tags": "#lingerie #fetish #baroque #wine #leather #corset #seamed #collar #domme #updo #batchL671-L680 #V5poses",
        "concepto": "Lenceria fetish domme barroca. Underbust corset de cuero vino con brocado barroco, longline bra, thong, medias con costura y collar O-ring. Punta cerrada por las medias. Pelo en alto.",
        "B": ("stunning woman wearing a baroque Lingerie Fetish Domme look, a deep-wine high-gloss leather "
              "baroque underbust corset with rigid steel-boned panels and raised black baroque brocade "
              "tooling sculpting the waist, six black suspender clips at the hem, opaque molded cups above on "
              "a deep-wine leather longline bra with a straight baroque-trimmed neckline, a matching deep-wine "
              "leather high-cut thong, sheer black seamed stockings clipped to the suspenders, a black latex "
              "O-ring collar at the throat, fully opaque at bust and groin, no text, bare arms and bare hands"),
        "calzado": ("single-sole pointed-toe stiletto pumps in deep-wine patent leather, 14cm thin pin "
                    "stiletto heel, sharp closed pointed toe, slip-on no strap, antique-gold heel cap"),
        "setting": ("in a candlelit baroque chamber, deep-wine damask walls, a carved ebony four-poster bed, "
                    "gold baroque candelabra, and a flickering amber glow"),
        "seat": "a wine velvet baroque fainting couch", "wall": "a wine damask baroque wall",
        "surface": "a carved ebony baroque chest",
        "ambientacion": "camara barroca a la luz de las velas con damasco vino y cama de ebano",
        "color": "vino — Monoblock",
    },
]

POSE_NAMES = ["Standing", "Back View", "Seated", "Side Profile", "Ditzy", "POV", "Odalisque"]
FECHA = "30/06/2026"
BATCH = 'L671-L680 "Barroco Fetish"'

def build_prompts(lk):
    Bf = lk["B"] + ", and " + lk["calzado"] + "."
    poses = rotate_poses(lk["num"], seat=lk["seat"], wall=lk["wall"], surface=lk["surface"])
    prompts = []
    for slot, txt in poses:
        ptxt = hair_up(txt)
        full = f"{A} {Bf} {ptxt}, {lk['setting']}, {CLOSE}"
        prompts.append((slot, full))
    return prompts

out = []
all_prompts = []
for lk in looks:
    ps = build_prompts(lk)
    all_prompts.extend([(lk["num"], s, p) for s, p in ps])
    out.append(f'\n## Look {lk["num"]}: {lk["nombre"]} ({FECHA} · batch {BATCH} · {lk["cat"]} · {lk["subcat"]} · {lk["color"]})\n')
    out.append(f'\n*{lk["concepto"]}* \U0001f525\U0001f460\n\n')
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
    out.append('\n### \U0001f4dd Prompts V3.5 Hard-Sync (poses rotadas con pose_rotation_v5)\n\n')
    for i, (nm, pr) in enumerate(ps):
        out.append(f'**{i+1}. {nm}:**\n\n```\n{pr}\n```\n\n')
    out.append(f'**Negative Prompt:** `{NEG}`\n\n**Adicional POV:** `{NEG_POV}`\n\n---\n')

content = ("# Batch L671-L680 — \"Barroco Fetish\" (30/06/2026)\n\n"
           "Tema: estetica barroca + pelo EN ALTO (updo) + CORSET en cada look + lente fetish.\n"
           "Motor: poses rotadas con `pose_rotation_v5` (POV = retrato IG, ancla close-up sin 'two hands').\n\n"
           + "".join(out))
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "_batch_L671_L680.md"),
          "w", encoding="utf-8") as f:
    f.write(content)

# ===================== QA =====================
errors = []
# 1) Guantes — solo en el POSITIVE (el negative SI los lleva a proposito)
for num, slot, pr in all_prompts:
    if "glove" in pr.lower():
        errors.append(f"guantes en el positive L{num} {slot}")
# 2) chunky en outfit (positive)
for lk in looks:
    if "chunky" in lk["B"].lower() or "chunky" in lk["calzado"].lower():
        errors.append(f"chunky en outfit/calzado L{lk['num']}")
# 3) corset presente en cada B
for lk in looks:
    if "corset" not in lk["B"].lower():
        errors.append(f"falta corset en L{lk['num']}")
# 4) token calzado x7
for lk in looks:
    c = content.count(lk["calzado"])
    if c < 7:
        errors.append(f"token calzado L{lk['num']} aparece {c} veces (<7)")
# 5) anti-POV-literal en los PROMPTS
POV_BAD = ["first-person", "point of view", "looking down over", "converging to", "stiletto tips", "selfie"]
for num, slot, pr in all_prompts:
    for b in POV_BAD:
        if b in pr.lower():
            errors.append(f"POV-literal '{b}' en L{num} {slot}")
# 6) ancla correcta por slot
for num, slot, pr in all_prompts:
    if slot in ("Ditzy", "POV"):
        if HANDS_ANCHOR not in pr:
            errors.append(f"falta ancla close-up en L{num} {slot}")
        if FULL_ANCHOR in pr:
            errors.append(f"ancla FULL indebida en close-up L{num} {slot}")
    else:
        if FULL_ANCHOR not in pr:
            errors.append(f"falta ancla FULL en L{num} {slot}")
# 7) pelo en alto (no debe quedar 'hair down' ni mechas sueltas sin updo en los prompts)
for num, slot, pr in all_prompts:
    if "voluminous waves, center parted" in pr:
        errors.append(f"pelo suelto (waves center parted) en L{num} {slot}")
# 8) 1000cc x todos
if content.count("massive 1000cc") < len(looks) * 7:
    errors.append("1000cc no presente en todos los prompts")
# 9) variedad de settings
warns = check_setting_variety([lk["setting"] for lk in looks])

print(f"OK: {len(content)} chars, {len(all_prompts)} prompts ({len(looks)} looks x 7)")
print("Anti-monoblock secuencia:", " · ".join(lk["color"].split("—")[-1].strip() for lk in looks))
if warns:
    print("AVISO settings:", "; ".join(warns))
else:
    print("Settings: variados (sin repeticion en ventana 5)")
if errors:
    print("\n*** QA FALLA ***")
    for e in errors:
        print("  -", e)
    sys.exit(1)
print("QA: 0 guantes · 0 chunky · corset x10 · token calzado x7 · 0 POV-literal · ancla por slot OK · pelo en alto · 1000cc x70")
