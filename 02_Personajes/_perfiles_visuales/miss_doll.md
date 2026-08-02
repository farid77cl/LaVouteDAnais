# 🎀 Perfil Visual — Miss Doll

> Contrato del `outfit-engine`. Creado 27/07/2026 al generalizar el motor.
> **Antes de esto Miss Doll no tenía motor**: solo una regla de canon (`.agent/rules/05-canon-miss-doll.md`) y un sistema de poses. No tenía Step 0 anti-repetición, ni token bloqueado, ni arquetipos con metas.

---

## §1 · Identidad y Rutas

| Campo | Valor |
|---|---|
| **Nombre canónico** | Miss Doll |
| **Slug** | `miss_doll` |
| **Galería** | `02_Personajes/01_Principales/miss_doll/GALERIA_OUTFITS_MISS_DOLL.md` |
| **Carpeta de imágenes** | `05_Imagenes/miss_doll/look<NNN>_<tema>/` |
| **Convención de nombre** | `miss_doll_<N>_<pose>.png` ⚠️ ver §9 |
| **Numeración** | correlativa con cero a la izquierda (`look001`, `look002`…) |
| **Canon profundo (enlace)** | [`CANON_VISUAL_MISS_DOLL.md`](../01_Principales/miss_doll/CANON_VISUAL_MISS_DOLL.md) — **manda sobre este perfil en caso de conflicto** |
| **Sistema de poses** | [`SISTEMA_POSES_VESTUARIO_MISS_DOLL.md`](../01_Principales/miss_doll/SISTEMA_POSES_VESTUARIO_MISS_DOLL.md) |

---

## §2 · BLOQUE A — ADN Inamovible

```text
hyper-realistic high-end editorial glamour photography of Miss Doll, adult glamorous woman, (sharp angular heart-shaped face:1.1), clean sharp defined jawline, (high very prominent razor-sculpted cheekbones:1.2), small refined pointed chin, delicate refined features COMMANDING, sharp platinum blonde asymmetric angled bob, sleek straight razor-cut strands, ice platinum highlights, clear exposed forehead, NO BANGS, (small refined perky upturned doll nose:1.2), (narrow slightly hooded almond-shaped cold pale steel grey eyes:1.2), pale icy grey iris with sharp dark limbal ring, (fixed dominant professional gaze zero warmth:1.2), chin elevated 5 degrees, (ultra-slim microbladed platinum blonde brows precise individual hair strokes sharp cold arch tapered tail:1.2), HEAVY GLAMOUR editorial makeup with (thick sharp angular winged eyeliner upticked pointed wing tip:1.2), intense shimmer smokey eye, (impossibly long mega XXL individual false lashes at outer corners dramatic cat-eye:1.2), (blinding chrome strobing highlight on cheekbones nose bridge and brow bone:1.2), (strong deep angular contour cold shadow under cheekbone:1.1), (aggressively overlined voluminous ULTRA PLUMP high-gloss wet lips exaggerated cupid's bow full pillowy lips mirror-gloss finish:1.3) open giving command, human realistic face DOMINANT expression, pale cold porcelain white skin, editorial realistic human skin texture subtle visible pores, cold undertone, sculptural EXTREME hourglass silhouette, extra full round chest prominent cleavage, aggressively narrow cinched waist, full wide hips, tall lean toned commanding figure, rigid upright posture, square shoulders pulled back
```

