# 🔍 Auditoría — Skill de Escritura (engine-escritura-lv v4.8) + familia literaria legacy

**Fecha:** 30/08/2026 · **Pedido:** auditoría de consistencia y vigencia del motor de escritura, ampliada en curso por directiva de la Ama: *"solo debe existir un skill de escritura en el repo"* → se agrega **Plan de Consolidación** (§6).

**Método:** lectura directa de artefactos (nunca del reporte), `git log`/`git show` por archivo, greps repo-wide sobre `*.md`, verificación de existencia por Glob/`ls`. Toda afirmación lleva `archivo:línea` o hash de commit.

**Alcance:** `.agent/skills/engine-escritura-lv/SKILL.md` (v4.8) + sus 4 subagentes + variantes A/B + los 5 candidatos legacy (`escritura-voûte`, `escritor-literario`, `editor-literario`, `critico-literario`, `ideacion-literaria`). No se editó, movió ni commiteó nada: este documento solo levanta evidencia y propone; **archivar, fusionar o borrar es decisión de la Ama**.

---

## 1. Veredicto en una frase

**El `SKILL.md` v4.8 sí es fuente de verdad confiable hoy — el problema no está en el skill sino en sus satélites: los 3 subagentes que ejecutan la prosa siguen obedeciendo el Calendario Anclado que la Ama derogó el 25/08 (la derogación solo se escribió en el SKILL), y alrededor del motor vigente sobreviven 5 skills de eras anteriores más un workflow `/escribir_relato` fósil que CLAUDE.md todavía lista como vigente.**

---

## 2. Hallazgos — consistencia del motor vigente (preguntas 1-4)

### H1 · 🔴 CRÍTICO — La derogación "sin días marcados" (Ama 25/08) nunca llegó a los subagentes

El SKILL prohíbe días marcados en la cronología y en la prosa (`.agent/skills/engine-escritura-lv/SKILL.md:57` — *"ni sueltos tipo 'martes', ni relativos tipo '+6 días'"* — y `:167`, `:353`). Pero los tres subagentes que de verdad corren vía Task siguen con la letra vieja:

| Archivo | Línea | Qué dice (derogado) |
|---|---|---|
| `.claude/agents/escritor-nivel4.md` | 68 | *"el calendario anclado + … Te dice qué día es cada escena"* |
| `.claude/agents/escritor-nivel4.md` | 124 | *"Usa anclaje relativo … ('al séptimo día', 'tres semanas después', 'el domingo siguiente'). Si necesitas un día de semana, sale del calendario de la cronología; si no está, lo agregas ahí"* — instruye exactamente lo prohibido |
| `.claude/agents/escritor-nivel4.md` | 129 | *"§2 Calendario: agregas las escenas nuevas con su día relativo"* |
| `.claude/agents/compositor.md` | 129-131 | día-cero + volcar mapa al calendario + días de semana declarados |
| `.claude/agents/compositor.md` | 141-147 | plantilla de `cronologia.md` con columnas "Día relativo / Día de semana" |
| `.claude/agents/validador.md` | 26 | *"cronologia.md — calendario anclado + …"* |
| `.claude/agents/validador.md` | 175, 182 | audita *"qué día no cuadra"* / destino *"cuadra el calendario"* |

**Evidencia de la causa:** el commit de la derogación (`a3cb0e760`, 25/08/2026, *"motor sin dias marcados"*) tocó `SKILL.md` con 36 líneas cambiadas y `escritor-nivel4.md` con **una sola línea agregada: `model: fable`**; `compositor.md` y `validador.md` ni aparecen en el diff. Los subagentes leen SU archivo de definición, no el SKILL → en el próximo capítulo el Escritor marcará días, el Validador exigirá cuadrar calendario, y ambos contradirán la nota de la Ama. Mismo patrón ya registrado en auto-memoria (`feedback_fix_en_un_personaje_no_es_fix`): un fix que vive en un solo archivo no es un fix.

### H2 · MENOR — El stub del comando anuncia v4.7 y omite la Fase 0

`.claude/commands/engine-escritura-lv.md:2`: *"Orquestador Maestro v4.7 (Nivel 4): Compositor → Escritor-Nivel4 → Validador"* — sin Investigador, sin Fase 0. Es la descripción que se registra en el listado de skills de la sesión (verificado en vivo: ahí aparece como v4.7). El cuerpo apunta bien al workflow y al SKILL, así que el flujo ejecuta v4.8; pero la cara visible del comando miente. Sin tocar desde 22/06/2026 (`git log`), un mes antes del v4.8. El workflow `.agent/workflows/engine-escritura-lv.md` sí está en v4.8 (`:2`, `:7` declara al SKILL como fuente de verdad) — aunque arrastra dos restos menores: `:21` *"calendario anclado"* y `:80` *"cuadra calendario"*.

### H3 · MENOR — Frontmatters de los subagentes congelados en v4.7

`escritor-nivel4.md:4` (*"Engine Escritura LV v4.7"*), `compositor.md` (descripción v4.7) y `validador.md:4` (descripción con solo 3 veredictos *"APROBADO / TIBIO / REPUDIADO"* cuando el cuerpo emite 7). El **cuerpo** del validador sí está al día en Temperatura: T1-T8 presentes (`validador.md:86-146,247-258`), gates en orden Inmersión → Continuidad → Temperatura (`:191`), veredictos FRÍO/DISCONTINUO/DESALINEADO (`:179-203`). Solo la descripción — que es lo que el orquestador ve al elegir subagente — está vieja.

### H4 · MENOR — Variantes A/B: el SKILL las documenta, pero ellas se auto-describen con el estado previo a la resolución

