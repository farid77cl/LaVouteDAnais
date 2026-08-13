# 🔍 Auditoría Visual — Miss Doll · 13/08/2026

> **Alcance:** las **8 imágenes nuevas** llegadas con el pull de 45 commits — **Look 07 Vogue Sovereign completo (7/7)** y **Look 08 Electric Violet Reverie Standing (1/7)**. Subidas por la app el 12-13/08, posteriores al barrido del 12/08 (que cubrió L01-L06 + L14).
> **Método:** el mismo del informe de Anaïs del 12/08 — cada imagen abierta y comparada campo por campo contra su propio prompt, con recorte ampliado ×3-×5 en cada duda antes de afirmar nada. Más medición sobre el texto de los 98 prompts.
> **Resolución:** 805×1200 (0,97 MP) ×5 · 669×1200 (0,80 MP) ×2 · 1200×669 ×1. **Todas muy por encima del piso de 0,3 MP** — auditar defecto fino aquí es válido.
> **Hashes:** los 8 archivos son distintos entre sí (se verificó MD5 — no hay ningún duplicado tipo `ele_535_back_view`).

---

## 🎯 La causa raíz de Anaïs NO aplica acá — y eso cambia el diagnóstico

Ayer el hallazgo de Anaïs fue de texto: el BLOQUE B se abreviaba por pose (Standing 81-100%, el resto 7-39%) y de ahí salía toda la deriva de prenda. **Medido sobre los 98 prompts de Miss Doll:**

| Look | Standing | Back | Seated | Side | Glacial | POV | Odalisque |
|---|---|---|---|---|---|---|---|
| **L01-L14 (los 14)** | **100%** | **100%** | **100%** | **100%** | **100%** | **100%** | **100%** |

Cobertura mínima **100%** en las 98. Cero prompts sin calzado. El linter del motor confirma: `CRITICOS: 0`, los 98 llegan expandidos y con negative a la app.

**Y sin embargo el Look 07 cambia de prenda entre poses.** Ese es el punto: acá el BLOQUE B está completo, textual e idéntico, con el ancla `GARMENT_CONSISTENCY` puesta — y el generador re-estiliza igual. **No es el mismo bug con otro nombre: es un bug distinto.** El texto ya no es la explicación.

**Qué falla exactamente:** la **asimetría**. El BLOQUE B pide `architectural asymmetric one-shoulder silhouette` y se pierde en **3 de las 7 poses**, cada vez de una forma distinta:

| Pose | Qué salió |
|---|---|
| Back View | **Strapless** — hombros y espalda enteramente desnudos, corpiño recto |
| Side Profile | **Dos tiras** (una en cada hombro) **+ cordonería lace-up rosa en la espalda** que no existe en ninguna otra pose |
| POV | **Escote en V simétrico con tira a ambos lados** |

Las cuatro poses donde el cuerpo está de frente y quieto (Standing, Seated, Glacial Command, Odalisque) mantienen el hombro único correcto. Las tres que fallan son las tres donde el torso gira o se recorta: **al rotar el cuerpo, el generador "resuelve" la asimetría convirtiéndola en simetría.** `GARMENT_CONSISTENCY` habla de escote, manga, ruedo, corte y color — **no nombra la asimetría ni el lado**, así que no la protege.

### 🔧 Fix propuesto — ancla `ASYMMETRY_LOCK` (no existe todavía)

`anclas_universales.json` tiene 16 anclas; ninguna cubre esto. Propuesta concreta, opt-in cuando el BLOQUE B declara prenda asimétrica (one-shoulder, monotirante, un solo guante, ruedo asimétrico):

```
the garment is deliberately ASYMMETRIC exactly as described: it covers one shoulder only —
the LEFT shoulder carried by a single strap and the RIGHT shoulder completely bare — and this
same single-shoulder asymmetry is kept identical from every angle including from behind and in
profile, never evened out into a symmetrical two-strap, halter or strapless bodice, and never
given a back lacing, closure or panel that is not described
```

