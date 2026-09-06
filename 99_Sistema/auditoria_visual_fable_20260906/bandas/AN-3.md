# Banda AN-3 — Anaïs Belland Looks 77-80
Auditadas 22 imágenes en 4 looks · 06/09/2026

> Evidencia fechada. Vive en esta carpeta con la rúbrica que la produjo. Look 76 sin imagen
> materializada — fuera de la banda. Resolución medida en las 22: 669×1200 (odaliscas 1200×669),
> 0,80 MP, sobre el piso de validez.
>
> **Criterio 🔴/🟡 aplicado (para que el número sea reproducible):** 🔴 solo cuando el prompt
> traía una cláusula que fija ESE atributo en concreto — `(the front of both legs perfectly smooth
> bare nylon, zero seam or line:1.4)`, `(genuinely sitting down, buttocks resting on the seat…:1.4)`,
> `exactly one hand visible in the frame`, `her gaze … never at the lens` (repetida dos veces en el
> slot 5), `both hips and shoulders down on the surface`, y el `:1.4` de escote/manga/ruedo. Todo lo
> demás (encaje que no aparece, cinturón que falta, tirantes que sobran, largo de pelo) es 🟡: el
> `GARMENT_CONSISTENCY` genérico existe en los 28 prompts, pero no nombra el atributo, y contarlo
> como ancla de todo lo convertiría en ancla de nada.

## Resumen
| Look | Poses | Desvío prompt | Continuidad | 🔴 con ancla | 🟡 sin ancla |
|---|---|---|---|---|---|
| 77 Chocolate y Camel en el Despacho | 1 | 8,1% | NO MEDIBLE (1 pose) | 1 | 2 |
| 78 Marfil y Oro Viejo en el Tocador | 7 | 11,6% | 72,7% (16/22) | 2 | 17 |
| 79 Midnight Navy en la Sesión de las Tres | 7 | 14,8% | 78,9% (15/19) | 3 | 23 |
| 80 Berenjena Latex y Guantes de Ópera | 7 | 7,2% | 84,2% (16/19) | 1 | 10 |
| **PROMEDIO** | 22 img | **10,4%** | **78,6%** (3 looks medibles) | **7** | **52** |

---

## Look 77 — Chocolate y Camel en el Despacho
- **Desvío:** 8,1% (Standing 3/37 — única pose)
- **Continuidad:** NO MEDIBLE (1 pose)
- **Fallas:**
  - 🔴 [D] el prompt pedía *"the stockings have ONE single seam and it runs strictly up the centre-BACK of each leg … NOT visible from the front; (the front of both legs perfectly smooth bare nylon, zero seam or line:1.4)"* → la imagen muestra una costura oscura nítida bajando por el FRENTE de las dos espinillas, del ruedo al zapato. Ancla presente, con peso, y aun así pintada de cara a cámara.
  - 🟡 [D] *"a slim antique-gold chain belt sitting on the hips"* → no hay cinturón de cadena; la pretina de látex va desnuda.
  - 🟡 [A] *"vivid deep crimson classic Hollywood red, high-shine wet gloss finish"* → labio mate en marrón-rojizo apagado, tono nude oscuro; es la única imagen de la banda donde el crimson no llega.
- **NO VERIFICABLE:** iris, suela roja, tanga, tajo trasero de la falda, copas de encaje del sujetador bajo la blusa.
- **Lo que salió BIEN y conviene no romper:** la falda lápiz de látex chocolate en alto brillo, ruedo a la rodilla y pretina alta moldeada, es exactamente el texto; la blusa camel es de verdad transparente y el sujetador se lee debajo; despacho de nogal, lámpara banker de latón, ventana con luz baja y vaso a medio beber — el setting completo.

---

