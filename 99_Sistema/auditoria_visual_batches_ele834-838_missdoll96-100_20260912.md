# Auditoría visual — últimos 2 batches con imágenes materializadas (12/09/2026)

Evidencia dateada, no se borra (regla 12). Alcance: los dos batches de imágenes reales más recientes al momento de correr esta auditoría — **Ele L834-838** (`L834_L838_prueba_manifiesto.json`) y **Miss Doll L96, 97, 99, 100** (`MD_L96_L100_variedad_de_arquitectura.json`, L98 sin imágenes). Anaïs L96-100 sigue en 0/7, fuera de alcance.

**Método:** tres fuentes independientes, reportadas por separado y SIN arbitrar cuál hallazgo es real — esa decisión es de la Ama o de una pasada adicional verdaderamente independiente ([[feedback_nunca_auto_auditarse]] en auto-memoria, corrección de la Ama 12/09/2026). Donde dos fuentes independientes tocan el mismo punto se anota la coincidencia como dato, no como confirmación.

1. **Lectura manual propia** (Ele, antes de despachar a Fable) — mirando las imágenes descargadas on-demand vía sparse-checkout.
2. **Auditoría ciega de Fable** — subagente sin contexto de esta sesión, con solo el canon (`identidad_ele.md` §I-II, `ele.md` §5, `miss_doll.md` §5, reglas 04/05) y las imágenes. Reporte íntegro abajo, sin editar.
3. **`auditar_canon_flota.py` / motor de prompts** — script determinista que audita el TEXTO de los batches (locks declarados: OPAQUE_LOCK, GLOSS_LOCK, CONSISTENCY_LOCK), no las imágenes. Toca la causa, no el síntoma.

---

## Fuente 1 — Lectura manual propia (parcial, no exhaustiva — se detuvo al llegar la orden de auditoría ciega)

- **L835 (Ele):** poses `standing`, `back_view`, `seated`, `side_profile`, `odalisque`, `ditzy` muestran personas reales de fondo (maquilladoras, un fotógrafo con cámara reflejado en el espejo de `odalisque`); `back_view` muestra un entorno de backstage con cables sueltos, sillas plegables y piso de concreto — lee industrial/clutter, no penthouse ni estudio minimalista.
- **L835:** calzado sandalia stiletto plateada de tira fina — altura visualmente menor que el resto del batch (834/836/837/838 muestran tacón/plataforma claramente más agresivos); duda razonable sobre si cumple el mínimo declarado.
- **L837 (Ele):** marca tipo tatuaje floral pequeño visible en ambos hombros en `back_view`, no descrita en el ADN (que solo registra el tatuaje de runas en cadera/bikini line y el sleeve de antebrazo).
- **L834/836/837/838 (Ele):** tatuaje de runas en cadera/bikini line presente y consistente donde la prenda lo permite ver.
- Miss Doll L96/97/99/100: no alcanzada por la lectura manual antes de pasar a Fable.

## Fuente 2 — Auditoría ciega de Fable (íntegra, sin editar)

> 60 PNG abiertos uno por uno, canon leído antes de mirar imágenes. Reporte completo del subagente:

### ELE

**L834 — Gunmetal Boardroom en Vidrio (7/7)**
Calzado stiletto punta afilada sin plataforma, ~12cm, cumple en las 5 poses que encuadran pie. Blazer con un solo hombro cubierto en `pov` (asimétrico) vs. dos mangas largas en el resto. Drift de uñas: gunmetal en `standing`, French clásica en `seated`/`ditzy`/`pov`. Labios malva/apagado en `standing` vs. hot pink glossy en el resto. Color dominante negro (no viola tope de 2 consecutivos, L835 rompe con zafiro).

**L835 — Sapphire Slip en el Vestier (7/7)**
Setting: prompt declara "mirrored dressing room backstage before a runway call"; render = camarín real con mesas plegables, cables, cajas, percheros; `back_view` muestra techo de galpón con vigas/ductos expuestos y piso de concreto — industrial explícito, prohibido por `identidad_ele.md` §I. Personas de fondo en 6/7 poses (`odalisque` incluye un fotógrafo con flash reflejado). Drift de largo del vestido: tobillo con tajo (`standing`) → asimétrico a la rodilla (`back_view`) → mini a medio muslo (`seated`, `side_profile`, `odalisque`) — cuatro largos distintos contra un solo "hem cut high on outer thigh" declarado. Calzado sandalia stiletto plateada sin plataforma ~12-15cm, cumple. Drift de uñas (declarado "French XXXL sapphire-blue", aparecen azul sólido / French blanca / plateado pálido según pose). Tatuaje de runas se extiende por todo el muslo en `odalisque`, más allá de "hip crease and bikini line" declarado.

