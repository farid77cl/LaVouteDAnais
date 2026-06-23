import sys
sys.stdout.reconfigure(encoding="utf-8")

A = ("stunning woman with (bimbofied facial features, oval face, high prominent cheekbones, "
     "large almond-shaped grey-green eyes, straight slim upturned nose, overlined glossy hot pink lips, "
     "small pointed chin:1.3), flawless white porcelain skin, hyper-polished smooth skin texture, "
     "dramatic siren liner, dramatic lash extensions, dark cherry red hair, artificial XXXL extensions "
     "hip-length, voluminous waves, center parted, slender hourglass silhouette, massive 1000cc breast "
     "implants each side, ultra high-profile, perfectly spherical augmented bust, obviously fake "
     "gravity-defying shape, wide hips, visible arm tattoos blackwork style, subtle minimalist blackwork "
     "tattoos on upper back and outer thighs, delicate blackwork rune-glyph identity tattoo of abstract "
     "esoteric calligraphic symbols along one hip crease and bikini line, navel piercing, nipple piercings "
     "pressing against and visible under clothing, aggressive bimbomakeup, extra long French XXXL nails "
     "with white tips and pink base 5cm.")

CLOSE = "Rim lighting to define silhouette, high-gloss specularity on vinyl surfaces."
NEG = ("red lips, dark lips, wine lips, maroon lips, crimson lips, different person, different face, "
       "different hair color, brown hair, black hair, blonde hair, flat shoes, block heel, wedge, "
       "platform mule, chunky heel, kitten heel, barefoot, socks, sneakers, two women, mirror reflection, "
       "split image, duplicate figure, side by side")
NEG_POV = "no phone, no smartphone, no device, no screen, no camera in hand"
FULL = "anatomically correct with exactly two arms, two hands each with five fingers, two legs and two feet,"
WAIST = "anatomically correct with two hands each with five fingers,"


def make_poses(B, calzado, setting, sp):
    Bf = B + ", and " + calzado + "."
    st = (f"{FULL} full body, one XXXL-nailed hand resting at the neckline and the other low on the hip, "
          f"the weight on one stiletto with a soft knee bend, the chin tilted and a self-aware sultry gaze "
          f"to the camera, lips parted glossy, an intimate self-aware posture, cherry red hair pushed to "
          f"one side, {setting}, {CLOSE}")
    bk = (f"{FULL} full body back view standing with both XXXL-nailed hands lifting all the cherry red "
          f"hair up off the nape, exposing the full back and spine line, the head dropped slightly forward, "
          f"the weight on one hip with the stiletto cocked, {setting}, {CLOSE}")
    se = (f"{FULL} perched on {sp} with one leg crossed over the other and the top stiletto pointed at "
          f"the camera, an extreme lumbar arch, one XXXL-nailed hand on the top knee and the other "
          f"fingertip at the bottom lip, the bust angled forward, shoulders rolled back, half-lidded "
          f"direct gaze, cherry red hair framing one breast, {setting}, {CLOSE}")
    si = (f"{FULL} side profile reclining on one side with an elegant S-curve, the hip rolled up and "
          f"the bust forward in silhouette, the legs stacked with the stilettos pointed, one XXXL-nailed "
          f"hand on the hip, half-lidded gaze, cherry red hair pooling, {setting}, {CLOSE}")
    di = (f"{WAIST} waist-up shot framed from the waist up, the torso turned and the augmented bust "
          f"presented, the chin dropped and the eyes lifted to the lens through the lashes, one XXXL "
          f"fingertip at the glossy bottom lip, the face the focus showing the detailed bimbo makeup, "
          f"a sensual half-lidded gaze, cherry red hair forward, the bodice detail crisp and legible, "
          f"{setting}, {CLOSE}")
    po = (f"{WAIST} first-person POV looking down over own body, chest + XXXL French nails in foreground, "
          f"full outfit converging to pointed stiletto tips, confident direct gaze into camera lens, face "
          f"centered and dominant in upper-mid frame, deep decollete visible in lower frame, lumbar arch "
          f"visible, body angled 30 degrees, cherry red hair cascading around face windblown, "
          f"{setting}, {CLOSE}")
    od = (f"{FULL} full body reclining back on both elbows with the legs draped and one stiletto pointed "
          f"at the camera, a deep elegant back arch with the bust lifted, looking to the camera through "
          f"the lashes, XXXL nails resting on the thigh, lips parted glossy, cherry red hair falling "
          f"around the face, {setting}, {CLOSE}")
    return [
        A + " " + Bf + " " + st,
        A + " " + Bf + " " + bk,
        A + " " + Bf + " " + se,
        A + " " + Bf + " " + si,
        A + " " + Bf + " " + di,
        A + " " + Bf + " " + po,
        A + " " + Bf + " " + od,
    ]


