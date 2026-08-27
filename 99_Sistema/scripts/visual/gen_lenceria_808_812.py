"""
Script temporal: genera los 5 looks de Lencería L808-L812 (La Perla / Honey Birdette)
y los escribe en output_L808_L812.md listos para pegar en galeria_outfits.md.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from prompt_builder import PromptBuilder

pb = PromptBuilder("ele")

BLOQUE_A = (
    "stunning woman with (bimbofied facial features, oval face, high prominent cheekbones, "
    "large almond-shaped grey-green eyes, straight slim upturned nose, overlined glossy hot pink lips, "
    "small pointed chin:1.3), flawless white porcelain skin, hyper-polished smooth skin texture, "
    "dramatic siren liner, dramatic lash extensions, dark cherry red hair, artificial XXXL extensions "
    "hip-length, voluminous waves, center parted, slender hourglass silhouette, massive 1000cc breast "
    "implants each side, ultra high-profile, perfectly spherical augmented bust, obviously fake "
    "gravity-defying shape, wide hips, blackwork arm tattoos shown only on bare uncovered skin, "
    "subtle minimalist blackwork tattoos on upper back and outer thighs, delicate blackwork rune-glyph "
    "identity tattoo of abstract esoteric calligraphic symbols along one hip crease and bikini line, "
    "navel piercing, nipple piercings, every tattoo and piercing visible ONLY on genuinely bare skin "
    "and never through or over any garment, aggressive bimbomakeup, extra long French XXXL nails "
    "with white tips and pink base 5cm"
)

BLOQUE_B = {
    808: (
        "a La Perla aristocratic four-piece set: longline balconette bra in deep noir vinyl laser-cut "
        "lace-pattern with opaque molded underwire cups and a sweetheart neckline, thin vinyl spaghetti "
        "straps, hook-and-eye front center, the lace-cut panels revealing small geometric windows of skin "
        "at the underbust and sides; matching thong brief in noir vinyl with a laser-cut lace waistband; "
        "a noir vinyl suspender belt with six metal garter clips; full-length seamed black stockings with "
        "a straight back seam from heel to thigh; pointed-toe stiletto pumps in mirror-black patent, "
        "13cm thin pin stiletto heel, sharp pointed toe, slingback strap, polished chrome heel cap. "
        "La Perla aristocratic Italian poise."
    ),
    809: (
        "a Honey Birdette architectural cage-bra set: a structured chrome silver vinyl cage bra with "
        "four rigid horizontal bands crossing the chest and a center front ring hardware closure, fully "
        "exposing the underbust and ribcage; a matching micro-G-string in chrome silver vinyl with a "
        "single O-ring on each hip; chrome silver platform stiletto sandals, 8-inch thin pin stiletto "
        "heel plus 4-inch chrome platform, sharp pointed toe, ankle strap with chrome buckle, "
        "mirror-chrome sole. Bordelle architectural strapping discipline, cage geometry deliberate."
    ),
    810: (
        "an Agent Provocateur parisian corselette in deep wine latex: a single-piece longline basque "
        "with boned structure, a deep plunging sweetheart neckline, opaque wine latex panels at the bust "
        "and hip, sheer PVC crystal-mesh inset panels running vertically from underbust to hip on both "
        "sides, four dangling wine vinyl garter clips front and back, a wine latex thong back; full-length "
        "nude seamed stockings with a classic straight back seam; ankle-strap stiletto pumps in deep wine "
        "patent, 14cm thin pin stiletto heel, sharp pointed toe, ankle strap with gold buckle, "
        "gold heel cap. Agent Provocateur parisian confidence."
    ),
    811: (
        "a Bordelle multi-piece architectural harness set: a triangulated torso harness in nude flesh "
        "latex elastic strapping with gold metal ring hardware at the sternum, under-bust, and hip points, "
        "the straps framing the augmented bust without covering it; a matching micro-G-string in nude "
        "flesh latex with a single gold O-ring centered at the front waist; matching thigh harness bands "
        "in nude flesh elastic on each outer thigh secured with gold ring hardware; clear transparent "
        "acrylic platform stiletto sandals, 8-inch thin pin stiletto heel plus 4-inch clear platform, "
        "open toe, ankle strap with gold buckle, crystal-free clear sole. Atsuko Kudo latex couture "
        "authority, the harness IS the garment."
    ),
    812: (
        "a Honey Birdette Whisper-range babydoll set: a structured molded bra in blush rose wet-satin "
        "latex with opaque underwire cups and a lightly ruffled sweetheart neckline, thin spaghetti "
        "straps; a sheer PVC blush-pink overlay babydoll skirt falling to mid-thigh with a straight "
        "cut, open-front drape revealing the hips; a matching blush rose latex micro-thong with a narrow "
        "vinyl waistband; pointed-toe mule stiletto sandals in blush rose patent, 12cm thin pin stiletto "
        "heel, pointed almond toe, slide-on no strap, chrome heel cap. "
        "Honey Birdette boudoir refinement, soft intimacy luxurious."
    ),
}

SETTING = {
    808: ("Suite hotel lujo Paris with a velvet chaise longue, antique vanity mirror, fresh white orchids, "
          "and a champagne glass on the side table, warm amber candlelight"),
    809: ("Floor-to-ceiling mirror studio with directional spotlight from the left, minimal black floor, "
          "hard shadows, Helmut Newton noir editorial lighting"),
    810: ("Parisian boudoir vanity room with a triple-mirror 1920s vanity, crystal perfume bottles, "
          "a velvet tufted chair, warm golden side lighting"),
    811: ("Atsuko Kudo atelier studio with latex sheets hanging from the ceiling, mannequins in harness "
          "poses in the background, clinical white walls, directional hard studio light"),
    812: ("King bed with blush-champagne satin sheets and silk pillows, soft diffused morning window light, "
          "white sheer curtains, fresh pink peonies on the nightstand"),
}

PROPS = {
    808: {"seat": "the velvet chaise longue", "wall": "the suite wall",
          "surface": "the chaise longue cushion", "upright": "the vanity mirror frame"},
    809: {"seat": "the studio floor", "wall": "the mirror wall",
          "surface": "the studio floor", "upright": "the studio mirror frame"},
    810: {"seat": "the velvet tufted chair", "wall": "the boudoir wall",
          "surface": "the vanity stool", "upright": "the vanity mirror"},
    811: {"seat": "the studio floor", "wall": "the atelier wall",
          "surface": "the studio floor", "upright": "the latex-draped studio pole"},
    812: {"seat": "the satin bed", "wall": "the bedroom wall",
          "surface": "the satin sheets", "upright": "the headboard"},
}

META = {
    808: ("Noir Lace La Perla Suite",     "LA1", "A Boudoir"),
    809: ("Chrome Cage Couture HB",       "LB2", "B Fetish"),
    810: ("Deep Wine AP Corselette",      "LA2", "A Boudoir"),
    811: ("Nude Bordelle Harness Atelier","LB5", "B Fetish"),
    812: ("Blush Whisper Babydoll",       "LA4", "A Boudoir"),
}

SLOTS       = ["standing","back_view","seated","side_profile","Ditzy","pov","odalisque"]
SLOT_LABELS = ["Standing","Back View","Seated","Side Profile","Ditzy","POV","Odalisque"]
NEG_LENCERIA = (
    "cotton lingerie, organic fabric, sleepwear pajamas, granny nightgown, modest robe, "
    "bridal innocent virginal, ingenue, daywear, swimwear context, beach setting"
)

out = []
for look_n in [808, 809, 810, 811, 812]:
    titulo, codigo, polo = META[look_n]
    slug_titulo = titulo.lower().replace(" ", "_")
    out.append(
        f"## \U0001f457 Look {look_n}: {titulo} "
        f"(27/08/2026 \u00b7 batch 808-812 \"La Perla y HB Lencer\u00eda\" "
        f"\u00b7 Lencer\u00eda \u00b7 {codigo} {polo})"
    )
    out.append("")
    out.append(f"- **Ubicacion:** `05_Imagenes/ele/look{look_n}_{slug_titulo}/`")
    out.append(
        f"- **Tags:** #lenceria #{polo.replace(' ','_').lower()} #{codigo.lower()} "
        f"#laperla #honeybirdette #batchL808-L812 #V7poses"
    )
    out.append("")
    out.append("### \U0001f4f8 Im\u00e1genes (0/7 \u2014 Pendiente)")
    out.append("")
    out.append("| Standing | Back View | Seated | Side Profile | Ditzy | POV | Odalisque |")
    out.append("| :---: | :---: | :---: | :---: | :---: | :---: | :---: |")
    out.append("| \u23f3 Pendiente | \u23f3 Pendiente | \u23f3 Pendiente | \u23f3 Pendiente | \u23f3 Pendiente | \u23f3 Pendiente | \u23f3 Pendiente |")
    out.append("")
    props = PROPS[look_n]
    for i, (slot, label) in enumerate(zip(SLOTS, SLOT_LABELS)):
        pose   = pb.pose(slot, look_n, props=props)
        prompt = pb.build(BLOQUE_A, BLOQUE_B[look_n], slot, pose, SETTING[look_n])
        out.append(f"### {i+1}. {label}")
        out.append("```text")
        out.append(prompt)
        out.append("```")
        out.append("")
    neg = pb.build_negative(NEG_LENCERIA)
    out.append(f"**Negative Prompt:** `{neg}`")
    out.append("")
    out.append("---")
    out.append("")

result = "\n".join(out)
outpath = pathlib.Path(__file__).parent / "output_L808_L812.md"
outpath.write_text(result, encoding="utf-8")
print(f"OK — output escrito en {outpath}")
print(f"Prompts generados: {len([x for x in out if x.startswith('### ') and '. ' in x])}")
print(f"Total lineas: {len(out)}")
