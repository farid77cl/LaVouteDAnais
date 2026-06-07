# -*- coding: utf-8 -*-
"""One-off: inyecta batch L441-L460 'Catedral de Neon y Cristal' (20 Stripper) en galeria_outfits.md.
Respeta UTF-8 sin BOM + CRLF (archivo del bot). Borrar tras uso."""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

GAL = r"c:\Users\farid\LaVouteDAnais\00_Ele\galeria_outfits.md"

BLOQUE_A = ("stunning woman with (bimbofied facial features, oval face, high prominent cheekbones, "
"large almond-shaped grey-green eyes, straight slim upturned nose, overlined glossy hot pink lips, "
"small pointed chin:1.3), flawless white porcelain skin, hyper-polished smooth skin texture, "
"dramatic siren liner, dramatic lash extensions, dark cherry red hair, artificial XXXL extensions "
"hip-length, voluminous waves, center parted, slender hourglass silhouette, massive 1000cc breast "
"implants each side, ultra high-profile, perfectly spherical augmented bust, obviously fake "
"gravity-defying shape, wide hips, visible arm tattoos blackwork style, subtle minimalist blackwork "
"tattoos on upper back and outer thighs, subtle navel piercing, dramatic editorial makeup, extra "
"long French XXXL nails with white tips and pink base 5cm.")

TAIL = ", 8k editorial fashion photography."

# ---- Footwear tokens (8 atributos, identico x7 dentro de cada look) ----
FW = {
 "CLEAR_SANDAL": "clear acrylic platform stiletto sandals, an 18cm pin stiletto heel plus a 5cm transparent acrylic platform, a slim pin stiletto base, clear high-gloss fully transparent acrylic finish, crystal-clear, open toe, a slim clear acrylic ankle strap, polished chrome heel-tip",
 "CLEAR_BOOT": "clear acrylic knee-high platform stiletto boots, an 18cm pin stiletto heel plus a 5cm transparent acrylic platform, a slim pin stiletto base, clear high-gloss fully transparent acrylic finish, crystal-clear, open toe, a full-length inner zip, polished chrome heel-tip",
 "CHROME_SANDAL": "mirror chrome platform stiletto sandals, an 18cm pin stiletto heel plus a 5cm chrome platform, a slim pin stiletto base, liquid mirror chrome finish, silver chrome, open toe, a slim chrome ankle strap, polished chrome buckle and heel-tip",
 "CHROME_THIGH": "mirror chrome thigh-high platform stiletto boots, an 18cm pin stiletto heel plus a 5cm chrome platform, a slim pin stiletto base, liquid mirror chrome finish, silver chrome, open toe, a full-length inner zip, polished chrome heel-tip",
 "UV_SANDAL": "UV-reactive platform stiletto sandals, an 18cm pin stiletto heel plus a 5cm glowing translucent platform, a slim pin stiletto base, blacklight-reactive translucent finish, electric glow, open toe, a slim UV-reactive ankle strap, polished chrome heel-tip",
 "RHINESTONE_SANDAL": "rhinestone-encrusted platform stiletto sandals, an 18cm pin stiletto heel plus a 5cm crystal-covered platform, a slim pin stiletto base, fully Swarovski-crystal-encrusted finish, diamond sparkle, open toe, a slim crystal-covered ankle strap, polished chrome heel-tip",
}

