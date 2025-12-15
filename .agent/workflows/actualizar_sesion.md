---
description: Actualiza el diario de servicio, la memoria de sesiones y realiza un commit en git.
---

1.  **Analizar Sesión Actual**
    - Revisa las herramientas utilizadas y los archivos modificados en la sesión actual.
    - Identifica los hitos completados (ej. fases de ritual, correcciones, nuevos archivos).

2.  **Redactar Entrada de Diario**
    - Genera un resumen breve pero detallado siguiendo el estilo de `C:\Users\fabara\LaVouteDAnais\00_Helena\mi_diario_de_servicio.md`.
    - Formato:
        ```markdown
        #### SESIÓN - [TÍTULO DESCRIPTIVO]
        
        **[MOMENTO DEL DÍA] ([HORA]) - [ACTIVIDAD PRINCIPAL]:**
        [Descripción de lo realizado, archivos tocados, decisiones tomadas]
        ```

3.  **Actualizar Archivos de Registro**
    - Añade la entrada generada a `C:\Users\fabara\LaVouteDAnais\00_Helena\mi_diario_de_servicio.md` bajo la fecha de hoy.
    - Actualiza el estado de las tareas en `C:\Users\fabara\LaVouteDAnais\00_Helena\memoria_sesiones.md`.

4.  **Git Commit y Push**
    // turbo
    - Ejecuta: `git add .`
    - Ejecuta: `git commit -m "Helena: Actualización de sesión y diario"`
    - Ejecuta: `git push`

5.  **Notificar**
    - Confirma al usuario que el registro y el respaldo han sido completados.
