from app.parsers.AbstractParser import AbstractParser

class TTSParser(AbstractParser):
    """
    Text-to-Speech parser.
    """
        
    def extract(self):
        raise NotImplementedError