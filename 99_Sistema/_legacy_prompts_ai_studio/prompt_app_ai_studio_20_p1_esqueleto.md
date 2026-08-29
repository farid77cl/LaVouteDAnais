# 📱 Prompt #20 · LV-App 2.0 — PASO 1: Esqueleto Navegable

> **Reemplaza al Prompt #19** (monolítico — colapsó AI Studio por pedir la app entera de un tiro).
> **Método nuevo:** Andamiaje Incremental. Cada prompt entrega algo **que compila y corre**; nunca la app completa de una vez.
> **Este paso (P1):** solo el esqueleto — la app abre, muestra 5 pestañas y navega entre ellas. Sin datos, sin red, sin audio todavía.
> **Destino:** Google AI Studio → repo `farid77cl/LV-App`.
> **Build objetivo:** `versionCode 1` · `versionName "1.0"` (app nueva, versionado reseteado desde cero).
>
> **Rev. 26/07/2026 (v2):** corregido el conflicto de SDK que reventó el primer intento — el prompt fijaba `compileSdk 34` mientras pedía el Compose BOM más nuevo, y las `androidx` modernas (`core-ktx`, `activity-compose`) exigen 36. Ahora va **SDK 36** + regla explícita de *subir el SDK, nunca bajar las librerías*. Se agregaron además: Kotlin DSL, plugin de Compose de Kotlin 2.x, JVM target, Manifest, borrón total de código previo, disciplina anti-timeout y reporte de versiones.

---

## ⚠️ REGLAS DE ESTE PROMPT (leer antes de generar)

1. **Genera SOLO los archivos listados abajo.** No crees pantallas de contenido, ni Room, ni Retrofit, ni Media3 en este paso.
2. **El resultado DEBE compilar y correr.** Al terminar, la app abre en la pestaña Visual y se puede navegar a las 5.
3. **No inventes dependencias extra.** Solo las declaradas en `build.gradle.kts`.
4. Kotlin + Jetpack Compose + Material 3 + Clean Architecture (paquetes creados aunque casi vacíos).
5. Si algo no cabe, **corta el alcance, no el que compile**: preferible menos, pero que buildee.

---

## 📋 PROMPT PARA PEGAR EN AI STUDIO (todo lo que sigue, hasta el cierre del bloque)

