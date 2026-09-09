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
