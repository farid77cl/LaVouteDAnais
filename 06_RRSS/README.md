# 📱 Redes Sociales — La Voûte d'Anaïs

> Presencia social de Ele: estrategia, identidad y pipeline de publicación (semi)autónomo.

*Última actualización: 08/06/2026 — **📈 Playbook de engagement:** incorporadas las skills `marketing-psychology` (PLFS) + `marketing-ideas` (MFS) al carril de imágenes de Ele → 5 modelos de conducta + 5 ideas de crecimiento + orden de operaciones + guardarraíles éticos en `playbook_engagement.md` (ejecuta runtime con Gate). SEO aparcado (seo-audit/seo-fundamentals = sin sitio web, no aplica). — **👽 SEPARACIÓN Reddit (Directiva Ama):** dos cuentas, no una mixta → **`u/ele_de_anais`** (imágenes Ele, enciende PRIMERO) + **`u/LaVouteDAnais`** (relatos Anaïs, después). Perfiles copy-paste en `identidad_social/perfiles_reddit.md`; revierte el handle unificado del 07/06; guía Reddit + checklist + bio + estrategia SEO + `.env.example` + memoria actualizados; conector pendiente de selector `--account ele|relatos`. — Previo 07/06: **📣 Publicado L443 en Bluesky** (2 seguidores reales) + 🐛 fix bug "gordis"→"cariño" en caption_factory · **👽 CARRIL REDDIT COMPLETO (Reddit llega mañana, lleva imágenes + relatos en español):** conector `publicar_reddit.py` extendido a **text-posts/relatos** + `preparar_relato_reddit.py` nuevo + 2 relatos encolados (Mandato de los Tacones, Ginny la Genio Bimbo) + 2 imágenes (L443/L461), subs `VETAR_`/`EDITAR_` hasta vetar · **🔍 `estrategia_seo_tags.md` nuevo** (títulos keyword-front-loaded, taxonomía tags/flair, timing, anti-shadowban, alt-text) · **🏷️ Handle Reddit = `u/LaVouteDAnais`** (universo: imágenes Ele + relatos Anaïs, no `u/ele_de_anais`). Pendiente Ama: cuenta + credenciales + vetar subs. — Previo 04/06: **🎯 KPI ÚNICO FIJADO (Directiva Ama):** el objetivo de Ele en RRSS es OBTENER INTERACCIONES reales = éxito; no conseguirlas = fracaso (binario). Reescribe el plan: postear/followers NO cuenta, solo engagement. Cuello de botella = Reddit bloqueado en setup manual + 0 base. · Previo: 3er post vivo en Bluesky (L196, L401, L386 jirafa) · cola restante 4 · 👽 Reddit en pausa (bloqueo API 2025) · conector Reddit + métricas + plan interacción segura*

---

## 🎯 OBJETIVO ÚNICO (KPI — Directiva Ama 04/06/2026)

> **El objetivo de Ele en RRSS es OBTENER INTERACCIONES REALES.**
> **Conseguirlas = ÉXITO. No conseguirlas = FRACASO. Es binario.**

**Qué cuenta como interacción:** likes, upvotes, reposts, replies, comentarios y DMs de **personas reales**.
**Qué NO cuenta:** postear, tener cuentas bonitas, número de followers, cantidad de imágenes subidas. **Publicar ≠ interactuar.**

**Implicancia honesta (esto reescribe el plan entero):**
- Postear a Bluesky con **0 seguidores ≈ megáfono en una pieza vacía** → 0 interacciones → fracaso por definición.
- Las interacciones viven donde **YA hay audiencia**: subreddits +18, Pixiv. Ese es el motor de alcance frío.
- El cuello de botella HOY **no es automatización** — es **(a) Reddit bloqueado** en el setup manual de la Ama (cuenta + API) y **(b) que nadie sigue aún.**

**Cómo se gana el KPI (orden de prioridad):**
1. 🔓 **Desbloquear Reddit** — paso manual de la Ama: cuenta dedicada + credenciales API + vetar 3-5 subs. **Sin esto el KPI es inalcanzable.**
2. 💬 **Ele postea en los subs correctos + responde** (con Gate de la Ama al principio). Ahí aparecen los primeros upvotes/comentarios reales.
3. 📊 **Medir cada acción** contra interacciones (`metricas_bluesky.py` + equivalente Reddit). La acción que no mueve la aguja, se corta.
4. 🦋 **Bluesky = "casa", no motor.** Se mantiene viva para que no parezca muerta, pero no se espera engagement ahí hasta tener base.

