# Prompt AI Studio #32 — El sync incremental existe pero es inalcanzable, y no reporta nada

> **Fecha:** 2026-08-18
> **Repo:** `LV-App` · **Medido sobre HEAD `f5c8736`** (versionCode 25 / versionName "4.16")
> Corrige dos defectos introducidos/no cubiertos por el #31. **No rehace la lógica incremental: esa está bien.**

---

## 1. Qué pasó, medido

La Ama instaló la 4.16, apretó el botón de sincronizar **tres veces** y **no vio ningún mensaje**. Se leyó el código y hay dos causas apiladas.

### 1.1 🔴 El único botón de sync global fuerza la descarga completa

`app/src/main/java/com/example/ui/LaVouteApp.kt:100` — el `IconButton` con `Icons.Filled.Refresh` de la barra superior, que es **el** botón de sincronizar de la app:

```diff
 IconButton(
-    onClick = { viewModel.triggerSync() },
+    onClick = { viewModel.triggerSync(force = true) },
```

Con `force = true`, `GitRepository.syncData` toma la rama `else`:

```kotlin
val filesToDownload = if (!force && prefs != null) { markdownFiles.filter { ... } } else { markdownFiles }
```

→ se descargan **los 6 `.md` completos (~33,5 MB) en cada pulsación**. Y como `isIncremental = filesToDownload.size < markdownFiles.size` da `6 < 6 = false`, además se hace el `replaceDataSilent` completo.

**Las tres pulsaciones de la Ama descargaron ~100 MB.** La ruta incremental es correcta, pero **el botón que ella usa no puede llegar a ella**.

> **Contexto honesto de por qué pasó:** el #31 §1.1 pedía *"debe existir un sync forzado que ignore ese atajo"* y **no aclaró que el botón normal debía seguir siendo el incremental**. Se convirtió el botón existente en vez de agregar una acción aparte. La instrucción era ambigua; este prompt la desambigua.

**Lo que sí quedó incremental** (no tocar): el auto-sync del arranque (`MainViewModel.kt:822`, `triggerSync()`) y el de después de guardar una nota (`LiteratureScreen.kt:717`).

### 1.2 🔴 El reporte del sync se construye y se descarta

`MainViewModel.kt:993-1000`:

```kotlin
val report = repository.syncData(com.example.BuildConfig.GITHUB_PAT, force = force)
val errors = report.lines().filter { it.startsWith("✗") }.map { it.trim() }
...
// Ocultar aviso de éxito, volver a Idle inmediatamente
_syncState.value = SyncState.Idle
```

Del reporte **solo sobreviven las líneas que empiezan con `✗`**. La línea `"0 de 6 archivos descargados · sin cambios"` que agregó el #31 **empieza con `0`**, así que se descarta. Y `SyncState.Success(val message: String)` está **declarado y nunca usado** (`MainViewModel.kt:20`): el flujo salta directo a `Idle`.

O sea: aunque el botón hubiera sido incremental, el mensaje tampoco se habría visto nunca.

---

## 2. Cambios requeridos

### 2.1 El botón ⟳ vuelve a ser incremental

```kotlin
// app/src/main/java/com/example/ui/LaVouteApp.kt:100
onClick = { viewModel.triggerSync() },   // sin force
```

### 2.2 El sync forzado va al diálogo de Ajustes, que ya existe

