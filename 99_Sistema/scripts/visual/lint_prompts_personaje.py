#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
lint_prompts_personaje.py — Linter de galerias del outfit-engine (multi-personaje).

QUE HACE
--------
No lee la galeria como la leeria un humano: **la parsea como la parsea LV-App**
(port del parser de `GitRepository.parseMarkdown`, repo farid77cl/LV-App) y
reporta lo que la app REALMENTE va a ingerir. Despues audita ese resultado
contra el contrato del motor.

POR QUE EXISTE
--------------
El 11/08/2026 la galeria de Miss Doll "se veia bien": 14 looks, 98 prompts,
bloques ordenados. Pero cada prompt contenia los corchetes `[BLOQUE A] +
[BLOQUE B]` LITERALES, ningun look tenia `Ubicacion`/`Tags`, y el negative
estaba etiquetado de una forma que el parser no reconoce -> la app habria
mandado a Gemini 98 prompts sin cara, sin cuerpo, sin ropa, sin setting y sin
negative. Revisar a ojo no lo detecto. Este linter si.

VERIFICA (por personaje registrado en anclas_universales.json)
--------------------------------------------------------------
  1. Placeholders sin expandir en cualquier prompt          -> CRITICO
  2. Nº de prompts por look distinto de N                   -> CRITICO
  3. Look sin `**Negative Prompt:**` legible por la app     -> CRITICO
  4. Prompt sin las anclas que su slot exige                -> AVISO
  5. Metalenguaje multi-toma (causa registrada de collage)  -> CRITICO
  6. Look sin `- **Ubicacion:**` / `- **Tags:**`            -> AVISO
  7. Poses duplicadas (dos slots resolviendo al mismo)      -> CRITICO
  8. Prompt sospechosamente corto                           -> AVISO
  9. Calzon nombrado sin corte tanga/g-string (Ele/MD)      -> AVISO
 10. Ancla opt-in que el propio prompt dispara y no lleva   -> AVISO
 11. Prefijo cinematografico que no corresponde al          -> CRITICO
     Arquetipo declarado (solo personajes con tabla de
     prefijos_arquetipo en anclas_universales.json)
 12. Rotacion de ARQUITECTURA DE PRENDA: repeticion dentro   -> AVISO / CRITICO
     de la ventana global + cuota de silueta cubierta
     (solo personajes con rotacion_prenda)

CHEQUEO 12 — POR QUE EXISTE
----------------------------
El 18/08/2026 la Ama pregunto sobre el batch L21-L25 de Miss Doll: "¿por que
salieron puros bikini y bodysuit?". Medido sobre sus 25 looks: desde el L15 al
L25 van ONCE looks seguidos sin un solo vestido, falda ni pantalon — 72% de la
flota es arquitectura de piel y el 28% cubierto vive entero en L01-L14.

La causa NO fue el motor: el log (99_Sistema/logs/outfit_engine.jsonl) da 50
builds con 0 fallas y el deficit de arquetipos estaba en meta en los 8. La
causa fue de diseno: §6 del perfil gobierna el ESCENARIO y nadie gobernaba la
PRENDA, y la ventana anti-repeticion de §7 estaba alcanzada POR ARQUETIPO — con
8 arquetipos rotando, dos looks vecinos casi nunca comparten arquetipo, asi que
la ventana no se disparo ni una vez en 25 looks. Una regla que no se puede
disparar es una regla que no existe.

Se clasifica SOLO el BLOQUE B, jamas el prompt ensamblado: BOTTOM_CUT_LOCK
nombra "bikini bottom" y "bodysuit, teddy, leotard or swimsuit", y
DRESS_LEG_CLOSURE nombra "dress, skirt or robe". Clasificar sobre el prompt
completo seria el clasificador leyendose a si mismo.

