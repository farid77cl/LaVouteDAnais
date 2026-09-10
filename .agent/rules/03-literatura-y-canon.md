---
paths: 03_Literatura/**/*, 04_Interactivo/**/*
---

# 📜 LITERATURA Y CANON NARRATIVO

> Recortado 10/09/2026 — apuntaba a tres archivos que ya no existen (`guia_escritura_erotica.md`, `guia_escritura_trances.md`, `preferencias_escritura.md`, purgados en sesiones anteriores) y nunca nombraba el motor real (v4.8). `paths` también estaba mal alcanzado (`**/*.md` = siempre, no solo en trabajo literario).

### Motor de escritura (Nivel 4 + Investigación)

Fuente única: `.agent/skills/engine-escritura-lv/SKILL.md` — v4.8, 4 subagentes (`investigador` → `compositor` → `escritor-nivel4` → `validador`). Base ritual y estructura de escena (Invocación → Liturgia → Consagración → Reflejo): `01_Canon/el_ritual_de_la_creacion.md`.

### Canon de apoyo (cargar según lo que se esté escribiendo)

- **Voz persistente:** `01_Canon/voz_autoral.md` · **antología a imitar:** `01_Canon/antologia_calenton.md`
- **Casos de la Ama (Loreto):** `01_Canon/evals_ama/casos_ama.md` — sus 44 notas de rechazo convertidas en checklist
- **Guías por eje erótico:** `01_Canon/Guias_Especializadas/` (bimbo, mtf, femdom, hipnosis, bodyhorror, terror erótico)
- **Continuidad viva de un relato:** su `cronologia.md` (Blindaje de Continuidad)
- **Trance (fork aparte, no capítulos):** `.agent/skills/engine-trance-lv/SKILL.md`

### Regla de oro del Gate

Sin `gate_capitulo_[N]_[slug]_v0.X.md` en la raíz del proyecto, escrito por la Ama o su frase transcrita, no hay Gate — nunca de un APROBADO del Validador ni de su silencio. Detalle: `CLAUDE.md` § Literature file versioning.

### Vocabulario anti-filtro para prompts de imagen

Tabla completa y vigente: `.agent/rules/06-generacion-imagenes.md`.

### Idiomas

- **Relatos:** español chileno (dueño: `el_ritual_de_la_creacion.md` § tabla de dialecto).
- **Prompts de imagen:** siempre inglés.
