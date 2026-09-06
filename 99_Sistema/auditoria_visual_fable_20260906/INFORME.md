# INFORME — Auditoría visual 06/09/2026 · lo que alcanzó a medirse

Encargo de la Ama, tres ejes: **(1)** desvío de la imagen respecto del prompt · **(2)** continuidad
del outfit entre las poses de un mismo look · **(3)** las reglas nuevas de anti-repetición de color
y de atuendo. Ventana: últimos 20 looks de Anaïs y de Miss Doll, últimos 10 de Ele —corrida a
**L813-L822** por decisión suya, porque L823-L827 no tienen ninguna imagen.

---

## 0. COBERTURA REAL — leer esto antes que cualquier número

| | Planificado | Medido | Cobertura |
|---|---:|---:|---:|
| Ejes 1 y 2 (imagen) | 269 imágenes · 10 bandas | **50 imágenes · 2 bandas** | **18,6 %** |
| Eje 3 (texto) | 55 looks de la ventana | 55 looks | **100 %** |

**Por qué.** Las 10 bandas Fable se lanzaron en paralelo. Ocho cayeron por **límite de sesión del
modelo** sin escribir nada — error de diseño mío: el reporte se escribía al final, así que un corte
se llevaba todo el trabajo hecho. Se relanzaron con escritura incremental por look y **la Ama las
detuvo a los dos minutos**, con la orden de cerrar con lo que hubiera. Bandas vivas: **AN-3**
(Anaïs L77-L80) y **MD-4** (Miss Doll L82-L85).

**Lo que esto significa para leer las cifras:** los porcentajes de abajo son sólidos *para esos 8
looks* — cada falla está citada con la cláusula del prompt y lo que muestra el píxel. **No son la
flota.** Faltan sin mirar: Anaïs L66-L75 y L83-L85 · Miss Doll L66-L79 y L81 · **Ele entera**.
Ningún look de Ele fue auditado contra su imagen en esta pasada.

---

## 1. EJE 1 — Desvío imagen ↔ prompt

| Banda | Looks | Imágenes | Desvío | Continuidad | 🔴 con ancla | 🟡 sin ancla |
|---|---|---:|---:|---:|---:|---:|
| AN-3 · Anaïs L77-L80 | 4 | 22 | **10,4 %** | 78,6 % | 7 | 52 |
| MD-4 · Miss Doll L82-L85 | 4 | 28 | **7,7 %** | 81,2 % | 37 | 30 |

Detalle por look:

| Look | Desvío | Continuidad |
|---|---:|---:|
| Anaïs L77 Chocolate y Camel (1 pose) | 8,1 % | no medible |
| Anaïs L78 Marfil y Oro Viejo | 11,6 % | 72,7 % |
| Anaïs L79 Midnight Navy | **14,8 %** | 78,9 % |
| Anaïs L80 Berenjena Latex | 7,2 % | 84,2 % |
| Miss Doll L82 UV Violet Gym | 9,8 % | **63,2 %** |
| Miss Doll L83 Rosa Shocking y Cristal | **6,1 %** | 89,5 % |
| Miss Doll L84 Emerald Chrome | 7,7 % | 85,7 % |
| Miss Doll L85 Gunmetal Corsetry | 7,1 % | 86,4 % |

**El desvío es bajo — entre 6 y 15 %.** El motor está cumpliendo en lo grueso: setting 50/50,
calzado con la plataforma y la altura pedidas en todas las tomas legibles, medias del color y largo
correctos, prenda principal sin fallas de arquitectura en las 22 de Anaïs.

**Lo que falla no es aleatorio: son candados que existen y no muerden.**

---

## 2. EJE 2 — Continuidad dentro del outfit

Promedio medido: **~80 %**. O sea **una de cada cinco propiedades del vestuario cambia entre poses
del mismo look**, que es exactamente lo que la Ama describió («si en la primera pose el vestido es
hasta la rodilla, en el resto debe ser el mismo largo»).

Lo que se mueve, por orden de frecuencia:

1. **Escote** — se reinventa en 9 tomas de Miss Doll pese al ancla con peso `:1.4`.
2. **Manga y hombros** — peignoir obispo ↔ campana, puesto ↔ caído (Anaïs L78).
3. **Copas del sujetador** — raso ↔ encaje (Anaïs L78 y L79).
4. **Collar** — metal al frente ↔ látex a la nuca ↔ ausente (Anaïs L80).
5. **Color del tacón** — hereda el del empeine cuando difieren (Miss Doll L84, 4 de 4).
6. **Largo del pelo** — a media espalda en 8 de 22 imágenes de Anaïs, siempre con victory rolls.

