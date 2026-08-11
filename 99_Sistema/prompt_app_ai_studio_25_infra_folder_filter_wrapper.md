# Prompt AI Studio #25 — Fix de Infraestructura de Imágenes & Gradle Wrapper

> **Fecha:** 2026-08-06
> Pégalo en AI Studio sobre el repo `LV-App`. Scope: **`GitRepository.kt`**, configuración del **Gradle Wrapper** e **Integridad de Base de Datos**.

---

## 🔍 Diagnóstico del Problema

Al auditar `LV-App` tras la sincronización de imágenes multi-personaje, se identificaron dos brechas críticas de infraestructura:

1. **Contaminación de la Base de Datos con Imágenes de Apoyo / Infraestructura:**
   En `GitRepository.kt` (`parseAndSaveTree`), la extracción del `lookNumber` escanea cualquier archivo `.png`/`.jpg` bajo `05_Imagenes/`.
   Carpetas como `05_Imagenes/anais/Reference/` (ej. `anais_belland_v2_regenta.png`), `05_Imagenes/anais/Scenes/` (ej. `custom_anais_scene_s011_...jpg`) y `05_Imagenes/anais/Outfits/` (ej. `custom_anais_outfit_s002_...png`) contienen dígitos en sus nombres (`2`, `011`, `002`).
   El scanner actual asocia erróneamente estas imágenes de referencia y escenas a los Looks `2` y `11` de la base de datos local, mezclándolas con las fotos de los looks reales.

2. **Ausencia del Gradle Wrapper:**
   El repositorio no incluye los archivos del Wrapper de Gradle (`gradlew`, `gradlew.bat`, `gradle-wrapper.properties` y `gradle-wrapper.jar`), lo que impide compilar o ejecutar los tests unitarios (`./gradlew test`) sin una instalación global de Gradle en el sistema.

---

## 🛠️ Cambios Requeridos

### 1. Filtrado de Carpetas de Infraestructura en `GitRepository.kt`

En `parseAndSaveTree` (línea ~754), se debe validar que el `parentFolder` de la imagen empiece por la subcadena `"look"` (ej. `look535_...`, `look22_...`, `look02_...`, `lookL04_...`):

```kotlin
// Dentro de parseAndSaveTree en GitRepository.kt (línea ~754):
if (path.startsWith("05_Imagenes/") && imageFormats.any { path.lowercase().endsWith(it) }) {
    val segments = path.split("/")
    if (segments.size < 4) continue

    val parentFolder = segments[segments.size - 2]
    // 🛡️ FIX: Filtrar carpetas de infraestructura (Reference, Scenes, Outfits, etc.)
    if (!parentFolder.startsWith("look", ignoreCase = true)) continue

    val fileName = segments[segments.size - 1]
    ...
```

---

### 2. Configuración del Gradle Wrapper (Raíz del Repositorio)

1. Crear `gradle/wrapper/gradle-wrapper.properties`:
```properties
distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
distributionUrl=https\://services.gradle.org/distributions/gradle-8.7-bin.zip
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
```

2. Asegurar la presencia de los ejecutables del wrapper en la raíz del repositorio:
   - `gradlew` (Unix)
   - `gradlew.bat` (Windows)
   - `gradle/wrapper/gradle-wrapper.jar`

---

## 📋 Criterios de Aceptación

1. **Aislamiento de Galería:** Las imágenes de `Reference`, `Scenes` y `Outfits` ya NO aparecen asignadas a los looks reales en la base de datos local.
2. **Consistencia de Galería:** Todos los looks de Ele (1-800), Miss Doll (1-26) y Anaïs (1-40) muestran únicamente sus fotos de pose correspondientes.
3. **Portabilidad de Build:** Ejecutar `./gradlew test` o `.\gradlew.bat test` compila el proyecto y ejecuta los tests unitarios sin requerir Gradle global.
