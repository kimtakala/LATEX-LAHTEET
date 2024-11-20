from config import db, schema_name
from sqlalchemy import text


def get_sources():
    pass


def exists_source(bibtex_key: str):
    query = f"SELECT 1 FROM {schema_name}.source WHERE bibtex_key = :bibtex_key"
    result = db.session.execute(text(query), {"bibtex_key": bibtex_key})
    return True if result.fetchone() else False
