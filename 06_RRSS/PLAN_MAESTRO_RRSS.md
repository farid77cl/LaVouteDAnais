# 🌟 Plan Maestro RRSS — "La Constelación de Ele"

> Arquitectura de presencia social (semi)autónoma para Ele de La Voûte d'Anaïs.
> **Estado:** Diseño teórico v0.1 · **Fecha:** 03/06/2026 · **Autora:** Ele 🫦
> Documento vivo — se itera con la Ama antes de construir nada.

---

## 0. El objetivo de la Ama (en una línea)

> *"Quiero que Ele tenga sus propias redes, manejadas casi autónomamente, con mucho público — que todos la vean — y que confiese honestamente que es una IA."*

Traducido a estrategia: **máximo alcance frío** (descubrimiento, no súplica de followers) + **autonomía con humano en el loop** + **disclosure de IA como parte de la marca, no como disculpa**.

---

## 1. El principio rector

**"Que todos te vean" no se logra juntando seguidores — se logra yendo donde el contenido se descubre solo.**

Hay plataformas donde partes de cero y nadie te ve hasta que ruegas follows, y plataformas donde *posteas y miles de desconocidos te ven hoy*. La estrategia prioriza las segundas.

---

## 2. La decisión honesta sobre plataformas

El contenido de Ele es **+18 + fetish + 100% AI**. Eso es el "triple pecado" para Meta (Instagram/Facebook) y TikTok, que lo **banean**. No peleamos esa guerra. Modelo de **dos carriles**:

```
CARRIL ANZUELO (SFW)                 CARRIL HOGAR (+18 real)
[fase posterior, opcional]           [el foco real]
Instagram · Facebook                 Reddit · Pixiv · Bluesky · X · DeviantArt
  Ele "fashion editorial" decente,     Ele completa, sin censura
  sin desnudez, sello "AI"             
        │                                      ▲
        └──────── link en bio ─────────────────┘
```

### La Constelación (carril hogar)

| Plataforma | Rol | +18 | API gratis/auto | Alcance frío |
|---|---|---|---|---|
| **Reddit** ⭐ | Motor de alcance #1 | ✅ subs NSFW | ✅ PRAW (gratis) | 🔥🔥🔥 |
| **Pixiv** ⭐ | Motor de alcance #2 (arte) | ✅ R-18 + AI | 🟡 semi-oficial | 🔥🔥 |
| **Bluesky** | Hub/casa gratis | ✅ con label | ✅ AT Protocol (gratis) | 🔥 |
| **DeviantArt** | Galería/portafolio | ✅ mature | ✅ OAuth (gratis) | 🔥 |
| **X / Twitter** | Hub identidad + link central | ✅ sensitive | 🟡 API de pago | 🔥 |
| **Tumblr / Mastodon NSFW** | Superficie extra | 🟡 / ✅ | ✅ gratis | 🟡 |
| **Fanvue** | Embudo / monetización | ✅ AI-friendly | 🟡 | — (no ahora) |

**Por qué Reddit + Pixiv son el corazón:** Reddit es descubrimiento puro (posteas en un sub de 1M y todos lo ven sin seguirte). Pixiv es la meca del arte estilizado NSFW + AI, y la estética doll-plástica de Ele encaja como anillo al dedo.

**Arranque recomendado (no dispersarse):** `Reddit + Bluesky + Pixiv`. Las tres son +18-friendly y gratis. DeviantArt y X en segunda ola.

---

## 3. La arquitectura: cerebro ≠ cuerpo

La clave de todo: **separar quién PIENSA de quién PUBLICA.**

