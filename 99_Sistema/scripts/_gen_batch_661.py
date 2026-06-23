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

CLOSE = "Rim lighting to define silhouette, high-gloss specularity on patent and latex surfaces."
NEG = ("red lips, dark lips, wine lips, maroon lips, crimson lips, different person, different face, "
       "different hair color, brown hair, black hair, blonde hair, open toe, open-toe sandal, flat shoes, "
       "block heel, wedge, chunky heel, kitten heel, barefoot, sneakers, clear platform, transparent heel, "
       "two women, mirror reflection, split image, duplicate figure, side by side")
NEG_POV = "no phone, no smartphone, no device, no screen, no camera in hand"
FULL = "anatomically correct with exactly two arms, two hands each with five fingers, two legs and two feet,"
WAIST = "anatomically correct with two hands each with five fingers,"


def make_poses(B, calzado, setting, sp, st_var="A"):
    Bf = B + ", and " + calzado + "."
    # Standing — two variants to spread across the batch
    if st_var == "A":
        st = (f"{FULL} full body from a low hero angle, feet planted apart and firm on both platform "
              f"stilettos, both XXXL-nailed hands on the hips, shoulders pulled back and chin dropped "
              f"for a dominant direct stare down at the camera, commanding lumbar arch, hair framing "
              f"the face, {setting}, {CLOSE}")
    else:
        st = (f"{FULL} full body from a low angle below the hip, the weight on one platform stiletto "
              f"with the other foot forward and pointed, exaggerated S-curve with hip jutted to one "
              f"side and chest pushed forward, one XXXL-nailed hand sliding down the hip, the other "
              f"at the neckline, chin lifted, half-lidded predatory gaze to camera, hair cascading "
              f"over one shoulder, {setting}, {CLOSE}")
    bk = (f"{FULL} full body back view standing with both XXXL-nailed hands lifting all the cherry red "
          f"hair up off the nape, exposing the full back and spine line, the head dropped slightly forward, "
          f"the weight on one hip with the platform stiletto cocked, {setting}, {CLOSE}")
    se = (f"{FULL} perched on {sp} with one leg crossed over the other and the top platform stiletto "
          f"pointed at the camera, an extreme lumbar arch, one XXXL-nailed hand on the top knee and the "
          f"other fingertip at the bottom lip, the bust angled forward, shoulders rolled back, half-lidded "
          f"direct gaze, cherry red hair framing one breast, {setting}, {CLOSE}")
    si = (f"{FULL} full body side profile reclining on one side with an elegant S-curve, the hip rolled "
          f"up and the bust forward in silhouette, one XXXL-nailed hand supporting the head and the other "
          f"trailing along the waist, the top platform stiletto pointed and the legs elegantly stacked, "
          f"lips parted glossy, cherry red hair cascading along the surface, {setting}, {CLOSE}")
    di = (f"{WAIST} waist-up shot framed from the waist up, the torso turned and the augmented bust "
          f"presented, the chin dropped and the eyes lifted to the lens through the lashes, one XXXL "
          f"fingertip at the glossy bottom lip, the face the focus showing the detailed bimbo makeup, "
          f"a sensual half-lidded gaze, cherry red hair forward, the bodice detail crisp and legible, "
          f"{setting}, {CLOSE}")
    po = (f"{WAIST} a single woman alone, close-up social-media thirst-trap angled toward the lens, "
          f"the augmented bust dominant in the lower frame with the deep decollete visible, the face "
          f"protagonista in the upper-mid frame, one XXXL-nailed hand trailing from the collarbone "
          f"downward, half-lidded smoldering gaze directly into the camera, lips parted glossy, "
          f"cherry red hair cascading forward windblown, {setting}, {CLOSE}")
    od = (f"{FULL} full body semi-reclined propped on both elbows with the legs draped and one platform "
          f"stiletto pointed at the camera, a deep elegant back arch with the bust lifted, one XXXL-nailed "
          f"hand trailing along the collarbone and the chin lifted toward the camera, lips parted glossy, "
          f"cherry red hair cascading to one side, {setting}, {CLOSE}")
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
        "num": 661, "slug": "onyx_gloss_phantom", "nombre": "Onyx Gloss Phantom",
        "fecha": "23/06/2026", "batch": 'L661-L670 "Cuero Negro Total"',
        "cat": "Nightclub", "subcat": "Nightclub Leather Phantom",
        "tags": "#nightclub #leather #black #patent #halter #cutout #seamed #platform #batchL661-L670 #V5poses",
        "concepto": ("Nightclub Leather. Halter-neck microvestido de vinilo negro con cutouts arquitectonicos "
                     "en la cintura. Medias con costura. Plataformas negras cerradas."),
        "B": ("stunning woman wearing a Nightclub Leather look, a black high-gloss patent vinyl structured "
              "halter-neck micro-dress with a deep halter V tied at the nape, two architectural oval cutout "
              "panels at the natural waist exposing the sides of the torso, a fitted bodycon silhouette, "
              "a hidden centre-back zip, sheer black seamed nylon stockings with a straight black back seam, "
              "fully opaque at bust and groin, no text, bare arms and bare hands"),
        "calzado": ("platform stiletto pumps in black patent vinyl, 6-inch thin pin stiletto heel + 2-inch "
                    "black patent platform, closed sharp pointed toe, black ankle strap with a chrome buckle, "
                    "chrome heel cap"),
        "setting": ("on an exclusive rooftop nightclub terrace at night, the city skyline glittering below, "
                    "a backlit black resin bar top, and a glossy black stone floor"),
        "sp": "the glossy black resin bar top",
        "ambientacion": "en terraza nightclub exclusiva con skyline nocturno, barra de resina negra y suelo de piedra negra",
        "color": "negro — Monoblock",
        "st_var": "A",
    },
    {
        "num": 662, "slug": "black_lacquer_noir", "nombre": "Black Lacquer Noir",
        "fecha": "23/06/2026", "batch": 'L661-L670 "Cuero Negro Total"',
        "cat": "Escort", "subcat": "Escort Noir Latex Trench",
        "tags": "#escort #noir #latex #trench #blazerdress #seamed #thighhigh #platform #batchL661-L670 #V5poses",
        "concepto": ("Escort Noir. Blazer-dress de latex negro lacado al muslo con solapas y cinturon fino. "
                     "Medias semitransparentes. Botas de muslo con plataforma."),
        "B": ("stunning woman wearing an Escort Noir look, a black high-gloss latex blazer-dress with wide "
              "peak lapels, structured broad shoulders, a double-breasted front with two chrome buttons, "
              "a nipped-in waist with a thin black leather belt and chrome square buckle, a hemline stopping "
              "at upper thigh, fully closed with no under-layer visible, sheer black nylon stockings, "
              "fully opaque, no text, bare arms and bare hands"),
        "calzado": ("platform stiletto thigh-high boots in black patent vinyl, 5.5-inch thin pin stiletto "
                    "heel + 2-inch black patent platform, closed sharp pointed toe, full inner zip, black sole"),
        "setting": ("in a five-star hotel lobby after midnight, floor-to-ceiling black polished marble, "
                    "amber pendant lighting, a long black marble reception desk, and a deserted tiled corridor"),
        "sp": "the black marble reception desk edge",
        "ambientacion": "en lobby de hotel 5 estrellas medianoche con marmol negro, luz ambar y corredor desierto",
        "color": "negro — Monoblock",
        "st_var": "B",
    },
    {
        "num": 663, "slug": "obsidian_maid", "nombre": "Obsidian Maid",
        "fecha": "23/06/2026", "batch": 'L661-L670 "Cuero Negro Total"',
        "cat": "Domestic", "subcat": "Domestic Fetish Maid",
        "tags": "#domestic #maid #fetish #black #vinyl #white #opaque #platform #maryjane #batchL661-L670 #V5poses",
        "concepto": ("Fetish Maid. Minivestido de vinilo negro glosado con ribetes de latex blanco en "
                     "cuello y punos. Medias opacas. Mary janes con plataforma."),
        "B": ("stunning woman wearing a Domestic Fetish Maid look, a black high-gloss vinyl structured "
              "fitted mini maid dress with a scoop neckline, short puffed sleeves, a fitted bodice, a "
              "flared micro-skirt with a built-in white latex frill hem, white latex trim on the collar "
              "and sleeve cuffs, a small white latex apron front panel tied at the waist with a bow, "
              "black opaque hold-up stockings, fully opaque, no text, bare arms and bare hands"),
        "calzado": ("platform mary jane pumps in black patent vinyl, 5-inch thin pin stiletto heel + "
                    "1.5-inch black patent platform, closed rounded toe, single black strap across the "
                    "instep with a chrome buckle, black sole"),
        "setting": ("in a luxury penthouse kitchen with polished black marble countertops, chrome appliances "
                    "reflecting the overhead halogen lighting, and a glossy black tiled floor"),
        "sp": "the black marble kitchen island corner",
        "ambientacion": "en cocina penthouse de lujo con encimeras de marmol negro, electrodomesticos de cromo y suelo de baldosa negra",
        "color": "negro + blanco — Contraste",
        "st_var": "A",
    },
    {
        "num": 664, "slug": "black_widow_swim", "nombre": "Black Widow Swim",
        "fecha": "23/06/2026", "batch": 'L661-L670 "Cuero Negro Total"',
        "cat": "Bikini", "subcat": "Bikini Fetish Pool Leather",
        "tags": "#bikini #fetish #pool #leather #black #harness #sheer #platform #batchL661-L670 #V5poses",
        "concepto": ("Fetish Pool. Micro-bikini triangular de vinilo negro con arnes O-ring de cuero "
                     "en la cintura. Medias sheer negras. Plataformas negras cerradas."),
        "B": ("stunning woman wearing a Bikini Fetish Pool look, a black high-gloss vinyl triangle "
              "micro-bikini, a structured underwire push-up triangle top with thin adjustable ring-hardware "
              "string ties at the neck and back, a matching black high-gloss vinyl high-leg thong with slim "
              "string sides sitting low on the hips, a black leather O-ring waist harness with two chrome "
              "O-rings at the front hip bones, sheer black thigh-high hold-up stockings, "
              "fully opaque at bust and groin, no text, bare arms and bare hands"),
        "calzado": ("platform stiletto pumps in black patent vinyl, 6-inch thin pin stiletto heel + 2-inch "
                    "black patent platform, closed sharp pointed toe, slip-on, no strap, black sole"),
        "setting": ("beside a private indoor pool at night with black mosaic tile walls and floor, dramatic "
                    "underwater uplighting casting teal shimmer, and a polished stone pool deck"),
        "sp": "the polished stone pool deck edge",
        "ambientacion": "en piscina interior privada de noche con mosaico negro, luz submarina teal y deck de piedra pulida",
        "color": "negro — Monoblock",
        "st_var": "B",
    },
    {
        "num": 665, "slug": "midnight_stage_command", "nombre": "Midnight Stage Command",
        "fecha": "23/06/2026", "batch": 'L661-L670 "Cuero Negro Total"',
        "cat": "Stripper", "subcat": "Stripper Stage Leather",
        "tags": "#stripper #stage #leather #black #matte #chrome #chainbelt #seamed #platform #batchL661-L670 #V5poses",
        "concepto": ("Stripper Stage Leather. Halter bodycon microvestido de cuero negro mate con zipper "
                     "de cromo y cinturon de cadena metalica. Medias con costura. Botines plataforma."),
        "B": ("stunning woman wearing a Stripper Stage Leather look, a black matte leather halter-neck "
              "bodycon micro-dress with a deep V halter tied at the nape, an exposed chrome O-ring zip "
              "running the full front center from neckline to hem, a fitted silhouette, a detachable thin "
              "chrome metal chain belt looped once at the natural waist, sheer black seamed nylon stockings "
              "with a straight black back seam, fully opaque, no text, bare arms and bare hands"),
        "calzado": ("platform ankle boots in black patent vinyl, 6-inch thin pin stiletto heel + 2-inch "
                    "black patent platform, closed sharp pointed toe, inner zip fastening, chrome toe cap, "
                    "black sole"),
        "setting": ("on a dramatic black lacquered cabaret stage, a single wide white overhead spotlight, "
                    "deep shadow backstage, and a polished black floor that mirrors the figure"),
        "sp": "a low black lacquered box platform on stage",
        "ambientacion": "en escenario de cabaret negro lacado con foco blanco cenital y suelo espejo",
        "color": "negro + cromo — Contraste",
        "st_var": "A",
    },
    {
        "num": 666, "slug": "black_dahlia_pinup", "nombre": "Black Dahlia Pin-Up",
        "fecha": "23/06/2026", "batch": 'L661-L670 "Cuero Negro Total"',
        "cat": "Pin-Up", "subcat": "Pin-Up Noir Femme Fatale",
        "tags": "#pinup #noir #femmefatale #leather #black #highwaist #seamed #platform #batchL661-L670 #V5poses",
        "concepto": ("Pin-Up Noir. Falda lapiz de vinilo negro de cintura alta + crop halter de latex negro "
                     "con V profundo. Medias con costura y encaje. Plataformas negras con suela roja."),
        "B": ("stunning woman wearing a Pin-Up Noir femme fatale look, a black high-gloss vinyl high-waisted "
              "pencil skirt stopping at mid-calf with a narrow centre-back kick slit, a matching black high-gloss "
              "latex halter crop-top with a deep V-neckline, thin tied halter straps, a fitted band hem sitting "
              "at the waist, a tiny chrome star brooch pinned at the V-centre, sheer black seamed nylon "
              "stockings with a straight black back seam and a lace stocking top visible at mid-thigh, "
              "fully opaque, no text, bare arms and bare hands"),
        "calzado": ("platform stiletto pumps in black patent vinyl, 5-inch thin pin stiletto heel + 1.5-inch "
                    "black patent platform, closed sharp pointed toe, slip-on, no strap, red lacquered sole"),
        "setting": ("in a retro 1950s pin-up photography studio, a black velvet seamless backdrop, a single "
                    "dramatic side key spotlight, a polished black lacquered floor, and a chrome director's chair"),
        "sp": "the chrome director's chair",
        "ambientacion": "en estudio pin-up retro 50s con fondo de terciopelo negro, foco lateral dramatico y suelo lacado negro",
        "color": "negro + rojo suela — Contraste",
        "st_var": "B",
    },
    {
        "num": 667, "slug": "dark_energy_training", "nombre": "Dark Energy Training",
        "fecha": "23/06/2026", "batch": 'L661-L670 "Cuero Negro Total"',
        "cat": "Gym", "subcat": "Gym Athletic Leather Fetish",
        "tags": "#gym #athletic #leather #black #matte #cutout #sheer #platform #kneehigh #batchL661-L670 #V5poses",
        "concepto": ("Gym Leather Fetish. Bra deportivo de cuero negro mate + micro-shorts de cuero negro "
                     "con cutouts de O-ring en la cadera. Medias nylon sheer. Botas plataforma rodilla."),
        "B": ("stunning woman wearing a Gym Athletic Leather Fetish look, a black matte leather structured "
              "sports bra with a straight-across neckline, a wide underbust band and hidden underwire, "
              "matching black matte leather micro-shorts sitting high on the hip with a wide waistband, "
              "two chrome O-ring cutout panels on each outer hip revealing the skin, a matte finish "
              "throughout, sheer black nylon thigh-high stockings, "
              "fully opaque at bust and groin, no text, bare arms and bare hands"),
        "calzado": ("platform stiletto knee-high boots in black patent vinyl, 6-inch thin pin stiletto "
                    "heel + 2-inch black patent platform, closed sharp pointed toe, full inner zip, black sole"),
        "setting": ("in a private high-end gym with black mirrored walls, exercise equipment silhouetted in "
                    "shadow, cool neon strip lighting at floor level, and a polished black rubber gym floor"),
        "sp": "a padded black weight bench",
        "ambientacion": "en gym privado de lujo con paredes espejo negras, equipamiento en sombra y neon frio a nivel de suelo",
        "color": "negro + cromo — Contraste",
        "st_var": "A",
    },
    {
        "num": 668, "slug": "black_diamond_executive", "nombre": "Black Diamond Executive",
        "fecha": "23/06/2026", "batch": 'L661-L670 "Cuero Negro Total"',
        "cat": "Corporate", "subcat": "Corporate Leather Power",
        "tags": "#corporate #leather #black #patent #blazer #pencilskirt #opaque #platform #batchL661-L670 #V5poses",
        "concepto": ("Corporate Leather Power. Blazer doble botonadura de vinilo negro glosado + falda "
                     "lapiz a juego bajo la rodilla. Medias opacas con costura. Plataformas con tacon cromo."),
        "B": ("stunning woman wearing a Corporate Leather Power look, a black high-gloss patent vinyl "
              "double-breasted structured blazer with sharp peak lapels, four chrome dome buttons, a "
              "nipped-in waist, strong square shoulders, worn with nothing beneath, a matching black "
              "high-gloss patent vinyl pencil skirt stopping just below the knee with a narrow centre-back "
              "slit, a thin black leather waist belt with a polished silver square buckle, black opaque "
              "seamed stockings with a straight black back seam, fully opaque, no text, bare arms and bare hands"),
        "calzado": ("platform stiletto pumps in black patent vinyl, 5.5-inch thin pin stiletto heel + "
                    "1.5-inch black patent platform, closed sharp pointed toe, slip-on, no strap, chrome heel cap"),
        "setting": ("in a high-rise executive corner office at night with floor-to-ceiling glass overlooking "
                    "the city, a single spotlit glass desk, a black leather executive chair, and a polished "
                    "dark marble floor"),
        "sp": "the edge of the glass executive desk",
        "ambientacion": "en oficina ejecutiva en altura de noche con cristal piso-techo, escritorio de vidrio y marmol oscuro",
        "color": "negro + plata — Contraste",
        "st_var": "B",
    },
    {
        "num": 669, "slug": "black_iron_corset", "nombre": "Black Iron Corset",
        "fecha": "23/06/2026", "batch": 'L661-L670 "Cuero Negro Total"',
        "cat": "Lenceria", "subcat": "Lenceria Fetish Corset",
        "tags": "#lingerie #fetish #corset #leather #black #suspenders #seamed #platform #batchL661-L670 #V5poses",
        "concepto": ("Lenceria Fetish. Corset longline overbust de cuero negro con ballenas, lace-up trasero "
                     "y clips de liguero. Brief de latex negro. Medias con costura y liguero. Plataformas."),
        "B": ("stunning woman wearing a Lenceria Fetish Corset look, a black high-gloss leather longline "
              "overbust corset with steel boning visible as raised ridges, a lace-up back, four chrome "
              "suspender clips at the hem holding the stockings, a straight-across bust shelf neckline, "
              "a matching black high-gloss latex high-cut brief with a thin waistband, a black satin "
              "ribbon bow detail at the centre-front corset top, sheer black seamed nylon stockings with "
              "a straight black back seam held by the suspender clips, "
              "fully opaque at bust and groin, no text, bare arms and bare hands"),
        "calzado": ("platform stiletto pumps in black patent vinyl, 6-inch thin pin stiletto heel + 2-inch "
                    "black patent platform, closed sharp pointed toe, slip-on, no strap, chrome heel cap"),
        "setting": ("in a dark boudoir suite with floor-to-ceiling black velvet drapes, a single warm amber "
                    "standing floor lamp, a dark lacquered vanity mirror, and a plush black carpet floor"),
        "sp": "the dark lacquered vanity stool",
        "ambientacion": "en suite boudoir oscura con cortinas de terciopelo negro, lampara ambar y alfombra negra",
        "color": "negro — Monoblock",
        "st_var": "A",
    },
    {
        "num": 670, "slug": "obsidian_siren_gala", "nombre": "Obsidian Siren Gala",
        "fecha": "23/06/2026", "batch": 'L661-L670 "Cuero Negro Total"',
        "cat": "Gala", "subcat": "Gala Leather Column Siren",
        "tags": "#gala #alfombranegra #leather #black #patent #column #slit #chrome #seamed #platform #batchL661-L670 #V5poses",
        "concepto": ("Gala Leather Siren. Vestido columna de vinilo negro glosado piso-suelo con tajo "
                     "extreme al muslo derecho y cadena de cintura de cromo. Medias con costura. Plataformas."),
        "B": ("stunning woman wearing a Gala Leather Siren look, a black high-gloss patent vinyl strapless "
              "column gown, a structured boned strapless bodice with a straight-across neckline, a smooth "
              "fitted floor-length silhouette, an extreme high thigh-slit on the right side revealing the "
              "full leg from the hip down, a thin chrome metal waist chain draped once at the natural waist, "
              "sheer black seamed nylon stockings with a straight black back seam visible through the slit, "
              "fully opaque, no text, bare arms and bare hands"),
        "calzado": ("platform stiletto pumps in black patent vinyl, 6-inch thin pin stiletto heel + 2-inch "
                    "black patent platform, closed sharp pointed toe, slip-on, no strap, chrome heel cap"),
        "setting": ("at a grand gala venue entrance with a glossy black marble floor, a suspended installation "
                    "of black crystal chandeliers overhead, and a dark press-carpet runner"),
        "sp": "a tall black-draped cocktail table",
        "ambientacion": "en entrada de gala con marmol negro, instalacion de aranas de cristal negro y alfombra oscura",
        "color": "negro + cromo — Contraste",
        "st_var": "B",
    },
]