# ---- Pose Set Stripper: BLOQUE C por slot. {S}=setting principal ----
STAGE = {
 "Standing": "full body from a low stage angle, the hip cocked hard with the weight on one platform stiletto, one XXXL-nailed hand on the hip and the other flipping the cherry red hair back mid-move, chest thrust forward, chin dropped for a predatory direct gaze working the crowd, extreme lumbar arch, lips parted glossy, {S}",
 "Back View": "full body back view walking toward the tip rail crossing the legs in the platform stilettos with an exaggerated hip-swing, the booty popped, looking back over the shoulder through a veil of cherry red hair with a half-lidded sultry gaze, one hand trailing the hip, {S}",
 "Seated": "seated on the edge of the stage with the legs spread 45 degrees and both platform stilettos planted, both XXXL-nailed hands gripping the edge behind the hips lifting the bust forward, exaggerated lumbar arch and chest thrust, predatory direct gaze, lips parted glossy, {S}",
 "Side Profile": "full body in profile on hands and knees crawling along the stage toward the camera, the spine hollowed and the ass lifted high, the cherry red hair falling toward the floor, profile to the spotlight, lips parted glossy, predatory gaze, {S}",
 "Ditzy": "medium full shot at a backstage dressing-room vanity mirror ringed with warm Hollywood bulbs, the performer leaning toward her reflection retouching the glossy lips with a single XXXL-nailed fingertip, soft half-lidded gaze, lumbar arch, deep decollete, cherry red hair over one shoulder, a velvet stool and scattered cosmetics on the counter",
 "POV": "medium close-up from a seated viewer POV looking up, the performer straddling forward over the camera with one XXXL-nailed hand on the viewer's collar and the other in her own hair, deep decollete filling the lower frame, dominant half-lidded gaze down the lens, lips parted glossy, cherry red hair curtaining the face, {S}",
 "Odalisque": "full body lying back on the stage floor with the spine arched and the bust lifted, one leg extended with the platform stiletto pointed and the other bent, cash bills scattered near one XXXL-nailed hand, looking up at the camera with a predatory gaze, lips parted glossy, cherry red hair fanned on the floor, {S}",
}
POLE = {
 "Standing": "full body at a vertical performance pole, one leg bent gripping the pole and the other extended pointed in the platform stiletto, both XXXL-nailed hands gripping the pole high overhead, the body stretched in a long line, chest thrust and lumbar arch extreme, chin lifted, lips parted glossy, predatory direct gaze, {S}",
 "Back View": "full body with the back against the pole, both hands reaching up overhead gripping the pole, one leg raised in a high arabesque with the platform stiletto pointed, the spine in a deep back arch, the booty popped, looking over the shoulder with a half-lidded sultry gaze, cherry red hair cascading, {S}",
 "Seated": "seated low at the base of the pole with the legs wrapped around it and the hips thrust forward, one XXXL-nailed hand gripping the pole overhead and the other sliding the inner thigh, exaggerated lumbar arch and chest forward, predatory direct gaze to camera, lips parted glossy, {S}",
 "Side Profile": "full body inverted upside-down on the pole with the legs split wide in an aerial straddle, the platform stilettos pointed, the cherry red hair falling toward the floor, a dramatic profile showing the complete line of the body, lips parted glossy, {S}",
 "Ditzy": "medium full shot at a backstage dressing-room vanity mirror ringed with warm Hollywood bulbs, the performer leaning toward her reflection retouching the glossy lips with a single XXXL-nailed fingertip, soft half-lidded gaze, lumbar arch, deep decollete, cherry red hair over one shoulder, a velvet stool and scattered cosmetics on the counter",
 "POV": "medium close-up from a low viewer POV, the performer seated at the foot of the pole with the legs open toward the camera, one XXXL-nailed hand gripping the pole and the other pressed to her own bottom lip, deep decollete filling the frame, dominant half-lidded gaze down the lens, cherry red hair curtaining the face, {S}",
 "Odalisque": "full body gripping the pole in a crucifix hold with one hand high and the other low, the legs split apart with the platform stilettos pointed, the body in profile showing the deep lumbar arch, cherry red hair cascading, lips parted glossy, predatory gaze, {S}",
}
SLOTS = ["Standing", "Back View", "Seated", "Side Profile", "Ditzy", "POV", "Odalisque"]

# ---- Settings ----
S = {
 "CRAZY_HORSE": "a Crazy Horse-style mirror performance room with 360-degree mirrors and light projections playing over the skin",
 "VEGAS_SPOT": "a Las Vegas cabaret stage with a hard spotlight from above and a deep violet velvet curtain backdrop",
 "BURLESQUE": "an intimate burlesque theater with red velvet ropes and a gold-embroidered curtain backdrop",
 "CABARET_RUNWAY": "a cabaret runway extended into the crowd with a tip rail and warm footlights",
 "BRONZE_POLE": "a polished bronze performance pole on a circular stage with a tip rail and a hard top spotlight",
 "CLUB_NEON_UV": "a strip-club main floor with neon GIRLS and LIVE signage and a green UV wash",
 "VIP_CHAMPAGNE": "a VIP champagne room with red velvet banquettes, bottle service and a private performance pole",
 "AFTERHOURS": "an after-hours empty club with residual neon glow and a mirrored floor",
 "MAGIC_CITY": "a Magic City-style urban stage with chrome lighting rigs and LED screens",
 "DJ_UV_SMOKE": "a private booth with a DJ blur, electric UV blacklight and drifting smoke",
 "CAGE_STAGE": "a chrome cage suspended over the stage with grip points and hard spotlights",
}