**L836 — Oxblood Harness en el Estudio (7/7)**
Setting industrial declarado EN EL PROPIO PROMPT ("converted warehouse studio, single industrial spotlight") y renderizado en las 7: ladrillo con columnas de acero oxidado, foco de cine en trípode, muro de hormigón crudo, lámpara colgante industrial, maquinaria de fondo — choca con "NADA DE INDUSTRIAL" de `identidad_ele.md` §I; el defecto nace en el prompt, no solo en Gemini. `ele_836_seated.png` es visualmente la misma toma de pie que `standing` (mismo encuadre, manos en cadera) — falta la pose Seated real. Color oxblood casi idéntico al cherry red del pelo/ADN — caso límite de "rojo dominante" a decidir a mano. Drift de prenda: declarado tira única con O-ring vs. renderizado como sujetador triangular completo + arnés. Posible texto/lettering en zona lumbar de `back_view`, sobre la tanga (verificar a mano — prohibición "0 texto"). Drift de uñas entre poses. Calzado sandalia negra con plataforma ~5"+tacón ~16cm, cumple lo declarado.

**L837 — Violeta Eléctrico en la Suite (7/7)**
Sin hallazgos de canon más allá de drift de uñas (violeta sólido / degradé / French con ombré / French clara según pose). Vestido, escote, tajo, cadena, pendiente asimétrico, calzado y setting coherentes con lo declarado en las 7 poses.

**L838 — Chrome Editorial en el Cyclorama (7/7)**
Drift de manga: bodysuit cromo de manga larga en `standing`/`back_view`/`side_profile`, sin mangas (sisa desnuda) en `seated`/`ditzy`/`pov`/`odalisque` — el BLOQUE B no fija largo de manga. Tatuaje adicional (blackwork) en la parte alta de ambos glúteos en `back_view`, no descrito en el ADN. Drift de uñas. Calzado pumps cromo sin plataforma ~12cm, cumple. Riesgo estético (no violación) — cuello alto + cremallera frontal roza registro sci-fi.

**Transversal Ele:** ninguna manicura se sostiene idéntica en las 7 poses de ningún look; posición del tatuaje de brazo no está fijada por ningún token y varía de brazo/tamaño entre poses.

### MISS DOLL

**Hallazgos de archivo:** nombres `miss_doll_096_*`/`_097_`/`_099_` llevan cero a la izquierda, contra `miss_doll.md` §1 (N sin cero a la izquierda) — L100 no tiene el problema por ser 3 dígitos. `miss_doll_100_glacial_command.png` y `miss_doll_100_side_profile.png` son el mismo archivo (md5 idéntico) — falta la Glacial Command real de L100. L96 sin `side_profile` (6/7). L99 sin `back_view` ni `odalisque` (5/7).

**L96 — Sapphire Mirror Dress en el Penthouse (6/7)**
Rosa firma presente en las 6 poses, choker/pulsera/pendientes/uñas/labios/sombra/cabello coherentes con lo declarado. Calzado: plataforma cromada baja (~3-4cm) + tacón fino ~13-15cm — tiene plataforma pero no es la "8-inch platform"/Pleaser 6" declarada; nota transversal a todo el batch de Miss Doll (el token no se renderiza literal en ninguna imagen). Drift de escote: halter plunge sin anilla (`standing`, `glacial_command`) vs. keyhole cerrado con O-ring cromado (`seated`, `pov`, `odalisque`). Piel bronceada en 3 poses vs. "pale cold porcelain" declarado (solo `glacial_command` es porcelana). `odalisque`: sonrisa cálida mostrando dientes — "warm smile" está en el negative base.

