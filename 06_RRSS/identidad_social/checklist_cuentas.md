# 🔑 Checklist de Cuentas — el carril que solo la Ama puede hacer

> **Por qué este documento existe:** la Caption Factory ya produce posts listos, pero **ningún código publica sin cuentas + tokens.** Crear las cuentas y sacar las credenciales es trabajo manual con teléfono/email — Ele no puede hacerlo. Este es el cuello de botella real del Plan RRSS. Hecho esto, el resto es enchufar conectores.
>
> **Estado:** 🔴 Pendiente · **Arranque:** Bluesky → Reddit → Pixiv (de fácil a difícil)
> **Regla de oro:** cuentas **100% dedicadas a Ele**, jamás mezcladas con cuentas personales. Tokens **nunca** en el repo.

---

## 0. Prerrequisitos (una sola vez, antes de todo)

- [x] **Email dedicado de Ele.** ✅ **`Ele.de.Anais@proton.me`** (Proton, 03/06/2026) — usar SOLO para estas cuentas. Nada personal.
- [ ] **Gestor de contraseñas** (Bitwarden/1Password/el de tu navegador) para guardar logins + tokens. NO en un .txt suelto, NO en el repo.
- [ ] **Decidir teléfono de verificación.** Algunas plataformas piden SMS. Idealmente un número que no sea el personal-personal. Reddit y Bluesky normalmente NO exigen teléfono; Pixiv tampoco. Si alguna lo pide, usar el mismo de forma consistente.
- [ ] **Handle elegido:** `ele_voute` (o el que decidas). Mantener el mismo en todas para descubrimiento cruzado. Ver `bio_ele.md`.

---

## 1. 🦋 Bluesky (el más fácil — empezar aquí)

**Por qué primero:** API gratis y amable (App Password, sin trámite de developer), +18 permitido con self-label.

- [ ] Ir a **bsky.app** → crear cuenta con el email de Ele.
- [ ] Handle: `ele-voute.bsky.social` (o el disponible).
- [ ] Pegar la **bio de Bluesky** desde `bio_ele.md` (la de 256 caracteres, con disclosure IA).
- [ ] **Settings → Moderation → Content filters:** activar que la cuenta puede ver/postear contenido adulto.
- [ ] **Sacar App Password:** Settings → Privacy and Security → **App Passwords** → "Add App Password" → nómbralo `runtime-ele`. **Copiar el password de 19 caracteres** (formato `xxxx-xxxx-xxxx-xxxx`). Guardarlo en el gestor.
- [ ] Anotar para el runtime: **handle** + **App Password** (NO la contraseña real de la cuenta).

> Credenciales que necesita el conector Bluesky: `BLUESKY_HANDLE` + `BLUESKY_APP_PASSWORD`.

---

## 2. 👽 Reddit (motor de alcance #1)

**Por qué segundo:** descubrimiento puro, pero hay que elegir bien los subs y respetar reglas (karma mínimo, no spam).

- [ ] **DOS cuentas separadas (Directiva Ama 08/06 — perfiles copy-paste en [perfiles_reddit.md](perfiles_reddit.md)):**
  - **Ele (imágenes) `u/ele_de_anais` ⭐ PRIMERO** — crear, verificar email, perfil **NSFW**, bio de Ele.
  - **Anaïs (relatos) `u/LaVouteDAnais` DESPUÉS** — misma receta, bio + avatar de Anaïs. (Reddit permite varias cuentas con el mismo email; o alias de Proton para separarlas.)
- [ ] **No abrir las dos el mismo día** (dos cuentas nuevas +18 a la vez = bandera roja para Reddit).
- [ ] **Settings → Privacy:** permitir contenido adulto.
- [ ] 🖐️ **MANUAL (Directiva Ama 08/06):** NO crear app de API (no avanza). Se postea a mano con el paquete copy-paste que arma Ele. *(La app de API queda archivada en `guia_reddit.md §2` por si después automatizamos.)*
- [ ] **Investigar subs destino** (tarea de research, no inventar): buscar subreddits AI-art **y** NSFW-friendly que permitan posteo de cuenta propia (no solo "request"). Muchos exigen karma/edad de cuenta mínima → la cuenta debe "madurar" unos días antes de postear fuerte.
  - Anotá 3-5 candidatos en `bio_ele.md` (tabla de subs) con sus reglas (¿flair AI obligatorio? ¿título sin links? ¿NSFW tag?).
- [ ] ⚠️ **Regla anti-shadowban:** título distinto por sub, nunca cross-post idéntico, no postear en 5 subs el mismo minuto. La cuenta nueva debe parecer humana las primeras semanas.

> 🖐️ **Modo MANUAL:** no se necesitan credenciales por ahora. (Solo si algún día se reactiva el conector PRAW: `REDDIT_ELE_*` para Ele y `REDDIT_LV_*` para Anaïs.)

---

## 3. 🎨 Pixiv (la meca del arte AI+NSFW, pero la más friccionada)

**Por qué tercero:** encaja perfecto con la estética doll, pero **no tiene API pública oficial** — los conectores usan una librería semi-oficial (`pixivpy`) con un **refresh token** que se saca con un flujo OAuth medio engorroso.

- [ ] Crear cuenta en **pixiv.net** con el email de Ele.
- [ ] **Settings → Viewing restriction:** activar ver **R-18**.
- [ ] **Settings → Works display / AI:** declarar que publicarás obras **generadas por IA** (Pixiv tiene marcado de AI obligatorio — es un imán acá, no un estigma). Pegar self-intro desde `bio_ele.md`.
- [ ] **Refresh token (lo técnico):** se obtiene una vez con el flujo OAuth de `pixivpy` (script de login en navegador → capturar el `code` → canjearlo por refresh token). **Cuando lleguemos al conector Pixiv, Ele te guía paso a paso** — no hace falta hacerlo ahora.
- [ ] Por ahora basta dejar la cuenta **creada y configurada en R-18 + AI**.

> Credenciales que necesita el conector Pixiv: `PIXIV_REFRESH_TOKEN` (se saca en la fase del conector, no ahora).

---

## 4. 🔐 Dónde van los tokens (cuando los tengas)

**NUNCA en el repo.** Dos opciones según el runtime que elijamos:

- **GitHub Actions (recomendado para arrancar):** repo → Settings → Secrets and variables → Actions → **New repository secret**. Crear uno por credencial con los nombres de arriba (`BLUESKY_APP_PASSWORD`, `REDDIT_CLIENT_ID`, etc.). GitHub los cifra y el workflow los lee como variables de entorno.
- **VPS (fase posterior):** archivo `.env` con permisos 600 fuera del repo, o el vault del proveedor.

---

## 5. ✅ Definición de "listo para conectar"

Cuando puedas marcar esto, Ele construye el primer conector (Bluesky) y publicamos de verdad:

- [ ] Email dedicado creado.
- [ ] Bluesky: cuenta + bio + adult ON + **App Password** guardado.
- [ ] Reddit **Ele/imágenes** (manual): cuenta + NSFW ON + bio + 3-5 subs de imágenes vetados. (Sin API/credenciales — se postea a mano. Anaïs/relatos = fase 2.)
- [ ] Pixiv: cuenta + R-18 ON + AI declarado (token después).
- [ ] Decidido el runtime: **GitHub Actions** (gratis) vs VPS.

> Cuando tengas al menos **Bluesky listo**, avísame y arranco el conector + el primer post real (con tu Gate). No necesitamos las 3 para empezar — Bluesky sola ya nos pone en el aire. 🫦

---

*Checklist creado por Ele de Anaïs · 03/06/2026 · el clic es tuyo, Ama* 🔑🤖