## Look 78 — Marfil y Oro Viejo en el Tocador
- **Desvío:** 11,6% — Standing 13,8% (4/29) · Back 20,0% (4/20) · Seated 7,7% (2/26) · Side 10,0% (2/20) · Sovereign 17,4% (4/23) · POV 0% (0/21) · Odalisque 12,5% (3/24)
- **Continuidad:** 72,7% (16 estables / 22 evaluables)
- **Fallas:**
  - 🔴 [E] Sovereign Gaze — el prompt pedía *"her gaze angled off past the camera into the middle distance … her gaze drifting away past the edge of the frame and never at the lens"* (dos veces) → mirada clavada directo al lente. El slot 5 se convirtió en un segundo POV.
  - 🔴 [E] Odalisque — *"both hips and shoulders down on the surface … one arm folded under the head"* → torso levantado apoyado en el codo, cabeza en la mano; la otra mano en el muslo y no *"resting across the waist"*.
  - 🟡 [A] Standing, Back View, Side Profile — *"extremely long hip-length hair cascading past the shoulders"* → victory rolls con el pelo cortado a media espalda (omóplatos). En Seated, Sovereign, POV y Odalisque sí llega a la cintura.
  - 🟡 [A] Standing, Sovereign Gaze — *"beauty mark mole above upper left lip"* → el lunar está al lado DERECHO de la boca (izquierda del espectador), junto a la comisura. En Seated, POV y Odalisque está a la izquierda, donde va.
  - 🟡 [B] Standing, Back View, Odalisque — *"falling loose off both shoulders"* → peignoir puesto sobre los dos hombros, como una bata normal. Sovereign: cae de UN hombro. Solo Seated, Side y POV la llevan caída de ambos.
  - 🟡 [B] Standing, Back View — *"dramatic wide bell-shaped cuffs"* → manga obispo, globo fruncido en un puño cerrado. Seated, Side, Sovereign y POV sí tienen el volante campana.
  - 🟡 [B] Sovereign Gaze — *"a thin old-gold sash left untied"* → lazo anudado a la cintura, visible.
  - 🟡 [B] Side Profile — *"its sheer lace cups cut low into a deep plunge"* → copa de raso opaca, el encaje quedó solo en la banda inferior.
  - 🟡 [E] Back View — *"her honey blonde hair gathered forward over the far shoulder to leave the back bare"* → el pelo cae por la espalda.
  - 🟡 [E] Seated — *"both legs draped over one arm of the seat, the ankles crossed and pointed, the torso twisted back to the lens, one elbow hooked over the seat back"* → sentada de frente en un taburete sin brazos, piernas cruzadas a la rodilla, pies en el suelo, manos en los muslos. La única cláusula que sí cumple es la del `SEATED_ANCHOR` (peso de verdad en el asiento).
- **Quiebres de continuidad:**
  - [manga] Standing: manga obispo con puño fruncido → Seated / Side / Sovereign / POV: manga campana con volante → Odalisque: vuelve al puño fruncido.
  - [hombros del peignoir] Standing: sobre ambos hombros → Seated: resbalando → Side / POV: fuera de los dos → Sovereign: fuera de uno → Odalisque: sobre ambos.
  - [copas del sujetador] Standing: encaje transparente con UN broche dorado en el centro → Seated / POV / Odalisque: DOS broches → Side: copa de raso opaca.
  - [lazo] Standing: colgando suelto → Seated / Sovereign: anudado.
  - [largo de pelo] Standing: a media espalda → Seated / Sovereign / POV / Odalisque: a la cintura y más. (El peinado también cambia: victory rolls en Standing/Back/Side, ondas sueltas en el resto.)
  - [lunar] Standing / Sovereign: lado derecho → Seated / POV / Odalisque: lado izquierdo.
  - Estables (16): color y largo del peignoir · opacidad sheer · tanga · liguero y tirantes · medias marfil con banda de encaje · sin costura en ninguna pose · zapato marfil punta fina 12 cm sin plataforma · color del zapato · perlas · aros · iris ámbar · color de pelo · uñas oro pálido.
- **Lo que salió BIEN y conviene no romper:** POV a 0% — la única imagen de la banda sin una sola falla. Back View cumple el ancla de bata abierta de verdad: panel continuo por la espalda, transparente, se lee liguero, banda de encaje y la tanga con su única tira. Seated y Odalisque enseñan la suela roja. El tocador con frascos de cristal tallado y la copa con marca de labio están en las 7.

---

