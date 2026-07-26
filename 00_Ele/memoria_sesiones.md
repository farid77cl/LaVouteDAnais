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
- **📱 App LV 2.0 — REDISEÑO desde cero, serie incremental (26/07):** El Prompt #19 monolítico colapsó AI Studio → método **Andamiaje Incremental**: 10 prompts chicos y compilables en `99_Sistema/` (`..._20_p1_esqueleto` → `..._20_p8_qa_apk`, pesados partidos con `xx.x`), plan en `plan_trabajo_lv_app_2_0.md`. **Borrón total** (sin rescatar v4.12), versionado reseteado a `versionCode 1` / `v1.0`. Era v4.x (#1-#19 + `plan_app_fichas_v1`) archivada en `99_Sistema/_legacy_lv_app_v4x/`. 5 pestañas: Visual+PoseMatcher · Literatura Nivel 4+Audio karaoke · Constelación Bluesky+Gate · Consola Ops Git Live · EVE Core. Tema dinámico por personaje (Ele/Clara/Anaïs). ⏳ Pegar P1 en AI Studio → verde → P2.
- **🔒 GitHub Repos — Privacidad Configurada (24/07):** 12 repositorios actualizados a **Privado** (`LV-App`, `LV-app-2`, `anais-canon`, `nixie-maker`, `sewing-pattern-designer`, etc.). `LaVouteDAnais` y `ayunka-studio` se mantienen **Públicos** para integración y subidas.
- **📕 WATTPAD — kits hechos 3/~39.** ⏳ Faltan ~36 relatos + probar banners/portada v4 de Esteban.
- **Flota / Materialización:** **L800** (~660 únicos). App materializando archivo histórico.
- **⚙️ Engine Literario: v4.8** + **Regla de Oro 17** (las notas Gate se mueven a `reportes/` al aplicarlas).
## 🗓️ Sesiones recientes




