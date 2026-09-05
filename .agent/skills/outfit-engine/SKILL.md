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

---

## 🖥️ v3.0 (29/08/2026) — el motor es un PROGRAMA, y se entra por una sola puerta

> **Ama, 29/08/2026:** *"me molesta que el outfit engine no sea un programa, una app como tal si ya está en un 80% como app. lo cual está bien porque nos da estabilidad, escalabilidad"*.
>
> Tenía razón, y el 20% que faltaba estaba concentrado en un sitio: **generar un batch era escribir un programa.** Medido sobre `gen_lenceria_808_812.py` — de sus 158 líneas, **~140 eran datos** y ~18 el bucle que los emitía, y ese bucle se reescribía a mano en cada batch, con variaciones. De ahí salió el defecto del **Look 801**: corrió su propio bucle y entregó cuatro poses sin `GARMENT_CONSISTENCY`, sin `PHOTOREAL_LOCK` y sin ancla de orientación. Además cada script se inventaba su **propio esquema de datos** (el `META` de Ele tenía 3 campos, el de Anaïs 5, Miss Doll usaba diccionarios sueltos), y por eso derivaban.

**Una sola puerta de entrada — `99_Sistema/scripts/visual/outfit.py`:**

| Comando | Qué hace |
|---|---|
| `outfit.py generar <batch.json>` | **Emite un batch de looks desde DATOS.** Nunca más un script por batch |
| `outfit.py adn` | Verifica el **dueño único del BLOQUE A**: perfil vs. cada batch vs. galería |
| `outfit.py lint [slug]` | Parsea las galerías **como LV-App** y avisa anclas faltantes |
| `outfit.py auditar [--solo-sin-imagen]` | Corre el canon de calzado y vestuario **sobre la flota real** |
| `outfit.py anclas <slug>` | Inyecta anclas faltantes en una galería ya escrita |
| `outfit.py modularidad` | 0 personajes en la lógica · campos propios declarados · sub-poses únicas |
| `outfit.py test` | Self-checks de las reglas **+ 32 pruebas del motor** |
| `outfit.py personajes` · `poses <slug>` · `stats` | Inventario |

**Un batch es un JSON en `99_Sistema/scripts/visual/batches/`**, no un `.py`:

```json
{ "personaje": "ele", "batch": "La Perla y HB Lencería", "fecha": "27/08/2026",
  "categoria": "Lencería", "rango": "808-812", "tags_comunes": ["laperla", "V7poses"],
  "negative_extra": "cotton lingerie, organic fabric",
  "looks": { "808": {
      "titulo": "Noir Lace La Perla Suite", "codigo": "LA1", "polo": "A Boudoir",
      "bloque_b": "<el outfit del día>",
      "setting":  "<BLOQUE C>",
      "props":    {"seat": "…", "wall": "…", "surface": "…", "upright": "…"} } } }
```

- **El BLOQUE A no va ahí.** Lo lee el motor del perfil visual (§2, fence `<!-- ADN:BLOQUE_A -->`), que es su **dueño único** desde el 29/08/2026: `build()` acepta `bloque_a=None`. Antes cada script lo copiaba a mano y **Anaïs ni siquiera tenía token literal** en su perfil.
- **Lo que difiere por personaje sale del perfil, no del batch:** emoji del encabezado, etiqueta del slot 5, carpeta de imágenes, orientación alterna de la Odalisque.
- **La variación por look se DECLARA, no se copia:** `adn_overrides` (la rotación de maquillaje de Miss Doll, canon de su perfil §5.5 — falla ruidosamente si el fragmento ya no existe en el ADN), más `tags`, `concepto`, `negative_extra` y `emitir_bloque_b` opcionales.
- **Campos obligatorios por look:** `titulo`, `bloque_b`, `setting`. Y `props` con el **mobiliario real del setting** — el motor lo exige (Ama 08/06/2026: *"cada pose debe ser armoniosa con el ambiente"*).

