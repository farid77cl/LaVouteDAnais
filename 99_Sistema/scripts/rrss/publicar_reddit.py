# -*- coding: utf-8 -*-
"""
Conector Reddit — el motor de ALCANCE de Ele (PRAW).

Reddit es descubrimiento puro: posteas en un sub grande y te ven hoy, sin
seguidores. Por eso es el #1 para "que te vean".

Lee entradas reddit de la cola (06_RRSS/cola/cola_publicacion.json) + credenciales
del .env y publica un image post en el subreddit indicado.

🔐 Credenciales solo en 06_RRSS/.env (gitignored): REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET,
   REDDIT_USERNAME, REDDIT_PASSWORD.  (NUNCA en el repo ni el chat.)

FRENO DE MANO:
    --test                 login + karma (no publica)
    --preview <id>         muestra qué publicaría (no publica)
    --publicar <id> --confirmar   ← publica de verdad

⚠️ Reddit castiga el spam: NUNCA el mismo título/post idéntico en varios subs,
   respetar karma/edad mínima del sub, y cadencia humana. Cada sub = título propio.

Uso:
    python publicar_reddit.py --test
    python publicar_reddit.py --preview L401-reddit-01
    python publicar_reddit.py --publicar L401-reddit-01 --confirmar
"""

import os
import sys
import json
import argparse
from datetime import datetime, timezone

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", ".."))
ENV_PATH = os.path.join(REPO_ROOT, "06_RRSS", ".env")
COLA_JSON = os.path.join(REPO_ROOT, "06_RRSS", "cola", "cola_publicacion.json")

USER_AGENT = "windows:lavoute.ele.publisher:v0.1 (by /u/{user})"


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


def load_cola():
    return json.load(open(COLA_JSON, encoding="utf-8"))


