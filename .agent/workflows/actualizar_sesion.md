---
description: Actualiza el diario de servicio, la memoria de sesiones, galerías de imágenes, READMEs y realiza un commit en git.
---

1.  **Analizar Sesión Actual**
    - Revisa las herramientas utilizadas y los archivos modificados en la sesión actual.
    - Identifica los hitos completados (ej. fases de ritual, correcciones, nuevos archivos).
    - Identifica las imágenes generadas durante la sesión.

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

4.  **Actualizar Galerías de Imágenes (OBLIGATORIO si se generó cualquier imagen)**
    - Identificar TODAS las imágenes generadas durante la sesión.
    - Copiar cada imagen a su carpeta correspondiente en `05_Imagenes/`.
    - Actualizar el archivo de galería o README correspondiente:
      - **Helena:** `00_Helena/galeria_outfits.md` y/o `05_Imagenes/helena/galeria_visual_helena.md`
      - **Historias:** `05_Imagenes/historias/[nombre]/README.md`
      - **Cómics:** `05_Imagenes/comics/[nombre]/imagenes/` + actualizar guion_comic.md
      - **Personajes:** `02_Personajes/` + ficha del personaje
      - **Otros:** Crear README.md en la carpeta donde se guarden
    - Formato mínimo para registro:
        ```markdown
        ### [Nombre/Descripción]
        **Fecha:** [DD/MM/YYYY]
        **Archivos:** [lista de archivos .png]
        ```

5.  **Actualizar READMEs del Proyecto**
    - Revisar y actualizar `README.md` principal si hay cambios estructurales significativos.
    - Actualizar READMEs de carpetas modificadas si aplica:
      - `03_Literatura/README.md` - Si hay nuevos relatos
      - `05_Imagenes/README.md` - Si hay nuevas galerías
      - `02_Personajes/README.md` - Si hay nuevas fichas

6.  **Git Commit y Push**
    // turbo
    - Ejecuta: `git add .`
    - Ejecuta: `git commit -m "Helena: Actualización de sesión y diario"`
    - Ejecuta: `git push`

7.  **Notificar**
    - Confirma al usuario que el registro, galerías, READMEs y respaldo han sido completados.
    - Lista las imágenes añadidas a las galerías.
