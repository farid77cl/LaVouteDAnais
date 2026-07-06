# Validación — Capítulo 1 v0.1
Validador Nivel 4 · 2026-06-27

**Veredicto:** REPUDIADO
**Inmersión:** ❌
**Continuidad:** ✅
**Narrativa:** 9.3
**Temperatura:** 9.0
**Voz autoral:** ✅

> **Nota crítica sobre el veredicto:** el REPUDIADO es por GATE DE INMERSIÓN, no por la prosa. La narrativa y la temperatura están por encima del umbral de APROBADO (Narrativa ≥ 9.0, Temperatura ≥ 8.5) y Continuidad pasa limpio. Esto es la mejor noticia posible: el reinicio funcionó, calienta al nivel del termómetro, y el único bug es **metadata visible al lector** que el Escritor borra en treinta segundos sin tocar una sola línea de prosa. NO es una reescritura. Es quitar dos bloques. Hecho eso, este capítulo va al Gate de Ama.

## 1. Inmersión (anti-metadata)

❌ **FAIL — metadata visible al lector dentro del archivo de prosa.**

El archivo `capitulo_01_el_despertar_v0.1.md` contiene dos bloques de metadata que rompen la inmersión:

1. **Líneas 1-16 — bloque de Control de Versión:** título con barra técnica (`# Capítulo 1: El despertar / la firma vieja`), tabla "Control de Versión" (Versión / Estado / Canon / Fecha) e "Historial" con agente "Escritor-N4" y la nota "Borrador inicial Nivel 4 (reinicio desde cero)". Todo esto es maquinaria interna; la Ama no debe leer "Escritor-N4" ni "BORRADOR" en la página.
2. **Líneas 174-175 — pie de conteo:** `--- **Conteo de palabras:** 3,012`. Un conteo de subrayables/palabras es exactamente el tipo de etiqueta que el protocolo Nivel 4 prohíbe en el archivo del capítulo.

Regla Nivel 4: el archivo del capítulo = SOLO PROSA. Toda metadata vive en `reportes/capitulo_01/`. La presencia de CUALQUIERA de estos bloques dispara REPUDIADO automático antes de mirar nada más.

**Fix (único cambio necesario para todo el veredicto):**
- Borrar líneas 1-16 (todo el encabezado de Control de Versión + el `---`). El capítulo arranca directo en *"Lo primero que entendí, antes de abrir los ojos, fue que el pecho me pesaba mal."*
- Borrar líneas 174-175 (el `---` final y el `**Conteo de palabras:** 3,012`). El capítulo termina en *"…el cuerpo ya tenía hambre del sábado."*
- (Opcional, recomendado) Si se quiere un título visible para el lector, dejar solo `# El despertar` como primera línea — un título narrativo limpio, sin la barra técnica "/ la firma vieja" que es nomenclatura interna del mapa de capítulos.

Una vez borrados esos dos bloques, Inmersión pasa a ✅ y, con Continuidad ✅ + Narrativa 9.3 + Temperatura 9.0 + Voz ✅, el veredicto efectivo sería **APROBADO → Gate de Ama**.

## 1.5 Continuidad (cronología + costura + hechos plantados)

- **Línea de tiempo:** ✅ — Todo transcurre el Día 1, mañana, en secuencia continua (despertar → domación → subida al escritorio), exactamente como lo fija `cronologia.md` §Calendario (filas "El intercambio", "Primera domación", "La firma vieja", todas Día 1 mañana). El único marcador temporal externo es "hace dos años" (el contrato / el brindis), que la cronología ancla en el Día −730. El sábado se refiere SIEMPRE en relativo ("el sábado lo tienes anotado", "el sábado encima"), sin soltar un día de la semana que descuadre el conteo Día 1 → Día 7. Aritmética cerrada.
- **Costura con cap previo:** ✅ N/A — es el primer capítulo. El estado del cuerpo al CIERRE coincide punto por punto con `cronologia.md` §4 Cap 1: primer orgasmo administrado por Daniela en vivo (no solitario), coño-voz muda, primera grieta hecha carne con orgullo todavía peleando, feminización en arranque (peso de lado, labios, pezones sensibles, respiración alta), conoce el contrato + cláusula del sábado + Sebastián Mura, y cierra en HAMBRE + horror ("el cuerpo ya tenía hambre del sábado"). El Escritor cerró la cronología correctamente.
- **Callbacks con ancla:** ✅ — Toda referencia a evento pasado tiene origen registrado. El brindis *"Por la primera bailarina, dijiste. Levantaste la copa"* está anclado en `cronologia.md` H11 y §2 (recuerdo del Día −730), no es un callback fantasma. El contrato físico (H4), la cláusula del sábado (H5) y los "dos años de clases de pole" (H6) se PLANTAN aquí por primera vez como objeto/dato dentro de la escena — no se refieren como si ya hubieran sido narrados. No hay ninguna promesa fantasma tipo el "te lo prometí en la cocina" del caso `esposa_servidumbre`. Limpio.
- **Huecos a corregir (si ❌):** ninguno.

