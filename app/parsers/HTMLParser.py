from app.parsers.AbstractParser import AbstractParser
from bs4 import BeautifulSoup

class HTMLParser(AbstractParser):
    """
    HTML to prose parser.
    """

    def extract(self) -> str:
        soup = BeautifulSoup(self.data, 'html.parser')

        return soup.get_text()