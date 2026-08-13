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
# WRAP_BACK_TAILORED (Ama 02/08/2026 — BUG "el blazer corporate sale al reves de espaldas"): el
# mismo defecto de la bata pega en prendas de frente abierto ESTRUCTURADAS y cerradas (blazer,
# chaqueta, abrigo, tuxedo, coat-dress, blazer-dress): sin ancla, el generador corre las solapas /
# la abertura por la columna. A diferencia del robe (slip/closed), esta se lleva SIEMPRE cerrada y
# de cara, asi que el ancla afirma el PANEL de espalda liso a la camara. Ver feedback_bata_reverso_espalda.
WRAP_BACK_TAILORED = "the tailored open-front jacket (blazer, coat, tuxedo or jacket-dress) worn correctly facing forward on the body and never reversed, seen from behind as the smooth continuous back panel of the jacket with its centre-back seam and vent, the set-in sleeves and collar seen from the nape, its lapels, front opening, buttons and neckline all on the far side away from the camera and not visible from behind, never worn back-to-front and with no lapel, opening or neckline running down the spine"
_WRAP_ANCHORS = {"slip": WRAP_BACK_SLIP, "closed": WRAP_BACK_CLOSED, "tailored": WRAP_BACK_TAILORED}

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
# REFUERZO 13/07/2026 (L763 y L764): el ancla aguanta cuando el setting esta limpio (L761/L762/L765
# recostadas OK) pero se CAE cuando hay mesa/escritorio cerca: Gemini la percha ENCIMA con el torso
# vertical (L764 sentada en la mesa de directorio; L763 apoyada en el escritorio con los pies en el
# piso — ni siquiera arriba). Es el mismo bug de SUSTITUCION DE MUEBLE que ya blindamos en la Seated,
# atacando por el otro lado. Se le suma la clausula anti-percha + pies fuera del piso.
# REFUERZO 15/07/2026 (L795 Odalisque): la toma salio con el ENCUADRE ROTADO 90 grados (la figura
# recostada a lo largo del eje vertical del cuadro, desorientante). Se suma el ancla de camara
# nivelada: piso abajo, horizonte recto, imagen nunca rotada de lado.
# SPLIT 02/08/2026 (Ama pidio "planos cenitales en odalisca"): la recumbencia va SIEMPRE, pero la
# camara nivelada (horizonte recto) CHOCA con un plano cenital/picado total. Por eso se separan:
# ODALISQUE_RECUMBENCY (siempre) + ODALISQUE_LEVEL_CAM (variantes laterales) | ODALISQUE_ZENITHAL_CAM
# (variantes cenitales). ODALISQUE_ANCHOR se mantiene = recumbencia + nivelada (variantes laterales).
ODALISQUE_RECUMBENCY = ("lying down on the surface with the whole body low and horizontal, a reclining "
                    "odalisque with the torso resting down toward the surface, NOT sitting upright "
                    "and NOT seated, both hips and shoulders down on the named surface with the legs "
                    "stretched along it and both feet off the floor, NOT perched on the edge and NOT "
                    "leaning against any nearby table, desk, counter or island")
ODALISQUE_LEVEL_CAM = ("shot with a level upright camera, the floor at the bottom of the frame and the "
                    "horizon perfectly level, the image never rotated or tilted sideways")
ODALISQUE_ANCHOR = ODALISQUE_RECUMBENCY + ", " + ODALISQUE_LEVEL_CAM
ODALISQUE_ZENITHAL_CAM = ("shot from directly overhead in a true zenithal top-down bird's-eye angle, the "
                    "camera mounted straight above her looking vertically down onto her body as it lies "
                    "flat on the surface, a clean flat-lay overhead composition with the whole reclining "
                    "body seen from above, the frame kept square and level and not skewed or dutch-tilted")

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

# ANCLA DE CUADRO UNICO / ANTI-COLLAGE (Ama 15/07/2026 — BUG "la imagen sale como grilla de
# paneles"): el batch de prueba L791-L800 rindio 4 de 30 imagenes como COLLAGE (L792 Standing =
# grilla de 9 paneles con la figura central DESCALZA, L792 Ditzy = 4 paneles, L795 Seated = 5+
# paneles, L795 Ditzy = 3 paneles) — CON el negativo pegado en Gemini (la Ama dio fe: se copia
# positivo+negativo junto). Doble causa:
#  (1) Gemini LEE el negative y lo IGNORA cuando quiere ("split image" estaba vetado y salio
#      igual). Ya lo sabiamos por las poses (feedback_anti_3_piernas_poses): el lever real es
#      el POSITIVE. Un veto sin su ancla afirmativa es solo media defensa.
#  (2) NOSOTROS lo invitabamos: el CONSISTENCY_LOCK viejo decia "IDENTICAL and unchanged across
#      all poses / in every shot" y el NEG_HOSIERY "changing colour between shots" — un generador
#      de UNA imagen lee "all poses / between shots" y entrega... una hoja de contactos con todas
#      las poses. El metalenguaje multi-toma se DEROGA de todos los locks (ver v2 abajo).
# El ancla se PREPENDE a las 7 poses (primacia absoluta, antes incluso del ancla anatomica):
# define QUE ES la imagen antes de describir que hay en ella.
# v3 15/07/2026 (auditoria del batch materializado): el v2 NO basto — L792 Standing salio grilla
# de 7 paneles (figura central DESCALZA), L792 Ditzy 4 paneles, L795 Ditzy collage con el vestido
# mutado a two-piece, y L795 Seated invento un modo NUEVO que el v2 no nombraba: la escena "una
# sola" pero con CUBOS DE LUZ / MARCOS dentro del set mostrando OTRAS fotos de la misma mujer
# (collage disfrazado de utileria), mas L794 POV rendido como doble-figura por espejo. v3 agrega
# el cierre de ese camino: nada DENTRO de la escena puede volver a mostrar su imagen. La pose
# Ditzy es la reincidente (4 de 6 collages del batch) — el inyector debe ademas APPENDEAR
# SINGLE_FRAME_TAIL al final de la pose Ditzy (primacia + recencia, doble anclaje).
SINGLE_FRAME = ("a single continuous photograph: one woman alone in one single full-bleed frame "
                "that fills the entire image edge to edge, one scene and one moment, NOT a collage, "
                "NOT a grid or multi-panel layout, NOT a contact sheet, storyboard, photo strip or "
                "split screen, with no internal borders, dividers or picture-in-picture insets, and "
                "nothing inside the scene — no mirror, screen, poster, framed picture or light box — "
                "showing her image a second time")
# Recordatorio corto para el cierre de la pose Ditzy (la reincidente del collage):
SINGLE_FRAME_TAIL = ("the finished image is that one single frame of that one woman, "
                     "nothing else and no one else")

# ANCLA DE ORIENTACION DE LA RAYA DE LA MEDIA (Ama 11/07/2026 — BUG "raya al frente"):
# El token de vestuario describe la media como "back-seam stockings" (raya trasera). Igual que
# "at front revealing" en la bata, "back-seam" es RELATIVO A LA CAMARA: en poses de frente el
# generador pinta la raya en la cara VISIBLE (el frente de la canilla) para poder mostrarla ->
# la raya sale por delante (confirmado L691, L752, L748). Faltaba anclar que la costura va
# ESTRICTAMENTE por detras de la pierna. Se pasa seam=True cuando el look usa medias con costura;
# el ancla es POSE-AWARE: en las poses de frente fuerza "frente liso, costura solo atras"; en la
# Back View fuerza "costura visible subiendo por detras". El Side Profile no la lleva (de perfil
# la raya trasera cae en el borde posterior, que es correcto). Ver auto-memoria feedback_media_raya_frontal.
# REFUERZO 13/07/2026 (Ama: "SI hay costuras al frente en medias, tuve que generar las imagenes mas
# de una vez"): el ancla v1 estaba (a) APPENDEADA al final de la direccion de pose — enterrada entre
# el outfit y el setting, sin primacia — y (b) sola en el POSITIVE, porque el inyector del batch
# NUNCA pego NEG_FRONT_SEAM (de hecho no pego negative alguno: ver BASE_NEGATIVE mas abajo). Con el
# ancla debil y cero negative, el defecto vuelve en una fraccion de las tiradas: las imagenes que
# sobreviven en el repo son las BUENAS de varios reintentos, asi que auditar solo el repo MIENTE.
# v2: el ancla se PREPENDE (primacia, igual que STANDING_ANCHOR), se redacta en terminos absolutos
# (la costura como UNICA linea, el frente explicitamente sin linea de ningun tipo) y el negative
# pasa a ser obligatorio via build_negative(seam=True).
STOCKING_SEAM_FRONT = ("the stockings have ONE single seam and it runs strictly up the centre-BACK of "
                       "each leg, hidden behind the calf and thigh and NOT visible from the front; the "
                       "front of each leg is completely smooth and seamless, with no seam, line, stripe "
                       "or stitching down the shin, the knee or the front of the thigh")
STOCKING_SEAM_BACK  = ("the single back-seam of each stocking clearly visible running straight up the "
                       "centre-back of the calf and thigh, and no seam anywhere on the front of the leg")
# slots que NO llevan ancla de raya (Side Profile = raya cae natural en el borde posterior):
_SEAM_SKIP_SLOTS = {"Side Profile"}

