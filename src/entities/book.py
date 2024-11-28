from entities.source import Source
from util import UserInputError


class Book(Source): #pylint: disable=too-few-public-methods
    def __init__( #pylint: disable=too-many-arguments,too-many-positional-arguments
        self, source_id, bibtex_key, title, year, author, source_book_id, publisher
    ):
        super().__init__(source_id, bibtex_key, title, year, author)
        self.source_book_id = source_book_id
        self.publisher = publisher

    def validate(self):
        super().validate()

        if len(self.publisher) == 0:
            raise UserInputError("Julkaisija vaaditaan")
