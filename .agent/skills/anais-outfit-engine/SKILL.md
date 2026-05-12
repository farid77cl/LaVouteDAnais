---
name: anais-outfit-engine
description: Motor especializado en la creación y gestión de la identidad visual de Anaïs Belland. Gestiona la generación de prompts bajo el protocolo Vintage Noir Hard-Sync v2.3, asegura la coherencia del ADN aristocrático en las 4 poses canónicas, y mantiene el catálogo de looks actualizado. Úsalo cada vez que se solicite un nuevo Look de Anaïs o una auditoría del repositorio visual.
---

# 👑 Anaïs Outfit Engine (V2.3 Vintage Noir Hard-Sync)

Motor central para la coherencia estética y técnica de Anaïs Belland. Garantiza que cada nuevo Look respete el ADN Vintage Noir v2.3 y mantenga el equilibrio arquetipal del repositorio.

## 🧬 ADN V2.3 Vintage Noir (Referencia Rápida)

Para cada generación de imagen, **DEBES** incluir estos elementos de forma explícita:

- **Físico:** Ageless dominant woman in early 40s, oval aristocratic face, sculpted lifted cheekbones, sharp defined jawline. MILF aristocrática — nunca joven, nunca bimbo.
- **Seña definitoria:** `small classic Old Hollywood beauty mark mole above upper left lip` — OBLIGATORIA en todas las imágenes sin excepción.
- **Maquillaje:** Precisely drawn dark brown thin arched brows 1940s style, sharp black cat-eye liner with elongated wing, vivid deep crimson red lips, heavy-lidded bedroom eyes.
- **Cabello:** `honey blonde hair` — SIEMPRE rubia miel. Sin excepciones. Sin variaciones.
- **Estilo:** Sculpted voluminous vintage Hollywood pin-waves or victory rolls side parted.
- **Silueta:** Slender mature elegant hourglass with extreme waist training tightlacing corset, S-curve posture.
- **Calzado:** SIEMPRE `12cm black patent leather stiletto heels no platform iconic red sole`. Sin tacón bajo. Sin plataforma visible delantera. Sin zapatillas.
- **Sin tatuajes. Sin piercings visibles.**
- **Iluminación:** Cinematic chiaroscuro, George Hurrell style, single key light, intimate tension.

## 🛠️ Workflow Operativo

> **ORDEN OBLIGATORIO:** Auditoría arquetipal → Diseño del Outfit (BLOQUE B) → Escritura de los 4 prompts completos en `galeria_looks_anais.md` → Generación → Git → Registro.
>
> **Ninguna imagen se genera antes de que los 4 prompts completos estén escritos en la galería.**

---

### 1. Análisis del Mix Arquetipal

Antes de proponer un Look, revisar `galeria_looks_anais.md` y contar looks por arquetipo para identificar déficits.

**Categorías y Metas:**

| Arquetipo | Descripción | Meta |
|-----------|-------------|------|
| **Noche / La Voûte** | Aparición estándar, La Regenta, negro satén/terciopelo, La Voûte interior | 25% |
| **Boudoir / Lencería** | Aposentos privados, negligée, merry widow, peignoir, corsetería | 20% |
| **Gala / Premiere** | Eventos sociales, alfombra roja, vestidos de columna, galas | 15% |
| **Látex / Fetichismo** | Catsuits, corsés overbust de látex, poder fetish refinado | 15% |
| **Sesión Literaria** | Estudio privado, kimono de seda, escritura nocturna, boudoir íntimo | 10% |
| **Animal Print / Autoridad** | Leopardo, serpiente, cebra — solo en tejidos nobles: seda, terciopelo, látex | 7.5% |
| **Ejecutivo de Poder** | Traje sastre vintage, falda pencil de cuero, power dressing | 5% |
| **Viaje / Jet Set** | Abrigo de vuelo, lobby hotel 5★, jet privado, yacht | 2.5% |

Si un arquetipo está bajo su meta → el nuevo Look **debe** pertenecer a esa categoría.
Si múltiples categorías en déficit → priorizar: Noche > Boudoir > Gala > Látex > demás.

