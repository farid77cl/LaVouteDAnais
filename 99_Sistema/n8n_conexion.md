# La conexión con n8n — documento completo

> Estado comprobado el **30-ago-2026** contra la instancia viva, no copiado de la
> documentación. Cada afirmación de estado abajo dice con qué prueba se sacó.
>
> **Origen:** copiado desde `negocio-accesorios-3d-costura/n8n/CONEXION.md` (repo distinto,
> proyecto de accesorios 3D/costura de la Ama) el 30/08/2026, a pedido suyo, para tenerlo
> disponible en este repo de cara al ítem pendiente **"datos de n8n aparcados"** de
> `memoria_sesiones.md` (decisión del 28/08 para LV-App 5.0: "n8n con los 4 usos"). La
> instancia de n8n (`dietpi.tail05c49d.ts.net`) es infraestructura compartida entre proyectos
> de la Ama, no exclusiva de La Voûte. Este archivo es una copia de referencia — el dueño
> real del contenido sigue siendo el repo de origen; si diverge, ese es el que manda.

---

## 1 · Qué hay que entender primero

n8n **no está en la nube de nadie**. Es un contenedor Docker corriendo en una máquina DietPi
en la casa de Farid, en `192.168.1.200:5678`. Todo lo que sigue existe para resolver un solo
problema: cómo llega algo de afuera hasta esa máquina.

```
                                    ┌─────────────────────────────────┐
   Claude (servidores de Anthropic) │                                 │
   Telegram (servidores de Telegram)│  INTERNET                       │
   Navegador fuera de casa          │                                 │
                                    └───────────────┬─────────────────┘
                                                    │ HTTPS 443
                                          ┌─────────▼──────────┐
                                          │ Tailscale Funnel   │
                                          │ dietpi.tail05c49d  │
                                          │      .ts.net       │
                                          └─────────┬──────────┘
                                                    │
   ┌────────────────────────────────────────────────▼─────────────────┐
   │  RED DE CASA — 192.168.1.x                                       │
   │                                                                  │
   │   ┌──────────────────────────────────────────────────────────┐   │
   │   │  DietPi 192.168.1.200   ·   Docker   ·   n8n :5678        │   │
   │   │                                                          │   │
   │   │   /            → interfaz web (login)                     │   │
   │   │   /api/v1/...  → API de administración  (X-N8N-API-KEY)   │   │
   │   │   /webhook/... → webhooks de producción (los flujos)      │   │
   │   │   /mcp-server/http → MCP Server Trigger (Bearer)          │   │
   │   │                                                          │   │
   │   │   volumen n8n_data → workflows, credenciales, SQLite      │   │
   │   └──────────────────────────────────────────────────────────┘   │
   └──────────────────────────────────────────────────────────────────┘
```

**La consecuencia práctica:** si el Funnel se cae, n8n sigue publicando en Instagram y
Facebook exactamente igual (esos flujos salen *hacia* internet), pero **deja de recibir**:
el bot de Telegram queda mudo y Claude no puede tocar nada.

---

## 2 · Las cuatro puertas de entrada

No hay "una" conexión con n8n. Hay cuatro, con credenciales distintas y usos distintos.
Confundirlas es la causa habitual de los diagnósticos largos.

| # | Puerta | URL | Credencial | Para qué sirve |
|---|---|---|---|---|
| 1 | **Interfaz web** | `https://dietpi.tail05c49d.ts.net/` | usuario + contraseña de n8n | Mirar y editar a mano |
| 2 | **API de administración** | `.../api/v1/…` | `X-N8N-API-KEY` | **Crear, activar, desactivar flujos y leer ejecuciones.** Es la que se usa de verdad |
| 3 | **MCP Server Trigger** | `.../mcp-server/http` | `Authorization: Bearer …` | Las herramientas colgadas de *un* workflow. **No** administra n8n |
| 4 | **Webhooks de producción** | `.../webhook/<ruta>` | la ruta secreta | Telegram, cotizar envío, historial de la impresora |

### La distinción que más cuesta

- La **puerta 2** (API key) es la que permite «importa este flujo y actívalo». Es la que
  usa el conector **oficial de n8n** del directorio de conectores de Claude, y la que usan
  `crear-flujos-crecimiento.py` y `rotar-token.py`.
- La **puerta 3** (`/mcp-server/http`) es un *conector personalizado* y solo expone lo que
  se le haya enganchado al workflow `workflow-mcp-servidor.json`. **Que aparezca vacío no es
  una falla**: es que el nodo no tiene herramientas conectadas.

Si lo que se quiere es que Claude opere n8n, la puerta es la **2**. La 3 es un extra.

---

## 3 · Estado comprobado hoy (30-ago-2026)

Pruebas hechas desde fuera de la red de casa, contra la URL pública:

