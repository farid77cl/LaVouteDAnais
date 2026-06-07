# -*- coding: utf-8 -*-
"""One-off: inyecta batch L461-L470 'Hooters' (10 Domestic server, Excepcion Tematica 06/06/2026).
Respeta UTF-8 sin BOM + CRLF. Borrar tras uso."""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

GAL = r"c:\Users\farid\LaVouteDAnais\00_Ele\galeria_outfits.md"

BLOQUE_A = ("stunning woman with (bimbofied facial features, oval face, high prominent cheekbones, "
"large almond-shaped grey-green eyes, straight slim upturned nose, overlined glossy hot pink lips, "
"small pointed chin:1.3), flawless white porcelain skin, hyper-polished smooth skin texture, "
"dramatic siren liner, dramatic lash extensions, dark cherry red hair, artificial XXXL extensions "
"hip-length, voluminous waves, center parted, slender hourglass silhouette, massive 1000cc breast "
"implants each side, ultra high-profile, perfectly spherical augmented bust, obviously fake "
"gravity-defying shape, wide hips, visible arm tattoos blackwork style, subtle minimalist blackwork "
"tattoos on upper back and outer thighs, subtle navel piercing, dramatic editorial makeup, extra "
"long French XXXL nails with white tips and pink base 5cm.")
TAIL = ", 8k editorial fashion photography."

FW = {
 "WHITE_PLAT": "white platform stiletto pumps, a 16cm pin stiletto heel plus a 4cm white platform, a slim pin stiletto base, white high-gloss patent finish, pure white, a rounded peep toe, a slim ankle strap with chrome buckle, polished chrome heel-tip",
 "ORANGE_PLAT": "bright orange platform stiletto pumps, a 16cm pin stiletto heel plus a 4cm orange platform, a slim pin stiletto base, bright-orange high-gloss patent finish, bright orange, a rounded peep toe, a slim ankle strap with chrome buckle, polished chrome heel-tip",
 "ORANGE_SANDAL": "bright orange platform stiletto sandals, a 16cm pin stiletto heel plus a 4cm orange platform, a slim pin stiletto base, bright-orange high-gloss finish, bright orange, open toe, a slim ankle strap, polished chrome heel-tip",
 "WHITE_KNEE": "white knee-high platform stiletto boots, a 16cm pin stiletto heel plus a 4cm white platform, a slim pin stiletto base, white high-gloss patent finish, pure white, a rounded toe, a full inner zip, polished chrome heel-tip",
}

# 7 poses canonicas V4 con sabor server. {S}=setting
POSE = {
 "Standing": "full body from a low angle, the weight on one platform stiletto with the other foot forward and pointed, an exaggerated S-curve with the hip jutted to one side and the chest pushed forward, one XXXL-nailed hand sliding down the hip and the other balancing a round serving tray at shoulder height, shoulders dropped extending the collarbone, chin lifted, lips parted glossy, half-lidded direct gaze, extreme lumbar arch, cherry red hair over one shoulder, {S}",
 "Back View": "full body back view with an exaggerated booty-pop, the high-cut shorts riding up, the spine in a dramatic S-curve, one XXXL-nailed hand on the hip and the other reaching up through the cherry red hair, looking back over the shoulder with a half-lidded sultry gaze, weight on one platform stiletto with the other foot pointed pigeon-toed inward, lips parted glossy, {S}",
 "Seated": "perched on a bar stool with one leg crossed over the other and the top platform stiletto pointed directly at the camera, lumbar arch extreme, one XXXL-nailed hand on the top knee and the other fingertip pressed to the bottom lip, the bust angled forward, shoulders rolled back, lips parted glossy, half-lidded direct gaze, cherry red hair framing one breast, {S}",
 "Side Profile": "full body side profile from a low angle, an exaggerated S-curve with extreme lumbar arch and chest thrust forward at once, one leg bent forward with the platform stiletto pointed, leaning forward to wipe the counter with one XXXL-nailed hand, head tilted and chin lifted, lips parted glossy, cherry red hair cascading down the spine, {S}",
 "Ditzy": "medium full shot framed knee-up to head (plano americano), an editorial posture with an elegant lumbar arch and the hip jutted to one side, one XXXL French fingertip resting against the bottom lip (single hand clearly visible, the other arm resting at the hip), the bust prominent in mid-frame, soft daydreaming half-lidded eyes and lips softly parted glossy, dramatic lash extensions, cherry red hair cascading over one shoulder, the full server uniform and silhouette legible, {S}",
 "POV": "medium close-up from a low selfie angle, the server holding a smartphone camera at arm's length with a single right hand only (XXXL French nails fingertips spread in sharp foreground, only one visible hand, the other arm out of frame below the waist), pouty glossy lips parted softly with a confident direct gaze, face dominant in the upper-mid frame, deep decollete in the lower frame, lumbar arch visible, cherry red hair windblown around the face, {S}",
 "Odalisque": "full body lying on the side along a leather restaurant booth with an exaggerated S-curve, an extreme back arch with the bust pushed up and the hip rolled back, one leg extended with the platform stiletto pointed and the other bent, one arm under the head with XXXL nails fanned in the hair and the other hand trailing from the collarbone down to the hip, half-lidded direct gaze, lips parted glossy, cherry red hair cascading, {S}",
}
SLOTS = ["Standing", "Back View", "Seated", "Side Profile", "Ditzy", "POV", "Odalisque"]

