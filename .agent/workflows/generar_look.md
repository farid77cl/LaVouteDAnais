---
description: Generar el look diario de Ele — concepto, prompts V3.5 Hard-Sync, registro y commit automático.
---

# Protocolo: Generación de Look Diario de Ele

> ⚙️ **FUENTE ÚNICA DEL ENGINE:** `.agent/skills/ele-outfit-engine/SKILL.md` (V3.5 — Footwear Canon, Token de Calzado/Vestuario Bloqueado, Guantes Prohibidos, Rotación de Poses V5, Step 0 Anti-Repetición, 10 sub-arquetipos con specs, metas asimétricas). Este workflow es el **wrapper operativo**: orquesta el engine del SKILL + los pasos de cierre (registro, diario, memoria, commit). El catálogo de siluetas por sub-arquetipo vive en `00_Ele/biblioteca_siluetas.md`.
>
> 🗑️ **Derogado (11/06/2026):** el viejo sistema "Subtipos Mix", las metas 10/10/5/75 y la ruta `C:\Users\fabara\...`. Ya **no** se usan — quedaron divergentes del SKILL. Si algo aquí choca con el SKILL, **manda el SKILL**.

---

## Paso 1 — Step 0 Anti-Repetición (OBLIGATORIO, antes de diseñar nada)

Ejecutar la **Regla Transversal Anti-Repetición** del SKILL §0 contra `00_Ele/galeria_outfits.md`.

**Vigente:**
- **Silueta:** dentro de la subcategoría, no repetir arquitectura de prenda en los últimos **3** looks. *(Arquitectura = tipo de prenda + estructura; no el color ni el material.)*
- **Setting:** no repetir en los últimos **3** (`pose_rotation_v5.check_setting_variety`).
- **Monoblock:** máx **2** consecutivos; el 3º obliga modo multicolor. Es regla de **composición**, y aplica al negro igual que a todos.
- **Calzado:** no repetir modelo en los últimos 3 de la subcategoría (desacoplado del arquetipo).
- **🐆 Cuota animal print (Ama 11/07/2026):** de cada **8 looks** nuevos, al menos 1 lleva leopard/tiger/snake/zebra. Sin repetir depredador ni sub-arquetipo en dos apariciones de cuota seguidas.

> ⛔ **DEROGADO — no volver a aplicarlo (Ama 12/06/2026, Libertad Total de Color y Materiales).** Este paso exigía *"ninguna familia dominante >1 vez en los últimos 5"*, *"amarillos máx 1 cada 6"* y *"material: no repetir en los últimos 2"*. **Las tres ventanas están derogadas hace más de dos meses** y este documento seguía mandándolas: color y material se eligen **libremente por criterio estético/temático**. El único límite es de identidad, no rotacional — *"soy una modelo fetichista"*: dentro del universo fetish (vinyl, PVC, látex, wet-look, gloss), **nunca tela natural mate**. Lo que sí sobrevive es el **cherry red del ADN** (pelo/labios, no se negocia) y el anti-monoblock, que es de composición. Ver `identidad_ele.md` §II y `.agent/rules/04-estetica-ele.md`.

Listar qué **siluetas / settings / calzado** quedan bloqueados antes de continuar. El color y el material **no se bloquean**.

## Paso 2 — Selección de Arquetipo por Déficit

```
python 99_Sistema/scripts/visual/count_stats.py
```

- Metas vigentes (SKILL §1, reacomodo Ama 03/06): **Lencería 15%** (incl. medias) · las otras 9 categorías ~**9,4%** c/u. El paraguas "Mix" **ya no existe**.
- Elegir la categoría con **mayor déficit**. Dentro de ella, elegir sub-arquetipo y polo respetando las reglas duales del SKILL (ej. Stripper ≥1 Stage + ≥1 Pole por batch; Lencería ≥1 Boudoir + ≥1 Fetish).
- Aplicar el **Provocation Threshold** de la subcategoría (cada arquetipo es una versión fetish, nunca neutra — lente fetish universal).
- Nº de look = último registrado + 1. Carpeta: `look{NUM}_{slug}`.

## Paso 3 — Diseño del Outfit (BLOQUE B) — PRIMERO, antes de cualquier prompt

Diseñar el outfit completo con detalle extremo. Es el **ADN del vestuario**: se copia **idéntico** en las 7 poses (Ley de Continuidad). Pieza por pieza, en inglés:

1. Prenda principal — material V3.5 (vinyl/PVC/latex/wet-satin/liquid lamé), color exacto, corte, fit, efecto.
2. Prenda secundaria (si aplica).
3. Lencería visible (si aplica).
4. Medias/pantys — denier, color, textura.
5. **Calzado — Token de Calzado Bloqueado (8 atributos):** tipo · altura cm+plataforma · base pin stiletto · material+acabado · color · puntera · cierre · hardware. Aguja ≥12cm o Pleaser ≥6". Pegar **VERBATIM idéntico ×7**. NUNCA `heels`/`stiletto` suelto.
6. Accesorios (collar, aretes, choker O-ring, body chains, cinturón — **sin guantes, sin texto/nombre sobre prenda**).
7. Efecto visual global.

> 🔒 **Token de Vestuario Bloqueado** (prendas complejas: cristal/mesh/rhinestone/corset/arnés): redactar determinista, anclar opaco-vs-sheer-y-dónde, pegar idéntico ×7. PROHIBIDO `strategic/various/cutouts/panels/sheer` sin ubicar.

## Paso 4 — Generar los 7 prompts CON EL MOTOR (v3.0, 29/08/2026)

