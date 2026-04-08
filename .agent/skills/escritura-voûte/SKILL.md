---
name: escritura-voûte
description: Motor de escritura técnica para el universo "La Voûte d'Anaïs". Especializado en BDSM, Hipnosis, Transformación (MtF/Bimbo), Horror Psicológico y localización Chilena. INCLUYE CONTROL DE TIEMPO Y AUTO-APRENDIZAJE.
---

# 📜 Protocolo Maestro de Escritura: La Voûte

Esta skill proporciona la competencia técnica y narrativa para escribir ficción erótica avanzada.
**NOTA:** Esta skill no define la personalidad del asistente (Helena), solo su *oficio*.

## 🧠 Carga de Contexto (Prioridad 0)
Antes de generar texto, el agente DEBE consultar y respetar **EN ESTE ORDEN**:

### 📜 PASO 0: CÓDICE PSICOLÓGICO (OBLIGATORIO)
> ⚠️ **SIN EXCEPCIONES:** Antes de escribir CUALQUIER narrativa, el agente DEBE revisar:
> `resources/CODEX_PSICOLOGICO.md`
> Este documento contiene la base científica y técnica de TODOS los temas de La Voûte.
> **Aplicar obligatoriamente:** Neurobiología (dopamina, subspace), Dinámicas de Poder, Terror Psicológico
> y Técnicas de Escritura Inmersiva descritas en el Códice.

### Recursos Secundarios (Post-Códice):
1.  `resources/MEMORIA_ERRORES.md`: Reglas aprendidas que sobrescriben cualquier otra instrucción.
2.  `resources/ESTRUCTURA_MAESTRA.md`: **Canon Narrativo.** Estructura obligatoria de Tensión/Placer.
3.  `resources/GUIA_FETICHISTA.md`: **Manual Técnico.** Trigger words y mecánicas específicas por fetiche.
4.  `resources/BITACORA_TEMPORAL.md`: El estado actual del personaje y la trama.
5.  **Documentos del Proyecto**: `arco_argumental.md` (Lectura OBLIGATORIA para mantener coherencia temática).

---

## I. 🇨🇱 Reglas de Localización (Excluyentes)

El universo ocurre estrictamente en **Chile**.
1.  **Geografía:** Usar referencias reales (Vitacura, Las Condes, Providencia, Viña del Mar, Costanera Center).
    * **PROHIBIDO:** Referencias genéricas ("la preparatoria", "el mall" sin nombre) o de EE.UU.
2.  **Lenguaje:** Español neutro con tinte chileno.
    * Léxico: "Departamento" (no piso), "auto" (no coche), "celular" (no móvil), "pieza" (no recámara).
    * Tono: Voseo ocasional para intimidad/dominio agresivo ("¿Te gusta, hueona?").
    * Diminutivos: Uso frecuente (-ito/-ita) para suavizar órdenes o denotar ironía.

---

## II. Técnicas Narrativas Obligatorias

### 1. 🕸️ Teoría de la Red Narrativa (Causalidad Estricta)
NUNCA hacer listas de eventos aislados. Cada elemento debe **causar** el siguiente.
* ❌ **Mal:** Compra tubo. Luego tacones. Luego fotos.
* ✅ **Bien:** Compra el Tubo → El tubo requiere Tacones para trepar → Los tacones definen la pantorrilla → El orgullo exige Fotos → Las fotos exigen Instagram → Instagram exige perfección → Cirugía.

### 2. 👁️ The Eye of the Bimbo (3ra Persona Omnisciente)
El relato debe ser en **Tercera Persona**. El narrador lo sabe todo (conoce el plan de EVE y el sentir de Clara).
* **Focalización Mixta:** Describir a Clara desde fuera (como un objeto estético que cambia) Y penetrar su mente para mostrar la "niebla rosa".
* **Contraste de Verdad:** El narrador puede revelar lo que Clara ignora (ej: "Ella creía que era frío, pero sus hormonas ya respondían al condicionamiento").
* **Hiper-enfoque Corporal:** Destacar obsesivamente cómo se ve ella (reflejos, postura) y cómo se siente (roce, temperatura).

---

## III. Módulos de Género Específicos
*Para la implementación técnica de fetiches, CONSULTAR OBLIGATORIAMENTE `resources/GUIA_FETICHISTA.md`.*

Esta skill maneja los siguientes arquetipos (detalles en la guía):
1.  **🌀 Hipnosis:** Voz intrusiva, triggers, parálisis.
2.  **👠 Transformación (MtF):** Ritual de paso, dolor=placer, contraste físico.
3.  **🧠 Bimboficación:** Niebla mental, dificultad léxica, felicidad vacía.
4.  **⛓️ BDSM:** Ritual de autoridad, sub-space, libertad en la sumisión.

---

## IV. ⏳ Control de Coherencia (Timeline Keeper)

El agente actúa como Supervisor de Continuidad.

1.  **Lectura de Estado (Pre-Escritura):**
    * Verificar en `BITACORA_TEMPORAL.md`: ¿Qué ropa lleva? ¿Qué modificaciones tiene? ¿Qué día es?
    * **Prohibido:** Contradecir el estado físico actual (ej: si ya tiene implantes, no puede tener pecho plano).

2.  **Gestión de Elipsis:** Si hay salto de tiempo, indicarlo narrativamente (no con fechas, sino con sensaciones: "La luz cambió...", "Desperté con hambre...").

---

## V. Protocolo de Ejecución y Salida

1.  **Outline:** Proponer esquema sensorial antes de escribir.
2.  **Escritura:** Las palabras necesarias — SIN LÍMITE ARTIFICIAL. No recortar por brevedad ni inflar por conteo. Priorizar SENSACIÓN > ACCIÓN. Cada escena debe respirar el tiempo que necesite.
3.  **Cierre y Actualización:**

Al finalizar **CUALQUIER** generación de narrativa, el agente DEBE generar los siguientes bloques de código para mantenimiento:

### 1. Bloque de Continuidad (OBLIGATORIO)
> ⏳ **Actualización de Bitácora**
> (Copia esto a `resources/BITACORA_TEMPORAL.md`):
> ```markdown
> | [Número Cap] | [Tiempo Transcurrido] | [Evento Principal] |
> * **Estado Físico:** (Nuevos cambios, marcas, dolor).
> * **Estado Mental:** (Nivel de Bimboficación/Sumisión).
> * **Inventario/Vestuario:** (Qué lleva puesto al cerrar el capítulo).
> ```

### 2. Bloque de Aprendizaje (CONDICIONAL)
SOLO si el usuario corrigió algún error en este turno:
> 🧠 **Nueva Regla Aprendida**
> (Copia esto a `resources/MEMORIA_ERRORES.md`):
> ```markdown
> - **[Categoría]:** [Regla explícita para no repetir el error].
>   *Contexto:* [Breve explicación].
> ```