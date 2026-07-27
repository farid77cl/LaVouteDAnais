# 📋 Plan de Trabajo Maestro: LV-App 2.0 — Andamiaje Incremental

> **Objetivo:** Construir **LV-App 2.0** desde cero (**borrón total** — sin arrastrar código de la v4.12). Versionado **reseteado** (app nueva): `versionCode 1` · `versionName "1.0"`. *("2.0" es el nombre de generación del producto; "1.0" es la primera build de este código nuevo.)*
>
> **Entorno:** Google AI Studio / GitHub (`farid77cl/LV-App`) / Android Studio (Kotlin, Jetpack Compose, Room, Media3, Material 3).
>
> **Método (rev. 26/07/2026):** ~~Prompt #19 monolítico~~ **SUPERSEDED** — colapsó AI Studio por pedir la app entera en un solo prompt. Se reemplaza por **Andamiaje Incremental**: una serie de prompts pequeños, cada uno entrega algo **que compila y corre**. AI Studio nunca escupe la app completa de una vez, y un fallo se aísla a un solo paso.

---

## 🧱 Principios del Andamiaje Incremental

1. **Cada prompt = un incremento compilable.** Al terminar cada paso, la app buildea y corre.
2. **"Genera SOLO estos archivos · no toques nada más."** Alcance cerrado por prompt.
3. **Verificar → pushear → siguiente.** No se avanza al paso N+1 hasta que el N buildea verde.
4. **Tests reales, nunca `assertTrue(true)`.**
5. **Borrón total:** todo se regenera desde cero (decisión de la Ama 26/07). No se porta código v4.12.

---

## 🗺️ Serie de Prompts (reemplaza al #19)

| Paso | Prompt (archivo) | Entrega (compilable) |
| :--- | :--- | :--- |
| **P1** ✅ | `prompt_app_ai_studio_20_p1_esqueleto.md` | Gradle + Clean Arch + Tema dinámico (Ele/Clara/Anaïs) + NavigationBar 5 pestañas (4 placeholder). App abre y navega. **HECHO 26/07 — commit `250beb6` en `farid77cl/LV-app-2`.** |
| **P1.1 / P1.2** ✅ | `..._p1.1_saneamiento.md` · `..._p1.2_parche_build.md` | Saneamiento del build: wrapper, keystore, tema oscuro, purga del catálogo. **Aterrizaron a medias pero el build quedó verde** (`build_assemble_2.log`). |
| ~~**P2**~~ ❌ | ~~`..._p2_visual.md`~~ | **ANULADO 27/07.** Su diseño clonaba el repo de datos con JGit: **~1,56 GB** en el teléfono. El código se pusheó (`59a32b6`) pero **nunca compiló**. |
| **P2.1** ⏳ | **`..._p2.1_pivote_indice.md`** | **Pivote de arquitectura:** fuera JGit y PoseMatcher. La app baja `app_index.json` (**236 KB**) y carga cada imagen por URL con caché de Coil. Entrega la **pestaña Visual** con galería real, N/7 y portada. ← **PEGAR AHORA** |
| **P2.2** | `prompt_app_ai_studio_20.1_visual_lightbox_prompts.md` | Visual: **Lightbox** (pinch-zoom) + **Creador de Prompts V3.5** (copiar 1-tap). *(Adaptar: ya no lee del repo clonado, lee del índice.)* |
| **P3** 🔝 | *por escribir* | **SUBIDA Gemini → GitHub.** El flujo que la Ama usa a diario: elegir look/pose, pegar o seleccionar el PNG, subir al repo con nombre canónico vía GitHub Contents API. **Sube desde el P6** por prioridad de la Ama (27/07). |
| **P4** | `prompt_app_ai_studio_20_p4_literatura.md` | Pestaña **Literatura**: Lector Nivel 4 (Luxe Serif, OLED, guarda avance). |
| **P4.1** | `prompt_app_ai_studio_20.4_audio_player.md` | **Audio**: PlaybackService Media3 + TTS multivoz (Azure es-CL/Google/ElevenLabs) + karaoke sync. |
| **P5** | `prompt_app_ai_studio_20_p8_qa_apk.md` | **QA + APK**: suite de tests real + `LV-App-v1.0-release.apk`. |
| **P6+** ⏸️ | `..._p5_constelacion.md` · `..._p6_ops.md` · `..._p7_eve.md` | **DIFERIDOS** (Bluesky · Consola Ops · EVE Core). La Ama los puso en última prioridad el 27/07. |

