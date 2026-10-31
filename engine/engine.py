"""Finance 101 v3 engine: one illustrated still per beat (Ken Burns push-in), single narrator, Anton captions.

python engine3.py <beats.py> <out dir> <models dir> <art dir> <fonts dir>
Stills are drawn here (free route). A beat may instead name an `image` file, which is how AI illustrations slot in later.
"""
import os, re, sys, json, math, subprocess, importlib
from multiprocessing import Pool
import numpy as np, soundfile as sf
from PIL import Image, ImageDraw, ImageFont, ImageFilter

MOD, OUT, MODELS, ART, FONTS = sys.argv[1:6]
sys.path.insert(0, os.path.dirname(MOD))
B = importlib.import_module(os.path.basename(MOD)[:-3])
BEATS, CAST = B.BEATS, B.CAST

W, H, FPS, SR = 1920, 1080, 30, 24000
SW, SH = 2496, 1404  # still size (1.3x) so the push-in stays sharp
K = SW / W
INK = (28, 28, 36)
GREEN, RED, AMBER, WHITE = (34, 197, 94), (239, 68, 68), (245, 158, 11), (255, 255, 255)
VOICE, SPEED = getattr(B, "VOICE", ("af_heart", 1.0))
EMOJI = "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf"
INTER = "/usr/share/fonts/opentype/inter/Inter-%s.otf"
_f = {}


def font(size, w="Bold"):
    if (size, w) not in _f:
        _f[(size, w)] = ImageFont.truetype(INTER % w if w != "Anton" else f"{FONTS}/Anton-Regular.ttf", size)
    return _f[(size, w)]


def S(v):
    return int(v * K)


# ------------------------------------------------------------------ backgrounds (flat cartoon rooms, thick outlines)
def outline_rect(d, box, fill, w=6, r=0):
    box = [S(v) for v in box]
    if r:
        d.rounded_rectangle(box, S(r), fill=fill, outline=INK, width=S(w))
    else:
        d.rectangle(box, fill=fill, outline=INK, width=S(w))


def window(d, x, y, w, h, sky=(186, 230, 253), night=False):
    outline_rect(d, [x, y, x + w, y + h], (30, 41, 82) if night else sky)
    d.line([S(x + w / 2), S(y), S(x + w / 2), S(y + h)], fill=INK, width=S(6))
    d.line([S(x), S(y + h / 2), S(x + w), S(y + h / 2)], fill=INK, width=S(6))


def plant(d, x, y):
    outline_rect(d, [x - 35, y - 60, x + 35, y], (180, 83, 9), r=8)
    for dx, dy in ((-40, -110), (0, -140), (40, -110), (-20, -95), (22, -95)):
        d.ellipse([S(x + dx - 32), S(y + dy - 32), S(x + dx + 32), S(y + dy + 32)], fill=(74, 222, 128), outline=INK, width=S(5))


def bg_room(d, wall=(254, 243, 199), floor=(217, 180, 140), night=False, win=True, extra=None):
    d.rectangle([0, 0, SW, S(760)], fill=wall)
    d.rectangle([0, S(760), SW, SH], fill=floor)
    d.line([0, S(760), SW, S(760)], fill=INK, width=S(6))
    if win:
        window(d, 1280, 150, 420, 330, night=night)
    if extra == "shelf":
        outline_rect(d, [180, 230, 620, 260], (180, 120, 70))
        for i, c in enumerate([(59, 130, 246), (239, 68, 68), (34, 197, 94), (245, 158, 11)]):
            outline_rect(d, [200 + i * 60, 120, 250 + i * 60, 230], c, w=4)
        plant(d, 1800, 760)
    elif extra == "couch":
        outline_rect(d, [1200, 560, 1800, 800], (99, 102, 241), r=40)
        outline_rect(d, [1160, 640, 1840, 860], (129, 140, 248), r=40)


