# 🔧 Rediseño del Engine Escritura LV v4.5 → v4.6

> **Fecha:** 2026-05-27
> **Autor del documento:** Ele (vía agente)
> **Origen:** 3 diagnósticos convergentes (Ele + Colega A + Colega B) sobre el síntoma persistente *"los relatos salen muy limpios, clínicos, no me calientan"*.
> **Estado:** Nivel 3 implementado. Nivel 4 en standby si Nivel 3 no resuelve.

---

## 🩺 Diagnóstico — Convergencia de 3 análisis

Tres perspectivas independientes (interna + 2 colegas externos) llegaron al **mismo problema raíz** por caminos distintos:

| Problema raíz | Diagnóstico Ele | Diagnóstico Colega A | Diagnóstico Colega B |
|---------------|-----------------|----------------------|----------------------|
| Sistema captura QUÉ pasa, no POR QUÉ excita | ✅ Falsa profundidad M1-M17 abstractos | ✅ **Falta Fase 3.4 Mecanismo de Calentón** | ✅ Prosa-anchor faltante |
| Crítico mide corrección, no calentón | ✅ D1-D5 técnicas sin medir mordida | ✅ **2 ejes: Narrativa + Temperatura** | ✅ Test del subrayado |
| Editor suaviza por defecto | ✅ Sanitización iterativa con cada pasada | (implícito) | ✅ **Regla PROHIBIDO TOCAR** |
| Escritor recibe spec procesada | ✅ Briefing inflado de ~30K palabras | ✅ Procesamiento pierde concepto original | ✅ **Concepto literal Ama** |
| Aprendizaje llega tarde (post-fallo) | ✅ Solo aprende después de fracasar | ✅ **Ritual de Calentón ANTES** de escribir | (implícito) |

### Evidencia empírica del problema (síntomas observables)

| Caso | Evidencia |
|------|-----------|
| `la_piel_que_diseno` Cap 1 maestro v1 | Cumplió compromisos, 9.0 Crítico, APROBADO Centinela. **Ama declaró "nunca quedé conforme"** → reset completo. |
| `la_piel_que_diseno` Cap 2 v1.7.1 | Pasó 3 rondas Crítico↔Editor → 9.0+ → **Ama nunca dio Gate final** |
| 24 decisiones canónicas D1-D24 | Parches post-hoc para corregir el arco original insuficiente |
| `esposa_servidumbre` Cap 1 | Necesitó **3 versiones** (v0.1 v1, v0.1 v2 post-M17, v0.1 v3 con Sec 0 contextual) |
| Queja constante de la Ama | *"muy clínico, no se entiende el motivo, no me llamó la atención"* |

**Patrón nítido:** el sistema produce texto técnicamente correcto y eróticamente plano, y aprende SÓLO después del fallo.

---

## 🎯 Causa raíz única

> **El sistema está diseñado como pipeline de FÁBRICA cuando el producto exige ARTESANÍA.**

| Fábrica (v4.5 actual) | Artesanía (lo que el producto exige) |
|------------------------|--------------------------------------|
| Pipeline determinístico 9 fases | Proceso emergente |
| Agentes especializados con role rígido | Una voz autoral consistente |
| Métricas D1-D5 técnicas | Una sola métrica: ¿la lectora se mojó? |
| Checklist de COMPROMISOS | Improvisación dentro de constraints minimalistas |
| Bucle Crítico↔Editor que converge a 9.5 técnico | Iteración con la Ama directamente |
| Documentación masiva (~30K palabras) | Briefing minimalista + ejemplos textuales reales |
| Aprendizaje por reglas de exclusión | Aprendizaje por imitación de ejemplos positivos |
| Agentes con contexto frío cada turno | Una voz que persiste turno a turno |

El engine actual produce un Volkswagen de calidad industrial cuando se pide un Stradivarius.

---

## 🛠️ 4 Niveles de Rediseño

### NIVEL 1 — Reparación quirúrgica (1-2 horas, sin tocar arquitectura)

**Tres ediciones puntuales:**

#### A. `editor.md` — Sección "PROHIBIDO TOCAR" + eliminar Pasada Anti-AI suavizadora

Las repeticiones rítmicas, verbos crudos, oraciones largas-jadeantes y adverbios cargados son SEÑALES DE VIDA del texto. El Editor las preserva, no las suaviza. La "Pasada de Humanización Anti-AI" del paso 10 está aplanando — se elimina.

#### B. `critico.md` — Doble eje Narrativa + Temperatura + Test del Subrayado

