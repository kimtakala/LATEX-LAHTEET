from config import db, schema_name
from sqlalchemy import text

from entities.article import Article
from util import try_parse_int


class ArticleRepository:
    @staticmethod
    def get():
        sql = f"""
            SELECT
                s.source_id,
                s.bibtex_key,
                s.title,
                s.year,
                s.author,
                sa.source_article_id,
                sa.journal,
                sa.volume,
                sa.number,
                sa.pages,
                sa.month,

            FROM {schema_name}.source_article sa

            LEFT JOIN {schema_name}.source s
            ON s.source_id = sb.source_id
        """
        result = db.session.execute(text(sql))
        books = result.fetchall()

        # NOTE: Varmista että SELECT queryn palattamat kentät ovat samat kuin olion konstruktorin,
        #  muutoin laita kentät manuaalisesti tyyliin SourceBook(book[0], book[1], jne...)

        # * -operaattori "avaa" listan, esim ["a", "b", "c"] --> "a", "b", "c"
        return [Article(*book) for book in books]

    @staticmethod
    def create(article):
        article.validate()

        # Tapa lisätä useihin tauluihin siten, että pääsemme kätevästi
        #  käsiksi edellisen lisäyksen ID:hen
        sql = f"""
            WITH q AS (
                INSERT INTO {schema_name}.source
                (title, year, bibtex_key, kind, author) 
                VALUES
                (:title, :year, :bibtex_key, 'article', :author)
                RETURNING source_id
            )
            INSERT INTO {schema_name}.source_article
                (source_id, journal, volume, number, pages, month)
                VALUES
                ((SELECT source_id FROM q), :journal, :volume, :number, :pages, :month)

        """

        db.session.execute(
            text(sql),
            {
                "bibtex_key": article.bibtex_key,
                "title": article.title,
                "year": article.year,
                "author": article.author,
                "journal": article.journal,
                "volume": try_parse_int(article.volume),
                "number": try_parse_int(article.number),
                "pages": article.pages,
                "month": article.month,
            },
        )
        db.session.commit()
