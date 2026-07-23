# 📱 Prompt #12 para AI Studio — La ficha «La Flota»: la pestaña Faltantes se convierte en centro de mando (dashboard + checklist + buscador)

> **Base:** repo `farid77cl/LV-App`. Escrito sobre el commit **`0b4b9b5`** (`versionCode 14`, `versionName 4.7`). **Aplicar DESPUÉS del #11** y rebasar sobre el commit que deje el #11 — este prompt toca `SummaryScreen.kt`, `LaVouteApp.kt`, `MainViewModel.kt` y `LookDao.kt`, casi sin solaparse con el audio del #11.
>
> **Todo lo de abajo está verificado leyendo el código clonado, con archivo y línea.** No es una pantalla de cero: es subir de nivel algo que ya existe.
>
> **Alcance:** SOLO la ficha de flota/materialización + un buscador. El flujo de subida de imágenes NO se toca.

---

## 🔍 ESTADO ACTUAL — qué ya existe (para no reinventarlo)

Auditado en el código de hoy:

| Pieza | Estado | Evidencia |
|---|---|---|
| Pestaña **«Faltantes»** (4ª tab) | ✅ Existe | `LaVouteApp.kt:177-190` → tab 3 → `SummaryScreen` (`:211`) |
| **Cálculo de poses que faltan por look** (prompts vs imágenes) | ✅ Ya lo hace | `SummaryScreen.kt:42-60` (`missingSummary`) |
| Tocar una pose faltante → salta a su **prompt para copiar** | ✅ Ya lo hace | `SummaryScreen.kt:167-171` (`selectLookNumber`+`selectPose`+`selectTab(0)`) |
| **Copiar el prompt** al portapapeles | ✅ Ya funciona | `PromptFilterScreen.kt:704-708` ("Prompt copiado 🌸") |
| **Buscador** en Prompts y en Galería (persistidos) | ✅ Ya existen | `MainViewModel.kt:57` (`_promptSearchQuery`), `:446` (`_galleryLookSearchQuery`) |
| Frecuencias por categoría/etiqueta (barras) | ✅ Reutilizable | `GalleryStats.kt:36-54`, `SimpleBarChartRow` (`:104`) |
| **Cabecera dashboard / anillo de progreso** | ❌ No existe | `SummaryScreen.kt` solo dice "Faltan N imágenes" (`:110-115`) |
| **Buscador dentro de la flota** (saltar a un look) | ❌ No existe | — |
| Buscador en **Relatos** | ❌ No existe | — |

**Traducción:** el motor de "qué falta" ya está y es correcto. Lo que falta es la **cara de centro de mando** (el número grande de un vistazo, el progreso, el salto rápido) y coser el buscador donde no está. Este prompt NO reescribe el cálculo de faltantes: lo envuelve.

---