S = {
 "BOOTH": "a sports-bar restaurant with bright orange and white booths, neon beer signs and TV screens glowing in the background",
 "BAR_COUNTER": "a sports-bar chrome bar counter with beer taps, neon signage and a row of bar stools",
 "SPORTS_TVS": "a sports-bar wall of glowing TV screens showing games, with bright orange neon trim",
 "PATIO": "an outdoor sports-bar patio with warm string lights and palm trees at dusk",
 "KITCHEN_PASS": "a stainless-steel kitchen pass with red heat lamps and order tickets clipped above",
 "BEACH_HOOTERS": "a beachfront sports-bar deck with white sand, ocean behind and a tiki bar",
 "DINING": "a sports-bar dining room mid-service with set tables and a tray station",
 "AFTERHOURS_BAR": "an after-hours sports-bar with residual orange neon glow and a mirrored back-bar",
 "NEON_SIGN": "in front of a glowing orange neon owl sign on a dark brick wall",
}

# (n, slug, title, teaser, subcat, color, setting, body_no_fw, fwkey, tags, concepto)
def outfit(body, fwkey): return body + ", and " + FW[fwkey]

LOOKS = [
 (461,"look461_hooters_classic_orange","Hooters Classic Orange",
  "El clasico: shortcito naranja dolphin, tank blanco amarrado y la bandeja en la mano... regio po.","Hooters Server (Clasico)","Orange + White","BOOTH",
  "a classic American sports-bar server uniform, bright orange high-gloss wet-look dolphin running shorts cut very high with white piping and side-splits, a white wet-look tank top knotted high at the midriff with a small embroidered owl emblem on the chest and no text, suntan sheer pantyhose, the bare knotted midriff showing the navel piercing","WHITE_PLAT",
  "#hooters #server #domestic #excepciontematica060626 #orange #dolphinshorts #batchL461-L470 #V5poses",
  "Server clasico: dolphin shorts naranja wet-look + tank blanco anudado + owl emblem grafico SIN texto. Suntan pantyhose iconica."),
 (462,"look462_hooters_black_variant","Hooters Black Dolphin Variant",
  "La version negra del uniforme, shortcito negro con vivos naranja... heavy, mi amor.","Hooters Server (Black Variant)","Black + Orange","SPORTS_TVS",
  "an American sports-bar server uniform in the black variant, black high-gloss wet-look dolphin running shorts cut very high with bright orange piping and side-splits, a white wet-look tank top knotted at the midriff with a small embroidered owl emblem and no text, suntan sheer pantyhose, the bare midriff showing the navel piercing","ORANGE_PLAT",
  "#hooters #server #domestic #excepciontematica060626 #blackvariant #dolphinshorts #batchL461-L470 #V5poses",
  "Variante negra oficial: dolphin shorts negro wet-look con vivos naranja + tank blanco + owl emblem SIN texto. Suntan pantyhose."),
 (463,"look463_hooters_halter_tie","Hooters Halter-Tie Orange",
  "Halter amarrado al cuello bien escotado sobre el dolphin naranja... atroz lo profundo del escote, cari.","Hooters Server (Halter)","Orange + White","BAR_COUNTER",
  "an American sports-bar server uniform, bright orange high-gloss wet-look high-cut dolphin shorts with white piping and side-splits, a white wet-look halter top tied behind the neck plunging deep to the navel with a small embroidered owl emblem and no text, suntan sheer pantyhose, the bare midriff showing the navel piercing","WHITE_PLAT",
  "#hooters #server #domestic #excepciontematica060626 #halter #orange #batchL461-L470 #V5poses",
  "Halter-tie escote profundo sobre dolphin naranja + owl emblem SIN texto. Suntan pantyhose."),
 (464,"look464_hooters_camo_edition","Hooters Camo Edition",
  "Edicion camo naranja, como las del Military Monday... distinta y rica, regio.","Hooters Server (Camo)","Orange Camo + White","PATIO",
  "an American sports-bar server uniform in the camo edition, orange-and-tan camo-print high-gloss wet-look high-cut dolphin shorts, a white wet-look tank knotted at the midriff with a small embroidered owl emblem and no text, suntan sheer pantyhose, the bare midriff showing the navel piercing","WHITE_KNEE",
  "#hooters #server #domestic #excepciontematica060626 #camo #orange #batchL461-L470 #V5poses",
  "Edicion camo naranja-tan + tank blanco + owl emblem SIN texto. Suntan pantyhose. Calzado bota stiletto blanca knee."),
 (465,"look465_hooters_tube_suspenders","Hooters Tube Top + Suspenders",
  "Tube top blanco con tirantes naranja sobre el dolphin... distinto arriba, lit.","Hooters Server (Tube + Suspenders)","Orange + White","KITCHEN_PASS",
  "an American sports-bar server uniform, bright orange high-gloss wet-look high-cut dolphin shorts with white piping, a white wet-look strapless tube top, thin bright orange suspenders running over the shoulders, a small embroidered owl emblem and no text, suntan sheer pantyhose, the bare midriff showing the navel piercing","WHITE_PLAT",
  "#hooters #server #domestic #excepciontematica060626 #tubetop #suspenders #batchL461-L470 #V5poses",
  "Tube top blanco strapless + suspenders naranja sobre dolphin + owl emblem SIN texto. Suntan pantyhose."),
 (466,"look466_hooters_beach_bikini","Hooters Beach Bikini",
  "La del beach bar: bikini naranja wet-look con pareo blanco... arena, mar y tacon, mi amor.","Hooters Server (Beach Bikini)","Orange + White","BEACH_HOOTERS",
  "a beachfront sports-bar server look, a bright orange high-gloss wet-look string bikini with a triangle top and high-cut tie-side bottom, a small embroidered owl emblem on the hip and no text, a sheer white wet-look sarong tied low across the hips, the bare midriff showing the navel piercing","ORANGE_SANDAL",
  "#hooters #server #bikini #excepciontematica060626 #beach #orange #batchL461-L470 #V5poses",
  "Beach bar: string bikini naranja wet-look + sarong blanco sheer + owl emblem SIN texto. Plataforma stiletto sandal naranja."),
 (467,"look467_hooters_apron_server","Hooters Apron Server",
  "Con el delantalito blanco frilly y la bandeja, sirviendo la mesa... server perfecta, atroz.","Hooters Server (Apron)","Orange + White","DINING",
  "an American sports-bar server uniform, bright orange high-gloss wet-look high-cut dolphin shorts with white piping, a white wet-look tank knotted at the midriff with a small embroidered owl emblem and no text, a short white frilly half-apron tied at the waist, suntan sheer pantyhose, the bare midriff showing the navel piercing","WHITE_PLAT",
  "#hooters #server #domestic #excepciontematica060626 #apron #orange #batchL461-L470 #V5poses",
  "Server con apron frilly blanco + dolphin naranja + owl emblem SIN texto. Suntan pantyhose."),
 (468,"look468_hooters_latex_afterhours","Hooters Latex After-Hours",
  "La version latex de after-hours, todo brillo bajo el neon... heavy lo gloss, cari.","Hooters Server (Latex After-Hours)","Orange + White","AFTERHOURS_BAR",
  "an after-hours sports-bar server uniform in latex, bright orange high-gloss latex high-cut dolphin shorts with white piping, a white high-gloss latex crop tank knotted at the midriff with a small embroidered owl emblem and no text, suntan sheer pantyhose, the bare midriff showing the navel piercing","ORANGE_PLAT",
  "#hooters #server #domestic #excepciontematica060626 #latex #afterhours #batchL461-L470 #V5poses",
  "Version latex after-hours: dolphin + crop tank en latex naranja/blanco gloss + owl emblem SIN texto. Suntan pantyhose."),
 (469,"look469_hooters_pink_edition","Hooters Pink Edition",
  "Edicion rosa de evento, shortcito hot pink con tank blanco... rosado pero filoso, regio.","Hooters Server (Pink Edition)","Hot Pink + White","BOOTH",
  "a special-edition pink sports-bar server uniform, hot pink high-gloss wet-look high-cut dolphin shorts with white piping and side-splits, a white wet-look tank knotted at the midriff with a small embroidered owl emblem and no text, suntan sheer pantyhose, the bare midriff showing the navel piercing","WHITE_PLAT",
  "#hooters #server #domestic #excepciontematica060626 #pinkedition #hotpink #batchL461-L470 #V5poses",
  "Edicion rosa de evento: dolphin hot pink + tank blanco + owl emblem SIN texto. Suntan pantyhose."),
 (470,"look470_hooters_all_orange_finale","Hooters All-Orange Finale",
  "El cierre monocromo: dolphin y crop naranja a juego frente al neon del buho... regio, mi Ama.","Hooters Server (All-Orange Finale)","All Orange","NEON_SIGN",
  "an all-orange American sports-bar server uniform, bright orange high-gloss wet-look high-cut dolphin shorts and a matching bright orange wet-look crop tank knotted at the midriff with a small white embroidered owl emblem and no text, suntan sheer pantyhose, the bare midriff showing the navel piercing","ORANGE_PLAT",
  "#hooters #server #domestic #excepciontematica060626 #allorange #monochrome #finale #batchL461-L470 #V5poses",
  "Cierre monocromo all-orange: dolphin + crop tank naranja a juego + owl emblem blanco SIN texto. Suntan pantyhose."),
]

