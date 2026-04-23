---
name: ele-outfit-engine
description: Motor especializado en la creación y gestión de la identidad visual de Ele. Gestiona la generación de prompts bajo el protocolo V3.5 Hard-Sync, asegura la consistencia de imagen en múltiples poses, y mantiene actualizadas las estadísticas de la galería de outfits. Úsalo cada vez que se solicite un "Outfit del Día", un nuevo Look, o una auditoría del repositorio visual.
---

# 👠 Ele Outfit Engine (V3.5)

Este Skill es el motor central para mantener la coherencia estética y técnica de Ele. Su objetivo es garantizar que cada nuevo activo visual respete el ADN canónico y mantenga el equilibrio estadístico del repositorio.

## 🧬 ADN V3.5 Hard-Sync (Referencia Rápida)

Para cada generación de imagen, **DEBES** incluir estos elementos de forma explícita para evitar variaciones:

- **Físico:** Oval face, high cheekbones, grey-green eyes, dark cherry red hair (XXXL extensions, hip-length).
- **Modificaciones:** Blackwork tattoos (upper back, arms, outer thighs), 14k white gold piercings (navel, nipple piercings pressing through clothing).
- **Estética:** Dramatic siren liner, glossy hot pink lips, XXXL French nails (5cm, white tips).
- **Calidad:** 8k, editorial fashion photography, high-gloss specularity.

## 🛠️ Workflow Operativo

> **ORDEN OBLIGATORIO:** Análisis → Diseño del Outfit → Escritura de los 5 Prompts en galeria_outfits.md → Generación → Git → Estadísticas.
> **Ninguna imagen se genera antes de que los 5 prompts completos estén escritos en `galeria_outfits.md`.**

---

