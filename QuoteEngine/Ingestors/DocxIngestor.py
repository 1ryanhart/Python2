from typing import List
import docx

from ..IngestorInterface import IngestorInterface
from ..QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """Realises the IngestorInterface abstract base class. Implements specific parse method
    for .docx files
    """

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parses the .docx file to extract quotes. Instantiates QuoteModel objects 
        for each quote. Returns list of all QuoteModel Objects created from the file.

        This method splits on a ' - '. However, the method enables the quotes themselves
        to contain the characters ' - ' 
        
        :param path: the file path to be parsed.
        """
        try:
            if not cls.can_ingest(path):
                raise Exception('cannot ingest file')
            
            quotes = []
            doc = docx.Document(path)
            for para in doc.paragraphs:
                if para.text != "":
                    parsed = para.text.split(' - ')
                    body_all = parsed[0:len(parsed)-1]
                    body = ' '.join(body_all)
                    author = parsed[-1]

                    new_quote = QuoteModel(body, author)
                    quotes.append(new_quote)

            return quotes
        except:
            raise Exception('Error parsing file')