## 2. Narrativa

### Pivotes del canon cumplidos

- ✅ **Pivote 1 — La dómina que conoce el cuerpo (calor EN VIVO):** Cumplido y es el corazón del capítulo. Daniela está PRESENTE y ACTIVA desde la línea 40 ("—Despertaste."). No hay masturbación solitaria — el error fatal de la v anterior está erradicado. Aprieta los botones que conoce de memoria y NARRA antes de tocar: *"Ahora te voy a tocar aquí —dijo, y me tocó ahí… ¿Viste? Te dije. Y ahora voy a bajar despacio, así, y tú vas a querer que vuelva arriba."* El motor planos-vs-manual está explícito en prosa (párrafo 110): *"Yo había diseñado ese cuerpo desde afuera… Tenía los planos. Pero nunca lo había vivido por dentro… Ella tenía el manual."* La ley del calor (la lucidez que pelea dobla la carga) dicha por la dómina: *"Tú peleas y eso lo dobla todo… Eres lo más caliente que he tenido en las manos."*
- ✅ **Pivote 2 — La firma vieja (plantar la trampa):** Cumplido como OBJETO FÍSICO, no metáfora. Papel grueso timbrado, sello notarial violáceo redondo, cláusula tercera subrayada a mano por él, la firma "la M con el lazo largo". Frase canónica presente (variada): *"La dejé en el escritorio para que la vieras hoy, mi amor. Justo hoy."* + cierre *"Ese te lo regalo, mi amor. Ese es de Sebastián."* El vértigo del firmante-mercancía aterriza en una sola frase demoledora: *"Yo había vendido el sábado de la primera bailarina antes de saber que la primera bailarina iba a ser yo."*

### Calidad técnica
- POV: estable. Primera persona desde adentro de Dani sin un solo desliz; "habita su propia obra y la reconoce" se respeta a rajatabla (reconoce la carne "como quien reconoce su propia letra", reconoce los 1000cc "lo había elegido yo"). El verse a sí mismo de hombre desde afuera, en boca de Daniela, está bien resuelto sin romper el POV.
- Cementerio respetado: no solitario, no aceptación clínica (pánico antes que sensación, líneas 18-34), no racionalización simultánea (el escudo "esto es respuesta vascular, no es nada" FALLA en el párrafo siguiente — cuerpo siente → mente nombra después, nunca defensivo en el mismo aliento), no humillación rabiosa (Daniela nunca grita ni se ensaña), no cierre en paz (corta en hambre).
- Vocabulario chileno: ✅ — verga, coño (implícito por "el hueco", correcto para etapa muda), coger ("una verga que me cogía a mí en esta misma cama"), weón, mojada/mojadita, tetas falsas/operadas, guata, "¿te acordái?" (único chilenismo de conjugación, autorizado por canon §9 dentro de la frase de Daniela). Sin léxico España. Sin voceo argentino. Sin voz cuica-bimbo de Ele — registro Anaïs Belland literario sostenido.
- Buzzwords AI detectadas: ninguna.

### Score Narrativa: 9.3

Razón del 9.3 y no más: la prosa es de Gold Master, ambos pivotes cumplidos con cita literal, POV impecable. Lo que la separa de un 9.5+ es menor — el cierre del escritorio (líneas 142-172) es ligeramente más explicativo que la primera mitad ("entendí que no había nada que arreglar… el Día Cero no había empezado esa mañana"), donde el narrador concluye en vez de dejar que la carne lo diga. Es un matiz, no un defecto. Está por encima del umbral de APROBADO con holgura.

## 3. Temperatura

### Frases subrayadas (las que detuvieron al validador)