Nombrar **el lado** es la mitad del ancla: sin lado, el generador es libre de "elegir" y en la toma siguiente elige otro. Es el mismo principio que ya se aplicó en `BACK_ANCHOR` (nombrar dónde va la abertura) y en `MIRROR_OWNER`.

---

## 📋 Look 07 · Vogue Sovereign — 7/7 materializado

**Lo pedido:** vestido escultórico de vinilo rosa hot alta brillantez, silueta arquitectónica asimétrica de un hombro, corpiño con ballenas integradas al vestido (no pieza aparte), tajo hasta el muslo, cola larga, plataforma stiletto rosa 8" con tira de tobillo, **un solo** cuff cromado sin más joyas, uñas stiletto rosa chrome.

| Pose | Veredicto | Detalle |
|---|---|---|
| **1 · Standing** | 🟠 casi limpio | Hombro asimétrico ✅ · corsé con ballenas integradas ✅ · tajo ✅ · cola ✅ · plataforma con tira ✅ · **un** cuff ✅ · uñas ✅. **Los párpados salen muy caídos**, el iris apenas asoma, contra `wide open eye opening:1.4` + `gaze directly at camera`. Aparte: le aparece un **lunar en la mejilla** que **no está en su ADN** (Miss Doll no tiene lunar — ese es rasgo de Anaïs) y no se repite en las otras 6 |
| **2 · Back View** | 🔴 deriva de prenda | **La tira de hombro desaparece: el vestido lee strapless.** Contradice `architectural asymmetric one-shoulder silhouette`. Lo demás correcto: cola desplegada ✅, plataforma ✅, **cuff cromado ✅** (ampliado ×4 para descartar que fuera reloj — es el cuff) |
| **3 · Seated** | 🟠 deriva menor | Hombro único ✅ · corsé ✅ · tajo ✅ · cola ✅ · cuff ✅ · sentada con el peso en el bloque blanco ✅. **El empeine del zapato cambia de diseño**: en Standing es cerrado con tira simple, acá lleva recorte lateral tipo d'Orsay con ojal. Mismo color, material, plataforma y aguja — deriva de modelo, no de canon |
| **4 · Side Profile** | 🔴 dos fallas | (a) **Dos tiras de hombro + lace-up rosa en la espalda**, ninguno de los dos existe en el BLOQUE B ni en las otras poses. (b) **El encuadre es tres cuartos DESDE ATRÁS** cuando el prompt pide `three-quarter turn toward camera` → termina duplicando el ángulo del Back View en vez de aportar el suyo |
| **5 · Glacial Command** | ✅ **la mejor del set** | Plano medio waist-up ✅ · **una sola mano** en cuadro ✅ · **mirada fuera del lente** ✅ · hombro único ✅ · ballenas ✅ · cuff ✅ · cejas oscuras marcadas ✅ · labios rojo-naranja ✅. Único reparo cosmético: las uñas leen almendra y el BLOQUE B pide `stiletto-shaped` |
| **6 · POV** | 🟠 dos cosas | (a) **Escote en V simétrico con tira a ambos lados** en vez del hombro único. (b) La variación pedida era `lying back with her head tipped toward the camera above her` y salió **retrato frontal erguido**. ⚠️ Ojo: **el canon POV sí se cumple** — retrato sensual de Instagram, mirada al lente, una sola mano, cero teléfono. Lo que falló es la variación de encuadre de este look, no la definición del slot |
| **7 · Odalisque** | 🔴 accesorio duplicado | **DOS cuffs cromados, uno en cada muñeca** (ampliado ×3 para confirmarlo). El BLOQUE B dice `a single oversized chrome cuff bracelet, no other jewelry`. Por lo demás es excelente: **sentada directamente en el suelo** ✅ (su canon propio `FLOOR_SEAT_ANCHOR` — Throne en Suelo, no reclinada), horizonte nivelado ✅, cola en espiral escultórica ✅ |

### ✅ Lo que se mantiene impecable en las 7 de Look 07

