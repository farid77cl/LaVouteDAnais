# Auditoría de Reglas — antirepetición, poses y metas de arquetipo · 06/09/2026

**Encargo de la Ama:** *"quiero saber si se están cumpliendo las reglas de antirepetición y poses, en la misma muestra de 10 outfits cada muñeca. Con más información tomaré decisiones."* · ampliado en la misma sesión: *"audita también que se estén cumpliendo los porcentajes de los arquetipos por muñeca"* (§5).

**Muestra:** Ele L817-L827 (11 looks declarados) · Miss Doll L75-L85 (11) · Anaïs L76-L85 (10).
Se auditan los **looks declarados en galería**, materializados o no: la antirepetición es una regla de texto y rige desde que el look se escribe.

**Método:** medición determinista sobre las galerías y sobre `repertorios_pose.json`, reutilizando los clasificadores del motor (`clasificar_arquitectura`, `color_canon`) a propósito — un criterio propio paralelo es exactamente como nació el lío de auditar la misma galería con dos varas distintas.

> ⚠️ **Dos instrumentos que descarté por equivocados, y por qué.** Primero medí repetición de poses por *similitud de texto* entre prompts: dio 550-750 n-gramas compartidos entre cualquier par, porque el prompt es ~85% boilerplate idéntico **por diseño**. Es la misma clase de error que un linter que se lee a sí mismo. La rotación de poses es **aritmética determinista**, así que se mide exacto con la fórmula, no por parecido.

---

## 1. Veredicto en una tabla

| Regla | Ele | Miss Doll | Anaïs |
|---|---|---|---|
| Arquitectura de prenda no repetida en ventana | 🟠 1 par a distancia 5 | ✅ | ✅ |
| Diversidad de arquitecturas | 9 en 11 | 9 en 11 | 9 en 10 |
| Clon intra-personaje (n-gramas verbatim) | 🔴 4 pares duros | ✅ máx 5 n-gramas | 🟠 4 pares en aviso |
| Clon cruzado entre muñecas | 🔴 | 🔴 | 🔴 |
| Familia cromática — nunca pegadas | 🟠 2 pares (pre-regla) | 🟠 1 par (pre-regla) | ✅ |
| Familia cromática — tope por ventana | ✅ | ✅ (rosa firma, 3/5 = su techo) | ✅ |
| 7 slots presentes y con nombre canónico | ✅ | ✅ | ✅ |
| **Rotación de poses — repetición en ventana** | ✅ máx 2/7 | 🔴 **6/7 en 4 pares** | 🔴 **7/7 en 3 pares** |

**Lo cromático y lo de arquitectura está esencialmente sano.** El agujero está en las **poses**, y es estructural.

---

## 2. 🔴 El hallazgo: la rotación de poses no tiene ventana, tiene ciclo

La fórmula, en la ruta de emisión **viva** (`prompt_builder.py:319-320`, que lee los offsets del JSON y es lo que corre `outfit.py generar` → `PromptBuilder.pose()`):

```
indice = (numero_de_look - 1 + offset_del_slot) % len(variaciones)
```

**Consecuencia aritmética inevitable: cada slot se repite exactamente cada `len(variaciones)` looks.** No hay ventana de bloqueo como sí la tiene la silueta (≥3) o el color (2 en 5). Hay un ciclo fijo, y el tamaño del ciclo es el tamaño del repertorio.

| Muñeca | Tamaño de repertorio por slot | Peor par en la muestra |
|---|---|---|
| Ele | **9 · 7 · 6 · 7 · 6 · 8 · 8** | ✅ **2/7 slots** — la mejor de las tres |
| Miss Doll | **7 · 7 · 7 · 7 · 9 · 7 · 7** | 🟠 **6/7** en L75↔L82, L76↔L83, L77↔L84, L78↔L85 |
| Anaïs | **7 · 7 · 7 · 7 · 7 · 7 · 7** | 🔴 **7/7** en L76↔L83, L77↔L84, L78↔L85 |

### Lo que esto significa, en concreto

**Anaïs tiene los siete repertorios de tamaño 7.** El ciclo es exactamente 7 looks, en todos los slots a la vez. Por lo tanto:

> **Anaïs L83, L84 y L85 llevan la dirección de pose *palabra por palabra* de L76, L77 y L78 — en los 7 slots.**

