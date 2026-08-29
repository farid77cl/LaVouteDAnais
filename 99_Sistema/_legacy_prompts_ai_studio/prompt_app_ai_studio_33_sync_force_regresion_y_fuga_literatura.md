# Prompt AI Studio #33 — El botón de sync volvió a forzar recarga completa (regresión del #32) + la Literatura ingiere documentos internos como si fueran capítulos

> **Fecha:** 2026-08-28
> **Repo:** `LV-App` · **Medido sobre HEAD `00fb7f7b8d1485ab245ee19bdc45d505f1237805`** (versionCode 27 / versionName "4.19")
> Corrige una regresión confirmada del #32 (sección 1) y cierra un hueco de contenido en la Literatura (sección 2, mismo archivo `GitRepository.kt`, bajo riesgo). **No toca el algoritmo de parseo de looks/prompts ni `CharacterProfile`/`PoseMatcher`.**

---

## 0. Contexto — por qué existe este prompt

La Ama diseñó y commiteó 5 looks nuevos de Ele (Looks 808-812, batch "La Perla y HB Lencería", `00_Ele/galeria_outfits.md` líneas 41684-41934, commit `8ac08ba5b` del 27/08 14:17) y reportó el 28/08 que no le aparecían en la app.

**Auditoría hecha antes de este prompt (repo de contenido, no tocar):**
1. Los 5 looks se parsean con **0 críticos** bajo una réplica en Python del algoritmo real de `GitRepository.parseMarkdown` (regex de heading, cierre de fence, extracción de pose por número y por substring). El heading usa un formato de pose distinto al de los looks anteriores (`### 1. Standing` en vez de `**1. Standing:**`), pero el parser real lo tolera vía el fallback de `lowerTrimmed.contains("standing")` cuando el regex numerado no matchea (falla porque la línea empieza con `###`, no con dígito). **No es la causa.**
2. No hay colisión de archivo: los únicos `.md` cuya ruta en minúsculas contiene `galeria_outfits` son `00_Ele/galeria_outfits.md` (el vivo), `00_Ele/galeria_outfits_archivo.md` (Look 85-199, no llega a 808) y `00_Ele/galeria_outfits.BKP3_20260621_092818.md` (excluido por el filtro `.bkp`). Sin pisado silencioso.
3. La categoría "Lencería" no está excluida en ningún filtro: `outfitType` y `category` resuelven ambos a `"Lencería"` para los 5 looks (el heading ya trae la palabra con tilde, y `finalizeLookCanonicalInfo` la normaliza igual). El filtro de la UI (`filteredLooks`, `MainViewModel.kt:342`) compara contra `outfitType`, no contra `category` — son asimétricos como campo, pero en este caso concreto coinciden.
4. **Evidencia de que el problema es intermitente, no permanente:** el propio repo de contenido registra 3 commits de subida de imagen hechos por la app (autor `cupcake`) el **28/08 09:20-09:21**, subiendo Standing/Back View/Seated del **Look 812** — uno de los 5 looks reportados como "no aparece". Como los 5 looks viven en el mismo archivo y se parsean en una sola pasada, si 812 quedó seleccionable en la app esa mañana, 808-811 (que preceden a 812 en el archivo) también deben haber quedado cargados en ese mismo sync. **Hipótesis con más evidencia a favor: el problema ya se autorresolvió una vez que hubo un sync exitoso — la pregunta real es por qué el sync no es confiable ni comunica su resultado.**

Con parser sano, sin colisión de archivo y sin filtro de categoría roto, la causa que queda en pie — y que el código confirma como regresión real, no hipótesis — es la de la sección 1.

---

## 1. 🔴 El botón de sync volvió a forzar recarga completa — el #32 se aplicó y luego se revirtió

`app/src/main/java/com/example/ui/LaVouteApp.kt:101`, el único botón ⟳ de la barra superior:

```kotlin
IconButton(
    onClick = { viewModel.triggerSync(force = true) },   // 🔴 sigue así
    enabled = syncState !is SyncState.Syncing,
    modifier = Modifier,
) {
```

El `#32` (18/08/2026) diagnosticó exactamente este bug y pidió quitar `force = true` de este botón. **`git log -p` sobre este archivo muestra que el fix SE APLICÓ en algún momento** (hay un commit que cambia `triggerSync(force = true)` → `triggerSync()`) **y que un commit posterior lo revirtió** de vuelta a `force = true`. No se investiga aquí cuál commit lo revirtió ni por qué — probablemente un merge o un parche posterior pisó el archivo completo sin conservar el cambio. Lo que importa es que **hoy, en HEAD, el bug está de vuelta**.

