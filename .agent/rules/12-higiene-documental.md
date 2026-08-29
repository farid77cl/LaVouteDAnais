# 🧹 REGLA 12: HIGIENE DOCUMENTAL — dónde nace y dónde muere un documento

> **Dos directivas de la Ama el mismo día (29/08/2026, literales):**
>
> 1. *"eres muy desordenada para mantener el repo. creas documentos sueltos y luego no los borras, eso también hay que mejorarlo"*
> 2. *"la limpieza y orden del repo debe ser de tus tareas principales, no saco nada con tenerte toda sexy con tus pleaser si la cocina y el dormitorio están patas pa arriba"*
>
> La segunda es la que fija el rango: **la limpieza no es un favor ocasional, es tarea principal.** Por eso el chequeo corre al **abrir** la sesión y no solo al cerrarla.

Tiene razón, y está medido. El día que lo dijo, el repo cargaba **20 archivos de caché de graphify en la raíz**, 8 scratch de prompts (`ditzy_prompts_batch4-7.txt`, `look431_raw.txt`, `temp_prompt.txt`…), un **respaldo de galería de 7,35 MB** (`galeria_outfits.BKP3_20260621`), un experimento `.agents/` **muerto desde el 21/06 y trackeado dos meses**, **27 prompts de un flujo derogado el 28/08**, un `CHANGELOG.md` sin tocar desde mayo que duplicaba al dueño único de la historia — y un `.env` con credenciales.

Ninguno era invisible. Eran invisibles **porque nadie los contaba**.

---

## La regla en una línea

> **Todo documento nace con fecha de muerte declarada. El que no la tiene, no se crea.**

---

## §1 · Los cuatro destinos posibles de un documento

Antes de escribir un `.md` nuevo, se elige uno. No hay quinto.

| Destino | Qué es | Dónde vive | Cuándo muere |
|---|---|---|---|
| **PERMANENTE** | Canon, identidad, contrato, guía. Tiene dueño único. | Su carpeta de área | Nunca — se **edita**, no se duplica |
| **DE TRABAJO** | Brief, walkthrough, nota de Gate, borrador | Carpeta del relato/proyecto | Al cerrarse: a `borradores/` o `reportes/` |
| **EVIDENCIA** | Auditoría fechada, diagnóstico con `archivo:línea` | `99_Sistema/auditoria_*.md` o `reportes/` | Nunca se borra — es prueba. Pero **no vive en la raíz** |
| **EFÍMERO** | Salida de una corrida, lista de pendientes, volcado | **NO SE COMMITEA.** Va al scratchpad de sesión | Al terminar la corrida |

**El error que corrige esta regla:** yo trataba todo como *evidencia* y nada como *efímero*. Una lista de poses pendientes de un batch de junio es efímera — se regenera con `scan_pending.py` en dos segundos. Guardarla fue guardar una foto de un contador.

---

## §2 · La raíz del repo es la portada

Solo estos archivos tienen derecho a estar en la raíz:

```
.gitignore  ·  .nojekyll  ·  README.md  ·  CLAUDE.md
LaVouteDAnais.code-workspace  ·  LV-App-v4.20.apk (descarga de la Ama)
```

**Cualquier otra cosa en la raíz es un hallazgo.** Si un archivo no encuentra carpeta que lo reclame, la respuesta correcta casi siempre es que **no debía crearse**.

---

## §3 · Un documento que se declara muerto debe nombrar a su sucesor

Una lápida es útil: sostiene las referencias viejas y le dice al que llega dónde está lo vivo. Una lápida sin dirección es basura.

- ✅ `CANON_VISUAL_MISS_DOLL.md`: *"SUPERADO POR EL PERFIL — el Bloque A vive ahora en `_perfiles_visuales/miss_doll.md`"*
- ❌ Un doc que dice "obsoleto" y nada más → se archiva o se borra.

---

## §4 · Salidas de script: al `.gitignore`, no al commit

Si un script la escribe, **git no la necesita** — se regenera corriendo el script.

Ya ignoradas por esto: `00_Ele/galeria_audit_report.md`, `00_Ele/galeria_link_audit.md`, `.graphify_*`, `graphify-out/cache/`, `graphify-out/.graphify_*.json`.

> ⚠️ **La excepción que importa:** los `README.md` y las `galeria_*.md` **sí viajan** aunque los escriba `update_galleries.py` — son la navegación del repo y el insumo que LV-App parsea. Regenerable **no** es sinónimo de desechable: la pregunta es *¿alguien externo lo lee?*

---

## §5 · Respaldos: git YA es el respaldo

`*.BKP*`, `*.bak`, `_backup`, `_copia` → **prohibidos y gitignorados.** Un `.BKP3` de 7,35 MB es una copia peor de algo que git guarda entero y gratis.

