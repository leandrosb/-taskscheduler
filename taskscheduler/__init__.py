from flask import Flask
from .restplus import api


def create_app():
    app = Flask("taskscheduler")
    api.init_app(app)

    return app
