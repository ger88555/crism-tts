import os
import requests
import tempfile

from flask import Blueprint, request
from flask.templating import render_template
from werkzeug.utils import send_file
from app.exceptions.UnreadableWebsiteError import UnreadableWebsiteError
from app.exceptions.WebsiteNotFoundError import WebsiteNotFoundError
from app.parsers.HTMLParser import HTMLParser
from app.parsers.TTSParser import TTSParser

bp = Blueprint("views", __name__, url_prefix="/")

CONVERSIONS_DIRECTORY = os.path.join( os.path.dirname(__file__), 'storage/' )

@bp.route("/")
def home():
    # Receive the text
    if 'text' in request.args:
        text = request.args.get('text').strip("\n\r ")

    elif 'url' in request.args:
        text = get_website_text(request.args.get('url'))

    else:
        text = None

    # Retrieve the speech
    speech = to_file(text) if text is not None else None

    return render_template("home.html", speech=speech)

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

def to_file(text) -> str:
    """
    Generate speech and retrieve the file name.
    """
    with tempfile.NamedTemporaryFile(dir=CONVERSIONS_DIRECTORY, delete=False) as temp:
        TTSParser(text).save(temp)

        return temp.name

@bp.route("/download/<name>", methods=['GET', 'POST'])
def download(name):
    with open(os.path.join(CONVERSIONS_DIRECTORY, name)) as file:
        return send_file(file, as_attachment=request.method == 'POST', download_name="voz.mp3")