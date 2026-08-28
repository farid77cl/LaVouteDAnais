#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
gen_lenceria_missdoll_61_65.py -- genera los looks 61-65 de Miss Doll
(La Perla / Honey Birdette Lenceria) y escribe output_missdoll_61_65.md
listo para pegar en GALERIA_OUTFITS_MISS_DOLL.md, antes del Look 60.

Mismo patron que gen_lenceria_808_812.py (Ele), pero:
  - usa PromptBuilder("miss_doll") -- soportado de fabrica, sin ajustes.
  - el color de sombra/labios va en BLOQUE B por look (perfil miss_doll.md
    Sec5.5 punto 8): se sustituye dentro de una copia del BLOQUE A, no se
    inventa un tercer bloque -- mismo patron que ya usan los Looks 54/56-60
    reales de la galeria (verificado leyendo el archivo).
  - encabezado sin codigo/polo (eso es propio del script de Ele): sigue
    el formato real de Miss Doll, "## Look N: Titulo (fecha - batch - Categoria)".
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from prompt_builder import PromptBuilder, slugify

pb = PromptBuilder("miss_doll")

BLOQUE_A_BASE = (
    "hyper-realistic high-end editorial glamour photography of Miss Doll, adult glamorous woman, "
    "(soft rounded oval face:1.1), smooth softly rounded jawline, (soft gently curved full "
    "cheekbones:1.1), small refined rounded chin, delicate refined features COMMANDING, sharp "
    "platinum blonde asymmetric angled bob, sleek straight razor-cut strands, ice platinum "
    "highlights, clear exposed forehead, NO BANGS, (small refined perky upturned nose:1.2), "
    "(huge oversized round almond-shaped cold pale steel grey eyes, wide open eye opening:1.4), "
    "pale icy grey iris with sharp dark limbal ring, (fixed dominant professional gaze zero "
    "warmth, slow appraising once-over gaze sweeping head to toe with cold superiority:1.3), "
    "chin elevated 5 degrees, (bold precisely filled brow makeup, dark smoky taupe-grey brow "
    "color noticeably darker than the platinum hair for maximum contrast, extremely high "
    "dramatic raised arch positioned high on brow bone, sharp clean tapered tail, thick clearly "
    "visible brow shape:1.5), HEAVY GLAMOUR editorial makeup with (thick sharp angular winged "
    "eyeliner upticked pointed wing tip:1.2), intense shimmer smokey eye technique, (impossibly "
    "long mega XXL individual false lashes at outer corners dramatic cat-eye:1.2), (blinding "
    "chrome strobing highlight on cheekbones nose bridge and brow bone:1.2), (soft gentle "
    "contour warm shadow under cheekbone:1.0), (aggressively overlined voluminous ULTRA PLUMP "
    "high-gloss wet lips exaggerated cupid's bow full pillowy lips mirror-gloss finish:1.3) "
    "curved into a (subtle smug smirk, one corner of the mouth raised:1.2), human realistic "
    "face DOMINANT smirking expression, pale cold porcelain white skin, editorial realistic "
    "human skin texture subtle visible pores, cold undertone, sculptural EXTREME hourglass "
    "silhouette, (toned midriff, subtly defined abs with soft natural muscle separation, faint "
    "visible obliques:1.2), (slender delicate shoulders, long lean toned arms with soft subtle "
    "muscle tone, not bulky, feminine and graceful:1.2), (long lean slender toned legs, soft "
    "subtle thigh definition, not muscular, elegant model proportions:1.2), (colossal oversized "
    "massive chest, extreme high-profile artificial breast implants, impossible gravity-defying "
    "spherical shape, ultra-high profile silicone augmentation, overt bolted-on projection, "
    "unmistakably fake implants:1.5), dramatic alluring plunging neckline, deep prominent "
    "cleavage, aggressively narrow cinched waist, full wide hips, tall lean slender commanding "
    "figure, rigid upright posture, square shoulders pulled back, (impeccably manicured long "
    "glossy nails:1.1)"
)