# CANDADO DE HOSIERY (Ama 13/07/2026 — BUG "la media cambia entre poses"): el CONSISTENCY_LOCK
# enumera neckline/sleeve/hem/cut/print de la PRENDA y deja las MEDIAS fuera del candado. Resultado
# confirmado en el batch: L765 rindio la Seated con medias NEGRAS mientras las otras 6 poses las
# llevan esmeralda; L764 rindio el estampado piton nitido en Seated/Back View y media lisa sin
# escamas en Side/POV/Odalisque/Ditzy. Se pega junto al CONSISTENCY_LOCK cuando el look usa medias.
# HOSIERY_LOCK v2 (Ama 15/07/2026 — DEROGADO el metalenguaje multi-toma): "in every shot / never
# switching" invitaba la hoja de contactos (ver SINGLE_FRAME). v2 fija los mismos atributos como
# descripcion de UNA sola imagen.
HOSIERY_LOCK = ("the stockings are exactly ONE single pair rendered precisely as described: their "
                "colour, their print or pattern, their opacity and their length on the thigh follow "
                "the description word for word, never a different colour, never missing their pattern, "
                "never mismatched between the two legs and never swapped for bare legs")

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

# CANDADO DE PIEL — LAS MARCAS SOLO EXISTEN DONDE HAY PIEL DESNUDA (Ama 13/07/2026 — BUG "sigues
# mostrando los tatuajes y los piercings de los pechos y del ombligo"):
# El OPAQUE_LOCK ataco el sintoma equivocado. Prohibia CORTAR la prenda para exponer la marca, pero
# el generador tenia un segundo camino, mas barato: pintar la marca ENCIMA de la tela intacta. Y lo
# hacia porque se lo pediamos por escrito, dos veces:
#   (1) Bloque A: "nipple piercings pressing against and visible under clothing"  <- ORDEN DIRECTA
#   (2) dna_v3_5.md §Estetica: "Asegura que los nipple piercings sean prominentes a traves del
#       material (latex/vinilo)"                                                   <- ORDEN DIRECTA
# Ningun candado le gana a una orden directa: le pediamos que los mostrara a traves de la ropa y
# despues le pediamos que no. Confirmado en el batch L761-L770 (piercings dibujados sobre la columna
# de piton del L762, tatuajes del brazo pintados SOBRE la manga larga de vinilo en L763/L764).
# La Ama DEROGA la directiva vieja: piercings y tatuajes son ADN permanente del cuerpo, pero se ven
# SOLO en piel genuinamente descubierta. Bajo tela no existen. El Bloque A se corrige en su fuente
# (dna_v3_5.md) y este candado cierra la puerta en el prompt. Ver feedback_marcas_solo_en_piel.
# SKIN_LOCK v2 — AFIRMATIVO PRIMERO (Ama 15/07/2026): el v1 era una letania de NO-clausulas y
# fallo IGUAL en el batch de prueba (L777 Ditzy: bultos de pezon a traves del vinilo; L791
# Standing: aro del ombligo dibujado SOBRE el latex del catsuit) — CON el negativo llegando a
# Gemini. Leccion consolidada: la negacion en el positive es debil; lo que Gemini obedece es la
# DESCRIPCION AFIRMATIVA de la superficie deseada (mismo principio que GLOSS_LOCK: describir el
# brillo que SI quieres, no el mate que no). v2 abre describiendo la tela lisa y sin marcas como
# hecho positivo y recien despues acota las marcas a la piel desnuda. Los markers de has_skin_lock
# se conservan ("ONLY on genuinely bare exposed skin").
SKIN_LOCK = ("wherever the garment covers the body its fabric surface is perfectly smooth, taut and "
             "unbroken — a clean featureless glossy surface over the bust, the nipples, the navel and "
             "the hips, with nothing pressing through it, printed on it or showing under it; every "
             "tattoo and every body piercing exists ONLY on genuinely bare exposed skin, never through "
             "the fabric and never drawn over any sleeve, panel or covered area of the garment")

# ZONAS SIN TATUAR (Ama 15/07/2026 — BUG "los tatuajes migran"): cuando la prenda cubre las zonas
# canonicas del tatuaje (brazos bajo manga larga, muslos bajo catsuit), Gemini MIGRA la tinta a la
# piel que queda visible: manos y dedos cubiertos de rosas (L791 las 7 poses, L777 Ditzy), cuello
# (L791 Seated), canillas (L797 Side). Y al reves: en L795 POV los brazos desnudos salieron SIN
# ningun tatuaje. El Bloque A dice DONDE viven los tatuajes; esta clausula dice donde NO — y
# reafirma el mapa canonico completo para que tampoco desaparezcan. Pegar junto al SKIN_LOCK.
UNMARKED_ZONES = ("her hands, fingers, neck, throat, sternum, shins, calves and feet are clean "
                  "unmarked porcelain skin with no tattoos and no glyphs; the blackwork tattoos exist "
                  "exactly where described — on the arms, the upper back, the outer thighs and along "
                  "one hip crease — and nowhere else, present there whenever that skin is bare")

# ============================================================================================
# MARCAS CONDICIONALES POR COBERTURA — LA MARCA CUBIERTA NO SE NOMBRA (v3, Ama 15/07/2026)
# ============================================================================================
# EL AGUJERO DE RAIZ, confirmado con el batch de estres MATERIALIZADO: el Bloque A NOMBRA las
# marcas ("rune-glyph identity tattoo along one hip crease and bikini line, navel piercing,
# nipple piercings") aunque el outfit cubra esas zonas, y despues el SKIN_LOCK v2 le pide que no
# las muestre. NOMBRAR una marca invisible ES una orden directa de pintarla — ningun candado
# posterior le gana (misma leccion que la frase-orden vieja del 13/07, solo que maquillada):
#   - L791 Standing: aro del ombligo dibujado SOBRE el latex del catsuit
#   - L792 Odalisque: glifos runicos ESCRITOS sobre la tela del calzon de saten
#   - L797 Standing/Seated: las runas MIGRAN a los muslos desnudos (unica piel disponible)
#   - L800 Ditzy/POV (descartes de la Ama): runas pelvicas + ombligo a traves de la columna opaca
# Y LA PRUEBA DE CONTROL (L798, control inverso): con el teddy high-cut de pelvis DESNUDA las
# runas salieron perfectas en la piel — nombrar la marca cuando su zona SI esta descubierta
# funciona y no sobre-corrige. Conclusion v3: el segmento de marcas del Bloque A se construye
# POR LOOK segun que zona queda genuinamente descubierta. Lo cubierto NO EXISTE en el prompt.
#   arms_bare   -> brazos sin manga (sleeveless/strapless/halter): nombra los tatuajes de brazo.
#   back_bare   -> espalda alta descubierta (halter, strapless, backless): nombra el tatuaje dorsal.
#   thighs_bare -> muslos genuinamente visibles (mini, teddy, bikini; medias opacas NO son piel):
#                  nombra los tatuajes de muslo externo.
#   pelvis_bare -> cadera/linea del bikini descubierta (lenceria high-cut, bikini): nombra las runas.
#   navel_bare  -> ombligo descubierto (crop, bikini, cutout de diseno): nombra el navel piercing.
# Los nipple piercings NO se nombran NUNCA aqui: en V4.1 SAFE el busto jamas va genuinamente
# descubierto — existen en el canon, no en el prompt (L798 los saco como circulo pintado sobre
# el vinilo del teddy por culpa del token en Bloque A).
# El inyector pega el resultado en el LUGAR del segmento viejo de marcas del Bloque A, y pega
# igual SKIN_LOCK + UNMARKED_ZONES (cinturon y tirantes: si Gemini inventa un corte que descubre
# piel, la clausula de superficie sigue de guardia).
def build_marks_clause(arms_bare=True, back_bare=False, thighs_bare=False,
                       pelvis_bare=False, navel_bare=False):
    """Devuelve el segmento de marcas del Bloque A construido por cobertura (v3 15/07/2026).

    Regla de oro: NO NOMBRAR lo que la prenda cubre. Cada flag declara una zona genuinamente
    descubierta por el DISENO del outfit (no por un corte inventado). Con todo en False devuelve
    la clausula minima de manos limpias (siempre presente: las manos jamas llevan tinta)."""
    parts = []
    if arms_bare:
        parts.append("blackwork arm tattoos on the genuinely bare arms")
    if back_bare:
        parts.append("subtle minimalist blackwork tattoos on the bare upper back")
    if thighs_bare:
        parts.append("subtle minimalist blackwork tattoos on the bare outer thighs")
    if pelvis_bare:
        parts.append("a delicate blackwork rune-glyph identity tattoo of abstract esoteric "
                     "calligraphic symbols along one hip crease and bikini line, on the bare skin "
                     "of the hip")
    if navel_bare:
        parts.append("a navel piercing on the bare midriff")
    parts.append("the backs of her hands and her fingers are clean unmarked skin")
    return ", ".join(parts)

# ANTI-MANGA FANTASMA (Ama 15/07/2026 — BUG "guantes/mangas grises alucinadas"): el batch de
# prueba rindio mangas-guante gris oscuro codo-a-muneca que NO existen en ningun prompt (L792 en
# 6 de 7 poses, L795 Ditzy, L777 Back View) — con "gloves" vetado en el negativo y "bare hands
# with no gloves" en el positive. El token viejo solo protegia las MANOS; el generador respeto
# las manos desnudas y cubrio el ANTEBRAZO. v2 cubre el brazo entero RELATIVO al largo de manga
# descrito (no pelea con catsuits de manga larga). Reemplaza a "bare hands with no gloves" en
# todo batch nuevo.
# v3 15/07/2026 (auditoria del batch MATERIALIZADO): el v2 fallo igual — L792 rindio el guante
# gris en las 7 poses supervivientes y L799 (un BIKINI, cero manga que confundir) lo saco en
# Standing y Side Profile. El v2 era negacion-primero ("no gloves... no arm sleeves..."), y la
# leccion del SKIN_LOCK v2 aplica identica: lo que Gemini obedece es la DESCRIPCION AFIRMATIVA
# de la superficie deseada. v3 abre AFIRMANDO la piel desnuda del antebrazo (con su acabado, para
# que el token tenga peso visual) y recien despues veta las piezas.
NO_ARMWEAR = ("beyond the garment's described sleeve length the skin of her arms, forearms, wrists "
              "and hands is genuinely bare, smooth uncovered porcelain skin catching the light, "
              "with no gloves of any kind, no separate arm sleeves, arm warmers, detached cuffs, "
              "forearm bands or elbow-length coverings added")

