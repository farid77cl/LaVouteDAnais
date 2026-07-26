# 📱 Prompt #20 · LV-App 2.0 — PASO 1: Esqueleto Navegable

> **Reemplaza al Prompt #19** (monolítico — colapsó AI Studio por pedir la app entera de un tiro).
> **Método nuevo:** Andamiaje Incremental. Cada prompt entrega algo **que compila y corre**; nunca la app completa de una vez.
> **Este paso (P1):** solo el esqueleto — la app abre, muestra 5 pestañas y navega entre ellas. Sin datos, sin red, sin audio todavía.
> **Destino:** Google AI Studio → repo `farid77cl/LV-App`.
> **Build objetivo:** `versionCode 1` · `versionName "1.0"` (app nueva, versionado reseteado desde cero).

---

## ⚠️ REGLAS DE ESTE PROMPT (leer antes de generar)

1. **Genera SOLO los archivos listados abajo.** No crees pantallas de contenido, ni Room, ni Retrofit, ni Media3 en este paso.
2. **El resultado DEBE compilar y correr.** Al terminar, la app abre en la pestaña Visual y se puede navegar a las 5.
3. **No inventes dependencias extra.** Solo las declaradas en `build.gradle`.
4. Kotlin + Jetpack Compose + Material 3 + Clean Architecture (paquetes creados aunque casi vacíos).
5. Si algo no cabe, **corta el alcance, no el que compile**: preferible menos, pero que buildee.

---

```markdown
Eres el desarrollador principal de la app Android LV-App 2.0 de La Voûte d'Anaïs.
Vamos a construirla por pasos incrementales. Este es el PASO 1: el ESQUELETO.

Stack: Kotlin, Jetpack Compose, Material 3, Navigation-Compose, Clean Architecture + MVVM.
NO uses todavía Room, Retrofit, Coil ni Media3 — esos entran en pasos siguientes.

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

1. build.gradle (app-level)
   - minSdk 26, targetSdk 36, compileSdk 36.
     ⚠️ REGLA DE COMPATIBILIDAD: si alguna dependencia exige un `compileSdk` MAYOR,
     SUBE el compileSdk — nunca bajes de versión las librerías ni las fijes a mano
     en versiones viejas. AGP y Kotlin deben ser los que soporten ese compileSdk.
   - versionCode 1, versionName "1.0".
   - Dependencias: Compose BOM (última estable), material3, activity-compose,
     navigation-compose, lifecycle-viewmodel-compose. NADA MÁS.

2. ui/theme/Color.kt
   - Tres paletas de personaje (fondo OLED oscuro por defecto):
     * Ele    → background #0B0612, primary #FF2B85 (Hot Magenta), secondary #D4AF37.
     * Clara  → background #0B0612, primary #C0392B (Cherry Red), secondary #C9A227 (Leopard Gold).
     * Anaïs  → background #0B0612, primary #D4AF37 (Imperial Gold), secondary #6B2E4E (Velvet).

3. ui/theme/Theme.kt
   - `enum class Character { ELE, CLARA, ANAIS }`.
   - `AppTheme(character: Character, content: @Composable () -> Unit)` que construye
     un `darkColorScheme` con la paleta del personaje y aplica Material 3.
   - Provee el personaje activo vía un `CompositionLocal` o parámetro simple.

4. ui/nav/Destinations.kt
   - `sealed class Screen(val route, val label, val emoji)` con:
     Visual("visual","Visual","👗"), Literatura("lit","Literatura","📖"),
     Constelacion("rrss","Constelación","🚀"), Ops("ops","Ops","⚡"), Eve("eve","EVE","🔮").
   - Lista ordenada de las 5 para pintar la barra.

5. ui/nav/AppNavBar.kt
   - `NavigationBar` de Material 3 con las 5 pestañas (emoji + label), resalta la activa.

6. ui/screens/PlaceholderScreen.kt
   - Composable reutilizable: recibe un título y muestra centrado "🚧 {título} — Próximamente ✨".

7. ui/screens/VisualScreen.kt, LiteraturaScreen.kt, ConstelacionScreen.kt, OpsScreen.kt, EveScreen.kt
   - Por ahora las 5 solo llaman a PlaceholderScreen con su nombre. (VisualScreen se
     llenará en el PASO 2 — déjala como placeholder pero en su propio archivo.)

8. MainActivity.kt
   - `setContent { }` con un `AppTheme(personajeActivo)`.
   - `Scaffold` con:
     * topBar: header que muestra "LV-App 2.0 · v1.0" + un selector de personaje
       (3 chips: Ele / Clara / Anaïs) que cambia el tema en vivo. El header muestra "LV-App 2.0 · v1.0".
     * bottomBar: AppNavBar.
     * content: NavHost con las 5 rutas, arrancando en "visual".
   - Estado del personaje activo con `remember { mutableStateOf(Character.ELE) }`.

9. Un test unitario mínimo real (NO `assertTrue(true)`):
   - `DestinationsTest.kt`: verifica que la lista de pantallas tiene 5 rutas únicas.

=====================================================================
## CRITERIO DE ÉXITO DEL PASO 1
=====================================================================
- Gradle sincroniza y compila sin errores.
- La app abre en la pestaña Visual (placeholder).
- Tocar cada pestaña navega y muestra su placeholder.
- Cambiar el chip de personaje recolorea la UI en vivo (Ele/Clara/Anaïs).
- El header muestra "LV-App 2.0 · v1.0".

Entrega el código de los 9 puntos y NADA más. En el PASO 2 llenaremos la pestaña Visual
(PoseMatcher + Galería N/7 + Lightbox).

## DISCIPLINA DE COMPILACIÓN (anti-timeout)
- UNA sola compilación a la vez. Si una quedó colgada, mátala antes de lanzar otra —
  nunca dos builds de Gradle en paralelo (se pelean el daemon y la memoria del contenedor
  y ninguna termina: "Timed out waiting for applet file system condition to be met").
- Ajusta primero TODA la configuración de Gradle (SDK, AGP, Kotlin, dependencias) y
  recién entonces compila una vez, limpio. No compiles para "ir viendo".
```

---

## ✅ Cómo verificar antes de pasar al P2
1. Sincronizar Gradle → sin errores.
2. Correr en emulador/dispositivo → abre en Visual, navega a las 5, cambia de personaje y recolorea.
3. Pushear el commit inicial de AI Studio al repo (`versionCode 1`, `versionName "1.0"`).
4. Recién con eso verde → **Prompt #20 · P2 (Pestaña Visual)**.
