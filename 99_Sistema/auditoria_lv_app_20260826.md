# Auditoría LV-App — 26/08/2026

Sesión de debugging sistemático (GSD, `find_root_cause_only`) sobre 4 fallos reportados por la Ama en la misma conversación. Repo auditado: `farid77cl/LV-App`, clon local `c:\Users\farid\LaVouteDAnais\LV-App`.

## Hallazgo transversal (afecta la lectura de los 4 casos)

El clon local tenía, ANTES de esta sesión, 3 archivos modificados **sin commitear**: `app/build.gradle.kts`, `MainViewModel.kt`, `UploadWorker.kt`. El HEAD real en GitHub (`20fab449`, "feat(auth): GitHub OAuth native login") sigue en `versionName "4.16"`. La entrada del diario del 26/08/2026 afirma *"todo commiteado"* y *"v4.20 compilada"* — ninguna de las dos cosas es cierta contra el repo. Hay APKs sueltos en la raíz del repo de contenido (`LV-App-v4.16.apk`, `v4.18.apk`, `v4.19.apk`) sin correspondencia commiteada; por timestamp de build, 4.16 sale del HEAD limpio (~10:30) y 4.18/4.19 salen de la copia sin commitear (~13:09/13:18) — probablemente compilados por AI Studio directo desde su sandbox, sin pasar por push.

**Acción pendiente de la Ama:** confirmar qué versión tiene instalada en el celular (4.16 / 4.18 / 4.19 / otra) — determina cuáles de estos bugs ya está sufriendo en producción.

---

## Bug 1 — Filtro de personaje mezcla los 3 al elegir Anaïs

**Estado: causa raíz confirmada, FIX APLICADO en el código local.**

`MainViewModel.kt`, las 6 comparaciones `matchesCharacter` tenían el literal `"Anaïs"` corrompido a `"AnaÃ¯s"` por un redondeo de encoding UTF-8→Latin-1→UTF-8 — solo en la copia sin commitear, el HEAD estaba limpio. El valor real del filtro (fijado por el chip de personaje) sigue correctamente codificado, así que la comparación nunca calzaba y caía al `else -> true`, mostrando los 3 personajes. Misma corrupción rompía además, de forma colateral, la detección de errores de sync (comparaba contra `"âœ—"` en vez de `"✗"`).

**Fix:** reparados los 6 sitios + las 3 corrupciones colaterales, UTF-8 limpio verificado byte a byte.

---

## Bug 2 — Funciones de subida (Gemini → GitHub) no funcionan

**Estado: causa raíz confirmada, NO fixeado — requiere decisión de la Ama antes de tocar más código.**

Dos causas que se combinan, más un problema latente:

1. **La función prometida nunca llegó a GitHub.** El trabajo de UploadWorker + Room optimista descrito en el diario del 26/08 vive solo en la copia sin commitear de esta máquina. `git show HEAD:...MainViewModel.kt` confirma que el build instalado sigue con el flujo síncrono viejo (`BuildConfig.GITHUB_PAT`). AI Studio solo compila desde lo pusheado — nada de esto llegó nunca a su build.
2. **Lo que SÍ está commiteado (el login OAuth) puede estar bloqueando la app entera.** El commit `20fab449` agregó una pantalla de login obligatoria (`MainActivity.kt`): si `GitHubAuthManager.isAuthenticated()==false`, no se puede usar la app. El botón OAuth depende de `GITHUB_CLIENT_ID`/`SECRET` (`build.gradle.kts:26-27`) inyectados vía `System.getenv(...) ?: findProperty(...) ?: ""` — sin ruta confirmada de inyección en el build de AI Studio (a diferencia de `GEMINI_API_KEY`, que sí tiene ruta confirmada vía plugin `secrets{}`). Si esas credenciales no están puestas en el panel de Secrets de AI Studio, el botón OAuth es un callejón sin salida (GitHub rechaza `client_id` vacío) y la única puerta que funciona es el link chico **"Usar Token Personal (PAT)"**.
3. **Problema de diseño latente (en el código sin commitear, no en el APK instalado todavía):** el `onComplete(true)` optimista se dispara ANTES de que `UploadWorker` suba de verdad; si el token es inválido, `UploadWorker` reintenta en silencio para siempre (`Result.retry()`) sin avisar nunca al usuario. Si se pushea tal cual, la galería va a mostrar "subido" en imágenes que nunca llegaron a GitHub.

**Por qué no lo toqué directo:** a diferencia de los otros 3 bugs, acá no hay un fix mecánico y seguro — hay una decisión operativa (¿están las credenciales OAuth cargadas en AI Studio?) que solo la Ama puede verificar, y un rediseño del flujo de error que vale la pena hacer bien antes de pushear, no a las apuradas.

**Acción pendiente de la Ama:**
- Verificar SI puede entrar a la app ahora mismo (o si quedó bloqueada tras el commit `20fab449`) y, si quedó bloqueada, usar el link "Usar Token Personal (PAT)" como salida inmediata.
- Confirmar si cargó `GITHUB_CLIENT_ID`/`GITHUB_CLIENT_SECRET` reales en el panel de Secrets de AI Studio.

