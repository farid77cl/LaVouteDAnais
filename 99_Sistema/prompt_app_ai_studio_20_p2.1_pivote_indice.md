# 🔄 Prompt #20 · LV-App 2.0 — PASO 2.1: Pivote a Índice + URL (reemplaza el P2)

> **Replanteo de raíz, 27/07/2026.** No es un parche del P2: es un **cambio de arquitectura de datos** decidido por la Ama tras el tercer timeout.
> **Supersede:** `prompt_app_ai_studio_20_p2.1_parche_compilacion.md` (aquel parchaba el diseño equivocado).

---

## 🩺 Por qué se cambia el diseño (medido, no opinado)

El P2 hacía que la app **clonara con JGit el repo de datos completo**. Se midió sobre `LaVouteDAnais`:

| | |
|---|---|
| PNG trackeados | **5.242** |
| Lo que baja un `clone --depth 1` | **~1,56 GB** |
| Almacenamiento ocupado en el teléfono | **~1,56 GB** |
| Lo que la app **necesita** para pintar la galería entera | **236 KB** (`app_index.json`) |
| Costo de una imagen concreta, bajo demanda | **644 KB · 0,26 s** (verificado: `HTTP 200` sobre raw público) |

`setDepth(1)` recorta el **historial**, no el **contenido**. La app bajaba 1,5 GB antes de mostrar la primera foto, y volvía a pullear en cada sync.

**Decisión:** fuera git del teléfono. La app baja **un índice** y carga **cada imagen por URL cuando la miras**, con la caché de Coil. Esto además elimina JGit (dependencia pesada) — que es justo la que producía `Unresolved reference 'eclipse'` y buena parte del peso de build que hacía timeout a AI Studio.

## 📦 El índice YA EXISTE — no lo generes tú

Ya está commiteado en el repo de datos, generado por
`99_Sistema/scripts/visual/generar_app_index.py`:

```
https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/99_Sistema/app_index.json
```

**236 KB · 733 looks · 4.190 imágenes · 465 looks completos 7/7.** Formato (claves cortas a propósito, para que pese poco):

```json
{
  "v": 1,
  "generado": "2026-07-27",
  "raw": "https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/",
  "poses": ["standing","side_profile","seated","back_view","ditzy","pov","odalisque"],
  "total_looks": 733,
  "total_imagenes": 4190,
  "looks": [
    {
      "n": 696,
      "t": "Champagne Pink Liquid Escort",
      "f": "01/07/2026",
      "d": "05_Imagenes/ele/look696_champagne_pink_liquid_escort/",
      "p": { "standing": "ele_696_standing.png", "side_profile": "ele_696_side_profile.png" },
      "c": "standing",
      "np": 7,
      "x": 0
    }
  ]
}
```

| Clave | Significado |
|---|---|
| `n` | número de look · `t` título (puede ser `null`) · `f` fecha |
| `d` | carpeta, relativa a `raw` |
| `p` | mapa `pose canónica → nombre de archivo`. **Ya viene normalizado** |
| `c` | pose de portada, ya resuelta jerárquicamente (Standing > Side Profile > Seated) |
| `np` | poses canónicas presentes (el **N** de "N/7") · `x` archivos extra sin pose |

**URL de cualquier imagen = `raw` + `d` + `p[pose]`.** Nada más. Concatenación de strings.

> ⚠️ **El PoseMatcher ya no va en la app.** La normalización de poses (alias español, sufijos `_2`, prefijos `ele_675_`) la hace el script en Python del lado del repo. La app **consume** poses ya canónicas. Un emparejador menos que mantener en Kotlin.

---

## 📋 PROMPT PARA PEGAR EN AI STUDIO

