from app.parsers.AbstractParser import AbstractParser

class HTMLParser(AbstractParser):
    """
    HTML to prose parser.
    """

    def extract(self) -> str:
        return NotImplementedError