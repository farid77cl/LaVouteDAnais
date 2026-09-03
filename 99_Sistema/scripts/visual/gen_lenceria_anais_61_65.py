"""
Script temporal: genera los 5 looks de Lencería L61-L65 de Anaïs Belland
(La Perla / Honey Birdette, reinterpretados en su registro noble) y los
escribe en output_anais_L61_L65.md listos para pegar en galeria_looks_anais.md.

Patrón técnico calcado de gen_lenceria_808_812.py (Ele), adaptado al motor
de Anaïs: usa PromptBuilder("anais"), su repertorio de sub-poses real
(pb.pose) y su tabla de prefijos cinematográficos por arquetipo
(pb.prefijo_arquetipo) — Anaïs es el único personaje con prefijo variable
por arquetipo, así que el ensamblado NO puede copiar el prefijo fijo que
usa el script de Ele.

BLOQUE A: copiado LITERAL desde dna_v2_3.md (ADN Inamovible V2.3), sin
resumir ni parafrasear, tal como exige `anais.md` §2 y `dna_v2_3.md`.
Precedente verificado en el batch más reciente de la galería (Look 56-60,
25/08/2026): el Look 60 usa el token literal completo (incluido su calzado
y luz por defecto) y agrega el calzado/luz específicos del look aparte —
la reiteración no rompe nada porque FOOTWEAR_ECHO cierra el prompt
reafirmando el calzado real de BLOQUE B. Se sigue el mismo patrón aquí.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from prompt_builder import PromptBuilder, slugify

pb = PromptBuilder("anais")

# ---------------------------------------------------------------- BLOQUE A
# Copiado literal de .agent/skills/anais-outfit-engine/references/dna_v2_3.md
# sección "BLOQUE A — ADN Inamovible". NO TOCAR ni una palabra.
BLOQUE_A_LITERAL = (
    "(unmistakably 42-year-old aristocratic woman, mature sharp bone structure and "
    "commanding severity of expression, never a soft youthful face:1.4), (her lips "
    "visibly and clearly parted, never fully closed, never smiling, the lower lip heavy "
    "and still; her eyelids half-lowered yet her eyes level and fixed, coldly sizing up "
    "whoever is looking rather than inviting them; one brow held a fraction higher than "
    "the other; her chin carried level or tipped slightly down, never lifted up sweetly; "
    "this is the face of a 42-year-old woman who has already won the room:1.5), (flawless "
    "completely smooth unlined forehead, taut porcelain skin with zero visible creases "
    "or fine lines anywhere, the seamless perfection of decades of obsessive cosmetic "
    "maintenance:1.4), radiant dewy porcelain skin, luminous flawless medical-grade "
    "cosmetic finish, (aristocratic refined oval face, sculpted lifted hollowed mature "
    "cheekbones, sharp angular defined jawline:1.3), composed poised expression of a "
    "woman who has commanded rooms for decades, quiet mature gravitas in her gaze, "
    "small classic Old Hollywood beauty mark mole above upper left lip, ultra precise "
    "Old Hollywood editorial makeup, precisely drawn dark brown thin arched brows 1940s "
    "style, deep taupe and charcoal eyeshadow softly sculpted into the crease giving "
    "heavy-lidded smoky depth, sharp precise black cat-eye liquid liner with dramatically "
    "elongated wing at outer corner, full voluminous glamorous lashes dense and defined, "
    "(naturally full lips with soft volume and a well-defined cupid's bow, vivid deep "
    "crimson classic Hollywood red, flawlessly defined with a subtle gloss on the inner "
    "edge, visibly parted and never closed, in a cold knowing look:1.4), honey blonde hair in sculpted "
    "voluminous vintage Hollywood pin-waves or victory rolls side parted, extremely long "
    "hip-length hair cascading past the shoulders, slender mature elegant hourglass "
    "figure with extreme waist training tightlacing corset, S-curve posture, not "
    "voluptuous, not augmented, not bimbo-exaggerated, (natural moderate breasts, firm "
    "and perky with a well-defined natural shape:1.2), firm smooth glutes softly toned "
    "rather than sharply muscular, heavy-lidded bedroom eyes gaze, long stiletto-shaped "
    "manicured fingernails with glossy deep red polish, wearing 12cm black patent "
    "leather stiletto heels no platform iconic red sole, cinematic chiaroscuro dramatic "
    "lighting, soft key light flattering her impeccably maintained features, George "
    "Hurrell style portraiture, intimate tension."
)

COLOR_LOCK = (
    "in rich vivid full color, not black and white, not monochrome, not grayscale, "
    "warm golden-amber color palette with honey blonde hair and deep crimson red lips "
    "clearly visible in color,"
)

ARQUETIPO = "Boudoir / Lencería"
pref = pb.prefijo_arquetipo(ARQUETIPO)  # {"prefijo": ..., "luz": ...}
# Orden verificado contra el batch más reciente (Look 56-60): prefijo, luz, color-lock, ADN.
BLOQUE_A = (
    f"{pref['prefijo']}, {pref['luz']}, {COLOR_LOCK} {BLOQUE_A_LITERAL}"
)

# ---------------------------------------------------------------- BLOQUE B
BLOQUE_B = {
    61: (  # La Perla — Merry Widow Carmesí (arquitectura A4, inédita en el roster reciente)
        "a longline crimson chantilly lace merry widow with integrated suspenders and "
        "visible spiral steel boning, a deep sweetheart neckline closed with a row of "
        "tiny hook-and-eye fastenings down the front, a small matching crimson chantilly "
        "lace thong cut high at the waist in true period style but with the leg openings "
        "cut sharply upward to the crest of the hip bone, the whole length of hip and "
        "thigh left bare, a scalloped lace edge, a floor-length sheer black chiffon open "
        "robe reaching all the way to the floor and trailing behind her, semi-transparent "
        "fabric that reveals the merry widow beneath from every angle including from "
        "behind, falling loose off one shoulder, dramatic wide bell-shaped cuffs, cinched "
        "loosely at the waist with a thin crimson satin belt, sheer black stockings with "
        "a fine back seam gartered above the thong, (12cm black patent leather D'Orsay "
        "stiletto pump with open sides and a closed pointed toe, iconic red sole:1.2), a "
        "vintage ruby collar necklace, a slim silver cigarette holder, almond-shaped "
        "nails in glossy deep crimson lacquer, La Perla aristocratic Italian poise"
    ),
    62: (  # La Perla — Corsé Medianoche y Zorro Plateado (arquitectura A6, + piel §5.1b)
        "an overbust corset in midnight-blue silk charmeuse with visible antique-silver "
        "spiral steel boning, a deep sweetheart neckline, a small matching midnight-blue "
        "chantilly lace thong cut high at the waist in true period style but with the leg "
        "openings cut sharply upward to the crest of the hip bone, the whole length of "
        "hip and thigh left bare, a scalloped lace edge, sheer graphite-grey stockings "
        "with a fine back seam gartered above the thong, (12cm midnight-blue suede "
        "knee-high stiletto boot ending exactly at the knee, antique-silver heel cap, "
        "iconic red sole:1.2), a silver fox fur stole draped over one shoulder, the fur "
        "lying flat and unbroken across both shoulder blades with its edge following the "
        "same line front and back, the cinched waist of the corset clearly visible below "
        "it, an antique silver Art Déco necklace, a slim silver cigarette holder, oval "
        "nails in glossy antique-silver lacquer, La Perla aristocratic Italian poise"
    ),
    63: (  # La Perla — Peignoir Marfil y Oro (arquitectura A9, sin medias)
        "a sheer ivory silk gauze peignoir robe, open at the front and falling all the "
        "way to the floor, trailing behind her, transparent under the candlelight, over bare "
        "toned skin, dramatic wide bell-shaped cuffs edged in gold thread, cinched "
        "loosely at the waist with a thin gold-satin belt, a small matching ivory "
        "chantilly lace thong beneath it, cut high at the waist in true period style but "
        "with the leg openings cut sharply upward to the crest of the hip bone, the whole "
        "length of hip and thigh left bare, a scalloped lace edge, bare toned legs, (12cm "
        "ivory satin 1940s-style strap stiletto sandal with a slender ankle strap and a "
        "gold buckle, open pointed toe, iconic red sole:1.2), matching glossy deep red "
        "pedicure on visible toenails, a single strand of pearls, a delicate gold "
        "necklace, oval nails in glossy deep red lacquer, La Perla aristocratic Italian "
        "poise"
    ),
    64: (  # Honey Birdette reinterpretado — Arnés Borgoña de Látex y Bronce Antiguo
        "a structured harness bodice in deep-wine clinical-grade latex, triangulated "
        "straps banding the ribcage and underbust with antique bronze ring hardware at "
        "the sternum and hip points, the straps cinching the waist and framing the bust "
        "without covering it, the bust left bare above the harness the way a guêpière "
        "leaves it bare, visible waist boning beneath the straps, a small matching "
        "deep-wine latex thong cut high at the waist in true period style but with the "
        "leg openings cut sharply upward to the crest of the hip bone, the whole length "
        "of hip and thigh left bare, a single antique bronze O-ring centered at the front "
        "waist, matching thigh harness bands in deep-wine latex on each outer thigh "
        "secured with antique bronze ring hardware, bare toned legs, (12cm deep-wine "
        "patent leather T-strap stiletto sandal, antique bronze buckle, open toe, iconic "
        "red sole:1.2), matching glossy deep red pedicure on visible toenails, a wide "
        "antique bronze cuff on one wrist, an antique bronze collar necklace, "
        "stiletto-shaped nails in glossy deep-wine lacquer, Honey Birdette architectural "
        "discipline reinterpreted in noble latex and antique bronze, the harness worn "
        "over the body rather than a rigid cage"
    ),
    65: (  # Honey Birdette reinterpretado — Arnés Negro y Oro Imperial
        "a structured harness bodice in noir clinical-grade latex, triangulated straps "
        "crossing the ribcage and underbust with imperial-gold ring hardware at the "
        "sternum and hip points, the straps cinching the waist and framing the bust "
        "without covering it, the bust left bare above the harness the way a guêpière "
        "leaves it bare, visible waist boning beneath the straps, a small matching noir "
        "latex thong cut high at the waist in true period style but with the leg openings "
        "cut sharply upward to the crest of the hip bone, the whole length of hip and "
        "thigh left bare, a single imperial-gold O-ring centered at the front waist, "
        "matching thigh harness bands in noir latex on each outer thigh secured with "
        "imperial-gold ring hardware, an open floor-length sheer noir clinical-grade "
        "latex robe reaching all the way to the floor and trailing behind her, "
        "semi-transparent fabric that reveals the harness beneath from every angle "
        "including from behind, falling loose off both shoulders, dramatic wide "
        "bell-shaped cuffs, cinched loosely at the waist with a thin gold cord belt, "
        "sheer black fishnet stockings with a fine back seam gartered above the thong, "
        "(12cm black patent leather stiletto pump pointed toe, imperial-gold heel cap, "
        "iconic red sole:1.2), a wide antique-gold cuff on one wrist, an imperial-gold "
        "collar necklace, stiletto-shaped nails in glossy black lacquer, Honey Birdette "
        "architectural discipline reinterpreted in noble latex and imperial gold, the "
        "harness worn over the body rather than a rigid cage"
    ),
}

SETTING = {
    61: ("an intimate Parisian boudoir suite at La Voûte, a tufted burgundy velvet "
         "chaise longue beneath a gilt Rococo mirror, a crystal decanter and a single "
         "red rose on the nightstand, warm amber candlelight"),
    62: ("a moonlit dressing room at La Voûte, a silver-leafed vanity with a triple "
         "mirror, a fainting couch upholstered in midnight-blue velvet, a crystal "
         "perfume tray catching the warm candlelight"),
    63: ("an ivory boudoir chamber at La Voûte, a chaise longue draped in ivory silk "
         "beneath a gilded arched mirror, a crystal vase with a single white gardenia "
         "on the vanity, warm candlelight glowing against pale silk"),
    64: ("a private atelier chamber at La Voûte styled for latex couture, a "
         "bronze-framed cheval mirror, a low chaise upholstered in wine-dark velvet, "
         "an antique bronze candelabra casting warm directional light across polished "
         "floors"),
    65: ("a black-lacquered boudoir salon at La Voûte, a gold-framed full-length "
         "mirror, a low ebony chaise longue with gold piping, an antique gold "
         "candelabra glowing against the dark walls"),
}

PROPS = {
    61: {"seat": "the tufted burgundy velvet chaise longue", "wall": "the boudoir suite wall",
         "surface": "the chaise longue cushion", "upright": "the gilt Rococo mirror frame"},
    62: {"seat": "the midnight-blue velvet fainting couch", "wall": "the dressing room wall",
         "surface": "the fainting couch cushion", "upright": "the triple vanity mirror"},
    63: {"seat": "the ivory silk chaise longue", "wall": "the boudoir chamber wall",
         "surface": "the chaise longue cushion", "upright": "the gilded arched mirror"},
    64: {"seat": "the wine-dark velvet chaise", "wall": "the atelier chamber wall",
         "surface": "the chaise cushion", "upright": "the bronze-framed cheval mirror"},
    65: {"seat": "the ebony chaise longue", "wall": "the black-lacquered salon wall",
         "surface": "the chaise longue cushion", "upright": "the gold-framed full-length mirror"},
}

META = {
    # numero: (titulo, paleta, con_medias, tag_extra, concepto)
    61: ("Merry Widow Carmesí", "Carmesí + Negro", True, "laperla",
         "Paso 0 contra Look 57/55/51: arquitectura A4 (Longline/merry widow), sin uso "
         "en el roster reciente -- rompe el molde guêpière/cuarto-copa/corselette de los "
         "últimos tres. Paleta carmesí+negro inédita en esos tres (rosa antiguo/esmeralda/"
         "teal). Calzado D'Orsay, distinto del pointed-toe pump y el Mary Jane recientes. "
         "Reinterpretación La Perla: encaje chantilly protagonista, silueta longline de "
         "tightlacing, aristocracia italiana sin fetiche sintético."),
    62: ("Corsé Medianoche y Zorro Plateado", "Azul Medianoche + Plata Antigua", True, "laperla",
         "Paso 0 contra Look 61/57/55: arquitectura A6 (corsé overbust), silueta distinta "
         "de merry widow/guêpière/cuarto-copa. Paleta azul medianoche + plata antigua, "
         "inédita en el trío reciente. Calzado bota a la rodilla, distinto de D'Orsay/"
         "Mary Jane/pointed-toe pump. Cubre la cuota de pieles (§8): zorro plateado, "
         "abierto, cintura de tightlacing visible debajo -- ninguno de los últimos tres "
         "looks de Boudoir llevaba piel."),
    63: ("Peignoir de Gasa Marfil y Oro", "Marfil + Oro Imperial", False, "laperla",
         "Paso 0 contra Look 62/61/57: arquitectura A9 (peignoir de gasa), nunca usada en "
         "el roster -- la única de las tres La Perla sin corsetería estructurada, el "
         "extremo opuesto de A4/A6. Paleta marfil+oro, inédita en el resto del batch. "
         "Sandalia de tira 1940s de puntera abierta (sin medias, piernas desnudas), "
         "distinta de D'Orsay y bota a la rodilla. Reinterpretación La Perla más cercana "
         "al canon existente: encaje chantilly + gasa transparente, cero fricción."),
    64: ("Arnés Borgoña de Látex y Bronce Antiguo", "Borgoña/Vino + Bronce Antiguo", False, "honeybirdette",
         "Paso 0 contra Look 63/62/61: primer look Honey Birdette del batch -- traduce la "
         "arquitectura de arnés de Honey Birdette (bandas triangulares + hardware anular) "
         "al léxico noble de Anaïs: látex de grado clínico en vez de vinilo de club, "
         "hardware en bronce antiguo en vez de chrome plateado, arnés SOBRE el cuerpo en "
         "vez de jaula rígida, y el busto descubierto por encima del arnés siguiendo el "
         "mismo precedente ya canónico de la guêpière (A5, 'the bust left bare and "
         "uncovered above it'). Sandalia T-strap de puntera abierta, calzado sin repetir "
         "contra los tres anteriores."),
    65: ("Arnés Negro y Oro Imperial", "Negro + Oro Imperial", True, "honeybirdette",
         "Paso 0 contra Look 64/63/62: segundo look Honey Birdette -- misma traducción de "
         "arquitectura de arnés que el 64 pero en negro + oro imperial (paleta reservada "
         "del canon, #D4AF37) y con bata de látex traslúcido abierta hasta el suelo "
         "encima, cerrando el batch con la silueta de bata que abrió el 61. Medias de "
         "fishnet bajo el arnés y stiletto pump clásico con tapa de tacón en oro -- "
         "calzado distinto de los cuatro anteriores del batch."),
}

SLOTS       = ["standing", "back_view", "seated", "side_profile", "sovereign_gaze", "pov", "odalisque"]
SLOT_LABELS = ["Standing", "Back View", "Seated", "Side Profile", "Sovereign Gaze", "POV", "Odalisque"]

# Negative: base literal de dna_v2_3.md + las adiciones obligatorias de anais.md §3
# (tatuajes/piercings/joven/sonrisa amplia -- siempre; pantalón/piernas abiertas --
# siempre, DRESS_LEG_CLOSURE ya cubre la mecánica pero el perfil pide reforzarlo aquí
# también) + un cierre propio de este batch (registro lencería fina, nunca casual).
NEG_BASE_DNA = (
    "(different face:1.3), smiling broadly, laughing, playful expression, casual pose, "
    "relaxed posture, red hair, dark hair, short hair, messy hair, modern makeup, bimbo "
    "makeup, hot pink lips, overlined lips (modern style), neon colors, bright colors, "
    "colorful outfit, white dress, pink outfit, glitter, modern clothing, block heel, "
    "chunky heel, flat shoes, barefoot, sneakers, cyberpunk, sci-fi, industrial, factory, "
    "neon lights, outdoor, natural setting, low quality, blurry, distorted face, child, "
    "teenager, man, male, platform heels, modern lingerie, sexy, hot, horny, naked, nude, "
    "seductive, provocative, tempting, naughty, open mouth, tongue, explicit nude, "
    "(distorted animal print, neon leopard:1.2), cheap fabric texture"
)
NEG_EXTRA_PERFIL = (
    "tattoos, piercings, young woman, teen, wide smile, trousers, pants, leggings, jeans, "
    "shorts, palazzo pants, jumpsuit, legs spread apart under a dress, legs parted under "
    "a skirt"
)
NEG_LENCERIA = (
    "cotton lingerie, granny nightgown, modest full-coverage underwear, cheap costume "
    "lingerie, daywear, swimwear context, beach setting, bridal innocent virginal, ingenue"
)
NEG_FULL_BASE = ", ".join([NEG_BASE_DNA, NEG_EXTRA_PERFIL, NEG_LENCERIA])

out = []
for look_n in [61, 62, 63, 64, 65]:
    titulo, paleta, con_medias, tag_extra, concepto = META[look_n]
    slug = slugify(titulo)
    medias_suffix = " · Con medias" if con_medias else ""
    out.append(
        f"## \U0001f451 Look {look_n}: {titulo} "
        f"(28/08/2026 · batch L61-L65 \"La Perla y HB Lencería\" · {ARQUETIPO})"
    )
    out.append(f"- **Ubicacion:** `05_Imagenes/anais/look{look_n}_{slug}/`")
    out.append(
        f"- **Tags:** #boudoir #{slugify(paleta).replace('_','')[:20]} #{tag_extra} "
        f"#anais #batchL61-L65 #V7poses"
    )
    out.append("")
    out.append(f"**Arquetipo:** {ARQUETIPO} · **Paleta:** {paleta}{medias_suffix}")
    out.append("")
    out.append(f"**Concepto:** {concepto}")
    out.append("")
    out.append(f"**BLOQUE B:** `{BLOQUE_B[look_n]}`")
    out.append("")
    out.append("### \U0001f4f8 Imágenes (0/7 — Pendiente)")
    out.append("")
    out.append("| Standing | Back View | Seated | Side Profile | Sovereign Gaze | POV | Odalisque |")
    out.append("| :---: | :---: | :---: | :---: | :---: | :---: | :---: |")
    out.append("| ⏳ Pendiente | ⏳ Pendiente | ⏳ Pendiente | ⏳ Pendiente | ⏳ Pendiente | ⏳ Pendiente | ⏳ Pendiente |")
    out.append("")
    props = PROPS[look_n]
    for i, (slot, label) in enumerate(zip(SLOTS, SLOT_LABELS)):
        pose   = pb.pose(slot, look_n, props=props)
        prompt = pb.build(BLOQUE_A, BLOQUE_B[look_n], slot, pose, SETTING[look_n])
        out.append(f"**{i+1}. {label}:**")
        out.append("")
        out.append("```text")
        out.append(prompt)
        out.append("```")
        out.append("")
    neg = pb.build_negative(NEG_FULL_BASE)
    out.append(f"**Negative Prompt:** `{neg}`")
    out.append("")
    out.append("---")
    out.append("")

result = "\n".join(out)
outpath = pathlib.Path(__file__).parent / "output_anais_L61_L65.md"
outpath.write_text(result, encoding="utf-8")
print(f"OK -- output escrito en {outpath}")
n_prompts = len([x for x in out if x.startswith("**") and ". " in x and x.endswith(":")])
print(f"Prompts generados: {n_prompts}")
print(f"Total lineas: {len(out)}")
