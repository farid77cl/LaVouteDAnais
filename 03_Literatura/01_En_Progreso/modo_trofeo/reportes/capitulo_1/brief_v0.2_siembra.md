# Brief del Escritor — «Modo Trofeo» Cap 1 · v0.1 → v0.2 (siembra de Fase 1.5)

> **Documento de TRABAJO.** Muere cuando la v0.2 quede escrita. Input único del Escritor (regla de presupuesto, `SKILL.md` §Presupuesto de tokens): **no leas ningún otro archivo del repo** salvo `01_Canon/voz_autoral.md` si lo necesitas para la cadencia.

## Qué es esta tarea

**NO es una reescritura ni un rework.** El capítulo está bien y no se toca. La Ama amplió el canon el 07/09/2026 (Fase 1.5) y hay que **sembrar dos cosas nuevas**, en total unas **60-80 palabras** repartidas en tres inserciones. Todo lo demás queda **byte a byte idéntico**.

**Archivo a editar:** `03_Literatura/01_En_Progreso/modo_trofeo/capitulo_1_cuatro_v0.2.md` (ya existe, es copia exacta de la v0.1).
**Solo `Edit`. Nunca `Write` sobre ese archivo.** No reemites prosa existente.

---

## Siembra 1 — NEXUM, dicho una vez

**Dónde:** el párrafo del encargo, cerca de la línea 11 — el que empieza *«El encargo llegó como llegan los buenos: sin cara, sin nombre, con la mitad por adelantado.»*

**Qué entra:** el nombre **NEXUM** aplicado **a la unidad**, no a la empresa. El hacker lo registra como registra un modelo de auto: dato técnico del encargo, y sigue de largo. Media línea, dentro de una frase que ya existe.

**Reglas duras:**
- ⛔ Él **no sabe** de quién es la casa (eso lo descubre después).
- ⛔ **Ni una palabra sobre legalidad, permiso, prohibición o riesgo.** La ilegalidad del mundo se siente porque **nadie la menciona nunca**. Si el hacker piensa «esto es ilegal», el relato se vuelve un thriller y se rompe el foco.
- ⛔ Nada de explicar qué es NEXUM.

**Prueba de que quedó bien:** si borras la palabra NEXUM, el párrafo funciona igual. Es textura, no información.

---

## Siembra 2 y 3 — El Manual, como epígrafe seco (exactamente DOS, ni uno más)

Dispositivo nuevo del canon (§0 W5): la casa tiene un manual y **el texto lo cita, nunca lo explica**. Resuelve de raíz la prohibición de explicar los modos.

**Formato exacto — cursiva, línea sola, atribución con número de página, sin comentario antes ni después:**

> *Una unidad en REPOSO no requiere supervisión.* —Manual de Operación NEXUM, pág. 112

**Dónde van los dos:**

1. **Antes del bloque de exhibición** (donde el dueño dicta `—Bambi. TROFEO.`, alrededor de la línea 53). El epígrafe habla de la unidad exhibida.
2. **Antes del bloque del préstamo / uso en serie** (donde el dueño habla *de* ella y no *con* ella, delante del hacker). El epígrafe habla de la unidad prestada o del uso.

**Reglas duras:**
- Los dos epígrafes son **frases de manual**: impersonales, secas, en presente, sobre «la unidad». Nunca sobre Bambi por su nombre, nunca sobre el dueño, nunca sobre sexo.
- El narrador **no los comenta jamás**. No hay «leí eso una vez» ni ironía. Entran y sigue la escena.
- Números de página distintos y no redondos.
- **Máximo dos en todo el capítulo.** Tres deja de ser textura y se vuelve recurso.

---

## Lo que NO se toca (verificable con `diff`)

Los tres tramos · las marcas [1]-[8] · el inventario que baja de cuatro a tres · las anclas ya dictadas (`TROFEO` l.53 · `REPOSO` l.143 y 207 · `CELO` l.199, 215 y 279) · el cierre (confrontación + fuga sin resolver) · el título · el largo. **Ni una frase existente se reescribe, se acorta ni se «mejora».**

---

## Voz y firma (obligatorio en las 60-80 palabras nuevas)

El capítulo va en **primera persona presente**, seco, sin adorno. Las inserciones tienen que ser indistinguibles de lo que ya está.

**Caso C17 de la Ama (07/09/2026): «se está notando demasiado que es escrito por IA».** En lo que escribas, prohibido:
- **dos puntos revelatorios** (enunciado neutro `:` revelación);
- **«como si» / «como quien»**;
- **el recibo de excitación** — cerrar una frase certificando lo que el cuerpo sintió;
- cláusulas todas del mismo largo: si escribes tres, que una sea de dos palabras o de dieciocho.

---

## Al cerrar

1. Corre `diff` mental contra la v0.1: **solo tres inserciones, cero líneas modificadas**.
2. Escribe `reportes/capitulo_1/autoverificacion_v0.2.md` con: las tres inserciones citadas literales con su línea, el conteo de palabras nuevas, y la confirmación de que no tocaste nada más.
3. **No actualices `cronologia.md`** — lo hace el Orquestador en este caso (la siembra no cambia eventos, solo paga H16).

## RETURN

`ESCRITOR_N4_RESULT:{"archivo":"...v0.2.md","inserciones":3,"palabras_nuevas":N,"lineas_modificadas":0,"autoverificacion":"..."}`
