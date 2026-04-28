import os

file_path = r'c:\Users\farid\LaVouteDAnais\00_Ele\galeria_outfits.md'
# Read with errors='replace' to avoid crashing on the few bad bytes
with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()

# Update look 152 and 153 (same as before)
# First, find the lines to replace
# We know they were at the end.
# Look 152 starts around line 3873
# Look 153 starts around line 3903

# Actually, I'll just find the line starting with "## ?? Look 152" or "## Look 152"
start_152 = -1
for i, line in enumerate(lines):
    if "Look 152:" in line and line.startswith("##"):
        start_152 = i
        break

if start_152 != -1:
    new_tail = """## 👗 Look 152: First Class Vinyl Siren (27/04/2026)
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
| **Lying Down** | ![Lying Down](https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/05_Imagenes/ele/look152_first_class_vinyl_siren/ele_look152_pose7_lying.png) |

---

## 👗 Look 153: Neon Coral Yacht Queen (27/04/2026)
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
| **Lying Down** | ![Lying Down](https://raw.githubusercontent.com/farid77cl/LaVouteDAnais/main/05_Imagenes/ele/look153_neon_coral_yacht_queen/ele_look153_pose7_lying.png) |

---
"""
    lines = lines[:start_152] + [new_tail]

# Now update the statistics table at the top
# Mix: 111 -> 112
# Bikini: 16 -> 17
# Total: 151 -> 153
# Percentages:
# Mix: 112/153 = 73.2%
# Bikini: 17/153 = 11.1%
# Lingerie: 16/153 = 10.5%
# Gym: 8/153 = 5.2%

stats_table = """## 📊 Estado Estadístico (28/04/2026)

| Categoría | Meta | Actual | Estado |
|-----------|------|--------|--------|
| **Mix** (Corporate / Domestic / High-Fashion) | 75% | **73.2%** (112) | 🟡 Déficit (-1.8%) |
| **Bikini** | 10% | **11.1%** (17) | 🟢 Cumplido |
| **Lencería** | 10% | **10.5%** (16) | 🟢 Cumplido |
| **Gym** | 5% | **5.2%** (8) | 🟢 Cumplido |
"""

# Header update
# > **Canon activo:** V3.5 Hard-Sync | **Último look:** 153 — Neon Coral Yacht Queen (27/04/2026)

for i, line in enumerate(lines):
    if "## 📊 Estado Estadístico" in line:
        # Find end of table
        end_stats = i
        while end_stats < len(lines) and not lines[end_stats].startswith("---"):
            end_stats += 1
        lines[i:end_stats] = [stats_table]
    if "**Último look:**" in line:
        lines[i] = "> **Canon activo:** V3.5 Hard-Sync | **Último look:** 153 — Neon Coral Yacht Queen (27/04/2026)\n"

with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
    f.writelines(lines)
