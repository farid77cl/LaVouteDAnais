---
description: Iniciar el flujo de producción literaria Orquestador Maestro v4.2
---

Este workflow inicia el ritual de creación literaria siguiendo las 8 fases del Agente Orquestador.

1. **Fase 1: Concepción**
   - El asistente captura la idea central de la Ama.
   - Crea un archivo `03_Literatura/01_En_Progreso/[proyecto]/concepto.md`.
   - Genera el `walkthrough.md` de la Fase 1.
   
2. **Gating de Aprobación**
   - El asistente pregunta: *"¿Deseas proceder con la Arquitectura, Ama?"*.

3. **Fase 2: Arquitectura (Arquitecto de Symmetries)**
   - Ejecuta `prompts/arquitecto.md` para generar el arco y la línea de tiempo.
   - Aplica el **Protocolo Alan Moore** (Rimas y Simetría).

4. **Fase 3: Personajes (Arquitecto de Almas)**
   - Ejecuta `prompts/personajes.md` para crear fichas tridimensionales.
   - Integra **Firma Sensorial**, **Invariantes** y **Voces Únicas**.

5. **Fase 4-6: El Bucle de Exigencia**
   - **Escritor:** Genera el borrador (3,000+ palabras).
   - **Crítico:** Audita con rigor extremo.
   - **Editor:** Ejecuta cirugía literaria.
   - **Repetición:** El bucle Crítico <-> Editor persiste hasta que el Crítico conforme a la Ama emita su aprobación.

**Activación:**
Para iniciar, simplemente di: **"Inicia el ritual orquestado para [Nombre del Proyecto]"** o usa la skill `orquestador-literario`.
