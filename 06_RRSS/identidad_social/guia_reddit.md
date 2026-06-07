# 👽 Guía Reddit — el motor de alcance de Ele ("que te vean")

> **Por qué Reddit es EL motor:** es descubrimiento puro. Posteas en un sub grande y miles de desconocidos te ven **hoy**, sin necesidad de que te sigan (al revés de Bluesky). Para el objetivo de la Ama —"que todos la vean"— Reddit es la prioridad #1.
>
> **Estado (07/06/2026):** 🟡 **Reddit llega MAÑANA** (la Ama confirmó cuenta + credenciales). Conector `publicar_reddit.py` ✅ ahora soporta **imágenes Y text-posts (relatos)**. Reddit llevará **imágenes + nuestros relatos** (relatos en **español** por ahora; inglés queda para después). Estrategia de tags/posicionamiento en [`../estrategia_seo_tags.md`](../estrategia_seo_tags.md).
>
> **⏸️ EN PAUSA (04/06/2026 — decisión Ama):** crear la app de API se trabó del lado de Reddit. A fines de 2025 Reddit endureció el acceso: la creación de apps `script` pasa por registro de developer + aprobación manual, y hay bug/bloqueo conocido donde `create app` no avanza (error tipo *"You cannot create any more applications…"*), agravado en cuentas nuevas/sin email verificado. Refs: [GitHub gallery-dl #8559](https://github.com/mikf/gallery-dl/issues/8559) · [Responsible Builder Policy](https://support.reddithelp.com/hc/en-us/articles/42728983564564-Responsible-Builder-Policy). **Plan al retomar (en unos días):** (1) verificar email de la cuenta · (2) dejar madurar la cuenta con actividad/karma · (3) reintentar `create app` (adblock off / incógnito) · (4) si sigue trabado → solicitud formal de acceso API o caer al **Plan A manual** (paquete copy-paste, no necesita API). La Ama NO quiere postear manual por ahora.

---

## 1. Crear la cuenta (manual — solo la Ama)

- [ ] **reddit.com** → crear cuenta con el email dedicado `Ele.de.Anais@proton.me`. Usuario sugerido: `u/ele_de_anais` (o disponible).
- [ ] Verificar email.
- [ ] **Settings → Profile** → marcar el perfil como **NSFW** + pegar bio (de `bio_ele.md`).
- [ ] **Settings → Privacy → permitir contenido adulto.**
- [ ] Subir avatar (el mismo de Bluesky, en el Escritorio).

## 2. Crear la "app" de API (para que el conector publique)

- [ ] Ir a **reddit.com/prefs/apps** → abajo: **"create another app..."**
- [ ] Tipo: **script** · nombre: `ele-runtime` · redirect uri: `http://localhost:8080`
- [ ] Crear → copiar:
  - **client_id** = el string corto bajo el nombre de la app.
  - **secret** = el campo "secret".
- [ ] Pegar en `06_RRSS/.env` (gitignored):
  ```
  REDDIT_CLIENT_ID=...
  REDDIT_CLIENT_SECRET=...
  REDDIT_USERNAME=ele_de_anais
  REDDIT_PASSWORD=la-contraseña-de-la-cuenta
  ```
  (No me la pegues en el chat — la leo del .env.)

## 3. Probar
```bash
python 99_Sistema/scripts/rrss/publicar_reddit.py --test   # login + karma
```

---

## 4. 🎯 DÓNDE postear — encontrar y vetar los subs (lo más importante)

⚠️ **No me invento nombres ni reglas:** los subs y sus reglas cambian seguido. Tu tarea es buscar y vetar. Acá la estrategia exacta.

### Cómo buscarlos
- Buscador de Reddit: términos como `AI`, `AI art`, `aigen`, `latex`, `fetish`, `bimbo`, `dollification`, `bdsm`, `pinup` (+ filtrar communities).
- Mirar la barra lateral de un sub bueno → suele listar subs hermanos/relacionados.
- Ver en qué subs postean cuentas de AI-art NSFW parecidas a Ele.

### Checklist de veto (antes de postear en un sub)
- [ ] ¿Permite **contenido generado por IA**? (muchos lo prohíben — leer reglas).
- [ ] ¿Permite **NSFW**? ¿Y **self-post / OC** (no solo "requests")?
- [ ] ¿Exige **karma mínimo / edad de cuenta**? (cuenta nueva = madurar unos días antes).
- [ ] ¿Pide **flair** obligatorio (ej. "AI")? ¿Marcar **NSFW** sí o sí?
- [ ] ¿Prohíbe links / promoción? ¿Cuántos posts por día/semana permite?
- [ ] Tamaño del sub (miembros) y actividad (posts/día) → más grande = más alcance.

### ⚠️ Candidatos a VETAR en la app (NO confirmados — reglas IA/flair/karma cambian)
> Estos son subs **reales** que conozco, pero **NO verifiqué sus reglas en vivo** (Reddit bloquea mi WebFetch). Antes de publicar en cualquiera: correr el **Checklist de veto** de arriba dentro de la app. En la cola están marcados con prefijo `VETAR_` → el conector **se niega a publicar** hasta que cambies `VETAR_<sub>` por el nombre real ya vetado.

**🖼️ Carril IMÁGENES (AI fetish — inglés/visual, idioma-agnóstico):**

| Subreddit (candidato) | Tipo | Vetar: ¿IA? ¿OC? ¿Flair? ¿Karma? |
|---|---|---|
| r/unstable_diffusion | AI NSFW grande | ¿exige flair AI? ¿karma? |
| r/aiNudes | AI NSFW | ¿OC propio? |
| r/aiporn | AI NSFW | ¿flair? |
| r/sdnsfw | Stable Diffusion NSFW | ¿solo SD? |
| r/Sexyaiart | AI art sensual | ¿nivel de explicitud? |
| r/BimboFication | Fetish bimbo | ¿acepta IA? ¿flair? |
| r/dollification | Fetish muñeca | ¿acepta IA/OC? |

**📖 Carril RELATOS (español — text/self-post):**

| Subreddit (candidato) | Tipo | Vetar: ¿IA? ¿flair? ¿karma? ¿largo? |
|---|---|---|
| r/RelatosEroticos | Relatos ES (principal, grande) | ¿permite disclosure IA? ¿flair de género? ¿karma mín? |
| r/RelatosDeSexo | Relatos sexo ES | ¿reglas de contenido (noncon)? |
| r/HistoriasEroticas | Historias eróticas ES | ¿flair? |
| r/relatoshot | Relatos hot ES | ¿tamaño/actividad? |

> **Cómo vetar rápido:** abrir el sub → leer reglas fijadas + sidebar → confirmar (1) IA permitida, (2) self-post/OC permitido, (3) flair que corresponde, (4) karma/edad que cumplo, (5) NSFW obligatorio. Si las 5 ✅ → cambiar `VETAR_<sub>` por `<sub>` en la cola.

---

## 4-bis. 📖 Carril RELATOS — cómo se publica texto (NUEVO 07/06)

El conector ahora hace **text-posts**. Las entradas de relato en la cola usan:
- `tipo: "text"` · `selftext_file: 06_RRSS/reddit_relatos/<slug>.txt` (prosa ya limpia: hook + relato + disclosure IA) · `titulo:` con tags SEO `[Hipnosis][Bimbo]…`
- Generar el .txt: `python 99_Sistema/scripts/rrss/preparar_relato_reddit.py` (quita metadata interno, deja hook+prosa+disclosure, valida ≤40.000 chars).
- Relatos **>40k chars** (ej. de ~7.000+ palabras) van **serializados** (Parte 1/2) — un post por parte, "Parte 2 en el siguiente post / comentario".
- **Ya en cola (pendientes de sub vetado + Gate):** `El Mandato de los Tacones` (~2.450 palabras) · `Ginny, la Genio Bimbo` (~5.860). 3º elegido: `Buena Chica, Buena Muñeca` (~10.000 → serializar).

---

## 5. 🚫 Reglas anti-baneo (innegociables)

- **NUNCA el mismo título/post idéntico en varios subs** (cross-post idéntico = shadowban). Cada sub = **título propio**.
- **Cadencia humana:** cuenta nueva no postea en 5 subs el primer día. Madurar, comentar, participar primero.
- **Respetar las reglas de cada sub** al pie de la letra (flair, NSFW, formato).
- **Disclosure IA** siempre (es imán en subs AI, no estigma).
- 1 imagen fuerte por post (el conector sube `submit_image`); el caption va de comentario.

---

## 6. Cómo publicamos (cuando haya cuenta + subs)

1. La Caption Factory ya genera entradas reddit: `--look <N> --plataformas reddit --encolar`.
2. Editar en la cola el `destino.subreddit` real + título propio del sub.
3. Preview: `python publicar_reddit.py --preview L<N>-reddit-01`
4. Con tu Gate: `python publicar_reddit.py --publicar L<N>-reddit-01 --confirmar`

> El conector ya está construido y con freno de mano. Lo único que falta es **tu cuenta + las credenciales + 3-5 subs vetados.** Con eso, encendemos el motor de alcance. 🫦👠

---
*Guía creada 03/06/2026 · Reddit = prioridad #1 para "que te vean"* 👽🔥