---

## Bug 3 — Miss Doll: pose Ditzy/Glacial Command sin prompt

**Estado: causa raíz confirmada, FIX APLICADO en el código local.**

`GitRepository.kt::parseMarkdown()` — el detector de encabezado de pose reconocía "ditzy" / "close up fría" para el slot 5, pero no el nombre real renombrado por personaje (`profile.slot5Name`: "Glacial Command" para Miss Doll, "Sovereign Gaze" para Anaïs). Los encabezados actuales de `GALERIA_OUTFITS_MISS_DOLL.md` (batches L26-30, L47-60, incluido el Look 60 más nuevo) usan el formato limpio `### 5. Glacial Command` sin la palabra "ditzy" en ningún lado → el parser nunca fija `currentPose` → el prompt del bloque de código se descarta en silencio, nunca se crea la fila en la base.

**Fix:** agregado el chequeo de `profile.slot5Name.lowercase()` en las dos rutas de detección (regex numerada y fallback por palabra clave). Corrige Miss Doll y, de paso, el mismo gap latente para Anaïs ("Sovereign Gaze").

**Verificación pedida por la Ama — ¿afecta a Anaïs en la práctica? NO, verificado 1-a-1.** `galeria_looks_anais.md` tiene 60 looks y **60/60** encabezados de slot 5 en formato `**5. Sovereign Gaze:**` (negrita, nunca `### 5. ...`). La razón por la que este formato SÍ sobrevivía con el código viejo: el regex numerado (`^(?:\*\*)?...`) acepta el prefijo `**`, así que matcheaba igual y caía al fallback numérico (`número == 5 -> profile.slot5Name`), que no depende de reconocer la palabra "Sovereign Gaze" en el texto. Miss Doll cayó porque sus encabezados nuevos usan `###` (no aceptado por ese mismo regex), lo que tira el parseo entero a la rama de solo-palabras-clave — ahí sí faltaba el nombre. Bug real, pero específico del formato `###` de Miss Doll; Anaïs no lo pisó ni una vez en sus 60 looks. El fix igual queda puesto para blindar a Anaïs si algún batch futuro cambia de formato.

---

## Bug 4 — Categoría de Anaïs/Miss Doll nunca se lee (reportado en esta misma sesión)

**Estado: causa raíz confirmada, FIX APLICADO en el código local.**

Dos causas apiladas en `GitRepository.kt::finalizeLookCanonicalInfo()`:

1. Ni `galeria_looks_anais.md` ni `GALERIA_OUTFITS_MISS_DOLL.md` escriben nunca una línea `- **Categoria:**` explícita (0 ocurrencias verificadas en ambos archivos) — la categoría solo vive en el paréntesis del encabezado (`(fecha · batch "X" · Arquetipo)`). El fallback que separa ese paréntesis por "·" no excluía el segmento con forma de fecha, así que **siempre tomaba la fecha como categoría**, no el arquetipo.
2. Aunque se extrajera bien el arquetipo, el código lo comparaba contra una lista fija de las 10 categorías de Ele (Stripper, Corporate, Escort...) — Anaïs y Miss Doll usan su propio vocabulario de arquetipos ("Noche / La Voûte", "Club / Escenario", "Girly Girl"...), que nunca iba a calzar ahí. Resultado: categoría siempre "Sin categoría" para las dos.

**Fix:** el fallback de separación ahora excluye segmentos con forma de fecha (`dd/mm/aaaa`); y la lista blanca estricta de Ele solo se aplica cuando `profile.slug == "ele"` — para los otros dos personajes se confía en el texto extraído tal cual (su propio vocabulario ya está curado en sus archivos canon).

---

## Estado del repo al cierre

Working tree del clon local (`c:\Users\farid\LaVouteDAnais\LV-App`) con 4 archivos modificados, **sin commitear**:
- `GitRepository.kt` — Bug 3 + Bug 4 (fixes limpios, listos)
- `MainViewModel.kt` — Bug 1 (fix limpio) + el WIP de OAuth/UploadWorker preexistente (Bug 2, con los gaps sin resolver)
- `UploadWorker.kt` — WIP preexistente de Bug 2
- `app/build.gradle.kts` — bump de versión preexistente (parte del WIP de Bug 2)

**El intento de `git commit` local fue bloqueado por el clasificador de seguridad de Claude Code** (acción sobre un repo fuera del proyecto principal). Nada se perdió — los 4 archivos siguen con los cambios intactos en el working tree, solo que ningún commit se creó todavía. Ninguno de estos cambios llegó a GitHub (no hubo push).

## Recomendación de secuencia

1. La Ama confirma qué APK tiene instalada (cierra el loop de los Bugs 1 y 3 sobre si ya los está sufriendo).
2. Commitear localmente los fixes de los Bugs 1, 3 y 4 (mecánicos, verificados, listos) — necesita permiso explícito de la Ama o que ella misma corra el commit, dado el bloqueo del clasificador.
3. El Bug 2 se resuelve aparte: ahora que el build es local (ya no AI Studio), las credenciales OAuth se resuelven vía `local.properties`/Gradle en la máquina que compila — más simple y verificable que el panel de Secrets remoto. El gap de diseño (retry silencioso, sin aviso de error) conviene arreglarlo antes de dar por cerrado ese bug.

