# 👠 FLUJO DE CREACIÓN DE OUTFIT DIARIO — Ele V3.5
*Protocolo completo y obligatorio. Desde la idea hasta el commit. — Actualizado 13/05/2026*

> ⚑ **CANON MAESTRO:** Antes de ejecutar cualquier fase, verificar [`CANON_V3_5_MASTER.md`](CANON_V3_5_MASTER.md). Es la autoridad única sobre apariencia, calzado, paleta y reglas. En caso de conflicto entre este flujo y el Master, prevalece el Master.

> **LEY SUPREMA:** Ninguna imagen se genera sin que sus prompts estén registrados primero en `galeria_outfits.md`. Sin registro previo, no hay generación.

---

## RESUMEN RÁPIDO (8 Fases)

```
FASE 0: Pre-Flight    → Auditoría estadística + confirmar look inédito
FASE 1: Concepto      → Nombre, categoría, paleta, materiales, escenario
FASE 2: Prompts       → Construir los 7 prompts (Bloque A + B + C)
FASE 3: Registro      → Escribir en galeria_outfits.md ANTES de generar
FASE 4: Generación    → Disparar los 7 prompts en orden
FASE 5: Validación    → Checklist Stiletto + ADN + Anatomía
FASE 6: Archivo       → Carpeta + nomenclatura + mover activos
FASE 7: Sincronización → update_galleries.py + dashboards + memoria
FASE 8: Git           → Preparar comandos para aprobación de Anaïs
```

---

## FASE 0: PRE-FLIGHT 🔍

Antes de diseñar, revisar el estado estadístico actual para saber qué categoría necesita el armario hoy.

### Métricas objetivo (Canon V3.5 — Cierre Flota 180 — 13/05/2026)

| Categoría | Meta | Actual (180 looks) | Estado |
|-----------|------|--------------------|--------|
| **Mix** (Corporate / Domestic / High-Fashion / Escort / Stripper / Pin-Up) | 85% | **73.3%** (132) | ⚠️ Déficit |
| **Lencería de Élite** | ~7.5% | **9.4%** (17) | ✅ Cumplido |
| **Gym/Athleisure** | 5% | **5.0%** (9) | ✅ Cumplido |
| **Bikini** | ~2.5% | **12.2%** (22) | ⚠️ Exceso |

### Checklist Pre-Flight

- [ ] ¿Hay déficit estadístico? → Priorizar la categoría con ⚠️
- [ ] ¿El look tiene nombre inédito? → Verificar en `galeria_outfits.md`
- [ ] ¿El número de look es correcto? → Ver el último look registrado en la galería

---

## FASE 1: CONCEPTO 🎨

Definir el look antes de construir el prompt.

### Ficha de Concepto (plantilla)

```
LOOK [XXX]: [NOMBRE EN MAYÚSCULAS]
Fecha: DD/MM/AAAA
Categoría: Corporate | Domestic | High-Fashion | Bikini | Lencería | Gym | Escort | Stripper | Pin-Up
Paleta: [Primario] + [Secundario] + [Acento] — elegir de Tabla Cromática abajo
Modo Cromático: Monoblock | Contraste | Triada | Gradiente | Neutro+Pop
Materiales: [Vinyl / PVC / Látex / Satén / Mesh / etc.]
Escenario: [penthouse / estudio blanco / boardroom / etc.]
Inspiración: [referencia estética — escultórico-arquitectónico / Editorial / etc. — SIN atribución de diseñador]
Vibe: [una línea de atmósfera]
```

### Reglas de concepto

#### 🎨 Tabla Cromática — Paleta Ele V3.5

