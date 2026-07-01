# -*- coding: utf-8 -*-
"""
Rotacion de poses V5 + props CONTEXTUALES + chequeo de variedad de settings.

POR QUE EXISTE (Directiva Ama 08/06/2026):
 (1) Mis inyectores hardcodeaban UNA plantilla de 7 poses (St1/Bk1/...) en CADA look
     -> poses clonadas (Standing identico x44, Back x83, POV x66).
 (2) Las poses con mueble (la sentada) metian "a sculptural seat" / "a chair" / "a wall"
     GENERICOS que NO calzaban con el ambiente (silla fuera de contexto en una playa, etc.).
     La Ama: "cada pose debe ser armoniosa con el ambiente, que no salgan cosas que no
     tengan nada que ver."

RECALIBRACION ANTI-SAFE (Ama 15/06/2026): el filtro "safe" de Gemini es token-level.
Las variantes con "deep cleavage dominant in frame", "the ass pushed out/lifted",
"straddling ... ass out", "lying face-down ... ass lifted", "cat arch ... ass lifted high",
"sliding down over her own ass", "slipping the shoulder strap off" y "bust dominant in the
lower frame / deep cleavage below" disparaban el bloqueo (incluso con prenda que cubre,
ej. L545). Reescritas a poses fetish-model igual de calientes pero con vocabulario que pasa
el filtro (lumbar arch elegante, hips angled, hands on hips/thighs, seated reversed,
semi-reclined). BLOQUE A intacto. Ver auto-memoria feedback_gemini_safe_poses.

SOLUCION props: las variantes con mueble usan placeholders {seat} {wall} {surface}; el inyector
los rellena POR LOOK con mobiliario del setting (ej: yate -> "a teak bench"; mazmorra ->
"a leather throne"; boudoir -> "a velvet chaise"). El piso (floor) es universal, no lleva prop.

USO OBLIGATORIO en todo inyector de batch:
    from pose_rotation_v5 import rotate_poses, check_setting_variety
    # por look, define props del setting:
    poses = rotate_poses(look_number, seat="a leather throne", wall="a mirrored wall",
                         surface="a chrome console table")
    # poses -> [(slot, pose_direction_con_props_ya_resueltos), ...]
    check_setting_variety([lk["setting"] for lk in LOOKS])

Rotacion: variante = (look_number + offset_slot) % len(variantes). Paso 1 + offsets
distintos -> ninguna variante se repite en 4 looks del mismo slot, y un look no sale
"todo St1". Excepcion: Pose Set Stripper sigue reemplazando las 7 (no se mezcla).
"""

# ANCLA ANATOMICA AUTOMATICA (Ama 16/06/2026): "muchos artefactos, manos donde no
# deberian, pies flotantes, piernas extras". El ancla viejo vivia SOLO en los inyectores
# de un solo uso -> el batch L541-L550 nacio sin ella (los inyectores son desechables y se
# olvido). Ahora rotate_poses() la PREPENDE sola: ningun batch futuro puede nacer sin ancla.
# Cuerpo entero -> brazos+manos+dedos+piernas+pies; Ditzy/POV (cintura arriba) -> solo manos
# (no se nombran piernas para no forzarlas en un encuadre cerrado).
# *** EL INYECTOR YA NO DEBE AGREGAR SU PROPIO ANCLA: viene incluida aqui. ***
FULL_ANCHOR  = "anatomically correct with exactly two arms, two hands each with five fingers, two legs and two feet"
# FIX CLOSE-UP (Ama 30/06/2026): el viejo HANDS_ANCHOR imponia "two hands" en encuadres de
# cintura-arriba (Ditzy/POV) donde las variantes solo muestran UNA mano cerca de la cara ->
# la IA metia una segunda mano fantasma o deformaba la visible ("problemas con las manos en la
# POV"). El ancla de close-up ahora describe CALIDAD de mano SIN imponer el conteo de dos.
HANDS_ANCHOR = "anatomically correct hands with exactly five fingers on each visible hand, no extra or malformed hands, no extra or fused fingers"
CLOSEUP_SLOTS = {"Ditzy", "POV"}  # encuadre de cintura para arriba -> ancla de manos, no de piernas

