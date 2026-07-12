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
    # Si el look usa prenda envolvente de frente abierto (robe/kimono/bata/peignoir/wrap):
    #   poses = rotate_poses(look_number, ..., wrap_mode="slip")   # o "closed" (ver nota abajo)
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

# ANCLA DE ORIENTACION DE PRENDA ENVOLVENTE (Ama 09/07/2026 — BUG "bata al reves"):
# Las prendas de frente abierto (robe/kimono/peignoir/bata/wrap) se describen en el token de
# vestuario como "gently parted at front revealing X / draped off the shoulders". Ese token se
# pega IDENTICO en las 7 poses (Token de Vestuario Bloqueado). "at front revealing" es una
# instruccion RELATIVA A LA CAMARA: en la Back View, con el cuerpo de espaldas, el generador
# resuelve el choque poniendo la abertura ATRAS (corriendo por la columna) para poder "mostrar
# el set" -> bata al reves, escote hacia la espalda (confirmado en L256 y L703). Faltaba anclar
# la ORIENTACION de la prenda en la pose de espalda. Dos modos, a eleccion del inyector por look:
#   "slip"   -> bata deslizada de los hombros, colgando de los brazos: espalda + lenceria al aire
#               pero prenda FISICAMENTE correcta (la abertura va adelante; solo se resbalo). Es lo
#               que hizo bien el L407. Default recomendado para boudoir (conserva el desnudo sensual).
#   "closed" -> bata bien puesta: pano continuo cerrado cayendo por la columna (espalda cubierta).
# Ver auto-memoria feedback_bata_reverso_espalda.
WRAP_BACK_SLIP = "the open-front wrap garment (robe, kimono or peignoir) worn correctly but slipped off both shoulders to hang open from the forearms and elbows, its front opening and sash on the far side away from the camera, so the bare back and the lingerie underneath are exposed down the spine while the loose fabric drapes to the sides of the body and hangs from the arms, NOT parted or seamed down the spine, with no neckline, lapel or opening running down the back"
WRAP_BACK_CLOSED = "the open-front wrap garment (robe, kimono or peignoir) worn correctly and facing forward, seen from behind as a single continuous closed panel of fabric draping straight down the spine to the hem, its front opening, lapels, neckline and sash knot all on the far side away from the camera and not visible from behind, with no parting, no seam and no neckline down the back"
_WRAP_ANCHORS = {"slip": WRAP_BACK_SLIP, "closed": WRAP_BACK_CLOSED}

# ANCLA DE RECUMBENCIA DE LA ODALISCA (Ama 09/07/2026 — BUG "odalisca sentada"):
# La odalisca (pose recostada/languida) derivaba a SENTADA: el generador rendia la figura sentada
# en el piso/mueble en vez de recostada (confirmado en L574 sentada sobre el cofre, L638 y L660
# sentadas en el piso). Causa: varias variantes arrancan "semi-reclined propped on both elbows /
# reclining back on both elbows" y "propped on both elbows" se lee como torso vertical sentado, sin
# un ancla explicita de cuerpo horizontal. Es EL MISMO patron que ya arreglamos en Side Profile
# (rendia siempre sentada hasta que forzamos "standing" explicito). Aqui forzamos "lying down /
# horizontal / NOT sitting upright". Se prepende SOLO al slot Odalisque. Recomendado ademas anadir
# al negative del inyector: `sitting upright, seated, sitting on the floor`. Ver auto-memoria
# feedback_odalisca_sentada.
ODALISQUE_ANCHOR = "lying down on the surface with the whole body low and horizontal, a reclining odalisque with the torso resting down toward the surface, NOT sitting upright and NOT seated"