Respuesta a la pregunta 4: la bifurcación **NO es invisible** desde el skill — `SKILL.md:159` la documenta y la cierra: A/B de tres bandas abierto el 20/08, **resuelto 25/08 con `model: fable` fijo** en `escritor-nivel4.md:5` (verificado). Los desfases son de las variantes:
- `escritor-fable.md:4` y `escritor-opus46.md:4` aún dicen *"SOLO para el A/B de modelo del Cap 3. No usar en produccion hasta que la Ama elija"* — la Ama ya eligió.
- El SKILL habla de **tres** bandas (Opus 4.6 / Opus 5 / Fable 5) pero solo existen **dos** archivos variantes; no hay `escritor-opus5.md`.
- Las variantes son copias congeladas al 19/08 (`git log`: commit del 19/08, "SIN VERIFICAR"); si se reabre un A/B futuro serían copias desactualizadas del escritor (p. ej. sin lo que haya cambiado después). No es error hoy — es deuda declarada si se reutilizan.

### H5 · MENOR — Los 9 agentes legacy v4.6 siguen REGISTRADOS como subagentes invocables

El SKILL cumple: solo los menciona como historia (`SKILL.md:18-23` tabla de reemplazos, `:390` *"No se invocan en Nivel 4"*). Pero archivarlos en `.claude/agents/_legacy_v46/` (10 archivos verificados) **no los des-registró**: en el roster vivo de esta sesión `ideador`, `arquitecto`, `personajes`, `disenador-sensual`, `escritor`, `critico`, `editor`, `contador` y `centinela` aparecen como `subagent_type` invocables, con descripciones en presente activo (*"Use this agent for FASE 5…"*) y sin marca de legacy. Riesgo real: un orquestador eligiendo por descripción puede tomar `escritor` en vez de `escritor-nivel4`, o `critico` en vez de `validador`. Es el mismo mecanismo de `feedback_archivar_es_renombrar_no_mover` (la app filtraba por subcadena y el legacy seguía entrando): la plataforma escanea subcarpetas. Mitigación barata sin mover nada: prefijar las `description` de los 9 con "⛔ LEGACY v4.6 — NO invocar".

### H6 · ✅ INFO — Todas las rutas citadas por el SKILL existen: 0 links rotos

Verificado por Glob/lectura, ruta por ruta: los 4 subagentes (`.claude/agents/investigador.md`, `compositor.md`, `escritor-nivel4.md`, `validador.md`) · `01_Canon/REDISENO_ENGINE_ESCRITURA_v4.6.md` · `01_Canon/voz_autoral.md` · `01_Canon/antologia_calenton.md` · `01_Canon/LIBRO_MAESTRO_ESCRITURA.md` · las 5 guías `01_Canon/Guias_Especializadas/arquitectura_erotica_{mtf,bimbo,hipnosis,femdom,bodyhorror}_v1.md` · `resources/HUMANIZADOR.md` · `escritor-fable.md`/`escritor-opus46.md` · `07_Recursos/plantilla_kit_wattpad.md` · `07_Recursos/guia_publicacion_wattpad.md` · `.agent/rules/00-contexto-obligatorio.md` (con su §Las notas de la Ama mandan) · `.agent/skills/engine-trance-lv/SKILL.md` · `03_Literatura/investigacion/`. Además: la advertencia de `SKILL.md:228` (*"humanizer NO INSTALADO EN LA MÁQUINA LITERARIA"*, medida 03/08) **no aplica a esta máquina**: `~/.claude/skills/humanizer/` existe con `CALIBRACION_CHILENO_LAVOUTE.md`. Es nota por-máquina; re-medir antes de darla por cierta en un cierre editorial.

### H7 · MENOR — La tabla de estado de Fase 0 quedó como foto del 22/07 dentro de un doc permanente

`SKILL.md:122-128` lista 10 relatos activos; hoy `01_En_Progreso/` tiene 13 — `cafe_con_piernas`, `manos_de_la_ama` y `modo_trofeo` nacieron después y no figuran. La tabla es honesta (está fechada), pero es **estado** incrustado en un documento **permanente**: contra dueño-único, su casa sería `memoria_sesiones.md` o el walkthrough de cada relato. El retrofit-al-tocar los cubre igual; el riesgo es que alguien lea la tabla como censo vigente.

### H8 · MENOR — CLAUDE.md lista `/escribir_relato` como motor vigente, pero su workflow es un fósil pre-v4.4

`.agent/workflows/escribir_relato.md` (último commit **27/03/2026** — de la migración Helena→Ele): ritual de 8 fases con `arco_argumental.md`, rutas viejas en minúscula `03_Literatura/en_progreso/` (`:31,:44,:57`), **"Extensión: Mínimo 1,500 palabras"** (`:73` — contradice la Directiva Ama 27/06/2026 y la Regla de Oro 7 del SKILL) y como artefacto de estilo `00_Ele/CODIGO_ESTILISTICO_Ele.md` (`:8`) que **no existe** en esa ruta (vive archivado en `01_Canon/_archivo/Leyes_Antiguas/CODIGO_ESTILISTICO_ELE.md`). El comando `/escribir_relato` ejecuta ESTE workflow (`.claude/commands/escribir_relato.md:5`), no el motor v4.8. La tabla de CLAUDE.md le da vigencia a algo que compite con el v4.8 y lo contradice.

### H9 · MENOR — `identidad_ele.md` sigue apuntando a la era anterior

`00_Ele/identidad_ele.md:385` describe `.agent/skills/engine-escritura-lv/SKILL.md` como *"Orquestador Maestro **v4.4 — 8 fases con Rúbrica D1-D5**"* (¡tres versiones atrás!); `:383-384` declara a `escritura-voûte` "**Motor de Escritura**" y al VADEMECUM "**OBLIGATORIO antes de escribir cualquier escena**"; `:327` repite la obligatoriedad. Están en §IV y §VIII (el arranque solo carga §I+§II, así que no se inyectan en cada sesión), pero es rot en el archivo dueño de la identidad. *(El coordinador de esta auditoría indicó que corrige él los punteros de identidad_ele.md — se deja constancia, no se toca aquí.)*

---

## 3. Orfandad — la familia literaria en `.agent/skills/` (preguntas 5-6)

