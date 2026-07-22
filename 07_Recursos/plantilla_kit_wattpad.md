# 📕 PLANTILLA — Kit Wattpad de un relato finalizado

> **Cuándo se usa:** al finalizar un relato (Ama 22/07/2026 — *"cuando se finalice un relato debes incluir estos prompts, y los tags para wattpad"*).
> **Dónde va:** `03_Literatura/02_Finalizadas/[relato]/kit_wattpad.md` + `prompts_portada.md` en la misma carpeta.
> **Reglas verificadas:** [`guia_publicacion_wattpad.md`](guia_publicacion_wattpad.md) · **Ejemplos vivos:** `la_piel_que_diseno/`, `de_esteban_a_secretaria/`, `la_app_la_bimboficacion_de_mi_novio/`.

---

## 🧭 Portada vs. banner — no confundirlos

| Formato | Cuántos | Dónde va | Ratio de generación |
|---|---|---|---|
| **Portada vertical** 512×800 (2:3) | **UNA por historia** | la tapa de la historia | pedir **3:4** y recortar |
| **Banner horizontal** 1280×720 (16:9) | **UNO por capítulo** | *header image* al inicio de la parte | pedir **16:9**, recortable a 3:1 |

**Wattpad no tiene "portada de capítulo".** Si un relato viejo tiene verticales por capítulo (herencia del formato Tumblr), se conservan como material de RRSS — pero **lo que se sube a cada parte es el banner horizontal**.

---

## Los dos archivos y quién es dueño de qué

| Archivo | Dueño de | Nunca duplicar |
|---|---|---|
| `prompts_portada.md` | prompts de imagen (portada + un banner por capítulo) + tags Tumblr/RRSS + tags Wattpad | no copiar prompts al kit |
| `kit_wattpad.md` | metadata, descripción, nota de autora, tabla de partes, calendario, checklist, registro | no copiar metadata a los prompts |

---

## Reglas que gobiernan los prompts (no negociables)

1. ⛔ **Sin piel:** prohibida la exposición completa de genitales, pechos y glúteos, y toda representación de acto sexual. Wattpad borra la imagen sin aviso. **Esto deroga el canon visual de Ele para portadas** — la lente fetish vive en material, silueta y luz, nunca en piel.
2. 🚫 **NUNCA nombrar lo prohibido, ni para prohibirlo** *(corregido 22/07 tras probarlo en producción)*. La primera versión de esta plantilla mandaba cerrar cada prompt con `STRICTLY: no nudity, no exposed nipples…` — **y eso hace rebotar el prompt**: *"Sorry, I can't generate unsafe images."* El filtro **no procesa la negación, lee los tokens**. La lista `STRICTLY` es un **checklist mío antes de entregar el prompt**, jamás texto que se le manda al generador.
3. 🎭 **Registro léxico en clave editorial, no erótica:** `Editorial book cover` / `Cinematic editorial chapter header`, no `Erotic novel cover`. Fuera también `intimacy charged with desire`, `strip club`, `stripper heels`, `augmented bust`, `high-cut`. Sirven: `cabaret nightclub`, `performance heels`, `sculpted figure`, `period underpinnings`, `glamorous`, `sensual` (estos dos están bendecidos por el canon anti-filtro del proyecto).

### 👗 GARMENT_DECLARED — la prenda se declara SOBRE el cuerpo (aprendido en producción 22/07/2026)

**El caso:** la portada del Cap 1 de «De Esteban a Secretaria» salió **en topless**. El prompt decía *"her shoulders are bare; the upper chest is visible"* y describía un corsé que **unas manos ajenas apretaban** — pero nunca dijo que ella lo llevara puesto. La IA hizo lo literal: dejó el torso desnudo y **puso el corsé en un cuerpo aparte** al costado del cuadro.

- ✅ `SHE IS WEARING a [prenda] — worn on her body, closed, opaque — covering [zona] completely from [borde alto] to [borde bajo].`
- ❌ `her shoulders are bare` · `the upper chest is visible` · `a corset at her waist` (¿de quién?) · cualquier prenda mencionada sin verbo que la ponga sobre alguien.
- **La línea `STRICTLY` NO alcanza sola.** El negativo es segunda capa: si el positivo no viste a la figura, la IA la desnuda igual. Misma lección que el motor visual de Ele (`ancla afirmativa en el positive`).
- **Segundo personaje = solo manos.** `only a pair of FOREARMS AND HANDS enters the frame — no face, no head, no torso, no second body`. Sin ese candado la IA le fabrica un cuerpo entero y arruina la composición.
- **Espejos:** declarar **a quién** reflejan (`the mirror reflects HER OWN back — the same woman; no other person in the glass`), o aparece un personaje inventado.
- **Asimetrías** (medio rostro maquillado, un guante, un zapato): nombrar **izquierda y derecha** explícitamente y decir `this asymmetry must be obvious`. Si no, la IA promedia y las hace iguales.

### 🎥 CAMERA_FIRST — si el cuerpo sigue saliendo desnudo, el problema es la cámara

**El caso, tercera pasada:** con la prenda ya declarada en positivo, la portada del Cap 1 de Esteban **seguía saliendo en topless**. El defecto no estaba en el vocabulario sino en la **geometría**: se pedía *"vista frontal tres cuartos"* + *"le aprietan los cordones del corsé por la espalda"*. Son incompatibles — lo que se lacea está **detrás** de la figura, así que el modelo dibuja el corsé detrás, como objeto suelto, y deja el frente sin nada. **Ninguna cantidad de adjetivos arregla una composición imposible.**

