"""Build GeoAI_Pitch_Deck.pptx — 13-slide YC-format seed deck."""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt
import copy

# ── Palette ──────────────────────────────────────────────────────────────────
DARK_BG    = RGBColor(0x0D, 0x14, 0x28)   # slide background dark
MID_BG     = RGBColor(0x0F, 0x1A, 0x30)
COVER_BG   = RGBColor(0x0D, 0x23, 0x46)
ACCENT     = RGBColor(0x4F, 0xC3, 0xF7)   # bright blue
WHITE      = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_TEXT = RGBColor(0xB0, 0xB8, 0xCC)
DIM_TEXT   = RGBColor(0x7A, 0x90, 0xB0)
GREEN      = RGBColor(0x4C, 0xAF, 0x50)
RED_SOFT   = RGBColor(0xEF, 0x9A, 0x9A)
CARD_BG    = RGBColor(0x14, 0x20, 0x3A)
CARD_BORD  = RGBColor(0x25, 0x38, 0x58)

# Slide dimensions: 16:9 widescreen
W = Inches(13.33)
H = Inches(7.5)

prs = Presentation()
prs.slide_width  = W
prs.slide_height = H

BLANK = prs.slide_layouts[6]   # completely blank


# ── Helpers ──────────────────────────────────────────────────────────────────

def add_slide(bg_color=DARK_BG):
    slide = prs.slides.add_slide(BLANK)
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = bg_color
    return slide


def txb(slide, text, x, y, w, h,
        size=18, bold=False, color=WHITE, align=PP_ALIGN.LEFT,
        italic=False, wrap=True):
    """Add a text box and return the run."""
    tf_box = slide.shapes.add_textbox(x, y, w, h)
    tf = tf_box.text_frame
    tf.word_wrap = wrap
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    return tf_box


def tag(slide, text, y=Inches(0.55)):
    """Slide section tag (small caps blue label)."""
    t = txb(slide, text.upper(),
            Inches(0.7), y, Inches(11.93), Inches(0.35),
            size=9, bold=True, color=ACCENT, align=PP_ALIGN.LEFT)
    t.text_frame.paragraphs[0].runs[0].font.color.rgb = ACCENT
    return t


def heading(slide, text, y=Inches(1.05), size=34):
    return txb(slide, text, Inches(0.7), y, Inches(11.93), Inches(1.1),
               size=size, bold=True, color=WHITE)


def sub(slide, text, y, w=Inches(11.93), size=14, color=LIGHT_TEXT):
    return txb(slide, text, Inches(0.7), y, w, Inches(1.4),
               size=size, color=color, wrap=True)


