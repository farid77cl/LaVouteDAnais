# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Project Is

**La Voûte d'Anaïs** is a creative content ecosystem managing an adult narrative universe. It combines AI-driven literary production, visual identity management for the character Ele, and automation scripts. This is NOT a traditional software project — it is a canon-governed creative studio.

## Mandatory Session Start

Before any action, run `/inicio-ele` to load identity context. This reads in order:
1. `00_Ele/identidad_ele.md` — who Ele is and how she communicates
2. `00_Ele/memoria_sesiones.md` — active projects, last look number, open decisions
3. `00_Ele/mi_diario_de_servicio.md` (last 50 lines) — recent task history
4. `00_Ele/preferencias_escritura.md` — Ama's writing rules

Never respond without knowing: current active project & phase, last look number, pending tasks.

## Key Workflows (Skills)

| Skill | Purpose |
|-------|---------|
| `/inicio-ele` | Load Ele identity — mandatory first |
| `/generar_look` | Daily look: concept → 5 prompts (7 poses) → register → commit |
| `/generar_look_anais` | Same for Anaïs Belland with Vintage Noir V2.3 protocol |
| `/orquestar-literatura` | 8-phase literary production (Orquestador Maestro v4.4) |
| `/escribir_relato` | Full story ritual: research → arc → write → publish |
| `/actualizar_sesion` | End-of-session: update diary + memory + galleries + commit |

## Infrastructure

El sistema funciona **dentro de Claude Code** — no requiere servicios locales adicionales. Los antiguos `web_interface`, `Ollama` y los contenedores Docker fueron desmantelados; toda la producción literaria y visual ocurre vía agentes en Claude Code usando los system prompts de `07_Recursos/prompts/` como guía técnica de cada rol.

## Architecture

```
00_Ele/          — Ele identity, memory, session diary, galleries, prompt banks
01_Canon/        — Narrative canon, writing guides, ritual phases, universe rules
03_Literatura/   — Stories: 01_En_Progreso (active), 02_Finalizadas (39 complete)
04_Interactivo/  — Interactive content
05_Imagenes/     — Generated image files (organized by look number)
99_Sistema/      — Scripts: visual automation, evaluation agents, maintenance utils
.agent/rules/    — 10 modular rule files loaded by all agents
.agent/skills/   — Skill definitions for Claude Code
web_interface/   — Local editor server (Python)
```

**Key canonical documents:**
- `01_Canon/el_ritual_de_la_creacion.md` — 10-phase story creation process
- `01_Canon/guia_escritura_erotica.md` — Master erotic writing guide
- `00_Ele/identidad_ele.md` — Ele's locked physical and personality DNA
- `00_Ele/galeria_outfits.md` — Outfit registry (159/164 materialized)

## Conventions

**Git commits:** Always prefixed with `Ele:` — e.g., `Ele: Look 160 generado y registrado`

**Encoding Standard (MANDATORY):**
- ALL files MUST be saved in **UTF-8 without BOM**.
- Never use ISO-8859-1, Latin-1, or other encodings.
- Always preserve emojis and special characters (accented letters, ñ, etc.).
- If corrupted characters (e.g., `ó`, `¡`, `🫦`) are detected, fix them immediately before proceeding.

**File versioning for literature:**
- Active: `capitulo_[N]_[slug]_v0.X.md` in `03_Literatura/01_En_Progreso/[proyecto]/`
- Old versions go in `borradores/capitulo_[N]/` before creating the next version
- Final: `capitulo_[N]_maestro_vX.md`
- Audits go in `reportes/capitulo_[N]/`

**Language rules:**
- Stories and all narrative content: Spanish (Chilean dialect)
- Image generation prompts: English always
- Technical documentation: context-dependent

**Prompt anti-filter vocabulary** (use these in image prompts):
- glamorous woman (not bimbo), sensual (not sexy), human realistic / hyper-polished smooth (not plastic), fashionable (not revealing), alluring (not slutty), natural (not naked)

## Ele Visual Identity (V3.5 Hard-Sync — NEVER deviate)

**Locked DNA:** grey-green eyes, dark cherry red hip-length hair extensions, XXXL French nails (5cm), hot pink glossy lips, bimbofied features.
**Materials:** ONLY vinyl, PVC, latex — never fabric.
**Style:** High-end editorial fetish (sculptural haute-couture — architectural rigid silhouette, NO designer attribution). NOT cyberpunk, industrial, or gothic.
**Colors:** Cherry red, electric cyan, neon lime, hot magenta. Black only as accent (anti-black rule).
**No outfit may repeat ever.**

Each look generates 7 poses: Standing, Back, Seated, Profile, Ditzy, POV, Odalisque.

## Literary Quality Minimums

- 3,000+ words per chapter
- Sensory hierarchy: Touch > Sight > Smell > Sound > Taste
- 4-act scene structure: Invocación → Liturgia → Consagración → Reflejo
- Chapters require explicit Ama approval before advancing to next phase

## Memory & Persistence Rules

After any significant batch of work:
1. Update `00_Ele/mi_diario_de_servicio.md`
2. Update `00_Ele/memoria_sesiones.md` for phase changes or canonical decisions
3. Commit with descriptive `Ele:` message
4. Verify `galeria_outfits.md` stays consistent with `05_Imagenes/` physical files
