from repositories.source_repository import exists_source
from util import UserInputError
import re


class Source:
    def __init__(self, source_id, bibtex_key, title, year, author):
        self.source_id = source_id
        self.bibtex_key = bibtex_key
        self.title = title
        self.year = year
        self.author = author

    def validate(self):
        if len(self.bibtex_key) == 0:
            raise UserInputError("Avain vaaditaan")

        if not re.compile("^[0-9a-zA-Z\\-_:]+$").match(self.bibtex_key):
            raise UserInputError(
                "Avain saa sisältää vain merkkejä 0-9, a-z, A-Z, -, _ ja :"
            )

        if exists_source(self.bibtex_key):
            raise UserInputError(f"Avain {self.bibtex_key} on jo käytössä")

        if len(self.title) == 0:
            raise UserInputError("Otsikko vaaditaan")

        if len(self.author) == 0:
            raise UserInputError("Kirjoittaja vaaditaan")

        if len(self.year) == 0:
            raise UserInputError("Julkaisuvuosi vaaditaan")