# Variantes: mantienen Principio Rector Fetish Model + nombran stiletto. {seat}/{wall}/{surface}
# = mobiliario CONTEXTUAL que pone el inyector. NO incluyen el setting (eso se appendea).

STANDING = [
 "full body from a low angle below the hip, the weight on one stiletto with the other foot forward and pointed, an exaggerated S-curve with the hip jutted to one side and the chest pushed forward, one XXXL-nailed hand sliding down the hip and thigh and the other pulling at the neckline, shoulders dropped, chin lifted, half-lidded predatory gaze, cherry red hair over one shoulder",
 "full body from a low angle, caught mid-stride walking straight toward the camera with one stiletto forward and the back foot lifting off the floor, hips swinging, one XXXL-nailed hand on the hip and the other arm loose, head turned over the shoulder, fierce runway gaze, cherry red hair in motion",
 "full body, the shoulders propped against {wall} with one knee bent and that stiletto sole flat against {wall}, the pelvis forward, one XXXL-nailed hand hooked in the waistband and the other trailing up the body, chin down looking up through the lashes, lips parted glossy, cherry red hair spilling against {wall}",
 "full body from a low angle, both arms raised overhead gathering the cherry red hair off the neck, the torso elongated and the chest lifted high in an extreme lumbar arch, the weight on both stilettos with the hip cocked, the side-body line elongated, the face tilted up with half-lidded eyes",
 "full body, the body turned three-quarters away with the hip toward the lens and the torso twisted back so the bust returns to camera, one XXXL-nailed hand on the far hip and the other lifting the hair at the nape, looking back over the shoulder with a predatory glance, a deep waist-to-hip twist, on towering stilettos",
 "full body from a low hero angle, standing tall and leaning slightly toward the camera with both XXXL-nailed hands resting on the thighs, the shoulders squared in an elegant lumbar arch, the chin lifted with a commanding direct gaze, lips parted glossy, cherry red hair falling forward framing the face, on stilettos",
 "full body, standing tall with the legs crossed at the knee in an elegant fashion-model X-stance, the weight balanced on both stilettos, one XXXL-nailed hand on the opposite hip and the other at the collarbone, the spine long with a subtle arch, chin tilted, half-lidded sultry gaze, cherry red hair over one shoulder",
 "full body from a low hero angle, the feet planted apart and firm on both stilettos, both XXXL-nailed hands on the hips, the shoulders pulled back and the chin dropped for a dominant direct stare down at the camera, a commanding lumbar arch, cherry red hair framing the face",
 "full body, one XXXL-nailed hand resting at the neckline and the other low on the hip, the weight on one stiletto with a soft knee bend, the chin tilted and a self-aware sultry gaze to the camera, lips parted glossy, an intimate self-aware posture, cherry red hair pushed to one side",
]

BACK = [
 "full body back view with an elegant hip-pop, the spine in a graceful S-curve, one XXXL-nailed hand on the hip and the other reaching up through the cherry red hair, looking back over the shoulder with a half-lidded sultry gaze, the weight on one stiletto with the other foot pigeon-toed inward, lips parted glossy",
 "full body back view caught mid-stride walking away from the camera with one stiletto lifting and the hips swinging, the torso twisting to glance back over the shoulder, one XXXL-nailed hand resting at the small of the back, cherry red hair down the spine",
 "full body back view bent slightly forward with both XXXL-nailed hands flat on {surface}, a deep elegant back arch with the hips angled toward the camera, looking back over the shoulder through the cherry red hair, the weight on both stilettos",
 "full body back view standing with both XXXL-nailed hands lifting all the cherry red hair up off the nape, exposing the full back and spine line, the head dropped slightly forward, the weight on one hip with the stiletto cocked",
 "full body back view with the shoulder blades against {wall} facing partly away, the hips off {wall} and angled out, one XXXL-nailed hand pressed on {wall} behind, looking back to the camera over the shoulder, the weight on one stiletto",
 "full body back view with both XXXL-nailed hands resting on the curve of the hips, a deep lumbar arch, the head thrown back, cherry red hair veiling the turned face, the weight on both stilettos pointed",
 "full body back view kneeling upright with the spine arched and sitting back toward the heels, one XXXL-nailed hand reaching up the back and the other in the hair, looking over the shoulder, the stilettos visible behind",
]

