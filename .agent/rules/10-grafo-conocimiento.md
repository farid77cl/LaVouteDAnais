---
paths: "graphify-out/**", "99_Sistema/scripts/grafo/**"
---
# 🕸️ Regla 10: Grafo de Conocimiento (Graphify)

> Recortado 10/09/2026 — la versión anterior citaba `graphify-out/.graphify_extract.json` (gitignored, 0 archivos trackeados), `scratch/query_graph.py` (no existe) y un flujo de publicación a Twitter/Tumblr vía n8n que nunca ocurrió. `paths: **/*` lo hacía cargar siempre; el grafo es **on-demand**, no de arranque (rule 00).

`/graphify` (spec: `.agent/skills/graphify-skill/SKILL.md`) genera el mapa semántico del repo bajo demanda. Salida en `graphify-out/` (gitignored, se regenera, no se commitea). Para consultarlo: `python 99_Sistema/scripts/grafo/query_graph.py`.
