import os, re
from pathlib import Path
from app.parsers.HTMLParser import HTMLParser

# Declare tests
HTML_REGEX = r"<\/?[\w\s]*>|<.+[\W]>"

class TestHTMLParser:

    def test_extract(self, random_website):
        # arrange
        html = Path(random_website).read_text('UTF-8')

        # act
        text = HTMLParser(html).extract()

        # assert
        assert isinstance(text, str)

        assert re.search(HTML_REGEX, text) is None

    def test_save(self, random_website, tmpdir):
        # arrange
        html = Path(random_website).read_text('UTF-8')
        parser = HTMLParser(html)
        output = parser.extract()
        dest = os.path.join(tmpdir, os.path.basename(random_website))

        # act
        with open(dest, 'w', encoding='UTF-8') as buffer:
            parser.save(buffer)

        # assert
        assert os.path.exists(dest)

        assert open(dest, 'r', encoding='UTF-8').read() == output
