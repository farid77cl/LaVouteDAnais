# ⚙️ Sistema — Scripts y Automatización Interna

Directorio de scripts de automatización y prompts de sistema de La Voûte d'Anaïs.

*Última actualización: 18/08/2026 — **📱 Cinco prompts para LV-App y auditoría de stack.** Clonado el repo de la app **solo para diagnosticar** (el entregable es el prompt, nunca un commit ahí). `prompt_app_ai_studio_28` encuentra la causa de los 8 slugs que reportó la Ama: `PromptFilterScreen.kt:490` comparaba contra una lista hardcodeada con «Ditzy», el nombre real del slot 5 caía en `customPoses` y se dibujaba como chip fantasma que al usarse escribía `_ditzy.png` — corrige el alcance del `_27`, cuyo §3 contradecía el código real. `auditoria_stack_lv_app_20260818.md` mide el stack contra las versiones vigentes del día (Compose BOM con ~23 releases de atraso · cero librería de navegación · `androidx.media` deprecada en uso · `GITHUB_PAT` como texto en el APK sin ofuscar · **113 archivos basura trackeados**) y deja un plan de 7 pasos, uno por prompt. De ahí: `_29` (toolchain — BOM 2026.08.00, Kotlin 2.4.10, AGP 9.3, Gradle 9.5.1, KSP 2.3.10, compileSdk 37) · `_30` (purga del repo y del catálogo) · `_31` (**la app bajaba 33,54 MB de markdown en cada sync** con cache-buster `?v=currentTimeMillis`, teniendo ya en mano los SHA que lo resolvían) · `_32` (el botón de sync quedó en `force = true` y el reporte se descarta con `startsWith("✗")`: se instrumenta con archivos/bytes/segundos para que la Ama verifique en pantalla). **Ningún prompt trajo log de build: la compilación sigue sin verificarse.***

*18/08/2026 — **👗 Chequeo 12: rotación de arquitectura de prenda.** La Ama preguntó por qué el último batch de Miss Doll salió en puros bikini y bodysuit; medido, iban **11 looks seguidos (L15-L25) sin vestido, falda ni pantalón** con el motor sano — 8 arquetipos en meta y 50 builds con 0 fallas. La causa era de diseño: el §6 del perfil gobierna el **escenario** y nadie gobernaba la **prenda**, y la ventana anti-repetición estaba alcanzada **por arquetipo**, así que con 8 arquetipos rotando **no se disparó ni una vez en 25 looks**. Nuevo en `anclas_universales.json`: **`arquitecturas_de_prenda`** (taxonomía M1-M10 genérica) + **`personajes.miss_doll.rotacion_prenda`** (ventana global ≥3 · cuota de silueta cubierta 1 de cada 4 · `desde_look` para no retrofitear el roster viejo). El chequeo 12 clasifica **solo el BLOQUE B** — sobre el prompt ensamblado sería el clasificador leyéndose a sí mismo, porque las anclas nombran «bikini», «bodysuit», «dress» y «skirt» — y borra las ausencias declaradas antes de medir (un `no corset` clasificaba el look como corsetería). Además, `--verbose` ahora imprime **todos** los avisos: topaba en 60 y remataba aconsejando una bandera que ya estaba puesta.*

*Previo: 17/08/2026 — **🔒 Blindaje del outfit-engine: prefijo por arquetipo verificado en código + orientación automática.** Diagnosticado el bug real detrás de la queja de la Ama sobre Anaïs (el batch L15-L20 copió el prefijo cinematográfico de Ejecutivo a los 6 looks nuevos sin variar por arquetipo — Boudoir perdió su luz cálida entera): la tabla ya existía en `dna_v2_3.md`, pero nadie la releía al copiar un bloque. Corregido en dos capas — `anclas_universales.json` gana `personajes.anais.prefijos_arquetipo` (copia máquina-legible) y `PromptBuilder.prefijo_arquetipo()` la resuelve en código; **`lint_prompts_personaje.py` gana el chequeo 11**, que audita cada look contra su `**Arquetipo:**` declarado — un prefijo que no corresponde es CRÍTICO. Además: anclas nuevas `ASPECT_VERTICAL`/`ASPECT_HORIZONTAL` (la proporción de imagen ya sale escrita en el prompt, dejó de elegirse a mano en la app) y `PromptBuilder.orientacion_odalisque()` (el Odalisque de Miss Doll alterna vertical/horizontal por número de look — el único slot que no va fijo, porque su pose es sentada, no reclinada). Verificado con un mismatch simulado en memoria: el chequeo 11 lo detecta.*

