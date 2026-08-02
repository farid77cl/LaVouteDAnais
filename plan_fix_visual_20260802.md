# 💅 Plan de Fix Visual — Rango Reciente L700-L800 (02/08/2026)

> Auditoría fresca hecha **mirando las imágenes en disco** (no releyendo el reporte del 29/07).
> Regla que la gobierna: *verificar el artefacto, nunca el reporte*. Varias "urgencias" del 29/07
> resultaron ya resueltas o inexistentes al medirlas hoy.

---

## 1. Alcance de esta auditoría

| Capa | Cobertura | Método |
|---|---|---|
| **Materialización** | Exhaustiva — 101 looks L700-L800 | `git ls-files` (fuente de verdad, no el disco) |
| **Texto de prompts** | Exhaustiva — 707 poses | parser sobre `galeria_outfits.md` |
| **Visual (píxeles)** | **Muestra profunda: 4 looks / 28 imágenes** — L771 (Stripper), L772 (Corporate), L774 (Domestic/Maid), L786 (Editorial) | lectura visual, full-res 1200px |

Las 193 imágenes L7xx en disco son **todas full-res** (0 miniaturas) → todo el rango es auditable por defecto fino.

---

## 2. Lo que el plan del 29/07 daba por urgente y HOY ya no lo es

| Item 29/07 | Medición 02/08 | Estado |
|---|---|---|
| 35 poses faltantes Tier 1 (13 looks) | **707/707 en git — 0 faltantes** | ✅ Resuelto (la app las materializó) |
| 138 prompts con `standing upright` en pose no-standing | **0** en los prompts actuales | ✅ Inexistente / ya corregido |
| 217 prompts con `glove` en el positivo | Siguen (630 en todo el rango) **pero 0 guantes en las 28 imágenes vistas** | 🟡 Cosmético (ver §4) |
| Metalenguaje multi-toma | 232 poses **pero 0 collages en las 28 imágenes vistas** (`SINGLE_FRAME` aguanta) | 🟡 Cosmético (ver §4) |

**Conclusión:** el defecto real del rango reciente **no es el texto de los prompts** — es la
**continuidad intra-outfit**, y se concentra en **siluetas estructuralmente complejas**
(couture arquitectónica, maid multi-pieza). Los outfits simples y bien definidos (bikini stripper,
traje sastre) sostienen la consistencia perfecta.

---

## 3. FIX A GENERAR — lista de regeneración (GPU)

> En todos estos casos el **prompt está correcto**: el garment descrito coincide con las poses buenas.
> El fallo es **drift de generación** → la acción es **re-tirar la pose**, no reescribir el prompt.

| Look | Pose(s) a regenerar | Qué salió mal | Cambio de prompt |
|---|---|---|---|
| **L774** Blush Maid | **Standing** | Salió un **vestido negro de látex + medias de red + pumps negros** en vez del maid blush. Las otras 6 poses son correctas. Prompt = "blush mirror-vinyl maid dress" (correcto). | **Ninguno** — re-roll |
| **L772** Pearl Boardroom | **Seated** | **Watermark de texto fantasma** ("RAI?TIRIO") incrustado (viola "no text") + **sujetador negro sheer** que las otras poses no llevan. | **Ninguno** — re-roll (el negativo ya veta logo/lettering; reforzar `watermark` si reincide) |
| **L786** Angular Couture | **Standing, Back View, Ditzy, POV** | Perdieron la silueta canónica (**vestido largo plateado con hombros angulares**, que SÍ está en Seated/Side/Odalisque). Standing salió corsé + falda lápiz negra a la rodilla; Back agregó cinturón cobre; Ditzy/POV salieron color-block. Además **color grading disparejo** (varias en B&N con solo labios en color) y **calzado disparejo** (pumps vs plataforma). | **Reforzar** el ancla afirmativa de silueta (hemline `floor-length` + `angular shoulder architecture` explícitos) · fijar un solo color grading · fijar un solo calzado |
| **L771** Salt Flat Pole | **Ditzy** (opcional, bajo) | Copa cambia a halter con keyhole + aparecen choker y pulseras que no están en las otras 6. | Opcional — re-roll o dejar |

**Total a regenerar (muestra):** 6 poses obligatorias (L774×1, L772×1, L786×4) + 1 opcional (L771).

**Referencia para L786** (la silueta canónica a replicar): las poses **Seated, Side Profile y Odalisque**
son el gold — vestido plateado largo al piso, hombros puntiagudos, tajo alto.

---

## 4. Higiene de prompt (cosmético — DIFERIBLE, no arregla ninguna imagen)

Barrido opcional sobre `galeria_outfits.md`, todo el rango, para pasar los linters sin cambiar el resultado visual:

1. **`glove` en positivo (630 poses):** reemplazar `"with no gloves of any kind..."` por una frase
   skin-only **sin la palabra glove** (p.ej. *"her arms, forearms, wrists and hands are bare uncovered
   porcelain skin"*). Riesgo: bajo (las imágenes ya salen con brazos desnudos). Beneficio: `grep -i glove = 0`.
2. **Metalenguaje (232 poses):** quitar `in every shot` / `across all poses` del positivo, dejando el
   ancla afirmativa de outfit único **sin lenguaje de tomas**. Riesgo: bajo (`SINGLE_FRAME` ya sostiene).

> Ambos son un `re.sub` idempotente sobre el .md. **No tocan las imágenes existentes** — solo protegen
> generaciones futuras y limpian la auditoría de texto. Puede correrse después de las regeneraciones.

---

## 5. Para cerrar el 100% del rango reciente

Esta pasada visual cubrió **4 de 31 looks materializados** (muestra por arquetipo). Faltan por mirar a
píxel: **L700-L731** (menos los 3 auditados), **L773, L775-L785, L787-L800**.

- **Opción A:** yo, por tandas de ~5 looks por turno (≈35 imágenes/turno).
- **Opción B:** equipo de subagentes como el 29/07 (orquestador + workers) — **requiere OK de la Ama** (es billable).

Recomendación: **Opción A** — el defecto ya está caracterizado (continuidad en siluetas complejas), así que
la pasada restante es confirmación dirigida, no exploración a ciegas.
