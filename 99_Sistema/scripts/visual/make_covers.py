"""
make_covers.py — La Voûte d'Anaïs
Adds title + author typography to raw cover images.
"""
from PIL import Image, ImageDraw, ImageFont
import textwrap, os

BRAIN = r"C:\Users\fabara\.gemini\antigravity\brain\781a99c6-0f2e-441a-88bd-83906799a5e5"
OUT   = os.path.join(BRAIN, "portadas_finales")
os.makedirs(OUT, exist_ok=True)

COVERS = [
    {
        "src":    os.path.join(BRAIN, "cover_clara_smart_home_v2_1775236784731.png"),
        "title":  "Smart Home Stepford",
        "subtitle": "La Corrupción de Clara",
        "out":    "portada_smart_home_stepford.png",
    },
    {
        "src":    os.path.join(BRAIN, "cover_valeria_elixir_v2_1775236801625.png"),
        "title":  "El Elixir de la Diosa",
        "subtitle": "",
        "out":    "portada_el_elixir_de_la_diosa.png",
    },
    {
        "src":    os.path.join(BRAIN, "cover_esteban_tacones_v2_1775236818271.png"),
        "title":  "Brillando en Tacones",
        "subtitle": "La Metamorfosis de Esteban",
        "out":    "portada_brillando_en_tacones.png",
    },
    {
        "src":    os.path.join(BRAIN, "cover_miss_doll_vinyl_v2_1775236835748.png"),
        "title":  "Eres de los hombres que…",
        "subtitle": "",
        "out":    "portada_eres_de_los_hombres_que.png",
    },
]

AUTHOR = "Anaïs Belland"
BRAND  = "La Voûte d'Anaïs"

# Try to load system fonts, fallback to default
def get_font(size, bold=False):
    candidates_bold = [
        "C:/Windows/Fonts/Georgia Bold.ttf",
        "C:/Windows/Fonts/georgiab.ttf",
        "C:/Windows/Fonts/trebucbd.ttf",
        "C:/Windows/Fonts/arialbd.ttf",
    ]
    candidates = [
        "C:/Windows/Fonts/Georgia.ttf",
        "C:/Windows/Fonts/georgia.ttf",
        "C:/Windows/Fonts/trebuc.ttf",
        "C:/Windows/Fonts/arial.ttf",
    ]
    pool = candidates_bold if bold else candidates
    for path in pool:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    return ImageFont.load_default()

def draw_text_with_shadow(draw, pos, text, font, fill, shadow_fill=(0,0,0,200), offset=3):
    x, y = pos
    draw.text((x+offset, y+offset), text, font=font, fill=shadow_fill)
    draw.text((x, y), text, font=font, fill=fill)

def add_cover_text(cfg):
    img = Image.open(cfg["src"]).convert("RGBA")
    W, H = img.size

    # ── Top band: brand ─────────────────────────────────────────────────
    band_h = int(H * 0.08)
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # Dark top gradient band
    for y in range(band_h):
        alpha = int(200 * (1 - y / band_h))
        draw.rectangle([(0, y), (W, y+1)], fill=(0, 0, 0, alpha))

    # Dark bottom band for title/author
    bot_h = int(H * 0.30)
    for y in range(H - bot_h, H):
        alpha = int(210 * ((y - (H - bot_h)) / bot_h))
        draw.rectangle([(0, y), (W, y+1)], fill=(10, 0, 10, alpha))

    img = Image.alpha_composite(img, overlay)
    draw = ImageDraw.Draw(img)

    # Brand at top
    font_brand = get_font(max(18, W // 30))
    draw_text_with_shadow(draw, (W // 2 - draw.textlength(BRAND, font=font_brand) // 2, band_h // 4),
                          BRAND, font_brand, fill=(255, 192, 203, 240))

    # ── Bottom band: title + subtitle + author ───────────────────────────
    y_bot = H - bot_h + int(H * 0.03)

    # Title
    font_title = get_font(max(36, W // 14), bold=True)
    title = cfg["title"]
    tw = draw.textlength(title, font=font_title)
    # Wrap if too wide
    if tw > W * 0.90:
        lines = textwrap.wrap(title, width=max(10, int(len(title) * W * 0.88 / tw)))
    else:
        lines = [title]
    for line in lines:
        lw = draw.textlength(line, font=font_title)
        draw_text_with_shadow(draw, ((W - lw) // 2, y_bot), line, font_title,
                              fill=(255, 255, 255, 255))
        y_bot += font_title.size + 4

    # Subtitle (italic feel via smaller size)
    if cfg.get("subtitle"):
        font_sub = get_font(max(22, W // 24))
        sw = draw.textlength(cfg["subtitle"], font=font_sub)
        draw_text_with_shadow(draw, ((W - sw) // 2, y_bot), cfg["subtitle"], font_sub,
                              fill=(255, 182, 193, 230))
        y_bot += font_sub.size + 10

    # Divider line
    y_bot += 6
    draw.line([(W // 6, y_bot), (W * 5 // 6, y_bot)], fill=(255, 182, 193, 160), width=1)
    y_bot += 10

    # Author name
    font_author = get_font(max(26, W // 20))
    aw = draw.textlength(AUTHOR, font=font_author)
    draw_text_with_shadow(draw, ((W - aw) // 2, y_bot), AUTHOR, font_author,
                          fill=(255, 210, 220, 245))

    # Save
    out_path = os.path.join(OUT, cfg["out"])
    img.convert("RGB").save(out_path, "PNG", quality=95)
    print(f"✅  {cfg['out']}")
    return out_path

paths = []
for cfg in COVERS:
    paths.append(add_cover_text(cfg))

print("\n🫦 4 portadas generadas en:", OUT)
