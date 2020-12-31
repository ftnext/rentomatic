from flask import Flask

from rentomatic.flask_settings import DevConfig
from rentomatic.rest import room


def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(room.blueprint)
    return app
