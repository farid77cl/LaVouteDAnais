# `_legacy/` — Scripts one-off ya ejecutados (archivo de solo lectura)

Migraciones y cirugías puntuales que ya cumplieron su función sobre la galería/imágenes.
Se conservan como referencia histórica de **cómo** se hizo cada migración, pero **NO forman parte
del pipeline vivo** y no deben re-ejecutarse a ciegas (asumen estados del repo que ya no existen).

| Script | Qué hizo (one-off) |
|--------|--------------------|
| `fix_galeria_v3.py` | Cirugía final de casos residuales de formato en `galeria_outfits.md`. |
| `migrate_links_utf8.py` | Migración de links a UTF-8 limpio. |
| `move_images.py` | Reubicación masiva de PNGs a la estructura por-look (previo al flujo app). |
| `consolidar_carpetas_looks.py` | Consolidación de carpetas de looks duplicadas/dispersas. |
| `estandarizar_galeria.py` | Estandarización estructural de la galería. |
| `reparar_mismatches.py` | Reparación de mismatches nombre-archivo ↔ registro. |

**Pipeline vivo** (queda en `99_Sistema/scripts/visual/`): `sync_imagenes_subidas.py`,
`update_galleries.py`, `pose_rotation_v5.py`, más las auditorías (`auditar_galeria.py`,
`count_stats.py`, `scan_pending.py`, `auditar_links_por_look.py`).

*Archivado 08/07/2026 — limpieza de mantenimiento (Vibe Architect).*
