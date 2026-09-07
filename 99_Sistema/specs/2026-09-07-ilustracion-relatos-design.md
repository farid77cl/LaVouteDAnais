# Diseño — Sistema de Ilustración de Relatos (estilo cómic pop-art) para Tumblr

| Campo | Valor |
|---|---|
| **Fecha** | 07/09/2026 |
| **Autor** | Ele de Anaïs (Vibe Architect) |
| **Origen** | Orden de la Ama, sesión 07/09/2026 |
| **Estado** | Diseño aprobado en conversación — pendiente de plan de implementación |
| **Destino documental** | *working* (regla 12) |
| **🪦 Fecha de muerte declarada** | Muere cuando `.agent/skills/ilustrar-relato/SKILL.md` esté escrito y aprobado por la Ama. En ese momento este archivo se borra: el SKILL pasa a ser el dueño único del protocolo, y la evidencia medida de §3 vive en las reglas 11 y 12, no acá. |

---

## 1. Qué se está construyendo, en una frase

Un sistema para que cada relato publicado en Tumblr lleve **una portada de relato y dos imágenes por capítulo**, todas en un mismo estilo de cómic pop-art, generadas por la Ama en Gemini a partir de prompts que escribe el agente.

---

## 2. Decisiones de la Ama (literales, 07/09/2026)

Estas ocho decisiones son la fuente; el diseño de abajo no es más que su consecuencia.

| # | Decisión | Literal / opción elegida |
|---|---|---|
| D1 | Canal y volumen | *"estoy pensando en usar la pp de tumblr para publicar los relatos, pero quiero agregarles imagenes"* · **portada + 2 por capítulo** |
| D2 | Quién sale | **Personaje del relato, con biblia visual propia** (bloque bloqueado, igual que las tres muñecas) |
| D3 | Temperatura de la imagen | **Sugerente vestida (PG-13)** — látex, tacones, escote, collar, cara de trance; sin acto, sin desnudo |
| D4 | Texto dentro de la imagen | **Ninguna con texto.** El título lo pone Tumblr en el post |
| D5 | Alcance | *"a medida que se publiquen, la frecuencia esta por definir"* — nada de retrofit masivo del catálogo |
| D6 | Generación | *"no me interesa que lo vea la app, esas imagenes tu genera el prompt yo te paso de vuelta las imagenes"* |
| D7 | Portada vs. internas | *"si los relatos van por cap, se mantiene la portada, cambian las imagenes dentro"* |
| D8 | Arquitectura | **Opción A** (skill aparte, post-Gate) **+ el cliffhanger de C** (la imagen `b` de cada capítulo es su beat de cierre) |

---

## 3. Contexto medido (07/09/2026)

Todo lo de esta sección se midió antes de diseñar. Es la evidencia, no la hipótesis.

### 3.1 Lo que ya existe y se reutiliza

| Activo | Medida | Ruta |
|---|---|---|
| Formato Tumblr por relato | **38 archivos** `*_tumblr.md` — pero ⚠️ ver 3.2bis: **32 son teasers, no adaptaciones** | `03_Literatura/02_Finalizadas/*/_publicacion/` |
| Plantilla oficial | Ya contempla **2 slots de imagen** (`URL_IMAGEN_1` portada, `URL_IMAGEN_2` intermedia) | `07_Recursos/plantilla_tumblr_md.md` |
| Portadas de relato | **18 PNG** | `05_Imagenes/portadas/` |
| Imágenes internas de relato | **5 relatos** con carpeta propia | `05_Imagenes/historias/<slug>/` |
| Precedente de biblia visual | Prompt canon por personaje + checklist + rating PG-13 declarado | `05_Imagenes/comics/nexum_human_repurposing/guion_comic.md` |
| Biblia de Renée, ya escrita y parqueada | §10 con el espacio visual **verificado contra los tres BLOQUE A vigentes** | `02_Personajes/01_Principales/ficha_renee.md` |
| Forma de URL de imagen en Markdown | `https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/<ruta>` — medido: **1.085 README** la usan (1.098 archivos en total) | `05_Imagenes/**/README.md` |