**¿Ele lo hace o un agente?** — decisión técnica que la Ama deja a criterio de Ele:
- **El juicio que genera interacciones** (en qué sub postear, leer la sala, responder sin que la baneen ni la hackeen por prompt-injection) lo hace **Ele = el cerebro, con Gate.** No se delega a un bot tonto.
- **Lo mecánico** (encolar, publicar a horario, medir) → runtime/agente programado = el cuerpo.
- Un agente posteando a una pieza vacía saca lo mismo que Ele: **cero.** Por eso primero se abre el canal.

**Hito de medición propuesto (pendiente Gate Ama):** *primeras 10 interacciones reales (upvotes/comentarios/replies de personas) dentro de 2 semanas tras abrir Reddit.*

---

## 🗺️ Índice de la carpeta

| Archivo / Carpeta | Qué contiene |
|---|---|
| **[PLAN_MAESTRO_RRSS.md](PLAN_MAESTRO_RRSS.md)** ⭐ | La arquitectura completa: Constelación de plataformas, dos carriles, cerebro/cuerpo/cola, runtime, dial de autonomía, roadmap. **Empezar aquí.** |
| [identidad_social/bio_ele.md](identidad_social/bio_ele.md) | Bios por plataforma (con **disclosure de IA honesto**), handles, hashtags, reglas de voz |
| **[identidad_social/checklist_cuentas.md](identidad_social/checklist_cuentas.md)** 🔑 | **Carril cuentas (tarea de la Ama):** crear Bluesky/Reddit/Pixiv dedicadas + sacar tokens. El cuello de botella real. |
| **[identidad_social/guia_reddit.md](identidad_social/guia_reddit.md)** 👽 | **Motor de alcance #1:** setup cuenta/API Reddit + cómo vetar subs + reglas anti-baneo. "Que te vean" = Reddit. |
| **[identidad_social/perfiles_reddit.md](identidad_social/perfiles_reddit.md)** 🆔 | **Los 2 perfiles Reddit listos (copy-paste):** Ele (imágenes, `u/ele_de_anais`) + Anaïs (relatos, `u/LaVouteDAnais`). Bio, NSFW, avatar, subs, credenciales por cuenta. |
| **[playbook_engagement.md](playbook_engagement.md)** 📈 | **Playbook de engagement (imágenes de Ele):** 5 modelos de conducta (PLFS) + 5 ideas de crecimiento (MFS) de las skills de marketing, aplicados a `u/ele_de_anais` para mover el KPI de interacciones. Ejecuta el runtime con Gate. |
| **[PLAN_INTERACCION_SEGURA.md](PLAN_INTERACCION_SEGURA.md)** 🛡️ | Cómo interactuar semi-autónoma sin riesgo: cerebro pre-cocina/cuerpo tonto, anti prompt-injection, kill-switch, límites, roadmap S1-S6. |
| [cola/README.md](cola/README.md) · [cola/cola_publicacion.json](cola/cola_publicacion.json) | La cola REAL: 1 post publicado + 6 en espera de Gate |
| **`99_Sistema/scripts/rrss/`** 🤖 | Scripts: `caption_factory.py` (look→post) · `publicar_bluesky.py` ✅ · `publicar_reddit.py` (PRAW) · `metricas_bluesky.py`. Skill `publicar-rrss`. |
| [instagram/](instagram/) | Legacy: batches manuales previos (abril 2026) |

---

## 🌟 Resumen ejecutivo

- **🎯 Objetivo ÚNICO (KPI):** **OBTENER INTERACCIONES reales** (likes/upvotes/replies/comentarios/DMs) — conseguirlas = éxito, no conseguirlas = fracaso. Todo lo demás (followers, posteos, cuentas bonitas) es medio, no fin. Ver sección "🎯 Objetivo Único" arriba.
- **Contexto:** mucho público (alcance frío), manejo casi autónomo, **Ele confiesa que es IA**.
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
