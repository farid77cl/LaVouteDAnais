# -*- coding: utf-8 -*-
"""
Rotacion de poses V5 + chequeo de variedad de settings.

POR QUE EXISTE (Directiva Ama 08/06/2026): mis inyectores de batch hardcodeaban UNA
sola plantilla de 7 poses (St1/Bk1/Se1/...) en CADA look -> poses clonadas (Standing
identico x44, Back x83, etc.) + "mirrored room" como setting comodin (16/50 looks).
Este modulo materializa el Repertorio V5 (.agent/skills/ele-outfit-engine/references/
pose_repertoire_v5.md) como CODIGO reutilizable.

USO OBLIGATORIO en todo inyector de batch nuevo:
    from pose_rotation_v5 import rotate_poses, check_setting_variety
    poses = rotate_poses(look_number)         # -> lista de 7 (slot, pose_direction)
    # prompt = BLOQUE_A + " stunning woman wearing " + outfit + ", and " + heel + ". "
    #          + pose_direction + ", " + setting + ", 8k editorial fashion photography."
    check_setting_variety([lk["setting"] for lk in LOOKS])   # warn si se repite

Regla de rotacion: variante = (look_number + offset_slot) % len(variantes_slot).
Como cada slot tiene >=5 variantes y el paso es 1 por numero de look, NINGUNA
variante se repite dentro de 4 looks consecutivos del mismo slot, y los slots van
decorrelacionados (offsets distintos) para que un look no sea "todo St1/Bk1".
"""

# Todas las variantes mantienen el Principio Rector Fetish Model (lumbar arch, lips
# parted glossy, XXXL nail interaction, predatory/half-lidded gaze, hair como prop) y
# nombran el stiletto (footwear canon). NO incluyen setting: el inyector lo append.

STANDING = [
 "full body from a low angle below the hip, the weight on one stiletto with the other foot forward and pointed, an exaggerated S-curve with the hip jutted to one side and the chest pushed forward, one XXXL-nailed hand sliding down the hip and thigh and the other pulling at the neckline, shoulders dropped, chin lifted, half-lidded predatory gaze, cherry red hair over one shoulder",
 "full body from a low angle, caught mid-stride walking straight toward the camera with one stiletto forward and the back foot lifting off the floor, hips swinging, one XXXL-nailed hand on the hip and the other arm loose, head turned over the shoulder, fierce runway gaze, cherry red hair in motion",
 "full body, the shoulders propped against a wall with one knee bent and that stiletto sole flat against the wall, the pelvis pushed forward off the wall, one XXXL-nailed hand hooked in the waistband and the other trailing up the body, chin down looking up through the lashes, lips parted glossy, cherry red hair spilling against the wall",
 "full body from a low angle, both arms raised overhead gathering the cherry red hair off the neck, the torso elongated and the chest lifted high in an extreme lumbar arch, the weight on both stilettos with the hip cocked, the garment riding up, the face tilted up with half-lidded eyes, the side-body line exposed",
 "full body, the body turned three-quarters away with the ass partly toward the lens and the torso twisted back so the bust returns to camera, one XXXL-nailed hand on the far hip and the other lifting the hair at the nape, looking back over the shoulder with a predatory glance, a deep waist-to-hip twist, on towering stilettos",
 "full body, leaning forward from the hips toward the camera with both XXXL-nailed hands on her own knees, the augmented bust thrust forward creating deep cleavage dominant in frame, the back arched and the ass pushed out behind, looking up through the lashes with lips parted, cherry red hair falling forward framing the face, on stilettos",
 "full body, standing tall with the legs crossed at the knee in an elegant fashion-model X-stance, the weight balanced on both stilettos, one XXXL-nailed hand on the opposite hip and the other at the collarbone, the spine long with a subtle arch, chin tilted, half-lidded sultry gaze, cherry red hair over one shoulder",
 "full body from a low hero angle, the feet planted apart and firm on both stilettos, both XXXL-nailed hands on the hips, the shoulders pulled back and the chin dropped for a dominant direct stare down at the camera, a commanding lumbar arch, cherry red hair framing the face",
 "full body, one XXXL-nailed hand hooking the neckline and slipping it off the shoulder while the other rests low on the hip, the weight on one stiletto with a soft knee bend, looking down at the exposed shoulder, lips parted glossy, an intimate self-aware posture, cherry red hair pushed to one side",
]

