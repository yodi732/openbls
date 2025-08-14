# Minimal Wiki — Render Ready

A clean starter that **just runs** on Render.

## Deploy
1. Push this folder to GitHub.
2. On Render, create a new **Web Service** from the repo.
3. Build: `pip install -r requirements.txt`
4. Start: `python app.py`
5. (Optional) Set env vars in render.yaml.

## Structure
- `app.py`: main entrypoint, auto-attaches routes
- `route/`: blueprints
- `route/tool/func.py`: small helpers to avoid import errors
- `data/`: place for DB/files if needed

Visit `/`, `/healthz`, `/wiki/Home`, `/api/ping` after deploy.