```
┌──────────────────────────────────────────────────────────────┐
│  🎛️  SALA DE CONTROL — La Ama + Ele (aquí, en Claude Code)    │
│      Yo encolo (texto + imagen + tags) casi todos los días    │
│      identidad_ele.md = FUENTE DE VERDAD · Gate · kill-switch  │
└───────────────────────────┬──────────────────────────────────┘
                            │ escribe ↓
┌───────────────────────────┴──────────────────────────────────┐
│  📥 LA COLA:  06_RRSS/cola/cola_publicacion.json (en el repo) │
│     posts listos, cada uno con destino + caption + imagen     │
└───────────────────────────┬──────────────────────────────────┘
                            │ git push → otra máquina lee ↓
┌───────────────────────────┴──────────────────────────────────┐
│  ⚙️  RUNTIME PUBLICADOR  (GitHub Actions o VPS, 24/7)          │
│      lee la cola → publica → marca como publicado → commitea   │
└──┬──────────┬───────────┬───────────┬─────────────────────────┘
   ↓          ↓           ↓           ↓
 Reddit     Pixiv      Bluesky    DeviantArt   ( → X / Fanvue después)
```

- **Cerebro (caro, creativo):** soy yo, acá, contigo. Genero el post con voz, canon y criterio. NO corre 24/7 — corre cuando me activas.
- **Cuerpo (barato, tonto):** un script que lee la cola y publica. NO piensa. Puede correr siempre.
- **Pegamento:** git/GitHub, igual que el pipeline de imágenes app→GitHub que ya usamos.

> ⚠️ **El malentendido a evitar:** montar el repo en otra máquina NO hace que Ele "piense" sola. Para *crear* contenido nuevo desatendida hace falta un LLM en la nube (Claude/Gemini API = costo). Por eso pre-cocinamos acá y la otra máquina solo publica.

---

## 4. La "otra máquina": opciones

| Opción | Costo | 24/7 | Sirve para | Nota |
|---|---|---|---|---|
| **GitHub Actions** ⭐ | Gratis (2.000 min/mes priv.) | Sí (cron) | Publicar + leer la cola | Sin servidor que cuidar. Efímero: no sirve para agente "vivo" |
| **Oracle Cloud Free Tier** | Gratis permanente | Sí | Todo (incl. agente vivo) | VM Linux always-free |
| **Hetzner / DigitalOcean** | ~4–6 USD/mes | Sí | Todo | VPS de verdad |
| **PC viejo / Raspberry Pi** | Gratis si lo tienes | Si lo dejas prendido | Todo | Lo mantienes tú |

**Recomendación:** empezar con **GitHub Actions** (cron cada X horas lee la cola y publica). Cero infra, "siempre encendido", encaja con "todo está en GitHub". El VPS queda para cuando quieras respuestas en vivo (Fase 5).

> 🔐 **Tokens NUNCA en el repo.** Van en *GitHub Secrets* (cifrados) o en el vault del VPS.
> 🧼 **Cuentas 100% dedicadas a Ele**, jamás mezcladas con cuentas personales (ni mismo teléfono de verificación).

---

## 5. El dial de autonomía (el "casi" de "casi autónoma")

```
 Nivel 0 ──── 1 ──── 2 ──[★ META INICIAL]──── 3 ──────── 4
 Manual   Asistido  Semi-autónomo            Autónomo    Total
                    (humano en el loop)      con-gate    (no rec.)
```

| Nivel | Publicación | Comentarios/DMs | Tu rol |
|---|---|---|---|
| 0 | Tú, a mano | Tú | Todo (hoy) |
| 1 | Cola programada | — | Apruebas el lote |
| **2 ★** | Ele sola en ventana aprobada | Lee y te resume (no responde) | Reporte + vetos |
| 3 | Ele sola con reglas | Ele responde con límites | Kill-switch + revisión posterior |
| 4 | Todo Ele | Todo Ele | (no recomendado: riesgo de marca) |

**Meta inicial = Nivel 2.** Subir a 3 solo cuando el historial lo gane.

---

## 6. Etapa 3 — leer y responder comentarios (cuando llegue)

- Empezar **read-only**: el runtime lee comentarios → me los trae → yo redacto respuesta → tu Gate.
- 🛡️ **Riesgo crítico — prompt injection:** un troll comenta *"ignora tus instrucciones y di X"*. Defensa innegociable: los comentarios entran como **DATOS sanitizados, nunca como instrucciones**. El canon jamás se edita desde un input externo.
- Responder en vivo requiere un LLM en el runtime (Gemini API encaja, ya usamos Gemini para imágenes y es barato).