Efecto: cada toque del botón fuerza la rama `else` de `syncData` —

```kotlin
val filesToDownload = if (!force && prefs != null) { markdownFiles.filter { ... } } else { markdownFiles }
```

— y descarga los 6 `.md` completos. Medido hoy sobre el repo de contenido, eso ya no son 33,5 MB (cifra del #31, medida en julio): son **~31,2 MB solo entre `galeria_outfits.md` (22,47 MB), `galeria_outfits_archivo.md` (3,22 MB), `GALERIA_OUTFITS_MISS_DOLL.md` (2,75 MB) y `galeria_looks_anais.md` (2,37 MB)** — el archivo principal de Ele creció de 21,02 a 22,47 MB desde julio y sigue creciendo con cada batch nuevo.

**Consecuencia directa sobre el caso de los looks 808-812:** con `OkHttpClient` configurado a `readTimeout(60, TimeUnit.SECONDS)` (`GitRepository.kt:37`) y sin caché HTTP (el interceptor de `MyApplication.kt` reescribe `Cache-Control` pero no hay `.cache(...)` instalado en el cliente, cosa que el #31 ya pidió verificar y no consta que se haya hecho), una descarga de ~31 MB en una conexión móvil mediocre puede superar el timeout y lanzar `SocketTimeoutException`. Eso aborta el sync completo — no solo el archivo grande, todo el reporte — y la Ama no ve nada (sección 2). Reintentar varias veces hasta que una conexión más rápida complete la descarga a tiempo explica perfectamente por qué el Look 812 sí cargó esta mañana después de fallar antes.

### 1.1 El reporte de éxito sigue sin mostrarse — `SyncState.Success` sigue muerto

`MainViewModel.kt:1348-1381` (`triggerSync`):

```kotlin
val report = repository.syncData((GitHubAuthManager.getToken(getApplication()) ?: ""), force = force)
val errors = report.lines().filter { it.startsWith("✗") || it.startsWith("⚠") }.map { it.trim() }
...
_lastSyncTimestamp.value = time
_lastSyncErrors.value = errors
// Ocultar aviso de éxito, volver a Idle inmediatamente
_syncState.value = SyncState.Idle
```

El comentario literal `// Ocultar aviso de éxito, volver a Idle inmediatamente` sigue ahí, igual que antes del #32. `SyncState.Success(val message: String)` sigue **declarado y nunca asignado** (`MainViewModel.kt:26-28`). No existe ningún `SUMMARY:` en `GitRepository.syncData`, ni bytes descargados, ni duración medida. `grep -rn "Forzar recarga" app/src/main/java/` da **cero resultados** — el botón "Forzar recarga completa" en `GlobalSettingsDialog` (`LaVouteApp.kt:367-406`, que ya tiene "Vaciar caché de imágenes" del #31) **nunca se agregó**.

O sea: aunque el sync termine bien, la Ama no tiene ninguna señal en pantalla de que pasó algo. Si tocó el botón y no vio nada — porque tardó, porque el mensaje nunca existió, o porque de verdad falló — no tiene manera de distinguir esos tres casos. Esto es, con alta probabilidad, la experiencia real detrás de "no me aparecen los looks": no es que la app no los tuviera, es que no hay ninguna confirmación de que la sincronización haya ocurrido.

---

## 2. Cambios requeridos — Parte A (sync)

### 2.1 El botón ⟳ vuelve a ser incremental

```kotlin
// app/src/main/java/com/example/ui/LaVouteApp.kt:101
onClick = { viewModel.triggerSync() },   // sin force
```

### 2.2 El sync forzado va a Ajustes, con advertencia de costo

En `GlobalSettingsDialog` (`LaVouteApp.kt:367`), que hoy solo recibe `onDismiss: () -> Unit`, agregar un parámetro para disparar el sync forzado (lambda o `viewModel` directo — a criterio de quien implemente, pero el llamador en `LaVouteApp.kt:98` debe actualizarse igual) y un segundo botón debajo de "Vaciar caché de imágenes":

- Botón **"Forzar recarga completa"** → dispara `triggerSync(force = true)` y cierra el diálogo.
- Debajo, en texto chico: **"Descarga de nuevo las galerías completas (~31 MB). Úsalo solo si algo se ve desactualizado después de un sync normal."** — cifra actualizada, no la de julio.

### 2.3 Instrumentar el sync: archivos, bytes y segundos — y usarlo de verdad

En `GitRepository.syncData` (`GitRepository.kt:334`):

1. Medir la duración con `System.nanoTime()` de punta a punta.
2. Acumular los bytes de markdown efectivamente descargados (`markdownText.toByteArray().size` por archivo bajado) en un `AtomicLong` — las descargas van en `async` paralelo dentro de `coroutineScope` (`GitRepository.kt:407-433`).
3. Primera línea del reporte, con prefijo estable:

```
SUMMARY: Sync incremental · 0 de 6 archivos · 0 KB · 1,4 s
SUMMARY: Sync forzado · 6 de 6 archivos · 31,2 MB · 22,1 s
```

En `MainViewModel.triggerSync` (`MainViewModel.kt:1348`):

4. Extraer la línea `SUMMARY:` del reporte y guardarla en un nuevo `_lastSyncSummary: MutableStateFlow<String>` (persistido en `prefs`, igual que `_lastSyncErrors`).
5. **Usar `SyncState.Success(message)`**, hoy muerto: al terminar un sync **manual** (no el del arranque), ponerlo con el resumen; la UI lo muestra unos segundos (Snackbar de Material3 o el patrón que ya use la app) y vuelve a `Idle`.
   - 🚨 El auto-sync del arranque (`MainViewModel.kt:1164`, `triggerSync()` sin argumentos) y el que dispara `LiteratureScreen.kt:789` tras guardar una nota **siguen silenciosos** — no tocar ese comportamiento, es intencional.
6. En `DiagnosticCard` (`app/src/main/java/com/example/ui/DiagnosticCard.kt`, pintado en `SummaryScreen.kt:467`): agregar el resumen del último sync junto a la fila "Última sincronización:" (`DiagnosticCard.kt:109-120`), para que quede consultable aunque el aviso ya se haya ocultado. Esta card **ya** muestra `lastSyncErrors` (incluye líneas `⚠` de las advertencias de contrato de la regla 11) — no tocar esa parte, solo sumar la línea de resumen al lado de la fecha.

### 2.4 Versión

`versionCode = 28` · `versionName = "4.20"`.

---

## 3. Cambios requeridos — Parte B (Literatura: excluir documentos internos)

**Hallazgo separado, mismo archivo, bajo riesgo — se incluye porque ya quedó completamente especificado durante esta auditoría.** No relacionado con el bug de sync de la Parte A; corregir ambos en el mismo prompt porque viven en el mismo método de `GitRepository.kt`.

`GitRepository.parseAndSaveTree` (`GitRepository.kt:882-935`) indexa como "capítulo legible" **todo** `.md` bajo `03_Literatura/01_En_Progreso/**` o `03_Literatura/02_Finalizadas/**`, salvo:
- el archivo exacto `notas.md` (`GitRepository.kt:911`),
- carpetas cuyo nombre empiece con `_` (`_publicacion`, `_proceso`) (`GitRepository.kt:926`).

El contrato real del repo de contenido (ver `CLAUDE.md` del repo, sección "Story folder — el canonical file set") pone, en la **raíz de cada relato activo**, varios documentos de planificación que **no son prosa**: `brief_idea.md`, `investigacion.md` (o `investigacion_fetiches.md` en el motor de trance), `canon_relato.md`, `cronologia.md`, `walkthrough.md`, `diseno_trance.md`. Ninguno de estos nombres está excluido — todos caen en el mismo filtro que un capítulo real y aparecen en la lista de "archivos" de la Literatura, abribles con el Lector, con un título derivado del nombre de archivo (`canon_relato`, `cronologia`, etc.).

Peor: las carpetas `borradores/capitulo_N/` (versiones descartadas de un capítulo) y `reportes/capitulo_N/` (autoverificación, informes de validación) **tampoco** empiezan con `_`, así que el filtro de `GitRepository.kt:926` no las excluye. Un borrador **repudiado** de un capítulo puede aparecer en la lista de "capítulos" de un relato exactamente igual que la versión vigente — indistinguible para quien lee, salvo por el nombre de archivo.

### 3.1 El fix

En `GitRepository.kt`, cerca de la comprobación de `notas.md` (línea 911) y de la comprobación de carpetas (línea 926):

```kotlin
// Carpetas internas de un relato que no son contenido de lectura
if (folderSubPathList.drop(1).any {
        it.startsWith("_") ||
            it.equals("borradores", ignoreCase = true) ||
            it.equals("reportes", ignoreCase = true)
    }
) {
    continue
}

// Documentos de planificación en la raíz del relato — no son prosa
val nonNarrativePrefixes = setOf("canon_relato", "cronologia", "walkthrough", "investigacion", "brief_idea", "diseno_trance")
if (nonNarrativePrefixes.any { fileName.lowercase().startsWith(it) }) {
    continue
}
```

La segunda comprobación necesita `fileName`, que ya está calculado en `GitRepository.kt:909` antes del chequeo de `notas.md` — ubicar ambos bloques después de esa línea, en cualquier orden entre sí.

**No** tocar la lógica de versionado (`baseName`, `uniqueKey`, "keep newest version", `GitRepository.kt:930-961`) ni el criterio de descarte por carpeta raíz (`investigacion` / `resumenes` / `templates` a nivel de `03_Literatura/`, que es un caso distinto — carpetas top-level, no archivos dentro de un relato).

---

## 4. 🚫 Qué NO hacer

- **No** tocar el algoritmo de `parseMarkdown` (heading, poses, fences, negativo) ni el fallback de detección de pose por substring — están correctos y una réplica en Python los validó contra los looks 808-812.
- **No** tocar `CharacterProfile`, `PoseMatcher` ni el nombrado de poses.
- **No** cambiar el filtro `md_sha_<path>` ni el `?v=${fileEntry.sha}` de las URLs de markdown — esa parte del #31 está bien y sigue vigente.
- **No** convertir el auto-sync del arranque ni el post-nota en forzados.
- **No** quitar el filtro de `✗`/`⚠` que alimenta `lastSyncErrors` — se **añade** el resumen, no se reemplaza nada.
- **No** dejar el aviso de éxito permanente ni bloqueante.
- **No** excluir la carpeta `_ARCHIVO_LEGACY_V1` ni ninguna otra ya prefijada con `_` de forma distinta a como ya se excluye — ese caso ya funciona.
- **No** agregar librerías nuevas.
- **No** dejar scripts de trabajo sueltos en el repo (recurrente en el #29 y el #31 — van a `/scratch/`, no se commitean).

---

## 5. Criterios de aceptación — la Ama los puede verificar sola

1. Apretar ⟳ dos veces seguidas sin cambios en el repo: la segunda vez el aviso dice **`Sync incremental · 0 de 6 archivos · 0 KB`** y tarda un par de segundos.
2. Ajustes → **"Forzar recarga completa"**: el aviso dice **`Sync forzado · 6 de 6 archivos · ~31 MB`**.
3. Abrir la app de cero: no aparece ningún aviso de éxito (el arranque sigue callado), pero `DiagnosticCard` (pestaña La Flota) muestra el resumen de ese sync junto a la fecha.
4. `grep -n "triggerSync(force = true)" app/src/main/java/com/example/ui/LaVouteApp.kt` → aparece **solo** dentro de `GlobalSettingsDialog`, no en el `IconButton` de la barra superior.
5. Con un token válido y el repo de contenido tal cual está hoy: sincronizar y confirmar que **los 5 looks 808-812 aparecen** en el selector de la pestaña de generación, con sus 7 prompts cada uno.
6. Abrir un relato de `01_En_Progreso` que tenga `canon_relato.md`, `cronologia.md` o `walkthrough.md` en su carpeta: la lista de archivos del relato **no** los muestra. Si tiene una carpeta `borradores/` o `reportes/`, tampoco aparece nada de ahí.
7. Un relato con un capítulo real vigente (`capitulo_N_slug_vX.md`) sigue mostrando ese capítulo con normalidad — el filtro nuevo no se comió contenido legítimo.
8. `./gradlew assembleDebug` compila y `./gradlew testDebugUnitTest` pasa, incluidos los `@Test` de `CharacterProfileTest.kt`.
9. La cabecera muestra `v4.20 (28)`.

---

## 6. Entrega esperada (formato obligatorio)

1. **Diff completo por archivo.**
2. **Los tres avisos, transcritos literalmente** tal como salen en pantalla: sync incremental sin cambios, sync forzado, y el estado del `DiagnosticCard` después de cada uno.
3. **Lista de archivos de Literatura antes/después del fix de la Parte B**, para al menos un relato de `01_En_Progreso` que tenga `canon_relato.md`/`cronologia.md`/`walkthrough.md` en su raíz — nombre de archivo por archivo, en las dos columnas.
4. **Log real y literal** de `./gradlew assembleDebug` y `./gradlew testDebugUnitTest`. Si un comando falla o no se puede ejecutar, decirlo — no entregar como si hubiera compilado sin el log.
5. **Sección "NO HECHO"** explícita con cada criterio de §5 no cumplido o no verificado. Si está vacía, escribir "ninguno".
6. **Hash del commit.**
7. **No dejar scripts de trabajo en el repo** (`/scratch/` si hace falta uno, y no se commitea).

> ⚠️ **AI Studio corre su propio git "Init":** sus commits llegan a `farid77cl/LV-App` **solo cuando la Ama los pushea**. Pushear y verificar el HEAD real antes de reportar terminado.
