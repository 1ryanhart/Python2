"""Define specific CSV ingestor."""
from typing import List
import pandas

from ..IngestorInterface import IngestorInterface
from ..QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """
    Realise the IngestorInterface abstract base class.

    Implement specific parse method for .csv files.
    """

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the .csv file to extract quotes.
        
        Instantiate QuoteModel objects for each quote.
        Return list of all QuoteModel Objects created from the file.

        :param path: the file path to be parsed.
        """
        try:
            if not cls.can_ingest(path):
                raise Exception('cannot ingest file')

            quotes = []
            df = pandas.read_csv(path)

            for index, row in df.iterrows():
                quote = QuoteModel(row['body'], row['author'])
                quotes.append(quote)

            return quotes
        except Exception:
            raise Exception('Error parsing file')
