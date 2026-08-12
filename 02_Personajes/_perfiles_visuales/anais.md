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
| **Convención de nombre** | `anais_<NUM>_<pose>.png` *(normalizado 05/08/2026 — antes `anais_look<NUM>_<pose>.png`; afecta L01-L04 ya materializados, renombrado pendiente en la máquina visual)* |
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

> **Estandarizado 05/08/2026 (directiva Ama):** las 3 muñecas comparten las mismas **7 categorías de cámara** que Ele — mismo slot, mismo orden, mismo propósito de encuadre — el motor de poses y la app las tratan con una sola taxonomía. El contenido/expresión de cada slot es 100% propio de Anaïs. La línea **Boudoir** (`L01…`, 4 poses: `boudoir_standing/chaise_seated/mirror_profile/intimate_closeup`) queda **fuera de este remapeo** — es su propio submundo de lencería, con su propia numeración y taxonomía; no se toca acá.

**7 poses (mismo slot que Ele, contenido de Anaïs):**

| # | Categoría (universal) | Nombre de pose | Slug de archivo | Descripción |
|---|---|---|---|---|
| 1 | Standing | command_standing | `standing` | Cuerpo entero, tres cuartos, peso en una cadera, mirada fría de mando a cámara, setting completo |
| 2 | Back View | mirror_back *(nueva — 05/08)* | `back_view` | De espaldas ante un espejo del set (tocador, salón), guante trazando la curva desnuda de la espalda, mirada por sobre el hombro hacia el reflejo — nunca directo a cámara |
| 3 | Seated | throne_seated | `seated` | Sentada (silla/chaise/trono coherente con el setting), piernas cruzadas en rodilla, mano en reposabrazos |
| 4 | Side Profile | three_quarter | `side_profile` | Giro de hombro hacia cámara, mirada fría por encima del hombro, hourglass definida por la luz |
| 5 | **Sovereign Gaze** *(slot Ditzy de Ele, renombrado — su registro es dominio, no vacío)* | domina_closeup | `sovereign_gaze` | Plano medio desde el pecho, mirada directa, lunar visible, detalle de escote |
| 6 | POV | kneeling_pov *(nueva — 05/08)* | `pov` | Vista desde abajo, como si el lector estuviera arrodillado ante ella — su mirada fría cae sobre el lente desde ese ángulo |
| 7 | Odalisque | chaise_command *(nueva — 05/08)* | `odalisque` | Reclinada en el chaise longue de su despacho o salón, vestuario de gala/látex de grado clínico — misma arquitectura que su Boudoir pero sin lencería |

- **Total por look:** 7
- **Fórmula del prompt (particularidad de Anaïs):** `[PREFIJO CINEMATOGRÁFICO] + [BLOQUE A] + [BLOQUE B] + [BLOQUE C]` — lleva un prefijo cinematográfico que los demás personajes no usan.
- **Repertorio de variaciones:** las 4 poses originales (command_standing/throne_seated/three_quarter/domina_closeup) ya materializadas en L01-L04 mantienen su nombre y contenido — solo se les asigna categoría universal por alias, no se regeneran. Las 3 nuevas (mirror_back/kneeling_pov/chaise_command) se estrenan desde el próximo look. Rotar al menos el ángulo, el nivel de contacto y la relación con el mobiliario para que looks consecutivos no se vean idénticos.

---

## §5 · BLOQUE B — Reglas de Vestuario

### 5.1 · Universo de materiales

> ✏️ **Ampliado 11/08/2026 (Ama).** · ✏️ **Pieles agregadas 11/08/2026 (Ama: "el uso de pieles al vestuario recurrente").**

- **Permitidos:** satén pesado, seda charmeuse, terciopelo italiano, látex de grado clínico, encaje francés, nylon con costura, charol, **cuero** (guante fino, cinturón ancho, abrigo — cuero de sastrería/lujo, nunca de motociclista), **látex estándar de alto brillo** (además del de grado clínico, para looks fetish más directos), **🦊 pieles** (ver 5.1b).
- **Prohibidos:** materiales baratos o deportivos; cualquier cosa que lea "casual" o "joven".
- **Lente de identidad:** *tejido noble.* Anaïs es aristocracia, no fetiche sintético — la separa de Ele y de Miss Doll. El látex y el cuero se usan con acabado impecable/pulido, nunca de estética industrial o club barato.