| Prueba | Respuesta | Qué significa |
|---|---|---|
| `GET /` | **200** | El Funnel está arriba y n8n contesta |
| `GET /api/v1/workflows` sin key | **401** `'X-N8N-API-KEY' header required` | La API existe y está protegida. **Viva** |
| `POST /mcp-server/http` sin token | **401** `Authorization header not sent` | Hay autenticación respondiendo en esa ruta |
| `POST /webhook/mcp-server/http` | **404** `webhook no registrado` | Esa ruta **no** es la correcta |
| `POST /mcp-server` | **404** `Cannot POST` | Falta el `/http` final |

**Conclusión: la máquina, el Funnel y la API están sanos.** El problema, si lo hay, está en
cómo está configurado el conector, no en n8n.

### El conector que está fallando ahora

En esta sesión aparece un servidor MCP llamado **N8n** que no conecta:

```
N8n (404): "Error POSTing to endpoint: No MCP endpoint was found at the URL provided"
```

Ese 404 lo devuelve el servidor al que Claude le está pegando. Como `/mcp-server/http`
responde 401 y no 404, **la URL configurada en el conector no es esa**. Las tres causas
posibles, en orden de probabilidad:

1. **La URL del conector está mal escrita** — le falta el `/http` final, sobra un `/webhook/`,
   o quedó con una barra al final. Es lo más probable.
2. **El workflow `workflow-mcp-servidor.json` está desactivado.** n8n devuelve 404 en la ruta
   de producción de un trigger cuyo flujo no está activo — el mismo mensaje que salió arriba
   en `/webhook/mcp-server/http`.
3. **Se configuró el conector personalizado creyendo que era el oficial.** Aunque conecte,
   ese no trae `publish_workflow` ni `search_workflows`, así que tampoco resolvería nada.

### Cómo arreglarlo, en orden

1. Abrir n8n y comprobar que el flujo del **MCP Server Trigger** está **activo**. Copiar de
   ahí la **URL de producción** que muestra el nodo, tal cual, sin retocarla.
2. En Claude → Configuración → Conectores, borrar el conector `N8n` actual y volver a
   agregarlo con esa URL exacta y el encabezado `Authorization: Bearer <token>`.
3. **Y aparte** — esto es lo que de verdad importa — agregar el **conector oficial de n8n**
   del directorio, con instancia `https://dietpi.tail05c49d.ts.net` y la API key.
4. Cerrar Claude por completo, abrirlo y empezar una conversación nueva. Los conectores no
   se recargan en caliente.

---

## 4 · Cómo se conecta cada cosa, paso a paso

### 4.1 · El conector oficial de n8n (el importante)

1. n8n → **Settings → n8n API → Create an API key**
2. Claude → **Configuración → Conectores** → buscar **n8n** en el directorio
3. Instancia: `https://dietpi.tail05c49d.ts.net`
4. Pegar la API key
5. Reiniciar Claude y abrir conversación nueva

Trae `publish_workflow`, `unpublish_workflow`, `search_workflows`, `search_executions` y
`get_execution`. Con eso se acaba el "reimporta y activa a mano".

### 4.2 · El conector personalizado (`/mcp-server/http`)

| Campo | Valor |
|---|---|
| URL | la URL de producción que muestra el nodo MCP Server Trigger |
| Encabezado | `Authorization: Bearer <token del nodo>` |

El token del MCP Server Trigger **no vence**. Quien lo tenga entra hasta que se revoque.

### 4.3 · Por API, sin conectores (siempre funciona)

Es la vía que no depende de que ningún conector esté bien configurado:

```bash
export N8N_KEY="…"        # está en credenciales-privadas.txt
BASE=https://dietpi.tail05c49d.ts.net/api/v1

# listar
curl -s -H "X-N8N-API-KEY: $N8N_KEY" "$BASE/workflows?limit=100"

# crear
curl -s -X POST -H "X-N8N-API-KEY: $N8N_KEY" -H 'Content-Type: application/json' \
     -d @flujo.json "$BASE/workflows"

# activar / desactivar
curl -s -X POST -H "X-N8N-API-KEY: $N8N_KEY" "$BASE/workflows/<id>/activate"
curl -s -X POST -H "X-N8N-API-KEY: $N8N_KEY" "$BASE/workflows/<id>/deactivate"

# ver una ejecución nodo por nodo — la mejor forma de diagnosticar
curl -s -H "X-N8N-API-KEY: $N8N_KEY" "$BASE/executions/<id>?includeData=true"
```

Los scripts del repo (`crear-flujos-crecimiento.py`, `parche-avisos-comentarios-dm.py`,
`rotar-token.py`) usan exactamente esto y son idempotentes: se pueden volver a correr.

---

## 5 · El Funnel: encender, apagar y qué se rompe

En la máquina `192.168.1.200`:

```bash
sudo tailscale funnel --bg 5678        # encender
sudo tailscale funnel --https=443 off  # apagar
```

**Al apagarlo se rompen tres cosas y ninguna avisa:**

| Se rompe | Por qué |
|---|---|
| El bot de Telegram `@Bordacreabot` | Su `setWebhook` apunta a `/webhook/ruleta-ayunka` a través del Funnel |
| Cualquier conector de Claude | Anthropic pega desde sus servidores, no desde la casa |
| El webhook de cotizar envío | Misma razón |

