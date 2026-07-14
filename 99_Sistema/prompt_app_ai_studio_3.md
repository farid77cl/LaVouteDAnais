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
  e) El código de la UI del botón de copiar (ver el punto 4, que cambia lo pedido antes).

---------------------------------------------------------------------
4. EL BOTÓN DE COPIAR: UNO SOLO, Y COPIA TODO
---------------------------------------------------------------------
Corrige lo que te pedí antes: NO quiero dos botones ("copiar positivo" y "copiar negativo").
Quiero UN SOLO botón de copiar, el de siempre, que copie el prompt COMPLETO: el positivo y el
negativo juntos, en un solo toque.

Razón: si el negativo depende de que la usuaria se acuerde de apretar un segundo botón, algún día
no lo va a apretar, y se vuelve a generar sin negativo — que es exactamente el bug que estamos
arreglando. Lo que se puede olvidar, se olvida. Un solo botón lo hace imposible.

Formato del texto que se copia al portapapeles:

    <prompt positivo tal cual>

    Do not include: <negative prompt tal cual>

IMPORTANTE — no uses la sintaxis "--no <negativo>". Ese formato es de Midjourney / Stable
Diffusion. El destino aquí es GEMINI, que es conversacional y NO interpreta "--no": se lo tragaría
como texto literal y podría dibujar justo lo que se quiere evitar. Tiene que ir en lenguaje
natural, en inglés (los prompts están en inglés): "Do not include: ...".

Si el look no tiene negativo (negativePrompt == null), el botón copia solo el positivo, sin
agregar la línea "Do not include:" vacía.

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
Compílame el APK con estos cambios para instalarlo y probarlo. En la app tiene que pasar esto:

  · aprieto el botón de copiar UNA vez, y en el portapapeles queda el prompt positivo Y el
    negativo (con "Do not include:"), listo para pegar en Gemini de un tirón.
  · los looks que no tengan negativo quedan marcados de forma visible.

Eso lo voy a comprobar pegando el portapapeles, así que no hace falta que me lo describas.
```

---

## ✅ Cómo verificar sin depender de lo que diga AI Studio

| Prueba | Qué significa |
|---|---|
| **Apretar "copiar" y pegar el portapapeles en cualquier parte** | Si aparece el positivo **y** el `Do not include: ...`, está implementado. Si sale solo el positivo, el reporte era humo. Un toque, todo copiado. |
| **Subir una pose a un look que YA tiene carpeta** | Si crea una carpeta gemela (`look<N>_otro_slug/`), el fix de directorios no está. |
| **`git log origin/main` en LV-App** | Si aparece un commit nuevo con el código, se puede leer y auditar línea por línea. |

> ⚠️ **`--no` NO sirve aquí.** Es sintaxis de Midjourney / Stable Diffusion. El destino es **Gemini**, que es conversacional y lo tomaría como texto literal — podría dibujar justo lo que se quiere evitar. El negativo va en lenguaje natural: `Do not include: ...`.
