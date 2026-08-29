# 📱 Propuesta de mejoras — LV-App

> **Base:** lectura completa del código (Kotlin/Compose) el 14/07/2026 — `GitRepository`, `MainViewModel`, `PromptFilterScreen`, `SummaryScreen`, `GeminiRepository`, `Entities`.
> **Dolor declarado por la Ama:** *«regenerar la misma pose mil veces»*. Todo lo de abajo está ordenado por cuánto ataca **eso**.
> **Uso real:** las 4 pestañas (Prompts · Galería · Relatos · Faltantes).

---

## 🩸 BLOQUE 1 — Atacar el dolor: que la imagen salga bien a la primera

### 1.1 · El negativo tiene que llegar a Gemini ⭐ (ya pedido en el prompt #3)
Hoy el bloque negativo **nunca se parsea ni se copia**, así que **nunca llegó al generador**. Es la causa mecánica número uno de que vuelvan los defectos (guantes, costura al frente, tacón chunky, marcas sobre la tela). Sin esto, todo lo demás es maquillaje.

### 1.2 · 🔴 REGISTRAR LOS DESCARTES — la mejora de mayor valor de toda la lista
**El problema real no es que las imágenes salgan mal. Es que cuando salen mal, el dato se pierde.**

Hoy la Ama borra la imagen fallada (`Delete image via Voute App`) y regenera. Resultado: el repo solo guarda **las sobrevivientes**. Nadie sabe cuántos intentos costó cada pose ni **por qué** falló. Y yo termino arreglando el motor a ciegas: adivino el defecto, escribo un lock, y no tengo forma de saber si sirvió.

**Propuesta:** cuando la Ama borre una imagen, la app pregunta **por qué**, con botones de un toque (no texto libre):

```
¿Por qué la descartas?
[ Costura de la media al frente ]   [ Zapato incorrecto ]
[ Marcas/piercings sobre la tela ]  [ Corte no pedido en la ropa ]
[ Anatomía (manos/piernas) ]        [ Material mate, no brilla ]
[ Pose equivocada ]                 [ La bloqueó el filtro ]
[ Outfit distinto a otras poses ]   [ Otro ]
```

Y lo guarda en una tabla local + un archivo en el repo (ej. `99_Sistema/descartes.csv`):

```
fecha, look, pose, motivo, intento_nº
2026-07-14, 785, odalisque, zapato_incorrecto, 3
```

**Qué desbloquea esto:**
- La **tasa de reintento por pose y por defecto**: la única métrica honesta de si el motor mejora. Hoy no existe.
- Yo dejo de adivinar: si 40 descartes dicen "costura al frente", sé exactamente qué anclar.
- Un **antes/después real** del fix del negativo. Sin este dato, cuando la app quede parchada, no vamos a poder demostrar que sirvió.

> Es barato de implementar (un diálogo + una tabla Room + un append a un archivo del repo) y es lo que convierte el proyecto de "arreglar a ciegas" a "medir y corregir".

### 1.3 · Contador de intentos visible por pose
Que en la ficha de cada pose se vea: **«3 intentos»**. La Ama ve al instante qué poses son problemáticas, y yo veo qué prompts hay que reescribir. Sale gratis del punto 1.2.

### 1.4 · Bloquear las miniaturas ⭐ (ya pedido en el prompt #3)
1.701 imágenes (40% de la flota) están subidas a 286×512 px porque el botón «Copiar» de Gemini entrega un **preview**, no el original. Además de arruinar la calidad, **hace imposible auditar**: un piercing marcado bajo el látex no se ve en 286 px. La app tiene que frenar la subida y avisar.

---

## ⚠️ BLOQUE 2 — Riesgos vivos en el código

### 2.1 · 🔴 `generateMissingPrompt()` inventa prompts que rompen el canon
`MainViewModel.kt:780` → `GeminiRepository.generatePrompt(look.canonicalInfo, poseName)`.

Cuando falta el prompt de una pose, la app le pide a **Gemini que lo invente** a partir del `canonicalInfo`. Pero en los looks nuevos el `canonicalInfo` es solo `Ubicacion` + `Tags`: **no contiene el Bloque A del ADN** (1000cc, pelo cherry hip-length, uñas XXXL 5cm, piel porcelana), **ni el token de vestuario bloqueado, ni el de calzado (8 atributos), ni las anclas de pose, ni los locks**.