| Skill | Qué dice ser | Arquitectura que describe | ¿Referenciado por algo vivo? | Última modif. (git) | Veredicto |
|---|---|---|---|---|---|
| `escritura-voûte` | "Motor de escritura del universo… voz canónica calibrada" (SKILL, frontmatter). Nota interna: no define personalidad, solo el oficio *(la mención "Helena" de `:9` ya fue corregida durante esta auditoría por el coordinador)* | Orquestador **v4.4** con Crítico/Centinela/Editor (`SKILL:40,56,97`); artefactos v4.4/v4.6: `arco_argumental.md`, `linea_de_tiempo_maestra.md` (`:75,169`); sistema propio de correcciones (MEMORIA_ERRORES/CORRECCIONES) paralelo a la auto-memoria | **SÍ, mucho** — ver §5. Y fue **usado en producción el 13/08/2026** (commit *"Reescritura v0.4 de Manos de la Ama (escritura-voute skill)"*) con Gates de la Ama del 08/08 y 13/08 codificados en sus §VII.7-9/§VIII.6-9 | **13/08/2026** | **NO huérfano — motor paralelo vivo y desalineado.** Es la violación de dueño-único más seria del área literaria: dos motores escribiendo, dos memorias de correcciones |
| `escritor-literario` | "Agente Escritor… el Orquestador lo invoca vía Agent()" (`SKILL:3`) | v4.4/v4.6: jerarquía `arco_maestro_vX` → `personajes_maestro_vX` → `linea_de_tiempo_maestra` (`:25-29`); **exige "Control de Versión" + "Historial" DENTRO del capítulo** (`:273-281`) = metadata visible = **REPUDIADO automático** bajo el validador v4.8 | Nada vivo lo referencia; pero la bitácora registra una **invocación el 29/07/2026** (el_podcast Cap 1 v0.4, `00_Ele/memoria_historica/bitacora_sesiones_2026.md:163`) — una semana después del v4.8 | 24/05/2026 | **Huérfano probable** (uso esporádico reciente, contenido superado y hoy contraproducente) |
| `editor-literario` | "Agente Editor… aplica instrucciones del Crítico, Fase 6" (`SKILL:3`) | Loop Crítico↔Editor del v4.6 — **la función que Nivel 4 eliminó adrede** (Regla de Oro 5 SIN EDITOR; el loop "sanitizaba la prosa") | Nada vivo | 01/05/2026 | **Huérfano probable** — mantenerlo invocable es un peligro doctrinal, no solo mugre |
| `critico-literario` | "Agente Crítico… rúbrica D1-D5, veredictos REPUDIADO/CIRUGÍA/OBSERVACIONES/EXCELENCIA" (`SKILL:3`) | v4.4/v4.6; el validador v4.8 consolidó D1-D5 en su eje Narrativa | Nada vivo | 01/05/2026 | **Huérfano probable** |
| `ideacion-literaria` | "Motor de ideación pura… **Fase 1 del Orquestador**" (`SKILL:3`) | v4.4 (Fase 1 de 8); método Divergencia 3-caminos + script `scripts/generar_ficha.py` (existe) | Nada vivo en el repo; **tiene copia global** en `~/.claude/skills/ideacion-literaria/` que la mantiene registrada como skill invocable en esta máquina | 09/04/2026 | **Huérfano probable** |

**Bonus (fuera de los 5, mismo síntoma):**
- `.agent/workflows/escribir_relato.md` — ver H8. Fósil del 27/03/2026 con puerta de entrada activa (`/escribir_relato`).
- `~/.claude/commands/orquestar-literatura.md` (global, fuera del repo) — registra el comando *"Orquestador Maestro v4.4 — 8 fases"* como invocable en esta máquina. Y `~/.claude/skills/escritura-voûte/` (copia global, sincronizada por última vez en la era en que se editaban en espejo — hoy garantía de drift).

---

## 4. Contenido único a RESCATAR antes de archivar

Medido contra el sistema v4.8 (4 subagentes + `voz_autoral.md` + `antologia_calenton.md` + `HUMANIZADOR.md` + `Guias_Especializadas/*` + `LIBRO_MAESTRO_ESCRITURA.md`):

**Ya migrado (no rescatar, solo constatar):**
- Firma sonora *jiji* / muletillas canónicas → `01_Canon/LIBRO_MAESTRO_ESCRITURA.md:732,779` y `01_Canon/personajes_principales.md:65`.
- Saturación "con la X de quien Y" (máx 6-8) → `arquitectura_erotica_mtf_v1.md:724`.
- Traición del cuerpo / sumisión refleja → patrón M1 en `escritor-nivel4.md:115` (Principio 2 de MEMORIA_ERRORES cubierto).
- Buzzwords AI → `HUMANIZADOR.md` (dueño único declarado en `escritor-nivel4.md:87-89`).
- `CORRECCIONES.md`: **deuda activa = 0** (todas las filas ✅, C01-C22 + LP-T01; verificado línea a línea). Se archiva como evidencia, nada pendiente.

**⚠️ RESCATAR — vive SOLO en escritura-voûte y son decisiones/Gates de la Ama:**