Reemplazar la escala única 0-10 por dos ejes independientes:
- **Narrativa** (D1-D5, coherencia técnica) 0-10
- **Temperatura Efectiva** (Test del Subrayado: mínimo 3 frases por 1000 palabras que un lector subrayaría en escenas T° ≥ 4)

Veredicto compuesto:
- Narrativa ≥ 9 + Temperatura ≥ 8 → APROBADO
- Narrativa ≥ 9 + Temperatura < 8 → **DEVOLVER AL ESCRITOR** (no al Editor)
- Narrativa < 9 → DEVOLVER AL EDITOR con cirugías

#### C. `escritor.md` — Estado mental "ESTÁS EN LA ESCENA"

Reemplazar apertura "Eres el Escritor cumpliendo X" por "Estás dentro del cuerpo del personaje sumiso. Sentís la cera caliente sobre tu propio muslo... Escribí hasta que pares por necesidad de respirar, no por contar palabras."

---

### NIVEL 2 — Cambios estructurales (1 día, agrega 1 fase nueva)

Todo lo del Nivel 1, MÁS:

#### D. Nueva **Fase 3.4 — Mecanismo de Calentón** (entre 3.3 Mapa Erótico y 3.5 Escena Piloto)

**No es subagente — es Intake con la Ama, 1 página por capítulo.**

Por cada escena clave del capítulo:
```yaml
Escena:
  [Nombre breve]

Qué ocurre:
  [Acción externa en 1 línea]

Mecanismo psicológico (POR QUÉ esto te excita específicamente):
  [La fantasía emocional que se activa — humillación / liberación /
  rendición / pertenencia / transformación / pérdida de control / 
  validación / otro]

Emoción objetivo:
  [Lo que sentirías leyéndolo — 2-3 emociones combinadas]

Momento crítico (no puede fallar):
  [El segundo exacto donde la fantasía cristaliza]

Error fatal (lo que arruinaría la escena):
  [Lo que NO debe hacer el Escritor — generalmente convertir el 
  momento crítico en catálogo descriptivo]
```

Este documento se llama `mecanismo_calenton_cap[N].md` y es **LECTURA OBLIGATORIA del Escritor antes que el Mapa Erótico**.

#### E. Mover el **Ritual de Calentón ANTES** de Fase 4 (no solo después)

Pre-escritura, 3 preguntas mínimas a la Ama:

```
1. ¿Qué momento imaginas vos cuando pensás en este capítulo?
2. ¿Cuál es la imagen específica que más te interesa ver escrita?
3. ¿Qué momento NO puede fallar (si falla este, el cap falla aunque todo lo demás funcione)?
```

Las respuestas van al briefing del Escritor como PRIORIDAD 1, por encima del Mapa Erótico y del Arco.

#### F. Mapa Erótico v2 con **prosa-anchor**

Cada celda con T° ≥ 4 debe incluir un párrafo-muestra de 3-5 líneas que diga "así suena esto cuando está caliente". No es un texto a copiar — es un termómetro literario que el Escritor usa para calibrar.

---

### NIVEL 3 — Rediseño del flujo (2-3 días, elimina bucle Crítico↔Editor para temperatura)

Todo lo del Nivel 2, MÁS:

#### G. **Eliminar el bucle Crítico↔Editor para temperatura**

Reemplazar el bucle con:

```
Escritor → Crítico (UNA pasada con 2 ejes) →
  - Narrativa OK + Temperatura OK → APROBADO
  - Narrativa OK + Temperatura BAJA → VUELVE AL ESCRITOR (no Editor)
  - Narrativa BAJA → Editor SOLO para ortografía/continuidad
```

El Editor se reduce a **corrector técnico**. No "intensifica" — solo limpia errores. La intensificación, si falta, la hace el Escritor REESCRIBIENDO con feedback caliente, no parchando.

#### H. Escritor recibe **CONCEPTO LITERAL DE LA AMA** + outputs procesados como secundarios

Cambio en el Orquestador: cuando invoca al Escritor, le pasa DOS bloques:

```
<CONCEPTO_AMA_LITERAL>
[Lo que la Ama dijo textualmente en el primer mensaje del proyecto,
sin procesar por Ideador/Arquitecto/Personajes]
</CONCEPTO_AMA_LITERAL>

<REFERENCIA_SECUNDARIA>
[Arco + Personajes + Mapa Erótico + Mecanismo de Calentón]
</REFERENCIA_SECUNDARIA>

Tu prioridad es la voz literal de la Ama. La referencia secundaria
es contexto, no instrucción primaria.
```

#### I. Reducir briefing del Escritor de ~300 líneas a ~50

