import os

from flask import Flask

from main.core.routes import core_bp
from main.extensions import db, migrate, redis


def create_app(config=os.environ.get("", "main.config.DevelopmentConfig")):
    app = Flask(__name__)
    app.config.from_object(config)

    # app debug enabled by default
    app.config["DEBUG"] = True

    # initialized database
    db.init_app(app)
    migrate.init_app(app=app, db=db)
    redis.init_app(app)

    # blueprint registration
    app.register_blueprint(core_bp)

    return app
