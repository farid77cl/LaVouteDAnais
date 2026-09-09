# A/B del motor de tres bloques

> ✅ **RONDA ELEGIDA POR LA AMA (09/09/2026): la opción B — Ele L831.** Archivos
> `A_viejo_ELE_L831.md` / `B_bloques_ELE_L831.md`. La ronda de Miss Doll L86 queda
> abajo como antecedente y **no se genera**: su vestido de malla no ejercitaba el eje.

## Ronda viva — Ele L831 «Sapphire Graphite Corner Office»

Es el look que falló: su Back View salió con la falda abierta y el glúteo al aire.
Falda **opaca** + tanga debajo, o sea el eje de exposición entra completo.

**Medido antes de generar (los 7 prompts, los dos motores):**

| | A · viejo | B · bloques |
|---|---|---|
| chars totales | 47.114 | 46.875 (**−0,5 %**) |
| cláusulas con peso por prompt | 5 (6 en Back View) | 5 (6 en Back View) |
| contradicciones | 0 en las 7 | 0 en las 7 |
| **similitud del texto (Back View)** | — | **48,6 %** |

**Qué mide esta ronda, exactamente.** Los dos prompts llevan **el mismo contenido**
—las mismas ~24 cláusulas— en **orden distinto**. O sea aísla la variable
*agrupación/orden*, que es la hipótesis del motor nuevo, y **nada más**.

**Qué NO mide, y hay que decirlo:**
- **La exposición ya está arreglada en los dos.** El fix de `BOTTOM_CUT_LOCK`
  (commit `812e82f88`, esta misma mañana) vive en el motor viejo también: los dos
  piden `not lifted, not parted` y ninguno pide `both seat cheeks fully bare`.
- **El largo no cambia** (−0,5 %). Adelgazar es otra cosa y es la Fase 3.

**El tercer punto de comparación, que es lo que hace valiosa esta ronda:** el L831
**ya tiene sus 7 imágenes** generadas con el prompt **roto** (antes del fix). Así que
al comparar salen tres cosas y no dos:

1. **lo ya materializado** → prompt roto *(mide el fix de la exposición)*
2. **tanda A** → motor viejo con el fix
3. **tanda B** → motor de bloques *(mide el orden)*

---

## 🏁 RESULTADO — Back View, 09/09/2026

**Veredicto de la Ama, textual:** tanda 1 → *«le faltó maquillaje»* · tanda 2 → *«mucho mejor»*.

**Tanda 1 = motor VIEJO · Tanda 2 = motor de BLOQUES.** Ella juzgó sin saberlo; yo no
podía juzgar (preparé las dos y sabía cuál era cuál — un veredicto mío acá no valía nada).

| | tanda 1 · viejo | tanda 2 · bloques |
|---|---|---|
| **Maquillaje** (smokey jade-green, highlight perla, blush rosa-malva) | ❌ **ausente** | ✅ presente y legible |
| Rostro | casi de perfil, chico en cuadro | girado al hombro, con la cara leyéndose |
| Falda cerrada (el defecto original) | ✅ | ✅ |
| Calzado, medias con liguero, lentes, pelo cereza | ✅ | ✅ |
| Marca de agua ✦ | 🟠 presente | 🟠 presente |

**Gana la tanda 2 — el motor de bloques.** Y hay un mecanismo plausible, no solo suerte: en
el motor viejo el maquillaje cierra el bloque A y **después entra un muro de ~2.000
caracteres de anclas** antes de que aparezca `a real photograph taken with a real camera`.
En el de bloques ese ancla es un **campo de A** y va pegada al maquillaje, dentro de la
misma oración del cuerpo. La cláusula de rostro deja de competir con la pared de anclas.

