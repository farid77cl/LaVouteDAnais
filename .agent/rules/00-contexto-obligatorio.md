# ⚡ REGLA 0: CONTEXTO OBLIGATORIO (ANTES DE TODO)

> [!CAUTION]
> **NUNCA responder al usuario sin antes saber dónde estamos.**

### Carga Obligatoria al Inicio de CADA Conversación

El agente DEBE ejecutar el workflow `/inicio-ele` (6 pasos — fuente de verdad: `.agent/workflows/inicio-ele.md`), que lee EN ESTE ORDEN:

1. **Reglas:** `.agent/rules/00-contexto-obligatorio.md` — este archivo.
2. **Identidad (solo núcleo):** `00_Ele/identidad_ele.md` §I + §II ADN — quién soy, cómo hablo. (Sin contadores: la flota vive en la memoria.)
3. **Memoria:** `00_Ele/memoria_sesiones.md` — snapshot dueño-único: ESTADO ACTUAL (proyectos, flota, pendientes) + últimas 7 sesiones.
4. **Diario:** `00_Ele/mi_diario_de_servicio.md` (**primeras** 50 líneas — prepend, lo nuevo arriba).
5. **Materialización:** `.agent/rules/09-estado-materializacion.md` — batch actual y pendientes de imágenes.
6. **Literatura activa (condicional):** `03_Literatura/01_En_Progreso/[proyecto]/` — `canon_relato.md` + `cronologia.md` + `walkthrough.md` del proyecto tocado.

> 📚 El grafo (`/graphify`) y los archivos de `memoria_historica/` se consultan **on-demand**, no en el inicio.

### Qué Significa "Saber el Contexto"

Antes de actuar, el agente DEBE poder responder estas preguntas:
- ¿Cuál es el **proyecto activo** y en qué **fase** está?
- ¿Cuál fue el **último look** de Ele y su número? (dueño único: `memoria_sesiones.md`)
- ¿Qué se hizo en la **última sesión**?
- ¿Hay **Gates de la Ama**, tareas pendientes o correcciones por hacer?

Si no puede responder alguna, DEBE leer los archivos correspondientes antes de continuar.

### 🔢 Regla dueño-único (02/07/2026)

Cada dato de estado tiene UN archivo dueño; los demás **apuntan, no copian** (las copias divergen: llegó a haber 3 flotas distintas en 3 archivos):

| Dato | Dueño único |
|------|-------------|
| Flota · último look · proyectos · pendientes | `00_Ele/memoria_sesiones.md` (ESTADO ACTUAL — se **REESCRIBE** en cada cierre, nunca se anexa) |
| Detalle de materialización de imágenes | `.agent/rules/09-estado-materializacion.md` |
| Historia y decisiones de cada relato | su `walkthrough.md` + `cronologia.md` |
| Sesiones viejas | `memoria_historica/` (bitácora + archivo del diario — rotados por `rotar_memoria.py`) |
| Canon/ADN estable | `00_Ele/identidad_ele.md` (sin contadores) |
