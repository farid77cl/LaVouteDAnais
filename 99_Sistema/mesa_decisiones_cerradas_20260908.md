# 📋 Mesa de La Voûte — decisiones cerradas el 08/09/2026

*Evidencia. Estas siete tarjetas se sacaron de la Mesa por orden de la Ama*
*(«anda quitando las decisiones ya hechas») y quedan acá enteras: su pregunta,*
*lo que ella eligió, y qué se ejecutó. La Mesa es superficie de trabajo, no archivo.*

> 🪦 **No tiene fecha de muerte: es evidencia fechada y no se borra.**

---

## ¿Le pongo a Loreto umbrales duros de temperatura?

`loreto-temperatura` · grupo **relato**

**Contexto que se le presentó:**

Hoy Loreto frenó el v0.1 por una repetición verbatim — y la tibieza que a usted le molestó salió solo en amarillo. Su cabecera lo dice: «esto NO mide si calienta». Pero sí puede medir el piso: narración con cuerpo, apertura, decil mínimo. El v0.2 cerrado quedó en apertura 25,8% y narración con cuerpo 25,8%, bajo el v0.1 (34,6% / 34,4%) — y pasó igual, en amarillo.

**Ella eligió:** Sí, ponle piso

> *Que frene bajo cierto porcentaje de cuerpo en apertura y en el global. No mide si calienta, pero corta lo que va por debajo del suelo.*

**Qué pasó — hecho · 08/09 — y le encontré algo:**

Piso T0 puesto en medir_capitulo.py, con prueba antes que código. Frena por dos vías: global (% de narración que nombra un cuerpo) y apertura (primeras 500 palabras). Batería verde, y el Cap 1 v0.2 sigue pasando — lo verifiqué corriendo el medidor sobre el archivo real.

Y acá lo que tiene que saber, porque le cambia el sentido a lo que me pidió. Calibré sobre los 140 capítulos del repo con más de 1.500 palabras, y el número salió al revés de lo que las dos habríamos apostado: la v0.1 que usted llamó tibia puntúa 28,2% de cuerpo, y la v0.2 que Loreto y el Validador aprobaron puntúa 25,8% — menos. Un piso alto habría aprobado la tibia y frenado la buena.

O sea el cuerpo-por-frase no sigue a la temperatura que usted siente. Por eso el piso quedó donde quedó: en 8,0% global / 2,0% apertura, debajo de todo lo que usted ya aprobó y publicó (su capítulo publicado más frío va en 9,0 / 2,6). Así calibrado caza el vacío real — el peor borrador del repo va en 1,8 / 0,0 — y nada más.

Para que muerda de verdad hay que subirlo, y subirlo significa reprobar capítulos que usted ya publicó. Eso no lo decido yo: se lo dejé como tarjeta aparte.

---

## ¿Subo el piso de Loreto, sabiendo que reprueba capítulos que usted ya publicó?

`piso-mas-alto` · grupo **relato**

**Contexto que se le presentó:**

El piso quedó en 8,0% global porque su capítulo publicado más frío va en 9,0%. Así casi no muerde. Lo que gana cada escalón, medido sobre los 140 capítulos del repo:
• 12% — empieza a cazar borradores fríos de verdad, y reprueba 3 capítulos publicados (9,0 · 11,5 · 11,6)
• 15% — muerde bastante más, y reprueba 7 publicados
• 20,6% (el cuartil de abajo) — reprueba uno de cada cuatro capítulos del repo

Ninguno de esos publicados se vuelve a medir en la práctica: Loreto corre sobre capítulos nuevos. O sea el daño es de calibración, no operativo. Pero un linter que reprueba lo que usted firmó es el que enseña a ignorarlo, y esa lección este repo ya la pagó.

**Ella eligió:** Súbalo a 12

> *Caza borradores fríos reales. Tres capítulos publicados quedarían bajo el piso, declarados históricos.*

**Qué pasó — hecho · 08/09:**

Piso subido a 12,0 y commiteado. Los tres publicados que quedan debajo están declarados por nombre en PISO_HISTORICOS — no se corrigen, se declaran, misma política que usó el motor visual con L818/L823. Y les puse una prueba encima: si alguien mañana baja el piso «porque reprueba cosas publicadas», esa prueba se cae y obliga a volver a preguntarle.

Una cosa que no me pidió y no hice: dejé la apertura en 2,0. Usted eligió sobre la escala global, que era la que tenía el costo medido al lado. Subirla habría botado dos publicados más que nunca vio en la tarjeta. Se mueve cuando lo diga usted, con su costo a la vista.

---

## Ele L823 y L818 son casi el mismo párrafo. Los dos ya tienen fotos.

`clon-l823` · grupo **imagen**

**Contexto que se le presentó:**

48,4% de léxico común y 15 n-gramas verbatim. El L823 tiene sus 7 imágenes; el L818 tiene 2. El detector de clones nació el mismo día que se emitió ese lote y ese lote nunca pasó por él.

**Ella eligió:** Declararlo histórico

> *Se silencia y no vuelve a gritar. Un linter que reclama lo inarreglable enseña a ignorarlo.*

**Qué pasó — hecho · 08/09:**