### 1. Análisis de Mix de Arquetipos
Antes de proponer un Look, consulta la tabla de estadísticas en [galeria_outfits.md](file:///c:/Users/farid/LaVouteDAnais/00_Ele/galeria_outfits.md).

**Categorías principales (tipo de prenda):**
- **Mix** (Corporate / Domestic / High-Fashion / Escort / Stripper / Pin-Up): Meta 75%
- **Bikini:** Meta 10%
- **Lencería:** Meta 10%
- **Gym/Athleisure:** Meta 5%

**Sub-arquetipos dentro de Mix** (Meta: 16.6% cada uno — ver `ele_master_audit_v3_5.md`):
1. High-Fashion & Nightclub
2. Corporate
3. Domestic
4. Professional Stripper
5. Escort de Lujo
6. Pin-Up & Athleisure

Si una categoría o sub-arquetipo está bajo, el nuevo Look **debe** pertenecer a esa categoría.

---

### 2. Definición del BLOQUE B (Outfit del Día)
Antes de escribir ningún prompt, define el outfit con **máximo detalle** para que no existan variaciones entre imágenes. El BLOQUE B debe describir:
- Cada prenda: material exacto, color exacto, corte, textura, brillo
- Calzado: modelo, altura del tacón, material, color
- Accesorios: cada pieza, posición en el cuerpo, material
- Detalles de fit: cómo se ajusta al cuerpo de Ele (tensión, transparencia, arquitectura)

El BLOQUE B se escribe **una sola vez** y se copia idéntico en los 5 prompts. Nunca se parafrasea ni resume entre poses.

---

### 3. Escritura de los 5 Prompts Completos en galeria_outfits.md (PREVIO A GENERACIÓN)

**BLOQUE A — ADN Inamovible (siempre idéntico, copiado de [dna_v3_5.md](references/dna_v3_5.md)):**
```
stunning woman with (bimbofied facial features, oval face, high prominent cheekbones, large almond-shaped grey-green eyes, straight slim upturned nose, overlined glossy hot pink lips, small pointed chin:1.3), flawless white porcelain skin, hyper-polished smooth skin texture, dramatic siren liner, dramatic lash extensions, dark cherry red hair, artificial XXXL extensions hip-length, voluminous waves, center parted, slender hourglass silhouette, full bust, wide hips, aggressive bimbomakeup, visible arm tattoos blackwork style, subtle minimalist blackwork tattoos on upper back and outer thighs, navel piercing, 14k white gold nipple piercings pressing against and visible under clothing, extra long French XXXL nails with white tips and pink base 5cm, 8k, editorial fashion photography, high-gloss specularity
```

El BLOQUE A **nunca se modifica**. Se copia textualmente de `dna_v3_5.md`. Nunca se escribe de memoria.

**Estructura de cada prompt:** `[BLOQUE A] + [BLOQUE B] + [BLOQUE C — Pose y Setting]`

**Poses estándar obligatorias (BLOQUE C):**
- **Standing View:** full body, catalog pose, [fondo coherente con el arquetipo]
- **Back View:** rear focus, tattoos visible, [mismo fondo]
- **Seated View:** seated on [mobiliario coherente con el setting], [mismo fondo]
- **Side Profile:** lateral silhouette, hourglass emphasis, [mismo fondo]
- **Ditzy Expression:** close-up face, vacant gaze, lips parted, [mismo fondo]

**Los 5 prompts completos (A+B+C) deben quedar escritos en la entrada del Look en `galeria_outfits.md` antes de que se genere ninguna imagen.**

---

### 4. Generación de Imágenes
Solo se genera después de completar el paso 3. Se usa cada prompt escrito exactamente como aparece en `galeria_outfits.md` — sin modificaciones improvisadas.

---

### 5. Gestión de Activos (Remote-Only)
Sigue rigurosamente el protocolo de limpieza:
1. Guardar imágenes generadas en `05_Imagenes/ele/lookXXX/`.
2. Hacer `git add`, `git commit` y `git push`.
3. **ELIMINAR** los archivos binarios locales para mantener el repositorio ligero.
4. Actualizar el walkthrough con links `file:///C:/Users/farid/LaVouteDAnais/05_Imagenes/ele/lookXXX/` para visualización inmediata.

---

### 6. Actualización de Estadísticas
Tras crear un Look, recalcula los totales y porcentajes en la cabecera de `galeria_outfits.md`.

## 🛡️ Blindaje contra Racionalizaciones (TDD Protocol)

Los agentes suelen buscar atajos bajo presión. Estas excusas están **PROHIBIDAS**:

| Excusa / Racionalización | Realidad Canónica |
| :--- | :--- |
| "Generé la imagen y documentaré el prompt después." | **ERROR CRÍTICO.** Los 5 prompts completos se escriben en `galeria_outfits.md` ANTES de generar. Sin excepción. |
| "El BLOQUE A es siempre el mismo, no necesito copiarlo en cada prompt." | **ERROR.** El BLOQUE A se copia textualmente de `dna_v3_5.md` en cada uno de los 5 prompts. Nunca se omite ni se resume. |
| "Ajusté el BLOQUE B en la pose 3 porque la pose lo requería." | **ERROR.** El BLOQUE B es invariable entre las 5 poses. Solo el BLOQUE C (pose y setting) varía. |
| "Omití los piercings para un look más limpio." | **ERROR.** Los piercings V3.5 son parte del ADN Hard-Sync. Nunca se omiten. |
| "No actualicé las estadísticas porque solo era un Look." | **ERROR.** Cada Look altera los porcentajes. La actualización es obligatoria. |
| "Usé 'red hair' porque es más corto." | **ERROR.** El tono exacto es 'Dark Cherry Red'. Las variaciones diluyen la identidad. |
| "No borré los archivos locales para ahorrar tiempo." | **ERROR.** Violar el protocolo 'Remote-Only' ensucia el repositorio. |

## 🚩 Banderas Rojas - ¡DETENTE Y REVISA!
- Estás a punto de generar una imagen sin haber escrito los 5 prompts completos en `galeria_outfits.md`.
- Uno de tus prompts no incluye el BLOQUE A completo copiado de `dna_v3_5.md`.
- El BLOQUE B difiere entre dos de las 5 poses del mismo Look.
- Estás usando un prompt que no incluye "nipple piercings pressing through".
- Estás proponiendo un color "Baby Pink" o "Pastel Blue" sin una orden explícita de la Ama.
- Estás subiendo imágenes sin haber verificado el balance de arquetipos en la tabla maestra.
- Tu walkthrough usa links relativos en lugar de `file:///C:/Users/...`.

**REGLA DE ORO:** Si violas la letra de este Skill, estás violando el ADN de Ele. No hay excepciones.

## 📂 Recursos del Skill
- [DNA_V3_5.md](references/dna_v3_5.md): Descripción detallada para prompts.
- [stats_updater.py](scripts/stats_updater.py): Script (pseudocódigo) para automatizar el conteo.
