import json


class FormField:
    def __init__(self, name, name_friendly, required=False, input_type="text"):
        self.name = name
        self.name_friendly = name_friendly
        self.required = required
        self.input_type = input_type


# Lomake luodaan tämän muuttujan perusteella
# "common" -listan kentät ovat kaikissa viitetyypeissä
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
        FormField("volume", "Nide", False, "number"),
        FormField("number", "Numero", False, "number"),
        FormField("pages", "Sivut"),
        FormField("month", "Kuukausi"),
    ],
    "inproceedings": [
        FormField("author", "Kirjoittaja", True),
        FormField("booktitle", "Kirjan otsikko", True),
        FormField("editor", "Editori"),
        FormField("series", "Sarja"),
        FormField("pages", "Sivut"),
        FormField("address", "Osoite"),
        FormField("month", "Kuukausi"),
        FormField("organization", "Organisaatio"),
        FormField("publisher", "Julkaisija"),
        FormField("volume", "Nide", False, "number"),
    ],
}


def get_fields_json():
    serializeable = {k: [f.__dict__ for f in fields[k]] for k in fields}
    return json.dumps(serializeable)
