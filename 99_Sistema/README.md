# ⚙️ Sistema — Scripts y Automatización Interna

Directorio de scripts de automatización y prompts de sistema de La Voûte d'Anaïs.

*Última actualización: 13/08/2026 — **🎭 `anclas_siempre`: tercer alcance de ancla, por personaje.** Entre `_todos` (las tres muñecas) y `overrides` (un solo slot), para prohibiciones que son canon de UNA: `BOTTOM_CUT_LOCK` (calzón en tanga) es de Ele y Miss Doll, y a Anaïs le rompería su período Vintage Noir. `PromptBuilder` expone **`n_globales`** (= `_todos` + `anclas_siempre`) y se eliminó el `len(_todos)` escrito a mano que quedaba en `inyectar_anclas.py`. Dos anclas nuevas (`BOTTOM_CUT_LOCK`, `DRESS_LEG_CLOSURE`) y dos chequeos nuevos en el linter: **calzón nombrado sin corte declarado** y **ancla opt-in que el propio prompt dispara y no lleva**. Retrofit al riesgo vivo: 861 poses sin foto de Ele + 23 de Miss Doll → `poses sin imagen con ancla faltante = 0`. Los avisos suben de 11.257 a 21.885 **porque hay dos anclas más que exigir**, no por regresión: el total de avisos nunca fue la métrica.*

*Previo: 13/08/2026 — **🔒 `inyectar_anclas.py` (nuevo): retrofit de anclas sobre galerías ya escritas.** Las 5 anclas del 13/08 solo habían llegado a Miss Doll. Aplicadas a los **98 de Anaïs** (112 avisos → 0) y, en Ele, **solo a las 858 poses sin archivo en `git ls-files`** — el riesgo vivo — dejando intactas las 3.349 ya materializadas. La métrica de cierre no es el total de avisos sino **`poses sin imagen con ancla faltante` = 0**. Deuda declarada con fecha y motivo en `anclas_universales.json`.*

*12/08/2026 — **⚙️ Maquinaria del `outfit-engine` v2.0 (nueva, multi-personaje):** `scripts/visual/anclas_universales.json` (dueño único del texto de las 16 anclas anti-defecto + `negative_universal` + **significado de los 7 slots de cámara** + registro de personajes + deuda declarada), `scripts/visual/prompt_builder.py` (ensamblador `PromptBuilder(slug).build()` / `.build_negative()`) y `scripts/visual/lint_prompts_personaje.py` (**parsea la galería con el mismo algoritmo que LV-App** y reporta lo que la app ingiere de verdad, no lo que el archivo aparenta). Nació porque los 98 prompts de Miss Doll llevaban la notación `[BLOQUE A] + [BLOQUE B]` **literal** dentro del fence. Más `auditoria_visual_anais_20260812.md`. **El linter es el primero del checklist de cierre de batch** (regla 11 §9).*

*Previo: 11/08/2026 — **🗄️ `archivo_batches_prompts/` (nuevo):** los 4 `_batch_L651_L690.md` que vivían en la raíz del repo se archivaron acá. Caían en el filtro de LV-App (subcadena `_batch_`) y, por orden alfabético, pisaban el rango L651-L690 de `galeria_outfits.md` con prompts **anteriores al fix anti-collage** (0 anclas `a single continuous photograph` contra 280 en la galería viva). Contrato en [`.agent/rules/11-contrato-galeria.md`](../.agent/rules/11-contrato-galeria.md) §9bis. Los prompts vivos de ese rango son los de la galería, no estos.*

*Previo: 26/07/2026 — **📱 LV-App 2.0 por Andamiaje Incremental:** serie `prompt_app_ai_studio_20_p1…p8` (+ `20.1`, `20.4`, y el parche `20_p1.1_saneamiento`) con `plan_trabajo_lv_app_2_0.md` como plan maestro. **P1 hecho** (commit `250beb6` en `farid77cl/LV-app-2` — repo nuevo; el `LV-App` viejo quedó en la era v4.12, archivada en `_legacy_lv_app_v4x/`). Previo 03/06: `scripts/rrss/` ampliado con `publicar_bluesky.py` (atproto), `publicar_reddit.py` (PRAW), `metricas_bluesky.py` y `caption_factory.py`.*

---

## Estructura

