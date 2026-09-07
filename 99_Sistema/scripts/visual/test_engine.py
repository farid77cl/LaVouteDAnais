# -*- coding: utf-8 -*-
"""test_engine.py — Bateria de pruebas del outfit-engine.

Ama 29/08/2026: "hace pruebas con el outfit engine".

Que cubre cada bloque, y por que existe:

  A. ENTRADAS MALAS — json roto, personaje inexistente, claves faltantes, props
     ausentes, un `adn_overrides` que apunta a un fragmento que ya no esta. El
     motor siempre valido bien, pero entregaba sus errores como traceback de
     Python: el mensaje util quedaba enterrado bajo la pila y cualquier entrada
     mala parecia un crash. Estas 9 pruebas encontraron 4 casos asi el mismo dia
     que se escribieron — por eso el bloque va primero.
  B. DETERMINISMO — el mismo input dos veces da el mismo prompt. Si esto se
     rompe, ningun batch es reproducible y las verificaciones byte-a-byte que se
     usaron para migrar los batches a datos dejan de significar nada.
  C. ROTACION — 20 looks seguidos deben recorrer el repertorio. Sin esto las
     imagenes salen "casi todas iguales" (Ama 12/08/2026, medido en Anais: 87%
     de similitud en POV antes de que existiera su repertorio).
  D. COBERTURA — los 7 slots x los 3 personajes generan prompts validos.
  E. REGRESIONES — lo arreglado el 29/08: ancla de bata solo en Back View, cero
     piernas abiertas en Miss Doll, ADN leido del perfil, los cuatro candados de
     material, la costura por slot y el falso positivo del pelo.

Se corre solo (`python test_engine.py`) o via `outfit.py test`.
"""
import io
import json
import os
import re
import subprocess
import sys
import tempfile

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
# Rutas relativas al propio archivo: el repo esta clonado en varias maquinas y
# una ruta absoluta haria que la suite solo corriera en la que la escribio.
V = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(V, "..", "..", ".."))
sys.path.insert(0, V)
os.chdir(RAIZ)

from prompt_builder import PromptBuilder, cargar_config  # noqa: E402

cfg = cargar_config()
PR = {"seat": "a velvet chair", "wall": "a mirrored wall",
      "surface": "a marble console", "upright": "a lacquered bedpost"}
B_SIMPLE = ("a wine latex corselette, sweetheart neckline, sleeveless, high-cut hem; "
            "closed pointed-toe stiletto pump in wine patent, 13cm thin pin stiletto heel")
SLOTS = list(cfg["slots_universales"])
SLUGS = list(cfg["personajes"])

ok = fallo = 0
notas = []


def check(nombre, cond, detalle=""):
    global ok, fallo
    if cond:
        ok += 1
        print("  ok    %s" % nombre)
    else:
        fallo += 1
        print("  \U0001f534 FALLA %s   %s" % (nombre, detalle))
        notas.append(nombre)


