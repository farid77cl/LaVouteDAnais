---
name: outfit-engine
description: Motor de looks GENÉRICO y modular, válido para cualquier personaje de La Voûte (Ele, Miss Doll, Anaïs Belland, o uno nuevo). Contiene la MAQUINARIA — Step 0 anti-repetición, token bloqueado, ensamblado A/B/C con anclas anti-defecto universales, contrato de archivo para LV-App, linter, git y estadísticas — y lee el ADN y las reglas de vestuario del PERFIL VISUAL del personaje en `02_Personajes/_perfiles_visuales/<slug>.md`. Úsalo cada vez que se pida un look de cualquier personaje. Personaje nuevo = perfil desde la plantilla + entrada en `anclas_universales.json` + entrada en `CharacterProfile` de la app. NUNCA un motor nuevo.
---

# 👠 Outfit Engine — Motor de Looks Multi-Personaje (v2.0)

> 🔧 **v2.0 (12/08/2026) — el motor deja de ser solo doctrina y pasa a tener maquinaria ejecutable.**
> La v1.0 describía el ensamblado con la notación `[BLOQUE A] + [BLOQUE B] + [BLOQUE C]`, y esa notación se escribió **literal** dentro de los 98 prompts de Miss Doll: la app los habría mandado así al generador. La v2.0 agrega (a) un **ensamblador** común, (b) una **librería de anclas anti-defecto** con dueño único y overrides por personaje, (c) el **contrato de archivo** que la app exige, y (d) un **linter** que parsea la galería como la parsea la app. Ele, Miss Doll y Anaïs corren sobre la misma maquinaria; un personaje nuevo entra con tres pasos y hereda todo.
>
> | Pieza | Archivo |
> |---|---|
> | Texto literal de las anclas + registro de personajes | `99_Sistema/scripts/visual/anclas_universales.json` |
> | Ensamblador (`PromptBuilder`) | `99_Sistema/scripts/visual/prompt_builder.py` |
> | Linter (parsea como LV-App) | `99_Sistema/scripts/visual/lint_prompts_personaje.py` |
> | Contrato de nombre de archivo y formato | `.agent/rules/11-contrato-galeria.md` |

Motor **agnóstico de personaje**. Todo lo que aquí se describe es *mecanismo*: vale igual para Ele, Miss Doll, Anaïs o cualquier personaje futuro. Lo que cambia de un personaje a otro — su cuerpo, su ropa, sus poses, sus tabúes — **no vive aquí**: vive en su **perfil visual**.

> 🧬 **La división (directiva Ama 27/07/2026):**
> **BLOQUE A = quién es** (ADN físico) · **reglas de BLOQUE B = cómo se viste** → ambos **por personaje**, en su perfil.
> **La maquinaria = idéntica para todos** → aquí.

## 🚫 Por qué este motor existe (y por qué NO se duplica)

El engine de Ele tiene ~1.800 líneas. Cuando se quiso dar a Anaïs su propio motor, se **copió** — y quedaron **147 líneas**: llegó el ADN, pero **no llegó la maquinaria**. Anaïs se quedó sin Step 0 anti-repetición, sin token bloqueado, sin rotación de poses, sin banderas rojas. Miss Doll nunca tuvo motor: solo una regla de canon.

**Duplicar un motor lo condena a divergir.** Este repo ya vivió eso con los contadores de flota (llegó a haber tres flotas distintas en tres archivos). La respuesta es la misma que allá: **un dueño, muchos punteros.** Un motor, muchos perfiles.

---

## 📥 Entrada obligatoria: el perfil visual

Antes de diseñar **nada**, cargar:

```
02_Personajes/_perfiles_visuales/<slug>.md
```

El perfil es el **dueño único** de: Bloque A · negative prompt · poses canónicas · reglas de vestuario · arquetipos y metas · ventanas anti-repetición · cuotas vivas · banderas rojas propias.

- Si el perfil **no existe** → crearlo desde [`_plantilla_perfil_visual.md`](references/_plantilla_perfil_visual.md) **con la Ama**, sección por sección. No inventar el ADN de un personaje.
- Si una sección del perfil está **vacía** → **detenerse y preguntar**. Improvisar el canon de un personaje es la peor falla posible de este motor.

