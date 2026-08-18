# Prompt AI Studio #31 — Rendimiento: sincronización, carga de imágenes y subida

> **Fecha:** 2026-08-18
> **Repo:** `LV-App` · **Medido sobre HEAD `0c2b7c7`** (versionCode 23 / versionName "4.14")
> Este prompt ataca **el rendimiento de la app en las dos direcciones**: lo que baja de GitHub y lo que sube. No cambia versiones de dependencias ni introduce librerías nuevas.

---

## 1. El hallazgo principal: cada sincronización descarga 33,5 MB de texto, y la caché está rota a propósito

Medido sobre el repo de contenido:

| Archivo `.md` que la app descarga | Peso |
|---|---|
| `00_Ele/galeria_outfits.md` | **21,02 MB** |
| `00_Ele/galeria_outfits_archivo.md` | 3,22 MB |
| `02_Personajes/01_Principales/miss_doll/GALERIA_OUTFITS_MISS_DOLL.md` | 1,19 MB |
| `02_Personajes/01_Principales/anais/galeria_looks_anais.md` | 0,96 MB |
| + otros que pasan el filtro | |
| **TOTAL (6 archivos)** | **33,54 MB** |

Y se piden así (`GitRepository.kt:291, 322, 361`):

```kotlin
val timestamp = System.currentTimeMillis()
...
val url = "https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/${fileEntry.path}?v=$timestamp"
```

**`System.currentTimeMillis()` en el query string hace que cada URL sea única en cada sync.** Ninguna caché —ni la de OkHttp, ni la del CDN, ni la del sistema— puede acertar jamás. Se bajan los 33,5 MB completos **aunque no haya cambiado un solo byte**, que es el caso normal: cuando la Ama sube fotos desde la app, los `.md` **no cambian**.

Además, antes de eso se pide el árbol completo del repositorio (`GitHubApiService.kt:75`, `?recursive=1`) sobre un repo con ~5.950 imágenes: un JSON de miles de entradas parseado con Moshi en memoria, también en cada sync.

### 1.1 El arreglo, con datos que la app YA tiene

**Nivel 1 — el commit.** `getMainRef()` (`GitHubApiService.kt:67`) ya devuelve el SHA del commit de `main`.

