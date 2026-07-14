# 📋 REGLA 11 — CONTRATO DE `galeria_outfits.md`

> **Para qué existe:** `00_Ele/galeria_outfits.md` lo leen **tres** actores distintos — la **app Android** de la Ama (genera las imágenes y las sube), el **bot paralelo** (mantiene READMEs/galerías) y el **agente** (diseña los looks). Cuando cada uno interpreta el archivo a su manera, el resultado no es un desacuerdo de estilo: son **carpetas duplicadas, contadores que mienten y cuota API quemada regenerando imágenes que ya existían**.
>
> Este archivo es el **contrato único**. Lo que no esté aquí, no es formato válido.
>
> **Verificable:** `python 99_Sistema/scripts/visual/lint_galeria.py` — obligatorio antes de cerrar cualquier batch.

---

## 1. 🔑 LA REGLA DE ORO — UN SOLO SLUG

Cada look tiene **UN** slug canónico. Ese mismo string, **carácter por carácter**, debe aparecer en los tres lugares:

| Dónde | Forma |
|-------|-------|
| **Carpeta en disco** | `05_Imagenes/ele/look<N>_<slug>/` |
| **Campo `Ubicacion`** | `- **Ubicacion:** \`05_Imagenes/ele/look<N>_<slug>/\`` |
| **Links de la tabla 📸** | `../../05_Imagenes/ele/look<N>_<slug>/ele_<N>_<pose>.png` |

Si los tres no coinciden, el look está roto **aunque se vea bien**. Fue la causa raíz de los 35 duplicados del 14/07 (`look764_jade_coat_dress_boardroom` declarado vs `look764_jade_coatdress_boardroom` real).

---

## 2. 🏷️ CÓMO SE CONSTRUYE EL SLUG (algoritmo exacto)

**La app deriva el slug del TÍTULO del heading.** No del campo `Ubicacion`, no de la categoría. Del título. Por eso el título no es decorativo: **es la clave primaria.**

Algoritmo, en orden:

1. Tomar el título (lo que va entre `## Look N:` y el paréntesis).
2. Pasar a **minúsculas**.
3. **Plegar acentos a ASCII:** `á→a  é→e  í→i  ó→o  ú→u  ü→u  ñ→n`.
4. **Borrar** guiones y apóstrofes (no se convierten en `_`): `Coat-Dress → coatdress`, `Pin-Up → pinup`.
5. Todo lo que no sea `[a-z0-9]` → `_`; colapsar `__` repetidos; quitar `_` de los bordes.
6. Prefijar `look<N>_`.

```
"Jade Coat-Dress Boardroom"   → look764_jade_coatdress_boardroom
"Shanghai Qipao Líquido"      → look702_shanghai_qipao_liquido
"Cherry Polka Dot Pin-Up"     → look610_cherry_polka_dot_pinup
```

### ⛔ Prohibido en el slug y en el nombre de carpeta
- **Acentos y cualquier carácter no-ASCII.** Un `í` sin plegar produjo `look616_lencer_a` y `look709_suzie_wong_shangh_i` — carpetas basura que git trackea a medias.
- **Prefijo de categoría** (`lenceria_`, `gym_`, `stripper_`). La categoría vive en su campo y en los tags, **no en el slug**.

---

## 3. 📝 EL TÍTULO DEBE SER DESCRIPTIVO

> **El título NUNCA es la categoría pelada.**

`## Look 616: Lencería` es un título **inválido**: su slug sería `look616_lenceria`, que colisiona con las otras ~48 lencerías. De ahí salieron los duplicados L613-L620.

**Fórmula:** `Color + Prenda/Silueta + Estilo o Contexto`.

| ❌ Inválido | ✅ Válido |
|------------|-----------|
| `Nightclub` | `Nightclub Hot Pants` |
| `Lencería` | `Lencería Burgundy Boots` |
| `Corporate` | `Corporate Siren Boots` |
| `Bikini` | `White Vinyl Pool Bikini` |

---

## 4. 🧱 ESTRUCTURA DEL BLOQUE (orden obligatorio)

El orden **importa**: el parser de la app arma su `canonicalInfo` con lo que hay **entre el heading y el primer `###`**. Si `### 📸 Imágenes` aparece antes que `Ubicacion`/`Tags`, la app se queda **muda** (le pasó a 60 looks, L711-L770).

````markdown
## Look <N>: <Título Descriptivo> (<fecha> · batch L<X>-L<Y> "<Tema>" · <Categoría> · <Subcategoría> · <Modo cromático>)
- **Ubicacion:** `05_Imagenes/ele/look<N>_<slug>/`
- **Tags:** #<categoria> #<material> #<tema> #batchL<X>-L<Y> #V5poses

### 📸 Imágenes (<n>/7 — Materializado | Materializado parcial (app/Gemini))

