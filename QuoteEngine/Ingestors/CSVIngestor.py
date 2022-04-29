from typing import List
import pandas

from ..IngestorInterface import IngestorInterface
from ..QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Realises the IngestorInterface abstract base class. Implements specific parse method
    for .csv files
    """

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parses the .csv file to extract quotes. Instantiates QuoteModel objects for each quote.
        Returns list of all QuoteModel Objects created from the file.

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
        except:
            raise Exception('Error parsing file')