No es un descuido de un batch: es lo que la fórmula garantiza. Cada look de Anaïs es la repetición postural exacta del look 7 anterior, y lo seguirá siendo indefinidamente.

**Miss Doll** falla en 6 de 7 slots con el mismo período: el único que rompe el patrón es **`odalisque`, con 9 variantes** (`miss_doll.md:105` lo dice literal: *"el slot Seated conserva sus 7 variantes y el Odalisque sus 9"*). Sus L82-L85 repiten postura de L75-L78.

**Ele es la única sana**, y no por diseño sino por accidente: sus tamaños son **9, 7, 6, 7, 6, 8, 8** — **no coprimos** (hay dos 7, dos 6 y dos 8), pero sí *distintos entre sí*, que es lo que hace desfasar los slots. **Ningún par de su muestra comparte más de 2 de 7.** Su punto débil son `seated` y `slot5`, ambos con **6** variantes — se repiten cada 6 looks, y 4 de sus 7 slots vuelven a coincidir cada 24.

### Confirmación independiente

**Verificado contra el texto real de la galería** por revisión externa independiente: Anaïs Standing L76 y L83 abren con las **mismas 47 palabras carácter por carácter** (`full body from a slightly low angle, one arm raised across the body with the fingers of the other hand at its wrist adjusting the edge of the glove…`), y el texto solo diverge al entrar el setting. Es `repertorios_pose.json → anais.standing[6]` servido dos veces. Además, la sub-pose observada coincide con la predicha por la fórmula en **224 de 224 prompts** de la muestra.

Y la auditoría visual del mismo día encontró, por los ojos: *"en L76, L78 y L79 el prompt pedía tres puestas distintas y las tres salieron igual"*. La aritmética explica de dónde viene la sensación.

### Las dos promesas escritas en el JSON

| Promesa | Estado |
|---|---|
| *"dos looks consecutivos nunca comparten variación en el mismo slot"* | ✅ **Se cumple en las tres.** Es cierta — pero es una garantía de distancia 1, no una ventana |
| *"dentro de un mismo look los siete slots caen en índices distintos"* | 🟠 **Falsa en Ele y Miss Doll** — pero la promesa está mal formulada: cada slot tiene su propio repertorio, así que dos slots con el mismo *índice* no comparten ningún texto. Es una condición que no mide lo que dice medir |

---

## 3. Antirepetición de prenda — lo que sí funciona

### Arquitectura (familia M)

| Muñeca | Secuencia | Repeticiones |
|---|---|---|
| Ele | M3·M9·M2·M4/A6·M7·M1·M6·M8·M3·M10·M1 | M3 a distancia 8 ✅ · 🟠 **M1 a distancia 5** (L822, L827) |
| Miss Doll | M6·M1·M7·M4/A6·M2·M10·M9·M8·M3·M1·M4/A6 | M1 a distancia 8 ✅ · M4/A6 a distancia 7 ✅ |
| Anaïs | M9·M7·M3·M10·M4/A6·M4/A4·M4/A2·M8·M4/A5·M7 | M7 a distancia 8 ✅ |

**9 arquitecturas distintas en 10-11 looks en las tres.** La regla de silueta está mordiendo. El único roce es Ele L822↔L827 (M1 a distancia 5), que ya lo había reportado `cruce` como aviso.

### Clon intra-personaje (n-gramas de 8 palabras verbatim, calzado excluido)

| Muñeca | Peores pares |
|---|---|
| Ele | 🔴 **L818↔L823: 19 n-gramas · 53,5% léxico** · L824↔L825: 14 · L823↔L824: 13 · L825↔L826: 11 |
| Miss Doll | L84↔L85: 5 n-gramas · 41,6% — el resto ≤2. **La más limpia de las tres** |
| Anaïs | L78↔L79: 7 · L83↔L85: 7 · L76↔L80: 6 |

**Ele es la que peor está en redacción repetida**, justo la muñeca cuya galería tiene 628 looks: se me está gastando el vocabulario.

### Clon cruzado entre muñecas (dentro de la muestra)

