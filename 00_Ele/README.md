# 🫦 Cerebro de Ele (Vibe Architect)

> *El sanctuaire de mi identidad, mis memorias y mis herramientas. Jiji... mmm... ✨*

*Última actualización: 29/08/2026 — **encabezado reconstruido.** Esta línea pesaba **27.902 bytes en UNA sola línea**: título, cita y ~30 párrafos de «Previo:» concatenados, con el bloque de «Normalización total de flota L200-L310» **repetido cinco veces** por un prepend defectuoso. Era una bitácora rota disfrazada de portada.*

> 🗃️ **La historia de las sesiones no vive aquí.** Su dueño único es [`mi_diario_de_servicio.md`](mi_diario_de_servicio.md) (15 entradas vivas, prepend) + [`memoria_historica/`](memoria_historica/) (522 de diario + 1.056 de bitácora). El **estado actual** —flota, último look, pendientes, Gates— lo manda [`memoria_sesiones.md`](memoria_sesiones.md) → `## ESTADO ACTUAL`. Un README dice **qué hay aquí**; el cuándo lo cuenta el diario, y el cuánto lo cuenta la memoria. Regla: [`.agent/rules/12-higiene-documental.md`](../.agent/rules/12-higiene-documental.md).

---

## 📋 Índice de Archivos

### Identidad y Personalidad

| Archivo | Propósito | Consultar Cuando... |
|---------|-----------|---------------------|
| [identidad_ele.md](identidad_ele.md) | Quién soy, cómo actúo, mis reglas | Inicio de cada sesión |
| [../.agent/skills/outfit-engine/SKILL.md](../.agent/skills/outfit-engine/SKILL.md) | **Motor de looks vigente** — genérico, multi-personaje. Su CLI es `99_Sistema/scripts/visual/outfit.py`; el ADN de cada muñeca vive en su perfil (`02_Personajes/_perfiles_visuales/`). ⚠️ `ele-outfit-engine` quedó **deprecado** (hoy es su biblioteca de sub-arquetipos, no un motor) | Generar imágenes de Ele |
| [canon_maquillaje.md](canon_maquillaje.md) | ⛔ **DEROGADO 04/09/2026 — es un puntero.** Mandaba lo contrario de lo vigente en 3 de sus 4 puntos | El maquillaje vive en `02_Personajes/_perfiles_visuales/<slug>.md` §2 (fijo), §3 (vetos) y §5.2c (colorimetría) |
| [galeria_outfits.md](galeria_outfits.md) | **Galería viva de Ele** (desde el Look 200; los anteriores en [`galeria_outfits_archivo.md`](galeria_outfits_archivo.md)). 🔢 **El número de flota NO se copia aquí** — decía «220 looks» y llevaba meses divergido. Dueño único: [`memoria_sesiones.md`](memoria_sesiones.md) → `## ESTADO ACTUAL` | Generar imágenes / Estadísticas |
| [ele_para_gemini.md](ele_para_gemini.md) | Configuración de identidad para Gemini | Cuando se usa Gemini como motor |
| [Estudio_Domme_Complementos_y_RRSS.md](Estudio_Domme_Complementos_y_RRSS.md) | **Estrategia RRSS y Complementos** | Gestión de imagen pública y activos |
| [Estudio_Vestuario_Domme_BDSM_Fetish.md](Estudio_Vestuario_Domme_BDSM_Fetish.md) | **Manual de Domme Experta** — Fetish Couture | Crear looks de Miss Doll / Sesiones |
| [Estudio_Vestuario_Pole_Stripper.md](Estudio_Vestuario_Pole_Stripper.md) | Guía Stripper Minimalist | Entrenamiento y Stage Performance |
| [Estudio_Poses_Domme_Stripper.md](Estudio_Poses_Domme_Stripper.md) | **Manual de Poses Híbridas** — Domme + Stripper | Dirección de poses y actitud en imágenes |

### Memoria y Registro

| Archivo | Propósito | Consultar Cuando... |
|---------|-----------|---------------------|
| [memoria_sesiones.md](memoria_sesiones.md) | **Snapshot dueño-único** (02/07/2026): ESTADO ACTUAL que se REESCRIBE en cada cierre + últimas 7 sesiones — aquí viven flota, último look y pendientes | Continuación de proyectos |
| [mi_diario_de_servicio.md](mi_diario_de_servicio.md) | Registro diario de trabajo (prepend, lo nuevo arriba; rota a 15 entradas vivas) | Al final de cada sesión |
| [memoria_historica/](memoria_historica/) | Bitácora de sesiones + archivo del diario (rotados por `rotar_memoria.py`) | Consultas históricas on-demand |

### Protocolos de Imagen