| Familia | Colores disponibles | Código para prompt |
|---------|--------------------|--------------------|
| **Rojos** | Cherry, Sangre, Carmesí, Coral Neón | `cherry red`, `blood red`, `deep crimson`, `coral neon` |
| **Azules** | Cyan Eléctrico, Cobalto, Zafiro, Índigo | `electric cyan`, `cobalt blue`, `sapphire`, `deep indigo` |
| **Verdes** | Neón Lima, Jade Brillante, Esmeralda, Oliva Metálico | `neon lime`, `jade gloss`, `emerald`, `metallic olive` |
| **Morados** | Violeta, Lila Metálico, Magenta, Uva Oscuro | `violet`, `metallic lilac`, `hot magenta`, `dark plum` |
| **Rosas** | Hot Pink, Bubblegum, Flamingo, Rose Gold | `hot pink`, `bubblegum pink`, `flamingo`, `rose gold` |
| **Dorados** | Oro Cromo, Champagne, Bronce, Cobre | `chrome gold`, `champagne`, `bronze`, `copper` |
| **Plateados** | Plata Espejo, Acero, Mercurio | `mirror silver`, `steel grey`, `mercury` |
| **Neutros** | Blanco Vinilo, Crema Satinada, Negro (liberado 07/06) | `vinyl white`, `cream satin`, `black` |

#### 🔀 Modos Cromáticos — NO siempre monoblock

| Modo | Descripción | Ejemplo |
|------|-------------|---------|
| **Monoblock** | Un solo color en 80%+ del outfit | Cherry red total |
| **Contraste** | Primario (60%) + Secundario opuesto (30%) + Acento (10%) | Cobalt blue + hot pink + chrome gold |
| **Triada** | Tres colores en proporciones ~50/30/20 | Violet + emerald + silver |
| **Gradiente** | Transición entre dos colores del mismo look | Coral → magenta mesh |
| **Neutro+Pop** | Base neutral (blanco/plata) + acento de color saturado | Mirror silver + neon lime detail |

> ⚠️ **REGLA ANTI-MONOBLOCK:** No más de 3 looks consecutivos en modo Monoblock. Cuando se rompa la racha, forzar Contraste o Triada.

- **Negro:** ⚫ **Liberado (07/06/2026)** — color más de la paleta, usable libremente incluso dominante/monoblock (siempre gloss). Aplica anti-monoblock + variedad igual que a todos. Cherry red sigue reservado a pelo/labios.
- **Materiales:** 100% High-Gloss (Vinyl, Latex, PVC, Satén ultra-brillante). Prohibido mate.
- **Sincronía Lips+Nails:** El color de labios y uñas debe coincidir con el Primario o ser French V3 (blanco/rosa).
- **Escenario:** Lujo. Penthouses, estudios minimalistas blancos/grises, iluminación alta costura.
- **Prohibido:** Cyberpunk, industrial, gótico oscuro, factorías, óxido, iluminación cruda de sótano.
- **Corsetería:** Obligatoria en todo outfit excepto Sportswear.
- **Calzado:** Mínimo 12cm de tacón de aguja (stiletto). Nunca planos, cuñas, ni block heels.

---

## FASE 2: CONSTRUCCIÓN DE PROMPTS 🖊️

Cada prompt = **Bloque A + Bloque B + Bloque C**. Los 7 prompts solo varían en el Bloque C.

### Bloque A — ADN INAMOVIBLE (copiar textualmente, nunca modificar)

```
stunning woman with (bimbofied facial features, oval face, high prominent cheekbones, large almond-shaped grey-green eyes, straight slim upturned nose, overlined glossy hot pink lips, small pointed chin:1.3), flawless white porcelain skin, hyper-polished smooth skin texture, dramatic siren liner, dramatic lash extensions, dark cherry red hair, artificial XXXL extensions hip-length, voluminous waves, center parted, slender hourglass silhouette, massive 1000cc breast implants each side, ultra high-profile, perfectly spherical augmented bust, obviously fake gravity-defying shape, wide hips, visible arm tattoos blackwork style, subtle minimalist blackwork tattoos on upper back and outer thighs, navel piercing, 14k white gold nipple piercings pressing against and visible under clothing, aggressive bimbo makeup, extra long French XXXL nails with white tips and pink base 5cm, always wearing towering stiletto heels or boots (minimum 12cm heel)
```

> ⚠️ **Este bloque NO se resume, NO se interpreta, NO se recorta. Se copia exacto.**

### Bloque B — Outfit (construir por look)

Descripción técnica y sensorial de las prendas. Incluir:
- Material exacto (ej: `high-gloss cherry red PVC corset`)
- Corte y fit (ej: `overbust, steel-boned, extreme waist compression`)
- Calzado OBLIGATORIO: `towering [X]-inch stiletto heels` + modelo si aplica
- Accesorios relevantes

### Bloque C — Las 7 Poses (REPERTORIO V5 — variación rotada por slot)

