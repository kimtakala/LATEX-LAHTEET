import re

from db_util import source_exists
from util import UserInputError


class Source: # pylint: disable=too-few-public-methods
    def __init__(self, data: dict):
        self.source_id = data["source_id"]
        self.bibtex_key = data["bibtex_key"]
        self.title = data["title"]
        self.year = data["year"]
        self.author = data["author"]

    def validate(self):
        if len(self.bibtex_key) == 0:
            raise UserInputError("Avain vaaditaan")

        if not re.compile("^[0-9a-zA-Z\\-_:]+$").match(self.bibtex_key):
            raise UserInputError(
                "Avain saa sisältää vain merkkejä 0-9, a-z, A-Z, -, _ ja :"
            )

        if source_exists(self.bibtex_key):
            raise UserInputError(f"Avain {self.bibtex_key} on jo käytössä")

        if len(self.title) == 0:
            raise UserInputError("Otsikko vaaditaan")

        if len(self.author) == 0:
            raise UserInputError("Kirjoittaja vaaditaan")

        if len(self.year) == 0:
            raise UserInputError("Julkaisuvuosi vaaditaan")

        if not re.compile("^[0-9]+$").match(self.year):
            raise UserInputError("Julkaisuvuoden on oltava numero")