---

## 🛠️ Workflow Operativo

> **ORDEN OBLIGATORIO:**
> Perfil → Step 0 Anti-Repetición → Arquetipo → BLOQUE B → **escribir los N prompts completos en la galería** → generar → git → estadísticas.
>
> 🔴 **Ninguna imagen se genera antes de que los N prompts completos estén escritos en la galería del personaje.** N lo dice el perfil (§4). Esta regla no admite excepción, ni por urgencia, ni por "es solo un look".

---

### Paso 0 · Regla Transversal Anti-Repetición

Antes de proponer cualquier look, consultar la galería del personaje y **bloquear** según sus ventanas (perfil §7) y **contar** sus cuotas vivas (perfil §8).

**Protocolo:**
1. Consultar los últimos N looks **del mismo sub-arquetipo** (N = ventana del perfil §7).
2. Listar qué **siluetas** y **settings** quedan bloqueados.
3. Consultar los últimos looks **globales** para las reglas de composición (ej. anti-monoblock: máx. 2 consecutivos).
4. Contar cada **cuota viva** del §8. Si una está vencida → este look **debe** cumplirla.
5. Recién entonces avanzar.

**El resultado del Paso 0 se escribe explícitamente** antes de diseñar: *"Bloqueadas: siluetas X, Y · settings Z · monoblock NO disponible · cuota animal print VENCIDA → obligatoria"*. Un Paso 0 que no deja rastro escrito es un Paso 0 que no se hizo.

---

### Paso 1 · Arquetipo por déficit

Contar los looks por arquetipo en la galería y comparar contra las metas del perfil (§6). **El arquetipo del look nuevo lo decide el déficit, no el gusto.** Si hay varios en déficit, desempatar con la prioridad del perfil.

---

### Paso 2 · BLOQUE B — el outfit del día

Diseñar el outfit contra las **reglas de vestuario del perfil (§5)**, y validarlo antes de escribir una línea de prompt:

- ¿El material está en el universo permitido (§5.1)? ¿Pasa el **lente de identidad**?
- ¿La paleta respeta las reglas vigentes y no toca los colores reservados al ADN (§5.2)?
- ¿El calzado cumple el canon, con **todos** sus atributos obligatorios (§5.3)?
- ¿Hay alguna prenda de la lista de prohibiciones absolutas (§5.4)? → sustituir por el autorizado.
- ¿Están nombrados **todos** los campos obligatorios de descripción (§5.5)?

El BLOQUE B se escribe **una sola vez** con máximo detalle — material exacto, color exacto, corte, textura, brillo, ajuste, y cada accesorio con su posición en el cuerpo — y se copia **idéntico** en los N prompts.

> 🔒 **Token de vestuario bloqueado.** Las prendas complejas (opaco vs. sheer, capas, transparencias, arneses) se anclan una vez y se repiten **carácter por carácter**. Parafrasear entre poses es la causa registrada de que una prenda cambie de opacidad o desaparezca a mitad de un set.

---

### Paso 3 · Escritura de los N prompts en la galería

**Composición conceptual de cada prompt:** `BLOQUE A` (ADN) + `BLOQUE B` (outfit) + `BLOQUE C` (pose, anclas y setting).

| Bloque | Qué es | Varía entre poses |
|---|---|---|
| **A** | ADN del personaje (perfil §2) | ❌ **Nunca.** Copiado textual |
| **B** | Outfit del día (Paso 2) | ❌ **Nunca.** Copiado textual |
| **C** | Pose + anclas del slot + setting | ✅ Es lo único que varía |