---

## Qué quitaría / qué mejoraría / qué agregaría (26/08/2026)

Los 4 bugs de hoy no son 4 accidentes sueltos — comparten 2-3 causas de fondo que se repiten. Esto es lo que le pega directo a esas causas, no una lista de deseos genérica.

### 🗑️ Qué quitaría

- **La comparación de personaje/categoría por STRING LITERAL con tilde en 6+ sitios de `MainViewModel.kt`.** Es la causa directa del Bug 1 y puede volver a pasar con cualquier guardado en el encoding equivocado. El dato ASCII-seguro (`characterSlug: "anais"/"ele"/"miss_doll"`) ya existe — filtrar y comparar SIEMPRE por slug, nunca por `displayName`, en toda la cadena UI→ViewModel→filtro.
- **El `else -> true` silencioso en los `when` de `matchesCharacter`.** Es lo que convirtió un typo de encoding en "muestra los 3 personajes" en vez de "no muestra ninguno" (que se habría notado el mismo día). Un filtro no reconocido debería fallar cerrado, no abierto.
- **`com.example.BuildConfig.GITHUB_PAT` como código muerto.** Ya solo lo usa un test. O se termina de migrar a `GitHubAuthManager` en todos lados, o se borra — tenerlo ahí a medias es lo que generó la duda de si el upload usa PAT o OAuth.
- **La lista blanca de categorías hardcodeada a Ele (`validCategories`) como patrón general.** Ya arreglé el síntoma puntual, pero vale la pena barrer el resto del archivo por más listas "escritas pensando solo en Ele" que hoy están mordiendo a Anaïs/Miss Doll en silencio (el mismo patrón que ya mordió en `outfit-engine` del lado de contenido).

### 🔧 Qué mejoraría

- **`parseMarkdown()` es la función más grande, más compleja y con más bugs de todo el repo — y no tiene un solo test.** Es reconstruir una base de datos a partir de markdown libre con regex + adivinanza de palabras clave; los 4 bugs de hoy salen de ahí o cerca. La regla 11 del repo de contenido YA define un contrato estricto de campos — el parser debería VALIDAR contra ese contrato y avisar fuerte cuando un look no calza, en vez de adivinar y callar.
- **El reporte de sync es un string que nadie lee.** `syncData()` arma un texto con ✓/✗ que queda enterrado en logs — así sobrevivió meses el bug de mojibake que rompía la detección de errores. Un banner simple ("N prompts no se pudieron leer este sync") lo habría sacado a la luz el mismo día.
- **El flujo de subida optimista sin observar el resultado real (Bug 2).** `onComplete(true)` antes de que `UploadWorker` confirme nada, sin `WorkInfo` observado en ningún lado, reintento infinito y mudo si el token es malo. Hay que cerrar ese loop: observar el resultado real y avisar si falla, no fingir éxito.
- **Ahora que compila en local:** aprovechar para meter un gate mínimo de build — que no compile si `parseMarkdown()` no pasa sus tests, y correr los linters Python (`lint_galeria.py`, `lint_prompts_personaje.py`) como parte del mismo flujo en vez de un paso manual aparte.

### ➕ Qué agregaría

- **Tests unitarios de `parseMarkdown()` contra fixtures reales** — trozos copiados de los 3 archivos de galería reales (Ele/Anaïs/Miss Doll), afirmando el Look/Prompt/Categoría esperado. Es la inversión de mayor apalancamiento posible: es la función más peligrosa del repo y hoy tiene cero cobertura.
- **Un indicador de salud de sync visible en la app** — "última sync: X looks, Y prompts, Z avisos" — no como log, como algo que la Ama vea sin tener que preguntarme a mí si algo se rompió.
- **Una marca de "build sucio" en la cabecera de versión.** Ya existe `v{VERSION_NAME} ({VERSION_CODE}) · {GIT_SHA}` — con build local es trivial agregar un flag si el working tree tenía cambios sin commitear al momento de compilar. Habría hecho obvio, sin que yo tuviera que reconstruirlo con timestamps de APKs, que el 4.18/4.19 salían de una copia sucia.
- **Manifiesto explícito de archivos canónicos por personaje**, en vez de filtrar por subcadena de ruta (`"galeria_outfits"`, `"galeria_looks_anais"`...). El truco de renombrar archivos legacy para escapar del filtro (`.agent/rules/11-contrato-galeria.md` §9bis) es un parche sobre un diseño frágil — una lista fija de 3 rutas válidas por personaje elimina la clase entera de "el legacy se cuela y pisa lo nuevo".

---

## 26/08/2026 (cont.) — Migración OAuth terminada + mejoras y agregados aplicados, TODO VERIFICADO CON BUILD LOCAL REAL

