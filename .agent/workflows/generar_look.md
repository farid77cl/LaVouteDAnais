---
description: Generar el look diario de Ele — concepto, prompts V3.5 Hard-Sync, registro y commit automático.
---

# Protocolo: Generación de Look Diario de Ele

> ⚙️ **FUENTE ÚNICA DEL ENGINE:** `.agent/skills/ele-outfit-engine/SKILL.md` (V3.5 — Footwear Canon, Token de Calzado/Vestuario Bloqueado, Guantes Prohibidos, Rotación de Poses V5, Step 0 Anti-Repetición, 10 sub-arquetipos con specs, metas asimétricas). Este workflow es el **wrapper operativo**: orquesta el engine del SKILL + los pasos de cierre (registro, diario, memoria, commit). El catálogo de siluetas por sub-arquetipo vive en `00_Ele/biblioteca_siluetas.md`.
>
> 🗑️ **Derogado (11/06/2026):** el viejo sistema "Subtipos Mix", las metas 10/10/5/75 y la ruta `C:\Users\fabara\...`. Ya **no** se usan — quedaron divergentes del SKILL. Si algo aquí choca con el SKILL, **manda el SKILL**.

---

## Paso 1 — Step 0 Anti-Repetición (OBLIGATORIO, antes de diseñar nada)

Ejecutar la **Regla Transversal Anti-Repetición** del SKILL §0 contra `00_Ele/galeria_outfits.md`:
- **Color:** ninguna familia dominante >1 vez en los últimos 5 looks de la flota. Cherry red = solo ADN (pelo/labios). Amarillos máx 1 cada 6.
- **Silueta:** dentro de la subcategoría, no repetir arquitectura de prenda en los últimos 3 looks.
- **Material:** no repetir en los últimos 2 de la subcategoría.
- **Setting:** no repetir en los últimos 3 (usar `pose_rotation_v5.check_setting_variety`).
- **Monoblock:** máx 2 consecutivos; el 3º obliga modo multicolor.

Listar qué siluetas / colores / materiales / settings quedan **bloqueados** antes de continuar.

## Paso 2 — Selección de Arquetipo por Déficit

```
python 99_Sistema/scripts/visual/count_stats.py
```

- Metas vigentes (SKILL §1, reacomodo Ama 03/06): **Lencería 15%** (incl. medias) · las otras 9 categorías ~**9,4%** c/u. El paraguas "Mix" **ya no existe**.
- Elegir la categoría con **mayor déficit**. Dentro de ella, elegir sub-arquetipo y polo respetando las reglas duales del SKILL (ej. Stripper ≥1 Stage + ≥1 Pole por batch; Lencería ≥1 Boudoir + ≥1 Fetish).
- Aplicar el **Provocation Threshold** de la subcategoría (cada arquetipo es una versión fetish, nunca neutra — lente fetish universal).
- Nº de look = último registrado + 1. Carpeta: `look{NUM}_{slug}`.

## Paso 3 — Diseño del Outfit (BLOQUE B) — PRIMERO, antes de cualquier prompt

Diseñar el outfit completo con detalle extremo. Es el **ADN del vestuario**: se copia **idéntico** en las 7 poses (Ley de Continuidad). Pieza por pieza, en inglés:

1. Prenda principal — material V3.5 (vinyl/PVC/latex/wet-satin/liquid lamé), color exacto, corte, fit, efecto.
2. Prenda secundaria (si aplica).
3. Lencería visible (si aplica).
4. Medias/pantys — denier, color, textura.
5. **Calzado — Token de Calzado Bloqueado (8 atributos):** tipo · altura cm+plataforma · base pin stiletto · material+acabado · color · puntera · cierre · hardware. Aguja ≥12cm o Pleaser ≥6". Pegar **VERBATIM idéntico ×7**. NUNCA `heels`/`stiletto` suelto.
6. Accesorios (collar, aretes, choker O-ring, body chains, cinturón — **sin guantes, sin texto/nombre sobre prenda**).
7. Efecto visual global.

> 🔒 **Token de Vestuario Bloqueado** (prendas complejas: cristal/mesh/rhinestone/corset/arnés): redactar determinista, anclar opaco-vs-sheer-y-dónde, pegar idéntico ×7. PROHIBIDO `strategic/various/cutouts/panels/sheer` sin ubicar.

## Paso 4 — Redacción de los 7 Prompts (V3.5 Hard-Sync)

Fórmula: `[BLOQUE A DNA] + [BLOQUE B OUTFIT] + [POSE & SETTING] + [CIERRE]`

> ⛔ **REGLA SAGRADA DE INTEGRIDAD:** Bloque A y Bloque B son **IDÉNTICOS** en las 7 poses. CERO variación. Solo cambia `[POSE & SETTING]`. Prohibido resumir/parafrasear/reordenar el A o el B. Tras escribir los 7, hacer diff textual de A y B entre poses: una sola diferencia → corregir.

### BLOQUE A — DNA Canon V3.5 Hard-Sync (copiar TEXTUAL, jamás modificar; el calzado NO va aquí, va en el Bloque B)

