# 💄 Canon de Maquillaje — DOCUMENTO DEROGADO, ES UN PUNTERO (04/09/2026)

> ➡️ **Sucesor:** `02_Personajes/_perfiles_visuales/ele.md`, `miss_doll.md` y `anais.md` — sus **§2** (maquillaje fijo), **§3** (vetos) y **§5.2c** (colorimetría del maquillaje). Ahí vive ahora todo lo que este archivo intentaba definir.

> ⛔ **Este archivo ya no define nada.** Estaba fechado el **29/04/2026**, nunca se actualizó, y
> al medirlo el 04/09/2026 resultó que **mandaba lo contrario de lo vigente en tres de los cuatro
> puntos que tocaba** — que es exactamente el modo de falla que la regla de dueño único existe para
> matar (este repo ya pagó lo mismo con tres flotas distintas en tres archivos).

## Qué decía que ya era falso

| Decía | Realidad vigente |
|---|---|
| «LABIOS ROJOS (NO pink)» para Miss Doll | **Derogado el 02/08/2026**: su maquillaje se elige por la
ocasión del look (`miss_doll.md` §2 y §5.5.8). El documento mandaba lo contrario |
| «❌ Pink eyeshadow» para Miss Doll | Contradicho por la práctica real: **28 de 74 looks (37%)**
llevan sombra rosa/magenta |
| Token de Miss Doll con `blonde brows` | Su ceja vigente es explícitamente **más oscura que el pelo**
(`dark smoky taupe-grey`, peso 1.5) — no coincide en ningún punto |
| Para Anaïs, `warm-toned smokey eyes` | Su ADN vigente pide `charcoal + deep taupe cut-crease` |
| Definía a **HELENA** | Era cerrada (Looks 001-084). Vive en `memoria_historica/` |

## Dueño único del maquillaje, por muñeca

| Qué | Dónde |
|---|---|
| Maquillaje **fijo** de cada muñeca | `02_Personajes/_perfiles_visuales/<slug>.md` **§2**, dentro del
fence `<!-- ADN:BLOQUE_A -->` |
| Qué le **prohíbe** el generador | el **§3** de ese mismo perfil |
| **Colorimetría** del maquillaje: qué le favorece, qué le pelea y por qué | el **§5.2c** de ese perfil
*(hermana de la §5.2b, que gobierna el color de la prenda)* |
| Maquillaje **variable por look** | el BLOQUE B del look, declarado con `adn_overrides` |

Verificable con `python 99_Sistema/scripts/visual/outfit.py adn`.

*Sucesor declarado: las §2 / §3 / §5.2c de los tres perfiles visuales. Su contenido histórico vive en el git log de este archivo.*