*Previo: 13/08/2026 — **🎭 `anclas_siempre`: tercer alcance de ancla, por personaje.** Entre `_todos` (las tres muñecas) y `overrides` (un solo slot), para prohibiciones que son canon de UNA: `BOTTOM_CUT_LOCK` (calzón en tanga) es de Ele y Miss Doll, y a Anaïs le rompería su período Vintage Noir. `PromptBuilder` expone **`n_globales`** (= `_todos` + `anclas_siempre`) y se eliminó el `len(_todos)` escrito a mano que quedaba en `inyectar_anclas.py`. Dos anclas nuevas (`BOTTOM_CUT_LOCK`, `DRESS_LEG_CLOSURE`) y dos chequeos nuevos en el linter: **calzón nombrado sin corte declarado** y **ancla opt-in que el propio prompt dispara y no lleva**. Retrofit al riesgo vivo: 861 poses sin foto de Ele + 23 de Miss Doll → `poses sin imagen con ancla faltante = 0`. Los avisos suben de 11.257 a 21.885 **porque hay dos anclas más que exigir**, no por regresión: el total de avisos nunca fue la métrica.*

*Previo: 13/08/2026 — **🔒 `inyectar_anclas.py` (nuevo): retrofit de anclas sobre galerías ya escritas.** Las 5 anclas del 13/08 solo habían llegado a Miss Doll. Aplicadas a los **98 de Anaïs** (112 avisos → 0) y, en Ele, **solo a las 858 poses sin archivo en `git ls-files`** — el riesgo vivo — dejando intactas las 3.349 ya materializadas. La métrica de cierre no es el total de avisos sino **`poses sin imagen con ancla faltante` = 0**. Deuda declarada con fecha y motivo en `anclas_universales.json`.*

*12/08/2026 — **⚙️ Maquinaria del `outfit-engine` v2.0 (nueva, multi-personaje):** `scripts/visual/anclas_universales.json` (dueño único del texto de las 16 anclas anti-defecto + `negative_universal` + **significado de los 7 slots de cámara** + registro de personajes + deuda declarada), `scripts/visual/prompt_builder.py` (ensamblador `PromptBuilder(slug).build()` / `.build_negative()`) y `scripts/visual/lint_prompts_personaje.py` (**parsea la galería con el mismo algoritmo que LV-App** y reporta lo que la app ingiere de verdad, no lo que el archivo aparenta). Nació porque los 98 prompts de Miss Doll llevaban la notación `[BLOQUE A] + [BLOQUE B]` **literal** dentro del fence. Más `auditoria_visual_anais_20260812.md`. **El linter es el primero del checklist de cierre de batch** (regla 11 §9).*

*Previo: 11/08/2026 — **🗄️ `archivo_batches_prompts/` (nuevo):** los 4 `_batch_L651_L690.md` que vivían en la raíz del repo se archivaron acá. Caían en el filtro de LV-App (subcadena `_batch_`) y, por orden alfabético, pisaban el rango L651-L690 de `galeria_outfits.md` con prompts **anteriores al fix anti-collage** (0 anclas `a single continuous photograph` contra 280 en la galería viva). Contrato en [`.agent/rules/11-contrato-galeria.md`](../.agent/rules/11-contrato-galeria.md) §9bis. Los prompts vivos de ese rango son los de la galería, no estos.*

