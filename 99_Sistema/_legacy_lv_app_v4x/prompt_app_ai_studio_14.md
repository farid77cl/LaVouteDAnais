# 📝 Prompt #14 para AI Studio — Notas sobre imágenes en la Galería: marcar las malas o que no corresponden al outfit

> **Base:** repo `farid77cl/LV-App`. **Aplicar DESPUÉS del #13** y rebasar sobre el commit que deje el #13.
>
> **Motivo (de la Ama):** «se han subido imágenes malas, o que no corresponden al outfit» — necesita poder **dejar una nota sobre una imagen** para marcarla, SIN borrarla, y revisarla o regenerarla después.
>
> **Todo lo de abajo está verificado leyendo el código clonado, con archivo y línea. Reutiliza lo que ya existe — NO reinventes.**
>
> **Alcance:** la Galería (`ImageGalleryScreen.kt` + `LightboxViewer`) — (a) dos arreglos visuales pedidos por la Ama (portada frontal en vez de espaldas + quitar el texto de la esquina inferior derecha), y (b) una entidad/tabla nueva de notas + su sincronización a un CSV del repo de contenido. El flujo de SUBIDA de imágenes (portapapeles, selector, guardia de resolución, share) NO se toca.
>
> **Base al día:** aplicar sobre HEAD `2461b13` (el #13 ya está en el repo, aunque quedó en `versionCode 15 / versionName "4.8"` porque no bumpeó — este prompt corrige eso).

---

## 🔍 QUÉ YA EXISTE (para no reinventarlo)

Auditado en el código de hoy:

| Pieza | Estado | Evidencia |
|---|---|---|
| Notas persistidas + sync a GitHub (patrón) | ✅ Existe para relatos | `LiteratureNoteEntity` (`Entities.kt:53-59`) + `saveLiteratureNoteToGithub` (`GitRepository.kt:81`) |
| Anotar/registrar sobre una imagen con motivo + nota libre | ✅ Existe para DESCARTE (al borrar) | `DescarteEntity` (`Entities.kt:81-92`), `DescarteDialog(motivo, nota)`, `registrarDescarteConEvidencia` (`MainViewModel.kt:312`) |
| Sync de un registro a un CSV del repo de contenido | ✅ Existe | `syncDescartes(...)` → `99_Sistema/descartes.csv` (`GitRepository.kt:241-270`, append idempotente vía `putFile`) |
| Rating por imagen (marca ligera por `imagePath`) | ✅ Existe | `ImageRatingEntity` (`Entities.kt:67-71`), `allImageRatings` (`MainViewModel.kt:252`) |
| Visor con acciones (borrar → descarte) | ✅ Existe | `LightboxViewer` con `onDeleteImage`/`onDelete` (`ImageGalleryScreen.kt:264-278`) |

**Traducción:** la maquinaria de «anotar una imagen con motivo + texto y sincronizarla a un CSV» YA existe para el descarte (que además BORRA la imagen). Lo nuevo es una **nota que NO borra**: marca la imagen como «mala / no corresponde» dejándola en su sitio, con un distintivo visible y un filtro para revisarlas. Es un `DescarteEntity` sin el borrado, o un `ImageRatingEntity` con texto — cópialo, no lo inventes.

---

```
Eres el desarrollador de LV-App (Kotlin / Jetpack Compose / Room / Retrofit / Moshi / Coil).
Trabaja sobre el repo al día (aplica este prompt DESPUÉS del #13).

CONTEXTO: la Ama necesita marcar imágenes malas o que no corresponden al outfit, dejándoles una
nota, SIN borrarlas. Reutiliza el patrón de DescarteEntity/DescarteDialog/syncDescartes y el de
LiteratureNoteEntity — no reescribas nada de eso. Si discrepas de algo, dilo al final en
"NO HECHO:" con evidencia.

⭐ INTOCABLE: el flujo de subida de imágenes (portapapeles, selector de galería, guardia de
resolución, share, descartes). No se toca ni un archivo de esa ruta. La nota NUNCA borra la imagen.

#####################################################################
##  PARTE 0 — DOS ARREGLOS RÁPIDOS DE LA GALERÍA (chicos, hazlos primero)
#####################################################################

0A. LA PORTADA DEL OUTFIT DEBE SER FRONTAL, NO DE ESPALDAS
En modo Outfit, la portada de cada look se elige hoy con
`filteredImages.distinctBy { it.lookNumber ?: it.path }` (ImageGalleryScreen.kt:146-152).
`distinctBy` se queda con la PRIMERA imagen de cada look en el orden de la lista, que muchas veces
es una pose de espaldas. Cámbialo para que la portada sea la pose FRONTAL (standing) si existe, y
solo si no existe, la primera disponible. Mismo criterio que YA usa SummaryScreen.kt:218
(`allImages.find { it.poseName.lowercase() == "standing" }`). Ejemplo:

    if (isOutfitsMode) {
        filteredImages
            .groupBy { it.lookNumber ?: -1 }         // groupBy preserva el orden de primera aparición
            .map { (_, imgs) ->
                imgs.firstOrNull { it.poseName.lowercase() == "standing" } ?: imgs.first()
            }
    } else {
        filteredImages
    }

Conserva el orden que la galería ya usa (el sort seleccionado): solo cambia CUÁL imagen representa a
cada look, no el orden de los looks.

CRITERIO DE ACEPTACIÓN: en modo Outfit, la tarjeta de cada look muestra la pose frontal (standing)
como portada; solo los looks sin standing muestran otra pose.

0B. QUITAR EL TEXTO DE LA ESQUINA INFERIOR DERECHA DE LA TARJETA
En ImageCard (ImageGalleryScreen.kt) hay dos rótulos sobre la imagen:
 - arriba-izquierda, el nombre del look (`Alignment.TopStart`, :551-565) → ESE SE QUEDA.
 - abajo-derecha, "85 - BACK VIEW" (`Alignment.BottomEnd`, :573-593) → ESE SE ELIMINA por completo
   (borra ese Box entero, con su `when` de formattedPose). No toques el rótulo de arriba.

CRITERIO DE ACEPTACIÓN: la tarjeta de la galería muestra SOLO el texto de arriba (el nombre del
look); la esquina inferior derecha queda limpia, sin el "N - POSE".

#####################################################################
##  A — ENTIDAD Y PERSISTENCIA
#####################################################################

A1. Nueva entidad `ImageNoteEntity` (tabla "image_notes"), en Entities.kt, calcada del par
    ImageRatingEntity + DescarteEntity:

    @Entity(tableName = "image_notes")
    data class ImageNoteEntity(
        @PrimaryKey val imagePath: String,   // misma PK que ImageEntity.path
        val lookNumber: Int?,
        val poseName: String,
        val motivo: String,                  // "No corresponde al outfit" | "Mala calidad / defecto"
                                             // | "Baja resolución" | "Otra"
        val nota: String,                    // texto libre
        val fechaIso: String,
        val sincronizado: Boolean = false
    )

A2. Registra la entidad en AppDatabase.kt (súbele la versión de Room y deja
    `.fallbackToDestructiveMigration()` como ya se hace, para no romper la base instalada).

A3. En LookDao.kt agrega, calcado de los métodos de rating/nota existentes:
    - `@Query("SELECT * FROM image_notes") fun getAllImageNotes(): Flow<List<ImageNoteEntity>>`
    - `@Query("SELECT * FROM image_notes WHERE imagePath = :path") suspend fun getImageNote(path: String): ImageNoteEntity?`
    - `@Insert(onConflict = REPLACE) suspend fun insertImageNote(note: ImageNoteEntity)`
    - `@Query("DELETE FROM image_notes WHERE imagePath = :path") suspend fun deleteImageNote(path: String)`

#####################################################################
##  B — UI: DEJAR LA NOTA EN EL VISOR (sin borrar)
#####################################################################

B1. En LightboxViewer, junto a la acción de borrar/descartar que ya existe (onDelete), agrega una
    acción NUEVA "📝 Nota" (IconButton con Icons.Default.EditNote o Icons.Default.Comment), con su
    propio callback `onAddNote: (ImageEntity) -> Unit`. NO reutilices el botón de borrar: la nota
    deja la imagen en su lugar.

B2. Al tocar "📝 Nota", abre un diálogo (reutiliza el patrón visual de DescarteDialog):
    - Chips de motivo (selección única): "No corresponde al outfit" (default), "Mala calidad /
      defecto", "Baja resolución", "Otra".
    - Un campo de texto libre (opcional) para la nota.
    - Si la imagen YA tiene nota, precarga motivo + texto (getImageNote(path)) para editarla, y
      ofrece un botón "Quitar nota" (deleteImageNote).
    - Guardar → insertImageNote(...) con fechaIso = ahora y sincronizado = false.

CRITERIO DE ACEPTACIÓN: abrir una imagen en el visor, tocar 📝 Nota, elegir «No corresponde al
outfit», escribir "el corsé es de otro look" y guardar → la imagen SIGUE en la galería y queda
marcada. Reabrir el diálogo muestra la nota guardada.

#####################################################################
##  C — UI: VERLAS DE UN VISTAZO Y FILTRARLAS
#####################################################################

C1. Distintivo en la miniatura: en la grilla de la galería, las imágenes con nota llevan un badge
    (por ejemplo un 📝 o un punto ámbar en una esquina), leyendo `getAllImageNotes()` (igual que hoy
    se leen los ratings con allImageRatings, MainViewModel.kt:252). Así se ven de un vistazo cuáles
    están marcadas sin abrirlas.

C2. Filtro en la galería: un conmutador/checkbox "Solo marcadas 📝" que muestra únicamente las
    imágenes con nota. Persiste en SharedPreferences ("gallery_notes_only"). Sirve para revisar en
    tanda todo lo malo o mal asignado.

CRITERIO DE ACEPTACIÓN: con al menos una imagen marcada, el badge aparece en su miniatura y el
filtro "Solo marcadas" reduce la galería a esas imágenes.

#####################################################################
##  D — SINCRONIZACIÓN AL REPO DE CONTENIDO (para poder actuar sobre ellas)
#####################################################################

D1. En GitRepository.kt, calca `syncDescartes(...)` (:241-270) en un `syncImageNotes(notes, token)`
    que haga append idempotente a `99_Sistema/notas_imagenes.csv` en el repo de contenido, una fila
    por nota:  `fechaIso,lookNumber,poseName,imagePath,motivo,nota`  (escapa comas/comillas del
    texto libre como ya se haga en descartes; si no se escapa allí, envuelve el campo en comillas).
    Marca las filas subidas como sincronizado = true (como hace syncDescartes).

D2. Dispara `syncImageNotes` en el MISMO punto donde hoy se sincronizan los descartes (junto al
    push / al botón de sync que ya exista), no en un flujo nuevo. Si los descartes se suben al hacer
    pull/push, las notas viajan igual.

CRITERIO DE ACEPTACIÓN: tras marcar una imagen y sincronizar, aparece/actualiza
`99_Sistema/notas_imagenes.csv` con una fila para esa imagen. (Así el agente puede leer ese CSV y
regenerar los looks marcados.)

#####################################################################
##  E — TESTS Y ENTREGA
#####################################################################

Tests que ejerzan la ruta (pega la salida real con nombres, --rerun-tasks; PROHIBIDO assertTrue(true)):
  - insertImageNote luego getImageNote(path) devuelve el mismo motivo + nota; deleteImageNote lo quita.
  - El filtro "Solo marcadas" sobre una lista de prueba (2 con nota, 3 sin) deja exactamente 2.
  - La fila CSV de una nota con coma en el texto queda bien escapada (se puede volver a parsear).

Entrega:
  1. `git rev-parse HEAD` (pega la salida) + `git log --oneline -5`.
  2. Sube versionCode +1 y versionName +0.1 respecto a lo que HAYA en el repo al aplicarlo (si el
     #15 dejó 16/"4.9", este queda 17/"4.10"). Mantén el hash de commit visible en la cabecera.
  3. Declara el keystore usado y si coincide con el anterior.
  4. El APK.
  5. Sección "NO HECHO:" obligatoria, una línea por punto no logrado. Vacía + un test de la Parte E
     que falle = entrega no verificada.
```

---

## 📌 Nota de prioridad para la Ama

| Prioridad | Punto | Por qué |
|---|---|---|
| 🥇 | **A + B** (entidad + dejar la nota en el visor) | Es el corazón: marcar la imagen mala/mal asignada sin borrarla. |
| 🥈 | **C** (badge + filtro «Solo marcadas») | Para revisarlas de un vistazo y en tanda. |
| 🥉 | **D** (sync a `notas_imagenes.csv`) | Para que yo pueda leer el CSV y **regenerar** los looks marcados desde el repo. |

**Lo honesto:** esto reutiliza tres cosas que ya funcionan (DescarteDialog, el rating por imagen y
el sync a CSV de los descartes). La diferencia con el descarte es una sola: la nota **no borra** la
imagen, la deja marcada. Si algo se corta, lo mínimo útil es A + B (poder dejar la nota); el badge,
el filtro y el sync se pueden completar después.
