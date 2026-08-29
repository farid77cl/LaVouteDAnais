# 📱 Prompt #20.1 · LV-App 2.0 — PASO 2.1: Lightbox + Creador de Prompts V3.5

> **Continuación de P2** (Pestaña Visual). Requiere P2 verde (galería N/7 pintando).
> **Este paso:** visor a pantalla completa con zoom + el Creador de Prompts V3.5 con copiar en 1 toque.
> **Si aterriza roto:** patch como **Prompt #20.1.x**.

---

## ⚠️ REGLAS
1. Genera SOLO los archivos listados. Reutiliza el `Look`/`Pose`/`LookRepository` de P2.
2. Debe compilar: tocar una imagen abre el Lightbox; el creador genera y copia.

---

```markdown
PASO 2.1 de LV-App 2.0. Sobre la Galería de P2, añade el visor inmersivo y el creador de prompts.

## ARCHIVOS A GENERAR (SOLO ESTOS)
1. ui/screens/visual/LightboxViewer.kt
   - Visor a pantalla completa: HorizontalPager con las poses del look.
   - Pinch-to-zoom + doble-tap (Transformable/graphicsLayer scale-pan).
   - Oculta las barras del sistema (immersive). Botones: compartir, cerrar, "ver prompt".
   - Pase automático opcional cada 4s (toggle).

2. ui/screens/visual/VisualScreen.kt (editar)
   - Al tocar una tarjeta/imagen → navega/abre LightboxViewer con ese look.

3. data/PromptV35Builder.kt
   - Ensambla el prompt en inglés bajo protocolo V3.5 Hard-Sync:
     BLOQUE A fijo (ADN físico: 1000cc ultra high-profile spherical implants, dark cherry red
     hip-length extensions, grey-green eyes, glossy hot pink lips, XXXL French nails, porcelain
     hyper-polished skin) + pose seleccionada + campos de outfit (material, color, silueta, calzado ≥12cm)
     + SINGLE_FRAME + SKIN_LOCK + negativos (flat shoes, sneakers, barefoot, kitten heel, chunky).
   - `build(fields): String`.

4. ui/screens/visual/PromptCreatorSheet.kt
   - Bottom sheet: selectores (pose, material, color, silueta, calzado), preview en vivo del prompt,
     botón "Copiar" que copia al portapapeles en 1 toque (con snackbar de confirmación).
   - Accesible desde un FAB en VisualScreen.

## CRITERIO DE ÉXITO
Compila · tocar imagen → Lightbox con zoom fluido e immersive · "ver prompt" muestra el prompt del look ·
el Creador arma un prompt V3.5 válido y lo copia en 1 toque.

Entrega SOLO estos 4 puntos. Siguiente: P3 (Room DB + notas por imagen).
```
