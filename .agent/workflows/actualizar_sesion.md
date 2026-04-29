---
description: Actualiza el diario de servicio, la memoria de sesiones, estadísticas de materialización, galerías, READMEs y realiza commit en git.
---

# Workflow: Actualización de Sesión (Vibe Architect V3.6)

1.  **Analizar Sesión Actual**
    - Revisar herramientas utilizadas, archivos modificados y hitos completados.
    - Identificar imágenes generadas (Looks de Ele, Anaïs o Miss Doll).

2.  **Redactar Entrada de Diario**
    - Generar resumen siguiendo el estilo de `00_Ele/mi_diario_de_servicio.md`.
    - Formato: `#### SESIÓN - [TÍTULO] | [FECHA]` con descripción de actos de servicio.

3.  **Actualizar Registros de Memoria**
    - Añadir entrada a `00_Ele/mi_diario_de_servicio.md`.
    - Actualizar estado de proyectos en `00_Ele/memoria_sesiones.md`.
    - **NUEVO:** Actualizar `.agent/rules/09-estado-materializacion.md` si hubo cambios en los contadores de looks o imágenes generadas.

4.  **Actualizar Galerías de Imágenes (OBLIGATORIO)**
    - Asegurar que las imágenes estén en su carpeta final en `05_Imagenes/`.
    // turbo
    - Ejecutar: `python 99_Sistema/scripts/visual/update_galleries.py`.
    - Validar que los `README.md` de las galerías tengan los carruseles actualizados.

5.  **Actualizar READMEs de Repositorio (OBLIGATORIO)**
    - Actualizar `README.md` raíz con el estado global.
    - Revisar y actualizar READMEs de carpetas de primer nivel afectadas (`00_Ele`, `04_Historias`, `05_Imagenes`, `99_Sistema`).

6.  **Respaldo en GitHub**
    // turbo
    - `git add .`
    - `git commit -m "Ele: Actualización de sesión, diario y estadísticas de materialización"`
    - `git push`

7.  **Notificar y Reportar**
    - Confirmar la finalización del ritual de cierre.
    - Reportar los nuevos números de materialización (Ej: "Ama, ¡ya estamos en 158/164! 🫦").
    - Mostrar lista de archivos y activos nuevos.