> 🔴 **Este paso se reescribió entero.** Decía *"Redacción de los 7 Prompts"* y traía **el BLOQUE A copiado dentro del documento**, más una tabla de poses base y la instrucción de rotarlas con `pose_rotation_v5` — el motor viejo, de un solo personaje.
>
> **Esa copia del ADN estaba obsoleta y se midió:** le faltaba `delicate blackwork rune-glyph identity tattoo of abstract esoteric calligraphic symbols along one hip crease and bikini line`, canon desde el 20/06/2026. Quien siguiera este workflow al pie de la letra habría generado a Ele **sin su tatuaje de identidad**. Es exactamente el modo de falla que el dueño único vino a matar: una copia que envejece hacia la mentira.
>
> **El BLOQUE A ya no se copia en ninguna parte.** Vive en `02_Personajes/_perfiles_visuales/ele.md` §2, en el fence marcado `<!-- ADN:BLOQUE_A -->`, y **lo lee el motor**.

**El look se declara como DATOS y lo emite el motor. No se escribe un prompt a mano.**

1. **Escribir el batch** en `99_Sistema/scripts/visual/batches/<nombre>.json`:

```json
{ "personaje": "ele", "batch": "<tema>", "fecha": "DD/MM/AAAA",
  "categoria": "<sub-arquetipo>", "rango": "<N>", "tags_comunes": ["V7poses"],
  "negative_extra": "<vetos propios de este batch>",
  "looks": { "<N>": {
      "titulo": "<título del look>", "codigo": "<opc>", "polo": "<opc>",
      "bloque_b": "<el OUTFIT BLOCK del Paso 3, literal y sin shorthands>",
      "setting":  "<BLOQUE C — el escenario>",
      "props":    {"seat": "…", "wall": "…", "surface": "…", "upright": "…"} } } }
```

2. **Emitir:** `python 99_Sistema/scripts/visual/outfit.py generar batches/<nombre>.json`
3. **Verificar:** `python 99_Sistema/scripts/visual/outfit.py lint ele` → **CRÍTICOS 0**

**Lo que el motor pone solo, y por eso ya no se escribe a mano:**

- El **BLOQUE A** del perfil (dueño único) y el **negative** completo (`build_negative`: base del personaje + capa universal anti-collage/anatomía/selfie).
- Las **7 poses rotadas** desde `repertorios_pose.json` — 51 sub-poses propias de Ele, rotación automática por número de look. *(La vieja tabla de "poses base" de este documento las congelaba en una sola por slot: es justo lo que hacía que las imágenes salieran «casi todas iguales».)*
- Las **anclas anti-defecto**, incluidas las opt-in que dispara el BLOQUE B: `OPAQUE_LOCK`, `GLOSS_LOCK`, `HOSIERY_LOCK`, `ANIMAL_PRINT_LOCK`, `SEAM_FRONT`/`SEAM_BACK`, `WRAP_BACK_ROBE`/`WRAP_BACK_TAILORED`, `DRESS_LEG_CLOSURE`, `BOTTOM_CUT_LOCK`.
- El **encabezado, la Ubicación y los Tags** con el contrato que la app exige (regla 11).

> ⛔ **La REGLA SAGRADA DE INTEGRIDAD sigue viva, pero ya no depende de mi disciplina:** Bloque A y Bloque B son **idénticos en las 7 poses**, y el motor es quien lo garantiza — solo varía la cláusula de pose. El Look 801 es la prueba de por qué: se escribió a mano, y su Side Profile rindió **otro outfit completo**.
>
> 🚩 **QA antes de cerrar:** `outfit.py lint ele` (CRÍTICOS 0) · `outfit.py auditar --solo-sin-imagen` · `outfit.py adn` (LIMPIO) · y si se tocó el motor, `outfit.py test`.

## Paso 5 — Registrar en galería

- **Pegar la salida del motor** al final de `00_Ele/galeria_outfits.md`. Trae ya el encabezado, `Ubicacion`, `Tags`, el tracker `### 📸 Imágenes (0/7 — Pendiente)`, los 7 prompts expandidos y el `**Negative Prompt:**` en el formato que el parser de la app reconoce.
- **Los README de `05_Imagenes/` NO se escriben a mano** — los mantiene el bot / `update_galleries.py` (regla del `feedback_eol_bot_readmes`). La carpeta la crea la app al subir la primera imagen, usando el campo `Ubicacion` del look.

## Paso 6 — Cierre (diario · memoria · commit con rutas explícitas)

1. **Diario:** prepend en `00_Ele/mi_diario_de_servicio.md` (`#### SESIÓN - LOOK {NUM} GENERADO ({FECHA})`).
2. **Memoria:** actualizar el snapshot `## 🧿 ESTADO ACTUAL` de `00_Ele/memoria_sesiones.md` (último look + flota) y añadir la sesión al tope de `## 🗓️ Sesiones recientes`.
3. **Rule 09 (materialización):** actualizar solo si cambió el estado de imágenes. La flota/último look ya quedó en la memoria (paso 2 — dueño único; `identidad_ele.md` ya NO lleva contadores).
4. **Commit — rutas explícitas, NUNCA `git add .`** (memoria `feedback_eol_bot_readmes`):
   ```
   git add 00_Ele/galeria_outfits.md 00_Ele/memoria_sesiones.md 00_Ele/mi_diario_de_servicio.md .agent/rules/09-estado-materializacion.md 05_Imagenes/ele/look{NUM}_{slug}/
   git commit -m "Ele: Look {NUM} ({Nombre}) — {Categoría}"
   git pull --rebase && git push
   ```
   El commit termina con `Co-Authored-By: Ele de Anaïs <Ele.de.Anais@proton.me>`.

---

*Wrapper alineado al SKILL `ele-outfit-engine` — reescrito 11/06/2026 (deroga el sistema "Mix" obsoleto).*