| Par | Arquitectura | Medida |
|---|---|---|
| 🔴 miss_doll L78 ↔ anais L80 | M4/A6 ambas | 12 n-gramas · **54,9% léxico** |
| 🔴 ele L826 ↔ miss_doll L80 | M10 ambas | 9 n-gramas · **54,3% léxico** |
| 🔴 ele L820 ↔ miss_doll L78 | M4/A6 ambas | 8 n-gramas · 46,7% |
| 🟠 ele L820 ↔ anais L80 | M4/A6 ambas | 6 n-gramas · 50,4% |

**Cuando dos muñecas caen en la misma familia de arquitectura, el texto se parece demasiado.** El corsé de una y el de la otra son el mismo párrafo con otro color. `outfit.py cruce` lo confirma a escala completa: **17 hallazgos duros y 23 avisos** en toda la flota.

### Color

| Muñeca | Secuencia en la muestra | Estado |
|---|---|---|
| Ele | metal·green·**green**·blue·**blue**·purple·red·green·orange·blue·metal | 🟠 2 pares pegados (L818-819, L820-821) — **anteriores al L823**, que es desde donde rige la regla |
| Miss Doll | blue·**blue**·pink·neutral-dark·pink·blue·pink·purple·pink·green·metal | 🟠 1 par pegado (L75-76), **anterior al L81**. El rosa a 3 en ventana de 5 es su **familia firma**, techo propio de 3 — cumple |
| Anaïs | green·neutral-warm·neutral-light·blue·purple·neutral-dark·green·metal·purple·metal | ✅ limpia |

**Ninguna violación posterior a la fecha de vigencia de cada regla.** El tope de color, que nació el 05/09, está funcionando.

---

## 4. Qué decidir — las tres opciones sobre las poses

El problema tiene una sola causa (repertorios chicos + módulo fijo) y tres salidas posibles. **Ninguna la ejecuto sin su palabra.**

**Opción A — agrandar los repertorios.** Escribir variantes nuevas hasta que ningún slot baje de ~15. Anaïs pasaría de repetirse cada 7 looks a cada 15. Es trabajo de redacción y no toca el código.
· *Costo:* ~50 variantes nuevas repartidas entre las tres. *Efecto:* duplica el ciclo, no lo elimina.

**Opción B — hacer los tamaños coprimos.** Es lo que hace sana a Ele por accidente (9·7·6·7·6·8·8). Si Anaïs pasa de 7·7·7·7·7·7·7 a algo como 7·8·9·11·13·6·5, dejaría de haber un par de looks que comparta los 7 slots: **nunca más dos looks con la misma postura completa**.
· *Costo:* mucho menor que A — bastan unas pocas variantes nuevas en los slots correctos. *Efecto:* mata el defecto de raíz.

**Opción C — ventana real, como la tiene la silueta.** Cambiar el módulo por una elección que consulte los últimos N looks y descarte lo usado, igual que `generar` ya hace con arquitectura y color desde el 05/09.
· *Costo:* toca el motor. *Efecto:* es el arreglo correcto y el más caro.

> 🔴 **Recomendación CORREGIDA tras revisión externa (06/09, mismo día).** Mi recomendación original era «B ahora, C después». **B es cosmética y su premisa era falsa.** La coprimalidad no elimina la repetición: solo empuja el clon *completo* al mínimo común múltiplo, mientras **cada slot sigue reciclándose cada `n` looks**. Y el ejemplo que propuse (`7·8·9·11·13·6·5`) **empeora la frecuencia**: baja el repertorio más chico de 7 a **5**, o sea un slot repitiéndose cada 5 looks, más seguido que hoy.
>
> **La salida real es C.** A (agrandar repertorios) es un paliativo honesto mientras tanto — sube el período de todos los slots a la vez y no depende de aritmética fina. B se descarta.

> 🕳️ **Y lo que este informe no decía, y es la mitad del problema:** hoy **ningún auditor mira la rotación de poses entre looks**. El chequeo 7 de `lint_prompts_personaje.py` detecta poses duplicadas *dentro* de un look, jamás *entre* looks. Por eso el defecto vivió intacto: no es que un chequeo fallara, es que no existe.

**Y una cosa aparte, que sí es mía y no necesita su decisión:** los 4 pares 🔴 de clon intra-personaje de Ele y los 4 cruces entre muñecas son redacción repetida mía. Se arreglan reescribiendo, no rotando.