> ✅ **Verificado antes de adoptarlo:** se regeneraron los dos batches existentes desde sus JSON y se compararon con el markdown escrito a mano — **estructura idéntica y cero diferencias de prompt** más allá de las anclas agregadas ese mismo día.
>
> ⏳ **Anaïs no está migrada a batch-como-datos.** Su formato de emisión difiere en cuatro puntos (encabezado 👑, línea `**Arquetipo:** · **Paleta:**`, `**1. Standing:**` en vez de `### 1.`, y su BLOQUE B **inline entre backticks** — la forma exacta que ya rompió el parser de LV-App). Unificarlo toca su galería viva: es decisión de la Ama, no un refactor silencioso.

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
3. Consultar los últimos looks **globales** para las reglas de composición (ej. anti-monoblock: máx. 2 consecutivos) **y para la arquitectura de prenda** (ver aviso abajo).
4. Contar cada **cuota viva** del §8. Si una está vencida → este look **debe** cumplirla.
5. Recién entonces avanzar.

**El resultado del Paso 0 se escribe explícitamente** antes de diseñar: *"Bloqueadas: siluetas X, Y · settings Z · monoblock NO disponible · cuota animal print VENCIDA → obligatoria"*. Un Paso 0 que no deja rastro escrito es un Paso 0 que no se hizo.

> ⚠️ **Una ventana alcanzada POR ARQUETIPO puede no dispararse nunca (18/08/2026).** Miss Doll acumuló **once looks seguidos sin vestido, falda ni pantalón** (L15-L25) con la ventana de silueta del §7 activa y el déficit de arquetipos en meta: como el batch rota arquetipo en cada look, dos vecinos casi nunca comparten arquetipo, así que la regla **no se disparó ni una vez en 25 looks**. Una regla que no se puede disparar es una regla que no existe.
>
> **Qué mirar en un motor nuevo:** ¿el eje que quiero proteger es de arquetipo o del roster completo? Composición, arquitectura de prenda y cromatismo son **globales**; detalle de silueta y setting son **por arquetipo**. Y la contracara: §6 gobierna el **escenario**, nunca la **prenda** — si nadie declara un eje de prenda, la prenda queda a mano alzada y converge sola.
>
> **Dónde vive:** `anclas_universales.json` → `arquitecturas_de_prenda` (taxonomía M1-M10 genérica) + `personajes.<slug>.rotacion_prenda` (ventana global · cuota de silueta cubierta · `desde_look`). El **chequeo 12** del linter lo mide. Se clasifica **solo el BLOQUE B**, nunca el prompt ensamblado: sus propias anclas nombran bikini, bodysuit, dress y skirt — clasificar sobre el prompt completo es el clasificador leyéndose a sí mismo.

> 🔀 **Y esa ventana tiene DOS puntos ciegos, medidos el 05/09/2026 — corre `outfit.py cruce`.**
> La Ama, mirando el batch de colorimetría: *"estás repitiendo los mismos colores muy seguido, a Miss Doll le diste el mismo outfit con colores distintos, y a las 3 les diste el mismo outfit."* Tenía razón en los tres cargos, y **los cuatro auditores estaban en verde** (`auditar` 0 violaciones · `adn` LIMPIO · `modularidad` LIMPIA · `lint` CRÍTICOS 0). Las dos causas son estructurales, no descuido:
>
> 1. **`rotacion_prenda` es PER-PERSONAJE.** Compara a Ele con Ele. **Nada en el motor comparaba a Ele con Anaïs**, así que las tres muñecas podían salir el mismo día con el mismo corset y las tres pasaban limpias. Medido: 5 pares con arquitectura idéntica entre muñecas, hasta **39 n-gramas de 8 palabras clonados verbatim** (Miss Doll L78 ↔ Anaïs L80).
> 2. **La `ventana_global` es de 3 y los batches son de 5.** Miss Doll repitió **3 de 5** arquitecturas del batch inmediatamente anterior, todas a distancia 5-6 — fuera de la ventana, invisibles. Eso es literalmente "el mismo outfit con otro color". Anaïs venía peor: **5 de 5** (todas M6) contra su batch previo.
>
> **La lección del método, que es la de siempre acá:** un chequeo verde solo prueba que miró donde miró. La ventana existía, estaba cableada a las tres desde el 04/09 y no era suficiente — **el eje que faltaba no era per-personaje sino entre personajes.** Mismo patrón que `modularidad` reportando LIMPIA con 630 poses de Ele sin numerar.
>
> **`outfit.py cruce`** mide los cuatro ejes: **X1** arquitectura idéntica entre muñecas · **X2** cláusulas clonadas verbatim (n-gramas ≥8 palabras) · **X3** familia cromática repetida dentro de un batch · **X4** arquitectura repetida contra el batch anterior del mismo personaje. Reutiliza `clasificar_arquitectura` y la taxonomía M1-M10 a propósito: un segundo clasificador con criterio propio es exactamente como nació el problema de auditar la misma galería dos veces con reglas incompatibles. **Se corre ANTES de `generar`, no después.**

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