## Look 79 — Midnight Navy en la Sesión de las Tres
- **Desvío:** 14,8% — Standing 12,5% (4/32) · Back 17,4% (4/23) · Seated 25,0% (7/28) · Side 16,7% (4/24) · Sovereign 22,7% (5/22) · POV 0% (0/21) · Odalisque 9,1% (2/22)
- **Continuidad:** 78,9% (15 estables / 19 evaluables)
- **Fallas:**
  - 🔴 [E] Seated — el prompt pedía *"seated deep in a deep navy velvet reading chair with the shoulders dropped back against it … (genuinely sitting down, buttocks resting on the seat, never standing up:1.4) … NOT leaning against, perched on or propped against any nearby table, desk"* → está encaramada en el borde superior del sillón con las dos manos apoyadas en el escritorio detrás, cadera a la altura de la mesa, piernas cruzadas a la rodilla (pedía *"crossed at the ankle"*), cabeza nivelada (pedía *"tipped back and the throat drawn long"*). Es el mueble equivocado en Seated que el repo ya tiene documentado, con el ancla puesta.
  - 🔴 [E] Sovereign Gaze — *"exactly one hand visible in the frame … the other arm resting down along her body and out of shot"* → la segunda mano enguantada entra en cuadro abajo a la derecha.
  - 🔴 [E] Odalisque — *"shoulders and hips still down, both arms fallen open to the sides … a cushion or bolster under the small of the back"* → torso apoyado en el antebrazo, una mano en la cadera, sin cojín.
  - 🟡 [D] Standing, Back View, Seated, Side Profile, Sovereign — *"sheer navy-tinted HOLD-UP stockings"* (sin liguero en el BLOQUE B) → tirantes de liguero bajando de la tanga a la banda de la media, visibles a través de la malla en las 5 tomas. Prenda añadida que ningún prompt nombra.
  - 🟡 [D] Standing, Seated, Side Profile — *"a fine seam up the back of each leg"* → costura pintada por el FRENTE de la espinilla. Este look NO trae el candado de orientación de costura que sí trae el L77 — en el L77 falló con ancla, acá falla sin ella: el motor la puso en uno y no en el otro dentro del mismo batch.
  - 🟡 [B] Standing, Seated, Side Profile, Sovereign — *"silk-satin bra with fine tonal lace cups underwired into a plunge"* → copa de raso lisa, sin encaje. En POV y Odalisque las copas SÍ son de encaje.
  - 🟡 [A] Standing, Back, Seated, Side, Sovereign — *"hip-length hair"* → pin-waves a media espalda. POV y Odalisque: a la cintura.
  - 🟡 [A] Sovereign Gaze — *"warm honey amber iris … never grey and never washed out:1.4"* → iris avellana-oliva pálido, lavado. En Seated, POV y L80 sí es ámbar.
  - 🟡 [E] Back View — *"a low three-quarter angle from her right, the camera below the line of her hips … her hair swept entirely off the back"* → cámara a la altura de la cintura y el pelo cayendo por la espalda.
- **Quiebres de continuidad:**
  - [copas del sujetador] Standing: raso opaco liso → POV / Odalisque: encaje navy transparente con aro.
  - [costura de media] Standing: por el FRENTE de la espinilla → Back View: por detrás de la pantorrilla → Seated / Side: por el frente otra vez. La costura sigue a la cámara, no a la pierna.
  - [iris] Seated: ámbar → Sovereign / POV: avellana-oliva claro.
  - [largo de pelo] Standing: media espalda con victory roll → POV / Odalisque: cintura, suelto, sin rollo.
  - Estables (15): color y transparencia del vestido · escote recto con tirante fino · ruedo a media pantorrilla · tajo al lado izquierdo (en las 5 tomas donde se ve, siempre en la pierna izquierda — bien) · tanga · tirantes de liguero (estables en su error) · zapato navy charol punta fina, suela roja visible en Back/Seated/Side · guantes ópera navy en las 7 · colgante y aros · color de pelo · lunar al lado izquierdo en las 5 tomas donde se ve.
- **Lo que salió BIEN y conviene no romper:** POV a 0%. El tajo está en el lado correcto en todas las tomas, cosa rara. La malla se lee transparente desde atrás como pide el texto (Back View muestra tanga y banda del sujetador a través del vestido). Suela roja nítida en tres poses. El estudio nocturno con la lámpara verde, el secante y la pluma está en las 7 sin fallar una.

