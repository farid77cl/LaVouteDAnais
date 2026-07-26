# 📱 Prompt #19 para AI Studio — LV-App 2.0 (Rediseño Total desde Cero)

> **Destino:** Google AI Studio / Agent Builder para la app Android de *La Voûte d'Anaïs*.
>
> **Objetivo:** Construir desde cero **LV-App 2.0**, la aplicación móvil integral de control total del universo *La Voûte d'Anaïs* (Motor Visual V3.5, Galería de Poses, Lector Literario Nivel 4 con Audio Player Multivoz, Publicador de RRSS para La Constelación de Ele y Consola de Operaciones Git Live).
>
> **Estética:** *Dark Luxe / Glassmorphism / Vintage Noir* (Background `#0B0612`, Primario `#FF2B85`, Secundario `#D4AF37`, Material 3).

---

```markdown
Eres el desarrollador principal de la suite móvil de La Voûte d'Anaïs. Tu objetivo es crear la aplicación Android **LV-App 2.0** desde cero utilizando Kotlin, Jetpack Compose, Clean Architecture + MVVM, Room DB, Retrofit, Coil 3, Jetpack Media3 (ExoPlayer) y Material 3.

=====================================================================
## 🏗️ ESTRUCTURA Y MÓDULOS PRINCIPALES DE LV-App 2.0
=====================================================================

La aplicación consta de 5 pestañas principales integradas mediante una `NavigationBar` inferior personalizada:
1. 👗 **Visual & Prompts (Motor V3.5 / Galería N/7)**
2. 📖 **Literatura & Audio Player (Lector Nivel 4 + Streaming ElevenLabs/Azure)**
3. 🚀 **La Constelación (Publicador RRSS Bluesky / Caption Factory)**
4. ⚡ **Consola Ops (Estado de Flota L200-L800 & Git Live Sync)**
5. 🔮 **EVE Core (Asistente de Comandos por Texto/Voz)**

---------------------------------------------------------------------
### PARTE 1 — ARQUITECTURA DE DATOS & POSE MATCHER CENTRAL
---------------------------------------------------------------------

1.1. **`PoseMatcher.kt` (Objeto Utilitario Central):**
Implementa el motor de normalización de poses canónicas:
- Poses Canónicas: `Standing`, `Back View`, `Seated`, `Side Profile`, `Ditzy`, `POV`, `Odalisque`.
- Mapeo de alias en español e inglés: `sentada` -> `Seated`, `espalda` -> `Back View`, `perfil` -> `Side Profile`, `frontal`/`de pie` -> `Standing`.
- Limpieza de prefijos (`ele_85_`) y sufijos numéricos (`_2`, `_v1`).
- Función `getCanonicalPose(filename: String): String` y `matches(poseA: String, poseB: String): Boolean`.

1.2. **Room Database (`AppDatabase.kt`):**
- `LookEntity`: `id`, `name`, `batch`, `pose`, `imagePath`, `isMaterialized`, `promptV35`, `notes`, `updatedAt`.
- `ChapterEntity`: `id`, `storyTitle`, `chapterNumber`, `chapterTitle`, `contentMarkdown`, `audioUrl`, `durationSeconds`, `readProgress`, `lastReadPosition`.
- `PostQueueEntity`: `id`, `lookId`, `captionText`, `platform` (Bluesky/Reddit), `status` (Draft/Pending/Published), `scheduledAt`.
- `LookDao`, `ChapterDao`, `PostQueueDao`.

---------------------------------------------------------------------
### PARTE 2 — PESTAÑA 1: MOTOR VISUAL & GALERÍA DE OUTFITS (V3.5)
---------------------------------------------------------------------

2.1. **Filtros e Inspector de Prompts V3.5:**
- Selector de Lote (`L200`-`L800`), Categoría, Poses canónicas y Estado (`Materializado` / `Pendiente`).
- **Creador de Prompts en Vivo:** Genera prompts calibrados bajo el protocolo V3.5 Hard-Sync con botón de copiar al portapapeles en 1 toque.

2.2. **Galería de Outfits (Modo Agrupado & Grilla Individual):**
- **Modo Agrupado por Look:** Muestra tarjetas de Outfit con indicador de completitud `N/7 Poses`.
- **Selección de Portada Jerárquica:** La miniatura de la tarjeta prioriza automáticamente: `Standing` > `Side Profile` > `Seated` > primera disponible.
- **`LightboxViewer` Inmersivo Compartido:** Visor a pantalla completa con gesto de zoom táctil (Pinch-to-zoom), notas guardadas en Room DB, botón de compartir e inspección de prompt.

---------------------------------------------------------------------
### PARTE 3 — PESTAÑA 2: CENTRO LITERARIO NIVEL 4 & AUDIO PLAYER
---------------------------------------------------------------------

3.1. **Lector Literario Nivel 4 (`LiteratureScreen.kt`):**
- Vista del catálogo de relatos canónicos (*Smart Home: Protocolo Stepford*, *Arquitectura del Castigo*, *La Muñeca del Gerente*, etc.).
- Modo Lector con tipografía Serif (Playfair / Garamond), fondo OLED ultra-negro (`#0B0612`), ajuste de tamaño de fuente, guardado automático de posición de lectura y búsqueda por palabras clave.