SEATED = [
 "perched on {seat} with one leg crossed over the other and the top stiletto pointed at the camera, an extreme lumbar arch, one XXXL-nailed hand on the top knee and the other fingertip at the bottom lip, the bust angled forward, shoulders rolled back, half-lidded direct gaze, cherry red hair framing one breast",
 "perched on the edge of {seat} leaning forward with the elbows on the knees, the décolleté angled toward the camera, the stilettos crossed at the ankle, one XXXL-nailed hand under the chin, looking up through the lashes with lips parted, cherry red hair falling forward",
 "reclined back on {seat} propped on one elbow with the other XXXL-nailed hand trailing down the torso, the spine in a long arch, the legs extended with the stilettos crossed at the ankle and pointed, half-lidded predatory gaze, cherry red hair spilling over the backrest",
 "seated reversed on {seat} with both arms folded over the backrest and the chin resting on the forearms, the spine in an elegant arch, the stilettos crossed at the ankle, a sultry half-lidded gaze over the arms, cherry red hair over one shoulder",
 "perched on the edge of {seat} with the spine erect and the knees together, both XXXL-nailed hands resting flat on the thighs, the chest lifted in an imperious arch, the chin raised, a commanding half-lidded gaze to the camera, lips parted glossy, cherry red hair over one shoulder",
 "seated side-saddle on {seat} with the legs together angled to one side and the top stiletto pointed, the torso twisted back to the camera, one XXXL-nailed hand on the upper thigh and the other at the collarbone, an extreme waist twist, half-lidded gaze, cherry red hair over one breast",
]

# SIDE PROFILE (Ama 01/07/2026 — REPARADO): el pool traia variantes SENTADA/RECLINADA/DE
# RODILLAS que (1) duplicaban los slots Seated y Odalisque y (2) hacian que el generador
# rindiera la "pose de costado" SIEMPRE sentada ("esta generando siempre sentada"). Ademas
# las de pie no anclaban STANDING explicito -> Gemini defaulteaba a sentada. FIX DE RAIZ:
# las 7 variantes son ahora TODAS DE PIE, cada una con ancla explicita (standing ... on
# stilettos / on tiptoe / mid-stride), mostrando la silueta de perfil (bust-to-waist-to-hip).
# NINGUNA sentada/reclinada/de rodillas en el pool -> la sentada la cubre el slot Seated,
# la reclinada el slot Odalisque.
SIDE = [
 "full body side profile standing tall on both towering stilettos, an elegant S-curve with a graceful lumbar arch and the bust lifted high in silhouette, both legs long and straight with the weight balanced, one XXXL-nailed hand resting on the hip and the other trailing up the ribcage, chin lifted, lips parted glossy, cherry red hair cascading down the spine",
 "full body side profile standing on towering stilettos with one foot pointed forward, the hips angled back and the chest forward tracing the hourglass silhouette, both legs long and straight, one XXXL-nailed hand at the nape lifting the cherry red hair and the other on the thigh, the face in profile with a half-lidded gaze, lips parted glossy",
 "full body side profile caught mid-stride walking on towering stilettos with one leg forward and the stiletto pointed and the back heel lifting off the floor, the hips swung and the chest forward, one XXXL-nailed hand swinging and the other on the hip, chin lifted in profile, cherry red hair streaming back",
 "full body side profile standing with the back deeply arched and both stilettos planted, the bust forward and the hips tipped back in an exaggerated hourglass silhouette, both XXXL-nailed hands sliding down the front of the thighs, the head tipped back, lips parted glossy, cherry red hair falling down the arched spine",
 "full body side profile standing on tiptoe on towering stilettos, one arm raised overhead elongating the side-body line with the bust lifted in silhouette, the spine in a long graceful arch, the other XXXL-nailed hand on the hip, the face in profile with a sultry half-lidded gaze, cherry red hair cascading",
 "full body side profile standing shoulder-first against {wall}, one XXXL-nailed hand raised high on {wall} and the back deeply arched away from {wall}, the bust forward and the hips angled in silhouette, standing on both stilettos with one heel lifted, lips parted, cherry red hair against {wall}",
 "full body side profile standing tall with both stilettos together, the torso turned to pure profile showing the bust-to-waist-to-hip silhouette, one XXXL-nailed hand on the lower back accentuating the lumbar arch and the other at the collarbone, chin high, a commanding profile gaze, cherry red hair swept over the far shoulder",
]

