"""Thumbnail in the episode-1 style. Reads the "thumbnail" block of episodes/<ep>/details.json:
{"line1": "START", "line2": "AT 18", "char": "maya", "face": "smileLOL", "props": ["🫙", "🪙"]}
python thumb.py <episode dir> <out dir> <engine dir> <fonts dir>"""
import os, sys, json, subprocess, importlib
from PIL import Image, ImageDraw, ImageFont, ImageFilter
EP, OUT, ENG, FONTS = sys.argv[1:5]
EMO = "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf"
t = json.load(open(f"{EP}/details.json"))["thumbnail"]
sys.path.insert(0, EP); CAST = importlib.import_module("beats").CAST
W, H = 1280, 720
im = Image.new("RGBA", (W, H), (254, 243, 199, 255))
d = ImageDraw.Draw(im)
d.rectangle([0, 520, W, H], fill=(217, 180, 140)); d.line([0, 520, W, 520], fill=(28, 28, 36), width=5)
glow_c = (239, 68, 68) if t.get("glow") == "red" else (34, 197, 94)
g = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ImageDraw.Draw(g).ellipse([780, 200, 1240, 660], fill=glow_c + (200,))
im.alpha_composite(g.filter(ImageFilter.GaussianBlur(100)))
def emoji(ch, size, xy):
    e = Image.new("RGBA", (160, 160)); ImageDraw.Draw(e).text((80, 80), ch, font=ImageFont.truetype(EMO, 109), embedded_color=True, anchor="mm")
    im.alpha_composite(e.resize((size, size), Image.LANCZOS), xy)
props = t.get("props", [])
if props: emoji(props[0], 340, (840, 260))
for p, (x, y, s) in zip(props[1:] * 3, ((1150, 220, 110), (1200, 360, 80), (860, 210, 90))):
    emoji(p, s, (x, y))
pf = f"{OUT}/thumb_char.png"
o = dict(CAST[t.get("char", "maya")]); o["face"] = [t.get("face", "smileLOL")]
subprocess.run(["node", f"{ENG}/peep.mjs", pf, json.dumps(o), "1081"], cwd=ENG, check=True)
m = Image.open(pf).convert("RGBA").resize((640, 640), Image.LANCZOS)
im.alpha_composite(m, (-40, H - 600))
d = ImageDraw.Draw(im)
for size in range(150, 80, -5):
    f = ImageFont.truetype(f"{FONTS}/Anton-Regular.ttf", size)
    if max(d.textlength(t["line1"], font=f), d.textlength(t.get("line2", ""), font=f)) <= W - 500: break
d.text((470, 40), t["line1"], font=f, fill="white", stroke_width=12, stroke_fill="black")
d.text((470, 40 + int(size * 1.13)), t.get("line2", ""), font=f, fill=glow_c, stroke_width=12, stroke_fill="black")
im.convert("RGB").save(f"{OUT}/thumbnail.png")
print("thumbnail ok")