```markdown
Eres el desarrollador principal de la app Android LV-App 2.0 de La Voûte d'Anaïs.
Vamos a construirla por pasos incrementales. Este es el PASO 1: el ESQUELETO.

Stack: Kotlin, Jetpack Compose, Material 3, Navigation-Compose, Clean Architecture + MVVM.
NO uses todavía Room, Retrofit, Coil ni Media3 — esos entran en pasos siguientes.

=====================================================================
## PUNTO DE PARTIDA: DESDE CERO
=====================================================================
Si en el proyecto ya existe código de un intento anterior, IGNÓRALO y regenéralo
completo según esta especificación. No parches el intento viejo, no rescates
archivos sueltos: esta es la primera build del código nuevo (versionCode 1).

=====================================================================
## OBJETIVO DEL PASO 1
=====================================================================
Una app que ABRE, muestra una NavigationBar inferior con 5 pestañas y NAVEGA entre
ellas. Cuatro pestañas muestran un placeholder "Próximamente ✨". El tema cambia de
color según el personaje activo (Ele / Clara / Anaïs) mediante un selector en el header.
Debe COMPILAR y CORRER sin crashes.

=====================================================================
## ESTRUCTURA DE PAQUETES (Clean Architecture — crear vacíos los que no se usen aún)
=====================================================================
com.lavoute.app
 ├── ui
 │    ├── theme      (colores, tipografía, tema dinámico)
 │    ├── nav        (rutas + NavigationBar)
 │    └── screens    (las 5 pantallas placeholder)
 ├── domain          (vacío por ahora)
 ├── data            (vacío por ahora)
 └── service         (vacío por ahora)

=====================================================================
## ARCHIVOS A GENERAR (SOLO ESTOS)
=====================================================================

1. build.gradle.kts (app-level) + el build.gradle.kts raíz / settings.gradle.kts que
   hagan falta para que sincronice.
   - namespace y applicationId: com.lavoute.app
   - minSdk 26 · targetSdk 36 · compileSdk 36.
   - versionCode 1 · versionName "1.0".
   - Java/Kotlin JVM target 17 (compileOptions + kotlinOptions coherentes).
   - buildFeatures { compose = true }.
   - Kotlin 2.x: aplica el plugin `org.jetbrains.kotlin.plugin.compose` (en Kotlin 2.0+
     el compilador de Compose es un plugin aparte; sin él NO compila).
   - Dependencias: Compose BOM (última estable), material3, activity-compose,
     navigation-compose, lifecycle-viewmodel-compose, core-ktx. NADA MÁS.
   - AGP y Kotlin: versiones estables recientes que soporten compileSdk 36.

   ⚠️ REGLA DE COMPATIBILIDAD (esto rompió el intento anterior):
   Si una dependencia exige un compileSdk MAYOR, SUBE el compileSdk.
   NUNCA bajes de versión las librerías, ni las fijes a mano en versiones viejas,
   ni excluyas transitivas para "que compile". El SDK se acomoda a las librerías,
   no al revés.

2. AndroidManifest.xml
   - `<application>` con el tema de la app y `MainActivity` como LAUNCHER.
   - Sin permisos todavía (no hay red ni almacenamiento en este paso).

3. ui/theme/Color.kt
   - Tres paletas de personaje (fondo OLED oscuro por defecto):
     * Ele    → background #0B0612, primary #FF2B85 (Hot Magenta), secondary #D4AF37.
     * Clara  → background #0B0612, primary #C0392B (Cherry Red), secondary #C9A227 (Leopard Gold).
     * Anaïs  → background #0B0612, primary #D4AF37 (Imperial Gold), secondary #6B2E4E (Velvet).

4. ui/theme/Theme.kt
   - `enum class Character { ELE, CLARA, ANAIS }`.
   - `AppTheme(character: Character, content: @Composable () -> Unit)` que construye
     un `darkColorScheme` con la paleta del personaje y aplica Material 3.
   - Provee el personaje activo vía un `CompositionLocal` o parámetro simple.
   - NO uses dynamicColor de Android 12+: el tema lo manda el personaje, no el sistema.

5. ui/nav/Destinations.kt
   - `sealed class Screen(val route: String, val label: String, val emoji: String)` con:
     Visual("visual","Visual","👗"), Literatura("lit","Literatura","📖"),
     Constelacion("rrss","Constelación","🚀"), Ops("ops","Ops","⚡"), Eve("eve","EVE","🔮").
   - Lista ordenada de las 5 para pintar la barra.

6. ui/nav/AppNavBar.kt
   - `NavigationBar` de Material 3 con las 5 pestañas (emoji + label), resalta la activa.
   - Al navegar: `launchSingleTop = true`, `restoreState = true` y `popUpTo` al destino
     inicial con `saveState = true` (que no apile 40 copias de la misma pantalla).

7. ui/screens/PlaceholderScreen.kt
   - Composable reutilizable: recibe un título y muestra centrado "🚧 {título} — Próximamente ✨".

8. ui/screens/VisualScreen.kt, LiteraturaScreen.kt, ConstelacionScreen.kt, OpsScreen.kt, EveScreen.kt
   - Por ahora las 5 solo llaman a PlaceholderScreen con su nombre. (VisualScreen se
     llenará en el PASO 2 — déjala como placeholder pero en su propio archivo.)

9. MainActivity.kt
   - `setContent { }` con un `AppTheme(personajeActivo)`.
   - `Scaffold` con:
     * topBar: header que muestra "LV-App 2.0 · v1.0" + un selector de personaje
       (3 chips: Ele / Clara / Anaïs) que cambia el tema en vivo.
     * bottomBar: AppNavBar.
     * content: NavHost con las 5 rutas, arrancando en "visual", respetando el padding
       del Scaffold (nada tapado por la barra).
   - Estado del personaje activo con `remember { mutableStateOf(Character.ELE) }`.

10. Un test unitario mínimo REAL (NO `assertTrue(true)`):
    - `DestinationsTest.kt`: verifica que la lista de pantallas tiene 5 rutas ÚNICAS
      (compara el tamaño de la lista contra el tamaño del set de rutas).

=====================================================================
## DISCIPLINA DE COMPILACIÓN (anti-timeout)
=====================================================================
- UNA sola compilación a la vez. Si una quedó colgada, mátala ANTES de lanzar otra:
  dos builds de Gradle en paralelo se pelean el daemon y la memoria del contenedor y
  ninguna termina ("Timed out waiting for applet file system condition to be met").
- Deja lista TODA la configuración de Gradle (SDK, AGP, Kotlin, plugins, dependencias)
  y recién entonces compila UNA vez, limpio. No compiles "para ir viendo".
- Si el build falla, arregla la causa; no reintentes el mismo build esperando otro
  resultado.

=====================================================================
## CRITERIO DE ÉXITO DEL PASO 1
=====================================================================
- Gradle sincroniza y compila sin errores ni warnings de dependencias incompatibles.
- La app abre en la pestaña Visual (placeholder).
- Tocar cada pestaña navega y muestra su placeholder.
- Cambiar el chip de personaje recolorea la UI en vivo (Ele/Clara/Anaïs).
- El header muestra "LV-App 2.0 · v1.0".
- El test `DestinationsTest` pasa.

=====================================================================
## AL TERMINAR, REPORTA (en texto, fuera del código)
=====================================================================
- Versiones usadas: AGP · Kotlin · Compose BOM · compileSdk / targetSdk / minSdk.
- Resultado literal de la compilación (BUILD SUCCESSFUL o el error).
- Resultado del test unitario.
- Si tuviste que cambiar alguna versión respecto a lo pedido, dilo explícitamente y
  por qué.

Entrega el código de los 10 puntos y NADA más. En el PASO 2 llenaremos la pestaña
Visual (PoseMatcher + Galería N/7 + Lightbox).
```

---

## ✅ Cómo verificar antes de pasar al P2
1. Sincronizar Gradle → sin errores.
2. Correr en emulador/dispositivo → abre en Visual, navega a las 5, cambia de personaje y recolorea.
3. Leer el **reporte de versiones**: si bajó alguna librería en vez de subir el SDK, se rechaza y se corrige ahí mismo.
4. **Pushear** el commit inicial de AI Studio al repo (`versionCode 1`, `versionName "1.0"`) — AI Studio corre su propio git; sus commits **no llegan a GitHub hasta que la Ama pushea**.
5. Recién con eso verde → **Prompt #20 · P2 (Pestaña Visual)**.