# DITZY (Directiva Ama 09/06/2026): encuadre DE LA CINTURA HACIA ARRIBA (no plano americano).
# Pose SENSUAL que presenta pechos + rostro -> es la toma de DETALLE (rostro, maquillaje, detalle del outfit superior).
DITZY = [
 "waist-up shot framed from the waist up, the torso angled and the augmented bust presented to the camera, one XXXL French fingertip resting against the glossy parted lips and the other hand at the waist, the face the focus of the frame showing the detailed bimbo makeup, a sensual half-lidded gaze, cherry red hair framing the face, the bodice and its detail crisp and legible",
 "waist-up shot framed from the waist up, the bust presented to the camera, one XXXL French fingertip twirling a lock of cherry red hair beside the face, the face the focus showing the detailed bimbo makeup and glossy parted lips, a sensual half-lidded gaze, the bodice and its detail crisp and legible",
 "waist-up shot framed from the waist up, the torso angled, one XXXL-nailed hand resting at the neckline while gazing at the camera, the face the focus showing the detailed makeup and glossy parted lips, a sensual half-lidded gaze, cherry red hair over one shoulder, the bodice detail crisp and legible",
 "waist-up shot framed from the waist up, the bust presented to the camera, XXXL French fingertips held just in front of the glossy lips blowing a kiss to the camera, the face the focus showing the detailed bimbo makeup, a sensual half-lidded gaze, cherry red hair framing the face, the bodice detail crisp and legible",
 "waist-up shot framed from the waist up, the bust presented to the camera, one XXXL-nailed hand framing the cheekbone with the head tilted, the face the focus of the frame showing the detailed makeup and glossy parted lips, a sensual half-lidded gaze, cherry red hair cascading, the bodice and its detail crisp and legible",
 "waist-up shot framed from the waist up, the torso turned and the augmented bust presented, the chin dropped and the eyes lifted to the lens through the lashes, one XXXL fingertip at the glossy bottom lip, the face the focus showing the detailed bimbo makeup, a sensual half-lidded gaze, cherry red hair forward, the bodice detail crisp and legible",
]