---

## 5. Metas de arquetipo por muñeca

**Fuente de las metas (dueño único):** `02_Personajes/_perfiles_visuales/<slug>.md` §6.
**Alcance del conteo:** Ele y Miss Doll sobre la galería completa; **Anaïs desde el Look 41**, como manda su §6 (*"el conteo de cuota reinicia en cero desde el Look 41"*).

> ⚠️ **Dos errores míos de parser, cazados antes de reportar.** La primera pasada leyó el campo con la cola `· **Paleta:** …` pegada y me tiró 8 de 10 arquetipos de Miss Doll como "fuera de tabla"; la segunda ignoraba la variante `**Categoria / Subcategoria:**` que usan los looks viejos de Ele. Los dos corregidos. Sin eso le habría reportado a Miss Doll con 7 arquetipos en rojo profundo, que era falso.

### Ele — 628 looks · 512 clasificables (81,5%)

| Arquetipo | Meta | Real | n | Desvío |
|---|---:|---:|---:|---:|
| 🟠 High-Fashion Editorial | 9,4% | 6,6% | 34 | **−2,8** |
| Corporate | 9,4% | 7,8% | 40 | −1,6 |
| Bikini | 9,4% | 8,4% | 43 | −1,0 |
| Domestic | 9,4% | 8,4% | 43 | −1,0 |
| Lencería | 15,0% | 14,6% | 75 | −0,4 |
| Pin-Up | 9,4% | 10,0% | 51 | +0,6 |
| Nightclub | 9,4% | 10,2% | 52 | +0,8 |
| Escort | 9,4% | 10,4% | 53 | +1,0 |
| Gym | 9,4% | 10,5% | 54 | +1,1 |
| 🟠 Stripper | 9,4% | 13,1% | 67 | **+3,7** |

**Manda el déficit: High-Fashion Editorial.** Ocho de diez arquetipos dentro de ±2 puntos. Los dos extremos son los mismos de siempre: sobra Stripper, falta editorial.

### Miss Doll — 85 looks · 70 clasificables (82,4%)

| Arquetipo | Meta | Real | n | Desvío |
|---|---:|---:|---:|---:|
| 🔴 Bikini / Lencería Erótica | 15,0% | 20,0% | 14 | **+5,0** |
| 🟠 VIP / Privado | 12,0% | 10,0% | 7 | −2,0 |
| Calabozo / Dungeon | 13,0% | 11,4% | 8 | −1,6 |
| Club / Escenario | 18,0% | 17,1% | 12 | −0,9 |
| Girly Girl | 12,0% | 11,4% | 8 | −0,6 |
| Gym / Athletic | 12,0% | 11,4% | 8 | −0,6 |
| Penthouse / Off-duty | 9,0% | 8,6% | 6 | −0,4 |
| Editorial / Portada | 9,0% | 10,0% | 7 | +1,0 |

**Un solo rojo: le sobra Bikini/Lencería.** Manda el déficit de VIP/Privado. 15 looks quedan fuera del conteo porque su única etiqueta es `Mix`, del paraguas viejo.

### Anaïs — 45 looks desde L41 · 45 clasificables (100%)

| Arquetipo | Meta | Real | n | Desvío |
|---|---:|---:|---:|---:|
| 🟠 Látex / Fetichismo | 20,0% | 22,2% | 10 | +2,2 |
| Ejecutivo de Poder | 7,0% | 8,9% | 4 | +1,9 |
| Boudoir / Lencería | 27,0% | 26,7% | 12 | −0,3 |
| Sesión Literaria | 13,0% | 11,1% | 5 | −1,9 |
| Noche / La Voûte | 33,0% | 31,1% | 14 | −1,9 |

**La más sana de las tres, y por lejos.** Ningún desvío pasa de 2,2 puntos y el 100% de sus looks es contable — porque su reset del 11/08 obligó al etiquetado textual y ella arrancó de cero con la regla puesta.

### La regla de déficit funciona — está medido

Los mismos números medidos el 05/09, antes de los batches correctivos, contra los de hoy:

