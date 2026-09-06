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
| **Rotación de poses — repetición en ventana** | 🟠 máx 4/7 | 🔴 **6/7 en 4 pares** | 🔴 **7/7 en 3 pares** |

**Lo cromático y lo de arquitectura está esencialmente sano.** El agujero está en las **poses**, y es estructural.

---

## 2. 🔴 El hallazgo: la rotación de poses no tiene ventana, tiene ciclo

La fórmula declarada en `repertorios_pose.json` es:

```
indice = (numero_de_look - 1 + offset_del_slot) % len(variaciones)
```

**Consecuencia aritmética inevitable: cada slot se repite exactamente cada `len(variaciones)` looks.** No hay ventana de bloqueo como sí la tiene la silueta (≥3) o el color (2 en 5). Hay un ciclo fijo, y el tamaño del ciclo es el tamaño del repertorio.

| Muñeca | Tamaño de repertorio por slot | Peor par en la muestra |
|---|---|---|
| Ele | **9 · 7 · 6 · 7 · 6 · 8 · 8** | 4/7 slots — ninguno grave |
| Miss Doll | **7 · 7 · 7 · 7 · 9 · 7 · 7** | 🟠 **6/7** en L75↔L82, L76↔L83, L77↔L84, L78↔L85 |
| Anaïs | **7 · 7 · 7 · 7 · 7 · 7 · 7** | 🔴 **7/7** en L76↔L83, L77↔L84, L78↔L85 |

### Lo que esto significa, en concreto

**Anaïs tiene los siete repertorios de tamaño 7.** El ciclo es exactamente 7 looks, en todos los slots a la vez. Por lo tanto:

> **Anaïs L83, L84 y L85 llevan la dirección de pose *palabra por palabra* de L76, L77 y L78 — en los 7 slots.**

No es un descuido de un batch: es lo que la fórmula garantiza. Cada look de Anaïs es la repetición postural exacta del look 7 anterior, y lo seguirá siendo indefinidamente.

**Miss Doll** falla en 6 de 7 slots con el mismo período: solo `slot5` (Glacial Command, 9 variantes) rompe el patrón. Sus L82-L85 repiten postura de L75-L78.

**Ele es la única sana**, y no por diseño sino por accidente: sus tamaños son **9, 7, 6, 7, 6, 8, 8**, casi coprimos entre sí, así que los slots desfasan y ningún par comparte más de 4 de 7. Su punto débil son `seated` y `slot5`, ambos con **6** variantes — se repiten cada 6 looks.

### Confirmación independiente

La medición por similitud de texto —el instrumento que descarté por ruidoso— igual señaló **L76 ↔ L83 de Anaïs como el peor par en los 7 slots** (73-74% de léxico común en cada uno) sin conocer la fórmula. Dos métodos distintos apuntando al mismo par: el dato es firme.

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

**Mi recomendación: B ahora, C después.** B compra el resultado casi entero con el costo más bajo y sin tocar código; C es la solución de fondo y encaja natural cuando `generar` ya es la puerta.

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
