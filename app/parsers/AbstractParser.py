from io import TextIOWrapper
from typing import Any
from abc import ABC, abstractmethod

class AbstractParser(ABC):
    """
    Abstract Parser class.

    Attributes
    ----------
    data : str
        Input data.
    """

    def __init__(self, data = None) -> None:
        if data:
            self.load(data)

    def load(self, data: str) -> None:
        """Load the data to parse."""
        self.data = data

    @abstractmethod
    def extract(self) -> Any:
        """Get the parsed data."""
        pass

    def save(self, file: TextIOWrapper):
        """Parse the data into a file."""
        file.write(self.extract())