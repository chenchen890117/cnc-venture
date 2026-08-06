"""Generate Arizona-palette placeholder imagery for the CnC Venture homepage.

These are deliberately abstract: low horizons, sun discs, sand-and-dusk gradients,
fine grain. They are placeholders for authentic Arizona photography and are built
as real <img> assets so they become swappable image slots after the Wix import.
"""
import math, os, random
from PIL import Image, ImageDraw, ImageFilter

random.seed(7)
OUT = os.path.join(os.path.dirname(__file__), "img")
os.makedirs(OUT, exist_ok=True)


def hexc(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def vgrad(w, h, stops):
    """Vertical gradient. stops = [(pos 0-1, '#hex'), ...]"""
    img = Image.new("RGB", (1, h))
    px = img.load()
    stops = sorted(stops)
    for y in range(h):
        t = y / max(h - 1, 1)
        for i in range(len(stops) - 1):
            p0, c0 = stops[i]
            p1, c1 = stops[i + 1]
            if p0 <= t <= p1 or i == len(stops) - 2:
                k = 0 if p1 == p0 else (t - p0) / (p1 - p0)
                k = max(0.0, min(1.0, k))
                k = k * k * (3 - 2 * k)  # smoothstep
                a, b = hexc(c0), hexc(c1)
                px[0, y] = tuple(int(a[j] + (b[j] - a[j]) * k) for j in range(3))
                break
    return img.resize((w, h), Image.BILINEAR)


def sun(img, cx, cy, r, color, strength=1.0):
    """Soft glowing disc, composited additively-ish."""
    w, h = img.size
    layer = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(layer)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=int(255 * strength))
    layer = layer.filter(ImageFilter.GaussianBlur(r * 0.06))
    glow = Image.new("L", (w, h), 0)
    dg = ImageDraw.Draw(glow)
    dg.ellipse([cx - r * 3, cy - r * 3, cx + r * 3, cy + r * 3], fill=int(90 * strength))
    glow = glow.filter(ImageFilter.GaussianBlur(r * 1.1))
    solid = Image.new("RGB", (w, h), hexc(color))
    img = Image.composite(solid, img, glow)
    img = Image.composite(solid, img, layer)
    return img


def ridge(img, base_y, amp, color, seed, opacity=1.0, blur=0.0):
    """A minimal desert ridge line — geometric, not illustrative."""
    w, h = img.size
    rnd = random.Random(seed)
    pts = []
    n = 9
    keys = [rnd.uniform(-1, 1) for _ in range(n + 1)]
    for x in range(0, w + 1, 4):
        t = x / w * n
        i = int(t)
        k = t - i
        k = k * k * (3 - 2 * k)
        v = keys[i] + (keys[min(i + 1, n)] - keys[i]) * k
        pts.append((x, base_y + v * amp))
    pts += [(w, h), (0, h)]
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).polygon(pts, fill=int(255 * opacity))
    if blur:
        mask = mask.filter(ImageFilter.GaussianBlur(blur))
    solid = Image.new("RGB", (w, h), hexc(color))
    return Image.composite(solid, img, mask)


def grain(img, amount=6):
    w, h = img.size
    noise = Image.effect_noise((w, h), 28).convert("L")
    noise = noise.filter(ImageFilter.GaussianBlur(0.4))
    n = noise.point(lambda v: 128 + (v - 128) * amount / 100)
    return Image.blend(img, Image.merge("RGB", (n, n, n)), 0.055)


def save(img, name, q=74):
    img = grain(img)
    p = os.path.join(OUT, name)
    img.save(p, "JPEG", quality=q, optimize=True, progressive=True)
    return os.path.getsize(p)


# ---------------------------------------------------------------- compositions
DUSK = ["#02383D", "#0B4A4C", "#3E6B60", "#A9825C", "#D9773F", "#EFC49A"]

def scene_dusk(w, h):
    """Deep teal sky falling into an Arizona sunset horizon."""
    img = vgrad(w, h, [(0, "#02272B"), (0.34, "#0A4448"), (0.6, "#4B6E5E"),
                       (0.78, "#B8834F"), (0.9, "#D9773F"), (1, "#F0C79C")])
    img = sun(img, int(w * 0.66), int(h * 0.80), int(h * 0.085), "#F7DCB4", 0.55)
    img = ridge(img, int(h * 0.845), h * 0.022, "#3C5A52", 11, 0.55, 1.2)
    img = ridge(img, int(h * 0.905), h * 0.016, "#123A3B", 5, 0.85, 0.6)
    img = ridge(img, int(h * 0.965), h * 0.010, "#02282B", 3, 1.0)
    return img