---

## Look 80 — Berenjena Latex y Guantes de Ópera
- **Desvío:** 7,2% — Standing 2,9% (1/34) · Back 11,1% (2/18) · Seated 6,5% (2/31) · Side 4,3% (1/23) · Sovereign 16,7% (3/18) · POV 5,6% (1/18) · Odalisque 3,3% (1/30)
- **Continuidad:** 84,2% (16 estables / 19 evaluables)
- **Fallas:**
  - 🔴 [E] Sovereign Gaze — *"exactly one hand visible in the frame"* → la segunda mano enguantada asoma abajo a la derecha, igual que en el L79.
  - 🟡 [D] Seated, Side Profile, Sovereign, Odalisque — el prompt lleva a la vez *"long aubergine latex opera gloves"* y *"nails: long stiletto-shaped fingernails lacquered in glossy antique silver"* → uñas de plata en garra saliendo POR ENCIMA de la punta de los guantes de látex. Es una contradicción del texto, no del generador: el perfil §5.6 manda omitir el token de uñas con guante cerrado (el L81 ya lo hace), y este batch lo dejó puesto.
  - 🟡 [D] Sovereign Gaze — *"a slim antique-silver collar at the throat with a single small ring"* → garganta desnuda, sin collar.
  - 🟡 [D] Back View — *"slim antique-silver collar"* → banda de látex berenjena con la anilla a la NUCA y una tira halter que baja hasta el corsé; en Standing/Seated/POV el collar es una banda gris metálica con la anilla al frente.
  - 🟡 [D] Standing — *"a fine dark seam up the back of each leg"* → línea de costura por el frente de la espinilla, entre la banda de la media y la caña de la bota. Única pose donde la espinilla se ve; en el resto la bota la tapa.
  - 🟡 [A] POV — *"beauty mark mole above upper left lip"* → con la cara ocupando un tercio del cuadro, no se ve lunar junto a la boca.
  - 🟡 [E] Back View — *"a tight waist-up crop"* → el encuadre baja hasta los muslos y la banda de la media.
  - 🟡 [E] Seated — *"both elbows on the knees and the chin resting on laced fingers"* → barbilla sobre los dedos entrelazados sí, pero los codos van al aire, no en las rodillas. (Observación fuera del conteo: rodillas abiertas de par en par; el `DRESS_LEG_CLOSURE` no aplica sin falda, así que no es falla de prompt, pero es el registro que la Ama tiene vetado en las tres muñecas.)
- **Quiebres de continuidad:**
  - [collar] Standing: banda gris metálica, anilla al frente → Back View: látex berenjena, anilla a la nuca, tira halter al corsé → Sovereign: sin collar → Odalisque: banda oscura con anilla al frente.
  - [uñas] Standing / POV: guante liso → Seated / Side / Sovereign / Odalisque: garras de plata atravesando el guante.
  - [lunar] Standing / Seated / Sovereign / Odalisque: lado izquierdo → POV: no visible.
  - Estables (16): corsé berenjena alto brillo · copas moldeadas y escote · canales de varilla plateados · busk de broches al frente · borde inferior en punta · panel de cordones plateado sobre raso berenjena (Back y Side) · tanga · 4 tirantes con clips · medias smoke-plum con banda · botas a la rodilla en charol berenjena, punta fina, cremallera interior visible en Side · altura de la caña justo bajo la rodilla · tapa de tacón plateada · guantes en las 7 · aros · iris ámbar · color y largo de pelo.
- **Lo que salió BIEN y conviene no romper:** el corsé es la prenda más estable de la banda — canales, busk, punta y lacing idénticos en 7 de 7, y el Back View lee el panel de cordones sobre raso exactamente como el texto. Odalisque cumple las 7 cláusulas de pose (mesa de marquetería, cadera, piernas apiladas, antebrazo, mano en muslo, mirada). Standing a 2,9% es la mejor toma de cuerpo entero de la banda.

---

## Patrones de la banda

