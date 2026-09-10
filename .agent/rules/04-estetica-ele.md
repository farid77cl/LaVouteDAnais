---
paths: 05_Imagenes/ele/**/*, 00_Ele/galeria_outfits.md
---

# 🫦 ESTÉTICA CANÓNICA DE ELE

> Actualizado 10/09/2026 (auditoría externa Fable) — los nombres de ancla de este archivo eran del motor viejo (`pose_rotation_v5.py`, un solo personaje) y ya no existen así en `anclas_universales.json` (el sistema vivo, usado por `outfit.py generar`/`prompt_builder.py`): `STANDING_ANCHOR`→`FRONT_ANCHOR`, `SEATED_ANCHOR`→`SEAT_ANCHOR`, `CONSISTENCY_LOCK`→`GARMENT_CONSISTENCY`. `CORSET_BUST_LOCK` vivía SOLO en el motor viejo — portado hoy mismo al vivo (§4-bis). El resto del razonamiento (por qué existe cada ancla, qué imagen la disparó) sigue siendo evidencia real y se conserva.

## 👠 Calzado

**Regla de Oro, dueño único: `02_Personajes/_perfiles_visuales/ele.md` §5.3.** Stiletto ≥12cm o Pleaser platform ≥6" — nunca un rango de pulgadas fijo por modelo, eso ya lo decide el perfil por arquetipo.

### 🧦 REGLAS DE MEDIAS + CALZADO (Directiva Ama 20/06/2026 — INQUEBRANTABLES)

Cuando un look lleva **medias de cualquier tipo** (nylon, red/fishnet, costura, opacas), el calzado obedece:

