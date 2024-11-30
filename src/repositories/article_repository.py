from typing import Optional

from config import SCHEMA_NAME
from entities.article import Article
from util import try_parse_int


class ArticleRepository:

    def __init__(self, database_service) -> None:
        self.database_service = database_service

    def get(self, source_id: Optional[int] = None) -> list[Article]:
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
                sa.month

            FROM {SCHEMA_NAME}.source_article sa

            LEFT JOIN {SCHEMA_NAME}.source s
            ON s.source_id = sa.source_id

            {f"WHERE s.source_id = '{source_id}'" if source_id else ""}
        """
        rows = self.database_service.fetch(sql)

        # NOTE: Varmista että SELECT queryn palattamat kentät ovat samat kuin olion konstruktorin,
        #  muutoin laita kentät manuaalisesti tyyliin SourceBook(book[0], book[1], jne...)
        return [Article(row) for row in rows]

    def create(self, article):
        article.validate()

        # Tapa lisätä useihin tauluihin siten, että pääsemme kätevästi
        #  käsiksi edellisen lisäyksen ID:hen
        sql = f"""
            WITH q AS (
                INSERT INTO {SCHEMA_NAME}.source
                (title, year, bibtex_key, kind, author) 
                VALUES
                (:title, :year, :bibtex_key, 'article', :author)
                RETURNING source_id
            )
            INSERT INTO {SCHEMA_NAME}.source_article
                (source_id, journal, volume, number, pages, month)
                VALUES
                ((SELECT source_id FROM q), :journal, :volume, :number, :pages, :month)

        """

        self.database_service.execute(
            sql,
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