POSE_NAMES = ["Standing", "Back View", "Seated", "Side Profile", "Ditzy", "Pov", "Odalisque"]

out_lines = []
for lk in looks:
    ps = make_poses(lk["B"], lk["calzado"], lk["setting"], lk["sp"], lk.get("st_var", "A"))
    out_lines.append(f'\n## Look {lk["num"]}: {lk["nombre"]} ({lk["fecha"]} - batch {lk["batch"]} - {lk["cat"]} - {lk["subcat"]} - {lk["color"]} - platform + medias)\n')
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

# Write standalone markdown
with open("_batch_L661_L670.md", "w", encoding="utf-8") as f:
    f.write(content)

# QA checks
assert content.count("glove") == 0, "FALLA: guantes detectados"
for lk in looks:
    b_lower = lk["B"].lower()
    assert "chunky" not in b_lower, f"FALLA: chunky en outfit L{lk['num']}"
    assert "open toe" not in b_lower, f"FALLA: open toe con medias en L{lk['num']}"
    assert "open-toe" not in b_lower, f"FALLA: open-toe con medias en L{lk['num']}"
    assert "transparent" not in lk["calzado"].lower(), f"FALLA: plataforma transparente con medias en L{lk['num']}"
    assert "clear" not in lk["calzado"].lower(), f"FALLA: clear platform con medias en L{lk['num']}"
    assert "platform" in lk["calzado"].lower(), f"FALLA: sin plataforma en L{lk['num']}"
    count = content.count(lk["calzado"])
    assert count >= 7, f"FALLA: token calzado L{lk['num']} aparece {count} veces (minimo 7)"

print(f"OK: {len(content)} chars, {content.count(chr(10))} lineas")
print("QA: 0 guantes | 0 chunky | 0 open-toe | 0 clear/transparent platform | plataforma x10 | tokens calzado x7 TODOS OK")