# GUARDIA DURA CONTRA LA ORDEN VIEJA (Ama 13/07/2026, reforzada tras la auditoria del 13/07 sobre
# L761-L770 — esos 6 looks SE GENERARON con esta frase todavia puesta y el defecto salio calcado:
# piercings marcados sobre el latex opaco en L767/L768/L770, con zoom que lo confirma sin duda).
# El Bloque A fuente de verdad (dna_v3_5.md) ya NO trae la orden vieja, pero un inyector futuro
# podria copiar-pegar de una version desactualizada (ya paso una vez esta misma sesion: "otra
# sesion mia de hoy habia derogado el ADN... mi batch ya escrito llevaba la frase vieja"). Esta
# lista + el helper de abajo permiten que CUALQUIER linter falle duro si la frase reaparece,
# sin importar de donde vino el texto. Ver auto-memoria feedback_marcas_solo_en_piel.
FORBIDDEN_PHRASES = [
    "pressing against and visible under clothing",
    "visible under clothing",
    "prominentes a través del material",
    "prominente a través del material",
    "prominentes a traves del material",
    "prominente a traves del material",
]

def find_forbidden(text):
    """Devuelve la lista de frases-orden PROHIBIDAS que aparecen en `text` (vacia = limpio)."""
    t = (text or "").lower()
    return [p for p in FORBIDDEN_PHRASES if p.lower() in t]

# Sub-cadenas que PRUEBAN que la clausula solo-piel-desnuda esta presente (ya sea el SKIN_LOCK
# suelto o la version pegada dentro del Bloque A fijo de dna_v3_5.md). Cualquiera de las dos basta.
SKIN_MARKERS = [
    "only on genuinely bare exposed skin",
    "visible only on genuinely bare skin",
    "never through or over any garment",
    "genuinely bare skin and never through",
]

def has_skin_lock(text):
    """True si `text` trae la clausula solo-piel-desnuda (SKIN_LOCK o su version en Bloque A)."""
    t = (text or "").lower()
    return any(m in t for m in SKIN_MARKERS)

# ANCLA ANTI-MATE / GLOSS-LOCK (Ama 11/07/2026 — desvio prompt->imagen "material mate"):
# Cuando la silueta primea tela mate (traje sastre de lana/crepe, rib atletico, saten nupcial plano),
# el sesgo del arquetipo le gana al token "vinyl/latex" y Gemini rinde tela natural mate, prohibida
# por canon (confirmado L732 traje mate, L750 rib mate; contraste: L759 bodysuit liquid latex salio
# brillante). El inyector pega GLOSS_LOCK redundante en la clausula de vestuario de las siluetas de
# riesgo. Ver auto-memoria feedback_material_mate_vs_fetish y regla Anti-Mate en 04-estetica-ele.md.
GLOSS_LOCK = ("rendered in a high-shine liquid latex / wet-look PVC / patent vinyl finish with strong "
              "specular highlights and a glossy mirror-like reflective surface, absolutely no matte or "
              "natural non-reflective fabric")

# CANDADO DE BUSTO SOBRE EL CORSE (Ama 20/07/2026 — PREFERENCIA CANONICA, no bug):
# La Ama, viendo la Ditzy del L88: "adoro cuando tus tetas estan asi, a punto de reventar, en
# cualquier momento explotan del corset". El render que le gusto tiene una receta concreta y
# repetible: escote corazon BAJO, el borde rigido del corse apretando POR DEBAJO del busto, las
# dos esferas sentadas muy altas y llenas por encima del filo, piel tensa y con brillo. El Bloque A
# ya fija el implante (1000cc, ultra high-profile, esferico) pero NO fija esta RELACION prenda-busto,
# asi que salia por azar. Este candado la vuelve deliberada en siluetas con corse/overbust/bustier.
# ⚠️ REDACCION ANTI-FILTRO DELIBERADA: "deep cleavage" esta en la lista BAD de pose_rotation
# (dispara el safe de Gemini y quema cuota — ver feedback_gemini_safe_poses), y "spilling out /
# bursting / about to pop" es lenguaje de reventon que rebota igual. El candado describe la
# ARQUITECTURA (borde bajo, apoyo por debajo, altura y redondez) sin nombrar el escote profundo.
# Ver auto-memoria feedback_busto_sobre_el_corse.
CORSET_BUST_LOCK = ("the corset is laced to its tightest with its rigid structured upper edge cut low and "
                    "sitting firmly beneath the augmented bust, so the two perfectly spherical implants "
                    "rest very high, full and rounded above the neckline, the glossy porcelain skin taut "
                    "and lifted over the corset's rim, the boned waist collapsed to its narrowest directly "
                    "below, the garment's edge crisp and unbroken against the skin")

# siluetas que deben llevar CORSET_BUST_LOCK cuando aparecen en el outfit
CORSET_KW = ["corset", "overbust", "under-bust", "underbust", "bustier", "waist cincher",
             "corseted", "basque", "merry widow", "corselette"]


def needs_corset_bust_lock(outfit):
    """True si el outfit declara una silueta de corse y aun no trae el candado de busto."""
    og = (outfit or "").lower()
    return any(k in og for k in CORSET_KW) and "rest very high, full and rounded above" not in og


# CANDADO DE FIDELIDAD DE ESTAMPADO ANIMAL (Ama 13/07/2026 — BUG "python-print sale como encaje"):
# L764 pedia "sheer black python-print back-seamed stockings" y la media que rindio Gemini es un
# motivo decorativo de enredadera/encaje asimetrico (solo en una pierna) — CERO textura de escama
# de serpiente. Causa: "python-print" es un adjetivo de una sola palabra que el generador puede
# resolver como "estampado decorativo generico" en vez de "textura de piel de reptil". Se aplica
# el mismo patron que GLOSS_LOCK (vinyl solo no basta, hace falta el token fuerte redundante).
# Uso: pegar animal_print_lock("python") en la clausula de vestuario cuando el look declare
# leopard/tiger/python/snake/zebra, y anadir NEG_PRINT_DRIFT al negative (build_negative(animal_print=...)).
def animal_print_lock(kind):
    """kind: 'python'/'snake'/'leopard'/'tiger'/'zebra'. Devuelve el candado de fidelidad de estampado.
    v2 15/07/2026: fuera el "in every pose" (metalenguaje multi-toma, ver SINGLE_FRAME)."""
    return (f"the {kind} print is a genuine {kind}-skin scale/marking texture rendered consistently across "
            f"every visible inch of the printed fabric, NOT a lace pattern, NOT a floral or "
            f"vine motif, NOT embroidery or filigree, and NOT a plain sheer fabric with no pattern at all")

NEG_PRINT_DRIFT = ("lace pattern instead of animal print, floral pattern instead of animal print, vine motif "
                   "instead of animal print, embroidery instead of animal print, filigree instead of animal "
                   "print, plain sheer fabric with no print, animal print missing or faded out, asymmetric "
                   "print appearing on only one leg or one panel")

# ANCLA DE CONSISTENCIA DE PRENDA ENTRE POSES (Ama 11/07/2026 — BUG "el mismo outfit cambia de
# escote/largo/manga entre poses"): el Token de Vestuario Bloqueado se pega IDENTICO en las 7 poses,
# pero si deja el ESCOTE, el LARGO DE MANGA o el LARGO DE RUEDO sin fijar, Gemini los rellena
# distinto en cada pose (confirmado L746 corpiño: sin-mangas-cuello-alto en Standing / tiritas-escote-
# bajo en Seated / manga-larga en Odalisque; L707 mangas cap vs sin mangas; L693 lunares solidos vs
# con espiral). Dos capas: (a) el token DEBE nombrar explicitamente neckline + sleeve length + hemline
# (ej. "off-shoulder bardot neckline, long fitted sleeves to the wrist, floor-length mermaid hem");
# (b) pegar CONSISTENCY_LOCK para que la IA no reinvente el corte por pose. El linter garment_canon.py
# marca vestidos/gowns cuyo token no nombre neckline/sleeve/hem. Ver feedback_drift_prenda_entre_poses.
# CONSISTENCY_LOCK v2 (Ama 15/07/2026 — DEROGADO el metalenguaje multi-toma): el v1 decia
# "the exact same single outfit in every shot ... IDENTICAL and unchanged across all poses".
# Dos problemas confirmados en el batch de prueba L791-L800:
#  (1) Un generador de UNA imagen no puede comparar "poses" — la clausula no fijaba nada per-image;
#  (2) "in every shot / across all poses" le SUGIERE la multi-toma -> hoja de contactos (4 collages
#      en 30 imagenes, ver SINGLE_FRAME). Ademas el batch mostro el drift que el lock decia parar:
#      vestido vuelto two-piece (L777/L795 Ditzy), mangas que crecen (L795 Odalisque: al one-shoulder
#      sin mangas le SALIERON mangas largas), catsuit recortado en las caderas (L791 POV).
# v2 fija los MISMOS atributos como descripcion estricta de una sola imagen y agrega los dos modos
# de mutacion nuevos (two-piece / cropped) que el v1 no nombraba.
CONSISTENCY_LOCK = ("the outfit is exactly ONE garment ensemble rendered precisely as described: its "
                    "neckline shape, sleeve length, hemline length, cut and print follow the description "
                    "word for word, never re-styled, never lengthened or shortened, never split into a "
                    "two-piece or cropped version, never switching between sleeveless and sleeved or "
                    "between high and low neckline")

