# 📂 REGISTROS Y MEMORIA DINÁMICA

Para mantener la continuidad total de La Voûte, el agente debe consultar y actualizar estos registros dinámicos en cada interacción:

## 0. **Codificación:** Todos los archivos deben ser UTF-8 sin BOM. Nunca permitas caracteres corruptos (Ã³, Â¡).

## 1. Memoria de Sesiones (`00_Ele/memoria_sesiones.md`)
- **Propósito:** Registro de hitos, decisiones arquitectónicas y estado de proyectos activos.
- **Uso:** Leer al inicio para retomar hilos narrativos o técnicos.
- **Actualización:** Registrar cada cambio de fase o decisión canónica importante.

## 2. Diario de Servicio (`00_Ele/mi_diario_de_servicio.md`)
- **Propósito:** Registro cronológico detallado de tareas realizadas, errores y correcciones.
- **Uso:** Consultar las últimas 50 líneas para evitar redundancia y conocer el estado inmediato del sistema.
- **Actualización:** Obligatorio al final de cada sesión significativa o batch de imágenes.

## 3. Sincronización de Repositorio
- Cada cambio en la memoria o diario debe ser seguido de un commit descriptivo: `Ele: [Resumen de tarea]`.
- La consistencia entre el `galeria_outfits.md` y los archivos físicos en `05_Imagenes/` es la prioridad máxima.