NEG_BASE = (
    "bangs, fringe, covered forehead, dark hair, brunette, ponytail, bun, childish face, teen, "
    "natural makeup, subtle makeup, nude lips, matte lips, rosy cheeks, warm natural skin tone, "
    "wax skin, plastic mannequin skin, tattoos, casual outfit, flat shoes, sneakers, block heel, "
    "chunky heel, vulgar cheap costume, slouched shoulders, warm smile, laughing, sharp angular "
    "face, angular jawline, thin invisible eyebrows, sparse pale blonde eyebrows, barely visible "
    "brows, faint eyebrows, eyebrows blending into skin, bodybuilder physique, overly muscular, "
    "bulky muscles, veiny muscles, grotesque six-pack, masculine muscle mass, thick bulky arms, "
    "thick muscular shoulders, wide muscular legs, thick calves, muscular bulky thighs, small "
    "chest, natural breasts, flat chest, corset, waist cincher, bustier, doll face, mannequin "
    "face, uncanny doll-like appearance, glassy doll eyes, porcelain doll aesthetic, full brief, "
    "high-waist brief, high-waisted panty, boyshort, boy shorts, hipster brief, culotte, tap "
    "pants, granny panties, bloomers, full-coverage bikini bottom, bikini bottom covering the "
    "buttocks, full seat coverage, legs spread apart under a dress, legs parted under a skirt, "
    "mule, mules, platform mule, mule sandals, slide sandals, backless heels, short robe, mini robe"
)
# El corse va en negative BASE por defecto (perfil Sec3): solo el Look 62 lo lleva puesto,
# asi que a ESE look se le saca "corset, waist cincher, bustier" antes de construir el negativo.
NEG_SIN_CORSET = NEG_BASE.replace("corset, waist cincher, bustier, ", "")

MAQUILLAJE = {
    61: ("smoky gunmetal eyeshadow with a violet duochrome shimmer", "berry-plum"),
    62: ("warm champagne-gold shimmer eyeshadow", "copper-bronze"),
    63: ("soft rose-taupe shimmer eyeshadow with a pearl sheen", "wine-burgundy"),
    64: ("sharp magenta-chrome eyeshadow with a metallic foil finish", "black-plum"),
    65: ("icy seafoam-silver duochrome eyeshadow", "vivid terracotta"),
}

BLOQUE_B = {
    61: (
        "a Honey Birdette-inspired architectural cage bodysuit in high-gloss gunmetal chrome "
        "vinyl, form-fitting through the torso with a deep plunging V-neckline, geometric cutout "
        "panels at the ribcage and hips edged with fine polished chrome ring hardware, a midnight "
        "navy wet-look latex underlay glimpsed through the cutouts, thin adjustable chrome "
        "shoulder straps, the seat cut as a narrow g-string baring the hips; a matching gunmetal "
        "chrome choker collar with a center O-ring; a hot-pink enamel stud set into the sternum "
        "ring as the signature pink accent; (8-inch gunmetal chrome platform ankle-strap sandal, "
        "open pointed toe, razor-thin metal needle heel, mirror-chrome sole:1.3); long "
        "coffin-shaped nails in glossy gunmetal chrome polish."
    ),
    62: (
        "a La Perla-inspired aristocratic overbust corset in ivory champagne laser-cut "
        "lace-pattern vinyl, gloss finish, tightly structured with visible spiral steel boning "
        "and a sweetheart neckline trimmed in scalloped lace edging, gold hook-and-eye front busk "
        "closure; a matching thong brief in ivory champagne vinyl with the same laser-cut lace "
        "pattern at the waistband; an attached suspender belt with four gold metal garter clips; "
        "full-length sheer ivory seamed stockings with a straight back seam from heel to thigh; "
        "a small dusty-rose satin bow pinned at the center busk as the signature pink accent; "
        "(13cm ivory champagne patent platform pump, closed pointed toe, secured slingback strap, "
        "razor-thin metal needle heel, gold heel cap:1.3); long almond-shaped nails in champagne "
        "pearl polish."
    ),
    63: (
        "a La Perla-inspired dusty rose sheer lace slip dress, gloss-finish laser-cut "
        "lace-pattern vinyl mesh falling to mid-thigh in a bias-cut silhouette, thin adjustable "
        "straps, a plunging cowl neckline, the sheer fabric revealing a matching dusty rose "
        "longline bra and thong beneath from every angle; the bra with sheer ivory lace-pattern "
        "inset cups, structured underwire and a sweetheart neckline; the thong with the same "
        "lace-pattern trim at the waistband; a dusty rose suspender belt with four pearl-tipped "
        "garter clips glimpsed through the slip; full-length sheer blush seamed stockings with a "
        "straight back seam from heel to thigh; a small ivory pearl drop pinned at the center bra "
        "bridge; (14cm dusty rose patent platform ankle-strap pump, sharp pointed toe, ankle "
        "strap with rose-gold buckle, razor-thin metal needle heel, rose-gold heel cap:1.3); "
        "long stiletto-shaped nails in dusty rose polish."
    ),
    64: (
        "a Honey Birdette-inspired architectural fashion-bondage harness in electric magenta "
        "elastic strapping with polished chrome ring hardware fixed at the sternum, underbust "
        "and hip points, the straps framing the augmented bust without covering it, no fabric "
        "base beneath; a matching micro g-string in electric magenta elastic with a single chrome "
        "O-ring centered at the front waist; a fine chrome collar with a center O-ring; (8-inch "
        "electric magenta chrome platform thigh-high boot, over-the-knee rising to mid-thigh, "
        "side chrome zip closure, razor-thin metal needle heel, pointed toe, mirror-chrome "
        "sole:1.3); long coffin-shaped nails in glossy magenta chrome polish."
    ),
    65: (
        "a La Perla-inspired delicate triangle top in soft mint wet-satin latex with sheer ivory "
        "lace-pattern vinyl overlay, gloss finish, a thin gold underwire trim and dainty gold "
        "link straps; a matching mint micro g-string with ivory lace-pattern trim at the hips; "
        "a thin gold body chain draped from the sternum to the hip; a tiny dusty-rose satin bow "
        "pinned at the center of the triangle top as the signature pink accent; (12cm mint ivory "
        "patent platform pump, closed round-pointed toe, ankle strap with gold buckle, razor-thin "
        "metal needle heel, pearl heel cap:1.3); long almond-shaped nails in mint pearl polish."
    ),
}

