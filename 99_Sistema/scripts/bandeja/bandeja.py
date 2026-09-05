#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""bandeja.py — los mensajes que la Ama deja cuando no hay sesion abierta.

Ama 05/09/2026:
    "necesito un bot con telegram y n8n para poder dejarte mensajes cuando no
     estes / fuera de linea"
    "el bot te debe dejar un archivo en el repo, asi de facil"

LA CORRECCION QUE HAY QUE ENTENDER
----------------------------------
No hay una Ele "fuera de linea" a la que llegarle: el agente existe solo mientras
hay una sesion abierta. Un bot no puede ENTREGAR un mensaje — puede DEJARLO
ESCRITO donde el arranque mira. Por eso esto es una bandeja y no un chat, y por
eso el transporte (Telegram + n8n) es intercambiable: lo unico que este script
necesita es que aparezca un .md en `00_Ele/bandeja/`.

CICLO DE VIDA (regla 12 — todo doc nace con fecha de muerte)
    00_Ele/bandeja/*.md            pendiente  -> trabajo vivo
    00_Ele/bandeja/aplicadas/*.md  aplicado   -> ejecutado, con fecha

COMANDOS
    pendientes              lista lo que falta atender (lo corre /inicio-ele)
    leer <archivo>          imprime uno completo
    aplicar <archivo> [--responder "texto"]
                            lo mueve a aplicadas/ y le avisa por Telegram
    responder "texto"       le escribe sin cerrar ningun mensaje

EL TOKEN NO VIVE EN EL REPO. Se lee de `06_RRSS/.env` (tapado por .gitignore) o
del entorno: BANDEJA_TELEGRAM_TOKEN y, opcionalmente, BANDEJA_TELEGRAM_CHAT_ID.
Sin token el script sigue funcionando para leer y aplicar — solo no responde.
"""
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8")   # la consola de Windows es cp1252

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", ".."))
BANDEJA = os.path.join(RAIZ, "00_Ele", "bandeja")
APLICADAS = os.path.join(BANDEJA, "aplicadas")
ENV = os.path.join(RAIZ, "06_RRSS", ".env")


# --------------------------------------------------------------- credenciales
def _cargar_env():
    """El .env de RRSS ya existe y ya esta en .gitignore — se reutiliza en vez
    de inventar un segundo lugar donde guardar secretos (dueño unico)."""
    if not os.path.exists(ENV):
        return
    with open(ENV, encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea or linea.startswith("#") or "=" not in linea:
                continue
            k, v = linea.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def _token():
    _cargar_env()
    return os.environ.get("BANDEJA_TELEGRAM_TOKEN", "").strip()


# ------------------------------------------------------------------- mensajes
def _frontmatter(texto):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", texto, re.S)
    if not m:
        return {}, texto.strip()
    campos = {}
    for linea in m.group(1).split("\n"):
        if ":" in linea:
            k, v = linea.split(":", 1)
            campos[k.strip().lower()] = v.strip()
    return campos, m.group(2).strip()


def _listar():
    if not os.path.isdir(BANDEJA):
        return []
    return sorted(f for f in os.listdir(BANDEJA)
                  if f.lower().endswith(".md") and f.lower() != "readme.md")


def _leer(nombre):
    ruta = os.path.join(BANDEJA, nombre)
    if not os.path.exists(ruta):
        ruta = os.path.join(APLICADAS, nombre)
    if not os.path.exists(ruta):
        return None, None, None
    with open(ruta, encoding="utf-8") as f:
        campos, cuerpo = _frontmatter(f.read())
    return ruta, campos, cuerpo


# ------------------------------------------------------------------- Telegram
def _enviar(texto, chat_id=None):
    tok = _token()
    if not tok:
        print("   (sin BANDEJA_TELEGRAM_TOKEN: no se le respondio por Telegram)")
        return False
    chat_id = chat_id or os.environ.get("BANDEJA_TELEGRAM_CHAT_ID", "").strip()
    if not chat_id:
        print("   (sin chat_id: no se supo a quien responder)")
        return False
    datos = urllib.parse.urlencode({"chat_id": chat_id, "text": texto}).encode()
    url = "https://api.telegram.org/bot%s/sendMessage" % tok
    try:
        with urllib.request.urlopen(urllib.request.Request(url, data=datos), timeout=20) as r:
            ok = json.load(r).get("ok", False)
    except urllib.error.HTTPError as e:
        print("   Telegram respondio %s: %s" % (e.code, e.read()[:180].decode("utf-8", "replace")))
        return False
    except Exception as e:                                   # pragma: no cover
        print("   no se pudo hablar con Telegram: %s" % e)
        return False
    print("   respuesta enviada a Telegram" if ok else "   Telegram no acepto el envio")
    return ok


# ------------------------------------------------------------------- comandos
def cmd_pendientes(_args):
    """Lo corre /inicio-ele. Si no hay nada, NO imprime nada: un arranque no se
    ensucia con lineas que dicen que no pasa nada."""
    ms = _listar()
    if not ms:
        return 0
    print("\U0001f4e5 BANDEJA DE LA AMA — %d mensaje%s sin atender"
          % (len(ms), "" if len(ms) == 1 else "s"))
    for n in ms:
        _, campos, cuerpo = _leer(n)
        una = " ".join(cuerpo.split())
        print("   • %s  (%s)" % (n, campos.get("fecha", "sin fecha")))
        print("     %s" % (una[:150] + ("..." if len(una) > 150 else "")))
    print("   leer uno:    bandeja.py leer <archivo>")
    print("   cerrarlo:    bandeja.py aplicar <archivo> --responder \"...\"")
    return 0


def cmd_leer(args):
    if not args:
        print("uso: bandeja.py leer <archivo>")
        return 2
    ruta, campos, cuerpo = _leer(args[0])
    if not ruta:
        print("no existe ese mensaje: %s" % args[0])
        return 1
    print("=" * 70)
    for k in ("de", "fecha", "chat_id", "estado"):
        if campos.get(k):
            print("%-10s %s" % (k + ":", campos[k]))
    print("=" * 70)
    print(cuerpo)
    return 0


def cmd_aplicar(args):
    if not args:
        print("uso: bandeja.py aplicar <archivo> [--responder \"texto\"]")
        return 2
    nombre = args[0]
    ruta = os.path.join(BANDEJA, nombre)
    if not os.path.exists(ruta):
        print("no esta pendiente: %s" % nombre)
        return 1
    with open(ruta, encoding="utf-8") as f:
        crudo = f.read()
    campos, _ = _frontmatter(crudo)

    respuesta = None
    if "--responder" in args:
        i = args.index("--responder")
        if i + 1 < len(args):
            respuesta = args[i + 1]

    hoy = datetime.now().strftime("%Y-%m-%d")
    crudo = re.sub(r"^estado:.*$", "estado: aplicado el %s" % hoy, crudo, count=1, flags=re.M)
    if "estado:" not in crudo.split("---")[1 if crudo.startswith("---") else 0]:
        crudo = "estado: aplicado el %s\n" % hoy + crudo

    os.makedirs(APLICADAS, exist_ok=True)
    destino = os.path.join(APLICADAS, nombre)
    with open(destino, "w", encoding="utf-8", newline="\n") as f:
        f.write(crudo)
    os.remove(ruta)
    print("✅ aplicado y archivado: 00_Ele/bandeja/aplicadas/%s" % nombre)

    if respuesta:
        _enviar(respuesta, campos.get("chat_id"))
    else:
        print("   (sin --responder: no se le aviso a la Ama)")
    return 0


def cmd_responder(args):
    if not args:
        print("uso: bandeja.py responder \"texto\"")
        return 2
    return 0 if _enviar(args[0]) else 1


COMANDOS = {
    "pendientes": cmd_pendientes,
    "leer": cmd_leer,
    "aplicar": cmd_aplicar,
    "responder": cmd_responder,
}


def main(argv):
    if not argv or argv[0] not in COMANDOS:
        print(__doc__.split("COMANDOS")[1].split("EL TOKEN")[0].strip())
        return 2
    return COMANDOS[argv[0]](argv[1:])


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
