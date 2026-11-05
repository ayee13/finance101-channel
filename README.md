# Finance 101

Pipeline for the Finance 101 YouTube channel: AI narration (Kokoro), Open Peeps characters, burned-in captions,
uploaded through the YouTube Data API. A scheduled Claude session makes one episode every Monday, Wednesday and Friday.

- `CLAUDE.md`: the run procedure and the style guide each scheduled run follows
- `topics.md`: the topic queue (edit freely)
- `episodes/epNNN/`: each episode's script (`beats.py`) and metadata (`details.json`)
- `engine/`: renderer, thumbnail, contact sheet and uploader
- `templates/description.txt`: the YouTube description layout

Manual run: `./setup.sh && ./make_episode.sh ep002 && .venv/bin/python -I engine/upload.py episodes/ep002 build/ep002`

Analytics report: `.venv/bin/python -I engine/analytics.py . analytics/report.md` (needs the analytics scopes on the token). Each run reviews it weekly and keeps `learnings.md` up to date.