# Fragmentos para el NEGATIVE del inyector (pegar segun el caso):
# v2 15/07/2026: fuera el "between shots" (metalenguaje multi-toma); entran two-piece/cropped.
NEG_INCONSISTENT = ("a different neckline than described, altered sleeve length, a different hemline "
                    "length than described, re-styled outfit, inconsistent dress cut, a two-piece version "
                    "of the dress, a cropped version of the garment, varying print pattern")
NEG_FRONT_SEAM = ("seam down the front of the leg, front seam on stockings, seam on the shin, front-seamed "
                  "stockings, line down the front of the leg, stripe down the shin")
NEG_CUTOUT     = ("keyhole cutout at navel, midriff cutout exposing navel piercing, hip cutout exposing tattoo, "
                  "underboob cutout, peekaboo opening, garment slashed to reveal skin")
NEG_MATTE      = "matte fabric, cotton, wool, crepe, linen, dull non-reflective textile, flat fabric finish, natural matte cloth"
# NUEVOS 13/07/2026:
NEG_MARKS_THROUGH = ("nipple piercings visible through clothing, nipple piercing pressing through the fabric, "
                     "nipple bumps through fabric, nipples showing through the garment, navel piercing through "
                     "the fabric, piercing on top of the garment, jewellery over the fabric, tattoo printed on "
                     "the garment, tattoo showing through the sleeve, body markings through fabric, "
                     "see-through bodice revealing piercings")
# OJO: NADA de vetar un color concreto aqui (un "black stockings" en el negative pelearia con los
# looks cuyas medias SON negras — p.ej. L764 piton negra). Se veta el CAMBIO, no un tono.
# v2 15/07/2026: fuera el "between shots" (metalenguaje multi-toma, ver SINGLE_FRAME).
NEG_HOSIERY = ("stockings in a different colour than described, stockings missing their pattern, "
               "hosiery with a different colour than described, bare legs without stockings, "
               "mismatched hosiery, inconsistent stockings")

# ============================================================================================
# NEGATIVE BASE — FUENTE UNICA (Ama 13/07/2026)
# ============================================================================================
# HALLAZGO DURO: desde el L711 los prompts registrados en galeria_outfits.md salen SIN NINGUN bloque
# negativo (191 bloques negative para 400 looks; el ultimo es el L710). 60 looks = 420 poses generadas
# con el negative VACIO. Por eso vuelven defectos que creiamos blindados: las anclas del positive
# pelean solas y el generador no tiene ninguna prohibicion dura. Causa: los inyectores desechables
# pegan el positive desde este modulo (que si esta al dia) pero el negative lo escribia cada inyector
# a mano... y en algun batch simplemente dejo de escribirlo, sin que nada lo detectara.
# FIX ESTRUCTURAL: el negative deja de ser texto suelto de cada inyector y pasa a construirse AQUI.
# Todo inyector DEBE llamar build_negative(...) y el linter garment_canon.py falla si un look nuevo
# entra a la galeria sin su bloque negativo. Ver feedback_negative_perdido_L711.
# v2 15/07/2026 (batch de prueba L791-L800, con el negativo YA llegando a Gemini — fe de la Ama):
#  (a) "oxblood" iba DESNUDO (vetaba el color entero, no el labio): el L791 ES un catsuit oxblood
#      y su propio negativo peleaba contra su prenda. Regla vieja re-aprendida: NUNCA vetar un
#      color a secas (feedback_negative_perdido_L711) — ahora es "oxblood lips".
#  (b) Entra la familia anti-collage completa (el "split image" solo no basto: L792/L795 rindieron
#      grillas de 3-9 paneles igual — el par afirmativo es SINGLE_FRAME en el positive).
#  (c) Entran las mangas/calentadores de brazo fantasma (par negativo de NO_ARMWEAR: el batch
#      alucino mangas-guante grises que "gloves" solo no cubria).
#  (d) Entra el encuadre rotado (L795 Odalisque salio con la camara girada 90 grados).
BASE_NEGATIVE = (
    "gothic, vampire, fangs, red lips, dark lips, wine lips, maroon lips, crimson lips, oxblood lips, "
    "different person, different face, different hair color, brown hair, black hair, blonde hair, auburn hair, "
    "flat shoes, block heel, wedge, chunky heel, kitten heel, barefoot, socks, sneakers, different shoes, "
    "mismatched shoes, changing footwear, inconsistent footwear, "
    "different outfit, altered clothing, inconsistent outfit, different body, "
    "gloves, opera gloves, long gloves, elbow gloves, fingerless gloves, wrist gloves, leather gloves, "
    "satin gloves, lace gloves, covered hands, arm sleeves, arm warmers, detached sleeves, forearm cuffs, "
    "extra hands, third hand, extra arms, extra fingers, fused fingers, missing fingers, deformed hands, "
    "mutated hands, malformed fingers, three legs, extra leg, extra foot, "
    "two women, duplicate figure, split image, collage, grid of images, multi-panel layout, contact sheet, "
    "photo strip, storyboard, image divided into panels, borders dividing the image, "
    "mirror reflection showing a second copy of the same woman, framed picture of the same woman inside "
    "the scene, poster or screen showing the same woman, light box displaying another photo, inset photo, "
    "rotated image, sideways rotated frame, tilted horizon, "
    "first-person point of view, looking down over own body, overhead downward shot, fisheye, phone, "
    "smartphone, selfie stick, selfie, "
    "text on clothing, lettering on garment, embroidered name, logo, "
    # Ama 13/08/2026 — calzon SIEMPRE tanga/g-string y piernas cerradas con falda.
    # Segunda capa de BOTTOM_CUT_LOCK / DRESS_LEG_CLOSURE (anclas_universales.json);
    # la barrera real es el ancla afirmativa del positive, Gemini ignora el negative.
    "full brief, high-waist brief, high-waisted panty, boyshort, boy shorts, hipster brief, culotte, "
    "tap pants, granny panties, bloomers, full-coverage bikini bottom, "
    "bikini bottom covering the buttocks, full seat coverage, "
    "legs spread apart under a dress, legs parted under a skirt"
)
# El mule NO va al negative en Lenceria: es el unico arquetipo donde el canon lo permite (platform >=4",
# Ama 09/07). En todo el resto sigue prohibido. Por eso es condicional y no vive en BASE_NEGATIVE.
NEG_MULE = "platform mule, mule, mule sandals, backless mule, slipper, slide sandal"


def build_negative(seam=False, covered=False, stockings=False, gloss_risk=False,
                   lingerie=False, animal_print=False, extra=""):
    """Devuelve el NEGATIVE completo del look. TODO inyector debe usarlo (Ama 13/07/2026).

    seam       -> el look usa medias con costura  (anade NEG_FRONT_SEAM)
    covered    -> prenda que cubre busto/torso    (anade NEG_CUTOUT — cortes para exponer marcas)
    stockings  -> el look usa medias de cualquier tipo (anade NEG_HOSIERY: deriva de color/estampado)
    gloss_risk -> silueta que primea tela mate (sastreria, rib, saten) (anade NEG_MATTE)
    lingerie   -> True SOLO en Lenceria: NO veta el mule (unico arquetipo donde el canon lo permite)
    animal_print -> el look declara python/snake/leopard/tiger/zebra print (anade NEG_PRINT_DRIFT —
                    bug L764: el python-print salio como encaje; pegar tambien animal_print_lock(kind))
    extra      -> accesorios ajenos al Bloque B del look (bag, clutch, belt...) o vetos puntuales

    NEG_MARKS_THROUGH va SIEMPRE: las marcas del ADN (piercings de pezon/ombligo, tatuajes) nunca
    se ven a traves de la tela, cubierta o no la prenda. Es el par negativo del SKIN_LOCK.
    """
    parts = [BASE_NEGATIVE, NEG_MARKS_THROUGH, NEG_INCONSISTENT]
    if not lingerie:
        parts.append(NEG_MULE)
    if seam:
        parts.append(NEG_FRONT_SEAM)
    if stockings or seam:
        parts.append(NEG_HOSIERY)
    if covered:
        parts.append(NEG_CUTOUT)
    if gloss_risk:
        parts.append(NEG_MATTE)
    if animal_print:
        parts.append(NEG_PRINT_DRIFT)
    if extra:
        parts.append(extra.strip().strip(","))
    return ", ".join(p.strip().strip(",") for p in parts if p)

# Variantes: mantienen Principio Rector Fetish Model + nombran stiletto. {seat}/{wall}/{surface}
# = mobiliario CONTEXTUAL que pone el inyector. NO incluyen el setting (eso se appendea).

