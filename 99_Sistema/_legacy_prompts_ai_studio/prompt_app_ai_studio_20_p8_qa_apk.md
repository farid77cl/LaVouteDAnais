# 📱 Prompt #20 · LV-App 2.0 — PASO 8: QA + Build APK v1.0

> **Requiere P1-P7 verdes.** Cierre: suite de pruebas + APK de release.
> **Si aterriza roto:** patch como **Prompt #20.8.x**.

---

## ⚠️ REGLAS
1. Genera SOLO lo listado. No agregues features nuevas — este paso estabiliza y empaqueta.
2. Todos los tests deben pasar de verdad (prohibido `assertTrue(true)`).

---

```markdown
PASO 8 de LV-App 2.0. Estabilización y empaquetado.

## TAREAS (SOLO ESTAS)
1. Suite de pruebas unitarias completa y verde:
   - PoseMatcherTest, DestinationsTest, AppDatabaseTest, LiteratureTest, TtsRetrofitTest,
     CaptionFactoryTest, FleetStatsTest, CommandRouterTest.
   - Cada uno con asserts reales sobre comportamiento (no tautologías).

2. Estabilidad:
   - Revisar que ninguna pantalla crashee sin datos / sin red / sin permisos (estados vacíos y de error).
   - Verificar que las llamadas de red y el troceado corren fuera del hilo principal.

3. Build de release:
   - `versionCode 1`, `versionName "1.0"`.
   - Configuración de firma (release signing config; documentar cómo se provee el keystore, sin
     hardcodear credenciales).
   - Generar `LV-App-v1.0-release.apk`.

4. Checklist de humo (manual) documentado en el README de la app:
   - Abre en Visual · navega las 5 pestañas · cambia de personaje (tema) · galería N/7 correcta ·
     Lightbox con zoom · lee un capítulo con progreso · reproduce audio con karaoke · genera y
     (simula) publica un post · dashboard Ops con % y sync · EVE ejecuta "ir al look N".

## CRITERIO DE ÉXITO
Toda la suite pasa · el APK de release compila y se instala · el checklist de humo pasa completo ·
la app es la LV-App 2.0 v1.0 funcional sin crashes.

Entrega la suite de tests + config de release + APK. FIN de la serie de andamiaje.
```
