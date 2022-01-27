from flask import Flask, Blueprint
from flask_cors import CORS

from back.application import api
from back.application.morse.viewer import morse_ns


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})
    blueprint = Blueprint("api", __name__)
    api.init_app(blueprint)
    api.add_namespace(morse_ns, path="/morse")
    app.register_blueprint(blueprint)
    return app
