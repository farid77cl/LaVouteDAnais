# -*- coding: utf-8 -*-
"""Fichas de outfit (ingles) para los looks del ARCHIVO HISTORICO que nunca tuvieron prompts.

FUENTE: el campo `- **Outfit:**` / `- **Tacones:**` / `- **Ambientación:**` en espanol de cada
look en `00_Ele/galeria_outfits_archivo.md`. Estos looks se registraron cuando el canon de 7
poses todavia no existia, asi que quedaron con descripcion y sin un solo prompt.

ALCANCE: L85-L199 unicamente. **L1-L84 quedan FUERA por orden directa de la Ama (20/07/2026)**
y por canon: son era Helena (pelo negro, gotica) — capitulo cerrado, no se resucita.

CRITERIO DE TRADUCCION (el canon vigente MANDA sobre la descripcion vieja):
 - GUANTES BORRADOS siempre (L88, L100, L140, L156 los traian). Manos desnudas es absoluto.
 - Tela natural mate PROHIBIDA: la "seda" de las fichas de lenceria/gala se rinde como
   `high-gloss silk-satin` / `liquid satin` (el canon admite wet-satin y silk-satin ahi).
 - Calzado SIEMPRE explicito y con altura nombrada, en los 7 prompts.
 - Nada de texto ni nombres sobre la prenda (el L114 traia una placa 'ASSET V3': se queda la
   placa, se va el texto).
 - Las unas son las French XXXL del Bloque A: se descarta cualquier una alternativa de la
   ficha vieja (el L85 pedia unas de leopardo).
 - Lo que ya vive en el Bloque A (rostro, pelo, labios, "Sacha Massacre canon") NO se repite.
 - Ambiguedades del tipo "vinilo rojo cereza O negro espejo" se resuelven al primer termino
   nombrado y queda anotado en el comentario del look.

Campos por look:
  outfit  : clausula de vestuario COMPLETA en ingles, cerrando SIEMPRE en el calzado.
  shoe    : descriptor corto del calzado -> footwear_echo en Back View y Odalisque.
  setting : ambientacion que se appendea tras la direccion de pose.
  seat/wall/surface : mobiliario REAL del setting (rotate_poses los inyecta en las variantes).
  seam    : True si el look lleva medias con costura trasera.
  wrap    : "slip"/"closed" si hay prenda envolvente de frente abierto (bata/kimono).
"""

