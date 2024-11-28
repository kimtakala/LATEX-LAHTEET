from sqlalchemy import text
from config import SCHEMA_NAME, db


def source_exists(bibtex_key):
    query = f"SELECT 1 FROM {SCHEMA_NAME}.source WHERE bibtex_key = :bibtex_key"
    result = db.session.execute(text(query), {"bibtex_key": bibtex_key})
    return bool(result.fetchone())


def truncate_db():
    sql = f"""
    TRUNCATE TABLE {SCHEMA_NAME}.source CASCADE;
    """
    db.session.execute(text(sql))
    db.session.commit()