```markdown
PASO 2.1 de LV-App 2.0: PIVOTE DE ARQUITECTURA DE DATOS. Reemplaza el enfoque del
P2. NO agregues pestañas nuevas, NO toques el tema por personaje ni la navegación.

Repo de código: farid77cl/LV-app-2 · paquete com.lavoute.app · estado: commit 59a32b6
(el P2 está pusheado pero NUNCA compiló — tu último BUILD SUCCESSFUL, build_assemble_2.log,
es anterior a las dependencias jgit/coil y no las menciona).

=====================================================================
## 0. ANTES DE COMPILAR NADA — lee esto, es la causa de los timeouts
=====================================================================
Los timeouts NO fueron de red. Tu propio output.txt dice:
    "Starting a Gradle Daemon, 5 busy Daemons could not be reused"  +  "Killed"
Eso es el OOM killer: 5 daemons acumulados de tus reintentos, a -Xmx4g cada uno.
Se arregla en el punto 4. Aplica los puntos 1-4 COMPLETOS y compila UNA sola vez.
Prohibido compilar "para ir viendo": así se acumularon los daemons.

=====================================================================
## 1. ELIMINA JGIT Y TODO EL CLONADO (esto es el corazón del paso)
=====================================================================
BORRA el archivo app/src/main/java/com/lavoute/app/data/git/GitRepository.kt
y su paquete. La app NO clona ningún repositorio.

Quita del catálogo y de app/build.gradle.kts:
  - org.eclipse.jgit  (la entrada `jgit` en [versions] y en [libraries], y la
    línea implementation(libs.jgit))

Motivo: clonar el repo de datos son ~1,56 GB en el teléfono. Se reemplaza por un
índice de 236 KB + carga de imágenes por URL.

BORRA también data/PoseMatcher.kt y PoseMatcherTest.kt: la normalización de poses
ya viene hecha en el índice. No la dupliques en Kotlin.

=====================================================================
## 2. NUEVA FUENTE DE DATOS: el índice remoto
=====================================================================
Genera SOLO estos archivos:

a) data/remote/IndexApi.kt
   - Descarga con OkHttp (ya tienes coil-network-okhttp, que trae OkHttp):
     https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/99_Sistema/app_index.json
   - Parsea con org.json (viene en Android, CERO dependencias nuevas) o
     kotlinx-serialization si prefieres. NO agregues Moshi ni Gson.
   - Devuelve Result<AppIndex>. Todo en Dispatchers.IO. Sin crashear en error.

b) data/local/IndexCache.kt
   - Guarda el JSON crudo en context.filesDir como app_index.json.
   - Al abrir: si hay caché, se muestra al instante y se refresca en segundo plano.
     La app debe funcionar SIN red si ya sincronizó una vez.

c) domain/model/Look.kt y domain/model/Pose.kt
   Look(n:Int, titulo:String?, fecha:String?, dir:String,
        poses:Map<String,String>, portada:String, nPoses:Int)
   Pose(canonical:String, url:String)
   - Añade `fun Look.urlDe(pose:String, raw:String): String = raw + dir + poses[pose]`
   - `fun Look.urlPortada(raw:String) = urlDe(portada, raw)`

d) data/LookRepository.kt
   - fun looks(): Flow<List<Look>>   ·   suspend fun refresh(): Result<Unit>
   - refresh() baja el índice, lo cachea y emite. Nada de git.

=====================================================================
## 3. PESTAÑA VISUAL (arregla lo que ya escribiste)
=====================================================================
En ui/screens/visual/VisualScreen.kt:

  LÍNEA 14 — ESTE ES EL ERROR QUE TE TIRÓ "Unresolved reference 'coil'":
      import coil.compose.AsyncImage        ← paquete de Coil 2, MAL
      import coil3.compose.AsyncImage       ← Coil 3, que es lo que declaraste
  Revisa TODO el proyecto: no debe quedar ningún import `coil.*` (todos `coil3.*`).

  ICONOS: build_assemble_4.log también reporta Unresolved reference 'Icons'. Estás
  declarando SIN versión, confiando en el BOM:
      implementation("androidx.compose.material:material-icons-core")
      implementation("androidx.compose.material:material-icons-extended")
  Los artefactos material-icons-* fueron deprecados y sacados del Compose BOM en
  versiones recientes, y tú estás en composeBom 2026.06.01. Comprueba si el BOM
  todavía los provee; si NO, quítalos y usa los iconos que sí trae Material 3.
  No dejes dependencias sin versión que el BOM no maneje. Reporta qué encontraste.

  CONTENIDO: grilla (LazyVerticalGrid) de tarjetas de look:
    - miniatura con AsyncImage(model = look.urlPortada(raw))
    - número de look + título
    - badge "N/7" usando look.nPoses
    - filtro por tramo (L1-L100, L101-L200, … L701-L800) y por estado (7/7 vs parcial)
    - pull-to-refresh que llama repository.refresh()
    - estado de carga, estado vacío y estado de error CON mensaje (no pantalla en blanco)

  Coil ya cachea en disco y memoria: no precargues nada, no bajes imágenes que no
  se ven. Es una lista perezosa y así debe quedar.

=====================================================================
## 4. BUILD LIVIANO (para que AI Studio deje de morirse)
=====================================================================
gradle.properties:
    org.gradle.jvmargs=-Xmx2g          (estaba -Xmx4g)
    org.gradle.parallel=false          (la app tiene UN módulo: paralelizar solo gasta RAM)
    org.gradle.workers.max=2
gradle/wrapper/gradle-wrapper.properties:
    networkTimeout=120000              (estaba 10000 = 10 s, para bajar ~130 MB)

NO cambies la versión de Gradle ni de AGP. Si el contenedor ya tiene la
distribución en caché, cambiarla te obliga a bajar otros ~130 MB y es justo lo
que te hizo timeout la última vez.

CÓMO COMPILAR EN ESTE ENTORNO (respétalo al pie de la letra):
  1. ./gradlew --stop                          ← mata los daemons acumulados
  2. ./gradlew --no-daemon :app:compileDebugKotlin
       Usa ESTE para iterar: es mucho más barato que assembleDebug y detecta
       todos los "Unresolved reference". No corras assembleDebug para ver si
       compila el Kotlin.
  3. Solo cuando el paso 2 esté verde:
       ./gradlew --no-daemon :app:assembleDebug
       ./gradlew --no-daemon :app:testDebugUnitTest

=====================================================================
## 5. LIMPIEZA DEL REPO
=====================================================================
BORRA del repo: update_libs.sh, update_versions.sh, build_assemble*.log,
build_test*.log, build_done.txt, output.txt.
Agrega al .gitignore: *.log y build_done.txt (hoy solo ignora `build.log`,
por eso se colaron 13 logs).

update_libs.sh es peligroso: hace `>> gradle/libs.versions.toml` (append al FINAL
del archivo, y el final es la sección [plugins]). Eso metió jgit dentro de
[plugins] y produjo el error "'jgit' is not a valid plugin notation". Si se
vuelve a correr, rompe el catálogo otra vez. El catálogo se edita a mano.

=====================================================================
## CRITERIO DE ÉXITO
=====================================================================
- ./gradlew --no-daemon :app:compileDebugKotlin  → BUILD SUCCESSFUL
- ./gradlew --no-daemon :app:assembleDebug       → BUILD SUCCESSFUL
- ./gradlew --no-daemon :app:testDebugUnitTest   → BUILD SUCCESSFUL
- La pestaña Visual muestra la grilla de looks con portada y badge N/7 reales,
  bajando SOLO el índice + las miniaturas visibles. Sin clonar nada.
- Segunda apertura sin red: la galería se ve igual (caché del índice + de Coil).
- No queda ningún `import coil.*`, ni JGit, ni PoseMatcher, ni logs commiteados.

=====================================================================
## AL TERMINAR, REPORTA (texto, fuera del código)
=====================================================================
- Salida LITERAL de las últimas 15 líneas de compileDebugKotlin, assembleDebug y
  testDebugUnitTest. No escribas "Build succeeded": pega las líneas reales.
- Qué pasó con material-icons (¿el BOM los provee o los reemplazaste?).
- Confirmación de que borraste JGit, PoseMatcher, los 2 scripts y los logs.
- Cuánto pesa el APK debug resultante.
- Si NO pudiste con algún punto, DILO explícitamente. No lo omitas.
```

---

## ✅ Cómo verificar antes del paso siguiente
1. **Salida literal** de los tres gradlew — no un resumen.
2. `grep -r "import coil\." app/src` → **vacío**.
3. `grep -ri "jgit" .` → **vacío** (ni catálogo, ni build.gradle.kts, ni código).
4. No existen `update_libs.sh`, `update_versions.sh` ni `build_*.log`.
5. En el teléfono: la app abre rápido y la galería se puebla sin descargar gigas.
6. **Pushear** desde AI Studio (sus commits no llegan a GitHub hasta que la Ama pushea).

## 🔁 Del lado del repo de datos (tarea de Ele, no de AI Studio)
`app_index.json` se **regenera y commitea** cada vez que entran imágenes nuevas:

```bash
python 99_Sistema/scripts/visual/generar_app_index.py
```

Va incorporado al cierre de sesión, junto a `update_galleries.py`. Si el índice
no se regenera, la app no ve los looks nuevos — es el único acoplamiento que
introduce esta arquitectura, y es barato.
