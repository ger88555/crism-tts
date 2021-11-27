import os

from flask import Flask
from flask.helpers import flash
from flask.templating import render_template
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
    
    # flash error messages from custom exceptions
    @app.errorhandler(HTTPException)
    def handle_error(e):
        if e is UnreadableWebsiteError or e is WebsiteNotFoundError:
            flash(e.description)

            return render_template("home.html")

        return e

    return app