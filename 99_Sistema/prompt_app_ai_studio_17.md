# ⚡ Prompt #17 para AI Studio — Subir sin confirmación cuando la imagen ya tiene el tamaño adecuado

> **Base:** repo `farid77cl/LV-App` al día (HEAD `4d8c556`, después del #15).
>
> **Pedido de la Ama:** quitar el diálogo «Confirmar Subida» cuando la imagen **cumple el tamaño** (≥400.000 px²). Que suba directo. El aviso de imagen **demasiado pequeña** se mantiene (esas NO deben subir).
>
> **Alcance:** SOLO `PromptFilterScreen.kt`. La guardia de resolución de `uploadImageToGithub` (MainViewModel:376) NO se toca — es la red de seguridad de fondo.

---

## 🔍 Estado actual (verificado, con línea)

En `PromptFilterScreen.kt` hay **dos rutas** que traen una imagen (selector de galería ~:146-182 y la otra ruta ~:200-234). Ambas hacen lo mismo:

```
imageResolutionStr = "${w}x${h}"
if (!isValidImageResolution(w, h)) {        // :159 / :210   (isValidImageResolution: :74, >=400000)
    showSmallImageWarning = true            // avisa y NO sube  → SE MANTIENE
} else {
    ... resize ...
    pendingUploadBytes = resizedBytes
    showUploadConfirmDialog = true          // :182 / :234  ← esta confirmación es la que sobra
}
```

Y el diálogo `showUploadConfirmDialog` (:903-945) pregunta «¿Subir esta imagen al repositorio? {WxH} ✓» y recién en su botón Confirmar (:920-934) llama a `viewModel.uploadImageToGithub(...)`.

**Traducción:** para las imágenes que YA pasan el tamaño, el diálogo solo agrega un tap de más. Se elimina; suben directo.

---

```
Eres el desarrollador de LV-App. Cambio chico y acotado a PromptFilterScreen.kt.

⭐ INTOCABLE: la guardia de resolución dentro de uploadImageToGithub (MainViewModel:376) y todo el
resto del flujo de subida. El aviso de "Imagen Demasiado Pequeña" (showSmallImageWarning, :887-901)
SE MANTIENE tal cual.

1. Extrae la lógica de subida que hoy vive en el botón Confirmar del diálogo (:920-934) a una
   función local reutilizable dentro del composable, p.ej.:

       fun performUpload(bytes: ByteArray) {
           isUploading = true
           val existingImage = matchedImages.firstOrNull { matchesPose(selectedPose, it.poseName) }
           viewModel.uploadImageToGithub(
               look = selectedLook!!,
               poseName = selectedPose,
               imageBytes = bytes,
               source = com.example.ui.viewmodel.ImageSource.GALLERY,
               existingPath = existingImage?.path,
               existingParentFolder = matchedImages.firstOrNull()?.path?.substringBeforeLast("/")
           ) { success ->
               isUploading = false
               Toast.makeText(context, if (success) "Subida OK ✓" else "Falló la subida", Toast.LENGTH_SHORT).show()
           }
       }

   (Conserva el `source` real de cada ruta si difiere: la ruta de galería usa GALLERY; si la otra
   ruta usaba otro ImageSource, respétalo.)

2. En las DOS ramas "else" de tamaño válido (:181-182 y :233-234), en lugar de
   `pendingUploadBytes = resizedBytes; showUploadConfirmDialog = true`, llama directo:
       performUpload(resizedBytes)
   Muestra un Toast breve "Subiendo…" al iniciar, para que se vea que arrancó (ya no hay diálogo).

3. Elimina el diálogo `showUploadConfirmDialog` (:903-945) y su variable de estado
   `showUploadConfirmDialog` + `pendingUploadBytes` si quedan sin uso. NO elimines
   `showSmallImageWarning` ni `imageResolutionStr`.

CRITERIO DE ACEPTACIÓN:
 - Elegir una imagen de tamaño válido (≥400.000 px²) la sube AL TIRO, sin diálogo de confirmación,
   con un Toast de progreso/resultado.
 - Elegir una imagen pequeña sigue mostrando el aviso "Imagen Demasiado Pequeña" y NO la sube.
 - La guardia de fondo en uploadImageToGithub sigue intacta.

TEST (real, prohibido assertTrue(true)):
 - isValidImageResolution(800,1200)==true ; isValidImageResolution(286,512)==false (frontera 400000).

ENTREGA:
 1. `git rev-parse HEAD` + `git log --oneline -5` (pega las salidas).
 2. versionCode +1 y versionName +0.1 respecto al repo. Hash de commit visible en la cabecera.
 3. Keystore usado y si coincide con el anterior.
 4. El APK.
 5. "NO HECHO:" obligatoria.
```

---

**Nota:** es un cambio de un solo archivo. La red de seguridad no se pierde: una imagen pequeña
sigue sin poder subir (doble candado: el aviso en pantalla + la guardia dentro de
`uploadImageToGithub`). Lo único que desaparece es el tap de "confirmar" para las que ya están bien.