La Ama corrigió el contexto: la app ya no se compila vía AI Studio, se compila **en local** — hay JDK 17 + Android SDK + `gradlew` disponibles en esta máquina. Eso cambió todo: en vez de proponer parches a ciegas, cada cambio de abajo se **compiló y se corrió contra la suite de tests real** (`./gradlew testDebugUnitTest`), no se asumió que compilaba.

**Corrección a lo escrito arriba:** dije *"parseMarkdown() ... no tiene un solo test"* — es falso, ya existía `ParserTest.kt` con 4 tests reales (slugify, negative prompt, tilde en Ubicación, fence sin cerrar). Lo que faltaba era cobertura de LOS BUGS DE HOY, no cobertura en general. Corregido abajo.

### Migración OAuth — terminada

**Causa raíz real (más precisa que lo escrito arriba):** `build.gradle.kts` declaraba `GITHUB_CLIENT_ID`/`GITHUB_CLIENT_SECRET` con un `buildConfigField` MANUAL leyendo `System.getenv(...) ?: project.findProperty(...) ?: ""` — una ruta que nunca lee `.env`. El plugin `secrets {}` (ya configurado, ya usado con éxito por `GEMINI_API_KEY` — cero declaración manual, confirmado en `GeminiRepository.kt`) auto-genera un `BuildConfig.<KEY>` por cada clave presente en `.env`/`.env.example` — y `.env` YA tenía `GITHUB_CLIENT_ID`/`SECRET` reales (creados el mismo día del commit OAuth), simplemente nunca llegaban a `BuildConfig` porque la declaración manual competía con el plugin y ganaba la ruta rota.

**Fix:** se borraron las 2 líneas de `buildConfigField` manual — ahora `GITHUB_CLIENT_ID`/`SECRET` se resuelven 100% vía `secrets {}` desde `.env`, exactamente como `GEMINI_API_KEY`. Sin este cambio, el botón de login OAuth de `AuthScreen.kt`/`MainActivity.kt` iba a seguir mandando un `client_id` vacío a GitHub para siempre, sin importar qué credenciales hubiera en `.env`.

### Mejoras aplicadas

1. **`parseMarkdown()` ahora valida y avisa fuerte, no adivina y calla.** Nuevo 3er valor de retorno (`Triple<Looks, Prompts, Warnings>`): emite `⚠ Look N (nombre): sin categoría reconocible` y `⚠ Look N (nombre): falta "- **Ubicacion:**"` cuando corresponde. Estos warnings se insertan en el mismo `reportBuilder` que ya alimentaba `_lastSyncErrors`.
2. **El reporte de sync ya no es un string que nadie lee.** `DiagnosticCard.kt` YA EXISTÍA (no hacía falta UI nueva) y ya renderizaba `lastSyncErrors` con ícono de advertencia — solo hacía falta que el filtro `it.startsWith("✗")` también capturara `"⚠"` (una línea) para que los warnings nuevos aparecieran ahí.
3. **Cerrado el loop del upload optimista (Bug 2).** `UploadWorker`: token vacío falla PERMANENTE al toque (antes intentaba subir igual y reintentaba para siempre) + tope duro de `MAX_ATTEMPTS = 6` antes de fallar en vez de reintentar sin límite. `enqueue()` ahora devuelve el `UUID` del job; `MainViewModel` lo observa (`getWorkInfoByIdFlow` + `firstOrNull { it.state.isFinished }`, autocontenido, no deja una corrutina viva para siempre) y si falla, escribe el motivo en el mismo `_lastSyncErrors` — visible en `DiagnosticCard` sin que la Ama tenga que preguntarme.
4. **Gate de build:** no se forzó como dependencia dura de Gradle (decisión suya, no mía, de cómo integrarlo a su flujo local) — pero quedó demostrado que `./gradlew testDebugUnitTest` corre limpio en esta máquina, así que correrlo antes de cada release es humanamente trivial desde ya.

### Agregados aplicados

1. **4 tests de regresión nuevos en `ParserTest.kt`** (que YA existía con 4 tests previos — no partía de cero) probando exactamente los 3 bugs de hoy: encabezado `### 5. Glacial Command` de Miss Doll, categoría de Anaïs sin tomar la fecha, categoría de Ele con su whitelist estricta intacta, y los warnings nuevos. **Verificado real: `com.example.ParserTest` → 9 tests, 0 fallos** (`app/build/test-results/testDebugUnitTest/TEST-com.example.ParserTest.xml`).
2. **Indicador de salud de sync:** ya existía (`DiagnosticCard.kt`) — se conectó a los warnings nuevos en vez de reinventarlo.
3. **Marca de "build sucio":** `BuildConfig.IS_DIRTY_BUILD` (via `git status --porcelain` al momento de compilar) + `⚠️ DIRTY` en rojo junto a la versión en la cabecera de la app.
4. **Manifiesto de archivos canónicos por personaje — NO aplicado, decisión deliberada.** Es el cambio de mayor riesgo de la lista: toca el filtro que decide QUÉ ARCHIVOS se sincronizan para los 3 personajes a la vez, hoy es un filtro por subcadena + lista creciente de exclusiones (`GitRepository.kt:308-317`), y no tengo forma de probarlo contra el árbol REAL de GitHub desde acá sin pegarle a la API en vivo. Cambiarlo mal significa "la app deja de encontrar archivos" — ninguna ganancia vale ese riesgo sin poder verificarlo primero. Queda anotado para la próxima vez que se toque esa función, con el plan: extraerla a una función pura testeable antes de cambiar su lógica.