looks = [
    {
        "num": 651, "slug": "crimson_command", "nombre": "Crimson Command",
        "fecha": "22/06/2026", "batch": 'L651-L660 "Dominatrices"',
        "cat": "Stripper", "subcat": "Stripper Stage Dominatrix",
        "tags": "#stripper #stage #crimson #vinyl #ridingcrop #dominatrix #batchL651-L660 #V5poses",
        "concepto": ("Stripper Stage Dominatrix. Vestido bodycon de vinilo rojo cereza con tajo al muslo, "
                     "cinturon de cuero negro y riding crop."),
        "B": ("stunning woman wearing a Stripper Stage dominatrix look, a structured cherry-red high-gloss "
              "vinyl halter-neck bodycon dress with an extreme left-leg thigh-high slit revealing the full leg, "
              "a deep halter neckline tied at the nape, a fitted silhouette with a cinched waist, a black leather "
              "waist belt with a single silver square buckle, a black leather riding crop held loosely in one hand, "
              "fully opaque, no text, bare arms and bare hands"),
        "calzado": ("platform stiletto pumps in cherry-red patent vinyl, 6-inch thin pin stiletto heel + 2-inch "
                    "cherry-red patent platform, closed sharp pointed toe, ankle strap with a silver buckle, "
                    "chrome heel cap"),
        "setting": ("on a glamorous burlesque cabaret stage, red velvet curtains drawn back, a single white "
                    "follow-spot overhead, and a dark lacquered stage floor"),
        "sp": "a velvet crimson director's chair",
        "ambientacion": ("on a glamorous burlesque cabaret stage with red velvet curtains, a white follow-spot, "
                         "and dark lacquered floor"),
        "color": "crimson + negro + cromo — Contraste",
    },
    {
        "num": 652, "slug": "black_chrome_cage_mistress", "nombre": "Black Chrome Cage Mistress",
        "fecha": "22/06/2026", "batch": 'L651-L660 "Dominatrices"',
        "cat": "Stripper", "subcat": "Stripper Pole Mistress",
        "tags": "#stripper #pole #cage #rhinestone #chrome #harness #batchL651-L660 #V5poses",
        "concepto": ("Stripper Pole Mistress. Bra de jaula con rhinestones, thong micro y arnes corporal de "
                     "cuero y O-rings de cromo. Pleasers transparentes."),
        "B": ("stunning woman wearing a Stripper Pole dominatrix look, a rhinestone-encrusted cage bra with "
              "opaque dense-rhinestone bust cups, a structured underwire, an open chrome-metal cage frame between "
              "the cups exposing the sternum, thin rhinestone-dusted shoulder straps, a matching rhinestone "
              "micro-thong bikini sitting low on the hips exposing the full abdomen and bikini line, a full-body "
              "black leather and chrome O-ring cage harness crossing the torso and upper thighs, fully opaque at "
              "bust and groin, no text, bare arms and bare hands"),
        "calzado": ("clear transparent acrylic platform stiletto sandals, 8-inch thin pin stiletto heel + 4-inch "
                    "clear acrylic platform, open toe, clear ankle strap with a silver buckle, crystal-free clear sole"),
        "setting": ("in a high-end pole-dance studio with floor-to-ceiling backlit chrome mirrored walls, a "
                    "centered polished steel pole catching the light, and a dark veined marble floor"),
        "sp": "the chrome pole base platform",
        "ambientacion": ("en pole studio con paredes espejadas de cromo retroiluminadas y marmol oscuro veteado"),
        "color": "negro + rhinestone cromo + transparente — Contraste",
    },
    {
        "num": 653, "slug": "burgundy_fetish_domme", "nombre": "Burgundy Fetish Domme",
        "fecha": "22/06/2026", "batch": 'L651-L660 "Dominatrices"',
        "cat": "Lenceria", "subcat": "Lenceria Fetish Domme",
        "tags": "#lingerie #fetish #burgundy #leather #corset #seamed #collar #batchL651-L660 #V5poses",
        "concepto": ("Lenceria Fetish. Bra corset longline de cuero borgona con copa rigida, thong, "
                     "medias nude con costura y collar O-ring negro."),
        "B": ("stunning woman wearing a Lenceria Fetish dominatrix look, a deep-burgundy high-gloss leather "
              "longline underwire overbust bra with a rigid structured silhouette, a straight-across bandeau "
              "neckline, opaque leather cups, a wide waist-cinching band with four chrome suspender clips, a "
              "matching deep-burgundy high-cut thong with exposed hip bones and bikini line, sheer nude seamed "
              "stockings with a straight black back seam, a black latex O-ring collar at the throat, fully opaque "
              "at bust and groin, no text, bare arms and bare hands"),
        "calzado": ("single-sole pointed-toe stiletto pumps in burgundy patent vinyl, 14cm thin pin stiletto heel, "
                    "sharp pointed toe, slip-on, no strap, chrome heel cap"),
        "setting": ("in a candlelit stone-walled dungeon loft, exposed raw stone arches, dim red tungsten "
                    "uplighting, a wrought iron bedframe as backdrop, and a polished slate floor"),
        "sp": "a low polished stone bench",
        "ambientacion": ("en dungeon loft con arcos de piedra, luz roja tungsteno y suelo de pizarra pulida"),
        "color": "borgona — Monoblock",
    },
    {
        "num": 654, "slug": "noir_boudoir_sadist", "nombre": "Noir Boudoir Sadist",
        "fecha": "22/06/2026", "batch": 'L651-L660 "Dominatrices"',
        "cat": "Lenceria", "subcat": "Lenceria Boudoir Noir",
        "tags": "#lingerie #boudoir #black #ivory #vinyl #robe #bodynecklace #batchL651-L660 #V5poses",
        "concepto": ("Lenceria Boudoir Noir. Bata de saten marfil abierta sobre bralette triangular de vinilo "
                     "negro y micro-brief negro con O-ring lateral. Sin medias."),
        "B": ("stunning woman wearing a Lenceria Boudoir noir look, an ivory wet-look satin open floor-length "
              "robe with wide lapels, left open to reveal the look beneath, a black high-gloss vinyl underwire "
              "triangle bralette with thin ring-adjustable straps, a matching black high-gloss vinyl micro-brief "
              "with O-ring side hardware, no stockings, a delicate gold chain body necklace draping the sternum, "
              "fully opaque at bust and groin, no text, bare arms and bare hands"),
        "calzado": ("single-sole pointed-toe slingback stiletto pumps in black patent vinyl, 13cm thin pin "
                    "stiletto heel, sharp pointed toe, slingback strap with a gold buckle, gold heel cap"),
        "setting": ("in a dark silk-draped boudoir with heavy ebony floor-to-ceiling panels, a tufted black "
                    "leather chesterfield chaise longue, and warm amber candlelight from a single art-deco floor lamp"),
        "sp": "the chesterfield chaise longue armrest",
        "ambientacion": ("en boudoir de seda negra con paneles de ebano, chaise longue de cuero tufted y luz ambar art-deco"),
        "color": "negro + marfil + oro — Contraste",
    },
    {
        "num": 655, "slug": "ivory_power_viper", "nombre": "Ivory Power Viper",
        "fecha": "22/06/2026", "batch": 'L651-L660 "Dominatrices"',
        "cat": "Corporate", "subcat": "Corporate Office Domme",
        "tags": "#corporate #office #ivory #vinyl #blazer #pencilskirt #batchL651-L660 #V5poses",
        "concepto": ("Corporate Office Domme. Blazer doble botonadura en vinilo marfil con falda lapiz a juego. "
                     "Sin camisa bajo el blazer. Domme de sala de juntas."),
        "B": ("stunning woman wearing a Corporate Office Domme look, an ivory high-gloss vinyl double-breasted "
              "structured blazer with sharp architectural lapels, three large chrome buttons down the center, "
              "a nipped-in waist, and strong square shoulders, worn open with nothing beneath, a matching ivory "
              "high-gloss vinyl pencil skirt stopping just above the knee with a narrow center-back slit, a thin "
              "black leather waist belt with a chrome square buckle, fully opaque, no text, bare arms and bare hands"),
        "calzado": ("single-sole pointed-toe stiletto pumps in ivory patent vinyl, 13cm thin pin stiletto heel, "
                    "sharp pointed toe, slip-on, no strap, chrome heel cap"),
        "setting": ("in a glass-walled penthouse boardroom with floor-to-ceiling city skyline views in daylight, "
                    "a long chrome-and-glass conference table, white leather executive chairs, and a polished "
                    "white marble floor"),
        "sp": "the edge of the chrome conference table",
        "ambientacion": ("en sala de juntas penthouse con vistas al skyline de dia, mesa de cromo y suelo de marmol blanco"),
        "color": "marfil — Monoblock",
    },
    {
        "num": 656, "slug": "obsidian_crystal_predator", "nombre": "Obsidian Crystal Predator",
        "fecha": "22/06/2026", "batch": 'L651-L660 "Dominatrices"',
        "cat": "Nightclub", "subcat": "Nightclub Crystal Dominatrix",
        "tags": "#nightclub #crystal #rhinestone #strapless #mesh #thighboots #batchL651-L660 #V5poses",
        "concepto": ("Nightclub Crystal Dominatrix. Micro-vestido strapless de rhinestones con panel de "
                     "crystal-mesh y botas de plataforma muslo. Sin medias."),
        "B": ("stunning woman wearing a Nightclub dominatrix look, a strapless crystal-encrusted micro-dress, "
              "opaque dense-rhinestone bust cups with a straight bandeau neckline, a semi-sheer black "
              "crystal-mesh body panel running from under the bust down to the mid-thigh hem, a thong back, "
              "a single black leather garter strap on each outer thigh visible beneath the hemline, no stockings, "
              "fully opaque at bust and groin, no text, bare arms and bare hands"),
        "calzado": ("platform stiletto thigh-high boots in black patent vinyl, 6-inch thin pin stiletto heel + "
                    "2-inch black patent platform, closed sharp pointed toe, full inner zip, black sole"),
        "setting": ("in an exclusive nightclub VIP booth with black leather banquettes, ultraviolet neon strip "
                    "lighting along the floor, smoke machine haze, and a view through a glass partition to the "
                    "dancefloor below"),
        "sp": "the VIP leather banquette armrest",
        "ambientacion": ("en VIP nightclub con butacas de cuero negro, luz UV y haze de maquina de humo"),
        "color": "negro + rhinestone cristal — Contraste",
    },
    {
        "num": 657, "slug": "deep_scarlet_gala", "nombre": "Deep Scarlet Gala",
        "fecha": "22/06/2026", "batch": 'L651-L660 "Dominatrices"',
        "cat": "Escort", "subcat": "Escort Gala Femme Fatale",
        "tags": "#escort #gala #scarlet #satin #oneshoulder #slit #silverchain #batchL651-L660 #V5poses",
        "concepto": ("Escort Gala Femme Fatale. Vestido de gala de saten escarlata de un hombro con tajo extremo "
                     "al muslo y cadena plateada en la cintura. Sin medias."),
        "B": ("stunning woman wearing an Escort Gala femme fatale look, a deep-scarlet wet-satin one-shoulder "
              "asymmetric gown, a single wide draped strap over the right shoulder, a smooth fitted bodice "
              "hugging the torso, a floor-length column skirt with an extreme high thigh-slit on the left side "
              "exposing the entire leg, a thin silver chain draped once at the waist, no stockings, fully opaque, "
              "no text, bare arms and bare hands"),
        "calzado": ("single-sole pointed-toe slingback stiletto pumps in scarlet patent vinyl, 14cm thin pin "
                    "stiletto heel, sharp pointed toe, slingback strap with a silver buckle, silver heel cap"),
        "setting": ("at a grand hotel gala ballroom entrance, gilded crystal chandeliers overhead, white Carrara "
                    "marble floor, a red carpet runner, and candlelit gala tables visible in the background"),
        "sp": "a velvet ballroom chair",
        "ambientacion": ("en entrada de gala de hotel de lujo con aranas de cristal dorado, marmol blanco y alfombra roja"),
        "color": "escarlata + plata — Contraste",
    },
    {
        "num": 658, "slug": "chrome_armure_editorial", "nombre": "Chrome Armure Editorial",
        "fecha": "22/06/2026", "batch": 'L651-L660 "Dominatrices"',
        "cat": "HF Editorial", "subcat": "HF Avant-Garde Dominatrix",
        "tags": "#hfeditorial #avantgarde #chrome #latex #cuirass #harness #architectural #batchL651-L660 #V5poses",
        "concepto": ("HF Avant-Garde. Cuirass bodice de latex espejo cromado con micro-shorts a juego y correas "
                     "de arnes cruzadas en el esternon. Editorial arquitectonico maximo."),
        "B": ("stunning woman wearing a High-Fashion Editorial dominatrix look, a mirror-chrome high-gloss latex "
              "cuirass bodice shaped like an architectural breastplate, strapless with a rigid structured silhouette, "
              "opaque chrome-finish latex forming a raised horizontal ridge across the upper bust, matching "
              "mirror-chrome latex micro-shorts with a high waist, two black leather harness straps crossing the "
              "sternum diagonally meeting at a chrome O-ring center-chest, fully opaque, no text, bare arms and bare hands"),
        "calzado": ("single-sole pointed-toe stiletto pumps in mirror-chrome patent, 14cm thin pin stiletto heel, "
                    "sharp pointed toe, slip-on, no strap, polished chrome sole"),
        "setting": ("in a stark pure-white photo studio cove, a single wide-angle overhead key light, a seamless "
                    "white glossy reflective floor, and two chrome bounce-reflector panels flanking the subject"),
        "sp": "a low polished chrome cube plinth",
        "ambientacion": ("en cove de estudio fotografico blanco puro con suelo reflectante blanco y paneles chrome bounce"),
        "color": "cromo espejo — Monoblock",
    },
    {
        "num": 659, "slug": "black_widow_pinup", "nombre": "Black Widow Pin-Up",
        "fecha": "22/06/2026", "batch": 'L651-L660 "Dominatrices"',
        "cat": "Pin-Up", "subcat": "Pin-Up Film Noir Femme Fatale",
        "tags": "#pinup #filmnoir #femmefatale #black #vinyl #wrapped #seamed #batchL651-L660 #V5poses",
        "concepto": ("Pin-Up Film Noir. Vestido wrap de vinilo negro con V profundo, falda acampanada a media "
                     "muslo, fajin de saten y medias con costura. Viuda negra anos 40s."),
        "B": ("stunning woman wearing a Pin-Up Film Noir femme fatale look, a black high-gloss vinyl wrap-style "
              "mini dress with a wide overlap front, a deep V-neckline framing the decollete, short cap sleeves, "
              "a fitted waist, and a flared skirt hemming at mid-thigh, a black satin-gloss wide waist sash tied "
              "in a knot at the hip, a small gold vintage brooch at the V-neckline center, sheer black seamed "
              "nylon stockings with a straight black back seam, fully opaque, no text, bare arms and bare hands"),
        "calzado": ("single-sole pointed-toe stiletto pumps in black patent vinyl, 13cm thin pin stiletto heel, "
                    "sharp pointed toe, slip-on, no strap, red lacquered sole"),
        "setting": ("in a 1940s film-noir photo studio, a single dramatic low-key side spotlight, a dark velvet "
                    "chaise longue, a polished black lacquered floor, and deep shadow gradients on the walls"),
        "sp": "the dark velvet chaise longue",
        "ambientacion": ("en estudio film-noir de los 40s con luz lateral dramatica, chaise de terciopelo oscuro y suelo lacado negro"),
        "color": "negro + oro + rojo suela — Contraste",
    },
    {
        "num": 660, "slug": "chrome_triangle_bikini", "nombre": "Chrome Triangle Bikini",
        "fecha": "22/06/2026", "batch": 'L651-L660 "Dominatrices"',
        "cat": "Bikini", "subcat": "Bikini Studio Fetish Chrome",
        "tags": "#bikini #fetish #chrome #triangle #microstring #bodychains #batchL651-L660 #V5poses",
        "concepto": ("Bikini Studio Fetish Chrome. Micro-bikini triangular de vinilo cromado con cuerdas de hilo "
                     "y O-ring de cadena corporal plateada. Pleasers transparentes."),
        "B": ("stunning woman wearing a Bikini Studio Fetish look, a chrome-metallic vinyl triangle micro-bikini, "
              "a structured underwire push-up triangle top with thin adjustable string ties at the neck and back, "
              "a matching chrome-metallic vinyl high-leg thong with slim string sides sitting low on the hips "
              "exposing the full hip bones and bikini line, a silver chrome O-ring waist body-chain looping once "
              "at the waist, fully opaque, no text, bare arms and bare hands"),
        "calzado": ("clear transparent acrylic platform stiletto sandals, 8-inch thin pin stiletto heel + 4-inch "
                    "clear acrylic platform, open toe, clear ankle strap with a silver buckle, crystal-free clear sole"),
        "setting": ("in a futuristic all-chrome photography studio, a seamless polished metallic floor, industrial "
                    "ring lights overhead casting even cool white light, and chrome-panelled walls with mirror-finish surfaces"),
        "sp": "a low chrome reflective block",
        "ambientacion": ("en estudio fotografico todo-cromo futurista con suelo metalico y paredes espejo"),
        "color": "cromo + transparente — Contraste",
    },
]

