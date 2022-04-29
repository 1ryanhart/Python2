from abc import ABC, abstractmethod

class IngestorInterface(ABC):
    """An abstract base class for other specific child Ingestors to inherit from"""
    allowed_extensions =  []

    @classmethod
    def can_ingest(cls, path) -> bool:
        """Tests to see if the path extension is in the allowed_extensions list.
        
        For example, for the PDFIngestor child, the allowed extensions_list is ['pdf']. 
        Hence, if the file path ends in '.pdf' then the method witll return True. Otherwise
        will return False 

        :param path: the file path to be tested.
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str):
        pass



