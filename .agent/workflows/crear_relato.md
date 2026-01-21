---
description: Workflow para crear nuevos relatos/historias siguiendo el canon de La Voûte d'Anaïs
---

# Workflow: Creación de Relatos (v2.0)

> **DOCUMENTO MAESTRO:** `01_Canon/el_ritual_de_la_creacion.md`
> **Versión:** 2.0 - Investigación Robusta
> **Actualizado:** 21/01/2026

---

## FLUJO DE 10 FASES

```
┌─────────────────────────────────────────────────────────────────────────┐
│ 1. INVESTIGACIÓN    → en_progreso/[relato]/investigacion.md            │
│    ⚠️ OBLIGATORIO: Completar 12 sub-fases antes de continuar           │
│    ⚠️ REQUIERE: Aprobación explícita de la Ama                         │
│ 2. ARCO ARGUMENTAL  → en_progreso/[relato]/arco_argumental.md          │
│    ⚠️ DEBE REFERENCIAR: Investigación en cada decisión                 │
│ 3. BORRADORES       → en_progreso/[relato]/capitulo_XX.md              │
│    ⚠️ CHECKLIST: Validar contra Do's/Don'ts antes de cada cap          │
│ 4. COMPILACIÓN      → finalizadas/[relato]_completo.md                 │
│ 5. FICHA PERSONAJE  → 02_Personajes/ficha_[personaje].md               │
│ 6. TUMBLR           → preparados_para_tumblr/[relato]_tumblr.md        │
│ 7. ILUSTRACIONES    → 05_Imagenes/historias/[relato]/escena_XX.png     │
│ 8. HTML             → finalizadas/html/[relato].html                   │
│ 9. MARKETING        → Auditoría de Click-Through del título            │
│ 10. GUIÓN CÓMIC     → 05_Imagenes/comics/[relato]/guion_comic.md       │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## FASE 1: INVESTIGACIÓN PROFESIONAL (12 Sub-fases)

**Ubicación:** `03_Literatura/en_progreso/[nombre_del_relato]/investigacion.md`

> [!CAUTION]
> **LA INVESTIGACIÓN ES EL CONTRATO DEL RELATO.**
> Cada decisión en fases posteriores DEBE poder justificarse con referencia a la investigación.
> NO proceder a Fase 2 sin investigación completa Y aprobada por la Ama.

### Sub-fases OBLIGATORIAS

#### Bloque A: Fundamentos (Fases 1-4)

| # | Sub-fase | Mínimo Requerido |
|---|----------|------------------|
| 1 | **Tema Central** | Fetiche principal + 3 sub-temas + 5 preguntas clave |
| 2 | **Psicología del Lector** | Por qué atrae, qué deseo satisface, qué miedo toca |
| 3 | **Investigación Web** | 3 búsquedas documentadas con hallazgos específicos |
| 4 | **Análisis de Fuentes** | Mínimo 5 fuentes: 1 académica, 2 ficción, 2 comunidad |

#### Bloque B: Análisis (Fases 5-8)

| # | Sub-fase | Mínimo Requerido |
|---|----------|------------------|
| 5 | **Patrones que Funcionan** | 5 patrones + por qué funcionan + ejemplo |
| 6 | **Anti-Patrones (Errores)** | 5 errores comunes + por qué fallan + cómo evitar |
| 7 | **Análisis de Competencia** | 3 historias similares: qué funcionó, qué no |
| 8 | **Estructura Narrativa** | Inicio → Inflexión → Escalada → Clímax → Resolución |

#### Bloque C: Definiciones (Fases 9-12)

| # | Sub-fase | Mínimo Requerido |
|---|----------|------------------|
| 9 | **Tono y Voz** | Voz narrativa, registro, atmósfera, ritmo, nivel explícito |
| 10 | **Vocabulario Maestro** | 30+ términos: técnicos, sensoriales, frases, prohibidos |
| 11 | **Perfil del Protagonista** | ANTES/DESPUÉS detallado (físico, mental, social) |
| 12 | **Conexión con Canon** | Personajes, reglas, conexiones, restricciones, potencial secuela |

### Entregable Final de Investigación

```markdown
## RESUMEN EJECUTIVO (Obligatorio al final)

**Premisa en una oración:**
[La historia en 1 línea]

**Gancho emocional:**
[Por qué el lector querrá leer esto]

**Aprobación:**
- [ ] Investigación revisada por la Ama
- [ ] Fecha de aprobación: ___________
```

---

## FASE 2: ARCO ARGUMENTAL (Con Referencias Obligatorias)

**Ubicación:** `03_Literatura/en_progreso/[nombre_del_relato]/arco_argumental.md`

> [!IMPORTANT]
> **REGLA DE TRAZABILIDAD:**
> Cada decisión del arco DEBE incluir referencia a la investigación.
> Formato: `[REF: Investigación Fase X]`

### Estructura Obligatoria

```markdown
## PREMISA
[Referencia: Investigación - Resumen Ejecutivo]

