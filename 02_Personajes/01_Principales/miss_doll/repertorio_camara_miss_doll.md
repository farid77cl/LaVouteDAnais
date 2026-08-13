# 🎥 Repertorio de Cámara — Miss Doll

> 🔢 **PUNTERO, no dueño (13/08/2026).** El texto de las **49 sub-poses** de Miss Doll vive en
> **`99_Sistema/scripts/visual/repertorios_pose.json`** → `personajes.miss_doll.slots`.
> Este archivo conserva el **porqué**; el texto operativo no se copia acá.
>
> Ver: `python 99_Sistema/scripts/visual/prompt_builder.py --poses miss_doll`
> Probar una: `python 99_Sistema/scripts/visual/prompt_builder.py --pose miss_doll standing 8`

---

## 🎪 Registro estético — POLE DANCE + BURLESQUE (Ama 13/08/2026)

El vocabulario de cuerpo sale del escenario: **agarre en la barra, arco lumbar largo, rodilla girada afuera, trabajo de silla invertida, floorwork sentada**. El principio rector del perfil §4 no se toca: *dispensa sensualidad como **poder**, no como oferta* — un movimiento donde otras hacen tres.

**7 sub-poses por slot × 7 slots = 49.**

| Slot | Sub-poses | Offset | Sabor |
|---|---|---|---|
| 1 · Standing | 7 | +0 | agarre alto en la barra · entrada de showgirl · rodilla girada · antes del kick · pie en alto · manos tras la nuca · parada a media caminata |
| 2 · Back View | 7 | +1 | doble agarre en la barra · shoulder-check · crop de corsetería · antebrazos contra el muro · salida caminando · línea de columna desde arriba · palma en el muro |
| 3 · Seated | 7 | +2 | silla invertida a horcajadas · pierna cruzada alta · talón en el filo · piernas sobre el brazo · echada atrás · codos en rodillas · rodillas juntas |
| 4 · Side Profile | 7 | +3 | colgada de la barra · cadera afuera · pierna extendida · arco con garganta larga · apoyada en muro · perchada en el filo · girando **hacia** el lente |
| 5 · Glacial Command | 7 | +4 | *(sin cambios — ya estaban desde el 12/08)* |
| 6 · Command POV | 7 | +6 | *(sin cambios — ya estaban desde el 12/08)* |
| 7 · Odalisque | 7 | +5 | V abierta con codos en rodillas *(canon)* · mermaid · una pierna estirada · apoyada atrás con torso alto · rodillas al pecho · sentada de lado · tobillos cruzados |

> 🔒 **Vocabulario prohibido** (gatillos MEDIDOS del filtro safe de Gemini, recalibración Ama 15/06/2026): `ass out/lifted` · `deep cleavage` · `spilling` · `bursting` · `straddling … ass out` · `lying face-down … ass lifted` · `slipping the shoulder strap off`. Bloquean **incluso con la prenda cubriendo**. Equivalentes que sí pasan: `elegant lumbar arch`, `hips angled`, `ribcage lifted`, `seated reversed`. El JSON lo lleva escrito en su propio campo.

---

## 🧭 Los dos slots que yo tenía MAL escritos (12/08/2026 — sigue vigente)

**Ditzy y POV están definidos desde mayo-junio de 2026.** No son definiciones nuevas: la Ama las fijó en su momento, Ele las cumple desde entonces, y **yo las escribí mal el 05/08/2026** al estandarizar las 7 poses de Miss Doll y Anaïs.

| Slot | Lo que yo escribí el 05/08 | El canon real |
|---|---|---|
| **5 · Glacial Command** | *"Plano medio/primer plano, mirada fría de mando directo a cámara"* | **WAIST-UP** (Ama 28/05, redef. 09/06): rostro grande y nítido + **busto/décolleté prominente abajo SIEMPRE** + outfit superior legible · **UNA sola mano** (fix 30/06) · **mirada FUERA de cuadro** (diferenciador 02/08) |
| **6 · Command POV** | *"Cámara a la altura de un sub arrodillado mirando hacia arriba"* | **RETRATO SENSUAL DE INSTAGRAM** (Ama 09/06, reforzado 30/06): **mira a la cámara**, medio cuerpo, cara protagonista + décolleté abajo, **una sola mano**, `a single woman alone`. **NO es point-of-view literal** |

**Fuentes** (las tres anteriores a mi error): `.agent/rules/06-generacion-imagenes.md` §5 y §9 · `.agent/skills/ele-outfit-engine/references/pose_repertoire_v5.md` §5-§6 · `dna_v3_5.md`. El significado de los 7 slots vive hoy en `anclas_universales.json` → `significado_de_los_slots`.

---

## ✅ El pendiente del 12/08 quedó cerrado el 13/08

Aquel día quedaron escritos solo los slots 5 y 6, y este archivo declaraba los otros cinco *"clonados al 79-83%"*. Se cerró así:

1. **Se midió bien primero.** El 79-83% mezclaba pose **y** escenario, y el escenario es lo que más varía. La cláusula de pose **sola** daba **Standing 68% · Side Profile 70% · Odalisque 54% · Seated 53% · POV 52% · Back View 41% · Glacial Command 21%** — y el único sano era el único con repertorio.
2. **Se escribieron los 35 que faltaban** en registro pole/burlesque.
3. **Se metieron al motor, no a un documento** (orden de la Ama): `repertorios_pose.json` es dueño único para las tres muñecas, `PromptBuilder.pose()` las rota.
4. **Se reensamblaron los 98 prompts** desde el motor. Verificado: **7/7 variaciones distintas por slot**, **cero repeticiones en looks consecutivos**, y dentro de un mismo look los siete slots caen en índices distintos.

> ⚠️ **La similitud media de texto ya NO es la métrica.** Con 14 looks y 7 variaciones, cada una sale exactamente dos veces: esos pares son idénticos por diseño y el promedio se queda en 43-57% aunque el repertorio funcione perfecto. Las métricas correctas son **variaciones distintas usadas** y **repeticiones consecutivas**. Auditar con el promedio otra vez es repetir el error de método del 13/08.
