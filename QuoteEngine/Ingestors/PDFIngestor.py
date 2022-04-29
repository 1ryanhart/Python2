import subprocess
import os
import random
from typing import List

from ..IngestorInterface import IngestorInterface
from ..QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parses the .pdf file to extract quotes. Instantiates QuoteModel objects for each quote.
        Returns list of all QuoteModel Objects created from the file.

        This method splits on a ' - '. However the method enables the quotes themselves
        to contain the characters ' - ' 
        
        :param path: the file path to be parsed.
        """

        if not cls.can_ingest(path):
            raise Exception('cannot ingest file')
        
        quotes = []
        tmp = f'./_data/tmp/{random.randint(0,100000)}.txt'
        call = subprocess.call(['pdftotext', '-raw', path, tmp])

        with open(tmp, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip('\n\r')
                if len(line) >0:
                    parts = line.split(' - ')
                    author = parts[-1]
                    body_all = parts[0:len(parts)-1]
                    body = ' '.join(body_all)
                    new_quote = QuoteModel(body, author)
                    quotes.append(new_quote)

        os.remove(tmp)
        return print(f'pdf: {quotes}')

# pdf_path = '../_data/DogQuotes/DogQuotesPDF.pdf'
# PDFImporter.parse(pdf_path)

"""THIS WORKS HOWEVER THE END OF THE FILE HAS A STRANGE CHARACTER AND THIS CREATES AN UNWANTED QUOTE INSTANCE: ♀"""