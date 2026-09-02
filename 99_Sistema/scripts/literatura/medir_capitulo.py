#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
medir_capitulo.py — Medidor mecánico de un capítulo · motor de escritura La Voûte (02/09/2026)

Nace de la orden de la Ama del 02/09/2026: "debo leer 5, 6 veces el mismo relato y eso al final mata
mi propia temperatura... lo que más me preocupa es que no logras dar con la temperatura y te pones muy
robótica con tus descripciones." Mide, sin cortesía, lo que ella corrige en cada relato. Los casos que
lo calibran viven en 01_Canon/evals_ama/casos_ama.md (dueño único de los patrones; este script solo mide).

  M1  Repetición interna         — frases/n-gramas repetidos dentro del capítulo            (caso C3)
  M2  Repetición contra previos  — clones verbatim y párrafos casi iguales vs caps previos  (caso C3, --contra)
  M3  Léxico explícito           — verga/coño/culo… por 1000 palabras · eufemismos · España (caso C2)
  M4  Tramos fríos               — corridas de frases sin cuerpo ni sexo                    (caso C1: "descriptiva y no calientas a nadie")
  M5  Trámite                    — vocabulario clínico/doméstico dentro de los tramos fríos (caso C1: arvejas, tele, enfermera)
  M6  Etiquetas de tema (H4)     — degradación/sumisión/humillación… en voz de narrador     (caso C15)
  M7  Tics de IA greppables      — H1 tricolón · H2 «no era X, era Y» · H3 remate · H5 «algo» · H6 dobletes · clichés
  M8  Varianza de frase (H8)     — por cada 500 palabras: ≥1 frase ≤5 y ≥1 ≥35
  M9  Apertura y cierre          — densidad erótica de las primeras y últimas 500 palabras   (T8 / T9b)
  M10 Distribución por decil     — dónde corre frío el capítulo                             (T9a)

Uso:
  python 99_Sistema/scripts/literatura/medir_capitulo.py <capitulo.md>
        [--contra cap_previo.md ...] [--out reportes/capitulo_N/medicion_v0.X.md] [--json] [--frio N]

Código de salida: 1 si falla un umbral DURO (M2 clon verbatim · M4 corrida fría ≥ --frio · M6 etiqueta
fuera de diálogo · M3 léxico de España), 0 si no. Los avisos blandos (tics, varianza) no cambian el código.

La salida es EFÍMERA o de TRABAJO: va a stdout o, con --out, a reportes/capitulo_N/medicion_v0.X.md.
Nunca a la raíz del relato. No lee ningún otro archivo del repo. No edita nada.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

# ────────────────────────────────────────────────────────────────────────────
# Léxicos (español de Chile). Regex con \b; los que terminan en \w* son raíces.
# ────────────────────────────────────────────────────────────────────────────

STOP = set(
    """a al ante bajo cabe con contra de del desde durante en entre hacia hasta mediante para por según sin
    sobre tras y e ni o u pero sino aunque que qué como cómo cuando cuándo donde dónde si el la los las un una
    unos unas lo le les se me te nos os mi mis tu tus su sus este esta estos estas ese esa esos esas aquel
    aquella aquello esto eso yo tú él ella ellos ellas usted es era fue son eran fueron ser estar está estaba
    estuvo están había hay ha han he hemos habían sido tan también tampoco todo toda todos todas otro otra
    otros otras mismo misma cada vez veces ahí allí aquí ahora después antes luego entonces mientras porque
    pues así solo sólo casi nada nadie algo alguien más muy no sí ya bien mal donde le lo al del les""".split()
)

EXPLICITO = [
    r"vergas?", r"coños?", r"culos?", r"tetas?", r"pezón", r"pezones", r"clítoris", r"chup\w*",
    r"mam(?:ad\w*|ar|ando|ándo\w*|ámela|ásela)", r"cog(?:er|ió|iendo|ida|idas|ía|ían|e|en|erla|erlo|iéndo\w*)",
    r"semen", r"corrid[ao]s?", r"corr(?:erse|iéndose|ámonos)", r"se corr(?:ió|ía|e|en|ían|ieron)",
    r"lam(?:er|ió|iendo|ía|e|erla|erlo|iéndo\w*)", r"mojad[ao]s?", r"empapad[ao]s?", r"penetr\w*",
    r"orgasmos?", r"gemid[ao]s?", r"gem(?:ir|ía|ían|ió)", r"jade\w*", r"eyacul\w*", r"esperma",
    r"vulva", r"nalgas", r"glúteos", r"pubis", r"tangas?", r"calz[oó]n(?:es)?", r"erecci[oó]n", r"erect[ao]",
    r"chorre\w*", r"put(?:a|ita|as|itas)", r"perr(?:a|ita)", r"zorra", r"maraca", r"sexo",
    r"la tenía dura", r"se le (?:puso|ponía|había puesto) dur[ao]", r"lubric\w*", r"clítoris",
]

