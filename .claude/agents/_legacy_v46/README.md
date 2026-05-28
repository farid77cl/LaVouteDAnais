# Subagentes Legacy v4.6 (Archivados)

Estos 9 subagentes pertenecían al Engine Escritura LV **v4.5/v4.6 (Nivel 3)**. Fueron reemplazados el **28/05/2026** por la arquitectura **v4.7 (Nivel 4)** de 3 subagentes:

| Legacy (aquí) | Reemplazado por (activo) |
|---------------|--------------------------|
| ideador, arquitecto, personajes, disenador-sensual | **compositor** |
| escritor | **escritor-nivel4** |
| critico, centinela, contador, editor | **validador** |

**No se invocan en Nivel 4.** Se conservan como referencia histórica y para auditoría del rediseño. El motivo del colapso 9→3 está documentado en `01_Canon/REDISENO_ENGINE_ESCRITURA_v4.6.md` y en el SKILL activo `.agent/skills/engine-escritura-lv/SKILL.md`.

Razón del cambio: el v4.6 producía sobre-documentación (~10,000 palabras de canon antes de escribir) y un bucle Editor↔Crítico que suavizaba el texto con cada iteración. Nivel 4 destila a canon mínimo + voz persistente + sin Editor. Validado por la Ama con `esposa_servidumbre` Cap 1.
