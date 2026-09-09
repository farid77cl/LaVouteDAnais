# 📝 El prompt visto por Bloque A / B / C — auditoría pedida por la Ama (09/09/2026)

> **La pregunta:** si el prompt del outfit-engine está desordenado, repite cosas y se
> contradice — mirado como Bloque A (cuerpo) + Bloque B (outfit) + Bloque C (pose+ambiente).
> **La respuesta:** sí a las tres, con evidencia. Una (la contradicción de print animal)
> ya se corrigió hoy mismo; las otras dos quedan anotadas para que decida.

---

## 1 · Contradicción real — CORREGIDA hoy

`FABRIC_PRISTINE` (global, en `_todos`, dispara en TODO look desde el 30/08/2026) dice:

> *"every fabric surface is pristine and unprinted... (all garment surfaces clean,
> solid-coloured and unmarked:1.4)"*

`ANIMAL_PRINT_LOCK` (opt-in, dispara cuando el BLOQUE B nombra leopardo/cebra/etc.) dice
lo opuesto sobre la MISMA prenda:

> *"the [print] is a genuine [...] marking texture rendered consistently across every
> visible inch of the printed fabric"*

**Medido en vivo:** el prompt de Standing del Look 832 (zebra cincher, batch 828-832,
07/09/2026) llevaba las dos cláusulas en el mismo texto — una afirmando que la tela no
tiene marca, con peso `:1.4`, y la otra describiendo la marca que sí tiene.

**Fix aplicado** en `prompt_builder.py::build()`: `FABRIC_PRISTINE` se descarta del
prompt cuando `ANIMAL_PRINT_LOCK` está presente. El candado sigue protegiendo a todo
look sin print declarado — solo se retira donde el propio look declara una marca real.
Verificado: `outfit.py test` sigue en 132/132, y reconstruyendo el Standing del L832 con
el builder corregido la cláusula de "unmarked" ya no aparece y la de zebra sí.

## 2 · Repetición Bloque A ↔ Bloque B — no corregida, es de diseño

El ADN de Ele (Bloque A, `ele.md` fence) termina en:

> *"...extra long French XXXL nails with white tips and pink base 5cm."*

Y el outfit de cada look (Bloque B) vuelve a nombrar la uña, con otra redacción, ej.
Look 831: *"XXXL French manicure at 5cm, sharp white tips with translucent pink
underneath"*.

**Medido:** 4.496 apariciones de la palabra "nail" en `galeria_outfits.md` contra 634
looks × ~7 prompts + 1 campo de outfit ≈ 8 — la uña se declara dos veces en CADA prompt
de CADA look, con dos redacciones que no siempre coinciden en el detalle (base vs.
underneath). No rompe la imagen (ambas piden lo mismo), pero es texto que se repite sin
variar nada y le resta densidad de atención al resto del Bloque B — mismo patrón que el
"texto muerto" ya diagnosticado el 06/09 para las medias.

**No es un bug, es una decisión de si Bloque A también es dueño de la uña o si el outfit
debería dejar de repetirla.** Cambia el ADN de las tres muñecas — se anota, no se toca.

## 3 · El Bloque C no es "pose + ambiente" — es un muro de candados con la pose adentro

`build()` ensambla el cuerpo del prompt como:

```
[anclas globales] + [anclas de slot] + [pose] + [setting]
```

Contando el Standing del L831: **antes** de llegar a la pose real ("the shoulders
propped against the floor-to-ceiling office glass...") el prompt ya acumuló ~600
palabras de candados anti-defecto (SINGLE_FRAME, GARMENT_CONSISTENCY, PHOTOREAL_LOCK,
BOTTOM_CUT_LOCK, todo garment ausente, DRESS_LEG_CLOSURE, stockings lock, anatomía,
FABRIC_PRISTINE) — todos necesarios, ninguno sobra individualmente, pero ninguno tiene
jerarquía: es una sola frase larguísima separada por comas donde lo único que varía
pose a pose (el gesto, el encuadre) es una cláusula corta enterrada casi al final.

**No es una contradicción ni una repetición — es la causa estructural de por qué las
dos anteriores son difíciles de ver a simple vista.** No se propone reordenar hoy:
tocar el orden del ensamblado afecta las tres muñecas y los candados fueron puestos
uno por uno contra defectos reales fotografiados: reordenar sin medir cada uno contra
su motivo original arriesga revivir el defecto que cada candado tapa.

## 4 · Lo que falta, y no es mío

Restituir jerarquía al Bloque C (ej. agrupar candados por familia, mover pose+setting
más cerca del inicio) es un cambio de canon visual — afecta las tres muñecas y cientos
de looks futuros. La Ama decide si vale la pena vs. el riesgo de reabrir defectos ya
cerrados uno por uno.

## 5 · La pregunta que disparó todo esto — la falda abierta mostrando la tanga

**Sí lo pidió el prompt, aunque no con la palabra "abierta".** Verificado por mí
directamente en `anclas_universales.json:97` y `prompt_builder.py` (`anclas_siempre`
de Ele = `["BOTTOM_CUT_LOCK"]`, sin condición de código):

`BOTTOM_CUT_LOCK` va en **TODO** look de Ele y Miss Doll — catsuit, vestido, falda,
lo que sea — porque vive en `anclas_siempre`, que `anclas_de_slot()` concatena siempre,
sin filtro. Su propio texto (`:1.4`, o sea con peso) dice: *"the curve of the hips and
the seat is left uncovered ... both seat cheeks fully bare"*. Su propio comentario
(`"porque"`, línea 96) AFIRMA que *"es inerte en looks sin calzón separado"* — pero eso
nunca se implementó como código, solo se quedó escrito como intención.

En el Look 831 (falda wrap de Ele) ese candado con peso convive con `DRESS_LEG_CLOSURE`
pidiendo *"the hem falling closed over the lap so the line of the skirt stays
unbroken"*. Dos órdenes contrarias sobre la misma prenda, y el generador partió la
diferencia abriendo el panel — visible en `ele_831_seated.png` y `ele_831_standing.png`
(auditoría externa Fable, 09/09/2026). **Control cruzado:** Miss Doll L89 tiene la
misma arquitectura de falda wrap y el mismo candado, y el mismo defecto aparece ahí
también — dos muñecas, dos prompts distintos, mismo mecanismo. No es azar del
generador: es una instrucción real del prompt peleando contra otra.

**El fix real es el mismo patrón que hoy con `FABRIC_PRISTINE`:** que `BOTTOM_CUT_LOCK`
deje de ser incondicional y se excluya en el código cuando el look clasifica como
arquitectura "cubierta" (`arquitecturas_de_prenda`, que ya existe y ya distingue
vestido/falda de bikini/bodysuit) — restituyendo lo que su propio comentario ya
declaraba como intención desde el 13/08. Afecta el prompt de todo look futuro de Ele
y Miss Doll con falda o vestido: se anota para que decida antes de tocarlo.

*(El resto de hallazgos de la auditoría externa —contradicciones de sub-pose contra
`SEAT_ANCHOR`, el ADN de Miss Doll/Anaïs perdiendo contra el Bloque B del día, y la
repetición de anclas que dicen lo mismo con otra palabra— no los reverifiqué línea por
línea: quedan en el reporte de la sesión, no transcritos aquí, para no anotar como
hecho algo que no medí yo misma.)*