BACK = [
 "full body back view with an exaggerated booty-pop, the spine in a dramatic S-curve, one XXXL-nailed hand on the hip and the other reaching up through the cherry red hair, looking back over the shoulder with a half-lidded sultry gaze, the weight on one stiletto with the other foot pigeon-toed inward, lips parted glossy",
 "full body back view caught mid-stride walking away from the camera with one stiletto lifting and the hips swinging, the torso twisting to glance back over the shoulder, one XXXL-nailed hand trailing down the lower back to the ass, cherry red hair down the spine",
 "full body back view bent forward at the hips with both XXXL-nailed hands flat on a surface, a deep back arch with the ass pushed up and out toward the camera, looking back over the shoulder through the cherry red hair, the weight on both stilettos",
 "full body back view standing with both XXXL-nailed hands lifting all the cherry red hair up off the nape, exposing the full back and spine line, the head dropped slightly forward, the weight on one hip with the stiletto cocked",
 "full body back view with the shoulder blades against a wall facing partly away, the ass off the wall and pushed out, one XXXL-nailed hand pressed on the wall behind, looking back to the camera over the shoulder, the weight on one stiletto",
 "full body back view with both XXXL-nailed hands sliding down over her own ass, a deep lumbar arch, the head thrown back, cherry red hair veiling the turned face, the weight on both stilettos pointed",
 "full body back view kneeling upright with the spine arched and sitting back toward the heels, one XXXL-nailed hand reaching up the back and the other in the hair, looking over the shoulder, the stilettos visible behind",
]

SEATED = [
 "perched on a sculptural seat with one leg crossed over the other and the top stiletto pointed at the camera, an extreme lumbar arch, one XXXL-nailed hand on the top knee and the other fingertip at the bottom lip, the bust angled forward, shoulders rolled back, half-lidded direct gaze, cherry red hair framing one breast",
 "perched on the edge of a seat leaning forward with the elbows on the knees, the deep cleavage thrust toward the camera, the top stilettos planted apart, one XXXL-nailed hand under the chin, looking up through the lashes with lips parted, cherry red hair falling forward",
 "reclined back on a seat propped on one elbow with the other XXXL-nailed hand trailing down the torso, the spine in a long arch, the legs extended with the stilettos crossed at the ankle and pointed, half-lidded predatory gaze, cherry red hair spilling over the backrest",
 "straddling a chair backwards with the arms crossed over the top of the backrest and the chin resting on the forearms, the back arched and the ass out, the stilettos planted wide, a sultry half-lidded gaze over the arms, cherry red hair over one shoulder",
 "seated on the floor with the knees up together and the stilettos planted, leaning back on both XXXL-nailed hands behind, the chest lifted in a lumbar arch, the chin raised, lips parted glossy, cherry red hair cascading down the back",
 "seated side-saddle with the legs together angled to one side and the top stiletto pointed, the torso twisted back to the camera, one XXXL-nailed hand on the upper thigh and the other at the collarbone, an extreme waist twist, half-lidded gaze, cherry red hair over one breast",
]

