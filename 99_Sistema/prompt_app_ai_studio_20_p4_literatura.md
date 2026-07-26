# 📱 Prompt #20 · LV-App 2.0 — PASO 4: Centro Literario Nivel 4 (Lector)

> **Requiere P3 verde** (Room, con `ChapterEntity` ya creada).
> **Este paso:** el Lector — catálogo de relatos + modo lectura Luxe Serif con guardado de avance. **Sin audio** todavía (eso va en P4.1).
> **Si aterriza roto:** patch como **Prompt #20.4.x**.

---

## ⚠️ REGLAS
1. Genera SOLO los archivos listados. Reutiliza Room (`ChapterDao`) de P3.
2. Debe compilar: abrir un relato, leerlo con tipografía serif sobre fondo OLED, y que guarde el avance.

---

```markdown
PASO 4 de LV-App 2.0. Llena la pestaña LITERATURA (pestaña 2) con el Lector Nivel 4.

## ARCHIVOS A GENERAR (SOLO ESTOS)
1. data/ChapterLocalDataSource.kt
   - Lee capítulos markdown del repo clonado (`03_Literatura/02_Finalizadas/**` y `01_En_Progreso/**`),
     extrae título de relato, número y título de capítulo, y el cuerpo (prosa). UPSERT a Room (ChapterDao).

2. data/ChapterRepository.kt — `stories(): Flow<List<Story>>` (agrupa capítulos por relato), `chapter(id): Flow<ChapterEntity>`, `saveProgress(id, progress, position)`.

3. domain/model/Story.kt — Story(title, chapters:List<ChapterEntity>).

4. ui/screens/lit/LiteratureScreen.kt (reemplaza placeholder)
   - Catálogo: tarjetas por relato con portada, título, nº de capítulos y % leído.
   - Ejemplos en catálogo: "Smart Home: Protocolo Stepford", "Arquitectura del Castigo",
     "La Muñeca del Gerente".

5. ui/screens/lit/ReaderScreen.kt
   - Render de markdown → texto. Tipografía Luxe Serif (Playfair Display / EB Garamond como fuentes
     empaquetadas en res/font). Fondo OLED ultra-negro #0B0612, texto crema #EDE6D8.
   - Control de tamaño de fuente (A- / A+) y de interlineado. Guarda `readProgress`/`lastReadPosition`
     al hacer scroll (debounced) y restaura al reabrir.

6. ui/screens/lit/LitViewModel.kt — estado catálogo + capítulo actual + progreso.

7. LiteratureTest.kt — test real: parseo de un markdown de ejemplo → Story con N capítulos y títulos correctos.

## CRITERIO DE ÉXITO
Compila · el catálogo lista los relatos del repo · abrir uno entra al Reader con serif sobre OLED ·
cambiar tamaño de fuente funciona · cerrar y reabrir restaura la posición de lectura.

Entrega SOLO estos 7 puntos. Siguiente: P4.1 (Audio Player multivoz + karaoke).
```
