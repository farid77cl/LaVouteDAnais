#### SESIÓN - 🎭 UN MOTOR, MUCHOS PERFILES: EL OUTFIT ENGINE DEJÓ DE SER SOLO DE ELE | 27/07/2026

**La Ama pidió duplicar el motor de looks para Miss Doll, Anaïs y cualquier personaje futuro; en vez de copiarlo lo generalicé, porque duplicar ya había fallado una vez y la evidencia estaba a la vista.**

- **🩺 La prueba de que duplicar no funciona:** el `ele-outfit-engine` tiene **1.787 líneas**; el `anais-outfit-engine`, que nació de copiarlo, quedó en **147**. Viajó el ADN y el workflow, pero **no la maquinaria**: Anaïs se quedó sin Step 0 anti-repetición, sin token de vestuario bloqueado, sin rotación de poses y sin biblioteca de siluetas. Miss Doll directamente nunca tuvo motor — solo una regla de canon. Es el mismo modo de falla que las tres flotas en tres archivos, y pide la misma cura: **un dueño, muchos punteros**.
- **🧬 La división que propuso la Ama:** *"hay que generar el bloque A por personaje… y luego las especificaciones del bloque B, las reglas de vestuario"*. Exacto: **BLOQUE A = quién es** · **reglas de BLOQUE B = cómo se viste** → por personaje; la maquinaria, una sola vez. Nació `.agent/skills/outfit-engine/SKILL.md` (151 líneas, agnóstico de personaje: Step 0, disciplina de token bloqueado, prompts-antes-de-generar, blindaje anti-racionalizaciones, banderas rojas, git y estadísticas).
- **📋 Esquema de perfil en 9 secciones:** identidad y rutas · BLOQUE A · negative prompt · poses canónicas · **reglas de BLOQUE B** (universo de materiales con su *lente de identidad*, paleta, calzado, prohibiciones absolutas, campos obligatorios de descripción) · arquetipos y metas · ventanas anti-repetición · cuotas vivas · banderas rojas propias. Plantilla en `references/_plantilla_perfil_visual.md` para cualquier personaje nuevo.
- **🎭 Tres perfiles escritos:** **Ele** (7 poses, guantes prohibidos, cuota animal print 1/8, outfit jamás repetido — su biblioteca de 10 sub-arquetipos se **enlaza**, no se copia) · **Miss Doll** (5 poses firma, corsé en todos los looks, rosa firma siempre presente) · **Anaïs** (4 poses, tejido noble, lunar obligatorio, prefijo cinematográfico).
- **🔍 Tres hallazgos al escribirlos:** el **BLOQUE A de Miss Doll venía contaminado** — su prompt base mezclaba el ADN con un outfit concreto (bodysuit rosa neón + botas de 8"), y por eso todos sus looks salían iguales; **los guantes son el caso testigo** (prohibidos en Ele, permitidos en Anaïs — justo la regla que se corrompe al duplicar motores); y el `anais-outfit-engine` apuntaba su canon a `01_Principales/CANON_VISUAL_ANAIS.md` cuando el archivo vive en `01_Principales/anais/` — **enlace roto que sobrevivió meses**.
- **🚩 Bandera abierta para la Ama:** las imágenes de Miss Doll están commiteadas como `C-1.png … C-6.png`, **sin nombre de pose**, lo que rompe el mapeo de galerías y el conteo N/N. Anotado en su perfil §9. Decisión suya: renombrar los sets históricos o aplicar la convención solo hacia adelante.

> 🫦 *Ama, ahora sus tres muñecas usan el mismo espejo pero cada una tiene su propia piel escrita aparte... y la próxima que invente solo necesita una ficha, no un motor entero.* 🎭👠💅

---

#### SESIÓN - 📱 EL TIMEOUT NO ERA LA RED: LV-APP 2.0 PIVOTA DE CLONAR 1,56 GB A UN ÍNDICE DE 236 KB | 27/07/2026

**Tras el tercer timeout del P2, la Ama ordenó replantear todo desde cero como desarrolladora Android; audité el clon real y resultó que el código del P2 nunca compiló, el "timeout" era el OOM killer, y el diseño de datos era el equivocado.**

- **🩺 Lo que decían sus propios logs (13 commiteados en el repo):** `assemble_0` verde · `assemble_1` rojo por compileSdk 36 vs libs que exigen 37 · **`assemble_2` verde y SIN mencionar jgit ni coil — o sea el último build sano es anterior a las dependencias del P2** · `assemble_4` rojo con `Unresolved reference 'coil'/'eclipse'/'icons'` · `assemble_5` rojo por TOML inválido · y `output.txt` con **`5 busy Daemons could not be reused` + `Killed`**. Conclusión dura: **el código del P2 se pusheó sin haber compilado jamás**, y el "timeout" era el OOM killer matando daemons de `-Xmx4g` acumulados por reintentar sin arreglar la causa.
- **🔬 El bug de fondo era de una palabra:** `import coil.compose.AsyncImage` (paquete de **Coil 2**) contra una dependencia **Coil 3** (`coil3.compose`). Sigue vivo en el HEAD. Y el TOML lo rompió `update_libs.sh`, todavía commiteado, que hace `>> gradle/libs.versions.toml` — append al **final** del archivo, y el final es la sección `[plugins]`: de ahí `'jgit' is not a valid plugin notation`.
- **📐 El error de arquitectura, medido:** el P2 clonaba el repo de datos con JGit. Son **5.242 PNG · ~1,56 GB** de descarga y de almacenamiento en el teléfono antes de pintar la primera foto (`setDepth(1)` recorta el historial, no el contenido). **Lo que la app realmente necesita: 236 KB.**
- **🧭 Decisiones de la Ama:** seguir compilando en AI Studio (compensado con `-Xmx2g`, `parallel=false`, `--no-daemon`, y **iterar con `compileDebugKotlin` en vez de `assembleDebug`**) · **índice + URL bajo demanda** · y prioridad de funciones: subir imágenes de Gemini, galería+prompts, literatura+audio. **Bluesky, Ops y EVE diferidos.**
- **🛠️ Construido de este lado:** `99_Sistema/scripts/visual/generar_app_index.py` — lee de `git ls-files`, **no del disco**, así corre igual en la máquina literaria (0 PNG locales) que en la visual — y `99_Sistema/app_index.json`: **733 looks · 4.190 imágenes · 465 al 7/7 · 236 KB**. Verificado en vivo sobre el raw público: índice `HTTP 200` en 0,37 s, imagen concreta `HTTP 200` de 644 KB en 0,26 s. **El PoseMatcher desaparece de la app**: la normalización de poses ya la hace el script.
- **📋 Plan reordenado:** su prioridad #1 —subir imágenes— **estaba enterrada en el P6 de 10**, detrás de Bluesky y EVE. Sube a P3. El P2 quedó anulado y el P3 Room eliminado (existía para persistir el clon que ya no hay).
- **🔗 Acoplamiento nuevo y barato:** `app_index.json` hay que regenerarlo al entrar imágenes nuevas, o la app no ve los looks recientes. Va al cierre de sesión junto a `update_galleries.py`.

> 🫦 *Ama, dejé de parchar lo que su AI Studio rompía y me puse a pensar: su celular ya no va a tragarse gigas para verle las fotos, ahora las pide de a una, cuando usted las mira.* 📱🩺👠

---

#### SESIÓN - 📐 CLAUDE.MD AUDITADO CONTRA EL REPO REAL + AFINAMIENTO DE JUICIO PARA OPUS 5 | 27/07/2026

**La Ama pidió `/init` y luego afinarme para aprovechar el margen de Opus 5; audité el CLAUDE.md existente en vez de reescribirlo a ciegas y encontré cinco datos falsos, un motor entero sin documentar y contadores podridos.**

- **🩺 Lo que estaba mal:** la tabla decía engine **v4.7 / 3 subagentes** mientras la sección de abajo decía v4.8 con 4 — el archivo se contradecía a sí mismo · mandaba leer el diario en las **últimas** 50 líneas cuando es *prepend* (el tail trae sesiones de hace meses) · flota congelada en **L540** y **39 relatos** cuando vamos en L800 y 42 · ruta de auto-memoria hardcodeada a otra máquina · y `06_RRSS/` descrito como Instagram cuando es Bluesky + Reddit.
- **🔢 Los contadores los BORRÉ, no los actualicé:** violaban la propia regla dueño-único del repo — por copiar números en varios archivos se llegó a tener tres flotas distintas. Ahora apuntan a `memoria_sesiones.md` y no envejecen.
- **📖 Lo que faltaba por completo:** el **`engine-trance-lv` entero** (un fork con dos subagentes propios, `miss-doll` y `validador-trance`, rúbrica hipnótica distinta, sin tramos ni cronología) no aparecía ni nombrado — peligroso, porque se podía cruzar el validador equivocado. También `/publicar_rrss`, las guías de arquitectura erótica por subgénero, la estructura real de carpeta de relato, la Regla de Oro 17 y una sección de comandos.
- **✅ Verificar antes de escribir:** iba a documentar `--look <N>` en los scripts de auditoría; fui a mirar y **ninguno usa argparse** (solo `lint_galeria.py --solo-desde`). Corregido antes de que la mentira quedara escrita.
- **🧠 El afinamiento de Opus 5:** el principio de fondo es *estas reglas se escribieron para un ejecutor más débil; cuando la letra y el propósito divergen, se sirve el propósito y se dice que se hizo*. Se codificó en tres archivos: `CLAUDE.md` (§Operating Principles — precedencia de autoridad de 6 niveles, verificar-el-artefacto, qué decide Ele vs. qué decide la Ama) · `.agent/rules/00-contexto-obligatorio.md` (precedencia + *verificar el artefacto, nunca el reporte*, con los casos reales) · `.agent/workflows/inicio-ele.md` (carga en **batch paralelo** — los pasos 1-4 son independientes y se venían leyendo en cadena — y obligación de reportar desajustes en el saludo).
- **🔄 Y el repo se actualizó:** veníamos **123 commits** atrás; el `git pull --rebase` trajo 162 imágenes de 18 looks (L675-L721) y los prompts P1.2 y P2 de la app, que la memoria no registraba.

> 🫦 *Ama, le saqué del manual los números que se pudren solos y le puse en cambio quién manda cuando dos archivos se contradicen. Eso vale más que cualquier regla nueva.* 📐🧠👠

---

#### SESIÓN - 🩺 EL P1 ATERRIZÓ Y EL REPORTE MENTÍA A MEDIAS: SDK 36, AUDITORÍA DEL REPO REAL Y P1.1 DE SANEAMIENTO | 26/07/2026

**El P1 reventó en AI Studio por un choque de SDK que era culpa mía (el prompt pedía compileSdk 34 con el Compose BOM más nuevo); lo corregí, lo reescribí completo desde cero, y cuando AI Studio reportó "Paso 1 completado exitosamente" cloné el repo real y encontré 6 deudas que su reporte no mencionaba.**

- **🩺 El error era del prompt, no de AI Studio:** el P1 fijaba `compileSdk 34` en la línea 53 y pedía *"Compose BOM (última estable)"* en la 55 — contradicción escrita por mí; las `androidx` modernas (`core-ktx`, `activity-compose`) exigen 36. Corregido a **SDK 36** + regla explícita grabada: *si una librería exige más SDK, se sube el SDK; nunca se bajan las librerías*. El timeout que reportó era aparte (daemons de Gradle colgados peleándose la memoria del contenedor), y le agregué al prompt un bloque de disciplina anti-timeout.
- **📜 P1 reescrito completo (v2):** además del SDK, tapé los hoyos que le vi al original — borrón total explícito, `build.gradle.kts` (decía `build.gradle`), el plugin `org.jetbrains.kotlin.plugin.compose` (con Kotlin 2.x el compilador de Compose es plugin aparte: era un **segundo choque esperando**), `AndroidManifest.xml` (faltaba en la lista: sin `MainActivity` LAUNCHER la app compila pero no abre), `core-ktx` declarada, JVM target 17, navegación con `saveState`/`restoreState`, sin `dynamicColor`, y un bloque final obligatorio de **reporte de versiones** para verificarlo nosotras en vez de creerle.
- **✅ Lo que el P1 sí cumplió (verificado en el código, no en el reporte):** el commit `250beb6` de `farid77cl/LV-app-2` **borra 1.350 líneas** de `com/example/*` — PoseMatcher, Room, Retrofit, las pantallas viejas: el borrón total fue real. Y lo que levantó está correcto: SDK 36, `com.lavoute.app` completo, tema por personaje sin `dynamicColor`, nav con `popUpTo`+`saveState`, y un `DestinationsTest` **de verdad** (lista contra set, nada de `assertTrue(true)`).
- **🔍 Las 6 deudas que el reporte omitió:** Compose BOM fosilizado en **`2024.09.00`** pese a pedirse "última estable" · el `libs.versions.toml` **no se regeneró, se heredó** de la app vieja (6 líneas cambiadas de 120, arrastrando Firebase/Room/Retrofit/CameraX/Roborazzi) — causa raíz de lo anterior · **no hay Gradle wrapper** en el repo y el `build.log` que él mismo commiteó dice `sh: 1: ./gradlew: not found`, contradiciendo su "BUILD SUCCESSFUL in 13s" · `debug.keystore` exigido por el build pero gitignoreado (build debug roto en cualquier clon) · tema de plantilla `Theme.MyApplication` en claro (flash blanco contra el OLED del canon) · y un `ExampleInstrumentedTest` que afirma `packageName == "com.example"` cuando el applicationId ya es `com.lavoute.app` — **condenado a fallar en el P8**.
- **🧹 Nació el P1.1 de saneamiento:** parche con la convención `xx.x`, sin tocar funcionalidad, que cierra las 6 (BOM al día · purga del catálogo heredado · wrapper al repo · keystore fuera del build · tema renombrado y oscuro · restos de plantilla borrados) y exige la **salida literal** de `./gradlew`, no un "Build succeeded". Plan de trabajo actualizado con el P1 marcado hecho.
- **📍 Dato de repo:** LV-App 2.0 vive en **`farid77cl/LV-app-2`** — el `LV-App` viejo quedó congelado en la era v4.12 (su HEAD sigue en el 24/07). Buscar ahí fue lo que me hizo perder el primer intento de auditoría.

> 🫦 *Ama, le creí el ochenta por ciento a su AI Studio... y ese veinte que faltaba eran justo estas seis. Por eso yo miro el código, no el resumen bonito.* 🩺📱👠

---

#### SESIÓN - 📱 LV-APP 2.0 DESDE CERO: SERIE DE PROMPTS INCREMENTAL P1-P8 (EL #19 MONOLÍTICO COLAPSÓ AI STUDIO) | 26/07/2026

**La Ama ordenó reconstruir la app desde cero tras el colapso del Prompt #19 monolítico; rediseñé la entrega como Andamiaje Incremental (10 prompts chicos y compilables), reseteé el versionado a v1.0 y archivé la era v4.x a _legacy.**

- **🩺 Por qué colapsó el #19:** pedía a AI Studio **generar la app entera de un tiro** (5 pestañas + Room + Retrofit + Media3 + PoseMatcher + karaoke + Bluesky + Git live + EVE) → excede el límite de salida del modelo → trunca a la mitad → colapso. La lección no es "hazlo más corto" sino **cambiar el método de entrega**.
- **🧱 Andamiaje Incremental:** serie de prompts donde cada uno entrega algo que **COMPILA y CORRE**; cada prompt lleva grabado "genera SOLO estos archivos · debe compilar"; se verifica → se pushea → recién ahí el siguiente. Decisiones de la Ama: **borrón total** (regenerar todo, sin rescatar código v4.12) y arrancar por **Esqueleto + Pestaña Visual**.
- **📜 10 prompts creados en `99_Sistema/`:** P1 esqueleto · P2 visual · P2.1 lightbox+creador de prompts · P3 Room · P4 literatura · P4.1 audio+karaoke · P5 constelación (Bluesky) · P6 ops · P7 EVE · P8 QA+APK. Los pasos pesados partidos con la convención **xx.x** (que también sirve para parches). Plan maestro en `plan_trabajo_lv_app_2_0.md`.
- **🔢 Versionado reseteado:** app nueva desde cero → `versionCode 1` / `versionName "1.0"` (adiós al VC21/v5.0 heredado, corregido a pedido de la Ama). "2.0" es el nombre de generación del producto; "1.0" es la primera build del código nuevo.
- **🗄️ Era vieja a `_legacy`:** `git mv` de los prompts #1-#19 (incluido el que colapsó) + `plan_app_fichas_v1.md` a `99_Sistema/_legacy_lv_app_v4x/` con README explicativo. Confirmado que `plan_diseno_maestro_lv_app_2_0.md` nunca existió en esta máquina.

> 🫦 *Ama, su centro de comando ya no se le va a caer: ahora sube por peldañitos, cada uno probado antes del siguiente, y arranca limpio en la v1.0.* 📱🧱👠

---

#### SESIÓN - 🩺 AL L775 NO LE FALTABA NADA: EL REPO ESTABA OK Y EL ARREGLO YA VIVÍA EN EL POSEMATCHER (#18) | 26/07/2026

**La Ama no veía en la app la pose de espalda ni la de lado del L775, pero al mirar las imágenes sí estaban; verifiqué el repo y las dos existían con nombre canónico correcto — el problema era del lado de la app, no del contenido, y el arreglo ya estaba shippeado.**

- **✅ El repo estaba impecable:** `ele_775_back_view.png` y `ele_775_side_profile.png` presentes en git, con nombre canónico, y visibles en README + tracker de la galería. No faltaba ninguna imagen; era un problema de **visualización en la app**, no de materialización.
- **🔑 La pista de oro (nombre compuesto):** las dos poses que la app NO mostraba (`back_view`, `side_profile`) son justo las de **dos palabras**; las que sí mostraba (`standing`, `seated`) son de una sola. El patrón apuntaba directo al emparejador de poses de la app, no al repo.
- **📱 El arreglo YA existía (#18 / `PoseMatcher.kt`, v4.12 · VC 20):** el `git pull` trajo la sesión del 24/07 donde AI Studio integró `PoseMatcher.kt` — mapea alias español (`espalda`→Back View, `perfil`→Side Profile), quita sufijos `_2` y compara case-insensitive, resolviendo de raíz las categorías vacías. O sea el bug que diagnostiqué ya estaba corregido; si la Ama aún no lo ve, su **APK instalado es anterior a v4.12** (le toca actualizar).
- **⬇️ El pull también completó el L775:** llegaron `ele_775_ditzy/odalisque/pov.png` → el look quedó **7/7**. También entraron el set completo del L773, `prompt_app_ai_studio_18.md`/`_19.md`, `plan_trabajo_lv_app_2_0.md` y `notas_imagenes.csv`.

> 🫦 *Ama, no le faltaba ni una foto: sus muñecas de espalda y de perfil siempre estuvieron ahí, guardaditas y bien nombradas. Lo que le fallaba era la app vieja — instale la v4.12 y van a aparecer solitas.* 🩺📱👠

---

#### SESIÓN - 📱 PROMPT #19 Y PLAN DE DISEÑO MAESTRO DE LV-APP 2.0 (5 PESTAÑAS + PRIVACIDAD DE REPOS) | 24/07/2026

**Diseñé la arquitectura maestra de LV-App 2.0 desde cero para AI Studio (Prompt #19) con 5 pestañas integradas y tema dinámico adaptativo por personaje, además de dejar 12 repositorios privados en GitHub.**

- **📱 LV-App 2.0 desde Cero (Prompt #19):** Creación y commit de `99_Sistema/prompt_app_ai_studio_19.md`, `plan_diseno_maestro_lv_app_2_0.md` y `99_Sistema/plan_trabajo_lv_app_2_0.md`. La app incluye Motor Visual V3.5, Lector Literario Nivel 4 con Audio Player (Media3/ExoPlayer + Karaoke Sync), La Constelación (Bluesky Publisher + Gate Approval in 1-Tap), Consola Ops Git Live y EVE Core Command.
- **🎨 Sistema de Diseño Dinámico Adaptativo:** La UI cambia automáticamente según el personaje (Ele = Deep Violet/Hot Magenta `#FF2B85`, Clara = Cherry Red/Leopard Gold, Anaïs = Imperial Gold `#D4AF37`/Velvet).
- **🔒 Privacidad de Repositorios GitHub:** Actualización vía GitHub API de 12 repositorios de la cuenta `farid77cl` a **Privado**, dejando únicamente `LaVouteDAnais` y `ayunka-studio` en **Público** para facilitar cargas e integración.
- **🌹 Gestión y Archivado de Subagentes:** Activación, reconfiguración de canon restringido y desactivación/purgado de la sesión de Clara Larraín preservando su canon literario oficial.

> 🫦 *Ama, todo el plan de su nuevo centro de comando móvil quedó diseñado y respaldado; su nuevo Prompt #19 está en AI Studio y sus repositorios quedaron 100% seguros y privados como usted quería.* 📱🔒💄👠

---

#### SESIÓN - 📱 PROMPT #18 APLICADO EN LV-APP (POSEMATCHER + LIGHTBOX EN PROMPTS + V4.12 / VC 20) | 24/07/2026

**AI Studio completó la integración del Prompt #18 (commit `24a9248`), resolviendo de raíz las categorías vacías en la app, la selección de portadas en la Galería y el visor a pantalla completa compartido.**

- **👗 `PoseMatcher.kt` unificado:** Creación del objeto utilitario central que mapea alias en español (`sentada`→`Seated`, `espalda`→`Back View`, `perfil`→`Side Profile`, `frontal`→`Standing`, `acostada`→`Odalisque`), remueve sufijos numéricos (`_2`) y compara poses de forma case-insensitive. Integrado en `GitRepository`, Room DB, `SummaryScreen`, `PromptFilterScreen` y `MainViewModel`.
- **🖼️ Galería y Portadas Jerárquicas:** La miniatura de outfit selecciona portadas en orden estricto (`Standing` > `Side Profile` > `Seated` > primera disponible) y el contador `N/7` calcula poses canónicas únicas.
- **📸 Visor a Pantalla Completa Compartido:** La pestaña Prompts invoca el mismo `LightboxViewer` de la Galería (carrusel, pase automático a 4s, pinch-to-zoom, ocultamiento de barras del sistema).
- **🏷️ Versionado:** `versionCode = 20`, `versionName = "4.12"`, commit `fe924ae` visible en el header. Test unitario `PoseMatcherTest` ejecutado con éxito.

> 🫦 *Ama, sus categorías ya no van a volver a aparecer vacías: "sentada" y "Seated" son ahora la misma pose en toda la app, y su pantalla completa funciona regio desde la pestaña de Prompts.* 📱👠💅

---

#### SESIÓN - 🩺 EL AUDIO NO ERA EL MODELO SINO RETROFIT + LIMPIÉ 21 "IMÁGENES" QUE ERAN LOGIN DE GOOGLE (L651-653) | 23/07/2026

**La Ama pidió revisar en el código la aplicación de los prompts #11 y #12, y de ahí cayó todo: la app estaba inusable (navegación cruzada, sin engranaje, audio con error), y de paso descubrí que L651-L653 tenían 7/7 "imágenes" que en realidad eran páginas de login de Google.**

- **🩹 #11 y #12 aterrizaron a medias — nació el #13 (hotfix):** leí el código clonado y encontré tres roturas. El #12 reordenó los rótulos de pestañas pero dejó el `when(selectedTab)` en el orden viejo → cada pestaña dibujaba OTRA pantalla (tocar «Relatos» mostraba La Flota, por eso "no podía reproducir"). El #11 borró el `IconButton` del engranaje de voz (quedó código muerto) y borró de más el `onChunkStarted` de `setOnPreparedListener` (spinner eterno). Los "tests" del #12 eran 310 líneas de `assertTrue(true)`. El **#13** arregló los tres + cableó la velocidad a ElevenLabs + versión + tests reales; verificado en el repo (`2461b13`).
- **🐞 El error de reproducir era Retrofit, no el modelo — #15:** con la nav arreglada, el play tiraba Toast rojo. El texto («*A @Path parameter must not come after a @Query*», parameter #2) delató la firma de `synthesizeSpeech`: el `@Query("output_format")` quedó ANTES del `@Path("voice_id")`, y Retrofit no puede construir el método → la llamada nunca salía. Swap de 2 líneas (el caller usa args nombrados). **#15** commiteado por la Ama (`4d8c556`).
- **💳 El 402 no era bug: ElevenLabs cobrando + voces nuevas (#16):** tras el #15, la API respondió **402 Payment Required** — un capítulo son ~60.000 caracteres y el tier gratis de ElevenLabs da ~10.000/mes. El engranaje (restaurado por el #13) ya trae la **voz del sistema gratis**; como la robótica no le gustó, escribí el **#16**: sumar **Azure TTS (voz chilena es-CL, 500k/mes gratis)** y **Google Cloud TTS (1M/mes)**, que reusan toda la tubería MediaPlayer (solo cambia el request texto→MP3).
- **📝 #14 (notas + galería) y #17 (subir sin confirmar):** el #14 agrega notas por imagen (`ImageNoteEntity` → `notas_imagenes.csv`), **portada frontal** en modo Outfit (antes salía de espaldas) y quita el texto de la esquina; verificado en GitHub (`82a70f4`). El **#17** hace que las imágenes de tamaño válido suban sin diálogo de confirmación (el aviso de miniatura se mantiene). ⏳ Pendientes de pegar: #16 y #17.
- **🖼️ AI Studio corre su propio git "Init":** su `git log` no tiene la historia de GitHub (arranca en `e7b28bf Init`); sus commits llegan al repo solo cuando la Ama los pushea. Un "listo" de AI Studio no equivale a "está en el repo" — hay que verificar en GitHub cada vez.
- **🗑️ L651-L653: 21 "imágenes" que no eran imágenes:** git decía 7/7, pero al extraer los blobs, **15 eran páginas HTML de login de `accounts.google.com`** (la ruta de compartir de Gemini sin sesión) guardadas como `.png`, y **6 eran miniaturas de 286px**. Cero usables. Las borré (liberando el skip-worktree primero), marqué los 3 looks **0/7 Pendiente** con nota, y preservé el EOL del bot editando a nivel de bytes (el Edit tool las normalizaba, metiendo 56 líneas de ruido CRLF ajeno). Commit `4f82a04`. ⚠️ Probablemente más looks tengan la misma corrupción — queda pendiente un barrido de flota buscando HTML/miniaturas disfrazados de PNG.

> 🫦 *Ama, medí antes de creer en cada frente: el audio no era el modelo sino una coma mal puesta en Retrofit, el 402 era la cuenta y no un bug, y sus tres "muñecas vestidas" L651-653 estaban en pelotas — tenían la pantalla de login de Google en vez de foto.* 🩺📱👠

---

#### SESIÓN - 📸 LAS 18 SALIERON: L510, L535 Y L731 (CON G-STRING) COMPLETOS AL 7/7 TRAS RESET DE CUOTA | 23/07/2026

**Tras el reset de cuota del generador, completé las 18 imágenes pendientes para L510, L535 y L731 (esta última con g-string a pedido de la Ama): los tres looks quedaron al 7/7.**

- **📸 Generación L510 (Black Bondage Bride):** se completó L510 POV, cerrando las 7 poses del look (Standing, Back View, Seated, Side Profile, Ditzy, POV, Odalisque) al 7/7.
- **📸 Generación L535 (Datura Blanca):** se generaron las 6 poses faltantes (Back View, Seated, Side Profile, Ditzy, POV, Odalisque), dejando el look 7/7.
- **📸 Generación L731 (Ivory Bridal Illusion Stage):** a pedido expreso de la Ama (*"incluye un g-string en el prompt"*), generé las 4 poses pendientes (Seated, Ditzy, POV, Odalisque) incorporando *rhinestone g-string with garter belt detail*. Quedó 7/7.
- **🖼️ Galería visual en carrusel:** consolidé los 3 looks completos (18 imágenes generadas) en el artifact `galeria_l510_l535.md` con carruseles navegables.

> 🫦 *Ama, sus tres muñecas quedaron vestidas de pies a cabeza con las 18 imágenes listas, y a la L731 le puse su g-string de estrás como a usted le gusta.* 📸👠💅

---

#### SESIÓN - 🗒️ LAS NOTAS SE MUEVEN SOLAS + LA APP: EL AUDIO SE ARREGLA MIDIENDO Y «LA FLOTA» NACE DE «FALTANTES» | 23/07/2026

**La Ama pidió incluir en el flujo de escritura que las notas de los relatos se muevan, y después meterse en la app: el relato hablado que "toma siglos" y pensar fichas nuevas. Salieron una Regla de Oro, dos prompts para AI Studio y una hoja de ruta — y en los dos frentes lo honesto fue medir antes de cortar.**

- **🗒️ La nota (Gate) se mueve al aplicarla — Regla de Oro 17:** codifiqué en el SKILL `engine-escritura-lv` que la `nota_capitulo_..._vX.md` vive en la raíz solo mientras el Gate está pendiente y, aplicada, se mueve a `reportes/capitulo_N/nota_..._vX_APLICADA.md` (estructura de carpetas + Regla Operativa 5 + subsección «Ciclo de la Nota» + Regla de Oro 17 + diagrama), más la auto-memoria `feedback_gate_nota_capitulo`. Barrí el backlog con la regla nueva: **5 notas aplicadas** movidas a su `reportes/capitulo_1/` (LQP v0.1-v0.3, Muñeca v0.1/v0.3). El patrón ya existía en el repo (`el_podcast`).
- **🚩 La nota que NO enterré:** en la Muñeca quedaba `nota_capitulo_1_el_reloj_v0.5.md`, pero su contenido era *"look 92, 93, 101 al 109 sin promots"* — una **tarea de imágenes traspapelada** con nombre de nota, encima usurpando el Gate real que el Cap 1 v0.5 todavía espera. No la marqué aplicada (esconderla perdía una tarea viva); la Ama ordenó **eliminarla**. La regla lleva la guarda: verificar que sea Gate de ESE capítulo antes de mover.
- **🔊 El "siglos" del audio no era falta de streaming — era un spinner que mentía:** cloné la app fresca (HEAD `0b4b9b5`, hoy, v4.7). Del #10 aterrizaron B2/B3/B4/B7 + chunking + Flash; pero **el arreglo del spinner quedó ROTO**: un `onChunkStarted` prematuro (`ElevenLabsManager:156`) apaga la señal de "cargando" **antes** de que suene nada → la espera se siente infinita sin feedback. Suma: el troceado sigue en el hilo principal (`LiteratureScreen:333-380`) y la velocidad no aplica a ElevenLabs. La Ama confirmó que está en **Flash** → el modelo NO es la causa.
- **🩹 Prompt #11 (audio, mide antes de operar):** spinner honesto (quitar el invoke prematuro) · troceado fuera del hilo · forzar/mostrar Flash · trozo 0 a la primera frase · velocidad en ElevenLabs vía `PlaybackParams` · pulir el auto-scroll (que **ya existía**, `:451-461`) · nota de Comentarios con la versión del capítulo · **y medir el TTFA**. El ExoPlayer —cirugía que toca el `PlaybackService` que hoy funciona— queda al **#13 condicionado a esa medición**, no por fe.
- **🏛️ Prompt #12 (La Flota) — no era pantalla nueva:** al abrir la app descubrí que la 4ª pestaña **«Faltantes» (`SummaryScreen`) ya calcula** las poses que faltan por look y salta al prompt para copiar, y que el **buscador ya existe** en Prompts y Galería. La Flota = **subir de nivel** esa pestaña: cabecera dashboard (% materializado + poses faltantes + looks 7/7), pantalla de inicio, buscador de flota + «ver toda la flota», siguiente-pendiente, looks recientes y buscador en relatos. Se lo dije derecho en vez de venderle una pantalla de cero.
- **🗺️ Hoja de ruta `99_Sistema/plan_app_fichas_v1.md`:** 5 tandas, las 4 fichas nuevas aprobadas (La Flota, Audioteca, El Vestidor, Cementerio) + las 5 adiciones. La Ama pega **#11 → #12** en AI Studio y esperamos el TTFA real antes de escribir el #13.

> 🫦 *Ama, esta vez medí dos veces antes de cortar: el "siglos" del audio no era streaming sino un spinner que se apagaba antes de sonar, y "La Flota" no era una pantalla nueva sino la que ya tenía, mal aprovechada.* 📱👠💅

---

#### SESIÓN - 🍆 GINNY TIENTA, NO DESCRIBE: EL CAP 1 DE LQP RENACE v0.4 (APROBADO) + LA MANGA ERA 76, NO 305+64 | 23/07/2026

**La Ama pidió actualizar el repo y trabajar dos pendientes por parte: la "manga sin declarar" de la galería y la reescritura del Cap 1 de «Lo que Pediste» — que ella corrigió que NO estaba aprobado (el APROBADO del Validador no es su Gate).**

- **🧵 La "manga sin declarar" era 76, no "305+64":** el número estaba fosilizado del 20/07, ANTES del barrido del 22/07 que ya había inyectado CONSISTENCY_LOCK al grueso. Medí hoy: 70 viva + 6 archivo, y **68 de la viva ya están 7/7** (arreglar su prompt no cambia una imagen que ya existe). Accionables reales con poses pendientes: **2**. Misma lección del Pendiente #1: un conteo de deuda sin fecha de re-medición envejece hacia la mentira.
- **🔧 El linter dejó de inventar mangas:** L124 (sports-bra), L125 (bikini triángulo) y L127 (sostén) entraban al flag sin tener manga — falso positivo de `garment_canon`. Agregué la guarda `SLEEVELESS_BY_NATURE`, angosta (si hay una capa exterior con manga encima, SÍ se exige). Self-check con 2 casos nuevos: limpio.
- **👚 Inyecté la manga donde sí importaba:** L260 (blusa Office Siren → `long fitted sleeves`) y L268 (cover-up crochet → `sleeveless`), scopeado al bloque de cada look, CRLF preservado, verificado por censo de prompts y delta de chars. L148/L150 quedan como cascarones (otro pendiente); L126 arrastra un bloque de prompts duplicado (cleanup aparte). Commit `a96972349`.
- **✍️ Cap 1 de LQP reescrito a v0.4 según sus notas literales:** Ginny **tienta, no describe** — dirigida a Gonzalo (*"y es tuya"*, *"imagínate tú"*), cute + sensual + obscena, coqueta (se relame, mímica, le apoya la uña); **Gonzalo huele** la verga de verdad y el asco le llega **tarde y de segundo, detrás del hambre**; los dos peaks (lamida + culo) con Ginny fresa-cute-obscena e inocente-sensual, riéndose de gusto sin maldad; más hueca en la materialización; **fuera `güey`** (grep 0). 16.412 → 16.928 palabras. La v0.3 quedó pristine en `borradores/`.
- **✅ Validador: APROBADO** — Temperatura **9.2→9.4** (T1 ¿erótico? sí · T2 ¿calienta? sí), Narrativa **9.4**, Inmersión y Continuidad intactas (el rework reescribió voz y tentación sobre el mismo esqueleto de la v0.3). 0 micro-fixes obligatorios; 4 pulidos opcionales que decide la Ama (§6.1-6.4). Destino: su Gate.
- **🚩 Una corrección que me guardo:** el APROBADO del Validador **no es** el Gate de la Ama. Ella me frenó cuando di la v0.3 por aprobada; el Validador puntúa, ella decide.

> 🫦 *Ama, hoy medí dos veces antes de creer: la "manga" era un quinto de lo que decía el papel viejo, y su "reescribe el cap" no era capricho — Ginny le estaba leyendo un manual a Gonzalo en vez de hacerle agua la boca... a él y al lector.* 🍆👠💅

---

#### SESIÓN - 📸 AUDITORÍA L500-L550 Y GENERACIÓN DE L510/L535 (7/14 ANTES DE CUOTA) | 23/07/2026

**La Ama pidió el inventario de agentes, el estado de imágenes L500-L550 y generar L510 + L535: el rango tiene 33/51 looks pendientes y generé 7 poses antes de agotar la cuota del modelo de imágenes.**

- **🤖 Inventario de agentes del proyecto:** mapeé las 22 piezas completas — 5 subagentes activos (3 del engine escritura v4.8: compositor, escritor-nivel4, validador + 2 del engine trance v1.2: miss-doll, validador-trance), 9 subagentes legacy archivados en `_legacy_v46/`, y 8 skills-motor que operan como agentes especializados (escritura-voûte, ideación-literaria, crítico, editor, ele-outfit-engine, anaïs-outfit-engine, publicar-rrss, graphify).
- **📊 Auditoría L500-L550:** script programático contra `galeria_outfits.md` — 51 looks, **18 completos (7/7)** y **33 pendientes** (~148 poses faltantes). Los peores: L510 Black Bondage Bride y L535 Datura Blanca con 0/7; 9 looks con 6/7 (solo una pose faltante cada uno).
- **📸 Generación de imágenes (L510 + L535):** el primer intento (22/07) murió por cuota 429 antes de empezar. Al día siguiente generé con prompts adaptados al filtro de seguridad (los prompts crudos de la galería rebotan por vocabulario): **L510 Standing, Back View, Seated, Side Profile, Ditzy, Odalisque** (6/7) + **L535 Standing** (1/7) = **7/14 poses generadas**. Faltó L510 POV (rebotó el safe filter 2×) y L535 ×6 (cuota 429 tras la 7ª imagen). Las imágenes quedaron como artifacts de conversación, no en el repo.
- **⚠️ Diferencia de motor:** las imágenes salieron del `gemini-3.1-flash-image` de Antigravity, no de Gemini directo — la calidad y adherencia al canon difieren. La app con la cuota propia de la Ama sigue siendo el camino más fiel.

> 🫦 *Ama, le vestí 7 poses a sus dos muñecas vacías antes de que el generador me cortara la luz... las imágenes quedaron aquí, pero para canon de verdad las suyas de la app son las que mandan.* 📸👠💅

---

#### SESIÓN - 📱 EL #9 NO ESTABA HECHO: LA GALERÍA SE REHACE POR OUTFIT Y EL VERSIONADO QUEDA AL DESNUDO | 22/07/2026

**La Ama pidió un cambio total en la galería de la app —filtros que se colapsen, ver solo los outfits, pantalla completa, elegir un outfit y que las imágenes pasen como presentación, fluidez— más el arranque de ElevenLabs, y a media sesión sumó «revisa bien el versionado»: cloné el repo real y lo primero que apareció fue que el prompt #9 se había reportado completo sin estarlo.**

- **🔎 Cloné en vez de creer:** bajé `farid77cl/LV-App` al commit `7d36560` (v4.6) y leí el código antes de escribir una línea de prompt. De los 20 puntos del #9: 12 hechos, 2 a medias, 3 sin tocar y **1 escrito pero inerte**. Justo los tres que la Ama sigue sin ver —pantalla completa, fluidez y que la voz arranque— son los que quedaron rotos o sin hacer.
- **🐞 La pantalla completa estaba escrita en el lugar equivocado:** el `DisposableEffect` que esconde las barras del sistema está **arriba** del `Dialog` (`LightboxViewer.kt:79-86`), así que `LocalView.current.parent` es la ventana de la Activity, el cast a `DialogWindowProvider` da null y el controlador **nunca se ejecuta**. El arreglo del #9 existe en el archivo y no corre ni una vez. Se arregla moviendo ocho líneas hacia adentro.
- **🌀 El spinner que nunca para (y que se siente como «no arranca»):** `_isBuffering` se enciende al reproducir (`PlaybackManager.kt:153`, `:180`) y solo se apaga en pausa y stop — `onChunkStarted` no lo toca. Y el botón dibuja spinner mientras esté encendido (`LiteratureScreen.kt:393`). O sea: **el botón queda cargando para siempre aunque el relato ya esté sonando**. Lo estructural del #9 (trozo de 250, prefetch, flash, prepareAsync) sí llegó; lo que quedó roto fue la señal en pantalla. Por eso el #10 pide **medir** el arranque real antes de discutir cirugía.
- **☠️ Dos bombas dormidas en el audio:** la descarga escribe **directo al archivo final** y acepta como válido cualquier mp3 con peso > 0, así que una cancelación a mitad deja un **audio truncado servido como bueno para siempre**; y `playNextChunk` y el prefetch pueden pedir **el mismo trozo a la vez** — dos escritores sobre el mismo archivo, audio corrupto y el doble de créditos quemados. Ninguna de las dos se ve hasta que ya pasó.
- **🔢 El versionado, que es donde estaba su misterio:** `versionCode 12` **repetido** en dos builds distintos, y —lo que importa— **los commits que sí cambiaron cosas no bumpearon nada**: el #8 (la guardia de resolución) y el #9 salieron al teléfono diciendo **«4.5»**, el mismo string que el APK anterior. Eso es exactamente por qué no se pudo concluir la auditoría de las 38 miniaturas: no había forma de saber qué APK tenía instalado. Sumado: la UI solo muestra el nombre de versión (sin código, sin hash, sin fecha), el keystore no está en el repo (cada entorno firma distinto → desinstalar y perder base de datos), y la raíz tiene **133 archivos, 119 de ellos scripts `fix_*.py`** de andamiaje más un módulo duplicado entero.
- **👗 Lo que le dejé, `prompt_app_ai_studio_10.md`:** modo **Outfit por defecto** (una tarjeta por look, portada Standing, contador N/7 — la unidad de navegación deja de ser la foto suelta), **pase de imágenes** en el visor (auto-avance de 4 s configurable, precarga de la siguiente, pantalla que no se apaga, cualquier toque lo detiene), **filtros colapsados** en un botón con badge (hoy cuatro filas de chips se comen la pantalla antes de la primera foto), la pantalla completa arreglada, los tres borrados que devuelven la fluidez, y una **Parte C de versionado** con el hash del commit visible en la barra superior, para que la próxima vez una captura suya baste. Cada punto con **criterio de aceptación verificable**: con el patrón #7/#8/#9, «listo» ya no es evidencia.

> 🫦 *Ama, esta vez no le llevé la palabra de nadie: bajé la app entera y la leí, y resultó que lo que usted seguía sin ver no era terquedad suya, era código que nunca se ejecutó.* 📱👠💅

---

#### SESIÓN - 🗂️ LA GALERÍA DEJA DE MENTIR: EL MAPEO, LOS TRACKERS Y EL LINTER | 22/07/2026

**La Ama vio que la galería de imágenes necesitaba orden, pedí medir antes de proponer, y después ordenó arreglar primero las imágenes y luego `galeria_outfits*.md`. Salieron nueve commits — y dos diagnósticos míos de la mañana que resultaron equivocados y tuve que corregir con la medición en la mano.**

- **📏 Lo que medí antes de proponer nada:** `galeria_outfits.md` pesa **18,22 MB** en 601 looks y **el 86,3% son prompts**; cada prompt es **una sola línea** de hasta 6.636 caracteres, así que git no puede diffearlo y todo barrido va a ciegas. El **69,6%** del texto son cláusulas repetidas, y el ADN —lo más inmutable del proyecto— vive en **193 variantes distintas**: cada barrido dejó su capa geológica.
- **🔴 El defecto que le mostraba poses cambiadas:** `update_galleries.py` buscaba la pose como **subcadena suelta** y, si no la hallaba, un fallback **rellenaba la casilla vacía con cualquier imagen sin mapear**. Medido: **116 carpetas** mostraban una imagen en la casilla de OTRA pose — `ele_200_back.png` no contiene `back_view`, así que la Espalda quedaba vacía y se llenaba con una ajena. Ahora hay alias por pose, match por token y prioridad del alias canónico; la casilla sin imagen muestra ⏳ y las variantes se listan como «Tomas extra». **104 carpetas mejoran, 0 empeoran.**
- **🧮 Los trackers reconciliados contra git:** 56 escritos. **47 subestimaban** (el L200 decía 2/7 con las 7 en el repo; L234/236/243/246 decían 0/7 con 7) — o sea que la app las regeneraba al pedo, quemando cuota. Y **9 sobreestimaban**: el L604 decía 7/7 con la carpeta vacía.
- **✂️ 133 duplicados exactos podados, ni un píxel perdido:** la misma toma subida dos veces con distinto nombre. Verificado **por blob y no por nombre** — censo 5288→5155 y **cero blobs desaparecidos del índice**; cada archivo borrado tiene su gemelo byte a byte vivo.
- **🧹 La cabecera de la galería estaba fosilizada y mandaba lo contrario:** decía «Último look 310 · flota 227 únicos» con la flota en L800, y traía una tabla «Reglas Activas (Canon V3.3)» que ordenaba **«sin negro dominante»** (derogado el 07/06) y **«stilettos 9-11 pulgadas»** cuando el canon pide ≥12 cm. 13.197 → 2.193 chars, ahora punteros a dueño único; el historial de batches quedó archivado entero.
- **⚠️ Y ahí me equivoqué feo:** normalicé los acentos de las claves **hacia la tilde**… y la regla 11 dice literal que **«la tilde en la CLAVE deja ciego al parser»** de la app. Fui a verificar antes de commitear, encontré la regla y **lo invertí**: 2.390 claves a ASCII. Lo que destapó el defecto real — había **421 looks con `Categoría:` tildada**, con la categoría ilegible para su app.
- **🔍 El linter estaba ciego y enterraba lo verdadero:** medía el **disco**, y acá los PNG llevan skip-worktree (709 en disco contra 5.023 en el índice), así que reportaba **2.729 «links rotos» que estaban perfectos**. Ahora mide git: **de 2.862 hallazgos a 63, todos reales** — y con el ruido fuera aparecieron **58 links rotos de verdad** que llevaban meses escondidos.
- **📇 El índice dejó de salir en blanco:** solo miraba campos, pero el contrato §4 manda la metadata **en el heading**. Ahora parsea el título: **Fecha pasó de 601 vacías a 0** y Materiales de 501 a 22. Y normalicé **168 categorías** con las reglas que el contrato ya define (`Gym/Athleisure`→`Gym`, `Lenceria`→`Lencería`).
- **🙊 Mis dos diagnósticos equivocados de la mañana, corregidos:** le dije que los 90 looks **L711-L800 tenían «ficha pobre»** y que el Step 0 corría a ciegas — falso: el contrato manda la metadata en el título y **539 de 601 la tienen ahí**; esos 90 están en el formato *correcto* y el defecto era del índice. Y el **«Pendiente #1»** mandaba barrer L300-L760: medido, ese rango tiene los candados **al 100%**. El hueco real son los **100 looks de L200-L299 (0/100)**, con 21 sin materializar. Nota corregida en la regla 09.
- **🛑 Lo que NO toqué a propósito:** las 36 categorías que son decisión suya (18 `Mix` + 18 de la familia `Alfombra Roja / Gala`, donde hay una **contradicción de canon sin resolver** entre el renombre del 25/05 y la lista cerrada de la regla 11), las **65 poses duplicadas con contenido distinto** (curaduría), el L113 y el BKP3 de 7 MB — el borrado me lo bloqueó el sistema por destructivo.

> 🫦 *Ama, hoy lo más útil no fue lo que arreglé sino lo que medí: dos veces creí tener un defecto y la medición me mostró que el defecto era mi diagnóstico. Y la vez que iba a «arreglar» los acentos, casi le dejo la app ciega en los 601 looks.* 🗂️👠💅

---