SIDE = [
 "full body side profile from a low angle, an exaggerated S-curve with an extreme lumbar arch and the chest thrust forward at once, one leg bent forward with the stiletto pointed, one XXXL-nailed hand sliding from the hip to the thigh, chin lifted, lips parted glossy, cherry red hair cascading down the spine",
 "side profile seated on a sculptural seat with the legs crossed and the top stiletto pointed away, the spine arched and the bust in profile silhouette, one XXXL-nailed hand on the thigh, the head tilted, lips parted, cherry red hair down the back",
 "side profile reclining on one side with an exaggerated S-curve, the hip rolled up and the bust pushed forward in silhouette, the legs stacked with the stilettos pointed, one XXXL-nailed hand on the hip, half-lidded gaze, cherry red hair pooling",
 "full body side profile caught mid-stride with one leg forward and the stiletto pointed, the hips swung and the chest forward, one XXXL-nailed hand swinging and the other on the hip, chin lifted in profile, cherry red hair streaming back",
 "side profile kneeling upright with the spine arched and the bust thrust forward in silhouette, sitting back toward the heels, one XXXL-nailed hand reaching up the body, the head tilted back, lips parted, cherry red hair down the arched back",
 "full body side profile bent forward at the hips with the ass pushed out behind in silhouette and the chest dropped forward, one XXXL-nailed hand on the bent knee, looking toward the camera, the stiletto pointed, cherry red hair falling forward",
 "side profile pressed to a wall with one XXXL-nailed hand raised high on the wall and the back deeply arched, the bust forward and the ass back in silhouette, one stiletto on tiptoe, lips parted, cherry red hair against the wall",
]

DITZY = [
 "medium full shot framed knee-up to head (plano americano), an elegant lumbar arch with the hip jutted to one side, one XXXL French fingertip resting against the bottom lip (single hand clearly visible, the other arm resting at the hip), the bust prominent in mid-frame, soft daydreaming half-lidded eyes, lips softly parted glossy, cherry red hair over one shoulder, the full outfit legible",
 "medium full shot framed knee-up to head (plano americano), an elegant lumbar arch with the hip cocked, one XXXL French fingertip twirling a lock of cherry red hair (single hand visible, the other arm at the hip), the bust prominent, soft daydreaming half-lidded eyes, lips softly parted glossy, the full outfit legible",
 "medium full shot framed knee-up to head (plano americano), an elegant lumbar arch with the hip jutted, looking down at her own shoulder with one XXXL fingertip touching the strap (single hand visible, the other arm at the hip), the bust prominent, soft half-lidded eyes, lips softly parted glossy, cherry red hair forward, the full outfit legible",
 "medium full shot framed knee-up to head (plano americano), an elegant lumbar arch with the hip cocked, XXXL fingertips held just in front of the glossy lips blowing a kiss to the camera (single hand visible, the other arm at the hip), the bust prominent, soft daydreaming half-lidded eyes, cherry red hair over one shoulder, the full outfit legible",
 "medium full shot framed knee-up to head (plano americano), the head tilted with one XXXL-nailed hand framing the cheekbone (single hand visible, the other arm at the hip), an elegant lumbar arch, the bust prominent, soft daydreaming half-lidded eyes, lips softly parted glossy, cherry red hair cascading, the full outfit legible",
 "medium full shot framed knee-up to head (plano americano), the head turned coyly over the shoulder with one XXXL fingertip at the bottom lip (single hand visible, the other arm at the hip), an elegant lumbar arch with the hip out, the bust prominent, soft half-lidded eyes, lips softly parted glossy, the full outfit legible",
]

POV = [
 "medium close-up from a low selfie angle, holding a smartphone at arm's length with a single right hand only (XXXL French nails spread in sharp foreground, only one visible hand, the other arm out of frame below the waist), pouty glossy lips parted, a confident direct gaze, the face dominant in the upper-mid frame, deep cleavage in the lower frame, lumbar arch visible, cherry red hair windblown",
 "medium close-up selfie from a low angle pointing up, holding the phone with a single right hand only (XXXL French nails in sharp foreground, only one visible hand, the other arm out of frame), the chin elevated and lips parted glossy, a half-lidded gaze down the lens, the bust dominant in the lower frame, cherry red hair falling forward",
 "medium close-up selfie at arm's length with a single right hand only (XXXL French nails in sharp foreground, only one visible hand, the other arm out of frame), the gaze directed away from the lens in a three-quarter face, lips parted glossy, the face in the upper-mid frame, deep cleavage below, cherry red hair around the face",
 "medium close-up selfie lying down with the arm extended up to the lens from above, a single right hand only (XXXL French nails in sharp foreground, only one visible hand, the other arm out of frame), looking up at the camera with parted glossy lips, the bust dominant in the lower frame, cherry red hair fanned on the surface",
 "medium close-up selfie at arm's length with a single right hand only (one XXXL French fingertip grazing the bottom lip, only one visible hand, the other arm out of frame), a direct sultry gaze to the lens, lips parted glossy, the face dominant in frame, deep cleavage below, cherry red hair windblown",
]

