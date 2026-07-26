# 📱 Prompt #18 para AI Studio — Normalización de Poses/Categorías (alias en español + sufijos numéricos + matching robusto en Galería y Flota)

> **Base:** repo `farid77cl/LV-App` al día (HEAD post-#17).
>
> **Problema reportado por la Ama:** "hay imágenes que están, pero que la app no las muestra dentro de su categoría, por ejemplo está la imagen sentada y no la muestra en donde corresponde, aparece vacía".
>
> **Diagnóstico técnico:** Las funciones de matching de poses (`matchesPose`, `matchesPoseLocal`, `poseFromFilename`) en `SummaryScreen.kt`, `ImageGalleryScreen.kt`, `PromptFilterScreen.kt` y `MainViewModel.kt` realizan comparaciones de substring rígidas o exactas (ej. `img.contains("_seated.")`). Si una imagen fue guardada o subida con alias en español (`sentada`, `espalda`, `perfil`), con sufijos numéricos (`ele_106_seated_2.png`, `look87_seated_v1.png`) o variaciones de mayúsculas/minúsculas (`Seated` vs `seated`), la app no la vincula a la categoría correspondiente y la casilla/grilla aparece **vacía (0/7 / ⏳)** a pesar de que el archivo existe en Room/disco.

---

## 🔍 Diagnóstico del Código (con archivos y funciones)

1. **Inconsistencia de Matching en `SummaryScreen.kt` / `PromptFilterScreen.kt`:**
   En las funciones locales que determinan qué imagen corresponde a qué pose:
   - Exigen exactitud de nombre en inglés o sufijo fijo (`_seated.png`, `_back_view.png`).
   - Si la imagen se llama `ele_85_sentada.png` o `ele_106_seated_2.png`, `matchesPose` devuelve `false`.
   
2. **Sensibilidad a Mayúsculas y Filtros en `ImageGalleryScreen.kt`:**
   El filtro de pose compara strings direktamente (`selectedPose == item.pose`). Al filtrar por "Seated", no hace match con "seated" ni con "sentada", haciendo que la categoría en la grilla se despliegue vacía.

3. **Selección de Portada en el Modo Outfit:**
   En las tarjetas de outfit de la Galería, la portada debe priorizar la pose `Standing` / `Frontal`. Si la detección de `Standing` falla por alias o sufijo, la tarjeta queda sin portada o muestra una foto de espaldas.

---

```markdown
Eres el desarrollador de LV-App (Kotlin / Jetpack Compose / Room / Retrofit / Moshi / Coil).
Trabaja sobre el repo al día.

CONTEXTO: El problema de categorías vacías (como "Sentada" / Seated) se produce por funciones de matching rígidas que no reconocen alias en español ni sufijos numéricos en los nombres de los archivos PNG.

⭐ INTOCABLE: El flujo de subida de imágenes y la guardia de resolución (≥400.000 px²). No modificar la red de seguridad de upload.

#####################################################################
##  PARTE A — UNIFICACIÓN Y NORMALIZACIÓN DE POSES (PoseMatcher)
#####################################################################

A1. CREAR EL COMPONENTE CENTRAL `PoseMatcher.kt`
Crea una clase/object utilitario utilitario en el paquete de modelos/utilidades:

```kotlin
object PoseMatcher {
    // Definición de poses canónicas
    val CANONICAL_POSES = listOf(
        "Standing",
        "Back View",
        "Seated",
        "Side Profile",
        "Ditzy",
        "POV",
        "Odalisque"
    )

    // Mapeo de alias a pose canónica
    private val ALIAS_MAP = mapOf(
        "standing" to "Standing",
        "frontal" to "Standing",
        
        "back_view" to "Back View",
        "backview" to "Back View",
        "back" to "Back View",
        "espalda" to "Back View",
        
        "seated" to "Seated",
        "sitting" to "Seated",
        "sentada" to "Seated",
        
        "side_profile" to "Side Profile",
        "sideprofile" to "Side Profile",
        "profile" to "Side Profile",
        "side" to "Side Profile",
        "perfil" to "Side Profile",
        
        "ditzy" to "Ditzy",
        "pov" to "POV",
        
        "odalisque" to "Odalisque",
        "lying" to "Odalisque",
        "acostada" to "Odalisque"
    )

    /**
     * Extrae y normaliza la pose canónica a partir del nombre de un archivo o string.
     * Ejemplo: "ele_106_seated_2.png" -> "Seated"
     *          "ele_85_sentada.png"  -> "Seated"
     *          "look87_back_v1.png"  -> "Back View"
     */
    fun getCanonicalPose(filenameOrPose: String): String? {
        val clean = filenameOrPose.lowercase()
            .replace(".png", "")
            .replace(".jpg", "")
            .replace(".jpeg", "")
            .replace(".webp", "")
            
        // Remover prefijos comunes
        val sansPrefix = clean.replace(Regex("^(ele|helena)_\\d+_"), "")
            .replace(Regex("^look0*\\d+_"), "")
            
        // 1. Probar coincidencia exacta con alias
        ALIAS_MAP[sansPrefix]?.let { return it }

        // 2. Probar si el texto empieza por o contiene algún alias como token
        // Ordenar alias por longitud descendente para que 'side_profile' gane a 'side'
        val sortedAliases = ALIAS_MAP.keys.sortedByDescending { it.length }
        for (alias in sortedAliases) {
            if (sansPrefix == alias || sansPrefix.startsWith("${alias}_") || sansPrefix.contains("_$alias") || sansPrefix.contains(alias)) {
                return ALIAS_MAP[alias]
            }
        }

        return null
    }

    /**
     * Compara si dos referencias de pose se refieren a la misma pose canónica.
     */
    fun matches(poseA: String, poseB: String): Boolean {
        val canonA = getCanonicalPose(poseA) ?: poseA.trim().lowercase()
        val canonB = getCanonicalPose(poseB) ?: poseB.trim().lowercase()
        return canonA.equals(canonB, ignoreCase = true)
    }
}
```

A2. REEMPLAZAR FUNCIONES LOCALES DISPARES
Reemplaza todas las implementaciones ad-hoc de `matchesPose`, `matchesPoseLocal` y parsing de pose en:
- `SummaryScreen.kt`
- `ImageGalleryScreen.kt`
- `PromptFilterScreen.kt`
- `MainViewModel.kt`

Para que TODAS usen `PoseMatcher.matches(requestedPose, imagePoseOrFilename)` y `PoseMatcher.getCanonicalPose(filename)`.

CRITERIO DE ACEPTACIÓN: Un archivo guardado como `ele_85_sentada.png` o `ele_106_seated_2.png` se clasifica correctamente bajo la pose/categoría "Seated" en todas las pantallas.

#####################################################################
##  PARTE B — MODO OUTFIT Y PORTADA DE TARJETAS
#####################################################################

B1. SELECCIÓN ROBUSTA DE PORTADA
En `ImageGalleryScreen.kt` (o composable de tarjeta de Outfit):
- Al seleccionar la imagen de portada de la tarjeta de un Outfit, busca primero una imagen cuya pose sea `Standing` (usando `PoseMatcher.getCanonicalPose(img.path) == "Standing"`).
- Si no existe `Standing`, busca en orden de preferencia: `Side Profile` > `Seated` > primera imagen disponible.
- Muestra el contador real `N/7` contando las poses canónicas únicas representadas entre las imágenes del outfit.

B2. FILTRADO DE CATEGORÍA / POSE SIN VACÍOS
Al aplicar el filtro por categoría o pose en la Galería:
- Filtrar la lista comparando `PoseMatcher.matches(selectedFilter, img.pose)`.
- Si ninguna imagen coincide exactamente pero el nombre del outfit o etiqueta contiene el texto buscado, incluirlo como fallback para no dejar la grilla en blanco injustificadamente.

B3. MISMA PANTALLA COMPLETA COMPARTIDA (`LightboxViewer`) EN PROMPTS Y GALERÍA
- En `PromptFilterScreen.kt`, al tocar la miniatura/preview de la imagen existente de la pose seleccionada, NO usar un diálogo secundario ni un visor simplificado.
- Debe invocar EXACTAMENTE EL MISMO composable `LightboxViewer` que utiliza la pestaña de Galería (`ImageGalleryScreen.kt`).
- Comparte el 100% de sus funcionalidades: carrusel/pase automático de fotos del outfit (botón ▶), gestos de zoom/swipe, visualización de resolución y notas por imagen, y ocultamiento real de las barras del sistema (fullscreen inmersivo).
- Si la pose seleccionada pertenece a un outfit con múltiples fotos, abrir el `LightboxViewer` posicionado en esa imagen concreta pero permitiendo deslizar entre las demás poses del mismo outfit.

CRITERIO DE ACEPTACIÓN: Al tocar la foto en la pestaña Prompts, se abre la misma experiencia idéntica de pantalla completa que en la Galería (`LightboxViewer`), con los mismos controles, gestos y carrusel.

#####################################################################
##  PARTE C — VERSIONADO OBLIGATORIO Y REPORTE
#####################################################################

1. Incrementa `versionCode` (+1) y actualiza `versionName = "4.12"`.
2. Muestra el número de versión y hash de commit visible en la barra superior / menú de ajustes de la app.

TESTS (reales, no dummy):
- `PoseMatcher.getCanonicalPose("ele_106_seated_2.png") == "Seated"`
- `PoseMatcher.getCanonicalPose("ele_85_sentada.png") == "Seated"`
- `PoseMatcher.matches("Seated", "sentada") == true`

ENTREGA:
1. `git rev-parse HEAD` + `git log --oneline -5`.
2. `versionCode` y `versionName` actualizados.
3. APK generado y listo para probar.
4. Sección "NO HECHO:" explícita si algún punto fue omitido.
```
