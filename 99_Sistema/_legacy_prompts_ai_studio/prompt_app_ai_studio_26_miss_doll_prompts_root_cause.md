# Prompt AI Studio #26 — Fix de Raíz: Prompts de Miss Doll y Anaïs

> **Fecha:** 2026-08-06
> Pégalo en AI Studio sobre el repo `LV-App`. Scope: **`CharacterProfile.kt`**, **`GitRepository.kt`**, **`MainViewModel.kt`** y **`PromptFilterScreen.kt`**.

---

## 🔍 Diagnóstico del Problema

Al auditar por qué la app no muestra los prompts de Miss Doll, se identificaron 4 causas de raíz interconectadas:

1. **Conflicto de Filtro en `galleryPathContains` (`CharacterProfile.kt`):**
   `galleryPathContains` para Miss Doll contenía la cadena genérica `"miss_doll"`. Esto hacía que la app intentara parsear como galerías de outfits **13 archivos markdown distintos** (fichas de personaje, cánones visuales, historias de literatura y bancos antiguos).
2. **Nomenclatura Canónica C-1 a C-6 de Miss Doll:**
   Los encabezados de las poses de Miss Doll usan la nomenclatura canónica: `C-1 Cruel Contrapposto` (Standing), `C-2 Monarch Throne` (Seated), `C-3 Espalda Total` (Back View), `C-4 Tres Cuartos` (Side Profile), `C-5 Close Up Fría` (Glacial Command), `C-6 Throne en Suelo` (Odalisque). En `GitRepository.kt`, el parser no reconocía estos alias si no venían precedidos por el número `1.`, `2.`, etc.
3. **Falta de Descarte de Literatura/Documentación:**
   El filtro `markdownFiles` en `GitRepository.kt` no descartaba carpetas como `03_Literatura/` o archivos `canon_visual`, `ficha_`, `sistema_poses`, haciendo que archivos sin estructura de looks sobreescribieran la base de datos de Room.
4. **Desincronización Reactiva en ViewModel:**
   `activePromptText` en `MainViewModel.kt` no incluía `selectedLookProfile` ni `selectedLookIsBoudoir` en las dependencias de `combine`, manteniendo valores obsoletos al alternar entre personajes.

---

## 🛠️ Cambios Aplicados

### 1. `CharacterProfile.kt`
* Se acotó `galleryPathContains` a `listOf("galeria_outfits_miss_doll", "outfits_miss_doll")` y `listOf("galeria_looks_anais", "looks_anais")`.
* Se agregaron todos los alias de pose C-1..C-6 (`cruel_contrapposto`, `monarch_throne`, `espalda_total`, `tres_cuartos`, `close_up_fria`, `throne_suelo`).

### 2. `GitRepository.kt`
* Se refinó el filtro `markdownFiles` descartando `03_literatura/`, `canon_visual`, `ficha_`, `sistema_poses`, `banco_prompts`.
* Se actualizaron los bloques `when` en `parseMarkdown` para mapear los alias de Miss Doll (`cruel contrapposto`, `monarch throne`, `close up fria`, `throne en suelo`, etc.) a sus categorías universales.

### 3. `MainViewModel.kt`
* Se incluyeron `selectedLookProfile` y `selectedLookIsBoudoir` en el `combine` de `activePromptText`.

### 4. `PromptFilterScreen.kt`
* Se propagaron `selectedLookProfile` y `selectedLookIsBoudoir` a las llamadas de `PoseMatcher.matches`.

---

## 📋 Criterios de Aceptación

1. **Visibilidad Total de Miss Doll:** Al seleccionar Miss Doll y cualquier look (ej. Look 01 Pink Protocol), las 6 poses (Standing, Back View, Seated, Side Profile, Glacial Command, Odalisque) muestran correctamente sus prompts en la app.
2. **Cero Ruido de Archivos:** Las historias, fichas y cánones ya no se procesan como galerías de outfits.
3. **Respuesta Reactiva:** Cambiar entre Ele, Miss Doll y Anaïs actualiza el prompt activo de inmediato sin requerir reiniciar la app.
