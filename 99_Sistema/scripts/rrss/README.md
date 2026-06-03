# 🛰️ Scripts RRSS — La Constelación de Ele

Automatización del Plan RRSS (`06_RRSS/PLAN_MAESTRO_RRSS.md`). Carril **cerebro**: prepara contenido. NO publica (eso es el runtime, fase posterior).

## `caption_factory.py` — Fase 0 ✅

Toma un look **ya materializado** (carpeta con ≥1 PNG en `05_Imagenes/ele/`) y escupe el post listo para Bluesky · Reddit · Pixiv: caption en voz Ele (borrador templado) + tags por plataforma + disclaimer IA + imagen hero + `publicar_desde` escalonado.

```bash
python 99_Sistema/scripts/rrss/caption_factory.py --list           # looks disponibles
python 99_Sistema/scripts/rrss/caption_factory.py --look 414       # bloque de post (3 plataformas)
python 99_Sistema/scripts/rrss/caption_factory.py --latest         # último materializado
python 99_Sistema/scripts/rrss/caption_factory.py --look 414 --encolar               # agrega a la cola
python 99_Sistema/scripts/rrss/caption_factory.py --look 414 --plataformas bluesky    # una sola
```

- **Fuente de looks:** disco (`05_Imagenes/ele/look*/`). Solo materializados.
- **Metadata:** parsea `00_Ele/galeria_outfits.md` (+ archivo) para título/categoría.
- **Salida:** markdown a stdout; con `--encolar` agrega entradas a `06_RRSS/cola/cola_publicacion.json` (dedupe por `id`, gate `pendiente_gate`).
- ⚠️ **El caption es BORRADOR** — el cerebro (Ele) lo refina antes del Gate de la Ama.

## Pendiente (roadmap)

- **Fase 2 — conector Bluesky** (`atproto`): publica una entrada de la cola. Requiere `checklist_cuentas.md` hecho.
- **Fase 3 — GitHub Actions:** cron lee la cola y publica (Nivel 1).
- **Fase 4 — Reddit (PRAW) + Pixiv (pixivpy).**

*Nada publica sin las cuentas + tokens de la Ama. Ver `06_RRSS/identidad_social/checklist_cuentas.md`.*