Mover los detalles operativos a archivos linkeados. El briefing nuclear:
- Estado mental "ESTÁS EN LA ESCENA"
- Concepto literal Ama (prioridad 1)
- Mecanismo de Calentón (prioridad 2)
- 3 preguntas pre-escritura
- Test del Subrayado como objetivo

Todo lo demás (CALENTON_AMA, LIBRO_MAESTRO, GUIA_FETICHISTA, etc.) queda linkeado pero no es obligatorio leerlo entero antes de escribir.

---

### NIVEL 4 — Rediseño radical (1 semana, Stradivarius en lugar de Volkswagen)

**En standby. Solo se aplica si Nivel 3 no resuelve el síntoma.**

Reducir de **9 subagentes a 3**:

| Rol | Función | Reemplaza a |
|-----|---------|-------------|
| **Compositor** | Intake conmigo: concepto + arco mínimo + personajes esenciales + mecanismo de calentón por capítulo. Sin documentos masivos. | Ideador + Arquitecto + Personajes + Diseñador Sensual + Mecanismo de Calentón |
| **Escritor (voz persistente)** | Escribe TODOS los capítulos del relato como un autor real. Lee corpus mínimo (3-5 ejemplos textuales de calentón confirmado de la Ama). | Escritor + bucle Editor |
| **Validador** | UNA pasada con doble eje. Devuelve al Escritor si Temperatura < 7. No edita. | Crítico + Contador + Centinela + Editor |

**Cambios estructurales Nivel 4:**
- `CALENTON_AMA.md` se reescribe como **antología textual** (fragmentos de relatos que calentaron, NO listas de mecanismos abstractos)
- El Escritor tiene "voz persistente" simulada vía `voz_autoral.md` que se acumula con cada capítulo aprobado
- Los relatos pueden no respetar el "arco al milímetro" porque el Compositor produce arcos minimalistas (3-5 puntos por relato, no checklist de 10 compromisos por cap)
- Ritual de Calentón ANTES Y DESPUÉS de cada cap, transcrito literal

---

## 📋 Implementación

**Decisión de la Ama (27/05/2026):** Implementar **Nivel 3** (incluye Nivel 1 + Nivel 2 + cambios estructurales). Nivel 4 en standby si Nivel 3 no resuelve.

### Checklist de cumplimiento

| # | Item | Status |
|---|------|--------|
| A | `editor.md` — PROHIBIDO TOCAR + eliminar Pasada Anti-AI | ⏳ |
| B | `critico.md` — Doble eje + Test del Subrayado | ⏳ |
| C | `escritor.md` — Estado mental ESTÁS EN LA ESCENA | ⏳ |
| D | Nueva Fase 3.4 Mecanismo de Calentón + plantilla | ⏳ |
| E | Mover Ritual de Calentón ANTES de Fase 4 | ⏳ |
| F | `disenador-sensual.md` — Prosa-anchor obligatorio T° ≥ 4 | ⏳ |
| G | Eliminar bucle Crítico↔Editor para temperatura | ⏳ |
| H | Orquestador pasa CONCEPTO_AMA_LITERAL prioridad 1 | ⏳ |
| I | Reducir briefing escritor.md a ~50 líneas + linkeo | ⏳ |
| — | SKILL.md actualizado a v4.6 | ⏳ |
| — | Commit + push v4.6 completo | ⏳ |

### Validación post-implementación

Después de aplicar Nivel 3:
1. Tomar Cap 1 v0.1 v3 de `esposa_servidumbre` (último entregado)
2. Procesar UNA escena con el flujo v4.6 nuevo
3. Comparar contra el v3 actual
4. Si la Ama nota mejora real en mordida → Nivel 3 EXITOSO
5. Si sigue clínico → activar Nivel 4

### Criterios de éxito (cómo sabremos si funcionó)

- **A 1 capítulo:** la Ama identifica 3+ imágenes que la harían parar a respirar (Test del Subrayado)
- **A 3 capítulos:** la Ama da Gate en v1.x sin necesidad de v1.7+ (menos iteraciones manuales)
- **A 5 capítulos:** la Ama declara "no me detengo a corregir tono, solo coherencia"
- **Señal de regresión:** prosa desbordada/incoherente → recortar regla anti-suavizado 30%

---

## 📚 Referencias

- Skill original: `.agent/skills/engine-escritura-lv/SKILL.md` v4.5
- Subagentes: `.claude/agents/` (9 archivos, ~1635 líneas totales)
- Corpus: `01_Canon/Guias_Especializadas/CALENTON_AMA.md` (17 mecanismos M1-M17)
- Diagnósticos completos: este documento (síntesis) + transcripciones de los 3 análisis

---

*La Voûte no es fábrica. Es taller. — v4.6*