| # | Contenido | Dónde vive hoy | Destino propuesto |
|---|---|---|---|
| R1 | **Peak Rush prohibido** — el clímax jamás comprimido en 1-2 párrafos; debe ser la sección más extensa y detallada (Gate Ama 13/08, Manos de la Ama) | `escritura-voûte/SKILL.md:361-363` + `resources/MEMORIA_ERRORES.md:56-57` | `escritor-nivel4.md` (regla operativa) + medida del validador (T5 hoy solo exige descarga en escena, no su extensión) |
| R2 | **Fuga de meta-texto** — prohibido "tensión sexual insoportable:" y etiquetas de intención en prosa (Gate Ama 13/08) | `SKILL.md:365-367` + `MEMORIA_ERRORES.md:58-59` | `HUMANIZADOR.md` (es un tell) o `escritor-nivel4.md` Reglas operativas |
| R3 | **Ejecutora como fuego sexual activo** + **vestuario con degradación erótica activa** (Gate Ama 13/08) | `SKILL.md:321-327,369-371` + `MEMORIA_ERRORES.md:60-63`; parcialmente encarnado en `manos_de_la_ama/walkthrough.md:21` | Generalización → `antologia_calenton.md`/`voz_autoral.md` (con los fragmentos v0.8 que la Ama aprobó); lo específico ya está en el walkthrough del relato |
| R4 | **Técnica del 1mm & Culpa Rebotada** — escalada de 5 pasos del privado (Gate Ama 08/08, Café con Piernas) | `SKILL.md:302-310` únicamente (grep en `01_Canon/` y en el proyecto: sin otra casa) | `canon_relato.md` de `cafe_con_piernas` (es mecánica de ESE relato) + si la Ama la declara universal, `CALENTON_AMA.md` o guía femdom |
| R5 | **Sustitución de reporte interno pasivo por firma sonora** como REGLA (la firma existe en LIBRO_MAESTRO; la *prohibición* del patrón "qué caliente me puse" solo está aquí) (Gate Ama 08/08) | `SKILL.md:312-319,357-359` | `escritor-nivel4.md` Reglas operativas o `voz_autoral.md` |
| R6 | **Principios 1, 3 y 4 de Dark Erotica** (Dualidad no resuelta / Ciclo abierto post-orgasmo / Ausencia de reacción como horror) — validados por la Ama 06/05 | `MEMORIA_ERRORES.md:110-191` | Verificar si las guías los encodan con esta nitidez; si no, `LIBRO_MAESTRO_ESCRITURA.md` (el Principio 2 ya está como M1) |
| R7 | **`grep -i` obligatorio en conteos de vocabulario** (lección LP-T01) | `MEMORIA_ERRORES.md:218-223` | Auto-memoria (es lección operativa de auditoría, no canon) |
| R8 | §VII.1-6 (degradación lingüística medible, dato numérico ancla, blackout, dispositivo muerto, cuenta regresiva, poder sistémico) | `SKILL.md:232-300` | Casi todo tiene raíz en `ANÁLISIS_RELATOS_REFERENCIA.md` (p. ej. `:64` dato numérico) — verificar 1:1 y completar la guía correspondiente antes de archivar |

**Opcional (valor menor):** método Divergencia 3-caminos de `ideacion-literaria` — el Compositor Pasada 1 no lo incluye; si a la Ama le sirve como técnica de intake, una nota en el Compositor basta. Si no, se archiva sin pérdida.

**NO rescatar (mata estado vivo, hay que ENTERRAR):** `resources/BITACORA_TEMPORal.md` — sigue describiendo `el_secreto_de_la_comoda` con la estructura de 6 capítulos previa a la reforma del 25/08 (Cap 2 "El Espejo Humillante" v0.8, Cap 3 "Día 15"…): es un **segundo dueño de estado que ya miente**; el dueño es `cronologia.md` del proyecto. Archivar con nota de sucesor, jamás consultar.

---

## 5. Referencias vivas externas a los 5 candidatos (inventario completo)

Punteros **activos** (excluye `memoria_historica/`, `_legacy_v46/`, `_archivo_pre_reinicio/` y los archivos de los propios 5 skills):

| Archivo:línea | Apunta a | Naturaleza |
|---|---|---|
| `00_Ele/identidad_ele.md:327` | VADEMECUM ("siempre obligatorio") | ⚠️ canon de identidad (§IV) |
| `00_Ele/identidad_ele.md:383-384` | escritura-voûte como "Motor de Escritura" + VADEMECUM | ⚠️ canon de identidad (§VIII) — *(coordinador lo corrige)* |
| `.agent/skills/engine-trance-lv/SKILL.md:37` | `escritura-voûte/resources/` (VADEMECUM §VI, GUIA_FETICHISTA Mód. 3, CODEX) como secundarios | ⚠️ motor VIGENTE — ruta explícita que se rompe con un `git mv` |
| `.agent/skills/engine-trance-lv/resources/PNL_CONTROL_MENTAL.md:223` | "guía escritura-voûte §0c-2" (cadena causal) | cita doctrinal; el §0c debe conservar casa legible |
| `01_Canon/Guias_Especializadas/arquitectura_erotica_hipnosis_v1.md:51,397-399,416` | VADEMECUM §VI, GUIA_FETICHISTA Mód. 3, CODEX — "fragmento raíz", "**No reemplaza**… **Complementa**" | ⚠️ guía viva que declara a los resources como complemento obligatorio |
| `01_Canon/Guias_Especializadas/arquitectura_erotica_femdom_v1.md:45,53,143,218,327,358-360,378` | VADEMECUM §V-VII, GUIA_FETICHISTA Mód. 2, CODEX, MEMORIA_ERRORES | ídem |
| `01_Canon/Guias_Especializadas/arquitectura_erotica_bodyhorror_v1.md:354-356` | GUIA_FETICHISTA Mód. 5, CODEX, VADEMECUM §I/§IX | ídem |
| `01_Canon/Guias_Especializadas/arquitectura_erotica_mtf_v1.md:161` | GUIA_FETICHISTA Mód. 5 | ídem |
| `01_Canon/Guias_Especializadas/ANÁLISIS_RELATOS_REFERENCIA.md:3,64,121,146,149,219` · `ANÁLISIS_ESTILO_LITERARIO.md:55,63,82` · `CALENTON_AMA.md:48,60` | VADEMECUM / GUIA_FETICHISTA | citas por nombre de archivo (sin ruta) |
| `03_Literatura/01_En_Progreso/el_podcast/investigacion_tema.md:5,13` | "Alimenta al escritor-nivel4 **y al motor escritura-voûte**" + VADEMECUM obligatorio | relato activo — doble motor declarado por escrito |
| `03_Literatura/01_En_Progreso/la_muneca_del_gerente/investigacion_tema.md:13` | VADEMECUM "siempre obligatorio" | relato activo |
| `.agent/rules/02-infraestructura.md:41` | escritura-voûte como ejemplo de skill | mención cosmética |
| `07_Recursos/prompts/escritor.md:43-46` · `termometro.md` · `orquestador.md` | resources de escritura-voûte | banco de prompts legacy (semi-archivado por convención de 07_Recursos) |

