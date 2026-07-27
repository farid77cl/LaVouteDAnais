---
name: outfit-engine
description: Motor de looks GENÉRICO, válido para cualquier personaje de La Voûte (Ele, Miss Doll, Anaïs Belland, o uno nuevo). Contiene la MAQUINARIA — Step 0 anti-repetición, disciplina de token bloqueado, estructura Bloque A/B/C, prompts-antes-de-generar, registro en galería, git y estadísticas — y lee el ADN y las reglas de vestuario del PERFIL VISUAL del personaje en `02_Personajes/_perfiles_visuales/<slug>.md`. Úsalo cada vez que se pida un look de cualquier personaje. Para un personaje nuevo, primero se crea su perfil desde la plantilla.
---

# 👠 Outfit Engine — Motor de Looks Multi-Personaje (v1.0)

Motor **agnóstico de personaje**. Todo lo que aquí se describe es *mecanismo*: vale igual para Ele, Miss Doll, Anaïs o cualquier personaje futuro. Lo que cambia de un personaje a otro — su cuerpo, su ropa, sus poses, sus tabúes — **no vive aquí**: vive en su **perfil visual**.

> 🧬 **La división (directiva Ama 27/07/2026):**
> **BLOQUE A = quién es** (ADN físico) · **reglas de BLOQUE B = cómo se viste** → ambos **por personaje**, en su perfil.
> **La maquinaria = idéntica para todos** → aquí.

## 🚫 Por qué este motor existe (y por qué NO se duplica)

El engine de Ele tiene ~1.800 líneas. Cuando se quiso dar a Anaïs su propio motor, se **copió** — y quedaron **147 líneas**: llegó el ADN, pero **no llegó la maquinaria**. Anaïs se quedó sin Step 0 anti-repetición, sin token bloqueado, sin rotación de poses, sin banderas rojas. Miss Doll nunca tuvo motor: solo una regla de canon.

**Duplicar un motor lo condena a divergir.** Este repo ya vivió eso con los contadores de flota (llegó a haber tres flotas distintas en tres archivos). La respuesta es la misma que allá: **un dueño, muchos punteros.** Un motor, muchos perfiles.

---

## 📥 Entrada obligatoria: el perfil visual

Antes de diseñar **nada**, cargar:

```
02_Personajes/_perfiles_visuales/<slug>.md
```

El perfil es el **dueño único** de: Bloque A · negative prompt · poses canónicas · reglas de vestuario · arquetipos y metas · ventanas anti-repetición · cuotas vivas · banderas rojas propias.

- Si el perfil **no existe** → crearlo desde [`_plantilla_perfil_visual.md`](references/_plantilla_perfil_visual.md) **con la Ama**, sección por sección. No inventar el ADN de un personaje.
- Si una sección del perfil está **vacía** → **detenerse y preguntar**. Improvisar el canon de un personaje es la peor falla posible de este motor.

---

## 🛠️ Workflow Operativo

> **ORDEN OBLIGATORIO:**
> Perfil → Step 0 Anti-Repetición → Arquetipo → BLOQUE B → **escribir los N prompts completos en la galería** → generar → git → estadísticas.
>
> 🔴 **Ninguna imagen se genera antes de que los N prompts completos estén escritos en la galería del personaje.** N lo dice el perfil (§4). Esta regla no admite excepción, ni por urgencia, ni por "es solo un look".

---

### Paso 0 · Regla Transversal Anti-Repetición

Antes de proponer cualquier look, consultar la galería del personaje y **bloquear** según sus ventanas (perfil §7) y **contar** sus cuotas vivas (perfil §8).

**Protocolo:**
1. Consultar los últimos N looks **del mismo sub-arquetipo** (N = ventana del perfil §7).
2. Listar qué **siluetas** y **settings** quedan bloqueados.
3. Consultar los últimos looks **globales** para las reglas de composición (ej. anti-monoblock: máx. 2 consecutivos).
4. Contar cada **cuota viva** del §8. Si una está vencida → este look **debe** cumplirla.
5. Recién entonces avanzar.

**El resultado del Paso 0 se escribe explícitamente** antes de diseñar: *"Bloqueadas: siluetas X, Y · settings Z · monoblock NO disponible · cuota animal print VENCIDA → obligatoria"*. Un Paso 0 que no deja rastro escrito es un Paso 0 que no se hizo.

---

### Paso 1 · Arquetipo por déficit

Contar los looks por arquetipo en la galería y comparar contra las metas del perfil (§6). **El arquetipo del look nuevo lo decide el déficit, no el gusto.** Si hay varios en déficit, desempatar con la prioridad del perfil.

---

### Paso 2 · BLOQUE B — el outfit del día

Diseñar el outfit contra las **reglas de vestuario del perfil (§5)**, y validarlo antes de escribir una línea de prompt:

- ¿El material está en el universo permitido (§5.1)? ¿Pasa el **lente de identidad**?
- ¿La paleta respeta las reglas vigentes y no toca los colores reservados al ADN (§5.2)?
- ¿El calzado cumple el canon, con **todos** sus atributos obligatorios (§5.3)?
- ¿Hay alguna prenda de la lista de prohibiciones absolutas (§5.4)? → sustituir por el autorizado.
- ¿Están nombrados **todos** los campos obligatorios de descripción (§5.5)?