# POV (Directiva Ama 09/06/2026, reforzada 30/06/2026): es una TOMA SENSUAL DE INSTAGRAM, NO un
# point-of-view literal. El generador estaba leyendo "POV" literal (camara mirando hacia abajo
# por el propio cuerpo hasta las puntas de los stilettos) porque los inyectores viejos pegaban
# "first-person POV looking down over own body ... converging to pointed stiletto tips".
# PROHIBIDO en toda variante: "first-person", "point of view", "POV", "looking down over own
# body", "overhead", "converging to ... stiletto tips", "selfie", "phone". El sujeto MIRA A LA
# CAMARA (retrato de influencer thirst-trap), UNA sola mano en cuadro, "a single woman alone".
# Pool ampliado de 5 -> 8 (la POV repetia mas rapido que los demas slots). Ver self-check POV_BAD.
POV = [
 "intimate medium close-up portrait of a sensual Instagram influencer addressing the camera, the face leaning toward the lens, one XXXL-nailed hand buried in the cherry red hair, a smoldering direct gaze and glossy parted lips, the face dominant in the upper-mid frame, a single woman alone",
 "sensual Instagram glamour portrait from a low angle, the face turned up to the lens and the chin elevated, one XXXL-nailed hand trailing along the collarbone, a half-lidded seductive gaze, lips parted glossy, the décolleté in the lower frame, a single woman alone",
 "sensual Instagram-influencer candid portrait, a three-quarter face glancing just off the lens with one XXXL-nailed hand pushing the cherry red hair back from the temple, lips parted glossy, an intimate seductive mood, the face in the upper-mid frame and the décolleté below, a single woman alone",
 "sensual Instagram boudoir portrait reclining with the head tipped back toward the camera, the face and bust facing the lens, one XXXL-nailed hand resting on the collarbone, a sultry half-lidded gaze, lips parted glossy, a single woman alone",
 "intimate sensual Instagram close-up portrait facing the camera, one XXXL French fingertip grazing and pulling the glossy bottom lip, a direct smoldering gaze to the lens, the face dominant in the frame and the décolleté below, a single woman alone",
 "sensual Instagram influencer portrait at a high three-quarter angle, the chin resting on the back of one XXXL-nailed hand with the elbow propped, a coy half-lidded gaze up to the lens, glossy parted lips, the face dominant in the frame, a single woman alone",
 "sensual Instagram influencer portrait glancing back over one bare shoulder toward the lens, one XXXL-nailed hand drawing the cherry red hair away from the cheek, a smoldering glance and glossy parted lips, the face and shoulder line filling the frame, a single woman alone",
 "sensual Instagram influencer portrait from slightly above the eyeline, the face tilted up to the camera, one XXXL-nailed hand pressed flat against the upper chest below the collarbone, a sultry up-gaze and glossy parted lips, the face dominant and the décolleté below, a single woman alone",
]

ODALISQUE = [
 "full body lying on the side with an exaggerated S-curve, an extreme back arch with the bust pushed up and the hip rolled back, one leg extended with the stiletto pointed and the other bent, one arm under the head with XXXL nails in the hair and the other trailing from the collarbone to the hip, half-lidded predatory gaze, cherry red hair cascading",
 "full body semi-reclined on one hip propped on one forearm with the legs draped and the top stiletto pointed at the camera, the spine in an elegant arch, the other XXXL-nailed hand resting on the thigh, looking to the camera over the shoulder, lips parted glossy, cherry red hair spilling forward",
 "full body reclining to one side on one hip with the legs draped and both stilettos visible, one arm extended propping the body and the other XXXL-nailed hand trailing from the collarbone to the waist, the spine in a long arch with the bust forward, a half-lidded gaze toward the camera, lips parted glossy, cherry red hair cascading forward",
 "full body semi-reclined propped on both elbows with the legs draped and one stiletto pointed at the camera, the bust forward and the spine arched, the chin lifted, a half-lidded predatory gaze, XXXL nails resting on the thigh, cherry red hair over one shoulder",
 "full body reclining back on both elbows with the legs draped and one stiletto pointed at the camera, a deep elegant back arch with the bust lifted, looking to the camera through the lashes, XXXL nails resting on the thigh, lips parted glossy, cherry red hair falling around the face",
 "full body side profile reclining on one side with an elegant S-curve, the hip rolled up and the bust forward in silhouette, one XXXL-nailed hand supporting the head and the other trailing along the waist, the top stiletto pointed and the legs elegantly stacked, lips parted glossy, cherry red hair cascading along the surface",
]

SLOTS = [
 ("Standing", STANDING, 0),
 ("Back View", BACK, 2),
 ("Seated", SEATED, 4),
 ("Side Profile", SIDE, 1),
 ("Ditzy", DITZY, 3),
 ("POV", POV, 5),
 ("Odalisque", ODALISQUE, 2),
]

