# Minimal Render-ready Wiki Skeleton (Flask)
# goal: start successfully on Render, show a home page, expose /healthz, and have room to grow.
import os
import logging
from flask import Flask, request, jsonify, render_template_string
try:
    from werkzeug.middleware.proxy_fix import ProxyFix
except Exception:
    ProxyFix = None

HOST = os.getenv("NAMU_HOST", "0.0.0.0")
PORT = int(os.getenv("PORT") or os.getenv("NAMU_PORT") or "5000")
DEBUG = os.getenv("NAMU_DEBUG", "0") == "1"

app = Flask(__name__, static_folder="static", template_folder="templates")
if ProxyFix:
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1)

# Try to attach routes from the bundled 'route' package.
def attach_routes() -> bool:
    try:
        from route import add_route
        add_route(app)
        return True
    except Exception as e:
        logging.warning(f"Route attach failed or not present: {e}")
        return False

attached = attach_routes()

@app.get("/")
def home():
    html = '''
    <!doctype html>
    <meta charset="utf-8"/>
    <title>Render Minimal Wiki</title>
    <style>
      body{font-family:system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;
           padding:40px;line-height:1.6;max-width:900px;margin:0 auto}
      .pill{display:inline-block;padding:6px 10px;border-radius:999px;background:#eef;border:1px solid #cdd}
      .warn{display:inline-block;padding:6px 10px;border-radius:999px;background:#ffe;
            border:1px solid #ddc;margin-left:8px}
      a{color:#06c;text-decoration:none} a:hover{text-decoration:underline}
      code{background:#f6f6f6;padding:2px 6px;border-radius:6px}
      .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px;margin-top:18px}
      .card{border:1px solid #eee;border-radius:14px;padding:14px;box-shadow:0 1px 4px rgba(0,0,0,.04)}
    </style>
    <h1>Render Minimal Wiki</h1>
    <p><span class="pill">Server online</span>
       {% if not attached %}<span class="warn">basic routes only (fallback)</span>{% endif %}
    </p>
    <div class="grid">
      <div class="card">
        <h3>Health</h3>
        <p><a href="/healthz">/healthz</a></p>
      </div>
      <div class="card">
        <h3>Sample Page</h3>
        <p><a href="/wiki/Home">/wiki/Home</a></p>
      </div>
      <div class="card">
        <h3>API</h3>
        <p><a href="/api/ping">/api/ping</a></p>
      </div>
    </div>
    <h3>Next Steps</h3>
    <ol>
      <li>Add/modify routes in <code>route/</code>.</li>
      <li>Connect SQLite/other DB as needed (data/ is provided).</li>
      <li>Deploy to Render with <code>render.yaml</code>.</li>
    </ol>
    '''
    return render_template_string(html, attached=attached)

@app.get("/healthz")
def healthz():
    return {"status": "ok", "attached": attached}

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=DEBUG)
