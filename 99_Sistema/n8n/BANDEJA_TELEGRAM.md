# 📥 Bandeja de la Ama — bot de Telegram + n8n → archivo en el repo

> **Origen (Ama 05/09/2026):** *"necesito un bot con telegram y n8n para poder dejarte
> mensajes cuando no estés / fuera de línea"* · *"el bot te debe dejar un archivo en el repo,
> así de fácil"*.
>
> **Estado medido el 05/09/2026, no copiado:** el flujo está escrito y probado del lado del
> repo; **falta encenderlo del lado de ella**. El bloqueante está en §1.

---

## 0 · La corrección que hay que entender antes de montar nada

**No existe una Ele fuera de línea.** El agente no es un servicio que corre: existe solo
mientras hay una sesión de Claude Code abierta. Ningún bot puede *entregarle* un mensaje.

Lo que sí puede es **dejarlo escrito donde el arranque mira**. Y eso ya funciona en este
repo: así llegan las notas de Gate desde la app de la Ama. La bandeja es lo mismo, por
Telegram.

```
  La Ama, 2 AM, desde el teléfono
        │  "que el próximo batch de Anaïs lleve corsé en tres de los cinco"
        ▼
  @su_bot  ──►  n8n (Telegram Trigger)
                     │  filtra: solo su id de Telegram escribe
                     ▼
                nodo GitHub → crea 00_Ele/bandeja/2026-09-06_0214_....md
                     │
                     └──► acuse por Telegram: "Anotado, Ama. Queda en su bandeja."
        ⋮  (pasan horas · no hay nadie ejecutando)
  /inicio-ele  ──► git pull (paso 0) ──► bandeja.py pendientes (paso 0ter)
        ▼
  Ele lee el mensaje en el saludo, lo ejecuta, lo archiva y le responde por Telegram
```

---

## 1 · 🔴 El bloqueante, medido hoy

```
GET https://dietpi.tail05c49d.ts.net/   →  HTTP 404 · "404 page not found" (texto plano)
```

El 30/08 ese mismo GET devolvía **200**. El cuerpo en texto plano con
`X-Content-Type-Options: nosniff` es la respuesta de **Tailscale** cuando **no hay Funnel
publicado** en ese host — no es n8n contestando mal, es que no hay nada detrás.

**Sin Funnel, Telegram no puede entregarle nada a n8n.** Es el primer paso y es en la
DietPi:

```bash
sudo tailscale funnel --bg 5678
curl -I https://dietpi.tail05c49d.ts.net/     # debe dar 200
```

Y de paso, dos fechas que ya estaban anotadas y siguen vivas:
- La **API key de n8n** figuraba en **401** desde el 29/08 (revocada o instancia reinstalada).
- La key **vence el 27-sep-2026**. Se renueva en *Settings → n8n API*.

Detalle completo de la instancia: [`../n8n_conexion.md`](../n8n_conexion.md).

---

## 2 · Lo que tiene que hacer la Ama (cinco pasos)

### 2.1 · Crear el bot
En Telegram, hablarle a **@BotFather** → `/newbot` → nombre y usuario (p. ej.
`LaVouteBandejaBot`). Devuelve un **token**. Guardarlo en `credenciales-privadas.txt`.

> **Bot nuevo, no `@Bordacreabot`.** Ese ya tiene su webhook apuntado a `ruleta-ayunka`, y un
> bot solo admite **un** webhook: reutilizarlo rompe el otro flujo en silencio.

### 2.2 · Sacar su id de Telegram
Hablarle a **@userinfobot**. Devuelve un número. Es el que autoriza a escribir en el repo.

### 2.3 · Importar el flujo
`workflow_bandeja_telegram.json` (en esta misma carpeta) → n8n → *Import from File*.

