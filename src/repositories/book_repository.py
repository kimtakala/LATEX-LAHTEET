from typing import Optional
from sqlalchemy import text

from config import SCHEMA_NAME
from entities.book import Book


class BookRepository:

    def __init__(self, database_service) -> None:
        self.database_service = database_service

    def get(self, source_id: Optional[int] = None) -> list[Book]:
        sql = f"""
            SELECT
                s.source_id,
                s.bibtex_key,
                s.title,
                s.year,
                s.author,
                sb.source_book_id,
                sb.publisher

            FROM {SCHEMA_NAME}.source_book sb

            LEFT JOIN {SCHEMA_NAME}.source s
            ON s.source_id = sb.source_id

            {f"WHERE s.source_id = '{source_id}'" if source_id else ""}
        """
        rows = self.database_service.fetch(sql)

        return [Book(row) for row in rows]

    def create(self, book):
        book.validate()

        # Tapa lisätä useihin tauluihin siten, että pääsemme kätevästi
        #  käsiksi edellisen lisäyksen ID:hen
        sql = f"""
            WITH q AS (
                INSERT INTO {SCHEMA_NAME}.source
                (title, year, bibtex_key, kind, author) 
                VALUES
                (:title, :year, :bibtex_key, 'book', :author)
                RETURNING source_id
            )
            INSERT INTO {SCHEMA_NAME}.source_book
                (source_id, publisher)
                VALUES
                ((SELECT source_id FROM q), :publisher)

        """
        self.database_service.execute(
            sql,
            {
                "bibtex_key": book.bibtex_key,
                "title": book.title,
                "year": book.year,
                "publisher": book.publisher,
                "author": book.author,
            },
        )
