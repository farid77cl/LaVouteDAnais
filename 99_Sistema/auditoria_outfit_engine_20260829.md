# 🔍 Auditoría del Outfit-Engine — 29/08/2026

> **Origen:** la Ama pidió retomar la auditoría de patrones repetidos que quedó detenida el 27-28/08 ("los errores y su fix"), y en medio de la sesión levantó: *"aún hay problemas con el renderizado de las batas"*.
>
> **Estado de la auditoría anterior:** **no dejó artefacto**. Cero archivo, cero commit. Se rehízo desde cero. Lo único que sobrevivía era la sospecha del falso positivo de `ASYMMETRY_LOCK`, anotada en memoria — confirmada aquí con evidencia (F-05).
>
> **Método:** GSD. `gsd-audit-fix` nativo **no corre en este repo** — busca sus hallazgos en `.planning/phases/*-UAT.md`, que no existe acá (se creó ayer en el repo de la app). Se aplicó el método (findings con ID → clasificación → fix atómico → commit trazable) sobre fuente propia: linter + auditorías visuales + correcciones de la Ama en auto-memoria.

---

## Tabla de hallazgos

| ID | Hallazgo | Sev | Estado | Commit |
|---|---|---|---|---|
| **F-01** | El ancla fuerte de bata/blazer vivía solo en el motor de Ele; el motor genérico no la conocía | 🔴 Alta | ✅ Arreglado | `3115d26` |
| **F-02** | 137 Back Views de prenda abierta sin ancla fuerte · 52 de riesgo vivo | 🔴 Alta | ✅ Arreglado (riesgo vivo) | `a7a0e7a` |
| **F-03** | `footwear_canon.py` y `garment_canon.py` nunca auditaron la flota | 🔴 Alta | ✅ Arreglado | `6462562` |
| **F-04** | La detección de anclas por prefijo de 45 chars da falsos negativos | 🟡 Media | 📋 Documentado, sin fix | — |
| **F-05** | `ASYMMETRY_LOCK` disparaba con el **pelo** de Miss Doll | 🔴 Alta | ✅ Arreglado | `a7a0e7a` |
| **F-06** | 635 violaciones de canon en la flota histórica de Ele | 🟠 Media-Alta | ⛔ **Ama 29/08: sin retrofit** | — |
| **F-07** | Al motor genérico le faltaban **todas** las anclas de material y prenda | 🔴 Alta | ✅ Arreglado | `76ebc39` |
| **F-08** | El BLOQUE A no tenía dueño único: cada script de batch lo copiaba a mano | 🔴 Alta | ✅ Arreglado | `3fa4367` |

---

## F-01 · El ancla de la bata nunca llegó al motor genérico

**Lo que reportó la Ama:** las batas siguen renderizando mal.

**Lo medido**, sobre las tres galerías, contando back-views de prenda de frente abierto (robe · kimono · peignoir · blazer · coat · tuxedo · bolero):

| | Back Views con prenda abierta | Ancla **fuerte** (`WRAP_BACK_*`) | Solo `BACK_ANCHOR` (una cláusula) | Sin nada |
|---|---|---|---|---|
| Ele | 117 | 49 | 45 | 23 |
| Miss Doll | 26 | **0** | 26 | 0 |
| Anaïs | 43 | **0** | 43 | 0 |
| **Total** | **186** | **49** | **114** | **23** |

**Causa raíz:** la cláusula larga (`WRAP_BACK_SLIP` / `_CLOSED` / `_TAILORED`, ~60 palabras que nombran solapas, costura central, vent, nuca y sash) vivía en `pose_rotation_v5.py` — el motor **viejo, de un solo personaje** — activada por un parámetro manual `wrap_mode`. La palabra `wrap_mode` **no aparecía ni una vez** en `prompt_builder.py`, el motor genérico que arma todo look nuevo desde el 12/08.

Los looks nuevos no estaban desnudos: llevaban la cláusula corta de `BACK_ANCHOR`. Pero una frase no alcanzó, y el dato de campo de la Ama manda sobre la tabla.

> Es el caso literal de `feedback_fix_en_un_personaje_no_es_fix`: un fix que vive en el motor de UN personaje no es un fix. El parche se aplicó a mano a las back-views de Ele el 02/08 y nunca se cableó.

