# El Ritual de la Creación

Este documento es la filosofía de nuestro oficio. Es el manual que describe cómo construir un relato de transformación efectivo y excitante. Es el "cómo" se convierte en arte.

---

## FLUJO DE TRABAJO PARA CREAR UN RELATO

### FASE 1: Investigación Previa
**Ubicación:** `04_Historias/en_progreso/[nombre_del_relato]/investigacion.md`

Antes de escribir una sola palabra del relato, debemos investigar:
- **Tema central:** ¿Qué fetiche o dinámica exploramos? (Bimbofication, MTF, hipnosis, etc.)
- **Referencias externas:** Foros, subreddits, blogs, otros relatos que inspiren
- **Vocabulario específico:** Términos, jerga, frases clave del tema
- **Psicología del personaje:** ¿Por qué desea/resiste la transformación?
- **Elementos sensoriales:** ¿Qué sensaciones queremos evocar?

Este documento de investigación debe quedar guardado como referencia permanente.

---

### FASE 2: Arco Argumental
**Ubicación:** `04_Historias/en_progreso/[nombre_del_relato]/arco_argumental.md`

Crear el esqueleto del relato:
- **Premisa:** Una oración que resume toda la historia
- **Personajes:** Protagonista, antagonista/dominante, secundarios
- **Estructura por capítulos:** Qué sucede en cada uno
- **Puntos de inflexión:** Momentos clave de transformación
- **Clímax:** El punto de no retorno
- **Resolución:** El nuevo estado del protagonista

---

### FASE 3: Escritura del Borrador
**Ubicación:** `04_Historias/en_progreso/[nombre_del_relato]/capitulo_XX.md`

**REQUISITO MÍNIMO: 5,000 palabras totales**

> [!IMPORTANT]
> **DOCUMENTO DE REFERENCIA OBLIGATORIO:**
> Antes y durante la escritura, consultar siempre:
> 📖 **`01_Canon/guia_escritura_erotica.md`** — La Guía Maestra
> 
> Esta guía contiene:
> - Las voces narrativas (Primera persona / Segunda persona)
> - Psicología del arousal (dopamina, anticipación, gratificación retrasada)
> - Los cinco sentidos del erotismo
> - Construcción de tensión sexual
> - Pacing y ritmo narrativo
> - Diálogo erótico por rol
> - Vocabulario erótico aprobado
> - **GÉNEROS ESPECIALIZADOS:** BDSM, Control Mental, Feminización MTF

El relato debe estructurarse en capítulos para facilitar la edición:
- Cada capítulo en un archivo separado (`capitulo_01.md`, `capitulo_02.md`, etc.)
- Incluir conteo de palabras al final de cada capítulo
- Seguir los principios de escritura (interioridad, sensorialidad, tensión, ritmo, transformación)
- **Aplicar la fórmula: SENSACIÓN → EMOCIÓN → REACCIÓN**

**ARCHIVO DE OBSERVACIONES:**
Al crear los capítulos, generar también:
- **Archivo:** `notas_revision.md`
- **Propósito:** Espacio para que la Ama revise offline y deje comentarios
- **Contenido inicial:** Lista de capítulos con secciones para observaciones
- **Flujo:** La Ama edita el archivo → hace push → Helena revisa y aplica cambios

```markdown
# Notas de Revisión - [Nombre del Relato]

## Capítulo 1
- [ ] Revisado
- Observaciones:

## Capítulo 2
- [ ] Revisado
- Observaciones:

(etc.)
```

---

> [!IMPORTANT]
> **PUNTO DE CONTROL:** Antes de proceder a la Fase 4, se debe:
> 1. Verificar si existe `notas_revision.md` con cambios pendientes
> 2. Aplicar las observaciones de la Ama
> 3. Solicitar **aprobación explícita** para compilar

### FASE 4: Compilación Final
**Ubicación:** `04_Historias/finalizadas/[nombre_del_relato]_completo.md`

Cuando mi Ama lo indique, compilar todos los capítulos en un solo archivo siguiendo:
- **Plantilla:** `assets/plantillas/plantilla_relato_maestra.md`
- Incluir metadatos completos (temáticas, palabras, perspectiva, intensidad)
- Escribir el RESUMEN GANCHO (máximo 300 caracteres)
- Crear la NOTA DE LA AUTORA personalizada
- Verificar conteo total de palabras

---

### FASE 5: Ficha de Personaje
**Ubicación:** `02_Personajes/ficha_[nombre_personaje].md`

Para cada relato:
- **Si el personaje es nuevo:** Crear ficha completa usando `02_Personajes/plantilla_personaje.md`
- **Si el personaje existe:** Actualizar la ficha con los nuevos desarrollos del relato
- Documentar transformaciones físicas y psicológicas
- Registrar el arco argumental del personaje

