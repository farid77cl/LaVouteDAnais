# 🔍 Auditoría Visual — Anaïs Belland · 12/08/2026

> **Alcance:** las 50 imágenes materializadas de la galería viva (Look 01-14, reset del 11/08).
> **Método:** 26 de las 50 inspeccionadas a ojo contra su prompt, cubriendo los 8 looks con imagen; el resto de la evidencia es medición sobre el texto de los 98 prompts.
> **Resolución:** 669×1200 (0,8 MP) en 44 imágenes y 1200×669 en 7. **Por encima del piso de 0,3 MP** — auditar defectos finos aquí SÍ es válido (a diferencia del 40% miniatura de la flota de Ele).

---

## 🎯 La causa raíz: una sola, y es de texto

**El BLOQUE B no se copiaba idéntico en las 7 poses.** Cada pose lo parafraseaba y lo iba acortando. Medido sobre los 98 prompts, antes del fix:

| Look | Standing | Back | Seated | Side | Sovereign | POV | Odalisque |
|---|---|---|---|---|---|---|---|
| L01 Terciopelo y Sangre | 100% | 36% | 36% | 29% | 21% | 21% | 26% |
| L02 Rosa y Látex | 83% | 29% | 21% | 21% | 10% | 21% | 21% |
| L03 Esmeralda | 81% | 22% | 26% | 26% | 15% | 26% | 26% |
| L07 Perla Fría | 92% | 28% | 39% | 19% | 17% | 22% | 31% |
| L08 Champagne y Plata | 93% | 28% | 17% | 17% | 7% | 17% | 21% |
| L12 Bronce Clínico | 95% | 24% | 24% | 29% | 10% | 19% | 24% |
| L13 Kimono | 92% | 33% | 25% | 25% | 21% | 21% | 25% |
| L14 Sastrería Borgoña | 97% | 11% | 14% | 14% | 16% | 14% | 14% |

*(% de tokens del BLOQUE B presentes en el prompt de esa pose.)*

**Y 65 de los 98 prompts (66%) no nombraban el calzado en absoluto.**

El motor lo dice desde su primera versión: *"El BLOQUE B se escribe una sola vez con máximo detalle y se copia **idéntico** en los N prompts. Parafrasear entre poses es la causa registrada de que una prenda cambie."* Los prompts de Anaïs se escribieron a mano antes de que existiera el ensamblador, y ahí se coló la abreviación.

**Correlación directa, no teórica:** los dos looks con prompts más completos (L07 Perla Fría 92%, L08 Champagne 93%) son los dos **sin una sola desviación de vestuario**. Los de menor cobertura (L14 11-16%, L12 10-29%) son los que cambian de prenda entre poses.

✅ **CORREGIDO el mismo día:** los 98 prompts llevan ahora el BLOQUE B completo y textual. Cobertura mínima: **100%**. Prompts sin calzado: **0**.

---

## 📋 Desviaciones por look

### 🔴 Prenda que cambia entre poses (la falla grave)

| Look | Pose | Qué pasó |
|---|---|---|
| **L01** | Seated | El vestido columna ajustado se vuelve **otro vestido**: corpiño recto sin escote corazón, falda drapeada con cola enorme. **El collar de plata desaparece.** Sostiene un objeto (pitillera dorada) que no está en el prompt |
| **L01** | POV | **Escote alto tipo caja, sin tirantes → cuello cerrado.** Contradice el `deep sweetheart neckline` del BLOQUE B |
| **L01** | Odalisque | Vestido de **un solo hombro asimétrico**. Collar ausente |
| **L03** | Seated · Side · Odalisque | **El cierre desaparece.** El catsuit se define por `fully zipped from waist to collarbone` (en Standing el cierre abierto en V se ve); en las otras tres es un cuello alto cerrado, sin cierre. En Side Profile el látex además vira a **verde azulado** |
| **L12** | Side Profile | **El vestido midi de tirantes se vuelve un halter largo hasta el suelo con cuello alto y espalda abierta.** Y **el zapato cambia de color**: negro charol con suela roja en Standing, bronce a juego con el vestido en Side Profile. Su prompt era el único que no nombraba el calzado |
| **L13** | Back View | **Bordado inventado:** el spec dice oro *en puños y ruedo*; la imagen trae **dragones dorados enormes** por toda la espalda y las mangas. Además la espalda del kimono aparece **abierta** (una prenda de frente cruzado no hace eso) |
| **L14** | Seated | El **traje de dos piezas se vuelve un vestido/abrigo de cuero**: sin blusa de charmeuse aparte, y **el broche de plata desaparece** |

