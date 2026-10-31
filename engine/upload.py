"""Upload a rendered episode to YouTube with its thumbnail. Standard library only.

python upload.py <episode dir> <build dir> [--publish-at 2026-11-02T16:00:00Z] [--dry-run]
Needs env: YT_CLIENT_ID, YT_CLIENT_SECRET, YT_REFRESH_TOKEN (scope youtube.upload).
Videos go up private. With --publish-at they are scheduled to go public at that time
(the same scheduling the clipper project uses)."""
import os, sys, json, urllib.request, urllib.parse, urllib.error

EP, BUILD = sys.argv[1:3]
args = sys.argv[3:]
publish_at = args[args.index("--publish-at") + 1] if "--publish-at" in args else None
dry = "--dry-run" in args
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def description():
    d = json.load(open(f"{EP}/details.json"))
    tpl = open(f"{ROOT}/templates/description.txt").read()
    chapters = open(f"{BUILD}/chapters.txt").read().strip()
    sources = "\n".join(d.get("sources", []))
    return tpl.format(summary=d["summary"].strip(), chapters=chapters, sources=sources).strip() + "\n", d


def req(url, data=None, headers=None, method=None):
    r = urllib.request.Request(url, data=data, headers=headers or {}, method=method)
    try:
        with urllib.request.urlopen(r, timeout=600) as resp:
            return resp.status, dict(resp.headers), resp.read()
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers), e.read()


def token():
    body = urllib.parse.urlencode(dict(client_id=os.environ["YT_CLIENT_ID"], client_secret=os.environ["YT_CLIENT_SECRET"],
                                       refresh_token=os.environ["YT_REFRESH_TOKEN"], grant_type="refresh_token")).encode()
    st, _, b = req("https://oauth2.googleapis.com/token", body, {"Content-Type": "application/x-www-form-urlencoded"})
    if st != 200:
        sys.exit(f"token refresh failed ({st}): {b[:300]!r}. If it says invalid_grant, the refresh token expired or was revoked: "
                 "make a new one (and make sure the OAuth consent screen is 'In production', not 'Testing').")
    return json.loads(b)["access_token"]


desc, d = description()
if len(desc) > 5000 or len(d["title"]) > 100:
    sys.exit("title or description too long")
status = {"privacyStatus": "private", "selfDeclaredMadeForKids": False, "containsSyntheticMedia": True}
if publish_at:
    status["publishAt"] = publish_at
meta = {"snippet": {"title": d["title"], "description": desc, "tags": d.get("tags", []), "categoryId": "27",
                    "defaultLanguage": "en", "defaultAudioLanguage": "en"}, "status": status}
open(f"{BUILD}/description.txt", "w").write(desc)
if dry:
    print(json.dumps(meta, indent=1, ensure_ascii=False)); sys.exit(0)

tok = token(); auth = {"Authorization": f"Bearer {tok}"}
video = f"{BUILD}/video.mp4"; size = os.path.getsize(video)
st, h, b = req("https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status",
               json.dumps(meta).encode(), {**auth, "Content-Type": "application/json; charset=UTF-8",
                                           "X-Upload-Content-Type": "video/mp4", "X-Upload-Content-Length": str(size)}, "POST")
loc = {k.lower(): v for k, v in h.items()}.get("location")
if st != 200 or not loc:
    sys.exit(f"could not start upload ({st}): {b[:500]!r}")
CH = 16 * 1024 * 1024; sent = 0; vid = None
with open(video, "rb") as f:
    while sent < size:
        chunk = f.read(CH)
        st, h, b = req(loc, chunk, {**auth, "Content-Length": str(len(chunk)),
                                    "Content-Range": f"bytes {sent}-{sent + len(chunk) - 1}/{size}"}, "PUT")
        if st in (200, 201):
            vid = json.loads(b)["id"]; break
        if st != 308:
            sys.exit(f"upload failed at byte {sent} ({st}): {b[:500]!r}")
        rng = {k.lower(): v for k, v in h.items()}.get("range")
        sent = int(rng.split("-")[1]) + 1 if rng else 0
        f.seek(sent); print(f"uploaded {sent * 100 // size}%", flush=True)
print("video id", vid, flush=True)
thumb = f"{BUILD}/thumbnail.png"
st, _, b = req(f"https://www.googleapis.com/upload/youtube/v3/thumbnails/set?videoId={vid}", open(thumb, "rb").read(),
               {**auth, "Content-Type": "image/png"}, "POST")
print("thumbnail", "ok" if st == 200 else f"failed ({st}): {b[:300]!r} (custom thumbnails need a phone-verified channel)")
json.dump({"video_id": vid, "url": f"https://youtu.be/{vid}", "publish_at": publish_at}, open(f"{EP}/uploaded.json", "w"), indent=1)
print(f"https://youtu.be/{vid}")