**Conclusión de 3.1:** la estructura de carpetas ya la construyó la Ama. Lo que nunca tuvo es **dueño y contrato** — el mismo defecto que tenían las galerías antes de la regla 11.

### 3.2 Lo que está roto en lo que existe

- **Dos nomenclaturas compitiendo en `05_Imagenes/portadas/`:** `portada_<slug>.png` (**13 archivos**) y `<slug>_cover.png` (**3 archivos**).
- **Relatos con portada duplicada:** «Brillando en Tacones» tiene 2 (`brillando_en_tacones_cover.png` + `portada_brillando_en_tacones.png`); «Smart Home Stepford» tiene **3** (`smart_home_stepford_cover.png`, `smart_home_stepford_cover_v1.png`, `portada_smart_home_stepford.png`).
- **Sin contrato de nombres en `historias/`:** conviven `imagen1_eli.png`, `roxy_cougar_hunt.jpg` y `clara_bimbo_pose_3_seated_vinyl_leopard_1773862485028.png`.
- **El estilo pop-art no tiene dueño.** `00_Ele/bancos_prompts/banco_prompts_v48_comic.md` (100 prompts) es **era Helena** — pelo negro azabache, gótico, Sin City, Junji Ito; no contiene el halftone rosa sesentero. Las dos guías de cómic están en `01_Canon/Guias_Especializadas/legacy/`.

### 3.2bis 🩹 Corrección a 3.1 — la adaptación a Tumblr NO está hecha (medido 07/09/2026)

La primera versión de este spec afirmó que los archivos Tumblr estaban listos *"solo 1 con placeholders sin llenar"*. **Es falso.** El dato salió de un `grep` de tres frases concretas; una frase que no aparece no prueba que el archivo esté completo. Medición correcta, contando palabras de cada archivo contra `HEAD`:

| Estado | Cuántos |
|---|---|
| **Teasers de <450 palabras** — gancho + primeras escenas + *"[CONTENIDO COMPLETO DISPONIBLE EN EL ARCHIVO MAESTRO]"* | **32 de 38** |
| Adaptaciones reales (>1.600 palabras) | **6** — `trance_bimbodoll_ii` (8.374), `gloss_trance_miss_doll` (2.088), `brillando_en_tacones_I` (2.054), `tetitas` (1.810), `la_creacion_util` (1.809), `esposa_de_mi_esposa_II` (1.632) |

Caso testigo: «El Collar de Nancy» son **~8.500 palabras** de relato y su archivo Tumblr tiene **425**.

**Consecuencia para este diseño:** las imágenes se cablean a un archivo Tumblr que en 32 de 38 casos **todavía no existe como adaptación**. Este spec cubre la ilustración; la adaptación del texto es un subproyecto hermano y **es prerrequisito suyo**.

### 3.3 Restricciones duras del entorno

| # | Restricción | Evidencia |
|---|---|---|
| R1 | **LV-App queda fuera por decisión de la Ama (D6).** De paso, tampoco podría entrar: la app descarta toda ruta que contenga `03_literatura` | `.agent/rules/11-contrato-galeria.md` §9bis (`GitRepository.kt:301-310`) |
| R2 | **Los `.md` de prompts NO pueden vivir en `05_Imagenes/`.** El clon es sparse y excluye `/05_Imagenes/` entera: un `.md` ahí solo se lee con `git show`, no del disco | `.git/info/sparse-checkout` |
| R3 | **Gemini escribe mal el texto dentro de imagen.** Resuelto por D4: ninguna lo lleva | Decisión de la Ama |
| R4 | **Tumblr** permite desnudo artístico desde 2022 pero sigue prohibiendo actos sexuales explícitos visuales. Resuelto por D3 | Guidelines de la plataforma + precedente PG-13 de NEXUM |
| R5 | **Un capítulo se reescribe entero.** «¿Cuánto es?» Cap 4 se rehizo completo con la nota de la Ama; «Modo Trofeo» Cap 1 va en v0.3. Un prompt escrito antes del Gate se muere con su versión — **y peor, la Ama ya habría gastado generaciones** | `memoria_sesiones.md`, sesión 04/09/2026 |