> 🚨 **ESA FÓRMULA ES UNA INSTRUCCIÓN DE ENSAMBLADO, NO TEXTO.**
> Lo que se escribe dentro del bloque de código de cada pose es el prompt **final, expandido y autocontenido**: el ADN completo, el outfit completo, las anclas y el setting completo, uno detrás de otro. **Un `[BLOQUE A]` entre corchetes dentro de un prompt es un bug crítico**, no una abreviatura.
>
> **La cicatriz (11/08/2026):** los 98 prompts nuevos de Miss Doll se escribieron literalmente como `[BLOQUE A] + [BLOQUE B], full body standing shot…, [BLOQUE C setting]`. La galería *se veía impecable*. Pero LV-App extrae el bloque de código tal cual y se lo manda al generador: 98 imágenes se habrían pedido **sin cara, sin cuerpo, sin pelo, sin ropa, sin escenario y sin negativo**. Mismo modo de falla que el placeholder `[ADN]` de Anaïs cuatro días antes. Revisar a ojo no lo detectó — lo detectó parsear el archivo como lo parsea la app.
>
> **Herramienta, no fuerza de voluntad:** el ensamblado lo hace `99_Sistema/scripts/visual/prompt_builder.py` (`PromptBuilder(slug).build(...)`), y `lint_prompts_personaje.py` lo verifica. Escribir los prompts a mano está permitido; entregarlos sin pasar el linter, no.

Reglas de escritura:
- El **BLOQUE A se copia del perfil**, nunca se escribe de memoria ni se resume.
- El **negative prompt** se arma con `PromptBuilder.build_negative(base_del_perfil_§3)`: base propia del personaje **+ la capa universal** anti-collage/anatomía/selfie. Va en el look como `**Negative Prompt:** \`…\`` (backticks en una sola línea) — **es la única forma que la app reconoce**.
- Las poses salen del perfil (§4); si tiene repertorio de variaciones, **rotar**: una variación por slot, sin repetir dentro de los últimos looks. Las N poses de un look deben sentirse como **una sesión real**, no como la misma foto N veces.
- **Prompts en inglés, siempre.**
- **Prohibido el metalenguaje multi-toma** (`in every shot`, `identical across all poses`): es causa registrada de collages. La consistencia entre poses se logra copiando el token, no pidiéndosela al generador.

---

### 🎬 Qué es cada slot de cámara (los 7, para las tres muñecas)

**Dos de los nombres engañan: son históricos.** La pose evolucionó y el nombre se quedó. Renombrar el slot por personaje está permitido (Ditzy → *Glacial Command* → *Sovereign Gaze*); **cambiar su propósito de encuadre, no.**

| Slot | Qué es |
|---|---|
| 1 · Standing | Cuerpo entero de pie, de frente. Outfit completo + calzado visibles. |
| 2 · Back View | Espalda a cámara. Arquitectura trasera de la prenda + calzado. |
| 3 · Seated | Sentada, con el peso íntegro en el asiento nombrado. |
| 4 · Side Profile | Perfil o tres cuartos lateral. Se lee la silueta. |
| **5 · Ditzy** | ⚠️ **NO es "poner cara de ditzy"** — el nombre describía la expresión bimbo original de Ele. Es el **plano medio WAIST-UP**: rostro grande y nítido + **busto/décolleté prominente en el frame inferior, SIEMPRE** + detalle del outfit superior legible · **UNA sola mano** en cuadro · **mirada FUERA de cuadro**. ⛔ NO plano americano knee-up, NO cuerpo entero. |
| **6 · POV** | ⚠️ **NO es un point-of-view literal** ni una cámara a la altura de alguien arrodillado. Es un **RETRATO SENSUAL DE INSTAGRAM** (thirst-trap de influencer): **mira a la cámara**, medio cuerpo, cara protagonista + décolleté abajo, **una sola mano**, `a single woman alone`. ⛔ Prohibido en el positive: `first-person POV`, `point of view`, `looking down over own body`, `overhead`, `selfie`, `phone` — el generador los lee LITERAL. |
| 7 · Odalisque | Figura baja: reclinada o sentada en el suelo, según el canon del personaje. |

**🔑 El diferenciador duro Ditzy ≠ POV:** el slot 5 mira **fuera** de cuadro, el slot 6 mira **al lente**. Sin eso las dos tomas salen casi idénticas — la Ama lo levantó el 02/08/2026 (*"salen casi iguales el 90%"*) y se arregló en el motor de Ele.