1. **🚫 MEDIAS + PUNTA ABIERTA = PROHIBIDO.** Nada de `peep toe` ni `open toe` con medias — la costura/refuerzo de la punta asomando se ve barato. El zapato va siempre de **punta cerrada** (`closed pointed toe`). Aplica a stiletto, plataforma y botas.
2. **🚫 MEDIAS NEGRAS + MINI FALDA BLANCA = NO ABSOLUTO.** La media negra parte la pierna en seco bajo la falda blanca. Si la falda es blanca/crema → la media va de otro color (o nude/transparente), o se quita la media.
3. **👠 MEDIAS + (donde iría Pleaser) = PLATFORM PUMP de punta cerrada.** El clear Pleaser open-toe que la Ama adora (default pole/bikini) **solo se usa en looks SIN medias**. En cuanto hay medias, ese Pleaser se reemplaza por un **platform pump cerrado** (mismo platform stiletto ≥6", `closed pointed toe`).
4. **🎨 PLATAFORMA = MISMO COLOR DEL ZAPATO (Ama 20/06/2026).** La plataforma NUNCA es de un color distinto al cuerpo del zapato. El token de calzado debe nombrar **explícitamente el color de la plataforma igual al del zapato** (ej. `cherry-red patent platform stiletto pumps … with a matching 2-inch cherry-red platform`). Excepción única: el **clear/transparent acrylic** (plataforma + zapato ambos transparentes = ya son "el mismo color").

> **Chequeo de batch:** si un prompt contiene `fishnet`/`nylon stocking`/`stockings`, NO puede contener `open toe`/`peep toe`. Y `white skirt` + `black stockings` = 0. El gate real es `outfit.py generar` — `footwear_canon.py`/`garment_canon.py` son sus self-tests de fixtures, no auditan la flota por sí solos (`auditar_canon_flota.py` sí).

## 🖥️ FIDELIDAD PROMPT→IMAGEN (Directiva Ama 11-12/07/2026 — auditorías L691-L760)

Seis desvíos sistemáticos detectados mirando la imagen final vs el prompt, cada uno con su ancla en `anclas_universales.json`:

1. **🧵 RAYA DE LA MEDIA SIEMPRE POR DETRÁS.** `back-seam stockings` es relativo a la cámara → de frente Gemini pinta la costura por delante (confirmado L691/L752/L748). Si el look declara medias con costura, `SEAM_FRONT`/`SEAM_BACK` se disparan solos por vocabulario (`prompt_builder.opt_in_de` — costura declarada + contexto de media + medias de verdad, las tres condiciones).
2. **🚫 PRENDA CUBIERTA = SÓLIDA, SIN CORTES.** Los tokens de ADN (`navel piercing`, `rune tattoo along hip crease and bikini line`) hacen que Gemini **le abra ventanas** a la prenda para exponerlos (confirmado L706, L699). En arquetipos **cubiertos** pegar `OPAQUE_LOCK`. El `wherever the garment covers` deja que runas/ombligo SÍ se luzcan en lencería/bikini/alto-corte (on-brand) — solo prohíbe cortar una prenda que debía cubrir. **Bloque A NO se toca.**
3. **✨ REGLA ANTI-MATE (siluetas de riesgo).** En siluetas que primean tela mate (sastrería de lana/crepé, rib atlético, satén nupcial plano), el sesgo del arquetipo le gana al token `vinyl/latex` (confirmado L732, L750) — tener `vinyl` en el texto NO basta. Dos capas: **(a)** preferir siluetas que no primeen mate; **(b)** si es obligada, pegar `GLOSS_LOCK`.
4. **📐 CONSISTENCIA DE PRENDA ENTRE POSES (escote/manga/largo).** El Token de Vestuario Bloqueado se pega idéntico ×7, pero si deja el escote/manga/ruedo sin fijar, Gemini reinventa el corte pose a pose (confirmado L746, L707, L693). El token DEBE nombrar explícito **neckline + sleeve length + hemline**; `GARMENT_CONSISTENCY` lo refuerza. Detalle del token: `02_Personajes/_perfiles_visuales/ele.md` §5 (Token de Vestuario Bloqueado — no en identidad, se movió).

4-bis. **🍈 ESCOTE ALTO SOBRE EL FILO — efecto recurrente que pidió la Ama (20/07/2026).** *"adoro cuando tus tetas están así, a punto de reventar del corset"* → no es un piropo, es canon de diseño: borde estructurado bajo, apretando por debajo del busto, las esferas altas y llenas sobre el filo. **`CORSET_BUST_LOCK`** (portado 10/09/2026 al vivo — antes solo existía en el motor viejo, así que ningún look de Miss Doll/Anaïs ni los looks nuevos de Ele lo recibían) se dispara solo cuando el BLOQUE B nombra corsé/overbust/bustier/waist-cincher/basque/merry-widow/corselette. **Redacción anti-filtro:** nunca `deep cleavage` ni `spilling out/bursting` (rebotan el safe de Gemini) — el ancla describe la arquitectura, no el escote.
5. **🪑 SEATED — mueble equivocado y postura ignorada.** Si el setting trae una segunda superficie cerca del asiento, Gemini apoya el cuerpo en ESA en vez del asiento nombrado (confirmado L732, L754) — `SEAT_ANCHOR` ancla el peso y prohíbe apoyarse en mobiliario vecino.
6. **🧍 STANDING — la pose de frente sale de espalda.** Era el único slot sin ancla de orientación propia; tokens de giro débiles la arrastraban fuera del frente (confirmado L751, L760). `FRONT_ANCHOR` prepende frontalidad explícita. **Standing es la pose HERO** — perderla duplica la Back View y el set queda sin frente. No se arregla con el negative (es compartido con Back View, que legítimamente ES de espalda) — el lever es el ancla en el positivo.

> 🔁 **Los prompts fosilizan.** Cada fix protege a los batches *futuros* — los ya registrados conservan el texto de su época. Al cerrar un fix, auditar los prompts SIN imagen y refrescarlos.

## 💋 Maquillaje, uñas, pelo, materiales — dueño único

Estos campos son ADN (Bloque A) — viven en el fence `<!-- ADN:BLOQUE_A -->` de `02_Personajes/_perfiles_visuales/ele.md` §2, no se copian aquí (una copia aparte fue exactamente lo que causó que este archivo quedara con el rostro pre-04/09). Lo único que no es ADN sino regla de vestuario: **vinilo/látex/PVC high-gloss siempre**, tela natural mate nunca — el negro está liberado (07/06/2026) pero también va siempre en gloss.

## 🎨 Color y materiales

**Dueño único: `ele.md` §5.2 y §7.** La libertad total de color del 12/06/2026 sigue siendo el principio, pero el **02/08/2026 reinstaló topes reales** (ventana de familia dominante en 3 looks, tope de 2 consecutivos negro/metal, rojo/cherry no dominante) y la regla 11 §9septies (05/09) suma el máximo 2-por-familia-en-5, aplicado por `outfit.py generar`. No se repiten los números aquí porque ya divergieron una vez — se apunta.

---

**Voz, personalidad, muletillas:** dueño único `00_Ele/identidad_ele.md` §III — no se copia aquí.