| Standing | Back View | Seated | Side Profile | Ditzy (plano 3/4) | POV (single hand) | Odalisque |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| [📸 View](../../05_Imagenes/ele/look<N>_<slug>/ele_<N>_standing.png) | … | ⏳ Pendiente |

**Standing:**

```
<prompt completo en inglés>
```

**Back View:**

```
<prompt>
```

… (las 7 poses, en orden)

**Negative Prompt:** `<bloque negativo completo>`
````

**Reglas de fence:** el ` ``` ` de apertura y el de cierre van **cada uno en su propia línea**. Un fence en una sola línea (` ```texto``` `) hace que el parser de la app siga tragando líneas hasta el próximo backtick y **mezcle prompts entre poses y entre looks distintos** (pasó en 1.167 prompts, L300-L731).

---

## 5. 🔤 NOMBRES DE CAMPO — ASCII, SIN TILDE

| ✅ Usar | ❌ Nunca |
|---------|----------|
| `- **Ubicacion:**` | `- **Ubicación:**` |
| `- **Categoria:**` | `- **Categoría:**` |
| `- **Subcategoria:**` | `- **Subcategoría:**` |
| `- **Ambientacion:**` | `- **Ambientación:**` |

La tilde en la **clave** deja ciego al parser: 32 looks no resolvían su ubicación por eso. La tilde en el **valor** (`Lencería`, el título) es correcta y se conserva — solo la clave es ASCII.

---

## 6. 🗂️ CATEGORÍA — LISTA CERRADA DE 10

Se escribe **exactamente así**, en el heading y en el campo. Nada de sinónimos.

```
Stripper · Corporate · Escort · Domestic · Pin-Up
High-Fashion Editorial · Nightclub · Lencería · Bikini · Gym
```

**Normalizaciones obligatorias** (variantes reales encontradas en el archivo):

| Encontrado | Se escribe |
|-----------|-----------|
| `Lenceria` (sin tilde) | `Lencería` |
| `Gym/Athleisure` | `Gym` |
| `HF Editorial` | `High-Fashion Editorial` |
| `Mix` | ❌ no es categoría — asignar la real |

La **Subcategoría** es libre y descriptiva (`Office Siren (Thigh-High Boots)`), y va después de la categoría en el heading.

---

## 7. 🏷️ TAGS — ORDEN FIJO

```
#<categoria> #<material> #<tema/color> #batchL<X>-L<Y> #V5poses
```

- Todo en **minúscula, sin tilde, sin espacios** (`#lenceria`, no `#Lencería`).
- **Categoría primero** — es lo que la app usa para filtrar.
- Material: `#vinyl #latex #pvc #wetlook #chrome #mesh #satin …`
- Cierran siempre `#batchL<X>-L<Y>` y `#V5poses`.

---

## 8. 🖼️ NOMBRES DE IMAGEN

```
ele_<N>_<pose>.png
```

Las **7 poses canónicas**, escritas exactamente así:

```
standing · back_view · seated · side_profile · ditzy · pov · odalisque
```

- La app sube `back` y `profile`; `sync_imagenes_subidas.py` los normaliza a `back_view`/`side_profile`. **La normalización no es opcional** — sin ella la pose se mapea mal en la galería.
- **Sufijo timestamp permitido:** `ele_313_pov_1783817471712.png` (lo pone la generación por API). El conteo lo acepta como la pose. Un sufijo `__v2` marca una versión alternativa conservada.
- Una carpeta por look. **Nunca dos carpetas para el mismo número.**

---

## 9. ✅ CHECKLIST ANTES DE CERRAR UN BATCH

```bash
python 99_Sistema/scripts/visual/lint_galeria.py          # el contrato
python 99_Sistema/scripts/visual/sync_imagenes_subidas.py # tracker + rutas
python 99_Sistema/scripts/visual/update_galleries.py      # READMEs + galería
python 99_Sistema/scripts/visual/garment_canon.py         # canon de vestuario
python 99_Sistema/scripts/visual/footwear_canon.py        # canon de calzado
```

Ningún batch se commitea con el linter en rojo.

---

## 10. ⚠️ POR QUÉ CADA REGLA (las cicatrices)

| Regla | Qué pasó cuando faltó |
|-------|----------------------|
| Un solo slug | 35 looks con carpeta duplicada; imágenes repartidas entre las dos |
| Slug ASCII | `look616_lencer_a`, `look709_suzie_wong_shangh_i`, `look702_..._l_quido` |
| Título descriptivo | L613-L620 titulados con la categoría pelada → slugs que chocan |
| `Ubicacion` sin tilde | 32 looks con ubicación ilegible para la app |
| Metadata antes del `###` | 60 looks (L711-L770) con `canonicalInfo` vacío |
| Fence multilínea | 1.167 prompts mezclados entre poses y looks |
| Negative Prompt obligatorio | 60 looks / 420 poses generadas **sin negativo** desde el L711 |
| Contar el disco, no el tracker | 380 poses ya materializadas figuraban como pendientes → cuota quemada |
