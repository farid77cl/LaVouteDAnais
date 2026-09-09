# 🔍 Auditoría sistemática de pares de anclas — Etapa 2 (09/09/2026)

> Plan: `C:\Users\farid\.claude\plans\humble-shimmying-stroustrup.md` (aprobado por la
> Ama el 09/09/2026). Etapa 1 (detector heurístico) construida en
> `99_Sistema/scripts/visual/auditar_anclas_pares.py`. Esto es la Etapa 2: revisión
> manual de los 38 pares candidatos que el escaneo real encontró, personaje por
> personaje, uno por uno.

## Resultado en una línea

De 38 candidatos (13 pares únicos, repetidos entre las tres muñecas): **1 contradicción
real y nueva** (corregida), **1 par que el propio código ya resolvía** (sin acción), y
**11 falsos positivos del heurístico** — todos por palabras genéricas de más de un
sentido ("plain", "seam", "worn", "behind", "texture"). El heurístico hizo su trabajo:
más ruido que señal, pero la señal estaba adentro.

## ✅ Hallazgo real — corregido

**`FABRIC_PRISTINE` vs `HOSIERY_LOCK`**, mismo mecanismo exacto que `FABRIC_PRISTINE`
vs `ANIMAL_PRINT_LOCK` (corregido horas antes ese mismo día), esta vez con patrón de
media en vez de estampado animal:

- `FABRIC_PRISTINE` (global, todo look): *"all garment surfaces clean, solid-coloured
  and unmarked:1.4"*.
- `HOSIERY_LOCK` (opt-in, dispara con cualquier media): *"their print or pattern...
  never missing their pattern"*.

Sin conflicto con medias LISAS (HOSIERY_LOCK no exige que exista un patrón, solo que
si lo hay se respete). **Con medias de fishnet/encaje/lunares SÍ hay conflicto real** —
verificado reconstruyendo un look de fishnet con `PromptBuilder.build()`: las dos
cláusulas convivían, igual que en el L832 con el print animal.

**Fix aplicado** (mismo patrón, tercera vez en el día): nueva lista
`garment_canon.HOSIERY_PATTERNED` (fishnet, lace-top, polka dot, houndstooth, diamond
grid, argyle, checkered, chevron) y una tercera exclusión condicional en
`PromptBuilder.build()` — `FABRIC_PRISTINE` se descarta cuando `HOSIERY_LOCK` está
activo Y el BLOQUE B nombra un patrón real. Con medias lisas, `FABRIC_PRISTINE` sigue
intacto (verificado). Regresión permanente: `test_engine.py` bloque H3 (+ su control).

## ⚪ Ya resuelto en código, sin acción nueva