> ⚠️ El prompt base histórico de la regla 05 mezclaba en un solo bloque el ADN **y** un outfit concreto (bodysuit rosa neón + botas de 8"). Aquí se separan: lo de arriba es **BLOQUE A puro** (cuerpo, cara, pelo, maquillaje, postura). El outfit va en el BLOQUE B de cada look. **Mezclarlos es lo que hace que todos sus looks salgan iguales.**

**Rasgos que NO se negocian jamás:**

- **Platinum blonde asymmetric bob**, corte navaja. Nunca oscuro, nunca coleta, nunca moño.
- **Frente despejada** — `clear exposed forehead, NO BANGS`. El flequillo es violación de canon.
- **Labios ULTRA PLUMP, overlined, high-gloss wet, cupid's bow** — la **forma** es inviolable. El **COLOR es variable por look** (rojo, rosa, humo negro…) y se fija en el BLOQUE B, igual que el maquillaje de ojos. Nunca nude, nunca mate, nunca maquillaje natural. *(Ama 02/08/2026: derogado el "labios rojos SIEMPRE"; el físico canónico pasó a ser el del banco que le gusta, con color de maquillaje variable.)*
- **Ojos gris hielo** con la *Face of the Pole*: disociación profesional, cero calidez.
- **Piel porcelana fría** con textura humana real y poros visibles — nunca cera, nunca maniquí.
- **Sin tatuajes** por defecto (blackwork solo si la Ama pide variante legacy explícita).
- **Barbilla 5-10° arriba, torso erguido, hombros atrás.** Nunca hombros caídos.

---

## §3 · Negative Prompt

**Base (siempre):**
```text
bangs, fringe, covered forehead, dark hair, brunette, ponytail, bun, childish face, teen, natural makeup, subtle makeup, nude lips, matte lips, rosy cheeks, warm natural skin tone, wax skin, plastic mannequin skin, tattoos, casual outfit, flat shoes, sneakers, block heel, chunky heel, vulgar cheap costume, slouched shoulders, warm smile, laughing
```

| Pose | Añadir al negative | Por qué |
|---|---|---|
| Cualquier POV / cámara en mano | `no phone, no smartphone, no device, no screen` | El encuadre POV invita al modelo a añadir un teléfono |
| Poses con barra | `two women, duplicate figure, mirror reflection` | El reflejo del club genera figuras dobles |

---

## §4 · Poses Canónicas

**5 poses firma** (canon vigente, de la regla 05 + su sistema de poses):

| # | Nombre canónico | Slug de archivo | Nota |
|---|---|---|---|
| 1 | Monarch Throne | `monarch_throne` | Sentada, piernas 60-90°, codos en reposabrazos, barbilla ladeada |
| 2 | Hip Carry contra Barra | `hip_carry` | Cadera contra el pole, peso cargado, línea de pierna larga |
| 3 | Pie en Hombro | `pie_en_hombro` | Stiletto apoyado sobre el hombro del sub |
| 4 | Throne en Suelo con Crop | `throne_suelo` | Suelo, piernas en V abierta, codos en rodillas, crop en mano |
| 5 | Caminata Circular Lenta | `caminata_circular` | Step-and-stop, interrupción brusca en contrapposto |

- **Total por look:** 5
- **Repertorio de variaciones:** el vocabulario completo (de pie / pole / floorwork / silla / con sub) está en `SISTEMA_POSES_VESTUARIO_MISS_DOLL.md` §2. Rotar dentro de cada categoría; no clonar la misma entrada dos looks seguidos.
- **Principio rector de pose:** *dispensa sensualidad como poder, no como oferta.* Un movimiento donde otras hacen tres. Pausas de 4+ segundos. La mirada se posa 2-4 s y **abandona deliberadamente**.

---

## §5 · BLOQUE B — Reglas de Vestuario

### 5.1 · Universo de materiales

- **Permitidos:** látex, PVC, vinilo, neopreno técnico, nylon estructural, chrome hardware, black bondage webbing.
- **Cuero:** **solo** en corsés, accesorios y arneses — **nunca como pieza principal**.
- **Prohibidos (absoluto):** tela natural mate, algodón, denim, punto casual.
- **Lente de identidad:** *"parece uniforme privado real, no disfraz."* Fetiche sintético de alto nivel. Su mundo es el club y el calabozo — si la prenda no funcionaría ahí, no es de Miss Doll.

### 5.2 · Paleta y reglas cromáticas

- **Firma inamovible:** el **rosa** (neon / hot / dusty) **SIEMPRE presente** en algún punto del look. Es su cuota cromática permanente.
- **Variantes controladas:** negro carbón, chrome, blanco, champagne, coral, mint, turquesa, lavanda, rose gold.
- **Reservado al ADN:** el **rojo** de los labios. No usar rojo como color dominante de prenda (compite con la firma facial).
- **Anti-monoblock:** máx. 2 looks monoblock consecutivos.

### 5.3 · Calzado (canon inamovible)

- **Regla:** platform stiletto boots / tacones estilo Pleaser.
- **Altura mínima:** plataforma 6" o superior (el canon histórico usa 8").
- **Prohibido:** flats, block heel, **chunky heel**, kitten heel, wedge, descalza.
- **Atributos obligatorios del token** (nombrar los 5 en cada pose): altura · tipo de plataforma · material/acabado · color · tipo de tacón (`razor-thin metal needle heel`).
- ⚠️ La palabra `chunky` va **solo en el negative**, jamás en el positive.