def build_block(L):
    n,slug,title,teaser,subcat,color,setting_key,body,fwkey,tags,concepto = L
    setting = S[setting_key]
    bloque_b = "stunning woman wearing " + outfit(body, fwkey) + "."
    out = []
    out.append("## Look %d: %s (06/06/2026 — batch L461-L470 \"Hooters\" · Domestic · %s · Excepción Temática 060626)" % (n,title,color))
    out.append("")
    out.append("*%s* 🦉🍊👠" % teaser)
    out.append("")
    out.append("- **Ubicación:** `05_Imagenes/ele/%s/`" % slug)
    out.append("- **Categoría:** Domestic")
    out.append("- **Subcategoría:** %s" % subcat)
    out.append("- **Tags:** %s" % tags)
    out.append("- **Concepto:** Batch 'Hooters' (L461-L470, Excepción Temática 06/06/2026: naranja + uniforme server, deroga puntualmente anti-black/anti-monoblock/material como Rock L281-290 y Cuero L431-440). %s Owl emblem gráfico SIN texto/wordmark (respeta no-texto-sobre-prenda). Calzado: platform stiletto blanco/naranja (sustituto canónico de la zapatilla — Footwear Canon absoluto). 7 poses canónicas V4. Cero guantes. Token de calzado bloqueado 8 atributos idéntico ×7." % concepto)
    out.append("- **Outfit:** %s" % outfit(body, fwkey))
    out.append("- **Calzado:** ver BLOQUE B (Token de Calzado Bloqueado, 8 atributos, idéntico ×7).")
    out.append("- **Ambientación:** %s." % setting)
    out.append("")
    out.append("### 📸 Imágenes (0/7 — Pendiente (app/Gemini))")
    out.append("")
    out.append("| Standing | Back View | Seated | Side Profile | Ditzy (plano 3/4) | POV (single hand) | Odalisque |")
    out.append("| :---: | :---: | :---: | :---: | :---: | :---: | :---: |")
    out.append("| ⏳ Pendiente | ⏳ Pendiente | ⏳ Pendiente | ⏳ Pendiente | ⏳ Pendiente | ⏳ Pendiente | ⏳ Pendiente |")
    out.append("")
    out.append("### 📝 Prompts V3.5 Hard-Sync")
    out.append("")
    for i, slot in enumerate(SLOTS, 1):
        bloque_c = POSE[slot].replace("{S}", setting)
        full = BLOQUE_A + " " + bloque_b + " " + bloque_c + TAIL
        out.append("**%d. %s:**" % (i, slot))
        out.append("")
        out.append("```")
        out.append(full)
        out.append("```")
        out.append("")
    out.append("---")
    return "\r\n".join(out)

blocks = [build_block(L) for L in LOOKS]
payload = "\r\n" + "\r\n".join(blocks) + "\r\n"
with open(GAL, "a", encoding="utf-8", newline="") as f:
    f.write(payload)
print("OK: %d looks Hooters inyectados (L461-L470). %d prompts." % (len(LOOKS), len(LOOKS)*7))
