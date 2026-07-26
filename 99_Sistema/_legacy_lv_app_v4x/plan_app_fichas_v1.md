# 🗺️ Hoja de Ruta — Adiciones a LV-App (v1 · 23/07/2026)

> **App:** `farid77cl/LV-App` (Kotlin / Jetpack Compose / Room / Retrofit / Moshi / Coil).
> **Base auditada:** commit `0b4b9b5` ("fix: improve gallery scroll reset and state flow"), `versionCode = 14`, `versionName = "4.7"`.
> **Origen:** la Ama pidió (23/07) arreglar el relato hablado que *"sigue tomando siglos"* + pensar adiciones **en toda la app, incluso fichas nuevas**. Este documento es el dueño único del plan; los prompts a AI Studio (`prompt_app_ai_studio_N.md`) ejecutan cada tanda.

---

## ✅ Adiciones aprobadas por la Ama (23/07)

| Adición | Estado en el código de hoy | Dónde entra |
|---|---|---|
| **Velocidad de lectura** | Existe para la voz del **sistema** (`ttsSpeechRate`); **ElevenLabs la ignora** (MediaPlayer no la aplica). | #11 |
| **Auto-scroll del texto** | **YA existe** (básico): `LiteratureScreen.kt:451-461` hace `animateScrollToItem` al cambiar de trozo. Solo pulir el match. | #11 (pulido) |
| **Compositor de "Comentarios" con versión** | El botón existe (`LiteratureScreen.kt:411`) y sube `nota_${generatedFileTitle}.md`; **no marca la versión del capítulo** que revisa. | #11 |
| **Checklist de materialización** | **Medio hecho:** la pestaña «Faltantes» (`SummaryScreen`) ya calcula poses faltantes por look y salta al prompt para copiar. | #12 (se pule en «La Flota») |
| **Buscador** | **Ya existe** en Prompts (`_promptSearchQuery`) y Galería (`_galleryLookSearchQuery`); falta en La Flota y Relatos. | #12 |

## 🆕 Fichas nuevas aprobadas (todas, 23/07)

| Ficha | Qué es | Datos que ya existen |
|---|---|---|
| 🏛️ **La Flota** | Pantalla de inicio / centro de mando: anillo de progreso, poses que faltan por look, últimos subidos + checklist + buscador. **Es upgrade de la pestaña «Faltantes» que ya existe** (`SummaryScreen`), no una pantalla de cero. | Lee la galería que la app ya consume. |
| 🎧 **Audioteca** | Repisa tipo podcast de los relatos: continuar escuchando, offline, cola, temporizador de sueño, saltar párrafo en la notificación. | Necesita el audio del #11 firme. |
| 👗 **El Vestidor** | Step 0 Anti-Repetición hecho pantalla: sub-arquetipo → últimas 3 siluetas → brief. | Lógica de anti-repetición del engine visual. |
| ⚰️ **Cementerio** | Galería de descartes por motivo. | `DescarteEntity` / `99_Sistema/descartes.csv` ya existen. |

---

## 📦 Tandas (una por prompt, para que nada llegue inerte)

| Tanda | Contenido | Por qué ahí |
|---|---|---|
| **#11 · Audio cierto + lector** | Spinner honesto (quitar el `onChunkStarted` prematuro) · troceado fuera del hilo principal · forzar/mostrar Flash · trozo 0 al primer punto · velocidad en ElevenLabs · pulir auto-scroll · nota con versión · **MEDIR el TTFA real** | Es lo que duele hoy. Todo del dominio lector, riesgo bajo, se prueba junto. |
| **#12 · Ficha «La Flota»** (+ checklist + buscador) — ✍️ `prompt_app_ai_studio_12.md` LISTO | Sube de nivel la pestaña «Faltantes»: cabecera dashboard (% materializado, poses que faltan), buscador de flota + "ver toda la flota", siguiente-pendiente, looks recientes, buscador en relatos. | Su dolor más repetido; independiente del audio. |
| **#13 · ExoPlayer streaming (CONDICIONAL) + Ficha «Audioteca»** | Streaming progresivo *gapless* **solo si el TTFA medido en el #11 sigue alto** + la repisa podcast. | Cirugía mayor: se hace si la medición la justifica, no por fe. |
| **#14 · Ficha «El Vestidor»** | Planificador Step 0. | No urge; alimenta el motor sin repetir. |
| **#15 · Ficha «Cementerio»** | Descartes por motivo. | La más chica; el dato ya existe. |

### ⚠️ Decisión de método (23/07)

El #10 **pospuso a propósito** el streaming real y pidió **medir antes de operar** (su punto B8). Al auditar el código de hoy se descubrió que el arreglo del spinner del #10 **quedó roto** (`ElevenLabsManager.kt:156` dispara `onChunkStarted` *antes* de descargar el audio → apaga la señal de "cargando" antes de que suene nada). Es decir: la hipótesis "arreglar solo la señal" **nunca se probó de verdad**. Por eso el #11 arregla la señal **bien** + el troceado + fuerza Flash + achica el trozo 0 **y mide el TTFA**; el ExoPlayer (riesgoso: toca el `PlaybackService` en primer plano que hoy funciona) queda en el #13 **condicionado a esa medición**. Medir antes de cortar.

---

*Dueño único del plan de la app. Cualquier cambio de alcance se hace acá, no en la memoria del agente.*
