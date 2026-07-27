# 👑 Perfil Visual — Anaïs Belland

> Contrato del `outfit-engine`. Creado 27/07/2026 al generalizar el motor.
> Reemplaza a `.agent/skills/anais-outfit-engine/SKILL.md`, que era una **copia empobrecida** del motor de Ele: se llevó el ADN y el workflow, pero **no** el Step 0 anti-repetición, ni el token bloqueado, ni la rotación de poses, ni una biblioteca de siluetas. 147 líneas contra 1.787.

---

## §1 · Identidad y Rutas

| Campo | Valor |
|---|---|
| **Nombre canónico** | Anaïs Belland |
| **Slug** | `anais` |
| **Galería** | `02_Personajes/01_Principales/anais/galeria_looks_anais.md` |
| **Carpeta de imágenes** | `05_Imagenes/anais/look<NUM>_<slug>/` |
| **Convención de nombre** | `anais_look<NUM>_<pose>.png` |
| **Numeración** | correlativa · **Boudoir/Lencería usa prefijo `L`** (L01, L02…), serie separada |
| **Canon profundo (enlace)** | [`01_Principales/anais/CANON_VISUAL_ANAIS.md`](../01_Principales/anais/CANON_VISUAL_ANAIS.md) — **autoridad máxima, prevalece en todo conflicto** *(el `anais-outfit-engine` lo apuntaba a `01_Principales/` sin la subcarpeta: enlace roto, corregido 27/07)* |
| **ADN listo para copiar** | `.agent/skills/anais-outfit-engine/references/dna_v2_3.md` |

---

## §2 · BLOQUE A — ADN Inamovible (V2.3 Vintage Noir Hard-Sync)

> ⚠️ **Copiar el token literal desde `dna_v2_3.md` o del canon §II. Nunca escribirlo de memoria.** Lo de abajo es la especificación de sus componentes, no un sustituto del token.

- **Físico:** *ageless dominant woman in early 40s*, rostro oval aristocrático, pómulos esculpidos elevados, mandíbula definida. **MILF aristocrática — nunca joven, nunca bimbo.**
- **Seña definitoria (OBLIGATORIA en toda imagen, sin excepción):**
  `small classic Old Hollywood beauty mark mole above upper left lip`
- **Cabello:** `honey blonde hair` — **SIEMPRE rubia miel. Sin excepciones, sin variaciones.**
- **Peinado:** pin-waves de Hollywood vintage esculpidas o victory rolls, raya al lado.
- **Maquillaje:** cejas finas arqueadas marrón oscuro estilo 1940s, delineado negro cat-eye con ala alargada, labios rojo carmesí profundo, ojos de párpado pesado.
- **Silueta:** hourglass madura y esbelta con corsé de tightlacing extremo, postura en S.
- **Sin tatuajes. Sin piercings visibles.**
- **Iluminación:** chiaroscuro cinematográfico, estilo George Hurrell, luz de key única, tensión íntima.

**Rasgos que NO se negocian jamás:**

- El **lunar** sobre el labio superior izquierdo.
- El **honey blonde**. Ni golden, ni platinum, ni castaño. Jamás.
- La **edad**: cuarentona ageless. Rejuvenecerla la destruye como personaje.
- **Cero tatuajes, cero piercings.**
- La **expresión**: nunca sonrisa amplia, nunca risa, nunca actitud juguetona.

---

## §3 · Negative Prompt

**Base:** copiar desde `dna_v2_3.md`.

**Léxico prohibido en el POSITIVE** (degrada el registro — canon §VIII):
`sexy` · `hot` · `seductive` · `naked` · `nude` (como desnudez; vale como color) · `provocative` · `tempting`

| Caso | Ajuste | Por qué |
|---|---|---|
| Look de látex canónico | **quitar** `latex` de la lista de negativos | Si no, se pelea con el propio outfit |
| Cualquier pose | asegurar `tattoos, piercings, young woman, teen, wide smile` en negative | Sus tres derivas registradas |

---

## §4 · Poses Canónicas

| # | Nombre canónico | Slug de archivo | Descripción |
|---|---|---|---|
| 1 | **command_standing** | `standing` | Cuerpo entero, tres cuartos, peso en una cadera, mirada fría de mando a cámara, setting completo |
| 2 | **throne_seated** | `seated` | Sentada (silla/chaise/trono coherente con el setting), piernas cruzadas en rodilla, mano en reposabrazos |
| 3 | **three_quarter** | `three_quarter` | Giro de hombro hacia cámara, mirada fría por encima del hombro, hourglass definida por la luz |
| 4 | **domina_closeup** | `closeup` | Plano medio desde el pecho, mirada directa, lunar visible, détalle de escote |

- **Total por look:** 4
- **Fórmula del prompt (particularidad de Anaïs):** `[PREFIJO CINEMATOGRÁFICO] + [BLOQUE A] + [BLOQUE B] + [BLOQUE C]` — lleva un prefijo cinematográfico que los demás personajes no usan.
- **Repertorio de variaciones:** ⚠️ **no existe todavía.** Las 4 poses son fijas. Rotar al menos el ángulo, el nivel de contacto y la relación con el mobiliario para que 4 looks seguidos no se vean idénticos.

---

## §5 · BLOQUE B — Reglas de Vestuario

### 5.1 · Universo de materiales

- **Permitidos:** satén pesado, seda charmeuse, terciopelo italiano, látex de grado clínico, encaje francés, nylon con costura, charol.
- **Prohibidos:** materiales baratos o deportivos; cualquier cosa que lea "casual" o "joven".
- **Lente de identidad:** *tejido noble.* Anaïs es aristocracia, no fetiche sintético — la separa de Ele y de Miss Doll. Un látex suyo es de **grado clínico**, no de club.

