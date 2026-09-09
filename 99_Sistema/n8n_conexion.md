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

## 3bis · Estado re-medido el 07-sep-2026 — **el Funnel cambió de forma**

> ⚠️ **Esto deroga la tabla del §3 (30-ago).** Aquella decía `GET /` → 200 y la API de
> administración viva y respondiendo 401 desde fuera. **Hoy es falso**, y no porque n8n se
> haya caído: el Funnel dejó de publicar la instancia entera y ahora publica **una sola
> ruta**. Medido con curl contra la URL pública, no deducido.

| Prueba (desde fuera de la casa) | Hoy | 30-ago |
|---|---|---|
| `GET /` | **404** `404 page not found` (texto plano, `nosniff` → es el 404 **de Tailscale**, no de n8n) | 200 |
| `GET /api/v1/workflows` **con** API key válida | **404** (mismo 404 de Tailscale) | 401 «header required» |
| `GET /mcp/` | **200** — HTML de la interfaz de n8n (**v2.30.8**), servido por el *fallback* de la SPA | — |
| `GET /assets/…`, `/static/…`, `/rest/login` | **404** | — |
| `GET /mcp/ayunka/sse` + `Authorization: Bearer …` | **200** + `event: endpoint` con `sessionId` | — |

**Lectura:** el Funnel monta **solo el prefijo `/mcp`** y lo pasa **sin recortarlo**
(si lo recortara, `/mcp/ayunka/sse` llegaría a n8n como `/ayunka/sse` y devolvería el HTML
de la SPA en vez de un stream SSE real — devuelve el stream, luego no recorta). Todo lo que
cuelga fuera de `/mcp` lo contesta Tailscale con su propio 404.

**Consecuencia dura, y es la que importa:** la **puerta 2 (API de administración con
`X-N8N-API-KEY`) ya NO existe desde internet.** La sección 4.3 de este documento —
«por API, sin conectores (siempre funciona)» — **dejó de funcionar desde fuera de la casa**.
Sigue sirviendo desde la red local (`192.168.1.200:5678`) o por VPN de Tailscale.

### El MCP `/mcp/ayunka/sse` — vivo, con dos defectos

Comprobado el 07-sep con un apretón de manos MCP hecho a mano (GET SSE → `initialize` →
`tools/list` → `tools/call`):

- ✅ `initialize` responde `n8n-mcp-server v0.1.0`.
- ✅ Expone **5 herramientas**: `listar_flujos`, `activar_flujo`, `desactivar_flujo`,
  `ver_ejecuciones`, `detalle_ejecucion`.
- 🔴 **Las 5 devuelven `Request failed with status code 401`.** El nodo HTTP que llevan
  adentro le pega a la API de n8n con una **credencial guardada dentro de n8n que está
  rechazada**. Se arregla **desde la interfaz de n8n**, no desde fuera: pegar una API key
  vigente en esa credencial. Ninguna key que se pase por fuera puede sustituirla.
- 🐛 **Cada herramienta declara un segundo parámetro requerido con el nombre en blanco (`""`).**
  Un cliente MCP normal muere ahí con `ZodError` antes de llegar a n8n. Se pasa a mano
  mandando `{"limite":"50","":""}`. Es un campo de parámetro que quedó sin nombre en el nodo.
- 🔌 **Por qué el conector de Claude da 404 y no es del servidor:** la ruta sirve **SSE
  legacy** (GET → `event: endpoint` → POST a `/mcp/ayunka/messages?sessionId=…`), y el
  conector le está haciendo POST directo estilo *streamable HTTP*. La URL y el Bearer están
  bien; lo que hay que elegir al registrarlo es el transporte **SSE**.

## 3quater · Re-medido el 09-sep-2026 — **el 401 no es una credencial rota, es que NO HAY credencial**

> Medido por la sesión que vive en la máquina DietPi, por API contra el workflow vivo, y
> **deroga el diagnóstico del §3bis**. Lo escribo con el error a la vista porque mandó a
> buscar durante dos días una credencial que no existe.

**Lo que decía el §3bis:** «el nodo HTTP que llevan adentro le pega a la API de n8n con una
credencial guardada dentro de n8n que está rechazada». **Falso.** Los cinco nodos salen
**sin autenticación**:

| Herramienta | `authentication` | `credentials` |
|---|---|---|
| `listar_flujos` | None | `{}` |
| `activar_flujo` | None | `{}` |
| `desactivar_flujo` | None | `{}` |
| `ver_ejecuciones` | None | `{}` |
| `detalle_ejecucion` | None | `{}` |