*Previo: 26/07/2026 — **📱 LV-App 2.0 por Andamiaje Incremental:** serie `prompt_app_ai_studio_20_p1…p8` (+ `20.1`, `20.4`, y el parche `20_p1.1_saneamiento`) con `plan_trabajo_lv_app_2_0.md` como plan maestro. **P1 hecho** (commit `250beb6` en `farid77cl/LV-app-2` — repo nuevo; el `LV-App` viejo quedó en la era v4.12, archivada en `_legacy_lv_app_v4x/`). Previo 03/06: `scripts/rrss/` ampliado con `publicar_bluesky.py` (atproto), `publicar_reddit.py` (PRAW), `metricas_bluesky.py` y `caption_factory.py`.*

---

## Estructura

```
99_Sistema/
├── archivo_batches_prompts/  # Batches de prompts archivados (fuera del filtro de LV-App)
├── _legacy_lv_app_v4x/       # 🗄️ Prompts AI Studio #1-#19 (era v4.x) — solo lectura
├── _legacy_prompts_ai_studio/# 🗄️ Prompts AI Studio #20-#33 — flujo DEROGADO 28/08/2026
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
├── logs/                 # Log del outfit-engine (outfit_engine.jsonl)
├── temp/                 # Archivos temporales (no commitear)
├── auditoria_*.md        # Auditorías fechadas (evidencia, no se borran)
└── app_index.json        # Índice que consume LV-App (regenerar con generar_app_index.py)
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
| `lint_galeria.py` | `scripts/visual/` | Linter del **contrato de la galería** (`.agent/rules/11-contrato-galeria.md`): slug único/ASCII, título descriptivo, orden y claves ASCII de la metadata, categoría de la lista cerrada, fences, `Negative Prompt` obligatorio, carpetas duplicadas, links vivos. **Mide `git ls-files`, NO el disco** (con los PNG en skip-worktree el disco produce miles de falsos «link roto»). **Estado 17/08: 29 hallazgos en 26 looks** (era 65 en 60) — C6 quedó en **0** tras verificar la *dirección* del error: la lista cerrada estaba vieja, no los looks (entró «Alfombra Roja / Gala» como 11ª categoría) y «Mix» era la meta cromática colada en el campo de 18 looks. Lo que queda es C1/C2/C3 = renombrar carpetas de imágenes, **visible para la app**, pendiente de decisión de la Ama |
| `sync_tracker_galeria_personaje.py` | `scripts/visual/` | **Sincroniza el tracker `### 📸 Imágenes (N/7)` de Anaïs y Miss Doll contra `git ls-files`** (17/08). Existe porque `update_galleries.py` **no** toca ese tracker: es manual y por eso reincide (13/08: 0/7 en 13 de 14 looks con 52 imágenes reales; 17/08: **33 looks** desfasados con L15-L25 en «0/7» y 60 imágenes en el índice). Cuenta **`.png` y `.jpg`** (varias poses viejas de Anaïs son jpg — contar solo png da un falso 0/7 en looks completos), **preserva las anotaciones humanas dentro de las celdas** (⚠️ de auditoría) y **no pisa los encabezados con nota propia**: los reporta. Orden del pipeline: `sync_imagenes_subidas.py` → **este** → `update_galleries.py` |
| `sync_imagenes_subidas.py` | `scripts/visual/` | Normaliza los nombres que sube la app (`back`→`back_view`, `profile`→`side_profile`) y **regenera el tracker `### 📸 Imágenes (N/7)` desde `git ls-files`** (19/07: leía el DISCO y en máquinas sparse declaraba pendientes poses que sí existen — la mentira del tracker al revés). Acepta las **tres** nomenclaturas: canónica, con sufijo timestamp y **slug largo** (`ele_look300_<slug>_back_view.png`, que antes no reconocía y dejaba looks completos en «2/7»). Compara rutas, no conteos |
| `prompt_factory/` | `scripts/visual/` | Genera prompts de imagen a partir de bancos temáticos |
| `prepend_diario.py` | `scripts/` | Inyecta nuevas entradas al inicio del diario de servicio |
| `rotar_memoria.py` | `scripts/mantenimiento/` | Autopoda dueño-único: memoria (keep 7 → bitácora) Y diario (keep 15 → archivo histórico) |
| `generar_app_index.py` | `scripts/visual/` | Genera `99_Sistema/app_index.json`, el índice que consume **LV-App 2.0** (27/07/2026). La app ya **no clona** el repo de datos —eran 5.242 PNG y ~1,56 GB en el teléfono—: baja este índice (~236 KB) y carga cada imagen por URL raw bajo demanda con caché de Coil. **Mide `git ls-files`, NO el disco**, así corre igual en la máquina literaria (0 PNG locales) que en la visual. Normaliza las poses del lado del repo (alias español, prefijos `ele_675_`/`helena_001_`, sufijos `_2`) — por eso el PoseMatcher desapareció de la app — y resuelve la portada jerárquica (Standing > Side Profile > Seated). ⚠️ **Regenerar y commitear cada vez que entren imágenes nuevas**, o la app no ve los looks recientes |

