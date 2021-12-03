import os, re
import pytest
from pathlib import Path
from app.parsers.HTMLParser import HTMLParser

# Declare test data
FIXTURE_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'data'
)

ALL_WEBSITES = pytest.mark.datafiles(
    os.path.join(FIXTURE_DIR, 'webpage1.html'),
    os.path.join(FIXTURE_DIR, 'webpage2.html'),
    os.path.join(FIXTURE_DIR, 'webpage3.html'),
)


# Declare tests
HTML_REGEX = r"<\/?[\w\s]*>|<.+[\W]>"

class TestHTMLParser:

    @ALL_WEBSITES
    def test_extract(self, datafiles):
        for file in datafiles.listdir():

            # arrange
            html = Path(file).read_text('UTF-8')

            # act
            text = HTMLParser(html).extract()

            # assert
            assert isinstance(text, str)

            assert re.search(HTML_REGEX, text) is None

    @ALL_WEBSITES
    def test_save(self, datafiles, tmpdir):
        for file in datafiles.listdir():

            # arrange
            html = Path(file).read_text('UTF-8')
            parser = HTMLParser(html)
            output = parser.extract()
            dest = os.path.join(tmpdir, os.path.basename(file))

            # act
            with open(dest, 'w', encoding='UTF-8') as buffer:
                parser.save(buffer)

            # assert
            assert os.path.exists(dest)

            assert open(dest, 'r', encoding='UTF-8').read() == output