### 5.4 · Prohibiciones absolutas

| Prohibido | Sustituto autorizado | Directiva |
|---|---|---|
| Flequillo / frente cubierta | frente despejada, `NO BANGS` | Canon V3.5 Stealth |
| Labios nude o rosados | rojo glossy/satin | Firma inviolable |
| Cuero como pieza principal | látex/PVC/vinilo; cuero solo en corsé/arnés/accesorio | Canon materiales |
| Tatuajes | piel limpia | Salvo variante legacy pedida por la Ama |
| Texto/nombre sobre prenda | choker liso, O-ring, hardware sin letras | Regla transversal del repo |
| Sonrisa amplia / actitud juguetona | Face of the Pole | Principio de registro |

### 5.5 · Campos obligatorios de descripción

El BLOQUE B debe nombrar, sin excepción:

1. **Arquitectura de corsé** — visible o integrada. Es el **centro del look**: ningún outfit de Miss Doll carece de ella.
2. Prenda principal: material exacto, color exacto, corte, acabado (gloss/matte), fit.
3. Hardware: chrome, anillas, hebillas, webbing — tipo y posición en el cuerpo.
4. Medias/hosiery si aplica: denier, tipo, color.
5. Calzado con sus 5 atributos (§5.3).
6. Accesorios: cada pieza con su posición.
7. Dónde aparece el **rosa firma** (§5.2).

---

## §6 · Arquetipos y Metas

| Arquetipo | Descripción | Meta |
|---|---|---|
| **Club / Escenario** | Pole, tarima, luz neón, revue | 30% |
| **Calabozo / Dungeon** | Sesión, arneses, mobiliario de dominación | 25% |
| **Uniforme Privado** | Latex couture estructurado, protocolo, "de servicio" | 20% |
| **Penthouse / Off-duty** | Su espacio, registro frío fuera del trabajo | 15% |
| **Editorial / Portada** | Sesión de foto pura, fondo controlado | 10% |

- **Regla de déficit:** el arquetipo bajo meta manda sobre el gusto.
- **Prioridad de desempate:** Club > Calabozo > Uniforme > Penthouse > Editorial.

---

## §7 · Ventanas Anti-Repetición

| Elemento | Ventana |
|---|---|
| Silueta | ≥ 3 looks del mismo arquetipo |
| Setting / escenario | ≥ 3 looks del mismo arquetipo |
| Modo cromático monoblock | máx. 2 consecutivos globales |

- **Outfit único:** sí. Miss Doll no repite outfit.

---

## §8 · Cuotas Vivas

| Cuota | Frecuencia | Alcance |
|---|---|---|
| **Rosa firma presente** | **todos los looks** | Cualquier prenda, calzado o accesorio |
| Arquitectura de corsé visible | todos los looks | Centro del look |

---

## §9 · Banderas Rojas Específicas

- 🔴 **Sus imágenes NO usan nombre canónico de pose.** Los looks existentes están como `C-1.png … C-6.png`, sin identificar la pose. Eso rompe el mapeo de galerías y el N/N. **Pendiente de decisión de la Ama:** renombrar los sets existentes a `miss_doll_<N>_<pose>.png` o dejar el archivo histórico como está y aplicar la convención solo hacia adelante.
- El BLOQUE A y el outfit vienen mezclados en el prompt base histórico (regla 05) → si al escribir un look aparece el bodysuit rosa neón "de fábrica", **es contaminación del Bloque A**: sepáralo.
- Look sin arquitectura de corsé → no es Miss Doll.
- Look sin rosa en ninguna parte → viola su cuota firma.
- Labios de cualquier color que no sea rojo → ADN roto, regenerar.