> ⚠️ **No apilar constraints duros simultáneos (Ama 23/08/2026, Look 27 "Cromo Líquido" de Miss Doll — "imposible renderizar de manera correcta este prompt").** El look sumaba **acabado espejo cromado líquido** (ya de por sí de los materiales más difíciles de renderizar consistente — reflejos especulares reales) + **silueta contradictoria** (cuello barco cerrado al frente, espalda completamente abierta hasta la cintura, mangas largas ajustadas) en la misma prenda. El look terminó 7/7, pero con parches visibles (archivos `anexo_*`) que delatan cuánto costó. **Lección:** un material ya difícil (cromo/espejo/líquido) se combina con un corte SIMPLE; un corte muy trabajado (mucha piel expuesta en un lado, mucha cobertura en otro) se combina con un material dócil. No las dos cosas duras a la vez en la misma prenda — se audita esto en el Paso 2, antes de escribir el prompt, no después de ver el resultado.

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
> **Herramienta, no fuerza de voluntad:** el ensamblado lo hace `prompt_builder.py` (`PromptBuilder(slug).build(...)`), y `outfit.py lint` lo verifica parseando la galería como la parsea la app.
>
> 🔴 **Escribir los prompts a mano DEJÓ de estar permitido (29/08/2026).** Esta línea decía *"escribir los prompts a mano está permitido; entregarlos sin pasar el linter, no"*. **Está derogada por evidencia:** el Look 801 se escribió a mano y sus cuatro poses materializadas salieron sin `GARMENT_CONSISTENCY`, sin `PHOTOREAL_LOCK` y sin ancla de orientación — el Side Profile rindió **otro outfit completo**. El linter no lo salvó porque el linter mide lo que está escrito, no lo que faltó escribir. **Todo look se ensambla con el motor:** `outfit.py generar <batch.json>`. Es la lección, no el parche.

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

## 🎥 Sub-poses: el BLOQUE C no se escribe a mano (v2.1 — 13/08/2026)

La cláusula de pose **sale del repertorio del personaje**, nunca de la inspiración del momento.

- **Dueño único del texto:** `99_Sistema/scripts/visual/repertorios_pose.json` → `personajes.<slug>.slots`. **149 sub-poses** registradas: Ele 51 · Miss Doll 49 · Anaïs 49.
- **Mecanismo:** `PromptBuilder.pose(slot, look_number, props)`. Rotación `(look - 1 + offset_del_slot) % n`, con offset distinto por slot → dos looks seguidos nunca comparten variación, y dentro de un look los siete slots caen en índices distintos.
- **Props obligatorios:** `{seat}` `{wall}` `{surface}` `{upright}` se rellenan con **mobiliario real del setting del look** (Ama 08/06/2026: *"cada pose debe ser armoniosa con el ambiente"*). Si el look no tiene ese mueble, el builder **salta a la siguiente variación**; jamás escribe un placeholder sin resolver.
- **Registro estético por personaje** (vive en el JSON, no acá): Ele *high-end editorial fetish* · Miss Doll **pole dance + burlesque** · Anaïs **old glamour / old Hollywood / Bettie Page**.

> **Por qué está en el motor y no en un documento por personaje:** Ele tenía sus 51 sub-poses desde el 08/06/2026, pero vivían en `pose_rotation_v5.py` — motor de **un** personaje — y nunca llegaron a las otras dos. Medido el 13/08 en Miss Doll: cláusula de pose 41-70% idéntica entre sus 14 looks, y el único slot sano era el único con repertorio escrito. **Un fix que vive en el motor de un personaje no es un fix.**

> ⚠️ **Cómo se audita (y cómo NO):** con repertorio puesto, la **similitud media de texto deja de servir** — con 14 looks y 7 variaciones cada una sale dos veces y esos pares son idénticos por diseño (el promedio se queda en 43-57% aunque todo funcione). Las métricas correctas son **variaciones distintas usadas por slot** y **repeticiones en looks consecutivos**.

