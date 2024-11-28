from sqlalchemy import text

from config import db, SCHEMA_NAME
from entities.source import Source


class SourceRepository:

    @staticmethod
    def get():
        sql = f"""
            SELECT
                source_id,
                bibtex_key,
                title,
                year,
                author

            FROM {SCHEMA_NAME}.source
        """
        result = db.session.execute(text(sql))
        books = result.fetchall()

        # NOTE: Varmista että SELECT queryn palattamat kentät ovat samat kuin olion konstruktorin,
        #  muutoin laita kentät manuaalisesti tyyliin SourceBook(book[0], book[1], jne...)

        # * -operaattori "avaa" listan, esim ["a", "b", "c"] --> "a", "b", "c"
        return [Source(*book) for book in books]

    @staticmethod
    def delete(source_id):
        sql = f"""
            DELETE FROM
            {SCHEMA_NAME}.source
            WHERE source_id = :source_id
        """
        db.session.execute(text(sql), {"source_id": source_id})
        db.session.commit()

    @staticmethod
    def download():
        sql = f"""
            SELECT
                bibtex_key,
                title,
                year,
                author
            
            FROM {SCHEMA_NAME}.source
            """
        result = db.session.execute(text(sql))
        books = result.fetchall()
        bibtex = ""
        for book in books:
            bibtex += f'@article {{{book[0]}}},\n'
            bibtex += f'title = "{book[1]}",\n'
            bibtex += f'year = "{book[2]}",\n'
            bibtex += f'author = "{book[3]}"\n\n'

        return bibtex
