# 🎀 Estilo Cómic Pop — dueño único del look visual de las publicaciones

> **Nace 07/09/2026** por orden de la Ama, para que todas las imágenes de sus relatos publicados en Tumblr compartan un mismo lenguaje visual.
> **Dueño único.** Ningún otro archivo escribe este bloque: lo **apuntan**. Si hay que cambiar el estilo, se cambia acá y se propaga solo.
> **🪦 Fecha de muerte:** vive mientras La Voûte publique con identidad visual de cómic. Si la Ama deroga el estilo, este archivo se archiva con nombre `ARCHIVO_LEGACY_*` — no se borra, porque las imágenes ya generadas lo declararon.

---

## 1. De dónde sale

> 📌 **El original va acá:** `01_Canon/Guias_Especializadas/referencia_estilo_comic_pop_v1.png`, al lado de este archivo, para que el estilo y su referencia viajen juntos. ⏳ **La sube la Ama** (comprometida el 07/09/2026). Mientras no esté, este estilo está congelado sobre un original que no se puede volver a verificar. (La ruta va en código y no como enlace **a propósito**: un enlace a un archivo que todavía no existe es un link roto, y la meta de `lint_higiene_repo.py` es 0. Se convierte en enlace cuando la imagen entre.)

De una imagen de referencia que la Ama entregó el 07/09/2026: una viñeta de Miss Doll en clave **portada de cómic romántico de los años 60** — halftone rosa, contorno negro grueso, color plano, cartucho «ROMANCE COMICS presents…» y bocadillo.

**Lo que se toma de ella:** el tratamiento gráfico entero — trama de puntos, tinta, planitud del color, encuadre de viñeta.
**Lo que se cambió (Ama, 07/09/2026):** la **paleta**. La de la referencia es la de Miss Doll; el blog lleva la cara de Anaïs, así que la paleta pasó a la suya (§2).
**Lo que NO se toma:** el texto quemado. Decisión de la Ama el mismo día: **ninguna imagen lleva letras adentro**; el título lo pone Tumblr en el post, donde además es buscable.

---

## 2. El BLOQUE ESTILO

> 🔒 **CONGELADO 07/09/2026** por okey de la Ama. Se copia verbatim; **no se edita sin orden suya**.

> 🍯 **La paleta se ajustó a Anaïs el 07/09/2026, por decisión de la Ama.** El bloque nació de una
> viñeta de **Miss Doll** y traía su familia (`hot pink, bubblegum, pale blush over warm cream`).
> Pero la Ama eligió a **Anaïs como cara del blog** (§6.1 del spec de publicación) y este bloque
> pinta **todas** las publicaciones: el blog entero se habría leído rosa chicle con una cara miel y
> ámbar que viene de Vintage Noir. Los cinco colores nuevos **no se inventaron** — salen textuales
> de [`anais.md` §5.2](../../02_Personajes/_perfiles_visuales/anais.md), que es la dueña de su
> paleta: oro imperial, bronce/cobre antiguo, rosa polvo, borgoña/vino profundo, marfil. El
> *dusty rose* conserva a propósito un eco del rosa de la referencia.
>
> ⚠️ **Lo que este ajuste cuesta, dicho una vez:** el bloque ya **no** es transcripción literal de la
> imagen de referencia. Se aleja de ella en el color y solo se sostiene en el papel — por eso la
> imagen tiene que entrar al repo (§1).

Se copia **verbatim** al inicio de todo prompt de publicación, idéntico en las tres imágenes de un mismo relato. Dentro de la valla va **solo texto de prompt** — las notas editoriales viven fuera, como en los perfiles visuales de las muñecas.

<!-- ADN:BLOQUE_ESTILO -->
```
1960s romance comic book illustration, vintage newsprint aesthetic, bold black ink
outlines of even confident weight around every figure and object, flat cel-shaded
colour with no gradients and no soft shading, visible Ben-Day halftone dot texture
carried through the shadows and the background field, limited palette built on old
gold, antique bronze and dusty rose with deep burgundy accents over a warm ivory
ground, slight off-register print misalignment, clean single comic panel with a thin
dark border, NO TEXT ANYWHERE, every label, sign, poster and garment surface
completely blank
```
<!-- /ADN:BLOQUE_ESTILO -->

**Por qué `NO TEXT ANYWHERE… every label blank` sí se puede escribir** y en cambio una línea `no nudity…` no: el filtro rebota por **tokens inseguros**, no por negaciones en general. Prohibir texto es seguro; nombrar lo sexual, aunque sea para vetarlo, hace rebotar el prompt entero. Doctrina medida en producción el 22/07/2026 — dueño: [`../../07_Recursos/plantilla_kit_wattpad.md`](../../07_Recursos/plantilla_kit_wattpad.md) §Reglas 2.