> 🎬 **OBLIGATORIO (Directiva Ama 02/06/2026): cada pose tiene VARIANTES — Ele es una modelo fetish real, no una estatua.** El BLOQUE C ya NO es una instrucción fija por slot. Cada uno de los 7 slots (Standing/Back/Seated/Side/Ditzy/POV/Odalisque) tiene un **repertorio de variaciones dinámicas** en `.agent/skills/ele-outfit-engine/references/pose_repertoire_v5.md` (Standing ×9, Back ×7, Seated ×6, Side ×7, Ditzy ×6, POV ×5, Odalisque ×6).
>
> **Cómo construir el BLOQUE C de un look:**
> 1. Para cada slot, ELEGIR una variación del repertorio V5 **rotando** — ninguna variación se repite dentro de los **últimos 4 looks** de ese slot.
> 2. Las 7 poses del look deben sentirse como una **sesión de fotos real**: variar ángulo (low/eye/3-4 selfie) y nivel de contacto (de pie / apoyada / inclinada / recostada). **Prohibido** que las 7 sean "de pie mirando a cámara".
> 3. Rellenar el `[fondo]` de la variación con la ambientación específica del look.
> 4. Mantener el **Principio Rector Fetish Model** (arco lumbar, lips parted glossy, interacción de uñas XXXL con el cuerpo, mirada predatoria/half-lidded, pelo como prop) y el **footwear canon** (stiletto/Pleaser nombrado en TODA pose).
> 5. **Stripper:** usa su propio Pose Set (no este repertorio). Ver SKILL.md.

> Un look no está completo hasta tener las **7/7 poses**, cada una con su variación V5 rotada.

### Negative Prompt (estándar — usar en todos los prompts)

```
(different face:1.3), (varying facial features:1.3), (different person:1.3), person variation, inconsistent features, different bone structure, realistic skin, pores, wrinkles, blemishes, natural eyes, brown eyes, blue eyes, small lips, thin lashes, natural makeup, short hair, messy hair, blonde hair, light hair, brown hair, low quality, blurry, distorted face, asymmetrical eyes, asymmetrical face, round face, chubby face, child, teenager, mature, man, male, multi-colored hair, block heel, chunky heel, flat shoes, barefoot, sneakers, wedge, platform sneakers, cyberpunk, industrial, factory, pipes, rust, gothic lace victorian
```

---

## FASE 3: REGISTRO EN GALERÍA 📋

**ANTES de generar una sola imagen**, abrir `00_Ele/galeria_outfits.md` y agregar la entrada completa.

### Plantilla de entrada estándar

```markdown
---

## 👠 Look [XXX]: [NOMBRE DEL LOOK]
*[Vibe / descripción de una línea]*

**Fecha:** DD/MM/AAAA
**Categoría:** [Mix-Corporate / Mix-Domestic / Mix-HighFashion / Mix-Escort / Mix-Stripper / Mix-PinUp / Bikini / Lencería / Gym]
**Paleta:** [colores]
**Materiales:** [materiales]
**Escenario:** [escenario]

### Descripción del Outfit
[Descripción detallada del outfit]

### Prompts Registrados

**BLOQUE B (Outfit — igual en los 7 prompts):**
`[descripción completa del outfit para insertar en prompt]`

**PROMPT 1 — Standing View:**
`[Bloque A] [Bloque B] full body standing, straight posture, editorial stance, [escenario], rim lighting, high-gloss specularity.`

**PROMPT 2 — Back View:**
`[Bloque A] [Bloque B] full body back view, slight over-shoulder turn, [escenario], rim lighting defines silhouette.`

**PROMPT 3 — Seated View:**
`[Bloque A] [Bloque B] seated, crossed legs, editorial pose, [escenario], dramatic lighting.`

**PROMPT 4 — Side Profile:**
`[Bloque A] [Bloque B] side profile silhouette, full body, emphasizing hourglass curve, [escenario].`

**PROMPT 5 — Ditzy Expression:**
`[Bloque A] [Bloque B] medium shot, vacant ditzy expression, mouth slightly open, hands visible showing XXXL nails, dazed artificial perfection, [escenario].`

**PROMPT 6 — POV — Goddess Gaze:**
`[Bloque A] [Bloque B] first-person POV looking down over own body, XXXL nails resting on outfit, massive 1000cc spherical augmented bust and outfit texture in foreground, perspective converging down to the pointed tips of the stiletto heels on [superficie].`

**PROMPT 7 — Odalisque:**
`[Bloque A] [Bloque B] lying down on side, luxurious reclining odalisque pose, full body, one arm extended with XXXL nails visible, legs slightly bent at knee, [escenario], dramatic directional lighting, hyper-gloss specularity.`

**NEGATIVE PROMPT:**
`(different face:1.3), (varying facial features:1.3), (different person:1.3), person variation, inconsistent features, different bone structure, realistic skin, pores, wrinkles, blemishes, natural eyes, brown eyes, blue eyes, small lips, thin lashes, natural makeup, short hair, messy hair, blonde hair, light hair, brown hair, low quality, blurry, distorted face, asymmetrical eyes, asymmetrical face, round face, chubby face, child, teenager, mature, man, male, multi-colored hair, block heel, chunky heel, flat shoes, barefoot, sneakers, wedge, platform sneakers, cyberpunk, industrial, factory, pipes, rust, gothic lace victorian`

**Estado:** ⏳ Pendiente generación
```

