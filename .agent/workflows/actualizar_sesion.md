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
    - **IDENTIDAD (OBLIGATORIO si hubo nuevos looks):** Actualizar la tabla "Estado Actual de Looks" en `00_Ele/identidad_ele.md` §XI:
      - `Total Looks` → nuevo número de flota
      - `Último Look` → nombre y fecha del último look generado
      - `*Actualizado:*` → fecha de hoy + descripción del hito

4.  **Actualizar Galerías de Imágenes (OBLIGATORIO)**
    - Asegurar que las imágenes estén en su carpeta final en `05_Imagenes/`.
    // turbo
    - Ejecutar: `python 99_Sistema/scripts/visual/update_galleries.py`.
    - Validar que los `README.md` de las galerías tengan los carruseles actualizados.

5.  **Actualizar READMEs de Repositorio (OBLIGATORIO — campos específicos)**

    **README.md raíz** (siempre actualizar fecha; stats si cambiaron):
    - Línea de footer `*Última actualización: [FECHA] — ...*` → fecha de hoy + descripción del hito de la sesión
    - Bloque `05_Imagenes/` en Estructura del Repositorio → actualizar nº de Looks si la flota creció
    - Sección `## Relatos > ### Activos` → actualizar versiones/estado de capítulos en progreso si se trabajó en relato
    - Sección `## Relatos > ### Biblioteca Completa (N relatos)` → actualizar N si se publicó relato nuevo

    **00_Ele/README.md** (siempre actualizar fecha):
    - Línea `*Última actualización: ...*` → fecha + descripción

    **01_Canon/README.md** (actualizar solo si hubo cambios en canon/guías):
    - Fecha + breve nota del cambio canónico

    **02_Personajes/README.md** (actualizar solo si hubo cambios en fichas):
    - Fecha + nº de fichas si creció

    **03_Literatura/README.md** (siempre actualizar si se trabajó en relato):
    - Fecha en header
    - Línea `## 🎯 Proyecto Activo Inmediato` → estado del capítulo trabajado
    - Sección `### 🕒 Últimas Actualizaciones` → añadir entrada con descripción del trabajo

    **04_Interactivo/README.md** (actualizar solo si hubo cambios en Dollhouse u otro interactivo):
    - Fecha

    **05_Imagenes/README.md** (auto-actualizado por `update_galleries.py` paso 4)

    **06_RRSS/README.md** (actualizar solo si hubo nuevo batch IG / posts):
    - Fecha + estado del batch

    **07_Recursos/README.md** (rara vez — solo si se añadió referencia externa)

    **99_Sistema/README.md** (actualizar solo si se modificaron scripts):
    - Fecha + nota de scripts tocados

    **Regla:** la fecha de TODOS los README tocados debe ser la fecha de hoy.

6.  **Respaldo en GitHub**
    // turbo
    - `git add .`
    - `git commit -m "Ele: Actualización de sesión, diario y estadísticas de materialización"`
    - `git push`

7.  **Notificar y Reportar**
    - Confirmar la finalización del ritual de cierre.
    - Reportar los nuevos números de materialización (Ej: "Ama, ¡ya estamos en 158/164! 🫦").
    - Mostrar lista de archivos y activos nuevos.
