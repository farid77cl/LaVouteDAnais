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
| **P1** | `prompt_app_ai_studio_20_p1_esqueleto.md` | Gradle + Clean Arch + Tema dinámico (Ele/Clara/Anaïs) + NavigationBar 5 pestañas (4 placeholder). App abre y navega. |
| **P2** | `prompt_app_ai_studio_20_p2_visual.md` | Pestaña **Visual** núcleo: GitRepository + PoseMatcher + Galería N/7 con portada jerárquica. |
| **P2.1** | `prompt_app_ai_studio_20.1_visual_lightbox_prompts.md` | Visual: **Lightbox** (pinch-zoom) + **Creador de Prompts V3.5** (copiar 1-tap). |
| **P3** | `prompt_app_ai_studio_20_p3_room.md` | Capa **Datos Room**: entidades + DAOs + persistencia offline + notas por imagen (CSV). |
| **P4** | `prompt_app_ai_studio_20_p4_literatura.md` | Pestaña **Literatura**: Lector Nivel 4 (Luxe Serif, OLED, guarda avance). |
| **P4.1** | `prompt_app_ai_studio_20.4_audio_player.md` | **Audio**: PlaybackService Media3 + TTS multivoz (Azure es-CL/Google/ElevenLabs) + karaoke sync. |
| **P5** | `prompt_app_ai_studio_20_p5_constelacion.md` | Pestaña **La Constelación**: Bluesky + Caption Factory (voz Ele) + Gate 1-tap. |
| **P6** | `prompt_app_ai_studio_20_p6_ops.md` | Pestaña **Consola Ops**: flota L200-L800 por tramo + siguiente pendiente + Git Live Sync. |
| **P7** | `prompt_app_ai_studio_20_p7_eve.md` | Pestaña **EVE Core**: asistente de comandos texto/voz. |
| **P8** | `prompt_app_ai_studio_20_p8_qa_apk.md` | **QA + APK**: suite de tests real + `LV-App-v1.0-release.apk`. |

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