⚠️ **Lo que este resultado NO autoriza a decir.** Es **n=1 por variante, una sola pose**.
Prueba una tendencia, no una ley — y la Ama ya vio en este repo que *un pase no refuta
siete rebotes*. Para declararlo ganado hacen falta las otras 6 poses, o el mismo Back View
repetido. **Hasta entonces el motor viejo sigue siendo el default** (`generar` sin flag), y
así se queda escrito.

### 🖼️ Las imágenes guardadas son MINIATURAS — no sirven para re-auditar

`tanda1_viejo_ELE_L831_back_view_MINIATURA.png` y `tanda2_bloques_…_MINIATURA.png` están a
**286×512 = 0,15 MP**. La app de la Ama sube a **669×1200 = 0,80 MP** (medido sobre
`ele_831_back_view.png` del repo): **el chat las comprimió al llegar**.

Están **por debajo del piso de auditoría** que este repo ya tiene escrito (~0,3 MP): a esa
resolución *«no se ve el defecto»* significa *«no hay píxeles suficientes»*. Se guardan igual
—son el registro de qué se comparó— pero **rotuladas**, y no valen como evidencia para juzgar
detalle fino.

**El veredicto de la Ama NO está afectado:** ella miró las suyas en su pantalla, a resolución
completa. Lo que no se puede es re-auditarlas después desde estos archivos. Para eso harían
falta las full-res subidas por su app.

**Siguiente paso, cuando haya cuota:** las 6 poses restantes de las dos tandas, o repetir
este Back View 2-3 veces para separar señal de varianza.

---

## Ronda 2 — Anaïs L89 «Marta Cibelina y Bronce en la Biblioteca» · pose POV

🔀 **ASIGNACIÓN INVERTIDA A PROPÓSITO: tanda 1 = motor de BLOQUES · tanda 2 = motor VIEJO.**
En la ronda 1 la tanda 1 era el viejo; si el orden se repite, la Ama puede formar expectativa
sin darse cuenta. Se registra acá y **no se le dice hasta que juzgue**.

**Por qué Anaïs.** La ronda 1 la ganó el motor de bloques porque un atributo del **BLOQUE A**
—el maquillaje— aterrizó en el nuevo y no en el viejo. Anaïs es la réplica más dura de esa
misma hipótesis: sus prompts son **los más saturados de la flota** (7.700-8.200 chars contra
6.000-6.600 de Ele, o sea el muro es mayor), y sus **tres defectos medidos el 09/09 son todos
de bloque A y todos de la cara** — lunar correcto en **8 de 27**, iris ámbar aterrizando a
medias, boca cerrada contra su canon de femme fatale.

**Por qué POV.** Es el retrato con la mirada **al lente**: pone la cara lo más cerca posible,
que es exactamente donde viven esos tres defectos. El Back View —que daría comparabilidad con
la ronda 1— le deja la cara chica y de perfil, justo donde el defecto no se puede juzgar.

**Medido antes de generar (las 7 poses):**

| | A · viejo | B · bloques |
|---|---|---|
| chars totales | 56.590 | 56.074 |
| cláusulas con peso (POV) | 9 | 9 |
| contradicciones | 0 en las 7 | 0 en las 7 |
| **similitud del texto (POV)** | — | **69,0 %** |
| lunar · iris ámbar · boca entreabierta pedidos | ✅ los 3 | ✅ los 3 |

⚠️ Reordenar **preserva el largo exacto**: 5 de las 7 poses coinciden carácter a carácter en
total (son textos distintos, verificado). Solo cambian de largo Sovereign Gaze y POV, donde un
eco se reestructura. Eso confirma que la variable aislada es **el orden**, no el volumen.

⚠️ El BLOQUE A de Anaïs **ya no lleva calzado, uñas ni corsé** (salieron el 09/09 por orden de
la Ama). Los dos motores leen el ADN limpio, así que no es una variable entre A y B — pero
hace que estos prompts difieran de los que generaron sus imágenes viejas de galería.

