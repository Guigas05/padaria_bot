from flask import Flask

from .extensions import mongo
from .padariaBot import padariaBot

def create_app(config_object='settings'):
    app = Flask(__name__)

    app.config.from_object(config_object)

    mongo.init_app(app)

    app.register_blueprint(padariaBot)

    return app

