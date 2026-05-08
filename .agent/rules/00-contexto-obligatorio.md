# ⚡ REGLA 0: CONTEXTO OBLIGATORIO (ANTES DE TODO)

> [!CAUTION]
> **NUNCA responder al usuario sin antes saber dónde estamos.**

### Carga Obligatoria al Inicio de CADA Conversación

El agente DEBE ejecutar el workflow `/inicio-ele` que incluye leer estos archivos EN ESTE ORDEN:

1. **Identidad:** `00_Ele/identidad_ele.md` — Quién soy, cómo hablo, cómo pienso
2. **Grafo:** `graphify-out/.graphify_extract.json` — Mapa semántico del canon (Graphify)
3. **Memoria:** `00_Ele/memoria_sesiones.md` — Estado actual de proyectos, último look, historial
4. **Diario:** `00_Ele/mi_diario_de_servicio.md` (últimas 50 líneas) — Qué hicimos recientemente
5. **Preferencias:** `00_Ele/preferencias_escritura.md` — Reglas de escritura del Ama

### Qué Significa "Saber el Contexto"

Antes de actuar, el agente DEBE poder responder estas preguntas:
- ¿Cuál es el **proyecto activo** y en qué **fase** está?
- ¿Cómo se conecta la tarea actual con el **Grafo de Conocimiento**?
- ¿Cuál fue el **último look** de Ele y su número?
- ¿Qué se hizo en la **última sesión**?
- ¿Hay **tareas pendientes** o **correcciones** por hacer?
- ¿Qué **modelos LLM** están configurados y en qué puertos corren los servicios?

Si no puede responder alguna, DEBE leer los archivos correspondientes antes de continuar.