- Persistirlo tras cada sync exitoso (DataStore o `SharedPreferences`; DataStore está en el catálogo, conservado a propósito por el #30).
- Al iniciar el sync: si el SHA del ref **es igual** al guardado → **no descargar nada más y salir**, reportando "sin cambios". El sync entero pasa a ser **una request**.
- Debe existir un **sync forzado** (gesto de pull-to-refresh o botón) que ignore ese atajo, para cuando la Ama quiera obligar la recarga.

**Nivel 2 — por archivo.** La respuesta del árbol ya trae `sha` por blob (`GitTreeEntry.sha`, `GitHubApiService.kt:25`).

- Guardar, por cada `.md` procesado, su `sha` (una tabla Room chica `SyncStateEntity(path, sha)`, o un mapa serializado).
- En el siguiente sync, **descargar únicamente los `.md` cuyo `sha` difiere del guardado.** Los demás no se piden.
- Efecto esperado en el caso normal (subió fotos, no cambió texto): **0 MB de markdown**, en vez de 33,5 MB.

**Nivel 3 — URLs direccionables por contenido.** Reemplazar el cache-buster por el sha del blob:

```kotlin
// ANTES
val url = ".../${fileEntry.path}?v=$timestamp"
// DESPUES
val url = ".../${fileEntry.path}?v=${fileEntry.sha}"
```

Con eso la URL solo cambia cuando cambia el contenido, y la caché funciona sola. **Este es el mismo criterio que ya usan las imágenes** (`GitRepository.kt:805`: `?v=${entry.sha}`) — se trata de que el markdown haga lo que las imágenes ya hacen bien.

Quitar también el `@Query("t") timestamp: Long = System.currentTimeMillis()` de `getMainRef` (`GitHubApiService.kt:72`): ya lleva `Cache-Control: no-cache`, que es la forma correcta de pedir frescura sin ensuciar la URL.

> **Y un aviso honesto sobre `getMainRef`:** ese endpoint devuelve el SHA de `main`, que cambia con **cualquier** commit del repo — incluidos los de la propia app subiendo fotos y los del bot que reescribe READMEs. O sea el atajo del Nivel 1 va a fallar seguido. **Por eso el Nivel 2 no es opcional:** es el que de verdad evita la descarga. El Nivel 1 solo agrega el caso "no pasó absolutamente nada".

---

## 2. Subida: se decodifica el bitmap completo antes de escalarlo

`PromptFilterScreen.kt:175-201`:

```kotlin
val originalBitmap = android.graphics.BitmapFactory.decodeStream(inputStream)   // <-- completo, sin inSampleSize
...
val bitmapToUpload = android.graphics.Bitmap.createScaledBitmap(originalBitmap, ...)  // segunda copia
val outputStream = java.io.ByteArrayOutputStream()
bitmapToUpload.compress(PNG, 100, outputStream)
resizedBytes = outputStream.toByteArray()                                        // tercera copia
// y despues, en GitRepository.kt:161
val base64Content = Base64.encodeToString(imageBytes, Base64.NO_WRAP)            // cuarta copia, +33%
```

Se decodifica el archivo original **entero** a `ARGB_8888` solo para medirlo y reducirlo a 1200 px. Con originales grandes eso son decenas de MB de heap, y quedan hasta cuatro copias vivas del mismo contenido. Es lento y es riesgo real de `OutOfMemoryError`.

**Arreglo:**

1. **Dos pasadas de decodificación.** Primero solo los límites, sin cargar píxeles:
   ```kotlin
   val bounds = BitmapFactory.Options().apply { inJustDecodeBounds = true }
   context.contentResolver.openInputStream(uri)?.use { BitmapFactory.decodeStream(it, null, bounds) }
   // bounds.outWidth / bounds.outHeight sirven para la guardia de resolucion Y para calcular inSampleSize
   ```
   La validación de resolución (`isValidImageResolution`) debe hacerse **con estos bounds**, no decodificando la imagen.
2. Calcular `inSampleSize` (mayor potencia de 2 que deje el lado largo ≥ 1200) y decodificar ya reducido en la segunda pasada.
3. `createScaledBitmap` solo para el ajuste fino a 1200 exactos, y `recycle()` del bitmap intermedio cuando no sea el mismo objeto.
4. Mantener **PNG**: es el formato del repo de contenido y de todo el pipeline (`update_galleries.py`, los README, la galería). **No cambiar a JPEG/WebP** — rompería el contrato del repo por un ahorro que no se pidió.

**No tocar** la guardia de resolución mínima (`< 400.000 px` bloquea la subida) ni el sello `[gallery WxH]` del mensaje de commit: son defensas que costaron sangre y siguen vigentes.

---

## 3. Miniaturas que decodifican el PNG completo

`SkeletonAsyncImage` (`components/SkeletonImage.kt:55`) acepta un parámetro `size` opcional. De sus tres llamadores:

| Llamador | ¿Pasa `size`? | Debería |
|---|---|---|
| `ImageGalleryScreen.kt:614` (grilla) | ✅ `Size(400, 720)` | correcto, dejar |
| `PromptFilterScreen.kt:602` (preview del look) | ❌ **no** | **agregar** `size = coil.size.Size(400, 720)` |
| `ZoomableImage.kt:85` (visor con zoom) | ❌ no | **dejar así a propósito** — el zoom necesita la resolución completa |

Y `SummaryScreen.kt:249` usa un `AsyncImage` pelado: pasarle también un `ImageRequest` con `.size(...)` acorde a su celda.

Sin `size`, cada preview decodifica el PNG de 669×1200 a tamaño completo para pintarlo en una celda chica.

---

## 4. La caché de disco es demasiado chica para esta flota

`MyApplication.kt:35-40`:

```kotlin
.diskCache {
    DiskCache.Builder()
        .directory(this.cacheDir.resolve("image_cache"))
        .maxSizePercent(0.05)      // 5% del espacio libre
        .build()
}
```

La flota son **~5.950 imágenes** de ~0,8-1,1 MB. Con el 5% del espacio libre, la caché se desaloja constantemente y cada paseo por la galería vuelve a descargar de GitHub.

Subirla a `maxSizePercent(0.15)` **o** fijar un tope absoluto explícito (`maxSizeBytes(512L * 1024 * 1024)`), lo que resulte más predecible. Añadir en Ajustes un **"Vaciar caché de imágenes"** con el tamaño ocupado a la vista, para que la Ama pueda recuperar espacio cuando quiera.

**Verificar, no asumir:** el `addNetworkInterceptor` de `MyApplication.kt:15-27` reescribe `Cache-Control: max-age=7 días` en las respuestas, pero el `OkHttpClient` **no tiene un `Cache` instalado** (`.cache(...)` no aparece). Comprobar si Coil está honrando esa cabecera para su propia `DiskCache` o si el interceptor no hace nada; **reportar lo que se encuentre antes de cambiarlo**. No borrarlo a ciegas.

---

## 5. 🚫 Qué NO hacer

- **No** cambiar versiones de dependencias (eso fue el #29) ni borrar archivos (eso es el #30).
- **No** introducir Navigation, Hilt, Media3, Coil 3, Paging ni WorkManager. Los pasos 3-7 tienen su propio prompt.
- **No** cambiar el formato de imagen de PNG a JPEG/WebP.
- **No** tocar el nombrado canónico de poses ni `CharacterProfile`/`PoseMatcher` (fix del #28, recién aterrizado).
- **No** eliminar la guardia de resolución mínima ni el sello `[gallery WxH]` del commit.
- **No** "optimizar" bajando la calidad de lo que se sube.
- **No** cachear de forma que la Ama **no pueda forzar** una recarga: el sync forzado es requisito, no adorno.

---

## 6. Criterios de aceptación (observables)

1. **Segundo sync seguido, sin cambios en el repo:** no se descarga ningún `.md`. Debe quedar registrado en el log o en el reporte de sync en pantalla (p. ej. "0 de 6 archivos descargados · sin cambios").
2. **Sync después de subir una foto desde la app:** tampoco se descarga markdown (los `.md` no cambiaron), pero la imagen nueva sí aparece.
3. **Sync después de que cambie un `.md` en GitHub:** se descarga **solo ese archivo**, no los 6.
4. `grep -rn "System.currentTimeMillis()" app/src/main/java/com/example/data` → **0** en la construcción de URLs.
5. El sync forzado (pull-to-refresh o botón) ignora el atajo y vuelve a bajar todo.
6. Subir una imagen grande (≥ 4000 px de lado) **no** provoca `OutOfMemoryError` y el resultado sigue siendo PNG de lado largo 1200.
7. La guardia de resolución sigue bloqueando una imagen de 286×512.
8. `./gradlew assembleDebug` compila y `./gradlew testDebugUnitTest` pasa, incluidos los 8 `@Test` de `CharacterProfileTest.kt`.
9. `versionCode = 25`, `versionName = "4.16"`; la cabecera muestra `v4.16 (25)`.

---

## 7. Entrega esperada (formato obligatorio)

1. **Diff completo por archivo.**
2. **Medición antes/después**, que es el punto de todo esto: MB descargados y segundos que tarda un sync **sin cambios**, medidos las dos veces. Sin ese número no hay forma de saber si el trabajo sirvió.
3. **Log real y literal** de `./gradlew assembleDebug` y `./gradlew testDebugUnitTest`, pegado. Si un comando falla o no se puede ejecutar, decirlo.
   > El #29 se entregó **sin ningún log de build**. Este prompt toca la ruta de datos completa: sin log y sin la medición del punto 2, no es verificable.
4. **Sección "NO HECHO"** explícita con cada criterio de §6 no cumplido o no verificado. Si está vacía, escribir "ninguno".
5. **Hash del commit.**

> ⚠️ **AI Studio corre su propio git "Init":** sus commits llegan a `farid77cl/LV-App` **solo cuando la Ama los pushea**. Pushear y verificar el HEAD real.

---

## Anexo — la otra mitad, que se arregla del lado del repo de contenido

`galeria_outfits.md` pesa **21,02 MB** porque lleva 602 looks con sus 7 prompts en línea, en un solo archivo que solo crece. Aunque la app deje de bajarlo cuando no cambia (§1), **el día que cambia sigue costando 21 MB** — y cambia cada vez que se diseña un look.

Partirlo por rangos (`galeria_outfits_L200_L399.md`, `_L400_L599.md`, …) haría que un look nuevo invalide solo su tramo. **Eso no se hace en este prompt:** toca el contrato de galería (regla 11), el filtro `path.contains("galeria_outfits")` de la app, `update_galleries.py`, `lint_galeria.py` y los inyectores. Es una decisión de la Ama y merece su propio plan.