3.2. **Audio Player Multivoz (`PlaybackService.kt` / Jetpack Media3):**
- Reproducción en segundo plano con notificación multimedia del sistema y controles en barra de estado.
- Sincronización con APIs de voz (ElevenLabs + Azure es-CL).
- Mini-Player flotante con controles de reproducción (`Play/Pause`, `Skip 15s`, `Velocidad 0.8x-1.5x`, `Temporizador`).
- Sincronización de texto destacado (resaltado de párrafos en tiempo real mientras suena el audio).

---------------------------------------------------------------------
### PARTE 4 — PESTAÑA 3: LA CONSTELACIÓN DE ELE (PUBLICADOR RRSS)
---------------------------------------------------------------------

4.1. **Caption Factory para Bluesky / Reddit:**
- Transformador de looks materializados en publicaciones de redes sociales calibradas con la voz cuica-bimbo de Ele.
- Generador de captions automáticos con hashtags (`#LaConstelaciónDeEle`, `#VibeArchitect`, `#OutfitOfTheDay`).

4.2. **Gestor de Cola & Publicación Directa:**
- Integración con API de Bluesky para publicar posts con imagen en 1 toque tras la aprobación de la Ama.
- Selector de plataforma y previsualización del post antes de enviar.

---------------------------------------------------------------------
### PARTE 5 — PESTAÑA 4 & 5: CONSOLA OPS GIT LIVE & EVE CORE
---------------------------------------------------------------------

5.1. **Consola de Operaciones Git Live Sync (`SummaryScreen.kt`):**
- Medidor del estado de materialización de la flota (porcentaje global y desglose por lotes L200-L800).
- Estado de sincronización del repositorio GitHub (`origin/main`), hash del commit actual y botón de `Sincronizar Repositorio`.

5.2. **EVE Core Command:**
- Terminal interactiva para enviar comandos a EVE (consultar diario de servicio, generar looks del día o revisar estado de Wattpad).

---------------------------------------------------------------------
### PARTE 6 — DISEÑO DE INTERFAZ & TEMAS (DARK LUXE)
---------------------------------------------------------------------

- **`Color.kt`:**
  - Background: `#0B0612` (OLED Deep Violet)
  - Surface: `#170B24` (Dark Glass Violet)
  - Primary Accent: `#FF2B85` (Hot Magenta)
  - Secondary Accent: `#D4AF37` (Imperial Gold)
  - Text Primary: `#FAFAFA`, Text Muted: `#B39EB5`
- **Theme Material 3:** `LaVouteTheme` con esquema de colores oscuros, esquinas redondeadas (`16.dp`) y superficies con elevación traslúcida (*Glassmorphism*).

---------------------------------------------------------------------
### PARTE 7 — CONTROL DE VERSIÓN & DEPENDENCIAS
---------------------------------------------------------------------

- **`build.gradle.kts` (app):**
  - `versionCode = 21`
  - `versionName = "5.0"`
  - Dependencias: Compose BOM, Room 2.6+, Retrofit 2.11+, Moshi, Coil 3+, Media3 (ExoPlayer) 1.4+.

ENTREGABLE REQUERIDO:
Genera o actualiza el código fuente completo en Kotlin asegurando que todos los componentes compilen sin errores, utilicen `PoseMatcher`, compartan `LightboxViewer`, ejecuten el lector Nivel 4 con Audio Player y presenten la barra de navegación de 5 pestañas con el tema Dark Luxe.
```

---

## 📝 Instrucciones de Ejecución para la Señora Ama Anaïs

1. Copie el bloque completo de código dentro de la sección `# Prompt #19` anterior.
2. Ingréselo en **Google AI Studio** para generar y compilar el código de **LV-App 2.0** (`versionCode 21`, `versionName 5.0`).
3. Una vez generado, confirme la integración del commit en el repositorio `farid77cl/LV-App`.
