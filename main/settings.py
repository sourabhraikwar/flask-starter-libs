import os
from flask import Flask


def create_app(config=os.environ.get('', 'main.config.DevelopmentConfig')):
    app = Flask(__name__)
    app.config.from_object(config)
    app.config['DEBUG'] = True
    return app