En `GlobalSettingsDialog` (`LaVouteApp.kt:339+`, el que agregó el #31 con "Vaciar caché de imágenes"), añadir una segunda acción:

- Botón **"Forzar recarga completa"** → `viewModel.triggerSync(force = true)` y cierra el diálogo.
- Debajo, en texto chico: **"Descarga los ~34 MB de galerías otra vez. Úsalo solo si algo se ve desactualizado."** La Ama tiene que poder decidir informada, no descubrir el costo después.

### 2.3 Instrumentar el sync: archivos, bytes y segundos

Esto es lo que hace el resultado **autoverificable** — hoy no hay forma de saber si el trabajo del #31 sirve.

En `GitRepository.syncData`:

1. Medir la duración con `System.nanoTime()` de punta a punta.
2. Acumular los bytes de markdown efectivamente descargados. El texto ya está en mano: sumar `markdownText.toByteArray().size` por archivo bajado (o el `contentLength()` del `ResponseBody`), en un contador thread-safe — las descargas van en `async` paralelo, así que usar `java.util.concurrent.atomic.AtomicLong`, no un `var`.
3. Construir **una línea resumen como PRIMERA línea del reporte**, con un prefijo estable para poder extraerla:

```
SUMMARY: Sync incremental · 0 de 6 archivos · 0 KB · 1,4 s
SUMMARY: Sync forzado · 6 de 6 archivos · 33,5 MB · 22,1 s
```

Formatear los bytes en KB/MB con un decimal. El prefijo `SUMMARY: ` no se muestra en pantalla: sirve para extraer la línea sin adivinar.

### 2.4 Mostrar el resumen

En `MainViewModel`:

1. Nuevo estado, persistido igual que los que ya existen:
   ```kotlin
   private val _lastSyncSummary = MutableStateFlow(prefs.getString("last_sync_summary", "") ?: "")
   val lastSyncSummary: StateFlow<String> = _lastSyncSummary.asStateFlow()
   ```
2. En `triggerSync`, además del filtro de `✗` que ya existe (**conservarlo**), extraer la línea de resumen y guardarla en el estado y en `prefs` (`"last_sync_summary"`).
3. **Usar `SyncState.Success(message)`**, que hoy está muerto: al terminar un sync **manual**, ponerlo con el resumen; que la UI lo muestre ~4 segundos y vuelva a `Idle`.
   - 🚨 **Solo en el sync manual.** El auto-sync del arranque (`MainViewModel.kt:822`) debe seguir silencioso — para eso existía el comentario *"Ocultar aviso de éxito"*, y esa intención se respeta. Pasar un parámetro (p. ej. `silent: Boolean = false`) o distinguir por el llamador; no mostrar avisos en el arranque.
4. En `DiagnosticCard` (`ui/DiagnosticCard.kt`, que se pinta en `SummaryScreen.kt:396` — pestaña La Flota) y que ya muestra la fecha del último sync y los errores: agregar **el resumen del último sync**, junto a la fecha. Así queda un registro consultable aunque el aviso ya se haya ido.

### 2.5 Versión

`versionCode = 26` · `versionName = "4.17"`.

---

## 3. 🚫 Qué NO hacer

- **No** tocar la lógica incremental de `syncData` (el filtro por `md_sha_<path>`, el `?v=${fileEntry.sha}`, el guardado del sha tras parse exitoso, el `insertLooks/insertPrompts` vs `replaceDataSilent`). **Está correcta** — se verificó que `prefs` está inyectado (`MainViewModel.kt:49`) y que el DAO usa `OnConflictStrategy.REPLACE`.
- **No** convertir el auto-sync del arranque en forzado.
- **No** quitar el filtro de `✗` que alimenta `lastSyncErrors`: se **añade** el resumen, no se reemplaza nada.
- **No** dejar el aviso de éxito permanente ni bloqueante: se auto-oculta.
- **No** tocar `CharacterProfile`, `PoseMatcher` ni el nombrado de poses (#28).
- **No** cambiar versiones de dependencias (#29) ni borrar archivos (#30, aún pendiente).
- **No** agregar librerías nuevas (ni snackbar de terceros: usar `SnackbarHost` de Material3 o el patrón que ya tenga la app).

---

## 4. Criterios de aceptación — la Ama los puede verificar sola

1. Apretar ⟳ **dos veces seguidas** sin cambios en el repo: el aviso de la segunda dice **`Sync incremental · 0 de 6 archivos · 0 KB`** y tarda un par de segundos, no veinte.
2. Ajustes → **"Forzar recarga completa"**: el aviso dice **`Sync forzado · 6 de 6 archivos · ~33 MB`**.
3. Abrir la app de cero: **no aparece ningún aviso de éxito** (el arranque sigue callado), pero el DiagnosticCard de La Flota **sí muestra** el resumen de ese sync.
4. Subir una foto desde la app y apretar ⟳: **0 de 6 archivos** (los `.md` no cambiaron) y la imagen nueva aparece igual.
5. Cambiar un `.md` en GitHub y apretar ⟳: **1 de 6 archivos** y los MB corresponden a ese archivo solo.
6. `grep -n "triggerSync(force = true)" app/src/main/java/com/example/ui/LaVouteApp.kt` → aparece **solo** dentro de `GlobalSettingsDialog`, no en el `IconButton` de la barra.
7. `./gradlew assembleDebug` compila y `./gradlew testDebugUnitTest` pasa, incluidos los 8 `@Test` de `CharacterProfileTest.kt`.
8. La cabecera muestra `v4.17 (26)`.

---

## 5. Entrega esperada (formato obligatorio)

1. **Diff completo por archivo.**
2. **Los dos avisos, transcritos literalmente** tal como salen en pantalla: el del sync incremental sin cambios y el del forzado. Son la evidencia del #31 y de este prompt a la vez.
3. **Log real y literal** de `./gradlew assembleDebug` y `./gradlew testDebugUnitTest`. Si un comando falla o no se puede ejecutar, **decirlo**.
   > Ni el #29 ni el #31 trajeron log de build. Van dos. Si no se puede compilar en el entorno, hay que decirlo una vez y dejar de entregar como si se hubiera compilado.
4. **Sección "NO HECHO"** explícita con cada criterio de §4 no cumplido o no verificado. Si está vacía, escribir "ninguno".
5. **Hash del commit.**
6. **No dejar scripts de trabajo en el repo.** Los commits del #29 y del #31 dejaron `fix_libs.py`, `fix_app.py`, `fix_git_sync2.py`, `fix_settings.py` y `fix_upload_and_coil.py` en la raíz; ya van **113 archivos basura trackeados**. Si se usa un script para editar, va a `/scratch/` y no se commitea.

> ⚠️ **AI Studio corre su propio git "Init":** sus commits llegan a `farid77cl/LV-App` **solo cuando la Ama los pushea**. Pushear y verificar el HEAD real.
