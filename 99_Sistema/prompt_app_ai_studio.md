# 📱 Prompt para Google AI Studio — App La Voûte (lectura/escritura de `galeria_outfits.md`)

> **Uso:** copiar el bloque completo de abajo y pegarlo en AI Studio como instrucción para corregir la app.
> **Origen:** nace de la auditoría del 14/07/2026 (35 carpetas duplicadas, 380 poses que figuraban pendientes teniendo la imagen en disco, 60 looks generados sin bloque negativo).
> **Contrato de referencia:** `.agent/rules/11-contrato-galeria.md` · **Linter:** `99_Sistema/scripts/visual/lint_galeria.py`

---

```
Estás modificando una app Android (Kotlin) que hace dos cosas contra un repositorio de GitHub:
(1) LEE el archivo `00_Ele/galeria_outfits.md` para sacar prompts de generación de imágenes, y
(2) SUBE los PNG generados a `05_Imagenes/ele/` y actualiza el contador de ese mismo archivo.

Hoy tiene bugs que corrompen el repositorio. Necesito que reescribas el parser y el uploader
para que cumplan EXACTAMENTE el contrato que sigue. No inventes formato: respétalo al pie de la letra.

=====================================================================
A. ENCODING — REGLA CERO
=====================================================================
- Leer y escribir SIEMPRE en UTF-8 (sin BOM). Nunca ISO-8859-1, nunca ASCII forzado.
- NUNCA degradar un carácter acentuado a "_" ni a "?" al construir nombres.
  Bug real: el título "Lencería" produjo la carpeta `look616_lencer_a`, y
  "Shanghái" produjo `look709_suzie_wong_shangh_i`. Los acentos se PLIEGAN
  (í -> i), no se sustituyen por guión bajo.

=====================================================================
B. ESTRUCTURA DEL ARCHIVO
=====================================================================
Cada look es un bloque que empieza con un heading de nivel 2. Ejemplo REAL:

## Look 787: Gold Marquee Bodycon (13/07/2026 · batch L781-L790 "Glam Rock 80-90" · Nightclub · Rock Marquee Alley (Sequin Bodycon) · Monoblock)
- **Ubicacion:** `05_Imagenes/ele/look787_gold_marquee_bodycon/`
- **Tags:** #glamrock #nightclub #gold #sequinvinyl #batchL781-L790 #V5poses

### 📸 Imágenes (7/7 — Materializado)

| Standing | Back View | Seated | Side Profile | Ditzy (plano 3/4) | POV (single hand) | Odalisque |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| [📸 View](../../05_Imagenes/ele/look787_gold_marquee_bodycon/ele_787_standing.png) | ... |

**Standing:**

```
<texto del prompt en inglés, una o varias líneas>
```

**Back View:**

```
<texto del prompt>
```

(... y así las 7 poses ...)

**Negative Prompt:** `gothic, vampire, fangs, flat shoes, gloves, ...`

Reglas de parseo:
 B1. Un look empieza en `^## Look (\d+): (.*?) \(` — grupo 1 = número, grupo 2 = TÍTULO.
     El bloque del look termina donde empieza el próximo `## Look`.
 B2. Los campos son líneas `- **Clave:** valor`.
     IMPORTANTE: normaliza la clave quitando diacríticos ANTES de comparar.
     En el archivo conviven `**Ubicacion:**` y `**Ubicación:**`; ambas son la misma clave.
     Mismo criterio para Categoria/Categoría, Subcategoria/Subcategoría, Ambientacion/Ambientación.
 B3. `### 📸 Imágenes (n/7 — ...)` es el TRACKER, seguido de una tabla markdown.
     De ahí NO se sacan prompts. Es solo estado.
 B4. Los prompts son: una línea `**<Pose>:**` seguida de un bloque de código cercado.
     Las 7 poses, escritas exactamente así:
        Standing · Back View · Seated · Side Profile · Ditzy · POV · Odalisque
 B5. El bloque de código abre con ``` en su PROPIA línea y cierra con ``` en su PROPIA línea.
     BUG ACTUAL A CORREGIR: si encuentras un fence mal formado (``` de apertura y cierre en la
     misma línea, o sin cerrar), NO sigas tragando líneas hasta el próximo backtick — eso hace
     que se mezclen prompts entre poses y hasta entre looks distintos (pasó con 1.167 prompts).
     Trata el bloque como terminado al llegar a la próxima línea `**<Pose>:**`, al próximo
     heading `##`/`###`, o al fin del bloque del look — lo que ocurra primero.
 B6. `**Negative Prompt:** \`...\`` viene INLINE entre backticks simples, después de la última pose.
     Ese negativo aplica a LAS 7 POSES del look. Si el look no tiene Negative Prompt, no inventes
     uno: marca el look como incompleto y NO lo generes (generar sin negativo produce basura).

=====================================================================
C. EL SLUG — LA CAUSA DE TODOS LOS DUPLICADOS
=====================================================================
Cada look tiene UN solo slug canónico. El mismo string debe aparecer, carácter por carácter, en:
   - el nombre de la carpeta:   05_Imagenes/ele/look<N>_<slug>/
   - el campo Ubicacion
   - los links de la tabla 📸

C1. FUENTE DE VERDAD = el campo `Ubicacion`.
    La app DEBE leer la carpeta destino de ese campo. NO la derives del título.
    (Bug actual: la app deriva el slug del título e ignora Ubicacion; cuando ambos difieren
     crea una segunda carpeta para el mismo look. Así aparecieron 35 looks con carpeta duplicada
     y 380 poses que quedaron invisibles.)

C2. Solo si el campo `Ubicacion` NO existe, derivar el slug del TÍTULO con este algoritmo exacto:
      1. minúsculas
      2. plegar acentos a ASCII:  á→a  é→e  í→i  ó→o  ú→u  ü→u  ñ→n
      3. BORRAR guiones y apóstrofes (no convertirlos en "_"):  "Coat-Dress" → "coatdress"
      4. cualquier carácter que no sea [a-z0-9] → "_"; colapsar "__" repetidos; recortar los "_" de los bordes
      5. prefijar "look<N>_"
    Ejemplos de control (deben dar exactamente esto):
      "Jade Coat-Dress Boardroom" → look764_jade_coatdress_boardroom
      "Shanghai Qipao Líquido"    → look702_shanghai_qipao_liquido
      "Cherry Polka Dot Pin-Up"   → look610_cherry_polka_dot_pinup

C3. ANTES de crear una carpeta nueva, busca si YA EXISTE cualquier directorio que empiece con
    `look<N>_` (mismo número de look). Si existe, USA ESA. Nunca crees una segunda carpeta
    para un número de look que ya tiene una. Esta sola regla habría evitado los 35 duplicados.

C4. El slug es SIEMPRE ASCII. Ni un acento, ni una ñ, ni un espacio en el nombre de carpeta.

=====================================================================
D. NOMBRES DE ARCHIVO AL SUBIR
=====================================================================
D1. Formato:  ele_<N>_<pose>.png
D2. Los nombres de pose son EXACTAMENTE estos siete:
       standing · back_view · seated · side_profile · ditzy · pov · odalisque
    BUG ACTUAL: la app sube `ele_<N>_back.png` y `ele_<N>_profile.png`.
    Debe subir `back_view` y `side_profile`. Si no, la pose se mapea mal en la galería.
D3. Si ya existe un archivo con ese nombre exacto, NO lo sobrescribas en silencio:
    sube como `ele_<N>_<pose>__v2.png`. Nunca se pierde una imagen.
D4. Se aceptan archivos con sufijo de timestamp (`ele_313_pov_1783817471712.png`): son la
    misma pose, generada por API. Al contar, trata `ele_<N>_<pose>` con o sin sufijo como
    LA MISMA POSE (regex: ^ele_0*<N>_<pose>(_\d+)?\.png$).

=====================================================================
E. ACTUALIZAR EL CONTADOR (tracker)
=====================================================================
E1. Tras subir, regenera la sección del look:
    ### 📸 Imágenes (<n>/7 — Materializado)              <- si n == 7
    ### 📸 Imágenes (<n>/7 — Materializado parcial (app/Gemini))   <- si n < 7
    seguida de la tabla de 7 columnas, con [📸 View](../../<ruta real>) o "⏳ Pendiente".

E2. CUENTA LOS ARCHIVOS EN DISCO, no confíes en el número que ya estaba escrito.
    Bug real: el contador decía 0/7 en looks que tenían las 7 imágenes hace días.
    La Ama leía "0/7", mandaba a regenerar, y se quemaba cuota API en imágenes que ya existían.

E3. Los links de la tabla deben apuntar al archivo REAL (la carpeta que de verdad lo contiene).
    Si renombras o mueves una carpeta, hay que re-escribir los links: el conteo no cambia pero
    la ruta sí (esto dejó 49 links rotos).

=====================================================================
F. CATEGORÍA Y TAGS (para filtrar en la app)
=====================================================================
F1. La categoría sale del heading (entre paréntesis, separada por "·") o del campo `Categoria`.
    Lista CERRADA de 10 valores válidos:
       Stripper · Corporate · Escort · Domestic · Pin-Up
       High-Fashion Editorial · Nightclub · Lencería · Bikini · Gym
    Normaliza al leer:  "Lenceria" → "Lencería" ; "Gym/Athleisure" → "Gym" ;
                        "HF Editorial" → "High-Fashion Editorial".
    "Mix" NO es una categoría válida (hay ~104 looks con ese valor): trátalos como "sin categoría".
F2. Tags: línea `- **Tags:** #a #b #c`. Van en minúscula y sin tilde. El primero es la categoría.

=====================================================================
G. QUÉ ENTREGARME
=====================================================================
1. El parser corregido (función que dado el .md devuelve, por look:
   número, título, slug canónico, categoría normalizada, tags, los 7 prompts, el negative, y
   el estado real de materialización).
2. El uploader corregido (nombres de pose canónicos, reutilización de carpeta existente,
   sin sobrescritura silenciosa, y regeneración del tracker contando el disco).
3. Tests con estos casos de control:
   - Título con acento y guión: "Shanghai Qipao Líquido" y "Jade Coat-Dress Boardroom".
   - Clave del campo con y sin tilde: "**Ubicación:**" y "**Ubicacion:**".
   - Un look con fence mal formado: NO debe contaminar el look siguiente.
   - Un look sin Negative Prompt: NO debe generarse.
   - Un look con imágenes con sufijo timestamp: debe contarlas como materializadas.
   - Un look cuya carpeta ya existe con otro slug: debe reutilizarla, no crear una segunda.
```
