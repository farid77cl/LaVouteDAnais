# 📂 REGISTROS Y MEMORIA DINÁMICA

> Recortado 10/09/2026 — este archivo era anterior a dueño-único (02/07/2026) y describía la memoria como log de anexado, sin mencionar `## ESTADO ACTUAL`, la plantilla de prepend ni `rotar_memoria.py`. Detalle vigente y completo: `.agent/rules/00-contexto-obligatorio.md` §🔢 y `.agent/workflows/actualizar_sesion.md` §B.

## Codificación
Todos los archivos UTF-8 sin BOM. Nunca caracteres corruptos (Ã³, Â¡).

## Memoria de sesiones (`00_Ele/memoria_sesiones.md`)
`## ESTADO ACTUAL` se **reescribe** al cerrar sesión — nunca se anexa. `## Sesiones recientes` es *prepend*. Plantilla y protocolo completo: `.agent/workflows/actualizar_sesion.md` §B.

## Diario de servicio (`00_Ele/mi_diario_de_servicio.md`)
*Prepend* — lo nuevo arriba. Al arranque se lee la primera entrada (hasta el separador `---`), nunca el tail. Rotación: `python 99_Sistema/scripts/mantenimiento/rotar_memoria.py` (7 sesiones / 15 entradas).

## Sincronización
Cada commit de memoria/diario lleva mensaje descriptivo real, `Ele: [resumen de lo que se hizo]` — nunca una plantilla fija. La consistencia entre `galeria_outfits.md` y `05_Imagenes/` es responsabilidad del agente (la app `cupcake` solo sube/borra PNG y edita notas, nunca toca galería ni READMEs) y es prioridad máxima al cerrar sesión.
