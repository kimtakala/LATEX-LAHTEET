import json


class FormField:
    def __init__(self, name, name_friendly, required=False, input_type="text"):
        self.name = name
        self.name_friendly = name_friendly
        self.required = required
        self.input_type = input_type


fields = {
    "common": [
        FormField("bibtex_key", "Avain", True),
        FormField("title", "Otsikko", True),
        FormField("year", "Julkaisuvuosi", True),
    ],
    "book": [
        FormField("author", "Kirjoittaja", True),
        FormField("publisher", "Julkaisija", True),
    ],
    "article": [
        FormField("author", "Kirjoittaja", True),
        FormField("journal", "Julkaisu", True),
        FormField("volume", "Nide"),
        FormField("number", "Numero"),
        FormField("pages", "Sivumäärä"),
        FormField("month", "Kuukausi"),
    ],
}


def get_fields_json():
    serializeable = {k: [f.__dict__ for f in fields[k]] for k in fields}
    return json.dumps(serializeable)
