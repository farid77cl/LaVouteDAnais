---
description: Generar look de Anaïs Belland — outfit-engine genérico + su perfil visual, 7 poses, registro y commit
---

Ejecuta el **`outfit-engine`** (`.agent/skills/outfit-engine/SKILL.md`) con el slug `anais`.

Todo lo que diferencia a Anaïs — su ADN (§2, fence `<!-- ADN:BLOQUE_A -->`), sus reglas de vestuario (§5), sus 7 poses, sus arquetipos y sus prohibiciones — vive en su **perfil visual**: `02_Personajes/_perfiles_visuales/anais.md`. El motor es el mismo de las tres muñecas.

> 🔧 **Corregido 29/08/2026.** Este stub decía *"lee y ejecuta `.agent/skills/anais-outfit-engine/SKILL.md`"* — el **motor legacy por personaje**, que el `outfit-engine` genérico reemplazó el 27/07. Seguir mandando ahí es reabrir la falla que ese cambio vino a cerrar: los motores por personaje derivan (el de Ele llegó a ~1.800 líneas, copiarlo para Anaïs produjo 147 — viajó el ADN, no la maquinaria) y un fix hecho en uno no llega a las otras. `anais-outfit-engine` queda como **material de personaje**, no como motor.

**Flujo (v3.0 — el look es DATOS, no un script):**

1. **Paso 0 Anti-Repetición** y diseño del outfit según el perfil (§5) y sus metas de arquetipo (§6).
2. **Declarar el batch** en `99_Sistema/scripts/visual/batches/<nombre>.json` — `personaje: "anais"`, y por look: `titulo`, `bloque_b`, `setting`, `props`.
3. **Emitir:** `python 99_Sistema/scripts/visual/outfit.py generar batches/<nombre>.json`
4. **Verificar:** `outfit.py lint anais` (CRÍTICOS 0) · `outfit.py adn` (LIMPIO)
5. **Registrar** la salida en `02_Personajes/01_Principales/anais/galeria_looks_anais.md` y cerrar con commit por rutas explícitas.

> ⏳ **Anaïs todavía no está migrada a batch-como-datos.** Su formato de emisión difiere en cuatro puntos del que produce `outfit.py generar` (encabezado 👑, línea `**Arquetipo:** · **Paleta:**`, `**1. Standing:**` en vez de `### 1.`, y su BLOQUE B **inline entre backticks** — la forma exacta que ya rompió el parser de LV-App una vez). Hasta que la Ama decida unificarlo, sus looks se ensamblan con `PromptBuilder("anais")` respetando el formato de su galería viva. **Lo que NO cambia:** el ADN se lee del perfil (nunca se copia) y todo prompt pasa por el linter antes de entregarse.
