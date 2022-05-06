"""Define specific pdf ingestor."""
import subprocess
import os
import random
from typing import List

from ..IngestorInterface import IngestorInterface
from ..QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Realise the IngestorInterface abstract base class.

    Implement specific parse method for .pdf files.
    """

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the .pdf file to extract quotes.

        Instantiate QuoteModel objects for each quote.
        Return list of all QuoteModel Objects created from the file.

        This method splits on a ' - '. However the method enables
        the quotes themselves to contain the characters ' - '

        :param path: the file path to be parsed.
        """
        try:
            if not cls.can_ingest(path):
                raise Exception('cannot ingest file')

            quotes = []
            tmp = f'./tmp/{random.randint(0,100000)}.txt'
            call = subprocess.call(['pdftotext', '-raw', path, tmp])

            with open(tmp, 'r', encoding='utf-8-sig') as f:
                lines = f.readlines()
                for line in lines:
                    line = line.strip('\n\r')
                    if len(line) > 0:
                        parts = line.split(' - ')
                        author = parts[-1]
                        body_all = parts[0:len(parts)-1]
                        body = ' '.join(body_all)
                        new_quote = QuoteModel(body, author)
                        quotes.append(new_quote)

            os.remove(tmp)
            return quotes
        except Exception:
            raise Exception('Error parsing file')