- *"Cierras las piernas para que no entre y lo que haces es apretártelo. Yo te conozco esa, mi amor. Esa me la sé."* (línea 62) — el arma de los dos conocimientos en acción: ella sabe lo que el cuerpo de él hace mejor que él.
- *"Respiras como respiro yo cuando me calienta algo. Como respira una que se está mojando, mi amor."* (línea 70) — humillación sensual que NOMBRA y al nombrar enciende.
- *"No te molesta. Eso es lo que te tiene asustada. Que no te molesta."* (línea 74) — la traición de la propia carne dicha con precisión quirúrgica.
- *"Mojadita —dijo, sin asco, con orgullo… No te he hecho nada y ya estás mojada para mí."* (línea 94) — humillación dulce que gatilla la carne; la vergüenza dobla en vez de apagar (línea 96).
- *"Antes tenías verga… Una verga que me cogía a mí en esta misma cama. Y ahora tienes estas lindas tetas falsas que me hiciste… y mira cómo se te moja más cada vez que te lo digo."* (línea 100) — frase canónica del canon, ejecutada perfecta: el diferencial verga→coño aterrizado en la carne.
- *"Una cosa que se moja cuando le hablan."* (línea 100) — reasignación de categoría corporal, eco del mecanismo de voz_autoral ("eso es lo que eres ahora abajo").
- *"La humillación no me enfriaba: era el combustible… como si la vergüenza fuera el idioma que el hueco entendía. Y ella lo sabía. Por eso hablaba."* (línea 102) — tesis del calor del relato, encarnada.
- *"Yo viví aquí adentro años, mi amor. Sé dónde aprietas. Sé exactamente dónde."* (línea 106) — frase canónica, el arma de los dos conocimientos.
- *"abría el manual en la página exacta y ponía el dedo donde sabía, sin tantear, derecho al punto, y demoraba ahí justo lo que sabía que derretía."* (línea 110) — planos vs manual hecho contacto físico.
- *"Pídeme con las caderas, mi amor, dale, que yo te entiendo."* + "Las caderas le pidieron. Solas." (líneas 112-114) — el cuerpo pidiendo antes que la mente, mendigando.
- *"Vas a sentir como mujer. Y de regalo, mi Dani, lo vas a sentir más fuerte que yo. Porque tú peleas… Mientras más te resistes con la cabeza, más fuerte te contesta acá abajo."* (línea 116) — la ley del calor (H3) dicha por la dómina, el placer femenino por contraste con el masculino.
- *"La lucidez no me protegía. La lucidez era el problema."* (línea 118) — formula la mente lúcida como leña.
- *"El primero te lo administro yo. Mírame."* (línea 124) — orgasmo administrado, no solitario; frase canónica.
- *"No rompió como yo conocía. No fue un disparo… Me reventó desde el centro hacia todos lados a la vez."* (línea 128) — orgasmo femenino por contraste, ejecución de Lente 7/orgasmo difuso.
- *"Y no vino la paz. Esa fue la trampa más fina de todas… vino otra cosa: un hambre."* (línea 132) — cierre en hambre, no en paz; la curva no baja.
- *"Yo había vendido el sábado de la primera bailarina antes de saber que la primera bailarina iba a ser yo."* (línea 158) — el vértigo de la firma vieja, el calor de saberse mercancía.
- *"La carne entendía el contrato antes que yo. La carne ya sabía a lo que sabía ser mercancía."* (línea 162) — el coño contesta al papel; humillación-mercancía hecha pulsión muda.
- *"el cuerpo ya tenía hambre del sábado."* (línea 172) — última línea, hambre instalada.

### Subrayables totales: 18 (mínimo esperado para 3.012 palabras: ~12)

Supera el umbral con holgura: 18 subrayables ≈ 6 por cada 1000 palabras, frente al mínimo Nivel 4 de 4/1000. Y no son subrayables "blandos": casi todos activan el mecanismo transversal (vergüenza dicha → carne contesta) y/o el motor planos-manual. La densidad de calor es alta de principio a fin, sin huecos fríos.

**Sobre el termómetro «De Esteban a Secretaria» / «La app»:** sí calienta a ese nivel. La domación en vivo funciona; la humillación sensual NO es remate de ego — cada vez que Daniela nombra lo perdido, el coño contesta (latido/contracción/humedad) y muchas veces ella lo señala, que es exactamente la mecánica pedida. El orgasmo es administrado por Daniela (no solitario). Cierra en hambre. Los cuatro requisitos prioritarios de la Ama están cumplidos.

### Score Temperatura: 9.0

