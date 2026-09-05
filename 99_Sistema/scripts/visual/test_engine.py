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

print()
print("=" * 74)
print("RESULTADO: %d ok · %d fallas" % (ok, fallo))
if notas:
    print("  fallaron: %s" % "; ".join(notas))
print("=" * 74)
sys.exit(1 if fallo else 0)
