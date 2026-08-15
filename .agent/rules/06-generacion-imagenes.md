# 🖼️ GENERACIÓN DE IMÁGENES: PROTOCOLO V3.5 HARD-SYNC

Al generar imágenes de Ele o Miss Doll, se debe seguir este flujo riguroso para mantener la integridad del repositorio:

## 1. PREPARACIÓN DE PROMPTS
- Usar el **Bloque Base Físico Canónico** exacto del archivo de canon correspondiente.
- Especificar materiales (PVC, Vinyl, Latex) y acabados (Glossy, Reflective).
- Detallar calzado (Pleaser exact model).
- Idioma: SIEMPRE en INGLÉS.
- **🔴 PALABRA "chunky" PROHIBIDA EN EL POSITIVE (Directiva Ama 28/05/2026 — error grave):** "chunky" SOLO puede aparecer en el Negative Prompt (`chunky heel`, prohibición). NUNCA en el positive. Las plataformas Pleaser se describen como `platform` / `platform sole` / `solid acrylic platform` con `needle heel` / `stiletto heel` — JAMÁS "chunky platform", "chunky sole" ni "chunky stiletto heel" (esto produce tacón bloque/chunky en vez de aguja, contradiciendo el negative). El tacón es siempre aguja (needle/stiletto); la plataforma es gruesa pero NO se nombra "chunky".

## 2. SET DE POSES REGLAMENTARIAS (TAXONOMÍA DE 7 POSES)
Cada look debe tener las 7 poses canónicas, adaptando el slot 5 según el personaje:
1. `standing` (full body frontal)
2. `back_view` (arquitectura trasera y calzado)
3. `seated` (peso total en el asiento)
4. `side_profile` (silueta lateral 3/4)
5. Slot 5 específico:
   - Ele: `ditzy` (plano medio, mirada soñadora fuera de cuadro)
   - Miss Doll: `glacial_command` (plano medio, mirada fría dominante)
   - Anaïs Belland: `sovereign_gaze` (plano medio, gravitas aristocrática)
6. `pov` (retrato sensual a cámara, mirada directa al lente, sin teléfono)
7. `odalisque` (figura baja horizontal reclinada)

## 3. GESTIÓN DE ARCHIVOS Y CONTRATO LV-APP (Directiva Ama 15/08/2026)
- Guardar en `05_Imagenes/<personaje>/look<N>_<slug>/`.
- Nombres de archivo estrictos según `CharacterProfile.kt` de LV-App:
  - **Ele:** `ele_<N>_<pose>.png`
  - **Miss Doll:** `miss_doll_<N>_<pose>.png` (NUNCA usar `ditzy`, siempre `glacial_command` en slot 5)
  - **Anaïs (Estándar):** `anais_<N>_<pose>.png` (NUNCA usar `ditzy`, siempre `sovereign_gaze` en slot 5)
  - **Anaïs (Boudoir):** `anais_L<NN>_<pose>.png` (ej. `anais_L08_standing.png`)
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

**Planos cenitales (Ama 02/08/2026):** el pool Odalisque ahora trae **2 variantes cenitales** (picado total, cámara directamente arriba mirando hacia abajo). El ancla se **partió** en `ODALISQUE_RECUMBENCY` (siempre) + `ODALISQUE_LEVEL_CAM` (variantes laterales) vs `ODALISQUE_ZENITHAL_CAM` (variantes cenitales) — porque el horizonte nivelado choca con un picado. `rotate_poses` detecta la variante cenital (`"zenithal" in v`) y le pone recumbencia + cámara cenital, nunca la nivelada. Automático, sin parámetro.

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

## 9. DITZY ≠ POV — DIFERENCIACIÓN (Directiva Ama 02/08/2026 — "salen casi iguales el 90%")

Ditzy y POV rendían casi idénticas: ambas close-up de cara, mano cerca del rostro, *half-lidded gaze*. **Fix en los pools de variantes** (`DITZY` / `POV` en `pose_rotation_v5.py`), diferenciador duro:
- **Ditzy** = toma cintura-arriba de **detalle del outfit** superior · **mirada perdida/soñadora FUERA de cuadro** (no al lente) · expresión de **bimbo despistada** (airhead daydream), no smoldering.
- **POV** = close-up de **cara al lente** · **mirada directa** thirst-trap de Instagram.

Self-check `Diferenciacion Ditzy/POV`: toda variante Ditzy mira fuera de cuadro; toda variante POV mira al lente. Automático, sin parámetro.

## 10. SENTADA CON FALDA — PIERNAS CERRADAS (Directiva Ama 02/08/2026 — "sentada con falda no puede ser abierta de piernas")

Las 6 variantes `SEATED` ya pedían piernas cruzadas/juntas, pero el generador **driftea a piernas abiertas** y con falda eso expone la entrepierna y rompe el canon editorial. **Fix:** parámetro `skirt=True` en `rotate_poses` → inyecta `SEATED_MODESTY` (*"rodillas y muslos apretados juntos, piernas cruzadas o juntas a un lado, nunca abiertas ni en M, ruedo de la falda cerrado sobre el regazo"*) **solo en el slot Seated**. **Todo inyector cuyo look lleve falda o vestido DEBE pasar `skirt=True`.** Self-check `Modestia Seated con falda`. (Con bikini/short no se pasa: ahí no aplica.)
