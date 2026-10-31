# Finance 101: scheduled episode run

This repo makes and uploads one Finance 101 YouTube episode per run. The channel is for late teens and early 20s
starting out. It is financial **education**, never personalized advice. Everything must stay free: no paid APIs,
no paid voices, no paid images.

A scheduled task runs this on Monday, Wednesday and Friday. Each run starts in a fresh container, so do every step.

## The run, step by step

1. `./setup.sh` (installs ffmpeg/fonts if missing, Python venv, npm packages, Kokoro voice models; about 3 minutes).
2. Open `topics.md`. Take the first line with `- [ ]`. The next episode number is the highest `episodes/epNNN` + 1.
3. Read `episodes/ep001/beats.py` and `episodes/ep001/details.json` fully. They are the style reference.
   Also skim the two most recent episodes so the new one does not repeat their cold open, characters' situation or jokes.
4. Research the facts you will state. Use web search for anything that changes (rates, limits, tax brackets,
   contribution limits) and note the source and date. Do every calculation in Python and use those exact numbers.
5. Write `episodes/epNNN/beats.py` and `episodes/epNNN/details.json` (format below).
6. `./make_episode.sh epNNN`. It prints the duration in seconds. It must be 900 to 1200 (15 to 20 minutes).
   If short, add a real section (an honesty check, a worked example, a common mistake) and re-render
   (delete `build/epNNN/tts.json` and `build/epNNN/stills`, `build/epNNN/clips` first so they rebuild).
7. Look at `build/epNNN/sheet.jpg` (every scene) and `build/epNNN/thumbnail.png`. Fix any label that overlaps
   another label, a character's head, or runs off the edge; delete only the affected still and its clip, then re-run.
8. Upload: `set -a; . ./.yt_env 2>/dev/null; set +a; .venv/bin/python -I engine/upload.py episodes/epNNN build/epNNN`
   The credentials come from the environment (`YT_CLIENT_ID`, `YT_CLIENT_SECRET`, `YT_REFRESH_TOKEN`).
   If they are missing, skip the upload, say so in the summary, and still commit.
   If `UPLOAD_PUBLISH_HOUR_UTC` is set and the Google project has passed YouTube's audit, add
   `--publish-at <today>T<hour>:00:00Z` to schedule it public; otherwise it uploads private.
9. Tick the topic in `topics.md` as `- [x] epNNN ...`, then `git add episodes topics.md && git commit` and push to the
   default branch. Never commit `build/`, `models/`, `.venv/` or any credential.
10. Finish with a short summary: title, duration, YouTube link (or why there is none), and anything Alan should check.

If any step fails twice, stop, commit what you have, and report the failure plainly. Never invent a link or a result.

## Style (copy episode 1)

- Length: about 2,000 to 2,300 narrated words, 40 to 50 beats, 15 to 20 minutes at `VOICE = ("af_heart", 0.75)`.
- Cold open: two fictional composite characters (reuse Maya and Jordan or add new ones to `CAST`) in a concrete
  everyday scene. A surprising contrast or question in the first 30 seconds. Then the disclaimer in one beat:
  "This channel is education, not financial advice..." within the first 2 minutes.
- Body: a numbered list of 5 to 9 moves or ideas, each a chapter. Use the `num(n)` element on the first scene of each.
- Tone: calm teacher who is a little funny. Dry humor, short sentences, talks to "you". One or two pop culture
  nods per section (games, streaming, memes), never a real person's likeness or a copyrighted character drawn on screen.
- At least one "honesty check" section: what if returns are lower, fees, inflation, or the catch nobody mentions.
- End: back to the characters, a one-line takeaway, and a tease of the next topic on the TV end card.
- Every 5 to 10 seconds of narration a new scene: give long beats 2 or 3 `scenes`.
- Green glow = good outcome, red glow = cost or mistake. Labels in CAPS, short (max ~22 characters per tag).
- Never recommend a specific stock, coin, fund ticker or company. Explain categories ("a total market index fund").
- State assumptions on screen and in the description (e.g. "assumed 7% yearly return, not a prediction").

## beats.py format

Copy the header of `episodes/ep001/beats.py` (VOICE, SAY, CAST, helper functions). Each beat:

```python
dict(chapter="2. Count the doublings",          # optional: starts a YouTube chapter at this beat
     text="Narration. Sentences end with . ! or ?",
     scenes=[R([num(2), ch("maya", "smile", 500), em("💸", 1300, 460, 220, "red", "LABEL")]),
             dict(bg="board", bgargs=dict(text="72 / 7 = ~10 YEARS"), els=[])])
```

Coordinates are on a 1920x1080 canvas. The first beat must have a chapter (it becomes 00:00) and there must be at
least 3 chapters. Backgrounds: room (bgargs extra="couch"|"shelf", night, win), hallway, cafe, outside, office,
board (bgargs text=...), plain. Elements: `ch(who, face, x, h=640, flip=True, glow=)`,
`em(emoji, x, y, size, glow, label)`, `tagel(text, x, y, color, glow, size)`, `big(text, x, y, color, size)`,
`num(n)`, `dict(t="bars", items=[(label, value, color)])`, and the generic line chart
`dict(t="chart", series=[{"name":..., "color":"green", "ys":[...]}], xlabels=[...], label="...")`.
Faces (Open Peeps): smile, smileBig, smileLOL, calm, serious, driven, cheeky, awe, concerned, concernedFear, fear,
suspicious, tired, eyesClosed, rage, lovingGrin1, explaining, solemn.
Leave space: two tags side by side need about 700 px between their centres; keep tags 40 px clear of heads.
`SAY` maps text to how it should be spoken (e.g. "$" removed because numbers are read with "dollars" in the text).

## details.json format

```json
{"title": "under 70 characters, curiosity + a number",
 "summary": "2 to 4 sentences: the hook, what the viewer learns, the assumptions. Ends with 'X and Y are fictional composites.'",
 "sources": ["Source name, date: URL"],
 "tags": ["6 to 10 search phrases"],
 "thumbnail": {"line1": "2-3 WORDS", "line2": "2-3 WORDS", "char": "maya", "face": "smileLOL", "props": ["emoji", "emoji"], "glow": "green"},
 "next": "the next topic, for the end card"}
```

The description is built from `templates/description.txt` (summary, disclaimer, chapters from the render, sources,
AI disclosure). Do not change the template wording during a run.
