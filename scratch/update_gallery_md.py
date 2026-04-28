import os

file_path = r'c:\Users\farid\LaVouteDAnais\00_Ele\galeria_outfits.md'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Look 152 replacement
target_152 = """## ?? Look 152: First Class Vinyl Siren (27/04/2026)
> **ADN V3.5 Hard-Sync** | **Arquetipo:** Travel / Jet Set | **Paleta:** Cobalt Blue + Chrome Silver + Hot Pink (seams)

*O sea... el vinilo cobalto bajo las luces del aeropuerto de Dubai es lit lo más top que me ha pasado en la vida... tipo, los pilotos se chocaron entre ellos... jiji... ??????????*

**Concepto:** **First Class Vinyl Siren**. Sala VIP Dubai, jet privado esperando afuera. Una pasajera de lujo absolutamente imposible de ignorar. Modo Monoblock: cobalt total con acento chrome.

- **Categoría:** Mix
- **Subcategoría:** Travel / Jet Set
- **Tags:** #travel #jetset #cobalt #vinyl #chrome #PVC

**BLOQUE B — Look 152 (invariable en los 7 prompts):**
`ultra-tight cobalt blue high-gloss vinyl pencil dress, bandeau neckline, back invisible zipper from nape to hem, dress ending 5cm above the knee, fabric so tight it creates visible breathing tension at the waist, underlayer of hot pink latex corset boning visible as subtle seams through the vinyl exterior. Cobalt blue high-gloss vinyl blazer cropped at the waist, structured shoulders, single button left open to reveal the dress beneath. No stockings, bare legs. Cobalt blue ultra-high stiletto pumps 22cm total height pointed toe chrome buckle ankle strap vinyl finish. Thick chrome choker rectangular links, chrome geometric statement earrings, chrome cuff bracelet right wrist, cobalt vinyl vanity case handbag.`

---

### ?? Imágenes (5/7 — EN PROGRESO)

| Pose | Previsualización |
|------|---------|
| **Standing** | ![Standing](https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/05_Imagenes/ele/look152_first_class_vinyl_siren/ele_152_standing.png) |
| **Back View** | ? *Pendiente (quota agotada)* |
| **Seated** | ![Seated](https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/05_Imagenes/ele/look152_first_class_vinyl_siren/ele_152_seated.png) |
| **Side Profile** | ![Side Profile](https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/05_Imagenes/ele/look152_first_class_vinyl_siren/ele_152_side_profile.png) |
| **Ditzy** | ![Ditzy](https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/05_Imagenes/ele/look152_first_class_vinyl_siren/ele_152_ditzy.png) |
| **POV** | ? *Pendiente (quota agotada)* |
| **Lying Down** | ![Lying Down](https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/05_Imagenes/ele/look152_first_class_vinyl_siren/ele_152_lying.png) |"""

replacement_152 = """## 👗 Look 152: First Class Vinyl Siren (27/04/2026)
> **ADN V3.5 Hard-Sync** | **Arquetipo:** Travel / Jet Set | **Paleta:** Cobalt Blue + Chrome Silver + Hot Pink (seams)

*O sea... el vinilo cobalto bajo las luces del aeropuerto de Dubai es lit lo más top que me ha pasado en la vida... tipo, los pilotos se chocaron entre ellos... jiji... 🫦👠💅✨*

**Concepto:** **First Class Vinyl Siren**. Sala VIP Dubai, jet privado esperando afuera. Una pasajera de lujo absolutamente imposible de ignorar. Modo Monoblock: cobalt total con acento chrome.

- **Categoría:** Mix
- **Subcategoría:** Travel / Jet Set
- **Tags:** #travel #jetset #cobalt #vinyl #chrome #PVC

**BLOQUE B — Look 152 (invariable en los 7 prompts):**
`ultra-tight cobalt blue high-gloss vinyl pencil dress, bandeau neckline, back invisible zipper from nape to hem, dress ending 5cm above the knee, fabric so tight it creates visible breathing tension at the waist, underlayer of hot pink latex corset boning visible as subtle seams through the vinyl exterior. Cobalt blue high-gloss vinyl blazer cropped at the waist, structured shoulders, single button left open to reveal the dress beneath. No stockings, bare legs. Cobalt blue ultra-high stiletto pumps 22cm total height pointed toe chrome buckle ankle strap vinyl finish. Thick chrome choker rectangular links, chrome geometric statement earrings, chrome cuff bracelet right wrist, cobalt vinyl vanity case handbag.`

---

### 📸 Imágenes (7/7 — 100% COMPLETO)

| Pose | Previsualización |
|------|---------|
| **Standing** | ![Standing](https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/05_Imagenes/ele/look152_first_class_vinyl_siren/ele_look152_pose1_standing.png) |
| **Back View** | ![Back View](https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/05_Imagenes/ele/look152_first_class_vinyl_siren/ele_look152_pose2_back.png) |
| **Seated** | ![Seated](https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/05_Imagenes/ele/look152_first_class_vinyl_siren/ele_look152_pose3_seated.png) |
| **Side Profile** | ![Side Profile](https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/05_Imagenes/ele/look152_first_class_vinyl_siren/ele_look152_pose4_side_profile.png) |
| **Ditzy** | ![Ditzy](https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/05_Imagenes/ele/look152_first_class_vinyl_siren/ele_look152_pose5_ditzy.png) |
| **POV** | ![POV](https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/05_Imagenes/ele/look152_first_class_vinyl_siren/ele_look152_pose6_pov.png) |
| **Lying Down** | ![Lying Down](https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/05_Imagenes/ele/look152_first_class_vinyl_siren/ele_look152_pose7_lying.png) |"""