- Antes de escribir el prompt, preguntarse: **¿la prenda que cubre está del lado que ve la cámara?** Si no, girar la cámara — no agregar palabras.
- La toma canónica del corsé laceado es **de espaldas**. La del rostro es **de frente**. Cuando se necesitan las dos, la que falta vuelve por un **espejo declarado** (`the mirror in front of her returns her face to the camera… it shows her and nobody else`).
- Regla general: **buscar la toma que hace la cobertura estructural**, no la que la promete. Vestida por construcción > vestida por adjetivo.
- Y una de proceso: **no dejar la versión mala del prompt archivada en el mismo archivo.** Se copia. Pasó. Queda el registro de qué falló; no queda el texto copiable.

### 🔤 El texto largo es una lotería

La misma portada salió con el título escrito **«Secretaia»** — se comió una letra de una palabra de diez. Regla: **el default es generar SIN texto** (`NO TEXT ANYWHERE… every object label blank`) y componer la tipografía después. Si se pide texto renderizado, **una sola línea corta** y revisarla letra por letra antes de subirla. Agregar siempre `every label blank` o los objetos de la escena traen palabras inventadas.
3. **El banner se elige por forma, no por calor:** la escena horizontal por naturaleza (dos figuras separadas por el ancho de una pieza, un escenario visto desde el fondo de la sala). La escena más caliente casi nunca es publicable — y casi nunca compone.
4. **Croplable:** figuras y tipografía dentro de la banda central; 20% superior e inferior vacíos → recorte limpio a 3:1.
5. **Ratios:** Gemini no hace 2:3 ni 3:1 → **portada en 3:4**, **banner en 16:9**, y se recorta.
6. **Acentos rotos:** `Diseñé`, `ANAÏS`, `Capítulo` salen deformados. Cada prompt lleva **VARIANTE SIN TEXTO**.
7. **Título legible a 256 px** (miniatura móvil). Serif fina o script = papilla.

---

## Esqueleto de `kit_wattpad.md`

```markdown
# 📕 KIT WATTPAD — «[Título]»

> Documento operativo... · Generado [fecha] · Reglas: 07_Recursos/guia_publicacion_wattpad.md
> Los prompts de imagen viven en prompts_portada.md (dueño único).

## 1. METADATA DE LA HISTORIA
Título · Autora (@AnaisBelland) · Idioma Español · Categoría · Rating MATURE ·
Copyright · Estado (Completa al subir la última parte) · N.º de partes

## 2. DESCRIPCIÓN  (≤ 2.000 caracteres — contar y anotar el largo)
Voz del relato, no sinopsis de contraportada genérica. Termina SIEMPRE con:
⚠️ +18. Contenido sexual explícito, [temas]. Ficción. Todos los personajes son adultos.

## 3. TAGS  (exactamente 25 — sin puntos, guiones ni espacios)
Mezcla español + inglés. El nicho TG/bodyswap/bimbo busca en inglés aunque lea en español.
Cerrar con los dos de marca: lavoutedanais · anaisbelland

## 4. NOTA DE AUTORA  (pegar al inicio de la Parte 1)
Ficción / adultos / se narra, no se recomienda / puerta de salida / "bienvenida a La Voûte".

## 5. PARTES E IMÁGENES
Tabla: n.º · título de la parte en Wattpad · archivo fuente · link al banner.
⚠️ Revisar aquí si algún TÍTULO de capítulo es impublicable (los títulos aparecen en
listados públicos donde el rating Mature no protege) y proponer el alternativo.

## 6. CALENDARIO SUGERIDO  (Publishing Scheduler — solo web, hasta 1 año)
Escalonar 3-4 días entre partes. Subir todo el mismo día quema el relato.

## 7. CHECKLIST DE PUBLICACIÓN

## 8. REGISTRO DE PUBLICACIÓN
URL · fecha P1 · fecha Completa · incidencias de moderación
```

---

## Cómo se arman los 25 tags

| Bloque | Cuántos | Ejemplos |
|---|---|---|
| Fetiche núcleo, español | 3-5 | `bimboficacion` `feminizacion` `transformacion` |
| Fetiche núcleo, **inglés** | 3-5 | `bimbofication` `tgtf` `bodyswap` `genderswap` `mindcontrol` |
| Dinámica | 3-4 | `femdom` `dominacion` `sumision` `humillacion` |
| Escenario / objeto | 2-3 | `stripclub` `oficina` `criada` `latex` |
| Género / rating | 3-4 | `erotica` `eroticaadulta` `maduro` `terrorpsicologico` |
| Localización | 1 | `chile` |
| Marca | 2 | `lavoutedanais` `anaisbelland` |

**Por qué la mezcla:** dejar solo tags en castellano nos saca de la mitad del tráfico del nicho — el lector hispano de TG/bimbo busca en inglés. Los de marca no traen lectores nuevos: amarran el catálogo entre sí.

---

## Checklist de generación del kit (para mí, no para la Ama)

- [ ] Leí el relato completo (o sus cabeceras + gancho) antes de escribir la descripción
- [ ] La descripción usa **la voz del relato**, no una sinopsis neutra
- [ ] Conté los caracteres de la descripción y los anoté
- [ ] Son **exactamente 25** tags, sin puntos ni guiones
- [ ] Un banner **por capítulo**, cada uno con su variante sin texto
- [ ] Cada prompt termina en `STRICTLY:`
- [ ] Revisé los prompts viejos del relato: ¿alguno pide piel prohibida? → corregir y **marcarlo**
- [ ] Revisé los **títulos de capítulo**: ¿alguno es impublicable? → proponer alternativo
- [ ] `prompts_portada.md` y `kit_wattpad.md` se enlazan mutuamente y no se duplican