def bg_hallway(d, **k):
    d.rectangle([0, 0, SW, S(780)], fill=(226, 232, 240)); d.rectangle([0, S(780), SW, SH], fill=(148, 163, 184))
    d.line([0, S(780), SW, S(780)], fill=INK, width=S(6))
    for x, c, n in ((330, (190, 18, 60), "2A"), (1290, (30, 64, 175), "2B")):
        outline_rect(d, [x, 230, x + 300, 780], c)
        d.ellipse([S(x + 245), S(500), S(x + 275), S(530)], fill=(250, 204, 21), outline=INK, width=S(4))
        d.text((S(x + 150), S(300)), n, font=font(S(48)), fill=WHITE, anchor="mm")


def bg_cafe(d, **k):
    d.rectangle([0, 0, SW, SH], fill=(254, 215, 170))
    outline_rect(d, [120, 90, 820, 420], (41, 37, 36), r=16)
    for i, t in enumerate(["LATTE 5.25", "COLD BREW 4.75", "MUFFIN 3.50"]):
        d.text((S(170), S(150 + i * 85)), t, font=font(S(46)), fill=(250, 250, 249))
    outline_rect(d, [0, 760, 1920, 1080], (120, 53, 15))
    d.rectangle([0, S(760), SW, S(800)], fill=(146, 64, 14), outline=INK, width=S(6))
    plant(d, 1780, 760)


def bg_outside(d, night=False, **k):
    sky = (30, 41, 82) if night else (186, 230, 253)
    d.rectangle([0, 0, SW, SH], fill=sky)
    if not night:
        d.ellipse([S(1650), S(80), S(1800), S(230)], fill=(253, 224, 71), outline=INK, width=S(5))
    d.rectangle([0, S(780), SW, SH], fill=(134, 239, 172)); d.line([0, S(780), SW, S(780)], fill=INK, width=S(6))
    outline_rect(d, [1150, 420, 1650, 780], (254, 243, 199))
    d.polygon([(S(1110), S(430)), (S(1400), S(240)), (S(1690), S(430))], fill=(220, 38, 38), outline=INK, width=S(6))
    outline_rect(d, [1350, 600, 1450, 780], (120, 53, 15))
    window(d, 1200, 480, 110, 90, night=night); window(d, 1500, 480, 110, 90, night=night)
    for x in (200, 520):
        outline_rect(d, [x - 20, 600, x + 20, 780], (120, 53, 15))
        d.ellipse([S(x - 110), S(420), S(x + 110), S(640)], fill=(34, 197, 94), outline=INK, width=S(6))


def bg_office(d, **k):
    bg_room(d, wall=(224, 242, 254), floor=(148, 163, 184), win=False)
    outline_rect(d, [1050, 120, 1800, 520], (125, 211, 252))
    for i, h in enumerate([200, 300, 250, 340, 180, 280]):
        outline_rect(d, [1080 + i * 120, 520 - h, 1170 + i * 120, 520], (71, 85, 105), w=4)
    outline_rect(d, [900, 760, 1920, 820], (161, 98, 7))


def bg_board(d, text="", **k):
    d.rectangle([0, 0, SW, SH], fill=(254, 249, 231))
    outline_rect(d, [260, 90, 1660, 760], (20, 83, 45), r=14)
    outline_rect(d, [240, 760, 1680, 800], (161, 98, 7))
    if text:
        sz = 120
        while d.textlength(text, font=font(S(sz), "Black")) > S(1280) and sz > 40:
            sz -= 4
        d.text((S(960), S(420)), text, font=font(S(sz), "Black"), fill=(220, 252, 231), anchor="mm")


def bg_plain(d, color=(255, 251, 235), **k):
    d.rectangle([0, 0, SW, SH], fill=color)


BGS = {"room": bg_room, "hallway": bg_hallway, "cafe": bg_cafe, "outside": bg_outside, "office": bg_office, "board": bg_board, "plain": bg_plain}


# ------------------------------------------------------------------ elements
_peeps = {}


