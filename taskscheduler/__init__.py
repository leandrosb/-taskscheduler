from flask import Flask
from .restplus import api


def create_app(test_config=None):
    app = Flask(__name__)
    api.init_app(app)

    return app