**No se rompe:** todo lo que corre por horario (publicar, historias, avisos, reportes,
respaldos). Esos salen hacia afuera y no necesitan que nadie entre.

### El detalle que confunde

`docker-compose.yml` sigue diciendo `N8N_HOST=192.168.1.200` y `N8N_PROTOCOL=http`, y eso
está **a propósito**. Solo cambia la URL que n8n *muestra* en su interfaz; el webhook de
producción responde igual entrando por el Funnel — comprobado el 5-ago-2026 con un POST real
que devolvió 200. Cambiarlo obliga a reiniciar el contenedor, y ese reinicio ya falló una vez.

---

## 6 · Las credenciales de la conexión

Ninguna vive en el repositorio. Todas están en `credenciales-privadas.txt`, que el
`.gitignore` tapa.

| Credencial | Dónde | Vence |
|---|---|---|
| **API key de n8n** (`X-N8N-API-KEY`) | `credenciales-privadas.txt` | ⚠️ **27-sep-2026** |
| Contraseña de la interfaz de n8n | gestor de contraseñas del navegador | no |
| `N8N_ENCRYPTION_KEY` | `docker-compose.yml` + `credenciales-privadas.txt` | no |
| Token del MCP Server Trigger | dentro del workflow, en n8n | no |
| Token de Telegram `@Bordacreabot` | `credenciales-privadas.txt` | no |
| Token de página de Meta | dentro de n8n + `n8n/token-pagina.txt` | no (rotado 11-ago-2026) |

> **La API key vence el 27 de septiembre.** Cuando pase, todo lo de la sección 4.3 va a
> devolver 401 y el conector oficial va a dejar de funcionar de golpe. Se renueva en
> Settings → n8n API, y hay que actualizarla en `credenciales-privadas.txt` **y** en el
> conector de Claude.

> **La clave de cifrado no se toca.** Si cambia, n8n no puede descifrar ninguna credencial
> guardada dentro — se rompen todos los flujos a la vez.

---

## 7 · Diagnóstico: qué significa cada respuesta

Antes de tocar nada, pegarle a la API y leer el código. Es más rápido que cualquier hipótesis.

| Código | Dónde | Qué significa | Qué hacer |
|---|---|---|---|
| **000 / timeout** | cualquiera | El Funnel está caído o la máquina apagada | Encender el Funnel |
| **200** en `/` | interfaz | Funnel arriba, n8n vivo | — |
| **401** en `/api/v1/…` | API | Falta la key, o venció | Revisar la fecha del punto 6 |
| **404** en `/webhook/<ruta>` | webhook | **El flujo está desactivado** o la ruta cambió | Activar el flujo |
| **404** desde un conector | MCP | La URL del conector no apunta a nada | Sección 3 |
| **200 pero sin herramientas** | MCP | El nodo no tiene nada colgado | No es una falla |

**Trampa de webhooks:** al cambiar la ruta de un webhook por API hay que **desactivar y
volver a activar** el flujo, o n8n sigue sirviendo la ruta antigua.

**Trampa de horarios:** el cron se escribe en hora de Chile y `startedAt` de la API viene en
UTC. Chile +4. Un flujo de las 07:30 aparece corriendo a las 11:30 y está perfecto.

**Regla del repo:** un mensaje de error escrito por nosotros no es evidencia, es la hipótesis
de quien lo escribió meses atrás. Antes de actuar, preguntarle a la API.

---

## 8 · Historia, para no repetir el camino largo

| Fecha | Qué pasó |
|---|---|
| **28-jul-2026** | Se decidió **no** exponer n8n. Se comprobó que la app de Claude no admite servidores MCP locales por archivo: no genera `claude_desktop_config.json` propio y su interfaz de conectores exige HTTPS. Un puente con `mcp-remote` tampoco sirve. Queda archivado en `n8n/archivo/` |
| **29-jul-2026** | Se monta el Tailscale Funnel. n8n queda en internet con HTTPS, sin abrir puertos del router |
| **5-ago-2026** | Se comprueba que **operar n8n por API funciona de verdad**: crear, activar y leer ejecuciones. Deja de importarse JSON a mano. Ese mismo día el bot de Telegram pasa a depender del Funnel |
| **11-ago-2026** | Token de Meta rotado y automatizado con `rotar-token.py` |
| **30-ago-2026** | Este documento. Funnel y API verificados sanos; el conector MCP configurado devuelve 404 |

---

## 9 · Resumen en cinco líneas

1. n8n vive en la casa, en `192.168.1.200:5678`, y sale a internet por Tailscale Funnel en
   `https://dietpi.tail05c49d.ts.net`.
2. La conexión que importa es la **API de administración** con `X-N8N-API-KEY` — hoy está
   viva y respondiendo.
3. El **conector oficial de n8n** (API key) es el que deja operar los flujos. El conector
   personalizado `/mcp-server/http` es un extra y hoy está mal apuntado.
4. Si el Funnel se apaga, se publica igual pero el bot queda mudo y Claude queda afuera.
5. **La API key vence el 27 de septiembre de 2026.** Es la única fecha que hay que recordar.