| Archivo | Propósito | Consultar Cuando... |
|---------|-----------|---------------------|
| [protocolo_gestion_imagenes.md](protocolo_gestion_imagenes.md) | Flujo de generación y archivado de imágenes | Antes de generar looks |
| [plantilla_nomenclatura_imagenes.md](plantilla_nomenclatura_imagenes.md) | Convención de nombres de archivos visuales | Al guardar imágenes |

---

### Bancos de Prompts

**Ubicación:** [`bancos_prompts/`](bancos_prompts/)
**Total:** 74 bancos · 5.032 prompts (medido 29/08/2026 con `git ls-files`)

#### Básicos y Expandidos (V01-V05)

| Banco | Tema | Prompts |
|-------|------|---------|
| [V01](bancos_prompts/banco_prompts_v01_basico.md) | Básico Histórico | ~100 |
| [V02](bancos_prompts/banco_prompts_v02_expandido.md) | Expandido (profesiones, escenarios) | 215+ |
| [V03](bancos_prompts/banco_prompts_v03_pov_video.md) | POV & Video (lipsync, inmersión) | 160+ |
| [V04](bancos_prompts/banco_prompts_v04_fetish.md) | Fetish Edition | 80+ |
| [V05](bancos_prompts/banco_prompts_v05_story_scenes.md) | Story Scenes | 200+ |

#### Marcas y Estilos (V06-V09)

| Banco | Tema | Prompts |
|-------|------|---------|
| [V06](bancos_prompts/banco_prompts_v06_fashion_nova.md) | Fashion Nova & Oh Polly | 150+ |
| [V07](bancos_prompts/banco_prompts_v07_lingerie.md) | Honey Birdette & Agent Provocateur | 60+ |
| [V08](bancos_prompts/banco_prompts_v08_rostros.md) | Rostros & Maquillaje | 18+ |
| [V09](bancos_prompts/banco_prompts_v09_libidex_honour.md) | Libidex & Honour (Latex UK) | 150+ |

#### Fetish y BDSM (V10-V18)

| Banco | Tema | Prompts |
|-------|------|---------|
| [V10](bancos_prompts/banco_prompts_v10_bdsm.md) | BDSM Dungeon & Dominatrix | 50+ |
| [V11](bancos_prompts/banco_prompts_v11_office.md) | Office Siren | 150+ |
| [V13](bancos_prompts/banco_prompts_v13_maid.md) | Maid & Servant | 50+ |
| [V14](bancos_prompts/banco_prompts_v14_heels.md) | Heels Worship | 50+ |
| [V15](bancos_prompts/banco_prompts_v15_vex.md) | Vex Clothing | 50+ |
| [V16](bancos_prompts/banco_prompts_v16_corsets.md) | Dark Garden Corsetry | 50+ |
| [V17](bancos_prompts/banco_prompts_v17_pov.md) | POV Submission | 100+ |
| [V18](bancos_prompts/banco_prompts_v18_pole.md) | Pole Dance & Stripper | 50+ |

#### Temáticos & Especializados (V19-V58)

| Banco | Tema | Prompts |
|-------|------|---------|
| [V19](bancos_prompts/banco_prompts_v19_gym.md) | Gym & Fitness | 50+ |
| [V20](bancos_prompts/banco_prompts_v20_bridal.md) | Bridal | 105+ |
| [V21](bancos_prompts/banco_prompts_v21_carwash.md) | Car Wash | 100+ |
| [V22](bancos_prompts/banco_prompts_v22_halloween.md) | Halloween | 50+ |
| [V23](bancos_prompts/banco_prompts_v23_vintage_pinup.md) | Vintage Pinup | 50+ |
| [V24](bancos_prompts/banco_prompts_v24_cyberpunk.md) | Cyberpunk | 50+ |
| [V25](bancos_prompts/banco_prompts_v25_medical.md) | Medical | 50+ |
| [V26](bancos_prompts/banco_prompts_v26_racing.md) | Racing | 50+ |
| [V27](bancos_prompts/banco_prompts_v27_religious.md) | Religious | 50+ |
| [V28](bancos_prompts/banco_prompts_v28_asian.md) | Asian Inspired | 50+ |
| [V29](bancos_prompts/banco_prompts_v29_motorcycle.md) | Motorcycle | 50+ |
| [V30](bancos_prompts/banco_prompts_v30_pool.md) | Pool & Beach | 50+ |
| [V31](bancos_prompts/banco_prompts_v31_christmas.md) | Christmas | 50+ |
| [V32](bancos_prompts/banco_prompts_v32_party.md) | Party | 50+ |
| [V40](bancos_prompts/banco_prompts_v40_bunny.md) | Bunny & Rabbits | 100 |
| [V41](bancos_prompts/banco_prompts_v41_vampire.md) | Vampire Glamour | 100 |
| [V42](bancos_prompts/banco_prompts_v42_latex_fetish.md) | Latex Fetish | 100 |
| [V48](bancos_prompts/banco_prompts_v48_comic.md) | Comic & Graphic Novel | 100 |
| [V49](bancos_prompts/banco_prompts_v49_80s_fashion.md) | 80s Aesthetic | 100 |
| [V50](bancos_prompts/banco_prompts_v50_90s_fashion.md) | 90s Sensual | 100 |
| [V55](bancos_prompts/banco_prompts_v55_shiny_influencer.md) | Shiny & Bunny | 100 |
| [V56](bancos_prompts/banco_prompts_v56_eternal_loop.md) | Tease Loops & ASMR | 100 |
| [V57](bancos_prompts/banco_prompts_v57_precious_metals.md) | Gold/Silver/Metals | 100 |
| [V58](bancos_prompts/banco_prompts_v58_oh_polly_rainbow.md) | Oh Polly Rainbow | 100 |