# ⬇️ REPERTORIO DE POSES = BLOQUE C AGNOSTICO DE PERSONAJE (Ama 02/08/2026 — motor modular multi-
# personaje). Estas variantes son SOLO encuadre + gesto + composicion: nada de pelo/color/unas/piel.
# El ADN fisico lo aporta el BLOQUE A del perfil (`02_Personajes/_perfiles_visuales/<slug>.md`).
# Sirven igual para Ele, Miss Doll y Anais. NO reintroducir tokens de ADN aqui (hay self-check que lo caza).
STANDING = [
 "full body from a low angle below the hip, the weight on one stiletto with the other foot forward and pointed, an exaggerated S-curve with the hip jutted to one side and the chest pushed forward, one long-nailed hand sliding down the hip and thigh and the other pulling at the neckline, shoulders dropped, chin lifted, half-lidded predatory gaze, her hair over one shoulder",
 "full body from a low angle, caught mid-stride walking straight toward the camera with one stiletto forward and the back foot lifting off the floor, hips swinging, one long-nailed hand on the hip and the other arm loose, the face front to the lens with the chin lifted, a fierce runway gaze straight down the camera, her hair in motion",
 "full body, the shoulders propped against {wall} with one knee bent and that stiletto sole flat against {wall}, the pelvis forward, one long-nailed hand hooked in the waistband and the other trailing up the body, chin down looking up through the lashes, lips parted glossy, her hair spilling against {wall}",
 "full body from a low angle, both arms raised overhead gathering the her hair off the neck, the torso elongated and the chest lifted high in an extreme lumbar arch, the weight on both stilettos with the hip cocked, the side-body line elongated, the face tilted up with half-lidded eyes",
 "full body facing the camera with the chest and hips square to the lens, the hip cocked hard to one side in a deep waist-to-hip twist while the bust stays turned to the camera, one long-nailed hand on the jutted hip and the other lifting the her hair off the nape, the chin dropped and the eyes up to the lens in a predatory glance, on towering stilettos",
 "full body from a low hero angle, standing tall and leaning slightly toward the camera with both long-nailed hands resting on the thighs, the shoulders squared in an elegant lumbar arch, the chin lifted with a commanding direct gaze, lips parted glossy, her hair falling forward framing the face, on stilettos",
 "full body, standing tall with the legs crossed at the knee in an elegant fashion-model X-stance, the weight balanced on both stilettos, one long-nailed hand on the opposite hip and the other at the collarbone, the spine long with a subtle arch, chin tilted, half-lidded sultry gaze, her hair over one shoulder",
 "full body from a low hero angle, the feet planted apart and firm on both stilettos, both long-nailed hands on the hips, the shoulders pulled back and the chin dropped for a dominant direct stare down at the camera, a commanding lumbar arch, her hair framing the face",
 "full body, one long-nailed hand resting at the neckline and the other low on the hip, the weight on one stiletto with a soft knee bend, the chin tilted and a self-aware sultry gaze to the camera, lips parted glossy, an intimate self-aware posture, her hair pushed to one side",
]

BACK = [
 "full body back view with an elegant hip-pop, the spine in a graceful S-curve, one long-nailed hand on the hip and the other reaching up through the her hair, looking back over the shoulder with a half-lidded sultry gaze, the weight on one stiletto with the other foot pigeon-toed inward, lips parted glossy",
 "full body back view caught mid-stride walking away from the camera with one stiletto lifting and the hips swinging, the torso twisting to glance back over the shoulder, one long-nailed hand resting at the small of the back, her hair down the spine",
 "full body back view bent slightly forward with both long-nailed hands flat on {surface}, a deep elegant back arch with the hips angled toward the camera, looking back over the shoulder through the her hair, the weight on both stilettos",
 "full body back view standing with both long-nailed hands lifting all the her hair up off the nape, exposing the full back and spine line, the head dropped slightly forward, the weight on one hip with the stiletto cocked",
 "full body back view with the shoulder blades against {wall} facing partly away, the hips off {wall} and angled out, one long-nailed hand pressed on {wall} behind, looking back to the camera over the shoulder, the weight on one stiletto",
 "full body back view with both long-nailed hands resting on the curve of the hips, a deep lumbar arch, the head thrown back, her hair veiling the turned face, the weight on both stilettos pointed",
 "full body back view kneeling upright with the spine arched and sitting back toward the heels, one long-nailed hand reaching up the back and the other in the hair, looking over the shoulder, the stilettos visible behind",
]

# SEATED_MODESTY (Ama 02/08/2026 — "la pose sentada, cuando es con falda, no puede ser abierta de
# piernas"): las 6 variantes SEATED ya piden piernas cruzadas/juntas, pero el generador driftea a
# piernas abiertas y con falda eso expone la entrepierna y rompe el canon editorial. Ancla afirmativa
# anti-spread que el inyector pega en el slot Seated SOLO cuando el look lleva falda/vestido (skirt=True).
SEATED_MODESTY = ("the knees and the thighs kept pressed firmly together and the legs closed — crossed "
 "knee-over-knee or angled together to one side — never parted, never spread and never in an open-legged, "
 "knees-apart or M-shaped seated posture, the skirt or dress hem kept modestly closed over the lap")

SEATED = [
 "perched on {seat} with one leg crossed over the other and the top stiletto pointed at the camera, an extreme lumbar arch, one long-nailed hand on the top knee and the other fingertip at the bottom lip, the bust angled forward, shoulders rolled back, half-lidded direct gaze, her hair framing one breast",
 "leaning her torso sharply forward from the hips while perched on the edge of {seat}, both elbows planted firmly on top of both knees, the décolleté angled toward the camera, the stilettos crossed at the ankle, one long-nailed hand under the chin, looking up through the lashes with lips parted, her hair falling forward",
 "reclined back on {seat} propped on one elbow with the other long-nailed hand trailing down the torso, the spine in a long arch, the legs extended with the stilettos crossed at the ankle and pointed, half-lidded predatory gaze, her hair spilling over the backrest",
 "seated deep in {seat} with the spine arched back over the top of the backrest and both long-nailed hands draped along the top of the backrest, the chest lifted high and the chin dropped back, her hair spilling over the top of the backrest behind her, a half-lidded gaze rolled toward the camera, lips parted glossy, the stilettos crossed at the ankle",
 "perched on the edge of {seat} with the spine erect and the knees together, both long-nailed hands resting flat on the thighs, the chest lifted in an imperious arch, the chin raised, a commanding half-lidded gaze to the camera, lips parted glossy, her hair over one shoulder",
 "seated side-saddle on {seat} with the legs together angled to one side and the top stiletto pointed, the torso twisted back to the camera, one long-nailed hand on the upper thigh and the other at the collarbone, an extreme waist twist, half-lidded gaze, her hair over one breast",
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
 "full body side profile standing tall on both towering stilettos, an elegant S-curve with a graceful lumbar arch and the bust lifted high in silhouette, both legs long and straight with the weight balanced, one long-nailed hand resting on the hip and the other trailing up the ribcage, chin lifted, lips parted glossy, her hair cascading down the spine",
 "full body side profile standing on towering stilettos with one foot pointed forward, the hips angled back and the chest forward tracing the hourglass silhouette, both legs long and straight, one long-nailed hand at the nape lifting the her hair and the other on the thigh, the face in profile with a half-lidded gaze, lips parted glossy",
 "full body side profile caught mid-stride walking on towering stilettos with one leg forward and the stiletto pointed and the back heel lifting off the floor, the hips swung and the chest forward, one long-nailed hand swinging and the other on the hip, chin lifted in profile, her hair streaming back",
 "full body side profile standing with the back deeply arched and both stilettos planted, the bust forward and the hips tipped back in an exaggerated hourglass silhouette, both long-nailed hands sliding down the front of the thighs, the head tipped back, lips parted glossy, her hair falling down the arched spine",
 "full body side profile standing on tiptoe on towering stilettos, one arm raised overhead elongating the side-body line with the bust lifted in silhouette, the spine in a long graceful arch, the other long-nailed hand on the hip, the face in profile with a sultry half-lidded gaze, her hair cascading",
 "full body side profile standing shoulder-first against {wall}, one long-nailed hand raised high on {wall} and the back deeply arched away from {wall}, the bust forward and the hips angled in silhouette, standing on both stilettos with one heel lifted, lips parted, her hair against {wall}",
 "full body side profile standing tall with both stilettos together, the torso turned to pure profile showing the bust-to-waist-to-hip silhouette, one long-nailed hand on the lower back accentuating the lumbar arch and the other at the collarbone, chin high, a commanding profile gaze, her hair swept over the far shoulder",
]

