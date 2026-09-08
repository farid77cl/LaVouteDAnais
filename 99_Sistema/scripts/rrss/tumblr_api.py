#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tumblr_api.py — cliente firmado de Tumblr para @lavoutedeanais (08/09/2026)

Nace el día que la Ama consiguió sus cuatro llaves. Hasta hoy el repo tenía el adaptador de
posts y la cola, pero **nadie que hablara con Tumblr**: ni una línea de OAuth en todo el árbol.

Firma **OAuth 1.0a de tres patas a mano** (HMAC-SHA1). No usa `requests_oauthlib` ni `dotenv` a
propósito: esta máquina no los tiene y la firma son treinta líneas — una dependencia menos que
instalar en cada clon.

Uso:
    python 99_Sistema/scripts/rrss/tumblr_api.py verificar
        Prueba las cuatro llaves y dice QUIÉN es la dueña según Tumblr.

    python 99_Sistema/scripts/rrss/tumblr_api.py linea_base [--out <archivo.md>]
        Captura el piso del blog: seguidores, posts, likes. Con --out lo deja escrito.

⚠️ Las credenciales viven SOLO en `06_RRSS/.env`, que está en .gitignore. Este archivo no
   contiene ni imprime ninguna llave completa — nunca agregar un print que las muestre.