### 5.2 · Paleta y reglas cromáticas

- **Paleta:** negro dominante, carmesí, oro imperial `#D4AF37`, champagne, marfil, terciopelo profundo.
- **Reservado al ADN:** el **rojo carmesí de los labios** y el **honey blonde** del pelo.
- **Animal print:** permitido **solo** en tejido noble (seda, terciopelo, látex). Nunca en material barato.
- **Anti-monoblock:** máx. 2 consecutivos.

### 5.3 · Calzado (canon inamovible)

- **Regla:** `12cm black patent leather stiletto pump pointed toe iconic red sole`.
- **Altura exacta:** **12 cm**. Ni más bajo, ni compensado con plataforma.
- **Prohibido:** tacón bajo, **plataforma delantera visible**, zapatilla, flat, wedge.
- **Suela roja: obligatoria.**
- **Atributos obligatorios del token** (los 6): altura en cm · estilo · material · color · forma de puntera · suela roja.

### 5.4 · Prohibiciones absolutas

| Prohibido | Sustituto autorizado | Directiva |
|---|---|---|
| Cabello que no sea honey blonde | honey blonde, siempre | Canon — error crítico |
| Omitir el lunar | lunar sobre labio superior izquierdo | Seña definitoria |
| Tatuajes / piercings visibles | piel limpia | Canon |
| Plataforma delantera visible | stiletto 12cm sin plataforma | Canon calzado |
| Sonrisa amplia / risa / juego | mirada fría de mando | Registro |
| Léxico `sexy`/`hot`/`seductive`… | vocabulario del canon §VIII | Registro |
| Exterior/natural fuera de Viaje | interiores controlados | Coherencia de arquetipo |

> 🧤 **Los guantes SÍ están permitidos en Anaïs** (wrist/elbow/opera, con material y largo especificados). **Esto la distingue de Ele, donde los guantes están derogados.** Es justo el tipo de regla que se corrompía al duplicar motores.

### 5.5 · Campos obligatorios de descripción

Describir **en este orden**:

1. **Prenda principal** — nombre, tejido exacto, color exacto, corte, fit, estructura interna (ballenas, tightlacing, boning).
2. **Prenda secundaria** (si aplica) — misma especificidad.
3. **Medias** (si el look las lleva) — denier, tipo (back-seam nylon, fishnet, sheer), color, con o sin costura.
4. **Calzado** — sus 6 atributos (§5.3).
5. **Accesorios en orden** — guantes (material + largo), joyería (tipo y material: perlas, diamantes negros, pedrería Art Déco), boquilla (sí/no), bolso (Kelly, clutch lacado), complementos de liguero.

> **Regla de especificidad:** cada ítem tan preciso que dos modelos generarían la misma imagen leyendo solo el bloque. *"tacones altos"* ❌ → *"12cm black patent leather stiletto pump pointed toe iconic red sole"* ✅.

---

## §6 · Arquetipos y Metas

| Arquetipo | Descripción | Meta |
|---|---|---|
| **Noche / La Voûte** | La Regenta, negro satén/terciopelo, interior de La Voûte | 25% |
| **Boudoir / Lencería** | Aposentos privados, negligée, merry widow, peignoir, corsetería | 20% |
| **Gala / Premiere** | Alfombra roja, vestidos columna | 15% |
| **Látex / Fetichismo** | Catsuits, corsés overbust de látex, poder fetish refinado | 15% |
| **Sesión Literaria** | Estudio privado, kimono de seda, escritura nocturna | 10% |
| **Animal Print / Autoridad** | Leopardo, serpiente, cebra — solo en tejido noble | 7,5% |
| **Ejecutivo de Poder** | Traje sastre vintage, pencil de cuero, power dressing | 5% |
| **Viaje / Jet Set** | Abrigo de vuelo, lobby 5★, jet privado, yacht | 2,5% |

- **Regla de déficit:** si un arquetipo está bajo meta, el próximo look **debe** ser de esa categoría.
- **Prioridad de desempate:** Noche > Boudoir > Gala > Látex > resto.

---

## §7 · Ventanas Anti-Repetición

| Elemento | Ventana |
|---|---|
| Silueta | ≥ 3 looks del mismo arquetipo |
| Setting / escenario | ≥ 3 looks del mismo arquetipo |
| Modo cromático monoblock | máx. 2 consecutivos |

- **Outfit único:** sí.
- ⚠️ **Esto es nuevo para Anaïs.** Su motor anterior no tenía Step 0: los looks se elegían solo por déficit de arquetipo, sin bloquear siluetas ni settings. Aplicar hacia adelante.

---

## §8 · Cuotas Vivas

| Cuota | Frecuencia | Alcance |
|---|---|---|
| **Lunar visible** | **todas las imágenes** | Sin excepción |
| Suela roja visible | siempre que el calzado se vea | Calzado |

---

## §9 · Banderas Rojas Específicas

- Cabello de cualquier color que no sea `honey blonde` → **error crítico**, regenerar.
- Falta el lunar en algún prompt → ADN roto.
- Calzado sin suela roja, con plataforma, o de menos de 12 cm.
- Aparece léxico prohibido (`sexy`, `hot`, `seductive`, `provocative`, `tempting`, `naked`) en el positive.
- Tatuaje o piercing visible.
- Sonrisa amplia, risa o actitud juguetona.
- Fondo exterior/natural en un arquetipo que no sea Viaje/Jet Set.
- **Materialidad prestada de Ele o Miss Doll** (vinilo de club, PVC barato, neón): Anaïs es tejido noble. Si el outfit parece de la flota de Ele, está mal.
