import unittest
from entities.article import Article
from entities.book import Book
from entities.inproceedings import Inproceedings


class TestStringify(unittest.TestCase):
    def test_kirja_muuttuu_oikeaksi_merkkijonoksi(self):
        data = {
            "source_id": 0,
            "bibtex_key": "avain",
            "title": "otsikko",
            "year": "1234",
            "author": "tatu",
            "source_book_id": 0,
            "publisher": "tatu oy",
        }

        expected_bibtex = """@book{avain,
    title = {otsikko},
    year = {1234},
    author = {tatu},
    publisher = {tatu oy},
}"""
        book = Book(data)
        assert expected_bibtex == str(book)

    def test_artikkeli_muuttuu_oikeaksi_merkkijonoksi(self):
        data = {
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

        expected_bibtex = """@article{avain,
    title = {otsikko},
    year = {1234},
    author = {tatu},
    journal = {tatu publishing},
    volume = {2},
    number = {3},
    pages = {12-13},
    month = {Jan},
}"""
        article = Article(data)
        assert expected_bibtex == str(article)

    def test_inproceedings_muuttuu_oikeaksi_merkkijonoksi(self):
        data = {
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

        expected_bibtex = """@inproceedings{avain,
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
        inproceedings = Inproceedings(data)
        assert expected_bibtex == str(inproceedings)
