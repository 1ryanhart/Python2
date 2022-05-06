from typing import List

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from .Ingestors.DocxIngestor import DocxIngestor
from .Ingestors.CSVIngestor import CSVIngestor
from .Ingestors.PDFIngestor import PDFIngestor
from .Ingestors.TextIngestor import TextIngestor


class Ingestor(IngestorInterface):
    """Realises the IngestorInterface abstract base class. Used as a
    selector to parse a given file to the correct Ingestor
    (pdf, txt, docx, csv).
    """
    importers = [DocxIngestor, CSVIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Tests to see if the path extension can
        be parsed by any of the parsers.

        :param path: the file path to be tested.
        :return: none if the file cannot be parsed.
        A list of QuoteModel objects if the file can be parsed.
        """
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)
