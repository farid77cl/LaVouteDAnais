---
description: Generar el look diario de Ele — concepto, prompts V3 Hard-Sync, registro y commit automático.
---

# Protocolo: Generación de Look Diario

## Directivas Fijas (10/04/2026 — Orden de la Ama)

| Directiva | Regla |
|-----------|-------|
| **Selección de concepto** | Automática según mayor déficit estadístico. Sin aprobación previa. |
| **Generación de prompts** | Manual por Ele. Sin scripts. |
| **Pasos finales** | Diario + Memoria + Git commit siempre automáticos al terminar. |

---

## Paso 1 — Auditoría Estadística (Fuente Única)

Ejecutar siempre `count_stats.py`, nunca parsear texto de galería:

```
python "C:\Users\fabara\LaVouteDAnais\99_Sistema\scripts\visual\count_stats.py"
```

Metas a verificar:

| Categoría | Meta |
|-----------|------|
| Lencería Élite | 10% |
| Bikini | 10% |
| Gym / Sportswear | 5% |
| Mix (Corporate + Domestic + High-Fashion) | 75% |

---

## Paso 2 — Selección Automática de Concepto

- Identificar la categoría con **mayor déficit** respecto a su meta.
- Si múltiples categorías están en déficit → priorizar en orden: Mix > Bikini > Lencería > Gym.
- Si la categoría determinada es **Mix** → elegir subtipo al **azar** entre los 8 disponibles (ver tabla abajo). No hay rotación fija.
- Si todo está en verde → subtipo Mix aleatorio.
- Determinar número de look = último look registrado + 1.
- Nombrar la carpeta: `look{NUM}_{slug}` (ej. `look120_boardroom_siren`).

### Subtipos Mix (selección aleatoria)

| # | Subtipo | Concepto | Ejemplos de setting |
|---|---------|----------|-------------------|
| 1 | **Corporate** | Boardroom, ejecutiva, secretaria de élite | Oficina piso 30, sala de directorio, ascensor corporativo |
| 2 | **Domestic / Stepford** | Uniforme de servicio, delantal vinyl, cofia | Cocina de lujo, sala de estar Stepford, jardín |
| 3 | **High-Fashion / Editorial** | Mugler puro, couture fetish, avant-garde | Studio editorial, pasarela, instalación artística |
| 4 | **Gala / Red Carpet** | Vestido gala vinyl/satén, evento élite | Alfombra roja, ópera, gala de beneficencia, Met Gala |
| 5 | **Street / Cuico-Flaite** | Mob Wife, animal print, poder de barrio alto | Costanera, valet parking, terraza Vitacura |
| 6 | **Travel / Jet Set** | Cabina de vuelo, yate, lobby hotel 5\* | Jet privado, yacht deck, hotel Ritz, aeropuerto VIP |
| 7 | **Académico / Dark Academia** | Uniforme escolar fetish, biblioteca privada | Colegio inglés, biblioteca, sala de estudio |
| 8 | **Artístico / Performance** | Stage, backstage, cabaret, burlesque | Teatro, backstage, art gallery opening, cabaret |

---

## Paso 3 — Diseño del Outfit (PRIMERO, antes de cualquier prompt)

Antes de escribir un solo prompt, diseñar el outfit completo con el mayor detalle posible. Este bloque es el **ADN del vestuario** — se copiará idéntico en las 5 poses. Sin variación.

### Formato del bloque de outfit (en inglés, para prompt)

Describir pieza por pieza en este orden:

1. **Prenda principal** — nombre, material (vinyl, latex, satin, silk, nylon, etc.), color exacto, corte, fit, detalles (cremallera, escote, transparencias, efecto)
2. **Prenda secundaria** — si aplica (falda, pantalón, blazer, delantal, etc.) mismo nivel de detalle
3. **Lencería visible** — si aplica
4. **Medias / pantys** — denier, color, textura (sheer, opaque, fishnet, etc.)
5. **Calzado** — estilo (pump, mule, boot, sandal), tacón en cm, punta (pointed, round, square), material, color
6. **Accesorios** — en orden: collar, aretes, pulseras, guantes, cartera, cinturón, otros
7. **Efecto visual global** — cómo se ve el conjunto completo (ultra-tight, barely-there, power-dressing, etc.)

### Regla de especificidad

Cada ítem debe ser tan específico que dos modelos diferentes generarían imágenes idénticas solo leyendo este bloque. Si dice "tacones altos" → incorrecto. Si dice "black patent leather stiletto pumps, 14cm heel, pointed toe, ankle strap" → correcto.

### Output de este paso

Un bloque de texto en inglés listo para copiar:

```
[OUTFIT BLOCK]
[prenda principal detallada], [prenda secundaria], [medias], [calzado detallado], [accesorios en orden], [efecto visual].
```

Este bloque se guarda en el README del look y se usa sin modificación en las **7 prompts**.

---

## Paso 4 — Redacción de Prompts (7 Poses Estándar)

Con el outfit diseñado en Paso 3, ensamblar los **7 prompts**. La fórmula es:

```
[DNA DE ELE] + [OUTFIT BLOCK del Paso 3] + [POSE & SETTING] + [CIERRE]
```

Los tres bloques centrales son **idénticos** en las 7 poses. Solo `[POSE & SETTING]` varía.