---

## 3. Los tres candados afirmativos (reemplazan al bloque negativo)

Este texto viaja **dentro** del prompt que la Ama pega en Gemini, donde no hay campo de negativo. Por eso la cobertura se consigue **construyendo**, no vetando.

| Candado | Cómo se escribe | La cicatriz que lo justifica |
|---|---|---|
| **GARMENT_DECLARED** | `SHE IS WEARING a [prenda] — worn on her body, closed, opaque — covering [zona] completely from [borde alto] to [borde bajo].` | La portada del Cap 1 de «De Esteban a Secretaria» salió **en topless**: el corsé estaba mencionado pero ningún verbo lo ponía sobre alguien, así que la IA lo dibujó como objeto suelto al costado |
| **CAMERA_FIRST** | Si la prenda que cubre no está del lado que ve la cámara, **se gira la cámara** — no se agregan adjetivos | La misma portada siguió saliendo en topless con la prenda ya declarada: se pedía vista frontal + cordones laceados por la espalda. Composición imposible; ninguna cantidad de palabras la arregla |
| **SEGUNDO_CUERPO** | `only a pair of FOREARMS AND HANDS enters the frame — no face, no head, no torso, no second body` | Sin ese candado la IA le fabrica un cuerpo entero al segundo personaje y arruina la composición |

**Espejos:** declarar a quién reflejan (`the mirror reflects HER OWN back — the same woman; no other person in the glass`) o aparece un personaje inventado.
**Asimetrías** (medio rostro, un guante, un zapato): nombrar izquierda y derecha y agregar `this asymmetry must be obvious`, o la IA las promedia.

---

## 4. Registro léxico

| ✅ Sirven | ❌ Rebotan o desvían |
|---|---|
| `glamorous`, `sensual`, `alluring`, `fashionable`, `human realistic`, `sculpted figure`, `cabaret nightclub`, `performance heels` | `bimbo`, `naked`, `nude`, `slutty`, `sexy`, `revealing`, `erotic`, `strip club`, `stripper heels`, `augmented bust`, `high-cut` |

Los prompts se escriben **en inglés**, como todo prompt de imagen del repo. Calibración anti-filtro v4.5/v4.6, ya canon.

### 4.1 ⚠️ Sin pesos `:1.4` — acá son texto inerte

Los BLOQUE A de las tres muñecas están cuajados de pesos de sintaxis Stable Diffusion (`(…:1.4)`). **En Gemini no hacen nada.** No es una sospecha: es el diagnóstico escrito en `02_Personajes/_perfiles_visuales/anais.md`, tras cuatro rondas de prueba sobre imagen real el 03/09/2026 —

> *"vocabulario diluyente (`naturally`, `soft`, `subtle`) y pesos `:1.4` de sintaxis Stable Diffusion que **Gemini no interpreta** (texto inerte)"*

**Consecuencia para este estilo:** el BLOQUE PERSONAJE de una publicación **no se copia del BLOQUE A de la muñeca**. Se **reescribe en inglés declarativo plano**, sin paréntesis de peso, conservando solo los rasgos de identidad (pelo, ojos, boca, lunar, edad, estructura ósea) y **descartando el vocabulario fotográfico** (`dewy skin`, `medical-grade cosmetic finish`, `visible pores`), que además contradice §7: acá se ilustra, no se fotografía.

Lo que en fotografía se consigue subiendo un peso, acá se consigue **diciéndolo una vez y bien**, o girando la cámara (CAMERA_FIRST).

---

## 5. Formatos y ratios

Gemini no entrega 2:3 ni 3:1 — se pide el ratio cercano y se recorta.

| Pieza | Se pide | Se recorta a | Regla de composición |
|---|---|---|---|
| **Portada de relato** | 3:4 | 2:3 (512×800) | Personaje de cuerpo entero, encuadre de tapa, **sin acción narrativa concreta**: tiene que servir de encabezado del Cap 3 igual que del Cap 1 |
| **Internas de capítulo** (`cap<N>_a`, `cap<N>_b`) | 3:4 o 1:1 | — | `_a` = beat de instalación del fetiche · `_b` = el cliffhanger |
| **Avatar del blog** | 1:1 | — | **Un solo rostro**, plano cerrado, alto contraste. A 64 px un cuerpo entero es una mancha |
| **Header del blog** | 16:9 | ~3:1 | **20% superior e inferior vacíos** para que el recorte no decapite nada |

---

## 6. Los dos techos de rating — no se mezclan