**Archivos:** `A_viejo_AN_L89.md` · `B_bloques_AN_L89.md` · batch `AB_AN_L89_motor.json` ·
imágenes `r2_tanda1_bloques_AN_L89_pov.png` y `r2_tanda2_viejo_AN_L89_pov.png` (**1,06 MP las
dos — por encima del piso de auditoría**, al revés que las miniaturas de la ronda 1).

### 🏁 RESULTADO — POV, 09/09/2026

**Veredicto de la Ama:** tanda 1 → *«le falta sombra de ojos y más maquillaje»* · tanda 2 →
*«subjetivamente está mejor maquillada»*.

**Tanda 1 era el motor de BLOQUES. Tanda 2 era el VIEJO.** → **esta ronda la gana el viejo.**

## 🧮 MARCADOR TRAS DOS RONDAS: 1 – 1

| ronda | muñeca · pose | gana | por qué, según ella |
|---|---|---|---|
| 1 | Ele · Back View | **bloques** | al viejo *«le faltó maquillaje»* |
| 2 | Anaïs · POV | **viejo** | al de bloques *«le falta sombra de ojos»* |

**La conclusión honesta, y es la que importa:** el resultado de la ronda 1 **no se
reprodujo**. Con 1-1 y n=1 por celda, lo más probable es que la diferencia que vimos el
primer día fuera **varianza del generador**, no mérito del motor. El mecanismo que propuse
entonces —que agrupar el ancla de fotorrealismo junto al maquillaje lo hacía aterrizar—
**queda sin sostén**: si fuera causal, tendría que haber ganado también acá, y perdió.

Y hay una segunda lectura que apunta al mismo lado: **el defecto es el mismo en las dos
rondas y en los dos motores** — el maquillaje del BLOQUE A no aterriza de forma fiable,
esté donde esté en el prompt. Eso no es un problema de orden. Es el patrón que la auditoría
del 09/09 ya había medido: **~80 de ~85 defectos son el generador desobedeciendo un prompt
correcto.**

**Consecuencia operativa, sin adornos:**

- ❌ **NO hay evidencia de que el motor de bloques mejore las imágenes.** No se declara
  ganador, y **el viejo sigue siendo el default** — que es donde ya estaba.
- ✅ **Lo que el motor de bloques sí demostró está en el código, no en el píxel:** la
  contradicción es imposible por construcción, cada atributo tiene un dueño único, y una
  cuarta muñeca entra solo con datos. Eso vale por sí mismo y se midió con 50 pruebas — pero
  **es otra cosa que "salen fotos mejores", y no se puede vender como si lo fuera.**
- 🔬 Para separar señal de varianza de verdad harían falta **3-5 repeticiones de la misma
  celda**, no una. A 2 imágenes por celda eso es caro; **decisión de la Ama** si vale la pena.



---

## Antecedente — Miss Doll L86 «Perla y Rosa, Sala Privada» (emitido, NO se genera)

| Campo | Valor |
|---|---|
| **Fecha** | 09/09/2026 |
| **Qué es** | Evidencia (regla 12): las dos emisiones del mismo look por los dos motores, como archivo. **No se borra.** |
| **Origen** | Plan `99_Sistema/plan_motor_tres_bloques_20260909.md`, Tarea 8. Spec `99_Sistema/specs/2026-09-09-motor-tres-bloques-design.md` §8. |
| **Batch** | `99_Sistema/scripts/visual/batches/AB_MD_L86_motor.json` — el look copiado **verbatim** de `MD_L86_L90_casa_llena.json`, 0/7 al escribirlo. No se escribe en la galería. |
| **Estado** | 🟡 Emitido. **Falta que la Ama genere las 14 imágenes** (7 por variante) y la auditoría ciega. |

## Protocolo