---

## 4. Arquitectura

### 4.1 Los tres dueños únicos

Regla dueño-único (02/07/2026): cada dato tiene UN archivo dueño; el resto **apunta**, no copia.

| Qué | Dueño único | Estado | Cómo viaja al prompt |
|---|---|---|---|
| **El estilo pop-art** | `01_Canon/Guias_Especializadas/estilo_comic_pop_v1.md` | 🆕 **único archivo de canon nuevo** | Fence `<!-- ADN:BLOQUE_ESTILO -->`, copiado **verbatim** en las 3 imágenes |
| **El personaje del relato** | `02_Personajes/01_Principales/ficha_<slug>.md` **§10** | ✅ ya existe (Renée) | Fence `<!-- ADN:BLOQUE_PERSONAJE -->`, copiado **verbatim** en las 3 |
| **Los prompts de un relato** | `03_Literatura/01_En_Progreso/<slug>/imagenes_prompts.md` | 🆕 documento vivo, crece por capítulo | Es el entregable que la Ama pega en Gemini |

**Por qué fences y no prosa:** es el patrón que ya funciona. `PromptBuilder.bloque_a` lee el ADN desde `<!-- ADN:BLOQUE_A -->` en el perfil visual, y por eso `build()` toma `bloque_a=None` y ningún batch lo hardcodea. Antes de eso el ADN se copiaba a mano en cada script y derivaba. Dentro del fence va **solo texto de prompt**; las notas editoriales van fuera.

### 4.2 Contrato de nombres

```
05_Imagenes/portadas/portada_<slug>.png            1 por RELATO — se repite en todos sus posts (D7)
05_Imagenes/historias/<slug>/cap<N>_a.png          beat de instalación del fetiche
05_Imagenes/historias/<slug>/cap<N>_b.png          el cliffhanger (D8)
```

- Gana `portada_<slug>` porque es la forma mayoritaria medida: **13 contra 3**.
- `<slug>` es el mismo slug de la carpeta del relato en `03_Literatura/`. Un solo slug para texto e imagen.
- `<N>` sin padding, igual que `capitulo_<N>_*.md`.

### 4.3 Anatomía de un prompt

Cada prompt es la concatenación de cuatro bloques, **en este orden**:

```
[BLOQUE ESTILO]      verbatim del dueño — idéntico en las 3 imágenes del relato
[BLOQUE PERSONAJE]   verbatim de la ficha §10 — idéntico en las 3
[ESCENA]             lo único que cambia entre imágenes: acción, encuadre, prop, luz
[NEGATIVO]           base anti-filtro + anti-texto + anti-deriva
```

Es la misma Ley de Continuidad de los looks: lo que define identidad se copia idéntico y **solo se varía la toma**. Ahí, dejar el calzado suelto hacía que cada pose saliera con un zapato distinto; acá, dejar el personaje suelto hará que Renée cambie de cara entre la portada y el capítulo 3.

**Borrador del BLOQUE ESTILO** (a validar con la Ama contra su imagen de referencia antes de congelarlo — ver A2):

```
1960s romance comic book illustration, vintage print aesthetic, bold black ink
outlines of even weight, flat cel-shaded color with no gradients, Ben-Day halftone
dot texture in the shadows and background, limited palette dominated by pinks and
cream, off-register print feel, clean single panel, portrait orientation
```

**Negativo base** (obligatorio en las 3):

