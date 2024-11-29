import unittest
from entities.source import Source
from util import UserInputError

class TestSource(unittest.TestCase):

    def setUp(self):
        data = {
        "source_id"     : 1,
        "bibtex_key"    : "key",
        "title"         : "title",
        "year"          : 2024,
        "author"        : "author"
        }
        self.source = Source(data)
        return super().setUp()
    
    def test_no_key(self):
        self.source.bibtex_key = []
        with self.assertRaises(UserInputError):
            self.source.validate()
    
    def test_wrong_stuff(self):
        self.source.bibtex_key = "\\"
        with self.assertRaises(UserInputError):
            self.source.validate()
    
    def test_no_title(self):
        self.source.title = []
        with self.assertRaises(UserInputError):
            self.source.validate()
    
    def test_no_year(self):
        self.source.year = []
        with self.assertRaises(UserInputError):
            self.source.validate()

    def test_no_author(self):
        self.source.author = []
        with self.assertRaises(UserInputError):
            self.source.validate()

    def test_year_not_num(self):
        self.source.year = "UUSI VUOSI"
        with self.assertRaises(UserInputError):
            self.source.validate()