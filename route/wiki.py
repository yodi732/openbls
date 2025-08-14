# route/wiki.py
from flask import Blueprint, render_template_string

bp = Blueprint("wiki", __name__)

@bp.get("/wiki/<title>")
def wiki_page(title):
    html = '''
    <!doctype html>
    <meta charset="utf-8"/>
    <title>{{ title }} - Minimal Wiki</title>
    <style>body{font-family:system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;padding:32px;max-width:900px;margin:0 auto}</style>
    <h1>{{ title }}</h1>
    <p>This is a placeholder wiki page. Replace with your renderer/storage.</p>
    <p><a href="/">← Home</a></p>
    '''
    return render_template_string(html, title=title)