**Clave del inventario:** casi nada vivo apunta al **protocolo** de escritura-voûte (su SKILL) — lo que el canon vigente necesita son sus **resources** (VADEMECUM, GUIA_FETICHISTA, CODEX), que las 5 guías y el engine-trance declaran explícitamente como complemento no reemplazado. El SKILL es archivable; los resources no se archivan: se **promueven**.

---

## 6. 📦 PLAN DE CONSOLIDACIÓN (propuesto — la ejecución y cada decisión de archivo son de la Ama)

**Principio rector:** "un solo skill de escritura" = `engine-escritura-lv` (relato) + su fork declarado `engine-trance-lv` (trance) — el fork no es un segundo motor, el propio SKILL v4.8 lo gobierna (§FASE PUBLICACIÓN, dueño único 03/07). Si la directiva pretendía incluir también el fork, eso lo resuelve la Ama, no este plan.

**Destino:** `.agent/skills/_legacy/` con README que date cada pieza y nombre su sucesor (regla 12: nada muere sin sucesor declarado). *(El coordinador propuso `_legacy_v46/` en espejo de `.claude/agents/_legacy_v46/`; funciona igual — solo que 3 de los 5 son de eras v4.4 o anteriores, no v4.6, así que el README debe datar por pieza para no mentir. El nombre es cosmético; su llamada.)*

### Fase A — Rescates (ANTES de mover nada)
1. Migrar R1-R5 (Gates de la Ama 08/08 y 13/08) a sus destinos de §4. Son decisiones editoriales de ella: se migran textuales, no resumidas.
2. Verificar R6 y R8 contra guías/LIBRO_MAESTRO y completar lo ausente. R7 a auto-memoria.
3. Registrar en `walkthrough.md` de `cafe_con_piernas` y `manos_de_la_ama` que sus Gates de agosto quedaron encarnados en (destino) — para que el próximo frío no busque en el skill archivado.

### Fase B — Promover los resources compartidos
4. `git mv` de `VADEMECUM_SENSORIAL.md`, `GUIA_FETICHISTA.md`, `CODEX_PSICOLOGICO.md` → `01_Canon/Guias_Especializadas/` (su vecindario natural: las guías ya los citan por nombre y se declaran sus complementos; la mayoría de las citas son por nombre de archivo, así que la mudanza a la misma carpeta las vuelve locales). `ESTRUCTURA_MAESTRA.md` (58 líneas): evaluar fusión en `LIBRO_MAESTRO_ESCRITURA.md` o archivo.
5. Actualizar las rutas explícitas: `engine-trance-lv/SKILL.md:37`, `el_podcast/investigacion_tema.md:5,13`, `la_muneca_del_gerente/investigacion_tema.md:13`, `identidad_ele.md:327,384` *(esta última la toma el coordinador)*.

### Fase C — Archivar los 5 + el fósil
6. `git mv` a `_legacy/`: `escritura-voûte/` (SKILL + MEMORIA_ERRORES + CORRECCIONES + BITACORA_TEMPORAL, post-rescate), `escritor-literario/`, `editor-literario/`, `critico-literario/`, `ideacion-literaria/` (con su `scripts/`). Ninguno merece quedar vivo: el único con contenido aún necesario (escritura-voûte) lo entrega vía Fases A-B; `escritor-literario` produce formato auto-REPUDIADO (§3); `editor-literario` contradice la Regla de Oro 5.
7. `.agent/workflows/escribir_relato.md` + `.claude/commands/escribir_relato.md`: **decisión de la Ama** — o se archivan (y CLAUDE.md quita la fila de su tabla), o el workflow se reescribe como wrapper fino del v4.8. Hoy es una segunda puerta que contradice al motor (H8).
8. `identidad_ele.md:383-385`: reemplazar la tabla de Escritura por engine-escritura-lv v4.8 + engine-trance-lv *(coordinador)*. `.agent/rules/02-infraestructura.md:41`: actualizar el ejemplo.

### Fase D — Cierre y verificación
9. Re-correr `grep -rn "escritura-vo\|escritor-literario\|editor-literario\|critico-literario\|ideacion-literaria"` sobre archivos vivos → objetivo: solo menciones históricas. `python 99_Sistema/scripts/mantenimiento/lint_higiene_repo.py` → 0.
10. **Fuera del repo (esta máquina):** `~/.claude/skills/escritura-voûte/` y `~/.claude/skills/ideacion-literaria/` + `~/.claude/commands/orquestar-literatura.md` y `~/.claude/commands/escribir_relato.md` seguirán registrando skills/comandos viejos aunque el repo quede limpio (lección `feedback_archivar_es_renombrar_no_mover`: lo que consume no mira dónde lo archivaste). Eliminarlos o vaciarlos es acción por-máquina que requiere okey de la Ama.
11. Mitigar H5 (descriptions "⛔ LEGACY" en `_legacy_v46/`) — barato y evita invocaciones por error.

### ⚠️ Fuera del plan pero MÁS urgente que él
El **H1** (subagentes con Calendario Anclado derogado) no es consolidación de skills — es el motor vigente contradiciendo una nota de la Ama en el próximo capítulo que se escriba. Corregir `escritor-nivel4.md`, `compositor.md` y `validador.md` a la letra del SKILL rev. 25/08 debería ir **antes** o junto con la Fase A.

---

---

## 7. 🔁 Investigación de seguimiento (30/08) — ¿Por qué se rehacen tanto las versiones?

**Pregunta de la Ama:** ¿hay un motivo de fondo detrás de los rechazos constantes y el rehacer versiones una y otra vez?

**Método:** censo completo de `01_En_Progreso/*/reportes/`, conteo de veredictos, lectura íntegra de reportes de validación y de notas Gate aplicadas, cruce con walkthroughs. Números medidos con `find`, no estimados.

### 7.1 Primera corrección a la premisa: el Validador casi NO rechaza

