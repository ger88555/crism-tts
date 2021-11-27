import os

from flask import Flask
from flask.helpers import make_response
from flask.json import jsonify
from werkzeug.exceptions import HTTPException

from app.exceptions.UnreadableWebsiteError import UnreadableWebsiteError
from app.exceptions.WebsiteNotFoundError import WebsiteNotFoundError
from . import views


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # register views
    app.register_blueprint(views.bp)
    
    # provide JSON responses for custom exceptions
    @app.errorhandler(HTTPException)
    def handle_error(e):
        if e is UnreadableWebsiteError or e is WebsiteNotFoundError:
            return make_response(jsonify(e.description), e.code)

        return e

    return app