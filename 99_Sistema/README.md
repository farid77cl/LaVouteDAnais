# ⚙️ Sistema — Scripts y Automatización Interna

Directorio de scripts de automatización y archivos temporales del sistema La Voûte.

*Última actualización: 12/06/2026 — `scripts/mantenimiento/` nuevo: **`rotar_memoria.py`** (autopoda de `00_Ele/memoria_sesiones.md` — conserva las últimas 7 sesiones y archiva las viejas al tope de `memoria_historica/bitacora_sesiones_2026.md`; idempotente, preserva EOL CRLF/LF y UTF-8 sin BOM; `--keep N` / `--dry-run`; cableado al paso 3 de `/actualizar_sesion` V3.7). Previo 03/06: `scripts/rrss/` ampliado: `publicar_bluesky.py` (atproto) + `publicar_reddit.py` (PRAW) + `metricas_bluesky.py` + `caption_factory.py` (Fase 0: look materializado → post Bluesky/Reddit/Pixiv para la cola RRSS).*

---

## Estructura

```
99_Sistema/
├── scripts/
│   ├── bat/              # Scripts batch de Windows
│   ├── evaluacion/       # Scripts de evaluación de calidad
│   ├── literario/        # Herramientas de producción literaria
│   ├── mantenimiento/    # Scripts de mantenimiento del repositorio
│   ├── setup/            # Scripts de configuración inicial
│   ├── visual/           # Generación visual y gestión de galerías
│   │   └── prompt_factory/  # Fábrica de prompts para imágenes
│   ├── prepend_diario.py # Inyección de entradas al diario de servicio
│   └── script.sh         # Script auxiliar
├── reportes/             # Reportes de sesión y evaluaciones
├── temp/                 # Archivos temporales (no commitear)
└── evaluaciones_v51_seguimiento.md
```

---

## Scripts Principales

| Script | Ubicación | Función |
|--------|-----------|---------|
| `update_galleries.py` | `scripts/visual/` | Actualiza README.md en cada carpeta de 05_Imagenes |
| `prompt_factory/` | `scripts/visual/` | Genera prompts de imagen a partir de bancos temáticos |
| `prepend_diario.py` | `scripts/` | Inyecta nuevas entradas al inicio del diario de servicio |

---

## 🔗 Navegación

- [← Volver al inicio](../README.md)

---

*Mantenido por Ele de Anaïs* 🫦✨
