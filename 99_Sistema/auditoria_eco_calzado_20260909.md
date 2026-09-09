# 👠 El eco de calzado — diagnóstico pedido por el plan del 06/09 (medido 09/09/2026)

> **Qué preguntaba el plan** (`plan_correccion_hallazgos_20260906.md`, Fuera de alcance §2):
> *"El eco de calzado existe y no sostiene la arquitectura — plataforma, puntera y altura de
> caña se pierden igual. Hay que medir si el eco llega a las poses donde falla antes de
> tocarlo."*
>
> **La respuesta corta: el eco llega. Lo que no llega es el eco BUENO — y dejó de llegar en
> el Look 801.**
>
> 🪦 **Muerte declarada:** evidencia fechada. No se borra; se cierra cuando la Ama decida si
> se restituye el eco completo, y entonces se anota su decisión acá mismo.

---

## 1 · Hay DOS ecos de calzado, no uno

| | Texto | Qué fija |
|---|---|---|
| **Eco débil** | `the footwear clearly visible and exactly as described above` | Nada. Apunta a «arriba» y confía |
| **Eco completo** | `the footwear clearly visible and exactly as described — <zapato> — with the same heel, the same platform height and the same toe shape, never swapped for boots, booties or any other shoe style` | **Tacón, plataforma y puntera**, por nombre |

El completo vive en `99_Sistema/scripts/visual/pose_rotation_v5.py:714`, función `footwear_echo()`.

## 2 · El eco SÍ llega a las poses donde falla

Medido sobre el Look 831 (7/7, emitido por la puerta actual), pose por pose:

| Pose | Lleva eco |
|---|---|
| Standing | ✅ débil |
| Back View | ✅ débil |
| Seated | ✅ débil |
| Side Profile | ✅ débil |
| Ditzy | — *(plano cerrado, correcto que no lo lleve)* |
| POV | — *(plano cerrado, correcto)* |
| Odalisque | ✅ débil |

**Las tres poses donde la auditoría visual del 06/09 vio romperse la arquitectura —Standing,
Seated y Side Profile— llevan el eco.** O sea la hipótesis «no llega» queda descartada: llega
y no alcanza, porque el texto que llega no nombra ni la plataforma ni la puntera.

## 3 · Y acá está lo que nadie había visto: es una REGRESIÓN con fecha

Contados los looks de la galería de Ele por cuál de los dos ecos llevan:

| | Looks | Rango | Último |
|---|---|---|---|
| Eco **completo** | 38 | L230 – **L800** | **L800** |
| Eco **débil** | 131 | L230 – L832 | L832 |

**Desde el Look 801 no hay un solo look con el eco completo.** De los 32 looks ≥800 con eco,
**31 llevan el débil y uno el completo** (el propio L800).

El L801 es donde arranca la era de **batch-como-datos** (29/08/2026), cuando `outfit.py generar`
pasó a ser la única puerta de emisión. Esa migración se verificó regenerando los dos batches
existentes y diffeando — *"estructura idéntica, cero diferencias de prompt más allá de las
anclas agregadas ese mismo día"*. **La verificación no lo vio** porque comparaba los batches
migrados contra sí mismos, no contra la era anterior.

`PromptBuilder` **nunca llama a `footwear_echo()`**: lo menciona en un comentario
(`prompt_builder.py:693`) como ejemplo del mecanismo que inspiró el eco de busto, y ahí queda.
El único que la invoca es `rotate_poses()` en `pose_rotation_v5.py`, que es el camino de la era
de los scripts a mano.

## 4 · Por qué importa, con la evidencia de la Ama al lado

La auditoría visual del 06/09 (174 PNG, 6 auditores externos) encontró exactamente lo que
predice este diagnóstico, y **todo en looks posteriores al 800**:

- *"la **plataforma de 6"** casi nunca se imprime (L76, L79, L75)"* — Miss Doll
- *"L826 entrega **tres zapatos distintos**"* · *"L818 Standing sin tira y Back View con tira"* — Ele
- *"plataforma donde se declaró «no platform» (L81 Seated)"* — Anaïs
- *"El canon de tacón alto se respeta siempre; el detalle declarado del zapato, nunca del todo"*

## 5 · Lo que falta, y no es mío

Restituir el eco completo **cambia el prompt de todos los looks futuros de las tres muñecas**.
Eso es canon visual y lo decide la Ama — el plan ya lo clasificó así y se respeta.

**Lo que sí se puede decir con los números:** el eco completo nombra tacón, plataforma y
puntera. **No nombra la altura de caña** ni el número de tiras, que son otros dos de los
atributos que la auditoría vio derivar (L820 muslo↔rodilla, L819 entramado↔tobillera). O sea
restituirlo tal cual cierra dos de los cuatro huecos medidos, no los cuatro.

| Hueco medido | ¿Lo cubre el eco completo? |
|---|---|
| Plataforma | ✅ sí |
| Puntera | ✅ sí |
| Altura de caña | ❌ no |
| Número/arquitectura de tiras | ❌ no |

Y un aviso que vale más que la propuesta: **el eco completo estuvo vivo entre el L230 y el
L800 y los defectos de calzado existían igual en ese tramo** (la auditoría del 20/06 ya los
tenía). No es una bala de plata — es poner de vuelta una pieza que se cayó sin que nadie lo
notara, y medir después.