CUERPO_EXTRA = [
    r"piel", r"boca", r"lengua", r"saliva", r"labios?", r"cuello", r"nuca", r"muslos?", r"caderas?", r"cintura",
    r"espalda", r"pechos?", r"escote", r"vientre", r"ombligo", r"entrepierna", r"ingle", r"pelvis", r"garganta",
    r"tembl\w*", r"temblor", r"húmed\w*", r"humedad", r"ard(?:er|ía|ían|iendo|or)", r"lat(?:ía|ían|ido|idos|iendo)",
    r"pulso", r"roz(?:ar|ó|aba|ando|e|arle|arla)", r"roce", r"ol(?:er|ía|ían|ió|iendo|erla|erlo)", r"olor",
    r"perfume", r"aliento", r"sabor", r"calor", r"calient\w*", r"calent\w*", r"hinch\w*", r"contracci[oó]n",
    r"contra(?:er|jo|ía)", r"estremec\w*", r"escalofrío", r"cosquill\w*", r"palpit\w*", r"deseo", r"dese(?:ar|aba|ó|ando|a|arlo|arla)",
    r"excit\w*", r"mord(?:er|ió|ía|iendo|isco|iéndose|erle|erse)", r"bes(?:o|os|ó|ar|aba|ando|arla|arlo)",
    r"se toc(?:ó|aba|a|ando)", r"tocarse", r"acarici\w*", r"caricias?", r"frot\w*", r"apret(?:ó|aba|ar|ando|ada|ado|arle)",
    r"liguero", r"tacones?", r"taco", r"stilettos?", r"pleaser", r"medias", r"corsé", r"sost[eé]n", r"bikini",
    r"lencería", r"encaje", r"desnud\w*", r"suspir\w*", r"respiraci[oó]n", r"jadeante", r"sudor", r"sud(?:ar|aba|ó|ando)",
    r"tibi[ao]", r"uñas", r"gloss", r"brillo en los labios", r"mirada", r"mir(?:ó|aba|ándola|ándolo)(?:\s+las?\s+(?:tetas|culo|escote))",
]

# Vocabulario de TRÁMITE: clínica · recuperación · traslado · quehacer doméstico · burocracia.
# Deliberadamente estrecho — «informe», «cocina», «desayuno» aparecen en escenas legítimas y se sacaron
# tras la calibración del 02/09 (Cap 3 aprobado de Café con Piernas disparaba falso con «informe»).
TRAMITE = [
    r"enfermer[ao]s?", r"anestesi\w*", r"cirujan[ao]s?", r"clínicas?", r"hospital", r"quirófano", r"recetas?",
    r"pastillas?", r"antibiótic\w*", r"analgésic\w*", r"vendas?", r"vendaje", r"faja", r"hielo", r"arvejas",
    r"control m[eé]dico", r"formulario", r"boleta", r"factura", r"recibo", r"transferencia",
    r"taxi", r"uber", r"televis\w*", r"tele", r"control remoto", r"noticiero",
    r"lavadora", r"planch\w*", r"supermercado", r"llamada a (?:la|su) mamá", r"trámite", r"papeleo", r"notaría",
    r"reposo", r"post[- ]?operatorio", r"cicatri\w*", r"drenaje", r"gasa", r"aseo", r"ordenar la pieza",
]

EUFEMISMOS = [
    r"su sexo", r"su intimidad", r"\bla humedad\b(?![^.]{0,40}entrepierna)", r"\baquello\b", r"ahí abajo",
    r"sus partes", r"su miembro", r"su virilidad", r"su hombría", r"su masculinidad", r"su feminidad",
    r"su centro", r"su núcleo", r"su flor", r"su cueva", r"calor (?:difuso|repartido|sin centro|sin punto fijo)",
    r"una válvula", r"algo se encendió", r"se encendió por dentro", r"un calor (?:la|lo) recorri[oó]",
    r"una oleada de (?:calor|placer)", r"su parte más íntima", r"ya había opinado", r"la parte de adelante del pantalón",
]

ESPANA = [r"\bpolla\b", r"\bfoll\w*", r"\bjoder\b", r"\btío\b", r"\bmóvil\b", r"\bcoche\b", r"\bgilipollas\b",
          r"\bhostia\b", r"\bmola\b", r"\bvosotros\b", r"\bos\b(?=\s+(?:voy|va|dije|dijo|gusta))", r"\bpiso\b(?=\s+de\s)"]

ETIQUETAS = [r"degrad\w*", r"hipersexual\w*", r"sumisi[oó]n", r"dominaci[oó]n", r"humillaci\w*", r"humillante",
             r"fetich\w*", r"condicionamiento", r"objetific\w*", r"cosificaci\w*", r"cosificad\w*", r"sexualizad\w*"]

CLICHES = [
    r"\bcrucial\b", r"\btapiz\b", r"intrincad\w*", r"\btestimonio\b", r"profundizar", r"dinamismo", r"una oleada de",
    r"un torbellino de", r"una mezcla de", r"no pudo evitar", r"sin poder evitarlo", r"en lo más profundo",
    r"lo más profundo de su ser", r"una parte de (?:ella|él)", r"como si el mundo", r"el tiempo se detuvo",
    r"innegable", r"inefable", r"indescriptible", r"palpable", r"vibrante", r"resonaba", r"abrumador\w*",
    r"visceral", r"descarga eléctrica", r"corriente eléctrica", r"electricidad", r"un escalofrío (?:le )?recorri[oó]",
]

