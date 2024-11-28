from string import digits

from entities.source import Source
from util import UserInputError


class Article(Source): # pylint: disable=too-few-public-methods
    def __init__(self, data: dict):
        super().__init__(data)
        self.source_article_id = data["source_article_id"]
        self.journal = data["journal"]
        self.volume = data["volume"]
        self.number = data["number"]
        self.pages = data["pages"]
        self.month = data["month"]

    def validate(self):
        super().validate()

        if len(self.journal) == 0:
            raise UserInputError("Julkaisu vaaditaan")

        if len(self.volume) > 0 and not set(self.volume).issubset(set(digits)):
            raise UserInputError("Kentän nide on oltava numero")

        if len(self.number) > 0 and not set(self.number).issubset(set(digits)):
            raise UserInputError("Kentän numero on oltava numero")
