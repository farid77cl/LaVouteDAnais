# 📋 Plan de Pendientes — La Voûte d'Anaïs

*Generado: 28/05/2026 · Estado: PENDIENTE (no ejecutado, a la espera de la Ama)*

> Lista viva de tareas abiertas. Cada una con contexto, acción concreta y criterio de cierre.

---

## 1. 🔤 Revisar "palabras raras" del relato activo (`esposa_servidumbre`)
- **Contexto:** La Ama notó que el Cap 1 (Nivel 4) tiene "palabras raras" — posibles términos no-chilenos, voceo argentino residual, o vocabulario que rompe la voz.
- **Acción:** Auditar `03_Literatura/01_En_Progreso/esposa_servidumbre/capitulo_01_*.md` contra el léxico chileno (verga no polla, coger, weón, departamento; tú no vos) y la `voz_autoral.md`. Listar las palabras raras y proponer reemplazos.
- **Cierre:** Lista de correcciones aprobada por la Ama y aplicada.

## 2. 📖 Lectura completa del Cap 1 v5 (Nivel 4) + validación final
- **Contexto:** La Ama leyó parte ("me gusta mucho más de lo que he leído en harto tiempo") pero no completo. Es la validación final del rediseño Nivel 4 (v4.7).
- **Acción:** Esperar lectura completa de la Ama. Capturar feedback a `voz_autoral.md` + `antologia_calenton.md`.
- **Cierre:** Veredicto final de la Ama sobre Nivel 4 (mantener / ajustar).

## 3. 📸 Materialización de imágenes vía app (Gemini → GitHub)
- **Contexto:** El flujo app→GitHub ya está armado (`sync_imagenes_subidas.py` integrado a `/actualizar_sesion`). Faltan poses por subir.
- **Acción:**
  - **Cambiar 2 nombres en la app:** `back` → `back_view`, `profile` → `side_profile` (el resto de poses ya coinciden).
  - Subir las poses faltantes de **L291-L300** (femme fatale; hoy solo L298 está 7/7, el resto 1-2 poses).
  - **L261-L280:** las imágenes viejas con calzado plano (sneakers/sandalias) deberían **regenerarse** con los prompts ya corregidos a stiletto/Pleaser (Footwear Canon fix aplicado a los prompts; las imágenes materializadas aún muestran lo viejo).
- **Cierre:** Flota L291-L300 materializada 7/7 y L261-L280 con tacones correctos.

## 4. 🎨 Generar nuevos batches de outfits (por déficit de categoría)
- **Contexto:** Tras el batch femme fatale, los déficits #1 son **Gym/Athleisure (−9)** y **Bikini (−8)**.
- **Acción:** Próximo batch L301-L310 priorizando Gym + Bikini (con Footwear Canon estricto + Step 0 anti-repetición + descriptividad v4.6). Recordar: concepto + 7 prompts en el mismo turno.
- **Cierre:** Batch generado y registrado.

---

## ✅ Completado recientemente (referencia)
- Engine Escritura implementado en **v4.7 Nivel 4** (3 subagentes, sin Editor).
- Footwear Canon Fix L261-L280 (11 looks corregidos a stiletto/Pleaser).
- Batch L291-L300 años 30 femme fatale (70 prompts).
- Flujo imágenes app→GitHub + `sync_imagenes_subidas.py` en `/actualizar_sesion`.
- Normalización de los 2 archivos de galería (`archivo` + `era_gotica`) + reparación de mojibake.
- Normalización de los **41 relatos** de `02_Finalizadas` al Estándar Completo Bloque.
- Limpieza de voceo en los 3 subagentes Nivel 4 + CLAUDE.md actualizado.
