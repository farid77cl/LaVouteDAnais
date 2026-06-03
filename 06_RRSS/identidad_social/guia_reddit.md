# 👽 Guía Reddit — el motor de alcance de Ele ("que te vean")

> **Por qué Reddit es EL motor:** es descubrimiento puro. Posteas en un sub grande y miles de desconocidos te ven **hoy**, sin necesidad de que te sigan (al revés de Bluesky). Para el objetivo de la Ama —"que todos la vean"— Reddit es la prioridad #1.
>
> **Estado:** 🔴 cuenta pendiente · conector `publicar_reddit.py` ✅ listo (espera credenciales).

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

### Categorías candidatas a investigar (verificar reglas — NO confirmadas)
- Comunidades de **AI art NSFW / unstable-diffusion-style** (las que aceptan IA explícita).
- Comunidades de **fetish / latex / pinup** que acepten arte IA con flair.
- **Subs propios de nicho** (dollification, bimbo) si permiten OC.

> Anotá 3-5 subs vetados acá abajo con sus reglas, y los ponemos en la cola.

| Subreddit | Permite IA | NSFW/OC | Karma mín. | Flair | Notas |
|---|---|---|---|---|---|
| _(por llenar)_ | | | | | |

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
