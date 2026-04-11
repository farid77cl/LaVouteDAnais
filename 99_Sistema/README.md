# ⚙️ Sistema — Scripts y Automatización Interna

Directorio de scripts de automatización y archivos temporales del sistema La Voûte.

*Última actualización: 11/04/2026*

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