### 5.1b · 🦊 Pieles — material recurrente (Ama 11/08/2026)

La piel es **la materialidad que más literalmente dice "aristocracia de los años 40"**: pesa, se hereda, no se compra en una tienda. Entra como **capa recurrente**, no como novedad ocasional.

**Formas autorizadas** (siempre como capa/accesorio sobre el look, nunca como prenda base):

| Forma | Token en inglés | Notas |
|---|---|---|
| Estola al hombro | `fur stole draped over one shoulder` | La forma reina — deja la cintura a la vista |
| Capa corta / capelet | `short fur capelet` | Cae sobre el escote, no lo tapa |
| Abrigo abierto | `full-length fur coat worn open` | **Siempre abierto**, ver regla de silueta |
| Cuello y puños | `fur collar and cuffs` | Sobre abrigo de sastrería o kimono |
| Ribete | `fur-trimmed peignoir / fur-trimmed opera coat` | La entrada natural al arquetipo Boudoir |
| Manguito | `fur muff` | Vintage puro; **incompatible con el token de uñas** (manos tapadas, ver §5.4) |
| Manta sobre mueble | `fur throw over the chaise longue` | La piel como parte del escenario, no del cuerpo |

**Tipos:** visón (`mink`), zorro plateado (`silver fox`), zorro ártico (`arctic fox`), marta (`sable`), astracán / cordero persa (`astrakhan`, `Persian lamb`), chinchilla. Rotarlos: no repetir el mismo tipo en dos looks consecutivos con piel.

**🔴 Regla de silueta (la que importa):** la piel **se superpone, nunca reemplaza**. El ADN de Anaïs es el hourglass de tightlacing en postura en S — un abrigo cerrado lo borra y mata el look. Por eso: abrigo **siempre abierto**, estola **caída del hombro o sostenida en el codo**, y en toda pose donde aparezca piel el prompt debe dejar explícita **la cintura ceñida visible bajo la capa**.

**Diferencia con el animal print (§5.2):** el print es un **acabado estampado sobre tejido noble**; la piel es **pelo real, con volumen y peso**. Son dos cosas distintas y **no cuentan como la misma cuota**. Pueden coexistir en un look, pero no en la misma prenda (leopardo estampado + estola de zorro sí; "piel estampada de leopardo" no).

**Prohibido:** piel que lea deportiva o moderna (parka con capucha de pelo, chaleco de peluche, forro polar), piel sintética de aspecto barato, look 100% cubierto de piel (traje entero), y piel en un arquetipo con escenario exterior/natural (§5.4 lo prohíbe igual).

### 5.2 · Paleta y reglas cromáticas

> ✏️ **Ampliada 11/08/2026 (Ama) — resuelve el desajuste con `CANON_VISUAL_ANAIS.md` §I, que ya traía azul medianoche/verde esmeralda sin que estuvieran aquí.** Esta tabla queda como dueño único de la paleta; `CANON_VISUAL_ANAIS.md` §I apunta aquí de ahora en más.

- **Paleta:** negro dominante, carmesí, oro imperial `#D4AF37`, dorado clásico, champagne, marfil, terciopelo profundo, gris perla, azul medianoche, verde esmeralda, **borgoña/vino profundo**, **bronce/cobre antiguo**, **plata antigua**, **rosa polvo/dusty rose**.
- **Reservado al ADN:** el **rojo carmesí de los labios** y el **honey blonde** del pelo.
- **Animal print:** ya NO es arquetipo (ver §6) — es acabado transversal, permitido **solo** en tejido noble (seda, terciopelo, látex, cuero). Nunca en material barato. Cuota pendiente de definir.
- **Anti-monoblock:** máx. 2 consecutivos.

### 5.3 · Calzado (canon inamovible)

> ✏️ **Ampliado 11/08/2026 (Ama) — de un solo modelo a 3 estilos, con la misma regla medias+puntera de Ele (`feedback_medias_calzado_reglas`, auto-memoria).**