El peor caso de la muestra es **Miss Doll L82 con 63,2 %**, y su causa está identificada: el ancla
`BOTTOM_CUT_LOCK` («cualquier prenda inferior deja el asiento descubierto») no distingue tanga de
legging, **y convirtió las calzas del look en chaps**.

---

## 3. LOS TRES HALLAZGOS QUE ARREGLAN EL MOTOR

### 3.1 El BLOQUE A le gana al BLOQUE B — y por eso el escote no obedece

El ADN de Miss Doll pide *"dramatic alluring plunging neckline, deep prominent cleavage"* **en todos
los looks, incluidos los de cuello alto**. El BLOQUE B fija el escote cerrado una sola vez, con
peso. El generador recibe dos órdenes incompatibles y obedece la del ADN, que se repite en cada
prompt. **Mientras esa cláusula viva en el ADN, un cuello alto es una apuesta, no un diseño.**

El mismo mecanismo explica el busto: la forma esférica del ADN rinde 12 de 12 en escote abierto y
falla en las 5 tomas de cuello cerrado. No es que el generador ignore el ADN — es que el ADN y la
prenda se contradicen y sólo uno puede ganar.

### 3.2 `ONE_HAND` falla en 7 de 8 tomas, y la causa es el encuadre

El ancla pide una sola mano visible; el encuadre pedido es *"waist-up medium shot"*. Con el corte a
la cadera, **la segunda mano entra sola por el borde inferior**. El arreglo no es más negativos: es
cortar el encuadre por encima de la cadera.

### 3.3 La costura de la media sigue a la cámara, no a la pierna

Aparece por el frente de la espinilla en cuatro tomas frontales, y por detrás cuando la toma es de
espaldas. En Anaïs L77 **el candado con peso `:1.4` estaba puesto y falló igual**; en L79 y L80, del
mismo batch, **el candado ni siquiera estaba** — el inyector no lo aplicó parejo. Dos defectos
distintos con el mismo síntoma.

---

## 4. Defectos que vienen del TEXTO, no del generador

Los más baratos de arreglar, y ninguno los estaba mirando:

- **Las Odaliscas de Miss Doll L82/L83/L84 piden *"cold pale steel grey eyes"*** — el iris viejo,
  contra el fence del ADN y contra su propio negativo. Es la plantilla del slot, no el look.
- **El negativo de los cuatro looks de Miss Doll lleva `corset, waist cincher, bustier`** — incluido
  el L85, que va vestido de corsé.
- **Fugas de Ele en el texto de las otras dos:** *"the navel piercing and the hip rune tattoos"* en
  Miss Doll L85 y en los 7 prompts de Anaïs L80. Ninguna de las dos tiene tatuajes ni piercings.
- **Anaïs L80: uñas de 5 cm + guantes cerrados** → garras de plata a través del látex en 4 de 7. La
  regla §5.6 ya existe; el batch no la aplicó.
- **Anaïs L79 pide *hold-up stockings*** y el generador añade liguero en 5 de 7.
- **Miss Doll L83 Odalisque:** cenital y cámara a nivel pedidas a la vez — irresoluble.
- Ningún BLOQUE B de Miss Doll fija color de labios ni sombra (campo 8 del §5.5).

**`outfit.py modularidad` no ve nada de esto** porque vive en el texto de las poses, no en la lógica
del motor.

---

## 5. EJE 3 — Anti-repetición (medición completa, determinista)

Detalle en [`EJE3_antirepeticion.md`](EJE3_antirepeticion.md). En tres líneas:

- **El tope de color funciona.** Cero violaciones del máximo de 2 por ventana; los tres batches
  nuevos salieron con familias cromáticas distintas.
- **La arquitectura no.** Miss Doll **L72 ↔ L78: 89,0 % de léxico común y 117 tramos de 8 palabras
  idénticos** — el mismo outfit escrito dos veces. Ele **L818 ↔ L823** (55,8 %, 43 n-gramas) ya está
  **bajo la regla nueva** y pasó igual.
- **Anaïs L71-L75 repite 5 de 5 arquitecturas** del batch anterior, y es justo el batch que se
  rehízo «desde cero» tras un rechazo: se cambió el color y el detalle, no el molde.

---

## 6. Lo que queda pendiente

Sin auditar contra su imagen: **Anaïs L66-L75, L83-L85 · Miss Doll L66-L79, L81 · Ele L813-L822
completa** — 219 de las 269 imágenes.

Cuando se retome, la rúbrica y el reparto por bandas ya están escritos y son reutilizables. Lo único
que hay que conservar del intento fallido es la lección: **el reporte se escribe por look, no al
final** — un corte a mitad no puede llevarse el trabajo ya hecho.