CHEQUEO 11 — POR QUE EXISTE
----------------------------
El 16/08/2026 el batch L15-L20 de Anais salio con el prefijo de Ejecutivo
("power portrait") copiado a los 6 looks nuevos sin variar por arquetipo:
Boudoir/Lenceria perdio su "warm amber candlelight chiaroscuro" y salio con
luz plana. La tabla arquetipo->prefijo YA EXISTIA en dna_v2_3.md — nadie la
releyo al copiar un bloque de codigo de otro look. Un dato correcto en un
documento que nadie vuelve a abrir no protege nada. Este chequeo lee la
MISMA tabla desde anclas_universales.json (personajes.<slug>.prefijos_arquetipo)
y audita cada look real de la galeria contra su propio campo Arquetipo: si no
coinciden, el commit no debería pasar. Blindaje pedido por la Ama 17/08/2026:
"siempre pasa que se actualiza algo y cuesta que esa actualizacion se integre".

USO
---
    python 99_Sistema/scripts/visual/lint_prompts_personaje.py            # todos
    python 99_Sistema/scripts/visual/lint_prompts_personaje.py miss_doll  # uno
    python 99_Sistema/scripts/visual/lint_prompts_personaje.py --verbose

Salida != 0 si hay CRITICOS. Ningun batch se commitea con el linter en rojo.
"""

import io
import os
import re
import sys
import unicodedata

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", ".."))
sys.path.insert(0, AQUI)
from prompt_builder import PromptBuilder, cargar_config, PLACEHOLDERS_PROHIBIDOS  # noqa: E402

METALENGUAJE = ["in every shot", "identical across all", "in all poses",
                "in each pose", "across all poses", "contact sheet of"]

# --- puerto del parser de la app -------------------------------------------

LOOK_HEADING = re.compile(
    r"(?i).*?\b(?:Look|Boudoir)\s+(?:[A-Za-z]+)?(\d+)\b[:\s]*(.*?)(?:\((.*)\))?\s*$")
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")


def sin_tildes(s):
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn")


ARQUETIPO_LINEA = re.compile(r"\*\*Arquetipo:\*\*\s*([^·\n]+)")


def extraer_arquetipos(texto):
    """Mapa {numero_de_look: arquetipo_declarado}, leido de la linea
    `**Arquetipo:** X · **Paleta:** ...` que antecede al concepto de cada
    look. Independiente del parser de poses: es una pasada aparte porque
    `parse_como_la_app` deja de leer el bloque de canon antes de llegar a
    esta linea (corta en el primer `### `, que es la seccion de imagenes)."""
    arquetipos = {}
    num_actual = None
    for linea in texto.split("\n"):
        t = linea.strip()
        if t.startswith("#"):
            m = LOOK_HEADING.match(t)
            if m:
                num_actual = int(m.group(1))
            continue
        m = ARQUETIPO_LINEA.search(t)
        if m and num_actual is not None and num_actual not in arquetipos:
            arquetipos[num_actual] = m.group(1).strip()
    return arquetipos


# Las TRES galerias escriben el outfit en formas distintas, y hasta el 04/09/2026
# este chequeo solo sabia leer la primera. Medido ese dia: Ele 0 de 618 looks
# clasificados y Anais 5 de 70 — o sea la regla estaba cableada y no podia
# dispararse, que es el mismo modo de falla que la ventana por arquetipo del
# 18/08 ("una regla que no se puede disparar es una regla que no existe").
# Se prueban en orden y gana la primera que exista dentro del bloque del look.
BLOQUE_B_FORMAS = (
    # 1. Fence ```text  — Miss Doll completa + Anais L71-L75
    re.compile(r"\*\*BLOQUE B[^\n]*\n```text\n(.*?)\n```", re.S),
    # 2. Inline entre backticks — Anais L01-L70
    re.compile(r"\*\*BLOQUE B[^\n]*?:\*\*\s*`([^`]{40,})`"),
    # 3. Campo `- **Outfit...:**` en prosa — Ele. Es su formato declarado en la
    #    regla 11 y no se migra: se aprende a leerlo. El sufijo es libre porque
    #    Ele nombra el MISMO campo de tres formas segun la era del look:
    #    `Outfit:` (391), `Outfit canonico (7 campos):` (100) y
    #    `Outfit (BLOQUE B):` (27). Medido el 04/09/2026.
    re.compile(r"^- \*\*Outfit[^:*\n]*:\*\*\s*(.+)$", re.M),
)
BLOQUE_B = BLOQUE_B_FORMAS[0]  # se conserva el nombre por compatibilidad


def extraer_bloques_b(texto):
    """Mapa {numero_de_look: texto del BLOQUE B}.

    Pasada aparte, igual que `extraer_arquetipos`: el BLOQUE B es la unica
    fuente valida para clasificar la arquitectura de prenda. El prompt
    ensamblado NO sirve — sus propias anclas nombran bikini, bodysuit, dress y
    skirt (ver el chequeo 12 en el docstring)."""
    bloques = {}
    heads = list(re.finditer(r"^#+ .*?\b(?:Look|Boudoir)\s+(?:[A-Za-z]+)?(\d+)\b", texto, re.M))
    for i, h in enumerate(heads):
        fin = heads[i + 1].start() if i + 1 < len(heads) else len(texto)
        num = int(h.group(1))
        if num in bloques:
            continue
        for rx in BLOQUE_B_FORMAS:
            m = rx.search(texto, h.end(), fin)
            if m:
                bloques[num] = m.group(1).strip()
                break
    return bloques


def total_looks(texto):
    """Cuantos looks tiene la galeria, contados igual que extraer_bloques_b.

    Existe para que el resumen pueda decir 'lei N de M': hasta el 04/09/2026 el
    chequeo 12 imprimia solo N, asi que un 0 de 618 se leia igual que un 'no
    aplica' y paso meses sin que nadie lo notara."""
    return len(set(re.findall(r"^#+ .*?\b(?:Look|Boudoir)\s+(?:[A-Za-z]+)?(\d+)\b", texto, re.M)))


