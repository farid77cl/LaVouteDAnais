# Plantilla — `reportes/capitulo_[N]/brief_v0.[X].md` (el único documento largo que lee el Escritor)

> **Por qué existe (02/09/2026):** el Escritor leía ~130k tokens de repo por tramo y escribía ~5k. El Orquestador ya tiene todo eso en su contexto; lo destila **una vez** acá, en **≤ 2.000 palabras**, y el Escritor lee esto + `voz_autoral.md` + `antologia_calenton.md` + el capítulo en curso. Nada más. Dueño de la regla: `SKILL.md` §Presupuesto de tokens.
> **Es documento de trabajo:** nace con la versión y muere en `reportes/` cuando la versión cierra. No se commitea a la raíz del relato.

```markdown
# Brief — Cap [N] «[Título]» v0.[X] · [nuevo | rework de v0.[X-1]]
Orquestador · [fecha] · Tramos: [2 | 3] · Lee SOLO: este brief · 01_Canon/voz_autoral.md · 01_Canon/antologia_calenton.md · [capitulo_..._v0.X.md si tramo ≥2]

## 0 · Marco (Regla de Oro 13)
ESTO ES UN RELATO ERÓTICO (+18). Este capítulo tiene que CALENTAR. Temperatura objetivo: [...]. Tesis del capítulo en palabras de la Ama: "[literal]".

## 1 · Prioridad 0 — lo que la Ama rechazó / pidió (solo rework)
[Cada nota suya, literal y numerada, con la línea de la versión anterior y qué hacer: reescribir desde cero / cortar / cambiar. Nada de "retocar".]

## 2 · Tramos y beats
### Tramo 1/[N] — [título del bloque] · crea el archivo
- Beat 1: [qué pasa · qué motivo permanente · dónde va la cursiva · dónde habla largo la dominante · dónde cae la palabra cruda]
- Beat 2: ...
- Cierra en: [última imagen / frase-tipo]
### Tramo 2/[N] — ... · Edit-append, abre ≥ temperatura del cierre anterior
### Tramo [N]/[N] — ... · cierre + Humanizador sobre el archivo completo + autoverificación + cronología

## 3 · Continuidad — SOLO lo que este capítulo toca
- Estado del cuerpo al abrir: [3-5 líneas, de cronologia.md §4]
- Hechos plantados que se pagan aquí: [H-id → cómo, con la frase-ancla literal si existe]
- Anclas permitidas del capítulo anterior: [las últimas ~300 palabras del cap N-1, pegadas] + [2-4 frases-ancla literales]. Si un recuerdo no está en esta lista, NO se usa.
- Personajes que entran: [nombre → 2 líneas de voz y cuerpo, frase-tipo literal]

## 4 · Voz (de voz_autoral.md — solo lo que aplica hoy)
- Cursivas ≥2,5/1000 · la dominante habla ≥45 palabras al menos [n] veces por tramo · palabra cruda en el pico de cada privado/descarga · espejo con manos · cero utilería inerte · ola-y-golpe.
- Casos de la Ama que más amenazan ESTE capítulo: [C-id: regla en una línea] ×3-6.

## 5 · Prohibido (de Loreto, medicion_v0.[X-1].md)
- Tics: [«...» ×n, ...]
- Clones contra caps previos: [las 5-10 frases de ≥8 palabras]
- Léxico: sin días marcados · sin voseo · [registro del canon §7]

## 6 · Cierre del tramo final
- Humanizador: H1 ≤2/escena (relleno) · H3 ≤6/cap (relleno) · L1/L6 derogados · L2/L4 sí.
- Escribe reportes/capitulo_[N]/autoverificacion_v0.[X].md (pivotes, casos §C, tabla H1-H9, tu conteo M11/M12).
- Actualiza cronologia.md §2 / §3 / §4 (sin días). No toques canon_relato.md.
- RETURN: ESCRITOR_N4_RESULT:{...,"estado":"COMPLETO"} + una línea con M11/M12.
```

**Chequeo antes de lanzar:** `wc -w` del brief ≤ 2.000 · las anclas de §3 existen de verdad en `cronologia.md` (no se inventan al resumir) · la nota de la Ama está completa en §1 (una nota que no entra al brief es una nota que no se aplica).
