import unittest
from entities.source import Source


class TestDownload(unittest.TestCase):

    def test_lataa_yksi_lähde(self):

        sources = (
            {
                "source_id": 1,
                "bibtex_key": "bibtex_key_1",
                "title": "bibtex_title_1",
                "year": "2020",
                "author": "bibtex_author_1",
            },
            {
                "source_id": 2,
                "bibtex_key": "bibtex_key_2",
                "title": "bibtex_title_2",
                "year": "2021",
                "author": "bibtex_author_2",
            },
        )

        books = []
        for item in sources:
            books.append(Source(item))

        bibtex = books[0].download()
        test = '@article {bibtex_key_1,\ntitle = "bibtex_title_1",\nyear = "2020",\nauthor = "bibtex_author_1"}\n\n'
        assert bibtex == test

    def test_lataa_kaksi_lähdettä(self):

        sources = (
            {
                "source_id": 1,
                "bibtex_key": "bibtex_key_1",
                "title": "bibtex_title_1",
                "year": "2020",
                "author": "bibtex_author_1",
            },
            {
                "source_id": 2,
                "bibtex_key": "bibtex_key_2",
                "title": "bibtex_title_2",
                "year": "2021",
                "author": "bibtex_author_2",
            },
        )

        books = []
        for item in sources:
            books.append(Source(item))
        bibtex = ""
        for i in books:
            bibtex += i.download()

        test = '@article {bibtex_key_1,\ntitle = "bibtex_title_1",\nyear = "2020",\nauthor = "bibtex_author_1"}\n\n@article {bibtex_key_2,\ntitle = "bibtex_title_2",\nyear = "2021",\nauthor = "bibtex_author_2"}\n\n'
        assert bibtex == test