def clasificar_arquitectura(bloque_b, tax):
    """(codigo, cubierta_bool, aviso_o_None) para un BLOQUE B.

    Primero borra las AUSENCIAS declaradas (`no corset`, `no stockings`): sin
    eso un look que dice literal "no corset" se clasificaba como corseteria."""
    b = re.sub(tax["_regex_ausencias"], " ", bloque_b.lower())
    for regla in tax["orden"]:
        if not re.search(regla["regex"], b):
            continue
        cubierta = regla["cobertura"] == "cubierta"
        aviso = None
        req = regla.get("requiere_para_cubierta")
        if cubierta and req and not re.search(req, b):
            cubierta = False
            aviso = regla.get("si_falta", "")
        return regla["codigo"], cubierta, aviso
    return None, False, None


def detectar_pose(linea, slot5):
    """Mismo arbol de decision que el parser de la app (orden incluido)."""
    t = linea.lower()
    m = re.match(r"^(?:\*\*)?(?:PROMPT\s+)?(\d+)[.\s—]+(?:[A-Za-z0-9-]+\s+)?(.*?)(?:[:\*]+|$)", linea)
    if m:
        t = m.group(2).strip().lower()
        num = int(m.group(1))
    else:
        num = None
    orden = [
        (["standing", "cruel contrapposto", "cruel_contrapposto", "c-1", "c1"], "Standing"),
        (["back view", "back_view", "espalda", "c-3", "c3"], "Back View"),
        (["seated", "monarch throne", "monarch_throne", "c-2", "c2"], "Seated"),
        (["side profile", "profile", "tres cuartos", "three_quarter", "three-quarter", "c-4", "c4"], "Side Profile"),
        (["ditzy", "glacial command", "glacial_command", "sovereign gaze", "sovereign_gaze",
          "close up fria", "close_up_fria", "c-5", "c5"], slot5),
        (["pov", "close up", "intimate", "c-6", "c6"], "POV"),
        (["odalisque", "throne en suelo", "throne_suelo", "throne_en_suelo", "c-7", "c7"], "Odalisque"),
    ]
    for i, (claves, nombre) in enumerate(orden):
        for k in claves:
            if k in t:
                if i == 1 and k == "back view" or k != "back view":
                    pass
                return nombre
        if i == 1 and "back" in t and "background" not in t:
            return "Back View"
    if m and num is not None:
        return {1: "Standing", 2: "Back View", 3: "Seated", 4: "Side Profile",
                5: slot5, 6: "POV", 7: "Odalisque"}.get(num)
    return None