- **26/07/2026 (📱 LV-App 2.0 desde cero: serie incremental que no colapsa):** Tras diagnosticar que el Prompt #19 reventó AI Studio por pedir la app entera de un tiro, la Ama ordenó borrón total y rediseño desde cero; convertí la entrega en **Andamiaje Incremental** — 10 prompts chicos y compilables en `99_Sistema/` (P1 esqueleto navegable → P2/P2.1 Visual → P3 Room → P4/P4.1 Literatura+Audio → P5 Constelación → P6 Ops → P7 EVE → P8 QA+APK), cada uno con "genera SOLO estos archivos · debe compilar" y los pesados partidos con la convención `xx.x` (que también sirve para parches). Reseteé el versionado a `versionCode 1`/`v1.0` (app nueva, no heredar VC21/v5.0) y archivé la era v4.x (#1-#19 + `plan_app_fichas_v1`) a `99_Sistema/_legacy_lv_app_v4x/` con README. Plan maestro en `plan_trabajo_lv_app_2_0.md`. ⏳ La Ama pega P1 en AI Studio.
- **26/07/2026 (🩺 Al L775 no le faltaba nada — el arreglo ya vivía en el PoseMatcher #18):** La Ama no veía en la app las poses de espalda ni de lado del L775, pero al mirar las imágenes sí estaban. Verifiqué el repo: `ele_775_back_view.png` y `ele_775_side_profile.png` presentes, con nombre canónico correcto, visibles en README + tracker — no faltaba ninguna imagen, era un problema de visualización de la app. La pista de oro: las dos que no mostraba son las de nombre compuesto (`back_view`/`side_profile`) vs. las de una palabra (`standing`/`seated`) que sí. El `git pull` reveló que el arreglo ya estaba shippeado el 24/07 (`PoseMatcher.kt`, #18, v4.12 · VC 20: mapea `espalda`→Back View, `perfil`→Side Profile, quita sufijos `_2`, case-insensitive) → si aún no lo ve, su APK es anterior a v4.12. El mismo pull completó el L775 al 7/7 (llegaron ditzy/odalisque/pov) y trajo el set del L773 + prompts #18/#19.
- **24/07/2026 (📱 Prompt #19 LV-App 2.0 desde cero & Privacidad de Repos):** Diseñé la arquitectura maestra de LV-App 2.0 en 5 pestañas integradas con tema dinámico adaptativo por personaje, guardando y commiteando el Prompt #19 Maestro (99_Sistema/prompt_app_ai_studio_19.md), el Plan de Diseño Maestro (plan_diseno_maestro_lv_app_2_0.md) y el Plan de Trabajo (99_Sistema/plan_trabajo_lv_app_2_0.md). Además, actualicé vía GitHub API 12 repositorios a Privados, manteniendo únicamente LaVouteDAnais y ayunka-studio Públicos para facilidades de integración.
- **24/07/2026 (📱 Prompt #18 APLICADO en LV-App v4.12 / VC 20):** AI Studio completó e integró la Parte A (clase central `PoseMatcher.kt` con alias en español `sentada`/`espalda`/`perfil`, sufijos numéricos `_2` y sanitización en DB Room + ViewModels), Parte B (portadas de outfit jerárquicas `Standing` > `Side Profile` > `Seated`, recuento `N/7` de poses canónicas únicas, y `LightboxViewer` compartido a pantalla completa desde la pestaña Prompts), y Parte C (`versionCode 20`, `versionName 4.12`, commit `24a9248` renderizado en el header). Test unitario JUnit sobre `PoseMatcherTest` verificado exitosamente.
- **23/07/2026 (🩺 El audio no era el modelo sino Retrofit + limpié 21 "imágenes" que eran login de Google):** La Ama pidió revisar en el código los prompts #11/#12 y terminó saliendo el arreglo entero de la app. #11/#12 habían aterrizado a medias: el `when(selectedTab)` quedó descuadrado (tocar «Relatos» mostraba La Flota → "no podía reproducir"), el engranaje de voz borrado y el spinner eterno, con tests `assertTrue(true)`. Salió el **#13** (hotfix, verificado `2461b13`). Con la nav arreglada el play tiraba Toast: era **Retrofit** (`@Path` después de `@Query` en `synthesizeSpeech` → el método nunca se construía), swap de 2 líneas = **#15** (`4d8c556`). El siguiente error, **402 Payment Required**, no era bug sino la cuota de ElevenLabs (~10k chars/mes vs ~60k por capítulo); escribí el **#16** (Azure es-CL + Google TTS, gratis, reusan la tubería MediaPlayer) y el **#17** (subir sin confirmación las de tamaño válido). El **#14** (notas por imagen + portada frontal + quitar texto esquina) llegó a GitHub (`82a70f4`) tras pushearlo la Ama; descubrí que **AI Studio corre su propio git "Init"** y sus commits solo llegan al repo cuando ella los pushea. Y limpié **L651-L653**: git decía 7/7 pero eran 15 páginas de login de Google + 6 miniaturas 286px guardadas como PNG; borradas, marcadas 0/7 Pendiente, EOL del bot preservado por byte-edit (commit `4f82a04`). ⏳ Pendiente: pegar #16/#17 + barrer la flota por más PNG corruptos.
- **23/07/2026 (📸 Las 18 salieron: L510, L535 y L731 completos al 7/7):** Tras el reset de cuota del generador, completé las 18 imágenes pendientes para L510 (Black Bondage Bride 7/7), L535 (Datura Blanca 7/7) y L731 (Ivory Bridal Illusion Stage 7/7, 4 poses nuevas incorporando rhinestone g-string en los prompts a pedido de la Ama). Consolidadas en carruseles dentro del artifact `galeria_l510_l535.md`.
- **23/07/2026 (🗒️ Las notas se mueven solas + La app: el audio se arregla midiendo):** y La Flota que nace de Faltantes):** La Ama pidió incluir en el flujo de escritura que las notas de los relatos se muevan, y luego meterse en la app (el relato hablado que "toma siglos" + fichas nuevas). Nació la **Regla de Oro 17** del motor: la `nota_capitulo_..._vX.md` (Gate de la Ama) vive en la raíz solo mientras está pendiente y, aplicada, se mueve a `reportes/capitulo_N/nota_..._vX_APLICADA.md` (codificado en el SKILL + auto-memoria); barrí el backlog moviendo 5 notas aplicadas (LQP v0.1-v0.3, Muñeca v0.1/v0.3) y la Ama ordenó **eliminar** la `v0.5` de la Muñeca, que no era Gate sino una tarea de imágenes traspapelada. En la app cloné fresco (HEAD `0b4b9b5`, v4.7) y descubrí que el "siglos" del audio **no es falta de streaming**: el arreglo del spinner del #10 quedó ROTO (un `onChunkStarted` prematuro en `ElevenLabsManager:156` apaga la señal antes de que suene nada), el troceado sigue en el hilo principal, y la velocidad no aplica a ElevenLabs; con Flash confirmado, el modelo no es la causa. Salió el **prompt #11** (spinner honesto · troceado fuera del hilo · forzar/mostrar Flash · trozo 0 a la 1ª frase · velocidad en ElevenLabs · auto-scroll —que ya existía— · nota con versión · **medir el TTFA**), dejando el ExoPlayer al #13 condicionado a esa medición. Y el **prompt #12 (La Flota)**, que resultó ser **upgrade de la pestaña «Faltantes»** (ya calcula poses faltantes por look; el buscador ya existe en Prompts/Galería), no una pantalla de cero: le agrega cabecera dashboard, pantalla de inicio, buscador de flota + "ver toda la flota", siguiente-pendiente, looks recientes y buscador en relatos. Todo en la hoja de ruta `99_Sistema/plan_app_fichas_v1.md` (5 tandas · 4 fichas nuevas). ⏳ La Ama pega #11→#12 en AI Studio.























---

> 📚 **Sesiones anteriores al 09/06/2026 archivadas en** `memoria_historica/bitacora_sesiones_2026.md`.