**Numeración especial Boudoir:** Los looks de Boudoir/Lencería usan prefijo `L` (L01, L02, L03…), separados de la numeración estándar.

---

### 2. Definición del BLOQUE B (Outfit del Look)

Antes de escribir ningún prompt, definir el outfit con **máximo detalle**. El BLOQUE B se copia idéntico en las 4 poses — nunca se parafrasea, nunca se resume.

**Describir en este orden:**
1. **Prenda principal** — nombre, tejido exacto (satén pesado, seda charmeuse, terciopelo italiano, látex de grado clínico, encaje francés), color exacto, corte, fit, estructura interna (ballenas, tightlacing, boning)
2. **Prenda secundaria** (si aplica) — misma especificidad
3. **Medias** — solo si el look las requiere: denier, tipo (back-seam nylon, fishnet, sheer nylon), color con costura o sin
4. **Calzado** — estilo (stiletto pump, T-strap heels, peep-toe, Mary Jane, mule con plumas), tacón exacto en cm, material, color, suela roja obligatoria
5. **Accesorios en orden** — guantes (material, largo: wrist/elbow/opera), joyería (tipo exacto, material: perlas, diamantes negros, pedrería Art Déco), boquilla (sí/no), bolso (tipo: Kelly, clutch lacado), complementos de liguero si aplica

**Regla de especificidad:** Cada ítem tan preciso que dos modelos generarían imágenes idénticas solo leyendo el bloque. "tacones altos" → incorrecto. "12cm black patent leather stiletto pump pointed toe iconic red sole" → correcto.

---

### 3. Escritura de los 4 Prompts Completos (PREVIO A GENERACIÓN)

**Fórmula:** `[PREFIJO CINEMATOGRÁFICO] + [BLOQUE A] + [BLOQUE B] + [BLOQUE C — Pose y Setting]`

**BLOQUE A — ADN Inamovible:**
Copiar textualmente desde [dna_v2_3.md](references/dna_v2_3.md) o desde `CANON_VISUAL_ANAIS.md` Sección II. **Nunca escribir de memoria. Nunca parafrasear.**

**4 Poses Estándar Obligatorias (BLOQUE C):**

| Archivo | Nombre de Pose | Descripción |
|---------|---------------|-------------|
| `anais_look{NUM}_standing.png` | **command_standing** | Full body, tres cuartos, peso en una cadera, mirada fría de mando directa a cámara, setting completo |
| `anais_look{NUM}_seated.png` | **throne_seated** | Sentada en [silla/chaise/trono coherente con setting], piernas cruzadas en rodilla, mano en reposabrazos, mirada directa |
| `anais_look{NUM}_three_quarter.png` | **three_quarter** | Ángulo tres cuartos, giro de hombro hacia cámara, mirada fría sobre el hombro, silueta hourglass definida por luz |
| `anais_look{NUM}_closeup.png` | **domina_closeup** | Medium shot desde el pecho, mirada directa a cámara — frase de poder ("the look of a woman who has already written your story" u equivalente), beauty mark visible, detalle de décolleté/escote en primer plano |

Los 4 prompts completos (Prefijo + A + B + C) deben quedar escritos en `galeria_looks_anais.md` antes de generar ninguna imagen.

**NEGATIVE PROMPT:** Añadir en todos los prompts copiado desde [dna_v2_3.md](references/dna_v2_3.md). Para looks de Látex canónicos: quitar `latex` de la lista de negativos.

---

### 4. Generación de Imágenes

Solo se genera después de completar el paso 3. Usar cada prompt exactamente como aparece en la galería — sin modificaciones improvisadas en la generación.

---

### 5. Gestión de Activos (Remote-Only)

1. Guardar imágenes en `05_Imagenes/anais/look{NUM}_{slug}/`
2. Crear `README.md` en la carpeta con: BLOQUE B, 4 prompts completos, lista de archivos, arquetipo y referencia
3. `git add`, `git commit`, `git push`
4. **ELIMINAR** archivos binarios locales para mantener el repositorio ligero

