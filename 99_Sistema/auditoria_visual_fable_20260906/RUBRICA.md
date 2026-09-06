# RÚBRICA — Auditoría visual Fable · imagen ↔ prompt · 06/09/2026

Documento de criterio único para las 10 bandas de la auditoría. **Nace con fecha de muerte
declarada:** es evidencia fechada, vive en esta carpeta junto a los reportes que produce y no
se mueve a la raíz ni se duplica.

Encargo de la Ama (06/09/2026), literal:
> *"1.- se audite la imagen contra el prompt, qué porcentaje de desvío tiene la imagen del prompt
> 2.- que dentro del mismo outfit mantener continuidad, qué porcentaje hay. Me explico, si en la
> primera pose el vestido es hasta la rodilla, en el resto de poses debe ser el mismo largo"*

El eje 3 del encargo (anti-repetición de color y atuendo) **NO se audita aquí**: es texto, tiene
ejecutor determinista (`outfit.py cruce`, tope de familia cromática, `rotacion_prenda`) y lo corre
la orquestadora. Esta rúbrica cubre solo lo que exige mirar el píxel.

---

## 0. Reglas de método (no negociables)

1. **Se verifica el artefacto, nunca el reporte.** Cada incumplimiento se afirma citando lo que se
   ve en la imagen Y la cláusula del prompt que se rompe, textual. Sin las dos mitades, no es un
   hallazgo: es una impresión.
2. **Solo se cuenta lo VERIFICABLE en esa pose.** Si la toma es un POV de torso, el calzado no es
   evaluable — no cuenta ni a favor ni en contra. El denominador es lo que la imagen puede mostrar.
3. **Resolución medida: 0,80 MP (669×1200) en toda la ventana.** Está sobre el piso de validez
   (~0,3 MP), así que el defecto fino (punta del zapato, costura, piercing bajo tela) SÍ es
   auditable. No se acepta "no se ve" sin decir por qué.
4. **Las imágenes commiteadas son las SOBREVIVIENTES de los reintentos de la Ama.** Un defecto que
   aparece en lo guardado es un defecto real y probablemente más frecuente de lo que se ve.
5. **No se edita NADA.** Ni galerías, ni perfiles, ni prompts. Esta auditoría solo escribe su
   propio reporte de banda.
6. Si un look tiene 1 o 2 poses materializadas, el Eje 2 **no es medible** — se declara
   `NO MEDIBLE (n poses)`, no se inventa un porcentaje.

---

## 1. Dónde está cada cosa

| Muñeca | Galería (prompts) | Carpeta de imágenes | Slot 5 |
|---|---|---|---|
| Ele | `00_Ele/galeria_outfits.md` | `05_Imagenes/ele/look<N>_<slug>/ele_<N>_<pose>.png` | `ditzy` |
| Miss Doll | `02_Personajes/01_Principales/miss_doll/GALERIA_OUTFITS_MISS_DOLL.md` | `05_Imagenes/miss_doll/look<N>_<slug>/miss_doll_<NNN>_<pose>.png` | `glacial_command` |
| Anaïs | `02_Personajes/01_Principales/anais/galeria_looks_anais.md` | `05_Imagenes/anais/look<N>_<slug>/anais_<NNN>_<pose>.png` | `sovereign_gaze` |

Taxonomía de 7 poses: `standing · back_view · seated · side_profile · <slot5> · pov · odalisque`.