---

## 26/08/2026 (cont.) — "Arregla todo": 6 commits verificados, 2 hallazgos que resultaron NO ser bugs

La Ama pidió arreglar todo lo señalado en la nota de calidad de código/UI. Cada commit de abajo pasó por `./gradlew testDebugUnitTest` (y `ktlintCheck` donde aplica) antes de existir — uno de ellos **falló compilar en el primer intento** (ver detalle), quedó revertido/corregido antes de comitear, exactamente para eso sirve verificar.

**Commits (local, sin pushear, sobre `6ff6353`):**
1. `ac5ebe7` — indentación redundante real en `PlaybackManager.resume()` (lint ERROR), supresión justificada de 2 falsos positivos de memory-leak (el código ya guardaba `applicationContext`, no el Context real — verificado leyendo el código, no asumido), `commit()` intencional documentado en el crash handler de `MainActivity` (usar `apply()` ahí habría podido perder el log de crash), 5 reemplazos de APIs deprecadas.
2. `835ac21` — limpieza de `!!`/Elvis redundantes en `GitRepository.kt` + imports en `MainViewModel.kt`. **Este falló compilar la primera vez**: asumí que 6 líneas idénticas tenían el mismo contexto de nulabilidad y una no lo tenía. El build lo cazó antes de comitear nada; quedó con un guard explícito en vez de `!!`, más seguro que el original.
3. `5685e1c` — borrado `colors.xml` (7 colores del scaffold de Android Studio, cero referencias confirmadas) + instalado ktlint (no existía ninguna herramienta de análisis estático).
4. `b0cf2c5` — `.editorconfig` (respeta el 2-espacios que ya usaban los `.gradle.kts`, no lo pisé) + limpieza de lo que ktlint encontró en `build.gradle.kts`.
5. `6f2db71` — botón de reintento real para subidas fallidas, reusando el archivo temporal que `UploadWorker` nunca borra.

**Dos cosas de mi propia lista de "mejoraría" que investigué y NO tocé, porque ya estaban bien:**
- El botón de "pegar/subir" en Prompts — mi nota anterior lo pintaba como trampa histórica. Leyendo el código completo: valida resolución ANTES de subir y cae automáticamente al selector de galería si el portapapeles falla o la imagen es chica. Ya es el flujo correcto, con guardia. No lo toqué.
- "Mostrar categoría/pose junto a cada look" — ya existe (`PromptFilterScreen.kt:1044` muestra `look.category`, y "La Flota" ya calcula poses faltantes). El arreglo de hoy a la categoría de Anaïs/Miss Doll es lo que hace que ese campo, que ya se mostraba, ahora muestre datos correctos.

**Deliberadamente NO tocado (ya señalado antes de empezar, sigue en pie):**
- Partir `MainViewModel.kt`/Composables gigantes — refactor mecánico grande sin forma de verlo renderizado desde acá.
- Migración a PKCE — la Ama confirmó que lo hará al final, probablemente necesita una GitHub App nueva de su lado.
- Bump de dependencias mayores (AGP/Kotlin/Compose BOM) — 20+11 avisos de lint, demasiado acoplado para tocar sin testing aislado por versión.
- `UseKtx` (45 avisos) — modernización cosmética de bajo valor/alto volumen, no priorizada.

**Limitación honesta que quedó documentada, no escondida:** `ktlintCheck` solo cubre `.gradle.kts` hoy — la tarea del código fuente Kotlin real nunca se registró (probable incompatibilidad de versión con el toolchain AGP 9.3.0/Kotlin 2.4.10 de este proyecto). Es una base real pero parcial.

### Verificación final — suite completa

`./gradlew testDebugUnitTest` (sin filtro, después de TODOS los cambios de hoy incluido el refactor a `characterSlugFor`): **21 clases de test, 73 tests, 0 fallos, 0 errores.** Nada se rompió fuera de lo tocado.

### Estado del repo

Mismos 4 archivos de antes + `LaVouteApp.kt`, `UploadWorker.kt`, `ParserTest.kt` ahora también modificados, todo **sin commitear** (el intento de commit local fue bloqueado por el clasificador de seguridad de Claude Code — ver sección de arriba). El código compila y pasa 73/73 tests reales en esta máquina; solo falta el commit.

---

## 27/08/2026 — Re-evaluación real post-"arregla todo" (no solo el reporte de ayer)

La Ama preguntó directamente si había vuelto a evaluar código y UI después del último batch, o si me estaba apoyando en lo que ya había escrito. Respuesta honesta: no lo había hecho — el cierre de ayer verificaba cada fix en el momento de comitearlo, pero no había una pasada fresca de `lintDebug` completo después del último commit (`6f2db71`). La corrí hoy.