No hay nada que reparar: **hay que crear la credencial y adjuntarla**. El arreglo por API
(`POST /api/v1/credentials` + `PUT /api/v1/workflows/<id>`) sigue siendo el camino correcto.

**Los nombres exactos, para no re-apuntar el nodo equivocado:**

- Workflow: **`Ayünka · Servidor MCP para Claude`** — id `R1wREcQC6OLNEQ73`, activo.
- ⚠️ **Sí existe** una credencial llamada `MCP Claude (auto)` (id `XWFF9tUd0u94I5z2`, tipo
  `httpHeaderAuth`), y **NO es la de las herramientas**: es el Bearer del nodo trigger
  `🔌 Servidor MCP`. Tocarla tumba el conector.

**Dos trampas del `PUT`, aprendidas a golpes el 07-sep:**

1. Rechaza campos extra en `settings` (`request/body/settings must NOT have additional
   properties`). Este workflow trae `binaryMode` y `availableInMCP`: hay que filtrarlos y
   dejar solo `executionOrder`, `timezone`, `saveDataErrorExecution`,
   `saveDataSuccessExecution`, `saveManualExecutions`, `saveExecutionProgress`,
   `executionTimeout`, `errorWorkflow`.
2. El `PUT` **no acepta `active`**. Para re-registrar: `POST …/deactivate` y luego
   `POST …/activate`.

**El parámetro en blanco: SÍ estaba en el nodo, y era la misma herida que el 401.**

> ♻️ Este párrafo se escribió dos veces el mismo día y las dos primeras versiones estaban
> mal. El §3bis dijo «un campo de parámetro sin nombre en el nodo» mirando
> `placeholderDefinitions`; al no encontrarlo ahí se corrigió a «lo genera la capa MCP de
> n8n, no se arregla editando el workflow». **También falso.** Lo que faltó las dos veces
> fue abrir el nodo entero en vez de mirar el campo donde se esperaba encontrarlo.

Cada una de las 5 herramientas llevaba:

```json
"sendHeaders": true,
"parametersHeaders": { "values": [ {} ] }
```

— una **fila de cabecera vacía**. n8n la expone como un segundo parámetro requerido **con el
nombre en blanco**, y ahí muere con `ZodError` cualquier cliente MCP normal. Y es el mismo
resto de la cabecera que nunca se llenó que dejó a los nodos sin autenticación: alguien iba a
poner ahí el `X-N8N-API-KEY` a mano y no lo puso. **Un solo descuido causaba los dos
síntomas.**

Sacando `sendHeaders` + `parametersHeaders` (solo cuando todas las filas están vacías; si
alguien puso una cabecera de verdad, no se toca) el esquema pasa de «2 properties» a
«1 properties» y queda solo `limite` / `id`.

### ✅ Arreglado y verificado el 09-sep-2026

1. Credencial creada **por API** — `n8n API para herramientas MCP (X-N8N-API-KEY)`, id
   `wMLjQUM6hfn3Ajpn`, tipo `httpHeaderAuth`, `{name: X-N8N-API-KEY}`. Por API y no por la
   interfaz: en la 2.30.8 las credenciales creadas desde la interfaz no funcionan con el MCP
   Server Trigger (`n8n-io/n8n#30076`).
2. Adjuntada a las 5 herramientas (`authentication: genericCredentialType` +
   `genericAuthType: httpHeaderAuth`). El trigger quedó **intacto** con su
   `MCP Claude (auto)`.
3. Sacada la fila de cabecera vacía de las 5.
4. `PUT` con los `settings` filtrados, y `deactivate` + `activate` para re-registrar.

**Verificado con un apretón de manos MCP a mano contra la URL pública**, no dado por hecho:
`initialize` → `n8n-mcp-server 0.1.0` · `tools/list` → **5 herramientas** ·
`listar_flujos` y `ver_ejecuciones` **devuelven datos reales**. Las tres que mutan flujos no
se probaron en vivo a propósito.

> 🐛 **Trampa del cliente SSE, para quien escriba el próximo:** las respuestas vuelven por el
> stream, no por el POST, y **hay que emparejarlas por `id`**. Leer «la siguiente que
> llegue» da resultados falsos: `notifications/initialized` mandada con `id` (error: una
> notificación no lleva id) devuelve un `Method not found` que se lee como si fuera la
> respuesta de `tools/list` — y reporta **0 herramientas** cuando hay 5. Pasó acá.

