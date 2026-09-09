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