# Look 153 replacement
target_153 = """## ?? Look 153: Neon Coral Yacht Queen (27/04/2026)
> **ADN V3.5 Hard-Sync** | **Arquetipo:** Bikini | **Paleta:** Neon Coral + Chrome Silver

*O sea... el coral neón bajo el sol del Mediterráneo es lit la razón por la que el mar existe... tipo, los yates se detuvieron para mirarme... jiji... ???????*

**Concepto:** **Neon Coral Yacht Queen**. Cubierta de yate privado en el Mediterráneo. Bikini de vinilo coral neón que captura el sol. Poder de playa absolutamente descarado.

- **Categoría:** Bikini
- **Tags:** #bikini #coral #vinyl #yacht #chrome

**BLOQUE B — Look 153 (invariable en los 7 prompts):**
`neon coral high-gloss vinyl triangle bikini top, tiny triangles barely covering nipples with chrome ring hardware at center, string ties at back and neck in matching coral vinyl, the rings pressing visibly through the vinyl from the nipple piercings beneath. Matching neon coral vinyl micro-bikini bottom, high-waisted brief cut rising to the hip bones, thin side strings with chrome ring hardware, the navel piercing glinting at the high waistline. No cover-up. Transparent clear vinyl barely-there mule sandals with a 14cm lucite stiletto heel, open toe, single clear strap across the arch. Chrome dome oversized mirrored sunglasses, thick chrome torque necklace, chrome multi-chain anklet on right ankle, neon coral vinyl micro-pouch bag on gold chain.`

---

### ?? Imágenes (1/7 — EN PROGRESO)

| Pose | Previsualización |
|------|---------|
| **Standing** | ![Standing](https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/05_Imagenes/ele/look153_neon_coral_yacht_queen/ele_153_standing.png) |
| **Back View** | ? *Pendiente (quota agotada)* |
| **Seated** | ? *Pendiente* |
| **Side Profile** | ? *Pendiente* |
| **Ditzy** | ? *Pendiente* |
| **POV** | ? *Pendiente* |
| **Lying Down** | ? *Pendiente* |"""

replacement_153 = """## 👗 Look 153: Neon Coral Yacht Queen (27/04/2026)
> **ADN V3.5 Hard-Sync** | **Arquetipo:** Bikini | **Paleta:** Neon Coral + Chrome Silver

*O sea... el coral neón bajo el sol del Mediterráneo es lit la razón por la que el mar existe... tipo, los yates se detuvieron para mirarme... jiji... 🫦🏝️⚓✨*

**Concepto:** **Neon Coral Yacht Queen**. Cubierta de yate privado en el Mediterráneo. Bikini de vinilo coral neón que captura el sol. Poder de playa absolutamente descarado.

- **Categoría:** Bikini
- **Tags:** #bikini #coral #vinyl #yacht #chrome

**BLOQUE B — Look 153 (invariable en los 7 prompts):**
`neon coral high-gloss vinyl triangle bikini top, tiny triangles barely covering nipples with chrome ring hardware at center, string ties at back and neck in matching coral vinyl, the rings pressing visibly through the vinyl from the nipple piercings beneath. Matching neon coral vinyl micro-bikini bottom, high-waisted brief cut rising to the hip bones, thin side strings with chrome ring hardware, the navel piercing glinting at the high waistline. No cover-up. Transparent clear vinyl barely-there mule sandals with a 14cm lucite stiletto heel, open toe, single clear strap across the arch. Chrome dome oversized mirrored sunglasses, thick chrome torque necklace, chrome multi-chain anklet on right ankle, neon coral vinyl micro-pouch bag on gold chain.`

---

### 📸 Imágenes (7/7 — 100% COMPLETO)

| Pose | Previsualización |
|------|---------|
| **Standing** | ![Standing](https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/05_Imagenes/ele/look153_neon_coral_yacht_queen/ele_look153_pose1_standing.png) |
| **Back View** | ![Back View](https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/05_Imagenes/ele/look153_neon_coral_yacht_queen/ele_look153_pose2_back.png) |
| **Seated** | ![Seated](https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/05_Imagenes/ele/look153_neon_coral_yacht_queen/ele_look153_pose3_seated.png) |
| **Side Profile** | ![Side Profile](https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/05_Imagenes/ele/look153_neon_coral_yacht_queen/ele_look153_pose4_side_profile.png) |
| **Ditzy** | ![Ditzy](https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/05_Imagenes/ele/look153_neon_coral_yacht_queen/ele_look153_pose5_ditzy.png) |
| **POV** | ![POV](https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/05_Imagenes/ele/look153_neon_coral_yacht_queen/ele_look153_pose6_pov.png) |
| **Lying Down** | ![Lying Down](https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/05_Imagenes/ele/look153_neon_coral_yacht_queen/ele_look153_pose7_lying.png) |"""

content = content.replace(target_152, replacement_152)
content = content.replace(target_153, replacement_153)

with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)