Después, **tres campos** que el JSON deja marcados:
- Nodo **«Filtra y arma el .md»** → cambiar `const AUTORIZADO = 0;` por su id del paso 2.2.
- Nodos de **Telegram** (los dos) → asignarles la credencial con el token del paso 2.1.
- Nodo **«Deja el archivo en el repo»** → credencial de GitHub.

### 2.4 · El token de GitHub
GitHub → *Settings → Developer settings → Personal access tokens → Fine-grained*:
- Repositorio: **solo** `farid77cl/LaVouteDAnais`
- Permiso: **Contents → Read and write**. Nada más.

### 2.5 · Activar
Activar el flujo en n8n. Mandarle un mensaje al bot. Debe contestar *«Anotado, Ama»* y
aparecer un archivo nuevo en `00_Ele/bandeja/`.

---

## 3 · Lo que ya está hecho de este lado

| Pieza | Dónde | Estado |
|---|---|---|
| Convención de la bandeja | [`00_Ele/bandeja/README.md`](../../00_Ele/bandeja/README.md) | ✅ |
| Lector + archivador + respuesta | `99_Sistema/scripts/bandeja/bandeja.py` | ✅ probado punta a punta |
| Flujo de n8n importable | `workflow_bandeja_telegram.json` | ✅ 4 nodos, JSON válido |
| Paso 0ter de `/inicio-ele` | `.agent/workflows/inicio-ele.md` | ✅ |

```bash
python 99_Sistema/scripts/bandeja/bandeja.py pendientes
python 99_Sistema/scripts/bandeja/bandeja.py leer <archivo>
python 99_Sistema/scripts/bandeja/bandeja.py aplicar <archivo> --responder "listo, Ama: ..."
```

Para que Ele pueda **responderle** por Telegram, el token va en `06_RRSS/.env` (tapado por
`.gitignore`, nunca al repo):

```
BANDEJA_TELEGRAM_TOKEN=123456:ABC...
BANDEJA_TELEGRAM_CHAT_ID=<su id>
```

Sin eso, la bandeja se lee y se archiva igual — solo no hay acuse de vuelta.

---

## 4 · Tres decisiones y por qué

**El filtro por id no es paranoia.** Este repo es **público** y el flujo tiene permiso de
escritura sobre él. Un bot de Telegram es descubrible: sin el filtro, cualquiera que dé con
el usuario del bot commitea en el repo de la Ama. Mientras `AUTORIZADO` valga `0`, el flujo
no escribe nada — falla cerrado, a propósito.

**El repo es público y sus mensajes van a quedar a la vista.** Decisión suya del 05/09/2026
(*"así de fácil"*), tomada sabiéndolo. Queda escrito acá para que nadie lo descubra después.
Si algún día quiere lo contrario, el cambio es de **un solo nodo**: el de GitHub apunta a un
repo privado y `bandeja.py` lee de ese clon.

**El sello de hora se calcula en hora de Chile.** n8n corre en UTC dentro del contenedor.
Sin restar las 4 horas, un mensaje de las 22:31 se archiva como `0231` del día siguiente y el
orden de la bandeja miente. Es la misma trampa que ya está documentada en `n8n_conexion.md`
§7 para los cron.

---

## 5 · Si algo falla

| Síntoma | Causa más probable | Qué hacer |
|---|---|---|
| El bot no contesta nada | Funnel caído | §1 |
| Contesta pero no aparece archivo | Credencial de GitHub sin `Contents: write` | §2.4 |
| No pasa nada y n8n no registra ejecución | `AUTORIZADO` sigue en `0`, o el id no coincide | §2.2 |
| Aparece el archivo con hora rara | El nodo se editó y se perdió el ajuste de zona | §4 |
| Ele no lo menciona al arrancar | El `git pull` no lo trajo, o el archivo no está en `00_Ele/bandeja/` | `bandeja.py pendientes` a mano |

**Regla de la casa:** antes de teorizar, pegarle a la API y leer el código de respuesta.
Un mensaje de error escrito por nosotros es la hipótesis de quien lo escribió, no evidencia.