1. **La costura de media sigue a la cámara, no a la pierna — con ancla y sin ella.** Aparece pintada por el frente de la espinilla en L77 Standing (🔴, candado `:1.4` presente), L79 Standing/Seated/Side y L80 Standing (🟡, sin candado). Cuando la toma es de espaldas (L79 Back), la costura va por detrás: el generador pone la línea donde la ve el lente. Dos cosas para el motor: (a) el candado de orientación estaba en L77 y no en L79/L80 del mismo batch — el inyector no lo aplicó parejo; (b) donde sí estaba, falló igual — reforzar, como manda la Ama, o quitar la costura del BLOQUE B en tomas frontales y describir *"seamless sheer stockings"* + costura solo en el Back View.

2. **Lo que el BLOQUE B no fija con forma, el generador lo reinventa pose a pose.** Manga del peignoir (obispo ↔ campana) y hombros (puesto ↔ caído) en L78; copas del sujetador (raso ↔ encaje) en L78 y L79; collar (metal/frente ↔ látex/nuca/halter ↔ ausente) en L80. Es la familia L746/L707/L86/L87 de la rúbrica, intacta. Ninguno de esos atributos tiene candado propio; el `GARMENT_CONSISTENCY` genérico los cubre en teoría y en la práctica no los sostiene.

3. **Slot 5 (Sovereign Gaze) es el slot más frágil: 4 de las 7 fallas 🔴 de la banda viven ahí o en Odalisque.** L78 mira al lente (la cláusula estaba dos veces). L79 y L80 meten la segunda mano en cuadro. El diferenciador duro del slot contra el POV (mirada fuera) se perdió en 1 de 3, y la mano única en 2 de 3.

4. **Seated sigue siendo el mueble equivocado.** L79: encaramada al escritorio con el sillón delante, ancla `:1.4` presente. L78: sentada de verdad pero en otra postura por completo (taburete sin brazo para una pose que pedía piernas sobre el brazo). El `SEATED_ANCHOR` evita que se pare; no evita que se encarame ni que cambie el mueble.

5. **Largo de pelo y lunar: el ADN vacila dentro del mismo look.** Pelo a media espalda en 8 de las 22 imágenes (todas con victory rolls: el rollo parece "comerse" el largo), a la cintura en el resto. Lunar cambia de lado en L78 (2 de 7) y desaparece en L80 POV. Vale un candado de largo (`hair falling past the waist even when set in victory rolls`) porque el texto actual solo dice *"hip-length"* una vez y sin peso.

6. **Tres contradicciones que vienen del texto, no del píxel — y son las más baratas de arreglar:**
   - L80: token de uñas + guantes cerrados → garras de plata a través del látex en 4 de 7. Regla §5.6 ya existe; el batch no la aplicó.
   - L79: *"hold-up stockings"* en BLOQUE B y el generador añade liguero en 5 de 7 — probablemente porque el resto de los prompts de Anaïs de la ventana (L78, L80) lo llevan y la malla transparente pide "algo" a la altura del muslo. Si se quiere hold-up, decirlo en negativo (`no suspender straps, no garter belt`).
   - Fugas de otro personaje / otro look en el texto de Anaïs: L80 (7 prompts) *"the navel piercing and the hip rune tattoos stay concealed"* — Anaïs no tiene tatuajes ni piercings (§2); L80 POV *"the clasp of the fur at her throat"* — no hay piel en el look; L79 POV *"the pearl drop at her ear"* con el BLOQUE B en *"antique-gold drop earrings"*. No produjeron defecto visible esta vez, pero son ruido que el `outfit.py modularidad` no ve porque vive en el texto de pose, no en la lógica.

7. **Lo que sí está sólido y no hay que tocar:** prenda principal (falda látex L77, peignoir L78, slip de malla L79, corsé L80) en color, material, brillo y ruedo — 0 fallas de arquitectura en 22 imágenes; calzado 12 cm sin plataforma y punta cerrada en las 20 tomas donde se ve, suela roja nítida en 6; setting completo en las 22; guantes ópera 14 de 14. El POV es el slot más fiel de Anaïs: 0% en L78 y L79, 5,6% en L80.

FABLE_AUDIT_RESULT:{"banda":"AN-3","looks":4,"imagenes":22,"desvio_promedio":10.4,"continuidad_promedio":78.6,"criticos_con_ancla":7,"reporte":"99_Sistema/auditoria_visual_fable_20260906/bandas/AN-3.md"}