**`WRAP_BACK_ROBE` vs `WRAP_BACK_TAILORED`** (back_view): el detector los marca
correctamente como incompatibles (una describe el panel de una bata, la otra el de una
chaqueta estructurada, sobre el mismo panel de espalda) — pero `build()` **ya** los
desambigua desde el 29/08 (*"un look que nombra bata Y chaqueta no puede llevar las
dos anclas... manda la estructurada"*, `prompt_builder.py`). El detector no sabe de esa
desambiguación porque solo lee texto de anclas, no el código que las combina — es
exactamente el límite que el plan anticipó. Se documenta para que la próxima revisión
no lo vuelva a mirar como nuevo.

## ✅ Actualización — apareció la foto, y sí era real

Escrito arriba, horas antes: *"no hay foto que muestre esto rompiéndose... no se toca
sin evidencia."* Apareció la foto. `ele_831_seated.png` (Look 831, ya materializado)
sale **de pie**, no sentada — y el índice de sub-pose que le tocó a ese look, medido
con `pb.pose_indice("seated", 831)`, es el **6**: *"perched on the very front edge of
{seat} with the knees carried apart to the width of the shoulders and both stilettos
planted, both long-nailed hands set flat on the seat behind her..."* Ninguna palabra
de esa frase ancla el peso en el asiento — "stilettos planted" y "hands... behind her"
describen igual de bien a alguien de pie apoyada en una superficie detrás. `SEAT_ANCHOR`
(con su cola `:1.4`, "genuinely sitting down, buttocks resting on the seat") va ANTES
en el prompt, más lejos de la pose real — y perdió contra la imagen concreta que sí
describe el gesto, mismo mecanismo de dilución por posición que el hallazgo #3 de la
mañana. La variante 4 (*"perched on the edge... knees together, hands resting flat on
the thighs"*) tiene la misma ambigüedad, sin foto confirmada todavía.

**Fix aplicado** en `repertorios_pose.json` (Seated de Ele, variantes 4 y 6): se
inserta *"her weight settled down through her hips onto the seat"* dentro de la
propia cláusula de pose, junto al mueble — no se depende de que `SEAT_ANCHOR`, lejano,
gane la disputa. Las otras dos variantes "perched" (0 y 1) no se tocan: cruzar las
piernas levantadas o apoyar los codos en las rodillas ya son geometrías que no leen
como estar de pie, así que no compiten con el mismo sesgo. Verificado: 140/140 tests,
y la reconstrucción del Look 831 con el fix ya no lee ambiguo.

Este es el primer caso real de la categoría que la Ama nombró después de la auditoría
de contradicciones: *"lo que no se nombra, el generador lo rellena con su propio
sesgo"* — no una contradicción entre dos anclas, sino una pose que no nombra lo
suficiente para que el sesgo del generador no gane.

## Los 11 falsos positivos del heurístico, por si alguien los vuelve a mirar

Todos por una palabra con dos sentidos, sin conflicto semántico real:

| Par | Por qué es falso positivo |
|---|---|
| `ACCESSORY_COUNT_LOCK` / `GARMENT_EXCLUSION_LOCK` | Las dos están DE ACUERDO (nada añadido, nada extra) — el heurístico lee coincidencia de vocabulario como negación |
| `ASYMMETRY_LOCK` / `WRAP_BACK_ROBE` | "back"/"behind" comparten sílaba, no sentido — asimetría de hombro no pelea con panel cerrado de espalda |
| `BACK_ANCHOR` / `WRAP_BACK_ROBE`, `BACK_ANCHOR` / `WRAP_BACK_TAILORED` | Las dos exigen la prenda puesta CORRECTA — redundantes, no contrarias |
| `FABRIC_PRISTINE` / `PHOTOREAL_LOCK` | "texture" en una es tela impresa, en la otra es grano de piel — palabra ambigua |
| `FABRIC_PRISTINE` / `SEAM_FRONT` | "seam" es costura de construcción, no marca de tela — dominio equivocado |
| `HOSIERY_LOCK` / `SEAM_FRONT` | "bare"/"legs" aparecen por tema compartido (medias), no por afirmar piernas desnudas |
| `HOSIERY_LOCK` / `SIDE_ANCHOR`, `PHOTOREAL_LOCK` / `SIDE_ANCHOR` | "plain" en `SIDE_ANCHOR` es *"a plain back view"* (encuadre soso), no tela sin marca |
| `SEAM_BACK` / `WRAP_BACK_ROBE` | "seam" de la media vs "seam" del panel de la bata — objetos distintos |
| `SEAM_FRONT` / `SENSUAL_STATE`, `SENSUAL_STATE` / `WRAP_BACK_ROBE` (solo Anaïs) | *"fingertips tracing a seam"* es gestual y genérico, no declara la costura de la media |

## Lo que esto deja para la Etapa 1 (nota para la próxima vez que se revise el detector)

Las familias de vocabulario ("plain", "seam", "texture", "behind", "worn") son
demasiado genéricas — capturan sentido de camino, no de tela/cobertura. No se afinan
hoy: afinarlas de más arriesga silenciar el próximo caso real (falso negativo), que es
justo el error que este mecanismo existe para evitar. El heurístico se deja tal cual,
advirtiendo con ruido, y la revisión humana sigue siendo la Etapa 2 real.

## Extensión — las otras dos variantes "perched", por consistencia (no por foto)

Comparado el repertorio de Seated de las tres muñecas: Miss Doll (10 variantes) y
Anaïs (12) **nunca** usan "perched" sola — las 22 anclan el peso explícitamente
("weight fully down", "hips fully down"). Solo Ele se desviaba, y solo en sus 4
variantes "perched". Las 0 y 1 no tienen foto que las delate (su propia geometría —
piernas cruzadas en alto, codos sobre las rodillas — ya hace improbable el mismo
error), pero se les agregó la misma cláusula de peso para que el repertorio de Ele
deje de ser la excepción sin ancla dentro de las tres. Verificado: JSON válido,
140/140 tests.

## Revisado y cerrado sin tocar — Odalisque de Miss Doll (kneeling)

Mismo patrón de sospecha que el de Seated: `FLOOR_SEAT_ANCHOR` exige *"the hips and
the backs of the thighs resting on the ground"*, y dos sub-poses de Odalisque de Miss
Doll (7 y 8) describen un **kneeling** ("both knees planted", "pelvis pushed forward")
— geometría donde el peso va en las rodillas, no en la cadera contra el suelo.
Candidato real por texto. **Verificado contra la foto:** Look 84 (índice 7,
`miss_doll_084_odalisque.png`) sale arrodillada con la cadera hacia atrás sobre los
talones, exactamente como se pidió — sin el defecto que el Seated de Ele sí tuvo.
Se cierra sin tocar: la sospecha textual no se confirmó en la imagen real.

## Barrido del mismo patrón en Side Profile — nada más que tocar

Mismo chequeo (¿"perched" sin ancla de peso?) sobre Standing, Back View y Side Profile
de las tres muñecas. Dos candidatos con la misma forma que el de Seated:

- Miss Doll Side Profile #5 — *"perched on the front edge of {seat}"*, sin "weight down".
- Anaïs Side Profile #4 — *"seated or perched"*, sin ancla de peso.

**Verificado contra fotos reales** (Miss Doll L80 y Anaïs L80, ambas con esa variante):
las dos salen correctamente sentadas, cadera abajo, sin el defecto del Seated de Ele.
**No se tocan.** La diferencia con el caso real: en Ele el resto de la frase ("stilettos
planted", "hands... behind her") describía activamente un cuerpo de pie; en estas dos el
resto de la frase (rodillas juntas, apoyo en el mueble) ya lee sentado sin ambigüedad
aunque falte la palabra "weight". El texto de la ancla no es la única señal — la escena
completa que describe la frase importa más que una palabra suelta.

Con esto se cierra el barrido de "lo que no se nombra" para esta ronda: 1 defecto real
corregido (Seated de Ele), 3 candidatos revisados y descartados con foto (Odalisque MD,
Side Profile MD y Anaïs).

## Sobre la categoría #2 (dilución por largo) — lo que la evidencia de hoy realmente dice

La hipótesis de la mañana era "el candado, temprano en el prompt, entierra la pose,
tardía". **La evidencia real del Seated de Ele dice lo contrario**: el candado
(`SEAT_ANCHOR`, temprano) perdió y la pose (tardía, concreta) ganó — el generador
hizo lo que describía la frase más vívida y cercana a la escena, no la más temprana.
Si eso es la regla general, mover la pose más temprano en el ensamblado no ayudaría:
la ganadora ya es tardía. **La categoría sigue siendo real (algo entierra algo), pero
la dirección del arreglo que se proponía en la mañana no está confirmada por el único
dato que hay hoy.** Se anota para que la decisión, cuando se tome, no parta de la
hipótesis original sin corregir.

## Barrido de un cuarto candidato — accesorios sin eco, descartado

Hipótesis: los accesorios (lentes, joyas) se declaran solo en el BLOQUE B, lejos de
la pose, sin un eco de cierre como `footwear_echo`/`eco_busto` — mismo riesgo en
teoría. **Verificado contra el Look 831 (lentes) en Ditzy y POV, los dos planos
cerrados donde más se esperaría el drift:** los lentes persisten correctamente en
ambos. No se confirma el hueco con esta muestra. No se toca.

## auditar_canon_flota.py — medido, y es otra categoría, no esta

Corrida completa: **844 violaciones sobre 685 looks auditados**, con 24 en la era del
motor genérico (L800+, incluidos L831/L832 ya tocados hoy). **No es la misma tarea.**
Es deuda de la FLOTA YA GENERADA (imágenes que ya existen, con el canon de HOY aplicado
retroactivamente) — la sesión de esta mañana ya midió que de un lote similar de 90
solo 1 era realmente arreglable (el resto era fósil histórico L200-L800, no
retrofiteable, o bug del propio auditor — 28 de 90 esa vez). Los 844 de hoy no están
triados; hacerlo es un proyecto propio, del tamaño del de esta mañana o más grande, y
es sobre el PASADO, no sobre que el motor genere bien HOY. Se deja anotado, no se
empieza sin que la Ama decida que es la prioridad.

## Un cuarto caso real — el negative, no el positive (09/09/2026, tarde)

Todo lo de arriba miraba el POSITIVE. El NEGATIVE tiene el mismo problema: Miss Doll
declara `corset` y `warm smile, laughing` en su negative BASE (porque ninguno es
obligatorio) con la intención documentada de sacarlos del negative cuando el look sí
los lleva — pero ese paso dependía 100% de que quien escribiera el batch pusiera
`negative_excluir` a mano.

**Medido en los batches reales:** 2 de 5 looks de corsetería (L62, L68) y 2 de 4 Girly
Girl (L66, L83) tenían ese campo en `None`. El prompt le pedía el corsé al positive y
se lo negaba al mismo tiempo — la misma "moneda al aire" de toda la auditoría de hoy,
esta vez en la otra mitad del prompt.

**Fix aplicado:** `personajes.miss_doll.negativo_condicional` (JSON, nuevo) declara las
dos reglas (`bloque_b_nombra` para corsé, `arquetipo_es` para Girly Girl).
`PromptBuilder.build_negative()` las lee solas y las une con el `excluir` manual —
ya no depende de la memoria de quien escribe el batch. Cuidado real encontrado en el
camino: un BLOQUE B que dice *"no corset"* (ausencia declarada) no debe disparar la
regla — se filtra igual que `arquitecturas_de_prenda._regex_ausencias`. Verificado
contra los 4 looks rotos (ya corrigen solos) y los 5 ya-correctos (sin cambio).
Regresión permanente: `test_engine.py` bloque H4, 144/144.

## Sexto hallazgo real — el mismo hueco de ausencias, generalizado (09/09/2026, noche)

El fix de `negativo_condicional` de esta tarde expuso el patrón completo: **una
ausencia declarada ("no X") no es una presencia**, pero varios disparadores de
`opt_in_de()` solo miraban si la PALABRA estaba en el texto, sin mirar si venía
negada. Ya se había parcheado a mano una vez (`SEAM_FRONT`/`SEAM_BACK`, 06/09, para
"no stockings"). Verificado hoy que el mismo hueco vivía en dos sitios más:

- **`HOSIERY_LOCK`** disparaba con *"no stockings anywhere"* — la cadena `stockings`
  está ahí, nomás negada. Un look de bikini sin medias se llevaba igual la cláusula
  *"the stockings are exactly ONE single pair... never missing their pattern"*.
- **`DRESS_LEG_CLOSURE`** disparaba con *"no dress, no gown"* — mismo mecanismo. Un
  bikini se llevaba *"her legs stay closed... never opened apart"*, exactamente la
  clase de instrucción que le pelea a una pose de bikini con piernas abiertas.

**Fix**: nuevo helper `PromptBuilder._sin_ausencias_de(texto, terminos)` (borra
"no <término>" antes de nombrar), aplicado en el loop de `opt_in_de()` para los
cuatro candados de vocabulario (`OPAQUE_LOCK`, `GLOSS_LOCK`, `HOSIERY_LOCK`,
`ANIMAL_PRINT_LOCK`) y, aparte, re-verificando `DRESS_LEG_CLOSURE` (vive en un
regex simple, no en el vocabulario) contra el mismo criterio. **Deliberadamente NO
se tocó `GARMENT_EXCLUSION_LOCK`**: esa ancla existe justo para disparar CON "no X".
El mismo helper unificó el de `negativo_condicional` de esta tarde (tenía el mismo
bug de plural: "no stockings" no coincidía con el término singular "stocking" hasta
agregar el `s?`). Verificado contra bikini-con-ausencias (limpio), vestido real
(dispara), medias reales (disparan), print real (dispara). Regresión permanente:
`test_engine.py` bloque H5, 149/149.

Con este son **6 contradicciones/omisiones reales corregidas hoy**, todas con el
mismo origen: algo en el prompt no dice exactamente lo que quiere decir, y el
generador — o el propio motor, en los dos últimos casos — rellena el resto con su
propio criterio.

## El hueco de ausencias, refactorizado a UNA regla (09/09/2026, noche)

El fix anterior mantenía una lista de términos por candado (una copia del vocabulario
de cada regex). Al revisar los otros disparadores de `OPT_IN` con el mismo criterio,
el hueco vivía en **cuatro sitios más**:

- `ASYMMETRY_LOCK` disparaba con *"no asymmetric hem"*.
- `ACCESSORY_COUNT_LOCK` disparaba con *"no single cuff"*.
- `WRAP_BACK_ROBE` disparaba con *"no robe, no kimono"*.
- `WRAP_BACK_TAILORED` disparaba con *"no blazer, no cardigan"*.

Seis sitios con el mismo bug y seis vocabularios copiados es la misma enfermedad que
este motor existe para curar (dueño único). **Refactorizado a una sola regla**: se
borra la cláusula completa que empieza en `"no "` hasta la coma/punto y coma
siguiente — verificado que esa es la convención real del repo (5.021 apariciones de
`"no "` en la galería de Ele, cero de `"not a/the"`, y cada atributo va separado por
coma). `PromptBuilder._sin_ausencias()` reemplaza el helper con lista de términos.
Única excepción deliberada: `GARMENT_EXCLUSION_LOCK`, que sigue viendo el texto
original — existe justo para disparar CON `"no X"`. Verificado: 12 casos (6 que no
deben disparar + 6 controles que sí deben seguir disparando), todos correctos.
157/157 tests.

**Con este son los mismos 6 hallazgos de hoy, pero el sexto ahora cubre 6 candados en
vez de 2** — el refactor no fue un hallazgo nuevo, fue terminar de medir el mismo.

## Séptimo hallazgo real — el clasificador de arquitectura tenía el mismo hueco, y era el más grave

`clasificar_arquitectura()` (usada HOY MISMO para el fix de `BOTTOM_CUT_LOCK`) tenía
su propia lista de ausencias a mano en el JSON — 12 términos, cubriendo solo un
cuarto de la taxonomía real de 10 arquitecturas. **`no bodysuit`, `no catsuit`,
`no bustier`, `no leggings`, `no jumpsuit`... no estaban.**

**Medido:** un bikini con la aclaración *"no catsuit, no bodysuit"* clasificaba como
**M9 (catsuit) — arquitectura CUBIERTA.** Eso alimenta directo el fix de esta tarde:
una arquitectura mal leída como cubierta le habría sacado `BOTTOM_CUT_LOCK` a un
bikini de verdad — el mismo defecto de la falda del Look 831, por una vía distinta.

**Fix:** el regex de ausencias de 12 términos se reemplazó por
`garment_canon.sin_clausulas_de_ausencia()` (el mismo mecanismo general del
hallazgo anterior — dueño único, sin una tercera copia del regex). El campo
`_regex_ausencias` se retiró del JSON en vez de dejarlo como fósil, ya que nadie
más lo leía. Verificado extremo a extremo: el bikini clasifica M2 y conserva
`BOTTOM_CUT_LOCK`; un catsuit real sigue clasificando M9 cubierta. 159/159 tests.

**Total del día: 7 hallazgos reales corregidos**, cuatro de ellos (BOTTOM_CUT_LOCK,
el negative de Miss Doll, los 6 candados de `opt_in_de`, y este clasificador)
compartiendo la misma causa raíz — una ausencia declarada leída como presencia —
encontrada primero en un lugar y generalizada después a los demás.

## Octavo hallazgo real — dos listas para la misma pregunta, ya divergidas

`footwear_canon.HOSIERY` y `garment_canon.HOSIERY_CONTEXTO` contestan la misma
pregunta ("¿el BLOQUE B declara medias?") con dos listas distintas — y ya habían
divergido. `PromptBuilder._vocab()` usa la de `footwear_canon` para disparar
`HOSIERY_LOCK`, y a esa le faltaban `tights`, `thigh-high`, `thigh high` (que
`garment_canon` sí tenía). **Medido:** *"sheer black polka-dot tights"* — un
patrón real declarado — no disparaba ningún opt-in. Cero candado protegiendo un
patrón que sí está en el prompt.

**Fix:** se agregaron los tres términos faltantes a `footwear_canon.HOSIERY`
(verificado que no introduce falsos positivos en su propio self-check). No se
fusionaron las dos listas del todo — `footwear_canon.HOSIERY` incluye además
`seamed`, `medias`, `sheer sock` sueltos que `garment_canon` no tiene, y unificar
esos de más habría podido introducir falsos positivos nuevos en el ancla de
costura sin evidencia que lo pida; se corrigió solo el hueco medido. 160/160 tests.

**8 hallazgos reales hoy.**

## Noveno hallazgo real — la misma silueta perdía el candado por nombrarse distinto

`COVERED_ARCHETYPES` (dispara `OPAQUE_LOCK`) tenía `catsuit` pero no `unitard` ni
`jumpsuit` — la MISMA familia de arquitectura: el propio regex de M9
(`arquitecturas_de_prenda`) los agrupa como equivalentes
(`\bcatsuit\b|\bunitard\b|\bjumpsuit\b`). No es el caso de exclusión deliberada que
ya documenta la lista (halter/bra/monokini/teddy — expuestos por diseño, on-brand):
un jumpsuit o unitard es panel sólido de pierna completa igual que un catsuit.

**Medido:** *"a full-length zip-up jumpsuit"* y *"a sheer black unitard"* no
disparaban `OPAQUE_LOCK`, mientras la misma silueta nombrada *"catsuit"* sí. Ambas
palabras aparecen 35-37 veces en cada galería — no es un caso raro. **Fix:**
agregados `unitard`/`jumpsuit` a `COVERED_ARCHETYPES`. Verificado sin falsos
positivos nuevos en el self-check de `garment_canon.py`. 162/162 tests.

**9 hallazgos reales hoy.**

## Décimo hallazgo real — el eco de busto afirmaba una prenda que no existía

`eco_busto()` (el hermano de `footwear_echo` para el busto en planos cerrados) tenía
el mismo hueco de ausencias, en un cuarto mecanismo. Un look sin prenda superior
declarada explícitamente (*"no bra, no bralette"*) producía:

> *"the upper garment in THIS frame exactly as described: no bra; no bralette"*

Una cláusula que le afirma al generador, en un plano cerrado, que reproduzca "no bra;
no bralette" como si fuera la construcción de la prenda — literalmente sin sentido, y
compitiendo con cualquier otra descripción de piel desnuda del prompt.

**Fix:** `eco_busto()` ahora limpia el BLOQUE B con
`garment_canon.sin_clausulas_de_ausencia()` antes de trocearlo en cláusulas — mismo
mecanismo que ya corrige `opt_in_de()`, `build_negative()` y `clasificar_arquitectura()`.
Verificado: el caso roto ahora devuelve `None` (sin eco, correcto — no hay prenda que
reafirmar), el caso real con bra sigue generando su eco normal. 163/163 tests.

**10 hallazgos reales hoy — cuatro mecanismos distintos con la misma causa raíz.**

## Undécimo hallazgo real — el candado de color caía sobre un color negado

`detect_dominant()` (`color_canon.py`) elige el primer color nombrado en el BLOQUE B
como el "dominante" de la prenda. **No filtraba ausencias**, quinto mecanismo con el
mismo hueco: *"no black accents anywhere, a sapphire blue high-gloss vinyl wrap
dress"* devolvía `"black"` — el primer color nombrado, negado — en vez de
`"sapphire"`.

**Esto no es un detalle menor:** `outfit.py generar` (la puerta que bloquea antes de
escribir) llama esto para **cada look de cada batch**, vía `audit_rotacion_familia` —
nunca se pasa un `"dominant"` explícito, así que el fallback corre siempre. Un color
negado nombrado antes del real podía **bloquear un batch bueno** (falsa racha de
negro/metálico) o **dejar pasar una racha real sin verla** (si el color negado tapaba
la detección correcta en el look equivocado de la ventana).

**Fix:** mismo mecanismo (`garment_canon.sin_clausulas_de_ausencia()`) aplicado antes
de buscar el color. Verificado: el caso roto ahora devuelve `sapphire`, el self-check
de `color_canon.py` sigue limpio, un negro real sigue detectándose. 165/165 tests.

**11 hallazgos reales hoy — cinco mecanismos distintos, misma causa raíz, y este
último vivía justo en la puerta que hoy mismo se declaró "el gate" del motor.**

## Fase 3 del manifiesto tipado — y un duodécimo hallazgo real en el camino

`opt_in_de()`, `animal_print_kind()` y el candado de `BOTTOM_CUT_LOCK` en `build()`
ganaron un parámetro `manifiesto` opcional: si el look lo declara, `OPAQUE_LOCK`,
`ANIMAL_PRINT_LOCK` y la exclusión de `BOTTOM_CUT_LOCK` se leen directo del dato
(`cobertura_de`, `lleva_estampado_animal`) — cero regex. Sin manifiesto, todo sigue
exactamente igual que antes de hoy (retrocompatible con los ~1.400 looks históricos).
Los demás opt-in (asimetría, conteo de accesorios, bata/blazer, brillo, costura)
todavía no tienen campo propio en el manifiesto — quedan para una vuelta futura.

**Al verificar extremo a extremo apareció un hallazgo real, no de esta fase:**
`clasificar_arquitectura()` — la que ya se corrigió hoy por el bug de ausencias —
tenía OTRO problema, anterior e independiente: sus regex M6/M7 (`\bdress\b`,
`\bskirt\b`) no calzan con compuestos de una sola palabra. **"miniskirt" no
clasifica como M7.** El Look 831 (mi caso de referencia todo el día) clasificaba
bien por pura casualidad: su BLOQUE B real dice *"a sapphire vinyl g-string
**under the skirt**"* para el calzón — esa frase, no la falda misma, es la que
salvaba la clasificación.

**Fix:** M6/M7 copian el mismo patrón que ya usa `DRESS_LEG_CLOSURE`
(`prompt_builder.py`) — `\b(?!headdress|undress|nodress)[a-z]*dress(es)?\b` y
`\b[a-z]*skirt(ed|s)?\b` — para que las dos lecturas del mismo vocabulario
coincidan. Verificado: "miniskirt" y "sundress" solos, sin ayuda de ninguna otra
mención, clasifican bien. 176/176 tests.

**12 hallazgos reales hoy.**

## Fase 4 del manifiesto tipado — `outfit.py generar` acepta el batch nuevo

`cmd_generar` (la puerta) ya renderiza el BLOQUE B desde `manifiesto` cuando un
look lo declara en vez de escribir `bloque_b` a mano — el render corre ANTES de
cualquier auditoría (rotación, canon de calzado/vestuario), así que una pieza
fuera del vocabulario aprobado bloquea el batch entero, igual que cualquier otro
error de entrada.

**Verificado extremo a extremo, vía la CLI real** (no una llamada aislada a una
función): un batch con un look de bikini + estampado cheetah (la especie
aprobada hoy) — declarado ÍNTEGRAMENTE por manifiesto, sin una palabra de
`bloque_b` escrita a mano — pasó por la rotación de arquitectura, el canon de
calzado/vestuario, se renderizó, y llegó al prompt final con
*"genuine cheetah-skin scale/marking texture"* — el candado real, con la especie
correcta, leída del dato. El primer intento (con corsetería) probó además que la
puerta de rotación SÍ frena un manifiesto que repite arquitectura reciente,
exactamente como con un look escrito a mano. 179/179 tests.

Quedan las Fases 5 (probarlo con un look real de la Ama, no de prueba) y, más
adelante, extender el manifiesto a los opt-in que todavía no tienen campo propio
(asimetría, accesorios, bata/blazer, brillo, costura).

## Fase 5 del manifiesto tipado — cerrada, con fotos reales

Primer look real de la flota escrito 100% por manifiesto: Look 833 de Ele, bikini
cheetah, concepto elegido por la Ama para cubrir el déficit de arquitectura Bikini
Y estrenar la especie recién aprobada (cheetah). Tres hallazgos reales en el camino
de escribirlo, los tres ya corregidos:

- `renderizar_prenda()` siempre decía **"a"**, nunca "an" — "a emerald green..."
  leía mal donde una persona habría escrito "an emerald green...". No afecta la
  imagen (Gemini no lee concordancia de artículo), pero sí afecta si la prosa
  lee tan bien como la escrita a mano, que es justo lo que esta fase mide.
  Corregido: agrega y quita la "n" según la primera letra.
- Mi primera redacción de la `descripcion` del calzón chocó con el filtro de
  seguridad (`"the seat left bare"`, ya bloqueado desde antes por
  `audit_safe_filter`) — la puerta lo frenó correctamente, se reescribió.
- El mismo intento generó una advertencia de clon contra el L831 (26,9% de
  léxico común) — no bloqueante, y bajó a 22,3% al reescribir. Es la
  arquitectura del hardware (O-rings, tiras finas) sonando parecida, no una
  copia real; se deja anotado, no se persigue más sin evidencia de que
  moleste de verdad.

**Tres fotos reales generadas** (Standing, Back View, Seated — las tres cubriendo
los mecanismos más delicados de hoy: estampado, `BOTTOM_CUT_LOCK`, y el fix de
`SEAT_ANCHOR` de la mañana). Las tres salieron correctas. La Back View se generó
dos veces con el MISMO prompt en el MISMO modelo, en chats distintos: la primera
con el maquillaje aplanado, la segunda completo — confirmación real, no teórica,
de que era variación pura del generador (categoría #3 de la mañana), no un
defecto del prompt ni del manifiesto.

**Veredicto de la Fase 5, con la Ama de acuerdo: el manifiesto rinde igual que la
prosa escrita a mano.** Queda como el camino recomendado para looks nuevos —
nunca migración masiva de los ~1.400 looks históricos.