POSE_NAMES = ["Standing", "Back View", "Seated", "Side Profile", "Ditzy", "Pov", "Odalisque"]

out_lines = []
for lk in looks:
    ps = make_poses(lk["B"], lk["calzado"], lk["setting"], lk["sp"])
    out_lines.append(f'\n## Look {lk["num"]}: {lk["nombre"]} ({lk["fecha"]} - batch {lk["batch"]} - {lk["cat"]} - {lk["subcat"]} - {lk["color"]} - platform)\n')
    out_lines.append(f'\n*{lk["concepto"]}* \U0001f525\U0001f460\n\n')
    out_lines.append(f'- **Ubicacion:** `05_Imagenes/ele/look{lk["num"]}_{lk["slug"]}/`\n')
    out_lines.append(f'- **Categoria:** {lk["cat"]}\n')
    out_lines.append(f'- **Subcategoria:** {lk["subcat"]}\n')
    out_lines.append(f'- **Tags:** {lk["tags"]}\n')
    out_lines.append(f'- **Concepto:** {lk["concepto"]}\n')
    out_lines.append(f'- **Outfit:** {lk["B"]}\n')
    out_lines.append('- **Calzado:** ver BLOQUE B (Token de Calzado Bloqueado, 8 atributos, identico x7).\n')
    out_lines.append(f'- **Ambientacion:** {lk["ambientacion"]}\n')
    out_lines.append('\n### \U0001f4f8 Imágenes (0/7 — Pendiente cuota API)\n\n')
    out_lines.append('| Standing | Back View | Seated | Side Profile | Ditzy (plano 3/4) | POV (single hand) | Odalisque |\n')
    out_lines.append('| :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n')
    out_lines.append('| ⏳ Pendiente | ⏳ Pendiente | ⏳ Pendiente | ⏳ Pendiente | ⏳ Pendiente | ⏳ Pendiente | ⏳ Pendiente |\n')
    out_lines.append('\n### \U0001f4dd Prompts V3.5 Hard-Sync\n\n')
    for i, (nm, pr) in enumerate(zip(POSE_NAMES, ps)):
        out_lines.append(f'**{i+1}. {nm}:**\n\n```\n{pr}\n```\n\n')
    out_lines.append(f'**Negative Prompt:** `{NEG}` · **Adicional POV:** `{NEG_POV}`\n\n---\n')

content = "".join(out_lines)
with open("_batch_L651_L660.md", "w", encoding="utf-8") as f:
    f.write(content)

# QA checks
assert content.count("glove") == 0, "FALLA: guantes detectados"
# "chunky" solo en negativos es OK; chequear que no esté en bloques de outfit
for lk in looks:
    b_lower = lk["B"].lower()
    assert "chunky" not in b_lower, f"FALLA: chunky en outfit L{lk['num']}"
import re
for lk in looks:
    count = content.count(lk["calzado"])
    assert count >= 7, f"FALLA: token calzado L{lk['num']} aparece {count} veces (minimo 7)"

print(f"OK: {len(content)} chars, {content.count(chr(10))} lineas")
print("QA: 0 guantes | 0 chunky | tokens calzado x7 TODOS OK")
