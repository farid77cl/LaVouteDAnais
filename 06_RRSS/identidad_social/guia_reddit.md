# 👽 Guía Reddit — el motor de alcance de Ele ("que te vean")

> **Por qué Reddit es EL motor:** es descubrimiento puro. Posteas en un sub grande y miles de desconocidos te ven **hoy**, sin necesidad de que te sigan (al revés de Bluesky). Para el objetivo de la Ama —"que todos la vean"— Reddit es la prioridad #1.
>
> **Estado (08/06/2026 — Directiva Ama: SEPARAR relatos de imágenes):** 🟡 **Dos cuentas Reddit separadas, no una mixta.** El conector `publicar_reddit.py` ✅ soporta imágenes Y text-posts; ahora cada tipo va a SU cuenta:
> - **`u/ele_de_anais`** = **imágenes de Ele** (mismo handle que Bluesky). ⭐ **Se enciende PRIMERO** (las fotos crecen más rápido en Reddit + público amplio e idioma-agnóstico).
> - **`u/LaVouteDAnais`** = **relatos de Anaïs / La Voûte** (en español por ahora). Se abre **después**, cuando la de imágenes esté caliente. (Alt handle: `u/AnaisBelland` si prefieres marcar a la autora.)
>
> **Por qué separar (Directiva Ama):** los públicos casi no se solapan; los subs de imágenes quieren foto y los de literatura quieren texto; y separar aísla baneos (un ban en un canal no mata el otro). Costo = doble setup manual. Estrategia de tags/posicionamiento en [`../estrategia_seo_tags.md`](../estrategia_seo_tags.md).
>
> **⏸️ EN PAUSA (04/06/2026 — decisión Ama):** crear la app de API se trabó del lado de Reddit. A fines de 2025 Reddit endureció el acceso: la creación de apps `script` pasa por registro de developer + aprobación manual, y hay bug/bloqueo conocido donde `create app` no avanza (error tipo *"You cannot create any more applications…"*), agravado en cuentas nuevas/sin email verificado. Refs: [GitHub gallery-dl #8559](https://github.com/mikf/gallery-dl/issues/8559) · [Responsible Builder Policy](https://support.reddithelp.com/hc/en-us/articles/42728983564564-Responsible-Builder-Policy). **Plan al retomar (en unos días):** (1) verificar email de la cuenta · (2) dejar madurar la cuenta con actividad/karma · (3) reintentar `create app` (adblock off / incógnito) · (4) si sigue trabado → solicitud formal de acceso API o caer al **Plan A manual** (paquete copy-paste, no necesita API). La Ama NO quiere postear manual por ahora.

---

## 1. Crear las DOS cuentas (manual — solo la Ama)

> 📋 **Los dos perfiles listos para copiar/pegar (bio, handle, NSFW, avatar, subs) están en [`perfiles_reddit.md`](perfiles_reddit.md).** Acá va el orden y lo esencial.

**Cuenta A — IMÁGENES (Ele) · `u/ele_de_anais` · ⭐ PRIMERO:**
- [ ] **reddit.com** → crear cuenta con el email `Ele.de.Anais@proton.me`. Handle: **`u/ele_de_anais`** (o disponible).
- [ ] Verificar email.
- [ ] **Settings → Profile** → marcar perfil **NSFW** + pegar la **bio de Ele** (ver `perfiles_reddit.md`).
- [ ] **Settings → Privacy → permitir contenido adulto.**
- [ ] Avatar: el mismo de Bluesky (Ele ditzy).

**Cuenta B — RELATOS (Anaïs / La Voûte) · `u/LaVouteDAnais` · DESPUÉS:**
- [ ] **reddit.com** → crear cuenta para los relatos. Handle: **`u/LaVouteDAnais`** (o `u/AnaisBelland`). 💡 Reddit permite **varias cuentas con el mismo email**; si quieres separarlas del todo, usa un alias de Proton.
- [ ] Verificar email + marcar perfil **NSFW** + permitir adulto.
- [ ] Pegar la **bio de Anaïs** (ver `perfiles_reddit.md`).
- [ ] Avatar: uno de **Anaïs** (Vintage Noir), NO el de Ele — son marcas distintas.

> ⚠️ **No crear las dos frías el mismo día.** Abre primero la de Ele, déjala madurar (karma/actividad) y luego la de Anaïs. Dos cuentas nuevas +18 posteando a la vez = bandera roja para Reddit.

## 2. Crear la "app" de API (para que el conector publique)

- [ ] Ir a **reddit.com/prefs/apps** → abajo: **"create another app..."**
- [ ] Tipo: **script** · nombre: `ele-runtime` · redirect uri: `http://localhost:8080`
- [ ] Crear → copiar:
  - **client_id** = el string corto bajo el nombre de la app.
  - **secret** = el campo "secret".
- [ ] **Una app de API por cuenta** (cada cuenta necesita su client_id/secret). Pegar en `06_RRSS/.env` (gitignored), con prefijo por cuenta:
  ```
  # Cuenta A — IMÁGENES (Ele) — se enciende primero
  REDDIT_ELE_CLIENT_ID=...
  REDDIT_ELE_CLIENT_SECRET=...
  REDDIT_ELE_USERNAME=ele_de_anais
  REDDIT_ELE_PASSWORD=la-contraseña-de-la-cuenta-Ele
  # Cuenta B — RELATOS (Anaïs / La Voûte) — después
  REDDIT_LV_CLIENT_ID=...
  REDDIT_LV_CLIENT_SECRET=...
  REDDIT_LV_USERNAME=LaVouteDAnais
  REDDIT_LV_PASSWORD=la-contraseña-de-la-cuenta-La-Voûte
  ```
  (No me las pegues en el chat — las leo del .env.)
  > 🔧 **Pendiente al cablear:** el conector `publicar_reddit.py` hoy lee un set genérico `REDDIT_*`; hay que agregarle un selector **`--account ele|relatos`** que elija el set con prefijo (`REDDIT_ELE_*` / `REDDIT_LV_*`). Cambio chico, se hace cuando exista la primera cuenta y haya con qué probar.

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

**🖼️ Carril IMÁGENES → cuenta `u/ele_de_anais` (AI fetish — inglés/visual, idioma-agnóstico):**

| Subreddit (candidato) | Tipo | Vetar: ¿IA? ¿OC? ¿Flair? ¿Karma? |
|---|---|---|
| r/unstable_diffusion | AI NSFW grande | ¿exige flair AI? ¿karma? |
| r/aiNudes | AI NSFW | ¿OC propio? |
| r/aiporn | AI NSFW | ¿flair? |
| r/sdnsfw | Stable Diffusion NSFW | ¿solo SD? |
| r/Sexyaiart | AI art sensual | ¿nivel de explicitud? |
| r/BimboFication | Fetish bimbo | ¿acepta IA? ¿flair? |
| r/dollification | Fetish muñeca | ¿acepta IA/OC? |

**📖 Carril RELATOS → cuenta `u/LaVouteDAnais` (español — text/self-post):**

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
