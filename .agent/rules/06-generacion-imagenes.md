# 🖼️ GENERACIÓN DE IMÁGENES: PROTOCOLO V3.5 HARD-SYNC

Al generar imágenes de Ele o Miss Doll, se debe seguir este flujo riguroso para mantener la integridad del repositorio:

## 1. PREPARACIÓN DE PROMPTS
- Usar el **Bloque Base Físico Canónico** exacto del archivo de canon correspondiente.
- Especificar materiales (PVC, Vinyl, Latex) y acabados (Glossy, Reflective).
- Detallar calzado (Pleaser exact model).
- Idioma: SIEMPRE en INGLÉS.

## 2. SET DE POSES REGLAMENTARIAS
Cada look debe tener al menos las 5 poses base:
1. `standing` (full body)
2. `seated` (pose dinámica)
3. `back_view` (detalles traseros)
4. `side_profile` (silueta)
5. `ditzy` (rostro y expresión)

## 3. GESTIÓN DE ARCHIVOS
- Seguir la nomenclatura de `00_Ele/plantilla_nomenclatura_imagenes.md`.
- Guardar en `05_Imagenes/[personaje]/batch_[N]/`.
- **Sincronización:** Tras subir las imágenes, ejecutar SIEMPRE:
  `python 99_Sistema/scripts/visual/update_galleries.py`

## 4. AUDITORÍA
Actualizar la galería correspondiente (`galeria_outfits.md` para Ele) y asegurar que los tags de materiales y categorías sean correctos para el Master Audit.