Cada look en la galería trae su **BLOQUE B** (el outfit, una línea o un bloque `text`) y los **7
prompts completos**, uno por pose, en bloques ` ```text `. El prompt de la pose es la fuente; el
BLOQUE B es el contrato de vestuario que las 7 deben respetar idéntico.

Canon de apoyo (leer solo lo que haga falta para juzgar):
- `02_Personajes/_perfiles_visuales/<slug>.md` — §2 BLOQUE A (ADN físico) y §5 (reglas BLOQUE B,
  calzado, prohibiciones absolutas).
- `.agent/rules/04-estetica-ele.md` — canon de calzado, reglas medias+calzado, y los 6 desvíos
  sistemáticos prompt→imagen ya documentados (costura de media, prenda cortada, anti-mate,
  consistencia de prenda, mueble equivocado en Seated).

---

## 2. EJE 1 — Desvío imagen ↔ prompt (%)

Para **cada pose**, construir la lista de afirmaciones verificables del prompt y marcarlas
`CUMPLE / FALLA / NO VERIFICABLE`. Agrupar en seis familias:

| # | Familia | Qué se chequea |
|---|---|---|
| A | **ADN / BLOQUE A** | iris (color exacto), pelo (color y largo), uñas (forma y largo), labios, busto (forma esférica exigida, no orgánica), piercings, tatuaje |
| B | **Prenda** | arquitectura, color, material y acabado (brillo vs mate), escote, largo de manga, ruedo/largo, cierre y estructura |
| C | **Calzado** | tipo, altura de taco, plataforma sí/no y altura, punta abierta/cerrada, color (plataforma = mismo color del zapato), correa |
| D | **Medias y accesorios** | medias (tipo, color, costura y su ORIENTACIÓN), choker/collar, guantes, joyas, cinturón |
| E | **Pose y encuadre** | lo que el slot exige: de pie / de espaldas / sentada de verdad en el asiento nombrado / perfil / mirada a lente o desviada / una sola mano en POV / reclinada |
| F | **Setting** | escenario, mobiliario, iluminación nombrada |

**Desvío de la pose = FALLA / (CUMPLE + FALLA) × 100.** Los `NO VERIFICABLE` quedan fuera del
denominador y se declaran aparte.

**Desvío del look** = promedio simple de las poses materializadas.

Cada FALLA se escribe así, en una línea:
`[familia] lo que pedía el prompt (cita textual corta) → lo que muestra la imagen`

**Marcar aparte, porque cambia la acción:**
- 🔴 **FALLA CON ANCLA PRESENTE** — el prompt traía el candado explícito (`GARMENT_CONSISTENCY`,
  `SEATED_ANCHOR`, `GLOSS_LOCK`, `OPAQUE_LOCK`, `CORSET_BUST_LOCK`, `FABRIC_PRISTINE`, cola `:1.4`)
  y aun así falló. Directiva de la Ama: *"si las anclas estaban y se generaron imágenes malas hay
  que reforzar el ancla"* — no se acepta "lotería de Gemini" como causa.
- 🟡 **FALLA SIN ANCLA** — el prompt nunca lo fijó. El defecto es del texto, no del generador.

---

## 3. EJE 2 — Continuidad dentro del mismo outfit (%)

La Ama lo definió exacto: *"si en la primera pose el vestido es hasta la rodilla, en el resto de
poses debe ser el mismo largo"*. **La referencia es la pose Standing** (o la primera materializada
si Standing no existe). No se juzga contra el prompt aquí: se juzga **imagen contra imagen**.

Atributos a seguir a través de las 7 poses (los que la toma permita ver):

| Grupo | Atributos |
|---|---|
| Prenda | color · material y brillo · escote · largo de manga · ruedo/largo · cierre/estructura · opacidad (qué es sheer y dónde) |
| Calzado | modelo · altura de taco · plataforma · color · correa |
| Piernas | medias sí/no · color · costura y orientación |
| Accesorios fijos | choker/collar · guantes · joyas · cinturón |
| ADN | color de iris · color y largo de pelo · uñas |

**Continuidad del look = atributos estables / atributos evaluables × 100.**
Un atributo cuenta como evaluable si es visible en **≥2 poses**.

Cada quiebre se escribe así:
`[atributo] Standing: <lo que muestra> → <pose>: <lo que muestra>`

Ojo con los dos patrones que este repo ya tiene documentados y que hay que buscar activamente:
- **Manga y escote reinventados** pose a pose cuando el BLOQUE B no los fija (familia de defecto
  del L746/L707/L86/L87).
- **Costura de media pintada por delante** en tomas frontales (relativa a cámara, no al cuerpo).

---

## 4. Formato del reporte de banda

Archivo: `99_Sistema/auditoria_visual_fable_20260906/bandas/<BANDA>.md`

```
# Banda <BANDA> — <muñeca> <rango de looks>
Auditadas N imágenes en M looks · 06/09/2026

## Resumen
| Look | Poses | Desvío prompt | Continuidad | 🔴 con ancla | 🟡 sin ancla |
(una fila por look, más una fila PROMEDIO)

## Look <N> — <título>
- **Desvío:** X% (detalle por pose)
- **Continuidad:** Y%  (o NO MEDIBLE (n poses))
- **Fallas:**
  - 🔴 [C] el prompt pedía "…" → la imagen muestra …
  - 🟡 [B] …
- **Quiebres de continuidad:**
  - [ruedo] Standing: hasta la rodilla → Seated: a media pantorrilla
- **Lo que salió BIEN y conviene no romper:** (1-3 líneas)

## Patrones de la banda
Lo que se repite en varios looks — que es lo que vale para arreglar el motor, no el caso suelto.
```

Cerrar la respuesta con una sola línea:

`FABLE_AUDIT_RESULT:{"banda":"…","looks":N,"imagenes":N,"desvio_promedio":X.X,"continuidad_promedio":Y.Y,"criticos_con_ancla":N,"reporte":"ruta"}`
