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

## Paso 3 — Redacción de Prompts (5 Poses Estándar)

Estructura Hard-Sync: el bloque `[IDENTIDAD FÍSICA]` + `[VESTUARIO]` es **textualmente idéntico** en las 5 poses. Solo varía `[POSE & SETTING]`.

**DNA Canon V3 Master (copiar literal):**
```
stunning woman with bimbofied facial features, oval face, high prominent cheekbones, large almond-shaped grey-green eyes, dramatic siren liner, dramatic lash extensions, straight slim upturned nose, overlined glossy hot pink lips, defined cupid's bow, small pointed chin, flawless white porcelain skin, hyper-polished smooth skin texture, dark cherry red hair, artificial XXXL extensions hip-length, voluminous waves, center parted, slender hourglass silhouette, full bust, wide hips, visible arm tattoos blackwork style, aggressive bimbo makeup, extra long French XXXL nails with white tips and pink base 5cm.
```

**Poses estándar:**

| Archivo | Pose | Técnica |
|---------|------|---------|
| `ele_{NUM}_standing.png` | Standing — full body | The Vertical Spear |
| `ele_{NUM}_back_view.png` | Back View — over shoulder | Turning, hair cascade |
| `ele_{NUM}_seated.png` | Seated | The Spider |
| `ele_{NUM}_side_profile.png` | Side Profile — full body | Extreme lumbar arch |
| `ele_{NUM}_ditzy.png` | Ditzy — beauty close-up | The Ditzy Vacant |

**Cierre obligatorio de cada prompt:**
```
Rim lighting to define silhouette, high-gloss specularity on vinyl surfaces.
```

---

## Paso 4 — Crear Carpeta y README

```
05_Imagenes/ele/look{NUM}_{slug}/README.md
```

El README lista los 5 archivos de imagen esperados.

---

## Paso 5 — Registrar en Galería

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

### 📸 Imágenes (5/5)

| Pose | Previsualización |
|------|---------|
| **Standing** | ![Standing](../05_Imagenes/ele/look{NUM}_{slug}/ele_{NUM}_standing.png) |
| **Back View** | ![Back View](../05_Imagenes/ele/look{NUM}_{slug}/ele_{NUM}_back_view.png) |
| **Seated** | ![Seated](../05_Imagenes/ele/look{NUM}_{slug}/ele_{NUM}_seated.png) |
| **Side Profile** | ![Side Profile](../05_Imagenes/ele/look{NUM}_{slug}/ele_{NUM}_side_profile.png) |
| **Ditzy** | ![Ditzy](../05_Imagenes/ele/look{NUM}_{slug}/ele_{NUM}_ditzy.png) |

---
```

---

## Paso 6 — Actualizar Walkthrough

Reemplazar el contenido de `walkthrough_imagenes_del_dia.md` para que el look nuevo aparezca primero con status COMPLETO (prompts listos).

---

## Paso 7 — Diario (AUTOMÁTICO)

Prepend en `00_Ele/mi_diario_de_servicio.md`:

```markdown
#### SESIÓN - LOOK {NUM} GENERADO ({FECHA}) {EMOJI}

**[MOMENTO] - LOOK DIARIO:**
- Look {NUM} ({Nombre}, {Categoría}) materializado. 5 prompts V3 Hard-Sync redactados.
- Stats: {N} looks desde L92. {Categoría}: {%} → Meta cumplida/déficit X%.
```

---

## Paso 8 — Memoria (AUTOMÁTICO)

En `00_Ele/memoria_sesiones.md`, sección `## 🎯 ESTADO ACTUAL DE PROYECTOS`:

- Actualizar **Último Look Ele** con el número y nombre del look nuevo.
- Agregar línea al Historial Reciente.

---

## Paso 9 — Git Commit (AUTOMÁTICO)

```
git add 00_Ele/galeria_outfits.md 00_Ele/memoria_sesiones.md 00_Ele/mi_diario_de_servicio.md 05_Imagenes/ele/look{NUM}_{slug}/ walkthrough_imagenes_del_dia.md
git commit -m "Ele: Look {NUM} ({Nombre}) — {Categoría}"
```

---

*Protocolo definido por la Ama — 10/04/2026*