| | 05/09 | 06/09 | |
|---|---:|---:|---|
| Miss Doll · Bikini/Lencería | +6,2 | **+5,0** | ↓ corrigiendo |
| Miss Doll · Club/Escenario | −2,8 | **−0,9** | ↓ casi cerrada |
| Anaïs · Noche/La Voûte | −5,5 | **−1,9** | ↓ corrigiendo |
| Ele · High-Fashion Editorial | −2,2 | −2,8 | ↑ (11 looks nuevos diluyen) |

Los batches del 05/09 se diseñaron contra el déficit medido —Ele abre en High-Fashion Editorial, Miss Doll lleva **dos** Club/Escenario, Anaïs lleva **tres** Noche— y las tres brechas que apuntaban se cerraron. **La regla muerde cuando se aplica.**

### 🔴 El problema real no son las metas: es que casi no se pueden medir

El campo `**Arquetipo:**` / `**Categoría:**` existe **solo en los batches del 05/09 en adelante**. En la muestra de 10:

| Muñeca | Looks con campo | Looks sin campo |
|---|---|---|
| Ele | L823-L827 (5) | **L817-L822 (6)** |
| Miss Doll | L81-L85 (5) | **L75-L80 (6)** |
| Anaïs | L81-L85 (5) | **L76-L80 (5)** |

Los batches del **04/09 no lo llevan**. A escala de flota: Ele tiene **105 de 628 looks sin el campo**, y Miss Doll solo **21 de 85 lo traen (24,7%)** — el resto se lee del título, y 15 de ellos dicen literalmente `Mix`, que no mapea a ninguna categoría.

Esto es exactamente el bug que se cerró el 05/09 (*"`generar` nunca escribió el campo de arquetipo"*): **la corrección quedó puesta hacia adelante y nunca se retrofiteó.** Mientras tanto los porcentajes se calculan sobre el 81-82% de la flota en dos de las tres muñecas, y la regla de déficit es ciega sobre el resto.

### 🔴 Hallazgo colateral: mojibake que ningún linter mira

**11 looks de Ele (L690-L700)** tienen el encoding roto en la galería — `Â·`, `â€"`, `ðŸ§›`, `Ã©` — y `lint_higiene_repo.py` da el repo **LIMPIO**. No es un fallo del linter: su chequeo H6 **excluye las galerías a propósito** (pertenecen a `lint_galeria.py`), y `lint_galeria.py` **no chequea encoding**. La galería más grande del repo no tiene a nadie mirándole el encoding. Miss Doll y Anaïs están limpias.

### Qué propongo

1. **Retrofitear el campo de arquetipo** en los looks que no lo tienen — para Ele son 105, y para la mayoría el dato está en el título, así que es un script, no trabajo a mano.
2. **Sumar el chequeo de encoding a `lint_galeria.py`**, que es quien sí mira las galerías.
3. **Las metas en sí no necesitan intervención.** Ele arrastra Stripper +3,7 y HF Editorial −2,8; el próximo batch suyo debería llevar dos High-Fashion Editorial y cero Stripper. Miss Doll debe frenar Bikini/Lencería y sumar VIP/Privado. Anaïs no necesita nada.

---

## 6. Revisión externa — qué se cayó y qué resistió (06/09/2026)

Por orden de la Ama (*"que sea auditor externo, no tú porque sueles equivocarte cuando te auto auditas"*), un revisor independiente re-derivó estos números con parser propio sobre los 32 looks / 224 prompts, identificando la sub-pose de cada prompt **empíricamente** (match verbatim contra el JSON, sin usar la fórmula).

**Recuento: 13 confirmados · 3 parciales · 4 refutados.**

### Lo que resistió

- **El hallazgo central, entero.** Anaïs L83/L84/L85 repiten la postura de L76/L77/L78 en los 7 slots, verificado **contra el texto real de la galería**: 47 palabras idénticas carácter por carácter en Standing. La fórmula existe tal cual en la ruta viva (`prompt_builder.py:319-320`) y predice **224/224** sub-poses.
- Los cuatro pares 6/7 de Miss Doll · las secuencias de color (coinciden valor por valor con `outfit.py cruce` §X3) · las de arquitectura y el 9-en-11 (coinciden con `lint` chequeo 12) · las dos promesas del JSON · los 17 duros y 23 avisos de `cruce`.

### Los cuatro errores míos, corregidos arriba en el cuerpo