### 🟠 Desviación imagen ↔ prompt (dentro de una misma pose)

| Look | Pose | Prompt dice | Imagen muestra |
|---|---|---|---|
| **L13** | Standing | `bare legs` | **Medias negras tupidas** (no pedidas) |
| **L14** | todas | `black leather **wrist-length** gloves` | Guantes **hasta el codo/antebrazo** |
| **L02** | Standing | Bata `off ONE shoulder`, ceñida con cinturón fino | Bata caída de **los dos hombros**, sin ceñir, cinturón suelto |
| **L02** | Back View | Látex `high-shine` | Lee **mate, tipo ante/cuero suave** |
| **L02** | Seated | Balconette con aro | **Bralette triangular suave** de encaje |
| **L01** | Standing/Back | Pelo `hip-length` | Llega a media espalda |

### 🟡 Deriva de escenario

El escenario cambia de habitación entre poses **cuando el texto del setting es genérico**. En L01: salón de baile con arañas e invitados (Standing/Back) → sala de piedra con licoreras (Seated) → panelado de madera con cortina (Side) → arcos góticos de castillo (POV). En L03: sala minimalista moderna (Standing) → sala de piedra con tapices (Seated) → despacho con tapices y libros (Side).

**Contraprueba:** L14, cuyo setting sí es específico (`dark wood-panelled study, mahogany desk, leather-bound bookshelves`), **mantiene la misma habitación en todas las poses**. El problema no es el generador: es la vaguedad de `dark chamber` / `La Voûte interior`.

### 🟡 Deriva de rostro

En L01 la cara cambia perceptiblemente entre Standing (más redonda y suave), Seated (más enjuta), Side Profile (más angulosa) y POV (mandíbula distinta). El lunar sí aparece en todas las inspeccionadas ✅, y el honey blonde se mantiene ✅ — pero con un matiz más cobrizo en Side Profile de L01 y en Back View de L02.

### 🔵 Formato: las 7 Odalisque salen apaisadas

**Las 7 imágenes Odalisque materializadas son 1200×669**; las otras 44, 669×1200. **No es el bug de rotación** — verifiqué: son composiciones horizontales legítimas de una figura reclinada, con el horizonte a nivel. Pero rompe el formato vertical del resto de la flota. **Decisión de la Ama:** dejarlo como firma del slot, o anclar el encuadre vertical en el prompt.

---

## ✅ Lo que está impecable

- **L07 Perla Fría** y **L08 Champagne y Plata**: cero desviaciones de vestuario en las poses inspeccionadas. Vestido/lencería, guantes, liguero, medias, joyería y calzado exactos.
- **Suela roja** visible y correcta en todas las poses donde el zapato entra en cuadro (L01 Standing/Back, L03 Standing, L07 Standing/Back, L08 Standing, L12 Standing, L14 Standing).
- **Regla medias → puntera cerrada** (§5.3) cumplida sin excepción: donde hay medias, el zapato es de punta cerrada.
- **Lunar** presente en todas las imágenes inspeccionadas.
- **Honey blonde** en todas — sin una sola deriva a castaño o platino.
- **Uñas rojas** presentes y correctas donde las manos están desnudas; ausentes (correctamente) donde hay guantes cerrados.
- **Cero tatuajes, cero piercings** ✅.
- **Cero sonrisa amplia / risa** ✅ — el registro frío se mantiene en las 26.

---

## 🔧 Estado y pendientes

| | |
|---|---|
| ✅ **Hecho 12/08** | BLOQUE B restituido completo y textual en los 98 prompts (cobertura mínima 100%, 0 sin calzado) |
| ✅ **Hecho 12/08** | Anclas anti-defecto + `Negative Prompt` + `Ubicacion`/`Tags` en los 14 looks |
| ⏳ **Pendiente — regeneración recomendada** | **L01** Seated · POV · Odalisque · **L03** Seated · Side · Odalisque · **L12** Side Profile · **L13** Standing (medias no pedidas) · Back View (dragones) · **L14** Seated. **10 poses.** Los prompts ya están corregidos: basta volver a generarlas |
| ⏳ **Pendiente — decisión de la Ama** | ¿Odalisque se queda apaisada o se ancla vertical? |
| ⏳ **Pendiente — mejora de texto** | Especificar los settings genéricos (`dark chamber`, `La Voûte interior`) al nivel de detalle del L14, que es el único que no derivó |
| ⏳ **Sin materializar** | 48 poses: L04, L05, L06, L09, L10, L11 completos · L03 POV · L07 (5 de 7) |
