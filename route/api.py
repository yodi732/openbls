# route/api.py
from flask import Blueprint, jsonify, request

bp = Blueprint("api", __name__)

@bp.get("/api/ping")
def ping():
    return jsonify({"pong": True, "ip": request.remote_addr})
