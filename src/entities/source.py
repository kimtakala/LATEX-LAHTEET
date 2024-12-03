import re

from db_util import source_exists_by_key
from util import UserInputError


class Source:
    def __init__(self, data: dict):
        self.source_id = data["source_id"]
        self.bibtex_key = data["bibtex_key"]
        self.title = data["title"]
        self.year = data["year"]
        self.author = data["author"]

        self.tags = []
        if "tags" in data and data["tags"]:
            self.tags = data["tags"].split(",")

        self.kind = "misc"
        self.stringify_ignore_fields = [
            "kind",
            "stringify_ignore_fields",
            "bibtex_key",
            "tags",
        ]

    def validate(self):
        if len(self.bibtex_key) == 0:
            raise UserInputError("Avain vaaditaan")

        if not re.compile("^[0-9a-zA-Z\\-_:]+$").match(self.bibtex_key):
            raise UserInputError(
                "Avain saa sisältää vain merkkejä 0-9, a-z, A-Z, -, _ ja :"
            )

        if len(self.title) == 0:
            raise UserInputError("Otsikko vaaditaan")

        if len(self.author) == 0:
            raise UserInputError("Kirjoittaja vaaditaan")

        if len(self.year) == 0:
            raise UserInputError("Julkaisuvuosi vaaditaan")

        if not re.compile("^[0-9]+$").match(self.year):
            raise UserInputError("Julkaisuvuoden on oltava numero")

        # siirretty samanlaisten avainten tarkistuksen viimeiseksi että testit toimii :D
        if source_exists_by_key(self.bibtex_key):
            raise UserInputError(f"Avain {self.bibtex_key} on jo käytössä")

    # str(objekti) muuntaa sen bibtex-muotoon
    def __str__(self) -> str:
        fields = self.__dict__
        fields_bibtex = ""

        for field, value in fields.items():
            if field in self.stringify_ignore_fields:
                continue

            if field.endswith("_id"):
                continue

            if len(str(value)) == 0:
                continue

            value = "{" + str(value) + "}"
            fields_bibtex += f"    {field} = {value},\n"

        return f"@{self.kind}" + "{" + f"{self.bibtex_key},\n{fields_bibtex}" + "}"