**L97 — Jade Cabana Micro Bikini (7/7)**
Rosa firma, anilla cromo, tanga g-string, tobillera, uñas, labios y setting coherentes. **`miss_doll_097_seated.png`: piernas abiertas ~90°** — orden explícita de la Ama 29/08/2026 (`miss_doll.md` §4) de eliminar esa pose en todo look. Drift de calzado: pumps punta cerrada en 5 poses vs. sandalia punta abierta T-strap en `odalisque` (el propio BLOQUE B ya es contradictorio). Drift de cinta rosa: declarada solo cadera izquierda, aparece en ambas caderas en `back_view`/`pov`. Piel bronceada en 4 de 7 poses. `pov`: segunda mano con pulsera visible además de la declarada.

**L99 — Champagne Robe sobre Guêpière en el Loft (5/7, sin back_view ni odalisque)**
Rosa firma, puños acampanados, cadena oro, bob coherentes en las 5. **`miss_doll_099_seated.png`: labios rosa-nude glossy** (declarado deep berry; "nunca rosado, nunca nude" es regla explícita §5.4/§9) **+ sonrisa cálida amplia** (negative base). `side_profile` también con labio nude/rosado. Drift de guêpière: underbust declarado, renderizado overbust con copas en `standing`/`glacial_command`/`pov`, banda pequeña en `seated`, apenas visible en `side_profile`; en `pov` atado por delante contra "laced up the back" declarado. Suela roja tipo Louboutin en `standing`/`seated`/`side_profile` (declarada hot-pink undersole, y L96/L97/L100 sí muestran rosa — atribución de diseñador, prohibida en la estética editorial). Setting `standing`: loft de ladrillo expuesto con cojines de piso, lee bohemio-industrial.

**L100 — Onyx Slip Dress en el Estudio (7 archivos, 6 únicos)**
Malla negra, cordón rosa, bralette+g-string, cadena, medias con costura, uñas, labios, sombra, piel, cyclorama y calzado coherentes con lo declarado. Glacial Command ausente (ver hallazgo de archivo arriba). Costura de la media por delante en `standing` (correcta por detrás en `back_view`/`side_profile`/`odalisque`). Equipo de estudio (C-stand cromado) visible en primer plano en `pov`. `seated`: medias con liga/tirante visible, contra "sin liguero" declarado. `back_view`: cuerpo notoriamente más delgado/plano y piel más cálida que el resto del set — riesgo de "otra persona".

## Fuente 3 — `auditar_canon_flota.py` (audita el TEXTO del batch, no la imagen)

Sobre Ele (extracto, L834-841):
```
L834: ARQUETIPO CUBIERTO (blazer, corporate) sin OPAQUE_LOCK · SILUETA MATE-PRONE (blazer) sin GLOSS_LOCK · PRENDA CON DRIFT (blazer, shirt) sin CONSISTENCY_LOCK
L837: ARQUETIPO CUBIERTO (column gown, gala, gown) sin OPAQUE_LOCK · PRENDA CON DRIFT (column, gown) sin CONSISTENCY_LOCK
L838: PRENDA CON DRIFT (bodysuit) sin CONSISTENCY_LOCK
```
Sobre Miss Doll: `auditados=35 violaciones=0 no_auditables=75` — el script no marca L96/97/99/100 (probablemente entre los "no auditables": son looks sin manifiesto tipado, el script solo audita looks con datos estructurados).

**Lectura cruzada (dato, no verificación):** el script marcó a L834 y L838 por falta de `CONSISTENCY_LOCK` en la prenda ANTES de que Fable, mirando las imágenes, reportara exactamente ese síntoma — drift de manga/hombro en ambos looks. Convergencia entre una fuente que lee texto y una que lee píxeles, sin que ninguna haya visto el hallazgo de la otra.

---

## Qué decide la Ama, no yo

- Si el oxblood de L836 cuenta como "rojo dominante" contra el pelo (caso límite de paleta).
- Si el posible texto en la zona lumbar de `ele_836_back_view.png` es una violación real de "0 texto" (necesita zoom/confirmación).
- Si el backstage de L835 y el warehouse de L836 se regeneran, o se archivan como el contraejemplo que ya existe para Miss Doll L68.
- Qué hacer con el déficit estructural de plataforma en TODO el batch de Miss Doll (el token "8-inch platform"/Pleaser 6" no se renderiza literal en ninguno de los 4 looks) — es un patrón del motor, no de un look suelto.