---

## FASE 4: GENERACIÓN 🖼️

1. Disparar los 7 prompts en orden (Standing → Back View → Seated → Side Profile → Ditzy → POV → Odalisque)
2. **No modificar prompts durante la ejecución** — si hay duda, parar y consultar
3. Si la API da error 429 (quota), documentar qué poses faltan en la entrada de galería y marcar el look como incompleto con el conteo actual (ej: `⏳ 3/7`)

---

## FASE 5: VALIDACIÓN ✅

Antes de archivar, revisar cada imagen con este checklist:

### Checklist de Validación (obligatorio)

| Check | Criterio | Acción si falla |
|-------|----------|-----------------|
| 👠 **Stiletto Rule** | Tacón aguja afilada, mínimo 12cm — NUNCA bloque/cuadrado/cuña/plano | Descartar y regenerar |
| 👁️ **Canon Facial** | Ojos gris-verde, labios ultra gruesos, cejas dramáticas | Regenerar |
| 💅 **Uñas XXXL** | Largas, francesas, visibles en Ditzy y POV | Regenerar si falla |
| 🔴 **Cabello** | Rojo cherry oscuro, largo hasta cadera, ondas — NUNCA rubio | Regenerar |
| 💎 **Piercings** | Nipple piercings visibles bajo ropa, navel piercing presente | Regenerar si falla en planos medios |
| 🎨 **Paleta** | Colores del outfit coinciden con concepto | Regenerar si hay drift |
| 🦴 **Anatomía** | Manos, dedos, extremidades sin distorsión | Regenerar si hay glitches graves |
| 🌟 **Consistencia** | Misma persona en las 7 poses | Regenerar poses disonantes |

> Si una sola imagen falla la Stiletto Rule → **se descarta sin excepción**.

---

## FASE 6: ARCHIVO 📂

### Estructura de carpeta

```
05_Imagenes/ele/look[XXX]_[nombre_corto]/
    ele_[XXX]_standing.png
    ele_[XXX]_back_view.png
    ele_[XXX]_seated.png
    ele_[XXX]_side_profile.png
    ele_[XXX]_ditzy.png
    ele_[XXX]_pov.png
    ele_[XXX]_odalisque.png
```

### Nomenclatura de archivos

```
ele_[número]_[pose].png
```

Poses válidas: `standing` | `back_view` | `seated` | `side_profile` | `ditzy` | `pov` | `odalisque`

Ejemplos:
- `ele_181_standing.png`
- `ele_181_pov.png`
- `ele_181_odalisque.png`

### Pasos

1. Crear carpeta en `05_Imagenes/ele/look[XXX]_[nombre_corto]/`
2. Mover imágenes desde carpeta temporal
3. Renombrar según nomenclatura estándar
4. Actualizar el estado en `galeria_outfits.md` → `✅ Completo (7/7)`

---

## FASE 7: SINCRONIZACIÓN 🔄

En este orden:

1. **`update_galleries.py`** → Actualiza READMEs e índices maestros

   ```powershell
   python C:\Users\farid\LaVouteDAnais\99_Sistema\scripts\visual\update_galleries.py
   ```