```
Eres el desarrollador de LV-App (Kotlin / Jetpack Compose / Room / Retrofit / Moshi / Coil).
Trabaja sobre el repo al día (aplica este prompt DESPUÉS del #11).

CONTEXTO: los puntos de abajo están sobre TU código, con archivo y línea. Ejecuta; no reescribas
lo que ya funciona. El cálculo de faltantes (SummaryScreen.kt:42-60) es correcto: se REUTILIZA,
no se rehace. Si discrepas de algo, dilo al final en "NO HECHO:" con evidencia.

⭐ INTOCABLE: el flujo de subida de imágenes (portapapeles, selector de galería, guardia de
resolución, share). No se toca ni un archivo de esa ruta.

#####################################################################
##  PARTE A — LA PESTAÑA «FALTANTES» SE CONVIERTE EN «LA FLOTA» (CENTRO DE MANDO)
#####################################################################

Renombra y sube de nivel la 4ª pestaña. Hoy es "Faltantes" (LaVouteApp.kt:177-190) → SummaryScreen.
Pasa a llamarse "La Flota" y a ser la pantalla de inicio.

=====================================================================
A1. LA FLOTA ES LA PANTALLA DE INICIO (primera pestaña)
=====================================================================
- En la NavigationBar (LaVouteApp.kt:134-190), mueve "La Flota" al PRIMER lugar (izquierda), con
  icono Icons.Default.Dashboard (o Icons.Default.Home) y label "La Flota". Las otras tres
  (Prompts, Galería, Relatos) corren a la derecha, en ese orden.
- Reordena en consecuencia el `when (selectedTab)` (LaVouteApp.kt:207-212): 0 → La Flota
  (SummaryScreen), 1 → PromptFilterScreen, 2 → ImageGalleryScreen, 3 → LiteratureScreen.
- Corrige TODOS los `selectTab(n)` del código que apuntan a esos índices (p. ej.
  SummaryScreen.kt:129,170 hoy hacen selectTab(0) para ir a Prompts → ahora es selectTab(1)).
  Búscalos todos con grep de `selectTab(`; ninguno puede quedar apuntando al índice viejo.
- Default de apertura: `selectedTab = 0` (La Flota). Si hay un valor persistido de una versión
  anterior, que no rompa (coérce al rango 0..3).

CRITERIO DE ACEPTACIÓN: la app abre en «La Flota»; tocar una pose faltante sigue llevando al
prompt correcto (no a otra pestaña).

=====================================================================
A2. CABECERA DASHBOARD — el número grande de un vistazo (lo nuevo, el corazón)
=====================================================================
Arriba de SummaryScreen, antes de la lista, agrega una cabecera de comando calculada de
allLooks + allPrompts + allImages (los tres ya están inyectados, :32-34):

  - Un ANILLO (o barra gruesa) de progreso con el % materializado global =
        poses con imagen / poses totales con prompt   (usa matchesPoseLocal, :205, para contar).
  - Tres números grandes en fila:
        🏛️ <looks totales>        ✅ <looks 7/7 completos>        ⏳ <poses que faltan>
    donde "completo" = un look con ≥1 prompt y 0 poses faltantes.
  - Una línea chica: "N looks con algo pendiente" (= missingSummary.size).

Usa VelvetCardLight y los colores del tema (MintTeal, la primaria) para que combine con el resto.
Puedes reutilizar SimpleBarChartRow de GalleryStats.kt para la barra si no quieres dibujar el anillo.

CRITERIO DE ACEPTACIÓN: al abrir La Flota se ve, sin desplazar, el % materializado y cuántas poses
faltan en total; los números cuadran con la suma de la lista de abajo.

=====================================================================
A3. CHECKLIST — "siguiente pendiente" y copiar en orden
=====================================================================
La lista de faltantes ya existe (SummaryScreen.kt:117-195) y al tocar una pose se copia su prompt.
Agrega, en la cabecera, UN botón "▶ Siguiente pendiente" que:
  - toma la primera pose faltante del look pendiente de número más bajo (o más alto — el orden que
    ya usa la lista), hace selectLookNumber + selectPose + salta a la pestaña Prompts y deja el
    prompt listo para copiar (como ya hace el toque de pose).
Así se puede ir "tacha y siguiente" sin buscar a mano cuál sigue.

CRITERIO DE ACEPTACIÓN: con al menos una pose faltante, "Siguiente pendiente" abre el prompt de esa
pose en la pestaña Prompts.

=====================================================================
A4. LOS LOOKS MÁS RECIENTES (proxy de "lo último")
=====================================================================
Debajo de la cabecera, una fila horizontal desplazable con los 8 looks de mayor número que tengan
al menos una imagen: miniatura (portada standing si existe), "L### · N/M". Tocarla abre ese look en
la Galería. (ImageEntity no guarda fecha de subida; el número de look es el proxy honesto de "lo
último" — no inventes un timestamp.)

CRITERIO DE ACEPTACIÓN: la fila muestra los looks de número más alto con imagen y cada uno abre la
Galería en ese look.

#####################################################################
##  PARTE B — BUSCADOR
#####################################################################

=====================================================================
B1. BUSCADOR DE LA FLOTA
=====================================================================
En la cabecera de La Flota, una barra de búsqueda (OutlinedTextField, como la que ya se usa en
PromptFilterScreen.kt:316) que filtra la lista de looks por: número, nombre, categoría, color y
tags (todo lo que trae LookEntity). Persiste el texto en SharedPreferences ("fleet_search_query").
El filtro aplica tanto a la lista de faltantes como a un modo "ver todos" (ver B2).

=====================================================================
B2. VER TODA LA FLOTA, NO SOLO LO QUE FALTA
=====================================================================
Hoy SummaryScreen solo lista looks CON faltantes. Agrega un conmutador arriba:
    [ Pendientes ]  [ Toda la flota ]
- "Pendientes" (default): la lista de hoy (looks con poses faltantes).
- "Toda la flota": TODOS los looks, cada tarjeta mostrando su progreso N/M (materializadas/total),
  ordenados por número desc. El buscador de B1 filtra ambos.

CRITERIO DE ACEPTACIÓN: buscar "corset" muestra solo los looks cuyo nombre/tags/categoría lo
contienen; el conmutador cambia entre "solo pendientes" y "toda la flota".

=====================================================================
B3. (menor) BUSCADOR EN RELATOS
=====================================================================
En la pestaña Relatos (LiteratureScreen), agrega una barra de búsqueda que filtre la lista de
relatos por título/carpeta. Persiste en SharedPreferences ("lit_search_query"). Es lo más chico
del prompt: si algo se corta, este va último.

#####################################################################
##  PARTE C — TESTS Y ENTREGA
#####################################################################

Tests que ejerzan la ruta (pega la salida real con nombres, --rerun-tasks):
  - Progreso (A2): dado allLooks/allPrompts/allImages de prueba (p. ej. 3 looks: uno 7/7, uno 3/7,
    uno 0/7), el % materializado, el conteo de completos (1) y el de poses faltantes cuadran.
  - Índices de tab (A1): tras reordenar, el mapa selectedTab→pantalla es
    0=Flota,1=Prompts,2=Galería,3=Relatos, y ningún selectTab() del código apunta al índice viejo.
  - Siguiente pendiente (A3): con una pose faltante conocida, el botón deja seleccionados ese
    lookNumber y esa pose.
  - Buscador (B1/B2): filtrar por "corset" reduce la lista a los looks que lo contienen en
    nombre/tags/categoría; el conmutador Pendientes/Toda-la-flota cambia el conjunto base.

Entrega:
  1. `git rev-parse HEAD` (pega la salida) + `git log --oneline -5`.
  2. Sube versionCode +1 y versionName +0.1 respecto al APK del #11 (si el #11 dejó 15/"4.8",
     este queda 16/"4.9"). Mantén el hash de commit visible en la cabecera (ya existe,
     LaVouteApp.kt:72).
  3. Declara el keystore usado y si coincide con el anterior.
  4. El APK.
  5. Sección "NO HECHO:" obligatoria, una línea por punto no logrado. Vacía + un test de la Parte C
     que falle = entrega no verificada.
```

---

## 📌 Nota de prioridad para la Ama

| Prioridad | Punto | Por qué |
|---|---|---|
| 🥇 | **A2** (cabecera dashboard) | Es el "de un vistazo" que hoy no existe: % materializado + cuántas poses faltan. El resto de la pantalla ya lo calcula. |
| 🥈 | **A1** (La Flota como inicio) | La convierte en centro de mando de verdad; ojo con corregir TODOS los `selectTab()` al reordenar. |
| 🥉 | **B1 + B2** (buscador + ver toda la flota) | Poder buscar un look y ver el progreso de los que YA están, no solo lo que falta. |
| 4 | **A3** (siguiente pendiente) | "Tacha y siguiente" sin buscar a mano. |
| 5 | **A4** (looks recientes) | Lindo, pero es proxy por número (no hay fecha real de subida). |
| 6 | **B3** (buscar en relatos) | El más chico; va último. |

**Lo honesto:** el buscador ya existe en Prompts y en Galería — este prompt lo suma donde falta (la
flota y relatos), no lo inventa. Y el cálculo de faltantes no se toca: La Flota es su cara nueva.
