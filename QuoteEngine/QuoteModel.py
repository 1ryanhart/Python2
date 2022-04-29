class QuoteModel():
    """A quote object"""

    def __init__(self, body: str, author: str):
        """Construct a new QuoteModel from a body value and an author value.

        :param body: The quote's body
        :param author: The quote's author
        """
        self.body = body
        self.author = author
    
    def __repr__(self) -> str:
        return f'{self.body} - {self.author}'