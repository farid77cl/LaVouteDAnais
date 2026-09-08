# 🔑 Guía de las 4 llaves de Tumblr — paso a paso

> **Para la Ama.** Decidido por ella el 08/09/2026 en la Mesa de La Voûte: *«Ármeme la guía paso a paso»*.
>
> 🪦 **Fecha de muerte declarada:** este archivo se borra el día en que las cuatro llaves estén en
> `06_RRSS/.env` y la línea base del blog corra por primera vez. No es documentación permanente —
> es un andamio, y los andamios se sacan.
>
> ⚠️ **Lo que esta guía NO tiene, y se lo digo antes de que lo busque: pantallazos.** Usted me los pidió
> y no se los puedo dar — no tengo forma de abrir su sesión de Tumblr ni de fotografiar su pantalla.
> Lo que sí puedo darle es el nombre exacto del botón y el orden exacto de los pasos. Si alguno no calza
> con lo que ve, dígamelo y lo corrijo: prefiero eso a inventarle una interfaz.

---

## Por qué son cuatro y no dos

Tumblr usa **OAuth 1.0a**, que firma cada llamada con **dos pares** de llaves:

| Par | Qué identifica | De dónde sale |
|---|---|---|
| **Consumer Key** + **Consumer Secret** | La *aplicación* — o sea el programa que llama | Registrar la app |
| **Token** + **Token Secret** | La *persona* — o sea usted, dueña del blog | Autorizar esa app con su cuenta |

**Con solo el primer par se leen datos públicos.** El conteo de **seguidores** —que es la mitad de la
línea base que queremos capturar— la API **solo lo entrega si la llamada va firmada como dueña del blog**.
De ahí que sean cuatro y no dos. Esto quedó verificado contra la API el 07/09/2026.

---

## Paso 1 · Registrar la aplicación (te da las dos primeras)

1. Entra a **<https://www.tumblr.com/oauth/apps>** con la cuenta dueña de `@lavoutedeanais`.
2. Botón **«Register application»**.
3. Rellena el formulario. Los campos que importan:
   - **Application name** → `La Voute d Anais` (sirve cualquier nombre; es solo etiqueta).
   - **Application website** → `https://lavoutedeanais.tumblr.com`
   - **Default callback URL** → `https://lavoutedeanais.tumblr.com`
     *(no lo vamos a usar para nada, pero el formulario lo exige.)*
   - **OAuth2 redirect URLs (space separate)** → `https://lavoutedeanais.tumblr.com`
   - **Application description** → una línea cualquiera.

   > 🩹 **Corregido el 08/09/2026, con la Ama al teléfono y el formulario abierto.** El campo
   > **OAuth2 redirect URLs** no estaba en esta guía: Tumblr agregó los campos de OAuth2 al
   > formulario y yo la escribí con lo que había en el repo, sin abrir la página. Ella lo encontró
   > llenándola.
   >
   > **Ese campo no se usa en este flujo** — nosotras firmamos con **OAuth 1.0a**, la de
   > `api.tumblr.com/console`, que es la que entrega Token y Token Secret. El formulario lo exige
   > igual, así que se repite la misma URL del blog. Acepta varias separadas por espacio; con una
   > basta. Debe ir con `https://` completo; si el formulario reclama, probar con la barra final.
4. Guardar. La app queda listada en esa misma página.
5. Ahí aparecen, bajo el nombre de la app:
   - **OAuth Consumer Key** → una cadena larga, visible directamente.
   - **Consumer Secret** → está escondido; hay que apretar **«Show secret key»**.

**Copia las dos.** Son la primera mitad.

---

## Paso 2 · Autorizar la app como dueña (te da las dos últimas)

1. Entra a **<https://api.tumblr.com/console>**.
2. Te va a pedir la **Consumer Key** y el **Consumer Secret** del paso anterior. Pégalos.
3. Tumblr muestra una pantalla de permiso: **«Allow»** / **«Autorizar»**. Acéptala — le estás dando
   permiso a *tu propia app*, no a un tercero.
4. Ya dentro de la consola, arriba a la derecha hay un menú que dice **«Show keys»**
   (en algunas versiones, un botón de llave 🔑).
5. Ahí salen las cuatro juntas. Las dos que te faltan se llaman:
   - **Token** (a veces rotulado *OAuth Token*)
   - **Token Secret** (a veces *OAuth Token Secret*)

---

## Paso 3 · Dejarlas en el repo

Crea el archivo **`06_RRSS/.env`** (no existe todavía) y pega esto con tus valores:

```
TUMBLR_CONSUMER_KEY=...
TUMBLR_CONSUMER_SECRET=...
TUMBLR_TOKEN=...
TUMBLR_TOKEN_SECRET=...
```

> ✅ **Ese archivo NUNCA se sube.** Verificado hoy: `.gitignore` línea 6 lo cubre con
> `06_RRSS/**/.env`, y `git check-ignore` lo confirma. Además yo no lo commiteo por regla.
>
> 📌 Los nombres exactos de las cuatro variables ya están escritos y explicados en
> `06_RRSS/.env.example`, que es su dueño único. Si alguna vez cambian, se cambian **ahí** y esta
> guía apunta, no copia.

---

## Paso 4 · Avísame

Cuando estén puestas, dímelo y corro dos cosas el mismo día:

1. **La línea base** — seguidores, notas y alcance del blog **hoy**. Con una advertencia que ya le
   hice el 07/09 y sigue en pie: **ese piso no es virgen**, usted ya publicó el Cap 1 de Café. Se
   rotula como «después del primer post», no como «antes de publicar nada».
2. **La prueba que decide la misión entera** — publicar un post con tags y mirar si un blog marcado
   **maduro** aparece en la búsqueda por tags. Las guías de Tumblr no lo dicen; no se resuelve
   leyendo, se resuelve publicando uno y mirando.

---

## ⚠️ Lo que las llaves NO destraban

**El avatar, el header y el tema del blog se suben a mano. Siempre.** Verificado contra la API el
07/09/2026: no hay endpoint para ninguno de los tres — `/avatar` es de *lectura* y `/info` devuelve
el tema pero no lo modifica. No es un pendiente que se abra consiguiendo credenciales, y prometerle
lo contrario sería prometerle de más.

Sus dos imágenes ya están listas en `05_Imagenes/blog_tumblr/`, el header ya cortado a
**3000 × 1055** con la cabeza a salvo. Eso se sube desde la interfaz de Tumblr, usted, con el dedo.

Todo lo demás —medir, publicar posts, leer asks— sí se automatiza.