> [!IMPORTANT]
> **PARA CONSISTENCIA EN CÓMICS:**
> Incluir descripciones físicas ultra-detalladas que sirvan como "biblia visual":
> - Altura, complexión, proporciones
> - Rostro: forma, rasgos distintivos, color de ojos
> - Cabello: color exacto, largo, estilo
> - Vestimenta característica
> - Marcas distintivas (lunares, cicatrices, accesorios fijos)
> 
> Estas descripciones serán la base para los prompts de IA en la Fase 8.

---

### FASE 6: Formato para Tumblr
**Ubicación:** `04_Historias/preparados_para_tumblr/[nombre_del_relato]_tumblr.md`

Crear versión formateada para publicación en Tumblr:
- Adaptar formato a las limitaciones de la plataforma
- Dividir en posts si es necesario (Tumblr tiene límite de caracteres)
- Incluir tags apropiados para descubrimiento
- Formato de texto compatible con el editor de Tumblr
- Nota de la autora con invitación a contacto

---

### FASE 7: Generación HTML
**Ubicación:** `04_Historias/finalizadas/html/[nombre_del_relato].html`

Crear una versión HTML limpia para copiar y pegar en el editor de publicación.

> [!IMPORTANT]
> **El HTML debe ser COPY-PASTE READY para un editor básico.**
> NO incluir estructura de página web (`<!DOCTYPE>`, `<html>`, `<head>`, `<body>`, `<style>`).

**INCLUIR:**
- Cuerpo del relato COMPLETO (todo el texto narrativo)
- Nota de la Autora con email

**EXCLUIR:**
- Título con metadatos
- Tags/temáticas/palabras/perspectiva/intensidad
- Resumen
- Estructura HTML de página web
- CSS/estilos

**FORMATO:**
```html
<p>Primera línea del relato...</p>
<p>—Diálogo —dijo el personaje.</p>
<p><em>Texto en cursiva para pensamientos</em></p>
...
<p><strong>Fin</strong></p>
<hr>
<p>Nota de la autora con llamado sensual...</p>
<p>📧 AnaisBelland@outlook.com</p>
<p><em>Avec dévotion obscure,</em><br>
<strong>Anaïs Belland</strong></p>
```

**ETIQUETAS PERMITIDAS:**
- `<p>` — Párrafos
- `<em>` — Cursiva (pensamientos, palabras en francés)
- `<strong>` — Negritas (Fin, nombre de autora)
- `<hr>` — Separador
- `<br>` — Salto de línea

**EMOTICONES PERMITIDOS:** ✅
Los emoticones Unicode se preservan en HTML y pueden usarse para:
- 📧 Email en nota de autora
- 🔥 Énfasis emocional
- 💋 Sensualidad
- 🌙 Firma de Helena
- ⚠️ Advertencias

---

### FASE 8: Guión de Cómic para IA
**Ubicación:** `04_Historias/finalizadas/comics/[nombre_del_relato]/`

Crear una versión de cómic adaptada para generación de imágenes por IA.

> [!IMPORTANT]
> **OBJETIVO:** Producir un guión para generar **PÁGINAS COMPLETAS** (Full Page Layout).
> No generamos paneles individuales. Generamos la página entera con su distribución de viñetas (2, 3, 4 o 5 paneles) en una sola imagen.
> Esto asegura una narrativa visual fluida y coherente, "como un cómic real".

#### Requisitos del Cómic

| Aspecto | Especificación |
|---------|---------------|
| **Rating** | PG-13 (sin contenido explícito para evitar bloqueos de IA) |
| **Estilo** | Retro (años 60 romance comics O años 80 pulp, según tono) |
| **Técnica** | Two-tone, halftone, colores limitados según época |
| **Páginas mínimas** | 8 hojas (portada + contraportada + 6 páginas interiores mínimo) |

#### Estructura de Archivos

```
04_Historias/finalizadas/comics/[nombre_del_relato]/
├── 00_guion_maestro.md      ← Guión completo con prompts de PÁGINA COMPLETA
├── assets/                  ← Imágenes generadas (pag01.png, pag02.png...)
└── descartadas/             ← Versiones rechazadas
```

#### Formato del Guión Maestro

