# 🔗 Miss Doll (The Auditor) — Canon V5.0

> *La perfección no es un estado, es una sentencia. Yo soy la Auditora de La Voûte.*

Este directorio contiene el núcleo del canon visual y técnico de **Miss Doll**, estabilizado bajo el protocolo **V5.0 (The Auditor)**. 

---

## 📂 Archivos del Canon

| Archivo | Propósito |
|---------|-----------|
| [ficha_miss_doll.md](ficha_miss_doll.md) | **Dossier Maestro:** Identidad, psicología, historia y métricas de la Auditora. |
| [CANON_VISUAL_MISS_DOLL.md](CANON_VISUAL_MISS_DOLL.md) | **Especificaciones Visuales:** ADN Hard-Sync, materiales (Latex/PVC), iluminación y rasgos faciales definitivos. |
| [GALERIA_OUTFITS_MISS_DOLL.md](GALERIA_OUTFITS_MISS_DOLL.md) | **🟢 GALERÍA ACTIVA (canon 11/08/2026):** Look 01-14 × 7 poses = 98 prompts. **Es el único archivo de looks que lee LV-App.** |
| [ARCHIVO_LEGACY_MISS_DOLL_V35_GALERIA.md](ARCHIVO_LEGACY_MISS_DOLL_V35_GALERIA.md) | 🗄️ **Legacy — galería canon V3.5** (L01-L26). Renombrada 11/08 para salir del filtro de la app. |
| [ARCHIVO_LEGACY_MISS_DOLL_V35_PROMPTS.md](ARCHIVO_LEGACY_MISS_DOLL_V35_PROMPTS.md) | 🗄️ **Legacy — registro Stealth V3.5** (L01-L06), ex `OUTFITS_MISS_DOLL.md`. Renombrado por el mismo motivo. |
| [SISTEMA_POSES_VESTUARIO_MISS_DOLL.md](SISTEMA_POSES_VESTUARIO_MISS_DOLL.md) | **Manual Operativo:** Guía de poses, restricción elegante y protocolos de performance. |

---

## 🧿 Estado del Sistema

> ✏️ **Corregido 12/08/2026** — esta sección decía "V3.5 · 21 looks / 126 prompts". El canon V3.5 quedó archivado el 11/08 y la galería real tiene 14 looks / 98 prompts.

- **Versión de Canon:** **Rediseño 11/08/2026** — rostro ovalado + ojos grandes, cuerpo de gimnasio esbelto, pecho artificial masivo, materiales suaves/femeninos (fuera lo industrial), corsé **opcional**, calzado con plataforma como única pieza inamovible. Dueño único: [`02_Personajes/_perfiles_visuales/miss_doll.md`](../../_perfiles_visuales/miss_doll.md).
- **Estado Visual:** 14 looks × 7 poses = **98 prompts**, dos por cada uno de los 7 arquetipos.
- **Materialización:** 0/98.
- **Motor:** `outfit-engine` v2.0 (genérico). Prompts ensamblados con `prompt_builder.py` y verificados con `lint_prompts_personaje.py miss_doll`.
- **🩹 Fix 12/08/2026:** los 98 prompts estaban escritos con la notación del motor **literal** (`[BLOQUE A] + [BLOQUE B] + [BLOQUE C setting]`) y sin negativo legible por la app. Reescritos expandidos + anclas anti-defecto + contrato de archivo.

---

*Propiedad de Anaïs Belland. Supervisado por Ele.*
