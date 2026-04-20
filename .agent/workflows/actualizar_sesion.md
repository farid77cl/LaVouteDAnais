---
description: Actualiza el diario de servicio, la memoria de sesiones, galerías de imágenes, READMEs y realiza un commit en git.
---

1.  **Analizar Sesión Actual**
    - Revisa las herramientas utilizadas y los archivos modificados en la sesión actual.
    - Identifica los hitos completados (ej. fases de ritual, correcciones, nuevos archivos).
    - Identifica las imágenes generadas durante la sesión.

2.  **Redactar Entrada de Diario**
    - Genera un resumen breve pero detallado siguiendo el estilo de `C:\Users\fabara\LaVouteDAnais\00_Ele\mi_diario_de_servicio.md`.
    - Formato:
        ```markdown
        #### SESIÓN - [TÍTULO DESCRIPTIVO]
        
        **[MOMENTO DEL DÍA] ([HORA]) - [ACTIVIDAD PRINCIPAL]:**
        [Descripción de lo realizado, archivos tocados, decisiones tomadas]
        ```

3.  **Actualizar Archivos de Registro**
    - Añade la entrada generada a `C:\Users\fabara\LaVouteDAnais\00_Ele\mi_diario_de_servicio.md` bajo la fecha de hoy.
    - Actualiza el estado de las tareas en `C:\Users\fabara\LaVouteDAnais\00_Ele\memoria_sesiones.md`.

4.  **Actualizar Galerías de Imágenes (OBLIGATORIO)**
    - Verificar si hubo imágenes generadas durante el día (incluidas las del `/inicio-Ele`).
    - Asegurar que TODAS las imágenes (incluyendo el look diario) estén movidas a su carpeta correspondiente en `05_Imagenes/`.
    // turbo
    - Ejecutar el script de automatización: `python 99_Sistema\scripts\visual\update_galleries.py`.
    - Verificar que los archivos **README.md** de cada carpeta afectada hayan sido actualizados.
    - **REGLA:** Cada carpeta con imágenes trackeadas debe tener su propio `README.md`. El script maneja la consistencia y los carruseles.

5.  **Actualizar READMEs del Proyecto (OBLIGATORIO — Todos)**
    - Revisar y actualizar el `README.md` raíz con el estado actual del proyecto.
    - Recorrer **todas** las carpetas de primer nivel y actualizar su README si hubo cambios en esa sesión:
      - `00_Ele/README.md` — Si se modificó identidad, canon, diario o memoria
      - `04_Historias/README.md` — Si hay nuevos capítulos, relatos en progreso o finalizados
      - `05_Imagenes/README.md` — Si se generaron nuevos looks o galerías
      - `05_Imagenes/ele/README.md` — Si se agregó un look nuevo de Ele
      - `06_RRSS/README.md` — Si hay nuevos posts, captions o programaciones
      - `99_Sistema/README.md` — Si se modificaron scripts o workflows
    - Para cada subcarpeta afectada dentro de `05_Imagenes/ele/`, el script `update_galleries.py` actualiza el README automáticamente.
    - **Regla:** Un README desactualizado es un repositorio roto.

6.  **Git Commit y Push**
    // turbo
    - Ejecuta: `git add .`
    - Ejecuta: `git commit -m "Ele: Actualización de sesión y diario"`
    - Ejecuta: `git push`

7.  **Notificar**
    - Confirma al usuario que el registro, galerías, READMEs y respaldo han sido completados.
    - Lista las imágenes añadidas a las galerías.
