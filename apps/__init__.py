import os

from flask import Flask
from flask_migrate import Migrate

from apps.api.urls import api_bp
from apps.base.models import db


def create_app(env="development"):
    print("(((****************************")
    settings = os.path.abspath("./settings/{}.py".format(env))

    app = Flask(__name__, template_folder="../templates")
    app.config.from_pyfile(settings)

    # Register blueprint
    app.register_blueprint(api_bp, url_prefix="/api")

    db.init_app(app)
    Migrate(app, db)

    return app