- **Rosa firma** presente y dominante en las 7 — la cuota §8 se cumple con creces tras el Look 06 que no lo llevó.
- **Calzado:** plataforma stiletto rosa con aguja de metal en **todas** las poses donde el pie entra en cuadro. **Cero planos, cero block heel.** Footwear canon intacto.
- **Corsé estructural integrado al vestido** (no pieza aparte) legible en Standing, Seated, Glacial Command, POV y Odalisque — que era el punto delicado del concepto.
- **Bob platinado asimétrico, frente despejada, cero flequillo** en las 7 ✅.
- **Cejas oscuras taupe-grey visibles** en las 7 ✅ — la corrección del 11/08 (cejas invisibles) sigue firme.
- **Labios rojo-naranja sangre ultra gloss** ✅ · **cero tatuajes, cero piercings** ✅ · **cero sonrisa abierta** ✅ (el smirk frío se sostiene).
- **Cero collage, cero grilla, cero figura duplicada, cero teléfono.** Las anclas del motor v2.0 están haciendo su trabajo.
- **Fotorrealismo** sostenido en las 7 (piel con textura, no render).

---

## 📋 Look 08 · Electric Violet Reverie — 1/7 (solo Standing)

**Vestuario: impecable, punto por punto.** Catsuit PVC violeta UV con recortes en cintura y cadera ✅ · corsé underbust violeta con ojales cromados **encima** del catsuit ✅ · piping azul eléctrico en todas las costuras ✅ · choker cromado con dije ✅ · uñas coffin violeta chrome ✅ · labios magenta profundo ✅ · sombra violeta-chrome ✅ · escenario VIP sobre el escenario del club con neón violeta y azul ✅.

**Las botas:** las levanté como sospecha de "no llegan a la rodilla" y las amplié ×2 antes de escribirlo — **la caña termina justo bajo la rodilla, que es exactamente lo que significa knee-high.** Hebillas ✅, plataforma ✅, aguja de metal finísima ✅. **No es defecto.**

### 🔴 Lo que sí es defecto: la imagen no es fotografía, es render 3D

Ampliada la cara ×5 y comparada con la Standing del Look 07, la diferencia es categórica: **piel plástica sin un solo poro, pelo modelado, luz de videojuego, ojos de material sintético.** Lee como render tipo DAZ, no como fotografía editorial.

Contra qué choca, textual:
- BLOQUE A: `editorial realistic human skin texture subtle visible pores` · `human realistic face`
- Negative Prompt: `wax skin, plastic mannequin skin, doll face, mannequin face, uncanny doll-like appearance, glassy doll eyes, porcelain doll aesthetic`

Es la **única** de las 8 imágenes nuevas con este problema — las 7 del Look 07 son fotorrealistas con el mismo BLOQUE A. **La deriva no está en el texto.** Sospecha razonable, no confirmada: el escenario oscuro con neón saturado empuja al generador hacia render. **Recomiendo regenerarla** antes de que la app siga con las 6 poses restantes del look, porque si el hilo viene sesgado hacia render las 6 salen iguales.

---

## ✨ El sello de Gemini está en toda la flota (no es de este batch)

Las 8 imágenes traen un **destello ✦ de cuatro puntas semitransparente abajo a la derecha** — la marca de agua de Gemini. Antes de reportarlo como novedad fui a mirar las anteriores: **está también en L01, L03, L05 y L14**, o sea en todo lo materializado de Miss Doll. **No es regresión de este batch ni defecto del prompt.**

Importa igual por una razón: **es visible sobre fondo claro** y estas imágenes están destinadas a RRSS. Queda anotado como dato de la flota, para que usted decida si se recorta al publicar.

---

## 🧹 Dos cosas del repositorio que la auditoría destapó de paso

### 1. 🔴 El tracker de la galería estaba mintiendo en 8 looks

