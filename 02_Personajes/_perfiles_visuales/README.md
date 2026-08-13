# 🎭 Perfiles Visuales — Contratos del `outfit-engine`

Un **perfil visual** es todo lo que hace único a un personaje frente al motor de looks: su **BLOQUE A** (ADN físico) y sus **reglas de BLOQUE B** (cómo se viste), más poses, arquetipos, ventanas y tabúes.

La **maquinaria** (Step 0 anti-repetición, token bloqueado, ensamblado de prompts, anclas anti-defecto, contrato de archivo, linter, git, estadísticas) **no está aquí**: vive una sola vez en [`.agent/skills/outfit-engine/SKILL.md`](../../.agent/skills/outfit-engine/SKILL.md) v2.0 + `99_Sistema/scripts/visual/{anclas_universales.json, prompt_builder.py, lint_prompts_personaje.py}`.

## Perfiles vigentes

> ✏️ **Corregido 12/08/2026.** Esta tabla decía Miss Doll = 5 poses / corsé obligatorio / neopreno y Anaïs = 4 poses: los tres datos quedaron obsoletos con la estandarización a 7 poses (05/08) y los rediseños del 11/08. Es el mismo modo de falla que el resto del repo: una copia que no se actualiza cuando cambia el dueño.

| Personaje | Perfil | Poses | Slot 5 | Universo material | Particularidad |
|---|---|---|---|---|---|
| 👠 **Ele** | [`ele.md`](ele.md) | **7** | Ditzy | Vinilo/PVC/látex/gloss | Guantes **prohibidos** · cuota animal print 1/8 · outfit nunca se repite |
| 🎀 **Miss Doll** | [`miss_doll.md`](miss_doll.md) | **7** | Glacial Command | Látex/PVC/vinilo/mesh/fashion-bondage fino *(fuera neopreno e industrial, 11/08)* | Corsé **opcional** desde 11/08 · lo único inamovible es el **calzado con plataforma** · rosa firma siempre presente · Odalisque es **sentada en el suelo** (único override de ancla del roster) |
| 👑 **Anaïs Belland** | [`anais.md`](anais.md) | **7** | Sovereign Gaze | Tejido noble: satén, seda, terciopelo, látex, cuero, **pieles** | Guantes **permitidos** · lunar obligatorio · prefijo cinematográfico · su slot 5 se resuelve por el **número** de pose |

## Personaje nuevo — los 4 registros *(eran 3 hasta el 13/08/2026)*

1. Copiar [`_plantilla_perfil_visual.md`](../../.agent/skills/outfit-engine/references/_plantilla_perfil_visual.md) a `<slug>.md` en esta carpeta y rellenarlo **con la Ama**, sección por sección. El ADN de un personaje no se improvisa.
2. Registrarlo en `99_Sistema/scripts/visual/anclas_universales.json` → `personajes.<slug>` (nombre, slot 5, galería, carpeta e infijo de imagen, overrides de ancla). Con eso hereda el ensamblador, las anclas y el linter.
3. **Escribirle su repertorio de sub-poses** en `99_Sistema/scripts/visual/repertorios_pose.json` → `personajes.<slug>` — **7 variaciones por cada uno de los 7 slots**, con su registro estético propio y sus offsets. **Sin esto, sus N looks salen con la misma cláusula de cámara y las imágenes se ven iguales** (medido en Miss Doll el 13/08: 41-70% de similitud por slot; el único slot sano era el único con repertorio).
4. Registrarlo en `CharacterProfile.ALL` del repo `farid77cl/LV-App` + su offset de `PrimaryKey`. **Sin este paso la galería existe pero la app no la ve.**
5. Añadir su fila a la tabla de arriba e invocar el `outfit-engine` con el slug. **No se crea un motor nuevo.**

## Por qué existe esta carpeta

Antes había un motor por personaje. El de Ele llegó a ~1.800 líneas; al copiarlo para Anaïs quedaron **147** — viajó el ADN, no la maquinaria. Miss Doll nunca tuvo motor. Resultado: Anaïs sin Step 0 ni token bloqueado, Miss Doll sin arquetipos ni metas, y un enlace de canon roto que sobrevivió meses.

**Duplicar un motor lo condena a divergir.** Mismo problema, misma solución que en el resto del repo: **un dueño, muchos punteros.**

> ⚠️ **Regla dueño-único:** estos perfiles son los **dueños** de sus campos. Si un dato aparece también en `.agent/rules/04-estetica-ele.md`, `05-canon-miss-doll.md` o en los engines viejos, esos deben **apuntar aquí**, no copiar. Dos copias divergen; siempre lo han hecho.