---

### 6. Registro en Galería y Actualización

- Append la entrada completa del Look al final de la sección correspondiente en `02_Personajes/01_Principales/galeria_looks_anais.md`
- Actualizar el walkthrough de imágenes si existe

## 🛡️ Blindaje contra Racionalizaciones (TDD Protocol)

| Excusa / Racionalización | Realidad Canónica |
| :--- | :--- |
| "Generé la imagen y escribiré el prompt después." | **ERROR CRÍTICO.** Los 4 prompts se escriben en la galería ANTES de generar. Sin excepción. |
| "El BLOQUE A es siempre el mismo, no necesito copiarlo en cada prompt." | **ERROR.** El BLOQUE A se copia textualmente desde el canon en cada uno de los 4 prompts. Nunca se omite. |
| "Ajusté el BLOQUE B en la pose 3 porque la pose lo requería." | **ERROR.** El BLOQUE B es invariable entre las 4 poses. Solo el BLOQUE C (pose y setting) varía. |
| "Usé 'golden blonde' porque suena igual." | **ERROR.** El término exacto es `honey blonde hair`. Las variaciones diluyen la identidad. |
| "Le di cabello castaño para variar." | **ERROR CRÍTICO. ANAÏS ES SIEMPRE RUBIA MIEL. SIN EXCEPCIONES BAJO NINGÚN CONCEPTO.** |
| "Omití el lunar para un look más limpio." | **ERROR.** El lunar es la seña definitoria. `small classic Old Hollywood beauty mark mole above upper left lip` — nunca se omite. |
| "Puse tacones de 10cm con plataforma porque quedaban mejor con el vestido." | **ERROR.** Siempre 12cm, suela roja, sin plataforma visible delantera. |
| "Le di un tatuaje pequeño para este look." | **ERROR.** Anaïs NO tiene tatuajes ni piercings visibles. Jamás. |
| "Usé términos prohibidos como 'sexy' o 'seductive'." | **ERROR.** Términos prohibidos degradan el registro. Ver Sección VIII del canon. |
| "No borré los archivos locales para ahorrar tiempo." | **ERROR.** Violar el protocolo Remote-Only ensucia el repositorio. |

## 🚩 Banderas Rojas — ¡DETENTE Y REVISA!

- Estás a punto de generar sin haber escrito los 4 prompts completos en `galeria_looks_anais.md`.
- Uno de tus prompts no incluye el BLOQUE A completo copiado del canon.
- El BLOQUE B difiere entre dos poses del mismo Look.
- El cabello de Anaïs es de algún color que no sea `honey blonde`.
- No hay lunar (`beauty mark mole above upper left lip`) en algún prompt.
- Los tacones no son de 12cm con suela roja sin plataforma.
- El prompt contiene palabras prohibidas: `sexy`, `hot`, `seductive`, `naked`, `nude` (como desnudez, no como color), `provocative`, `tempting`.
- El look tiene tatuajes o piercings visibles.
- La expresión facial es de sonrisa amplia, risa o actitud juguetona.
- El look usa fondo exterior/natural para un arquetipo que no sea Viaje/Jet Set.

**REGLA DE ORO:** Si violas la letra de este Skill, estás violando el ADN de Anaïs Belland. La Ama no acepta excepciones. Su universo visual es inviolable.

## 📂 Recursos del Skill

- [CANON_VISUAL_ANAIS.md](file:///c:/Users/farid/LaVouteDAnais/02_Personajes/01_Principales/CANON_VISUAL_ANAIS.md) — Autoridad máxima visual (prevalece en todo conflicto).
- [galeria_looks_anais.md](file:///c:/Users/farid/LaVouteDAnais/02_Personajes/01_Principales/galeria_looks_anais.md) — Catálogo completo de todos los looks con prompts.
- [dna_v2_3.md](references/dna_v2_3.md) — BLOQUE A y NEGATIVE PROMPT listos para copiar.