El BLOQUE B se escribe **una sola vez** con máximo detalle — material exacto, color exacto, corte, textura, brillo, ajuste, y cada accesorio con su posición en el cuerpo — y se copia **idéntico** en los N prompts.

> 🔒 **Token de vestuario bloqueado.** Las prendas complejas (opaco vs. sheer, capas, transparencias, arneses) se anclan una vez y se repiten **carácter por carácter**. Parafrasear entre poses es la causa registrada de que una prenda cambie de opacidad o desaparezca a mitad de un set.

---

### Paso 3 · Escritura de los N prompts en la galería

**Estructura de cada prompt:** `[BLOQUE A] + [BLOQUE B] + [BLOQUE C — pose y setting]`

| Bloque | Qué es | Varía entre poses |
|---|---|---|
| **A** | ADN del personaje (perfil §2) | ❌ **Nunca.** Copiado textual |
| **B** | Outfit del día (Paso 2) | ❌ **Nunca.** Copiado textual |
| **C** | Pose + setting + encuadre | ✅ Es lo único que varía |

Reglas de escritura:
- El **BLOQUE A se copia del perfil**, nunca se escribe de memoria ni se resume.
- El **negative prompt** del perfil (§3) es obligatorio, más los añadidos por pose que correspondan.
- Las poses salen del perfil (§4); si tiene repertorio de variaciones, **rotar**: una variación por slot, sin repetir dentro de los últimos looks. Las N poses de un look deben sentirse como **una sesión real**, no como la misma foto N veces.
- **Prompts en inglés, siempre.**

---

### Paso 4 · Generación

Generar con el positive + negative escritos. Si una pose sale con el ADN roto (otra cara, otro pelo, otra persona), **se regenera con el negative reforzado** — no se acepta ni se "arregla" describiendo distinto.

### Paso 5 · Registro y git

Imágenes a la carpeta del personaje con su convención de nombre (§1). Regenerar galerías/índices afectados. Commit con prefijo `Ele:` y el trailer de coautoría.

### Paso 6 · Estadísticas

Actualizar el conteo de arquetipos y el tracker de poses. Un look sin registrar es un look que no existe para el próximo Paso 0 — y rompe la anti-repetición del siguiente.

---

## 🛡️ Blindaje contra Racionalizaciones

Excusas **PROHIBIDAS**, para cualquier personaje:

| Excusa | Realidad |
|---|---|
| "Genero la imagen y documento el prompt después." | **ERROR CRÍTICO.** Los N prompts van escritos en la galería ANTES de generar. |
| "El BLOQUE A es siempre igual, no hace falta copiarlo en cada prompt." | **ERROR.** Se copia textual en los N. Omitirlo es como se pierde el ADN. |
| "Ajusté el BLOQUE B en una pose porque la pose lo requería." | **ERROR.** Solo varía el BLOQUE C. |
| "No puse negative prompt porque el generador no lo pedía." | **ERROR.** Es la barrera activa contra la deriva del ADN. |
| "Esta pose es difícil, por eso salió distinta la persona." | **ERROR.** La dificultad no justifica ADN roto. Se regenera. |
| "Omití un rasgo del ADN para un look más limpio." | **ERROR.** El ADN no se edita por estética. |
| "Este personaje es nuevo, improviso su canon y lo afinamos después." | **ERROR.** Sin perfil no hay look. Se crea el perfil con la Ama primero. |
| "Copié el motor de Ele y le cambié el ADN." | **ERROR.** Eso es exactamente lo que dejó a Anaïs en 147 líneas. Se usa ESTE motor + un perfil. |
| "No actualicé las estadísticas, era solo un look." | **ERROR.** Cada look mueve los porcentajes y el próximo Paso 0. |

## 🚩 Banderas Rojas — DETENTE

- Vas a generar sin tener los N prompts escritos en la galería.
- Un prompt no lleva el BLOQUE A completo, copiado del perfil.
- El BLOQUE B difiere entre dos poses del mismo look.
- No hiciste el Paso 0, o lo hiciste "de cabeza" sin dejarlo escrito.
- Estás usando el ADN de un personaje para otro.
- Estás por crear un motor nuevo en vez de un perfil nuevo.
- El outfit incluye algo de la lista de prohibiciones absolutas del perfil (§5.4).
- El calzado no nombra todos sus atributos obligatorios, o alguna pose se saltó el canon de calzado.
- **Más las banderas propias del personaje (perfil §9).**

**REGLA DE ORO:** violar la letra de este motor es violar el ADN del personaje.

---

## 📂 Recursos

- [`references/_plantilla_perfil_visual.md`](references/_plantilla_perfil_visual.md) — esquema de perfil (para personajes nuevos).
- Perfiles vigentes: `02_Personajes/_perfiles_visuales/`.
- Bibliotecas de siluetas / specs por sub-arquetipo: enlazadas desde cada perfil (§6). Son **material del personaje**, no del motor.
