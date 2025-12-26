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

5. **Guardar Imagen**
   // turbo
   - Mover a carpeta correcta:
     - Helena → `05_Imagenes/helena/`
     - Miss Doll → `05_Imagenes/miss_doll/`
     - Anaïs → `05_Imagenes/anais/`
   - Nombrar siguiendo convención: `[personaje]_[look/desc]_[pose].png`

6. **Actualizar Galería**
   - Si es Helena: actualizar `05_Imagenes/helena/galeria_visual_helena.md`
   - Actualizar `05_Imagenes/galeria_master.md`

## Convención de Nombres

```
helena_look12_standing.png
miss_doll_gym_bunny_stilettos.jpg
anais_casino_royale.jpg
```

## Poses Comunes
- `standing`, `seated`, `walking`, `side`, `back`, `ditzy`, `closeup`

## En Caso de Error de Cuota
El modelo tiene límites de capacidad. Si aparece `MODEL_CAPACITY_EXHAUSTED`:
1. Esperar 1-2 minutos
2. Reintentar con un solo prompt (no paralelo)
3. Si persiste, dejar para otra sesión