def peep(who, face, h):
    fn = f"{OUT}/peeps/{who}_{face}_{h}.png"
    if fn not in _peeps:
        if not os.path.exists(fn):
            os.makedirs(f"{OUT}/peeps", exist_ok=True)
            o = dict(CAST[who]); o["face"] = [face]
            subprocess.run(["node", f"{ART}/peep.mjs", fn, json.dumps(o), str(h)], cwd=ART, check=True)
        _peeps[fn] = Image.open(fn).convert("RGBA")
    return _peeps[fn]


def glow(img, cx, cy, r, color):
    g = Image.new("RGBA", img.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(g)
    gd.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color + (190,))
    img.alpha_composite(g.filter(ImageFilter.GaussianBlur(r * .45)))


def el_char(img, d, e):
    h = S(e.get("h", 640) * 1.3)
    im = peep(e["who"], e.get("face", "smile"), h)
    if e.get("flip"):
        im = im.transpose(Image.FLIP_LEFT_RIGHT)
    if e.get("glow"):
        glow(img, S(e["x"]), SH - h // 2, int(h * .55), GREEN if e["glow"] == "green" else RED)
    img.alpha_composite(im, (S(e["x"]) - im.width // 2, SH - im.height + S(e.get("dy", 20))))


def el_emoji(img, d, e):
    size = S(e.get("size", 200) * 1.35)
    x, y = S(e["x"]), S(e["y"])
    if e.get("glow"):
        glow(img, x, y, int(size * .85), GREEN if e["glow"] == "green" else RED)
    t = Image.new("RGBA", (160, 160), (0, 0, 0, 0))
    ImageDraw.Draw(t).text((80, 80), e["e"], font=ImageFont.truetype(EMOJI, 109), embedded_color=True, anchor="mm")
    t = t.resize((int(size * 1.2), int(size * 1.2)), Image.LANCZOS)
    img.alpha_composite(t, (x - t.width // 2, y - t.height // 2))
    if e.get("label"):
        tag(d, x, y + int(size * .72), e["label"], GREEN if e.get("glow") == "green" else RED if e.get("glow") == "red" else INK)


def tag(d, x, y, s, color, size=64):
    f = font(S(size), "Black")
    tw = d.textlength(s, font=f)
    d.rounded_rectangle([x - tw / 2 - S(24), y - S(size * .75), x + tw / 2 + S(24), y + S(size * .75)], S(18), fill=WHITE, outline=color, width=S(7))
    d.text((x, y), s, font=f, fill=color if color != WHITE else INK, anchor="mm")


def el_tag(img, d, e):
    c = {"green": GREEN, "red": RED, "amber": AMBER}.get(e.get("color"), INK)
    if e.get("glow"):
        glow(img, S(e["x"]), S(e["y"]), S(160), c)
    tag(d, S(e["x"]), S(e["y"]), e["text"], c, e.get("size", 64))


def el_num(img, d, e):
    glow(img, S(140), S(150), S(130), GREEN)
    d.ellipse([S(60), S(70), S(220), S(230)], fill=WHITE, outline=INK, width=S(8))
    d.text((S(140), S(152)), str(e["n"]), font=font(S(110), "Anton"), fill=(21, 128, 61), anchor="mm")


def el_bigtext(img, d, e):
    c = {"green": (21, 128, 61), "red": (185, 28, 28), "amber": (180, 83, 9)}.get(e.get("color"), INK)
    d.text((S(e.get("x", 960)), S(e.get("y", 300))), e["text"], font=font(S(e.get("size", 120)), "Anton"), fill=c, anchor="mm",
           stroke_width=S(6), stroke_fill=WHITE)


def el_bars(img, d, e):
    x0, y0, x1, y1 = e.get("box", (760, 200, 1820, 740))
    outline_rect(d, [x0, y0, x1, y1], WHITE, r=20)
    vals = [v for _, v, _ in e["items"]]
    mx = max(vals) * 1.18
    n = len(vals); bw = (x1 - x0 - 80) / n
    for i, (lab, v, col) in enumerate(e["items"]):
        c = {"green": GREEN, "red": RED, "amber": AMBER, "violet": (139, 92, 246)}[col]
        bx = x0 + 40 + i * bw + bw * .15
        top = y1 - 80 - (y1 - y0 - 160) * v / mx
        outline_rect(d, [bx, top, bx + bw * .7, y1 - 80], c, w=5)
        d.text((S(bx + bw * .35), S(top - 40)), f"${v/1000:,.0f}k", font=font(S(46), "Black"), fill=INK, anchor="mm")
        d.text((S(bx + bw * .35), S(y1 - 40)), lab, font=font(S(30), "Bold"), fill=INK, anchor="mm")


def monthly(m, r, months, start=0.0):
    out, b = [start], start
    for _ in range(months):
        b = b * (1 + r / 12) + m; out.append(b)
    return out


def el_lines(img, d, e):
    x0, y0, x1, y1 = e.get("box", (700, 170, 1840, 740))
    outline_rect(d, [x0, y0, x1, y1], WHITE, r=20)
    px0, py0, px1, py1 = x0 + 50, y0 + 60, x1 - 230, y1 - 60
    series = []
    for s in e["series"]:
        if s["kind"] == "maya_stop":
            a = monthly(100, s.get("r", .07), 120); ys = a + monthly(0, s.get("r", .07), 444, a[-1])[1:]
        elif s["kind"] == "jordan":
            ys = [0.0] * 120 + monthly(100, s.get("r", .07), 444)
        elif s["kind"] == "maya_all":
            ys = monthly(100, s.get("r", .07), 564)
        elif s["kind"] == "fee":
            ys = monthly(100, .06, 564)
        series.append((ys, s))
    upto = int((e.get("age", 65) - 18) * 12)
    mx = e.get("ymax", max(max(ys[:upto + 1]) for ys, _ in series) * 1.1)
    for x in (18, 28, 38, 48, 58, 65):
        X = px0 + (x - 18) / 47 * (px1 - px0)
        d.text((S(X), S(py1 + 30)), str(x), font=font(S(30), "SemiBold"), fill=(100, 100, 110), anchor="mm")
    d.line([S(px0), S(py1), S(px1), S(py1)], fill=INK, width=S(4))
    for ys, s in series:
        c = {"green": GREEN, "red": RED, "amber": AMBER, "violet": (139, 92, 246)}[s["color"]]
        pts = [(S(px0 + i / 564 * (px1 - px0)), S(py1 - ys[i] / mx * (py1 - py0))) for i in range(0, upto + 1, 3)]
        d.line(pts, fill=c, width=S(12), joint="curve")
        lx, ly = pts[-1]
        d.text((lx + S(18), ly + S(s.get("dy", 0))), f"{s['name']} ${ys[upto]/1000:,.0f}k", font=font(S(36), "Black"), fill=c, anchor="lm")
    if e.get("label"):
        d.text((S(x0 + 40), S(y0 + 30)), e["label"], font=font(S(40), "Black"), fill=INK, anchor="lm")


def el_chart(img, d, e):
    """Generic line chart: {"t":"chart","series":[{"name":"Maya","color":"green","ys":[...]}],"xlabels":["18","28",...],"label":"...","fmt":"${k}k"}
    ys are equally spaced points; xlabels are spread evenly under the axis."""
    x0, y0, x1, y1 = e.get("box", (700, 170, 1840, 740))
    outline_rect(d, [x0, y0, x1, y1], WHITE, r=20)
    px0, py0, px1, py1 = x0 + 50, y0 + 80, x1 - 250, y1 - 60
    mx = e.get("ymax", max(max(s["ys"]) for s in e["series"]) * 1.1) or 1
    xl = e.get("xlabels", [])
    for k, lab in enumerate(xl):
        X = px0 + k / max(len(xl) - 1, 1) * (px1 - px0)
        d.text((S(X), S(py1 + 30)), str(lab), font=font(S(30), "SemiBold"), fill=(100, 100, 110), anchor="mm")
    d.line([S(px0), S(py1), S(px1), S(py1)], fill=INK, width=S(4))
    fmt = e.get("fmt", "${k}k")
    for s in e["series"]:
        ys = s["ys"]; c = {"green": GREEN, "red": RED, "amber": AMBER, "violet": (139, 92, 246)}[s["color"]]
        pts = [(S(px0 + i / max(len(ys) - 1, 1) * (px1 - px0)), S(py1 - v / mx * (py1 - py0))) for i, v in enumerate(ys)]
        d.line(pts, fill=c, width=S(12), joint="curve")
        lx, ly = pts[-1]; v = ys[-1]
        val = fmt.replace("{k}", f"{v/1000:,.0f}").replace("{v}", f"{v:,.0f}")
        d.text((lx + S(18), ly + S(s.get("dy", 0))), f"{s['name']} {val}", font=font(S(36), "Black"), fill=c, anchor="lm")
    if e.get("label"):
        d.text((S(x0 + 40), S(y0 + 35)), e["label"], font=font(S(40), "Black"), fill=INK, anchor="lm")


ELS = {k[3:]: v for k, v in globals().items() if k.startswith("el_")}


def still(i, sc):
    fn = f"{OUT}/stills/{i:03d}.png"
    if os.path.exists(fn):
        return fn
    if sc.get("image"):
        im = Image.open(sc["image"]).convert("RGBA").resize((SW, SH), Image.LANCZOS)
    else:
        im = Image.new("RGBA", (SW, SH), (255, 255, 255, 255))
        d = ImageDraw.Draw(im)
        BGS[sc.get("bg", "plain")](d, **sc.get("bgargs", {}))
        for e in sc.get("els", []):
            ELS[e["t"]](im, d, e)
            d = ImageDraw.Draw(im)
    im.convert("RGB").save(fn)
    return fn


# ------------------------------------------------------------------ pipeline
def sentences(text):
    return [p for p in re.split(r'(?<=[.?!])\s+', text.strip()) if p]


def tts():
    p = f"{OUT}/tts.json"
    if os.path.exists(p):
        return json.load(open(p))
    from kokoro_onnx import Kokoro
    k = Kokoro(f"{MODELS}/kokoro-v1.0.onnx", f"{MODELS}/voices-v1.0.bin")
    os.makedirs(f"{OUT}/wav", exist_ok=True)
    plan = []
    for i, b in enumerate(BEATS):
        parts = []
        for j, s in enumerate(sentences(b["text"])):
            say = s
            for a, r in getattr(B, "SAY", {}).items():
                say = say.replace(a, r)
            a, sr = k.create(say, voice=VOICE, speed=SPEED, lang="en-us")
            fn = f"{OUT}/wav/{i:03d}_{j:02d}.wav"; sf.write(fn, a, sr)
            parts.append([s, fn, len(a) / sr])
        plan.append(parts); print("tts", i, flush=True)
    json.dump(plan, open(p, "w"))
    return plan


def clip(args):
    """Smooth sub-pixel push-in: PIL resamples a float crop box each frame (ffmpeg zoompan rounds to whole pixels and shakes)."""
    i, img, dur = args
    fn = f"{OUT}/clips/{i:03d}.mp4"
    if os.path.exists(fn):
        return fn
    n = int(round(dur * FPS))
    src = Image.open(img).convert("RGB")
    sw, sh = src.size
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
                          "-i", "-", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", fn], stdin=subprocess.PIPE)
    for f in range(n):
        u = f / max(n - 1, 1)
        u = u * u * (3 - 2 * u)  # ease in/out
        z = 1 + 0.06 * (u if i % 2 == 0 else 1 - u)
        cw, ch = sw / z, sh / z
        x0, y0 = (sw - cw) / 2, (sh - ch) / 2
        p.stdin.write(src.resize((W, H), Image.BILINEAR, box=(x0, y0, x0 + cw, y0 + ch)).tobytes())
    p.stdin.close(); p.wait()
    return fn


def ass_time(x):
    return f"{int(x//3600)}:{int(x%3600//60):02d}:{x%60:05.2f}"


if __name__ == "__main__":
    for sub in ("stills", "clips"):
        os.makedirs(f"{OUT}/{sub}", exist_ok=True)
    if len(sys.argv) > 6 and sys.argv[6] == "stills":
        for i, b in enumerate(BEATS):
            for k, sc in enumerate(b["scenes"]):
                still(i * 10 + k, sc)
        sys.exit(0)
    plan = tts()
    GAP_S, GAP_B = .35, .7
    audio, jobs, cues, t = [], [], [], 0.0
    chapters = []
    for i, parts in enumerate(plan):
        b = BEATS[i]
        if b.get("chapter"): chapters.append((t, b["chapter"]))
        scenes = b["scenes"]
        # sentences split evenly across this beat's scenes
        per = max(1, math.ceil(len(parts) / len(scenes)))
        chunk, local, cuts = [], 0.0, [0.0]
        for j, (s, fn, dur) in enumerate(parts):
            a, _ = sf.read(fn); chunk.append(a)
            words = s.split(); groups = [words[k:k + 6] for k in range(0, len(words), 6)]
            tot = sum(len(" ".join(g)) for g in groups)
            st = t + local
            for g in groups:
                gd = dur * len(" ".join(g)) / tot
                cues.append((st, st + gd, " ".join(g))); st += gd
            g = GAP_S if j < len(parts) - 1 else GAP_B
            chunk.append(np.zeros(int(g * SR))); local += dur + g
            if (j + 1) % per == 0 and j < len(parts) - 1 and len(cuts) < len(scenes):
                cuts.append(local)
        nfr = int(math.ceil(local * FPS)); n = int(round(nfr * SR / FPS))
        c = np.concatenate(chunk); audio.append(np.concatenate([c, np.zeros(max(0, n - len(c)))])[:n])
        cuts.append(nfr / FPS)
        for k, sc in enumerate(scenes[:len(cuts) - 1]):
            jobs.append((len(jobs), still(i * 10 + k, sc), round((cuts[k + 1] - cuts[k]) * FPS) / FPS))
        t += nfr / FPS
        print("beat", i, round(t / 60, 2), flush=True)
    with Pool(4) as p:
        clips = p.map(clip, jobs)
    sf.write(f"{OUT}/voice.wav", np.concatenate(audio), SR)
    open(f"{OUT}/clips.txt", "w").write("".join(f"file '{c}'\n" for c in clips))
    ass = ["[Script Info]", "ScriptType: v4.00+", f"PlayResX: {W}", f"PlayResY: {H}", "",
           "[V4+ Styles]",
           "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding",
           "Style: Cap,Anton,120,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,0,0,0,0,100,100,1,0,1,9,3,2,60,60,70,1", "",
           "[Events]", "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text"]
    for a, b2, s in cues:
        ass.append(f"Dialogue: 0,{ass_time(a)},{ass_time(b2)},Cap,,0,0,0,,{s.upper()}")
    open(f"{OUT}/captions.ass", "w").write("\n".join(ass) + "\n")
    with open(f"{OUT}/captions.srt", "w") as f:
        ts = lambda x: f"{int(x//3600):02d}:{int(x%3600//60):02d}:{int(x%60):02d},{int(x%1*1000):03d}"
        for k, (a, b2, s) in enumerate(cues, 1):
            f.write(f"{k}\n{ts(a)} --> {ts(b2)}\n{s}\n\n")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", f"{OUT}/clips.txt", "-i", f"{OUT}/voice.wav",
                    "-vf", f"ass={OUT}/captions.ass:fontsdir={FONTS}", "-c:v", "libx264", "-preset", "medium", "-crf", "20",
                    "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-ar", "48000", "-c:a", "aac", "-b:a", "192k",
                    "-shortest", "-movflags", "+faststart", f"{OUT}/video.mp4"], check=True)
    open(f"{OUT}/chapters.txt", "w").write("".join(f"{int(a//60):02d}:{int(a%60):02d} {c}\n" for a, c in chapters))
    print("total", t / 60, "min")