# Tics H1-H6 (aprox. greppables — el conteo fino sigue siendo del Validador)
RE_H2 = [
    re.compile(r"[Nn]o (?:era|fue|es|había sido|parecía|se trataba de)\s[^.;:!?\n]{2,80}[.;:,—]\s*(?:[Ee]ra|[Ff]ue|[Ee]s)\b"),
    re.compile(r"[Nn]o (?:era|fue|es|se trataba de)\s[^.;:!?\n]{2,80},\s*sino\b"),
]
RE_H5 = re.compile(r"\balgo\b", re.IGNORECASE)
ADJ = r"\w{4,}(?:os[oa]s?|ad[oa]s?|id[oa]s?|entes?|antes?|al(?:es)?|ic[oa]s?|iv[oa]s?|ient[oa]s?|ud[oa]s?|eñ[oa]s?)"
RE_H6 = re.compile(rf"\b({ADJ})\s+y\s+({ADJ})\b")
RE_H1 = re.compile(r"(?<![,.;:—])\b[^,.;:!?\n—]{3,45},\s[^,.;:!?\n—]{3,45}\s(?:y|e|o|ni)\s[^,.;:!?\n—]{3,45}[.,;:!?]")
RE_SEP = re.compile(r"^\s*(?:\*\s*){3,}\s*$|^\s*-{3,}\s*$|^\s*\* \* \*\s*$")
RE_SENT = re.compile(r"(?<=[.!?…])\s+(?=[—«\"'¿¡A-ZÁÉÍÓÚÑ])")
RE_WORD = re.compile(r"[a-záéíóúüñ]+", re.IGNORECASE)


def rx(lst: list[str]) -> re.Pattern:
    return re.compile(r"\b(?:" + "|".join(lst) + r")\b", re.IGNORECASE)


RX_EXPLICITO = rx(EXPLICITO)
RX_CUERPO = rx(EXPLICITO + CUERPO_EXTRA)
RX_TRAMITE = rx(TRAMITE)
RX_EUF = re.compile("|".join(EUFEMISMOS), re.IGNORECASE)
RX_ESP = re.compile("|".join(ESPANA), re.IGNORECASE)
RX_ETIQ = rx(ETIQUETAS)
RX_CLICHE = re.compile("|".join(CLICHES), re.IGNORECASE)

# ────────────────────────────────────────────────────────────────────────────
# Carga y segmentación
# ────────────────────────────────────────────────────────────────────────────


def cargar(path: Path) -> str:
    t = path.read_text(encoding="utf-8-sig")
    lines = t.split("\n")
    if lines and lines[0].lstrip().startswith("#"):
        lines[0] = ""
    return "\n".join(lines)


def parrafos_con_linea(text: str) -> list[tuple[int, str]]:
    """[(línea_1based, párrafo)] — párrafos separados por línea en blanco; separadores de escena se conservan como '***'."""
    out, buf, start = [], [], None
    for i, ln in enumerate(text.split("\n"), 1):
        if RE_SEP.match(ln):
            if buf:
                out.append((start, " ".join(buf).strip()))
                buf, start = [], None
            out.append((i, "***"))
            continue
        if ln.strip():
            if start is None:
                start = i
            buf.append(ln.strip())
        elif buf:
            out.append((start, " ".join(buf).strip()))
            buf, start = [], None
    if buf:
        out.append((start, " ".join(buf).strip()))
    return out


def oraciones(par: str) -> list[str]:
    return [s.strip() for s in RE_SENT.split(par) if s.strip()]


def palabras(s: str) -> list[str]:
    return [w.lower() for w in RE_WORD.findall(s)]


def es_dialogo(s: str) -> bool:
    return s.lstrip().startswith(("—", "«", '"', "“"))


def excerpt(s: str, n: int = 170) -> str:
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= n else s[: n - 1] + "…"


# ────────────────────────────────────────────────────────────────────────────
# Medidas
# ────────────────────────────────────────────────────────────────────────────


def ngramas(tokens: list[str], n: int):
    for i in range(len(tokens) - n + 1):
        yield i, tuple(tokens[i : i + n])


def contenido(gram: tuple[str, ...]) -> int:
    return sum(1 for w in gram if w not in STOP and len(w) >= 4)


def _spans(tokens: list[str], n: int, es_rep) -> list[tuple[int, int]]:
    """Marca las posiciones cubiertas por n-gramas repetidos y las funde en tramos máximos [i, j)."""
    marks = [False] * len(tokens)
    for i in range(len(tokens) - n + 1):
        if es_rep(tuple(tokens[i : i + n])):
            for k in range(i, i + n):
                marks[k] = True
    spans, i = [], 0
    while i < len(tokens):
        if marks[i]:
            j = i
            while j < len(tokens) and marks[j]:
                j += 1
            spans.append((i, j))
            i = j
        else:
            i += 1
    return spans


def _veces(tokens: list[str], sub: list[str]) -> int:
    n, c = len(sub), 0
    for i in range(len(tokens) - n + 1):
        if tokens[i : i + n] == sub:
            c += 1
    return c