def parse_como_la_app(texto, slot5):
    """Devuelve [{num, titulo, ubicacion, tags, negative, prompts:{pose:txt}}]."""
    looks = []
    cur = None
    pose = None
    leyendo_codigo = False
    leyendo_canon = False
    buf = []
    canon = []

    def cerrar_prompt():
        nonlocal pose, buf
        txt = "\n".join(buf).strip()
        if txt and pose and cur is not None:
            cur["prompts"][pose] = cur["prompts"].get(pose, [])
            cur["prompts"][pose].append(txt)
            pose = None
        buf = []

    def cerrar_canon():
        if cur is None:
            return
        for l in canon:
            s = l.strip()
            if s.startswith("- **"):
                clave = sin_tildes(s.split(":**")[0][4:].strip()).lower()
                valor = s.split(":**", 1)[1].strip().strip("`").strip() if ":**" in s else ""
                if clave == "ubicacion":
                    cur["ubicacion"] = valor
                elif clave == "tags":
                    cur["tags"] = valor

    for linea in texto.split("\n"):
        t = linea.strip()
        m = LOOK_HEADING.match(t) if t.startswith("#") else None
        if m:
            if leyendo_codigo:
                leyendo_codigo = False
                cerrar_prompt()
            cerrar_canon()
            canon = []
            leyendo_canon = True
            cur = {"num": int(m.group(1)), "titulo": (m.group(2) or "").strip(),
                   "ubicacion": None, "tags": None, "negative": None, "prompts": {}}
            looks.append(cur)
            pose = None
            continue
        if cur is None:
            continue

        if leyendo_canon:
            if t.startswith("### "):
                leyendo_canon = False
            else:
                canon.append(linea)

        es_pose_header = t.startswith("**") and t.endswith(":**")
        es_negative = t.startswith("**Negative Prompt:**") or t.startswith("**Negative prompt:**")

        if leyendo_codigo and (es_pose_header or t.startswith("###") or es_negative):
            leyendo_codigo = False
            cerrar_prompt()

        if es_negative:
            mm = re.search(r"`([^`]+)`", t)
            if mm:
                cur["negative"] = mm.group(1).strip()
            continue

        if leyendo_codigo:
            if t.startswith("```"):
                leyendo_codigo = False
                cerrar_prompt()
            else:
                buf.append(linea)
            continue

        if not t.startswith("`") and (len(t) < 100 or "prompt" in t.lower()):
            p = detectar_pose(t, slot5)
            if p:
                pose = p
                inline = re.search(r"`(.*?)`", t)
                if inline and inline.group(1).strip():
                    cur["prompts"].setdefault(pose, []).append(inline.group(1).strip())
                    pose = None
                continue

        if t.startswith("```"):
            if pose:
                leyendo_codigo = True
            continue

    if leyendo_codigo:
        cerrar_prompt()
    cerrar_canon()
    return looks


# --- auditoria --------------------------------------------------------------