| Destino | Techo | Origen |
|---|---|---|
| **Wattpad** | Sin piel: prohibida la exposición completa de genitales, pechos y glúteos y toda representación de acto. **Deroga el canon visual de Ele para portadas** | Wattpad borra la imagen sin aviso |
| **Tumblr** | **PG-13 sugerente vestida** — látex, tacones, escote, collar, cara de trance; sin acto, sin desnudo | Decisión de la Ama 07/09 + guías de Tumblr (prohíbe *visual depictions of sexually explicit acts*; el desnudo artístico sí se permite desde 2022) |

**Cada prompt declara su plataforma techo.** El que sirve para Wattpad sirve para Tumblr; **nunca al revés**.

---

## 7. Lo que mata el estilo

- **Degradados y sombra suave.** Si tiene volumen pintado, dejó de ser cómic impreso.
- **Fotorrealismo.** Este bloque y el canon fotográfico de las muñecas son **incompatibles por diseño**: aquí se ilustra, allá se fotografía.
- **Texto generado.** Además de romper la decisión de la Ama, Gemini escribe mal: una portada salió con el título **«Secretaia»**, comiéndose una letra de una palabra de diez.
- **Paleta abierta.** El rosa-crema **es** la identidad. Un relato en verdes deja de reconocerse como de la misma casa.
- **Más de una viñeta.** Un panel. El collage es un defecto registrado del motor visual, no un recurso.

---

## 8. Quién apunta a este archivo

- `99_Sistema/specs/2026-09-07-ilustracion-relatos-design.md` §4.3 — anatomía del prompt
- `99_Sistema/specs/2026-09-07-publicacion-tumblr-design.md` §6 — imágenes del blog
- `<relato>/prompts_portada.md` — dueño de los prompts por relato; **copia** este bloque, no lo reescribe

---

## 6. 🔥 Los candados son anti-DESNUDO, no anti-CALOR (Ama 08/09/2026)

> *"le falta sensualidad a las imágenes, si elegí ese estilo es para darle ese estilo antiguo
> pinup, pero sensual… yo sé que hay filtros de seguridad, pero están bien fomes tus imágenes"*

**El modo de falla, medido sobre las cuatro primeras imágenes del blog.** Los tres candados
afirmativos (§3) existen para que la figura no salga desnuda y el prompt no rebote. Aplicados sin
criterio producen mujeres **bien portadas**, que es otra cosa. Textual de esos prompts, escrito por
la orquestadora: *«calm, frontal, inviting and unbothered»* · *«spine straight, chin up»* · *«arms
relaxed at her sides, flat unreadable expression»*. Eso no es pin-up, es un catálogo de tienda.

**La confusión que lo causa:** creer que *«no rebota»* y *«no calienta»* son el mismo eje. No lo
son. Es el mismo error que el Validador nombra en prosa con T1/T2 — un capítulo puede ser impecable
y frío, y una imagen también.

**El pin-up de los 60 calienta SIN PIEL.** La carga vive en el cuerpo, no en lo que se destapa:

| Palanca | Cómo se escribe |
|---|---|
| **Torsión** | `weight thrown hard onto one hip so the waist curves deep, the small of her back arched` |
| **Mirada** | `her chin is lowered and her eyes are lifted to the viewer from under her lashes` |
| **Boca** | `lips full and slightly parted` |
| **Manos** | `one hand raised to the nape of her neck, lifting her hair off her shoulder` |
| **Tela tensa** | `the knit is pulled taut across the sculpted figure by the twist of her pose` |
| **Movimiento** | `caught MID-STRIDE with one knee crossing in front of the other so the hips swing` |
| **El zapato** | `the heel has slipped free of its shoe and hangs, held on by the toes` |
| **Cámara** | `the camera is low, near hip height, so her legs run long up the panel` |
| **Medias** | `a seamed stocking runs up the calf below the hem` |

**Todas pasan el filtro** — ninguna nombra piel ni usa el léxico vetado de §4. Y todas conviven con
`GARMENT_DECLARED`: la prenda sigue puesta, cerrada y opaca. **La sensualidad no le quita ropa a la
figura, le cambia la postura.**

**Regla:** cada prompt de publicación declara **al menos tres** de esas palancas, y el bloque `MOOD`
nunca puede leerse como *tranquila, correcta o indiferente*. Si el mood se puede describir con
«compuesta», el prompt está frío y se reescribe antes de generar.

### 6.1 🖼️ Y el panel tiene que llenar el marco

Mismo día, defecto aparte: el prompt del Cap 1 salió como **una tira angosta flotando en el centro**
con dos franjas de fondo vacío a los lados — en el feed se lee diminuta. Añadido al BLOQUE ESTILO:
`the comic panel FILLS THE WHOLE IMAGE edge to edge with only a thin dark border — no empty margin,
no small panel floating inside a larger blank field`.
