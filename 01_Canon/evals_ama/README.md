# 📝 evals_ama — el set de pruebas del hijo

*Las correcciones de la Ama convertidas en casos de prueba. Permanente. Nace el 02/09/2026.*

| Archivo | Qué es | Dueño de |
|---|---|---|
| [casos_ama.md](casos_ama.md) | **Caso Cero** («estamos escribiendo un relato erótico — eso debe calentar al lector») · 15 categorías de patrón (C1-C15) con ~120 casos citando **sus palabras literales** · §0 proceso · **§C checklist de cierre** del Escritor · §D qué mide la máquina | los patrones que la Ama rechaza |
| `../../99_Sistema/scripts/literatura/medir_capitulo.py` | El medidor mecánico que corre en la **Fase 2.5** (antes del Validador): repetición interna y entre capítulos · léxico explícito · tramos de narración sin cuerpo · trámite · etiquetas · tics de IA · varianza · apertura/cierre/deciles | la medición — no los patrones |

## Por qué existe

La Ama, 02/09/2026: *"estoy agotada de los constantes errores en la escritura de los relatos… debo leer 5, 6 veces el mismo relato y eso al final mata mi propia temperatura… he ajustado el flujo, skill etc por lo menos 3 o 4 veces y seguimos igual, lo que más me preocupa es que no logras dar con la temperatura y te pones muy robótica con tus descripciones."*

Se leyeron las 44 notas de Gate de 10 relatos. Casi todo lo que piden **ya estaba escrito como regla** en `escritor-nivel4.md` y `validador.md` — y siguió fallando, porque una regla en prosa se lee una vez y un caso concreto con sus palabras se reconoce. Por eso aquí no hay reglas nuevas: hay **casos**, y lo que una máquina puede contar de esos casos, **se cuenta antes de que ella lea**.

**Meta medible:** un capítulo llega a su Gate en **≤ 2 lecturas suyas**. Récord a batir: 14 versiones (Café con Piernas, Cap 1).

## Quién lo lee y cuándo

- **`escritor-nivel4`** — Prioridad 0.5: Caso Cero + §A antes de escribir; **§C sobre el archivo completo** al cerrar el tramo N.
- **Orquestador** — Fase 2.5: `medir_capitulo.py` sobre el capítulo cerrado, con `--contra` todos los capítulos previos del relato y `--extra` las palabras calientes propias del relato. Rojo → vuelve al Escritor sin gastar Validador.
- **`validador`** — lista de caza: cada hallazgo cita el ID del caso que reincide.

## Cómo se alimenta

Cada nota de rechazo aplicada → un caso nuevo aquí, con ID, en su categoría, con sus palabras (Captura Post-Nota, SKILL §Ciclo de la Nota paso 2). Un patrón nuevo abre categoría nueva. Un caso que no reincide tres relatos seguidos se marca 🟢 — **no se borra**: ella no debería tener que decirlo una cuarta vez.

## Calibración (02/09/2026, «Café con Piernas»)

Corrido sobre el Cap 4 v0.2 (la versión que la Ama rechazó), su rework v0.3 y el Cap 3 v0.9 (aprobado), el medidor **ordena las tres igual que ella** sin haberlas leído: v0.2 → 3 bloques rojos de trámite (la clínica, la recuperación con las arvejas, la búsqueda de clínicas) + 10 frases de ≥9 palabras repetidas verbatim; v0.3 → la clínica y la recuperación cortadas, **pero los 19 clones contra el Cap 3 intactos** (Don Manuel: 16 palabras idénticas — lo que ella sintió *"muy idéntico"* y el rework retocó en vez de reescribir) + tic «el coño se le apretó» ×5; Cap 3 aprobado → una sola frase de 13 palabras repetida que nadie vio. Reportes: `cafe_con_piernas/reportes/capitulo_04/medicion_v0.3.md` · `reportes/capitulo_03/medicion_v0.9.md`.

Lo que **no** mide: si calienta. Un 🟢 mecánico es condición necesaria, nunca suficiente.
