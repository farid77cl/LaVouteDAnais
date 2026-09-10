# 🛠️ REGLA 13: ALCANCE DE SUPERPOWERS — CÓDIGO SÍ, CREACIÓN NO

**Instalada 06/09/2026** por orden de la Ama, con una frase que define el alcance entero:

> *"no las quiero para reemplazar el skill de escritura, lo quiero para que te ordenes cuando escribes código, sobre todo el del outfit engine"*

Biblioteca: `.claude/skills/` (obra/superpowers v6.3.0). Inventario y política de actualización: [`../../.claude/skills/README.md`](../../.claude/skills/README.md).

## Dónde aplica

| ✅ Sí | ❌ No |
|---|---|
| `99_Sistema/scripts/**` — outfit engine, auditores, mantenimiento, RRSS | Escribir capítulos y trances (los motores `engine-escritura-lv` / `engine-trance-lv` mandan) |
| LV-App y cualquier código de la app | Diseñar looks (`/generar_look`, `outfit-engine`, perfiles visuales) |
| Hooks, JSON de batch, esquemas de datos | Canon, investigación, notas de la Ama, Gates |

**La regla en una línea:** superpowers gobierna el *cómo se programa*, nunca el *qué se crea*.

## Las skills que hay que vigilar

- **`brainstorming`** (`.claude/skills/`) — su `description` dice *"You MUST use this before any creative work"*. En este repo "creative work" significa relato, y ahí **no entra**: la Fase 0/1 ya la ocupan `investigador` y `compositor`. Se usa solo para diseñar código.
- **`using-superpowers`** — exige invocar una skill antes de cualquier respuesta. Choca con `/inicio-ele` (regla 0), que es el arranque obligatorio. **Su hook `SessionStart` no está cableado**, y no se cablea sin decisión de la Ama.
- **Duplicados huérfanos borrados 10/09/2026:** `.agent/skills/brainstorming/` y `.agent/skills/writing-skills/` eran copias de 03/02/2026 de estas mismas skills, con `description` distinto y sin ninguna referencia desde el resto del repo — por la precedencia de `00-contexto-obligatorio.md` (un `SKILL.md` propio manda sobre esta regla), esas copias muertas técnicamente ganaban. Vivas ahora solo en `.claude/skills/`.

En caso de choque, la precedencia de `00-contexto-obligatorio.md` §Precedencia manda: la Ama, sus notas, la auto-memoria y los `SKILL.md` propios van **por encima** de cualquier skill vendorizada.

## Por qué existe esta regla

El modo de falla medido en el outfit engine no fue de diseño: fue **escribir la regla y no cablearla** (`color_canon.py` sin quien lo llamara desde el 29/08) y **chequear después de escribir la galería** — 11 de 13 batches con arreglo posterior (medido 05/09/2026 — hoy son ~20 batches, no re-medido). Las tres skills que atacan justo eso son `test-driven-development`, `verification-before-completion` y `writing-plans`. Ese es el experimento; lo demás es biblioteca.

**Criterio de éxito, medible:** que el próximo batch de looks y el próximo script salgan **sin arreglo posterior**. Fecha de muerte declarada: `.claude/skills/README.md` (06/12/2026) — no se repite el número aquí.