| # | Error | Corrección |
|---|---|---|
| 1 | *"solo `slot5` (Glacial Command, 9 variantes) rompe el patrón"* en Miss Doll | El 9 está en **`odalisque`**; slot5=7. **Consecuencia práctica: quien tomara el informe habría escrito las variantes nuevas en el slot equivocado** |
| 2 | *"peor par de Ele: 4/7"* | El peor par real es **2/7**. El 4/7 es el peor caso *teórico* a distancia 24, fuera de la ventana. Presenté como medido algo que no medí |
| 3 | *"Confirmación independiente"* vía similitud de texto | **Circular** — invoqué como aval el mismo instrumento que descarté por inválido dos párrafos antes. Reemplazado por la evidencia verbatim |
| 4 | Recomendación B | **Refutada.** Ver el recuadro del §4 |

### Dos parciales que dejo anotados

- **Las cifras de clon intra-personaje del §3 no son reproducibles** sin publicar mi definición de troceo: el revisor, con implementación propia, obtiene `L823↔L824 = 23 n-gramas` como peor par de Ele y `L818↔L823 = 15 / 50,9%`. **El orden se sostiene** (Ele ≫ Anaïs ≥ Miss Doll); las magnitudes concretas, no. Tómense como ranking, no como medida.
- **El ✅ a la arquitectura de Miss Doll y Anaïs** es correcto contra la ventana de 3-5, pero `cruce` §X4 sí emite avisos sobre esos mismos looks (`miss_doll L84=M1 ya en L76`, `L85=M4/A6 ya en L78`, `anais L85=M7 ya en L77`). Son ventanas distintas; el ✅ no debía ir sin citar el aviso.

### 🔴 Una regla violada que yo no miré

**Miss Doll lleva medias en L83, L84 y L85 — tres seguidas**, contra el máximo de 2 consecutivos de `miss_doll.md:258`. Verificado sobre el BLOQUE B: L75-L77 y L79-L81 sin medias, L78 con, L82 no lo declara. **Es del último batch y está sin corregir.**

### Reglas que este informe no auditó

| Regla | Resultado sobre la muestra |
|---|---|
| R1 · Cuota de silueta cubierta ≥1 de cada 4 | ✅ limpia en las tres (Ele 38% · MD 41% · Anaïs 59%) |
| **R2 · Miss Doll máx 2 looks seguidos con medias** | 🔴 **VIOLADA — L83, L84, L85** |
| R3 · Ventana de escenario | 🟠 Ele 1 hit (`mirror` L820/L822) · MD 3 (`mirrored` L76-77, `pool` L78-79, `mirrored` L81-83) · Anaïs limpia |
| R4 · Arquitectura contra el batch anterior (X4) | 🟠 4 casos; el informe solo mencionaba uno |
| R5 · Ele animal print ≥1 de cada 8 | ✅ cumple (L817 y L825, distancia 8) |
| R6 · Anaïs corsé+tanga ≥2 de cada 5 | ✅ con holgura: **4 de 5** en L81-L85 |
| R7 · Anaïs guantes de ópera >3 de cada 5 | ✅ **corregida** — de 8 de 10 el 05/09 a **3 de 5** hoy, justo en el límite |
| R8 · Anti-monoblock | **No medible**: el modo cromático no es campo declarado en los batches |
| R9 · Rotación de calzado | **No medible**: el calzado vive dentro del BLOQUE B, sin campo propio |

### Y una línea de `CLAUDE.md` que estaba mintiendo

`CLAUDE.md` describía a Miss Doll como *"corset in every look"*. **Esa regla está derogada**: `02_Personajes/_perfiles_visuales/miss_doll.md:74` — *"el `corset/waist cincher/bustier` va en negative BASE porque el corsé ya no es obligatorio (§5.5)"*. Corregido el mismo día.

### El error de método que hay que retener

**Ningún módulo de rotación se citó con `archivo:línea`.** Cité el JSON (el dato) y nunca el código (el comportamiento) — que es justo la brecha por la que `pose_rotation_v5.rotate_poses:761` lleva viviendo con **otra fórmula** (`(look_number + off)`, sin el −1, con offsets hardcodeados) **y sin ningún llamador vivo**. No tumba nada, porque la ruta que emite es la otra; pero un informe que no cita el código no puede distinguir cuál de los dos corre.