"""
from __future__ import annotations

import base64
import hashlib
import hmac
import json
import random
import sys
import time
import urllib.parse
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

RAIZ = Path(__file__).resolve().parents[3]
ENV = RAIZ / "06_RRSS" / ".env"
BLOG = "lavoutedeanais.tumblr.com"
API = "https://api.tumblr.com/v2"

LLAVES = ("TUMBLR_CONSUMER_KEY", "TUMBLR_CONSUMER_SECRET", "TUMBLR_TOKEN", "TUMBLR_TOKEN_SECRET")


# ── .env ──────────────────────────────────────────────────────────────────

def leer_env(path: Path = ENV) -> dict[str, str]:
    """Lee un .env plano. Sin dependencias: `KEY=valor`, ignora comentarios y vacíos."""
    if not path.exists():
        raise SystemExit(f"❌ No existe {path}. Las llaves van ahí (ver 06_RRSS/GUIA_LLAVES_TUMBLR.md).")
    datos = {}
    for linea in path.read_text(encoding="utf-8").splitlines():
        linea = linea.strip()
        if not linea or linea.startswith("#") or "=" not in linea:
            continue
        k, _, v = linea.partition("=")
        datos[k.strip()] = v.strip().strip('"').strip("'")
    return datos


def credenciales(path: Path = ENV) -> dict[str, str]:
    env = leer_env(path)
    faltan = [k for k in LLAVES if not env.get(k)]
    if faltan:
        raise SystemExit("❌ Faltan llaves en 06_RRSS/.env: " + ", ".join(faltan))
    return {k: env[k] for k in LLAVES}


# ── OAuth 1.0a ────────────────────────────────────────────────────────────

def _q(s: str) -> str:
    """Percent-encoding de OAuth: RFC 3986, sin dejar ningún carácter reservado sin escapar."""
    return urllib.parse.quote(str(s), safe="~")


def firmar(metodo: str, url: str, params: dict, cred: dict) -> str:
    """Devuelve el header Authorization firmado (HMAC-SHA1)."""
    oauth = {
        "oauth_consumer_key": cred["TUMBLR_CONSUMER_KEY"],
        "oauth_token": cred["TUMBLR_TOKEN"],
        "oauth_signature_method": "HMAC-SHA1",
        "oauth_timestamp": str(int(time.time())),
        "oauth_nonce": f"{random.getrandbits(64):x}{int(time.time())}",
        "oauth_version": "1.0",
    }
    # La firma se calcula sobre oauth_* + los parámetros de query, todos juntos y ordenados.
    todos = {**oauth, **{k: str(v) for k, v in params.items()}}
    normalizados = "&".join(f"{_q(k)}={_q(todos[k])}" for k in sorted(todos))
    base = f"{metodo.upper()}&{_q(url)}&{_q(normalizados)}"
    clave = f'{_q(cred["TUMBLR_CONSUMER_SECRET"])}&{_q(cred["TUMBLR_TOKEN_SECRET"])}'
    firma = base64.b64encode(
        hmac.new(clave.encode(), base.encode(), hashlib.sha1).digest()).decode()
    oauth["oauth_signature"] = firma
    return "OAuth " + ", ".join(f'{_q(k)}="{_q(v)}"' for k, v in sorted(oauth.items()))


def get(ruta: str, params: dict | None = None, cred: dict | None = None) -> dict:
    """GET firmado. `ruta` es relativa a /v2, por ejemplo 'user/info'."""
    import requests
    cred = cred or credenciales()
    params = params or {}
    url = f"{API}/{ruta.lstrip('/')}"
    cab = {"Authorization": firmar("GET", url, params, cred)}
    r = requests.get(url, headers=cab, params=params, timeout=30)
    try:
        cuerpo = r.json()
    except ValueError:
        raise SystemExit(f"❌ Tumblr no devolvió JSON ({r.status_code}): {r.text[:300]}")
    if r.status_code >= 400:
        msg = cuerpo.get("meta", {}).get("msg", "sin detalle")
        pista = ""
        if r.status_code == 401:
            pista = ("\n   401 = la firma no la aceptó. Lo más común: las cuatro llaves están"
                     "\n   cruzadas en el .env (las Consumer arriba, las Token abajo).")
        raise SystemExit(f"❌ HTTP {r.status_code} — {msg}{pista}")
    return cuerpo.get("response", cuerpo)


# ── comandos ──────────────────────────────────────────────────────────────

def cmd_verificar() -> int:
    cred = credenciales()
    print("🔑 Las cuatro llaves están en 06_RRSS/.env. Preguntándole a Tumblr quién es la dueña…\n")
    yo = get("user/info", cred=cred)
    usuario = yo.get("user", {})
    blogs = usuario.get("blogs", [])
    print(f"   ✅ Tumblr contestó. Usuaria: {usuario.get('name', '(sin nombre)')}")
    print(f"   📚 Blogs de esta cuenta: {len(blogs)}")
    propio = None
    for b in blogs:
        marca = "👑" if b.get("primary") else "  "
        admin = "dueña" if b.get("admin") else "no-dueña"
        print(f"      {marca} {b.get('name')} — {admin} · {b.get('followers', '?')} seguidores")
        if b.get("name") in (BLOG, BLOG.split(".")[0]):
            propio = b
    print()
    if not propio:
        print(f"   ⚠️ Ojo: entre los blogs de esta cuenta NO aparece «{BLOG}».")
        print("      Las llaves sirven, pero son de otra cuenta. Hay que rehacerlas con la dueña.")
        return 1
    if not propio.get("admin"):
        print(f"   ⚠️ «{BLOG}» aparece, pero esta cuenta no figura como dueña.")
        return 1
    print(f"   🎉 Verificado: esta cuenta es DUEÑA de «{BLOG}».")
    print("      O sea el conteo de seguidores sí se puede leer. Las cuatro llaves sirven.")
    return 0


def cmd_linea_base(destino: str | None) -> int:
    cred = credenciales()
    info = get(f"blog/{BLOG}/info", cred=cred).get("blog", {})
    campos = {
        "título": info.get("title"),
        "seguidores": info.get("followers"),
        "posts": info.get("posts"),
        "likes": info.get("likes"),
        "es NSFW/maduro": info.get("is_nsfw", info.get("is_adult")),
        "descripción": (info.get("description") or "").strip()[:120] or "(vacía)",
    }
    print(f"📊 Línea base de @{BLOG.split('.')[0]} — {time.strftime('%d/%m/%Y %H:%M')}\n")
    for k, v in campos.items():
        print(f"   {k:>16} : {v}")
    print("\n   ⚠️ Este piso NO es virgen: el Cap 1 de «Café con Piernas» ya estaba publicado")
    print("      cuando se capturó. Se rotula así y no como «antes de publicar nada».")
    if destino:
        p = Path(destino)
        p.parent.mkdir(parents=True, exist_ok=True)
        lineas = [f"# 📊 Línea base — @{BLOG.split('.')[0]}", "",
                  f"*Capturada el {time.strftime('%d/%m/%Y %H:%M')} con "
                  f"`tumblr_api.py linea_base`.*", "",
                  "> ⚠️ **Piso NO virgen.** El Cap 1 de «Café con Piernas» ya estaba publicado.",
                  "", "| Dato | Valor |", "|---|---|"]
        lineas += [f"| {k} | {v} |" for k, v in campos.items()]
        p.write_text("\n".join(lineas) + "\n", encoding="utf-8")
        print(f"\n   💾 Escrita en {p}")
    return 0


def main() -> int:
    args = sys.argv[1:]
    cmd = args[0] if args else "verificar"
    if cmd == "verificar":
        return cmd_verificar()
    if cmd == "linea_base":
        out = args[args.index("--out") + 1] if "--out" in args else None
        return cmd_linea_base(out)
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