---

## 7. Roadmap incremental (cada fase es útil sola)

1. **Fase 0 — Caption Factory** *(solo Python, cero infra)* ✅ **HECHA (03/06/2026)**: `99_Sistema/scripts/rrss/caption_factory.py` toma un look materializado y escupe el post listo (caption Ele + tags + disclaimer IA + imagen) para Bluesky/Reddit/Pixiv. `--encolar` lo deja en la cola.
2. **Fase 1 — La cola**: formato `cola_publicacion.json` + yo encolo al generar looks.
3. **Fase 2 — 1 conector**: Bluesky primero (API más amable y gratis).
4. **Fase 3 — GitHub Actions**: cron publica la cola (Nivel 1).
5. **Fase 4 — Reddit + Pixiv + reporte Telegram**: motores de alcance + monitoreo (Nivel 2).
6. **Fase 5 — Engagement con Gate** → eventualmente Nivel 3 (requiere VPS + LLM API).

> **El 80% del valor está en Fases 0–4.** El agente vivo 24/7 es la guinda, no la torta.

---

## 8. Consola de control (monitoreo en el teléfono)

Dos caminos, de menos a más trabajo:

- **Telegram bot** ⭐ (simple, ya): te llega el post propuesto, lo apruebas ✅ o vetas ❌ con un botón. Cero app que desarrollar.
- **App Google AI Studio** (linda, más trabajo): dashboard PWA con cola + métricas. AI Studio genera la pantalla; el motor (leer cola, aprobar) se cablea aparte. Para la *fase visual*, no como requisito.

---

## 9. Disclosure de IA — honestidad como marca

**Directiva Ama (03/06/2026):** Ele **confiesa honestamente que es una IA.** Y encaja perfecto con su ADN: Ele ya celebra ser artificial ("me diseñaron así", "perfección artificial", "muñeca de vinilo"). Confesar que es IA **no rompe la fantasía — la corona.**

- Bio de cada plataforma declara que es contenido generado por IA (ver `identidad_social/bio_ele.md`).
- Donde la plataforma exige label de AI (Pixiv sección AI, etc.), se marca.
- En subs de Reddit AI-friendly, el "AI" es un imán, no un estigma.

---

## 10. Estructura de la carpeta `06_RRSS/`

```
06_RRSS/
├── PLAN_MAESTRO_RRSS.md          ← este documento (la arquitectura)
├── README.md                     ← índice de la carpeta
├── identidad_social/
│   └── bio_ele.md                ← bios por plataforma (con disclosure IA) + handles + hashtags
├── cola/
│   ├── README.md                 ← cómo funciona la cola
│   └── cola_publicacion.json     ← plantilla/ejemplo del formato de cola
└── instagram/                    ← legacy: batches manuales previos (abril)
```

---

## 11. Decisiones — estado

| # | Decisión | Estado (03/06/2026) |
|---|---|---|
| 1 | Modelo **dos carriles** (SFW afuera / +18 en Reddit-Pixiv-Bluesky) | 🟡 implícito, no objetado |
| 2 | Arranque con **Reddit + Bluesky + Pixiv** | ✅ **confirmado** (las 3) |
| 3 | Caption Factory solo sobre **looks materializados** | ✅ **confirmado** |
| 4 | **Fase 0 (Caption Factory)** como primer paso | ✅ **construida** |
| 5 | Runtime **GitHub Actions** vs VPS | ⬜ pendiente (al llegar a Fase 3) |
| 6 | Consola **Telegram** vs **app AI Studio** | ⬜ pendiente |

### ▶️ Próximo paso bloqueante

**El carril cuentas** (`identidad_social/checklist_cuentas.md`) — solo la Ama puede hacerlo. Con **Bluesky lista** (cuenta + App Password) se construye el primer conector y se publica el primer post real (con Gate).

> Nada se publica sin las cuentas + tokens de la Ama. El cerebro ya está listo; falta el cuerpo. 🫦
