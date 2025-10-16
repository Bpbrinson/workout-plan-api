from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    # Basic Config
    app.config["VERSION"] = os.getenv("VERSION", "0.1.5")
    app.config["GIT_SHA"] = os.getenv("GIT_SHA", "local-dev")

    # Register Blueprints
    from .routes.health import bp as health_bp
    app.register_blueprint(health_bp)

    from .db import SessionLocal
    from flask import g

    @app.before_request
    def open_session():
        print("opened")
        g.db = SessionLocal()

    @app.teardown_request
    def clse_session(exc):
        db = getattr(g, "db", None)
        if not db:
            return
        if exc is not None:
            db.rollback()
            print("closed")
        db.close()

    return app
