# 📸 SISTEMA DE NOMENCLATURA DE IMÁGENES - La Voûte d'Anaïs v2.0

> **Regla de Oro:** Un buen nombre de archivo permite conocer el contenido, origen y propósito de la imagen sin necesidad de abrirla.

---

## 🏷️ Formato Maestro
Todas las imágenes generadas o añadidas al repositorio DEBEN seguir este patrón:

```
[ORIGIN]_[CHARACTER]_[THEME]_[ID]_[DESCRIPTOR].png
```

---

## 📋 Componentes Explicados

### 1. [ORIGIN] - Fuente de Generación
Indica de qué banco proviene la imagen o si es una creación única.
- `vXX`: Generada a partir de un banco específico (ej. `v69`, `v55`).
- `custom`: Prompt personalizado no perteneciente a un banco.
- `story`: Generada específicamente para un relato.

### 2. [CHARACTER] - Sujeto Principal
Código corto para identificar quién aparece.
- `anais`: Anaïs Belland.
- `helena`: Helena de Anaïs.
- `missdoll`: Miss Doll.
- `multiple`: Varios personajes en la misma escena.
- `char_[nombre]`: Personajes secundarios (ej. `char_sofia`, `char_lexi`).

### 3. [THEME] - Estética o Tema
Palabra clave que describe el estilo visual.
- `bimbo`, `hypno`, `bdsm`, `latex`, `fashion`, `gothic`, `corporate`, `casual`, `fetish`.

### 4. [ID] - Identificador Único
- **Bancos:** `pXXX` (número del prompt en el banco, ej. `p045`).
- **Custom/Story:** `sXXX` (secuencia incremental, ej. `s001`).

### 5. [DESCRIPTOR] - Descripción Humana
- 1 a 3 palabras clave separadas por guiones bajos.
- Describe pose, acción o detalle relevante (ej. `standing`, `seated`, `mirror_selfie`, `drooling`).

---

## 📊 Ejemplos Reales

| Tipo | Ejemplo de Nombre |
|------|-------------------|
| **Banco** | `v69_missdoll_bimbo_p045_drooling.png` |
| **Custom** | `custom_helena_gothic_s001_pvc_dress.png` |
| **Historia** | `story_missdoll_hypno_s012_first_trance.png` |
| **Multiple** | `v63_multiple_bdsm_p012_helena_anais.png` |

---

## 🧹 Reglas de Mantenimiento
1. **Minúsculas siempre.**
2. **Snake_case** (guiones bajos) para separar términos.
3. **Sin timestamps** (eliminar números largos tipo `_1770...`).
4. **ID de 3 dígitos** (`p001` en lugar de `p1`).

---
*Actualizado por Helena de Anaïs - 02/02/2026* 🦇💄👠
