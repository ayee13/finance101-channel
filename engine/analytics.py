"""Pull YouTube Analytics for every uploaded episode into a markdown report. Standard library only.

python analytics.py <repo root> <out.md>
Needs env: YT_CLIENT_ID, YT_CLIENT_SECRET, YT_REFRESH_TOKEN, with the refresh token granted the scopes
youtube.upload, youtube.readonly and yt-analytics.readonly. Analytics lag about 2 days behind."""
import os, sys, json, glob, datetime, urllib.request, urllib.parse, urllib.error

ROOT, OUT = sys.argv[1:3]
API = "https://youtubeanalytics.googleapis.com/v2/reports"


def req(url, data=None, headers=None):
    r = urllib.request.Request(url, data=data, headers=headers or {})
    try:
        with urllib.request.urlopen(r, timeout=120) as resp:
            return resp.status, json.loads(resp.read())
    except urllib.error.HTTPError as e:
        return e.code, e.read()[:400]


body = urllib.parse.urlencode(dict(client_id=os.environ["YT_CLIENT_ID"], client_secret=os.environ["YT_CLIENT_SECRET"],
                                   refresh_token=os.environ["YT_REFRESH_TOKEN"], grant_type="refresh_token")).encode()
st, tok = req("https://oauth2.googleapis.com/token", body, {"Content-Type": "application/x-www-form-urlencoded"})
if st != 200:
    sys.exit(f"token refresh failed ({st}): {tok!r}")
if "yt-analytics.readonly" not in tok.get("scope", ""):
    sys.exit("the refresh token has no yt-analytics.readonly scope: redo setup Step 3 with the analytics scopes")
AUTH = {"Authorization": f"Bearer {tok['access_token']}"}


def report(**q):
    q = {"ids": "channel==MINE", "startDate": "2026-10-01", "endDate": datetime.date.today().isoformat(), **q}
    st, b = req(f"{API}?{urllib.parse.urlencode(q)}", headers=AUTH)
    if st != 200:
        return None, f"error {st}: {b!r}"
    cols = [c["name"] for c in b.get("columnHeaders", [])]
    return [dict(zip(cols, r)) for r in b.get("rows", [])], None


eps = []
for f in sorted(glob.glob(f"{ROOT}/episodes/ep*/uploaded.json")):
    u = json.load(open(f)); d = json.load(open(os.path.join(os.path.dirname(f), "details.json")))
    if u.get("video_id"):
        eps.append((os.path.basename(os.path.dirname(f)), u["video_id"], d["title"], d.get("thumbnail", {})))
lines = [f"# Finance 101 analytics, {datetime.date.today().isoformat()}", "",
         "Data lags about 2 days. Episodes younger than 3 days have little data yet.", ""]
ids = ",".join(v for _, v, _, _ in eps)
rows, err = report(dimensions="video", filters=f"video=={ids}", sort="-views",
                   metrics="views,estimatedMinutesWatched,averageViewDuration,averageViewPercentage,likes,comments,subscribersGained")
lines += ["## Per video", ""]
if err:
    lines.append(err)
else:
    by = {r["video"]: r for r in rows}
    lines += ["| ep | title | thumbnail | views | avg watched | avg % | likes | subs |", "|---|---|---|---|---|---|---|---|"]
    for ep, vid, title, th in eps:
        r = by.get(vid, {})
        avd = r.get("averageViewDuration", 0)
        lines.append(f"| {ep} | {title} | {th.get('line1', '')} / {th.get('line2', '')} | {r.get('views', 0)} | "
                     f"{int(avd)//60}:{int(avd)%60:02d} | {r.get('averageViewPercentage', 0):.0f}% | {r.get('likes', 0)} | {r.get('subscribersGained', 0)} |")
lines += ["", "## Retention (share of viewers still watching)", ""]
for ep, vid, title, _ in eps:
    rows, err = report(dimensions="elapsedVideoTimeRatio", filters=f"video=={vid}", metrics="audienceWatchRatio,relativeRetentionPerformance")
    if err or not rows:
        lines.append(f"- {ep}: {err or 'no data yet'}"); continue
    pick = {k: min(rows, key=lambda r: abs(r["elapsedVideoTimeRatio"] - k)) for k in (.03, .1, .25, .5, .75, .95)}
    s = ", ".join(f"{int(k*100)}%: {r['audienceWatchRatio']*100:.0f}%" for k, r in pick.items())
    rel = sum(r["relativeRetentionPerformance"] for r in rows) / len(rows)
    lines.append(f"- {ep}: {s} (vs similar videos: {rel:.2f}, 0.5 = average)")
lines += ["", "## Where viewers come from (all videos)", ""]
rows, err = report(dimensions="insightTrafficSourceType", metrics="views", sort="-views")
lines += [err] if err else [f"- {r['insightTrafficSourceType']}: {r['views']}" for r in rows]
lines += ["", "## YouTube search terms that found the channel", ""]
rows, err = report(dimensions="insightTrafficSourceDetail", filters="insightTrafficSourceType==YT_SEARCH",
                   metrics="views", sort="-views", maxResults="25")
lines += [err] if err else ([f"- {r['insightTrafficSourceDetail']}: {r['views']}" for r in rows] or ["- none yet"])
open(OUT, "w").write("\n".join(lines) + "\n")
print(open(OUT).read())
