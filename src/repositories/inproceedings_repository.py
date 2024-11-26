from config import db, schema_name
from sqlalchemy import text

from entities.inproceedings import Inproceedings
from util import try_parse_int


class InproceedingsRepository:
    @staticmethod
    def get():
        sql = f"""
            SELECT
                s.source_id,
                s.bibtex_key,
                s.title,
                s.year,
                s.author,
                si.source_inproceedings_id,
                si.booktitle,
                si.editor,
                si.series,
                si.pages,
                si.address,
                si.month,
                si.organization,
                si.publisher,
                si.volume

            FROM {schema_name}.source_inproceedings si

            LEFT JOIN {schema_name}.source s
            ON s.source_id = si.source_id
        """
        result = db.session.execute(text(sql))
        rows = result.fetchall()

        # NOTE: Varmista että SELECT queryn palattamat kentät ovat samat kuin olion konstruktorin,
        #  muutoin laita kentät manuaalisesti tyyliin SourceBook(book[0], book[1], jne...)

        # * -operaattori "avaa" listan, esim ["a", "b", "c"] --> "a", "b", "c"
        return [Inproceedings(*row) for row in rows]

    @staticmethod
    def create(inproceedings):
        inproceedings.validate()

        # Tapa lisätä useihin tauluihin siten, että pääsemme kätevästi
        #  käsiksi edellisen lisäyksen ID:hen
        sql = f"""
            WITH q AS (
                INSERT INTO {schema_name}.source
                (title, year, bibtex_key, kind, author) 
                VALUES
                (:title, :year, :bibtex_key, 'inproceedings', :author)
                RETURNING source_id
            )
            INSERT INTO {schema_name}.source_inproceedings
                (source_id, booktitle, editor, series, pages, address, month, organization, publisher, volume)
                VALUES
                ((SELECT source_id FROM q), :booktitle, :editor, :series, :pages, :address, :month, :organization, :publisher, :volume)
        """

        db.session.execute(
            text(sql),
            {
                "bibtex_key": inproceedings.bibtex_key,
                "title": inproceedings.title,
                "year": inproceedings.year,
                "author": inproceedings.author,
                "booktitle": inproceedings.booktitle,
                "editor": inproceedings.editor,
                "series": inproceedings.series,
                "pages": inproceedings.pages,
                "address": inproceedings.address,
                "month": inproceedings.month,
                "organization": inproceedings.organization,
                "publisher": inproceedings.publisher,
                "volume": try_parse_int(inproceedings.volume),
            },
        )
        db.session.commit()