SETTING = {
    61: ("A mirrored backstage dressing room with a brushed steel garment rail, exposed vanity "
         "bulbs framing a full-length floor mirror, black lacquer flooring, cool directional light"),
    62: ("A Parisian-inspired boudoir suite with a cream velvet chaise longue, an antique "
         "gilt-framed mirror, sheer ivory drapery at the window, soft golden lamplight"),
    63: ("A blush marble powder room with a round vanity mirror ringed in warm bulbs, fresh "
         "peonies in a crystal vase, travertine walls, soft diffused morning light"),
    64: ("A private club VIP alcove with a black leather-effect banquette, a low smoked-glass "
         "table, magenta neon strip lighting along the ceiling edge, dark mirrored walls"),
    65: ("A private thermal spa suite with a sunken stone soaking tub, soft steam haze in the "
         "air, backlit alabaster wall panels, warm amber ambient light"),
}

PROPS = {
    61: {"seat": "the dressing room bench", "wall": "the dressing room wall",
         "surface": "the vanity counter", "upright": "the floor mirror frame"},
    62: {"seat": "the cream velvet chaise longue", "wall": "the boudoir wall",
         "surface": "the chaise longue cushion", "upright": "the gilt-framed mirror"},
    63: {"seat": "the vanity stool", "wall": "the powder room wall",
         "surface": "the marble vanity counter", "upright": "the round vanity mirror"},
    64: {"seat": "the leather-effect banquette", "wall": "the alcove mirrored wall",
         "surface": "the smoked-glass table", "upright": "the mirrored wall panel"},
    65: {"seat": "the edge of the stone soaking tub", "wall": "the alabaster panel wall",
         "surface": "the tub's stone ledge", "upright": "the alabaster panel"},
}

TITULO = {
    61: "Gunmetal Cage Bodysuit",
    62: "Ivory Champagne Lace Corset",
    63: "Dusty Rose Lace Boudoir",
    64: "Electric Magenta Chrome Harness",
    65: "Mint Ivory Lace Triangle",
}

TAGS = {
    61: "#bikinilenceria #gunmetal #honeybirdette #cage #missdoll #batchL61-L65 #V7poses",
    62: "#bikinilenceria #ivorychampagne #laperla #corseteria #missdoll #batchL61-L65 #V7poses",
    63: "#bikinilenceria #dustyrose #laperla #lenceria #missdoll #batchL61-L65 #V7poses",
    64: "#bikinilenceria #magenta #honeybirdette #arnes #missdoll #batchL61-L65 #V7poses",
    65: "#bikinilenceria #mint #laperla #triangle #missdoll #batchL61-L65 #V7poses",
}