def m1_repeticion(sents: list[dict]) -> tuple[list[dict], list[dict], list[dict]]:
    tokens, owner = [], []
    for si, s in enumerate(sents):
        for w in s["words"]:
            tokens.append(w)
            owner.append(si)
    # tramos largos (≥6 palabras con ≥3 de contenido) repetidos verbatim, fundidos en su extensión máxima
    cnt6 = defaultdict(int)
    for _, g in ngramas(tokens, 6):
        if contenido(g) >= 3:
            cnt6[g] += 1
    spans = _spans(tokens, 6, lambda g: cnt6.get(g, 0) >= 2)
    unicos: dict[str, dict] = {}
    for i, j in spans:
        sub = tokens[i:j]
        txt = " ".join(sub)
        if txt in unicos:
            unicos[txt]["lineas"].append(sents[owner[i]]["linea"])
            continue
        unicos[txt] = {"n": j - i, "frase": txt, "lineas": [sents[owner[i]]["linea"]], "veces": _veces(tokens, sub)}
    largos = [d for d in unicos.values() if d["veces"] >= 2]
    for d in largos:
        d["duro"] = d["n"] >= 9
        d["lineas"] = sorted(set(d["lineas"]))[:6]
    largos.sort(key=lambda d: (-d["n"], -d["veces"]))
    # tics cortos: 4-5 palabras con ≥2 de contenido, ≥3 veces (o ≥2 si 5 palabras) — aviso, para cazar muletillas
    cortos = []
    vistos: set[str] = set()
    for n in (5, 4):
        pos = defaultdict(list)
        for i, g in ngramas(tokens, n):
            if contenido(g) >= 2:
                pos[g].append(i)
        for g, ps in pos.items():
            txt = " ".join(g)
            if len(ps) >= (2 if n == 5 else 3) and not any(txt in u for u in unicos) and txt not in vistos:
                vistos.add(txt)
                cortos.append({"n": n, "veces": len(ps), "frase": txt, "lineas": sorted({sents[owner[p]]["linea"] for p in ps})[:6]})
    cortos.sort(key=lambda d: (-d["veces"], -d["n"]))
    # oraciones enteras repetidas
    seen = defaultdict(list)
    for s in sents:
        if len(s["words"]) >= 5:
            seen[" ".join(s["words"])].append(s["linea"])
    frases = [{"frase": k, "veces": len(v), "lineas": v} for k, v in seen.items() if len(v) >= 2]
    return largos[:30], cortos[:15], frases


def m2_contra(sents: list[dict], pars: list[tuple[int, str]], previos: list[Path]) -> tuple[list[dict], list[dict]]:
    clones, similares = [], []
    cur_tokens = [w for s in sents for w in s["words"]]
    cur_owner = [s["linea"] for s in sents for _ in s["words"]]
    cur_pars = [(ln, set(w for w in palabras(p) if w not in STOP and len(w) >= 4), p)
                for ln, p in pars if p != "***"]
    for pv in previos:
        if pv.resolve() == ACTUAL.resolve():
            continue  # no compararse consigo mismo
        ptxt = cargar(pv)
        ptoks = [w for _, p in parrafos_con_linea(ptxt) if p != "***" for w in palabras(p)]
        pset = set()
        for _, g in ngramas(ptoks, 6):
            if contenido(g) >= 3:
                pset.add(g)
        vistos: set[str] = set()
        for i, j in _spans(cur_tokens, 6, lambda g: g in pset):
            txt = " ".join(cur_tokens[i:j])
            if txt in vistos:
                continue
            vistos.add(txt)
            clones.append({"contra": pv.name, "frase": txt, "linea": cur_owner[i], "n": j - i, "duro": (j - i) >= 8})
        # párrafos casi iguales (Jaccard de palabras de contenido)
        ppars = [(ln, set(w for w in palabras(p) if w not in STOP and len(w) >= 4), p)
                 for ln, p in parrafos_con_linea(ptxt) if p != "***"]
        for ln, cs, ctext in cur_pars:
            if len(cs) < 15:
                continue
            best = (0.0, None, None)
            for pln, ps, ptext in ppars:
                if len(ps) < 15:
                    continue
                j = len(cs & ps) / len(cs | ps)
                if j > best[0]:
                    best = (j, pln, ptext)
            if best[0] >= 0.30:
                similares.append({"contra": pv.name, "jaccard": round(best[0], 2), "linea": ln,
                                  "linea_previa": best[1], "actual": excerpt(ctext, 140), "previo": excerpt(best[2], 140)})
    clones.sort(key=lambda d: (not d["duro"], -len(d["frase"])))
    similares.sort(key=lambda d: -d["jaccard"])
    return clones[:40], similares[:20]


ACTUAL = Path(".")


def m3_lexico(text: str, nwords: int) -> dict:
    expl = RX_EXPLICITO.findall(text)
    euf = [(m.group(0), m.start()) for m in RX_EUF.finditer(text)]
    esp = [(m.group(0), m.start()) for m in RX_ESP.finditer(text)]
    cnt = defaultdict(int)
    for w in expl:
        cnt[w.lower()] += 1
    top = sorted(cnt.items(), key=lambda kv: -kv[1])[:12]
    return {
        "explicito_total": len(expl),
        "explicito_por_1000": round(len(expl) * 1000 / max(nwords, 1), 1),
        "top": top,
        "eufemismos": [{"texto": t, "ctx": excerpt(text[max(0, p - 60): p + 80], 140)} for t, p in euf],
        "espana": [{"texto": t, "ctx": excerpt(text[max(0, p - 60): p + 80], 140)} for t, p in esp],
    }