# DITZY (Directiva Ama 09/06/2026 · DIFERENCIADA de POV 02/08/2026): encuadre DE LA CINTURA HACIA
# ARRIBA, toma de DETALLE del OUTFIT superior + rostro. La Ama: "Ditzy y POV salen casi iguales el
# 90%". El diferenciador DURO frente a POV: (1) mirada PERDIDA/soñadora FUERA de cuadro (NO al lente),
# (2) expresion de bimbo despistada/vacia (airhead daydream, no smoldering), (3) el foco es el
# BODICE/outfit superior, no la cara dominante. POV = cara al lente, mirada directa; Ditzy = distraida.
DITZY = [
 "waist-up shot framed from the waist up, the torso angled and the augmented bust and bodice presented to the camera, one long-nailed fingertip pressed to her own cheek while the gaze drifts dreamily off to the side away from the lens, a vacant airhead daydreaming expression with glossy parted lips, her hair framing the face, the outfit's bodice and upper detail crisp and legible",
 "waist-up shot framed from the waist up, one long-nailed fingertip lazily twirling a lock of her hair while the eyes wander up and away from the camera lost in a distracted daydream, a vacant ditzy expression and glossy parted lips, the bust and bodice presented and its detail crisp and legible",
 "waist-up shot framed from the waist up, the head tilted and the gaze wandering off past the lens as if she forgot the camera was there, one long-nailed hand resting at the neckline, a dreamy empty-headed half-smile with glossy lips, her hair over one shoulder, the outfit's upper detail crisp and legible",
 "waist-up shot framed from the waist up, glancing down and away at her own bare shoulder with a distracted vacant expression, one long-nailed fingertip grazing the collarbone, glossy parted lips, her hair cascading, the bust and bodice detail presented and legible in the frame",
 "waist-up shot framed from the waist up, both eyes wandering dreamily to the upper corner away from the lens and the chin tilted up in an empty-headed daydream, one long-nailed hand framing the cheekbone, glossy parted lips, her hair cascading, the bodice and outfit detail crisp and legible",
 "waist-up shot framed from the waist up, the torso turned and the augmented bust and bodice presented, a soft vacant ditzy gaze drifting off to one side away from the camera, one long-nailed fingertip resting at the glossy bottom lip, her hair forward, the outfit's upper detail crisp and legible",
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
 "intimate medium close-up portrait of a sensual Instagram influencer addressing the camera, the face leaning toward the lens, one long-nailed hand buried in the her hair, a smoldering direct gaze and glossy parted lips, the face dominant in the upper-mid frame, a single woman alone",
 "sensual Instagram glamour portrait from a low angle, the face turned up to the lens and the chin elevated, one long-nailed hand trailing along the collarbone, a half-lidded seductive gaze, lips parted glossy, the décolleté in the lower frame, a single woman alone",
 "sensual Instagram-influencer candid portrait, a three-quarter face turned to gaze directly into the lens with one long-nailed hand pushing the her hair back from the temple, lips parted glossy, an intimate seductive mood, the face in the upper-mid frame and the décolleté below, a single woman alone",
 "sensual Instagram boudoir portrait reclining with the head tipped back toward the camera, the face and bust facing the lens, one long-nailed hand resting on the collarbone, a sultry half-lidded gaze, lips parted glossy, a single woman alone",
 "intimate sensual Instagram close-up portrait facing the camera, one long-nailed fingertip grazing and pulling the glossy bottom lip, a direct smoldering gaze to the lens, the face dominant in the frame and the décolleté below, a single woman alone",
 "sensual Instagram influencer portrait at a high three-quarter angle, the chin resting on the back of one long-nailed hand with the elbow propped, a coy half-lidded gaze up to the lens, glossy parted lips, the face dominant in the frame, a single woman alone",
 "sensual Instagram influencer portrait glancing back over one bare shoulder toward the lens, one long-nailed hand drawing the her hair away from the cheek, a smoldering glance and glossy parted lips, the face and shoulder line filling the frame, a single woman alone",
 "sensual Instagram influencer portrait from slightly above the eyeline, the face tilted up to the camera, one long-nailed hand pressed flat against the upper chest below the collarbone, a sultry up-gaze and glossy parted lips, the face dominant and the décolleté below, a single woman alone",
]

