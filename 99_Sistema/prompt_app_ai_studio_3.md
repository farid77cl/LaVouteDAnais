# 📱 Prompt #3 para AI Studio — LV-App: **muéstrame el código y los tests corridos de verdad**

> **Contexto (14/07/2026):** AI Studio reportó haber implementado todo (slugify, negativePrompt, Room v8, botones de copiado, fallback de directorios). **No se puede verificar**: el código vive en el workspace de AI Studio y el repo `farid77cl/LV-App` es solo un respaldo — su último commit sigue siendo `bc32f6d` (los tests).
>
> **Lo único objetable con certeza** es su prueba: pegó `> Task :app:testDebugUnitTest UP-TO-DATE` / `BUILD SUCCESSFUL in 1s` / `32 up-to-date`. **`UP-TO-DATE` significa que Gradle NO ejecutó nada** (usó caché): esa salida no demuestra que los 5 tests pasen.
>
> Este prompt pide las tres cosas que no se pueden fabricar: el código pegado, los tests **forzados** a correr, y el push al repo para poder leerlo.
>
> **La prueba final es del otro lado:** instalar el APK y mirar si aparece el botón «Copiar negativo». Ese botón no existía antes.

---

```
Dices que implementaste slugify(), el campo negativePrompt (Room v8), el parseo de Ubicacion y
Categoria, el cierre seguro de fences y el fallback de directorios. Puede que sea cierto, pero
NO ME LO DEMOSTRASTE, y hay un problema concreto con la prueba que diste:

    > Task :app:compileDebugUnitTestKotlin UP-TO-DATE
    > Task :app:testDebugUnitTest UP-TO-DATE
    BUILD SUCCESSFUL in 1s
    32 actionable tasks: 32 up-to-date

"UP-TO-DATE" significa que Gradle NO EJECUTÓ esas tareas: las saltó porque cree que ya estaban
hechas. "32 up-to-date" = cero tareas corridas, y terminó "in 1s". Esa salida NO demuestra que
los 5 tests pasen. Solo demuestra que Gradle no hizo nada.

Necesito tres cosas. Las tres, o no puedo dar el trabajo por hecho.

---------------------------------------------------------------------
1. LOS TESTS, CORRIDOS DE VERDAD (sin caché)
---------------------------------------------------------------------
Corre EXACTAMENTE este comando, que fuerza la ejecución e invalida el caché:

    ./gradlew test --rerun-tasks

Pégame la salida literal. Si aparece la palabra "UP-TO-DATE", la salida no sirve.
Quiero ver los 5 tests ejecutándose:

    testSlugify
    testParseMarkdown_CapturesNegativePrompt
    testParseMarkdown_NoNegativePrompt_IsNull
    testParseMarkdown_UbicacionWithAndWithoutTilde
    testParseMarkdown_UnclosedFenceDoesNotContaminate

Si alguno falla, dímelo y arréglalo. Un test rojo declarado es infinitamente mejor que un
BUILD SUCCESSFUL inventado.

---------------------------------------------------------------------
2. EL CÓDIGO, PEGADO EN LA RESPUESTA
---------------------------------------------------------------------
No me describas lo que hace. Pégame el código real, completo:

  a) La función `slugify()` entera, y la línea de `saveImageToGithub` donde la usas
     (la que antes decía:
        val slug = look.name.lowercase().replace(Regex("[^a-z0-9]"), "_").replace(Regex("_+"), "_")
     )
  b) El `data class LookEntity` completo (para ver el campo negativePrompt) y la Migration de Room.
  c) El fragmento de `parseMarkdown` que captura `**Negative Prompt:**`.
  d) El fragmento que resuelve la carpeta destino al subir una imagen.
  e) El código de la UI donde agregaste el botón de copiar el negativo.

---------------------------------------------------------------------
3. EXPORTA EL CÓDIGO AL REPO
---------------------------------------------------------------------
El repositorio farid77cl/LV-App es el respaldo, y hoy está desactualizado: su último commit es
bc32f6d ("test: add slugify utility tests"), que solo trae los tests, sin implementación.

Haz commit y push de los cambios a origin/main y dame el hash del commit.
Mientras el código no esté ahí, nadie más que tú puede leerlo ni verificarlo.

---------------------------------------------------------------------
Y DAME EL APK
---------------------------------------------------------------------
Compílame el APK con estos cambios para instalarlo y probarlo. En la app tiene que verse:

  · un botón "Copiar negativo" (y la opción de copiar positivo + "--no <negativo>" juntos)
  · una marca visible en los looks que NO tengan bloque negativo

Eso lo voy a comprobar con los ojos, así que no hace falta que me lo describas.
```

---

## ✅ Cómo verificar sin depender de lo que diga AI Studio

| Prueba | Qué significa |
|---|---|
| **Instalar el APK y buscar el botón «Copiar negativo»** | No existía antes. Si está → implementó de verdad. Si no está → el reporte era humo. |
| **Subir una pose a un look que YA tiene carpeta** | Si crea una carpeta gemela (`look<N>_otro_slug/`), el fix de directorios no está. |
| **`git log origin/main` en LV-App** | Si aparece un commit nuevo con el código, se puede leer y auditar línea por línea. |
