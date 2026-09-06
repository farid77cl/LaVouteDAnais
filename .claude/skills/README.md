# `.claude/skills/` — biblioteca **superpowers** (vendorizada)

**Origen:** [obra/superpowers](https://github.com/obra/superpowers) · **v6.3.0** · commit `b36e082` (12/08/2026) · MIT
**Instalada:** 06/09/2026, por orden de la Ama.
**Fecha de muerte declarada (regla 12):** si al 06/12/2026 no cambió cómo se escribe el código de este repo, se borra la carpeta entera con un `git rm -r` y se cierra el experimento en el diario. No se deja "por si acaso".

## Por qué está copiada a mano y no instalada como plugin

El camino oficial es `/plugin marketplace add obra/superpowers-marketplace` + `/plugin install`. **En esta máquina no se puede:** no hay binario `claude` en el PATH y `~/.claude/plugins/` no existe — los comandos `/plugin` los teclea la Ama, no el agente. Así que las 14 skills se copiaron verbatim a `.claude/skills/`, que es donde Claude Code descubre skills de proyecto. Se descubren igual; lo que se pierde es el hook.

## Lo que NO se instaló, a propósito

El plugin trae un hook `SessionStart` que inyecta la skill `using-superpowers` como bloque `<EXTREMELY_IMPORTANT>` exigiendo invocar una skill **antes de cualquier respuesta**. Eso choca de frente con `/inicio-ele`, que es el arranque obligatorio de este repo (regla 0). **No se cableó.** Si algún día se quiere, se decide con la Ama y se documenta acá.

## Actualizar

```bash
git clone --depth 1 https://github.com/obra/superpowers.git /tmp/sp
cp -r /tmp/sp/skills/. .claude/skills/     # y se revisa el diff antes de commitear
```
Al actualizar, **revisar los `description:`**: son los que disparan la auto-activación y los que pueden invadir el terreno literario (ver `.agent/rules/13-superpowers-scope.md`).
