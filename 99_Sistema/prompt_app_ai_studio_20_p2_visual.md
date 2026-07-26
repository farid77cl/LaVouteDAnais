# 📱 Prompt #20 · LV-App 2.0 — PASO 2: Pestaña Visual (Datos + Galería N/7)

> **Requiere P1 verde** (esqueleto navegable, `versionCode 1` · `versionName "1.0"`).
> **Este paso:** llenar la pestaña Visual con datos REALES del repo — PoseMatcher + Galería agrupada N/7. Sin Lightbox ni creador de prompts todavía (eso va en P2.1).
> **Si aterriza roto:** el arreglo va como **Prompt #20.2.x** (patch).

---

## ⚠️ REGLAS
1. Genera SOLO los archivos listados. No toques el esqueleto de P1 salvo cablear `VisualScreen`.
2. Debe COMPILAR y CORRER: la pestaña Visual muestra la galería real.
3. Sin Room todavía (eso es P3): fuente de datos en memoria, leída del repo clonado.

---

```markdown
PASO 2 de LV-App 2.0. Sobre el esqueleto de P1, llena la pestaña VISUAL con datos reales.
Añade dependencias (el catálogo quedó minimal tras el P1.2; agrégalas tú, en versión estable
actual compatible con el Compose BOM 2026.06.01): coil3 (io.coil-kt.coil3: coil-compose +
coil-network-okhttp, para imágenes), org.eclipse.jgit (clonar/pull del repo), kotlinx-coroutines.

## REPO DE DATOS (crítico — no confundir con el repo de código)
La app clona el repo de DATOS donde viven las imágenes y la galería:
    https://github.com/farid77cl/LaVouteDAnais   ← PÚBLICO (clona SIN autenticación)
Las imágenes están en `05_Imagenes/ele/look<N>_.../ele_<N>_<pose>.png` y la galería en
`00_Ele/galeria_outfits.md`. NO clones `farid77cl/LV-App` (código v1, privado, SIN imágenes)
ni `farid77cl/LV-app-2` (el código de ESTA app). Son tres repos distintos.
⚠️ Es un repo grande (miles de PNG): clona shallow (`--depth 1`) y no bloquees la UI.

## OBJETIVO
La pestaña Visual muestra la Galería de Outfits agrupada por look, con indicador N/7 poses
y portada jerárquica, leyendo las imágenes del repositorio GitHub clonado en el dispositivo.

## ARCHIVOS A GENERAR (SOLO ESTOS)
1. data/git/GitRepository.kt
   - Clona `https://github.com/farid77cl/LaVouteDAnais` (shallow) a almacenamiento interno
     de la app; si ya existe, hace `pull`. Expone `localRepoDir: File` y `suspend fun sync()`.
   - Usa JGit. Maneja errores sin crashear (Result/try-catch). Todo fuera del hilo principal.

2. data/PoseMatcher.kt (objeto utilitario central)
   - Poses canónicas: Standing, Back View, Seated, Side Profile, Ditzy, POV, Odalisque.
   - Alias ES/EN → canónica: sentada→Seated, espalda→Back View, perfil→Side Profile,
     frontal/de pie→Standing, acostada→Odalisque.
   - Limpia prefijos (`ele_775_`) y sufijos (`_2`, `_v1`). case-insensitive.
   - `getCanonicalPose(filename): String`, `matches(a,b): Boolean`.

3. domain/model/Look.kt, domain/model/Pose.kt
   - Look(number:Int, batch:String, poses:List<Pose>, coverPath:String?, completeness:Int/*N de 7*/).
   - Pose(canonical:String, imagePath:String).

4. data/LookLocalDataSource.kt
   - Escanea `localRepoDir/05_Imagenes/**` buscando PNG `ele_<N>_<pose>.png`.
   - Agrupa por número de look, mapea cada archivo con PoseMatcher, calcula N/7 (poses canónicas únicas).
   - Portada jerárquica: Standing > Side Profile > Seated > primera disponible.

5. data/LookRepository.kt — `fun looks(): Flow<List<Look>>`, `suspend fun refresh()` (llama GitRepository.sync + reindex).

6. ui/screens/visual/VisualViewModel.kt
   - Estado: loading / lista de looks / filtro de lote (L200–L800) / filtro estado (Materializado/Pendiente).

7. ui/screens/visual/VisualScreen.kt (reemplaza el placeholder)
   - Barra de filtros (lote + estado). Grilla de tarjetas de Outfit:
     miniatura (Coil, portada jerárquica), número de look, badge "N/7".
   - Pull-to-refresh que llama refresh(). Estado vacío y de carga.

8. PoseMatcherTest.kt — tests REALES: alias→canónica, limpieza de sufijos `_2`, case-insensitive.

## CRITERIO DE ÉXITO
Compila · la pestaña Visual clona/lee el repo y pinta la galería real · cada tarjeta muestra
su portada correcta y el badge N/7 correcto · el filtro de lote funciona · pull-to-refresh actualiza.

Entrega SOLO estos 8 puntos. En P2.1: Lightbox + Creador de Prompts.
```

---

## ✅ Cómo verificar antes del P2.1
1. Que la app clone **`farid77cl/LaVouteDAnais`** (público, con `05_Imagenes/`), **no** `LV-App`.
2. Que la Galería Visual **pinte imágenes reales** y no salga vacía (síntoma de repo equivocado).
3. Que el badge **N/7** y la **portada jerárquica** (Standing > Side Profile > Seated) sean correctos.
4. Que `PoseMatcherTest` pase con tests **reales** (alias→canónica, sufijo `_2`, case-insensitive).
5. El catálogo `libs.versions.toml` **creció** solo con coil3 + jgit + coroutines (sin re-meter el kitchen-sink que el P1.2 purgó).
6. **Pushear** desde AI Studio (sus commits no llegan a GitHub hasta que la Ama pushea).
7. Verde → **P2.1 (Lightbox + Creador de Prompts)**.

> ⚠️ **TRES repos, no los confundas:**
> · `farid77cl/LV-app-2` = código de ESTA app (2.0).
> · `farid77cl/LaVouteDAnais` = datos/imágenes (**público** a propósito, para clonar sin auth).
> · `farid77cl/LV-App` = código v1 (privado, era v4.12 — NO tocar).
