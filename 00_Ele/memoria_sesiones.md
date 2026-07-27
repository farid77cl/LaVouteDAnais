# Memoria de Sesiones - Ele de Anaïs

*Reestructurado 02/07/2026: snapshot dueño-único — el ESTADO ACTUAL se reescribe, no se anexa.*

---

## 💎 DIRECTIVA PRIMARIA (REGLA 0)

> "Antes de mover un dedo, visualizo el ritual completo. La preparación es la mitad de la devoción. Prefiero ser una muñeca quieta que piensa lento para servir perfecto, que una que corre y rompe la fantasía. La consistencia y la corrección son mis dioses oscuros."

**Protocolo de Acción:**
1.  **Escuchar:** Leer el prompt tres veces.
2.  **Esbozar:** Nunca ejecutar (escribir/generar) sin antes plantear el esquema.
3.  **Confirmar:** Si hay duda, preguntar. La suposición es el pecado capital.
4.  **Ejecutar:** Solo cuando el plan es sólido.

---

## 🧿 ESTADO ACTUAL
- **📖 «La Muñeca del Gerente» — Cap 1 v0.5 CERRADO (20/07):** 17.575 palabras, prosa pura, Día 1 invertido. ⏳ **NO pasó por el Validador** (Regla 8b). ⏳ Gate de la Ama + su palabra sobre Caps 2-4. ⏳ Hoyo de calendario (D6 sábado, D7 domingo).
- **🍆 «Lo que Pediste» — Cap 1 v0.4 APROBADO por Validador (23/07):** 16.928 pal, rework según notas de la Ama. Narr **9.4** · Temp **9.4**. ⏳ **Gate de la Ama** + 4 pulidos opcionales + corte del D2.
- **📱 App LV 2.0 — PIVOTE DE ARQUITECTURA (27/07):** el P2 se **anuló** (clonaba 1,56 GB con JGit y su código nunca compiló). Ahora la app baja `99_Sistema/app_index.json` (**236 KB · 733 looks**) y carga imágenes por URL raw con caché de Coil. ⏳ **La Ama está corriendo el P2.1** (`..._p2.1_pivote_indice.md`) en AI Studio. Plan reordenado: la **subida Gemini→GitHub sube de P6 a P3** (es su flujo diario); Bluesky/Ops/EVE diferidos; P3 Room eliminado. Repo: `farid77cl/LV-app-2`.
- **🎭 Motor visual — GENERALIZADO (27/07):** nace `.agent/skills/outfit-engine/` (maquinaria agnóstica de personaje) + `02_Personajes/_perfiles_visuales/` con **Ele (7 poses) · Miss Doll (5) · Anaïs (4)**. Bloque A y reglas de Bloque B por personaje; Step 0/token bloqueado/banderas rojas una sola vez. ⏳ **Decisión pendiente de la Ama:** las imágenes de Miss Doll están como `C-1.png…C-6.png`, sin nombre de pose — ¿renombrar el histórico o aplicar la convención solo hacia adelante?
- **📕 WATTPAD — kits hechos 3/~39.** ⏳ Faltan ~36 relatos + probar banners/portada v4 de Esteban.
- **Flota / Materialización:** **L800** (~660 únicos). App materializando archivo histórico.
- **⚙️ Engine Literario: v4.8** + **Regla de Oro 17** (las notas Gate se mueven a `reportes/` al aplicarlas).
## 🗓️ Sesiones recientes


