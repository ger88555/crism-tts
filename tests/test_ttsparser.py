import os, re
from pathlib import Path
from app.parsers.TTSParser import TTSParser

# Declare tests

class TestTTSParser:

    def test_extract(self, faker):
        # arrange
        text = faker.text(max_nb_chars=80)

        # act
        audio = TTSParser(text).extract()

        # assert
        assert isinstance(audio, bytes)

        assert len(audio) > 0

    def test_save(self, faker, tmpdir):
        # arrange
        text = faker.text(max_nb_chars=80)
        parser = TTSParser(text)
        output = parser.extract()
        dest = os.path.join(tmpdir, os.path.basename(faker.name()))

        # act
        with open(dest, 'wb') as buffer:
            parser.save(buffer)

        # assert
        assert os.path.exists(dest)

        assert open(dest, 'rb').read() == output