def m4_tramos_frios(sents: list[dict], umbral_palabras: int, duro_palabras: int) -> tuple[list[dict], float, float]:
    """Corridas de NARRACIÓN sin cuerpo ni sexo. Los diálogos no rompen la corrida ni suman a ella
    (una línea de diálogo puede calentar sin nombrar un solo cuerpo). Se mide en palabras de narración."""
    runs, cur = [], []

    def cerrar():
        if cur and sum(len(x["words"]) for x in cur if not x["dial"]) >= umbral_palabras:
            runs.append(list(cur))

    for s in sents:
        if s["dial"]:
            if cur:
                cur.append(s)
            continue
        if s["hot"]:
            cerrar()
            cur = []
        else:
            cur.append(s)
    cerrar()
    out = []
    for r in runs:
        narr = [x for x in r if not x["dial"]]
        texto = " ".join(x["text"] for x in narr)
        tram = sorted({m.group(0).lower() for m in RX_TRAMITE.finditer(texto)})
        npal = sum(len(x["words"]) for x in narr)
        out.append({
            "frases": len(narr), "palabras": npal, "linea": narr[0]["linea"], "escena": narr[0]["escena"],
            "tramite": tram, "duro": bool(tram) or npal >= duro_palabras,
            "inicio": excerpt(narr[0]["text"], 150), "fin": excerpt(narr[-1]["text"], 110),
        })
    out.sort(key=lambda d: (not d["duro"], -d["palabras"]))
    narr_all = [s for s in sents if not s["dial"]]
    share = sum(1 for s in narr_all if s["hot"]) / max(len(narr_all), 1)
    dial_share = sum(1 for s in sents if s["dial"]) / max(len(sents), 1)
    return out, round(share * 100, 1), round(dial_share * 100, 1)


def m6_etiquetas(sents: list[dict]) -> list[dict]:
    out = []
    for s in sents:
        if es_dialogo(s["text"]):
            continue
        for m in RX_ETIQ.finditer(s["text"]):
            out.append({"palabra": m.group(0), "linea": s["linea"], "ctx": excerpt(s["text"], 150)})
    return out


def m7_tics(sents: list[dict], text: str, n_escenas: int) -> dict:
    h2 = []
    for r in RE_H2:
        for m in r.finditer(text):
            h2.append(excerpt(m.group(0), 130))
    h5 = [excerpt(s["text"], 120) for s in sents if RE_H5.search(s["text"]) and not es_dialogo(s["text"])]
    h6 = [m.group(0) for m in RE_H6.finditer(text)]
    h1_por_escena = defaultdict(list)
    for s in sents:
        for m in RE_H1.finditer(s["text"]):
            h1_por_escena[s["escena"]].append(excerpt(m.group(0), 110))
    cliches = [{"texto": m.group(0), "ctx": excerpt(text[max(0, m.start() - 50): m.end() + 60], 130)}
               for m in RX_CLICHE.finditer(text)]
    return {"h2": h2, "h5": h5, "h6": h6, "h1_por_escena": dict(h1_por_escena), "cliches": cliches,
            "n_escenas": n_escenas}


def m7_remates(pars: list[tuple[int, str]]) -> list[dict]:
    out = []
    for ln, p in pars:
        if p == "***" or es_dialogo(p):
            continue
        ss = oraciones(p)
        if len(ss) >= 3 and len(palabras(ss[-1])) <= 4 and ss[-1].endswith("."):
            out.append({"linea": ln, "remate": ss[-1], "ctx": excerpt(ss[-2], 90)})
    return out


def m8_varianza(sents: list[dict]) -> list[dict]:
    fails, win, acc, start = [], [], 0, 1
    for s in sents:
        win.append(s)
        acc += len(s["words"])
        if acc >= 500:
            lens = [len(x["words"]) for x in win]
            ok_short, ok_long = any(l <= 5 for l in lens), any(l >= 35 for l in lens)
            if not (ok_short and ok_long):
                fails.append({"desde_linea": win[0]["linea"], "corta": ok_short, "larga": ok_long,
                              "min": min(lens), "max": max(lens)})
            win, acc = [], 0
    return fails


def m9_m10(sents: list[dict]) -> dict:
    total = sum(len(s["words"]) for s in sents)

    def share(sub):
        narr = [s for s in sub if not s["dial"]]
        if not narr:  # ventana puramente dialogada: no se penaliza
            return 100.0
        return round(100 * sum(1 for s in narr if s["hot"]) / len(narr), 1)

    # apertura / cierre por palabras
    acc, first = 0, []
    for s in sents:
        first.append(s); acc += len(s["words"])
        if acc >= 500:
            break
    acc, last = 0, []
    for s in reversed(sents):
        last.append(s); acc += len(s["words"])
        if acc >= 500:
            break
    # deciles
    deciles = [[] for _ in range(10)]
    acc = 0
    for s in sents:
        d = min(9, int(10 * acc / max(total, 1)))
        deciles[d].append(s)
        acc += len(s["words"])
    return {"apertura": share(first), "cierre": share(last), "deciles": [share(d) for d in deciles], "palabras": total}


# ────────────────────────────────────────────────────────────────────────────
# Reporte
# ────────────────────────────────────────────────────────────────────────────


def barra(p: float) -> str:
    n = int(round(p / 10))
    return "█" * n + "·" * (10 - n)