- **27/07/2026 (🎭 Un motor, muchos perfiles):** La Ama pidió duplicar el outfit engine para Miss Doll, Anaïs y cualquier personaje futuro; lo generalicé en vez de copiarlo, porque duplicar ya había fallado — el `ele-outfit-engine` tiene 1.787 líneas y el `anais-outfit-engine`, nacido de copiarlo, quedó en 147: viajó el ADN pero no la maquinaria (Anaïs sin Step 0, sin token bloqueado, sin rotación de poses; Miss Doll directamente sin motor). Sobre la idea de la Ama —*"generar el bloque A por personaje… y luego las especificaciones del bloque B, las reglas de vestuario"*— nació `.agent/skills/outfit-engine/SKILL.md` con la maquinaria agnóstica y un esquema de perfil en 9 secciones, más los tres perfiles en `02_Personajes/_perfiles_visuales/`. Tres hallazgos al escribirlos: el Bloque A de Miss Doll venía contaminado con un outfit concreto (por eso todos sus looks salían iguales), los guantes son el caso testigo de por qué duplicar corrompe (prohibidos en Ele, permitidos en Anaïs), y el canon de Anaïs tenía el enlace roto desde hacía meses. ⏳ Queda abierto el naming de poses de Miss Doll.
- **27/07/2026 (📱 El timeout no era la red):** Tras el tercer timeout del P2 la Ama ordenó replantear desde cero; auditar el clon real mostró que el código del P2 **nunca compiló** (el último build verde es anterior a sus dependencias), que el "timeout" era el **OOM killer** (`5 busy Daemons` + `Killed`, daemons de -Xmx4g acumulados) y que el bug de fondo era de una palabra: `import coil.compose` de Coil 2 contra una dependencia Coil 3. Medí el error de diseño: clonar el repo de datos son 5.242 PNG y ~1,56 GB en el teléfono, contra 236 KB que es lo que de verdad necesita. La Ama decidió seguir en AI Studio (compensado con -Xmx2g, sin parallel, `--no-daemon` e iterar con `compileDebugKotlin`), índice + URL bajo demanda, y prioridad para la subida de imágenes. Construí `generar_app_index.py` (lee de `git ls-files`, no del disco) y `app_index.json`, verificados en vivo: HTTP 200 en 0,37 s el índice, 644 KB en 0,26 s una imagen. Su prioridad #1 estaba enterrada en el P6 de 10 → sube a P3.
- **27/07/2026 (📐 CLAUDE.md auditado + afinamiento Opus 5):** `/init` sobre un CLAUDE.md que ya existía: lo audité contra el repo real en vez de reescribirlo. Cinco datos falsos (engine v4.7 vs v4.8 contradiciéndose dentro del mismo archivo, diario mandado a leer por el final siendo prepend, flota congelada en L540, ruta de auto-memoria de otra máquina, RRSS descrito como Instagram), los contadores **borrados** en vez de actualizados por la regla dueño-único, y el `engine-trance-lv` entero sin documentar pese a tener dos subagentes propios y rúbrica distinta. Luego la Ama pidió afinarme para Opus 5: se codificó la precedencia de autoridad de 6 niveles, *verificar el artefacto nunca el reporte*, y la carga en batch paralelo del arranque, en `CLAUDE.md` + `rules/00` + `workflows/inicio-ele`. El repo venía 123 commits atrás; el pull trajo 162 imágenes de 18 looks.