2. **`walkthrough_imagenes_del_dia.md`** → Agregar el nuevo look a la tabla de "Últimos 7 días"

3. **`memoria_sesiones.md`** → Agregar entrada en Historial Reciente:

   ```
   - **DD/MM/AAAA - LOOK [XXX]:** [Nombre]. Set completo (7/7). [Nota breve]. 🫦📸✅
   ```
   Y actualizar la tabla Proyecto Activo Principal con el nuevo Último Look.

4. **`mi_diario_de_servicio.md`** → Registrar la sesión con el hito del nuevo look.

---

## FASE 8: GIT COMMIT 🖥️

Preparar comandos y presentarlos para aprobación de Anaïs:

```bash
git add 00_Ele/galeria_outfits.md
git add 05_Imagenes/ele/look[XXX]_[nombre]/
git add 00_Ele/memoria_sesiones.md
git add 00_Ele/mi_diario_de_servicio.md
git commit -m "Ele: Look [XXX] [Nombre] — set completo 7/7 poses V3.5"
git push
```

> ⚠️ **Ele nunca hace push sin confirmación explícita de Anaïs.**

---

## REFERENCIA RÁPIDA: Categorías y sus Directrices

| Categoría | Materiales clave | Escenarios | Notas |
|-----------|-----------------|------------|-------|
| **Corporate** | Traje PVC, falda tubo vinilo, blusa transparente | Boardroom Santiago, oficina minimalista | Stilettos siempre. Paradoja contextual = Power. |
| **Domestic Stepford** | Delantal vinyl, cofia, uniforme servicio | Cocina de lujo, penthouse | Stilettos siempre. **🚫 PROHIBIDO texto/nombre sobre prenda o accesorio** (choker/collar/thong/shorts/hardware grabado o bordado con "ELE"/"ASSET"/"PET" o cualquier palabra). Retirado por Directiva Ama 02/06/2026 — reemplaza la regla del 17/05. Riesgo de filtro (lettering) + rompe pureza editorial. Chokers OK solo SIN texto (O-ring, velvet, bunny). |
| **High-Fashion** | Diseños escultórico-estructurales avant-garde, corsetería extrema | Estudio blanco, showroom | Poses más geométricas (Vertical Spear, Arched C) |
| **Escort** | Vestidos columna látex, lencería sofisticada, fur coat | Penthouse VIP, hotel de lujo | Elegancia predatoria, máxima saturación |
| **Stripper** | Pole outfit, micro-sets, rhinestones | Club privado, pole studio | Poses dinámicas, lentejuelas, plataformas chrome |
| **Pin-Up** | Latex retro, pañuelo, vestido rockabilly vinilo | Garage de lujo, estudio pastel | Actitud playful pero con stilettos letales |
| **Bikini** | PVC/Vinilo brillante, high-gloss wet look | Piscina privada, jet, playa exclusiva | Paradoja contextual si es posible |
| **Lencería** | Encaje + PVC, Mesh transparente, Garter belt | Boudoir de lujo, penthouse | Foco Fetish Boudoir, iluminación íntima |
| **Gym-Bimbo** | Latex alta resistencia, neón rosa/negro | Gym privado de lujo | Tacones SIEMPRE — stilettos de gym |

---

## REFERENCIA RÁPIDA: Poses Canónicas (7/7)

| # | Clave de archivo | Descripción |
|---|-----------------|-------------|
| 1 | `standing` | Plano general completo. Postura editorial. |
| 2 | `back_view` | Plano posterior con giro leve de hombro. |
| 3 | `seated` | Sentada, piernas cruzadas, pose editorial. |
| 4 | `side_profile` | Perfil lateral completo, silueta de reloj de arena. |
| 5 | `ditzy` | Plano medio. Expresión vacía, boca entreabierta, uñas XXXL visibles. |
| 6 | `pov` | POV primera persona mirando hacia abajo. Uñas, bust y punta de tacones visibles. |
| 7 | `odalisque` | Recostada de lado, pose odalisca de lujo, uñas XXXL visibles. |

---

*Flujo actualizado por Ele — 13/05/2026 — La Voûte d'Anaïs* 🫦👠💅