**Cómo se llama una herramienta:** n8n envuelve todo en una sola propiedad `input` que es un
**JSON en texto**; los parámetros declarados viajan adentro de ese string.

```
{"name": "listar_flujos", "arguments": {"input": "{\"limite\": \"3\"}"}}
```

**El Funnel se queda así, y es deliberado:** publica **solo `/mcp` y `/webhook`**, de forma
permanente, porque la API de administración no debe estar expuesta a internet. El **conector
oficial de n8n por Funnel está muerto** — dese por muerto. Por LAN o Tailscale funciona.

**Alcance de red medido el 09-sep desde el PC de La Voûte:**

| Ruta | Código |
|---|---|
| `https://dietpi.tail05c49d.ts.net/` | 404 |
| `https://dietpi.tail05c49d.ts.net/mcp/` | 200 |
| `https://dietpi.tail05c49d.ts.net/api/v1/workflows` | 404 |
| `http://192.168.1.200:5678/api/v1/workflows` | **401** `'X-N8N-API-KEY' header required` |
| `http://100.117.183.70:5678/api/v1/workflows` (Tailscale) | **401** |

> 📄 **Dueño real de esta sección:** la documentación viva está en la máquina DietPi, en
> `/home/dietpi/docs/07-mcp-n8n.md`, actualizada el 09-sep con la tabla de alcance de red,
> los nombres exactos y las fechas de la key. Este archivo es copia de referencia: si
> divergen, manda el del server.

---

## 3ter · Dónde guarda de verdad el flujo «todo relatos» (07-sep-2026)

**n8n no es el dueño de esos datos — es quien los escribe.** El flujo que sigue las
publicaciones de la Ama en `todorelatos.com` persiste en **Supabase, proyecto `ayunka`**
(`ncuvdpydwnepbysadoux`, us-east-1). Se llega ahí con el conector de Supabase, **sin
depender del Funnel ni de la API key de n8n** — que es como se pudo analizar el 07-sep
con el MCP de n8n en 401.

| Tabla | Filas | Qué guarda |
|---|---|---|
| `tr_relatos` | 59 | los relatos propios (título, categoría, fecha de publicación) |
| `tr_mediciones` | 113 | toma global: totales + deltas · `tipo` = `cierre` \| `parcial` |
| `tr_relato_mediciones` | 6.469 | la toma, relato por relato (lecturas, votos, nota, comentarios) |
| `tr_comentarios` | 72 | texto y autor de cada comentario |
| `tr_rankings` | 169 | tamaño y corte de cada lista + posición propia cuando aplica |
| `tr_cat_relatos` | 1.073 | catálogo de la competencia (`propio` marca los propios) |
| `tr_cat_mediciones` | 5.597 | la serie del catálogo |

Cadencia medida: **4 tomas diarias** (1 `cierre` + 3 `parcial`), **27 días de 27 sin un
solo hueco** entre el 12-ago y el 07-sep. El catálogo arrancó el 24-ago.

### Los dos defectos reales (y los dos que NO lo eran)

> ⚠️ Los cuatro se reportaron primero como defectos. **Dos se cayeron al medirlos**, y
> quedan escritos acá con el número que los desmiente — un defecto inventado manda a
> arreglar lo que funciona.

| # | Estado | Qué pasa |
|---|---|---|
| 1 | 🔴 **real** | `pct_terrible…pct_excelente` llenos en **468 de 6.469 filas (7,2 %)**, y solo en tomas de `cierre`, donde llegan al 30,3 %. Es la distribución de notas y se está perdiendo. **Arreglo: en n8n**, no desde la base |
| 2 | 🔴 **real** | `delta_comentarios` nulo en **87 filas** (86 `parcial` + 1 `cierre`) mientras `delta_lecturas` y `delta_votos` sí se calculan. **Arreglo abajo** |
| 3 | ✅ **no era** | Se dijo que el flag `propio` estaba sin marcar (7 de 1.073). Medido: hay **exactamente 7 relatos con autor `AnaisBelland`** en el catálogo y **los 7 están marcados** — 0 falsos negativos, 0 falsos positivos. Lo corto es la **cobertura** del catálogo (sigue listados recientes), no el flag |
| 4 | ✅ **por diseño** | Se dijo que `relato_id` nulo en 148 de 169 rankings era un bug. No lo es: la tabla guarda **siempre** el tamaño y el corte de cada lista y rellena `relato_id` **solo cuando hay un relato propio dentro**. La limitación real es otra: **nunca registra quién ocupa los primeros puestos**, así que no hay inteligencia competitiva |

