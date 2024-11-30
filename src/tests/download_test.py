import unittest
from bibtex_convert import to_bibtex
from entities.inproceedings import Inproceedings
from entities.article import Article
from entities.book import Book


class TestDownload(unittest.TestCase):
    def test_lataa_useampi_lähde(self):
        sources = [
            Book(
                {
                    "source_id": 0,
                    "bibtex_key": "avain",
                    "title": "otsikko",
                    "year": "1234",
                    "author": "tatu",
                    "source_book_id": 0,
                    "publisher": "tatu oy",
                }
            ),
            Article(
                {
                    "source_id": 0,
                    "bibtex_key": "avain",
                    "title": "otsikko",
                    "year": "1234",
                    "author": "tatu",
                    "source_article_id": 0,
                    "journal": "tatu publishing",
                    "volume": "2",
                    "number": "3",
                    "pages": "12-13",
                    "month": "Jan",
                }
            ),
            Inproceedings(
                {
                    "source_id": 0,
                    "bibtex_key": "avain",
                    "title": "otsikko",
                    "year": "1234",
                    "author": "tatu",
                    "source_inproceeding_id": "",
                    "booktitle": "tatun kirja",
                    "editor": "tatu",
                    "series": "sarja",
                    "pages": "12-13",
                    "address": "Osoitekatu 12",
                    "month": "Dec",
                    "organization": "tatu oy",
                    "publisher": "tatu publishing",
                    "volume": "3",
                }
            ),
        ]

        expected_bibtex = """@book{avain,
    title = {otsikko},
    year = {1234},
    author = {tatu},
    publisher = {tatu oy},
}

@article{avain,
    title = {otsikko},
    year = {1234},
    author = {tatu},
    journal = {tatu publishing},
    volume = {2},
    number = {3},
    pages = {12-13},
    month = {Jan},
}

@inproceedings{avain,
    title = {otsikko},
    year = {1234},
    author = {tatu},
    booktitle = {tatun kirja},
    editor = {tatu},
    series = {sarja},
    pages = {12-13},
    address = {Osoitekatu 12},
    month = {Dec},
    organization = {tatu oy},
    publisher = {tatu publishing},
    volume = {3},
}"""
        assert to_bibtex(sources) == expected_bibtex