> 🩹 **Cicatriz doble (12/08/2026).** Estas definiciones son de **mayo y junio de 2026** — `.agent/rules/06-generacion-imagenes.md` §5 y §9 · `pose_repertoire_v5.md` §5-§6 · `dna_v3_5.md`. Ele las cumple desde entonces. Al estandarizar las 7 poses el **05/08** para Miss Doll y Anaïs se escribieron **mal** en sus perfiles ("primer plano frío", "cámara de sub arrodillado"), y el fix del diferenciador del 02/08 **nunca se propagó fuera de Ele**. Resultado medido: el Ditzy de Anaïs volvió a salir casi idéntico entre looks, dos meses después de haberse cerrado el caso. **Lección: un fix que vive en el motor de un solo personaje no es un fix, es un parche local.** Por eso el significado de los slots vive ahora acá y en `anclas_universales.json → significado_de_los_slots`, no en cada perfil.

---

### 🔒 Anclas anti-defecto universales (el candado del motor)

Cada defecto que este repo pagó con cuota quemada dejó un **ancla afirmativa en el positive** — porque el generador **ignora el negative con frecuencia**. Esas anclas son **maquinaria, no material de personaje**: valen para todos.

**Dueño único del texto literal:** `99_Sistema/scripts/visual/anclas_universales.json`. Nadie las copia; el builder las lee y el linter las verifica.

| Ancla | Slots | Defecto que mata |
|---|---|---|
| `SINGLE_FRAME` | todos | Collage / hoja de contactos / marco con su imagen dentro de la escena |
| `GARMENT_CONSISTENCY` | todos | La prenda cambia de escote/manga/ruedo entre poses |
| `ANATOMY_FULL` | cuerpo entero | Tercera pierna, manos de más |
| `ANATOMY_CLOSE` | primer plano | Dedos fusionados con la mano cerca del lente |
| `FRONT_ANCHOR` | Standing | Standing salía de espalda (era el único slot sin ancla de orientación) |
| `BACK_ANCHOR` | Back View | Bata/kimono/blazer al revés: el generador rota la prenda de frente abierto |
| `SEAT_ANCHOR` | Seated | La figura termina apoyada en una isla/mesa cercana |
| `RECLINE_ANCHOR` | Odalisque | La odalisca reclinada sale sentada |
| `FLOOR_SEAT_ANCHOR` | Odalisque *(variante)* | Para personajes cuyo Odalisque es **sentada en el suelo** |
| `LEVEL_HORIZON` | Odalisque | Encuadre rotado 90° |
| `FOOTWEAR_ECHO` | Back View · Odalisque | El zapato cambia de modelo cuando queda lejos del bloque que lo describe |
| `SINGLE_HAND_CLOSE` | Ditzy · POV | En encuadre cerrado solo cabe UNA mano: forzar dos metía una mano fantasma o deformada (Ama 30/06/2026) |
| `GAZE_OFF_LENS` · `GAZE_TO_LENS` | Ditzy / POV | El diferenciador duro entre los dos slots (Ama 02/08/2026) |
| `POV_NO_DEVICE` · `SINGLE_SUBJECT` | POV | Aparece un teléfono (selfie) o una segunda mujer |

**Cómo se personaliza sin duplicar el motor:** el perfil declara en su **§10** qué anclas sustituye y por qué; el JSON lo registra en `personajes.<slug>.overrides`. Ejemplo real: el slot Odalisque de Miss Doll es *Throne en Suelo* — sentada en el piso, no reclinada — así que `RECLINE_ANCHOR` se sustituye por `FLOOR_SEAT_ANCHOR`. **Aplicar la letra del ancla de Ele ahí habría contradicho el canon de Miss Doll**: cuando la letra y el propósito divergen, se sirve el propósito y se deja escrito.

---

### 📄 Contrato de archivo — lo que la app realmente lee

La galería no es un documento: es **la entrada de un parser** (`GitRepository.parseMarkdown` de LV-App). Estructura obligatoria por look, **en este orden**:

