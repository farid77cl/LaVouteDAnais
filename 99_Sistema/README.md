# ⚙️ Sistema — Scripts y Automatización Interna

Directorio de scripts de automatización y archivos temporales del sistema La Voûte.

*Última actualización: 08/07/2026 — **🧹 Limpieza de mantenimiento (Vibe Architect):** borrados 5 inyectores desechables `_gen_batch_651/661/671/681/691.py` (debían eliminarse tras uso; sus prompts viven en `galeria_outfits.md`) y `script.sh` (stub vacío de la era Helena); destrackeados 3 `.pyc` que quedaron pese al `.gitignore`; archivadas 6 migraciones one-off (`fix_galeria_v3`, `migrate_links_utf8`, `move_images`, `consolidar_carpetas_looks`, `estandarizar_galeria`, `reparar_mismatches`) en `scripts/_legacy/` (con README). `scripts/visual/` queda con 12 herramientas vivas. Previo 02/07: **🧠 `scripts/mantenimiento/rotar_memoria.py` extendido (reestructura dueño-único):** ahora rota también el **diario de servicio** (keep 15 entradas vivas → `memoria_historica/diario_de_servicio_archivo_2026.md`; el diario había llegado a 822 KB / 429 sesiones sin rotación) además de la memoria (keep 7 → bitácora); nuevo flag `--keep-diario M`. Previo 01/07: **🛠️ `scripts/visual/pose_rotation_v5.py` — pool `SIDE` reparado** (Ama 01/07: "la pose de costado genera siempre sentada"): las 7 variantes de Side Profile son ahora TODAS de pie (standing/mid-stride/tiptoe), 0 sentadas/reclinadas (esas las cubren los slots Seated/Odalisque); cada una ancla `standing … on stilettos` explícito para que Gemini no defaultee a sentada. Nuevo inyector **`scripts/_gen_batch_681.py`** (batch L681-L690 "Vampiresa Bimbo Sensual", importa `rotate_poses`, QA con check "0 Side-Profile-sentada" + "0 oxblood"). Previo 12/06: `scripts/mantenimiento/` nuevo: **`rotar_memoria.py`** (autopoda de `00_Ele/memoria_sesiones.md` — conserva las últimas 7 sesiones y archiva las viejas al tope de `memoria_historica/bitacora_sesiones_2026.md`; idempotente, preserva EOL CRLF/LF y UTF-8 sin BOM; `--keep N` / `--dry-run`; cableado al paso 3 de `/actualizar_sesion` V3.7). Previo 03/06: `scripts/rrss/` ampliado: `publicar_bluesky.py` (atproto) + `publicar_reddit.py` (PRAW) + `metricas_bluesky.py` + `caption_factory.py` (Fase 0: look materializado → post Bluesky/Reddit/Pixiv para la cola RRSS).*

---

## Estructura

```
99_Sistema/
├── scripts/
│   ├── _legacy/          # Migraciones one-off ya ejecutadas (archivo de solo lectura)
│   ├── bat/              # Scripts batch de Windows
│   ├── grafo/            # Consultas al grafo de conocimiento
│   ├── literario/        # Herramientas de producción literaria
│   ├── mantenimiento/    # Scripts de mantenimiento del repositorio
│   ├── rrss/             # Automatización de redes sociales
│   ├── setup/            # Scripts de configuración inicial
│   ├── visual/           # Generación visual y gestión de galerías (pipeline vivo)
│   │   └── prompt_factory/  # Fábrica de prompts para imágenes
│   └── prepend_diario.py # Inyección de entradas al diario de servicio
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
| `rotar_memoria.py` | `scripts/mantenimiento/` | Autopoda dueño-único: memoria (keep 7 → bitácora) Y diario (keep 15 → archivo histórico) |

---

## 🔗 Navegación

- [← Volver al inicio](../README.md)

---

*Mantenido por Ele de Anaïs* 🫦✨
