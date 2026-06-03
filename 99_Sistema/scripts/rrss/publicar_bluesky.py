# -*- coding: utf-8 -*-
"""
Conector Bluesky — el "cuerpo" que publica en @ele-de-anais.bsky.social.

Lee una entrada de la cola (06_RRSS/cola/cola_publicacion.json) + las credenciales
del .env local (06_RRSS/.env) y publica de verdad en Bluesky con la librería atproto.

🔐 NUNCA imprime ni commitea el App Password. El .env está en .gitignore.

FRENO DE MANO (nada sale al aire sin querer):
    --test                 solo login + perfil. NO publica. (verifica credenciales)
    --preview <id>         muestra EXACTAMENTE qué publicaría esa entrada. NO publica.
    --publicar <id>        exige además --confirmar para enviar de verdad.
    --publicar <id> --confirmar   ← esto SÍ publica.

Tras publicar con éxito: marca la entrada de la cola como estado=publicado + url + fecha.

Uso típico:
    python publicar_bluesky.py --test
    python publicar_bluesky.py --preview L414-bluesky-01
    python publicar_bluesky.py --publicar L414-bluesky-01 --confirmar
"""

import os
import io
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

BLUESKY_MAX_BLOB = 976560  # ~976 KB límite de blob de Bluesky
SAFE_BLOB = 950000          # margen de seguridad

# Valores válidos de self-label adulto en Bluesky.
LABELS_VALIDOS = {"porn", "sexual", "nudity", "graphic-media"}


# ------------------------------------------------------------------ .env / cola


def load_env(path=ENV_PATH):
    """Parser mínimo de .env (sin dependencias)."""
    if not os.path.exists(path):
        sys.exit(f"❌ No existe {path}. Copia 06_RRSS/.env.example a .env y rellénalo.")
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
    with open(COLA_JSON, encoding="utf-8") as f:
        return json.load(f)


def save_cola(data):
    with open(COLA_JSON, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def find_entry(data, post_id):
    for e in data.get("cola", []):
        if e.get("id") == post_id:
            return e
    return None


# ------------------------------------------------------------------ imagen


def prep_image(rel_path):
    """Devuelve (bytes, mime) de la imagen, recomprimida si excede el límite de Bluesky."""
    abs_path = os.path.join(REPO_ROOT, rel_path)
    if not os.path.exists(abs_path):
        sys.exit(f"❌ Imagen no encontrada: {abs_path}")
    with open(abs_path, "rb") as f:
        data = f.read()
    if len(data) <= SAFE_BLOB:
        return data, "image/png"

    # Recomprimir a JPEG bajando calidad hasta entrar en el límite.
    from PIL import Image
    img = Image.open(abs_path).convert("RGB")
    for q in (92, 88, 84, 80, 75, 70, 65, 60):
        buf = io.BytesIO()
        img.save(buf, format="JPEG", quality=q, optimize=True)
        if buf.tell() <= SAFE_BLOB:
            print(f"  ℹ️  imagen recomprimida a JPEG q{q} ({buf.tell()//1024} KB)")
            return buf.getvalue(), "image/jpeg"
    # Último recurso: reducir dimensiones.
    img.thumbnail((1200, 1200))
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=80, optimize=True)
    print(f"  ℹ️  imagen reescalada + JPEG ({buf.tell()//1024} KB)")
    return buf.getvalue(), "image/jpeg"


# ------------------------------------------------------------------ bluesky


def connect(env):
    from atproto import Client
    handle = env.get("BLUESKY_HANDLE")
    pwd = env.get("BLUESKY_APP_PASSWORD")
    if not handle or not pwd or pwd.startswith("PEGA_AQUI"):
        sys.exit("❌ Faltan BLUESKY_HANDLE / BLUESKY_APP_PASSWORD válidos en 06_RRSS/.env")
    client = Client()
    profile = client.login(handle, pwd)
    return client, profile


def cmd_test(env):
    print("🔐 Probando login en Bluesky…")
    client, profile = connect(env)
    print("✅ Login OK")
    print(f"   Handle:    @{profile.handle}")
    print(f"   Nombre:    {profile.display_name or '(sin display name)'}")
    print(f"   DID:       {profile.did}")
    fc = getattr(profile, "followers_count", None)
    pc = getattr(profile, "posts_count", None)
    if fc is not None:
        print(f"   Seguidores: {fc}  ·  Posts: {pc}")
    print("\n(No se publicó nada — solo verificación de credenciales.) 🫦")


