from entities.source import Source


class SourceBook(Source):
    def __init__(
        self, source_id, bibtex_key, title, year, source_book_id, author, publisher
    ):
        super().__init__(source_id, bibtex_key, title, year)
        self.source_book_id = source_book_id
        self.author = author
        self.publisher = publisher
