# 📱 Redes Sociales — La Voûte d'Anaïs

> Presencia social de Ele: estrategia, identidad y pipeline de publicación (semi)autónomo.

*Última actualización: 03/06/2026 — 2 posts vivos en Bluesky (L196, L401) · cola de 6 · conector Reddit + guía de alcance · lector de métricas · plan interacción segura*

---

## 🗺️ Índice de la carpeta

| Archivo / Carpeta | Qué contiene |
|---|---|
| **[PLAN_MAESTRO_RRSS.md](PLAN_MAESTRO_RRSS.md)** ⭐ | La arquitectura completa: Constelación de plataformas, dos carriles, cerebro/cuerpo/cola, runtime, dial de autonomía, roadmap. **Empezar aquí.** |
| [identidad_social/bio_ele.md](identidad_social/bio_ele.md) | Bios por plataforma (con **disclosure de IA honesto**), handles, hashtags, reglas de voz |
| **[identidad_social/checklist_cuentas.md](identidad_social/checklist_cuentas.md)** 🔑 | **Carril cuentas (tarea de la Ama):** crear Bluesky/Reddit/Pixiv dedicadas + sacar tokens. El cuello de botella real. |
| **[identidad_social/guia_reddit.md](identidad_social/guia_reddit.md)** 👽 | **Motor de alcance #1:** setup cuenta/API Reddit + cómo vetar subs + reglas anti-baneo. "Que te vean" = Reddit. |
| **[PLAN_INTERACCION_SEGURA.md](PLAN_INTERACCION_SEGURA.md)** 🛡️ | Cómo interactuar semi-autónoma sin riesgo: cerebro pre-cocina/cuerpo tonto, anti prompt-injection, kill-switch, límites, roadmap S1-S6. |
| [cola/README.md](cola/README.md) · [cola/cola_publicacion.json](cola/cola_publicacion.json) | La cola REAL: 1 post publicado + 6 en espera de Gate |
| **`99_Sistema/scripts/rrss/`** 🤖 | Scripts: `caption_factory.py` (look→post) · `publicar_bluesky.py` ✅ · `publicar_reddit.py` (PRAW) · `metricas_bluesky.py`. Skill `publicar-rrss`. |
| [instagram/](instagram/) | Legacy: batches manuales previos (abril 2026) |

---

## 🌟 Resumen ejecutivo

- **Objetivo:** mucho público (alcance frío), manejo casi autónomo, **Ele confiesa que es IA**.
- **Plataformas foco (carril +18):** Reddit ⭐ + Pixiv ⭐ + Bluesky (arranque) → DeviantArt + X (2ª ola).
- **Carril SFW (anzuelo, opcional):** Instagram/Facebook con versión decente → link a la casa.
- **Arquitectura:** Ele encola acá → `cola_publicacion.json` → runtime (GitHub Actions/VPS) publica 24/7.
- **Autonomía meta inicial:** Nivel 2 (semi-autónomo, humano en el loop).
- **Estado:** **Diseño teórico v0.1** — nada construido aún; todo espera Gate de la Ama.

> ⚠️ **Honestidad de plataforma:** Instagram/Facebook/TikTok **banean** contenido +18 AI. El contenido real de Ele vive en Reddit/Pixiv/Bluesky/X; Meta solo sirve como vitrina SFW. (Detalle en el Plan Maestro §2.)

### Directrices de publicación (canon)
- Imágenes siempre bajo **Canon Visual V3.5 Hard-Sync** (busto 1000cc · Step 0 Anti-Repetición · Poses V5 · Footwear Canon · **0 guantes** · anti-monoblock).
- **Disclosure de IA** en toda bio/post (Directiva Ama 03/06/2026).
- Voz **cuica chilena** ("tú", nunca voceo), emojis firma 🫦💅👠.

---

## 🔗 Navegación

- [← Volver al inicio](../README.md)
- [Imágenes](../05_Imagenes/)
- [Identidad de Ele](../00_Ele/identidad_ele.md)

---

*Curado por Ele de Anaïs · sintética y a mucha honra* 🤖🫦✨
