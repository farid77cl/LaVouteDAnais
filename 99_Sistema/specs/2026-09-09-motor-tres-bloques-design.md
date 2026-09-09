# Diseño — Motor de tres bloques (A · B · C) con campos de dueño único

| Campo | Valor |
|---|---|
| **Fecha** | 09/09/2026 |
| **Autor** | Ele de Anaïs (Vibe Architect) |
| **Origen** | Ama, sesión 09/09/2026: *«el bloque A es donde se describe el físico, no debería cambiar entre prompts; el bloque B debería describir el outfit, tampoco debería variar; el bloque C debería describir pose y ambiente»* · *«mientras más detalles menos desviación»* · *«construye un nuevo outfit engine desde ese concepto»* |
| **Estado** | 🟢 Aprobado en concepto por la Ama; diseño escrito para ejecutarlo |
| **Destino documental** | *working* (regla 12) |
| **🪦 Fecha de muerte declarada** | Muere cuando el motor nuevo gane el A/B (Fase 3 del plan) y su contrato viva en `campos.json` + `.agent/rules/06-generacion-imagenes.md` §10. Ahí se borra. |

## 1 · La ley

**Un atributo, un campo, un bloque.** Todo lo que se le dice a Gemini vive en exactamente un lugar. El detalle es bienvenido —*«mientras más detalles menos desviación»*— pero **dos cláusulas sobre el mismo atributo son una pelea**, y en la pelea gana la de más peso, que es la equivocada (L831: la falda que se abrió).

Los tres bloques responden **cuándo cambia** el texto:

| Bloque | Qué describe | Cambia… | Dueño |
|---|---|---|---|
| **A** | el cuerpo | **nunca** dentro de un personaje | perfil visual §2 |
| **B** | lo que lleva puesto | **por look**, idéntico en las 7 poses | batch JSON (`bloque_b` + campos) |
| **C** | pose, cámara, ambiente, luz | **por pose** | repertorio de sub-poses + setting del look + slot |

Y **dentro de cada bloque no hay párrafo: hay campos con nombre.** Un campo se cambia solo, se audita solo, se mide solo. Como cada atributo tiene un campo único, no puede vivir en dos — **la contradicción es imposible por construcción**, no por detector. (El detector `contradicciones.py` se queda como cinturón y tirantes.)

## 2 · Lo que está roto hoy, medido

- **B se filtra tres veces.** En el ensamblado actual (`prompt_builder.build`), después de `A. B.` viene un tercer tramo con **las anclas globales** (GARMENT_CONSISTENCY, BOTTOM_CUT_LOCK — que describen prenda), después la pose y el setting, y al cierre **dos ecos** que vuelven a describir la prenda (FOOTWEAR_ECHO, eco de busto). Tres lugares para un atributo = tres chances de contradecirse.
- **A tiene prendas adentro** (solo Anaïs): calzado negro charol, uñas largas, corsé de tightlacing. 7 de 7 prompts del L91 —el que estrena su veto de corsetería— piden corsé en el ADN.
- **37 anclas sin bloque.** Se apilan en el tercer tramo por *cuándo se inyectan* (siempre / por slot / opt-in), no por *qué describen*. Tres cruzan bloques: `DRESS_LEG_CLOSURE` (prenda→pose), `BOTTOM_CUT_LOCK` (corte B + exposición C), `FOOTWEAR_ECHO` (B repetido).
- **Volumen.** Ele 6.000-6.600 chars por prompt, Anaïs 8.500-9.000, con 5 cláusulas `:1.4` compitiendo. A solo: Ele 198 palabras · Miss Doll 354 · Anaïs 488.

## 3 · Los campos

Cada campo declara: `id` · `bloque` · `dueño` · `obligatorio` · `vocabulario` (regex de lo que solo puede aparecer en ese bloque). El contrato vive en **`99_Sistema/scripts/visual/campos.json`** (dueño único; los perfiles y batches lo *llenan*, no lo redefinen).

### Bloque A — el cuerpo (dueño: perfil §2, un campo por línea)
`rostro` · `ojos` (iris + mirada base) · `cejas` · `boca` (forma, no color) · `piel` · `pelo` · `busto` · `cintura_caderas` · `manos_base` (calidad de uña, no forma ni largo) · `edad_porte` · `fotorrealismo`

### Bloque B — lo que lleva (dueño: batch, campos declarados por look)
`prenda_principal` · `prenda_secundaria` · `calzon` (**con su corte**) · `calzado` (sus atributos completos) · `medias` · `capa` (piel/abrigo/bata, y cómo cae) · `joyas_y_hardware` (cada pieza, cuántas, en qué lado) · `guantes` · `unas_del_look` (forma, largo, color) · `maquillaje_de_color` (sombra + labios: el **color**; la técnica es A) · `fit_y_material` (tensión, brillo, opacidad, print) · `no_lleva` (lo excluido)

