from config import db, app, schema_name
from sqlalchemy import text
from pathlib import Path


def setup_db():
    # Tyhjennä skeema
    sql = f"""
        DROP SCHEMA IF EXISTS {schema_name} CASCADE;
        CREATE SCHEMA {schema_name};
    """
    db.session.execute(text(sql))

    # Luo uusi skeema tiedoston /src/schema.sql pohjalta
    path = Path(__file__).parent / "schema.sql"
    with path.open() as fp:
        sql = fp.read()
        db.session.execute(text(sql))

    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        setup_db()