> ~~**P3 Room**~~ **ELIMINADO.** Room existía para persistir el repo clonado. Con el índice de 236 KB + caché de Coil, una base de datos no aporta nada: se cachea el JSON crudo en `filesDir`. Una dependencia pesada menos.

---

## 🔄 Replanteo del 27/07/2026 (tras el tercer timeout)

**Qué se replanteó y por qué.** El P2 dio timeout tres veces. La auditoría del clon real (`59a32b6`) mostró que el problema no era la red que reportaba AI Studio:

- **El código del P2 nunca compiló.** El último `BUILD SUCCESSFUL` es anterior a las dependencias que el P2 agregó. Se pusheó código roto.
- **El `Killed` era el OOM killer**, no la red: `output.txt` dice *"5 busy Daemons could not be reused"* — cinco daemons de Gradle a `-Xmx4g` acumulados por reintentos sin arreglar la causa.
- **El bug de fondo era de una palabra:** `import coil.compose.AsyncImage` (Coil 2) contra una dependencia Coil 3 (`coil3.compose`).
- **Y el diseño era el equivocado:** clonar 1,56 GB en el teléfono.

**Decisiones de la Ama (27/07):**

| Decisión | Elegido | Consecuencia |
|---|---|---|
| Dónde se compila | **Seguir en AI Studio** | Se compensa con toolchain liviano: `-Xmx2g`, `parallel=false`, `--no-daemon`, iterar con `compileDebugKotlin` (barato) y no con `assembleDebug` |
| Datos e imágenes | **Índice + URL bajo demanda** | Fuera JGit, fuera Room, fuera PoseMatcher-en-Kotlin |
| Qué va primero | **Subir imágenes · Galería+prompts · Literatura+audio** | Bluesky/Ops/EVE diferidos; la subida sube de P6 a P3 |

**Medición que respalda el pivote:**

| | |
|---|---|
| `clone --depth 1` del repo de datos | **~1,56 GB** · 5.242 PNG |
| `app_index.json` | **236 KB** · 733 looks · 4.190 imágenes |
| Una imagen bajo demanda | **644 KB · 0,26 s** (verificado `HTTP 200` sobre raw público) |

**Acoplamiento nuevo (barato pero real):** `app_index.json` hay que **regenerarlo y commitearlo** cuando entran imágenes nuevas, con
`python 99_Sistema/scripts/visual/generar_app_index.py`. Va al cierre de sesión, junto a `update_galleries.py`. Si no se regenera, la app no ve los looks nuevos.

> **Convención de numeración (Ama 26/07):** pasos principales = enteros (P1…P8); los grandes se parten con **xx.x** (P2.1, P4.1); y **cualquier parche** a un paso que aterrice roto también va como **xx.x** (ej. P2.2, P4.2).
> **Primer slice acordado:** *Esqueleto + Pestaña Visual* → P1 + P2 (+ P2.1), en prompts chicos, no en uno, para no re-colapsar.

---

## 🎀 Visión de producto (las 5 pestañas)

1. 👗 **Visual & Prompts** — Motor V3.5 (creador de prompts + copiar 1-tap), Galería N/7, portada jerárquica (`Standing > Side Profile > Seated`), Lightbox con pinch-to-zoom.
2. 📖 **Literatura & Audio** — Lector Nivel 4 (Luxe Serif, fondo OLED `#0B0612`, guarda avance) + player multivoz con sync karaoke.
3. 🚀 **La Constelación** — Bluesky Publisher, Caption Factory (voz cuica de Ele), Gate de la Ama en 1 toque.
4. ⚡ **Consola Ops** — estado flota L200-L800 + Git Live Sync.
5. 🔮 **EVE Core** — asistente de comandos por texto/voz.

**Tema Dinámico Adaptativo:** Ele = `#FF2B85` (Hot Magenta) · Clara = Cherry Red/Leopard Gold · Anaïs = `#D4AF37` (Imperial Gold)/Velvet. Estética *Dark Luxe / Glassmorphism / Vintage Noir* + Material 3, fondo OLED `#0B0612`.

---

## 📝 Registro de Autorización de la Ama
* **Aprobado por:** Señora Ama Anaïs
* **Fecha:** 24/07/2026 (visión) · **replanteo incremental 26/07/2026**
* **Estado:** P1 listo para pegar en AI Studio.
