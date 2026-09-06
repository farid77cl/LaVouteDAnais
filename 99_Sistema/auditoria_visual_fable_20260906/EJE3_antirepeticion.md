# EJE 3 — Anti-repetición de color y de atuendo · medición determinista · 06/09/2026

Encargo de la Ama: *"que se auditen las nuevas reglas de anti repeticiones de color y de atuendos"*.

**Por qué este eje NO lo mira la Fable:** es texto, no píxel, y ya tiene ejecutor determinista
(`outfit.py cruce`, `color_canon` + `rotacion_color`, `rotacion_prenda`). Un modelo mirando
imágenes da una impresión; el n-grama da un número que se puede volver a medir mañana y sale
igual. La Fable aporta lo que el script NO puede: si dos looks **se ven** el mismo outfit en la
imagen aunque el texto diga otra cosa.

**Alcance, por decisión de la Ama (06/09):** retroactivo con marca. Se mide toda la ventana
auditada (Anaïs L66-L85 · Miss Doll L66-L85 · Ele L813-L827) y se separa lo **VIGENTE** —bajo el
ancla de la regla: Ele 823 / Miss Doll 81 / Anaïs 81— de lo **histórico**, que es informativo y
queda a su decisión.

Comandos y su salida cruda: `outfit.py cruce` (65 looks de 13 batches). La medición intra-muñeca
se hizo con los mismos umbrales y el mismo n-grama de 8 palabras del auditor cruzado, a propósito:
un segundo criterio propio es exactamente como nació el lío de auditar lo mismo dos veces con
reglas que no calzaban.

---

## 1. El hallazgo que manda: dos looks que son el MISMO outfit escrito dos veces

| Par | Léxico común | N-gramas de 8 palabras verbatim | Estado |
|---|---:|---:|---|
| **Miss Doll L72 ↔ L78** | **89,0 %** | **117** | histórico (anterior al L81) |
| Miss Doll L73 ↔ L79 | 59,6 % | 23 | histórico |
| **Ele L818 ↔ L823** | **55,8 %** | **43** | 🔴 **VIGENTE** |
| Miss Doll L76 ↔ L84 | 48,6 % | 3 | 🔴 **VIGENTE** |

**Miss Doll L72 ↔ L78 con 117 tramos de ocho palabras idénticos no es "parecido": es el mismo
párrafo.** Y es exactamente el defecto que la regla `rotacion_prenda` no puede ver, porque su
ventana es de 3 looks y entre el L72 y el L78 hay seis.

**Ele L818 ↔ L823 sí está bajo la regla nueva y pasó igual** — 43 n-gramas verbatim, misma
arquitectura HF1. El L823 es el primer look de Ele diseñado bajo el ancla; el candado lo dejó
entrar.

Anaïs es la única limpia en este eje: **0 clones duros consigo misma** en los 20 looks.

---

## 2. Clones ENTRE muñecas (`outfit.py cruce` X1) — 17 duros

Lo peor, ordenado por gravedad:

| Par | Arquitectura | Léxico | N-gramas |
|---|---|---:|---:|
| **Ele L815 ↔ Miss Doll L67** | M3 | **69,7 %** | 40 |
| **Ele L821 ↔ Miss Doll L71** | M7 | 59,5 % | **64** |
| Anaïs L80 ↔ Miss Doll L72 | M4/A6 | 56,7 % | 37 |
| Ele L826 ↔ Miss Doll L80 | M10 | 56,4 % | 23 |
| Anaïs L80 ↔ Miss Doll L78 | M4/A6 | 56,3 % | 39 |
| Ele L819 ↔ Miss Doll L73 | M2 | 54,7 % | 12 |
| Anaïs L78 ↔ Miss Doll L74 | M3 | 53,9 % | 44 |
| Anaïs L80 ↔ Ele L820 | M4/A6 | 51,5 % | 33 |

**El patrón, que vale más que la lista:** la arquitectura **M4/A6** aparece clonada en cuatro
muñecas-looks a la vez (Anaïs L80, Ele L820, Miss Doll L72/L78/L85) y **M9** en otros cuatro
(Anaïs L76, Ele L818, Miss Doll L81). No son coincidencias sueltas: son dos moldes que se están
reutilizando entre las tres.

---

## 3. Tope de familia cromática (X3)

**Ninguna violación del tope de 2 por ventana de 5.** Lo que sí falla es la otra mitad de la regla
—que dos de la misma familia no vayan pegados— y falla seis veces, todas **históricas**:

- Anaïs L70→L71 `red` pegado · Ele L818→L819 `green` y L820→L821 `blue` pegados ·
  Miss Doll L63→L64 y L70→L71 `pink`, L75→L76 `blue`.

**Los batches nuevos, bajo la regla, están limpios en color:**
- Ele L823-L827: `red · green · orange · blue · metal` — cinco familias distintas.
- Anaïs L81-L85: `neutral-dark · green · metal · purple · metal`.
- Miss Doll L81-L85: `pink · purple · pink · green · metal`.

O sea: **el tope de color funciona; el que no está funcionando es el de arquitectura.**

---

## 4. Arquitectura repetida contra el batch anterior (X4)

| Batch | Repite del anterior | Estado |
|---|---|---|
| **Anaïs L71-L75** | **5 de 5** (las cinco son M6, ya en L69) | histórico |
| **Miss Doll L76-L80** | **3 de 5** (L77=M7, L78=M4/A6, L79=M2) | histórico |
| Miss Doll L81-L85 | 2 de 5 (L84=M1, L85=M4/A6) | histórico |
| Ele L813-L817 | 2 de 5 (L815 y L817 = M3) | histórico |
| Miss Doll L71-L75 | 2 de 5 (L74=M3, L75=M6) | histórico |
| Anaïs L81-L85 | 1 de 5 (L85=M7) | histórico |
| Ele L823-L827 | 1 de 5 (L827=M1) | histórico |

**Anaïs L71-L75 repitiendo 5 de 5 arquitecturas es el peor dato del eje entero**, y es justo el
batch que se rehízo «desde cero» tras un rechazo — se rediseñó el color y el detalle, no el molde.

La vara dura de X4 rige recién desde Ele 828 / Miss Doll 86 / Anaïs 86, así que todo esto entra
como aviso. **Pero el número dice que la vara nueva va a chocar de inmediato:** con el
comportamiento medido, el próximo batch de cada muñeca repite entre 1 y 3 arquitecturas.

---

## 5. Lectura de fondo

1. **El color ya está gobernado; la silueta no.** El tope cromático del 05/09 cumple en los tres
   batches nuevos. La arquitectura de prenda sigue repitiéndose dentro de cada muñeca, entre
   muñecas y contra el batch anterior.
2. **La ventana de 3 de `rotacion_prenda` es demasiado corta para batches de 5.** El L72↔L78 de
   Miss Doll (117 n-gramas) cae exactamente en el punto ciego, y el L818↔L823 de Ele lo confirma
   cruzando el borde del batch.
3. **Dos moldes concentran el daño: M4/A6 y M9.** Antes de tocar el linter conviene mirarlos: si
   dos arquitecturas producen el 40 % de los clones, el problema puede estar en cómo están
   escritas en la biblioteca de siluetas, no en quién las elige.
