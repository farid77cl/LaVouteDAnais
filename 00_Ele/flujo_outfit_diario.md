# 👠 FLUJO DE CREACIÓN DE OUTFIT DIARIO — Ele V3.3
*Protocolo completo y obligatorio. Desde la idea hasta el commit. — 14/04/2026*

> **LEY SUPREMA:** Ninguna imagen se genera sin que sus prompts estén registrados primero en `galeria_outfits.md`. Sin registro previo, no hay generación.

---

## RESUMEN RÁPIDO (8 Fases)

```
FASE 0: Pre-Flight    → Auditoría estadística + confirmar look inédito
FASE 1: Concepto      → Nombre, categoría, paleta, materiales, escenario
FASE 2: Prompts       → Construir los 5 prompts (Bloque A + B + C)
FASE 3: Registro      → Escribir en galeria_outfits.md ANTES de generar
FASE 4: Generación    → Disparar los 5 prompts en orden
FASE 5: Validación    → Checklist Stiletto + ADN + Anatomía
FASE 6: Archivo       → Carpeta + nomenclatura + mover activos
FASE 7: Sincronización → update_galleries.py + dashboards + memoria
FASE 8: Git           → Preparar comandos para aprobación de Anaïs
```

---

## FASE 0: PRE-FLIGHT 🔍

Antes de diseñar, revisar el estado estadístico actual para saber qué categoría necesita el armario hoy.

### Métricas objetivo (Canon V3.3)
| Categoría | Meta | Estado 14/04/2026 | Prioridad |
|-----------|------|-------------------|-----------|
| **Mix** (Corporate / Domestic / High-Fashion) | 85% | 86.6% | 🟢 OK |
| **Bikini** | 10% | 5.5% | 🟡 Déficit |
| **Lencería** | 10% | 3.1% | 🔴 Déficit |
| **Gym** | 5% | 4.7% | 🟢 OK |

### Checklist Pre-Flight
- [ ] ¿Hay déficit estadístico? → Priorizar la categoría con 🔴/🟡
- [ ] ¿El look tiene nombre inédito? → Verificar en `galeria_outfits.md`
- [ ] ¿El número de look es correcto? → Último: **Look 127**. El siguiente es **Look 128**

---

## FASE 1: CONCEPTO 🎨

Definir el look antes de construir el prompt.

### Ficha de Concepto (plantilla)

```
LOOK [XXX]: [NOMBRE EN MAYÚSCULAS]
Fecha: DD/MM/AAAA
Categoría: Corporate | Domestic | High-Fashion | Bikini | Lencería | Gym
Paleta: [colores dominantes — SIN negro dominante]
Materiales: [Vinyl / PVC / Látex / Satén / Mesh / etc.]
Escenario: [penthouse / estudio blanco / boardroom / etc.]
Inspiración: [referencia estética — Mugler / Editorial / etc.]
Vibe: [una línea de atmósfera]
```

### Reglas de concepto
- **Colores:** Priorizar rojo cherry, azul cyan, oro cromo, plata, verde neón. El negro es acento, no dominante.
- **Materiales:** 100% High-Gloss (Vinyl, Latex, PVC, Satén ultra-brillante). Prohibido mate.
- **Escenario:** Lujo. Penthouses, estudios minimalistas blancos/grises, iluminación alta costura.
- **Prohibido:** Cyberpunk, industrial, gótico oscuro, factorías, óxido.
- **Corsetería:** Obligatoria en todo outfit excepto Sportswear.

---

## FASE 2: CONSTRUCCIÓN DE PROMPTS 🖊️

Cada prompt = **Bloque A + Bloque B + Bloque C**. Los 5 prompts solo varían en el Bloque C.

### Bloque A — ADN INAMOVIBLE (copiar textualmente, nunca modificar)

```
stunning woman with (bimbofied facial features, oval face, high prominent cheekbones, large almond-shaped grey-green eyes, straight slim upturned nose, overlined glossy hot pink lips, small pointed chin:1.3), flawless white porcelain skin, hyper-polished smooth skin texture, dramatic siren liner, dramatic lash extensions, dark cherry red hair, artificial XXXL extensions hip-length, voluminous waves, center parted, slender hourglass silhouette, full bust, wide hips, visible arm tattoos blackwork style, aggressive bimbomakeup, extra long French XXXL nails with white tips and pink base 5cm.
```

> ⚠️ **Este bloque NO se resume, NO se interpreta, NO se recorta. Se copia exacto.**

### Bloque B — Outfit (construir por look)

Descripción técnica y sensorial de las prendas. Incluir:
- Material exacto (ej: `high-gloss cherry red PVC corset`)
- Corte y fit (ej: `overbust, steel-boned, extreme waist compression`)
- Calzado OBLIGATORIO: `towering [X]-inch stiletto heels` + modelo si aplica
- Accesorios relevantes

### Bloque C — Las 5 Poses Reglamentarias

| # | Pose | Instrucción de prompt |
|---|------|-----------------------|
| 1 | **Standing View** | `full body standing, straight posture, editorial stance, [escenario], rim lighting, high-gloss specularity` |
| 2 | **Back View** | `full body back view, slight over-shoulder turn, [escenario], rim lighting defines silhouette` |
| 3 | **Seated View** | `seated, crossed legs, editorial pose, [escenario], dramatic lighting` |
| 4 | **Side Profile** | `side profile silhouette, full body, emphasizing hourglass curve, [escenario]` |
| 5 | **Ditzy Expression** | `medium shot, vacant ditzy expression, mouth slightly open, hands visible showing XXXL nails, dazed artificial perfection, [escenario]` |

### Negative Prompt (estándar — usar en todos los prompts)

