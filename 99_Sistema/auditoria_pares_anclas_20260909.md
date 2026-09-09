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

## 🟡 Revisado, evidencia insuficiente para tocar

**`SEAT_ANCHOR` vs las sub-poses "perched on {seat}"** (4 de 9 variantes de Seated de
Ele) — la pregunta que dejó abierta la auditoría externa Fable de ayer. Revisado a
mano: `SEAT_ANCHOR` niega *"perched on... any nearby table, desk, counter, island **or
other surface**"* — el objeto de la negación es OTRO mueble, no el asiento correcto.
"Perched on {seat}" nombra el mueble correcto, así que no viola esa negación literal.
La tensión real, si existe, es más fina: *"genuinely sitting down, buttocks resting on
the seat... full weight"* (con peso `:1.4`) contra una postura de borde/poised como
"perched on the edge... knees carried apart" — y sentarse en el borde SÍ es sentarse
(no es el defecto que `SEAT_ANCHOR` nació para cazar: la figura apoyada en una isla o
mesa cercana). **No hay foto que muestre esto rompiéndose** — a diferencia de los tres
casos de arriba, que sí la tienen. Por la misma regla que ya se aplicó dos veces hoy
("verificar el artefacto, nunca el reporte"): no se toca sin evidencia. Queda anotado
para revisar si aparece una foto real de una Seated con postura incoherente.

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