- **Altura exacta:** **12 cm**, sin excepción — no se abre a rango (se descarta el "10-12cm" que traía `CANON_VISUAL_ANAIS.md` §VI, ese documento queda desactualizado en esto).
- **Estilos permitidos (3):**
  1. `stiletto pump pointed toe` — el original, punta cerrada.
  2. `peep-toe stiletto pump` — **nuevo.** Punta abierta permitida SOLO si el look no lleva medias (ver regla siguiente).
  3. `knee-high stiletto boot` (bota bajo rodilla, punta cerrada) — **nuevo.**
- **🔴 Regla medias + puntera (idéntica a Ele):** si el look lleva medias, el calzado **debe** ser de puntera cerrada (pump o bota). El peep-toe **queda prohibido en cualquier look con medias**, sin excepción.
- **Prohibido:** tacón bajo, **plataforma delantera visible**, zapatilla, flat, wedge.
- **Suela roja: obligatoria** en los tres estilos.
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
>
> ✏️ **Conflicto detectado 11/08/2026, corrección revertida por la Ama — "guantes sin dedos NO".** Los guantes de Anaïs siguen siendo los normales de siempre (opera length hasta el codo, cerrados, sin variante sin-dedos forzada). El error no era el guante — era mío, por meter el token de manicura de todos modos en un prompt donde las manos van tapadas. **Regla correcta: si el look lleva guantes que cubren los dedos, se OMITE el token de uñas de mano en ese prompt** (no se ve, no se describe). El token de manicura solo va cuando las manos están visiblemente desnudas.

### 5.5 · Campos obligatorios de descripción

Describir **en este orden**:

1. **Prenda principal** — nombre, tejido exacto, color exacto, corte, fit, estructura interna (ballenas, tightlacing, boning).
2. **Prenda secundaria** (si aplica) — misma especificidad.
3. **Medias** (si el look las lleva) — denier, tipo (back-seam nylon, fishnet, sheer), color, con o sin costura.
4. **Calzado** — sus 6 atributos (§5.3).
5. **Capa de piel** (si el look la lleva) — forma (estola/capelet/abrigo abierto/cuello y puños/ribete/manguito), tipo de pelo (visón, zorro plateado, marta, astracán, chinchilla), color, **y cómo cae** (hombro, codo, abierta) dejando la cintura ceñida visible. Ver §5.1b.
6. **Accesorios en orden** — guantes (material + largo), joyería (tipo y material: perlas, diamantes negros, pedrería Art Déco), boquilla (sí/no), bolso (Kelly, clutch lacado), complementos de liguero.

> **Regla de especificidad:** cada ítem tan preciso que dos modelos generarían la misma imagen leyendo solo el bloque. *"tacones altos"* ❌ → *"12cm black patent leather stiletto pump pointed toe iconic red sole"* ✅.

---

## §6 · Arquetipos y Metas

> 🔄 **RESET 11/08/2026 (Ama: "partamos de cero").** Auditoría de los 40 looks existentes encontró que ~20 de ellos usaban etiquetas ad-hoc que no mapean a esta tabla ("High-Fashion/Matriarch", "Corporate Power/Exotic", "Night Gowns/Exotic", etc.) — la regla de déficit llevaba meses siendo inaplicable porque casi la mitad de la galería no se podía contar. **Los Looks 1-40 quedan como legado, sin reclasificar ni retrofitear.** El conteo de cuota **reinicia en cero desde el Look 41**.
>
> **Segunda pasada, misma fecha:** la Ama sacó **Gala/Premiere** y **Viaje/Jet Set** de la tabla, y corrigió que **Animal Print no es un arquetipo** — es un acabado/patrón transversal que se aplica sobre cualquier arquetipo (mismo tratamiento que en Ele: cuota "1 de cada 8 looks", no una categoría que compite por el mismo 100%). Sale de esta tabla; su tratamiento como cuota de paleta/materialidad queda **pendiente de definir** en la revisión de §5 que sigue. Las cinco categorías que quedan se reescalaron proporcional a como estaban (misma relación de peso, ahora sumando 100%).

