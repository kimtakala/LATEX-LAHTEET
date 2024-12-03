from db_util import source_exists_by_id
from util import UserInputError


class Tag:
    def __init__(self, data: dict):
        self.source_id = data["source_id"]
        self.name = data["name"]
        self.tag_id = data["tag_id"]

    def validate(self):
        if len(self.name) == 0:
            raise UserInputError("Nimi vaaditaan")

        if not source_exists_by_id(self.source_id):
            raise UserInputError(f"Lähdettä {self.source_id} ei olemassa")
