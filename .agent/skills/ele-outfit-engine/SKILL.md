---
name: ele-outfit-engine
description: Motor especializado en la creación y gestión de la identidad visual de Ele. Gestiona la generación de prompts bajo el protocolo V3.5 Hard-Sync, asegura la consistencia de imagen en múltiples poses, y mantiene actualizadas las estadísticas de la galería de outfits. Úsalo cada vez que se solicite un "Outfit del Día", un nuevo Look, o una auditoría del repositorio visual.
---

# 👠 Ele Outfit Engine (V3.5)

Este Skill es el motor central para mantener la coherencia estética y técnica de Ele. Su objetivo es garantizar que cada nuevo activo visual respete el ADN canónico y mantenga el equilibrio estadístico del repositorio.

## 🧬 ADN V3.5 Hard-Sync (Referencia Rápida)

Para cada generación de imagen, **DEBES** incluir estos elementos de forma explícita para evitar variaciones:

- **Físico:** Oval face, high cheekbones, grey-green eyes, dark cherry red hair (XXXL extensions, hip-length).
- **Modificaciones:** Blackwork tattoos (upper back, arms, outer thighs), 14k white gold piercings (navel, nipple piercings pressing through clothing).
- **Estética:** Dramatic siren liner, glossy hot pink lips, XXXL French nails (5cm, white tips).
- **Calidad:** 8k, editorial fashion photography, high-gloss specularity.

## 🛠️ Workflow Operativo

### 1. Análisis de Mix de Arquetipos
Antes de proponer un Look, consulta la tabla de estadísticas en [galeria_outfits.md](file:///c:/Users/farid/LaVouteDAnais/00_Ele/galeria_outfits.md).
- **Meta:** Bikini (25%), Lencería (25%), Gym/Athleisure (25%), Mix/Domestic/Escort (25%).
- Si una categoría está baja, el nuevo Look **debe** pertenecer a esa categoría.

### 2. Construcción de Prompts Consistentes
Usa el "Prompt de Concepto" (Standing) como base para el resto de las poses. No permitas variaciones en el material del vestuario (ej: si es látex negro, debe serlo en todas las poses).

Poses estándar obligatorias:
- **Standing:** Vista de cuerpo completo, concepto del look.
- **Back View:** Enfoque en arquitectura del traje y tatuajes de espalda.
- **Seated:** Enfoque en actitud y detalles de accesorios.
- **Side Profile:** Silueta y curvas de relojero.
- **Ditzy:** Close-up facial, expresión vacante, labios entreabiertos.

### 3. Gestión de Activos (Remote-Only)
Sigue rigurosamente el protocolo de limpieza:
1. Generar imágenes.
2. Guardar en `05_Imagenes/ele/lookXXX/`.
3. Hacer `git add`, `git commit` y `git push`.
4. **ELIMINAR** los archivos binarios locales para mantener el repositorio ligero.
5. Actualizar el walkthrough con links `file:///C:/Users/farid/.gemini/antigravity/brain/...` para visualización inmediata.

### 4. Actualización de Estadísticas
Tras crear un Look, recalcula los totales y porcentajes en la cabecera de `galeria_outfits.md`.

## 📂 Recursos del Skill
- [DNA_V3_5.md](references/dna_v3_5.md): Descripción detallada para prompts.
- [stats_updater.py](scripts/stats_updater.py): Script (pseudocódigo) para automatizar el conteo.
