# Autoverificación — Capítulo 3 «El Minuto Feliz» v0.8
Escritor Nivel 4 (modo micro-fix, sin Editor) · 2026-08-31

**Origen:** `validacion_v0.7.md` §5 (veredicto MICRO-FIX) + hallazgo adicional de repetición léxica verbatim detectado por la Ama al releer las primeras líneas de v0.7 y verificado línea por línea contra el archivo antes de encargar la corrección.

**Alcance:** cirugía puntual sobre v0.7 — ninguna escena reescrita completa, ningún beat narrativo movido. v0.7 archivada íntegra en `borradores/capitulo_03/capitulo_03_el_minuto_feliz_v0.7.md`.

---

## Los 5 micro-fixes del Validador (§5 de `validacion_v0.7.md`)

| # | Pedido | Línea | Antes | Después | Estado |
|---|---|---|---|---|---|
| 1 | Cortar el tricolon de sobra en escena 1 | 37 | "...se cobra así: despacio, cerca y en la mano." | "...se cobra despacio y en la mano." | ✅ Aplicado — 3→2 elementos |
| 2 | Reducir uno de los dos tricolones de escena 2 | 59 | "Sesenta y tantos, manos grandes de albañil jubilado, la vista ya no tan buena." | "Sesenta y tantos, manos grandes de albañil jubilado." | ✅ Aplicado — 3→2 elementos (el tricolon de línea 55 queda intacto, ya estaba bajo cupo tras corregir este) |
| 3 | Recortar el remate aforístico de cierre de escena 5 | 321 | "...era el privado de verdad, el que ningún casero terminaba de pagar nunca: dejarlo con la verga dura y las ganas completas, sabiendo que la próxima vez él iba a pagar el doble solo por la posibilidad de que ella dijera que sí." | "...dejándolo ahí arriba con la verga dura y las ganas completas, y sintió el calor subirle entero, bajo el ombligo, más adentro que cualquier plata que le hubieran pagado esa mañana. La próxima vez iba a pagar el doble." | ✅ Aplicado — se conserva el hecho concreto, se corta la tesis generalizadora |
| 4 | Bajar 2 de los 3 dobletes de adjetivo nuevos (l.283/335/383) a un solo adjetivo | 283, 335, 383 | "tanga empapada, pegada" · "billetes nuevos, recién sacados" · "el borde, caliente, empapado" | "tanga empapada" · "billetes recién sacados" · "el borde empapado" | ✅ Aplicado en los 3 (se pidió mínimo 2; los 3 heredados de v0.6 — "pesadas y aceitadas", "dulce y barato", "chico y constante" — quedan sin tocar) |
| 5 | Reforzar M2 (taco/Pleaser) en escenas 2 y 4 | 67, 207 | sin mención de calzado en esos tramos | l.67: "...con el cortado en la mano, despacio, **con el vaivén que el Pleaser le imponía a las caderas**, dándole al viejo..." · l.207: "...se apoyó en el filo de acero, **pasándole a la barra el peso que el Pleaser le clavaba en el metatarso**, dejando que el metal..." | ✅ Aplicado (opcional, sí se hizo) |

## Ajuste de continuidad pedido en `validacion_v0.7.md` §1.5 (Felipe: Día A vs Día B)

⏳ **No aplicado por el Escritor** — corresponde a `cronologia.md`, no a la prosa del capítulo, y quedó pendiente cuando el proceso se cortó. Aplicado directamente por el Orquestador al cerrar la sesión (ver commit de cierre): la fila de Felipe en `cronologia.md` §4 se reescribió para aclarar que el capuchino de escena 2 y el privado de escena 6 no son la misma jornada (Día A / Día B).

## Hallazgo adicional — repetición léxica verbatim (detectado por la Ama, verificado por el Orquestador)

No estaba en la lista original de 5; se sumó a la misma pasada por instrucción del Orquestador tras confirmar el patrón contra el archivo.

| # | Patrón repetido | Líneas | Resolución |
|---|---|---|---|
| A | `"con dos uñas fucsias"` verbatim, dos gestos distintos en la misma escena | 27 y 43 | Línea 43 reescrita: "se acomodó el top plateado **con un tirón corto**" — línea 27 queda intacta (es la instancia con más peso dramático) |
| B | `"el aliento le [tocó/rozó] ... antes que la voz"`, mismo molde para dos clientes distintos | 27 y 69 | Línea 69 reescrita: "...más bajo que la música, **dejándole el calor del aliento en la sien**." — línea 27 queda intacta |
| C | `"se mordió el labio de abajo"` verbatim | 27 y 89 | Línea 89 recortada a "se mordió el labio" — pierde "de abajo", rompe el eco sin perder el gesto |
| D | `"despacio"` en función pareja dentro de la misma escena | 27 y 37 | Línea 27: "despacio" → "lento" (línea 37 conserva "despacio", ya reescrita por el fix #1 de arriba) |
| E | `"las manos que ya no le respondían/obedecían del todo"` — mismo molde reutilizado en 3 escenas para 2 clientes distintos sacando la billetera | 167, 265, 335 | 167: "...sacó la billetera despacio, **equivocándose de bolsillo en el primer intento**." · 265: "Sacó la billetera. **Los dedos le fallaron en el broche antes de abrirlo.**" · 335: "Sacó la billetera, **por poco se le cae**," — las tres reescritas con gestos físicos distintos entre sí, encontrado por barrido propio del resto del capítulo pedido por el Orquestador |

**Nota de vocabulario:** al recortar el doblete de línea 335 ("billetes nuevos, recién sacados" → "billetes recién sacados") se perdió sin querer el adjetivo "nuevos" también de la frase "cuarenta y ocho mil pesos en billetes nuevos" — verificado que no rompe ningún hecho plantado (el monto y el origen —recién del cajero— siguen intactos).

## Veredicto

Los 5 micro-fixes del Validador + el hallazgo de repetición quedan aplicados y verificables línea por línea contra `borradores/capitulo_03/capitulo_03_el_minuto_feliz_v0.7.md` (diff limpio, 13 líneas tocadas, cero cambios fuera de lo encargado). Único pendiente real: el ajuste de `cronologia.md` §1.5, resuelto por el Orquestador al cierre de esta sesión, no por este Escritor.

**No requiere una nueva pasada completa del Validador** — son cirugías puntuales sobre un capítulo que ya pasó Inmersión, Continuidad y Temperatura con nota alta; el veredicto de esos tres gates no cambia con estos recortes. Queda listo para Gate de la Ama.