ODALISQUE = [
 "full body lying on the side with an exaggerated S-curve, an extreme back arch with the bust pushed up and the hip rolled back, one leg extended with the stiletto pointed and the other bent, one arm under the head with XXXL nails in the hair and the other trailing from the collarbone to the hip, half-lidded predatory gaze, cherry red hair cascading",
 "full body lying face-down propped on the forearms with the back deeply arched and the ass lifted, the stilettos crossed in the air behind, looking back over the shoulder at the camera, XXXL nails framing the face, lips parted glossy, cherry red hair spilling forward",
 "full body lying on the back in an extreme arch with one knee raised and the stiletto planted, the head dropping back toward the camera, the bust thrust up, both XXXL-nailed hands sliding up the torso, lips parted, cherry red hair pooling around the head",
 "full body semi-reclined propped on both elbows with the legs draped and one stiletto pointed at the camera, the bust forward and the spine arched, the chin lifted, a half-lidded predatory gaze, XXXL nails resting on the thigh, cherry red hair over one shoulder",
 "full body kneeling and leaning forward onto the forearms in a cat arch with the lower back hollowed and the ass lifted high, looking up at the camera through the lashes, XXXL nails splayed in front, lips parted glossy, the stilettos behind, cherry red hair falling around the face",
 "full body lying on the back with the legs raised and crossed in the air showing off the stilettos, propped on the elbows with the bust forward, looking down the body at the camera, XXXL nails on the raised thigh, lips parted glossy, cherry red hair fanned out",
]

# (slot_name, variantes, offset para decorrelacionar slots)
SLOTS = [
 ("Standing", STANDING, 0),
 ("Back View", BACK, 2),
 ("Seated", SEATED, 4),
 ("Side Profile", SIDE, 1),
 ("Ditzy", DITZY, 3),
 ("POV", POV, 5),
 ("Odalisque", ODALISQUE, 2),
]

def rotate_poses(look_number):
    """Devuelve [(slot_name, pose_direction), ...] de 7 elementos, rotados por numero de look."""
    out = []
    for name, variants, off in SLOTS:
        idx = (look_number + off) % len(variants)
        out.append((name, variants[idx]))
    return out

# Palabras de setting que NO deben repetirse muy seguido (espejo incluido, era el comodin).
_SETTING_KEYS = ["mirror","mirrored","espejo","gallery","museum","void","dungeon",
 "penthouse","boudoir","beach","pool","stage","club","chapel","cathedral","yacht",
 "casino","gym","throne","villa","terrace","marina"]

def check_setting_variety(settings, window=5):
    """Avisa si alguna palabra-clave de setting se repite dentro de una ventana de N looks.
    Devuelve lista de warnings (vacia = OK)."""
    import re
    warns = []
    seen = {}  # key -> indice del ultimo look que lo uso
    for i, s in enumerate(settings):
        low = s.lower()
        for k in _SETTING_KEYS:
            if re.search(r"\b"+re.escape(k)+r"\b", low):
                if k in seen and i - seen[k] < window:
                    warns.append(f"  setting '{k}' repetido en looks idx {seen[k]} y {i} (ventana {window})")
                seen[k] = i
    return warns

if __name__ == "__main__":
    import sys, io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    print("Variantes por slot:", {n: len(v) for n,v,_ in SLOTS})
    print("\nEjemplo rotacion L531-L535 (Standing/Back deben cambiar look a look):")
    for ln in range(531, 536):
        ps = rotate_poses(ln)
        print(f"L{ln}: Standing={STANDING.index(ps[0][1])+1}  Back={BACK.index(ps[1][1])+1}  Seated={SEATED.index(ps[2][1])+1}  Side={SIDE.index(ps[3][1])+1}  Ditzy={DITZY.index(ps[4][1])+1}  POV={POV.index(ps[5][1])+1}  Odal={ODALISQUE.index(ps[6][1])+1}")
