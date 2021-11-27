from flask.helpers import make_response
from flask.json import jsonify
import requests
import tempfile

from flask import Blueprint, request
from flask.templating import render_template
from werkzeug.exceptions import HTTPException
from werkzeug.utils import send_file
from app.exceptions.UnreadableWebsiteError import UnreadableWebsiteError
from app.exceptions.WebsiteNotFoundError import WebsiteNotFoundError
from app.parsers.HTMLParser import HTMLParser
from app.parsers.TTSParser import TTSParser

bp = Blueprint("views", __name__, url_prefix="/")

@bp.route("/")
def home():
    return render_template("home.html")

@bp.route("/read", methods=['POST'])
def read():
    # Receive the text
    if 'text' in request.form:
        text = request.form['text']

    elif 'url' in request.form:
        text = get_website_text(request.form['url'])

    # Retrieve the speech
    with tempfile.TemporaryDirectory() as td:
        filename = f"{td}/voz.mp3"
        TTSParser(text).save(filename)

        with open(filename, 'r') as speech:
            return send_file(speech, as_attachment=True)


def get_website_text(url):
    """
    Get readable text from a website.
    """
    try:
        html = requests.get(url).text
    except Exception:
        raise WebsiteNotFoundError

    try:
        return HTMLParser(html).extract()
    except Exception:
        raise UnreadableWebsiteError