def medir(path: Path, previos: list[Path], umbral_frio: int, duro_frio: int) -> dict:
    global ACTUAL
    ACTUAL = path
    text = cargar(path)
    pars = parrafos_con_linea(text)
    sents, escena = [], 1
    for ln, p in pars:
        if p == "***":
            escena += 1
            continue
        for s in oraciones(p):
            ws = palabras(s)
            if not ws:
                continue
            sents.append({"text": s, "words": ws, "linea": ln, "escena": escena,
                          "hot": bool(RX_CUERPO.search(s)), "dial": es_dialogo(s)})
    nwords = sum(len(s["words"]) for s in sents)
    rep, tics_cortos, frases_rep = m1_repeticion(sents)
    clones, similares = m2_contra(sents, pars, previos) if previos else ([], [])
    lex = m3_lexico(text, nwords)
    frios, hot_share, dial_share = m4_tramos_frios(sents, umbral_frio, duro_frio)
    etiq = m6_etiquetas(sents)
    tics = m7_tics(sents, text, escena)
    remates = m7_remates(pars)
    var = m8_varianza(sents)
    dist = m9_m10(sents)

    duros = []
    clones_duros = [c for c in clones if c["duro"]]
    frios_duros = [f for f in frios if f["duro"]]
    rep_duros = [g for g in rep if g["duro"]]
    if clones_duros:
        duros.append(f"M2 · {len(clones_duros)} clon(es) verbatim de ≥8 palabras contra capítulos previos")
    if frios_duros:
        duros.append(f"M4 · {len(frios_duros)} tramo(s) frío(s) de narración con vocabulario de trámite o ≥{duro_frio} palabras sin cuerpo")
    if rep_duros or frases_rep:
        duros.append(f"M1 · {len(rep_duros)} frase(s) de ≥9 palabras repetida(s) verbatim dentro del capítulo + {len(frases_rep)} oración(es) entera(s)")
    if etiq:
        duros.append(f"M6 · {len(etiq)} etiqueta(s) de tema en voz de narrador (H4 exige 0)")
    if lex["espana"]:
        duros.append(f"M3 · {len(lex['espana'])} término(s) de España")
    blandos = []
    if len(tics["h2"]) > 1:
        blandos.append(f"H2 «no era X, era Y» ×{len(tics['h2'])} (cupo 1)")
    if len(remates) > 2:
        blandos.append(f"H3 remates ×{len(remates)} (cupo 2, greppable aprox.)")
    if len(tics["h5"]) > 4:
        blandos.append(f"H5 «algo» ×{len(tics['h5'])} (revisar cuáles son comodín; cupo 2)")
    if len(tics["h6"]) > 3:
        blandos.append(f"H6 dobletes ×{len(tics['h6'])} (cupo 3, aprox.)")
    tri = {k: len(v) for k, v in tics["h1_por_escena"].items() if len(v) > 1}
    if tri:
        blandos.append(f"H1 tricolones sobre cupo en {len(tri)} escena(s) (aprox.)")
    if var:
        blandos.append(f"H8 varianza falla en {len(var)} ventana(s) de 500 palabras")
    if lex["eufemismos"]:
        blandos.append(f"T3 eufemismos evasivos ×{len(lex['eufemismos'])}")
    rep_blandos = [g for g in rep if not g["duro"]]
    if rep_blandos:
        blandos.append(f"M1 tramos de 6-8 palabras repetidos verbatim: {len(rep_blandos)}")
    if tics_cortos:
        blandos.append(f"M1 tics cortos (4-5 palabras, ×3 o más): {len(tics_cortos)} — revisar muletillas")
    clones_blandos = [c for c in clones if not c["duro"]]
    if clones_blandos:
        blandos.append(f"M2 frases de 6-7 palabras compartidas con capítulos previos: {len(clones_blandos)} (rituales o tics)")
    if similares:
        blandos.append(f"M2 párrafos casi iguales a capítulos previos: {len(similares)} (J≥0.30)")
    frios_blandos = [f for f in frios if not f["duro"]]
    if frios_blandos:
        blandos.append(f"M4 tramos de narración ≥{umbral_frio} palabras sin cuerpo (no duros): {len(frios_blandos)}")
    if dist["apertura"] < 40:
        blandos.append(f"T8 apertura: solo {dist['apertura']}% de la narración con cuerpo en las primeras 500 palabras")
    if dist["cierre"] < 50:
        blandos.append(f"T9b cierre: solo {dist['cierre']}% de la narración con cuerpo en las últimas 500 palabras")
    frios_dec = [i + 1 for i, p in enumerate(dist["deciles"]) if p < 25]
    if frios_dec:
        blandos.append(f"T9a deciles con <25% de narración con cuerpo: {frios_dec}")

    return {
        "archivo": str(path), "palabras": nwords, "frases": len(sents), "escenas": escena,
        "contra": [str(p) for p in previos], "umbral_frio": umbral_frio, "duro_frio": duro_frio,
        "duros": duros, "blandos": blandos,
        "m1_ngramas": rep, "m1_tics": tics_cortos, "m1_frases": frases_rep, "m2_clones": clones, "m2_similares": similares,
        "m3": lex, "m4_frios": frios, "m4_share_caliente": hot_share, "m4_share_dialogo": dial_share,
        "m6": etiq, "m7": tics, "m7_remates": remates, "m8": var, "m9m10": dist,
    }