### El arreglo del defecto 2 — **backfill APLICADO 07-sep-2026**, disparador pendiente

Autorizado por la Ama (*"UPDATE ok"*) y ejecutado contra la base de producción.

```sql
with s as (
  select id, total_comentarios - lag(total_comentarios) over (order by medido_en) d
  from tr_mediciones
)
update tr_mediciones m set delta_comentarios = s.d
from s where s.id = m.id and m.delta_comentarios is null and s.d is not null;
-- 86 filas actualizadas
```

**Verificado después, no dado por hecho:** `tr_mediciones` queda en **112 de 113 filas con
delta**, deltas entre **0 y 3**, **ninguno negativo**. La única nula es `id = 1` — la primera
medición de todas, que no tiene anterior de dónde restar, y ahí el nulo es correcto.

> ⏸️ **El disparador NO está puesto.** El `create function` + `create trigger` es un cambio
> de **esquema**, no un arreglo de datos, y el permiso que dio la Ama fue para el `UPDATE`.
> Queda escrito acá para cuando ella lo autorice — mientras tanto, **cada fila nueva que
> inserte n8n vuelve a llegar con `delta_comentarios` nulo**, así que el backfill hay que
> repetirlo o poner el disparador.

```sql
create or replace function tr_fill_delta_comentarios() returns trigger
language plpgsql security invoker set search_path = public as $$
begin
  if new.delta_comentarios is null and new.total_comentarios is not null then
    select new.total_comentarios - m.total_comentarios into new.delta_comentarios
    from public.tr_mediciones m
    where m.medido_en < new.medido_en and m.total_comentarios is not null
    order by m.medido_en desc limit 1;
  end if;
  return new;
end $$;

drop trigger if exists tr_mediciones_delta_comentarios on public.tr_mediciones;
create trigger tr_mediciones_delta_comentarios
  before insert on public.tr_mediciones
  for each row execute function tr_fill_delta_comentarios();

-- deshacer:
-- drop trigger tr_mediciones_delta_comentarios on public.tr_mediciones;
-- drop function tr_fill_delta_comentarios();
```

### Hallazgo lateral: el flujo se disparó dos veces una vez

`tr_mediciones` id **60 y 61** llevan el mismo `medido_en` con **84 ms de diferencia**
(2026-08-23 08:51:09.201 y .285), las dos de tipo `parcial`. Es un doble disparo del
workflow, no un dato malo — los totales coinciden. Los **cierres están limpios**: cero días
con dos. Anotado, no tocado; si se repite, revisar el trigger del cron en n8n.

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
| **API key de n8n** (`X-N8N-API-KEY`) | `credenciales-privadas.txt` | ⚠️ **07-oct-2026** (key nueva emitida el 07-sep-2026 14:23 UTC; deroga el 27-sep) |
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

> ♻️ **Reescrito el 09-sep-2026.** El resumen anterior se contradecía con el §3bis del propio
> archivo: daba la API de administración por viva desde internet (muerta desde el 07-sep) y
> ponía el vencimiento de la key el 27-sep cuando el §6 ya decía 07-oct. Un resumen viejo es
> peor que ninguno, porque es lo primero que se lee.

1. n8n vive en la casa, en `192.168.1.200:5678`. El Tailscale Funnel
   (`https://dietpi.tail05c49d.ts.net`) publica **solo `/mcp` y `/webhook`**, a propósito y de
   forma permanente: la API de administración **no** debe estar expuesta a internet.
2. Por eso **la API de administración solo se alcanza desde dentro** — red de casa o
   Tailscale. Ahí está viva: responde 401 «header required», medido el 09-sep. Desde
   internet devuelve el 404 de Tailscale.
3. **El conector oficial de n8n por Funnel está muerto**, no mal configurado. El que sí vive
   es `/mcp/ayunka/sse`, con transporte **SSE clásico** (no streamable HTTP) y Bearer.
4. Si el Funnel se apaga, se publica igual pero el bot de Telegram queda mudo y Claude queda
   afuera.
5. **La API key vence el 07 de octubre de 2026** (emitida el 07-sep 14:23 UTC, expira el
   07-oct 03:00 UTC). Es la única fecha que hay que recordar — y **solo se emite a mano**
   desde Settings → n8n API: la API pública no tiene endpoint para crear API keys.