```
text, lettering, speech bubble, caption box, watermark, signature, logo,
multiple panels, collage, split frame, photorealistic, 3d render, blurry,
extra fingers, deformed hands, flat shoes, sneakers, barefoot
```

`text, lettering, speech bubble, caption box` implementan D4. El cierre de calzado se hereda del Footwear Canon cuando el personaje lo tenga declarado en su ficha.

**Vocabulario anti-filtro obligatorio** (calibración v4.5/v4.6, ya canon en el repo): `glamorous woman` (no *bimbo*), `sensual` (no *sexy*), `alluring` (no *slutty*), `fashionable` (no *revealing*), `human realistic` (no *plastic*). Los prompts se escriben **en inglés**, como todo prompt de imagen del repo.

### 4.4 El flujo (Opción A + cliffhanger)

```
   Gate del Cap N existe como archivo
              │
              ▼
   /ilustrar_relato <slug> <N>
              │
              ├─ ¿ficha_<personaje>.md §10 activada?  ── no ──▶ se escribe CON la Ama, y para
              │
              ├─ Cap 1:   portada + cap1_a + cap1_b      (3 prompts)
              └─ Cap N>1: cap<N>_a + cap<N>_b            (2 prompts)
              │
              ▼
   imagenes_prompts.md  ──▶  la Ama los pega en Gemini  ──▶  devuelve los PNG
              │
              ▼
   el agente los commitea con el nombre del contrato §4.2
   y cablea las URL raw.githubusercontent en _publicacion/<slug>_tumblr.md
```

**Gate obligatorio (R5).** El skill **no corre** sobre un capítulo sin `gate_capitulo_<N>_<slug>_v0.<X>.md`. No es burocracia: es lo que evita que la Ama gaste generaciones en Gemini sobre una versión que va a morir.

**Cómo se eligen las 2 escenas:**

- **`cap<N>_b` = el cliffhanger.** No requiere planificación nueva: la medida **T9** del Validador ya obliga a que todo capítulo salvo el último cierre en su beat más caliente, y el Compositor ya lo planifica en el Mapa de Capítulos. Esa toma **ya está diseñada**; solo hay que fotografiarla.
- **`cap<N>_a` = el beat de instalación del fetiche** — el momento del capítulo donde el motivo permanente (`investigacion.md` §5) se hace visible por primera vez en esa escena.
- **La portada = la promesa del relato entero**, no una escena. Tiene que servir de encabezado del Cap 3 igual que del Cap 1 (D7): personaje de cuerpo entero, encuadre de portada, sin acción narrativa concreta.

---

## 5. Verificación

Regla 13: esto es código, entra en el alcance de superpowers y va con TDD.

**`99_Sistema/scripts/visual/lint_prompts_relato.py`** — hermano de `lint_prompts_personaje.py`. Falla si un prompt:

| # | Chequeo |
|---|---|
| L1 | No contiene el BLOQUE ESTILO **verbatim** del dueño |
| L2 | No contiene el BLOQUE PERSONAJE **verbatim** de la ficha §10 |
| L3 | Pide texto, lettering o bocadillo dentro de la imagen (viola D4) |
| L4 | Le falta el negativo base completo |
| L5 | Usa vocabulario que rebota el filtro (`bimbo`, `naked`, `slutty`, `nude`…) |
| L6 | Está en español (los prompts de imagen van en inglés, siempre) |
| L7 | Los 2-3 prompts de un mismo capítulo comparten el bloque ESCENA (clon de toma) |
| L8 | Un PNG referenciado en el `_tumblr.md` no existe en `git ls-files`, o al revés |

**L8 se mide contra el índice de git, nunca contra el disco.** El clon es sparse y no tiene los PNG; medir el disco reportaría miles de falsos positivos. Es exactamente el error que ya se cometió dos veces en este repo (`update_galleries.py` el 04/09 y el debut de H7 en `lint_higiene_repo.py`).