| `auditar_canon_flota.py` | `scripts/visual/` | **Corre el canon de calzado y vestuario sobre la FLOTA REAL** (29/08/2026). Nació de medir que `footwear_canon.py` y `garment_canon.py` **no abren un solo archivo**: son la regla más su self-test con seis casos escritos a mano, y nunca miraron una galería — por eso el mule sin plataforma del Look 812 llegó a generarse mientras `audit_footwear` detectaba esa violación exacta en su propio test. Este script no reimplementa el canon: parsea las tres galerías y le entrega los looks reales a esas mismas funciones. Extrae el **segmento de outfit acotado** (entre el cierre del BLOQUE A y la primera ancla), nunca el prompt completo — las anclas nombran `flats`, `thong`, `bodysuit`, y el auditor leería su propia defensa como si fuera la prenda. Un look que no se puede acotar se marca **NO AUDITABLE**. Acepta `[slug]`, `--solo-sin-imagen`, `--detalle` |
| `prompt_builder.py --adn` | `scripts/visual/` | **Verificador de dueño único del BLOQUE A** (29/08/2026). Cruza el ADN del perfil visual contra cada script de batch y contra la galería. Antes de esto el ADN no tenía dueño mecánico: cada batch lo copiaba a mano, Miss Doll lo tenía con una nota en castellano incrustada y **Anaïs no tenía token literal en su perfil**. Ahora vive en un fence marcado `<!-- ADN:BLOQUE_A -->` que **lee el motor** (`build()` acepta `bloque_a=None`) |

> ⚠️ **`footwear_canon.py` y `garment_canon.py` son self-tests, no auditorías de flota.** Corren sobre fixtures inventados y su `Self-check: LIMPIO` no dice nada sobre las galerías. Siguen valiendo como tests unitarios de las reglas — pero para medir la flota es `auditar_canon_flota.py`.

---

## 🔗 Navegación

- [← Volver al inicio](../README.md)

---

## 🖥️ `outfit.py` — la puerta única del outfit-engine (29/08/2026)

| Comando | Qué hace |
|---|---|
| `generar <batch.json>` | Emite un batch de looks **desde datos**. Nunca más un script por batch |
| `adn` | Dueño único del BLOQUE A: perfil vs. batches vs. galería vs. **documentación** |
| `lint [slug]` | Parsea las galerías **como LV-App** |
| `auditar [--solo-sin-imagen]` | Canon de calzado y vestuario **sobre la flota real** |
| `anclas <slug>` | Inyecta anclas faltantes en una galería ya escrita |
| `modularidad` | 0 personajes en la lógica · campos propios · sub-poses únicas |
| `test` | Self-checks de las reglas **+ 32 pruebas del motor** (`test_engine.py`) |

Un batch vive en `scripts/visual/batches/<nombre>.json`. **El BLOQUE A no va ahí:** lo lee el motor del perfil visual, que es su dueño único.

---

*Mantenido por Ele de Anaïs* 🫦✨
*Última actualización: 29/08/2026*
