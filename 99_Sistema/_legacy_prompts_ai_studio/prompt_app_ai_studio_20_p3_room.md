# 📱 Prompt #20 · LV-App 2.0 — PASO 3: Capa de Datos Room (persistencia + notas)

> **Requiere P2 + P2.1 verdes.** Formaliza la persistencia: cachea la flota offline y agrega notas por imagen.
> **Si aterriza roto:** patch como **Prompt #20.3.x**.

---

## ⚠️ REGLAS
1. Genera SOLO los archivos listados. Añade room-runtime, room-ktx y el compilador vía KSP.
2. Debe compilar: la galería carga desde Room (offline) y las notas persisten.

---

```markdown
PASO 3 de LV-App 2.0. Añade persistencia con Room sobre la capa de datos de P2.

## ARCHIVOS A GENERAR (SOLO ESTOS)
1. data/db/AppDatabase.kt (version = 1, exportSchema = false)
   Entidades:
   - LookEntity: id, number, batch, pose, imagePath, isMaterialized, promptV35, updatedAt.
   - ChapterEntity: id, storyTitle, chapterNumber, chapterTitle, contentMarkdown, audioUrl,
     durationSeconds, readProgress, lastReadPosition. (se usa en P4 — crear ya la tabla)
   - PostQueueEntity: id, lookId, captionText, platform, status, scheduledAt. (se usa en P5 — crear ya)
   - ImageNoteEntity: id, lookNumber, pose, noteText, updatedAt.
   DAOs: LookDao, ChapterDao, PostQueueDao, ImageNoteDao (con Flow).

2. data/LookRepository.kt (editar)
   - `refresh()` reindexa desde archivos (P2) y hace UPSERT a Room.
   - `looks()` ahora emite desde Room (single source of truth); si Room vacío, dispara refresh.

3. data/NotesRepository.kt
   - CRUD de notas por (lookNumber, pose). `notesFor(look): Flow<List<ImageNoteEntity>>`.
   - `exportCsv(): File` → escribe `notas_imagenes.csv` en el repo clonado (lookNumber,pose,note).

4. ui/screens/visual/LightboxViewer.kt (editar)
   - Campo de nota por imagen (lee/guarda vía NotesRepository), visible en el visor.

5. AppDatabaseTest.kt — test real de insert/read de LookEntity e ImageNoteEntity.

## CRITERIO DE ÉXITO
Compila · primera carga clona+indexa+guarda en Room · segunda carga es offline desde Room ·
agregar una nota en el Lightbox persiste tras reabrir · exportCsv genera notas_imagenes.csv.

Entrega SOLO estos 5 puntos. Siguiente: P4 (Lector Nivel 4).
```