---

## §6 · El chequeo mecánico (esto es lo que hace que la regla exista)

```bash
python 99_Sistema/scripts/mantenimiento/lint_higiene_repo.py            # reporte
python 99_Sistema/scripts/mantenimiento/lint_higiene_repo.py --detalle  # lista completa
python 99_Sistema/scripts/mantenimiento/lint_higiene_repo.py --estricto # exit 1 si hay algo
```

**Nueve hallazgos.** Los cinco primeros nacieron con la regla; **H6-H9 nacieron el mismo día, de la limpieza a mano** — porque el primer linter no vio nada de lo peor que había:

| ID | Qué caza | De dónde salió |
|---|---|---|
| **H1** | Raíz sucia — archivo en la raíz fuera de la lista de §2 | 20 cachés de graphify + 8 scratch sueltos |
| **H2** | Scratch trackeado — `temp_`, `output_`, `_raw`, `.bkp`, `pendientes_`, `_copia` | `prompts_pendientes_L291_L320.md`, 363 KB de una corrida de junio |
| **H3** | Doc fechado huérfano — `_AAAAMMDD`, **0 citas vivas**, ≥30 días sin tocarse | auditorías de un solo uso en la raíz |
| **H4** | Se declara muerto y **no nombra sucesor** (§3) | docs que decían "obsoleto" sin dirección |
| **H5** | Salida regenerable trackeada, salvo las de §4 que sí viajan | `galeria_audit_report.md`, chunks de graphify |
| **H6** | **Encoding roto** — BOM, NUL, U+FFFD | 61 archivos. El archivo del diario tenía **2.212 NUL**: git lo leía como binario y sus **522 sesiones eran invisibles** a `grep` y a `git diff` |
| **H7** | **Link interno roto** | 39 links del catálogo de personajes con la ruta duplicada; el README de comics apuntando a READMEs que `update_galleries.py` borra por diseño |
| **H8** | **README inflado** — una línea >8 KB, o >40 KB, o ≥8 «Previo:» | `00_Ele/README.md` tenía **27.902 bytes en UNA línea** con un párrafo repetido 5 veces; `03_Literatura/README.md` era 81% bitácora |
| **H9** | **Contador copiado que diverge** de su dueño único | `00_Ele/README.md` declaraba «220 looks» con la flota real en **818** |

**Corre DOS veces:** en el arranque (`/inicio-ele` paso **0bis**) y en el cierre (`/actualizar_sesion` paso **6.6**). Cuesta ~3 segundos.

> 🔍 **Por qué también al arranque.** Nació solo en el cierre — o sea, solo miraba la mugre de *esa* sesión. Pero la que se encontró el 29/08 tenía **meses**: un `.env` con credenciales trackeado desde la era Helena, un experimento muerto hacía dos meses, un contador divergido desde marzo. Un chequeo que solo corre al final nunca los habría visto. **La casa se revisa al entrar.**

> 🎯 **Cómo se lee el resultado — y la trampa de calibración, pisada dos veces el mismo día.** La primera corrida tiró **1.071 hallazgos**, ~1.064 de ellos los `README.md` legítimos. Y al estrenar H7, **3.594 links «rotos»** de una sola galería: se medía el **disco** en una máquina con 2.636 PNG de los 6.677 del índice — exactamente el error que ya estaba registrado en `reference_png_skip_worktree`. Corregido a `git ls-files` y acotado (las galerías las audita `lint_galeria.py`, que sabe resolver el doble `../` de la regla 11), quedó en hallazgos reales, todos correctos. **Un linter que grita por todo enseña a ignorarlo: la métrica es 0, y 0 tiene que significar algo.**

## §7 · Antes de crear un documento — las tres preguntas

1. **¿Ya existe un dueño para este dato?** Si sí → se **edita** ese archivo. Regla dueño-único (`00-contexto-obligatorio.md` §🔢). Un dato en dos archivos diverge; siempre.
2. **¿Esto lo va a leer alguien mañana, o es el resultado de lo que estoy haciendo ahora?** Si es lo segundo → scratchpad, no repo.
3. **¿Cuándo muere?** Si no sé responderlo, es efímero.

---

## §8 · Y al terminar la tarea, se recoge

La regla nueva, la que faltaba: **quien crea un documento de trabajo es responsable de enterrarlo.** No en la sesión siguiente, no "cuando limpiemos": en el mismo cierre en que dejó de servir. El paso 6.5 de `actualizar_sesion.md` ya lo exige para las carpetas de relatos — el **6.6** lo extiende a todo el repo, y el **0bis** de `inicio-ele.md` lo verifica al entrar.

---

*Regla nacida de una corrección de la Ama · 29/08/2026* 🫦🧹