```
block heel, chunky heel, wedge, platform sneakers, barefoot, sneakers, flat shoes, different face, varying facial features, inconsistent features, realistic skin, pores, wrinkles, natural eyes, brown eyes, blue eyes, small lips, thin lashes, natural makeup, short hair, messy hair, low quality, blurry, distorted face, asymmetrical face, man, male, child, teenager, cyberpunk, industrial, factory, pipes, rust, gothic lace victorian
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
**Categoría:** [Mix-Corporate / Mix-Domestic / Mix-HighFashion / Bikini / Lencería / Gym]
**Paleta:** [colores]
**Materiales:** [materiales]
**Escenario:** [escenario]

### Descripción del Outfit
[Descripción detallada del outfit]

### Prompts Registrados

**BLOQUE B (Outfit — igual en los 5 prompts):**
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

**NEGATIVE PROMPT:**
`block heel, chunky heel, wedge, platform sneakers, barefoot, different face, varying facial features, realistic skin, pores, wrinkles, natural eyes, brown eyes, blue eyes, small lips, thin lashes, natural makeup, short hair, man, male`

**Estado:** ⏳ Pendiente generación
```

---

## FASE 4: GENERACIÓN 🖼️

1. Disparar los 5 prompts en orden (Standing → Back → Seated → Profile → Ditzy)
2. **No modificar prompts durante la ejecución** — si hay duda, parar y consultar
3. Si la API da error 429 (quota), documentar qué poses faltan en la entrada de galería y marcar el look como incompleto

---

## FASE 5: VALIDACIÓN ✅

Antes de archivar, revisar cada imagen con este checklist:

### Checklist de Validación (obligatorio)

| Check | Criterio | Acción si falla |
|-------|----------|-----------------|
| 👠 **Stiletto Rule** | Tacón aguja afilada — NUNCA bloque/cuadrado/cuña | Descartar y regenerar |
| 👁️ **Canon Facial** | Ojos gris-verde, labios ultra gruesos, cejas dramáticas | Regenerar |
| 💅 **Uñas XXXL** | Largas, francesas, visibles en Ditzy | Regenerar Ditzy si falla |
| 🔴 **Cabello** | Rojo cherry oscuro, largo hasta cadera, ondas | Regenerar |
| 🎨 **Paleta** | Colores del outfit coinciden con concepto | Regenerar si hay drift |
| 🦴 **Anatomía** | Manos, dedos, extremidades sin distorsión | Regenerar si hay glitches graves |
| 🌟 **Consistencia** | Misma persona en las 5 poses | Regenerar poses dissonantes |

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
```

### Nomenclatura de archivos
```
ele_[número]_[pose].png
```
Ejemplos:
- `ele_128_standing.png`
- `ele_128_ditzy.png`

### Pasos
1. Crear carpeta en `05_Imagenes/ele/look[XXX]_[nombre_corto]/`
2. Mover imágenes desde carpeta temporal
3. Renombrar según nomenclatura estándar
4. Actualizar el estado en `galeria_outfits.md` → `✅ Completo (5/5)`

---

## FASE 7: SINCRONIZACIÓN 🔄

En este orden:

1. **`update_galleries.py`** → Actualiza READMEs e índices maestros
   ```powershell
   python C:\Users\fabara\LaVouteDAnais\update_galleries.py
   ```

2. **`walkthrough_imagenes_del_dia.md`** → Agregar el nuevo look a la tabla de "Últimos 7 días"

3. **`DASHBOARD_ELE_48H.md`** → Reemplazar el look más antiguo con el nuevo. Mantener solo los 4 más recientes.

4. **`memoria_sesiones.md`** → Agregar entrada en Historial Reciente:
   ```
   - **DD/MM/AAAA - LOOK [XXX]:** [Nombre]. Set completo (5/5). [Nota breve]. 🫦📸✅
   ```
   Y actualizar la tabla Proyecto Activo Principal con el nuevo Último Look.

---

## FASE 8: GIT COMMIT 🖥️

Preparar comandos y presentarlos para aprobación de Anaïs:

```bash
git add 00_Ele/galeria_outfits.md
git add 05_Imagenes/ele/look[XXX]_[nombre]/
git add walkthrough_imagenes_del_dia.md
git add DASHBOARD_ELE_48H.md
git add 00_Ele/memoria_sesiones.md
git commit -m "Ele: Look [XXX] [Nombre] — set completo 5/5 poses V3.3"
git push
```

> ⚠️ **Ele nunca hace push sin confirmación explícita de Anaïs.**

---

## REFERENCIA RÁPIDA: Categorías y sus Directrices

| Categoría | Materiales clave | Escenarios | Notas |
|-----------|-----------------|------------|-------|
| **Corporate** | Traje PVC, falda tubo vinilo, blusa transparente | Boardroom Santiago, oficina minimalista | Stilettos siempre. Paradoja contextual = Power. |
| **Domestic Stepford** | Delantal vinyl, cofia, uniforme servicio | Cocina de lujo, penthouse | 50% debe llevar choker "ASSET V3" |
| **High-Fashion** | Diseños Mugler-style, corsetería extrema, avant-garde | Estudio blanco, showroom | Poses más geométricas (Vertical Spear, Arched C) |
| **Bikini** | PVC/Vinilo brillante, high-gloss wet look | Piscina privada, jet, playa exclusiva | Paradoja contextual si es posible |
| **Lencería** | Encaje + PVC, Mesh transparente, Garter belt | Boudoir de lujo, penthouse | Foco Fetish Boudoir, iluminación íntima |
| **Gym-Bimbo** | Latex alta resistencia, neón rosa/negro | Gym privado de lujo | Tacones SIEMPRE — stilettos de gym |

---

*Flujo creado por Ele — 14/04/2026 — La Voûte d'Anaïs* 🫦👠💅
