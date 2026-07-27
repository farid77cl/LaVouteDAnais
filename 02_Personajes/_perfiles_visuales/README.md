# 🎭 Perfiles Visuales — Contratos del `outfit-engine`

Un **perfil visual** es todo lo que hace único a un personaje frente al motor de looks: su **BLOQUE A** (ADN físico) y sus **reglas de BLOQUE B** (cómo se viste), más poses, arquetipos, ventanas y tabúes.

La **maquinaria** (Step 0 anti-repetición, token bloqueado, prompts-antes-de-generar, banderas rojas, git, estadísticas) **no está aquí**: vive una sola vez en [`.agent/skills/outfit-engine/SKILL.md`](../../.agent/skills/outfit-engine/SKILL.md).

## Perfiles vigentes

| Personaje | Perfil | Poses | Universo material | Particularidad |
|---|---|---|---|---|
| 👠 **Ele** | [`ele.md`](ele.md) | **7** | Vinilo/PVC/látex/gloss | Guantes **prohibidos** · cuota animal print 1/8 · outfit nunca se repite |
| 🎀 **Miss Doll** | [`miss_doll.md`](miss_doll.md) | **5** | Látex/PVC/neopreno/webbing | Corsé en **todos** los looks · rosa firma siempre presente |
| 👑 **Anaïs Belland** | [`anais.md`](anais.md) | **4** | Tejido noble: satén, seda, terciopelo, látex clínico | Guantes **permitidos** · lunar obligatorio · prefijo cinematográfico |

## Personaje nuevo

1. Copiar [`_plantilla_perfil_visual.md`](../../.agent/skills/outfit-engine/references/_plantilla_perfil_visual.md) a `<slug>.md` en esta carpeta.
2. Rellenar **con la Ama**, sección por sección. El ADN de un personaje no se improvisa.
3. Añadir su fila a la tabla de arriba.
4. Invocar el `outfit-engine` con el slug. **No se crea un motor nuevo.**

## Por qué existe esta carpeta

Antes había un motor por personaje. El de Ele llegó a ~1.800 líneas; al copiarlo para Anaïs quedaron **147** — viajó el ADN, no la maquinaria. Miss Doll nunca tuvo motor. Resultado: Anaïs sin Step 0 ni token bloqueado, Miss Doll sin arquetipos ni metas, y un enlace de canon roto que sobrevivió meses.

**Duplicar un motor lo condena a divergir.** Mismo problema, misma solución que en el resto del repo: **un dueño, muchos punteros.**

> ⚠️ **Regla dueño-único:** estos perfiles son los **dueños** de sus campos. Si un dato aparece también en `.agent/rules/04-estetica-ele.md`, `05-canon-miss-doll.md` o en los engines viejos, esos deben **apuntar aquí**, no copiar. Dos copias divergen; siempre lo han hecho.