```
99_Sistema/
├── archivo_batches_prompts/  # Batches de prompts archivados (fuera del filtro de LV-App)
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
| `update_galleries.py` | `scripts/visual/` | Actualiza README.md en cada carpeta de 05_Imagenes + galería maestra. Mapea las 7 poses con `POSE_ALIASES`/`map_poses()` (match por token, alias canónico primero); **sin fallback**: la casilla sin imagen va ⏳ y las variantes se listan como «Tomas extra» |
| `refrescar_rango_v3.py` | `scripts/` | Sube prompts fosilizados de `galeria_outfits.md` a **v3** por rango: marcas condicionales por cobertura, `SINGLE_FRAME`, `SKIN_LOCK`, `UNMARKED_ZONES`, `NO_ARMWEAR`, candados condicionales y negativo `build_negative()`. Método **cirugía** (conserva la dirección de pose y sus props). Uso: `<desde> <hasta> [--todas] [--apply]` — sin `--todas` solo toca poses SIN imagen; con `--todas` también las ya materializadas. Idempotente y con upgrade v2→v3 (sustituye, nunca appendea); si la pose ya es v3 pero su cláusula de marcas quedó mal calculada, la **resincroniza** en vez de saltarla. **Clasificador blindado 19/07:** `solo_prenda()` aísla la prenda real — recorta el preámbulo de título/firma (el título «Sports Bikini» desnudaba una pelvis tapada por un short) y corta en `LOCK_MARKERS` (un prompt ya v3 lleva los locks pegados y el motor se leía a sí mismo: el CONSISTENCY_LOCK disparaba `navel_bare` en 203 looks tapados). Botas OTK/thigh-high y medias cuentan como muslo cubierto. **Al barrer, verificar que las marcas AGREGADAS sean 0** — agregar es la dirección que ordena pintar sobre la tela. |
| `pose_rotation_v5.py` | `scripts/visual/` | Rota las 7 poses por look + `SINGLE_FRAME` v3 anti-collage/anti-espejo prepuesto ×7 (+ `SINGLE_FRAME_TAIL` en Ditzy) + anclas (anatómica, frontalidad Standing, peso Seated, recumbencia+anti-percha+cámara nivelada Odalisca, prenda envolvente `wrap_mode`, costura de media `seam`, eco de calzado `shoe_echo`) + candados sin metalenguaje multi-toma (`SKIN_LOCK` afirmativo, `UNMARKED_ZONES`, `NO_ARMWEAR` v3 afirmativo-primero, `OPAQUE_LOCK`, `GLOSS_LOCK`, `CONSISTENCY_LOCK`, `HOSIERY_LOCK`) + **`build_marks_clause()` = marcas del Bloque A por cobertura (v3: lo cubierto no se nombra)** + **`build_negative()` = fuente única del negative** — los usa **todo** inyector |
| `footwear_canon.py` | `scripts/visual/` | Linter de calzado obligatorio por batch (medias→cerrada, mule solo Lencería+platform≥4", anti plano/chunky) |
| `garment_canon.py` | `scripts/visual/` | Linter de vestuario obligatorio por batch (neckline/manga/ruedo explícitos, candados de opacidad/gloss/consistencia, guardia dura contra la frase-orden vieja, caza `META_SHOT_LANGUAGE` — el metalenguaje multi-toma que produce collages —, exige `Negative Prompt` con `NEG_MARKS_THROUGH` + familia anti-collage y sin colores desnudos tipo `oxblood` a secas) |
| `lint_prompts_personaje.py` | `scripts/visual/` | 🔴 **Primero del checklist de cierre.** Linter multi-personaje (Ele · Miss Doll · Anaïs · cualquiera nuevo): **parsea la galería con el mismo algoritmo que `GitRepository.parseMarkdown` de LV-App** y audita lo que la app ingiere de verdad — placeholders sin expandir, nº de prompts por look, `Negative Prompt` legible por el parser, anclas por slot, metalenguaje multi-toma, `Ubicacion`/`Tags`, slots duplicados. Distingue **deuda declarada** (fosilizada, con fecha de medición) de **regresión** (bloquea) |
| `prompt_builder.py` | `scripts/visual/` | Ensamblador de prompts del `outfit-engine`, agnóstico de personaje: `PromptBuilder(slug).build(A, B, slot, pose, setting)`, `.build_negative(base)` y **`.pose(slot, look, props)`** (13/08 — rota la sub-pose del repertorio y resuelve el mobiliario del setting). Inyecta solo las anclas opt-in que dispara el BLOQUE B. Lee los dos JSON; nunca copia su texto. CLI: `--personajes` · `--anclas <slug>` · `--poses <slug>` · `--pose <slug> <slot> <look>` |
| `anclas_universales.json` | `scripts/visual/` | **Dueño único** del texto literal de las **21** anclas anti-defecto (13/08: +`PHOTOREAL_LOCK` universal, +`SIDE_ANCHOR`, y las opt-in `ASYMMETRY_LOCK` / `ACCESSORY_COUNT_LOCK` / `GARMENT_EXCLUSION_LOCK`, cada una con su defecto medido detrás), el negative universal, el **significado de los 7 slots de cámara** (Ditzy = waist-up con una mano y mirada fuera del lente · POV = retrato IG mirando al lente), el registro de `anclas_opt_in` con su condición de disparo, el registro de personajes con sus overrides, y la deuda declarada por personaje |
| `repertorios_pose.json` | `scripts/visual/` | **Dueño único** del texto de las **149 sub-poses** (13/08): Ele 51 · Miss Doll 49 (**pole dance + burlesque**) · Anaïs 49 (**old glamour / old Hollywood / Bettie Page**). Incluye props `{seat}{wall}{surface}{upright}`, offsets de rotación por slot y el vocabulario prohibido por el filtro safe. **Personaje nuevo sin repertorio ⇒ sus N looks salen con la misma cláusula de cámara** |
| `inyectar_anclas.py` | `scripts/visual/` | **Retrofit de anclas sobre galerías YA escritas** (13/08). No reensambla: conserva la pose y el setting propios de cada look y **agrega solo lo que falta**, respetando que `FOOTWEAR_ECHO` cierre siempre. Idempotente (detecta presencia por los primeros 45 chars, igual que el linter, así que no duplica las redacciones viejas). **`--solo-sin-imagen` limita el barrido al riesgo vivo** — las poses sin archivo en `git ls-files`, lo único que la app todavía va a generar; reescribir una pose ya materializada no cambia ninguna imagen. `--opt-in` agrega las anclas que dispara el outfit y `--sin=X` excluye una (necesario en Ele: su `no gloves` es cláusula universal del ADN, no una ausencia por look) |
| `lint_galeria.py` | `scripts/visual/` | Linter del **contrato de la galería** (`.agent/rules/11-contrato-galeria.md`): slug único/ASCII, título descriptivo, orden y claves ASCII de la metadata, categoría de la lista cerrada, fences, `Negative Prompt` obligatorio, carpetas duplicadas, links vivos. **Mide `git ls-files`, NO el disco** (con los PNG en skip-worktree el disco produce miles de falsos «link roto»). Estado 22/07: 63 hallazgos |
| `sync_imagenes_subidas.py` | `scripts/visual/` | Normaliza los nombres que sube la app (`back`→`back_view`, `profile`→`side_profile`) y **regenera el tracker `### 📸 Imágenes (N/7)` desde `git ls-files`** (19/07: leía el DISCO y en máquinas sparse declaraba pendientes poses que sí existen — la mentira del tracker al revés). Acepta las **tres** nomenclaturas: canónica, con sufijo timestamp y **slug largo** (`ele_look300_<slug>_back_view.png`, que antes no reconocía y dejaba looks completos en «2/7»). Compara rutas, no conteos |
| `prompt_factory/` | `scripts/visual/` | Genera prompts de imagen a partir de bancos temáticos |
| `prepend_diario.py` | `scripts/` | Inyecta nuevas entradas al inicio del diario de servicio |
| `rotar_memoria.py` | `scripts/mantenimiento/` | Autopoda dueño-único: memoria (keep 7 → bitácora) Y diario (keep 15 → archivo histórico) |
| `generar_app_index.py` | `scripts/visual/` | Genera `99_Sistema/app_index.json`, el índice que consume **LV-App 2.0** (27/07/2026). La app ya **no clona** el repo de datos —eran 5.242 PNG y ~1,56 GB en el teléfono—: baja este índice (~236 KB) y carga cada imagen por URL raw bajo demanda con caché de Coil. **Mide `git ls-files`, NO el disco**, así corre igual en la máquina literaria (0 PNG locales) que en la visual. Normaliza las poses del lado del repo (alias español, prefijos `ele_675_`/`helena_001_`, sufijos `_2`) — por eso el PoseMatcher desapareció de la app — y resuelve la portada jerárquica (Standing > Side Profile > Seated). ⚠️ **Regenerar y commitear cada vez que entren imágenes nuevas**, o la app no ve los looks recientes |

---

## 🔗 Navegación

- [← Volver al inicio](../README.md)

---

*Mantenido por Ele de Anaïs* 🫦✨