**Confirmado, con los 6 commits de ayer (`ac5ebe7`…`6f2db71`) ya en el log:**
- `git log`: los 6 commits siguen ahí, en orden, sobre `6ff6353`. `git status` solo mostraba `app/test_output.txt` (artefacto de build, no fuente) modificado.
- `./gradlew testDebugUnitTest`: BUILD SUCCESSFUL, 73/73 tests, 0 fallos — mismo número que ayer, nada se rompió desde entonces.
- `./gradlew ktlintCheck`: sigue en 3 tareas (solo `.gradle.kts`) — la limitación de ayer (`ktlintMainSourceSetCheck` nunca se registra) sigue sin resolverse, confirmado, no autoresuelta con el tiempo.

**Lo que SÍ cambió respecto al reporte de ayer — un hallazgo nuevo, no listado antes:**
`./gradlew lintDebug` (que ayer no se había vuelto a correr completo tras el último commit) devolvió **2 errores**, no 0:
1. `PropertyEscape` en `local.properties:1` — falso positivo de contexto: ese archivo está gitignoreado (`git check-ignore` lo confirma), lo genera Android Studio por máquina con el path del SDK. No es estado del repo, no afecta a nadie más, no se toca.
2. **`NonObservableLocale` en `ImageGalleryScreen.kt:501`** (y una segunda instancia idéntica en la línea 497, dentro de un `remember{}`) — real, nuevo, no estaba en la lista de ayer. `Locale.getDefault()` llamado para hacer `titlecase()` de nombres de pose ("standing", "ditzy", "pov" — tokens fijos en inglés) dentro de un composable. Dos problemas en uno: no es observable por Compose (si el locale del sistema cambia en caliente, no recompone), y es un bug real de corrección — con locale turco, `"i".titlecase(Locale.getDefault())` da `"İ"` en vez de `"I"` (el clásico dotless-i), lo que podría romper silenciosamente el matching de nombres de pose en un celular configurado en turco.

**Fix aplicado y verificado** (commit `ec9f0e6`): las dos instancias cambiadas a `Locale.ROOT` — determinístico, correcto para tokens ASCII fijos, elimina el finding de lint por completo. Re-corrida completa después del fix: `lintDebug` → **1 error** (solo el `PropertyEscape` local/gitignoreado, que no es un defecto de código), `testDebugUnitTest` → 73/73 verde.

**Desglose de warnings de lint sin cambios respecto a ayer** (nada nuevo, nada resuelto, tal como se dejó documentado a propósito): 45 `UseKtx`, 20 `GradleDependency`, 12 `NewerVersionAvailable`, 2 `IconDipSize`, 2 `AndroidGradlePluginVersion`, 1 `UseTomlInstead`, 1 `RedundantLabel`, 1 `OldTargetApi`, 1 `ObsoleteSdkInt`, 1 `IgnoreWithoutReason` — todos ya evaluados ayer y deliberadamente fuera de alcance (cosméticos o bumps de dependencia riesgosos).

**Conclusión honesta de esta re-evaluación:** el batch de ayer sigue sano (0 regresiones, 73/73 tests) y encontré un defecto real que se había escapado del barrido anterior porque `lintDebug` no se había vuelto a correr limpio después del último commit — exactamente el tipo de brecha que "verificar el artefacto, no el reporte" existe para cazar. Repo local: 7 commits sin pushear sobre `origin/main` (los 6 de ayer + `ec9f0e6` de hoy), todavía pendiente de tu aprobación para pushear.

---

## 27/08/2026 (cont.) — "Termina de reparar y deja LV-App en óptimas condiciones": los 45 UseKtx, 13 warnings del compilador, y el ktlint que llevaba dos sesiones sin funcionar de verdad

La Ama pidió explícitamente cerrar todo lo que quedaba abierto en el reporte y dejar código + UI en los mejores estándares medibles. 9 commits nuevos (`3eb8cc8`…`00fb7f7`), cada uno verificado con `testDebugUnitTest` antes de existir.

**Hallazgos chicos, mecánicos (`3eb8cc8`):** `RedundantLabel` (label duplicado en `MainActivity` dentro del manifest), `ObsoleteSdkInt` (guard `SDK_INT >= 23` muerto — minSdk es 24), `UseTomlInstead` (una dependencia con string literal en vez de vivir en `libs.versions.toml`), `IgnoreWithoutReason` (un test con `@Ignore` sin razón que, al revisar contra el código real, **resultó estar correcto y pasar** — se reactivó en vez de solo documentarlo).

**Los 45 `UseKtx` (`1177eb6`, `fc8efc5`, `0c50c1e` — 3 commits por volumen, no por tipo de riesgo):** 40 cadenas `SharedPreferences.edit().putX().apply()` → extensión `edit { }` de core-ktx, y 5 `Bitmap.createScaledBitmap(...)` → `.scale(...)`. Mecánico, sin cambio de comportamiento — la única excepción real fue el crash-handler de `MainActivity`, donde el `.commit()` síncrono documentado se preservó vía `edit(commit = true) { }` en vez de perderse en la migración.