def scene_sunset(w, h):
    """Full sunset — warmer, lower horizon, for the closing CTA."""
    img = vgrad(w, h, [(0, "#123C43"), (0.22, "#3E5F5B"), (0.44, "#A9754D"),
                       (0.62, "#D9773F"), (0.78, "#E6A06A"), (1, "#F6DFC2")])
    img = sun(img, int(w * 0.80), int(h * 0.60), int(h * 0.105), "#FBEBD2", 0.62)
    img = ridge(img, int(h * 0.78), h * 0.030, "#8A6249", 21, 0.45, 2.0)
    img = ridge(img, int(h * 0.88), h * 0.020, "#3E4A44", 9, 0.8, 0.8)
    img = ridge(img, int(h * 0.955), h * 0.012, "#0E2C2E", 4, 1.0)
    return img


def scene_field(w, h, stops, sun_at=None, sun_col="#F3D8B2", ridges=None):
    img = vgrad(w, h, stops)
    if sun_at:
        img = sun(img, int(w * sun_at[0]), int(h * sun_at[1]), int(h * sun_at[2]), sun_col, 0.5)
    for (y, a, c, s, o) in (ridges or []):
        img = ridge(img, int(h * y), h * a, c, s, o)
    return img


PALETTES = {
    # name: (stops, sun, ridges)
    "sand":   ([(0, "#EBDBC0"), (0.5, "#D7BE95"), (1, "#AC8D62")], (0.70, 0.28, 0.11), [(0.80, .018, "#9C7C55", 31, .55), (0.90, .012, "#7A5F3E", 32, .8)]),
    "teal":   ([(0, "#02383D"), (0.6, "#0C4F50"), (1, "#2C6A62")], (0.28, 0.34, 0.09), [(0.88, .012, "#012629", 33, .9)]),
    "clay":   ([(0, "#E8B98F"), (0.5, "#D9773F"), (1, "#A9502C")], (0.30, 0.26, 0.11), [(0.84, .016, "#8C4526", 37, .75)]),
    "stone":  ([(0, "#DAD5C9"), (0.5, "#B8B1A0"), (1, "#847D6C")], (0.30, 0.30, 0.09), [(0.78, .020, "#77705F", 41, .5), (0.90, .012, "#575142", 42, .85)]),
    "dusk":   ([(0, "#0C3236"), (0.45, "#3F5F5A"), (0.8, "#B07A4F"), (1, "#E4A574")], (0.62, 0.66, 0.08), [(0.9, .012, "#0B2E31", 43, .9)]),
    "beige":  ([(0, "#F4E9D6"), (0.55, "#E2CDAB"), (1, "#C0A377")], (0.62, 0.24, 0.10), [(0.82, .016, "#AD8F63", 47, .5), (0.92, .010, "#8B7048", 48, .8)]),
    "pine":   ([(0, "#14413F"), (0.5, "#2E6154"), (1, "#5C8060")], (0.75, 0.30, 0.07), [(0.86, .014, "#0F3634", 53, .85)]),
    "ember":  ([(0, "#3A2A28"), (0.42, "#8A4A32"), (0.8, "#D9773F"), (1, "#EFB483")], (0.34, 0.60, 0.09), [(0.9, .012, "#2E1F1E", 59, .9)]),
}


def make(name, w, h, pal):
    stops, s, r = PALETTES[pal]
    ridges = [(y, a, c, sd, o) for (y, a, c, sd, o) in r]
    return scene_field(w, h, stops, s, "#F7E3C4", ridges)


JOBS = [
    ("hero.jpg",        1920, 1080, "dusk-scene"),
    ("cta-sunset.jpg",  1920,  980, "sunset-scene"),
    ("arizona.jpg",     1100, 1400, "sand"),
    ("ind-restaurant.jpg", 1000, 750, "clay"),
    ("ind-brand.jpg",      1000, 750, "beige"),
    ("ind-startup.jpg",    1000, 750, "teal"),
    ("ind-tech.jpg",       1000, 750, "dusk"),
    ("ind-manufacturing.jpg", 1000, 750, "stone"),
    ("ind-retail.jpg",     1000, 750, "ember"),
    ("story-1.jpg", 1000, 700, "clay"),
    ("story-2.jpg", 1000, 700, "pine"),
    ("story-3.jpg", 1000, 700, "sand"),
    ("insight-lead.jpg", 1400, 900, "dusk"),
    ("insight-1.jpg", 760, 520, "stone"),
    ("insight-2.jpg", 760, 520, "clay"),
    ("insight-3.jpg", 760, 520, "teal"),
    ("city-phoenix.jpg",   720, 940, "ember"),
    ("city-scottsdale.jpg", 720, 940, "sand"),
    ("city-tempe.jpg",     720, 940, "pine"),
    ("city-mesa.jpg",      720, 940, "stone"),
    ("city-gilbert.jpg",   720, 940, "beige"),
]

total = 0
for name, w, h, pal in JOBS:
    if pal == "dusk-scene":
        img = scene_dusk(w, h)
    elif pal == "sunset-scene":
        img = scene_sunset(w, h)
    else:
        img = make(name, w, h, pal)
    sz = save(img, name)
    total += sz
    print(f"{name:26s} {w}x{h:<5d} {sz/1024:7.1f} KB")
print(f"{'TOTAL':26s} {'':11s} {total/1024:7.1f} KB  (base64 ~{total*1.34/1024/1024:.2f} MB)")
