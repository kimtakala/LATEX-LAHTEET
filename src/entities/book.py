from entities.source import Source
from util import UserInputError


class Book(Source):
    def __init__(self, data: dict):
        super().__init__(data)
        self.source_book_id = data["source_book_id"]
        self.publisher = data["publisher"]

    def validate(self):
        super().validate()

        if len(self.publisher) == 0:
            raise UserInputError("Julkaisija vaaditaan")
