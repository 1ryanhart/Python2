"""Define IngestorInterface class."""
from abc import ABC, abstractmethod


class IngestorInterface(ABC):
    """
    Define abstract base class.
    
    Other specific child Ingestors to inherit this class.
    """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """Test if the path extension is in the allowed_extensions list.

        For example, for the PDFIngestor child, the
        allowed extensions_list is ['pdf']. Hence, if the
        file path ends in '.pdf' then the method will
        return True. Otherwise will return False

        :param path: the file path to be tested.
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str):
        """Define placeholder function to parse the file."""
        pass