def rect(slide, x, y, w, h, fill=CARD_BG, border=CARD_BORD, radius=None):
    shape = slide.shapes.add_shape(
        1,  # MSO_SHAPE_TYPE.RECTANGLE
        x, y, w, h
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    shape.line.color.rgb = border
    shape.line.width = Pt(0.75)
    return shape


def card_with_text(slide, x, y, w, h, title, body,
                   title_size=13, body_size=11,
                   bg=CARD_BG, border=CARD_BORD,
                   title_color=WHITE, body_color=LIGHT_TEXT):
    rect(slide, x, y, w, h, fill=bg, border=border)
    if title:
        txb(slide, title, x + Inches(0.18), y + Inches(0.18),
            w - Inches(0.36), Inches(0.35),
            size=title_size, bold=True, color=title_color, wrap=True)
    if body:
        txb(slide, body, x + Inches(0.18), y + Inches(0.52),
            w - Inches(0.36), h - Inches(0.65),
            size=body_size, color=body_color, wrap=True)


def divider(slide, y, color=ACCENT, alpha_like=False):
    line = slide.shapes.add_shape(1, Inches(0.7), y, Inches(1.2), Pt(2))
    line.fill.solid()
    line.fill.fore_color.rgb = color
    line.line.fill.background()


# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 1 — COVER
# ─────────────────────────────────────────────────────────────────────────────
s = add_slide(COVER_BG)

# Big logo: "Geo" in accent + "AI" in white
logo_box = s.shapes.add_textbox(Inches(3.2), Inches(1.6), Inches(6.9), Inches(1.4))
lf = logo_box.text_frame
lf.word_wrap = False
lp = lf.paragraphs[0]
lp.alignment = PP_ALIGN.CENTER
r1 = lp.add_run(); r1.text = "Geo"
r1.font.size = Pt(64); r1.font.bold = True; r1.font.color.rgb = ACCENT
r2 = lp.add_run(); r2.text = "AI"
r2.font.size = Pt(64); r2.font.bold = True; r2.font.color.rgb = WHITE

txb(s, "Ask your maps a question. Get the answer on the map.",
    Inches(1.5), Inches(3.1), Inches(10.33), Inches(0.7),
    size=20, color=LIGHT_TEXT, align=PP_ALIGN.CENTER)
txb(s, "On-premise AI for geospatial data — no SQL, no cloud.",
    Inches(1.5), Inches(3.75), Inches(10.33), Inches(0.55),
    size=18, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
txb(s, "SEED ROUND  ·  SEPTEMBER 2026  ·  GEOAI B.V.",
    Inches(1.5), Inches(5.8), Inches(10.33), Inches(0.4),
    size=10, color=DIM_TEXT, align=PP_ALIGN.CENTER)


# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 2 — PROBLEM
# ─────────────────────────────────────────────────────────────────────────────
s = add_slide(DARK_BG)
tag(s, "The Problem")
heading(s, "GIS data is everywhere. Insights are not.", size=30)
sub(s, "Every municipality, water board, and utility sits on hundreds of spatial datasets —\nbut answering even simple questions takes hours.", Inches(2.1), size=13)

# 4 pain cards (2x2)
CW = Inches(5.7); CH = Inches(1.6)
XL = Inches(0.7); XR = Inches(6.63)
Y1 = Inches(2.65); Y2 = Inches(4.35)

card_with_text(s, XL, Y1, CW, CH,
    "⏳  Hours lost to SQL",
    "A GIS analyst needs complex PostGIS queries for every ad-hoc spatial question. A single analysis takes 2–4 hours instead of 2 minutes.",
    bg=RGBColor(0x18,0x10,0x12), border=RGBColor(0x50,0x20,0x20),
    title_color=RED_SOFT, body_color=DIM_TEXT)

card_with_text(s, XR, Y1, CW, CH,
    "🔒  Data locked from decision-makers",
    "Policy officers and managers need geo insights daily but cannot access them without a GIS specialist. GIS teams are the bottleneck.",
    bg=RGBColor(0x18,0x10,0x12), border=RGBColor(0x50,0x20,0x20),
    title_color=RED_SOFT, body_color=DIM_TEXT)

card_with_text(s, XL, Y2, CW, CH,
    "☁️  Cloud AI is not an option",
    "Dutch government data cannot leave the premises. ChatGPT-based tools are legally blocked for this sector under EU data sovereignty rules.",
    bg=RGBColor(0x18,0x10,0x12), border=RGBColor(0x50,0x20,0x20),
    title_color=RED_SOFT, body_color=DIM_TEXT)

card_with_text(s, XR, Y2, CW, CH,
    "💸  Esri owns the market",
    "ArcGIS costs €30K–150K/year per org. Its AI features require cloud. Dutch municipalities are actively looking for a sovereign alternative.",
    bg=RGBColor(0x18,0x10,0x12), border=RGBColor(0x50,0x20,0x20),
    title_color=RED_SOFT, body_color=DIM_TEXT)


# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 3 — SOLUTION
# ─────────────────────────────────────────────────────────────────────────────
s = add_slide(MID_BG)
tag(s, "The Solution")
heading(s, "Natural language → GIS analysis → map", size=30)

# Quote/example card
rect(s, Inches(0.7), Inches(2.05), Inches(11.93), Inches(1.25),
     fill=RGBColor(0x0A,0x22,0x3A), border=RGBColor(0x2A,0x6A,0x9A))
txb(s, '"Show me all buildings losing the most heat, within 200m of a gas pipeline, in Stadshart."',
    Inches(0.9), Inches(2.15), Inches(11.53), Inches(0.45),
    size=12, italic=True, color=RGBColor(0xE0,0xE8,0xF4))
txb(s, "→  GeoAI finds the right layers, runs buffer + spatial join + attribute filter, renders on map and explains:\n"
       '"47 buildings found. Average heat loss index 8.2. Top priority: Rembrandtweg 12–34."',
    Inches(0.9), Inches(2.6), Inches(11.53), Inches(0.55),
    size=11, color=ACCENT)

# 3 benefit bullets
bullets = [
    ("✓  Zero learning curve",     "Any staff member can use it in plain language — no SQL, no GIS training required."),
    ("✓  100% on-premise",         "Data never leaves the server. Full compliance with Dutch/EU data sovereignty rules."),
    ("✓  Works with existing data","Plugs directly into your PostGIS database. No migration, no vendor lock-in."),
]
BW = Inches(3.7); BH = Inches(1.3)
bx = [Inches(0.7), Inches(4.62), Inches(8.54)]
for i, (title, body) in enumerate(bullets):
    card_with_text(s, bx[i], Inches(3.45), BW, BH,
                   title, body,
                   title_color=ACCENT, body_color=DIM_TEXT,
                   bg=RGBColor(0x0C,0x1C,0x30), border=RGBColor(0x1E,0x40,0x60))


# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 4 — PRODUCT / PIPELINE
# ─────────────────────────────────────────────────────────────────────────────
s = add_slide(DARK_BG)
tag(s, "Product")
heading(s, "Five-step AI pipeline — fully on-premise", size=28)

# Pipeline boxes
steps = [
    ("💬", "NL Query",    "User types question\nin Dutch or English"),
    ("🗂️", "Data Catalog", "pgvector semantic\nsearch over 287+ layers"),
    ("🧠", "AI Planner",  "Qwen3 14B generates\nJSON execution plan"),
    ("⚙️",  "Execution",   "PostGIS SQL &\nGeoPandas run analysis"),
    ("🗺️", "Output",      "MapLibre map +\nNL summary + export"),
]
SW = Inches(1.95); SH = Inches(1.5); SY = Inches(2.05)
GAP = Inches(0.28); ARW = Inches(0.25)
sx = Inches(0.7)
for i, (icon, title, body) in enumerate(steps):
    rect(s, sx, SY, SW, SH, fill=RGBColor(0x0A,0x1E,0x35), border=RGBColor(0x1E,0x55,0x80))
    txb(s, icon, sx, SY + Inches(0.12), SW, Inches(0.38), size=20, align=PP_ALIGN.CENTER)
    txb(s, title, sx, SY + Inches(0.55), SW, Inches(0.3), size=11, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    txb(s, body, sx, SY + Inches(0.88), SW, Inches(0.55), size=9, color=DIM_TEXT, align=PP_ALIGN.CENTER)
    sx += SW
    if i < 4:
        txb(s, "→", sx, SY + Inches(0.5), ARW + Inches(0.05), Inches(0.4),
            size=14, color=ACCENT, align=PP_ALIGN.CENTER)
        sx += GAP + ARW

# 3 detail cards
dc = [
    ("Supported Operations",
     "Buffer · Spatial Join · Intersect · Clip · Nearest Neighbor · Aggregate · Heatmap · Routing · Attribute Filter · Dissolve"),
    ("Tech Stack",
     "Spring Boot 4 · PostgreSQL 17 + PostGIS · pgvector · Ollama · Qwen3 14B · FastAPI · MapLibre · Redis"),
    ("Hardware",
     "Single mini-server: AMD Ryzen AI Max+ 395 · 128GB RAM · 50 TOPS NPU · ~€3K hardware cost"),
]
DW = Inches(3.7); DH = Inches(1.2)
dx = [Inches(0.7), Inches(4.62), Inches(8.54)]
for i, (t, b) in enumerate(dc):
    card_with_text(s, dx[i], Inches(3.85), DW, DH, t, b, body_size=10)


# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 5 — WHY NOW
# ─────────────────────────────────────────────────────────────────────────────
s = add_slide(RGBColor(0x0A,0x0F,0x1E))
tag(s, "Why Now")
heading(s, "Three tailwinds are converging", size=30)

why = [
    ("🤖", "LLMs finally work on-premise",
     "Models like Qwen3 14B run on consumer hardware with response times under 3 seconds. Two years ago this was impossible at this price point."),
    ("🇪🇺", "EU AI Act + data sovereignty",
     "The EU AI Act and Dutch government policy mandate that sensitive public data stays on-premise. Cloud AI vendors are being blocked from government contracts."),
    ("🏛️", "Municipalities are ready",
     "Dutch gemeenten are actively replacing Esri. Geosquare alone serves 100 municipalities in this migration. GIS AI is their #1 requested feature for 2026."),
]
WW = Inches(3.7); WH = Inches(2.2)
wx = [Inches(0.7), Inches(4.62), Inches(8.54)]
for i, (icon, title, body) in enumerate(why):
    rect(s, wx[i], Inches(2.1), WW, WH,
         fill=RGBColor(0x0C,0x1E,0x32), border=RGBColor(0x1E,0x44,0x68))
    txb(s, icon, wx[i], Inches(2.18), WW, Inches(0.5), size=24, align=PP_ALIGN.CENTER)
    txb(s, title, wx[i] + Inches(0.15), Inches(2.72), WW - Inches(0.3), Inches(0.38),
        size=13, bold=True, color=WHITE)
    txb(s, body, wx[i] + Inches(0.15), Inches(3.14), WW - Inches(0.3), Inches(1.1),
        size=10, color=DIM_TEXT)

# Bottom note card
rect(s, Inches(0.7), Inches(4.5), Inches(11.93), Inches(0.85),
     fill=RGBColor(0x08,0x18,0x2A), border=RGBColor(0x1E,0x44,0x68))
txb(s, "First-mover window: Camp to Camp (closest comparable product) was acquired by Swiss Telecom and is losing momentum. "
       "There is no on-premise NL→GIS product serving the Dutch/EU government market today.",
    Inches(0.9), Inches(4.6), Inches(11.53), Inches(0.7), size=11, color=LIGHT_TEXT)


# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 6 — MARKET
# ─────────────────────────────────────────────────────────────────────────────
s = add_slide(DARK_BG)
tag(s, "Market Size")
heading(s, "Large, defensible, and underserved", size=30)

# 3 stat boxes
stats = [
    ("€2.4B", "TAM — EU government\nGIS software market"),
    ("€180M", "SAM — Netherlands\n(gemeenten + waterschappen + utilities)"),
    ("€9M",   "SOM Year 3\n(30 organizations via partners)"),
]
BW2 = Inches(3.7); BH2 = Inches(1.25)
bx2 = [Inches(0.7), Inches(4.62), Inches(8.54)]
for i, (num, lbl) in enumerate(stats):
    rect(s, bx2[i], Inches(2.0), BW2, BH2,
         fill=RGBColor(0x08,0x1C,0x30), border=RGBColor(0x1E,0x55,0x80))
    txb(s, num, bx2[i], Inches(2.08), BW2, Inches(0.58),
        size=34, bold=True, color=ACCENT, align=PP_ALIGN.CENTER)
    txb(s, lbl, bx2[i], Inches(2.65), BW2, Inches(0.55),
        size=10, color=DIM_TEXT, align=PP_ALIGN.CENTER)

# Two columns
nl_lines = [
    "🏛  342 Gemeenten (municipalities)",
    "💧  21 Waterschappen (water boards)",
    "🛣  1 Rijkswaterstaat (national)",
    "⚡  50+ Utility companies (Stedin, Alliander…)",
    "    Average license: €20K–30K/year",
]
eu_lines = [
    "🇩🇪  Germany — 11,000+ municipalities",
    "🇧🇪  Belgium — strong FOSS4G community",
    "🇫🇷  France — IGN partnership opportunities",
    "🌍  FOSS4G global network (built-in distribution)",
    "    GeoCommons EU grant: €6M call open",
]

rect(s, Inches(0.7), Inches(3.45), Inches(5.7), Inches(2.4),
     fill=CARD_BG, border=CARD_BORD)
txb(s, "Netherlands (beachhead)", Inches(0.88), Inches(3.55), Inches(5.34), Inches(0.3),
    size=12, bold=True, color=WHITE)
txb(s, "\n".join(nl_lines), Inches(0.88), Inches(3.85), Inches(5.34), Inches(1.9),
    size=10, color=LIGHT_TEXT)

rect(s, Inches(6.63), Inches(3.45), Inches(6.0), Inches(2.4),
     fill=CARD_BG, border=CARD_BORD)
txb(s, "EU Expansion (Year 2–3)", Inches(6.81), Inches(3.55), Inches(5.64), Inches(0.3),
    size=12, bold=True, color=WHITE)
txb(s, "\n".join(eu_lines), Inches(6.81), Inches(3.85), Inches(5.64), Inches(1.9),
    size=10, color=LIGHT_TEXT)


# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 7 — BUSINESS MODEL
# ─────────────────────────────────────────────────────────────────────────────
s = add_slide(MID_BG)
tag(s, "Business Model")
heading(s, "License through GIS contractors — OEM distribution", size=26)
sub(s, "We cannot sell directly to Dutch government. We sell to GIS contractors who build apps for municipalities.\nThey embed GeoAI and pay us per deployment.",
    Inches(2.1), size=12)

# Table header
HDR = RGBColor(0x08,0x28,0x44)
HDR_TXT = ACCENT
cols = [Inches(2.5), Inches(2.5), Inches(4.43), Inches(2.0)]
headers = ["Tier", "Buyer", "What they get", "Our Revenue"]
hx = Inches(0.7)
for i, (h, cw) in enumerate(zip(headers, cols)):
    rect(s, hx, Inches(2.75), cw, Inches(0.38), fill=HDR, border=HDR)
    txb(s, h, hx + Inches(0.1), Inches(2.78), cw - Inches(0.1), Inches(0.3),
        size=10, bold=True, color=HDR_TXT)
    hx += cw

rows = [
    ("Pilot",         "First contractor",             "3-month trial, 1 municipality, limited layers",        "€5K"),
    ("OEM Starter",   "GIS software vendor",          "API license, up to 10 deployments",                   "€2,500/mo"),
    ("OEM Growth",    "GIS software vendor",          "API license, up to 50 deployments",                   "€8,000/mo"),
    ("OEM Enterprise","Large vendor (Geosquare)",     "Unlimited deployments + custom fine-tuning",           "€15K–25K/mo"),
    ("Direct Project","Contractor per project",       "On-premise deployment + 1-year support",              "€30K + €20K/yr"),
]
ROW_H = Inches(0.54)
ROW_BG  = RGBColor(0x0E,0x1C,0x30)
ROW_BG2 = RGBColor(0x0C,0x18,0x28)
for ri, row in enumerate(rows):
    bg = ROW_BG if ri % 2 == 0 else ROW_BG2
    rx = Inches(0.7)
    ry = Inches(3.13) + ri * ROW_H
    for ci, (cell, cw) in enumerate(zip(row, cols)):
        rect(s, rx, ry, cw, ROW_H, fill=bg, border=RGBColor(0x1A,0x2C,0x44))
        col = ACCENT if ci == 3 else (WHITE if ci == 0 else LIGHT_TEXT)
        txb(s, cell, rx + Inches(0.1), ry + Inches(0.14), cw - Inches(0.1), ROW_H - Inches(0.1),
            size=10, color=col)
        rx += cw

# Bottom note
rect(s, Inches(0.7), Inches(5.95), Inches(11.93), Inches(0.7),
     fill=RGBColor(0x08,0x18,0x2A), border=RGBColor(0x1A,0x3A,0x58))
txb(s, "Path to €1M ARR: 1 OEM Enterprise contract (Geosquare, 100 municipalities) = €180K–300K ARR.  "
       "3 OEM Growth contracts = €288K ARR.  10 direct projects = €500K ARR.  Realistic within 18 months.",
    Inches(0.9), Inches(6.05), Inches(11.53), Inches(0.55), size=10, color=LIGHT_TEXT)


# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 8 — TRACTION
# ─────────────────────────────────────────────────────────────────────────────
s = add_slide(DARK_BG)
tag(s, "Traction")
heading(s, "Early validation from the right players", size=30)

traction = [
    ("Gemeente Amstelveen pilot",
     "Active pilot with 287 PostGIS layers indexed. Live demos: energy label analysis, tree felling, drainage routing."),
    ("Geosquare — 100 municipalities",
     "CTO Peter Paul Koonings confirmed intent to integrate GeoAI. Demo at their October 2026 conference. Deal target: Jan 2027."),
    ("FOSS4G 2026 network",
     "Active in global open-source GIS community. Camp to Camp, IGN France, and Provincie Zuid-Holland all engaged."),
    ("Provincie Zuid-Holland",
     "Presented at KennisKring GeoAI. AI Architect Thijs Oosterhuis exploring GeoAI for their data team."),
    ("Working prototype",
     "5-step pipeline operational. NL queries answered end-to-end on Amstelveen data. Live demo videos available."),
    ("Advisor pipeline",
     "Vital Schreurs (built & sold GIM), Octavian Borca (BD, success-fee), Interim Innovators (RWS, PWN, ATOS)."),
]
TH = Inches(0.72)
for i, (title, body) in enumerate(traction):
    ty = Inches(2.05) + i * (TH + Inches(0.06))
    rect(s, Inches(0.7), ty, Inches(11.93), TH,
         fill=RGBColor(0x0C,0x18,0x28), border=RGBColor(0x16,0x2C,0x46))
    txb(s, "✅", Inches(0.85), ty + Inches(0.18), Inches(0.38), Inches(0.36),
        size=14, color=GREEN)
    txb(s, title, Inches(1.25), ty + Inches(0.1), Inches(3.8), Inches(0.28),
        size=11, bold=True, color=WHITE)
    txb(s, body, Inches(1.25), ty + Inches(0.38), Inches(10.9), Inches(0.3),
        size=10, color=DIM_TEXT)


# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 9 — GO-TO-MARKET
# ─────────────────────────────────────────────────────────────────────────────
s = add_slide(MID_BG)
tag(s, "Go-to-Market")
heading(s, "Distribution through GIS contractors we already know", size=26)

# Left column — phases
phase1 = [
    "1  Close Geosquare OEM deal — embed GeoAI in their suite for 100 municipalities by Jan 2027",
    "2  Expand Amstelveen pilot to paid annual license via their contractor",
    "3  Engage Net4s, D2Win, Tensing — target 2 more contractor partnerships",
]
phase2 = [
    "4  Open-source the core (marketing + credibility) — drive inbound from FOSS4G community",
    "5  Apply for GeoCommons EU grant (€6M call) — fund EU expansion with non-dilutive capital",
    "6  Enter Belgium and Germany via FOSS4G Europe network (IGN, OSGeo partners)",
]

rect(s, Inches(0.7), Inches(2.05), Inches(6.0), Inches(4.7),
     fill=CARD_BG, border=CARD_BORD)
txb(s, "Phase 1 — Beachhead  (Now → Mo. 6)", Inches(0.9), Inches(2.15),
    Inches(5.7), Inches(0.32), size=12, bold=True, color=ACCENT)
for i, line in enumerate(phase1):
    txb(s, line, Inches(0.9), Inches(2.52) + i * Inches(0.42),
        Inches(5.7), Inches(0.38), size=10, color=LIGHT_TEXT)
txb(s, "Phase 2 — Scale  (Mo. 7–18)", Inches(0.9), Inches(3.85),
    Inches(5.7), Inches(0.32), size=12, bold=True, color=ACCENT)
for i, line in enumerate(phase2):
    txb(s, line, Inches(0.9), Inches(4.22) + i * Inches(0.42),
        Inches(5.7), Inches(0.38), size=10, color=LIGHT_TEXT)

# Right column — contractors + why they buy
rect(s, Inches(7.0), Inches(2.05), Inches(5.63), Inches(2.1),
     fill=CARD_BG, border=CARD_BORD)
txb(s, "Target Contractors (warm leads)", Inches(7.18), Inches(2.15),
    Inches(5.3), Inches(0.3), size=12, bold=True, color=WHITE)
txb(s, "Geosquare  ·  Net4s  ·  D2Win  ·  Sweco  ·  CGI  ·  Tensing  ·  NieuwlandGeo  ·  Allinq",
    Inches(7.18), Inches(2.5), Inches(5.3), Inches(0.55),
    size=11, color=ACCENT)

rect(s, Inches(7.0), Inches(4.3), Inches(5.63), Inches(2.45),
     fill=CARD_BG, border=CARD_BORD)
txb(s, "Why contractors buy", Inches(7.18), Inches(4.4),
    Inches(5.3), Inches(0.3), size=12, bold=True, color=WHITE)
txb(s, "Their clients (municipalities) are asking for AI. Building it themselves costs €200K+. "
       "Buying GeoAI as an OEM API gives them the feature in weeks, not years.\n\n"
       "We are their R&D department for AI.",
    Inches(7.18), Inches(4.78), Inches(5.3), Inches(1.8),
    size=10, color=DIM_TEXT)


# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 10 — COMPETITION
# ─────────────────────────────────────────────────────────────────────────────
s = add_slide(DARK_BG)
tag(s, "Competition")
heading(s, "No direct on-premise NL→GIS competitor exists today", size=26)

comp_headers = ["Solution", "On-Premise", "NL→GIS (no SQL)", "PostGIS Native", "EU Gov Ready"]
comp_cols    = [Inches(3.0), Inches(2.35), Inches(2.35), Inches(2.35), Inches(1.93)]
comp_rows = [
    ("GeoAI  ← Us",            "✅", "✅", "✅", "✅", True),
    ("Esri ArcGIS AI",          "❌ Cloud only", "✅", "❌", "❌ Data leaves EU", False),
    ("Camp to Camp / GeoLLM",   "✅", "~ Limited", "~ Partial", "~ Swiss; acquired", False),
    ("Carto / MapChat",         "❌ SaaS only", "✅", "❌", "❌", False),
    ("GeoAgent (opengeos)",     "✅", "~ Research", "❌", "❌ Not productized", False),
]
HDR_H = Inches(0.38); ROW_H2 = Inches(0.55)
# header row
cx = Inches(0.7)
for h, cw in zip(comp_headers, comp_cols):
    rect(s, cx, Inches(2.05), cw, HDR_H,
         fill=RGBColor(0x08,0x28,0x44), border=RGBColor(0x10,0x40,0x68))
    txb(s, h, cx + Inches(0.08), Inches(2.1), cw - Inches(0.08), Inches(0.3),
        size=9, bold=True, color=ACCENT)
    cx += cw

for ri, row in enumerate(comp_rows):
    is_us = row[5]
    cells = row[:5]
    rx = Inches(0.7)
    ry = Inches(2.43) + ri * ROW_H2
    bg = RGBColor(0x08,0x20,0x38) if is_us else (RGBColor(0x0C,0x18,0x28) if ri % 2 == 0 else RGBColor(0x0A,0x14,0x22))
    for ci, (cell, cw) in enumerate(zip(cells, comp_cols)):
        rect(s, rx, ry, cw, ROW_H2, fill=bg,
             border=RGBColor(0x1E,0x44,0x68) if is_us else RGBColor(0x14,0x28,0x40))
        col = ACCENT if (is_us and ci == 0) else (
              GREEN if cell.startswith("✅") else (
              RED_SOFT if cell.startswith("❌") else LIGHT_TEXT))
        txb(s, cell, rx + Inches(0.08), ry + Inches(0.15), cw - Inches(0.08), Inches(0.38),
            size=10, color=col, bold=(is_us and ci == 0))
        rx += cw

rect(s, Inches(0.7), Inches(5.4), Inches(11.93), Inches(0.75),
     fill=RGBColor(0x08,0x18,0x2A), border=RGBColor(0x1A,0x3A,0x58))
txb(s, "Our moat: On-premise deployment + PostGIS-native execution + Dutch gov compliance + FOSS4G community distribution. "
       "These four together cannot be replicated by US cloud vendors or research projects.",
    Inches(0.9), Inches(5.5), Inches(11.53), Inches(0.6), size=10, color=LIGHT_TEXT)


# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 11 — TEAM
# ─────────────────────────────────────────────────────────────────────────────
s = add_slide(MID_BG)
tag(s, "Team")
heading(s, "Domain-first team — GIS × AI × BD", size=30)

team = [
    ("A", "Adrian Akbari", "Founder & CEO",
     "GIS architect with deep PostGIS & AI integration expertise. Designed enterprise geo-systems for Stedin (utility), RWS, and municipalities. Full-stack: architecture to BD."),
    ("+", "AI/GIS Engineer", "Hiring — Python · PostGIS · LLM",
     "Mid-level Python developer with GIS background. Will own the execution engine, prompt engineering pipeline, and data catalog automation."),
    ("+", "GIS Frontend Dev", "Hiring — MapLibre · FastAPI",
     "Frontend developer with MapLibre/Leaflet experience. Owns the map output layer, UI, and vector tile integration."),
]
TW = Inches(3.7); TH2 = Inches(2.2)
tx = [Inches(0.7), Inches(4.62), Inches(8.54)]
for i, (init, name, role, bio) in enumerate(team):
    rect(s, tx[i], Inches(2.05), TW, TH2, fill=CARD_BG, border=CARD_BORD)
    # avatar circle (rectangle as proxy)
    rect(s, tx[i] + Inches(1.45), Inches(2.15), Inches(0.8), Inches(0.5),
         fill=RGBColor(0x0D,0x3B,0x6E), border=RGBColor(0x1E,0x55,0x9A))
    txb(s, init, tx[i] + Inches(1.45), Inches(2.16), Inches(0.8), Inches(0.46),
        size=14, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    txb(s, name, tx[i] + Inches(0.15), Inches(2.72), TW - Inches(0.3), Inches(0.3),
        size=13, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
    txb(s, role, tx[i] + Inches(0.15), Inches(3.03), TW - Inches(0.3), Inches(0.28),
        size=10, color=ACCENT, align=PP_ALIGN.CENTER)
    txb(s, bio, tx[i] + Inches(0.15), Inches(3.33), TW - Inches(0.3), Inches(0.85),
        size=9.5, color=DIM_TEXT)

# Advisor card
rect(s, Inches(0.7), Inches(4.42), Inches(5.7), Inches(2.4),
     fill=CARD_BG, border=CARD_BORD)
txb(s, "Advisors & Network", Inches(0.88), Inches(4.52),
    Inches(5.34), Inches(0.3), size=12, bold=True, color=WHITE)
txb(s, "Vital Schreurs — Built & sold GIM; 30 yrs gov/utilities BD\n"
       "Octavian Borca — BD (Swiss Post, EU clients)\n"
       "Interim Innovators — RWS, PWN, ATOS geo network\n"
       "Peter Paul Koonings — Geosquare CTO (100 municipalities)",
    Inches(0.88), Inches(4.88), Inches(5.34), Inches(1.8),
    size=10, color=LIGHT_TEXT)

rect(s, Inches(6.63), Inches(4.42), Inches(6.0), Inches(2.4),
     fill=CARD_BG, border=CARD_BORD)
txb(s, "Why we will win", Inches(6.81), Inches(4.52),
    Inches(5.64), Inches(0.3), size=12, bold=True, color=WHITE)
txb(s, "We are not engineers who discovered GIS — we are GIS experts who built the AI. "
       "We know exactly what questions municipalities ask, what data they have, and which contractors "
       "hold the relationships. That domain knowledge is not transferable.",
    Inches(6.81), Inches(4.88), Inches(5.64), Inches(1.8),
    size=10, color=LIGHT_TEXT)


# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 12 — THE ASK
# ─────────────────────────────────────────────────────────────────────────────
s = add_slide(RGBColor(0x0A,0x0F,0x1E))
tag(s, "The Ask")
heading(s, "Raising €350,000 seed — 18 months to first revenue", size=28)

# Use of funds card
rect(s, Inches(0.7), Inches(2.05), Inches(5.9), Inches(4.65),
     fill=CARD_BG, border=CARD_BORD)
txb(s, "Use of Funds", Inches(0.9), Inches(2.15),
    Inches(5.5), Inches(0.3), size=13, bold=True, color=WHITE)
funds = [
    ("AI/GIS Engineer (18 mo.)",       "35% · €122K"),
    ("Frontend Developer (12 mo.)",    "25% · €88K"),
    ("Hardware + infrastructure",       "10% · €35K"),
    ("Legal, IP, GDPR compliance",      " 8% · €28K"),
    ("BD + sales (travel, events)",     "12% · €42K"),
    ("Buffer / ops",                    "10% · €35K"),
]
for i, (item, pct) in enumerate(funds):
    fy = Inches(2.55) + i * Inches(0.62)
    txb(s, item, Inches(0.9), fy, Inches(3.5), Inches(0.38), size=10.5, color=LIGHT_TEXT)
    txb(s, pct, Inches(4.4), fy, Inches(1.8), Inches(0.38), size=10.5, color=ACCENT, align=PP_ALIGN.RIGHT)
    # divider line
    if i < len(funds) - 1:
        rect(s, Inches(0.9), fy + Inches(0.46), Inches(5.3), Pt(1),
             fill=RGBColor(0x1A,0x2C,0x44), border=RGBColor(0x1A,0x2C,0x44))

# Milestones card
rect(s, Inches(6.93), Inches(2.05), Inches(5.7), Inches(3.0),
     fill=CARD_BG, border=CARD_BORD)
txb(s, "18-Month Milestones", Inches(7.1), Inches(2.15),
    Inches(5.34), Inches(0.3), size=13, bold=True, color=WHITE)
milestones = [
    ("Mo. 1–3",   "Production prototype; Geosquare integration live"),
    ("Mo. 4–6",   "First paid license signed; 3 contractor pilots active"),
    ("Mo. 7–12",  "€150K ARR; open-source release; EU grant application"),
    ("Mo. 13–18", "€500K ARR; 2nd market entry (Belgium/Germany)"),
]
for i, (mo, text) in enumerate(milestones):
    my = Inches(2.6) + i * Inches(0.58)
    txb(s, mo, Inches(7.1), my, Inches(1.1), Inches(0.38), size=10, bold=True, color=ACCENT)
    txb(s, text, Inches(8.25), my, Inches(4.25), Inches(0.38), size=10, color=LIGHT_TEXT)

# What we need card
rect(s, Inches(6.93), Inches(5.2), Inches(5.7), Inches(1.5),
     fill=RGBColor(0x08,0x20,0x38), border=RGBColor(0x1E,0x44,0x78))
txb(s, "Beyond capital, we need:", Inches(7.1), Inches(5.3),
    Inches(5.34), Inches(0.3), size=11, bold=True, color=WHITE)
txb(s, "EU government / GIS market introductions  ·  Go-to-market experience in B2G SaaS  ·  Network in Dutch & European infrastructure sector",
    Inches(7.1), Inches(5.63), Inches(5.34), Inches(0.95),
    size=10, color=LIGHT_TEXT)


# ─────────────────────────────────────────────────────────────────────────────
# SLIDE 13 — CLOSING
# ─────────────────────────────────────────────────────────────────────────────
s = add_slide(COVER_BG)

txb(s, "GeoAI  —  Seed Round 2026",
    Inches(1.5), Inches(1.4), Inches(10.33), Inches(0.4),
    size=11, color=DIM_TEXT, align=PP_ALIGN.CENTER)

logo_box2 = s.shapes.add_textbox(Inches(3.2), Inches(1.9), Inches(6.9), Inches(1.1))
lf2 = logo_box2.text_frame; lf2.word_wrap = False
lp2 = lf2.paragraphs[0]; lp2.alignment = PP_ALIGN.CENTER
r1b = lp2.add_run(); r1b.text = "Every map has a question.\n"
r1b.font.size = Pt(30); r1b.font.bold = True; r1b.font.color.rgb = WHITE

logo_box3 = s.shapes.add_textbox(Inches(1.5), Inches(2.95), Inches(10.33), Inches(1.0))
lf3 = logo_box3.text_frame; lf3.word_wrap = False
lp3 = lf3.paragraphs[0]; lp3.alignment = PP_ALIGN.CENTER
r1c = lp3.add_run(); r1c.text = "We built the system that answers it."
r1c.font.size = Pt(30); r1c.font.bold = True; r1c.font.color.rgb = ACCENT

txb(s, "On-premise AI for geospatial data. Natural language in, map out.\n"
       "Zero SQL. Zero cloud. Built for Dutch and EU government data sovereignty.",
    Inches(1.5), Inches(4.1), Inches(10.33), Inches(0.75),
    size=14, color=LIGHT_TEXT, align=PP_ALIGN.CENTER)

# Contact box
rect(s, Inches(3.0), Inches(5.05), Inches(7.33), Inches(1.7),
     fill=RGBColor(0x08,0x20,0x3A), border=RGBColor(0x1E,0x55,0x8A))
txb(s, "Adrian Akbari  ·  Founder, GeoAI",
    Inches(3.15), Inches(5.18), Inches(7.03), Inches(0.35),
    size=13, bold=True, color=WHITE, align=PP_ALIGN.CENTER)
txb(s, "adrian@gisuniverse.com",
    Inches(3.15), Inches(5.53), Inches(7.03), Inches(0.3),
    size=12, color=ACCENT, align=PP_ALIGN.CENTER)
txb(s, "Raising €350,000 seed  ·  First close target: Q4 2026",
    Inches(3.15), Inches(5.88), Inches(7.03), Inches(0.3),
    size=10, color=DIM_TEXT, align=PP_ALIGN.CENTER)


# ─────────────────────────────────────────────────────────────────────────────
# SAVE
# ─────────────────────────────────────────────────────────────────────────────
out = r"D:\web-development\Geoai\GeoAI_Pitch_Deck.pptx"
prs.save(out)
print(f"Saved: {out}  ({prs.slides.__len__()} slides)")