FICHAS = {

# ---------------------------------------------------------------- L85-L100
# L85: la ficha ofrecia "rojo cereza O negro espejo" -> se toma el primero (cherry red).
# Los "leggings opcionales" se descartan: un prompt no puede llevar una prenda opcional.
85: dict(
    outfit="a cherry red high-gloss vinyl micro mini dress, ultra-tight and almost restrictive, "
           "sleeveless with a rounded scoop neckline, seamless smooth surface moulded to the "
           "silicone curves, hemline at upper thigh, "
           "11-inch clear acrylic platform stiletto heels with cherry red vinyl ankle straps",
    shoe="clear acrylic platform stiletto heels with cherry red vinyl ankle straps, 11-inch",
    setting="a mirror-walled high-fashion nightclub lounge at night, saturated magenta and red "
            "neon washing the glossy vinyl",
    seat="a red lacquered lounge stool", wall="a mirrored club wall", surface="a black lacquer bar top"),

86: dict(
    outfit="a lilac high-gloss liquid-satin semi-sheer blouse tucked in tight, and a black mirror "
           "vinyl high-waisted pencil tube skirt, ultra-fitted to knee, "
           "a black velvet choker and fine-framed angular glasses, "
           "9-inch black patent needle stiletto pumps with a pointed toe and no platform",
    shoe="black patent needle stiletto pumps, 9-inch, pointed toe, no platform",
    setting="a floor-40 Sanhattan corporate office at dusk, floor-to-ceiling glass and the "
            "Cordillera behind her",
    seat="an ergonomic executive chair", wall="a glass office partition", surface="a lacquered desk"),

87: dict(
    outfit="a midnight blue high-gloss vinyl flight-attendant uniform: an ultra-fitted tailored "
           "jacket with chrome insignia hardware, a matching ultra-tight vinyl mini pencil skirt, "
           "and a regulation pillbox cap pinned to the hair, "
           "11-inch black patent platform stiletto heels with a needle heel",
    shoe="black patent platform stiletto heels, 11-inch, needle heel",
    setting="a private jet cabin interior of cream leather and polished chrome, warm directional "
            "cabin light",
    seat="a cream leather cabin seat", wall="a polished cabin bulkhead", surface="a chrome galley counter"),

# L88: la ficha traia "guantes de malla negra hasta el antebrazo" -> BORRADOS (canon).
88: dict(
    outfit="a black high-gloss vinyl strapless overbust corset, ultra-cinched with visible boning, "
           "and a black mirror latex midi skirt with an extreme thigh-high side slit, "
           "black back-seamed sheer stockings held by concealed suspenders, "
           "11-inch black patent platform stiletto heels with a sharp pointed toe",
    shoe="black patent platform stiletto heels, 11-inch, sharp pointed toe",
    setting="a white-walled contemporary art gallery opening at night, track spotlights raking "
            "the glossy black surfaces",
    seat="a gallery bench", wall="a white gallery wall", surface="a plinth", seam=True),

89: dict(
    outfit="a burgundy wet-look vinyl mini dress, ultra-tight with a deep plunging neckline and "
           "a moulded seamless bodice, hemline at upper thigh, "
           "9-inch burgundy patent stiletto boots, knee-high, with a needle heel and pointed toe",
    shoe="burgundy patent knee-high stiletto boots, 9-inch, needle heel, pointed toe",
    setting="a deep burgundy velvet imperial salon, gilded mouldings and low warm lamplight",
    seat="a burgundy velvet chaise", wall="a panelled salon wall", surface="a gilded console"),

90: dict(
    outfit="a gold chrome mirror-finish latex bodysuit, high-cut at the hip, long-sleeved and "
           "moulded seamlessly to the body with a mirror-bright surface built to catch every "
           "studio light, "
           "8-inch rose gold chrome platform stiletto sandals with ankle straps",
    shoe="rose gold chrome platform stiletto sandals, 8-inch, ankle straps",
    setting="a minimalist white photographic studio with high-end rim lighting and hard shadows",
    seat="a white studio cube", wall="a white cyclorama wall", surface="a white studio riser"),

91: dict(
    outfit="a dark cyan high-gloss vinyl asymmetric crop top with transparent PVC panels, and "
           "matching high-waisted cyan vinyl leggings with mirror-chrome silver side stripes, "
           "hair in a high technical ponytail with a chrome cuff, "
           "8-inch mirror-chrome silver platform stiletto ankle boots",
    shoe="mirror-chrome silver platform stiletto ankle boots, 8-inch",
    setting="a luxury minimalist yoga studio with pale wood floors and floor-to-ceiling windows",
    seat="a low bench", wall="a studio mirror wall", surface="a wooden platform"),

# L94: la ficha no nombraba calzado. Se le asigna el canonico del arquetipo retro (canon:
# JAMAS sin tacon), y el "collar de cuero con candado" se conserva como accesorio.
94: dict(
    outfit="a flesh-tone latex open-bottom girdle with visible suspender tabs, a white satin-finish "
           "bullet bra with sharply conical moulded cups, a black leather collar closed with a "
           "polished brass padlock, and sheer nude stockings clipped to the girdle, "
           "12-inch black patent stiletto pumps with a pointed toe and no platform",
    shoe="black patent stiletto pumps, 12-inch, pointed toe, no platform",
    setting="a 1950s domestic interior restaged in high-gloss editorial light, pale walls and "
            "chrome fittings",
    seat="a chrome kitchen chair", wall="a pale panelled wall", surface="a formica counter"),

95: dict(
    outfit="a mirror-silver high-gloss vinyl micro dress, ultra-tight and fully reflective, worn "
           "under a transparent PVC harness with polished silver hardware, "
           "11-inch mirror-chrome silver platform stiletto boots, knee-high",
    shoe="mirror-chrome silver platform stiletto boots, knee-high, 11-inch",
    setting="a liquid-metal editorial studio, silver seamless backdrop and hard specular lighting",
    seat="a chrome stool", wall="a brushed steel wall", surface="a polished steel plinth"),

96: dict(
    outfit="a polished chrome mirror-effect rigid bustier with extreme push-up moulding and a "
           "subtle underbust curve, and a liquid silver vinyl micro thong with fine chain side "
           "straps, "
           "11-inch polished stainless steel needle stiletto heels with a pointed toe",
    shoe="polished stainless steel needle stiletto heels, 11-inch, pointed toe",
    setting="a mercury-toned editorial set, liquid metal backdrop and cold specular rim light",
    seat="a steel bench", wall="a mirrored steel wall", surface="a mercury-finish pedestal"),

97: dict(
    outfit="a liquid black latex bodysuit with an ultra-deep V neckline plunging to the navel, "
           "reinforced seams creating a gravity-defying push-up effect, the material so glossy it "
           "reads as wet, long-sleeved and high-cut at the hip, "
           "12-inch black vinyl thigh-high stiletto boots with a metal heel",
    shoe="black vinyl thigh-high stiletto boots, 12-inch, metal heel",
    setting="a black void editorial set with a single hard key light and deep specular highlights",
    seat="a black lacquer cube", wall="a matte black wall", surface="a black lacquer plinth"),

98: dict(
    outfit="a bubblegum pink and mirror-white high-gloss vinyl cheerleader uniform: a short halter "
           "top with a rigid stand collar and a micro pleated skirt in rigid PVC, holding reflective "
           "vinyl-strip pompoms, "
           "11-inch white patent platform stiletto heels",
    shoe="white patent platform stiletto heels, 11-inch",
    setting="a glossy white gymnasium set with saturated pink accent lighting",
    seat="a bleacher bench", wall="a white gym wall", surface="a polished court floor"),

99: dict(
    outfit="a one-piece dark cherry latex bodysuit with neon pink trim and waist cutouts at both "
           "sides emphasising the silhouette, matching neon pink latex wristbands, the latex "
           "surface carrying a high specular sheen, hair in two high wavy pigtails, "
           "11-inch platform stiletto heels with a clear acrylic base and neon pink latex straps",
    shoe="platform stiletto heels with clear acrylic base and neon pink latex straps, 11-inch",
    setting="a luxury performance gym with chrome equipment and saturated pink neon",
    seat="a padded weight bench", wall="a mirrored gym wall", surface="a chrome equipment frame"),

# L100: la ficha traia "guantes de opera en vinilo azul cobalto" -> BORRADOS (canon).
100: dict(
    outfit="a cobalt blue mirror-finish PVC external wasp-waist corset, severely cinched with "
           "visible boning, and a matching cobalt latex pencil skirt with a strategic side slit, "
           "hair partly pinned with chrome clasps, "
           "12-inch cobalt blue vinyl thigh-high boots with a silver chrome needle stiletto heel",
    shoe="cobalt blue vinyl thigh-high boots, 12-inch, silver chrome needle stiletto heel",
    setting="a cobalt-lit editorial studio, seamless backdrop and extreme specular reflection",
    seat="a chrome bench", wall="a cobalt lacquer wall", surface="a chrome plinth"),

# ---------------------------------------------------------------- L110-L128
110: dict(
    outfit="a black mirror PVC micro bodycon dress with a sweetheart neckline, ultra-tight, worn "
           "open under a high-gloss cherry red vinyl trench coat with a wide belt, black fishnet "
           "stockings on a cherry red vinyl suspender belt, and a cherry red vinyl choker with a "
           "chrome moon pendant, "
           "11-inch chrome red platform stiletto heels",
    shoe="chrome red platform stiletto heels, 11-inch",
    setting="a rain-slick city street at night under red neon signage, wet asphalt reflections",
    seat="a low concrete ledge", wall="a neon-lit wall", surface="a wet stone step", wrap="slip"),

111: dict(
    outfit="a cyan chrome mirror-finish vinyl structured bralette with high-profile moulded cups "
           "and wide PVC straps, a holographic rainbow PVC bodycon micro skirt reading dominant "
           "cyan, worn under a floor-length smoked transparent PVC trench with neon cyan trim, "
           "pearlescent fishnet stockings on a cyan vinyl suspender belt, and a cyan PVC choker "
           "with a chrome moon pendant, "
           "11-inch cyan chrome platform stiletto heels",
    shoe="cyan chrome platform stiletto heels, 11-inch",
    setting="a cyan-lit penthouse corridor at night, smoked glass and hard neon reflections",
    seat="a smoked glass bench", wall="a smoked glass wall", surface="a chrome console", wrap="slip"),

112: dict(
    outfit="a gold chrome mirror-vinyl mini dress with white ruffled latex trim at the neckline "
           "and hem, ultra-fitted, and a gold vinyl choker with a chrome moon pendant, "
           "11-inch clear platform stiletto heels with chrome gold heels",
    shoe="clear platform stiletto heels with chrome gold heels, 11-inch",
    setting="a modern luxury kitchen in Sanhattan, marble island and polished chrome appliances",
    seat="a chrome bar stool", wall="a marble backsplash", surface="a marble kitchen island"),

113: dict(
    outfit="a skin-tight neon pink heavy-duty latex sports bra and matching high-waisted latex "
           "workout leggings with black mesh panels at the thigh, and a neon pink latex choker "
           "with a silver O-ring, "
           "11-inch clear platform stiletto heels with neon pink vinyl straps",
    shoe="clear platform stiletto heels with neon pink vinyl straps, 11-inch",
    setting="a high-tech luxury neon-lit gym with mirrored walls",
    seat="a padded bench", wall="a mirrored gym wall", surface="a chrome rack"),

# L114: la placa del choker se conserva SIN texto (canon: 0 texto/nombre sobre la prenda).
114: dict(
    outfit="a mirror-white vinyl mini skirt, high-waisted, a translucent leopard-print liquid-satin "
           "blouse knotted at the waist, a wide leather belt with a gold buckle, a white leather "
           "choker with a blank polished gold plaque bearing no lettering, and gold cat-eye "
           "sunglasses, "
           "8-inch white patent lace-up platform stiletto boots",
    shoe="white patent lace-up platform stiletto boots, 8-inch",
    setting="a floor-40 Sanhattan luxury office at sunset, Cordillera view through full-height glass",
    seat="an executive chair", wall="a floor-to-ceiling window", surface="a lacquered desk"),

115: dict(
    outfit="a liquid mirror-silver vinyl micro bikini, minimal triangle top and ultra-thin strap "
           "bottom with polished silver O-rings, a rigid chrome choker and crystal drop earrings, "
           "11-inch silver chrome stiletto heels with a transparent platform",
    shoe="silver chrome stiletto heels with transparent platform, 11-inch",
    setting="a minimalist glass-walled penthouse at golden hour, warm sunset raking the silver vinyl",
    seat="a low designer bench", wall="a full-height window", surface="a stone ledge"),

116: dict(
    outfit="a tight black high-gloss leather pencil skirt and a leopard-print liquid-satin blouse "
           "unbuttoned dangerously low, "
           "8-inch clear platform stiletto heels",
    shoe="clear platform stiletto heels, 8-inch",
    setting="an immaculate editorial studio with high-gloss specularity and clean rim lighting",
    seat="a studio cube", wall="a seamless studio wall", surface="a studio riser"),

117: dict(
    outfit="an electric cobalt blue high-gloss vinyl micro bikini, asymmetric top with silver "
           "chrome O-rings and a high-cut bottom with side ties, and a cyan vinyl choker with a "
           "silver moon pendant, "
           "11-inch silver chrome stiletto heels with a transparent platform",
    shoe="silver chrome stiletto heels with transparent platform, 11-inch",
    setting="the deck of a luxury yacht at sunset, deep blue sea behind and golden hour light",
    seat="a teak deck bench", wall="a polished yacht rail", surface="a teak deck table"),

118: dict(
    outfit="a black high-gloss vinyl bodysuit with crimson lace overlays across the bust and hips, "
           "high-cut at the hip, and blood red lace stockings on black vinyl suspenders, "
           "8-inch black patent lace-up stiletto boots",
    shoe="black patent lace-up stiletto boots, 8-inch",
    setting="a dark noir boudoir with crimson velvet drapery and low cinematic lighting",
    seat="a velvet chaise", wall="a draped velvet wall", surface="a lacquered vanity"),

119: dict(
    outfit="a liquid gold mirror-finish vinyl micro bikini, minimal triangle top strung on fine "
           "gold chains and a high-rise bottom with gold O-rings, "
           "11-inch mirror chrome gold stiletto heels",
    shoe="mirror chrome gold stiletto heels, 11-inch",
    setting="a minimalist luxury penthouse at golden hour for maximum reflection",
    seat="a designer lounge chair", wall="a full-height window", surface="a marble ledge"),

120: dict(
    outfit="a black mirror PVC high-waisted tube skirt to the knee with a side slit, a black vinyl "
           "Mugler-style blazer with sculptural angular shoulders worn open over a black satin-finish "
           "bustier with sweetheart cups and visible boning, ultra-sheer black back-seamed stockings "
           "and a black leather suspender belt visible beneath the skirt, "
           "7-inch black patent vinyl lace-up platform stiletto boots",
    shoe="black patent vinyl lace-up platform stiletto boots, 7-inch",
    setting="a floor-30 Santiago boardroom, full-height glass, ebony table and CEO lighting",
    seat="a leather boardroom chair", wall="a floor-to-ceiling window", surface="an ebony table",
    seam=True),

121: dict(
    outfit="a black high-gloss vinyl corset with visible boning and rose gold lacing, a black vinyl "
           "thong with rose gold O-rings, and semi-sheer black thigh-high stockings with lace tops "
           "clipped to black vinyl suspenders, "
           "8-inch black patent platform stiletto heels",
    shoe="black patent platform stiletto heels, 8-inch",
    setting="a dark romantic boudoir with red velvet drapes, scattered dark roses and candlelight",
    seat="a velvet armchair", wall="a velvet-draped wall", surface="a carved side table"),

122: dict(
    outfit="an ultra-glossy white vinyl bikini, halter-style top with silver chrome buckles and a "
           "high-rise deeply cut bottom, "
           "8-inch white patent platform stiletto heels",
    shoe="white patent platform stiletto heels, 8-inch",
    setting="an oceanfront luxury penthouse in Zapallar, Chile, at golden hour",
    seat="a white outdoor lounger", wall="a glass balustrade", surface="a stone terrace ledge"),

123: dict(
    outfit="an ultra-glossy azure blue vinyl jumpsuit, surgically fitted, with a silver front zip "
           "open to the navel revealing a white satin-finish overbust corset beneath, and a wide "
           "blue PVC belt with a chrome buckle, "
           "8-inch cyan blue patent stiletto boots, knee-high",
    shoe="cyan blue patent knee-high stiletto boots, 8-inch",
    setting="a private airfield VIP lounge in Santiago, haute-couture editorial lighting and "
            "extreme specular reflection",
    seat="a designer lounge chair", wall="a glass lounge partition", surface="a chrome console"),

124: dict(
    outfit="a neon pink latex sports bra with ultra-glossy black trim, high-waisted black latex "
           "leggings with neon pink side stripes, and a rigid chrome choker, "
           "8-inch neon pink patent platform stiletto sandals",
    shoe="neon pink patent platform stiletto sandals, 8-inch",
    setting="a minimalist luxury gym in Santiago with full-height windows at golden hour",
    seat="a padded bench", wall="a mirrored gym wall", surface="a chrome rack"),

125: dict(
    outfit="a sapphire blue mirror-finish vinyl micro bikini, triangle top on silver chrome straps "
           "and an ultra-high-cut high-rise bottom, "
           "11-inch mirror chrome silver stiletto heels",
    shoe="mirror chrome silver stiletto heels, 11-inch",
    setting="a penthouse in Zapallar at golden hour, sea reflections across the vinyl",
    seat="a designer lounger", wall="a full-height window", surface="a stone ledge"),

126: dict(
    outfit="a platinum mirror-finish vinyl high-waisted pencil skirt, a white liquid-satin blouse "
           "with crystal buttons fitted to the body and strategically unbuttoned, and a rigid "
           "silver chrome corset belt, "
           "9-inch platinum mirror patent stiletto boots, knee-high",
    shoe="platinum mirror patent knee-high stiletto boots, 9-inch",
    setting="a luxury rooftop lounge in Santiago at dusk, glass floor and skyline behind",
    seat="a rooftop lounge chair", wall="a glass balustrade", surface="a glass bar top"),

127: dict(
    outfit="a black high-gloss silk-satin push-up bra with Chantilly lace appliques, a matching "
           "lace thong on satin straps, and a black satin suspender belt with silver chrome "
           "buckles holding ultra-sheer black stockings with Chantilly lace tops, "
           "11-inch black patent stiletto heels",
    shoe="black patent stiletto heels, 11-inch",
    setting="a luxury suite in warm boudoir lighting, soft shadows and black satin sheets",
    seat="an upholstered bedroom chair", wall="a padded headboard", surface="a satin-covered bed"),

128: dict(
    outfit="a red high-gloss silk-satin push-up bra with black Chantilly lace appliques, a matching "
           "red satin and black lace thong, and a black satin suspender belt with silver chrome "
           "buckles holding ultra-sheer black stockings with floral lace tops, "
           "8-inch black patent platform stiletto heels",
    shoe="black patent platform stiletto heels, 8-inch",
    setting="a luxury suite with red velvet drapery, warm editorial lighting and soft shadows",
    seat="an upholstered chair", wall="a velvet-draped wall", surface="a satin-covered bed"),

# ---------------------------------------------------------------- L129-L142
129: dict(
    outfit="a white high-gloss Italian silk-satin push-up corset embroidered with pearls and silver "
           "filigree, a white Chantilly lace thong, and a white satin suspender belt with pearl "
           "clasps holding ultra-sheer white thigh-high stockings with white floral lace tops, "
           "11-inch white patent platform stiletto heels",
    shoe="white patent platform stiletto heels, 11-inch",
    setting="a minimalist bridal suite in diffuse white light with white silk sheets",
    seat="an upholstered white chair", wall="a white padded headboard", surface="a white silk bed"),

130: dict(
    outfit="a liquid metallic gold vinyl micro bikini with ultra-fine straps and a minimalist "
           "high-cut line, and fine gold body chains circling the torso, "
           "11-inch mirror chrome gold platform stiletto heels",
    shoe="mirror chrome gold platform stiletto heels, 11-inch",
    setting="a luxury Santiago rooftop at midnight, infinity pool, city lights and party bokeh",
    seat="a poolside lounger", wall="a glass balustrade", surface="a stone pool edge"),

131: dict(
    outfit="an electric blue metallic vinyl bikini with crossed wrap-around straps at the waist, "
           "a minimalist high-leg cut, and a blue metallic cuff bracelet, "
           "11-inch mirror chrome blue platform stiletto heels",
    shoe="mirror chrome blue platform stiletto heels, 11-inch",
    setting="a coastal sunset by an infinity pool, golden sunlight across the metallic blue and "
            "palm bokeh",
    seat="a poolside lounger", wall="a glass balustrade", surface="a stone pool edge"),

132: dict(
    outfit="an emerald green high-gloss Italian silk-satin teddy with a deep neckline, black "
           "Chantilly lace trim at the edges and a fully open back, the fabric fluid and liquid to "
           "the touch, with a black pearl collar, "
           "11-inch emerald green satin-finish platform stiletto heels",
    shoe="emerald green satin-finish platform stiletto heels, 11-inch",
    setting="a Victorian library at night, firelight, dark wood shelving and velvet rugs",
    seat="a leather reading chair", wall="a dark wood bookshelf", surface="a carved library table"),

133: dict(
    outfit="a neon fuchsia high-gloss vinyl micro string bikini with minimal cord straps, an ultra "
           "high-leg cut and minimal coverage, and XXL silver hoop earrings, "
           "11-inch clear acrylic platform stiletto heels with a neon fuchsia base",
    shoe="clear acrylic platform stiletto heels with neon fuchsia base, 11-inch",
    setting="a tropical beach at midday, palms and crystalline turquoise sea in saturated sunlight",
    seat="a low beach lounger", wall="a palm trunk", surface="a bleached wooden deck"),

134: dict(
    outfit="a champagne liquid-satin babydoll with 24k gold sequin embroidery across the bust and "
           "hem, ultra-fine straps and a fluid sheer skirt, with pearl bracelets, "
           "11-inch gold platform stiletto sandals with jewelled straps",
    shoe="gold platform stiletto sandals with jewelled straps, 11-inch",
    setting="a seven-star hotel balcony at sunrise, snow-capped cordillera view and marble furniture",
    seat="a marble balcony chair", wall="a marble balustrade", surface="a marble table"),

135: dict(
    outfit="a high-shine silver sequinned triangle bikini with slim silver straps, a minimalist cut "
           "and hard specular reflections, and a crystal collar, "
           "11-inch mirror chrome silver platform stiletto heels",
    shoe="mirror chrome silver platform stiletto heels, 11-inch",
    setting="a night gala pool party under blue and magenta RGB lighting, disco reflections on water",
    seat="a poolside lounger", wall="a lit glass panel", surface="a stone pool edge"),

136: dict(
    outfit="a deep plum silk-velvet soft-cup bra with no underwire and a matching high-rise thong, "
           "trimmed with black satin bows at the hips and bust, and a black velvet choker with a "
           "silver pendant, "
           "11-inch matching plum velvet platform stiletto heels",
    shoe="plum velvet platform stiletto heels, 11-inch",
    setting="a luxury bedroom with dark grey silk sheets and soft purple lighting",
    seat="an upholstered bedroom chair", wall="a padded headboard", surface="a silk-covered bed"),

137: dict(
    outfit="a leopard-print high-shine satin-lycra micro bikini with gold hardware at the shoulders "
           "and hips and an ultra-provocative cut, with wide gold cuff bracelets, "
           "11-inch matching leopard-print platform stiletto heels",
    shoe="leopard-print platform stiletto heels, 11-inch",
    setting="an exotic botanical garden in sunlight, dense foliage and light filtered through leaves",
    seat="a stone garden bench", wall="a wall of foliage", surface="a stone plinth"),

138: dict(
    outfit="a floor-length pure white liquid-satin robe with flared sleeves worn open over a short "
           "matching chemise, both trimmed with translucent floral lace, the fabric ethereal and "
           "fluid, and a white satin headband, "
           "11-inch white satin-covered platform mules with ostrich feather trim",
    shoe="white satin-covered platform mules with ostrich feather trim, 11-inch",
    setting="an ethereal room bathed in white light, tall windows with white linen curtains lifting "
            "and a canopy bed in pure morning light",
    seat="a white upholstered chair", wall="a white canopy post", surface="a white linen bed",
    wrap="slip"),

139: dict(
    outfit="a shimmering metallic red bikini with an ultra high-leg cut, slim straps and a liquid "
           "sheen, and a silver choker, "
           "11-inch mirror chrome red platform stiletto heels",
    shoe="mirror chrome red platform stiletto heels, 11-inch",
    setting="a black volcanic sand beach at sunset, orange and violet sky against the metallic red",
    seat="a low beach lounger", wall="a volcanic rock face", surface="a dark stone slab"),

# L140: la ficha traia "guantes de encaje negro cortos" -> BORRADOS (canon).
140: dict(
    outfit="a short deep black liquid-satin slip dress embroidered with jet black sequins and dark "
           "crystals, a straight neckline on fine chain straps, the fabric heavy and fluid and "
           "moulded to the curves, "
           "11-inch polished black obsidian platform stiletto heels",
    shoe="polished black obsidian platform stiletto heels, 11-inch",
    setting="a contemporary gothic salon with soaring ceilings, dark minimalist architecture and "
            "dramatic pinpoint lighting",
    seat="a black lacquer chair", wall="a dark stone column", surface="a black stone plinth"),

141: dict(
    outfit="a neon lime latex bodysuit with geometric laser-cut openings, worn inside an "
           "architectural cage structure of transparent PVC edged in reflective black vinyl, and a "
           "rigid clear acrylic choker, "
           "11-inch black mirror vinyl thigh-high platform stiletto boots with a silver needle heel",
    shoe="black mirror vinyl thigh-high platform stiletto boots, 11-inch, silver needle heel",
    setting="a minimalist white photographic studio with high-end rim lighting and hard shadows",
    seat="a white studio cube", wall="a white cyclorama wall", surface="a white studio riser"),

142: dict(
    outfit="a midnight blue high-gloss vinyl bodysuit encrusted with Swarovski crystals and built-in "
           "harness straps, high-cut at the hip, "
           "11-inch clear and blue vinyl platform stiletto heels with a needle heel",
    shoe="clear and blue vinyl platform stiletto heels, 11-inch, needle heel",
    setting="a professional strip club stage with a polished chrome pole, deep blue stage light and "
            "crystal glints",
    seat="a stage step", wall="a mirrored stage wall", surface="a polished stage floor"),

# ---------------------------------------------------------------- L155-L173
155: dict(
    outfit="a high-shine black latex blazer with structured shoulders and a deep V neckline, and "
           "matching electric blue liquid vinyl leggings, with a 14k white gold choker, "
           "silver metallic stiletto pumps with a 14cm needle heel and a pointed toe, no platform",
    shoe="silver metallic stiletto pumps, 14cm needle heel, pointed toe, no platform",
    setting="a glass boardroom high in a skyscraper, skyline through full-height windows",
    seat="a leather boardroom chair", wall="a glass partition", surface="a lacquered boardroom table"),

# L156: la ficha traia "opera length transparent vinyl gloves" -> BORRADOS (canon).
156: dict(
    outfit="a liquid chrome metal micro bikini with thin reflective straps, "
           "12-inch clear platform stiletto heels with an internal violet neon glow",
    shoe="clear platform stiletto heels with internal violet neon glow, 12-inch",
    setting="a Vegas stage set in violet neon and drifting smoke",
    seat="a stage step", wall="a mirrored stage wall", surface="a polished stage floor"),

172: dict(
    outfit="a jet-black latex micro bikini top with moulded underwire cups and a central gold O-ring, "
           "and an ultra-high-cut black latex bottom on ultra-fine straps with gold O-rings at the "
           "hips, a 24k gold body chain running diagonally from the left shoulder to the right hip, "
           "a gold choker with a rectangular noir pendant and 7cm gold hoop earrings, "
           "20cm black patent leather stiletto sandals with a sharp pointed toe and a transparent "
           "PVC ankle strap with a gold buckle",
    shoe="black patent leather stiletto sandals, 20cm, sharp pointed toe, transparent PVC ankle "
         "strap with gold buckle",
    setting="a black glass penthouse at midnight, floor-to-ceiling city panorama, dramatic overhead "
            "spotlight and noir atmosphere with blue-black shadows",
    seat="a black leather lounge chair", wall="a black glass wall", surface="a black stone console"),

173: dict(
    outfit="an electric cyan latex micro bikini top with moulded underwire push-up cups and a "
           "central chrome O-ring, and an ultra-high-cut cheeky cyan latex bottom with chrome "
           "O-rings at the hips, a chrome choker with a front ring, XXXL chrome hoop earrings and "
           "a chrome cuff bracelet on the right wrist, "
           "14cm transparent perspex stiletto sandals with an open toe and a chrome ankle buckle",
    shoe="transparent perspex stiletto sandals, 14cm, open toe, chrome ankle buckle",
    setting="the deck of a luxury yacht, turquoise sea behind and bright Mediterranean light",
    seat="a teak deck bench", wall="a polished yacht rail", surface="a teak deck table"),

}