def cli(*args):
    r = subprocess.run([sys.executable, os.path.join(V, "outfit.py")] + list(args),
                       cwd=RAIZ, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    return r.returncode, (r.stdout or "") + (r.stderr or "")


print("=" * 74)
print("A. ENTRADAS MALAS — el motor debe fallar limpio, nunca reventar")
print("=" * 74)

cod, out = cli("generar", "no_existe.json")
check("batch inexistente", cod != 0 and "Traceback" not in out, out[-90:])

tmp = tempfile.mkdtemp()
malos = {
    "json_roto.json": "{ esto no es json ",
    "sin_personaje.json": json.dumps({"looks": {"1": {"titulo": "x", "bloque_b": "y", "setting": "z"}}}),
    "sin_looks.json": json.dumps({"personaje": "ele"}),
    "sin_bloque_b.json": json.dumps({"personaje": "ele", "looks": {"1": {"titulo": "x", "setting": "z"}}}),
    "sin_setting.json": json.dumps({"personaje": "ele", "looks": {"1": {"titulo": "x", "bloque_b": "y"}}}),
    "personaje_falso.json": json.dumps({"personaje": "barbie", "looks": {"1": {"titulo": "x", "bloque_b": "y", "setting": "z"}}}),
    "sin_props.json": json.dumps({"personaje": "ele", "looks": {"1": {"titulo": "x", "bloque_b": B_SIMPLE, "setting": "z"}}}),
    "override_zombi.json": json.dumps({"personaje": "miss_doll", "looks": {"1": {
        "titulo": "x", "bloque_b": B_SIMPLE, "setting": "z", "props": PR,
        "adn_overrides": {"fragmento que no existe en su ADN": "otra cosa"}}}}),
}
for nombre, contenido in malos.items():
    p = os.path.join(tmp, nombre)
    open(p, "w", encoding="utf-8").write(contenido)
    cod, out = cli("generar", p)
    check(nombre[:-5].replace("_", " "), cod != 0 and "Traceback" not in out,
          "exit=%d %s" % (cod, out.strip().split("\n")[-1][:70] if out.strip() else ""))

print()
print("=" * 74)
print("B. DETERMINISMO — el mismo input dos veces da el mismo prompt")
print("=" * 74)
for slug in SLUGS:
    pb1, pb2 = PromptBuilder(slug, cfg), PromptBuilder(slug, cfg)
    iguales = all(
        pb1.build(None, B_SIMPLE, s, pb1.pose(s, 500, props=PR), "a hall")
        == pb2.build(None, B_SIMPLE, s, pb2.pose(s, 500, props=PR), "a hall")
        for s in SLOTS)
    check("determinista: %s" % slug, iguales)

print()
print("=" * 74)
print("C. ROTACIÓN — 20 looks seguidos no pueden repetir la misma sub-pose")
print("=" * 74)
for slug in SLUGS:
    pb = PromptBuilder(slug, cfg)
    peor = None
    for s in SLOTS:
        vistos = [pb.pose_indice(s, n) for n in range(1, 21)]
        distintos = len(set(vistos))
        if peor is None or distintos < peor[1]:
            peor = (s, distintos, len(pb.variaciones(s)))
    check("rotación %s (peor slot: %s, %d distintas de %d disponibles en 20 looks)"
          % (slug, peor[0], peor[1], peor[2]), peor[1] >= min(5, peor[2]))

print()
print("=" * 74)
print("D. TODOS LOS SLOTS × TODOS LOS PERSONAJES generan válido")
print("=" * 74)
for slug in SLUGS:
    pb = PromptBuilder(slug, cfg)
    fallas = []
    for s in SLOTS:
        for n in (1, 47, 300, 812):
            p = pb.build(None, B_SIMPLE, s, pb.pose(s, n, props=PR), "a marble hall")
            fallas += ["%s/L%d: %s" % (s, n, f) for f in pb.validar(p)]
    check("%s — 28 prompts válidos" % slug, not fallas, "; ".join(fallas[:2]))

print()
print("=" * 74)
print("E. REGRESIONES de lo arreglado hoy")
print("=" * 74)

# E1 bata / blazer -> ancla solo en back_view
W = cfg["anclas"]["WRAP_BACK_ROBE"]["texto"][:45]
T = cfg["anclas"]["WRAP_BACK_TAILORED"]["texto"][:45]
for slug in SLUGS:
    pb = PromptBuilder(slug, cfg)
    bata = "a black silk-satin robe over a latex bodysuit; stiletto pump 13cm"
    bv = pb.build(None, bata, "back_view", pb.pose("back_view", 7, props=PR), "a hall")
    st = pb.build(None, bata, "standing", pb.pose("standing", 7, props=PR), "a hall")
    check("bata: ancla en Back View y NO en Standing (%s)" % slug, W in bv and W not in st)

# E2 Miss Doll sin piernas abiertas
pb = PromptBuilder("miss_doll", cfg)
RXP = re.compile(r"(?<!never )(?<!not )\b(knees?|legs?|thighs?)\s+(wide|apart|open|spread|parted)\b|in a wide V|astride", re.I)
malos = []
for s in SLOTS:
    for n in range(1, 31):
        p = pb.pose(s, n, props=PR)
        for m in RXP.finditer(p):
            frag = p[max(0, m.start() - 60):m.end() + 20]
            if "never" not in frag and "not " not in frag:
                malos.append("%s/L%d" % (s, n))
check("Miss Doll: 0 piernas abiertas en 210 poses", not malos, ", ".join(malos[:3]))

# E3 ADN leído del perfil
for slug in SLUGS:
    pb = PromptBuilder(slug, cfg)
    p = pb.build(None, B_SIMPLE, "standing", pb.pose("standing", 3, props=PR), "a hall")
    check("ADN del perfil sin pasarlo (%s)" % slug, p.startswith(pb.bloque_a[:70]))

# E4 candados de material
pb = PromptBuilder("ele", cfg)
casos = [("bodycon dress", "OPAQUE_LOCK"), ("wool blazer", "GLOSS_LOCK"),
         ("sheer stockings", "HOSIERY_LOCK"), ("leopard-print vinyl dress", "ANIMAL_PRINT_LOCK")]
for texto, ancla in casos:
    check("dispara %s con %r" % (ancla, texto), ancla in pb.opt_in_de(texto))

# E5 SEAM por slot
seam_b = "a corselette; full-length seamed stockings with a straight back seam; stiletto pump 13cm"
F = cfg["anclas"]["SEAM_FRONT"]["texto"][:45]
K = cfg["anclas"]["SEAM_BACK"]["texto"][:45]
pb = PromptBuilder("ele", cfg)
est = {s: pb.build(None, seam_b, s, pb.pose(s, 9, props=PR), "a hall") for s in SLOTS}
check("costura: FRONT en standing, BACK en back_view, ninguna en side_profile",
      F in est["standing"] and K in est["back_view"]
      and F not in est["side_profile"] and K not in est["side_profile"])

# E6 falso positivo del pelo de Miss Doll
pbm = PromptBuilder("miss_doll", cfg)
check("ASYMMETRY_LOCK no lo dispara el pelo",
      "ASYMMETRY_LOCK" not in pbm.opt_in_de("platinum blonde asymmetric angled bob, latex corset"))
check("ASYMMETRY_LOCK sí lo dispara una prenda",
      "ASYMMETRY_LOCK" in pbm.opt_in_de("asymmetric one-shoulder latex gown"))


# E7 clon de outfit DENTRO del mismo personaje (05/09/2026)
#     Ama: "cada vez que me generas un batch sale algun error... como evitamos
#     eso?". Un chequeo sin prueba esta a un paso de ser una regla sin ejecutor,
#     que es la causa raiz que se repitio cuatro veces ese mismo dia.
from garment_canon import audit_clon_intra, _cuerpo_sin_calzado   # noqa: E402

_A = ("a deep aubergine high-shine latex overbust corset, heavily boned with fine "
      "antique-silver boning channels visible on the outside, moulded cups lifting the "
      "bust high; beneath it an aubergine latex thong with a slim shield-shaped front "
      "panel; sheer smoke-plum stockings; closed pointed-toe boots, 12cm stiletto heel")
_B = _A.replace("aubergine", "emerald").replace("smoke-plum", "smoke-green")
_C = ("a champagne silk-satin pencil miniskirt cut high on the natural waist with a "
      "concealed hook closure; above it a pussy-bow blouse with long full sleeves; a "
      "silver fox stole across the shoulders; closed pointed-toe slingback, 12cm heel")

d, _a = audit_clon_intra([(1, _A), (2, _B)], {2})
check("clon intra: el mismo parrafo con otro color sale DURO", len(d) == 1)
d2, _a2 = audit_clon_intra([(1, _A), (2, _C)], {2})
check("clon intra: dos outfits de verdad distintos pasan limpios", not d2)
d3, _a3 = audit_clon_intra([(1, _A), (2, _B)], {1})
check("clon intra: solo mide los looks NUEVOS, no la historia contra si misma",
      len(d3) == 1)
check("clon intra: el calzado se excluye antes de comparar",
      "heel" not in _cuerpo_sin_calzado(_A))

# E8 guante cerrado + token de uñas (regla de la Ama del 11/08, sin ejecutor hasta el 05/09)
from garment_canon import warn_glove_nail_conflict                # noqa: E402
check("guantes: opera + token de uñas avisa",
      bool(warn_glove_nail_conflict("long latex opera gloves to above the elbow; "
                                    "nails: long stiletto-shaped fingernails")))
check("guantes: sin guante + uñas NO avisa",
      not warn_glove_nail_conflict("bare hands, no gloves; nails: oval manicured "
                                   "glossy fingernails"))
check("guantes: guante sin dedos + uñas NO avisa",
      not warn_glove_nail_conflict("fingerless lace gloves to the elbow; nails: almond acrylics"))

# E9 la corseteria de epoca ya no es invisible para la taxonomia
from lint_prompts_personaje import clasificar_arquitectura        # noqa: E402
_tax = cfg["arquitecturas_de_prenda"]
for _pieza, _sub in (("a black silk-velvet longline merry widow, boned, with six suspender tabs", "A4"),
                     ("a deep plum latex guepiere in the 1950s cut, boned", "A5"),
                     ("an emerald silk-satin waspie cinching the waist alone, boned", "A2"),
                     ("a deep aubergine latex overbust corset as the central piece", "A6")):
    _cod = clasificar_arquitectura(_pieza + "; a matching thong", _tax)[0]
    check("taxonomia: %s clasifica M4/%s" % (_sub, _sub), _cod == "M4/" + _sub)

# ---------------------------------------------------------------------------
# F. INTEGRIDAD DE IMAGENES (06/09/2026 — auditoria visual de las tres munecas)
#    Funciones PURAS a proposito: reciben bytes y medidas, no abren archivos ni
#    llaman a git. Asi corren en el clon sparse, que tiene 0 PNG en disco.
# ---------------------------------------------------------------------------

# F1 poses duplicadas por md5 dentro de un mismo look.
# Medido ese dia: ele L819 y anais L83 tenian un archivo byte-a-byte duplicado
# haciendose pasar por dos poses, y los dos figuraban 7/7 con 6 poses reales.
from integridad_imagenes import duplicados_por_look                  # noqa: E402
_pack = {"ele_819_seated.png": b"AAA", "ele_819_side_profile.png": b"AAA",
         "ele_819_standing.png": b"BBB"}
check("integridad: caza el par byte-identico",
      duplicados_por_look(_pack) == [("ele_819_seated.png", "ele_819_side_profile.png")])
check("integridad: no inventa duplicados",
      duplicados_por_look({"a.png": b"1", "b.png": b"2"}) == [])
check("integridad: tres iguales dan los tres pares",
      len(duplicados_por_look({"a.png": b"X", "b.png": b"X", "c.png": b"X"})) == 3)

# F2 orientacion por slot. El septimo slot (Odalisque) es el unico apaisado del
# set; cuatro de Miss Doll (L75, L79, L83, L85) salieron verticales y ningun
# control lo miraba.
from integridad_imagenes import orientacion_correcta                 # noqa: E402
check("orientacion: odalisque apaisada es correcta",
      orientacion_correcta("miss_doll_083_odalisque.png", 1200, 669))
check("orientacion: odalisque vertical NO es correcta",
      not orientacion_correcta("miss_doll_083_odalisque.png", 669, 1200))
check("orientacion: standing vertical es correcta",
      orientacion_correcta("ele_827_standing.png", 669, 1200))
check("orientacion: standing apaisada NO es correcta",
      not orientacion_correcta("ele_827_standing.png", 1200, 669))
check("orientacion: el slot 5 se llama distinto en cada muneca y todos van verticales",
      all(orientacion_correcta(f"x_{p}.png", 669, 1200)
          for p in ("ditzy", "glacial_command", "sovereign_gaze")))

# F3 duplicado por blob SHA del indice de git — la version barata del F1.
# Leer los bytes de las 8.504 imagenes toma minutos por corrida; el indice ya
# trae el SHA de cada blob y dos SHA iguales SON el mismo contenido.
from integridad_imagenes import duplicados_por_sha                   # noqa: E402
check("integridad: caza el duplicado por SHA sin leer bytes",
      duplicados_por_sha({"a.png": "563d79d8", "b.png": "563d79d8", "c.png": "0f1e2d3c"})
      == [("a.png", "b.png")])
check("integridad: SHA distintos no son duplicado",
      duplicados_por_sha({"a.png": "111", "b.png": "222"}) == [])
check("integridad: SHA y bytes dan el mismo veredicto",
      len(duplicados_por_sha({"a.png": "h1", "b.png": "h1"}))
      == len(duplicados_por_look({"a.png": b"Z", "b.png": b"Z"})))

# F4 veredicto de orientacion en TRES estados, no en dos.
# Medido el 06/09/2026 al cablear el chequeo: 18 odalisques de Miss Doll PIDEN
# vertical en su propio prompt y 30 no declaran nada. La imagen obedecio. Un
# chequeo binario los habria marcado a los 37 como defecto de render y habria
# mandado a regenerar imagenes correctas — el linter que grita por lo que no se
# puede arreglar es el que enseña a ignorarlo.
from integridad_imagenes import veredicto_orientacion                # noqa: E402
check("veredicto: apaisada y el prompt pedia apaisada -> ok",
      veredicto_orientacion("x_odalisque.png", 1200, 669, "16:9") == "ok")
check("veredicto: vertical con prompt que pedia apaisada -> defecto de RENDER",
      veredicto_orientacion("x_odalisque.png", 669, 1200, "16:9") == "render")
check("veredicto: vertical y el prompt tambien pedia vertical -> defecto de PROMPT",
      veredicto_orientacion("x_odalisque.png", 669, 1200, "9:16") == "prompt")
check("veredicto: el prompt no declara orientacion -> hueco, no defecto",
      veredicto_orientacion("x_odalisque.png", 669, 1200, None) == "sin_declarar")
check("veredicto: standing vertical con prompt vertical -> ok",
      veredicto_orientacion("x_standing.png", 669, 1200, "9:16") == "ok")
check("veredicto: standing apaisada -> defecto de render",
      veredicto_orientacion("x_standing.png", 1200, 669, "9:16") == "render")

# F5 el parser de orientacion no se estrecha en silencio.
# Historia: la primera version exigia `### N. Odalisque` + fence ```text y
# parseaba 20 de 628 looks de Ele, reportando 86 "sin declarar" que eran su
# propio hueco. La segunda acepto `**N. Odalisque:**` y subio a 21. Recien
# cortando por tramo entre encabezados (sin mirar el fence) llego a 624.
# Este check existe para que nadie vuelva a estrecharlo sin que la bateria grite.
import sync_imagenes_subidas as _sync                                # noqa: E402
_orient = _sync.orientacion_pedida("00_Ele/galeria_outfits.md")
check("orientacion: el parser cubre casi toda la galeria de Ele",
      len(_orient) >= 600, "parsea %d looks" % len(_orient))
check("orientacion: distingue declarado de no declarado",
      sum(1 for v in _orient.values() if v == "16:9") > 100
      and sum(1 for v in _orient.values() if v is None) > 0)

# F6 mojibake en la galeria — el hueco que no era de nadie.
# Medido el 06/09/2026: 11 looks de Ele (L690-L700) con el encoding roto
# mientras lint_higiene_repo.py daba el repo LIMPIO. Su chequeo H6 excluye las
# galerias a proposito (son de lint_galeria) y lint_galeria no miraba encoding.
from lint_galeria import secuencias_mojibake                        # noqa: E402
check("mojibake: caza el punto medio roto",
      secuencias_mojibake("batch L691 Â· Gym") == ["Â·"])
_roto = lambda c: c.encode("utf-8").decode("cp1252")
check("mojibake: caza la raya larga rota",
      secuencias_mojibake("dusty rose " + _roto("—") + " Contraste")
      == [_roto("—")])
check("mojibake: caza el emoji roto",
      secuencias_mojibake(_roto("🫦") + " atroz") == [_roto("🫦")])
check("mojibake: texto sano con emojis y acentos NO dispara",
      secuencias_mojibake("Look 827 · Lencería 🫦 atroz de regio 💅") == [])
check("mojibake: acento correcto solo NO dispara",
      secuencias_mojibake("Anais Belland, la regenta: cómo, qué, mañana") == [])

# G. ROTACION DE SUB-POSES ENTRE LOOKS (06/09/2026)
#    El chequeo 7 de lint_prompts_personaje detecta poses duplicadas DENTRO de
#    un look y jamas ENTRE looks. Con indice = (look-1+off) %% n, cada slot se
#    repite cada n looks; como los 7 repertorios de Anais miden 7, sus L83/L84/
#    L85 repiten la postura completa de L76/L77/L78 — verbatim, 47 palabras
#    identicas en Standing. El defecto no vivio porque un chequeo fallara: vivio
#    porque NO EXISTIA.
from rotacion_poses import indice_de, colisiones                     # noqa: E402
check("rotacion: la formula espeja prompt_builder.pose()",
      indice_de("standing", 817, {"standing": 5}, 9) == (817 - 1 + 5) % 9)
_rep7 = {"offsets": {"standing": 0, "pov": 3},
         "slots": {"standing": ["a"] * 7, "pov": ["b"] * 7}}
_col = colisiones([76, 83], _rep7)
check("rotacion: caza el par a distancia n en los dos slots",
      len(_col) == 1 and _col[0]["a"] == 76 and _col[0]["b"] == 83
      and _col[0]["slots"] == ["pov", "standing"])
check("rotacion: looks consecutivos NO colisionan (paso 1, n>1)",
      colisiones([76, 77], _rep7) == [])
_rep9 = {"offsets": {"odalisque": 0}, "slots": {"odalisque": ["x"] * 9}}
check("rotacion: con 9 variantes el par a distancia 7 se salva",
      colisiones([75, 82], _rep9) == [])
check("rotacion: el orden pone primero al par que mas comparte",
      [c["n"] for c in colisiones([76, 83, 84], _rep7)] == sorted(
          [c["n"] for c in colisiones([76, 83, 84], _rep7)], reverse=True))

# G2 tope de racha de medias. Regla de miss_doll.md:258, violada en el ULTIMO
# batch (L83, L84 y L85, tres seguidas) y encontrada por revision externa despues
# de que mi propia auditoria no la mirara.
from garment_canon import lleva_medias, audit_racha_medias           # noqa: E402
_CON = "sheer black stockings held by a suspender belt"
_SIN = "bare legs, no stockings"
check("medias: 'no stockings' NO cuenta como que lleva medias",
      not lleva_medias(_SIN) and lleva_medias(_CON))
check("medias: dos seguidas pasan", audit_racha_medias([_SIN, _CON, _CON, _SIN]) is None)
check("medias: tres seguidas fallan", audit_racha_medias([_SIN, _CON, _CON, _CON]) is not None)
check("medias: cuatro sin medias pasan", audit_racha_medias([_SIN] * 4) is None)
check("medias: el mensaje dice el largo de la racha",
      "3" in (audit_racha_medias([_CON, _CON, _CON]) or ""))
check("medias: el maximo es parametro, no constante",
      audit_racha_medias([_CON, _CON], maximo=1) is not None
      and audit_racha_medias([_CON, _CON], maximo=2) is None)

# REGRESION 07/09/2026 — a QUIEN se culpa por la racha.
# `audit_racha_medias` devolvia solo el texto y `outfit.py generar` reconstruia
# el culpable barriendo la ventana hacia atras hasta el ultimo look CON medias.
# No es lo mismo: con la racha infractora ya escrita en la galeria (L83-L85 de
# Miss Doll) y un batch nuevo cuyo unico look con medias va al final y aislado,
# el motor frenaba el lote culpando a ese ultimo look, que no forma racha con
# nadie. Con la racha vieja dentro de la ventana de 12, ningun batch nuevo con
# una sola media podia volver a pasar.
from garment_canon import racha_medias_detalle                      # noqa: E402
_msg_r, _idx_r = racha_medias_detalle([_CON, _CON, _CON] + [_SIN] * 4 + [_CON])
check("medias: el culpable es el look que CIERRA la racha, no el ultimo con medias",
      _msg_r is not None and _idx_r == 2)
check("medias: sin racha, el detalle no devuelve indice",
      racha_medias_detalle([_SIN, _CON, _CON, _SIN]) == (None, None))

# G3 el ancla de costura no viaja en un look SIN medias.
# miss_doll L77 declara `bare legs, no stockings` en su BLOQUE B y sus prompts
# traen igual "the stockings have ONE single seam...". El disparador ya pedia dos
# condiciones (costura declarada Y contexto de media) pero ninguna miraba la
# AUSENCIA: la cadena "no stockings" CONTIENE la palabra "stockings".
_pb_seam = PromptBuilder("miss_doll")
_SIN_MEDIAS = ("a fuchsia vinyl pencil miniskirt with a fine back seam up the centre; "
               "bare legs, no stockings; closed pointed-toe platform stilettos")
_CON_MEDIAS = ("a fuchsia vinyl pencil miniskirt; sheer black stockings with a fine "
               "back seam up each leg; closed pointed-toe platform stilettos")
check("costura: look SIN medias no dispara SEAM_*",
      not [n for n in _pb_seam.opt_in_de(_SIN_MEDIAS) if n.startswith("SEAM_")])
check("costura: look CON medias SI dispara SEAM_*",
      [n for n in _pb_seam.opt_in_de(_CON_MEDIAS) if n.startswith("SEAM_")])

# G4 ninguna sub-pose IMPONE una prenda concreta.
# La sub-pose describe el CUERPO y la CAMARA; la prenda vive en el BLOQUE B, que
# es su dueño unico. Una sub-pose que nombra una prenda se la impone a TODOS los
# looks a los que les toque esa variante, la tengan o no. Medido el 06/09/2026
# por auditoria visual externa: el POV de Anais nombraba `the strand of pearls`
# (L77), `the clasp of the fur at her throat` (L80, en un look que NO lleva piel)
# y `the ring turned to the light` (L78 — de ahi el solitario que aparece en UNA
# sola pose y en ninguna otra).
#
# La regla distingue dos formas, porque no son el mismo defecto:
#   · IMPONE  -> "a single hand at the strand of pearls"      (prohibido)
#   · OFRECE  -> "a single hand at the choker, buckle or chain detail"  (valido:
#     le da alternativas al generador y funciona lleve lo que lleve el look)
# Marcar las dos igual seria un linter que grita por lo correcto.
#
# El patron se compila con `\b` de verdad y se auto-verifica antes de usarse: la
# primera version se escribio con un heredoc que convirtio el `\b` en un
# BACKSPACE literal (0x08) dentro de la r-string. El patron quedo
# '\x08(pearls?|...)\x08', no matcheo nunca, y el check paso EN VERDE sobre 8
# hallazgos reales. Invisible al leer el archivo — misma familia que el mojibake.
import json as _json                                                 # noqa: E402
_rep_all = _json.load(io.open(os.path.join(V, "repertorios_pose.json"), encoding="utf-8"))
_PRENDA_RX = re.compile(
    r"\b(pearls?|fur|gloves?|veil|corset|stockings?|necklace|bra|thong|garter"
    r"|choker|cuffs?)\b", re.I)
assert _PRENDA_RX.search("a hand at the strand of pearls"), \
    "el patron de prenda no compila (revisa que los \\b sean escapes y no bytes)"
assert not _PRENDA_RX.search("a hand at her collarbone"), "el patron matchea de mas"


def _impone(texto, m):
    """True si la prenda se impone; False si la clausula ofrece alternativas."""
    ini = max(0, m.start() - 60)
    fin = min(len(texto), m.end() + 60)
    return " or " not in texto[ini:fin]


_sucias = []
for _slug, _p in _rep_all.get("personajes", {}).items():
    for _slot, _vars in _p.get("slots", {}).items():
        for _i, _v in enumerate(_vars):
            for _m in _PRENDA_RX.finditer(_v):
                if _impone(_v, _m):
                    _sucias.append("%s/%s[%d]:%s" % (_slug, _slot, _i, _m.group(1)))
                    break
check("repertorio: ninguna sub-pose IMPONE una prenda concreta",
      not _sucias, "%d hallazgo(s): %s" % (len(_sucias), "; ".join(_sucias[:8])))

# H. AUDITOR DE CIERRE DEL MOTOR (Ama 07/09/2026: "mete al final del outfit
#    engine un pequeño auditor").
#
#    Por que al FINAL y no en la puerta. `generar` ya bloquea ANTES de escribir,
#    y eso mide las ENTRADAS: el BLOQUE B, el color, la arquitectura. Lo que
#    nadie miraba es el ARTEFACTO — los prompts ya expandidos, que es lo unico
#    que llega al generador. La regla del repo es literal: verificar el
#    artefacto, nunca el reporte. Un batch puede pasar todas las validaciones de
#    entrada y salir con el zapato distinto en la pose 4 porque el token se
#    expandio mal.
#
#    Chequea lo que solo se puede ver DESPUES de expandir, y nada mas — es un
#    auditor pequeño a proposito:
#      A1 los 7 slots presentes, sin faltantes ni repetidos
#      A2 el token de calzado IDENTICO en las 7 poses (Ley de Continuidad)
#      A3 el BLOQUE B IDENTICO en las 7 poses
#      A4 ningun placeholder sin resolver ({seat}, [BLOQUE A]) sobrevivio
#      A5 la Odalisque pide apaisada y ninguna otra pose lo hace
from auditor_cierre import auditar_batch                             # noqa: E402

_BB = "a jade vinyl mini dress; closed pointed-toe stiletto pumps, 12cm pin heel"
_OK = {n: _BB + " ... " + n + (" aspect ratio 16:9" if n == "odalisque"
                               else " aspect ratio 9:16")
       for n in ("standing", "back_view", "seated", "side_profile", "ditzy", "pov",
                 "odalisque")}
check("cierre: un batch sano no tiene hallazgos", auditar_batch({1: _OK}) == [])

_falta = {1: {k: v for k, v in _OK.items() if k != "pov"}}
check("cierre: A1 caza un slot faltante",
      any("A1" in h for h in auditar_batch(_falta)))

_zap = dict(_OK)
_zap["seated"] = _zap["seated"].replace("12cm pin heel", "10cm block heel")
check("cierre: A2 caza el zapato que cambia entre poses",
      any("A2" in h for h in auditar_batch({1: _zap})))

_out = dict(_OK)
_out["ditzy"] = _out["ditzy"].replace("jade vinyl mini dress", "jade vinyl catsuit")
check("cierre: A3 caza el BLOQUE B que cambia entre poses",
      any("A3" in h for h in auditar_batch({1: _out})))

_ph = dict(_OK)
_ph["seated"] = _ph["seated"] + " perched on {seat}"
check("cierre: A4 caza un placeholder sin resolver",
      any("A4" in h for h in auditar_batch({1: _ph})))

_ori = dict(_OK)
_ori["odalisque"] = _ori["odalisque"].replace("16:9", "9:16")
check("cierre: A5 caza la Odalisque pedida en vertical",
      any("A5" in h for h in auditar_batch({1: _ori})))

_ori2 = dict(_OK)
_ori2["standing"] = _ori2["standing"].replace("9:16", "16:9")
check("cierre: A5 caza una pose vertical pedida apaisada",
      any("A5" in h for h in auditar_batch({1: _ori2})))

# I. ECO DE BUSTO EN LOS PLANOS CERRADOS (Ama 07/09/2026)
#    Decision suya tras la auditoria visual: "si, solo escote y busto".
#
#    El defecto medido en las 3 muñecas: Ditzy, POV, Sovereign Gaze y Glacial
#    Command REINVENTAN la prenda de arriba. L820 POV saca el busto FUERA de la
#    copa; L821 Ditzy le pone tirante a un bandeau declarado strapless; L819
#    cambia la construccion de las copas; en Miss Doll el volumen de busto es
#    mayor en los planos medios en 4 de 4 looks multipose. Sin cuerpo entero que
#    ancle la construccion, el generador la inventa.
#
#    El repo ya tiene exactamente este mecanismo para el calzado
#    (`footwear_echo`) desde que la Ama reporto el "zapato que muta". Esto es su
#    hermano para el busto, y solo para el busto: repetir el outfit entero
#    alargaria un prompt que YA esta saturado (clausulas con peso 1.4 que se
#    ignoran).
from garment_canon import eco_busto                                  # noqa: E402

check("eco: extrae la construccion de la copa",
      "moulded balconette cups" in (eco_busto(
          "a jade vinyl mini dress with moulded balconette cups and a straight "
          "bandeau neckline, closed pointed-toe stiletto pumps") or ""))
check("eco: extrae el escote strapless y lo afirma",
      "strapless" in (eco_busto(
          "an emerald satin strapless bustier, boned, with a sweetheart neckline; "
          "a matching thong") or "").lower())
check("eco: un look sin prenda de arriba no genera eco",
      eco_busto("sheer black stockings and closed pointed-toe stiletto pumps, bare torso")
      is None)
check("eco: el eco NO nombra el calzado (de eso se encarga footwear_echo)",
      "stiletto" not in (eco_busto(
          "a jade vinyl mini dress with moulded balconette cups, closed "
          "pointed-toe stiletto pumps with a 12cm pin heel") or "").lower())
check("eco: es CORTO — el prompt ya esta saturado",
      len(eco_busto("an emerald satin strapless bustier, boned, with a sweetheart "
                    "neckline and moulded cups; a matching thong") or "") < 260)
check("eco: el override declarado en el batch manda sobre la extraccion",
      eco_busto("cualquier cosa", declarado="the cups exactly as described above")
      == "the cups exactly as described above")

# J. NINGUN FUENTE LLEVA CARACTERES DE CONTROL INVISIBLES (07/09/2026)
#
#    Pasó DOS VECES el mismo dia. Al escribir codigo desde un heredoc, un `\b`
#    destinado a ser el "limite de palabra" de una regex termino como el BYTE
#    0x08 (backspace) dentro de la r-string. El patron quedaba
#    '\x08(pearls?|...)\x08' y '\x08(stiletto|...)\x08': **no matcheaban nada**.
#
#    Lo grave no es el error, es que es INVISIBLE. El archivo se lee normal, el
#    linter no dice nada, y el check pasa EN VERDE sobre 8 hallazgos reales la
#    primera vez y sobre un eco que nunca se generaba la segunda. Misma familia
#    que el mojibake de las galerias: caracteres que no se ven y mienten.
#
#    Este check barre TODO `99_Sistema/scripts` y es la unica defensa que no
#    depende de que yo me acuerde.
_CTRL_OK = "\r\n\t"
_sucios = []
for _raiz, _dirs, _files in os.walk(os.path.join(RAIZ, "99_Sistema", "scripts")):
    _dirs[:] = [d for d in _dirs if d not in ("__pycache__", ".git")]
    for _f in _files:
        if not _f.endswith((".py", ".json")):
            continue
        _ruta = os.path.join(_raiz, _f)
        try:
            _t = io.open(_ruta, encoding="utf-8", newline="").read()
        except (OSError, UnicodeDecodeError):
            continue
        _mal = sorted({hex(ord(c)) for c in _t if ord(c) < 32 and c not in _CTRL_OK})
        if _mal:
            _sucios.append("%s %s" % (os.path.relpath(_ruta, RAIZ), _mal))
check("fuentes: ningun script lleva caracteres de control invisibles",
      not _sucios, "; ".join(_sucios[:5]))

print()
print("=" * 74)
print("RESULTADO: %d ok · %d fallas" % (ok, fallo))
if notas:
    print("  fallaron: %s" % "; ".join(notas))
print("=" * 74)
sys.exit(1 if fallo else 0)