| Arquetipo | Descripción | Meta |
|---|---|---|
| **Noche / La Voûte** | La Regenta, negro satén/terciopelo, interior de La Voûte. **Medias de red de uso casi regular en este arquetipo (Ama 11/08/2026)** — no en cada look, pero frecuente; puntera cerrada obligatoria cuando aparecen (regla §5.3) | 33% |
| **Boudoir / Lencería** | Aposentos privados, negligée, merry widow, peignoir, corsetería | 27% |
| **Látex / Fetichismo** | Catsuits, corsés overbust de látex, poder fetish refinado | 20% |
| **Sesión Literaria** | Estudio privado, kimono de seda, escritura nocturna | 13% |
| **Ejecutivo de Poder** | Traje sastre vintage, pencil de cuero, power dressing | 7% |

- **Regla de déficit:** si un arquetipo está bajo meta, el próximo look **debe** ser de esa categoría. Conteo empieza en Look 41, no antes.
- **Prioridad de desempate:** Noche > Boudoir > Látex > Sesión Literaria > Ejecutivo.
- **Etiquetado obligatorio:** el campo `**Arquetipo:**` de cada look nuevo debe usar **textualmente** uno de los 5 nombres de esta tabla — nada de variantes ad-hoc ("Exotic", "Noir Glamour", "High-Fashion..."), esa fue la causa raíz del desorden. **Gala/Premiere y Viaje/Jet Set no desaparecen del todo** — si vuelven, es como escenario/paleta dentro de uno de los 5 arquetipos, no como categoría propia; a definir cuando se necesite.

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
| **🦊 Pieles** *(nueva 11/08/2026)* | **≥ 1 de cada 4 looks nuevos** | Transversal a todos los arquetipos. Chequeo pre-diseño: si los últimos 3 looks no llevaron piel, el que se está diseñando **debe** llevarla. No repetir el mismo tipo (visón/zorro/marta/astracán/chinchilla) en dos apariciones consecutivas. Ver §5.1b |

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
- **Piel que borra la cintura** (abrigo cerrado, look enteramente cubierto de pelo) → rompe el hourglass del ADN, regenerar. La piel va **abierta o caída**, con la cintura ceñida explícita en el prompt (§5.1b).
- **Piel de registro deportivo o moderno** (capucha con pelo, chaleco de peluche, sintética barata) → materialidad prestada, mismo error que el vinilo de club.

---

## §10 · Ensamblado y Anclas (contrato con el motor)

> 🔧 **Agregado 12/08/2026 con el `outfit-engine` v2.0.** Esta sección NO define nada nuevo del personaje: declara **cómo se ensamblan sus prompts** y qué anclas anti-defecto le aplican. El texto literal de las anclas vive en `99_Sistema/scripts/visual/anclas_universales.json` (dueño único) — aquí se **apunta**, jamás se copia.

| Campo | Valor |
|---|---|
| **Registro en el motor** | `anclas_universales.json` → `personajes.anais` |
| **Nombre del slot 5** | `Sovereign Gaze` |
| **Ensamblador** | `PromptBuilder("anais").build(bloque_a, bloque_b, slot, pose, setting)` |
| **Negative del look** | `PromptBuilder("anais").build_negative(<base del §3 de arriba>)` — base propia **+ capa universal** anti-collage/anatomía/selfie |
| **Verificación obligatoria** | `python 99_Sistema/scripts/visual/lint_prompts_personaje.py anais` |

**Anclas por slot:** las del mapa por defecto del motor, sin overrides.

> 🧤 Su BLOQUE B suele llevar guantes de ópera: el `FOOTWEAR_ECHO` aplica igual, pero el **token de uñas de mano se omite** cuando los guantes cubren los dedos (§5.4).
>
> 🩹 **Corregido el 12/08/2026:** sus 14 looks nuevos no tenían `Ubicacion`, ni `Tags`, ni `**Negative Prompt:**` — **las 98 poses se estaban generando sin negativo** (50 imágenes ya materializadas así). Agregados los tres campos, el tracker medido contra el índice de git, y las anclas anti-defecto en los 98 prompts.
>
> ⚠️ **Su slot 5 se resuelve por el NÚMERO de la pose**, no por el nombre: el matcher de la app no alcanza `Sovereign Gaze` y sin el `5.` del encabezado colapsaría con POV.

🚨 **Cada prompt de la galería va FINAL Y EXPANDIDO.** El ADN completo, el outfit completo, las anclas y el setting, uno detrás de otro dentro del bloque de código. Un `[BLOQUE A]` entre corchetes dentro de un prompt no es una abreviatura: es un prompt roto que la app manda tal cual al generador.
