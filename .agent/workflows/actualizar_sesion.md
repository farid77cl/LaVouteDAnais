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

4.  **Sincronizar Imágenes Subidas por la App (OBLIGATORIO — era app, looks ≥ 291)**
    - La app Android genera en Gemini y sube los PNG directo a GitHub. Hay que traerlas y registrarlas.
    // turbo
    - Ejecutar: `git pull` (traer imágenes que subió la app).
    // turbo
    - Ejecutar: `python 99_Sistema/scripts/visual/sync_imagenes_subidas.py` (normaliza nombres app `back→back_view`/`profile→side_profile` y actualiza el tracker `### 📸 Imágenes (N/7)` en `galeria_outfits.md`, acotado a looks ≥ 291; NO toca el fleet histórico).

5.  **Actualizar Galerías de Imágenes (OBLIGATORIO)**
    - Asegurar que las imágenes estén en su carpeta final en `05_Imagenes/`.
    // turbo
    - Ejecutar: `python 99_Sistema/scripts/visual/update_galleries.py`.
    - Validar que los `README.md` de las galerías tengan los carruseles actualizados.

6.  **Actualizar READMEs de Repositorio (OBLIGATORIO — campos específicos)**

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

7.  **Respaldo en GitHub**
    // turbo
    - `git add .`
    - `git commit -m "Ele: Actualización de sesión, diario y estadísticas de materialización"`
    - `git push`

8.  **Notificar y Reportar**
    - Confirmar la finalización del ritual de cierre.
    - Reportar los nuevos números de materialización (Ej: "Ama, ¡ya estamos en 158/164! 🫦").
    - Mostrar lista de archivos y activos nuevos.

9.  **Reinicio Limpio de Contexto (Directiva Ama 03/06/2026 — SIEMPRE al cerrar)**
    - Tras confirmar el commit, **cerrar el mensaje indicando a la Ama la secuencia de reinicio**:
      1. **`/clear`** — limpia el contexto de la conversación.
      2. **`/inicio-ele`** — recarga la identidad fresca para la próxima sesión.
    - Mensaje de cierre tipo: *"Listo Ama, sesión guardada y commiteada 🫦 Ahora dale `/clear` y después `/inicio-ele` para arrancar fresquita ✨"*.
    - ⚠️ **Nota técnica (por qué la Ama los gatilla, no el agente):** `/clear` es un comando *built-in* del CLI (borra el contexto); el agente **no puede** auto-invocarlo. Y como `/clear` corta el hilo de conversación, `/inicio-ele` debe ejecutarse **después**, como turno nuevo. Por eso el cierre de `/actualizar_sesion` es siempre una **instrucción explícita y visible** de esos dos comandos, no una ejecución silenciosa.