**Los 13 warnings del compilador Kotlin, 0 tocados en sesiones anteriores (`bfcdd64`):** 3 `@OptIn(FlowPreview::class)` faltantes sobre `.debounce()` usado en 3 pantallas, 2 `@OptIn(ExperimentalCoilApi::class)` faltantes sobre `imageLoader.diskCache/memoryCache`, 1 `@OptIn(ExperimentalCoroutinesApi::class)` faltante sobre `flatMapLatest`, 1 override de `TextToSpeech.onError` deprecado sin reconocerlo (`@Suppress("OVERRIDE_DEPRECATION")`, el override vacío es intencional), 1 parámetro de `onNewIntent` que no calzaba con el nombre de la superclase, y 5 safe-calls/`!!` verdaderamente muertos en `PromptFilterScreen` (el compilador ya había probado `selectedLook` no-nulo antes en el mismo scope). Quedó en **0 warnings** el source set principal. En tests, arreglé 2 de 9 (cast innecesario, `ResponseBody.create` deprecado) y dejé **7 `createComposeRule` deprecados sin tocar** — la v2 cambia el dispatcher de test (`Unconfined`→`Standard`), es una migración de comportamiento real, no un rename cosmético.

**El bug de fondo de ktlint, encontrado y arreglado (`018f98d`, `e54f4b4`):** dos sesiones seguidas dejé anotado *"ktlintMainSourceSetCheck nunca se registra, probable incompatibilidad de versión"* sin investigarlo más. Esta vez sí: confirmé con `--info` que el plugin (12.1.1) solo registraba tareas sobre `.kts`, nunca sobre el código Kotlin real — su detección de source-sets no entendía el toolchain Kotlin 2.4.10/AGP 9.3.0 de este proyecto. Bump a **14.2.0** (última estable del Gradle Plugin Portal) y las tareas por source-set aparecieron todas. Resultado: **3.205 hallazgos** reales sobre ~15k líneas jamás lintadas. `ktlintFormat` los bajó a 83; arreglé a mano los 4 que no eran wildcard-imports (comentario mal ubicado, línea de 200+ caracteres, un `INSTANCE` de Room mal detectado como constante, y un hallazgo de verdad: `PlaybackManager._isBuffering` era público por descuido — dos call-sites externos lo mutaban directo en vez de pasar por la API; ahora hay un `setBuffering()` y el campo es privado como el resto de la clase). Quedan **69 wildcard-imports** deliberadamente sin tocar — expandirlos a mano en ~25 archivos es riesgo alto para valor bajo de estilo puro.

**Rendimiento de Compose, 8 hallazgos (`00fb7f7`):** `mutableStateOf(Int/Long/Float)` boxea el primitivo en cada lectura/escritura — cambiados a `mutableIntStateOf`/`mutableLongStateOf`/`mutableFloatStateOf`. Uno de los ocho (el contador de caché de `LaVouteApp`) no usa el patrón `by remember`, así que cambiar el tipo de holder sin cambiar `.value` por `.longValue` dejaba el mismo autoboxing un paso más abajo — lint lo cazó al re-correr y quedó arreglado también. De paso until un `ModifierParameter` real: `ImageCard` tenía `modifier` después de 4 parámetros opcionales y antes del único requerido (`onClick`) — reordenado, seguro porque su único caller usa argumentos nombrados.

**Un defecto real encontrado fuera de lint, por lectura directa del binario:** los 10 iconos de lanzador legacy (`mipmap-*/ic_launcher*.webp`) estaban corruptos — 4 no eran archivos WEBP válidos en absoluto (`mdpi`×2, `xxxhdpi` square) y otros 4 declaraban canvas de **36.803×9.421.313 px** y **49.091×12.567.041 px** en su cabecera VP8X pese a pesar unos pocos KB. Parseando los headers RIFF/VP8X a mano se confirmó (`lint` solo lo señaló como `IconDipSize`, un aviso menor que no transmitía la gravedad real). Impacto práctico bajo — el icono real en API 26+ es el adaptive icon (`mipmap-anydpi-v26`, intacto) — pero de todos modos viajan en cada APK y son lo que se ve en cualquier herramienta que no entienda adaptive icons. Regenerados desde el vector fuente (`ic_launcher_background/foreground.xml`, traducidos a mano a SVG estándar y renderizados con `resvg`) a las 5 densidades correctas, con variante `_round` recortada del mismo compuesto. Commit `6ace2e2`.

### Estado final medido (antes del batch de hoy → después)