**Fix:** `anclas_universales.json` pasa a ser dueño único de `WRAP_BACK_ROBE` y `WRAP_BACK_TAILORED`, declaradas opt-in; `prompt_builder.py` las dispara por BLOQUE B y las limita al slot `back_view` (`OPT_IN_SOLO_SLOT`), con desempate a favor de la estructurada cuando un look nombra las dos.

**Verificado:** entra en Back View y no en Standing, en los tres personajes; desempate correcto; sin disparo cuando no hay prenda abierta.

---

## F-02 · Retrofit al riesgo vivo

Alcance `--solo-sin-imagen`: solo poses sin archivo en `git ls-files`. Reescribir un prompt que ya tiene foto no cambia ninguna imagen — la métrica es el riesgo vivo, no el total de avisos (`feedback_ancla_nueva_va_al_riesgo_vivo`).

| | prompts | looks | detalle |
|---|---|---|---|
| Ele | 50 | 49 | 44 ROBE + 7 TAILORED + 3 ASYMMETRY |
| Miss Doll | 3 | 2 | |
| Anaïs | 26 | 13 | 14 DRESS_LEG + 13 ROBE + 1 ASYMMETRY |

**Bug encontrado antes de disparar:** `inyectar_anclas.py` no conocía `OPT_IN_SOLO_SLOT` y habría escrito el ancla de espalda en Standing y POV, donde su texto (*"seen from behind"*) contradice la pose. Filtro agregado — es la otra mitad de la regla que `build()` ya aplicaba.

**Verificado sobre el artefacto:** 72 anclas `WRAP_*` en las tres galerías, **las 72 en Back View, 0 fuera de slot**. Linter `CRÍTICOS 0`; avisos 28.590 → 28.138.

---

## F-03 · Los auditores que nunca auditaron

`CLAUDE.md` documentaba:

```
python 99_Sistema/scripts/visual/footwear_canon.py    # stiletto/Pleaser rule across looks
python 99_Sistema/scripts/visual/garment_canon.py     # garment-token consistency
```

**Medido: ninguno de los dos abre un archivo.** Cada uno es la función validadora más su self-test sobre seis casos escritos a mano (`L734`, `L737`, `L746`, `L791-negviejo`…). Su salida dice *"=== DEBEN saltar (bad) ==="* y *"Self-check: LIMPIO"* — se estaban probando a sí mismos y nadie leyó que los `L7xx` eran fixtures, no looks.

**Consecuencia concreta:** el 28/08 el Look 812 se materializó con un mule sin plataforma. `audit_footwear` detecta esa violación exacta — **en su propio self-test**. La pilló un ojo humano leyendo el markdown, porque al auditor nadie le pasó nunca el look.

**Fix:** `auditar_canon_flota.py`. No reimplementa el canon: parsea las tres galerías y le entrega los looks reales a esas mismas funciones.

Extrae el **segmento de outfit acotado** (entre el cierre del BLOQUE A y la primera ancla) en vez del prompt completo — deliberado: las anclas nombran `flats, block heels, wedges`, `bikini bottom`, `thong`, `bodysuit`, y pasarle el prompt entero al auditor le haría leer su propia defensa como si fuera la prenda (`feedback_clasificador_se_lee_a_si_mismo`, 203 falsos positivos en julio). Un look que no se puede acotar se marca **NO AUDITABLE** — nunca se audita a medias.

**Y en la primera corrida real saltó un bug del canon mismo:** `_has_any` comparaba **subcadenas**, así que el término `ugg` saltaba en decenas de looks de Ele — la palabra que lo disparaba era **`suggestion`**. Mismo riesgo latente en `clog`/clogged y `wedge`/wedged. Seis fixtures escritos a mano nunca contuvieron esa palabra; la flota real la tenía por todas partes.

> ⚠️ **Y el primer intento del fix corrompió:** con `\b` seco al final, `stocking` dejó de ver `stockings` y el self-check cayó de 4 casos detectados a 2 sin que ninguna regla de canon cambiara. Es `feedback_fix_que_hace_pasar_puede_corromper` en vivo — hay que leer los casos que **cambian de estado**, no el contador. Resuelto con sufijo plural opcional.

---

## F-04 · La detección de anclas por prefijo da falsos negativos

El linter y el inyector detectan presencia de un ancla por sus **primeros 45 caracteres**. En la flota hay anclas legítimas con **otro prefijo**: 57 back-views de Ele llevan `"...worn correctly facing forwards on the body and is never reversed"`, una redacción alterna que el criterio de 45 chars cuenta como ausente.