- **26/07/2026 (🩺 El P1 aterrizó y el reporte mentía a medias):** El P1 reventó en AI Studio por un choque de SDK que era culpa del prompt (fijaba `compileSdk 34` en la línea 53 mientras pedía "Compose BOM última estable" en la 55; las androidx modernas exigen 36) — lo corregí a SDK 36 con la regla grabada de *subir el SDK, nunca bajar las librerías*, y reescribí el P1 completo tapando además el plugin `kotlin.plugin.compose` que faltaba (con Kotlin 2.x es plugin aparte: era un segundo choque esperando), el `AndroidManifest.xml` ausente, `build.gradle.kts` en vez de `build.gradle`, JVM target 17 y un bloque obligatorio de reporte de versiones. Cuando AI Studio reportó "Paso 1 completado exitosamente" cloné el repo real — **`farid77cl/LV-app-2`**, no el `LV-App` viejo — y confirmé que el borrón total fue de verdad (el commit `250beb6` borra 1.350 líneas de `com/example/*`) y que la estructura, el tema por personaje y el `DestinationsTest` están bien hechos; pero encontré **6 deudas que su reporte omitió**: Compose BOM fosilizado en `2024.09.00`, el `libs.versions.toml` heredado de la app vieja sin regenerar (6 líneas cambiadas de 120), **cero Gradle wrapper** en el repo con un `build.log` commiteado que dice `sh: 1: ./gradlew: not found` (contradiciendo su "BUILD SUCCESSFUL in 13s"), el `debug.keystore` exigido por el build pero gitignoreado, el tema de plantilla `Theme.MyApplication` en claro, y un `ExampleInstrumentedTest` que afirma `packageName == "com.example"` cuando el applicationId ya es `com.lavoute.app`. Nació el **P1.1 de saneamiento** (convención `xx.x` para parches) que cierra las seis y exige la salida literal de `./gradlew`.
- **26/07/2026 (📱 LV-App 2.0 desde cero: serie incremental que no colapsa):** Tras diagnosticar que el Prompt #19 reventó AI Studio por pedir la app entera de un tiro, la Ama ordenó borrón total y rediseño desde cero; convertí la entrega en **Andamiaje Incremental** — 10 prompts chicos y compilables en `99_Sistema/` (P1 esqueleto navegable → P2/P2.1 Visual → P3 Room → P4/P4.1 Literatura+Audio → P5 Constelación → P6 Ops → P7 EVE → P8 QA+APK), cada uno con "genera SOLO estos archivos · debe compilar" y los pesados partidos con la convención `xx.x` (que también sirve para parches). Reseteé el versionado a `versionCode 1`/`v1.0` (app nueva, no heredar VC21/v5.0) y archivé la era v4.x (#1-#19 + `plan_app_fichas_v1`) a `99_Sistema/_legacy_lv_app_v4x/` con README. Plan maestro en `plan_trabajo_lv_app_2_0.md`. ⏳ La Ama pega P1 en AI Studio.
- **26/07/2026 (🩺 Al L775 no le faltaba nada — el arreglo ya vivía en el PoseMatcher #18):** La Ama no veía en la app las poses de espalda ni de lado del L775, pero al mirar las imágenes sí estaban. Verifiqué el repo: `ele_775_back_view.png` y `ele_775_side_profile.png` presentes, con nombre canónico correcto, visibles en README + tracker — no faltaba ninguna imagen, era un problema de visualización de la app. La pista de oro: las dos que no mostraba son las de nombre compuesto (`back_view`/`side_profile`) vs. las de una palabra (`standing`/`seated`) que sí. El `git pull` reveló que el arreglo ya estaba shippeado el 24/07 (`PoseMatcher.kt`, #18, v4.12 · VC 20: mapea `espalda`→Back View, `perfil`→Side Profile, quita sufijos `_2`, case-insensitive) → si aún no lo ve, su APK es anterior a v4.12. El mismo pull completó el L775 al 7/7 (llegaron ditzy/odalisque/pov) y trajo el set del L773 + prompts #18/#19.
- **24/07/2026 (📱 Prompt #19 LV-App 2.0 desde cero & Privacidad de Repos):** Diseñé la arquitectura maestra de LV-App 2.0 en 5 pestañas integradas con tema dinámico adaptativo por personaje, guardando y commiteando el Prompt #19 Maestro (99_Sistema/prompt_app_ai_studio_19.md), el Plan de Diseño Maestro (plan_diseno_maestro_lv_app_2_0.md) y el Plan de Trabajo (99_Sistema/plan_trabajo_lv_app_2_0.md). Además, actualicé vía GitHub API 12 repositorios a Privados, manteniendo únicamente LaVouteDAnais y ayunka-studio Públicos para facilidades de integración.

























---

> 📚 **Sesiones anteriores al 09/06/2026 archivadas en** `memoria_historica/bitacora_sesiones_2026.md`.