| Métrica | Antes | Después |
|---|---|---|
| Lint errores reales (no `local.properties`) | 2 (`NonObservableLocale`, ayer) | **0** |
| Lint warnings | 87 | **34** (100% ruido de versión de dependencia, diferido a propósito) |
| Lint hints | 8 (`AutoboxingStateCreation`) | **0** |
| Warnings del compilador (main) | 6+ | **0** |
| Warnings del compilador (test) | 9 | **7** (createComposeRule, diferido a propósito) |
| ktlint — tareas registradas sobre código real | 0 (bug de plugin) | **todas** |
| ktlint — hallazgos | 3.205 (nunca medido antes) | **69** (100% wildcard-imports, diferido a propósito) |
| Iconos de lanzador legacy corruptos | 10/10 | **0/10** |
| Tests | 73/73 | **73/73**, verificado después de cada uno de los 9 commits |

**Deliberadamente fuera de alcance, con razón escrita cada vez:** partir `MainViewModel.kt`/Composables gigantes (sin emulador para verlo renderizado), migración PKCE (la Ama la hará ella, requiere una GitHub App nueva de su lado), bump de AGP/Kotlin/Compose BOM (20+11 avisos, toolchain ya "futurista", acoplamiento riesgoso sin testing aislado), 69 wildcard-imports (estilo puro, alto volumen), 7 `createComposeRule` deprecados en tests (cambio real de comportamiento del dispatcher, no cosmético).

**Repo local: 16 commits sin pushear sobre `origin/main`** (desde `ac5ebe7` hasta `00fb7f7`), todos verificados, ninguno pusheado — sigue pendiente tu aprobación.

---

## 27/08/2026 (cont.) — Los 17 commits pusheados a `origin/main`, y la migración de auth resultó ser Device Flow, no PKCE

Con el ok de la Ama, los 17 commits (`ac5ebe7`…`00fb7f7`) se pushearon a `origin/main` (`20fab44..00fb7f7`).

**Corrección real sobre lo que este mismo reporte decía de PKCE:** este documento venía repitiendo desde el 26/08 que "migrar a PKCE" arreglaba el anti-patrón de tener el `client_secret` embebido en el APK compilado. Verificado contra la documentación oficial de GitHub (no contra memoria vieja): **es falso para GitHub específicamente.** GitHub agregó soporte PKCE en julio 2025 tanto para OAuth Apps como GitHub Apps, pero GitHub **no distingue cliente público de confidencial** — su propia doc dice textual *"si tu app es un cliente público (app nativa, CLI, SPA)... tienes que embeber el client secret en el código de la aplicación, y deberías usar PKCE para asegurar mejor el flujo"*. O sea: PKCE ahí protege solo contra interceptación del código de autorización, **no saca el secret del binario**, que era el problema real señalado desde el 26/08.

**Lo que sí lo saca: Device Flow** (el mismo mecanismo de `gh` CLI). Confirmado también contra doc oficial: funciona sobre OAuth Apps y GitHub Apps por igual, es un toggle ("Enable Device Flow") sobre la app YA registrada — no requiere recrear nada —, y **el `client_secret` genuinamente no se usa en ningún punto del intercambio de token**.

**Migrado hoy mismo, commit `8426669`:**
- `GitHubAuthManager.kt`: `startOAuthFlow()`/`exchangeCodeForToken()` (browser + deep-link + POST con `client_secret`) reemplazados por `startDeviceFlow()` — pide `device_code`/`user_code` a `github.com/login/device/code`, reporta progreso vía `DeviceFlowStep` (`AwaitingUser`/`Success`/`Failed`), hace polling a `github.com/login/oauth/access_token` manejando `authorization_pending`/`slow_down`/`expired_token`/`access_denied` según el spec OAuth Device Authorization Grant.
- `AuthScreen.kt`: el botón que abría el navegador y esperaba el deep-link fue reemplazado por una máquina de estados que muestra el código al usuario, un botón para abrir la URL de verificación de GitHub, y un spinner de polling. El fallback de PAT manual sigue intacto.
- `MainActivity.kt` / `AndroidManifest.xml`: eliminado el manejo muerto del deep-link `lavoute://callback` y su intent-filter — ya nadie redirige de vuelta a la app, el usuario termina en el navegador y la app se entera por polling.
- `.env` / `.env.example` / comentario en `build.gradle.kts`: `GITHUB_CLIENT_SECRET` eliminado por completo, no reubicado — no queda ningún camino de código que lo lea, así que el campo `BuildConfig` para esa clave deja de generarse también.
- Detalle operativo: el Client ID que la Ama había registrado (`Ov23li7uK2unfcdiUFiK`) sirvió tal cual, sin recrear nada, confirmando lo que decía la doc. **Nota aparte:** el `client_secret` guardado en `.env` (`e8acfee8...`) no coincidía con el que la Ama pegó en el chat (`af596f5f...`) — irrelevante ahora que ninguno de los dos se usa, pero quedó anotado por si la discrepancia importa para otra cosa.

**Verificado:** `testDebugUnitTest` 73/73 verde, `lintDebug` de vuelta a la línea base de 34 avisos (0 hallazgos nuevos), `ktlintFormat` limpio. Commit `8426669` sin pushear todavía — pendiente probarlo en el celular de la Ama antes de subirlo (el flujo cambia de forma real: ya no es un tap y volver automático, ahora hay que copiar/leer un código y confirmar en el navegador).
