"""Contact sheet of every still, for a quick overlap check. python sheet.py <stills dir> <out.jpg>"""
import os, sys
from PIL import Image
fs = sorted(f for f in os.listdir(sys.argv[1]) if f.endswith(".png"))
cols, w, h = 6, 416, 234
rows = (len(fs) + cols - 1) // cols
c = Image.new("RGB", (cols * w, rows * h), "white")
for k, f in enumerate(fs):
    c.paste(Image.open(os.path.join(sys.argv[1], f)).convert("RGB").resize((w - 4, h - 4)), ((k % cols) * w, (k // cols) * h))
c.save(sys.argv[2], quality=80)