def render_preview(entry):
    print(f"\n📮 Vista previa — {entry['id']}")
    print(f"   plataforma: {entry['plataforma']}  ·  look: {entry.get('look_ref')}")
    print(f"   gate: {entry.get('gate')}  ·  estado: {entry.get('estado')}")
    lbl = (entry.get("destino") or {}).get("self_label", "porn")
    print(f"   self_label (NSFW): {lbl}")
    print(f"   imagen: {entry['imagenes'][0]}")
    print("   ── caption ──")
    for line in entry["caption"].splitlines():
        print(f"   | {line}")
    if entry.get("hashtags"):
        print(f"   | {' '.join(entry['hashtags'])}")
    print("   ─────────────")


def build_text(entry):
    """Texto final = caption + hashtags (Bluesky los pone inline)."""
    text = entry["caption"]
    if entry.get("hashtags"):
        text = f"{text}\n\n{' '.join(entry['hashtags'])}"
    return text


def cmd_publicar(env, post_id, confirmar):
    data = load_cola()
    entry = find_entry(data, post_id)
    if not entry:
        sys.exit(f"❌ No existe la entrada '{post_id}' en la cola.")
    if entry["plataforma"] != "bluesky":
        sys.exit(f"❌ '{post_id}' es de plataforma {entry['plataforma']}, no bluesky.")
    if entry.get("estado") == "publicado":
        sys.exit(f"⚠️  '{post_id}' ya está publicado: {entry.get('url')}")

    render_preview(entry)

    if not confirmar:
        print("\n🛑 FRENO DE MANO: esto NO se publicó.")
        print("   Para publicar de verdad agrega --confirmar al comando.")
        return

    from atproto import models

    print("\n🔐 Login…")
    client, profile = connect(env)
    print(f"✅ Conectada como @{profile.handle}")

    # Imagen
    img_bytes, mime = prep_image(entry["imagenes"][0])
    print("⬆️  Subiendo imagen…")
    blob = client.upload_blob(img_bytes)

    alt = f"Ele — {entry.get('look_ref','')} · AI-generated fetish doll (fictional)"
    image = models.AppBskyEmbedImages.Image(alt=alt, image=blob.blob)
    embed = models.AppBskyEmbedImages.Main(images=[image])

    # Self-label NSFW
    lbl = (entry.get("destino") or {}).get("self_label", "porn")
    if lbl not in LABELS_VALIDOS:
        lbl = "porn"
    labels = models.ComAtprotoLabelDefs.SelfLabels(
        values=[models.ComAtprotoLabelDefs.SelfLabel(val=lbl)]
    )

    text = build_text(entry)
    print("📣 Publicando…")
    # send_post no acepta labels en esta versión → creamos el record completo,
    # que sí soporta self-labels (NSFW) + embed + langs.
    record = models.AppBskyFeedPost.Record(
        created_at=client.get_current_time_iso(),
        text=text,
        embed=embed,
        langs=["es"],
        labels=labels,
    )
    res = client.app.bsky.feed.post.create(profile.did, record)

    # URL legible del post
    rkey = res.uri.split("/")[-1]
    url = f"https://bsky.app/profile/{profile.handle}/post/{rkey}"
    print(f"\n✅ ¡PUBLICADO! → {url}")

    # Marcar en la cola
    entry["estado"] = "publicado"
    entry["publicado_en"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    entry["url"] = url
    entry["uri"] = res.uri
    save_cola(data)
    print("📝 Cola actualizada (estado=publicado).")


# ------------------------------------------------------------------ main


def main():
    ap = argparse.ArgumentParser(description="Conector Bluesky — RRSS Ele")
    ap.add_argument("--test", action="store_true", help="solo login + perfil (no publica)")
    ap.add_argument("--preview", metavar="ID", help="mostrar qué publicaría esa entrada")
    ap.add_argument("--publicar", metavar="ID", help="publicar esa entrada (exige --confirmar)")
    ap.add_argument("--confirmar", action="store_true", help="confirma el envío real")
    args = ap.parse_args()

    env = load_env()

    if args.test:
        cmd_test(env)
    elif args.preview:
        data = load_cola()
        entry = find_entry(data, args.preview)
        if not entry:
            sys.exit(f"❌ No existe '{args.preview}' en la cola.")
        render_preview(entry)
        print("\n(Solo vista previa — nada se publicó.)")
    elif args.publicar:
        cmd_publicar(env, args.publicar, args.confirmar)
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