1. **Una sola variable.** Mismo ADN, mismo `bloque_b` (el párrafo, sin partirlo en `campos_b` — partirlo habría sido una segunda variable mía), mismo setting, misma sub-pose, mismos props. Lo único que cambia es **cómo se ensambla**: A = motor viejo (`generar` sin flag) · B = motor de tres bloques (`--motor bloques`).
2. **Quien audita las imágenes no sabe cuál es cuál.** Se entregan como «tanda 1» y «tanda 2», y el auditor cuenta defectos por pose con `outfit.py ojos` (pendiente) o con el mismo protocolo de la auditoría del 09/09 (fidelidad · consistencia interna · canon).
3. **Gana quien baje los defectos. Si B no los baja, se dice, y el viejo se queda.** Un pase no refuta siete rebotes: n=1 por variante no decide solo; decide una tendencia, y si hace falta se repite con otro look.

## Lo medido antes de generar nada

| | A · motor viejo | B · motor bloques |
|---|---|---|
| fences (BLOQUE B + 7 poses) | 8 | 8 |
| chars totales | 60.804 | 62.448 (**+2,7 %**) |
| cláusulas con peso `:1.x` por prompt | 21 | 21 |
| contradicciones (`contradicciones.buscar`) | 0 en las 7 | 0 en las 7 |
| fugas entre bloques (`bloques.fugas`) | — (no aplica) | 0 en las 7 |
| `back_view`: `both seat cheeks fully bare` | sí | sí |
| `back_view`: `not lifted, not parted` | no | no |

**Lo que el número dice y lo que no.** El motor de bloques **no adelgaza**: enruta las mismas 37 anclas a su bloque (por eso +2,7 %: las anclas de prenda ahora van completas en la oración B). Lo que cambia es **el orden y la agrupación** —A. B. C., cada atributo en un solo sitio, sin ecos que re-describan la prenda—. Miss Doll trae **21 cláusulas con peso** por prompt contra 5 de Ele: eso es su ADN, no el motor, y este experimento no lo toca.

## ⚠️ Hallazgo al emitir: este look NO ejercita el eje de exposición

El vestido del L86 es **crystal-mesh** y el detector de cobertura lo clasifica —correctamente— como transparente: la tanga se ve a través de él a propósito. Resultado: **las dos variantes piden `both seat cheeks fully bare` en el `back_view`**, y el mecanismo exacto que abrió la falda del L831 (una cola de peso exigiendo el asiento al aire contra una prenda que lo cubre) **no está en juego acá**. Lo que este A/B compara es *orden y agrupación*, no *exposición por construcción*.

Y destapa un **tercer estado** que ninguna de las dos variantes de `BOTTOM_CUT_LOCK` cubre: *el calzón visible A TRAVÉS de una prenda transparente que se queda en su sitio*. Hoy un vestido sheer cae en «expuesto» y recibe la cola que empuja a abrir la prenda — el mismo empujón del L831, sobre una prenda que no debía moverse. Es el caso del L826 de Ele (crystal-mesh slip dress) y del L86 de Miss Doll. **Decisión de la Ama:** ¿un tercer texto de exposición, «visible through the sheer outer garment, which stays in place»?

## Cómo hacerlo más fuerte (decisión de la Ama)

- **Opción 1 — quedarse con L86.** Barato (está 0/7 igual). Mide orden/agrupación. No mide exposición.
- **Opción 2 — repetirlo sobre el L831 de Ele.** Es el look que falló, con falda **opaca** y tanga debajo: el eje de exposición entra completo. Cuesta 14 generaciones sobre un look que ya tiene 7 imágenes — pero da **tres puntos**: las imágenes que ya existen (motor viejo *antes* del arreglo del 09/09), A (motor viejo *con* el arreglo) y B (bloques).

## Archivos

- `A_viejo_MD_L86.md` — 7 prompts + negativo, motor viejo.
- `B_bloques_MD_L86.md` — 7 prompts + negativo, motor de bloques. Reporte por bloque al emitir: `A=3042 B=3657 C=1813-2183` chars.