````markdown
## <emoji> Look <N>: <Título Descriptivo> (<fecha> · batch <X>-<Y> "<Tema>" · <Arquetipo>)
- **Ubicacion:** `05_Imagenes/<slug>/look<N>_<slug_titulo>/`
- **Tags:** #<arquetipo> #<material> #<personaje> #batch… #V7poses

… BLOQUE A / BLOQUE B / Setting / negative de referencia (documentación legible) …

### 📸 Imágenes (<n>/7 — Materializado | Materializado parcial | Pendiente)

| Standing | Back View | Seated | Side Profile | <slot 5> | POV | Odalisque |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| [📸 View](…) | ⏳ Pendiente | … |

### 1. Standing — <nombre de la pose>
```text
<prompt FINAL expandido>
```
… las 7, numeradas 1..7 …

**Negative Prompt:** `<bloque negativo completo, una sola línea>`
````

Las cinco que **rompen en silencio** si se ignoran:

1. **Metadata antes del primer `###`.** Si `### 📸` aparece antes de `Ubicacion`/`Tags`, la app se queda sin ubicación ni categoría (le pasó a 60 looks de Ele).
2. **La etiqueta del negativo es literal:** solo `**Negative Prompt:**` con el contenido entre backticks se ingiere. Cualquier otra redacción (`**Negative (base del perfil §3):**`) es invisible → el look se genera **sin negativo**.
3. **Numerar la pose (`### 1. …`).** El nombre solo no basta: `Sovereign Gaze` y `Glacial Command` se resuelven por el número cuando el matcher de texto no los alcanza. Sin número, dos slots pueden colapsar en uno y el `REPLACE` de la base borra el otro.
4. **Fence de apertura y cierre cada uno en su línea.** Un fence en una sola línea mezcla prompts entre poses y entre looks (pasó en 1.167 prompts).
5. **El nombre del archivo es el interruptor.** La app filtra por subcadena en la ruta, no por lista. Ver `.agent/rules/11-contrato-galeria.md` §9bis antes de archivar nada.

**Verificación obligatoria antes de cerrar cualquier batch, de cualquier personaje:**

```bash
python 99_Sistema/scripts/visual/lint_prompts_personaje.py          # todos
python 99_Sistema/scripts/visual/lint_prompts_personaje.py <slug>   # uno
```

Parsea la galería **con el mismo algoritmo que la app** y reporta lo que la app va a ingerir de verdad, no lo que el archivo aparenta. Ningún batch se commitea con el linter en rojo.

---

### 🧩 Alta de un personaje nuevo (la parte modular)

Tres pasos, ninguno de ellos "escribir un motor":

1. **Perfil visual** — copiar [`references/_plantilla_perfil_visual.md`](references/_plantilla_perfil_visual.md) a `02_Personajes/_perfiles_visuales/<slug>.md` y rellenarlo **con la Ama**, sección por sección. Sin §2 (ADN) y §3 (negative) no hay look.
2. **Registro en el motor** — una entrada en `99_Sistema/scripts/visual/anclas_universales.json` → `personajes.<slug>`: nombre, nombre y slug del slot 5, ruta de galería, carpeta e infijo de imagen, y los `overrides` de ancla que su canon exija. Con eso el builder y el linter ya lo soportan.
3. **Registro en la app** — una entrada en `CharacterProfile.ALL` del repo `farid77cl/LV-App` (subcadenas gatillo, carpeta, prefijo, `slot5Name`, alias de pose) + su offset de `PrimaryKey`. **Sin este paso la galería existe pero la app no la ve.**

El personaje hereda gratis: Step 0, token bloqueado, las 7 categorías de cámara, las anclas anti-defecto, el contrato de archivo y el linter.

---

### Paso 4 · Generación

Generar con el positive + negative escritos. Si una pose sale con el ADN roto (otra cara, otro pelo, otra persona), **se regenera con el negative reforzado** — no se acepta ni se "arregla" describiendo distinto.

### Paso 5 · Registro y git

Imágenes a la carpeta del personaje con su convención de nombre (§1). Regenerar galerías/índices afectados. Commit con prefijo `Ele:` y el trailer de coautoría.

### Paso 6 · Estadísticas

