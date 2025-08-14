# route/__init__.py
# Minimal route package with add_route(app) so the main app can attach real routes.
from .wiki import bp as wiki_bp
from .api import bp as api_bp

def add_route(app):
    app.register_blueprint(wiki_bp)
    app.register_blueprint(api_bp)