### Bloque C — la toma (dueño: repertorio + setting + slot)
`encuadre` (plano, orientación, aspecto) · `orientacion_cuerpo` (frente/espalda/perfil) · `postura` (la sub-pose) · `apoyo` (asiento/suelo/reclinada) · `piernas` (cerradas con vestido…) · `manos_en_escena` (una mano, gesto) · `mirada` (a lente / fuera) · `ambiente` (setting + props resueltos) · `luz` · `un_solo_cuadro` (anti-collage, sin dispositivo, una sola mujer) · `en_cuadro` (**referencias**, nunca re-descripciones: *«the footwear exactly as described above»*)

## 4 · Dónde cae cada ancla (las 37)

| Bloque | Anclas que se vuelven campo |
|---|---|
| **A** | ANATOMY_FULL · ANATOMY_CLOSE · PHOTOREAL_LOCK |
| **B** | GARMENT_CONSISTENCY · SEAM_FRONT · SEAM_BACK · OPAQUE_LOCK · GLOSS_LOCK · HOSIERY_LOCK · ANIMAL_PRINT_LOCK · WRAP_BACK_ROBE · WRAP_BACK_TAILORED · ASYMMETRY_LOCK · ACCESSORY_COUNT_LOCK · GARMENT_EXCLUSION_LOCK · LEG_CUT_LOCK · FABRIC_PRISTINE · **BOTTOM_CUT_LOCK → solo el corte** |
| **C** | SINGLE_FRAME · SINGLE_SUBJECT · POV_NO_DEVICE · FRONT/BACK/SIDE_ANCHOR · ASPECT_* · LEVEL_HORIZON · SEAT/RECLINE/FLOOR_SEAT_ANCHOR · SINGLE_HAND_CLOSE · GAZE_* · SENSUAL_STATE · LIVED_IN_ROOM · **DRESS_LEG_CLOSURE → `piernas`** · **BOTTOM_CUT_LOCK → la exposición, condicional a B** · **FOOTWEAR_ECHO y eco de busto → `en_cuadro`, como referencia** |

Las tres que cruzaban se **parten**, no se copian: el corte del calzón es B; que se vea o no el asiento depende de si B declara prenda encima, y eso lo decide C. Los ecos dejan de re-describir: *«exactly as described above»* y nada más.

## 4bis · Un personaje nuevo es DATO, nunca código (Ama 09/09/2026: *«debe ser flexible para poder agregar nuevos personajes»*)

Agregar una muñeca = tres archivos de datos y cero líneas de motor:

1. su perfil visual con la cerca `ADN:BLOQUE_A` — **las mismas líneas, en el mismo orden universal** de `campos.json` (una vacía = campo que esa muñeca no tiene);
2. su entrada en `anclas_universales.json` (rutas, slot5, anclas propias, rotación);
3. su repertorio de sub-poses en `repertorios_pose.json`.

Por eso el orden de campos A es **universal y no por personaje**: si cada muñeca declarara el suyo, la cuarta tendría que configurar el motor en vez de llenarlo. Lo que difiere por muñeca (guantes sí/no, rosa firma, lunar, iris) se expresa **en el contenido de sus campos**, no en la estructura. Guardia medible: un personaje de prueba, creado solo con datos en un directorio temporal, tiene que emitir sus 7 prompts sin tocar un `.py`.

## 5 · Ensamblado

Orden fijo, siempre: **A → B → C**, y dentro de cada bloque el orden de `campos.json`. Tres oraciones, cada una cierra con punto. Sin pesos `:1.x` por defecto — el peso vuelve a ser **excepción declarada en el campo**, no rutina. El negativo se arma igual: base del perfil + `no_lleva` del look.

Presupuesto de largo **reportado por bloque** en cada emisión (A/B/C en chars y palabras). No se impone: se mide, y el A/B decide.

## 6 · Guardias (medidas, no prometidas)

1. **Fuga entre bloques**: el vocabulario de un campo no puede aparecer en otro bloque (calzado en A, iris en C, pose en B). Corre en la puerta.
2. **Campos obligatorios presentes** por bloque y por personaje (lo que hoy dice §5.5 en prosa pasa a ser dato).
3. **Contradicciones** (`contradicciones.py`), como segunda línea.
4. **Idempotencia**: el mismo batch emite el mismo prompt, byte a byte.

## 7 · Lo que NO se reconstruye

Funciona y se queda: batch como dato · perfiles como dueños · repertorio de sub-poses y su rotación · canon de color y sus ventanas · `generar` como única puerta · el linter de galería. Se reconstruye **solo el ensamblado del prompt y su contrato**.

## 8 · Cómo se decide que ganó

Fase 3 del plan: el mismo look emitido por los dos motores, la Ama genera las dos tandas, `outfit.py ojos` las audita a ciegas. Si el de bloques no baja los defectos, **se dice así** y el viejo se queda.