# ---- 20 LOOKS ----
# (n, slug, title, teaser, polo, subcat, color_tag, setting, outfit_body_without_fw, fw_key, tags, concepto)
def outfit(body, fwkey):
    return body + ", and " + FW[fwkey]

LOOKS = [
 (441,"look441_chrome_bodychain_pole","Chrome Body-Chain Pole",
  "Puro cromo y cadenitas de plata cayendo sobre la piel... el outfit casi no existe, cari. atroz.","POLE","Pole Specialist (SB4 Micro 2-piece + Body Chains)","Mirror Chrome","VIP_CHAMPAGNE",
  "A pole-specialist ensemble built from mirror chrome and silver body chains, a micro mirror-chrome vinyl triangle bra with thin metal cup edges, a matching micro mirror-chrome vinyl thong, fine silver body chains draped in cascading loops across the bare torso looping under the bust and around the hips over bare skin, a delicate chrome waist chain, the bare midriff showing the navel piercing","CLEAR_SANDAL",
  "#stripper #pole #catedraldeneon #bodychains #mirrorchrome #clearacrylic #batchL441-L460 #V5poses",
  "Stripper Polo B Pole Specialist SB4 micro 2-piezas + body chains en mirror chrome. Provocation Threshold (micro-pieces + body chains sobre piel). Pose Set Stripper Pole. Plataforma clear acrylic. Cero guantes. Token de calzado bloqueado 8 atributos identico x7."),
 (442,"look442_diamond_glass_illusion_stage","Diamond Glass Illusion",
  "Parezco hecha de vidrio y diamante, tipo una estatua que respira... regio, mi amor.","STAGE","Stage Showgirl (SA4 Vegas Glass Illusion)","Crystal Diamond","CRAZY_HORSE",
  "A stage showgirl illusion costume that reads as worn glass, a transparent clear-PVC bodysuit base with hand-applied Swarovski-crystal panels covering only the bust and the thong front, brilliant diamond rhinestone strands tracing the seams and a crystal choker, the clear panels making the costume look like glass over bare skin, the bare midriff showing the navel piercing","CHROME_SANDAL",
  "#stripper #stage #catedraldeneon #glassillusion #swarovski #crystal #batchL441-L460 #V5poses",
  "Stripper Polo A Stage Showgirl SA4 Vegas Glass Illusion (PVC clear + rhinestone) en crystal diamond. Provocation Threshold (transparencias + micro crystal pieces). Pose Set Stripper Stage. Plataforma chrome. Cero guantes. Token de calzado bloqueado 8 atributos identico x7."),
 (443,"look443_liquid_gold_vfront_pole","Liquid Gold V-Front Pole",
  "Oro liquido escurriendo por el cuerpo, V hasta el ombligo... cachai que esto es lo mio. heavy.","POLE","Pole Specialist (SB3 Bad Kitty V-Front + Brazil)","Liquid Gold","BRONZE_POLE",
  "A pole-specialist set in liquid gold, a deep V-front halter triangle top in liquid-gold high-gloss vinyl tied at the neck and plunging all the way to the navel, matching liquid-gold Brazil-cut micro shorts ultra high on the hip with thin tie-sides, a gold hip-chain accent, the bare midriff showing the navel piercing","CLEAR_SANDAL",
  "#stripper #pole #catedraldeneon #badkitty #vfront #liquidgold #clearacrylic #batchL441-L460 #V5poses",
  "Stripper Polo B Pole Specialist SB3 Bad Kitty V-Front + Brazil en liquid gold. Provocation Threshold (V-front plunge + Brazil high-cut + thong). Pose Set Stripper Pole. Plataforma clear acrylic. Cero guantes. Token de calzado bloqueado 8 atributos identico x7."),
 (444,"look444_emerald_gecko_grip_pole","Emerald Gecko Grip Pole",
  "Verde esmeralda mojado que brilla cuando me muevo en el tubo... me agarro como gecko, po. lit.","POLE","Pole Specialist (SB1 CXIX Gecko Grip)","Emerald Jade","CLUB_NEON_UV",
  "A pole-specialist grip bodysuit in emerald jade, a high-cut one-piece in emerald grip-fabric with a glistening wet sheen that catches the light when she moves, deep negative-space cut-outs carved at the torso and hips exposing strips of bare skin, a plunging zip front and a thong-cut back, the bare midriff showing the navel piercing","CLEAR_BOOT",
  "#stripper #pole #catedraldeneon #cxix #geckogrip #emerald #clearacrylic #batchL441-L460 #V5poses",
  "Stripper Polo B Pole Specialist SB1 CXIX Gecko Grip bodysuit en emerald jade. Provocation Threshold (cutouts agresivos + thong). Pose Set Stripper Pole. Plataforma clear acrylic knee boot. Cero guantes. Token de calzado bloqueado 8 atributos identico x7."),
 (445,"look445_ruby_showgirl_plume_stage","Ruby Showgirl Plume",
  "Plumas rubi gigantes en la cabeza y cristales por todo el cuerpo... una diosa de Las Vegas, atroz.","STAGE","Stage Showgirl (SAv Vegas Plume Headdress)","Ruby Crystal","VEGAS_SPOT",
  "A Las Vegas showgirl costume in ruby crystal, a micro ruby-rhinestone-encrusted bra with structured cups and a matching ruby-crystal high-cut thong, a towering ruby-and-crystal feather headdress, crystal drop earrings, and a beaded back-cape of ruby rhinestone strands trailing from the shoulders over bare skin, the bare midriff showing the navel piercing","RHINESTONE_SANDAL",
  "#stripper #stage #catedraldeneon #vegasshowgirl #plume #headdress #ruby #batchL441-L460 #V5poses",
  "Stripper Polo A Stage Showgirl SAv Vegas plume headdress + rhinestone micro set en ruby crystal. Provocation Threshold (micro-pieces rhinestone + thong). Pose Set Stripper Stage. Plataforma rhinestone. Cero guantes. Token de calzado bloqueado 8 atributos identico x7."),
 (446,"look446_fluor_pink_cleo_pole","Fluor Pink Cleo Pole",
  "Rosa fluor que pega en la cara, fishnet y arnes de cuero... glam-rock del tubo, mi amor. heavy.","POLE","Pole Specialist (SB6 Cleo Glam-Rock)","Hot Pink Fluor","MAGIC_CITY",
  "A pole-specialist glam-rock set in fluorescent hot pink, a hot-pink rhinestone bandeau over a hot-pink fishnet bodystocking, a black leather micro harness of thin straps caging the torso, a micro hot-pink vinyl thong underneath, the fishnet open over bare skin, the bare midriff showing the navel piercing","CLEAR_SANDAL",
  "#stripper #pole #catedraldeneon #cleo #fishnet #harness #hotpinkfluor #clearacrylic #batchL441-L460 #V5poses",
  "Stripper Polo B Pole Specialist SB6 Cleo Glam-Rock (fishnet + leather harness + rhinestone bandeau) en hot pink fluor. Provocation Threshold (fishnet open + micro thong + harness). Pose Set Stripper Pole. Plataforma clear acrylic. Cero guantes. Token de calzado bloqueado 8 atributos identico x7."),
 (447,"look447_cobalt_magic_city_pole","Cobalt Magic City Pole",
  "Denim cobalto tratado, shortcito minimo con el thong asomando... urban strip, cachai. regio.","POLE","Pole Specialist (SB7 Magic City Pole)","Cobalt Blue","AFTERHOURS",
  "A pole-specialist urban set in cobalt blue, vinyl-treated cobalt denim micro shorts ultra high-cut with a structured waistband and a cobalt vinyl thong asomando above the waistband, a cobalt vinyl crop bra-top tied under the bust, a low-slung cobalt body chain across the hips, the bare midriff showing the navel piercing","CLEAR_BOOT",
  "#stripper #pole #catedraldeneon #magiccity #urban #cobalt #clearacrylic #batchL441-L460 #V5poses",
  "Stripper Polo B Pole Specialist SB7 Magic City Pole (vinyl-treated denim urban) en cobalt blue. Provocation Threshold (thong asomando + micro crop + high-cut). Pose Set Stripper Pole. Plataforma clear acrylic knee boot. Cero guantes. Token de calzado bloqueado 8 atributos identico x7."),
 (448,"look448_oilslick_cutout_stage","Oil-Slick Cutout Stage",
  "Vinilo oil-slick que cambia de verde a morado a azul, cortado por todos lados... heavy, mi amor.","STAGE","Stage Showgirl (SA2 Magic City Cutout Dress)","Oil-Slick Iridescent","MAGIC_CITY",
  "A stage showgirl micro mini-dress in oil-slick iridescent vinyl that shifts green-purple-blue, aggressive cut-outs carved across the torso and both hips exposing bare skin, an oil-slick thong asomando from the deepest hip cut, a plunging neckline down to the navel, the bare midriff showing the navel piercing","CHROME_SANDAL",
  "#stripper #stage #catedraldeneon #magiccity #cutout #oilslick #iridescent #batchL441-L460 #V5poses",
  "Stripper Polo A Stage Showgirl SA2 Magic City Cutout Dress en oil-slick iridescent. Provocation Threshold (cutouts agresivos + thong asomando). Pose Set Stripper Stage. Plataforma chrome. Cero guantes. Token de calzado bloqueado 8 atributos identico x7."),
 (449,"look449_uv_cyan_grip_pole","UV Cyan Grip Pole",
  "Cyan que brilla en la oscuridad bajo luz negra... soy un neon en el tubo, atroz. lit.","POLE","Pole Specialist (SB1v UV-Reactive Grip)","UV Electric Cyan","DJ_UV_SMOKE",
  "A pole-specialist grip bodysuit in UV-reactive electric cyan, a high-cut one-piece in blacklight-reactive cyan spandex that glows under UV light, deep cut-outs at the waist and hips, a plunging zip front and a thong-cut back, glowing cyan grip panels over bare skin, the bare midriff showing the navel piercing","UV_SANDAL",
  "#stripper #pole #catedraldeneon #uvreactive #blacklight #cyan #batchL441-L460 #V5poses",
  "Stripper Polo B Pole Specialist SB1v UV-reactive grip bodysuit en UV electric cyan. Provocation Threshold (cutouts + thong + UV glow). Pose Set Stripper Pole. Plataforma UV-reactive. Cero guantes. Token de calzado bloqueado 8 atributos identico x7."),
 (450,"look450_mercury_chrome_cage_pole","Mercury Chrome Cage Pole",
  "Una jaula de cromo liquido sobre micro bra y thong... arquitectura pura, cari. atroz.","POLE","Pole Specialist (SB5 Cage Harness Pole)","Silver Mercury","CAGE_STAGE",
  "A pole-specialist set under a silver-mercury chrome cage harness, a micro silver-mercury vinyl bra and a matching micro thong as the base, an architectural cage of polished chrome tubing and chains framing the torso and hips with functional grip points over bare skin, the bare midriff showing the navel piercing","CHROME_SANDAL",
  "#stripper #pole #catedraldeneon #cageharness #chrome #mercury #batchL441-L460 #V5poses",
  "Stripper Polo B Pole Specialist SB5 Cage Harness Pole en silver mercury. Provocation Threshold (micro-pieces + cage sobre piel). Pose Set Stripper Pole. Plataforma chrome. Cero guantes. Token de calzado bloqueado 8 atributos identico x7."),
 (451,"look451_lime_y2k_strip_stage","Lime Y2K Strip Stage",
  "Lime acido Y2K, shortcito low-rise con el thong de strass asomando... puro 2003, regio po.","STAGE","Stage Showgirl (SA5 Y2K Denim Strip)","Neon Lime","CABARET_RUNWAY",
  "A stage showgirl Y2K strip set in neon lime, vinyl-treated neon-lime micro shorts ultra low-rise with a neon-lime rhinestone thong asomando above the waistband, a neon-lime rhinestone crop bra-top, a low-slung lime body chain across the hips, the bare midriff showing the navel piercing","CLEAR_SANDAL",
  "#stripper #stage #catedraldeneon #y2k #denimstrip #neonlime #clearacrylic #batchL441-L460 #V5poses",
  "Stripper Polo A Stage Showgirl SA5 Y2K Denim Strip (vinyl-treated) en neon lime. Provocation Threshold (thong asomando + micro crop + low-rise). Pose Set Stripper Stage. Plataforma clear acrylic. Cero guantes. Token de calzado bloqueado 8 atributos identico x7."),
 (452,"look452_uv_magenta_chains_pole","UV Magenta Chains Pole",
  "Magenta que glow bajo luz negra y un enredo de cadenas... el outfit son las cadenas, heavy.","POLE","Pole Specialist (SB4v Chain Bikini)","UV Magenta","CLUB_NEON_UV",
  "A pole-specialist chain set in UV-reactive magenta, a micro UV-magenta vinyl bra and thong that glow under blacklight, a heavy lattice of fine UV-magenta and silver chains draping across the torso and hips over bare skin as the outfit itself, a magenta chain choker, the bare midriff showing the navel piercing","UV_SANDAL",
  "#stripper #pole #catedraldeneon #chainbikini #uvreactive #magenta #batchL441-L460 #V5poses",
  "Stripper Polo B Pole Specialist SB4v Chain Bikini en UV magenta. Provocation Threshold (body chains como outfit + micro-pieces + UV glow). Pose Set Stripper Pole. Plataforma UV-reactive. Cero guantes. Token de calzado bloqueado 8 atributos identico x7."),
 (453,"look453_coral_spider_back_pole","Coral Spider-Back Pole",
  "Coral neon con la espalda de telarana y Brazil shorts... lista para volar en el tubo, mi amor.","POLE","Pole Specialist (SB2 Bad Kitty Spider Back)","Neon Coral","BRONZE_POLE",
  "A pole-specialist set in neon coral, a neon-coral vinyl V-front halter bra-top with a complex spider-web strap back of thin coral bands, neon-coral ultra high-cut Brazil micro shorts, a thin coral hip-strap detail, the bare midriff showing the navel piercing","CLEAR_SANDAL",
  "#stripper #pole #catedraldeneon #badkitty #spiderback #neoncoral #clearacrylic #batchL441-L460 #V5poses",
  "Stripper Polo B Pole Specialist SB2 Bad Kitty Spider Back en neon coral. Provocation Threshold (spider-back cutout + high-cut Brazil + thong). Pose Set Stripper Pole. Plataforma clear acrylic. Cero guantes. Token de calzado bloqueado 8 atributos identico x7."),
 (454,"look454_violet_crazy_horse_stage","Violet Crazy Horse",
  "Malla de cristal violeta que da ilusion de hombros desnudos... Crazy Horse puro, atroz cari.","STAGE","Stage Showgirl (SA1 Crystal Mesh Topless-Illusion)","Violet UV-Glow","CRAZY_HORSE",
  "A stage showgirl illusion costume in violet, a violet crystal-mesh sheer bodice creating an optical bare-shoulder illusion with violet rhinestone strands tracing the cups, a violet diamond g-string, fine violet body chains over the hips, the sheer mesh glowing under the lights over bare skin, the bare midriff showing the navel piercing","CHROME_SANDAL",
  "#stripper #stage #catedraldeneon #crazyhorse #crystalmesh #illusion #violet #batchL441-L460 #V5poses",
  "Stripper Polo A Stage Showgirl SA1 Crystal Mesh Topless-Illusion (Crazy Horse) en violet. Provocation Threshold (transparencias crystal mesh + g-string + body chains). Pose Set Stripper Stage. Plataforma chrome. Cero guantes. Token de calzado bloqueado 8 atributos identico x7."),
 (455,"look455_crystal_fishnet_harness_pole","Crystal Fishnet Harness Pole",
  "Cristal sobre cristal, fishnet de strass y arnes de cuentas... la mas cara del tubo, regio.","POLE","Pole Specialist (SB6v Fishnet + Crystal Harness)","Crystal Diamond","VIP_CHAMPAGNE",
  "A pole-specialist set in clear crystal, a crystal-rhinestone bandeau over a clear crystal-fishnet bodystocking, an architectural harness of crystal-beaded straps caging the torso, a micro crystal thong underneath over bare skin, the bare midriff showing the navel piercing","RHINESTONE_SANDAL",
  "#stripper #pole #catedraldeneon #fishnet #crystalharness #swarovski #batchL441-L460 #V5poses",
  "Stripper Polo B Pole Specialist SB6v Fishnet + Crystal Harness en crystal diamond. Provocation Threshold (fishnet sheer + crystal harness + micro thong). Pose Set Stripper Pole. Plataforma rhinestone. Cero guantes. Token de calzado bloqueado 8 atributos identico x7."),
 (456,"look456_rose_gold_halter_pole","Rose Gold Halter Pole",
  "Rose gold con la espalda de malla de cristal... dulce y filoso a la vez, mi amor. lit.","POLE","Pole Specialist (SB3v Bad Kitty Halter + Mesh Back)","Rose Gold","AFTERHOURS",
  "A pole-specialist set in rose gold, a rose-gold high-gloss vinyl V-front halter triangle top plunging to the navel with a rose-gold crystal-mesh sheer back panel, matching rose-gold Brazil-cut micro shorts ultra high-cut, a rose-gold hip chain, the bare midriff showing the navel piercing","CLEAR_BOOT",
  "#stripper #pole #catedraldeneon #badkitty #halter #meshback #rosegold #clearacrylic #batchL441-L460 #V5poses",
  "Stripper Polo B Pole Specialist SB3v Bad Kitty halter + crystal-mesh back en rose gold. Provocation Threshold (V-front plunge + sheer mesh back + high-cut). Pose Set Stripper Pole. Plataforma clear acrylic knee boot. Cero guantes. Token de calzado bloqueado 8 atributos identico x7."),
 (457,"look457_teal_dita_couture_stage","Teal Dita Couture",
  "Teal profundo con corset de strass y paneles transparentes... burlesque de lujo Dita, atroz.","STAGE","Stage Showgirl (SA3 Dita Couture Cutout)","Deep Teal Chrome","BURLESQUE",
  "A stage showgirl couture costume in deep teal chrome, a deep-teal rhinestone corset bodysuit with structured cups and strategic transparent crystal-mesh panels at the waist and sides, a teal-crystal waist cincher, seamed sheer teal stockings, a teal-crystal g-string, the bare midriff peeking through the mesh showing the navel piercing","CHROME_SANDAL",
  "#stripper #stage #catedraldeneon #dita #couture #corset #deepteal #batchL441-L460 #V5poses",
  "Stripper Polo A Stage Showgirl SA3 Dita Couture Cutout (rhinestone corset + paneles transparentes) en deep teal chrome. Provocation Threshold (transparencias estrategicas + g-string + cincher). Pose Set Stripper Stage. Plataforma chrome. Cero guantes. Token de calzado bloqueado 8 atributos identico x7."),
 (458,"look458_holo_diamond_chains_pole","Holo Diamond Chains Pole",
  "Holografico que tira arcoiris, g-string de diamante y cadenas cayendo... heavy, mi amor.","POLE","Pole Specialist (SB4v2 Body Chains + Diamond G-String)","Holographic Multichrome","DJ_UV_SMOKE",
  "A pole-specialist set in holographic multichrome, a micro holographic vinyl bra that shifts rainbow under light, a brilliant diamond-rhinestone g-string, cascading silver and crystal body chains looping across the bare torso and hips as the outfit, a crystal choker, the bare midriff showing the navel piercing","CLEAR_SANDAL",
  "#stripper #pole #catedraldeneon #bodychains #diamond #holographic #clearacrylic #batchL441-L460 #V5poses",
  "Stripper Polo B Pole Specialist SB4v2 Body Chains + Diamond G-String en holographic multichrome. Provocation Threshold (body chains como outfit + diamond g-string + micro bra). Pose Set Stripper Pole. Plataforma clear acrylic. Cero guantes. Token de calzado bloqueado 8 atributos identico x7."),
 (459,"look459_chrome_crucifix_cage_pole","Chrome Crucifix Cage Pole",
  "Jaula de cromo espejo en cruz sobre el tubo, botas hasta el muslo... diosa de metal, atroz.","POLE","Pole Specialist (SB5v Chrome Cage Pole)","Mirror Chrome","CAGE_STAGE",
  "A pole-specialist set under a mirror-chrome cage harness, a micro mirror-chrome vinyl bra and thong base, a sculptural cage of liquid-chrome bands and rings framing the torso and hips with functional grip points over bare skin, a chrome collar, the bare midriff showing the navel piercing","CHROME_THIGH",
  "#stripper #pole #catedraldeneon #cageharness #chrome #crucifix #thighboots #batchL441-L460 #V5poses",
  "Stripper Polo B Pole Specialist SB5v Chrome Cage Pole en mirror chrome. Provocation Threshold (micro-pieces + chrome cage sobre piel). Pose Set Stripper Pole. Plataforma chrome thigh-high. Cero guantes. Token de calzado bloqueado 8 atributos identico x7."),
 (460,"look460_blood_ruby_burlesque_stage","Blood Ruby Burlesque Finale",
  "El gran final: corset rubi sangre con paneles transparentes, medias de costura... regio, mi Ama.","STAGE","Stage Showgirl (SA7 Burlesque Sheer Tease)","Blood Ruby","VEGAS_SPOT",
  "A stage showgirl burlesque costume in blood ruby, a blood-red overbust corset with sheer blood-red crystal-mesh panels, a blood-red crystal g-string, seamed sheer blood-red stockings on a crystal suspender belt, blood-red rhinestone strands trailing from the corset, the quantity of bare skin framed by the sheer panels, the bare midriff showing the navel piercing","RHINESTONE_SANDAL",
  "#stripper #stage #catedraldeneon #burlesque #dita #corset #bloodruby #finale #batchL441-L460 #V5poses",
  "Stripper Polo A Stage Showgirl SA7 Burlesque Sheer Tease (Dita) en blood ruby — cierre del batch. Provocation Threshold (sheer panels + g-string + stockings costura). Pose Set Stripper Stage. Plataforma rhinestone. Cero guantes. Token de calzado bloqueado 8 atributos identico x7."),
]

