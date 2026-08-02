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
- **Ditzy:** rotar el gesto (fingertip-to-lip / twirling-hair / hand-on-cheek) con UNA sola mano visible. **🔴 ENCUADRE = PLANO MEDIO (Directiva Ama 28/05/2026):** waist-up (cintura hacia arriba), rostro **grande, nítido y detallado** + busto/décolleté **prominente en el frame inferior, SIEMPRE**. NO plano americano (knee-up), NO plano entero/full-body, NO distante. El control va 100% en el POSITIVE del Ditzy (no se puede meter `full body` al negative porque es compartido con Standing/Side Profile/Odalisque que sí son cuerpo entero).
- **POV:** rotar el gesto (hand-near-cheek / blowing-kiss / biting-fingertip) manteniendo V4.1 SAFE: bust-up, UNA sola mano derecha, **SIN phone** (alineado al negative `no phone, no smartphone`).

Las variantes preservan ADN V3.5 + Footwear Canon. No regenerar batches con plantilla de pose única.

## 6. PRENDA ENVOLVENTE DE FRENTE ABIERTO — ORIENTACIÓN EN BACK VIEW (Directiva Ama 09/07/2026 — BUG "bata al revés")

Cuando el look use una prenda **envolvente de frente abierto** — robe, kimono, peignoir, **bata**, wrap cardigan, hanbok/qipao abierto — el generador la ponía **AL REVÉS en la pose de espalda**: la abertura/escote corría por la columna (dejando el poto y la lencería al aire por donde va el *paño trasero*), porque el token de vestuario dice *"parted at front revealing X / off the shoulders"* y eso es una instrucción **relativa a la cámara** que, con el cuerpo de espaldas, la IA resuelve abriendo la prenda hacia el lente. Confirmado en **L256** (bata La Perla) y **L703** (kimono peacock). Los que salieron bien (L407) tenían la bata deslizada de los hombros.

**Regla:** todo inyector que genere un look con prenda envolvente **DEBE** pasar `wrap_mode` a `rotate_poses`:

```python
poses = rotate_poses(look_number, ..., wrap_mode="slip")   # o "closed"
```

- `wrap_mode="slip"` → bata **deslizada de los hombros, colgando de los brazos**: espalda + lencería al aire pero prenda físicamente correcta (la abertura va adelante; solo se resbaló). **Default recomendado** para boudoir/lencería (conserva el desnudo sensual).
- `wrap_mode="closed"` → bata **bien puesta**: paño continuo cerrado cayendo por la columna (espalda cubierta). Para batas cortas/deportivas o cuando no se busca desnudo.
- `wrap_mode="tailored"` (Ama 02/08/2026) → **prenda de frente abierto ESTRUCTURADA y cerrada** (blazer, chaqueta, abrigo, tuxedo, coat-dress, blazer-dress): ancla el **panel de espalda liso a la cámara**, solapas/abertura/botones al lado lejano, nunca al revés. Es el mismo bug de la bata pero en sastrería — pega en los looks corporate. Usarlo siempre que el outfit lleve blazer/chaqueta cerrada.
- `wrap_mode=None` → sin prenda envolvente (comportamiento normal). **La elección es caso a caso** (directiva Ama): la decide el inyector según el concepto del look.

El ancla se inyecta **solo en el slot Back View** (donde ocurre el fallo). Vive en `pose_rotation_v5.py` (`WRAP_BACK_SLIP` / `WRAP_BACK_CLOSED` / `WRAP_BACK_TAILORED`), con self-check en el `__main__`. Ver auto-memoria `feedback_bata_reverso_espalda`. **Los prompts ya escritos (71 back-views de la flota) se blindaron por barrido el 02/08** — esta regla protege los looks NUEVOS.

## 7. ODALISCA RECOSTADA, NO SENTADA (Directiva Ama 09/07/2026 — BUG "odalisca sentada")

La **odalisca** (pose recostada/lánguida) derivaba a **SENTADA**: el generador rendía a Ele *sentada* en el piso o el mueble en vez de recostada (confirmado en L574 sentada sobre el cofre, L638 y L660 sentadas en el piso). Causa: varias variantes arrancan *"semi-reclined propped on both elbows"* y ese *"propped on both elbows"* se lee como torso vertical sentado, sin ancla explícita de cuerpo horizontal. **Mismo patrón que Side Profile** (que se sentaba hasta que forzamos `standing` explícito).

**Fix (automático, ya en el motor):** `rotate_poses` prepende `ODALISQUE_ANCHOR` (*"lying down on the surface, the whole body low and horizontal, a reclining odalisque, NOT sitting upright and NOT seated"*) **solo al slot Odalisque**. No requiere nada del inyector. **Recomendado además** añadir al negative del inyector: `sitting upright, seated, sitting on the floor`. Self-check en el `__main__` del módulo. Ver auto-memoria `feedback_odalisca_sentada`.

## 8. LINT DE CALZADO OBLIGATORIO (Directiva Ama 09/07/2026 — "aplica los fix en el engine para que no pase")

El token de calzado se escribe libre por look y nada lo validaba → se colaban errores de canon que solo se cazaban mirando las imágenes ya generadas (auditoría del batch blanco de novia L731-L740: open/peep toe **con medias**, mule fuera de Lencería, mule sin plataforma). **Fix de raíz:** `99_Sistema/scripts/visual/footwear_canon.py`, un linter que **todo inyector DEBE correr antes de escribir la galería** (igual que `check_setting_variety`):

```python
from footwear_canon import audit_footwear_batch
problems = audit_footwear_batch(LOOKS)   # cada look: dict con footwear + outfit + category
if problems:
    for p in problems: print(p)
    raise SystemExit("Calzado no-canonico: corrige antes de cerrar el batch.")
```

Reglas que impone (devuelve la lista de violaciones; vacía = limpio):
1. **Medias + puntera abierta** (`open/peep toe` con `stocking/fishnet/nylon/bodystocking…`) → prohibido (regla medias 20/06: con medias, puntera **cerrada**).
2. **Mule fuera de Lencería** → prohibido (Ama 09/07: mule EXCLUSIVO de Lencería).
3. **Mule sin plataforma ≥4"** (~10cm) → prohibido (Ama 09/07: el mule es platform mule ≥4").
4. **Calzado plano/no-canónico o `chunky` en el positive** (`flat/wedge/block/kitten/sneaker/barefoot/chunky`) → eso va solo en el negative.

Self-check en el `__main__`. Ver auto-memorias `feedback_medias_calzado_reglas` y `feedback_footwear_canon_absoluto`.
