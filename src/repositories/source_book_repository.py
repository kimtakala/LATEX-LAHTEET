from config import db, schema_name
from sqlalchemy import text

from entities.source_book import SourceBook


def get_books():
    sql = f"""
        SELECT
            s.source_id,
            s.bibtex_key,
            s.title,
            s.year,
            s.author,
            sb.source_book_id,
            sb.publisher

        FROM {schema_name}.source_book sb

        LEFT JOIN {schema_name}.source s
        ON s.source_id = sb.source_id
    """
    result = db.session.execute(text(sql))
    books = result.fetchall()

    # NOTE: Varmista että SELECT queryn palattamat kentät ovat samat kuin olion konstruktorin,
    #  muutoin laita kentät manuaalisesti tyyliin SourceBook(book[0], book[1], jne...)

    # * -operaattori "avaa" listan, esim ["a", "b", "c"] --> "a", "b", "c"
    return [SourceBook(*book) for book in books]


def create_book(book: SourceBook):
    book.validate()

    # Tapa lisätä useihin tauluihin siten, että pääsemme kätevästi
    #  käsiksi edellisen lisäyksen ID:hen
    sql = f"""
        WITH q AS (
            INSERT INTO {schema_name}.source
            (title, year, bibtex_key, kind, author) 
            VALUES
            (:title, :year, :bibtex_key, 'book', :author)
            RETURNING source_id
        )
        INSERT INTO {schema_name}.source_book
            (source_id, publisher)
            VALUES
            ((SELECT source_id FROM q), :publisher)

    """
    db.session.execute(
        text(sql),
        {
            "bibtex_key": book.bibtex_key,
            "title": book.title,
            "year": book.year,
            "publisher": book.publisher,
            "author": book.author,
        },
    )
    db.session.commit()


def delete_book(source_id):
    sql = f"""
        DELETE FROM
        {schema_name}.source
        WHERE source_id = :source_id
    """
    db.session.execute(text(sql), {"source_id": source_id})
    db.session.commit()


def reset_db():
    sql = f"""
    TRUNCATE TABLE {schema_name}.source_book, {schema_name}.source;
    """
    db.session.execute(text(sql))
    db.session.commit()