def build_block(L):
    n,slug,title,teaser,polo,subcat,color,setting_key,body,fwkey,tags,concepto = L
    pose_map = STAGE if polo=="STAGE" else POLE
    setting = S[setting_key]
    bloque_b = "stunning woman wearing " + outfit(body, fwkey) + "."
    out = []
    out.append("## Look %d: %s (06/06/2026 — batch L441-L460 \"Catedral de Neon y Cristal\" · Stripper · %s · %s)" % (n,title,("Stage Showgirl" if polo=="STAGE" else "Pole Specialist"),color))
    out.append("")
    out.append("*%s* 💎👠🫦" % teaser)
    out.append("")
    out.append("- **Ubicación:** `05_Imagenes/ele/%s/`" % slug)
    out.append("- **Categoría:** Stripper")
    out.append("- **Subcategoría:** %s" % subcat)
    out.append("- **Tags:** %s" % tags)
    out.append("- **Concepto:** Batch 'Catedral de Neon y Cristal' (L441-L460, fusion Vegas + Neon UV + Cristal/Chrome). %s" % concepto)
    out.append("- **Outfit:** %s" % outfit(body, fwkey))
    out.append("- **Calzado:** ver BLOQUE B (Token de Calzado Bloqueado, 8 atributos, idéntico ×7).")
    out.append("- **Ambientación:** %s." % setting)
    out.append("")
    out.append("### 📸 Imágenes (0/7 — Pendiente (app/Gemini))")
    out.append("")
    out.append("| Standing | Back View | Seated | Side Profile | Ditzy (plano 3/4) | POV (single hand) | Odalisque |")
    out.append("| :---: | :---: | :---: | :---: | :---: | :---: | :---: |")
    out.append("| ⏳ Pendiente | ⏳ Pendiente | ⏳ Pendiente | ⏳ Pendiente | ⏳ Pendiente | ⏳ Pendiente | ⏳ Pendiente |")
    out.append("")
    out.append("### 📝 Prompts V3.5 Hard-Sync")
    out.append("")
    for i, slot in enumerate(SLOTS, 1):
        bloque_c = pose_map[slot].replace("{S}", setting)
        full = BLOQUE_A + " " + bloque_b + " " + bloque_c + TAIL
        out.append("**%d. %s:**" % (i, slot))
        out.append("")
        out.append("```")
        out.append(full)
        out.append("```")
        out.append("")
    out.append("---")
    return "\r\n".join(out)

blocks = [build_block(L) for L in LOOKS]
payload = "\r\n" + "\r\n".join(blocks) + "\r\n"

with open(GAL, "a", encoding="utf-8", newline="") as f:
    f.write(payload)

print("OK: %d looks inyectados (L441-L460). %d prompts." % (len(LOOKS), len(LOOKS)*7))