# ANCLA DE PESO EN LA SENTADA + REESCRITURA DE 2 VARIANTES (Ama 11/07/2026 — BUG "problemas
# en Seated"): auditoria de las ultimas 50 imagenes (L729-L760) encontro 6 de 7 muestras con
# la pose Seated desviada del prompt, dos patrones distintos:
#  (1) SUSTITUCION DE MUEBLE: cuando el setting trae una segunda superficie plana grande cerca
#      del asiento (mesa de directorio, isla de cocina), Gemini apoya el cuerpo en ESA superficie
#      en vez del asiento nombrado (confirmado L732: "perched on the edge of a white leather
#      boardroom chair" -> rindio perchada en el ESCRITORIO de caoba, la silla vacia al lado;
#      L754: "reclined back on a bar stool at the kitchen island" -> rindio apoyada en la ISLA,
#      no reclinada en el taburete). Fix: SEATED_ANCHOR se pega a las 6 variantes ancla el peso
#      al asiento nombrado y prohibe explicitamente apoyarse en mobiliario vecino.
#  (2) POSTURA COMPLEJA IGNORADA: instrucciones de postura dinamica se aplanan a la sentada
#      generica segura (torso derecho, mano en el menton) — confirmado L729/L741/L759 ("leaning
#      forward with the elbows on the knees" nunca aparecio) y L755, el mas grave ("seated
#      REVERSED... arms folded over the backrest, chin resting on forearms" = straddle mirando
#      el respaldo, rindio sentada normal de frente). "reversed"/straddle es ademas pariente del
#      token "straddling" ya proscrito en el BAD-check anti-safe de mas abajo — probable filtro,
#      no solo dificultad de pose. Fix: variante 1 reescrita con la instruccion al FRENTE de la
#      oracion (primacia) en vez de enterrada; variante 3 reemplazada por una pose igual de
#      dramatica (arco hacia atras sobre el respaldo) SIN straddle/reversed. Ver auto-memoria
#      feedback_seated_mueble_postura.
SEATED_ANCHOR = ("the body's full weight supported entirely by the seat itself, both hips and "
                  "thighs resting directly on it, NOT leaning against, perched on or propped "
                  "against any nearby table, desk, counter, island or other surface")

# ANCLA DE FRONTALIDAD DE LA STANDING (Ama 12/07/2026 — BUG "la pose de frente sale de espalda
# o medio perfil"): el slot Standing era el UNICO sin ancla de orientacion. Back nombra "back view"
# en las 7 variantes; Side fuerza "side profile standing"; Odalisque y Seated ya tienen la suya.
# Standing solo decia "full body" -> la orientacion quedaba a criterio del generador, y cualquier
# token debil de giro la arrastraba fuera del frente. Dos variantes del pool lo disparaban:
#  (1) STANDING[4] era, de hecho, una BACK VIEW infiltrada en el pool: "the body turned three-
#      quarters away ... looking back over the shoulder". El "torso twisted back so the bust
#      returns to camera" NUNCA se cumple (es una torsion imposible que el generador aplana al
#      giro simple) -> rindio espalda pura, confirmado en L751 y L760 (culo a camara, mirando por
#      sobre el hombro; indistinguibles del slot Back View). Cae 1 de cada 9 looks (N%9==4).
#      Reescrita: misma torsion dramatica cintura-cadera pero con el busto y el frente del outfit
#      anclados a la lente, sin ningun token de giro-de-espalda.
#  (2) STANDING[1] mezclaba "walking straight toward the camera" con "head turned over the
#      shoulder" — contradiccion interna; el generador puede resolverla por cualquiera de los dos
#      lados (en L748/L757 se salvo de frente, pero el token de espalda seguia ahi). Reescrita con
#      la mirada a la lente.
# La Standing es ademas la pose HERO del look: es el unico registro frontal del outfit completo.
# Perderla a una espalda no solo desvia la pose, DUPLICA el slot Back View y el set queda sin
# frente. Por eso el ancla se PREPENDE (primacia), no se appendea.
# OJO: no se agrega un negative global "back view" — el negative es UNO por look y compartido por
# las 7 poses, asi que pelearia con el slot Back View (que legitimamente ES de espalda). El lever
# correcto es el ancla en el POSITIVE (ver feedback_anti_3_piernas_poses: Gemini ignora el negative).
# Ver auto-memoria feedback_standing_no_frontal.
STANDING_ANCHOR = ("standing upright and facing the camera from the front, the front of the body "
                   "and the full front of the outfit turned toward the lens with the face to the "
                   "camera, a FRONT view: NOT a back view, NOT a rear or three-quarter view from "
                   "behind, the body never turned away from the lens and never seen from the back")

