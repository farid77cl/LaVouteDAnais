# 🖼️ GENERACIÓN DE IMÁGENES: PROTOCOLO V3.5 HARD-SYNC

Al generar imágenes de Ele o Miss Doll, se debe seguir este flujo riguroso para mantener la integridad del repositorio:

## 1. PREPARACIÓN DE PROMPTS
- Usar el **Bloque Base Físico Canónico** exacto del archivo de canon correspondiente.
- Especificar materiales (PVC, Vinyl, Latex) y acabados (Glossy, Reflective).
- Detallar calzado (Pleaser exact model).
- Idioma: SIEMPRE en INGLÉS.
- **🔴 PALABRA "chunky" PROHIBIDA EN EL POSITIVE (Directiva Ama 28/05/2026 — error grave):** "chunky" SOLO puede aparecer en el Negative Prompt (`chunky heel`, prohibición). NUNCA en el positive. Las plataformas Pleaser se describen como `platform` / `platform sole` / `solid acrylic platform` con `needle heel` / `stiletto heel` — JAMÁS "chunky platform", "chunky sole" ni "chunky stiletto heel" (esto produce tacón bloque/chunky en vez de aguja, contradiciendo el negative). El tacón es siempre aguja (needle/stiletto); la plataforma es gruesa pero NO se nombra "chunky".

## 2. SET DE POSES REGLAMENTARIAS
Cada look debe tener al menos las 5 poses base:
1. `standing` (full body)
2. `seated` (pose dinámica)
3. `back_view` (detalles traseros)
4. `side_profile` (silueta)
5. `ditzy` (rostro y expresión)

## 3. GESTIÓN DE ARCHIVOS
- Seguir la nomenclatura de `00_Ele/plantilla_nomenclatura_imagenes.md`.
- Guardar en `05_Imagenes/[personaje]/batch_[N]/`.
- **Sincronización:** Tras subir las imágenes, ejecutar SIEMPRE:
  `python 99_Sistema/scripts/visual/update_galleries.py`

## 4. AUDITORÍA
Actualizar la galería correspondiente (`galeria_outfits.md` para Ele) y asegurar que los tags de materiales y categorías sean correctos para el Master Audit.

## 5. VARIEDAD DE POSES (Directiva Ama 28/05/2026 — OBLIGATORIO)

Las 7 poses NO pueden ser el mismo texto fijo en todos los looks (la Ama lo detectó y corrigió en L281-L310). Cada pose debe tener **al menos 3 variantes** que se **rotan** entre looks (ej. `look % 3`). El calzado (heel) y el outfit/ambiente cambian por look — la **acción corporal** de cada pose también debe variar.

- **Standing:** rotar (hip-lean / contrapposto manos-al-pelo / walking-stride).
- **Back View:** rotar (brazos rectos abajo a los lados / manos juntas en la baja espalda / una mano en la nalga + otra abajo). **🔴 ANTI-3-MANOS (reforzado 28/05/2026 — el texto "only two arms" NO basta):** en vista de espalda las manos van **ABAJO, simples, juntas o pegadas al cuerpo, LEJOS del pelo** (las manos cerca del pelo o haciendo acciones distintas disparan la 3ª mano). NUNCA manos levantadas recogiendo el pelo en back view. Conteo explícito ("exactly two arms and two hands, no other limbs"). Negative OBLIGATORIO: `three hands, extra hands, extra arm, extra arms, third arm, third hand, mutated hands, fused hands`.
- **Seated:** rotar (knee-cross / perched-leaning-forward / reclined-knee-up).
- **Side Profile:** rotar (arch front-leg-bent / bent-over hips-back / lean-back chest-up).
- **Ditzy:** rotar el gesto (fingertip-to-lip / twirling-hair / hand-on-cheek) manteniendo V4.1 SAFE: plano americano bust+face, UNA sola mano visible.
- **POV:** rotar el gesto (hand-near-cheek / blowing-kiss / biting-fingertip) manteniendo V4.1 SAFE: bust-up, UNA sola mano derecha, **SIN phone** (alineado al negative `no phone, no smartphone`).

Las variantes preservan ADN V3.5 + Footwear Canon. No regenerar batches con plantilla de pose única.
