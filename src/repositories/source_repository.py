from config import db, schema_name
from sqlalchemy import text

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

            FROM {schema_name}.source
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
            {schema_name}.source
            WHERE source_id = :source_id
        """
        db.session.execute(text(sql), {"source_id": source_id})
        db.session.commit()

    @staticmethod
    def download(source_id):
        sql = f"""
            SELECT
                bibtex_key,
                title,
                year,
                author
            
            FROM {schema_name}.source
            WHERE source_id = :source_id
            """
        result = db.session.execute(text(sql), {"source_id": source_id})
        book = result.fetchone()

        BibTeX = f'@article {{{book[0]}}},\ntitle = "{book[1]}",\nyear = "{book[2]}",\nauthor = "{book[3]}"'

        return BibTeX