Efecto medido: mi primera pasada reportó 119 back-views desprotegidos en Ele; el número real era 68. **Un tercio del hallazgo era ruido.**

**Sin fix.** El criterio de 45 chars es también lo que impide duplicar anclas con cola distinta (2.617 casos en Ele). Cambiarlo requiere decidir una identidad de ancla estable, y eso es rediseño, no parche.

---

## F-06 · Lo que la flota real muestra ahora que hay quien la mire

| | looks auditados | violaciones | no auditables |
|---|---|---|---|
| **Ele** | 613 | **635** | 0 |
| Miss Doll | 35 | **0** | 30 |
| Anaïs | 15 | **0** | 50 |

Con alcance `--solo-sin-imagen` (lo que la app todavía va a generar): **40 violaciones en 29 looks, todas de Ele.**

Tipos más frecuentes en la flota completa: `PRENDA CON DRIFT` 167 · `ARQUETIPO CUBIERTO sin OPAQUE_LOCK` 137 · `MEDIAS CON COSTURA sin seam` 78 · `MULE` 78 · `MEDIAS + punta abierta` 61 · `SILUETA MATE-PRONE sin GLOSS_LOCK` 60 · `METALENGUAJE MULTI-TOMA` 36 · `ESTAMPADO ANIMAL sin candado` 15.

**Miss Doll y Anaïs salen en cero** — sus galerías se construyeron enteras con `prompt_builder.py`. Las 635 son deuda histórica de Ele, de los 613 looks escritos antes del motor v2.0.

**Decisión de la Ama:** las 40 de riesgo vivo se pueden barrer; las ~595 restantes viven en looks que **ya tienen foto**, y reescribirlas no cambia ninguna imagen. La convención del repo es retrofit-al-tocar.

**80 looks quedan no auditables** — su prompt no permite acotar el outfit con seguridad. Cobertura parcial declarada, no silenciada.

---

---

## F-07 · El motor genérico no tenía una sola ancla de material

**Orden de la Ama (29/08):** *"necesito que el outfit engine funcione bien, así que nada de retrofix por ahora"*. La auditoría gira: deja de mirar la flota vieja y mide **lo que el motor produce hoy**.

**Prueba de motor:** 105 prompts generados con `prompt_builder` — 3 personajes × 7 slots × 5 outfits diseñados para estresar el canon (bata · blazer · medias con costura · animal print · asimetría) — auditados contra `footwear_canon` y `garment_canon`.

**Resultado inicial: 84 de 105 con falla.**

**Causa:** el motor genérico nació con 30 anclas de **pose, encuadre, orientación y anatomía**, y **sin una sola de material o prenda**. Éstas vivían únicamente en `pose_rotation_v5.py`, el motor viejo de Ele:

| Ancla ausente | Defecto que dejaba pasar | Memoria |
|---|---|---|
| `OPAQUE_LOCK` | Gemini corta la prenda para mostrar ombligo/runas | `feedback_cortes_ropa_runas_ombligo` |
| `GLOSS_LOCK` | material mate pese al token `vinyl` | `feedback_material_mate_vs_fetish` |
| `HOSIERY_LOCK` | la media cambia de color/largo entre poses | `feedback_medias_calzado_reglas` |
| `ANIMAL_PRINT_LOCK` | el leopardo rinde como encaje genérico | bug L764 |
| `SEAM_FRONT` / `SEAM_BACK` | la raya de la media sale por delante | `feedback_media_raya_frontal` |

Los 130 looks de Miss Doll y Anaïs se construyeron **sin ninguna de las cinco**. Es el patrón de F-01 multiplicado por seis.

> ⚠️ **`CONSISTENCY_LOCK` NO faltaba** — está en el motor con otro nombre (`GARMENT_CONSISTENCY`, texto casi idéntico). Falso positivo de mi primera medición, que auditaba el BLOQUE B crudo en vez del prompt final.

**Fix:** las cinco al JSON como opt-in, cableadas en `prompt_builder`. Notas de diseño:

- **El vocabulario que las dispara no se copia:** se importa de `garment_canon` y `footwear_canon`, que son sus dueños.
- `ANIMAL_PRINT_LOCK` es la única ancla **paramétrica**: `build()` resuelve `{kind}` con la especie del BLOQUE B; un `{kind}` sin resolver lo caza `validar()`.
- `SEAM_FRONT`/`SEAM_BACK` son **pose-aware** (`OPT_IN_SOLO_SLOT` acepta conjuntos): frente liso en los slots frontales, costura visible en `back_view`, y **Side Profile sin ninguna** — de perfil la raya trasera cae en el borde posterior, que es lo correcto.
- `SEAM_*` exige **dos** condiciones (costura **y** hosiery): *"centre-back seam"* también lo dice un blazer — lo dice mi propia ancla `WRAP_BACK_TAILORED` — y sin el segundo filtro la costura de la chaqueta activaba el candado de la media.

**Resultado: 105 prompts, 3 con falla** — las tres el mismo Side Profile del caso "medias", **limpio por canon** (el auditor no conoce el slot desde el que se generó, así que no puede saber que ahí no va ancla).

---

## Estado del motor al cierre

| | antes | después |
|---|---|---|
| Prompts de prueba con falla | **84 / 105** | **3 / 105** (y los 3 son correctos) |
| Anclas del motor genérico | 30 | **36** |
| Candados de material | **0** | 6 |

Self-checks de `footwear_canon` y `garment_canon`: **LIMPIO**. Linter: **CRÍTICOS 0**.

---

## Pendiente

- [x] ~~Barrer las 40 violaciones de riesgo vivo~~ — **la Ama ordenó no hacer retrofit (29/08)**.
- [x] ~~El BLOQUE A no tiene dueño único mecánico~~ — **resuelto, F-08 (ver abajo)**.
- [ ] Subir la cobertura del auditor de flota: 80 looks no auditables por formato de prompt.
- [ ] F-04: identidad estable de ancla (rediseño, no parche).
- [ ] Deuda declarada, **sin tocar por orden de la Ama:** la flota vieja de Ele no lleva los candados nuevos.

---

## F-08 · El BLOQUE A pasa a tener dueño único — y lo lee el motor

**Orden de la Ama (29/08):** *"El BLOQUE A no tiene dueño único. Eso soluciónalo"*.

**Lo medido antes de tocar nada:**

| | Dónde vivía su ADN | Estado |
|---|---|---|
| **Ele** | fence en el perfil + `dna_v3_5.md` + cada script | las 3 copias **idénticas** ✅ |
| **Miss Doll** | fence en el perfil, **con una nota en castellano incrustada a media cláusula** | los scripts la omitían a mano |
| **Anaïs** | **sin token literal en el perfil** — solo la spec en prosa y una instrucción de ir a copiarlo a `dna_v2_3.md` | nada verificaba la copia |

> ✅ **El ADN todavía no había divergido.** Las tres copias coincidían carácter por carácter. El riesgo era **estructural, no consumado** — se cierra antes de que costara una cara.

**Fix:**

- **Dueño único = el perfil visual §2**, que `CLAUDE.md` ya declaraba dueño. El ADN va en un fence marcado `<!-- ADN:BLOQUE_A -->` — comentario HTML: invisible al leer el `.md`, inequívoco al parsearlo. *Buscar "el §2" o "el fence más largo" es adivinar, y adivinar sobre el ADN es justo lo que esto viene a terminar.*
- **Anaïs:** token literal insertado, traído de `dna_v2_3.md` y **verificado idéntico al que usan sus batches antes de escribirlo**.
- **Miss Doll:** la nota en castellano sale del fence a la zona de notas.
- **`PromptBuilder.bloque_a` LEE el perfil** — no lo copia: duplicarlo en el JSON habría creado el segundo dueño que este fix elimina. Y **rechaza** un fence que traiga marcadores de nota en castellano.
- `build(bloque_a=None)` usa el del perfil. Los batches ya no necesitan hardcodearlo.
- `dna_v3_5.md` y `dna_v2_3.md` quedan como **punteros**.
- **Verificador nuevo `prompt_builder.py --adn`:** cruza el perfil contra cada script de batch y contra la galería. Es lo que impide que vuelva a divergir en silencio.

**Verificado:** `--adn` **LIMPIO**, ninguna copia diverge (Ele 4.291 prompts de galería abren con su ADN · Miss Doll 490 · Anaïs 98). Los tres personajes construyen con `bloque_a=None` y **0 fallas**.