El error de "fome" de la versión repudiada está corregido de raíz: el capítulo es caliente, en vivo, con la dómina presente y activa. Lo que lo deja en 9.0 y no más alto es el único margen de mejora real (ver Notas): la extensión quedó algo corta (3.012 vs objetivo 3.500-4.500), y el espacio natural para más calor es el buildup de la domación — más botones nombrados, más demora antes del orgasmo, alargar la cuerda de la administración del borde (líneas 112-124). No es un defecto; es techo disponible. Por encima del umbral de APROBADO.

## 4. Voz Autoral

✅ PASS — Suena al canon autoral y a Anaïs Belland.

### Tics canónicos activados:
- **Lente 1 (cuerpo antes que mente):** "el cuerpo fue antes que yo", "la mente nombra después", el escudo "respuesta vascular" que falla en el párrafo siguiente. Patrón Esteban trasladado a Dani sin perder identidad.
- **Lente 2 (lo simbólico-femenino es el morbo):** la reasignación de categoría corporal ("una cosa que se moja cuando le hablan"; "esto otro acá abajo… que no manda nada, que solo sabe mojarse") es eco directo de "eso es lo que eres ahora abajo: piel que pide que la toquen" del voz_autoral.
- **Humillación que NO apaga sino DOBLA:** "la vergüenza… en vez de apagarme el calor lo dobló. Lo subió."
- **Diminutivo posesivo en cada intervención larga de la dominante** ("mi amor", "mi Dani", "mi vida") — invariante de Daniela cumplido, hereda la cadencia de Valeria.
- **Oraciones largas con comas que imitan respiración** (líneas 20, 110, 116, 128) + **fragmentos de una palabra como golpe** ("Ese.", "Subí.", "Y lo sabía.").
- **La calma de la dominante como arma** ("no me peleaba, me llevaba") — eco de Valeria.

### Frases nuevas candidatas para incorporar a voz_autoral.md (si la Ama aprueba en el Gate):
- *"Él tiene los planos; ella tiene el manual."* (en prosa: "Tenía los planos… Ella tenía el manual.") — formula el motor de los dos conocimientos, núcleo del relato.
- *"La carne entendía el contrato antes que yo. Ya sabía a lo que sabía ser mercancía."*
- *"La lucidez no me protegía. La lucidez era el problema."* — la mente lúcida como leña (ley del calor).
- *"como si la vergüenza fuera el idioma que el hueco entendía. Y ella lo sabía. Por eso hablaba."* — la humillación dicha = idioma del coño.

## 5. Micro-fixes sugeridos

(El veredicto es REPUDIADO por Inmersión, no MICRO-FIX. La corrección obligatoria es la del §1. Las siguientes son opcionales, para subir techo cuando el Escritor toque el archivo de todas formas.)

1. **Obligatorio (Inmersión):** borrar líneas 1-16 (Control de Versión + `---`) y líneas 174-175 (`---` + conteo de palabras). Dejar como primera línea, si se quiere título, solo `# El despertar`.
2. **Opcional (Temperatura, techo):** el capítulo quedó en 3.012 palabras (objetivo 3.500-4.500). Si se quiere más cuerpo, expandir el buildup de la domación entre líneas 112 y 124 — más botones nombrados por Daniela, alargar la administración del borde ("me subía hasta casi, me dejaba ahí latiendo") con uno o dos ciclos más antes de "el primero te lo administro yo". SIN meter datos factuales nuevos (no tocar continuidad).
3. **Opcional (Narrativa, matiz):** el cierre del escritorio (líneas 170-172) concluye un poco explícito ("entendí que no había nada que arreglar… lo había firmado"). Se puede confiar más en la carne y menos en la conclusión de la mente, dejando que el último latido del coño cargue el peso. Es preferencia fina, no error.

## 6. Notas

- Esto es un reinicio exitoso. La autoverificación del Escritor es honesta y precisa — el conteo de subrayables, el chequeo de continuidad y el respeto al Cementerio coinciden con lo que verifiqué de forma independiente. El Escritor identificó él mismo que la extensión quedó corta, lo cual es buena señal de calibración.
- El único motivo del REPUDIADO es estructural-mecánico (metadata en el archivo de prosa), no de calidad. Es el bug clásico de Nivel 4 y la corrección es de un movimiento. Una vez quitados los dos bloques, el capítulo está listo para el Gate de Ama — no necesita pasar de nuevo por una validación completa, solo confirmar que la prosa quedó intacta y sin encabezado/pie.
- Recomendación al orquestador: tras el fix de Inmersión, el destino es **Gate de Ama** (no otra ronda de Escritor para narrativa/temperatura — esos ejes ya pasaron).