Veredictos de TODOS los reportes de validación en disco (21 en total, motor v4.8 + fork trance):

| Veredicto | Cuántos | Casos |
|---|---|---|
| APROBADO | **13** | arquitectura_castigo v0.1 · podcast v0.1, v0.3 · muñeca v0.3, v0.6 · lo_que_pediste v0.3, v0.4 · manos v0.1 · latex_drone v0.1 · office_siren v0.14-v0.16 |
| MICRO-FIX | 7 | podcast v0.2 · café cap1 v0.3, cap2 v0.8, cap3 v0.3 · comoda v3.0 · lo_que_pediste v0.5, v0.6 |
| DISCONTINUO | 1 | muñeca v0.1 — y su causa fue **infraestructura**, no oficio: *"El Escritor cayó por límite de cuota a mitad de la tarea"* (`la_muneca_del_gerente/reportes/capitulo_1/fixes_v0.2.md:3`) |
| REPUDIADO / TIBIO / FRÍO | **0** | — |

**El churn de versiones no lo produce el Validador.** Lo producen los **Gates de la Ama**: 22 notas `_APLICADA` contra 21 validaciones en total — y en el caso extremo, `cafe_con_piernas`: **13 notas aplicadas + 26 borradores contra solo 3 validaciones** en los 3 capítulos. El Cap 1 llegó a v0.14 con **UNA sola validación** (v0.3) y **seis** notas de la Ama (v0.1, v0.3, v0.7, v0.8, v0.9, v0.13).

### 7.2 Cómo se llega a 14 versiones: la anatomía del caso café (cap 1)

Reconstruido del walkthrough (`cafe_con_piernas/walkthrough.md:86-150`):
- **v0.1 → Gate (04/08):** la nota + corrección en vivo introduce **los dos mecanismos nucleares del relato** — la bebida (H32) y "el otro yo" (H31) — y mata geografía entera ("no hay sótano"). El pivote P2 del canon se reemplaza (`walkthrough.md:126-145`). ¿Por qué no estaban? La Fase 1 se corrió **"Sin intake"** (`walkthrough.md:117`) — el flujo de dos pasadas diseñado para capturar esto se saltó.
- **v0.3 → Gate (05/08):** *"veredicto mucho más duro que el MICRO-FIX del Validador automático"* — *"más de la mitad del relato y nada erótico"* (`walkthrough.md:122`).
- **v0.4 → Ama (05/08):** *"300 líneas y cero erotismo... esto es la Antártica, temperatura -40... es un relato de control mental!!!"* → reescritura TOTAL (`walkthrough.md:121`). **v0.4 llegó a la Ama sin pasar por el Validador** — la bitácora dice cuatro veces "Pendiente: correr `validador`" (`walkthrough.md:121,122,111,98`) y el Gate ocurrió antes. La Regla de Oro 8b (*"nada llega a la Ama sin Validador"*, nacida el 22/07 de un incumplimiento idéntico) se violó de forma sistemática en este relato: **la Ama quedó de Validador de facto, y cada rechazo suyo costó una versión entera.**
- **v0.7-v0.13 → cuatro notas más**, leídas completas (ver 7.3).

### 7.3 Lo que las notas de la Ama repiten (leídas íntegras, no resumidas)

| Nota | Causa citada | Clase |
|---|---|---|
| café cap1 v0.3 | *"más de la mitad del relato y nada erótico"* | 🔥 temperatura |
| café cap1 (v0.4, en vivo) | *"Antártica, temperatura -40… es un relato de control mental!!!"* | 🔥 temperatura + género olvidado |
| café cap1 v0.7 (`:5`) | *"muy realista, no tiene ese sentido de relato erotico de control mental mas fantasioso"* + *"tira toda la cronologia y armala de nuevo"* (`:3`) | 🔥 tono/género + fricción calendario |
| café cap1 v0.8 (`:1`) | *"'qué caliente me puse' → cambia esta frase por otra, que sea un jiji"* + especifica la escena del tease | 🗣️ reporte pasivo → firma sonora |
| café cap1 v0.9 (`:1`) | *"la degradación es el motor de la excitación… debe ser consciente de su autodegradación… le falta más degradación autoconsciente"* | 🎯 **el mecanismo nuclear, precisado recién en la novena versión** |
| café cap1 v0.13 (`:1`) | *"evita usar la palabra degradación y similares… también hiper sexualizada… y sus variantes"* | 🏷️ vocabulario de teoría filtrado a la prosa |

La secuencia v0.9 → v0.13 es la radiografía del bucle: ella pide **más degradación** (el concepto) y cuatro versiones después tiene que prohibir **la palabra** — el Escritor tradujo la corrección conceptual a etiqueta léxica en vez de ejecutarla en carne. Es la misma clase de error tres veces en agosto, en **tres contextos distintos**: reporte pasivo → jiji (café, nota v0.8, codificado 08/08), fuga de meta-texto (*"tensión sexual insoportable:"*, Manos de la Ama, Gate 13/08, `MEMORIA_ERRORES.md:58-59`), y el ban de vocabulario (café v0.13). **La misma familia de falla reincidió porque su corrección se capturó cada vez en el motor equivocado** — `escritura-voûte` §VII.8/§VIII.6-8 y `MEMORIA_ERRORES.md`, archivos que el `escritor-nivel4` de producción **no lee** (verificado en §4 de esta auditoría: R2/R5 no existían en ningún archivo v4.8 hasta el rescate de ayer).

### 7.4 Causa raíz: el circuito de aprendizaje está cortado en cuatro puntos

No hay UNA causa; hay un circuito con cuatro cortes medibles, y los cuatro producen la misma factura — otra versión:

