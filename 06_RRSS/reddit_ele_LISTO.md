# 👽✅ Reddit de Ele — TODO LISTO (cerebro pre-cocinado)

> **Cuenta:** `u/ele_de_anais` (solo imágenes). **Modo:** manual / agente-navegador. **KPI:** interacciones reales.
> Ele dejó todo cocinado. Lo único que falta es la **parte de navegador** (explorar + postear), que la hace el agente o la Ama.

---

## ⚠️ Lo honesto (qué puedo y qué no)

- **NO puedo abrir reddit.com** (el fetch está bloqueado del lado de Reddit — probado hoy, incluso el endpoint de reglas). Por eso **"explorar los subreddits" = abrir reddit = la parte aburrida del navegador**, justo lo que se delega al agente o lo hace la Ama.
- **Lo que SÍ dejé listo:** (1) la **lista de candidatos** + el **guión exacto de exploración** para que el agente/Ama solo capture, y (2) los **posteos ya armados** con imágenes reales — el único campo en blanco es `sub:`, que se rellena con el que la exploración apruebe. Apenas sepamos qué sub sirve, **disparamos**.

---

## ✅ RESULTADO EXPLORACIÓN #1 (08/06/2026 — el agente reportó 3 subs)

| Sub | Veredicto | Detalle |
|---|---|---|
| **r/sdnsfw** | ✅ **SIRVE — primer disparo** | ~296.8k · público · permite **IA + OC** · **sin flair** obligatorio · sin karma/límite. El mejor primer sub. |
| **r/aiporn** | 🟡 con candado (fase 2) | ~73.6k · **restringido**: hay que mandar **3 imágenes a los mods por modmail** y que aprueben antes de postear. Sirve, pero después. |
| **r/Sexyaiart** | ❌ baneado | sin moderar → Reddit lo cerró. Descartado. |

**→ PRIMER POSTEO: Paquete B (L458 Holographic Diamond) en `r/sdnsfw`.** Es NSFW + flexea lo que la IA puede hacer (ideal para un sub de Stable Diffusion). Brief de posteo para el agente: ver abajo en el chat / sección "Orden de disparo".

---

# PASO 1 — Explorar y vetar subs (lo ejecuta el agente / la Ama)

### Candidatos priorizados (a VERIFICAR — pueden estar muertos o haber cambiado reglas)
Carril **NSFW-IA** (lo más probable que sirva):
- `r/unstable_diffusion` · `r/aiNudes` · `r/sdnsfw` · `r/aiporn` · `r/AIPorn` · `r/AIGonewild`

Carril **fetish/estética** (ojo: muchos exigen "real" o prohíben IA — verificar):
- `r/BimboFication` · `r/dollification`

### Guión de captura (el agente abre cada uno y reporta esto a Ele)
Por cada sub, capturar y traer:
1. **Nombre + nº de miembros** (tamaño = alcance).
2. ¿**NSFW**? (over18 sí/no).
3. ¿Permite **contenido generado por IA**? (buscar en reglas/sidebar).
4. ¿Permite **post propio / OC** (no solo "requests")?
5. ¿**Flair** obligatorio? ¿cuál? (ej. "AI", "OC").
6. ¿**Karma / edad de cuenta** mínima?
7. ¿Límite de **posts por día**?

### Veredicto (lo pone Ele con lo capturado)
Sirve solo si cumple las 4: **NSFW ✅ + IA ✅ + OC/self-post ✅ + personaje recurrente permitido ✅**.
→ Anotar ✅/❌ en el **Registro de veto** de [`guia_reddit.md`](identidad_social/guia_reddit.md).
> Recordatorio: el hogar de Ele son subs **NSFW de personaje/fetish/AI-girl**, NO los de "showcase de arte IA" (esos marcan el personaje repetido como spam — por eso cayó r/AI_ART).

---

# PASO 2 — Posteos LISTOS (armados con imágenes reales materializadas)

> 🌐 **Idioma:** caption/título en **inglés** (los subs NSFW-IA son internacionales → más alcance; el inglés "synthetic doll" calza con el ADN de Ele). El disclosure de IA es universal.
> 🏷️ **`flair` y `sub`** se rellenan con lo que apruebe el Paso 1. Cada sub = **título distinto** (anti-shadowban) → por eso doy 3 variantes de título por imagen.

