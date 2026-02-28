# ⚙️ Sistema — Scripts y Automatización Interna

Directorio de scripts de automatización y archivos temporales del sistema La Voûte.

## Estructura

```
99_Sistema/
├── scripts/              # Scripts de automatización
│   └── visual/           # Generación visual
│       └── prompt_factory/  # Fábrica de prompts para imágenes
└── temp/                 # Archivos temporales (no commitear)
```

## Scripts Principales

| Script | Ubicación | Función |
|--------|-----------|---------|
| `update_galleries.py` | Raíz del repo | Actualiza GALERIA.md en cada carpeta de 05_Imagenes |
| `prompt_factory/` | `scripts/visual/` | Genera prompts de imagen a partir de bancos temáticos |