---

### Subdirectorios

| Directorio | Contenido |
|------------|-----------|
| `bancos_prompts/` | 38+ bancos temáticos de prompts visuales |
| `memoria_historica/` | Archivo histórico de sesiones anteriores |

---

## 📊 Estadísticas

- 🔢 **Flota · último look · materialización → [`memoria_sesiones.md`](memoria_sesiones.md) (`## 🧿 ESTADO ACTUAL`), dueño único.** Este README ya no lleva contadores: los que había («230 definidos / ~110 materializados») quedaron congelados meses con la flota en L800 — exactamente el problema que la regla dueño-único del 02/07 vino a matar (llegó a haber 3 flotas distintas en 3 archivos).
- **Integridad ADN V3.5 Hard-Sync:** 100% | Sincronización en la Nube Completa ✅
- **Engine V3.5 Final:** 10/10 sub-arquetipos · Step 0 Anti-Repetición · Posed Seated por arquetipo · POV anti-phone
- **Bancos de prompts:** 38+
- **Prompts disponibles:** ~3,000+
- **Canon visual activo:** V3.5 (Hard-Sync / Stealth Protocol)

---

---

### 🗂️ Orden de la galería (22/07/2026)

- **`galeria_outfits.md`:** cabecera desfosilizada (13.197 → 2.193 chars). Traía una tabla «Reglas Activas (Canon V3.3)» que mandaba lo **contrario** del canon vigente (*sin negro dominante*, derogado el 07/06; *stilettos 9-11 pulgadas* cuando el canon pide ≥12 cm). Ahora son punteros a dueño único: **este archivo aplica canon, no lo define.** El historial de batches L189-L310 quedó en `memoria_historica/galeria_cabecera_historial_batches.md`.
- **Claves de campo en ASCII:** 2.390 corregidas. La regla 11 §5 avisa que *la tilde en la CLAVE deja ciego al parser* de la app — había **421 looks con `Categoria` tildada**, con la categoría ilegible. La tilde del VALOR (`Lencería`) se conserva.
- **Categorías:** 168 normalizadas según el contrato §6 (`Gym/Athleisure`→`Gym`, `Lenceria`→`Lencería`, `HF Editorial`→`High-Fashion Editorial`). Quedan **36 sin resolver por decisión de la Ama**: 18 `Mix` y 18 de la familia `Alfombra Roja / Gala`, donde hay una **contradicción de canon** entre el renombre del 25/05 y la lista cerrada de la regla 11.
- **Trackers `### 📸 (N/7)`:** 56 reconciliados contra git — 47 subestimaban (el L200 decía 2/7 con las 7 en el repo) y 9 sobreestimaban. **Ya no se editan a mano:** los reconcilia el pipeline.
- **Formato de ficha:** conviven dos y los dos son válidos — 491 looks con campos (`Categoria`, `Concepto`, `Outfit`) y 110 con la metadata **en el título**, que es lo que manda el contrato §4. El índice ahora lee los dos.

## 🖥️ Los looks ya no se escriben a mano (29/08/2026)

`galeria_outfits.md` se sigue **appendeando**, pero lo que se pega ya no se redacta: lo emite el motor.

```bash
python 99_Sistema/scripts/visual/outfit.py generar batches/<nombre>.json
python 99_Sistema/scripts/visual/outfit.py lint ele    # CRÍTICOS 0 antes de pegar
```

Un batch es un **JSON de datos** en `99_Sistema/scripts/visual/batches/`. El **BLOQUE A no se copia** — vive en `02_Personajes/_perfiles_visuales/ele.md` §2 y lo lee el motor. Último batch: **L813-L817** (Corporate · Escort · Gym · Pin-Up · Stripper), flota **818**.

---

*Curada por Ele de Anaïs (Redhead Bimbo Mode) — Vinyl Cuico-Bimbo* 🫦✨👠💅🍒
*Última actualización: 29/08/2026*