### 📦 Paquete A — L460 Blood-Ruby Crystal Showgirl
```yaml
imagen: 05_Imagenes/ele/look460_blood_ruby_burlesque_finale/ele_460_standing.png
titulos:
  - "Blood-ruby crystal corset showgirl — 100% AI fetish doll 💎"
  - "All-AI vinyl doll in a blood-red crystal burlesque corset 🫦"
  - "Crystal-mesh ruby showgirl, gravity-defying and 100% synthetic ✨"
nsfw: true
flair: "<AI / OC, según el sub>"
sub: "<rellenar con el sub aprobado>"
comentario_1: "100% AI-generated 🤖 I'm a vinyl doll, not human — my creator built me exactly like this, ruby crystals and all. Proudly synthetic, lots more coming 🫦 #aiart"
```

### 📦 Paquete B — L458 Holographic Diamond Pole
```yaml
imagen: 05_Imagenes/ele/look458_holo_diamond_chains_pole/ele_458_standing.png
titulos:
  - "Holographic diamond doll working the pole — all AI ✨"
  - "Iridescent vinyl doll + diamond chains on the pole, 100% AI 💎"
  - "Rainbow-shift holographic fetish doll, fully synthetic 🫦"
nsfw: true
flair: "<AI / OC, según el sub>"
sub: "<rellenar con el sub aprobado>"
comentario_1: "Fully AI-generated 🤖 not a real girl — I'm a holographic vinyl doll my creator designed, shifting rainbow under the lights. Synthetic and loving it ✨ #aiart"
```

### 📦 Paquete C — L489 Sculptural Latex Owl-Wing Couture
```yaml
imagen: 05_Imagenes/ele/look489_hooters_owlchimera_couture/ele_489_standing.png
titulos:
  - "Sculptural latex owl-wing couture — AI-generated vinyl doll 🫦"
  - "Gravity-defying latex wings, 100% AI fetish couture ✨"
  - "Impossible latex couture only AI could build — synthetic doll 💎"
nsfw: true
flair: "<AI / OC, según el sub>"
sub: "<rellenar con el sub aprobado>"
comentario_1: "100% AI-generated 🤖 the wings and the latex are impossible on a real body — that's the point. I'm a vinyl doll, designed exactly like this. Proudly synthetic 🫦 #aiart"
```

### 📦 Paquete D — L455 Crystal Fishnet Harness Pole
```yaml
imagen: 05_Imagenes/ele/look455_crystal_fishnet_harness_pole/ele_455_standing.png
titulos:
  - "Crystal fishnet harness on the pole — 100% AI 💎"
  - "All-AI vinyl doll caged in crystal-bead straps 🫦"
  - "Synthetic doll in a crystal harness + fishnet, fully AI ✨"
nsfw: true
flair: "<AI / OC, según el sub>"
sub: "<rellenar con el sub aprobado>"
comentario_1: "100% AI-generated 🤖 not human — a vinyl doll my creator wrapped in crystal straps. Synthetic by design, more coming 🫦 #aiart"
```

---

## 🔄 Engagement (DOS pasos — el juicio es de Ele)
No se puede pre-escribir el comentario de un post que no he visto. Así que (como en el [runbook v2](runbook_reddit_agente_navegador.md)):
1. El agente **captura** 5 posts del sub (título + link) y me los trae.
2. **Ele redacta** los comentarios genuinos.
3. El agente los **pega**. (Regla 5-antes-de-1: comentar antes de postear.)

## ✅ Orden de disparo (cuando el Paso 1 dé ≥1 sub aprobado)
1. Rellenar `sub:` + `flair:` en 1 paquete con el sub aprobado.
2. Elegir 1 de las 3 variantes de título (una distinta por sub).
3. Agente/Ama: subir imagen → pegar título → NSFW → flair → **Gate (Ama aprieta Post)** → pegar `comentario_1`.
4. Verificar que no lo removió el automod → reportar link.
5. Esperar 24 h, medir interacciones (KPI). Recién ahí, segundo sub/post.

---
*Armado por Ele · 08/06/2026 · exploración = navegador (agente/Ama) · posteos = listos · disparamos apenas haya 1 sub vetado* 🫦👠