def render(r: dict) -> str:
    L = []
    veredicto = "🔴 FALLA UMBRAL DURO" if r["duros"] else ("🟡 AVISOS" if r["blandos"] else "🟢 LIMPIO (mecánico)")
    L.append(f"# Medición mecánica — `{Path(r['archivo']).name}`")
    L.append(f"medir_capitulo.py · {r['palabras']} palabras · {r['frases']} frases · {r['escenas']} escena(s)"
             + (f" · contra: {', '.join(Path(p).name for p in r['contra'])}" if r["contra"] else ""))
    L.append("")
    L.append(f"**Veredicto mecánico:** {veredicto}")
    L.append("")
    L.append("> Esto NO mide si calienta — mide lo que la Ama corrige y una máquina puede contar. "
             "Un 🟢 aquí es condición necesaria, nunca suficiente; el Validador y la Ama siguen mandando.")
    L.append("")
    if r["duros"]:
        L.append("## 🔴 Umbrales duros fallados")
        L += [f"- {d}" for d in r["duros"]]
        L.append("")
    if r["blandos"]:
        L.append("## 🟡 Avisos")
        L += [f"- {b}" for b in r["blandos"]]
        L.append("")

    # M4
    L.append(f"## M4 · Tramos fríos de narración — «te pones descriptiva y no calientas a nadie»")
    L.append(f"Narración con cuerpo/sexo: **{r['m4_share_caliente']}%** de las frases narrativas · diálogo: {r['m4_share_dialogo']}% de las frases "
             f"(el diálogo no cuenta como frío). Se lista toda corrida de narración ≥{r['umbral_frio']} palabras sin cuerpo; "
             f"🔴 = trae vocabulario de trámite o pasa de {r['duro_frio']} palabras.")
    if r["m4_frios"]:
        L.append("")
        L.append("| | Línea | Esc. | Frases | Palabras | Trámite | Empieza | Termina |")
        L.append("|---|---|---|---|---|---|---|---|")
        for f in r["m4_frios"]:
            L.append(f"| {'🔴' if f['duro'] else '🟡'} | {f['linea']} | {f['escena']} | {f['frases']} | {f['palabras']} | {', '.join(f['tramite']) or '—'} | {f['inicio']} | {f['fin']} |")
    else:
        L.append("Ninguno. ✅")
    L.append("")

    # M9/M10
    d = r["m9m10"]
    L.append("## M9/M10 · Apertura · cierre · distribución por decil (% de narración con cuerpo)")
    L.append(f"- **Apertura** (primeras 500 palabras): {d['apertura']}% · **Cierre** (últimas 500): {d['cierre']}%")
    L.append("- Deciles: " + " ".join(f"`{i+1}:{barra(p)} {p}%`" for i, p in enumerate(d["deciles"])))
    L.append("")

    # M3
    m3 = r["m3"]
    L.append("## M3 · Léxico explícito (T3)")
    L.append(f"- **{m3['explicito_por_1000']} por 1000 palabras** ({m3['explicito_total']} en total). Top: "
             + ", ".join(f"{w}×{c}" for w, c in m3["top"]))
    if m3["eufemismos"]:
        L.append(f"- Eufemismos evasivos ({len(m3['eufemismos'])}):")
        L += [f"  - *{e['texto']}* — …{e['ctx']}…" for e in m3["eufemismos"]]
    else:
        L.append("- Eufemismos evasivos: ninguno ✅")
    if m3["espana"]:
        L.append(f"- 🔴 Léxico de España ({len(m3['espana'])}):")
        L += [f"  - *{e['texto']}* — …{e['ctx']}…" for e in m3["espana"]]
    L.append("")

    # M1
    L.append("## M1 · Repetición interna")
    if r["m1_frases"]:
        L.append("**Frases enteras repetidas:**")
        L += [f"- ×{f['veces']} (líneas {f['lineas']}): «{f['frase']}»" for f in r["m1_frases"]]
    if r["m1_ngramas"]:
        L.append("**Tramos repetidos verbatim (extensión máxima; 🔴 = ≥9 palabras):**")
        L += [f"- {'🔴' if g['duro'] else '·'} ×{g['veces']} · {g['n']} palabras · líneas {g['lineas']}: «{g['frase']}»" for g in r["m1_ngramas"][:25]]
    if r["m1_tics"]:
        L.append("**Tics cortos (4-5 palabras que vuelven ×3 o más — muletillas del capítulo):**")
        L += [f"- ×{g['veces']} · líneas {g['lineas']}: «{g['frase']}»" for g in r["m1_tics"]]
    if not r["m1_frases"] and not r["m1_ngramas"] and not r["m1_tics"]:
        L.append("Ninguna. ✅")
    L.append("")

    # M2
    if r["contra"]:
        L.append("## M2 · Repetición contra capítulos previos")
        if r["m2_clones"]:
            L.append("**Clones verbatim (🔴 = ≥8 palabras; · = 6-7, pueden ser rituales o tics):**")
            L += [f"- {'🔴' if c['duro'] else '·'} línea {c['linea']} ← `{c['contra']}`: «{c['frase']}»" for c in r["m2_clones"]]
        if r["m2_similares"]:
            L.append("**Párrafos casi iguales (Jaccard ≥ 0.30 sobre palabras de contenido):**")
            for s in r["m2_similares"]:
                L.append(f"- J={s['jaccard']} · línea {s['linea']} vs `{s['contra']}`:{s['linea_previa']}")
                L.append(f"  - ahora: {s['actual']}")
                L.append(f"  - antes: {s['previo']}")
        if not r["m2_clones"] and not r["m2_similares"]:
            L.append("Nada. ✅")
        L.append("")

    # M6
    L.append("## M6 · Etiquetas de tema en voz de narrador (H4 = 0)")
    if r["m6"]:
        L += [f"- 🔴 *{e['palabra']}* (línea {e['linea']}): {e['ctx']}" for e in r["m6"]]
    else:
        L.append("Ninguna fuera de diálogo. ✅")
    L.append("")

    # M7
    t = r["m7"]
    L.append("## M7 · Tics de IA (greppables, aproximados — el Validador afina)")
    L.append(f"- **H2 «no era X, era Y»** ×{len(t['h2'])} (cupo 1)" + ("".join(f"\n  - {x}" for x in t["h2"][:8]) if t["h2"] else ""))
    L.append(f"- **H3 remates aforísticos** ×{len(r['m7_remates'])} (cupo 2)" + ("".join(f"\n  - línea {x['linea']}: …{x['ctx']} **{x['remate']}**" for x in r["m7_remates"][:8]) if r["m7_remates"] else ""))
    L.append(f"- **H5 «algo»** ×{len(t['h5'])} fuera de diálogo (cupo 2 como comodín)" + ("".join(f"\n  - {x}" for x in t["h5"][:8]) if t["h5"] else ""))
    L.append(f"- **H6 dobletes de adjetivo** ×{len(t['h6'])} (cupo 3): " + (", ".join(f"*{x}*" for x in t["h6"][:12]) if t["h6"] else "ninguno"))
    tri = {k: v for k, v in t["h1_por_escena"].items() if len(v) > 1}
    L.append(f"- **H1 tricolones por escena** (cupo 1/escena): " + (", ".join(f"esc.{k}×{len(v)}" for k, v in sorted(tri.items())) if tri else "en cupo"))
    for k, v in sorted(tri.items())[:6]:
        L += [f"  - esc.{k}: {x}" for x in v[:3]]
    L.append(f"- **Clichés de IA** ×{len(t['cliches'])}" + ("".join(f"\n  - *{c['texto']}* — …{c['ctx']}…" for c in t["cliches"][:10]) if t["cliches"] else ""))
    L.append("")

    # M8
    L.append("## M8 · Varianza de frase (H8: ≥1 frase ≤5 y ≥1 ≥35 por cada 500 palabras)")
    if r["m8"]:
        L += [f"- ventana desde línea {v['desde_linea']}: corta {'✅' if v['corta'] else '❌'} · larga {'✅' if v['larga'] else '❌'} (min {v['min']} / max {v['max']})" for v in r["m8"]]
    else:
        L.append("Cumple en todas las ventanas. ✅")
    L.append("")
    L.append("---")
    L.append("*Salida efímera de `99_Sistema/scripts/literatura/medir_capitulo.py`. Los patrones que mide viven en `01_Canon/evals_ama/casos_ama.md`.*")
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser(description="Medidor mecánico de un capítulo (La Voûte).")
    ap.add_argument("capitulo", type=Path)
    ap.add_argument("--contra", type=Path, nargs="*", default=[], help="capítulos previos para medir repetición")
    ap.add_argument("--out", type=Path, help="escribir el reporte markdown aquí (reportes/capitulo_N/medicion_v0.X.md)")
    ap.add_argument("--json", action="store_true", help="imprimir JSON en vez de markdown")
    ap.add_argument("--frio", type=int, default=120, help="palabras de narración seguidas sin cuerpo que se listan como tramo frío (default 120)")
    ap.add_argument("--duro", type=int, default=300, help="palabras de narración sin cuerpo a partir de las cuales el tramo es falla dura (default 300)")
    ap.add_argument("--extra", type=str, default="", help="palabras 'calientes' extra del relato, separadas por coma (ej. billete,luca,propina para Café con Piernas)")
    a = ap.parse_args()
    if not a.capitulo.exists():
        print(f"No existe: {a.capitulo}", file=sys.stderr)
        return 2
    if a.extra.strip():
        global RX_CUERPO
        extras = [re.escape(w.strip()) + r"\w*" for w in a.extra.split(",") if w.strip()]
        RX_CUERPO = rx(EXPLICITO + CUERPO_EXTRA + extras)
    r = medir(a.capitulo, a.contra, a.frio, a.duro)
    if a.json:
        print(json.dumps(r, ensure_ascii=False, indent=1))
    else:
        md = render(r)
        if a.out:
            a.out.parent.mkdir(parents=True, exist_ok=True)
            a.out.write_text(md + "\n", encoding="utf-8")
            print(f"Reporte → {a.out}")
            print(f"Veredicto: {'🔴 DURO' if r['duros'] else ('🟡' if r['blandos'] else '🟢')} · "
                  f"{r['palabras']} pal · frío {r['m4_share_caliente']}% caliente · {len(r['m4_frios'])} tramos fríos · "
                  f"{r['m3']['explicito_por_1000']} explícitas/1000")
        else:
            print(md)
    return 1 if r["duros"] else 0


if __name__ == "__main__":
    sys.exit(main())