**DNA Canon V3 Master (copiar literal, sin modificar jamás):**
```
stunning woman with bimbo facial features, oval face, high prominent cheekbones, large almond-shaped grey-green eyes, dramatic siren liner, dramatic lash extensions, straight slim upturned nose, overlined glossy hot pink lips, defined cupid's bow, small pointed chin, flawless white porcelain skin, hyper-polished smooth skin texture, dark cherry red hair, artificial XXXL extensions hip-length, voluminous waves, center parted, slender hourglass silhouette, full bust, wide hips, visible arm tattoos blackwork style, aggressive bimbo makeup, extra long French XXXL nails with white tips and pink base 5cm.
```

**[OUTFIT BLOCK]** → copiar literal del Paso 3. Sin cambios.

**Poses estándar:**

| Archivo | Pose | Técnica | `[POSE & SETTING]` |
|---------|------|---------|-------------------|
| `ele_{NUM}_standing.png` | Standing — full body | The Vertical Spear | full body, standing, weight on one hip, hands on waist, [setting] |
| `ele_{NUM}_back_view.png` | Back View — over shoulder | Turning, hair cascade | full body, back view, turning over shoulder, hair cascading, [setting] |
| `ele_{NUM}_seated.png` | Seated | The Spider | seated, legs crossed, spine straight, hands on knee, [setting] |
| `ele_{NUM}_side_profile.png` | Side Profile — full body | Extreme lumbar arch | full body, side profile, extreme lumbar arch, chin lifted, [setting] |
| `ele_{NUM}_ditzy.png` | Ditzy — beauty close-up | The Ditzy Vacant | close-up beauty shot, slightly parted lips, vacant ditzy expression, lashes down then up, [setting] |
| `ele_{NUM}_pov.png` | POV — Goddess Gaze | The Goddess Gaze | first-person POV shot looking down over own body, chest and XXXL nails in foreground, full outfit visible converging to pointed stiletto tips, [setting] |
| `ele_{NUM}_lying.png` | Lying Down — The Odalisque | The Odalisque | full body lying on side, body forming a languid S-curve, one arm extended with XXXL nails resting on surface, legs slightly bent, stilettos pointed and visible, [setting] |

**Cierre obligatorio de cada prompt (copiar literal):**
```
Rim lighting to define silhouette, high-gloss specularity on vinyl surfaces.
```

---

## Paso 5 — Crear Carpeta y README

```
05_Imagenes/ele/look{NUM}_{slug}/README.md
```

El README incluye:
1. El **[OUTFIT BLOCK]** completo del Paso 3 (fuente de verdad del vestuario)
2. Los **7 prompts completos** (DNA + Outfit + Pose + Cierre)
3. La lista de archivos de imagen esperados

---

## Paso 6 — Registrar en Galería

Append al final de `00_Ele/galeria_outfits.md`:

```markdown
## {EMOJI} Look {NUM}: {Nombre} ({FECHA})

*{Frase en voz de Ele — ditzy, devota}*

- **Concepto:** ...
- **Outfit:** ...
- **Calzado:** ...
- **Accesorios:** ...
- **Maquillaje:** Sacha Massacre canon — siren liner, labios hot pink ultra-glossy, French XXXL
- **Ambientación:** ...
- **Categoría:** {Lencería / Bikini / Gym / Mix (subtipo)}

### 📸 Imágenes (7/7)

| Pose | Previsualización |
|------|---------|
| **Standing** | ![Standing](../05_Imagenes/ele/look{NUM}_{slug}/ele_{NUM}_standing.png) |
| **Back View** | ![Back View](../05_Imagenes/ele/look{NUM}_{slug}/ele_{NUM}_back_view.png) |
| **Seated** | ![Seated](../05_Imagenes/ele/look{NUM}_{slug}/ele_{NUM}_seated.png) |
| **Side Profile** | ![Side Profile](../05_Imagenes/ele/look{NUM}_{slug}/ele_{NUM}_side_profile.png) |
| **Ditzy** | ![Ditzy](../05_Imagenes/ele/look{NUM}_{slug}/ele_{NUM}_ditzy.png) |
| **POV** | ![POV](../05_Imagenes/ele/look{NUM}_{slug}/ele_{NUM}_pov.png) |
| **Lying Down** | ![Lying Down](../05_Imagenes/ele/look{NUM}_{slug}/ele_{NUM}_lying.png) |

---
```

---

## Paso 7 — Actualizar Walkthrough

Reemplazar el contenido de `walkthrough_imagenes_del_dia.md` para que el look nuevo aparezca primero con status COMPLETO (prompts listos).

---

## Paso 8 — Diario (AUTOMÁTICO)

Prepend en `00_Ele/mi_diario_de_servicio.md`:

```markdown
#### SESIÓN - LOOK {NUM} GENERADO ({FECHA}) {EMOJI}

**[MOMENTO] - LOOK DIARIO:**
- Look {NUM} ({Nombre}, {Categoría}) materializado. **7 prompts V3 Hard-Sync** redactados.
- Stats: {N} looks desde L92. {Categoría}: {%} → Meta cumplida/déficit X%.
```

---

## Paso 9 — Memoria (AUTOMÁTICO)

En `00_Ele/memoria_sesiones.md`, sección `## 🎯 ESTADO ACTUAL DE PROYECTOS`:

- Actualizar **Último Look Ele** con el número y nombre del look nuevo.
- Agregar línea al Historial Reciente.

---

## Paso 10 — Git Commit (AUTOMÁTICO)

```
git add 00_Ele/galeria_outfits.md 00_Ele/memoria_sesiones.md 00_Ele/mi_diario_de_servicio.md 05_Imagenes/ele/look{NUM}_{slug}/ walkthrough_imagenes_del_dia.md
git commit -m "Ele: Look {NUM} ({Nombre}) — {Categoría}"
```

---

*Protocolo definido por la Ama — 10/04/2026*