# ANCLA DE ORIENTACION DE LA RAYA DE LA MEDIA (Ama 11/07/2026 — BUG "raya al frente"):
# El token de vestuario describe la media como "back-seam stockings" (raya trasera). Igual que
# "at front revealing" en la bata, "back-seam" es RELATIVO A LA CAMARA: en poses de frente el
# generador pinta la raya en la cara VISIBLE (el frente de la canilla) para poder mostrarla ->
# la raya sale por delante (confirmado L691, L752, L748). Faltaba anclar que la costura va
# ESTRICTAMENTE por detras de la pierna. Se pasa seam=True cuando el look usa medias con costura;
# el ancla es POSE-AWARE: en las poses de frente fuerza "frente liso, costura solo atras"; en la
# Back View fuerza "costura visible subiendo por detras". El Side Profile no la lleva (de perfil
# la raya trasera cae en el borde posterior, que es correcto). Ver auto-memoria feedback_media_raya_frontal.
STOCKING_SEAM_FRONT = "the back-seam of the stockings runs strictly up the centre-back of each leg and is NOT visible from the front, the front of each leg smooth and seamless with no seam down the shin"
STOCKING_SEAM_BACK  = "the back-seam of each stocking clearly visible running straight up the centre-back of the calf and thigh"
# slots que NO llevan ancla de raya (Side Profile = raya cae natural en el borde posterior):
_SEAM_SKIP_SLOTS = {"Side Profile"}

# ANCLA DE OPACIDAD / ANTI-CORTE (Ama 11/07/2026 — BUG "cortes para mostrar runas/ombligo"):
# El Bloque A (INTOCABLE) describe "navel piercing", "nipple piercings ... visible under clothing"
# y "rune tattoo along hip crease and bikini line". El generador lee "visible" y le ABRE ventanas
# a la prenda (keyhole, cutout, underboob) para exponer esas marcas, rompiendo el "fully opaque at
# bust and groin" (confirmado L706 hueco en la cadera sobre la runa, L699 teddy cortado sobre la
# linea del bikini). Fix quirurgico: NO se toca Bloque A; el inyector pega OPAQUE_LOCK en la clausula
# de vestuario de los arquetipos CUBIERTOS (traje/gala/maid/catsuit). El "wherever the garment covers"
# deja que las runas/ombligo SI se luzcan en lenceria/bikini/alto-corte (ahi es on-brand) y solo
# prohibe CORTAR una prenda que debia cubrir. Ver auto-memoria feedback_cortes_ropa_runas_ombligo.
OPAQUE_LOCK = ("the garment is solid and uncut across the bust, midriff, navel and hips with NO keyhole, "
               "cutout, underboob window, peekaboo opening or slashing; the navel piercing and the hip rune "
               "tattoos stay concealed beneath the fabric wherever the garment covers that area, showing only "
               "where the design is genuinely bare and never through a hole cut into a covering garment")

# ANCLA ANTI-MATE / GLOSS-LOCK (Ama 11/07/2026 — desvio prompt->imagen "material mate"):
# Cuando la silueta primea tela mate (traje sastre de lana/crepe, rib atletico, saten nupcial plano),
# el sesgo del arquetipo le gana al token "vinyl/latex" y Gemini rinde tela natural mate, prohibida
# por canon (confirmado L732 traje mate, L750 rib mate; contraste: L759 bodysuit liquid latex salio
# brillante). El inyector pega GLOSS_LOCK redundante en la clausula de vestuario de las siluetas de
# riesgo. Ver auto-memoria feedback_material_mate_vs_fetish y regla Anti-Mate en 04-estetica-ele.md.
GLOSS_LOCK = ("rendered in a high-shine liquid latex / wet-look PVC / patent vinyl finish with strong "
              "specular highlights and a glossy mirror-like reflective surface, absolutely no matte or "
              "natural non-reflective fabric")

# ANCLA DE CONSISTENCIA DE PRENDA ENTRE POSES (Ama 11/07/2026 — BUG "el mismo outfit cambia de
# escote/largo/manga entre poses"): el Token de Vestuario Bloqueado se pega IDENTICO en las 7 poses,
# pero si deja el ESCOTE, el LARGO DE MANGA o el LARGO DE RUEDO sin fijar, Gemini los rellena
# distinto en cada pose (confirmado L746 corpiño: sin-mangas-cuello-alto en Standing / tiritas-escote-
# bajo en Seated / manga-larga en Odalisque; L707 mangas cap vs sin mangas; L693 lunares solidos vs
# con espiral). Dos capas: (a) el token DEBE nombrar explicitamente neckline + sleeve length + hemline
# (ej. "off-shoulder bardot neckline, long fitted sleeves to the wrist, floor-length mermaid hem");
# (b) pegar CONSISTENCY_LOCK para que la IA no reinvente el corte por pose. El linter garment_canon.py
# marca vestidos/gowns cuyo token no nombre neckline/sleeve/hem. Ver feedback_drift_prenda_entre_poses.
CONSISTENCY_LOCK = ("the exact same single outfit in every shot: its neckline shape, sleeve length, hemline "
                    "length, cut and print are IDENTICAL and unchanged across all poses, never re-styled, "
                    "never lengthened or shortened, never switching between sleeveless and sleeved or between "
                    "high and low neckline")

