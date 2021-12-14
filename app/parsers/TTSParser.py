from app.parsers.AbstractParser import AbstractParser
from gtts import gTTS
from io import BytesIO
class TTSParser(AbstractParser):
    """
    Text-to-Speech parser.
    """
        
    def extract(self):
        mp3_fp = BytesIO()
    	tts = gTTS(self.data, lang='es', tld = 'es')
    	tts.write_to_fp(mp3_fp)

        return mp3_fp