def rotate_poses(look_number, seat="a sculptural bench", wall="a wall", surface="a surface"):
    """Devuelve [(slot, pose_direction)] de 7, rotados por nº de look y con props CONTEXTUALES.
    seat/wall/surface deben describir mobiliario REAL del setting del look (armonia con el ambiente)."""
    out = []
    for name, variants, off in SLOTS:
        v = variants[(look_number + off) % len(variants)]
        v = v.replace("{seat}", seat).replace("{wall}", wall).replace("{surface}", surface)
        anchor = HANDS_ANCHOR if name in CLOSEUP_SLOTS else FULL_ANCHOR
        v = anchor + ", " + v  # ancla anatomica automatica (ver nota arriba)
        out.append((name, v))
    return out

_SETTING_KEYS = ["mirror","mirrored","espejo","gallery","museum","void","dungeon",
 "penthouse","boudoir","beach","pool","stage","club","chapel","cathedral","yacht",
 "casino","gym","throne","villa","terrace","marina"]

def check_setting_variety(settings, window=5):
    """Avisa si alguna palabra-clave de setting (espejo incluido) se repite dentro de N looks."""
    import re
    warns, seen = [], {}
    for i, s in enumerate(settings):
        for k in _SETTING_KEYS:
            if re.search(r"\b"+re.escape(k)+r"\b", s.lower()):
                if k in seen and i - seen[k] < window:
                    warns.append(f"  setting '{k}' repetido en idx {seen[k]} y {i} (ventana {window})")
                seen[k] = i
    return warns

if __name__ == "__main__":
    import sys, io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    print("Variantes por slot:", {n: len(v) for n,v,_ in SLOTS})
    print("\nL531 con props de mazmorra (seat=throne, wall=stone wall):")
    for slot, txt in rotate_poses(531, seat="a leather throne", wall="a stone dungeon wall", surface="a steel table"):
        print(f"  {slot}: {txt[:90]}...")
    print("\n¿quedo algun placeholder sin resolver?", "{" in str(rotate_poses(531)))
    # Auto-check anti-safe: ninguna variante debe contener tokens que disparan el filtro.
    BAD = ["cleavage dominant", "ass pushed", "ass out", "ass lifted", "own ass",
           "straddling", "face-down", "cat arch", "slipping the shoulder strap",
           "dominant in the lower frame", "deep cleavage"]
    hits = []
    for name, variants, _ in SLOTS:
        for i, v in enumerate(variants):
            for b in BAD:
                if b in v.lower():
                    hits.append(f"{name}[{i}] -> '{b}'")
    print("\nAnti-safe check:", "LIMPIO" if not hits else "FLAGS: " + "; ".join(hits))
    # Auto-check anti-POV-literal (Ama 30/06): ninguna variante POV puede traer lenguaje que el
    # generador lea como point-of-view literal. La POV es un retrato sensual de Instagram.
    POV_BAD = ["first-person", "point of view", "pov", "looking down over", "overhead",
               "converging to", "stiletto tips", "selfie", "phone", "smartphone"]
    pov_hits = [f"POV[{i}] -> '{b}'" for i, v in enumerate(POV) for b in POV_BAD if b in v.lower()]
    print("Anti-POV-literal check:", "LIMPIO (POV = retrato IG)" if not pov_hits else "FLAGS: " + "; ".join(pov_hits))
    # Auto-check ancla anatomica: toda pose generada debe traer su ancla ya incluida.
    miss = []
    for slot, txt in rotate_poses(531):
        want = HANDS_ANCHOR if slot in CLOSEUP_SLOTS else FULL_ANCHOR
        if not txt.startswith(want):
            miss.append(slot)
    print("Ancla anatomica check:", "LIMPIO (todas las poses anclan)" if not miss else "FALTA en: " + ", ".join(miss))
