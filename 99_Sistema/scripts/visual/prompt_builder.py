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

DUENO UNICO
-----------
El texto literal de las anclas vive en anclas_universales.json. Este script lo
lee, no lo copia.

USO COMO LIBRERIA
-----------------
    from prompt_builder import PromptBuilder
    pb = PromptBuilder("miss_doll")
    prompt = pb.build(bloque_a, bloque_b, "standing", pose_text, setting)

USO COMO CLI (autotest de la libreria)
--------------------------------------
    python 99_Sistema/scripts/visual/prompt_builder.py --personajes
    python 99_Sistema/scripts/visual/prompt_builder.py --anclas miss_doll
"""

import json
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

AQUI = os.path.dirname(os.path.abspath(__file__))
JSON_ANCLAS = os.path.join(AQUI, "anclas_universales.json")

# Marcadores de placeholder que JAMAS pueden sobrevivir en un prompt final.
PLACEHOLDERS_PROHIBIDOS = re.compile(
    r"\[\s*(BLOQUE|ADN|DNA|OUTFIT|SETTING|POSE)\b[^\]]*\]", re.IGNORECASE
)


def cargar_config(ruta=JSON_ANCLAS):
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

    def __init__(self, slug, config=None):
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

    # ------------------------------------------------------------------ anclas

    def anclas_de_slot(self, slot):
        """Nombres de ancla que aplican a un slot, en orden de escritura."""
        slot = self.normalizar_slot(slot)
        base = list(self.mapa.get("_todos", []))
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

    # ----------------------------------------------------------------- ensamble

    def build(self, bloque_a, bloque_b, slot, pose_text, setting, extra_final=None):
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
        # SINGLE_FRAME y GARMENT_CONSISTENCY van antes de la pose (contexto global);
        # las de slot van pegadas a la pose porque corrigen ESA toma.
        globales = anclas[: len(self.mapa.get("_todos", []))]
        de_slot = anclas[len(self.mapa.get("_todos", [])):]

        # FOOTWEAR_ECHO cierra siempre (va despues del setting, como en la flota de Ele).
        eco = None
        nombres_slot = self.anclas_de_slot(slot_n)[len(self.mapa.get("_todos", [])):]
        if "FOOTWEAR_ECHO" in nombres_slot:
            eco = self.anclas["FOOTWEAR_ECHO"]["texto"]
            de_slot = [t for t in de_slot if t != eco]

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
        prompt = prompt.rstrip(" ,")
        if not prompt.endswith("."):
            prompt += "."
        return self._colapsar(prompt)

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
        return ", ".join(vistos)

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