def auditar(slug, cfg, verbose=False):
    pb = PromptBuilder(slug, cfg)
    ruta = os.path.join(RAIZ, pb.perfil["galeria"].replace("/", os.sep))
    if not os.path.exists(ruta):
        return ["[CRITICO] %s: no existe la galeria %s" % (slug, pb.perfil["galeria"])], []
    texto = io.open(ruta, encoding="utf-8").read()
    slot5 = pb.perfil["slot5_nombre"]
    looks = parse_como_la_app(texto, slot5)
    arquetipos = extraer_arquetipos(texto)
    tabla_prefijos = pb.perfil.get("prefijos_arquetipo")
    n_poses = len(cfg["slots_universales"])
    slots_por_nombre = {
        "Standing": "standing", "Back View": "back_view", "Seated": "seated",
        "Side Profile": "side_profile", slot5: "slot5", "POV": "pov", "Odalisque": "odalisque",
    }

    deuda_cfg = pb.perfil.get("deuda_declarada", {}).get("metalenguaje_multi_toma", {})
    looks_deuda = set(deuda_cfg.get("looks", []))

    criticos, avisos, deuda = [], [], []
    total_prompts = 0
    for lk in looks:
        et = "%s Look %s (%s)" % (pb.perfil["nombre"], lk["num"], (lk["titulo"] or "")[:40])
        planos = {k: v for k, v in lk["prompts"].items()}
        # Solo cuentan los prompts REALES: una linea de metadata con backticks
        # (p.ej. `Ubicacion` de un look cuyo slug contiene "back") el parser la
        # confunde con prompt inline, pero el REPLACE la pisa con el verdadero.
        n = sum(len([p for p in v if len(p) > 600]) for v in planos.values())
        total_prompts += n
        if n != n_poses:
            criticos.append("[CRITICO] %s: la app ingiere %d prompts reales, deberian ser %d" % (et, n, n_poses))
        for pose, lista in planos.items():
            if len(lista) > 1:
                reales = [p for p in lista if len(p) > 600]
                if len(reales) > 1:
                    criticos.append("[CRITICO] %s: el slot '%s' recibe %d prompts REALES -> "
                                    "PrimaryKey REPLACE, solo sobrevive el ultimo"
                                    % (et, pose, len(reales)))
                else:
                    avisos.append("[AVISO]  %s: el slot '%s' se resuelve %d veces; %d de ellas son "
                                  "basura corta (una linea de metadata con backticks que el parser "
                                  "confunde con prompt inline). El REPLACE deja el prompt real "
                                  "porque va despues — pero es fragil"
                                  % (et, pose, len(lista), len(lista) - len(reales)))
        if not lk["negative"]:
            criticos.append("[CRITICO] %s: sin `**Negative Prompt:**` legible por la app "
                            "-> las %d poses se generarian SIN negativo" % (et, n_poses))
        if not lk["ubicacion"]:
            avisos.append("[AVISO]  %s: sin `- **Ubicacion:**` (la app no resuelve su carpeta)" % et)
        if not lk["tags"]:
            avisos.append("[AVISO]  %s: sin `- **Tags:**` (no filtrable en la app)" % et)

        # Chequeo 11: prefijo cinematografico vs Arquetipo declarado (blindaje 17/08/2026).
        if tabla_prefijos:
            arquetipo = arquetipos.get(lk["num"])
            if not arquetipo:
                avisos.append("[AVISO]  %s: sin linea `**Arquetipo:**` -> no se puede "
                              "verificar su prefijo cinematografico" % et)
            elif arquetipo not in tabla_prefijos:
                avisos.append("[AVISO]  %s: Arquetipo '%s' no esta en prefijos_arquetipo "
                              "de anclas_universales.json -> agregarlo antes del proximo "
                              "look de ese arquetipo" % (et, arquetipo))
            else:
                esperado = tabla_prefijos[arquetipo]["prefijo"]
                textos_reales = [p for lista in planos.values() for p in lista if len(p) > 600]
                if textos_reales and not any(esperado in p for p in textos_reales):
                    criticos.append("[CRITICO] %s: Arquetipo '%s' pide el prefijo '%s' "
                                    "pero ninguna de sus %d poses lo tiene -> revisar si se "
                                    "copio el bloque de otro look sin adaptar el prefijo"
                                    % (et, arquetipo, esperado, len(textos_reales)))

        for pose, lista in planos.items():
            for pr in lista:
                mm = PLACEHOLDERS_PROHIBIDOS.search(pr)
                if mm:
                    criticos.append("[CRITICO] %s / %s: placeholder sin expandir %s"
                                    % (et, pose, mm.group(0)))
                bajo = pr.lower()
                for tk in METALENGUAJE:
                    if tk in bajo:
                        if lk["num"] in looks_deuda:
                            deuda.append((lk["num"], pose, tk))
                        else:
                            criticos.append("[CRITICO] %s / %s: metalenguaje multi-toma '%s' "
                                            "(look FUERA de la deuda declarada = regresion)"
                                            % (et, pose, tk))
                if len(pr) < 600:
                    avisos.append("[AVISO]  %s / %s: prompt de %d chars (sospechoso: "
                                  "ADN+outfit+anclas no baja de ~1.500)" % (et, pose, len(pr)))
                # Calzon sin corte declarado (Ama 13/08/2026): la causa raiz del
                # calzon de talle alto del Look 801 no fue una ancla ausente sino
                # un BLOQUE B que nombra la prenda y no su corte.
                if "BOTTOM_CUT_LOCK" in pb.anclas_siempre and pb.calzon_sin_corte(pr):
                    avisos.append("[AVISO]  %s / %s: nombra calzon SIN declarar corte "
                                  "tanga/g-string (BOTTOM_CUT_LOCK)" % (et, pose))
                slot = slots_por_nombre.get(pose)
                if slot:
                    for nombre_ancla in pb.anclas_de_slot(slot):
                        frag = pb.anclas[nombre_ancla]["texto"][:45]
                        if frag not in pr:
                            avisos.append("[AVISO]  %s / %s: falta el ancla %s" % (et, pose, nombre_ancla))
                for nombre_ancla in pb.opt_in_de(pr):
                    frag = pb.anclas[nombre_ancla]["texto"][:45]
                    if frag not in pr:
                        avisos.append("[AVISO]  %s / %s: el look dispara %s (opt-in) y el ancla no esta"
                                      % (et, pose, nombre_ancla))

    # Chequeo 12: rotacion de arquitectura de prenda (Ama 18/08/2026).
    # Es un chequeo CRUZADO entre looks, no dentro de uno: por eso va aqui y no
    # en el bucle de arriba.
    rot = pb.perfil.get("rotacion_prenda")
    tax = cfg.get("arquitecturas_de_prenda")
    if rot and tax:
        bloques = extraer_bloques_b(texto)
        nums = sorted(bloques)
        clasif = {}
        for n in nums:
            cod, cubierta, aviso = clasificar_arquitectura(bloques[n], tax)
            clasif[n] = (cod, cubierta)
            if cod is None:
                avisos.append("[AVISO]  %s Look %s: no se pudo clasificar la arquitectura de "
                              "prenda de su BLOQUE B (§5.6) — revisar que nombre la prenda "
                              "principal" % (pb.perfil["nombre"], n))
            elif aviso:
                avisos.append("[AVISO]  %s Look %s: %s" % (pb.perfil["nombre"], n, aviso))

        desde = rot.get("desde_look", 0)
        vent = rot.get("ventana_global", 3)
        cada = rot.get("cuota_cubierta", {}).get("cada", 4)
        minimo = rot.get("cuota_cubierta", {}).get("minimo", 1)

        # Looks materializados cuya violacion es real pero inarreglable, declarados
        # uno por uno con motivo en anclas_universales.json. No suben desde_look
        # (eso taparia tambien lo que venga despues) ni quedan en rojo permanente.
        historicos = set(rot.get("historicos_declarados", []))

        def reportar(n, msg):
            if n in historicos:
                avisos.append("[AVISO]  %s Look %s: %s (HISTORICO DECLARADO: look ya "
                              "materializado, ver rotacion_prenda._historicos_porque)"
                              % (pb.perfil["nombre"], n, msg))
            elif n >= desde:
                criticos.append("[CRITICO] %s Look %s: %s" % (pb.perfil["nombre"], n, msg))
            else:
                avisos.append("[AVISO]  %s Look %s: %s (historico: la regla rige desde el "
                              "Look %s, no se retrofitea)" % (pb.perfil["nombre"], n, msg, desde))

        for i, n in enumerate(nums):
            cod = clasif[n][0]
            if cod is None:
                continue
            previos = [clasif[x][0] for x in nums[max(0, i - vent):i]]
            if cod in previos:
                reportar(n, "arquitectura de prenda %s repetida dentro de la ventana global "
                            "de %d looks (previos: %s)" % (cod, vent, ", ".join(p or "?" for p in previos)))
            if i + 1 >= cada:
                bloque = nums[i + 1 - cada:i + 1]
                cubiertos = sum(1 for x in bloque if clasif[x][1])
                if cubiertos < minimo:
                    reportar(n, "cuota de silueta cubierta incumplida: %d de los ultimos %d looks "
                                "(L%s) llevan M6-M10, se exige %d"
                                % (cubiertos, cada, "-L".join(str(x) for x in (bloque[0], bloque[-1])), minimo))

        n_cub = sum(1 for n in nums if clasif[n][1])
        n_total = total_looks(texto)
        cobertura = ("leidos %d/%d looks" % (len(nums), n_total)
                     + ("  ⚠ %d SIN LEER" % (n_total - len(nums)) if len(nums) < n_total else ""))
        resumen_prenda = ("  · PRENDA: %s · cubierta %d (%.0f%%) · %s"
                          % (cobertura, n_cub, (n_cub * 100.0 / len(nums)) if nums else 0,
                             " ".join("L%s=%s" % (n, clasif[n][0] or "??") for n in nums[-8:])))
    else:
        resumen_prenda = ""

    if verbose:
        extra = ""
        if deuda:
            d = pb.perfil["deuda_declarada"]["metalenguaje_multi_toma"]
            extra = ("  · DEUDA DECLARADA: %d poses con metalenguaje en %d looks fosilizados "
                     "(%d sin imagen -> riesgo vivo). Medido %s"
                     % (len(set((x[0], x[1]) for x in deuda)), len(set(x[0] for x in deuda)),
                        d.get("poses_afectadas_sin_imagen", "?"),
                        pb.perfil["deuda_declarada"].get("medida", "?")))
        print("  %-12s looks=%d prompts=%d%s" % (slug, len(looks), total_prompts, extra))
        if resumen_prenda:
            print(resumen_prenda)
    return criticos, avisos