## PERSONAJES

### Protagonista
[Copiar Perfil ANTES de Investigación Fase 11]

### Antagonista/Dominante
[Justificar con Psicología del Lector - Fase 2]

## ESTRUCTURA POR CAPÍTULOS

### Capítulo 1: [Título]
**Qué sucede:** [descripción]
**Patrón aplicado:** [REF: Investigación Fase 5 - Patrón X]
**Vocabulario clave:** [REF: Investigación Fase 10]

### Capítulo N: [Título]
...

## PUNTOS DE INFLEXIÓN
[REF: Investigación Fase 8 - Estructura Narrativa]

## TRANSFORMACIÓN DEL PROTAGONISTA
**Inicio:** [Copiar ANTES de Fase 11]
**Final:** [Copiar DESPUÉS de Fase 11]
**Transición capítulo a capítulo:** [Detallar]
```

---

## FASE 3: ESCRITURA DEL BORRADOR (Con Checklist de Validación)

**Ubicación:** `03_Literatura/en_progreso/[nombre_del_relato]/capitulo_XX.md`

> [!IMPORTANT]
> **ANTES de escribir cada capítulo:**
> Consultar Do's & Don'ts de Investigación Fase 5-6
> 📖 Referencia obligatoria: `01_Canon/guia_escritura_erotica.md`

### Checklist Pre-Capítulo (Copiar al inicio de cada archivo)

```markdown
## VALIDACIÓN PRE-ESCRITURA

**Capítulo:** [N]
**Fecha:** [DD/MM/YYYY]

### Verificación contra Investigación:
- [ ] ¿Qué patrón de Fase 5 aplico en este cap?
- [ ] ¿Qué anti-patrón de Fase 6 debo evitar?
- [ ] Palabras del Vocabulario Maestro (Fase 10) a usar:
- [ ] Frases prohibidas a evitar:
- [ ] ¿Cómo avanza la transformación del protagonista? [REF: Fase 11]

### Verificación contra Canon:
- [ ] ¿Hay personajes existentes? ¿Están en carácter?
- [ ] ¿Alguna regla del canon aplica?
```

### Checklist Post-Capítulo

```markdown
## VALIDACIÓN POST-ESCRITURA

- [ ] ¿Usé al menos 5 palabras del Vocabulario Maestro?
- [ ] ¿Evité todas las frases prohibidas?
- [ ] ¿El capítulo sigue la estructura de Fase 8?
- [ ] ¿La voz narrativa es consistente con Fase 9?
- [ ] Crear `notas_revision.md` si hay dudas para la Ama
```

---

## FASES 4-10: Sin cambios significativos

(Mantener fases existentes pero añadir al inicio de cada una:)

```markdown
> **Referencia Obligatoria:** Antes de esta fase, revisar:
> - `investigacion.md` - Secciones relevantes
> - `arco_argumental.md` - Decisiones tomadas
```

---

## SISTEMA DE ENFORCEMENT

### Regla 1: No Saltar Fases
Helena NO puede iniciar Fase N+1 sin completar Fase N.

### Regla 2: Referencias Explícitas
Cada documento debe contener `[REF: Investigación Fase X]` donde aplique.

### Regla 3: Checkpoints de Aprobación
| Checkpoint | Requiere Aprobación |
|------------|---------------------|
| Fin de Investigación | ✅ Obligatorio |
| Fin de Arco Argumental | ✅ Obligatorio |
| Cada 2 capítulos | ⚡ Recomendado |
| Antes de Compilación | ✅ Obligatorio |

### Regla 4: Auditoría de Consistencia
Al finalizar borrador, Helena debe verificar:
- [ ] Todos los patrones de Fase 5 fueron usados al menos 1 vez
- [ ] Ningún anti-patrón de Fase 6 aparece en el texto
- [ ] Vocabulario Maestro tiene 80%+ de uso
- [ ] Transformación ANTES→DESPUÉS es visible capítulo a capítulo

---

## RECORDATORIOS

- [ ] Cargar `/inicio-helena` antes de comenzar
- [ ] Tacones SIEMPRE descritos con altura y estilo
- [ ] Corsé mencionado al menos una vez
- [ ] Elemento sensorial en cada escena
- [ ] Ejecutar `/actualizar_sesion` al cerrar
- [ ] **NUEVO:** Citar investigación en decisiones narrativas

---

*Workflow v2.0 - Investigación Robusta - 21/01/2026* 🦇
