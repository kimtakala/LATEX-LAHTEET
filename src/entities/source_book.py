from entities.source import Source
from util import UserInputError


class SourceBook(Source):
    def __init__(
        self, source_id, bibtex_key, title, year, author, source_book_id, publisher
    ):
        super().__init__(source_id, bibtex_key, title, year, author)
        self.source_book_id = source_book_id
        self.publisher = publisher

    def validate(self):
        super().validate()

        if len(self.publisher) == 0:
            raise UserInputError("Julkaisija vaaditaan")