def save_cola(data):
    with open(COLA_JSON, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def find_entry(data, post_id):
    for e in data.get("cola", []):
        if e.get("id") == post_id:
            return e
    return None


def connect(env):
    import praw
    req = ["REDDIT_CLIENT_ID", "REDDIT_CLIENT_SECRET", "REDDIT_USERNAME", "REDDIT_PASSWORD"]
    faltan = [k for k in req if not env.get(k) or env[k].startswith("PEGA_")]
    if faltan:
        sys.exit("❌ Faltan en 06_RRSS/.env: " + ", ".join(faltan))
    reddit = praw.Reddit(
        client_id=env["REDDIT_CLIENT_ID"],
        client_secret=env["REDDIT_CLIENT_SECRET"],
        username=env["REDDIT_USERNAME"],
        password=env["REDDIT_PASSWORD"],
        user_agent=USER_AGENT.format(user=env["REDDIT_USERNAME"]),
    )
    reddit.validate_on_submit = True
    return reddit


def cmd_test(env):
    print("🔐 Probando login en Reddit…")
    reddit = connect(env)
    me = reddit.user.me()
    print("✅ Login OK")
    print(f"   Usuario:   u/{me.name}")
    print(f"   Karma:     post {me.link_karma} · comentario {me.comment_karma}")
    print(f"   Creada:    {datetime.fromtimestamp(me.created_utc).date()}")
    print("\n(No se publicó nada — solo verificación.)")


def read_selftext(entry):
    """Texto del self-post: inline (entry['selftext']) o desde archivo (entry['selftext_file'])."""
    if entry.get("selftext_file"):
        p = os.path.join(REPO_ROOT, entry["selftext_file"])
        if not os.path.exists(p):
            sys.exit(f"❌ selftext_file no encontrado: {p}")
        return open(p, encoding="utf-8").read()
    return entry.get("selftext", "")


def render_preview(entry):
    d = entry.get("destino") or {}
    tipo = entry.get("tipo", "image")
    print(f"\n📮 Vista previa — {entry['id']}  ·  tipo: {tipo}")
    print(f"   subreddit: r/{d.get('subreddit','?')}  ·  flair: {d.get('flair','-')}")
    print(f"   gate: {entry.get('gate')}  ·  estado: {entry.get('estado')}  ·  nsfw: {entry.get('nsfw')}")
    print(f"   título: {entry.get('titulo','')}")
    if tipo == "text":
        body = read_selftext(entry)
        print(f"   ── selftext ({len(body)} chars, límite Reddit ~40000) ──")
        preview = body if len(body) <= 1200 else body[:1200] + "\n   […recortado para preview…]"
        for line in preview.splitlines():
            print(f"   | {line}")
    else:
        print(f"   look: {entry.get('look_ref')}")
        print(f"   imagen: {entry['imagenes'][0]}")
        if entry.get("caption"):
            print("   ── caption (comentario opcional) ──")
            for line in entry["caption"].splitlines():
                print(f"   | {line}")


def cmd_publicar(env, post_id, confirmar):
    data = load_cola()
    entry = find_entry(data, post_id)
    if not entry:
        sys.exit(f"❌ No existe '{post_id}' en la cola.")
    if entry["plataforma"] != "reddit":
        sys.exit(f"❌ '{post_id}' es {entry['plataforma']}, no reddit.")
    if entry.get("estado") == "publicado":
        sys.exit(f"⚠️  '{post_id}' ya está publicado: {entry.get('url')}")

    d = entry.get("destino") or {}
    tipo = entry.get("tipo", "image")
    sub = d.get("subreddit", "")
    if not sub or sub.startswith("EDITAR") or sub.startswith("EJEMPLO") or sub.startswith("VETAR"):
        sys.exit(f"❌ El subreddit '{sub}' es un placeholder. Edita 'destino.subreddit' en la cola con un sub real YA VETADO.")
    if not entry.get("titulo"):
        sys.exit("❌ Falta 'titulo' (Reddit lo exige).")

    # Validaciones por tipo
    if tipo == "text":
        body = read_selftext(entry)
        if not body.strip():
            sys.exit("❌ tipo=text pero el selftext/selftext_file está vacío.")
        if len(body) > 40000:
            sys.exit(f"❌ selftext {len(body)} chars > 40000 (límite Reddit). Divide el relato en partes.")
    else:
        img = os.path.join(REPO_ROOT, entry["imagenes"][0])
        if not os.path.exists(img):
            sys.exit(f"❌ Imagen no encontrada: {img}")

    render_preview(entry)
    if not confirmar:
        print("\n🛑 FRENO DE MANO: no se publicó. Agrega --confirmar para enviar.")
        return

    print("\n🔐 Login…")
    reddit = connect(env)
    print(f"✅ Conectada como u/{reddit.user.me().name}")
    print(f"⬆️  Publicando en r/{sub} (tipo={tipo})…")
    subreddit = reddit.subreddit(sub)

    if tipo == "text":
        kwargs = {"title": entry["titulo"], "selftext": body, "nsfw": bool(entry.get("nsfw"))}
        if entry.get("spoiler"):
            kwargs["spoiler"] = True
        if d.get("flair_id"):
            kwargs["flair_id"] = d["flair_id"]
        submission = subreddit.submit(**kwargs)
    else:
        kwargs = {"title": entry["titulo"], "image_path": img, "nsfw": bool(entry.get("nsfw"))}
        if d.get("flair_id"):
            kwargs["flair_id"] = d["flair_id"]
        submission = subreddit.submit_image(**kwargs)

    url = f"https://www.reddit.com{submission.permalink}"
    print(f"\n✅ ¡PUBLICADO! → {url}")

    # Comentario opcional con el caption (OC + disclosure IA) — solo en image posts.
    if tipo != "text" and entry.get("caption"):
        try:
            submission.reply(entry["caption"])
            print("💬 Caption agregado como comentario.")
        except Exception as e:
            print(f"   (no se pudo comentar: {e})")

    entry["estado"] = "publicado"
    entry["publicado_en"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    entry["url"] = url
    entry["reddit_id"] = submission.id
    save_cola(data)
    print("📝 Cola actualizada (estado=publicado).")


def main():
    ap = argparse.ArgumentParser(description="Conector Reddit — RRSS Ele")
    ap.add_argument("--test", action="store_true")
    ap.add_argument("--preview", metavar="ID")
    ap.add_argument("--publicar", metavar="ID")
    ap.add_argument("--confirmar", action="store_true")
    args = ap.parse_args()

    env = load_env()
    if args.test:
        cmd_test(env)
    elif args.preview:
        data = load_cola()
        e = find_entry(data, args.preview)
        if not e:
            sys.exit(f"❌ No existe '{args.preview}'.")
        render_preview(e)
        print("\n(Solo vista previa.)")
    elif args.publicar:
        cmd_publicar(env, args.publicar, args.confirmar)
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
