from sqlalchemy import text
from config import schema_name, db


def source_exists(bibtex_key):
    query = f"SELECT 1 FROM {schema_name}.source WHERE bibtex_key = :bibtex_key"
    result = db.session.execute(text(query), {"bibtex_key": bibtex_key})
    return True if result.fetchone() else False


def truncate_db():
    sql = f"""
    TRUNCATE TABLE {schema_name}.source CASCADE;
    """
    db.session.execute(text(sql))
    db.session.commit()