ODALISQUE = [
 "full body lying on the side with an exaggerated S-curve, an extreme back arch with the bust pushed up and the hip rolled back, one leg extended with the stiletto pointed and the other bent, one arm under the head with long nails in the hair and the other trailing from the collarbone to the hip, half-lidded predatory gaze, her hair cascading",
 "full body semi-reclined on one hip propped on one forearm with the legs draped and the top stiletto pointed at the camera, the spine in an elegant arch, the other long-nailed hand resting on the thigh, looking to the camera over the shoulder, lips parted glossy, her hair spilling forward",
 "full body reclining to one side on one hip with the legs draped and both stilettos visible, one arm extended propping the body and the other long-nailed hand trailing from the collarbone to the waist, the spine in a long arch with the bust forward, a half-lidded gaze toward the camera, lips parted glossy, her hair cascading forward",
 "full body semi-reclined propped on both elbows with the legs draped and one stiletto pointed at the camera, the bust forward and the spine arched, the chin lifted, a half-lidded predatory gaze, long nails resting on the thigh, her hair over one shoulder",
 "full body reclining back on both elbows with the legs draped and one stiletto pointed at the camera, a deep elegant back arch with the bust lifted, looking to the camera through the lashes, long nails resting on the thigh, lips parted glossy, her hair falling around the face",
 "full body side profile reclining on one side with an elegant S-curve, the hip rolled up and the bust forward in silhouette, one long-nailed hand supporting the head and the other trailing along the waist, the top stiletto pointed and the legs elegantly stacked, lips parted glossy, her hair cascading along the surface",
 "full body seen from directly overhead in a zenithal top-down view, lying flat on the back along {surface} with the spine in a long S-curve, one knee drawn up and the stilettos pointed, both long-nailed hands framing the collarbone and the her hair fanned out around the head across the surface, lips parted glossy, gazing straight up into the overhead lens",
 "full body seen from directly overhead in a zenithal top-down view, the body lying flat on {surface} twisted into an elegant hip-rolled S-curve with the legs stacked and one stiletto pointed, one long-nailed hand resting on the flat stomach and the other above the head amid the fanned her hair, glossy lips parted, looking up to the overhead camera",
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

# ECO DE CALZADO EN POSES NO-FRONTALES (Ama 15/07/2026 — BUG "el zapato muta cuando la camara
# no lo mira de frente"): el Token de Calzado Bloqueado (8 atributos x7) aguanta en Standing/
# Seated/Side pero el batch de prueba lo vio mutar justo en los slots donde el pie queda lejos
# del foco: L791 Odalisque rindio BOTINES con plataforma donde el token pedia pumps slip-on sin
# plataforma; L797 Back View rindio booties de punta redonda con plataforma dorada donde el token
# pedia botin puntiagudo sin plataforma. El token vive enterrado en el medio del prompt; en Back/
# Odalisque se le suma un ECO corto al final de la direccion de pose (cerca del encuadre, donde
# el generador decide que se ve) reafirmando heel/plataforma/puntera.
def footwear_echo(shoe_short):
    """shoe_short: descriptor corto del calzado (ej. 'oxblood patent pointed-toe stiletto pumps,
    no platform'). Devuelve el eco a appendear en Back View y Odalisque."""
    return (f"the footwear clearly visible and exactly as described — {shoe_short} — with the same "
            f"heel, the same platform height and the same toe shape, never swapped for boots, "
            f"booties or any other shoe style")

_SHOE_ECHO_SLOTS = {"Back View", "Odalisque"}


def rotate_poses(look_number, seat="a sculptural bench", wall="a wall", surface="a surface",
                 wrap_mode=None, seam=False, shoe_echo=None, skirt=False):
    """Devuelve [(slot, pose_direction)] de 7, rotados por nº de look y con props CONTEXTUALES.
    seat/wall/surface deben describir mobiliario REAL del setting del look (armonia con el ambiente).

    wrap_mode (Ama 09/07/2026 — BUG "bata al reves"): si el look usa una prenda ENVOLVENTE de
    frente abierto (robe/kimono/peignoir/bata/wrap), pasar wrap_mode para anclar la ORIENTACION
    de la prenda SOLO en la pose de espalda (Back View), donde el generador la ponia al reves
    (abertura corriendo por la columna). Valores: None (sin prenda envolvente) · "slip" (bata
    deslizada de los hombros, espalda desnuda pero correcta — default recomendado boudoir) ·
    "closed" (bata bien puesta, espalda cubierta) · "tailored" (blazer/chaqueta/abrigo/tuxedo/
    coat-dress de frente abierto CERRADO: panel de espalda liso a la camara, solapas al lado lejano
    — Ama 02/08/2026). Ver auto-memoria feedback_bata_reverso_espalda.

    seam (Ama 11/07/2026 — BUG "raya de la media al frente"): pasar seam=True cuando el look usa
    MEDIAS CON COSTURA (back-seam / seamed stockings). Ancla POSE-AWARE la orientacion de la raya:
    poses de frente -> "frente liso, costura solo por detras"; Back View -> "costura visible por
    detras"; Side Profile no la lleva. Ver auto-memoria feedback_media_raya_frontal.

    shoe_echo (Ama 15/07/2026 — BUG "el zapato muta en Back/Odalisque"): descriptor corto del
    calzado del look (ej. 'silver mirror-chrome knee-high stiletto boots, no platform'). Si se
    pasa, Back View y Odalisque reciben footwear_echo(shoe_echo) al final de la pose.

    skirt (Ama 02/08/2026 — BUG "sentada con falda abierta de piernas"): pasar skirt=True cuando el
    look lleva FALDA o VESTIDO. Inyecta SEATED_MODESTY en el slot Seated (rodillas y muslos juntos,
    piernas cruzadas/cerradas, nunca abiertas) para que el generador no abra las piernas y exponga la
    entrepierna bajo la falda. Ver .agent/rules/06 §6.

    TODA pose sale ademas con SINGLE_FRAME prepuesto (primacia absoluta, Ama 15/07/2026): define
    la imagen como UN solo cuadro continuo antes de describir nada — el batch de prueba rindio
    4 collages/grillas de 30 imagenes CON "split image" vetado en el negativo (Gemini lo ignora;
    el lever es el positive)."""
    if wrap_mode not in (None, "slip", "closed", "tailored"):
        raise ValueError(f"wrap_mode invalido: {wrap_mode!r} (usa None, 'slip', 'closed' o 'tailored')")
    wrap_anchor = _WRAP_ANCHORS.get(wrap_mode)
    out = []
    for name, variants, off in SLOTS:
        v = variants[(look_number + off) % len(variants)]
        v = v.replace("{seat}", seat).replace("{wall}", wall).replace("{surface}", surface)
        anchor = HANDS_ANCHOR if name in CLOSEUP_SLOTS else FULL_ANCHOR
        if name == "Odalisque":
            if "zenithal" in v:  # variante cenital (Ama 02/08): recumbencia SI, camara nivelada NO (choca)
                anchor = anchor + ", " + ODALISQUE_RECUMBENCY + ", " + ODALISQUE_ZENITHAL_CAM
            else:
                anchor = anchor + ", " + ODALISQUE_ANCHOR  # fuerza recumbencia + nivelada (bug odalisca-sentada/rotada)
        if name == "Standing":
            anchor = anchor + ", " + STANDING_ANCHOR  # fuerza frontalidad (bug standing-de-espalda)
        if seam and name not in _SEAM_SKIP_SLOTS:
            # Ancla de orientacion de la raya (bug raya-al-frente). REFUERZO 13/07: viaja PEGADA AL
            # ANCLA, al FRENTE de la direccion de pose (primacia), en vez de appendeada al final —
            # ahi quedaba enterrada bajo una direccion larguisima y perdia contra la tendencia del
            # generador a pintar la costura en la cara VISIBLE de la pierna. La respalda ademas
            # build_negative(seam=True), que antes ningun inyector pegaba.
            anchor = anchor + ", " + (STOCKING_SEAM_BACK if name == "Back View" else STOCKING_SEAM_FRONT)
        # SINGLE_FRAME va PRIMERO que todo (anti-collage, primacia absoluta):
        v = SINGLE_FRAME + ", " + anchor + ", " + v
        if name == "Seated":
            v = v + ", " + SEATED_ANCHOR  # ancla de peso (bug sustitucion de mueble)
            if skirt:
                v = v + ", " + SEATED_MODESTY  # anti-piernas-abiertas con falda (Ama 02/08/2026)
        if name == "Back View" and wrap_anchor:
            v = v + ", " + wrap_anchor  # ancla de orientacion de prenda envolvente (bug bata-al-reves)
        if shoe_echo and name in _SHOE_ECHO_SLOTS:
            v = v + ", " + footwear_echo(shoe_echo)  # eco de calzado (bug zapato-que-muta)
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
    # Auto-check ancla anatomica: toda pose generada debe traer su ancla ya incluida,
    # precedida SIEMPRE por SINGLE_FRAME (anti-collage, primacia absoluta, Ama 15/07).
    miss = []
    for slot, txt in rotate_poses(531):
        want = SINGLE_FRAME + ", " + (HANDS_ANCHOR if slot in CLOSEUP_SLOTS else FULL_ANCHOR)
        if not txt.startswith(want):
            miss.append(slot)
    print("Ancla anatomica check:", "LIMPIO (todas las poses anclan tras SINGLE_FRAME)" if not miss else "FALTA en: " + ", ".join(miss))
    # Auto-check SINGLE_FRAME (Ama 15/07 — bug collage): las 7 poses lo llevan al FRENTE.
    sf_ok = all(txt.startswith(SINGLE_FRAME) for _, txt in rotate_poses(792))
    print("Ancla cuadro unico check:",
          "LIMPIO (SINGLE_FRAME prepuesto en las 7 poses)" if sf_ok else "FALLA (falta SINGLE_FRAME)")
    # Auto-check METALENGUAJE MULTI-TOMA (Ama 15/07 — el lock viejo invitaba la hoja de contactos):
    # ningun lock/negative del motor puede volver a decir "every shot / all poses / between shots".
    META = ["every shot", "all poses", "between shots", "in every pose"]
    meta_hits = [f"{name} -> '{m}'" for name, txt in [
        ("CONSISTENCY_LOCK", CONSISTENCY_LOCK), ("HOSIERY_LOCK", HOSIERY_LOCK),
        ("NEG_INCONSISTENT", NEG_INCONSISTENT), ("NEG_HOSIERY", NEG_HOSIERY),
        ("animal_print_lock", animal_print_lock("python")), ("SKIN_LOCK", SKIN_LOCK),
        ("UNMARKED_ZONES", UNMARKED_ZONES), ("NO_ARMWEAR", NO_ARMWEAR),
        ("BASE_NEGATIVE", BASE_NEGATIVE)] for m in META if m in txt.lower()]
    print("Metalenguaje multi-toma check:",
          "LIMPIO (ningun lock habla de shots/poses)" if not meta_hits else "FLAGS: " + "; ".join(meta_hits))
    # Auto-check eco de calzado (Ama 15/07 — bug zapato-que-muta en Back/Odalisque): con shoe_echo,
    # SOLO Back View y Odalisque lo llevan; sin shoe_echo, ninguna pose lo lleva.
    echo_txt = footwear_echo("test pumps, no platform")
    echo_poses = dict(rotate_poses(791, shoe_echo="test pumps, no platform"))
    echo_ok = echo_txt in echo_poses["Back View"] and echo_txt in echo_poses["Odalisque"]
    echo_leak = any(echo_txt in txt for slot, txt in echo_poses.items()
                    if slot not in ("Back View", "Odalisque"))
    echo_none = any("never swapped for boots" in txt for _, txt in rotate_poses(791))
    print("Eco de calzado check:",
          "LIMPIO (echo solo en Back/Odalisque, sin fuga)" if (echo_ok and not echo_leak and not echo_none)
          else f"FALLA (echo_ok={echo_ok} fuga={echo_leak} sin_param={echo_none})")
    # Auto-check camara Odalisque (Ama 15/07 nivelada L795 rotada + Ama 02/08 planos cenitales):
    # las variantes laterales llevan horizonte nivelado; las cenitales llevan picado total y NO la
    # nivelacion (chocan). Busco un look que caiga en variante lateral y otro en cenital.
    _lat = next(dict(rotate_poses(n))["Odalisque"] for n in range(700,900)
                if "zenithal" not in dict(rotate_poses(n))["Odalisque"])
    _zen = next(dict(rotate_poses(n))["Odalisque"] for n in range(700,900)
                if "zenithal" in dict(rotate_poses(n))["Odalisque"])
    lvl_ok = "never rotated or tilted sideways" in _lat
    zen_ok = ("zenithal top-down" in _zen and "horizon perfectly level" not in _zen
              and "reclining odalisque" in _zen)
    print("Camara Odalisque (nivelada + cenital) check:",
          "LIMPIO (lateral=horizonte nivelado, cenital=picado sin nivelacion, recumbencia en ambas)"
          if (lvl_ok and zen_ok) else f"FALLA (lateral={lvl_ok} cenital={zen_ok})")
    # Auto-check constantes nuevas 15/07 (UNMARKED_ZONES anti-migracion + NO_ARMWEAR anti-manga):
    # v3 15/07: NO_ARMWEAR ya no abre con "bare hands" (afirmativo-primero: la piel del brazo).
    nz_ok = ("unmarked porcelain skin" in UNMARKED_ZONES and "hip crease" in UNMARKED_ZONES
             and "arm sleeves" in NO_ARMWEAR and "hands is genuinely bare" in NO_ARMWEAR)
    print("Zonas sin tatuar / anti-manga check:",
          "LIMPIO (UNMARKED_ZONES + NO_ARMWEAR definidos)" if nz_ok else "FALLA (constantes mal formadas)")
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
    # Auto-check ancla blazer/tailored (Ama 02/08 — bug blazer-al-reves): SOLO Back View la lleva.
    ok_tailored   = WRAP_BACK_TAILORED in _bv(rotate_poses(772, wrap_mode="tailored"))
    leak_tailored = any(WRAP_BACK_TAILORED in txt for slot, txt in rotate_poses(772, wrap_mode="tailored") if slot != "Back View")
    print("Ancla blazer/tailored check:",
          "LIMPIO (tailored en Back View, sin fuga)" if (ok_tailored and not leak_tailored)
          else f"FALLA (tailored={ok_tailored} fuga_otro_slot={leak_tailored})")
    # Auto-check modestia Seated con falda (Ama 02/08 — bug sentada-abierta-de-piernas): SOLO Seated.
    ok_skirt   = SEATED_MODESTY in dict(rotate_poses(250, skirt=True))["Seated"]
    leak_skirt = any(SEATED_MODESTY in v for s, v in rotate_poses(250, skirt=True) if s != "Seated")
    off_skirt  = SEATED_MODESTY not in dict(rotate_poses(250))["Seated"]
    print("Modestia Seated con falda check:",
          "LIMPIO (SEATED_MODESTY solo en Seated con skirt=True, ausente sin skirt)" if (ok_skirt and not leak_skirt and off_skirt)
          else f"FALLA (ok={ok_skirt} fuga={leak_skirt} ausente_sin_skirt={off_skirt})")
    # Auto-check diferenciacion Ditzy vs POV (Ama 02/08 — "salen casi iguales"): Ditzy mira FUERA, POV al lente.
    _OFF = ("away from the lens", "away from the camera", "off past the lens", "off to one side", "off to the side", "down and away", "upper corner away")
    _GAZE_OFF = ("away from the lens", "away from the camera", "off past the lens", "wandering off", "drifts dreamily off", "upper corner away", "gaze wandering off")
    ditzy_off = all(any(k in d for k in _OFF) for d in DITZY)
    pov_on    = all(("lens" in p or "the camera" in p) and not any(g in p for g in _GAZE_OFF) for p in POV)
    print("Diferenciacion Ditzy/POV check:",
          "LIMPIO (Ditzy mira fuera de cuadro, POV mira al lente)" if (ditzy_off and pov_on)
          else f"FALLA (ditzy_off={ditzy_off} pov_on={pov_on})")
    # Auto-check poses AGNOSTICAS de personaje (Ama 02/08 — motor modular multi-personaje): las
    # variantes de pose son BLOQUE C puro (encuadre + gesto). El ADN (pelo/unas/ojos/piel) lo pone el
    # BLOQUE A del perfil de cada personaje (ele/miss_doll/anais), NUNCA la pose. Guard anti-recontaminacion.
    _POOLS = STANDING + BACK + SEATED + SIDE + DITZY + POV + ODALISQUE
    _DNA = ("cherry", "xxxl", "platinum", "blonde", "brunette", "steel grey", "grey-green", "red hair", " bob", "mole")
    _leak = sorted({d for v in _POOLS for d in _DNA if d in v.lower()})
    print("Poses agnosticas de personaje check:",
          "LIMPIO (Bloque C sin ADN; el fisico lo pone el perfil)" if not _leak
          else f"FALLA (ADN de personaje filtrado en poses: {_leak})")
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
    # Auto-check constantes de vestuario (Ama 11/07, v2 15/07): OPAQUE / GLOSS / CONSISTENCY.
    print("Constantes vestuario check:",
          "LIMPIO (OPAQUE_LOCK + GLOSS_LOCK + CONSISTENCY_LOCK v2 definidas)"
          if (len(OPAQUE_LOCK) > 40 and len(GLOSS_LOCK) > 40 and "no matte" in GLOSS_LOCK.lower()
              and len(CONSISTENCY_LOCK) > 40 and "word for word" in CONSISTENCY_LOCK.lower()
              and "two-piece" in CONSISTENCY_LOCK.lower())
          else "FALLA (constantes vacias o mal formadas)")
    # Auto-check SKIN_LOCK v2 + HOSIERY_LOCK v2 (Ama 13/07, v2 15/07 — afirmativo primero).
    skin_ok = all(t in SKIN_LOCK.lower() for t in
                  ("smooth", "bare exposed skin", "nipple", "navel", "tattoo", "piercing"))
    hos_ok = all(t in HOSIERY_LOCK.lower() for t in ("one single pair", "word for word", "bare legs"))
    print("Candados piel/medias check:",
          "LIMPIO (SKIN_LOCK v2 afirmativo + HOSIERY_LOCK v2 definidos)" if (skin_ok and hos_ok)
          else f"FALLA (skin_ok={skin_ok} hosiery_ok={hos_ok})")
    # Auto-check del NEGATIVE (Ama 13/07 — bug "sin bloque negativo desde el L711"):
    #  (1) NEG_MARKS_THROUGH va SIEMPRE (el par negativo del SKIN_LOCK);
    #  (2) el mule solo se veta FUERA de Lenceria (canon del mule, Ama 09/07);
    #  (3) la raya frontal y la deriva de medias entran con seam/stockings;
    #  (4) NINGUN color concreto de media puede estar vetado (pelearia con los looks de media negra).
    neg_plain  = build_negative()
    neg_seam   = build_negative(seam=True, covered=True)
    neg_ling   = build_negative(lingerie=True, stockings=True)
    neg_checks = {
        "marks_siempre":  NEG_MARKS_THROUGH in neg_plain and NEG_MARKS_THROUGH in neg_ling,
        "mule_fuera_lenc": NEG_MULE in neg_plain,
        "mule_ok_lenc":   NEG_MULE not in neg_ling,
        "seam_entra":     NEG_FRONT_SEAM in neg_seam and NEG_FRONT_SEAM not in neg_plain,
        "hosiery_entra":  NEG_HOSIERY in neg_seam and NEG_HOSIERY in neg_ling,
        "cutout_entra":   NEG_CUTOUT in neg_seam and NEG_CUTOUT not in neg_plain,
        "sin_color_media": not any(c in NEG_HOSIERY.lower()
                                   for c in ("black stockings", "green stockings", "white stockings")),
        "guantes":        "gloves" in neg_plain,
        "planos":         "flat shoes" in neg_plain and "barefoot" in neg_plain,
        # v2 15/07: oxblood solo como labio (nunca el color desnudo — pelearia con prendas oxblood):
        "oxblood_solo_labios": "oxblood lips" in neg_plain and not __import__("re").search(
            r"oxblood(?!\s+lips)", neg_plain),
        # v2 15/07: familia anti-collage + mangas fantasma + encuadre rotado presentes:
        "anti_collage":   "collage" in neg_plain and "contact sheet" in neg_plain,
        "anti_mangas":    "arm sleeves" in neg_plain and "arm warmers" in neg_plain,
        "anti_rotacion":  "rotated image" in neg_plain,
    }
    bad_neg = [k for k, ok in neg_checks.items() if not ok]
    print("Negative check:", "LIMPIO (build_negative es fuente unica y condicional)" if not bad_neg
          else "FALLA en: " + ", ".join(bad_neg))
    # Auto-check odalisca anti-percha (refuerzo 13/07 tras L763/L764 perchadas en la mesa).
    od_txt = dict(rotate_poses(763))["Odalisque"].lower()
    print("Odalisca anti-percha check:",
          "LIMPIO (prohibe percha en mesa/escritorio y pies en el piso)"
          if ("not perched on the edge" in od_txt and "both feet off the floor" in od_txt)
          else "FALLA (falta la clausula anti-mueble)")
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
    # Auto-check guardia contra la orden vieja (Ama 13/07 — L761-L770 se generaron con la frase
    # todavia puesta): find_forbidden() debe cazarla en texto sucio y NO disparar falso positivo
    # en el Bloque A ya corregido.
    dirty = "navel piercing, nipple piercings pressing against and visible under clothing, aggressive"
    clean = "navel piercing, nipple piercings, every tattoo and piercing visible ONLY on genuinely bare skin and never through or over any garment"
    forb_ok = bool(find_forbidden(dirty)) and not find_forbidden(clean)
    skin_ok2 = has_skin_lock(clean) and has_skin_lock(SKIN_LOCK) and not has_skin_lock(dirty)
    print("Guardia frase-orden-vieja check:",
          "LIMPIO (detecta texto sucio, no marca falso positivo en Bloque A corregido)"
          if (forb_ok and skin_ok2) else f"FALLA (forb_ok={forb_ok} skin_ok={skin_ok2})")
    # Auto-check candado de estampado animal (Ama 13/07 — bug python-print sale como encaje).
    apl = animal_print_lock("python")
    print("Candado estampado animal check:",
          "LIMPIO (animal_print_lock + NEG_PRINT_DRIFT definidos)"
          if ("python" in apl.lower() and "not a lace" in apl.lower() and len(NEG_PRINT_DRIFT) > 40)
          else "FALLA (candado de estampado mal formado)")
    neg_print_on  = build_negative(animal_print=True)
    neg_print_off = build_negative(animal_print=False)
    print("Negative estampado animal check:",
          "LIMPIO (NEG_PRINT_DRIFT entra solo con animal_print=True)"
          if (NEG_PRINT_DRIFT in neg_print_on and NEG_PRINT_DRIFT not in neg_print_off)
          else "FALLA (NEG_PRINT_DRIFT no condicional)")
    # Auto-check v3 (Ama 15/07 — auditoria del batch materializado):
    # (1) build_marks_clause: lo cubierto NO se nombra; nipple piercings JAMAS; manos limpias siempre.
    mc_covered = build_marks_clause(arms_bare=True)                       # catsuit manga corta p.ej.
    mc_bikini  = build_marks_clause(arms_bare=True, back_bare=True, thighs_bare=True,
                                    pelvis_bare=True, navel_bare=True)   # bikini: todo descubierto
    mc_full    = build_marks_clause(arms_bare=False)                     # full-coverage manga larga
    mc_checks = {
        "cubierto_no_nombra": ("rune" not in mc_covered and "navel" not in mc_covered
                               and "thigh" not in mc_covered),
        "descubierto_nombra": ("rune" in mc_bikini and "navel" in mc_bikini
                               and "outer thighs" in mc_bikini and "upper back" in mc_bikini),
        "nipple_jamas":       "nipple" not in mc_covered and "nipple" not in mc_bikini,
        "manos_siempre":      all("clean unmarked skin" in m for m in (mc_covered, mc_bikini, mc_full)),
        "full_solo_manos":    "tattoo" not in mc_full,
    }
    bad_mc = [k for k, ok in mc_checks.items() if not ok]
    print("Marcas condicionales v3 check:",
          "LIMPIO (build_marks_clause: lo cubierto no se nombra)" if not bad_mc
          else "FALLA en: " + ", ".join(bad_mc))
    # (2) SINGLE_FRAME v3 cierra el camino del espejo/marco-dentro-de-escena + TAIL definido;
    #     el negative trae los pares (espejo duplicado / marco / poster / light box).
    sf_ok = ("mirror" in SINGLE_FRAME and "light box" in SINGLE_FRAME
             and len(SINGLE_FRAME_TAIL) > 30)
    neg_dup_ok = ("second copy of the same woman" in neg_plain
                  and "light box" in neg_plain and "inset photo" in neg_plain)
    print("Anti-duplicado-en-escena v3 check:",
          "LIMPIO (SINGLE_FRAME v3 + TAIL + negative de espejos/marcos)"
          if (sf_ok and neg_dup_ok) else f"FALLA (sf_ok={sf_ok} neg_dup_ok={neg_dup_ok})")
    # (3) NO_ARMWEAR v3 afirmativo-primero (la piel desnuda ANTES que los vetos).
    naw = NO_ARMWEAR.lower()
    naw_ok = (naw.find("genuinely bare") < naw.find("no gloves")
              and "porcelain skin" in naw and "arm warmers" in naw)
    print("Anti-armwear v3 check:",
          "LIMPIO (NO_ARMWEAR afirmativo primero)" if naw_ok
          else "FALLA (NO_ARMWEAR no es afirmativo-primero)")
