from flask import Blueprint, jsonify, current_app, g
from sqlalchemy import text

bp = Blueprint("health", __name__)

@bp.get("/healthz")
def healthz():
    return jsonify({"status": "ok"}), 200

@bp.get("/version")
def version():
    return jsonify({
        "version": current_app.config.get("VERSION"), 
        "git_sha": current_app.config.get("GIT_SHA")
    }), 200

@bp.get("/db-check")
def db_check():
    g.db.execute(text("SELECT 1"))
    return {"db": "ok"}, 200