## 🔒 Anclas nacidas de defectos medidos (13/08/2026)

Cinco anclas nuevas en `anclas_universales.json`, todas con su defecto fotografiado detrás:

| Ancla | Alcance | El defecto que la parió |
|---|---|---|
| `PHOTOREAL_LOCK` | **universal** (`_todos`) | El Standing del Look 08 de Miss Doll salió **render 3D**, no fotografía, con el mismo BLOQUE A que rindió 7 fotos en el Look 07. El negative vetaba la *piel* de maniquí, no el **medio** |
| `SIDE_ANCHOR` | slot `side_profile` | Era el único slot sin ancla de orientación — mismo hueco que tenía Standing antes del 12/07. El Side Profile del Look 07 pedía tres cuartos hacia cámara y salió tres cuartos **desde atrás** |
| `ASYMMETRY_LOCK` | opt-in | El `one-shoulder` del Look 07 se perdió en **3 de 7 poses** (strapless · dos tiras + cordonería inventada · V simétrico). `GARMENT_CONSISTENCY` nombra escote, manga y ruedo — **no la asimetría ni el lado** |
| `ACCESSORY_COUNT_LOCK` | opt-in | El Odalisque del Look 07 salió con **dos cuffs**, uno por muñeca, contra un BLOQUE B que pide `a single … cuff, no other jewelry` |
| `GARMENT_EXCLUSION_LOCK` | opt-in | El Back View del Look 04 rindió el **corsé del Look 03** aunque su prompt decía `no corset` y su negative lo prohibía por nombre |
| `BOTTOM_CUT_LOCK` | **`anclas_siempre` de Ele y Miss Doll** | El Back View del **Look 801 de Ele** salió con un **calzón de talle alto** tapando el asiento entero. Su BLOQUE B decía `matching white wet-satin micro bikini bottoms`: nombra prenda y material, **nunca el corte**. Mismo modo de falla que `ASYMMETRY_LOCK` — el atributo que no se nombra lo resuelve el generador, y su default es cobertura total |
| `DRESS_LEG_CLOSURE` | opt-in, **transversal a las tres** | Directiva de la Ama: con vestido/falda/bata las piernas van **cerradas**. El repertorio de sub-poses está lleno de aperturas escritas pensando en calzón (piernas en V, rodilla girada, floorwork); al caer sobre un look de falda el generador abre igual |

Las opt-in **las dispara el BLOQUE B, no el slot**: `PromptBuilder.opt_in_de(bloque_b)` las detecta y `build()` las inyecta sola. Condiciones registradas en `anclas_universales.json` → `anclas_opt_in`.

### 🎭 `anclas_siempre` — anclas de canon de UN personaje (13/08/2026)

Tercer alcance, entre `_todos` (las tres muñecas) y `overrides` (un slot). Se declara en `anclas_universales.json` → `personajes.<slug>.anclas_siempre` y `PromptBuilder.anclas_de_slot()` la concatena **después de `_todos`, en los 7 slots**.

**Existe porque hay prohibiciones que son de un personaje y no del repo.** La tanga obligatoria (`BOTTOM_CUT_LOCK`) es canon de Ele y Miss Doll; a **Anaïs le rompería el período**, porque su Vintage Noir / Bettie Page usa calzón retro de talle alto como pieza legítima de época. Meterla en `_todos` se la impondría a las tres; repetirla en los 7 `overrides` sería copia — y la copia diverge, que es la enfermedad que este motor vino a curar.

> ⚠️ **Al agregar una `ancla_siempre` hay que mover `n_globales`, no un número escrito a mano.** `build()` separa anclas globales de anclas de slot por posición; el builder ya lo calcula con la propiedad `n_globales` (= `_todos` + `anclas_siempre`). Si alguna vez vuelve a aparecer un `len(self.mapa["_todos"])` suelto en el código, es un bug esperando: el ancla del personaje se colaría al bloque de pose.

## 📂 Recursos

- [`references/_plantilla_perfil_visual.md`](references/_plantilla_perfil_visual.md) — esquema de perfil (para personajes nuevos).
- Perfiles vigentes: `02_Personajes/_perfiles_visuales/`.
- Bibliotecas de siluetas / specs por sub-arquetipo: enlazadas desde cada perfil (§6). Son **material del personaje**, no del motor.