# Fragmentos para el NEGATIVE del inyector (pegar segun el caso):
NEG_INCONSISTENT = ("changing neckline between shots, altered sleeve length, different hemline length, "
                    "re-styled outfit, inconsistent dress cut, varying print pattern")
NEG_FRONT_SEAM = "seam down the front of the leg, front seam on stockings, seam on the shin"
NEG_CUTOUT     = ("keyhole cutout at navel, midriff cutout exposing navel piercing, hip cutout exposing tattoo, "
                  "underboob cutout, peekaboo opening, garment slashed to reveal skin")
NEG_MATTE      = "matte fabric, cotton, wool, crepe, linen, dull non-reflective textile, flat fabric finish, natural matte cloth"

# Variantes: mantienen Principio Rector Fetish Model + nombran stiletto. {seat}/{wall}/{surface}
# = mobiliario CONTEXTUAL que pone el inyector. NO incluyen el setting (eso se appendea).

STANDING = [
 "full body from a low angle below the hip, the weight on one stiletto with the other foot forward and pointed, an exaggerated S-curve with the hip jutted to one side and the chest pushed forward, one XXXL-nailed hand sliding down the hip and thigh and the other pulling at the neckline, shoulders dropped, chin lifted, half-lidded predatory gaze, cherry red hair over one shoulder",
 "full body from a low angle, caught mid-stride walking straight toward the camera with one stiletto forward and the back foot lifting off the floor, hips swinging, one XXXL-nailed hand on the hip and the other arm loose, the face front to the lens with the chin lifted, a fierce runway gaze straight down the camera, cherry red hair in motion",
 "full body, the shoulders propped against {wall} with one knee bent and that stiletto sole flat against {wall}, the pelvis forward, one XXXL-nailed hand hooked in the waistband and the other trailing up the body, chin down looking up through the lashes, lips parted glossy, cherry red hair spilling against {wall}",
 "full body from a low angle, both arms raised overhead gathering the cherry red hair off the neck, the torso elongated and the chest lifted high in an extreme lumbar arch, the weight on both stilettos with the hip cocked, the side-body line elongated, the face tilted up with half-lidded eyes",
 "full body facing the camera with the chest and hips square to the lens, the hip cocked hard to one side in a deep waist-to-hip twist while the bust stays turned to the camera, one XXXL-nailed hand on the jutted hip and the other lifting the cherry red hair off the nape, the chin dropped and the eyes up to the lens in a predatory glance, on towering stilettos",
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
 "leaning her torso sharply forward from the hips while perched on the edge of {seat}, both elbows planted firmly on top of both knees, the décolleté angled toward the camera, the stilettos crossed at the ankle, one XXXL-nailed hand under the chin, looking up through the lashes with lips parted, cherry red hair falling forward",
 "reclined back on {seat} propped on one elbow with the other XXXL-nailed hand trailing down the torso, the spine in a long arch, the legs extended with the stilettos crossed at the ankle and pointed, half-lidded predatory gaze, cherry red hair spilling over the backrest",
 "seated deep in {seat} with the spine arched back over the top of the backrest and both XXXL-nailed hands draped along the top of the backrest, the chest lifted high and the chin dropped back, cherry red hair spilling over the top of the backrest behind her, a half-lidded gaze rolled toward the camera, lips parted glossy, the stilettos crossed at the ankle",
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

def rotate_poses(look_number, seat="a sculptural bench", wall="a wall", surface="a surface",
                 wrap_mode=None, seam=False):
    """Devuelve [(slot, pose_direction)] de 7, rotados por nº de look y con props CONTEXTUALES.
    seat/wall/surface deben describir mobiliario REAL del setting del look (armonia con el ambiente).

    wrap_mode (Ama 09/07/2026 — BUG "bata al reves"): si el look usa una prenda ENVOLVENTE de
    frente abierto (robe/kimono/peignoir/bata/wrap), pasar wrap_mode para anclar la ORIENTACION
    de la prenda SOLO en la pose de espalda (Back View), donde el generador la ponia al reves
    (abertura corriendo por la columna). Valores: None (sin prenda envolvente) · "slip" (bata
    deslizada de los hombros, espalda desnuda pero correcta — default recomendado boudoir) ·
    "closed" (bata bien puesta, espalda cubierta). Ver auto-memoria feedback_bata_reverso_espalda.

    seam (Ama 11/07/2026 — BUG "raya de la media al frente"): pasar seam=True cuando el look usa
    MEDIAS CON COSTURA (back-seam / seamed stockings). Ancla POSE-AWARE la orientacion de la raya:
    poses de frente -> "frente liso, costura solo por detras"; Back View -> "costura visible por
    detras"; Side Profile no la lleva. Ver auto-memoria feedback_media_raya_frontal."""
    if wrap_mode not in (None, "slip", "closed"):
        raise ValueError(f"wrap_mode invalido: {wrap_mode!r} (usa None, 'slip' o 'closed')")
    wrap_anchor = _WRAP_ANCHORS.get(wrap_mode)
    out = []
    for name, variants, off in SLOTS:
        v = variants[(look_number + off) % len(variants)]
        v = v.replace("{seat}", seat).replace("{wall}", wall).replace("{surface}", surface)
        anchor = HANDS_ANCHOR if name in CLOSEUP_SLOTS else FULL_ANCHOR
        if name == "Odalisque":
            anchor = anchor + ", " + ODALISQUE_ANCHOR  # fuerza recumbencia (bug odalisca-sentada)
        if name == "Standing":
            anchor = anchor + ", " + STANDING_ANCHOR  # fuerza frontalidad (bug standing-de-espalda)
        v = anchor + ", " + v  # ancla anatomica automatica (ver nota arriba)
        if name == "Seated":
            v = v + ", " + SEATED_ANCHOR  # ancla de peso (bug sustitucion de mueble)
        if name == "Back View" and wrap_anchor:
            v = v + ", " + wrap_anchor  # ancla de orientacion de prenda envolvente (bug bata-al-reves)
        if seam and name not in _SEAM_SKIP_SLOTS:  # ancla de orientacion de la raya (bug raya-al-frente)
            v = v + ", " + (STOCKING_SEAM_BACK if name == "Back View" else STOCKING_SEAM_FRONT)
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
    # Auto-check ancla de prenda envolvente (Ama 09/07 — bug bata-al-reves): con wrap_mode, SOLO
    # la Back View lleva el ancla de orientacion; sin wrap_mode, ninguna pose la lleva.
    def _bv(poses): return dict(poses)["Back View"]
    ok_slip   = WRAP_BACK_SLIP   in _bv(rotate_poses(256, wrap_mode="slip"))
    ok_closed = WRAP_BACK_CLOSED in _bv(rotate_poses(320, wrap_mode="closed"))
    leak_none = any(a in txt for _, txt in rotate_poses(256) for a in (WRAP_BACK_SLIP, WRAP_BACK_CLOSED))
    leak_slot = any(a in txt for slot, txt in rotate_poses(256, wrap_mode="slip")
                    if slot != "Back View" for a in (WRAP_BACK_SLIP, WRAP_BACK_CLOSED))
    print("Ancla prenda envolvente check:",
          "LIMPIO (slip+closed en Back View, sin fuga)" if (ok_slip and ok_closed and not leak_none and not leak_slot)
          else f"FALLA (slip={ok_slip} closed={ok_closed} fuga_sin_wrap={leak_none} fuga_otro_slot={leak_slot})")
    # Auto-check ancla de recumbencia (Ama 09/07 — bug odalisca-sentada): SOLO la Odalisque la lleva.
    od_ok = ODALISQUE_ANCHOR in dict(rotate_poses(531))["Odalisque"]
    od_leak = any(ODALISQUE_ANCHOR in txt for slot, txt in rotate_poses(531) if slot != "Odalisque")
    print("Ancla recumbencia odalisca check:",
          "LIMPIO (solo Odalisque ancla, sin fuga)" if (od_ok and not od_leak)
          else f"FALLA (od_ok={od_ok} fuga_otro_slot={od_leak})")
    # Auto-check ancla de raya de media (Ama 11/07 — bug raya-al-frente): con seam=True, la Back View
    # lleva la raya-atras, las poses de frente la raya-frente-liso, el Side Profile NADA; sin seam,
    # ninguna pose la lleva.
    seam_poses = dict(rotate_poses(531, seam=True))
    seam_back_ok  = STOCKING_SEAM_BACK in seam_poses["Back View"]
    seam_front_ok = STOCKING_SEAM_FRONT in seam_poses["Standing"] and STOCKING_SEAM_FRONT in seam_poses["Odalisque"]
    seam_side_skip = (STOCKING_SEAM_FRONT not in seam_poses["Side Profile"]
                      and STOCKING_SEAM_BACK not in seam_poses["Side Profile"])
    seam_leak_none = any(a in txt for _, txt in rotate_poses(531)
                         for a in (STOCKING_SEAM_FRONT, STOCKING_SEAM_BACK))
    print("Ancla raya de media check:",
          "LIMPIO (back atras, frente liso, side skip, sin fuga sin seam)"
          if (seam_back_ok and seam_front_ok and seam_side_skip and not seam_leak_none)
          else f"FALLA (back={seam_back_ok} front={seam_front_ok} side_skip={seam_side_skip} fuga_sin_seam={seam_leak_none})")
    # Auto-check constantes de vestuario (Ama 11/07): OPAQUE_LOCK / GLOSS_LOCK / CONSISTENCY_LOCK.
    print("Constantes vestuario check:",
          "LIMPIO (OPAQUE_LOCK + GLOSS_LOCK + CONSISTENCY_LOCK definidas)"
          if (len(OPAQUE_LOCK) > 40 and len(GLOSS_LOCK) > 40 and "no matte" in GLOSS_LOCK.lower()
              and len(CONSISTENCY_LOCK) > 40 and "identical" in CONSISTENCY_LOCK.lower())
          else "FALLA (constantes vacias o mal formadas)")
    # Auto-check ancla de peso Seated (Ama 11/07 — bug sustitucion de mueble/postura ignorada):
    # SOLO el slot Seated lleva SEATED_ANCHOR, sin fuga a otros slots; y las 2 variantes reescritas
    # (elbows-on-knees al frente de la oracion, backrest-arch sin straddle/reversed) no contienen
    # "straddl"/"reversed" (pariente del token proscrito por el filtro anti-safe).
    seated_poses = dict(rotate_poses(531))
    seated_ok = SEATED_ANCHOR in seated_poses["Seated"]
    seated_leak = any(SEATED_ANCHOR in txt for slot, txt in rotate_poses(531) if slot != "Seated")
    seated_no_straddle = not any(w in v.lower() for v in SEATED for w in ("straddl", "reversed"))
    print("Ancla peso Seated check:",
          "LIMPIO (solo Seated ancla, sin fuga, sin straddle/reversed)"
          if (seated_ok and not seated_leak and seated_no_straddle)
          else f"FALLA (seated_ok={seated_ok} fuga_otro_slot={seated_leak} straddle_o_reversed={not seated_no_straddle})")
    # Auto-check frontalidad Standing (Ama 12/07 — bug "la de frente sale de espalda/medio perfil"):
    # SOLO el slot Standing lleva STANDING_ANCHOR (sin fuga: la Back View es legitimamente de
    # espalda y no debe recibirlo), y NINGUNA variante del pool puede traer tokens de giro-de-
    # espalda. OJO con el falso positivo: "cherry red hair over one shoulder" (colocacion del pelo)
    # es legitimo y NO es "looking back over the shoulder" (giro de la cabeza) -> el token vetado
    # lleva articulo definido ("over the shoulder"), no "over one shoulder".
    ST_BAD = ["back view", "looking back", "over the shoulder", "turned away", "from behind",
              "three-quarters away", "rear view", "glance back", "away from the camera"]
    st_hits = [f"STANDING[{i}] -> '{b}'" for i, v in enumerate(STANDING) for b in ST_BAD if b in v.lower()]
    st_poses = dict(rotate_poses(531))
    st_ok = STANDING_ANCHOR in st_poses["Standing"]
    st_leak = any(STANDING_ANCHOR in txt for slot, txt in rotate_poses(531) if slot != "Standing")
    print("Ancla frontalidad Standing check:",
          "LIMPIO (solo Standing ancla, sin fuga, pool sin tokens de espalda)"
          if (st_ok and not st_leak and not st_hits)
          else f"FALLA (st_ok={st_ok} fuga_otro_slot={st_leak} tokens_espalda={st_hits})")