Declarados. L818 y L823 entraron a anclas_universales.json → personajes.ele.rotacion_prenda.historicos_declarados, con el motivo escrito al lado — los dos están materializados y rehacerlos botaría generación ya pagada. Bajan a aviso, misma política que usó Miss Doll con su L72/L78. La regla sigue dura de ahí en adelante. Batería del motor: 124 ok · 0 fallas.

---

## Miss Doll L85 lleva botines de plataforma, y su §5.3 los sacó de la rotación el 11/08.

`md-l85-botines` · grupo **imagen**

**Contexto que se le presentó:**

El look está en 0/7 — no tiene ni una imagen. O sea hoy se arregla cambiando un token del prompt y no cuesta nada. Si se genera antes de que usted decida, ya no: pasa a ser una carpeta de imágenes que contradice su propia regla.

**Ella eligió:** Déjelo como excepción

> *Se declara por escrito para que ningún auditor lo vuelva a levantar.*

**Qué pasó — no había nada que hacer — y el error es mío:**

Fui a ejecutarlo y medí primero: el L85 ya no lleva botines. Se corrigió a bota a la rodilla el 07/09, con okey suyo, cuando el look todavía estaba 0/7. Busqué ankle boots en toda su galería: 23 apariciones, y 22 son del prompt negativo — o sea el término vetado, no el calzado. La única que es calzado real es el Look 68, que usted ya vetó aparte y se conserva como contraejemplo.

La tarjeta no debí escribirla. La saqué de una línea de pendientes de la memoria que llevaba un día desactualizada, y se la puse a decidir sin re-medir. Es exactamente el modo de falla que este repo tiene escrito: un estado sin fecha de verificación se vuelve mentira solo. Ya limpié la línea vieja.

---

## ¿El arnés (M5) sale de la taxonomía o se queda?

`m5-arnes` · grupo **imagen**

**Contexto que se le presentó:**

Usted dijo «fuera arnés» pero yo le había reportado que M5 era código muerto, y me equivoqué. Medí después: hay 11 looks vivos clasificados M5 (Ele L334, L359, L366, L483, L510, L522, L658, L811 · Miss&nbsp;Doll L31, L60, L64). Sí es alcanzable — basta escribir g-string en vez de thong. No lo saqué porque su orden se basaba en un dato mío que estaba malo.

**Ella eligió:** Que se quede

> *Once looks suyos ya lo usan. Sacarlo los reclasifica y le angosta la rotación.*

**Qué pasó — cerrada · no había nada que ejecutar:**

M5 se queda, como decidió. No hubo cambio de código: ya estaba en la taxonomía y los 11 looks vivos que lo usan siguen clasificados igual.

Lo que sigue abierto y usted no eligió arreglar: M5 es inalcanzable para el clasificador — su regex va detrás de M3, que matchea thong, y thong es obligatorio por el ancla de corte. O sea el código existe y nunca se asigna a un look nuevo. Usted tenía esa opción en la tarjeta y eligió la otra, así que lo dejo como está y queda anotado en la memoria.

---

## Renée: ¿guía, o además manda?

`renee-ordena` · grupo **relato**

**Contexto que se le presentó:**

Su nota pidió guía, condescendiente y seductora — no pidió órdenes. Conservé su invariante «ni una orden directa» porque el §8 del canon dice que una orden directa «rompe el personaje entero». Es una lectura mía y se cambia en un renglón.

**Ella eligió:** Guía, sin órdenes

> *Como quedó: propone, invita, se adelanta, da por hecho. Nunca manda.*

**Qué pasó — cerrada · confirmó lo que ya estaba:**

Sin cambios: Renée conduce y no manda, tal como quedó escrita. Su respuesta confirma el §8 del canon (una orden directa le rompe el personaje entero) en vez de derogarlo, y eso importa — esa lectura era mía y ahora es suya.

---

## El blog está parado esperando sus 4 llaves de OAuth.

`tumblr-llaves` · grupo **casa**

**Contexto que se le presentó:**

Sin ellas no hay línea base ni la prueba que decide la misión entera — si un blog marcado maduro aparece en la búsqueda por tags. Son cuatro y no dos: el conteo de seguidores solo sale si la llamada va firmada como dueña. Van a 06_RRSS/.env, que nunca se commitea. Y ojo, el avatar y el header se suben a mano siempre: la API no tiene endpoint, verificado el 07/09.

**Ella eligió:** Ármeme la guía paso a paso

> *Le dejo escrito dónde sacar cada una y dónde hacer clic.*

**Qué pasó — 🎉 CERRADA · el blog quedó conectado 08/09:**

Sus cuatro llaves sirven, verificado contra la API y no supuesto: la cuenta figura como dueña de lavoutedeanais.tumblr.com.

Línea base capturada — 0 seguidores · 1 post · descripción vacía. Guardada en 06_RRSS/metricas/linea_base_tumblr_20260908.md, rotulada como piso NO virgen porque el Cap 1 de Café ya estaba publicado.

Y nació lo que faltaba: 99_Sistema/scripts/rrss/tumblr_api.py. Hasta hoy el repo tenía el adaptador de posts y la cola, pero nadie que hablara con Tumblr — cero líneas de OAuth en todo el árbol.

La verificación destapó dos cosas que no estaban en ningún archivo. Están como tarjetas nuevas acá abajo.

---