def main():
    cfg = cargar_config()
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    verbose = "--verbose" in sys.argv or "-v" in sys.argv
    slugs = args or list(cfg["personajes"].keys())

    print("=" * 78)
    print("LINT DE PROMPTS — outfit-engine multi-personaje")
    print("Parseado con el MISMO algoritmo que LV-App: esto es lo que la app ingiere.")
    print("=" * 78)

    tot_c, tot_a = [], []
    for slug in slugs:
        c, a = auditar(slug, cfg, verbose=True)
        tot_c += c
        tot_a += a

    print("")
    for l in tot_c:
        print(l)
    if verbose or not tot_c:
        # --verbose imprime TODOS los avisos. Antes topaba en 60 y remataba con
        # "usar --verbose" incluso estando ya en verbose: el consejo era imposible
        # de seguir y escondia el resto (corregido 18/08/2026).
        tope = len(tot_a) if verbose else 60
        for l in tot_a[:tope]:
            print(l)
        if len(tot_a) > tope:
            print("  ... y %d avisos mas (usar --verbose)" % (len(tot_a) - tope))
    print("")
    print("-" * 78)
    print("CRITICOS: %d   AVISOS: %d" % (len(tot_c), len(tot_a)))
    if not tot_c:
        print("OK — todos los prompts llegan expandidos y con negative a la app.")
    print("-" * 78)
    return 1 if tot_c else 0


if __name__ == "__main__":
    sys.exit(main())