Un prompt así sale **sin ADN** y produce una Ele que no es Ele. Rompe la Ley de Continuidad (los 7 prompts de un look deben compartir el bloque físico **idéntico**).

**Además ya no hace falta:** desde el 14/07 los **591 looks tienen sus 7 prompts completos**. Es riesgo puro sin beneficio.

**Propuesta:** eliminar el botón, o —si se quiere conservar— que **no invente**: que construya el prompt pegando el Bloque A + outfit + calzado **de otra pose del mismo look** y solo cambie la dirección de pose. Nunca dejar que la IA redacte el ADN.

### 2.2 · El token de GitHub va compilado dentro del APK
`BuildConfig.GITHUB_PAT` y `BuildConfig.GEMINI_API_KEY` quedan **dentro del APK** y son extraíbles con herramientas triviales. Si el APK sale del teléfono, alguien puede escribir en el repo con ese token.
**Propuesta:** mover a `EncryptedSharedPreferences` con la clave pegada una vez desde ajustes, o al menos un PAT de alcance mínimo (solo `contents:write` de ese repo) y rotable.

### 2.3 · `extractLookNumber()` toma el primer número que encuentra
`GitRepository.kt:741` → `"\\d+".toRegex().find(path)`. Funciona porque las carpetas empiezan con `look<N>_`, pero es frágil: cualquier ruta con un número antes lo rompe.
**Propuesta:** anclar el regex: `^ele/look0*(\d+)_`.

---

## ⚡ BLOQUE 3 — Menos toques por imagen

### 3.1 · Ver la imagen (y su resolución) antes de subir
Preview + `1024×1024 ✓` en verde o `286×512 ⚠️ miniatura` en rojo. Evita subir la equivocada y evita el bug de las miniaturas de un vistazo.

### 3.2 · Botón «Abrir Gemini» con el prompt ya copiado
Un solo toque que copia el prompt completo **y** abre Gemini. Hoy son: copiar → salir → abrir Gemini → pegar. Se ahorran dos pasos **por cada una de las 7 poses de cada look**.

### 3.3 · Marcar un look como «cerrado»
Para no volver a mirarlo. Hoy la única señal es el contador de imágenes, que hasta ayer **mentía**.

---

## 🔧 BLOQUE 4 — Calidad de vida

### 4.1 · Sync incremental
`syncData()` baja el árbol completo, re-descarga `galeria_outfits.md` y re-parsea **los 4.325 prompts** en cada sincronización, y luego hace `replaceDataSilent` de todo. Con la flota actual eso es lento y gasta datos.
**Propuesta:** guardar el SHA del último árbol y del `.md`; si no cambió, no re-parsear.

### 4.2 · La voz de Ele en el chat no es la canónica
`GeminiRepository.chatWithEle()` define una Ele que *«habla de sí misma en tercera persona o como "esta bimbo" / "madame"»*. El canon real es **chilena cuica**: usa «tú», trata de **«cariño»**, jamás voceo argentino. Hoy la app tiene una Ele distinta a la del repo.
**Propuesta:** alinear el system prompt con `00_Ele/identidad_ele.md`.

### 4.3 · Las categorías son inventadas (ya pedido en el prompt #3)
`GitRepository.kt:373-403` adivina la categoría por keywords, con 13 categorías propias («Moda Elegante», «Gótico & Dark») que **no son las 10 del canon**. Y falla feo: `"platform"` → *Stripper & Pole*, cuando **todos** los looks llevan plataforma. Los filtros de la app filtran por categorías falsas.

---

## 📊 Orden recomendado

| # | Mejora | Ataca | Costo |
|---|--------|-------|-------|
| 1 | El negativo llega a Gemini | El dolor, directo | ya pedido |
| 2 | **Registrar los descartes** | El dolor, y nos da **la métrica** | bajo |
| 3 | Bloquear miniaturas | Calidad + hace posible auditar | ya pedido |
| 4 | Quitar `generateMissingPrompt` | Riesgo de canon | trivial |
| 5 | Preview + resolución antes de subir | Toques | bajo |
| 6 | Abrir Gemini con un toque | Toques | bajo |
| 7 | Sync incremental | Velocidad | medio |
| 8 | Token fuera del APK | Seguridad | medio |
| 9 | Voz de Ele canónica | Coherencia | trivial |

> **El #2 es el que cambia el juego.** Sin él seguimos arreglando a ciegas y no vamos a poder demostrar si el fix del negativo sirvió.
