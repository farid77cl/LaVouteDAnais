# -*- coding: utf-8 -*-
"""
Métricas Bluesky — lee el alcance/engagement de los posts publicados de Ele.

Para cada entrada de la cola con estado=publicado, consulta en vivo: likes,
reposts, respuestas y quotes. Más el perfil: seguidores / seguidos / posts.

🔎 Honestidad de plataforma: Bluesky NO expone "impresiones/visualizaciones"
   por su API pública. El "alcance" medible son los engagements (like/repost/
   reply/quote) + crecimiento de seguidores. No hay contador de "views".

Uso:
    python metricas_bluesky.py            # tabla de todos los publicados
    python metricas_bluesky.py --perfil   # solo el resumen de perfil
"""

import os
import sys
import json
import argparse

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", ".."))
ENV_PATH = os.path.join(REPO_ROOT, "06_RRSS", ".env")
COLA_JSON = os.path.join(REPO_ROOT, "06_RRSS", "cola", "cola_publicacion.json")


def load_env(path=ENV_PATH):
    if not os.path.exists(path):
        sys.exit(f"❌ No existe {path}.")
    env = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def connect(env):
    from atproto import Client
    handle = env.get("BLUESKY_HANDLE")
    pwd = env.get("BLUESKY_APP_PASSWORD")
    if not handle or not pwd or pwd.startswith("PEGA_AQUI"):
        sys.exit("❌ Faltan credenciales válidas en 06_RRSS/.env")
    client = Client()
    profile = client.login(handle, pwd)
    return client, profile


def perfil_resumen(profile):
    print("👤 PERFIL  @" + profile.handle)
    print(f"   Seguidores: {getattr(profile,'followers_count',0)}"
          f"  ·  Seguidos: {getattr(profile,'follows_count',0)}"
          f"  ·  Posts: {getattr(profile,'posts_count',0)}")


def main():
    ap = argparse.ArgumentParser(description="Métricas Bluesky — RRSS Ele")
    ap.add_argument("--perfil", action="store_true", help="solo resumen de perfil")
    args = ap.parse_args()

    env = load_env()
    client, profile = connect(env)
    perfil_resumen(profile)

    if args.perfil:
        return

    data = json.load(open(COLA_JSON, encoding="utf-8"))
    publicados = [e for e in data["cola"]
                  if e.get("estado") == "publicado" and e.get("uri")]
    if not publicados:
        print("\n(No hay posts publicados con URI en la cola todavía.)")
        return

    # Bluesky permite pedir hasta 25 posts por llamada.
    uris = [e["uri"] for e in publicados]
    res = client.get_posts(uris)
    by_uri = {p.uri: p for p in res.posts}

    print("\n📊 ENGAGEMENT POR POST")
    print(f"{'LOOK':<7} {'❤️ likes':>8} {'🔁 rep':>7} {'💬 resp':>8} {'❝ quote':>8}  url")
    print("-" * 78)
    tot = {"l": 0, "r": 0, "c": 0, "q": 0}
    for e in publicados:
        p = by_uri.get(e["uri"])
        if not p:
            print(f"{e['look_ref']:<7} (no encontrado)")
            continue
        lk = getattr(p, "like_count", 0) or 0
        rp = getattr(p, "repost_count", 0) or 0
        rc = getattr(p, "reply_count", 0) or 0
        qt = getattr(p, "quote_count", 0) or 0
        tot["l"] += lk; tot["r"] += rp; tot["c"] += rc; tot["q"] += qt
        print(f"{e['look_ref']:<7} {lk:>8} {rp:>7} {rc:>8} {qt:>8}  {e.get('url','')}")
    print("-" * 78)
    print(f"{'TOTAL':<7} {tot['l']:>8} {tot['r']:>7} {tot['c']:>8} {tot['q']:>8}")
    print("\nℹ️  Bluesky no expone impresiones/'views' por API — el alcance medible")
    print("   son estos engagements + el crecimiento de seguidores.")


if __name__ == "__main__":
    main()