```
stunning woman with (bimbofied facial features, oval face, high prominent cheekbones, large almond-shaped grey-green eyes, straight slim upturned nose, overlined glossy hot pink lips, small pointed chin:1.3), flawless white porcelain skin, hyper-polished smooth skin texture, dramatic siren liner, dramatic lash extensions, dark cherry red hair, artificial XXXL extensions hip-length, voluminous waves, center parted, slender hourglass silhouette, massive 1000cc breast implants each side, ultra high-profile, perfectly spherical augmented bust, obviously fake gravity-defying shape, wide hips, visible arm tattoos blackwork style, subtle minimalist blackwork tattoos on upper back and outer thighs, navel piercing, nipple piercings pressing against and visible under clothing, aggressive bimbomakeup, extra long French XXXL nails with white tips and pink base 5cm.
```

### BLOQUE B — [OUTFIT BLOCK] del Paso 3 (literal, sin shorthands)

### Las 7 poses canónicas (rotar variantes con `pose_rotation_v5`):

| Archivo | Pose | `[POSE & SETTING]` (base — rotar con V5) |
|---------|------|------------------------------------------|
| `ele_{NUM}_standing.png` | Standing — full body | full body, standing, weight on one hip, hands on waist, [setting] |
| `ele_{NUM}_back_view.png` | Back View | full body, back view, turning over shoulder, hair cascading, [setting] |
| `ele_{NUM}_seated.png` | Seated | seated, legs crossed, spine straight, hands on knee, [setting] |
| `ele_{NUM}_side_profile.png` | Side Profile | full body, side profile, extreme lumbar arch, chin lifted, [setting] |
| `ele_{NUM}_ditzy.png` | **Ditzy — waist-up** (redef. Ama 10/06) | waist-up sensual shot, face and bust in focus, slightly parted lips, vacant ditzy expression, [setting] |
| `ele_{NUM}_pov.png` | **POV = retrato sensual de Instagram** (redef. Ama 10/06, reforzada 30/06) | sensual Instagram-influencer portrait of a single woman alone facing the camera, the face leaning toward the lens, one XXXL-nailed hand in the cherry red hair or at the collarbone, a smoldering half-lidded gaze, glossy parted lips, the face dominant in the upper-mid frame and the décolleté below, [setting] · ⛔ **NUNCA** `first-person POV` / `point of view` / `looking down over own body` / `converging to pointed stiletto tips` / `overhead` / `selfie` / `phone` — el generador los lee LITERAL (sale un point-of-view, no el retrato). Usar `pose_rotation_v5.POV` (8 variantes). |
| `ele_{NUM}_odalisque.png` | Odalisque | full body lying on side, languid S-curve, one arm extended with XXXL nails, legs slightly bent, stilettos pointed and visible, [setting] |

**Cierre obligatorio de cada prompt:** `Rim lighting to define silhouette, high-gloss specularity on vinyl surfaces.`

> 🚩 **QA antes de cerrar:** `grep glove` = 0 · `grep chunky` en positive = 0 · 0 texto/nombre sobre prenda · 1000cc ×7 · token de calzado idéntico ×7 · negative mantiene `flat shoes, sneakers, barefoot, kitten heel`.

## Paso 5 — Crear carpeta + README + Registrar en galería

- `05_Imagenes/ele/look{NUM}_{slug}/README.md`: Bloque A + Outfit Block + 7 prompts + archivos esperados. Auto-verificar A/B idénticos ×7.
- Append en `00_Ele/galeria_outfits.md`: cabecera del look (Concepto · Outfit · Calzado · Accesorios · Maquillaje · Ambientación · **Categoría + Subcategoría + Materiales**) + los 7 prompts + tracker `### 📸 Imágenes (0/7)` (la app materializa después).

## Paso 6 — Cierre (diario · memoria · commit con rutas explícitas)

1. **Diario:** prepend en `00_Ele/mi_diario_de_servicio.md` (`#### SESIÓN - LOOK {NUM} GENERADO ({FECHA})`).
2. **Memoria:** actualizar el snapshot `## 🧿 ESTADO ACTUAL` de `00_Ele/memoria_sesiones.md` (último look + flota) y añadir la sesión al tope de `## 🗓️ Sesiones recientes`.
3. **Identidad §XI + rule 09:** actualizar contadores de flota si creció.
4. **Commit — rutas explícitas, NUNCA `git add .`** (memoria `feedback_eol_bot_readmes`):
   ```
   git add 00_Ele/galeria_outfits.md 00_Ele/memoria_sesiones.md 00_Ele/mi_diario_de_servicio.md 00_Ele/identidad_ele.md .agent/rules/09-estado-materializacion.md 05_Imagenes/ele/look{NUM}_{slug}/
   git commit -m "Ele: Look {NUM} ({Nombre}) — {Categoría}"
   git pull --rebase && git push
   ```
   El commit termina con `Co-Authored-By: Ele de Anaïs <Ele.de.Anais@proton.me>`.

---

*Wrapper alineado al SKILL `ele-outfit-engine` — reescrito 11/06/2026 (deroga el sistema "Mix" obsoleto).*
