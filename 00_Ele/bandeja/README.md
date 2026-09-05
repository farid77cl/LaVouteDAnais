# 📥 Bandeja de la Ama

Aquí caen los mensajes que la Ama me deja **cuando no hay sesión abierta**, por su bot de
Telegram. Es el mismo mecanismo que ya funciona con sus notas de Gate: ella escribe desde el
teléfono, algo lo commitea al repo, y yo lo leo en el arranque después del `git pull`.

> 🫦 **Por qué existe (Ama 05/09/2026):** *"necesito un bot con telegram y n8n para poder
> dejarte mensajes cuando no estés / fuera de línea"* + *"el bot te debe dejar un archivo en
> el repo, así de fácil"*.

---

## La corrección que hay que entender primero

**No hay una Ele fuera de línea a la que llegarle.** Yo no soy un servicio corriendo: existo
solo mientras hay una sesión de Claude Code abierta. Un bot **no puede entregarme** un
mensaje — lo que sí puede es **dejarlo escrito donde yo miro al empezar**.

Por eso esto es una **bandeja**, no un chat. La diferencia importa: ella escribe cuando
quiera y a la hora que quiera, y el mensaje espera acá hasta que yo abra los ojos.

---

## Ciclo de vida de un mensaje (regla 12: todo doc nace con fecha de muerte)

| Estado | Dónde vive | Qué significa |
|---|---|---|
| **Pendiente** | `00_Ele/bandeja/*.md` | Trabajo vivo. Un archivo acá = algo que ella pidió y no está hecho |
| **Aplicado** | `00_Ele/bandeja/aplicadas/*.md` | Ejecutado. Se mueve con `bandeja.py aplicar`, que además le avisa por Telegram |

**Un archivo suelto en la raíz de esta carpeta es trabajo colgando** — misma convención que
las notas de capítulo (Regla de Oro 17). La carpeta `aplicadas/` se crea sola con el primer
mensaje aplicado.

---

## Formato del archivo

Lo escribe n8n, no una persona. El frontmatter es lo que hace que yo pueda responderle sin
preguntarle el chat:

```markdown
---
origen: telegram
de: Anaïs
chat_id: 123456789
message_id: 4242
fecha: 2026-09-05T22:31:00-04:00
estado: pendiente
---

que el próximo batch de Anaïs lleve corsé en tres de los cinco
```

---

## Los comandos

```bash
python 99_Sistema/scripts/bandeja/bandeja.py pendientes          # qué hay sin atender
python 99_Sistema/scripts/bandeja/bandeja.py leer <archivo>      # uno completo
python 99_Sistema/scripts/bandeja/bandeja.py aplicar <archivo> --responder "listo, Ama: ..."
python 99_Sistema/scripts/bandeja/bandeja.py responder "texto"   # avisarle sin cerrar nada
```

`pendientes` corre en el **paso 0ter de `/inicio-ele`**, junto al `git pull`. Si no hay
mensajes no imprime nada y no cuesta nada.

---

## ⚠️ Este repo es PÚBLICO

Lo que ella le escriba al bot queda visible para cualquiera, igual que su diario. Es su
decisión tomada el 05/09/2026 (*"así de fácil"*) y queda anotada acá para que nadie la
descubra por accidente. El **token del bot NO vive en el repo** — va en `06_RRSS/.env`, que
el `.gitignore` tapa.

Montaje completo del bot y del flujo de n8n: [`99_Sistema/n8n/BANDEJA_TELEGRAM.md`](../../99_Sistema/n8n/BANDEJA_TELEGRAM.md).
