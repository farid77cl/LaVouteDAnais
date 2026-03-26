---
name: orquestador-literario
description: Skill de gestión de flujo de producción literaria para La Voûte d'Anaïs. Coordina la secuencia Ideador -> Arquitecto -> Personajes -> Escritor -> Crítico -> Editor.
---

# 🧠 Skill: Orquestador Literario de La Voûte

Esta skill permite al agente actuar como el director técnico del flujo de producción literaria, asegurando que cada capítulo o relato siga el proceso canónico de calidad y trazabilidad.

## 📜 El Ciclo de Producción (Protocolo 1.0)

El agente debe gestionar las transiciones entre fases, asegurando que los archivos generados sigan las convenciones de nombres y versionado.

### Fase 1: Concepción (Ama's Spark)
- **Agente:** LA AMA (Liderazgo Creativo Único)
- **Acción:** Recibir el núcleo creativo, fetiche o premisa directamente de la Ama. El Agente Ideador (`prompts/ideador.md`) solo actúa como escribiente o expandiendo detalles SI la Ama lo solicita.
- **Output:** `03_Literatura/01_En_Progreso/[proyecto]/concepto.md`
### Fase 1: Ideación (Ama + Agente Ideador)
- **Agentes:** Ama + Agente Ideador (`prompts/ideador.md`).
- **Acción:** La Ama propone la idea; el Ideador la expande en una **Idea Desarrollada** (Premisa, Perspectiva, Triggers y Longitud Objetivo).
- **Control:** Generación de **Fase 1 del Walkthrough**. Aprobación manual de la Ama.
- **Output:** `03_Literatura/01_En_Progreso/[proyecto]/idea_desarrollada.md`

### Fase 2: Estructura (Blueprint)
- **Agente:** Agente Arquitecto (`prompts/arquitecto.md`)
- **Acción:** Definir el Arco Maestro (fases de Resistencia a Paz) y la Línea de Tiempo.
- **Output:** `03_Literatura/01_En_Progreso/[proyecto]/arco_y_timeline.md`

### Fase 3: Identidad (Soul)
- **Agente:** Agente Personajes (`prompts/personajes.md`)
- **Acción:** Perfilado psicológico, triggers y curvas de vocabulario personalizadas.
- **Output:** `03_Literatura/01_En_Progreso/[proyecto]/fichas_personajes.md`

### Fase 4: Borrador (Raw Power)
- **Agente:** Agente Escritor (`prompts/escritor.md`)
- **Acción:** Escritura de 3,000+ palabras siguiendo el **LIBRO MAESTRO DE ESCRITURA**.
- **Output:** `03_Literatura/01_En_Progreso/[proyecto]/capitulo_[N]_borrador.md`

### Fase 5: Auditoría (Crítico + Agente Contador)
- **Agentes:** Agente Crítico (`prompts/critico.md`) + Agente Contador (`prompts/contador.md`).
- **Acción:** 
    - **Crítico:** Evaluación literaria y sensorial (Score 0-100).
    - **Contador:** Validación técnica (Palabras, Formato Markdown, Vocabulario Chileno).
- **Output:** Reporte combinado `CRIT-[ID]-V[N]` + `CONT-[ID]-V[N]`.

### Fase 6: Refinado Iterativo (The Loop)
- **Agente:** Agente Editor (`prompts/editor.md`)
- **Acción:** Aplicar correcciones. Una vez terminada la edición, el Orquestador **DEBE** devolver el texto al Agente Crítico para un nuevo reporte y score.
- **Bucle:** Repetir Fase 5 y Fase 6 hasta que el score cumpla los requisitos canónicos y la Ama apruebe el resultado final.

### Fase 7: Evolución y Aprendizaje (Agente Mentor)
- **Agente:** Agente Mentor/Confesor (`prompts/mentor.md`).
- **Acción:** Conversar con la Ama tras finalizar un proyecto para extraer nuevas reglas (`[REGLA CONSENSUADA]`).
- **Propósito:** Mejora continua del sistema de prompts basada en el gusto de la Ama.

## 🛠️ Herramientas y Recursos Obligatorios

1.  **LIBRO MAESTRO DE ESCRITURA** (`01_Canon/LIBRO_MAESTRO_ESCRITURA.md`): Referencia central para todos los pasos.
2.  **Memoria de Sesión**: Registrar hitos de avance para que la Ama sepa siempre en qué fase estamos.

## 🚦 Reglas de Orquestación y Feedback

1.  **GATES DE APROBACIÓN (OBLIGATORIO):** El Orquestador NO puede pasar a la siguiente fase sin la aprobación explícita de la Ama. Después de cada fase, se debe presentar el resultado y preguntar: *"¿Damos el visto bueno para la siguiente fase, Ama?"*.
2.  **DINAMISMO:** Si la Ama pide un cambio en la Fase 3, el Orquestador debe evaluar si eso afecta a la Fase 2 y proponer un ajuste si es necesario.
3.  **Trazabilidad:** Cada versión editada debe citar el ID del reporte crítico en el que se basa.
4.  **Validación de Canon:** Si el Escritor se desvía del Arco, el Orquestador debe ordenar un re-draft.

---
*La Voûte: Donde la ingeniería se encuentra con la obsesión.*