Actualizar el conteo de arquetipos y el tracker de poses. Un look sin registrar es un look que no existe para el próximo Paso 0 — y rompe la anti-repetición del siguiente.

---

## 🛡️ Blindaje contra Racionalizaciones

Excusas **PROHIBIDAS**, para cualquier personaje:

| Excusa | Realidad |
|---|---|
| "Genero la imagen y documento el prompt después." | **ERROR CRÍTICO.** Los N prompts van escritos en la galería ANTES de generar. |
| "El BLOQUE A es siempre igual, no hace falta copiarlo en cada prompt." | **ERROR.** Se copia textual en los N. Omitirlo es como se pierde el ADN. |
| "Ajusté el BLOQUE B en una pose porque la pose lo requería." | **ERROR.** Solo varía el BLOQUE C. |
| "No puse negative prompt porque el generador no lo pedía." | **ERROR.** Es la barrera activa contra la deriva del ADN. |
| "Esta pose es difícil, por eso salió distinta la persona." | **ERROR.** La dificultad no justifica ADN roto. Se regenera. |
| "Omití un rasgo del ADN para un look más limpio." | **ERROR.** El ADN no se edita por estética. |
| "Este personaje es nuevo, improviso su canon y lo afinamos después." | **ERROR.** Sin perfil no hay look. Se crea el perfil con la Ama primero. |
| "Copié el motor de Ele y le cambié el ADN." | **ERROR.** Eso es exactamente lo que dejó a Anaïs en 147 líneas. Se usa ESTE motor + un perfil. |
| "No actualicé las estadísticas, era solo un look." | **ERROR.** Cada look mueve los porcentajes y el próximo Paso 0. |
| "Dejé `[BLOQUE A]` en el prompt: se entiende que ahí va el ADN." | **ERROR CRÍTICO.** Lo entiende un humano; la app manda el texto **literal** al generador. Cicatriz del 11/08/2026: 98 prompts inservibles. |
| "El negativo está escrito arriba del look, se ve perfecto." | **ERROR.** Solo `**Negative Prompt:** \`…\`` se ingiere. Cualquier otra etiqueta = look generado sin negativo. |
| "Revisé la galería y se ve bien." | **ERROR.** Verificar el artefacto, no el reporte: se corre `lint_prompts_personaje.py`, que la parsea como la parsea la app. |

## 🚩 Banderas Rojas — DETENTE

- Vas a generar sin tener los N prompts escritos en la galería.
- **Un prompt contiene corchetes `[BLOQUE …]`, `[ADN]`, `[SETTING]` o cualquier placeholder** → el prompt no está escrito, está esbozado.
- **El look no tiene una línea `**Negative Prompt:** \`…\``** al cierre.
- **Las poses no están numeradas 1..N** en su encabezado.
- Un prompt no lleva el BLOQUE A completo, copiado del perfil.
- El BLOQUE B difiere entre dos poses del mismo look.
- Aparece metalenguaje multi-toma (`in every shot`, `identical across all poses`) dentro de un prompt.
- No hiciste el Paso 0, o lo hiciste "de cabeza" sin dejarlo escrito.
- Estás usando el ADN de un personaje para otro.
- Estás por crear un motor nuevo en vez de un perfil nuevo.
- **Estás por copiar el texto de un ancla a un archivo nuevo** en vez de apuntar a `anclas_universales.json`.
- El outfit incluye algo de la lista de prohibiciones absolutas del perfil (§5.4).
- El calzado no nombra todos sus atributos obligatorios, o alguna pose se saltó el canon de calzado.
- **Más las banderas propias del personaje (perfil §9).**

**REGLA DE ORO:** violar la letra de este motor es violar el ADN del personaje.

---

## 📂 Recursos

- [`references/_plantilla_perfil_visual.md`](references/_plantilla_perfil_visual.md) — esquema de perfil (para personajes nuevos).
- Perfiles vigentes: `02_Personajes/_perfiles_visuales/`.
- Bibliotecas de siluetas / specs por sub-arquetipo: enlazadas desde cada perfil (§6). Son **material del personaje**, no del motor.
