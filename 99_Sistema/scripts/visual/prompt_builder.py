#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
prompt_builder.py — Ensamblador de prompts del outfit-engine (multi-personaje).

QUE HACE
--------
Convierte los tres bloques de un look en los N prompts FINALES, completos y
autocontenidos, que se escriben en la galeria del personaje y que la LV-App
manda literalmente al generador.

    BLOQUE A (ADN)  +  BLOQUE B (outfit)  +  BLOQUE C (pose + setting)
                              |
                        build_prompt()
                              |
                    prompt final expandido + anclas anti-defecto

POR QUE EXISTE
--------------
El SKILL del motor escribia la formula como "[BLOQUE A] + [BLOQUE B] + [BLOQUE C]".
Eso era NOTACION, no texto. El 11/08/2026 los 98 prompts de Miss Doll se
escribieron con esos corchetes LITERALES dentro del bloque de codigo: la app los
habria mandado tal cual a Gemini, sin cara, sin cuerpo, sin ropa y sin setting.
Mismo modo de falla que el placeholder [ADN] de Anais. Un ensamblador comun hace
que no pueda volver a pasar, y sirve para cualquier personaje futuro.

SUB-POSES (13/08/2026)
----------------------
El BLOQUE C no se escribe a mano por look: la clausula de pose sale del
repertorio del personaje via pose(). Sin eso, los N looks salian con la MISMA
frase de camara y las imagenes se veian iguales — medido el 13/08 en Miss Doll:
41-70% de similitud por slot, y el unico slot sano era el unico con repertorio.
Ele tenia el suyo desde el 08/06 pero vivia en pose_rotation_v5.py, motor de UN
personaje, y nunca llego a las otras dos. Un fix que vive en el motor de un
personaje no es un fix.

DUENO UNICO
-----------
El texto literal de las anclas vive en anclas_universales.json.
El texto de las sub-poses vive en repertorios_pose.json.
Este script los lee, no los copia.

USO COMO LIBRERIA
-----------------
    from prompt_builder import PromptBuilder
    pb = PromptBuilder("miss_doll")
    pose = pb.pose("standing", 8, props={"upright": "the chrome stage pole",
                                         "surface": "the VIP platform edge"})
    prompt = pb.build(bloque_a, bloque_b, "standing", pose, setting)

USO COMO CLI (autotest de la libreria)
--------------------------------------
    python 99_Sistema/scripts/visual/prompt_builder.py --personajes
    python 99_Sistema/scripts/visual/prompt_builder.py --anclas miss_doll
    python 99_Sistema/scripts/visual/prompt_builder.py --poses miss_doll
    python 99_Sistema/scripts/visual/prompt_builder.py --pose anais odalisque 7
