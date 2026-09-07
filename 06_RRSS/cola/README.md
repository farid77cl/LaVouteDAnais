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
| `plataforma` | `reddit` / `pixiv` / `bluesky` / `deviantart` / `x` / **`tumblr`** |
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

### Campos que agrega Tumblr (07/09/2026)

Tumblr entró como **destino de relatos**, no de imágenes (D9: *el relato completo vive en
Tumblr*), y eso rompe dos supuestos que la cola traía desde junio.

| Campo | Qué es |
|---|---|
| `cuerpo_ref` | **Ruta al `_tumblr.md`**, no el texto. Un capítulo son 10.000-14.000 palabras: meterlo dentro del JSON convierte la cola en un archivo ilegible y hace que cualquier `git diff` sea inservible. El runtime lee el archivo y publica su contenido |
| `relato_ref` | slug del relato (el equivalente de `look_ref` para literatura) |
| `capitulo` | número de capítulo — decide la navegación entre posts |

> ⚠️ **`caption` dice «texto en voz Ele» y para Tumblr eso NO aplica.** El blog lleva la cara
> y el nombre de Anaïs, así que **hacia afuera habla ella** (Ama 07/09/2026: *"debes responder
> como si fueras anais"*). En una entrada de Tumblr, `caption` va en voz de Anaïs. Regla
> completa: `.agent/rules/00-contexto-obligatorio.md` §La voz, Excepción 2.

> 🏷️ **`destino` de Tumblr** lleva `{"blog": "lavoutedeanais", "content_label": "mature"}`.
> Etiquetar el contenido maduro **es obligatorio** en Tumblr, no opcional.

> 🗝️ **Dos llaves, no una.** Para un capítulo, `gate: aprobado` exige las dos: el **Gate de la
> Ama sobre ese capítulo** (Regla de Oro 8c — archivo, nunca inferencia) **y** su okey de
> publicación post por post. Un capítulo aprobado no es un post autorizado.

## Reglas

- 🔐 La cola NO contiene tokens ni credenciales (esos viven en GitHub Secrets / VPS vault).
- 🧼 `disclaimer_ia` por defecto `true` (Directiva Ama: honestidad de IA).
- 🚦 En Nivel 2, ninguna entrada se publica con `gate: pendiente_gate`.
- 🚫 Reddit: títulos distintos por sub, nunca cross-post idéntico (evita shadowban).

---

*Formato v0.2 · 03/06/2026, ampliado 07/09/2026 con Tumblr · plantilla en `cola_publicacion.json`*