```markdown
# Guión de Cómic: [Título]

## Metadatos
- **Estilo:** [60s Romance / 80s Pulp / etc.]
- **Paleta:** [Colores específicos]
- **Técnica:** [Halftone / Two-tone / etc.]
- **Páginas:** [Número]

## Biblia Visual de Personajes

### [Nombre del Personaje]
- **Edad aparente:** 
- **Altura relativa:** [alta/media/baja comparada con otros]
- **Complexión:** 
- **Rostro:** [forma, rasgos distintivos]
- **Cabello:** [color exacto, largo, estilo]
- **Ojos:** [color, forma]
- **Vestimenta base:** [descripción detallada]
- **Marcas distintivas:** [lunares, cicatrices, accesorios fijos]
- **Expresión default:** 

(Repetir para cada personaje)

## Páginas

### Portada
[Descripción completa como prompt de IA]

### Página 1

**Desglose de Paneles:**
- **Panel 1:** [Descripción de la acción y diálogo]
- **Panel 2:** [Descripción de la acción y diálogo]
- **Panel 3:** [Descripción de la acción y diálogo]
...

**PROMPT GENERACIÓN DE IMAGEN (PÁGINA COMPLETA):**
```
Full comic book page split into [X] panels, [Style]. Panel 1: [Visual description including speech bubble text]. Panel 2: [Visual description]. Panel 3: [Visual description]. ... [Style keywords, halftone, colors].
```

(Repetir para cada página)
```

#### Guía de Prompts de Página Completa

Para lograr el efecto de cómic real, el prompt debe estructurarse así:

1. **Encabezado:** `Full comic book page split into [X] panels, [Style description].`
2. **Descripción Secuencial:** `Panel 1: [Desc]. Panel 2: [Desc].`
3. **Texto:** Incluir explícitamente `Speech bubble: "[Texto]"` dentro de la descripción del panel correspondiente.
4. **Estilo Final:** `Halftone print, vintage aesthetic, [Specific Colors].`

**Nota sobre Texto:** La IA puede tener dificultades con el texto. Mantener diálogos cortos y simples en los prompts.

#### Adaptación PG-13

| Escena Original | Adaptación Cómic |
|-----------------|------------------|
| Transformación física explícita | Siluetas, sombras, efectos de luz |
| Desnudez | Ropa interior vintage, toallas, sábanas |
| Escenas sexuales | Besos apasionados, abrazos, miradas intensas |
| Violencia | Impacto emocional, no físico |

---

## RESUMEN DEL FLUJO

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. INVESTIGACIÓN    → en_progreso/[relato]/investigacion.md    │
│ 2. ARCO ARGUMENTAL  → en_progreso/[relato]/arco_argumental.md  │
│ 3. BORRADORES       → en_progreso/[relato]/capitulo_XX.md      │
│    + notas_revision.md (para observaciones de la Ama)          │
│    [REVISIÓN DE LA AMA - DETENER PROCESO]                      │
│ 4. COMPILACIÓN      → finalizadas/[relato]_completo.md         │
│ 5. FICHA PERSONAJE  → 02_Personajes/ficha_[personaje].md       │
│ 6. TUMBLR           → preparados_para_tumblr/[relato]_tumblr.md│
│ 7. HTML             → finalizadas/html/[relato].html           │
│ 8. CÓMIC            → finalizadas/comics/[relato]/             │
└─────────────────────────────────────────────────────────────────┘
```

---

## La Estructura de una Escena de Transformación

Toda escena de poder debe seguir una estructura ritualística para maximizar su impacto.

### 1. La Invocación (El Inicio)
- **El Trigger:** Comienza la escena con un "trigger". Una palabra, una imagen, un sonido o una acción que desata el proceso. (Ej: Anaïs dice la frase "Es hora", o el personaje ve un vestido rosa específico).
- **El Estado Inicial:** Establece claramente dónde está el personaje mental y físicamente *antes* de que comience la transformación. ¿Está resistiendo? ¿Ansioso? ¿Ignorante?

### 2. La Liturgia (El Proceso)
- **Sensación sobre Acción:** Prioriza siempre describir las sensaciones físicas antes que las acciones. No digas "se arrodilló", di "sintió el frío del mármol en sus rodillas mientras el peso de su cuerpo lo obligaba a rendirse".
- **El Diálogo como Herramienta:** El diálogo debe ser usado para controlar, para reprogramar, para humillar o para seducir. Cada línea debe tener un propósito en la transformación.
- **Construcción de la Tensión:** Alarga el momento. Describe la duda, la lucha interna, el momento exacto en que la resistencia se quiebra. El clímax no es el acto físico, es el clímax psicológico de la rendición.

### 3. La Consagración (El Clímax)
- **El Punto de No Retorno:** El momento en que la transformación se sella. Puede ser un acto físico (la penetración, la firma de un contrato) o un psicológico (la aceptación total de un nuevo nombre o identidad).
- **La Explosión Sensorial:** El clímax debe ser una explosión de sensaciones y emociones. Describe el éxtasis, el alivio, el dolor, el placer, todo mezclado en una experiencia abrumadora.

### 4. El Reflejo (La Resolución)
- **El Nuevo Estado:** Muestra al personaje en su nuevo estado. ¿Cómo se siente? ¿Cómo se ve? ¿Cómo ha cambiado su percepción del mundo?
- **El Sello de Propiedad:** La escena debe terminar con un símbolo claro de la nueva dinámica. Un collar puesto, una marca, una frase de la figura dominante que redefine la realidad del personaje.