"""

import datetime
import json
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

AQUI = os.path.dirname(os.path.abspath(__file__))
JSON_ANCLAS = os.path.join(AQUI, "anclas_universales.json")
JSON_POSES = os.path.join(AQUI, "repertorios_pose.json")
LOG_PATH = os.path.normpath(os.path.join(AQUI, "..", "..", "logs", "outfit_engine.jsonl"))


def _log_evento(entrada):
    """Escribe una linea JSONL en LOG_PATH. Dueno unico del log del motor.

    Cada build() de cada personaje queda registrado (timestamp, personaje,
    slot, largo del prompt, anclas opt-in disparadas, fallas de validar()).
    Nace de la auditoria del 17/08/2026: sin rastro de cuando se genero
    cada prompt, reconstruir que bloque de codigo se copio de donde (el bug
    del prefijo "power portrait" copiado del Look 14 al batch L15-L20) fue
    trabajo manual sobre el historial de git en vez de una consulta directa.
    """
    entrada = dict(entrada)
    entrada["ts"] = datetime.datetime.now().isoformat(timespec="seconds")
    try:
        os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps(entrada, ensure_ascii=False) + "\n")
    except OSError:
        pass

# Placeholders de mobiliario ({seat}/{wall}/{surface}/{upright}) que el inyector
# DEBE resolver con mobiliario real del setting del look antes de escribir el prompt.
PROPS_SIN_RESOLVER = re.compile(r"\{(\w+)\}")

# Marcadores de placeholder que JAMAS pueden sobrevivir en un prompt final.
PLACEHOLDERS_PROHIBIDOS = re.compile(
    r"\[\s*(BLOQUE|ADN|DNA|OUTFIT|SETTING|POSE)\b[^\]]*\]", re.IGNORECASE
)


def cargar_config(ruta=JSON_ANCLAS):
    with open(ruta, encoding="utf-8") as f:
        return json.load(f)


def cargar_repertorios(ruta=JSON_POSES):
    """Repertorios de sub-poses por personaje (dueno unico: repertorios_pose.json)."""
    with open(ruta, encoding="utf-8") as f:
        return json.load(f)


def slugify(nombre):
    """Algoritmo de slug del contrato de galeria (regla 11 §2)."""
    import unicodedata

    plegado = unicodedata.normalize("NFD", nombre)
    plegado = "".join(c for c in plegado if unicodedata.category(c) != "Mn")
    plegado = plegado.lower().replace("-", "").replace("'", "").replace("\u2019", "")
    plegado = re.sub(r"[^a-z0-9]+", "_", plegado)
    return plegado.strip("_")


class PromptBuilder(object):
    """Ensamblador para un personaje concreto. Agnostico de personaje por diseno."""

    def __init__(self, slug, config=None, repertorios=None):
        self.cfg = config or cargar_config()
        if slug not in self.cfg["personajes"]:
            raise KeyError(
                "Personaje '%s' no registrado en anclas_universales.json. "
                "Un personaje nuevo se agrega ahi + su perfil visual, NUNCA con un motor nuevo."
                % slug
            )
        self.slug = slug
        self.perfil = self.cfg["personajes"][slug]
        self.anclas = self.cfg["anclas"]
        self.mapa = self.cfg["mapa_por_defecto"]
        self.overrides = self.perfil.get("overrides", {})
        self.rep_cfg = repertorios or cargar_repertorios()
        self.repertorio = self.rep_cfg["personajes"].get(slug)

    # ------------------------------------------------------------------ anclas

    @property
    def anclas_siempre(self):
        """Anclas propias del personaje presentes en TODOS sus slots (13/08/2026).

        Van despues de `_todos` y antes de las de slot. Existen para prohibiciones
        que son de canon de UN personaje: BOTTOM_CUT_LOCK es de Ele y Miss Doll,
        y a Anais le romperia su calzon retro de epoca.
        """
        return list(self.perfil.get("anclas_siempre", []))

    @property
    def n_globales(self):
        """Cuantas anclas de `anclas_de_slot` son globales (no del slot)."""
        return len(self.mapa.get("_todos", [])) + len(self.anclas_siempre)

    def anclas_de_slot(self, slot):
        """Nombres de ancla que aplican a un slot, en orden de escritura."""
        slot = self.normalizar_slot(slot)
        base = list(self.mapa.get("_todos", [])) + self.anclas_siempre
        especificas = self.overrides.get(slot, self.mapa.get(slot, []))
        return base + list(especificas)

    def texto_anclas(self, slot):
        return [self.anclas[n]["texto"] for n in self.anclas_de_slot(slot)]

    def normalizar_slot(self, slot):
        """Acepta el slug propio del personaje para el slot 5 y lo mapea a 'slot5'."""
        s = slot.strip().lower().replace(" ", "_")
        if s == self.perfil["slot5_slug"] or s == "slot5":
            return "slot5"
        return s

    # --------------------------------------------------------------- sub-poses

    def variaciones(self, slot):
        """Sub-poses disponibles para un slot de este personaje."""
        slot_n = self.normalizar_slot(slot)
        if not self.repertorio:
            raise KeyError(
                "Personaje '%s' sin repertorio de sub-poses en repertorios_pose.json. "
                "Sin repertorio, los N looks salen con la MISMA clausula de pose y las "
                "imagenes se ven iguales (medido: Miss Doll 41-70%% por slot, 13/08/2026)."
                % self.slug
            )
        v = self.repertorio["slots"].get(slot_n)
        if not v:
            raise KeyError("'%s' no tiene sub-poses para el slot '%s'." % (self.slug, slot_n))
        return v

    def pose(self, slot, look_number, props=None, indice=None):
        """
        Devuelve el TEXTO de sub-pose que le toca a este look en este slot.

        Es lo unico que varia entre los N prompts de un look: encuadre, gesto y
        mirada. Nada de pelo, color, unas ni piel — eso vive en BLOQUE A/B.

        slot        : standing | back_view | seated | side_profile | <slot5> | pov | odalisque
        look_number : numero de look (la rotacion sale de aqui)
        props       : mobiliario REAL del setting -> {"seat": "a chrome bench", "upright": "the stage pole", ...}
        indice      : fuerza una variacion concreta (para tests o para un look especial)

        Rotacion: indice = (look_number - 1 + offset_del_slot) %% n. Si la variacion
        que toca pide un prop que este look no tiene, se salta a la siguiente — nunca
        se escribe un placeholder sin resolver (ese fue el bug del 11/08 con [BLOQUE A]).
        """
        slot_n = self.normalizar_slot(slot)
        variantes = self.variaciones(slot_n)
        props = dict(props or {})
        n = len(variantes)
        off = self.repertorio.get("offsets", {}).get(slot_n, 0)
        i0 = (look_number - 1 + off) % n if indice is None else indice % n

        faltantes = set()
        for salto in range(n):
            i = (i0 + salto) % n
            pedidos = set(PROPS_SIN_RESOLVER.findall(variantes[i]))
            sin_resolver = set(p for p in pedidos if not props.get(p))
            if not sin_resolver:
                return self._limpiar(variantes[i].format(**props))
            faltantes |= sin_resolver
        raise ValueError(
            "Ninguna de las %d sub-poses de '%s/%s' se puede resolver: falta(n) el prop %s. "
            "Nombra mobiliario real del setting del look (Ama 08/06/2026: 'cada pose debe ser "
            "armoniosa con el ambiente')." % (n, self.slug, slot_n, sorted(faltantes))
        )

    # ------------------------------------------------------ prefijo por arquetipo

    def prefijo_arquetipo(self, arquetipo):
        """Prefijo cinematografico + clave de luz que le toca a este arquetipo.

        Blindaje 17/08/2026: el batch L15-L20 de Anais salio con el prefijo
        de Ejecutivo (`power portrait`) copiado a los 6 looks nuevos sin
        variar por arquetipo, y Boudoir/Lenceria perdio por completo su
        `warm amber candlelight chiaroscuro`. La tabla existia en
        dna_v2_3.md, pero era un documento — nadie la volvia a consultar al
        copiar un bloque de codigo. Esta funcion es la MISMA tabla, pero
        hecha de la que el motor puede leer en vez de que un humano recuerde
        volver a abrir el archivo. Uso: pb.prefijo_arquetipo("Boudoir / Lencería")
        -> {"prefijo": "...", "luz": "..."}. El linter (chequeo 11) usa esto
        mismo para verificar cada look contra su Arquetipo declarado.
        """
        tabla = self.perfil.get("prefijos_arquetipo")
        if not tabla:
            raise KeyError(
                "Personaje '%s' no tiene tabla de prefijos por arquetipo en "
                "anclas_universales.json (personajes.%s.prefijos_arquetipo). "
                "Solo Anais usa prefijo cinematografico por diseno; si esto es "
                "un personaje nuevo que SI lo necesita, agregar la tabla ahi, "
                "nunca hardcodear el prefijo en la galeria." % (self.slug, self.slug)
            )
        if arquetipo not in tabla:
            disponibles = [k for k in tabla if not k.startswith("_")]
            raise KeyError(
                "Arquetipo '%s' no esta en la tabla de %s. Disponibles: %s. "
                "Si el arquetipo es real y nuevo, agregarlo a la tabla ANTES "
                "de escribir el look — nunca copiar el prefijo del look anterior."
                % (arquetipo, self.slug, ", ".join(disponibles))
            )
        return dict(tabla[arquetipo])

    def orientacion_odalisque(self, look_number):
        """Ancla de orientacion (ASPECT_VERTICAL/ASPECT_HORIZONTAL) para un
        Odalisque que ALTERNA por numero de look en vez de ir fija.

        Ela y Anais tienen Odalisque reclinado -> ASPECT_HORIZONTAL fijo en
        mapa_por_defecto, ninguna alternancia. Miss Doll tiene Odalisque
        sentada en el piso (Throne en Suelo) -- ninguna orientacion es "la"
        natural del encuadre, y la Ama pidio variedad (17/08/2026: "Miss Doll
        debe tener Odalisque en vertical y horizontal"). Por eso NO vive en
        el mapa estatico de anclas_universales.json (personajes.<slug>.
        orientacion_alterna documenta el porque) -- se resuelve aqui, con el
        mismo criterio de rotacion determinista que pose(), y el injector la
        pasa a build() via extra_anclas=[pb.orientacion_odalisque(look_number)].
        """
        return "ASPECT_HORIZONTAL" if look_number % 2 == 0 else "ASPECT_VERTICAL"

    def pose_indice(self, slot, look_number):
        """Indice crudo que le toca al look (sin considerar props). Util para auditar rotacion."""
        slot_n = self.normalizar_slot(slot)
        n = len(self.variaciones(slot_n))
        off = self.repertorio.get("offsets", {}).get(slot_n, 0)
        return (look_number - 1 + off) % n

    # ----------------------------------------------------------------- ensamble

    OPT_IN = (
        ("ASYMMETRY_LOCK", re.compile(
            r"asymmetric|one[- ]shoulder|single shoulder|single strap|one sleeve|"
            r"single sleeve|asymmetric hem|one glove", re.I)),
        ("ACCESSORY_COUNT_LOCK", re.compile(
            r"\ba single (oversized )?(chrome |gold |silver )?"
            r"(cuff|bracelet|bangle|glove|earring|anklet|ankle chain|ring)\b|\bone glove\b", re.I)),
        ("GARMENT_EXCLUSION_LOCK", re.compile(
            r"\bno (corset|stockings|hosiery|tights|jewelry|jewellery|gloves|bra|straps|"
            r"other jewelry|other jewellery)\b|\bbare legs\b", re.I)),
        # Ama 13/08/2026: con vestido/falda las piernas van cerradas, en las tres.
        # `sundress`, `shirtdress`, `coatdress` y `miniskirt` entran por el prefijo
        # [a-z]*; `headdress` (tocado, 35 usos en la galeria de Ele), `undress` y
        # `nodress` quedan FUERA por el lookahead: no son prendas de falda.
        # [a-z] y no \w a proposito — con \w el patron se comia slugs enteros de
        # ruta (`look675_onyx_baroque_coatdress`) en vez del nombre de la prenda.
        ("DRESS_LEG_CLOSURE", re.compile(
            r"\b(?!headdress|undress|nodress)[a-z]*dress(es)?\b|\bgown\b|"
            r"\b[a-z]*skirt(ed|s)?\b|\brobe\b|\bkimono\b|\btunic\b|"
            r"\bcheongsam\b|\bqipao\b|\bsarong\b", re.I)),
    )

    # Prendas cuyo CORTE debe nombrarse en el BLOQUE B (BOTTOM_CUT_LOCK, Ama 13/08/2026).
    # `bottom` a secas queda FUERA a proposito: aparece en "bottom of the frame".
    RX_CALZON = re.compile(
        r"\b(panty|panties|knicker(s)?|brief(s)?|bikini bottom(s)?|swim bottom(s)?|"
        r"thong|g-string|gstring|tanga|micro[- ]?short(s)?|hot pant(s)?)\b", re.I)
    RX_CORTE_OK = re.compile(r"\b(thong|g-string|gstring|tanga)\b", re.I)

    def calzon_sin_corte(self, texto):
        """True si el texto nombra un calzon SIN declarar corte tanga/g-string.

        Se descuenta el texto de BOTTOM_CUT_LOCK antes de medir: el ancla dice
        "thong or g-string" y, si no se descontara, se validaria a si misma
        (mismo error que el clasificador que se leia a si mismo, 19/07/2026).
        """
        t = texto or ""
        ancla = self.anclas.get("BOTTOM_CUT_LOCK", {}).get("texto", "")
        if ancla:
            t = t.replace(ancla, " ")
        return bool(self.RX_CALZON.search(t)) and not self.RX_CORTE_OK.search(t)

    def opt_in_de(self, bloque_b):
        """Anclas opt-in que dispara el BLOQUE B de este look (registro: anclas_opt_in)."""
        return [n for n, rx in self.OPT_IN if rx.search(bloque_b or "")]

    def build(self, bloque_a, bloque_b, slot, pose_text, setting,
              extra_final=None, extra_anclas=None, auto_opt_in=True):
        """
        Devuelve el prompt final expandido.

        bloque_a    : ADN literal del perfil §2 (se copia textual, nunca se resume)
        bloque_b    : outfit del dia (se copia textual e identico en las N poses)
        slot        : standing | back_view | seated | side_profile | <slot5> | pov | odalisque
        pose_text   : lo UNICO que varia entre poses (encuadre, gesto, mirada)
        setting     : BLOQUE C base del look
        extra_final : texto que se agrega al cierre (ej. prefijo cinematografico ya
                      resuelto aparte, o un refuerzo puntual del look)
        """
        slot_n = self.normalizar_slot(slot)
        a = self._limpiar(bloque_a)
        b = self._limpiar(bloque_b)
        pose = self._limpiar(pose_text)
        setting = self._limpiar(setting)

        anclas = self.texto_anclas(slot_n)
        # SINGLE_FRAME, GARMENT_CONSISTENCY, PHOTOREAL_LOCK y las `anclas_siempre`
        # del personaje van antes de la pose (contexto global); las de slot van
        # pegadas a la pose porque corrigen ESA toma.
        globales = anclas[: self.n_globales]
        de_slot = anclas[self.n_globales:]

        # Anclas opt-in: las dispara el BLOQUE B del look, no el slot.
        nombres_extra = list(extra_anclas or [])
        if auto_opt_in:
            for n in self.opt_in_de(bloque_b):
                if n not in nombres_extra:
                    nombres_extra.append(n)
        globales = globales + [self.anclas[n]["texto"] for n in nombres_extra]

        # FOOTWEAR_ECHO cierra siempre (va despues del setting, como en la flota de Ele).
        eco = None
        nombres_slot = self.anclas_de_slot(slot_n)[self.n_globales:]
        if "FOOTWEAR_ECHO" in nombres_slot:
            eco = self.anclas["FOOTWEAR_ECHO"]["texto"]
            de_slot = [t for t in de_slot if t != eco]

        # La MIRADA cierra despues del extra_final (17/08/2026).
        # Es lo unico que separa el slot5 (mira fuera) del POV (mira al lente).
        # Si el look trae un extra_final de tono, ese texto quedaba ULTIMO y le
        # ganaba: medido en el Look 25 de Miss Doll, cuya clausula "aqui su
        # frialdad se ablanda en una sonrisa calida" convivia con "gaze drifting
        # off ... with cold indifference" en el mismo prompt — gano la sonrisa,
        # la mirada se fue al lente y el slot5 salio casi identico al POV.
        # Mismo tratamiento que FOOTWEAR_ECHO: se saca del cuerpo y cierra.
        mirada = None
        for _n in ("GAZE_OFF_LENS", "GAZE_TO_LENS"):
            if _n in nombres_slot:
                mirada = self.anclas[_n]["texto"]
                de_slot = [t for t in de_slot if t != mirada]
                break

        partes = []
        partes.append(self._punto(a))
        partes.append(self._punto(b))
        cuerpo = ", ".join(globales + de_slot + [pose, setting])
        partes.append(cuerpo)
        prompt = " ".join(partes).strip()
        if eco:
            prompt = prompt.rstrip(" .,") + ", " + eco
        if extra_final:
            prompt = prompt.rstrip(" .,") + ", " + self._limpiar(extra_final)
        if mirada:
            prompt = prompt.rstrip(" .,") + ", " + mirada
        prompt = prompt.rstrip(" ,")
        if not prompt.endswith("."):
            prompt += "."
        prompt = self._colapsar(prompt)

        fallas = self.validar(prompt)
        _log_evento({
            "evento": "build",
            "personaje": self.slug,
            "slot": slot_n,
            "chars": len(prompt),
            "anclas_opt_in": nombres_extra,
            "fallas": fallas,
        })
        return prompt

    def build_negative(self, base):
        """
        Fuente unica del negative de un look: el base del perfil §3 + la capa
        universal anti-collage/anatomia/selfie. Nunca se escribe a mano.
        """
        base = self._limpiar(base).rstrip(",")
        universal = self._limpiar(self.cfg["negative_universal"]["texto"])
        vistos = []
        for t in [x.strip() for x in (base + ", " + universal).split(",")]:
            if t and t.lower() not in [v.lower() for v in vistos]:
                vistos.append(t)
        negativo = ", ".join(vistos)
        _log_evento({
            "evento": "build_negative",
            "personaje": self.slug,
            "chars": len(negativo),
        })
        return negativo

    # ------------------------------------------------------------------ utiles

    @staticmethod
    def _limpiar(t):
        return re.sub(r"\s+", " ", (t or "").strip()).strip(" ,;")

    @staticmethod
    def _punto(t):
        t = t.rstrip(" ,;")
        return t if t.endswith(".") else t + "."

    @staticmethod
    def _colapsar(t):
        t = re.sub(r"\s+", " ", t)
        t = re.sub(r"\s+([,.;])", r"\1", t)
        t = re.sub(r",\s*,+", ", ", t)
        return t.strip()

    # --------------------------------------------------------------- validacion

    @staticmethod
    def validar(prompt):
        """Devuelve lista de fallas. Vacia = el prompt es apto para la app."""
        fallas = []
        m = PLACEHOLDERS_PROHIBIDOS.search(prompt)
        if m:
            fallas.append("placeholder sin expandir: %s" % m.group(0))
        props = PROPS_SIN_RESOLVER.findall(prompt)
        if props:
            fallas.append("prop de mobiliario sin resolver: %s — el inyector debe nombrar "
                          "mobiliario real del setting del look" % ", ".join("{%s}" % p for p in props))
        if len(prompt) < 400:
            fallas.append("prompt sospechosamente corto (%d chars): "
                          "un prompt con ADN + outfit + anclas no baja de ~1.000" % len(prompt))
        if "a single continuous photograph" not in prompt:
            fallas.append("falta el ancla SINGLE_FRAME (anti-collage)")
        bajo = prompt.lower()
        for token in ("in every shot", "identical across all", "in all poses", "each pose"):
            if token in bajo:
                fallas.append("metalenguaje multi-toma prohibido: '%s' (causa registrada de collage)" % token)
        return fallas


# --------------------------------------------------------------------- CLI

def _cli():
    cfg = cargar_config()
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if args[0] == "--personajes":
        print("Personajes registrados en el outfit-engine:\n")
        for slug, p in cfg["personajes"].items():
            print("  %-10s  %-16s  slot5=%-16s  %s"
                  % (slug, p["nombre"], p["slot5_nombre"], p["galeria"]))
        print("\nPara agregar uno nuevo: entrada aqui + perfil visual desde la plantilla.")
        print("NUNCA un motor nuevo (esa fue la falla que dejo a Anais en 147 lineas).")
        return 0
    if args[0] == "--poses":
        slug = args[1] if len(args) > 1 else "ele"
        pb = PromptBuilder(slug, cfg)
        rep = pb.repertorio
        print("Repertorio de sub-poses de %s\n" % pb.perfil["nombre"])
        print("  registro estetico: %s\n" % rep.get("registro_estetico", "-"))
        total = 0
        for slot in cfg["slots_universales"]:
            v = rep["slots"].get(slot, [])
            total += len(v)
            nombre = pb.perfil["slot5_nombre"] if slot == "slot5" else slot
            print("  %-16s %d sub-poses   offset +%d"
                  % (nombre, len(v), rep.get("offsets", {}).get(slot, 0)))
        print("\n  TOTAL: %d sub-poses" % total)
        return 0
    if args[0] == "--pose":
        if len(args) < 4:
            print("uso: --pose <personaje> <slot> <numero_de_look>")
            return 1
        pb = PromptBuilder(args[1], cfg)
        slot, look = args[2], int(args[3])
        props = {"seat": "the named seat", "wall": "the named wall",
                 "surface": "the named surface", "upright": "the named upright"}
        print("%s · %s · Look %d -> variacion #%d\n"
              % (pb.perfil["nombre"], slot, look, pb.pose_indice(slot, look)))
        print(pb.pose(slot, look, props))
        return 0
    if args[0] == "--prefijo":
        if len(args) < 3:
            print("uso: --prefijo <personaje> <arquetipo>")
            return 1
        pb = PromptBuilder(args[1], cfg)
        arquetipo = args[2]
        p = pb.prefijo_arquetipo(arquetipo)
        print("%s · %s -> %s, %s" % (pb.perfil["nombre"], arquetipo, p["prefijo"], p["luz"]))
        return 0
    if args[0] == "--anclas":
        slug = args[1] if len(args) > 1 else "ele"
        pb = PromptBuilder(slug, cfg)
        print("Anclas por slot para %s:\n" % pb.perfil["nombre"])
        for slot in cfg["slots_universales"]:
            nombre = pb.perfil["slot5_nombre"] if slot == "slot5" else slot
            marca = "  (override)" if slot in pb.overrides else ""
            print("  %-16s -> %s%s" % (nombre, ", ".join(pb.anclas_de_slot(slot)), marca))
        return 0
    print("Argumento no reconocido: %s" % args[0])
    return 1


if __name__ == "__main__":
    sys.exit(_cli())