`### 📸 Imágenes (0/7 — Pendiente)` en **13 de los 14 looks**, con **52 imágenes reales en el índice de git**. El único actualizado era el Look 04 (por la nota del corsé de ayer). Este es exactamente el modo de falla registrado en `feedback_tracker_galeria_miente`: la Ama pide un look "pendiente", la app genera lo que ya existe, se quema cuota.

**Medido contra `git ls-files` y corregido en esta sesión:**

| Look | Tracker decía | Real |
|---|---|---|
| L01 Neon Pink Cage | 0/7 | **7/7** |
| L02 Pink Champagne Sovereign | 0/7 | **6/7** (falta Glacial Command) |
| L03 Oxblood Session | 0/7 | **7/7** |
| L04 Champagne Room | 6/7 real ✅ | 7/7 en disco, **6/7 útil** (Back View con el corsé ajeno) |
| L05 Chrome Sweat | 0/7 | **7/7** |
| L06 Ice Lavender Solitude | 0/7 | **7/7** |
| L07 Vogue Sovereign | 0/7 | **7/7** |
| L08 Electric Violet Reverie | 0/7 | **1/7** |
| L09-L13 | 0/7 | **0/7** ✅ correcto |
| L14 Chrome Cathedral | 0/7 | **3/7** |

**Total real: 52/98.** `update_galleries.py` regenera los README de carpeta y la galería maestra, pero **no toca este tracker** — es manual, y por eso envejece.

### 2. 🟠 La nota de auditoría de ayer volvió frágil el parseo del Look 04

El linter lo cazó: `el slot 'Back View' se resuelve 2 veces; 1 de ellas es basura corta`. El encabezado que escribí ayer —`### 📸 Imágenes (6/7 real — Back View viola el "no corset", ver nota)`— contiene el nombre del slot, y el bloque con backticks que viene después queda a tiro del parser de LV-App: extrae **25 caracteres** en vez del prompt real. El `REPLACE` lo salva porque el prompt bueno viene después, así que **no hay pérdida hoy** — pero es la misma clase de fragilidad que ya costó dos incidentes. Corregido: el encabezado ya no nombra el slot.

---

## 🔧 Estado y pendientes

| | |
|---|---|
| ✅ **Hecho 13/08** | Tracker `### 📸` de los 14 looks medido contra `git ls-files` y corregido (**52/98**), con tablas de imagen enlazadas donde hay archivo |
| ✅ **Hecho 13/08** | Encabezado del Look 04 desarmado para que el parser de LV-App no lo confunda con prompt inline |
| ✅ **Verificado 13/08** | Cobertura BLOQUE B **100%** en las 98 · linter `CRITICOS: 0` · **cero duplicados MD5** en las 8 nuevas |
| ✅ **Verificado 13/08** | Similitud de pose+setting entre los 14 looks (descontando anclas): **10-28% por slot, cero pares idénticos** — Miss Doll **no** tiene el problema de "todas las fotos iguales" que sí tenía Anaïs. Su repertorio de cámara funciona |
| ✅ **Cerrado sin marcar** | Botas knee-high del L08 (correctas) · Odalisque apaisado 1200×669 (mismo criterio deliberado que la Ama fijó para Anaïs el 12/08) · destello ✦ de Gemini (marca de agua de toda la flota) |
| ⏳ **Regeneración recomendada — 5 poses** | **L07** Back View · Side Profile · POV · Odalisque (las cuatro con deriva de prenda o accesorio) · **L08** Standing (render 3D) |
| ⏳ **Decisión suya** | Escribir el ancla `ASYMMETRY_LOCK` en `anclas_universales.json` e inyectarla en los looks con prenda asimétrica. **Sin ella, regenerar el L07 va a repetir la misma deriva** — el texto actual ya está al 100% y aun así falló |
| ⏳ **Heredado del 12/08** | **L04** Back View sigue con el corsé oxblood del Look 03 — pendiente de regenerar |
| ⏳ **Sin materializar** | 46 poses: L09, L10, L11, L12, L13 completos · L02 Glacial Command · L08 (6 de 7) · L14 (4 de 7) |