1. **El Validador se salta (violación de Regla 8b).** Café: 1 validación por 14 versiones; v0.4 y v0.5 fueron/iban al Gate con el validador "pendiente" (`walkthrough.md:121,122`). Cada rechazo de la Ama que el Validador habría cazado antes (temperatura -40 es exactamente su gate T1/T2) costó una vuelta completa de ella.
2. **Cuando corre, su vara está bajo la de ella.** `lo_que_pediste`: APROBADO en v0.3 y v0.4, y la Ama rechazó tres veces seguidas la misma sub-medida — el propio Validador lo admite: *"la sub-medida que la Ama viene nombrando hace tres versiones"* (`validacion_v0.5.md:149`) y en v0.5/v0.6 emite MICRO-FIX **contra su propia tabla** (*"Por la tabla correspondía [APROBADO]. No lo doy porque…"*, `validacion_v0.5.md:207-209`; ídem `v0.6.md:461`). Ya estaba en auto-memoria: el 23/07 ella rechazó la v0.3 de LQP pese al APROBADO (*"solo describe, no tienta"*).
3. **Las correcciones de la Ama no se generalizan: se aplican y mueren.** El flujo nota→`_APLICADA` arregla ESA versión; la **Captura Doble** (que alimenta `voz_autoral`/`antologia`) solo corre tras APROBADO+Gate feliz — **las 22 notas de rechazo no tienen paso de captura**, y cuando alguien las capturó, fue en `escritura-voûte`/`MEMORIA_ERRORES` (el motor paralelo, §3-4 de esta auditoría). Peor: los pendientes ni siquiera persisten dentro del mismo relato — la v0.5 de LQP llegó al Validador con **dos pendientes de la v0.4 sin aplicar** (*"pendiente desde la v0.4, no aplicado"*, `validacion_v0.5.md:133,141`), y el brief del Cap 3 de café **se escribió dos veces con direcciones contradictorias en 3 puntos** porque el primero se perdió sin commitear (`walkthrough.md:94`).
4. **El patrón H1 (una decisión que no llega a todos los archivos) se repite DENTRO de los relatos.** `canon_relato.md` §6 de café siguió mapeando **9 capítulos** un mes después de que la cronología lo comprimiera a **3** (*"choque real entre documentos dueños"*, `walkthrough.md:109`; aún "deuda heredada" el 23/08, `:105`); §4b/M8 describía el mecanismo de v0.3 dos versiones después (*"otro dato que había envejecido sin que nadie lo notara"*, `:96`); y el único MICRO-FIX de comoda v3.0 fue **solo** un *"viernes inventado (×3)"* (`validacion_v3.0.md:148`) — fricción del aparato de calendario que la Ama terminó derogando el 25/08 y que ella misma ya había señalado (*"tira toda la cronología y ármala de nuevo"*, nota v0.7 `:3`).

**Dos factores más, para el cuadro honesto:**
- **Iteración creativa legítima de la dueña (no es defecto).** El final del Cap 3 de café cambió **tres veces por órdenes vivas sucesivas** (v0.3 "FIN" → v0.5 "versión final del cierre" → v0.6 final nuevo, `walkthrough.md:99,98,92`), y el Cap 2 v0.6 lo derogó ella misma (*"sé que di el okey a esto, pero no tiene sentido, quítalo. mejor vuelve a la v0.5"*, `:111`). Ella está diseñando en el material — ningún motor elimina esas vueltas; el motor solo puede **abaratárselas** (que cada vuelta llegue ya validada y sin errores viejos).
- **Tensión canon-temprano vs. dirección-viva.** La Ley 1 de café (lucidez, sin excusa química — decisión suya del 04/08, `walkthrough.md:144`) tira contra su pedido posterior de *"control mental más fantasioso"* (nota v0.7). El 18/08 esa tensión explotó: el sistema le dio la razón al canon contra su brief y reescribió el Cap 2 entero (14.661 palabras) — ella lo devolvió (auto-memoria `feedback_notas_ama_prioridad_absoluta`). Ya está legislado (19/08: la nota manda), pero muestra que un canon de Fase 1 envejece y nadie lo re-visa contra sus directivas vivas — Fase 1.5 existe desde el 25/08 exactamente para esto y hay que usarla.
- **Infraestructura:** el único DISCONTINUO fue un corte de cuota a mitad de tarea; café 18/08 registró *"cuatro cortes de infraestructura previos (dos 529 y dos conexiones perdidas)"* (`walkthrough.md:114`); el validador de LQP v0.5 se cortó por límite de sesión (`nota_..._v0.5_APLICADA.md:82`). Versiones extra puramente operativas.

**Era legacy (para no mezclar):** los 17 borradores de comoda cap2 y las 16 versiones de office_siren pertenecen al bucle v4.6 documentado — 8 críticas *"APROBADO CON EXCELENCIA"* consecutivas (v0.5-v0.12, `reportes/capitulo_02/critica_capitulo_2_v0.*.md:2`) mientras la Ama seguía insatisfecha. Ese bucle ya fue eliminado (v4.8, Temperatura como gate). No es la causa del churn actual, pero infla los conteos históricos.

### 7.5 ¿Entrada o salida?

**Ambas, con reparto medible — y el arreglo es distinto para cada una:**
- **Entrada (canon insuficiente o saltado):** el caso más caro (café, 14 versiones) empezó con Fase 1 **sin intake** y los dos mecanismos nucleares llegaron por Gate un día después; el motivo permanente central se terminó de precisar en la **v0.9**. Cuando el intake sí se hizo completo (podcast, arquitectura_del_castigo, manos, latex_drone), el primer veredicto fue APROBADO y las versiones fueron pocas. **La correlación más limpia de todo el censo: capítulos con Fase 0+1 completas ≈ 1-3 versiones; capítulos con intake saltado o canon desactualizado ≈ 8-14.**
- **Salida (el Escritor no ejecuta lo ya dicho):** pendientes de una versión que no llegan a la siguiente (LQP v0.4→v0.5), correcciones conceptuales implementadas como etiquetas léxicas (degradación v0.9→v0.13), y reglas de ella capturadas donde el Escritor de producción no las lee (jiji/meta-texto en `escritura-voûte`). Esto no lo arregla más canon — lo arregla el circuito de captura.

### 7.6 Recomendaciones (acotadas; decidir es de la Ama)

