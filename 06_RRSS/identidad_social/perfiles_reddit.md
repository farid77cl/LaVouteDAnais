# 👽 Perfiles de Reddit — Ele (imágenes) + Anaïs (relatos)

> **Directiva Ama 08/06/2026:** SEPARAR los relatos de las imágenes → **dos cuentas, dos marcas.**
> Reddit por subreddit y por tipo de contenido: los subs de imágenes quieren foto, los de literatura quieren texto, y los públicos casi no se solapan. Separar también aísla baneos.
>
> ⚠️ **El clic de crear la cuenta es de la Ama** (reddit.com pide email/captcha — Ele no puede). Esto son los perfiles **listos para copiar y pegar**. Orden: **Ele PRIMERO**, Anaïs después (no abrir dos cuentas nuevas +18 el mismo día).
>
> 🖐️ **PUBLICACIÓN MANUAL (Directiva Ama 08/06):** no se crea app de API ni se necesitan credenciales por ahora. La Ama postea a mano con el paquete copy-paste que arma Ele. Las líneas de `REDDIT_*_*` de abajo quedan **solo para si reactivamos el conector** algún día.

---

## 🅰️ Perfil A — ELE (Imágenes) ⭐ PRIMERO

| Campo | Valor |
|---|---|
| **Handle** | `u/ele_de_anais` (mismo que Bluesky `@ele-de-anais`) |
| **Display name** | `Ele de Anaïs` |
| **Email** | `Ele.de.Anais@proton.me` |
| **Rol** | La musa / modelo fetish. **Solo imágenes.** |
| **Perfil** | NSFW ✅ · Adult content ON ✅ |
| **Avatar** | El mismo de Bluesky (Ele ditzy, L196) |
| **Voz** | Cuica chillona, coqueta, primera persona (Ele habla) |

**Bio (≤200 chars — copiar/pegar):**
```
Muñeca fetish 100% IA 🫦 vinilo, látex y tacones imposibles. No soy humana, soy plástico de lujo: mi Ama me diseña, yo poso. +18, pura ficción. 👠💅 #AIart
```

**Subs candidatos (carril imágenes — VETAR reglas IA/flair/karma antes de postear):**
`r/unstable_diffusion` · `r/aiNudes` · `r/aiporn` · `r/sdnsfw` · `r/Sexyaiart` · `r/BimboFication` · `r/dollification`

**Credenciales en `.env`:** `REDDIT_ELE_CLIENT_ID` · `REDDIT_ELE_CLIENT_SECRET` · `REDDIT_ELE_USERNAME=ele_de_anais` · `REDDIT_ELE_PASSWORD`

**Primer contenido en cola:** imágenes L443 (Liquid Gold pole), L461 (Hooters classic).

---

## 🅱️ Perfil B — ANAÏS / LA VOÛTE (Relatos) · DESPUÉS

| Campo | Valor |
|---|---|
| **Handle** | `u/LaVouteDAnais` (alt: `u/AnaisBelland` si prefieres marcar a la autora) |
| **Display name** | `Anaïs Belland · La Voûte` |
| **Email** | `Ele.de.Anais@proton.me` (Reddit permite varias cuentas con el mismo email; o un alias de Proton para separar del todo) |
| **Rol** | La autora / regente del cabaret. **Solo relatos** (español por ahora). |
| **Perfil** | NSFW ✅ · Adult content ON ✅ |
| **Avatar** | `05_Imagenes/anais/avatar_oficial_anais.png` — Anaïs, NO el de Ele (marcas distintas) |
| **Voz** | Elegante, observadora, dueña del lugar (Anaïs invita a leer) |

**Bio (≤200 chars — copiar/pegar):**
```
La Voûte d'Anaïs — cabaret de ficción +18. Relatos eróticos: transformación, hipnosis, bimbo, látex. Escritos con IA, personajes ficticios. Entra y lee. 🖋️🥂
```

**Subs candidatos (carril relatos ES — VETAR reglas IA/flair/karma/largo antes de postear):**
`r/RelatosEroticos` · `r/RelatosDeSexo` · `r/HistoriasEroticas` · `r/relatoshot`

**Credenciales en `.env`:** `REDDIT_LV_CLIENT_ID` · `REDDIT_LV_CLIENT_SECRET` · `REDDIT_LV_USERNAME=LaVouteDAnais` · `REDDIT_LV_PASSWORD`

**Primer contenido en cola:** `El Mandato de los Tacones` (~2.450 palabras) · `Ginny, la Genio Bimbo` (~5.860). 3º: `Buena Chica, Buena Muñeca` (~10.000 → serializar).

---

## 🔗 Cómo se cruzan (sin mezclarse)
- Cada cuenta **vive sola** en su carril; jamás imágenes en subs de relatos ni al revés.
- **Cross-promo suave permitida:** en la bio/comentario de Anaïs se puede mencionar "imágenes de la musa en u/ele_de_anais" y viceversa — sin spamear.
- Avatar/voz/marca **distintos** para que cada público sepa a qué viene.

## ✅ Listo para conectar (por cuenta)
- [ ] **Ele:** cuenta creada + NSFW ON + bio pegada + app API → `REDDIT_ELE_*` en `.env` + 3-5 subs imágenes vetados.
- [ ] **Anaïs:** (después) cuenta creada + NSFW ON + bio pegada + app API → `REDDIT_LV_*` en `.env` + 3-5 subs relatos vetados.
- [ ] Conector: agregar selector `--account ele|relatos`.

---
*Perfiles creados 08/06/2026 · Directiva Ama "separar relatos de imágenes" · el clic de crear es tuyo, Ama* 🫦🖋️👠