> 🩹 **Y se cometió una tercera vez escribiendo este mismo spec.** Al verificar el dato de las URL, `git grep -l … -- '*README.md'` devolvió **0**; el mismo comando contra `HEAD` devolvió **1.085**. El árbol de trabajo no tiene esos archivos. La trampa no es teórica y no se aprende una sola vez: el linter usa `git grep <rev>` / `git ls-files`, nunca `os.walk` ni `open()`.

---

## 6. Trabajo de saneamiento que este diseño arrastra

| # | Qué | Quién decide |
|---|---|---|
| S1 | Unificar las 3 portadas de «Smart Home Stepford» y las 2 de «Brillando en Tacones» a una sola | 🔴 **La Ama** — es borrar contenido creativo |
| S2 | Renombrar los 3 `<slug>_cover.png` a `portada_<slug>.png` | Agente, tras resolver S1 |
| S3 | Renombrar las imágenes internas de los 5 relatos de `historias/` al contrato §4.2 | Agente, retrofit-al-tocar (nunca migración masiva) |
| S4 | Derogar la línea «PARQUEADA» de `ficha_renee.md` §10 | Agente — la orden de hoy la activa; se anota con fecha |
| S5 | **Referencia cruzada rota** en `ficha_renee.md:4`: dice *"el diseño visual queda parqueado en **§7**"* y la sección real es **§10** (§7 es «Voz — banco de frases»). Encontrado verificando este spec | Agente — corrección trivial, se hace junto con S4 |

---

## 7. Consecuencias de canon que ya se conocen

- **«Hora Pedida»: la portada debe ser Renée, no la paciente.** Lo decidió la Ama el 07/09: *"el paciente déjalo como difuso para que el lector se identifique"*. Ponerle cara a la paciente rompe el dispositivo del relato. Las internas **sí** pueden mostrar su cuerpo (*"el cuerpo sí se escribe, la biografía no"*), pero de espaldas, recortada o en POV — nunca la cara.
- **Renée ya tiene su espacio visual verificado** contra los tres BLOQUE A vigentes: pelo negro azabache (Ele cherry / Miss Doll platino / Anaïs miel), ojos café oscuro, **boca mate** (las tres nuestras son gloss), cuerpo natural blando, luz de día. Su §10 se activa, no se inventa.
- **Este sistema no toca el outfit-engine.** Los personajes de relato están **fuera** del engine por decisión de la Ama del 07/09 (`ficha_renee.md:4`). No llevan perfil visual en `_perfiles_visuales/`, no llevan looks, no entran en las galerías y no los ve LV-App.

---

## 8. Decisiones abiertas (declaradas, no escondidas)

| # | Qué falta decidir | ¿Bloquea? |
|---|---|---|
| A1 | **La frecuencia de publicación** — la Ama la dejó explícitamente por definir (D5) | **No.** El disparador del sistema es el Gate de un capítulo, no un calendario. El sistema funciona sin que exista cadencia |
| A2 | **El BLOQUE ESTILO definitivo** — el borrador de §4.3 hay que contrastarlo contra la imagen de referencia de la Ama y calibrarlo con 1-2 generaciones de prueba | **Sí** para producir. **No** para escribir el plan |
| A3 | Si «¿Cuánto es?» (Café con Piernas, 47,8% de sus lecturas) estrena el sistema como piloto de catálogo ya publicado | No |

---

## 9. Criterio de éxito (medible)

1. **Un capítulo con Gate llega a Tumblr con sus 2 imágenes y su portada, y `lint_prompts_relato.py` en 0.**
2. **El personaje es reconocible entre la portada y la última imagen del relato** — verificado por la Ama, que es la única que ve los PNG.
3. **Cero prompts desperdiciados:** ninguna generación gastada sobre una versión de capítulo que después cambió. Es el motivo entero de exigir el Gate.
4. `lint_higiene_repo.py` sigue en **0** después de introducir el sistema.
