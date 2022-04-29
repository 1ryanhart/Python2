from typing import List

from ..IngestorInterface import IngestorInterface
from ..QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """Realises the IngestorInterface abstract base class. Implements specific parse method
    for .txt files
    """
    
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parses the .txt file to extract quotes. Instantiates QuoteModel objects for each quote.
        Returns list of all QuoteModel Objects created from the file.

        This method splits on a ' - '. However the method enables the quotes themselves
        to contain the characters ' - ' 
        
        :param path: the file path to be parsed.
        """

        if not cls.can_ingest(path):
            raise Exception('cannot ingest file')
        
        quotes = []
        with open(path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if len(line) ==0:
                    pass
                parts = line.split(' - ')
                author = parts[-1]
                body_all = parts[0:len(parts)-1]
                body = ' '.join(body_all)

                new_quote = QuoteModel(body, author)
                quotes.append(new_quote)
        
        return print(f'text: {quotes}')

# txt_path = '../_data/DogQuotes/DogQuotesTXT.txt'
# TXTImporter.parse(txt_path)


"""THIS WORKS HOWEVER THE VERY FIRST QUOTE STARTS WITH THE STRANGE CHARACTERS ï»¿"""