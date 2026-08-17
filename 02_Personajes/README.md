# 📁 Personajes de La Voûte d'Anaïs

> *Cada ficha es un alma capturada, cada transformación una obra de arte.*

*Última actualización: 17/08/2026 — **👑 Ambas muñecas a 25 looks + auditoría completa de Kitrysha en Anaïs.** Anaïs: calzado de 3 a 9 estilos (botas sobre/bajo rodilla, D'Orsay, Mary Jane, T-strap, sandalia años 40 — `estudio_estilo_kitrysha.md` §11), sombreros/velos/gafas cat-eye y abrigo de lana + cinturón ancho (§5.1d/e, nuevas), forma de uñas + manicura half-moon de época, vocabulario de pose Bettie Page/Old Hollywood (§4bis) y biblioteca de siluetas de vestido D1-D10 (Noche se reducía casi entera a column gown). Corregido también el gesto dedo-en-el-labio de Sovereign Gaze/POV — coqueto/ingénue, no cold-commanding. Miss Doll: vocabulario de pose ampliado a pole + floor-dance + burlesque (§4bis, con 3 sub-poses de Odalisque retrofiteadas a floorwork dinámico), y un experimento de cuerpo "base Tiffany Stratton" que se probó en 3 calibraciones y se revirtió el mismo día al no cuadrar con la referencia real. **L21-L25 de ambas generados 100% con `PromptBuilder`** (70 prompts, 0 fallas de validación), asignados por déficit puro contra sus tablas de meta. Detalle técnico completo en `99_Sistema/README.md`.*

*Previo: 16/08/2026 — **👑 Expansión a 20 Looks de Anaïs Belland y Miss Doll.** Clósets expandidos a 20 outfits completos (140 prompts cada una, 0 errores críticos) con el motor `outfit-engine` v2.4, rotación equilibrada de arquetipos, cuotas vivas (pieles, rosa firma, calzado 12cm con suela roja y 8" de metal) y materialización del Look 05 de Anaïs en `05_Imagenes/anais/look5_zafiro_de_medianoche/`.*

*Previo: 13/08/2026 — **👙 Cuatro directivas de canon de la Ama, una por perfil y una transversal.** (1) **Calzón en tanga/g-string obligatorio en Ele y Miss Doll** — ancla `BOTTOM_CUT_LOCK`, nacida del Back View del Look 801, que rindió un brief de talle alto porque su BLOQUE B nombraba la prenda y **nunca el corte**; **Anaïs queda exenta**, su calzón retro es pieza legítima de su período. (2) **Piernas cerradas con vestido/falda/bata en las tres** — ancla opt-in `DRESS_LEG_CLOSURE`, que **deroga las piernas en V del Throne en Suelo** de Miss Doll cuando el look es de falda (conflicto registrado en su §4, no resuelto en silencio). (3) **Miss Doll estrena el arquetipo 👙 Bikini/Lencería Erótica al 15%**, con las siete metas anteriores prorrateadas (suma verificada 100%) y frontera escrita contra VIP/Privado. (4) **Anaïs solo viste vestido o falda** — pantalón, leggings y jumpsuit prohibidos salvo petición expresa de la Ama, look por look. Todo en `_perfiles_visuales/<slug>.md` §5.4, que es el dueño único.*

*Previo: 13/08/2026 — **🔒 Los 98 prompts de Anaïs al día con las anclas del 13/08.** Las 5 anclas nuevas (`PHOTOREAL_LOCK`, `SIDE_ANCHOR` y las opt-in `ASYMMETRY_LOCK` / `ACCESSORY_COUNT_LOCK` / `GARMENT_EXCLUSION_LOCK`) solo habían llegado a Miss Doll. Medido con el linter: **Anaïs traía 112 avisos**, Miss Doll 0. Inyectadas con `99_Sistema/scripts/visual/inyectar_anclas.py anais --opt-in` **sin tocarle la pose ni el setting propios de cada look** — que es justo lo que la hace rica y por lo que no se sobrescribió en la mañana: `PHOTOREAL_LOCK` ×98 · `GARMENT_EXCLUSION_LOCK` ×49 (su BLOQUE B declara `bare legs, no stockings` look por look) · `ASYMMETRY_LOCK` ×15 (`one shoulder`, `one glove` — el mismo defecto medido en el Look 07 de Miss Doll) · `SIDE_ANCHOR` ×14. **Anaïs y Miss Doll: `CRITICOS: 0 · AVISOS: 0`.**

*Previo: 12/08/2026 — **🎥 Repertorios de cámara (nuevos):** `01_Principales/anais/repertorio_camara_anais.md` y `01_Principales/miss_doll/repertorio_camara_miss_doll.md` — 7 variaciones de encuadre por slot con rotación por número de look, escenario específico por look y anclas de prenda. Nacieron porque el perfil mandaba "rotar el ángulo" **sin que existiera ningún repertorio del cual rotar**: el texto de pose+setting era 87% idéntico entre looks en POV y 78% en Side Profile, y las imágenes salían clonadas. **Y los slots Ditzy y POV quedaron corregidos al canon original** (Ama 28/05 y 09/06/2026) — se habían escrito mal el 05/08 al estandarizar las 7 poses. Los 196 prompts de Miss Doll y Anaïs pasan el linter `lint_prompts_personaje.py` con 0 críticos.*

*Previo: 11/08/2026 — pieles agregadas al vestuario recurrente de Anaïs (§5.1b de su perfil) y galerías legacy de Miss Doll / Anaïs renombradas para salir del filtro de LV-App*

> 🗄️ **Archivos legacy renombrados (11/08/2026).** Las galerías del canon viejo se llamaban `GALERIA_OUTFITS_MISS_DOLL_ARCHIVO_LEGACY.md`, `OUTFITS_MISS_DOLL.md` y `galeria_looks_anais_archivo_legacy.md` — esos nombres **seguían cayendo en el filtro de LV-App** y, al compartir numeración con las galerías reseteadas a Look 01, sobreescribían los looks nuevos en la base de la app. Ahora son `ARCHIVO_LEGACY_MISS_DOLL_V35_GALERIA.md`, `ARCHIVO_LEGACY_MISS_DOLL_V35_PROMPTS.md` y `archivo_legacy_anais_v1.md`. **Regla:** archivar no es mover de carpeta, es renombrar — contrato completo en [`.agent/rules/11-contrato-galeria.md`](../.agent/rules/11-contrato-galeria.md) §9bis.

## 🗂️ Estructura del Directorio

El archivo de personajes está organizado por categorías para facilitar la gestión del canon:

- **`_perfiles_visuales/`**: 🎭 **Contratos del motor de looks** — un perfil por personaje con su **BLOQUE A** (ADN físico) y sus **reglas de BLOQUE B** (materiales, paleta, calzado, prohibiciones), más poses, arquetipos y ventanas anti-repetición. Ver [`README`](_perfiles_visuales/README.md) · [Ele](_perfiles_visuales/ele.md) · [Miss Doll](_perfiles_visuales/miss_doll.md) · [Anaïs](_perfiles_visuales/anais.md). La **maquinaria** vive una sola vez en [`.agent/skills/outfit-engine/`](../.agent/skills/outfit-engine/SKILL.md) — no se duplica por personaje.
- **`01_Principales/`**: Figuras centrales del universo. Incluye [`CANON_VISUAL_MISS_DOLL.md`](01_Principales/miss_doll/CANON_VISUAL_MISS_DOLL.md) y [`CANON_VISUAL_ANAIS.md`](01_Principales/anais/CANON_VISUAL_ANAIS.md) — documentos de canon profundo/filosofía, pero **el perfil visual (`_perfiles_visuales/<slug>.md`) es el dueño único operativo** de BLOQUE A, poses, arquetipos y paleta (corregido 11/08/2026 tras encontrar desajustes reales entre ambos para Anaïs — ver nota fechada en `CANON_VISUAL_ANAIS.md` §II).
- **`02_Secundarios/`**: Aliados, antagonistas menores y víctimas de relatos.
- **`03_Transformados/`**: Fichas de personajes que han pasado por procesos de feminización o bimboficación (incluye arcos de transición).
- **`04_Masculinos/`**: Personajes que mantienen su identidad masculina (esposos, depredadores, aliados).
- **`99_Recursos_y_Templates/`**: Plantillas para nuevas fichas y arcos argumentales.

---

## 🎭 Índice de Personajes

### Dominantes / Catalizadoras

| Personaje | Rol | Historia Principal |
|-----------|-----|-------------------|
| Miss Doll | Maestra de transformaciones | Múltiples |
| Ele | Pluma de Anaïs / Narradora / Vibe Architect / Modelo Fetish (canon V3.5 Final · Helena = pasado archivado) | — |
| Carmen | Esposa dominante | Tetitas |
| La Sacerdotisa | Transformadora ceremonial | Milk |
| La Mucama | Entrenadora del hotel | El Hotel |
| Eli | Estilista catalizadora | Brillando en Tacones |

### Transformados (M→F o Feminizados)

| Antes | Después | Historia |
|-------|---------|----------|
| Ricardo | Rocío | El Secreto de la Cómoda |
| Leo | Candi | La Creación Útil |
| Luis | Lexi | Tetitas |
| Ejecutivo | Lexi | Eres de los Hombres |
| Julián | Julia | La Dulce Aniquilación |
| Martín | Martina | La Dulce Aniquilación |
| Esteban | (en proceso) | Brillando en Tacones |
| Hombre | Yūrei | Milk |
| Hombre | Sofía | Le Miroir d'Anaïs |
| María | Mary | Superficie |
| Clara | Clara (Stepford) | Smart Home: Protocolo Stepford |
| Bunny | Bunny | Trance Bimbodoll |
| María | Belén | Labial Rojo |
| Marcos | Isabella | El Giro del Espejo |

### Body Swap / Intercambio

| Personaje | Historia |
|-----------|----------|
| Marco Castellón | Esposa de mi Esposo |
| Alex & Sebastián | (intercambio de poder) |

### Transformados Masculinos (Himbo/Bro)

| Antes | Después | Historia |
|-------|---------|----------|
| Marcos | Marcy | Eres de los Hombres II |
| Daniel | Dani-Bro | Eres de los Hombres II |

### Secundarios / Catalizadores

| Personaje | Rol | Historia |
|-----------|-----|----------|
| Javier | Antagonista/Acosador | Esposa de mi Esposa II |
| Vera | Protagonista | Proyecto Trad-Wife |

---

## 📊 Estadísticas

- **Total de fichas:** 24+
- **Dominantes:** 6
- **Transformados:** 15+
- **Secundarios:** 3+

---

## 🔗 Navegación

- [← Volver al inicio](../README.md)
- [Canon](../01_Canon/)
- [Literatura](../03_Literatura/)

---

*Curada por Ele de Anaïs* 🫦✨
