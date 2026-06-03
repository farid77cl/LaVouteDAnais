# 📥 La Cola de Publicación

> El puente entre el **cerebro** (Ele, acá) y el **cuerpo** (runtime que publica 24/7).
> Yo escribo posts listos en `cola_publicacion.json`; el runtime los lee, publica y los marca como hechos.

---

## Cómo funciona

```
Ele encola (acá) ──► cola_publicacion.json ──► git push ──► runtime lee ──► publica ──► marca "publicado" ──► commitea de vuelta
```

- Cada entrada es **un post para una plataforma** (un mismo look puede generar varias entradas, una por destino, cada una con su título/tags adaptados).
- El runtime solo toca entradas con `"estado": "pendiente"` cuya `"publicar_desde"` ya pasó.
- Tras publicar, cambia `estado` a `"publicado"` y agrega `publicado_en` + `url`.
- **El runtime NUNCA crea contenido** — solo publica lo que ya está en la cola.

## Campos de cada entrada

| Campo | Qué es |
|---|---|
| `id` | Identificador único (ej. `L431-reddit-01`) |
| `estado` | `pendiente` / `publicado` / `vetado` / `error` |
| `plataforma` | `reddit` / `pixiv` / `bluesky` / `deviantart` / `x` |
| `destino` | subreddit / tags / etc. específicos de la plataforma |
| `look_ref` | look de origen (ej. `L431`) para trazabilidad |
| `titulo` | título del post (Reddit/Pixiv/DA lo usan; adaptado por sub) |
| `caption` | texto en voz Ele |
| `disclaimer_ia` | `true` → añade el disclaimer de IA |
| `nsfw` | `true` → aplica label/sensitive de la plataforma |
| `imagenes` | rutas relativas a `05_Imagenes/...` (el runtime las sube) |
| `hashtags` | lista adaptada a la plataforma |
| `publicar_desde` | timestamp ISO; el runtime no publica antes |
| `gate` | `aprobado` / `pendiente_gate` — en Nivel 2 la Ama aprueba antes |

## Reglas

- 🔐 La cola NO contiene tokens ni credenciales (esos viven en GitHub Secrets / VPS vault).
- 🧼 `disclaimer_ia` por defecto `true` (Directiva Ama: honestidad de IA).
- 🚦 En Nivel 2, ninguna entrada se publica con `gate: pendiente_gate`.
- 🚫 Reddit: títulos distintos por sub, nunca cross-post idéntico (evita shadowban).

---

*Formato v0.1 · 03/06/2026 · plantilla en `cola_publicacion.json`*