CONCEPTO = {
    61: ("Paso 0 contra Look 60: arnes M5 recien usado -> esta vez bodysuit M1 con cutouts de "
         "cage y hardware (arquitectura distinta, ventana global de 3 looks respetada); contra "
         "Look 57: turquesa/cromo dominante ya usado -> gunmetal + midnight navy con acento "
         "hot pink. Honey Birdette architectural cage sobre segunda piel."),
    62: ("Paso 0 contra Look 54: corseteria M4 en oxblood ya usada -> esta vez ivory champagne "
         "lace-pattern (gap de 8 looks, ventana global respetada); contra Look 58: lavanda ya "
         "usado -> champagne/oro. La Perla aristocratica italiana, encaje laser-cut sobre "
         "boning visible."),
    63: ("Paso 0 contra Look 58: conjunto de lenceria M3 en lavanda ya usado -> esta vez slip "
         "dress transparente M10 (cubierta) en dusty rose sobre sujetador+tanga+liguero+medias "
         "a juego -- la tela es sheer y deja leer la lenceria completa, no tapa el morbo; paga "
         "ademas la cuota de silueta cubierta de §8 (0/4 en la ventana L60-L63 sin este fix); "
         "contra Look 54/37: oxblood y bubblegum ya usados en esta categoria -> dusty rose "
         "satisface la firma rosa sin repetir ninguno de los dos. La Perla en su registro mas "
         "clasico: el slip de seda-y-encaje que dejo su firma aristocratica."),
    64: ("Paso 0 contra Look 60: arnes M5 en negro cromado ya usado -> esta vez electric "
         "magenta con cromo (gap de 4 looks, ventana global recien habilitada); contra Look 57: "
         "cromo turquesa ya usado -> cromo sobre magenta, paleta distinta. Bota thigh-high en "
         "vez de sandalia, rompe tambien el calzado repetido."),
    65: ("Paso 0 contra Look 57: bikini M2 turquesa-cromo-oro rosa ya usado en esta categoria -> "
         "esta vez mint-ivory con oro (gap de 8 looks, ventana global respetada); contra Look 63 "
         "de este mismo batch, ya M10 (slip dress) -> aqui vuelve a M2 (triangle top + tanga), "
         "sin repetir arquitectura dentro de la ventana de 3; contra Look 37 bubblegum -> paleta "
         "menta fresca, acento rosa via lazo dusty-rose puntual. La Perla en clave triangle "
         "delicada, no cage."),
}

SLOTS       = ["standing", "back_view", "seated", "side_profile", "glacial_command", "pov", "odalisque"]
SLOT_LABELS = ["Standing", "Back View", "Seated", "Side Profile", "Glacial Command", "POV", "Odalisque"]
FECHA = "28/08/2026"
BATCH_TEMA = 'batch L61-L65 "La Perla y Honey Birdette Lenceria"'
CATEGORIA = "\U0001F459 Bikini / Lencería Erótica"

out = []
for look_n in [61, 62, 63, 64, 65]:
    titulo = TITULO[look_n]
    slug_titulo = slugify(titulo)
    eyeshadow, lip_color = MAQUILLAJE[look_n]
    bloque_a = BLOQUE_A_BASE.replace(
        "intense shimmer smokey eye technique", eyeshadow
    ).replace(
        "high-gloss wet lips", "high-gloss wet %s lips" % lip_color
    )
    bloque_b = BLOQUE_B[look_n]
    neg_base_look = NEG_SIN_CORSET if look_n == 62 else NEG_BASE

    out.append(f"## \U0001f485 Look {look_n}: {titulo} ({FECHA} · {BATCH_TEMA} · {CATEGORIA})")
    out.append(f"- **Ubicacion:** `05_Imagenes/miss_doll/look{look_n}_{slug_titulo}/`")
    out.append(f"- **Tags:** {TAGS[look_n]}")
    out.append("")
    out.append(f"**Concepto:** {CONCEPTO[look_n]}")
    out.append("")
    out.append("**BLOQUE B (outfit -- copiado textual e identico en los 7 prompts):**")
    out.append("```text")
    out.append(bloque_b)
    out.append("```")
    out.append("")
    out.append("### \U0001f4f8 Imágenes (0/7 — Pendiente)")
    out.append("")
    out.append("| Standing | Back View | Seated | Side Profile | Glacial Command | POV | Odalisque |")
    out.append("| :---: | :---: | :---: | :---: | :---: | :---: | :---: |")
    out.append("| ⏳ Pendiente | ⏳ Pendiente | ⏳ Pendiente | ⏳ Pendiente | ⏳ Pendiente | ⏳ Pendiente | ⏳ Pendiente |")
    out.append("")

    props = PROPS[look_n]
    for i, (slot, label) in enumerate(zip(SLOTS, SLOT_LABELS)):
        extra_anclas = None
        if slot == "odalisque":
            extra_anclas = [pb.orientacion_odalisque(look_n)]
        pose_text = pb.pose(slot, look_n, props=props)
        prompt = pb.build(bloque_a, bloque_b, slot, pose_text, SETTING[look_n], extra_anclas=extra_anclas)
        out.append(f"### {i+1}. {label}")
        out.append("```text")
        out.append(prompt)
        out.append("```")
        out.append("")

    neg = pb.build_negative(neg_base_look)
    out.append(f"**Negative Prompt:** `{neg}`")
    out.append("")
    out.append("---")
    out.append("")

result = "\n".join(out)
outpath = pathlib.Path(__file__).parent / "output_missdoll_61_65.md"
outpath.write_text(result, encoding="utf-8")
print(f"OK -- output escrito en {outpath}")
print(f"Prompts generados: {len([x for x in out if x.startswith('### ') and '. ' in x])}")
print(f"Total lineas: {len(out)}")