1. **Cerrojo mecánico para la Regla 8b:** ninguna versión sube a Gate sin su `validacion_vX.md` en disco. Chequeo barato en `lint_higiene_repo.py` o en `/actualizar_sesion`: una `nota_..._APLICADA` cuya versión no tenga validación previa = hallazgo. Hoy la regla existe solo como texto y se violó 11 veces de 14 en el peor caso.
2. **Captura post-nota (el hueco número uno):** cada nota Gate aplicada dispara la pregunta *"¿qué regla general contiene esto?"* y su destino (`voz_autoral` · `canon §4b/§5` del relato · regla del Escritor). Hoy la Captura Doble solo corre en el CIERRE feliz; las 22 notas de rechazo — el feedback más valioso del sistema — no alimentan nada.
3. **Arrastre de pendientes:** el brief de cada rework abre listando los pendientes NO aplicados de la versión anterior (el Validador de LQP ya los detecta; nadie los arrastra al brief siguiente).
4. **Ban de vocabulario de teoría en prosa** (degradación, hipersexualizada, sumisión, humillación como etiquetas): la Ama ya lo ordenó (nota v0.13); convertirlo en chequeo del Validador/HUMANIZADOR para que no dependa de su ojo.
5. **Medir el efecto de lo ya arreglado:** la consolidación de ayer (motor único + R1-R5 rescatados + H1 corregido) ataca directamente los cortes 3 y 4. La métrica de éxito es simple y ya existe en disco: **notas-por-capítulo antes del APROBADO**. Hoy: café 4,3 promedio; podcast/manos/castigo ≈ 0-1. Si en los próximos 2-3 capítulos el promedio no baja hacia 1, el corte que queda vivo es el 2 (calibración del Validador) y ahí sí tocaría recalibrar la rúbrica con sus notas como fixtures.

---

## 8. 💡 Sugerencias de diseño no pedidas (30/08) — para decisión de la Ama, NADA implementado

Vistas durante la investigación, fuera del alcance de lo corregido. Cada una con su evidencia; son ideas, no hallazgos.

1. **"Eco del canon" cuando la Fase 1 corre sin intake.** El caso más caro (café, 14 versiones) nació de una Fase 1 "Sin intake" (`walkthrough.md:117`) cuyo Gate era "¿reconoces este canon como tuyo?" sobre 2.000 palabras — y los dos mecanismos nucleares faltantes (bebida, otro-yo) solo se hicieron visibles cuando ella leyó el capítulo. Propuesta: cuando el intake se salta (legítimo), el Compositor devuelve además **5 líneas** con las 5 afirmaciones más arriesgadas del canon (género/tono · mecanismo nuclear · qué NO pasa · cierre · léxico), y ESO es lo que la Ama confirma. Leíble en 20 segundos; habría delatado el hueco el 03/08.

2. **Diff-de-canon al cerrar cada capítulo.** Un canon envejecido no tiene dueño de re-visado: café arrastró un mapa de 9 capítulos un mes después de comprimirse a 3 (`walkthrough.md:109,105`) y una mecánica de dos versiones atrás (`:96`). Fase 1.5 es on-demand puro y nunca se dispara sola. Propuesta mínima: al cerrar un capítulo, el Orquestador contesta 3 preguntas contra el canon (¿el mapa sigue siendo verdad? ¿los pivotes restantes siguen? ¿alguna mecánica quedó obsoleta?) y **reporta** discrepancias en una línea — sin editar nada sin okey.

3. **Canal persistente para las órdenes vivas.** La mitad del Gate real ocurre en chat y muere con la sesión: el brief del Cap 3 se perdió sin commitear y se reescribió con 3 direcciones contradictorias (`walkthrough.md:94`); las derogaciones en vivo ("sé que di el okey… quítalo") solo sobreviven si la bitácora las citó. Propuesta: toda orden viva que cambie contenido se transcribe EN EL MOMENTO, con sus palabras literales, a la nota vigente del capítulo (o a una `nota_viva_....md` en la raíz del proyecto) — el mismo tratamiento que ya tienen las notas de la app.

4. **Recalibrar T2 con las notas de rechazo como fixtures.** El eje donde ella más rechaza (tentación / vector de deseo entre los cuerpos EN escena) no tiene casilla en la rúbrica: el Validador aprobó dos veces lo que ella rechazó tres, y terminó vetando contra su propia tabla (`lo_que_pediste/validacion_v0.5.md:149,207`). Las 22 notas están en `reportes/` — correr la rúbrica actual contra los capítulos que ella rechazó y ver cuáles habrían pasado es calibración empírica barata; la sub-medida que falta ya está formulada por el propio Validador (*"los dos cuerpos que están en la pieza no se desean"*, `validacion_v0.5.md:203`).

5. **Separar bitácora de estado en el walkthrough.** El de café pesa ~26k tokens con entradas de +1.000 palabras, y aun así se le escapó una sesión completa (27/08). Propuesta: sección corta `## ESTADO` **reescrita** en cada cierre (versión actual, tramo, pendientes — patrón ESTADO ACTUAL de `memoria_sesiones.md`) + bitácora narrativa en append. El resume-frío hoy tiene que leer todo para saber dónde está parado.

6. **Mini-conteo de tells por tramo cuando N>3.** Ya anotado por el propio orquestador y nunca subido al motor (`cafe_con_piernas/walkthrough.md:103`: los tramos intermedios acumulan tells sin medirse — 11 correcciones de golpe al cierre). Un conteo H2/H5 (solo contar, no editar) al final de cada tramo intermedio evitaría el pico. Es, de paso, un ejemplo del patrón que el nuevo paso de Captura Post-Nota debería atrapar.

---

*Secciones 1-6: auditoría de solo-lectura (30/08 AM). Sección 7: investigación de causa raíz. Las correcciones ordenadas por la Ama ("corrija el skill") se ejecutaron el 30/08 PM directamente sobre los archivos del motor — ver diff de la sesión; nada commiteado, revisa el coordinador. Evidencia verificada contra artefactos, no contra reportes.*
