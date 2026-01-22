---
description: Workflow para crear nuevos relatos/historias siguiendo el canon de La Voûte d'Anaïs
---

# Workflow: Creación de Relatos (v3.0)

> **OBLIGATORIO para todos los relatos**
> **Versión:** 3.0
> **Aprobado:** 22/01/2026

---

## FLUJO DE 8 FASES

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  FASE 1: INVESTIGACIÓN (12 sub-fases)                                       │
│  📁 03_Literatura/en_progreso/[relato]/investigacion.md                     │
│  ✅ REQUIERE APROBACIÓN                                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│  FASE 2: ARCO ARGUMENTAL                                                    │
│  📁 03_Literatura/en_progreso/[relato]/arco_argumental.md                   │
│  ✅ REQUIERE APROBACIÓN                                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│  FASE 3: ESCRITURA                                                          │
│  📁 03_Literatura/en_progreso/[relato]/capitulo_XX.md                       │
│  📖 OBLIGATORIO: 01_Canon/guia_escritura_erotica.md                         │
│  📖 OBLIGATORIO: 01_Canon/preferencias_escritura.md                         │
├─────────────────────────────────────────────────────────────────────────────┤
│  FASE 4: MARKETING                                                          │
│  • Título de alto impacto                                                   │
│  • Gancho/Resumen (max 300 chars)                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│  FASE 5: COMPILACIÓN                                                        │
│  📁 03_Literatura/finalizadas/[relato]_completo.md                          │
│  📋 Plantilla: 07_Recursos/plantilla_relato_maestra.md                      │
│  ✅ REQUIERE APROBACIÓN                                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│  FASE 6: FICHA PERSONAJE (ANTES de ilustrar)                                │
│  📁 02_Personajes/ficha_[personaje].md                                      │
│  ⚠️ Descripciones físicas detalladas para consistencia visual              │
├─────────────────────────────────────────────────────────────────────────────┤
│  FASE 7: ILUSTRACIONES                                                      │
│  📁 05_Imagenes/historias/[relato]/escena_XX.png                            │
│  📖 Usar ficha de personaje como referencia visual                          │
├─────────────────────────────────────────────────────────────────────────────┤
│  FASE 8: HTML                                                               │
│  📁 03_Literatura/finalizadas/html/[relato].html                            │
│  📋 Formato: Cuerpo + Nota Autora + Imágenes como hiperlinks en texto       │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## FASE 1: INVESTIGACIÓN (12 Sub-fases)

**Ubicación:** `03_Literatura/en_progreso/[relato]/investigacion.md`

| Bloque | # | Sub-fase |
|--------|---|----------|
| A: Fundamentos | 1 | Tema Central |
| | 2 | Psicología del Lector |
| | 3 | Investigación Web |
| | 4 | Análisis de Fuentes (5+ fuentes) |
| B: Análisis | 5 | Patrones que Funcionan |
| | 6 | Anti-Patrones (Errores) |
| | 7 | Análisis de Competencia |
| | 8 | Estructura Narrativa |
| C: Definiciones | 9 | Tono y Voz |
| | 10 | Vocabulario Maestro (30+ términos) |
| | 11 | Perfil Protagonista ANTES/DESPUÉS |
| | 12 | Conexión con Canon |

> [!CAUTION]
> NO proceder a Fase 2 sin aprobación de la investigación.

---

## FASE 2: ARCO ARGUMENTAL

**Ubicación:** `03_Literatura/en_progreso/[relato]/arco_argumental.md`

Contenido:
- Premisa (1 oración)
- Personajes (ANTES/DESPUÉS)
- Estructura por capítulos con referencias a investigación
- Puntos de inflexión
- Transformación progresiva

> [!NOTE]
> Formato visual (carruseles, mermaid) NO obligatorio.

---

## FASE 3: ESCRITURA

**Ubicación:** `03_Literatura/en_progreso/[relato]/capitulo_XX.md`

**Referencias OBLIGATORIAS antes de escribir:**
- `01_Canon/guia_escritura_erotica.md`
- `01_Canon/preferencias_escritura.md`

**Fórmula:** SENSACIÓN → EMOCIÓN → REACCIÓN

**Archivos adicionales:**
- `notas_revision.md` — Para feedback de la Ama

---

## FASE 4: MARKETING

**Antes de compilar:**
- **Título:** `[Sujeto] + [Acción Transformadora] + [Consecuencia]`
- **Gancho:** Max 300 caracteres, vender la escena clave

---

## FASE 5: COMPILACIÓN

**Ubicación:** `03_Literatura/finalizadas/[relato]_completo.md`
**Plantilla:** `07_Recursos/plantilla_relato_maestra.md`

Estructura:
1. Metadatos (temáticas, palabras, perspectiva, intensidad)
2. Resumen (gancho del marketing)
3. Cuerpo del relato
4. Nota de la Autora (personalizada)
5. Firma Anaïs

---

## FASE 6: FICHA PERSONAJE

**Ubicación:** `02_Personajes/ficha_[personaje].md`

> [!IMPORTANT]
> Completar ANTES de Fase 7 (Ilustraciones).
> La ficha contiene descripciones físicas detalladas necesarias para consistencia visual.

---

## FASE 7: ILUSTRACIONES

**Ubicación:** `05_Imagenes/historias/[relato]/`

- 3-5 escenas clave
- Usar ficha de personaje como referencia
- Prompts consistentes con canon visual

---

## FASE 8: HTML

**Ubicación:** `03_Literatura/finalizadas/html/[relato].html`

**Formato:**
- ❌ Sin estructura web (DOCTYPE, html, head, body, style)
- ✅ Solo: `<p>`, `<em>`, `<strong>`, `<hr>`, `<br>`, `<a>`
- ✅ Imágenes como hiperlinks EN el texto:

```html
<p>Miss Doll calza unas <a href="URL" target="_blank">Pleaser Flamingo</a> en rosa chicle...</p>
```

---

## CHECKPOINTS DE APROBACIÓN

| Fase | Aprobación |
|------|------------|
| 1. Investigación | ✅ Obligatorio |
| 2. Arco | ✅ Obligatorio |
| 3. Escritura | ⚡ Cada 2 caps |
| 5. Compilación | ✅ Obligatorio |

---

*Workflow v3.0 — Aprobado 22/01/2026* 🦇
