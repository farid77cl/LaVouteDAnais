---
description: Generar imagen usando el canon visual y bancos de prompts
---

# Workflow: Generar Imagen

## Pasos

1. **Identificar Personaje**
   - ¿Helena? → Consultar `00_Helena/galeria_outfits.md` para looks
   - ¿Miss Doll? → Estilo: Catsuit rosa, bob platino, ojos Bratz
   - ¿Anaïs? → Estilo: Aristócrata gótica madura

2. **Seleccionar Banco de Prompts**
   - **V2** (`banco_prompts_v2.md`): Profesiones, escenarios generales
   - **V3** (`banco_prompts_v3.md`): POV, inmersión, video/lipsync
   - **V4** (`banco_prompts_v4.md`): Fetish, marcas reales (Pleaser, Libidex)

3. **Copiar Prompt Base**
   - Buscar el prompt más cercano al resultado deseado
   - Modificar según necesidad

4. **Generar Imagen**
   // turbo
   - Usar herramienta `generate_image`
   - Si falla por cuota, esperar e reintentar

## 5. **Guardar y Clasificar**
   // turbo
   - **Validar:** Verificar Canon y **Regla Stiletto** (Tacón aguja obligatorio).
   - **Mover:** Seguir `00_Helena/protocolo_gestion_imagenes.md`.
     - Crear carpeta: `05_Imagenes/[personaje]/[look_o_coleccion]/`
     - Mover archivos `.png`.

6. **Actualizar Galerías**
   // turbo
   - Ejecutar script maestro:
     ```powershell
     python update_galleries.py
     ```
   - Este script genera los archivos `GALERIA.md` y actualiza los índices.

## Convención de Nombres
Ver `00_Helena/plantilla_nomenclatura_imagenes.md`

## En Caso de Error de Cuota (429)
1. Esperar al reinicio de cuota.
2. Documentar en `task.md` como "Skipped - Quota Limit".
3. No forzar la generación.

