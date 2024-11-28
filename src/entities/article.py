from string import digits

from entities.source import Source
from util import UserInputError


class Article(Source): # pylint: disable=too-few-public-methods
    def __init__( #pylint: disable=too-many-arguments,too-many-positional-arguments
        self,
        source_id,
        bibtex_key,
        title,
        year,
        author,
        source_article_id,
        journal,
        volume,
        number,
        pages,
        month,
    ):
        super().__init__(source_id, bibtex_key, title, year, author)
        self.source_article_id = source_article_id
        self.journal = journal
        self.volume = volume
        self.number = number
        self.pages = pages
        self.month = month

    def validate(self):
        super().validate()

        if len(self.journal) == 0:
            raise UserInputError("Julkaisu vaaditaan")

        if len(self.volume) > 0 and not set(self.volume).issubset(set(digits)):
            raise UserInputError("Kentän nide on oltava numero")

        if len(self.number) > 0 and not set(self.number).issubset(set(digits)):
            raise UserInputError("Kentän numero on oltava numero")
